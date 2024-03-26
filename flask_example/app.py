from flask import Flask, render_template, request, redirect, url_for, send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/page1_upload', methods=['POST'])
def upload_file_page1():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('page1'))


@app.route('/page1')
def page1():
    return render_template('page1.html')


@app.route('/page2_upload', methods=['POST'])
def upload_file_page2():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # return redirect(url_for('page1'))
        return send_file(file_path, as_attachment=True)


@app.route('/page2')
def page2():
    return render_template('page2.html')


if __name__ == '__main__':
    app.run(debug=True)
