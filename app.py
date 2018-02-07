from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/waze_jams/")
def wazeJams():
    return render_template('waze_jams.html')



if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')