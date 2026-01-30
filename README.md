# 🏛️ NyayaSahayak (Justice Helper)

**Bridging the gap between Complex Policy and the Common Citizen.**

NyayaSahayak is an AI-powered Governance Assistant designed to simplify official government documents, schemes, and legal acts for the average Indian citizen. It allows users to upload complex PDF documents (like UGC Guidelines, Gazettes, or Legal Acts) and receive instant, simplified explanations in plain English.

---

## 🚀 The Problem
Government documents are often lengthy, filled with legal jargon, and difficult for non-experts to navigate. This creates a barrier between the administration and the people, leading to:
- Lack of awareness about eligible schemes.
- Misinterpretation of new rules (e.g., UGC guidelines).
- Decreased civic participation.

## 💡 The Solution
**NyayaSahayak** leverages the massive context window of **Google Gemini 1.5** to ingest entire legal documents without information loss. Unlike traditional search methods that chop documents into pieces, NyayaSahayak reads the *entire* context to provide answers that are:
1.  **Accurate:** No missing context.
2.  **Transparent:** Explains rules based *only* on the uploaded file.
3.  **Accessible:** Instant summaries and Q&A.

---

## 🎥 Working Demo
**See NyayaSahayak in action:**

👉 **[Click here to watch the demo video (demo.mp4)](demo.mp4)**

*(Note: Please ensure the file `demo.mp4` is present in the repository to view)*

---

## 🛠️ Tech Stack
-   **Frontend:** Streamlit (Python)
-   **AI Engine:** Google Gemini Pro / 1.5 Flash (via `google-generativeai`)
-   **Processing:** PyPDF2 (Text Extraction)
-   **Architecture:** Direct Context Injection (RAG-Free) for maximum accuracy on government texts.

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10 or higher
- A Free Google Gemini API Key

### Steps
1.  **Clone the Repository**
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

---

## 🔮 Future Roadmap
-   **Voice Interface:** For rural users to ask questions verbally.
-   **Multilingual Support:** Translating answers into Hindi, Tamil, and Bengali.
-   **WhatsApp Integration:** Delivering scheme details via simple chat messages.

---

**Built for the AI for Governance Hackathon.**
