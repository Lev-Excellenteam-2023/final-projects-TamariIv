import json
import os
import threading

from flask import Flask, request, jsonify, render_template
from datetime import datetime
from uuid import uuid4

app = Flask(__name__, template_folder='template')
UPLOADS_FOLDER = 'uploads'
OUTPUTS_FOLDER = 'outputs'


@app.route('/submit', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file attached", 400

        file = request.files['file']
        original_filename, filetype = os.path.splitext(file.filename)

        # Generate a unique filename using UID, timestamp, and original filename
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        uid = str(uuid4())
        filename = f'{original_filename}_{timestamp}_{uid}{filetype}'

        # Save the file in the uploads folder
        file.save(os.path.join('uploads', filename))

        return jsonify({'uid': uid})
    elif request.method == 'GET':
        return render_template('submit.html')


@app.route('/status/<uid>', methods=['GET'])
def get_upload_status(uid):
    upload_data = {}
    upload_status = 'not found'
    explanation = None

    # Check if the file exists
    for filename in os.listdir(UPLOADS_FOLDER):
        if uid in filename:
            upload_status = 'done' if is_file_processed(filename) else 'pending'
            upload_data = parse_file_info(filename)
            if upload_status == 'done':
                explanation = parse_file_explanation(filename)
            break

    # Prepare the JSON response
    response = {
        'status': upload_status,
        'filename': upload_data.get('original_filename'),
        'timestamp': upload_data.get('timestamp'),
        'explanation': explanation
    }

    if upload_status == 'not found':
        return jsonify(response), 404
    return jsonify(response)


def is_file_processed(filename):
    for file in os.listdir(OUTPUTS_FOLDER):
        if filename in file:
            return True
    return False


def parse_file_info(filename):
    # Parse the file information and return it as a dictionary
    _, original_filename, timestamp, uid = filename.split('_')
    return {
        'original_filename': original_filename,
        'timestamp': timestamp,
        'uid': uid
    }


def parse_file_explanation(filename):
    # Parse the file's JSON content and return the explanation
    with open(os.path.join(UPLOADS_FOLDER, filename)) as file:
        content = json.load(file)
        return content.get('explanation')


def run_app():
    app.run(debug=True, use_reloader=False)


def start():
    explainer_thread = threading.Thread(target=run_app)
    explainer_thread.start()


if __name__ == '__main__':
    app.run(debug=True)
