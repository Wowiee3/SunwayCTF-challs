from flask import Flask, render_template, request
from waitress import serve
import os

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('index.html', query="")
    
    elif request.method == "POST":
        number = request.form["number"]
        if not number:
            return render_template('index.html', query="Specify how many times to ping remote server!")
        else:
            os.system(f"ping -c {number} 127.0.0.1")
            return render_template('index.html', query=f"Pinged {number} times on remote server. Server will be not sleeping anymore!")
    
    return "Method not allowed"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5001)
