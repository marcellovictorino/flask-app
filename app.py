from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/waze_jams/")
def wazeJams():
    return render_template('waze_jams.html')

@app.route("/waze_potholes/")
def wazePotholes():
    return render_template('waze_potholes.html')

@app.route("/equipment_comm_status/")
def equipmentCommStatus():
    return render_template('equipmentCommStatus.html')

@app.route("/gpx/")
def gpx():
    return render_template('gpx.html')



if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')