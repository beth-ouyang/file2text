from io import StringIO
import docx

def convert_word(path):
    """Extract text from Word file

    Words are made lowercase and punctuation is removed 
    before counting.

    Parameters
    ----------
    path : str
        Path to docx file.

    Returns
    -------
    string
        Plain text contained in the docx file.

    Examples
    --------
    >>> convert_word("text.docx")
    """
    doc = docx.Document(path)
    
    convert_text = ''
    
    for para in doc.paragraphs:
        convert_text += para.text
    
    return convert_text