from flask import *
import os
import werkzeug
from datetime import datetime

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 20*1024*1024
UPLOAD_DIR = "C:/Users\daina teranishi/PycharmProjects/flask_sample/logfile"
app.config['UPLOAD_DIR'] = UPLOAD_DIR
app.config['SECRET_KEY'] = os.urandom(24)


@app.route("/data/upload", methods=['POST'])
def log():
        if 'uploadfile' not in request.files:
            make_response(jsonify({'result':'uploadFile is required'}))
        file = request.files['data']
        filename = file.filename
        if '' == filename:
            make_response(jsonify({'result':'filename must not empty.'}))
        saveFileName = datetime.now().strftime("%Y%m%d_%H%M%S_") \
                       + werkzeug.utils.secure_filename(filename)
        file.save(os.path.join(app.config['UPLOAD_DIR'], saveFileName))
        return make_response(jsonify({'result':'upload OK.'}))

@app.errorhandler(werkzeug.exceptions.RequestEntityTooLarge)
def handle_over_max_file_size(error):
    print("werkzeug.exceptions.RequestEntityTooLarge")
    return 'result : file size is overed.'

if __name__ == '__main__':
    print (app.url_map)
    app.run(debug=True, host = '0.0.0.0', port=3000, threaded=True)
