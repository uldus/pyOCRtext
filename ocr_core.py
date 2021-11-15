try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def ocr_core(filename,lang):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename),lang)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core(r'''temp\test3.png''','rus'))