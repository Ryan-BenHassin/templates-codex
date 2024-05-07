import os
from PIL import Image
from flask import Flask, request, render_template
from flask_uploads import UploadManager, configure_uploads, IMAGES
app = Flask(__name__)
app.config['UPLOADS_DEFAULT_DEST'] = '/uploads'
upload_manager = UploadManager(app, folder='/uploads')
configure_uploads(app, upload_manager)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' in request.files:
            img = request.files['image']
            img_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOADS_DEFAULT_DEST'], img.filename)
            img.save(img_path)
            image = Image.open(img_path)
            width, height = image.size
            image = image.resize((width // 2, height // 2))
            image.save(img_path)
            return render_template('index.html', uploaded=True, filename=img.filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)