import os
import time
from flask import Flask, render_template, request

# import our OCR function
from ocr_core import ocr_core
from webcam_test1 import cam_save


# define a folder to store and later serve the images
UPLOAD_FOLDER = 'static\\uploads\\'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the home page
@app.route('/')
def home_page():
    return render_template('index.html')

# route and function to handle the upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        #lang = 'rus'
        lang = request.form.getlist('selectID')[0]
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # call the OCR function on it
            extracted_text = ocr_core(file,lang)

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

# route and function to handle the upload page

@app.route('/camocr', methods=['GET', 'POST'])
def camocr_page():

    if request.method == 'POST':
        if request.form['submit_button'] == 'Photo':
            global fn
            fn = UPLOAD_FOLDER + time.strftime("%Y%m%d-%H%M%S") + '.jpg'
            print(fn)
            cam_save(fn)
            return render_template('camocr.html', msg='Successfully processed',
                                   img_src=fn)
        elif request.form['submit_button'] == 'OCR':
            lang = 'rus'
            print(fn)
            #extracted_text = fn
            extracted_text = ocr_core(fn, lang)

            # extract the text and display it
            return render_template('camocr.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=fn)


    elif request.method == 'GET':
        return render_template('camocr.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0')
