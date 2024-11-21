# Import the necessary library
from docx2pdf import convert

def convert_docx_to_pdf(docx_path, pdf_path):
    """
    Convert a .docx file to .pdf using docx2pdf.
    
    :param docx_path: The input .docx file path.
    :param pdf_path: The output .pdf file path.
    """
    try:
        # Convert the .docx to .pdf
        convert(docx_path, pdf_path)
        print(f"File successfully converted and saved to {pdf_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_docx = "input.docx"  # Path to your input .docx file
    output_pdf = "output.pdf"  # Path to save the output .pdf file
    
    convert_docx_to_pdf(input_docx, output_pdf)
