import pandas as pd
from fpdf import FPDF

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    
    pdf.add_page()
# Set Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    for y in range(21,290,10):
        pdf.line(10, y, 200, y)

# Set Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.cell(w=0, h=8, txt=row['Topic'], align="R")

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        for i in range(21,290,10):
            pdf.line(10, i, 200, i)
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=8, txt=row['Topic'], align="R")


pdf.output("output.pdf")