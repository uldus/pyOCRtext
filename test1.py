import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

# нужно установить tesseract-ocr-w64-setup-v5.0.0-rc1.20211030.exe
# x86
#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
# x86_64
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def main():
    # читать изображение с помощью OpenCV
    image = cv2.imread(r'''temp\test2.png''')
    # или вы можете использовать подушку
    #image = Image.open('C:/Users/galimov/PycharmProjects/pyOCRtext1/temp/test1.png')
    # получаем строку
    string = pytesseract.image_to_string(image,lang = 'rus')
    # печатаем
    print(string)

if __name__ == '__main__':
    main()