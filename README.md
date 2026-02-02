# 🏛️ NyayaSahayak (Justice Helper)

**Bridging the gap between complex governance documents and the common citizen — in text and voice, across Indian languages.**

NyayaSahayak is an AI-powered Governance Assistant designed to simplify official government documents, schemes, and legal acts for Indian citizens. Users can upload complex PDFs (UGC Guidelines, Gazettes, Legal Acts, Policies, etc.) and receive clear, contextual answers—now with multilingual support and voice playback.

---

## 🚀 The Problem
Government and legal documents are often:
* **Lengthy and dense:** Overwhelming for the average reader.
* **Bureaucratic:** Written in complex "legalese" that is hard to decipher.
* **Language Barriers:** Frequently inaccessible to non-English speakers.

**The Impact:** Low awareness of rights, misinterpretation of policy (like internship or education rules), and reduced civic trust.

## 💡 The Solution
NyayaSahayak leverages the massive context window of **Google Gemini (1.5 Flash / Pro)** to ingest entire official documents at once.

**What makes it different:**
* **Full-document understanding:** No "chunking" or losing nuances—the AI sees the whole picture.
* **Document-grounded:** Responses are strictly tied to the uploaded PDFs to prevent hallucinations.
* **Multilingual & Auditory:** Translates complex clauses into regional languages and speaks them aloud.

---

## 🎥 Working Demo
[**Click here to watch the demo video**](demo.mp4)  

---

## 🌐 Key Features

### 📄 Document Intelligence
* Upload one or multiple official PDFs.
* Handles large-scale documents (50+ pages) with ease.
* **RAG-Free Architecture:** Entire documents are passed as context for maximum accuracy.

### 🗣️ Multilingual Support
Choose your output language for automated translation and explanation:
* **English** | **Hindi (हिंदी)** | **Hinglish** | **Tamil (தமிழ்)** | **Telugu (తెలుగు)** | **Marathi (मराठी)**

### 🔊 Voice Output (TTS)
AI responses are converted to speech using **gTTS**, specifically designed for:
* Visually impaired users.
* Low-literacy accessibility.
* Rural/Mobile-first usage.

### 🛡️ Safety & Accuracy
* **Zero Hallucination:** Answers are restricted to the uploaded text.
* **Privacy-First:** Documents are processed in-memory and are not stored.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | Streamlit (Python) |
| **AI Engine** | Google Gemini Pro / 1.5 Flash |
| **PDF Processing** | PyPDF2 |
| **Voice Engine** | gTTS (Google Text-to-Speech) |
| **Architecture** | Direct Context Injection |

---

## ⚙️ Installation & Setup

### Prerequisites
* Python 3.10+
* [Google Gemini API Key](https://aistudio.google.com/)

### Steps

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/your-username/nyaya-sahayak.git](https://github.com/your-username/nyaya-sahayak.git)
   cd nyaya-sahayak
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    streamlit run app.py
    ```

4.  **Usage**
    - Enter your Google API Key in the sidebar.
    - Select your preferred Model (Auto-detected).
    - Upload a PDF (e.g., "UGC_New_Guidelines.pdf").
    - Ask questions like: *"What are the new internship rules?"*

---

## 📸 Features
-   **Auto-Model Detection:** Automatically detects available Gemini models for your API key.
-   **Full Document Context:** Analyzes 50+ page documents in seconds.
-   **Secure Processing:** Documents are processed in memory and not stored permanently.
-   **Hallucination Control:** Strict prompts ensure the AI only answers from the provided document.
`   **Audio Output** User can hear the soltuions to their problems in their native language.
---

## 🔮 Future Roadmap
-   **Voice Input:** Speech-to-text for a fully hands-free experience..
-   **Adding more languages:** Adding Bengali, Kannada, Malayalam, etc..
-   **Citations:** Highlighting specific clauses/pages for every answer.

---

**Built for the AI for Governance Hackathon.**
