from flask import Flask, request, render_template
 
app = Flask(__name__)  

@app.route('/', methods =["GET","POST"])
def calc():
    area = 0
    if request.method == "POST":
       base = request.form.get("base",10)
       height = request.form.get("height", 10)
       area = (int(base)*int(height))/2

    return render_template("home.html", area=area)