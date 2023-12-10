from flask import Flask, render_template, Blueprint, request, redirect, url_for
from utilsapp import doit
app =Flask(__name__, template_folder=".")
app.config['SECRET_KEY'] = 'your secret key'


@app.route("/sign", methods=["GET","POST"])
def index():
      email=""
      if request.method=="POST":
            email=request.form.get('email')
            print(email)
            doit(email)
            return render_template("page2.html",email=email)
      return render_template('index.html',email=email)
      #return render_template('index.html')




if __name__=="__main__":
      app.run(debug=True)