from fpdf import FPDF

def save_as_text(text, filename="output.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return filename

def save_as_pdf(text, filename="output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    lines = text.split('\n')
    for line in lines:
        pdf.cell(200, 10, txt=line, ln=True)
    
    pdf.output(filename)
    return filename