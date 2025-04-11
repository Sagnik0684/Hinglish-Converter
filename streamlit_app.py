import streamlit as st
import os
import tempfile
import magic  # 🧙 Install with: pip install python-magic-bin

from utils.ocr_utils import process_pdf_for_ocr, process_image_for_ocr
from utils.transliterate_utils import transliterate_text

st.set_page_config(page_title="Hinglish Converter", layout="centered")

st.title("📄 Hinglish Converter")
st.subheader("Convert Hindi/Bengali PDFs to Hinglish/Benglish – Instantly ✨")

st.markdown("""
Upload your PDF or image file below.  
We'll extract the Hindi/Bengali text and convert it to Roman script (Hinglish).  
_Nothing is stored. Everything runs locally or in-session only 💚_
""")

# 💡 Helper function to check if uploaded file is a valid PDF
def is_valid_pdf(file_path):
    file_type = magic.from_file(file_path, mime=True)
    return file_type == 'application/pdf'

uploaded_file = st.file_uploader("📁 Upload PDF or Image", type=["pdf", "png", "jpg", "jpeg"])

lang_choice = st.selectbox("🌐 Choose Language", ["Hindi", "Bengali"])
lang_code = "hin" if lang_choice == "Hindi" else "ben"

# After user uploads a file
if uploaded_file:
    st.write("✅ Uploaded:", uploaded_file.name)

    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    if st.button("🚀 Convert Now"):
        with st.spinner("Extracting text and transliterating... ✨🪄"):
            if is_valid_pdf(temp_path):
                extracted_text = process_pdf_for_ocr(temp_path, lang=lang_code)
            else:
                extracted_text = process_image_for_ocr(temp_path, lang=lang_code)

            hinglish_output = transliterate_text(extracted_text, lang=lang_code)

        st.success("🎉 Done! Here's the Hinglish output:")
        st.text_area("📜 Hinglish Output", hinglish_output, height=300)
        st.download_button("💾 Download as TXT", data=hinglish_output, file_name="output.txt")

        try:
            os.remove(temp_path)
        except:
            pass