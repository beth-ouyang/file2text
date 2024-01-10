from io import StringIO
import docx

def convert_word(path):
    """Extract text from Word file"""
    doc = docx.Document(path)
    
    convert_text = ''
    
    for para in doc.paragraphs:
        convert_text += para.text
    
    return convert_text