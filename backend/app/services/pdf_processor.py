import PyPDF2
import pdfplumber
from io import BytesIO

class PDFProcessor:
    def extract_text(self, file):
        """Extract text from PDF file using multiple methods for better results"""
        try:
            # Try pdfplumber first (better for Greek text)
            return self._extract_with_pdfplumber(file)
        except Exception as e:
            print(f"pdfplumber failed: {e}, trying PyPDF2...")
            try:
                return self._extract_with_pypdf2(file)
            except Exception as e2:
                print(f"PyPDF2 also failed: {e2}")
                raise Exception("Could not extract text from PDF")
    
    def _extract_with_pdfplumber(self, file):
        """Extract text using pdfplumber"""
        text = ""
        file_bytes = BytesIO(file.read())
        
        with pdfplumber.open(file_bytes) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        
        return text
    
    def _extract_with_pypdf2(self, file):
        """Extract text using PyPDF2 as fallback"""
        text = ""
        file.seek(0)  # Reset file pointer
        
        pdf_reader = PyPDF2.PdfReader(file)
        
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        
        return text
