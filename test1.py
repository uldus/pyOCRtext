import pytesseract
import cv2
import os
import matplotlib.pyplot as plt
from PIL import Image

# нужно установить tesseract-ocr-w64-setup-v5.0.0-rc1.20211030.exe
# https://pythobyte.com/pytesseract-simple-python-optical-character-recognition-14a4bd3c/
# https://stackoverflow.com/questions/50655738/how-do-i-resolve-a-tesseractnotfounderror
# x86
#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
# x86_64
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def main():
    # читать изображение с помощью OpenCV
    #filename = r'''temp\example_01.png'''
    image = r'''temp\111.png'''

    #preprocess = "thresh"
    preprocess = "blur"

    # загрузить образ и преобразовать его в оттенки серого
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # проверьте, следует ли применять пороговое значение для предварительной обработки изображения

    if preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # если нужно медианное размытие, чтобы удалить шум
    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)

    # сохраним временную картинку в оттенках серого, чтобы можно было применить к ней OCR

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    # загрузка изображения в виде объекта image Pillow, применение OCR, а затем удаление временного файла
    text = pytesseract.image_to_string(Image.open(filename))
    #os.remove(filename)
    print(text)

    # показать выходные изображения
    cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    #input(‘pause…’)

if __name__ == '__main__':
    main()