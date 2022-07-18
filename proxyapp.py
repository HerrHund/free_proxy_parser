from flask import Flask, Response, render_template, stream_with_context, redirect
import json
app = Flask(__name__)



@app.route("/")
def free():
    
    return render_template("index.html")
    

@app.route("/free")
def get_free():
    with open('free.json') as json_file:
        data = json.load(json_file)
        
    return render_template("free.html", content=data)
    
@app.route("/anonymous")
def get_anonymous():
    with open('anonymous.json') as json_file:
        data = json.load(json_file)
        
    return render_template("anonymous.html", content=data)


@app.route("/socks")
def get_socks():
    with open('socks.json') as json_file:
        data = json.load(json_file)
        
    return render_template("socks.html", content=data)
    
@app.route("/ssl")
def get_ssl():
    with open('ssl.json') as json_file:
        data = json.load(json_file)
        
    return render_template("ssl.html", content=data)


@app.route("/uk")
def get_uk():
    with open('uk.json') as json_file:
        data = json.load(json_file)
        
    return render_template("uk.html", content=data)
    
@app.route("/us")
def get_us():
    with open('us.json') as json_file:
        data = json.load(json_file)
        
    return render_template("us.html", content=data)



app.template_folder = "templates"
app.run(host="0.0.0.0", port=8000)

