import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

def main():
    # читать изображение с помощью OpenCV
    image = cv2.imread(r'''C:\Users\galimov\PycharmProjects\pyOCRtext1\temp\test.png''')
    # или вы можете использовать подушку
    #image = Image.open('C:/Users/galimov/PycharmProjects/pyOCRtext1/temp/test1.png')
    # получаем строку
    string = pytesseract.image_to_string(image,lang = 'eng')
    # печатаем
    print(string)

if __name__ == '__main__':
    main()