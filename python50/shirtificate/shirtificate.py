from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        #self.image("./shirtificate.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 30)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(10)


pdf = PDF()
pdf.add_page()
pdf.image("./shirtificate.png", x=55, y=30, w=pdf.epw/2)
pdf.set_font("Times", size=20)
pdf.cell(70)
name = input("Name: ")
pdf.cell(50, 100, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
