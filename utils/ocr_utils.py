from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os
import tempfile

# Disable decompression bomb warnings for large images
Image.MAX_IMAGE_PIXELS = None

def ocr_image(image_path, lang='hin'):
    """
    Perform OCR on a single image.
    """
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang=lang)
    return text

def process_pdf_for_ocr(pdf_path, lang='hin', dpi=200):
    """
    Convert a PDF to images, then perform OCR on each page.
    """
    extracted_text = ""
    with tempfile.TemporaryDirectory() as output_folder:
        images = convert_from_path(pdf_path, dpi=dpi, output_folder=output_folder, fmt='jpeg')
        for i, img in enumerate(images):
            temp_img_path = os.path.join(output_folder, f"page_{i + 1}.jpg")
            img.save(temp_img_path, "JPEG")
            extracted_text += ocr_image(temp_img_path, lang) + "\n\n"
    return extracted_text

def process_image_for_ocr(image_path, lang='hin'):
    """
    Perform OCR directly on an image (not from PDF).
    """
    return ocr_image(image_path, lang)