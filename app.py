import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# --- Page Config ---
st.set_page_config(page_title="NyayaSahayak: Governance AI", layout="wide", page_icon="🏛️")

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

# --- Sidebar ---
with st.sidebar:
    st.title("🏛️ NyayaSahayak")
    st.info("Governance Assistant")
    
    st.divider()
    
    # 1. API Key Input
    api_key = st.text_input("Enter Google Gemini API Key:", type="password")
    
    # 2. Model Selector (The Fix for 404 Errors)
    selected_model = None
    if api_key:
        try:
            genai.configure(api_key=api_key)
            # Ask Google which models are available for this key
            available_models = []
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    available_models.append(m.name)
            
            if available_models:
                # Default to a Flash model if available (it's faster), otherwise first option
                default_index = 0
                for i, m in enumerate(available_models):
                    if "flash" in m:
                        default_index = i
                        break
                
                selected_model = st.selectbox("Select AI Model:", available_models, index=default_index)
            else:
                st.error("Key valid, but no chat models found. Check Google AI Studio permissions.")
        except Exception as e:
            st.error(f"API Key Error: {e}")

    st.divider()
    
    # 3. File Upload
    uploaded_files = st.file_uploader("📂 Upload Official PDFs", type="pdf", accept_multiple_files=True)

    if st.button("🚀 Analyze Document"):
        if uploaded_files and api_key:
            with st.spinner("Reading document..."):
                try:
                    raw_text = ""
                    for uploaded_file in uploaded_files:
                        pdf_reader = PdfReader(uploaded_file)
                        for page in pdf_reader.pages:
                            text = page.extract_text()
                            if text:
                                raw_text += text + "\n"
                    
                    if raw_text:
                        st.session_state.pdf_text = raw_text
                        st.success("✅ Document Loaded! Ready for questions.")
                    else:
                        st.error("Could not extract text. Is this a scanned PDF?")
                        
                except Exception as e:
                    st.error(f"Error reading PDF: {e}")

# --- Main Interface ---
st.header("🇮🇳 NyayaSahayak (Justice Helper)")
st.caption("Instant analysis of UGC Rules, Government Schemes & Acts.")
st.divider()

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if human_input := st.chat_input("Ask about the document (e.g., 'Explain UGC new rules')..."):
    if not st.session_state.pdf_text:
        st.warning("⚠️ Please upload a document first.")
    elif not api_key:
        st.warning("⚠️ Please enter your API Key.")
    elif not selected_model:
        st.warning("⚠️ Please select a model from the sidebar.")
    else:
        # Show user message
        st.session_state.messages.append({"role": "user", "content": human_input})
        with st.chat_message("user"):
            st.markdown(human_input)

        # AI Response
        try:
            # Use the model selected from the dropdown
            model = genai.GenerativeModel(selected_model)
            
            prompt = f"""
            You are NyayaSahayak. Answer strictly based on the provided document text.
            
            Document Context:
            {st.session_state.pdf_text[:50000]} 
            
            Question: {human_input}
            """
            
            with st.spinner(f"Consulting {selected_model}..."):
                response = model.generate_content(prompt)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                with st.chat_message("assistant"):
                    st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Error: {e}")