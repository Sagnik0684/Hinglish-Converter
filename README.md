# Hinglish Converter 💬🇮🇳

This is a simple Streamlit app that lets you:
- Upload a Hindi/Bengali PDF or image
- Extract the text using OCR
- Convert that text to Hinglish (or Bengalish?)
- Download the result as .txt or .pdf

✨ No data is stored. Everything happens in-session.

## Project Structure
hinglish-converter/
├── streamlit_app.py          ← Main app
├── requirements.txt
├── utils/
│   ├── ocr_utils.py
│   ├── transliterate_utils.py
│   └── file_utils.py
├── output/
├── sample_docs/
└── README.md

## Setup

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py