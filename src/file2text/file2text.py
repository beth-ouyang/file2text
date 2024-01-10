from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
import docx


def convert_pdf(path, page=1):
    """Extract text from PDF file"""
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()

    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, pageno=page, laparams=laparams)
    fp = open(path, 'rb')

    process_pdf(rsrcmgr, device, fp)

    fp.close()
    device.close()
    s = retstr.getvalue()
    retstr.close()

    return s

def convert_word(path):
    """Extract text from Word file"""
    doc = docx.Document(path)
    
    convert_text = ''
    
    for para in doc.paragraphs:
        convert_text += para.text
    
    return convert_text