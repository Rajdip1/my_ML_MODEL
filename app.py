from flask import Flask , render_template , request

import marks as m

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def hello():
    if request.method=="POST":
        hours=request.form['hours']
        marks_pred=m.marks_prediction(hours)
        mk=marks_pred
    return render_template("index.html",my_marks=mk)

# @app.route("/sub",methods=["POST"])
# def submit():

#     #html to python
#     if request.method == "POST":
#         name=request.form["username"]

#         #python file to html
#         return render_template("sub.html",n=name)


if __name__ == "__main__":
    app.run(debug=True)