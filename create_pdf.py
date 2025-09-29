from fpdf import FPDF

# Create PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'main_django.py', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create an instance of the PDF class
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Content to be written
content = """# main_django.py\n\nimport os\nimport sys\nfrom django.core.management import execute_from_command_line\n\n# Set up the Django environment\nos.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')\ntry:\n    import django\n    django.setup()\nexcept ImportError:\n    print("Django is not installed. Please install it using 'pip install django'")\n    sys.exit(1)\n\n# Basic Django app setup\nif __name__ == '__main__':\n    execute_from_command_line(sys.argv)\n""" 

# Add content to PDF
for line in content.splitlines():
    pdf.cell(0, 10, line, ln=True)

# Save the PDF to a file
pdf_file_path = 'main_django.pdf'
pdf.output(pdf_file_path)