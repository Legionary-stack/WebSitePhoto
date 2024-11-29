from flask import Flask, render_template, request, redirect, url_for
from image_processing import replace_colors
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')
            colors = [(196, 243, 56), (27, 27, 27)]  # Example colors
            num_squares = 102
            replace_colors(file_path, output_path, colors, num_squares)
            return redirect(url_for('uploaded_file', filename='output.png'))
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('uploaded.html', filename=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

