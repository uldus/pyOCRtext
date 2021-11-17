try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def ocr_core(filename,lang):
    """
    This function will handle the core OCR processing of images.
    """
    #image = cv2.imread(filename)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename),lang)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core(r'''temp\test3.png''','rus'))