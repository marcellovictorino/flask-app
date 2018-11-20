from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploaded/gpxFiles'
ALLOWED_EXTENSIONS = set(['gpx', 'pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'ireallydontknowwhatthisisfor'

@app.route("/")
def home():
    return render_template('home.html')

# Dashboards
##############
@app.route("/waze_jams/")
def wazeJams():
    return render_template('waze_jams.html')

@app.route("/waze_potholes/")
def wazePotholes():
    return render_template('waze_potholes.html')

@app.route("/potholes_integration/")
def potholesIntegration():
    return render_template('potholes_integration.html')

@app.route("/equipment_comm_status/")
def equipmentCommStatus():
    return render_template('equipmentCommStatus.html')

@app.route("/FBC_Transit_Operational_Data/")
def fbc_transit():
    return render_template('FBC_Transit.html')

##############
# Bluetooth
##############
@app.route("/bluetooth_bluetoad/")
def bluetoothBluetoad():
    return render_template('bluetoothBluetoad.html')

@app.route("/bluetooth_po/")
def bluetoothPO():
    return render_template('bluetoothPostOak.html')

##############
# GPX + others
##############

@app.route("/gpx/")
def gpx():
    return render_template('gpx.html')

@app.route("/login/")
def login():
    return render_template('login.html')

@app.route("/login_action/", methods=['POST', 'GET'])
def login_action():
    if request.method == 'POST':
        user = request.form['nm']
        return "Welcome, {}".format(user)
    else:
        user = request.args.get('nm')
        return "(GET) Welcome, {}".format(user)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/gpx_file_uploader/", methods = ['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Do something to let user know file was uploaded succesfully
            # add progress bar for file upload
            # return redirect(url_for('upload_file', filename=filename)) # Why is this necessary!?
            flash('File uploaded successfully!', 'success')
        
            return redirect(url_for('gpx'))
            # return "File uploaded succesfully!"
    else:
        return 'Opsss... something wrong!'



if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')