import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def main():
    # читать изображение с помощью OpenCV
    filename = r'''/temp/test3.png'''
    lang = 'rus'
    image = cv2.imread(filename)

    # remove color info
    gray_image = image[:, :, 0]

    # (1) thresholding image
    ret, thresh_value = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY_INV)

    # (2) dilating image to glue letter with e/a
    kernel = np.ones((2, 2), np.uint8)
    dilated_value = cv2.dilate(thresh_value, kernel, iterations=1)

    # (3) looking for countours
    contours, hierarchy = cv2.findContours(dilated_value, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # (4) extracting coordinates and filtering them empirically
    coordinates = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if h > 50 and w > 50 and h * w < 350000:
            coordinates.append((x, y, w, h))



    text = pytesseract.image_to_string(image, lang)
    # os.remove(filename)
    #print(text)
    print(text.replace("\n", " "))

if __name__ == '__main__':
    main()