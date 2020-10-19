import datetime
import hashlib
import os
import shutil
from werkzeug.utils import secure_filename

from flask import Flask, request, render_template, send_file


app = Flask(__name__, template_folder='templates')

UPLOAD_DIRECTORY = f'{os.environ["HOME"]}/store/'


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Please add a file to upload'

        file = request.files['file']
        return save_file(file)

    return render_template('upload_file.html')


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = f'{UPLOAD_DIRECTORY}/{filename[:2]}/{filename}'

    if os.path.isfile(file_path):
        return send_file(file_path, as_attachment=True, attachment_filename='')
    else:
        return f'File {filename} not found'


@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    path_to_delete = f'{UPLOAD_DIRECTORY}/{filename[:2]}'

    if os.path.isdir(path_to_delete):
        shutil.rmtree(path_to_delete)
    else:
        return f'File {filename} not found'

    return f'File {filename} has been deleted'


def save_file(file):
    # This check is needed if you upload a file via the web interface
    if file.filename == '':
        return 'Please add a file to upload.'

    hashed_filename = get_hash(file)

    file_directory = f'{UPLOAD_DIRECTORY}/{hashed_filename[:2]}'
    os.mkdir(file_directory)
    file.save(os.path.join(file_directory, hashed_filename))

    return f'The file has been successfully saved as {hashed_filename} in {file_directory}'


def get_hash(file):
    current_time = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
    filename = bytearray(
        f'{current_time}{secure_filename(file.filename)}', encoding='utf-8')
    return hashlib.md5(filename).hexdigest()


def main():
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
