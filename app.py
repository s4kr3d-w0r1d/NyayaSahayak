import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from gtts import gTTS
import os

# --- Page Config ---
st.set_page_config(page_title="NyayaSahayak: Governance AI", layout="wide", page_icon="🏛️")

# --- Custom Styling ---
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #FF9933; font-weight: bold;}
    .sub-text {font-size: 1.1rem; color: #333;}
    .stChatInput {border-radius: 20px;}
    .stAudio {width: 100%;}
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

# --- Helper Function for Voice ---
def text_to_speech(text, lang_code):
    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)
        filename = "response.mp3"
        tts.save(filename)
        return filename
    except Exception as e:
        return None

# --- Sidebar ---
with st.sidebar:
    st.title("🏛️ NyayaSahayak")
    st.info("Governance Assistant for All Citizens")
    
    st.divider()
    
    # 1. API Key
    api_key = st.text_input("Enter Google Gemini API Key:", type="password")
    
    # 2. Language Selector (The New Feature)
    st.subheader("🗣️ Language / भाषा")
    language = st.selectbox(
        "Select Output Language:",
        ["English", "Hindi (हिंदी)", "Hinglish", "Tamil (தமிழ்)", "Telugu (తెలుగు)", "Marathi (मराठी)"]
    )
    
    # Map selection to Gemini prompt & gTTS code
    lang_map = {
        "English": "en",
        "Hindi (हिंदी)": "hi",
        "Hinglish": "en", # gTTS doesn't support Hinglish, fallback to English accent
        "Tamil (தமிழ்)": "ta",
        "Telugu (తెలుగు)": "te",
        "Marathi (मराठी)": "mr"
    }
    
    # 3. Model Selector
    selected_model = None
    if api_key:
        try:
            genai.configure(api_key=api_key)
            available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            if available_models:
                # Prefer Flash or Pro
                default_index = 0
                for i, m in enumerate(available_models):
                    if "flash" in m:
                        default_index = i
                        break
                selected_model = st.selectbox("Select AI Model:", available_models, index=default_index)
        except:
            pass

    st.divider()
    
    uploaded_files = st.file_uploader("📂 Upload Official PDFs", type="pdf", accept_multiple_files=True)

    if st.button("🚀 Analyze Document"):
        if uploaded_files and api_key:
            with st.spinner("Reading document..."):
                raw_text = ""
                for uploaded_file in uploaded_files:
                    pdf_reader = PdfReader(uploaded_file)
                    for page in pdf_reader.pages:
                        text = page.extract_text()
                        if text:
                            raw_text += text + "\n"
                if raw_text:
                    st.session_state.pdf_text = raw_text
                    st.success("✅ Document Loaded!")

# --- Main Interface ---
st.markdown('<div class="main-header">🇮🇳 NyayaSahayak</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Simplifying Governance with Voice & Multilingual Support.</div>', unsafe_allow_html=True)
st.divider()

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # If it's an assistant message, show the audio player if it exists
        if message.get("audio"):
            st.audio(message["audio"])

# User Input
if human_input := st.chat_input("Ask a question..."):
    if not st.session_state.pdf_text:
        st.warning("⚠️ Please upload a document first.")
    elif not api_key:
        st.warning("⚠️ Please enter your API Key.")
    else:
        # User Message
        st.session_state.messages.append({"role": "user", "content": human_input})
        with st.chat_message("user"):
            st.markdown(human_input)

        # AI Response
        try:
            model = genai.GenerativeModel(selected_model)
            
            # Smart Prompt Engineering for Language
            prompt = f"""
            You are NyayaSahayak. Answer based on the document provided.
            
            IMPORTANT: Answer in {language} language.
            Keep the answer simple and conversational.
            
            Document Context:
            {st.session_state.pdf_text[:50000]} 
            
            Question: {human_input}
            """
            
            with st.spinner(f"Thinking in {language}..."):
                response = model.generate_content(prompt)
                ai_text = response.text
                
                # Generate Audio (Voice Feature)
                audio_file = None
                target_lang = lang_map.get(language, 'en')
                
                # Only generate audio for shorter responses to save time/space
                audio_file = text_to_speech(ai_text[:500], target_lang) # Speak first 500 chars
                
                # Save to history
                message_data = {"role": "assistant", "content": ai_text}
                if audio_file:
                    message_data["audio"] = audio_file
                
                st.session_state.messages.append(message_data)
                
                # Display Immediately
                with st.chat_message("assistant"):
                    st.markdown(ai_text)
                    if audio_file:
                        st.audio(audio_file)
                
        except Exception as e:
            st.error(f"Error: {e}")
