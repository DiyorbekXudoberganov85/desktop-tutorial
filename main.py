from flask import Flask, render_template , request , redirect
from database.db import obj
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")
@app.route('/menulist')
def menulist():
    foodlist=obj.foodlist()
    return render_template("menu/menulist.html",foodlist=foodlist )

@app.route("/detail/<id>/<nomi>/")
def menudetail(id , nomi):
    ovqat =obj.menudetail(id)
    return render_template("menu/menudetall.html" , ovqat=ovqat ,nomi=nomi)

@app.route("/savatcha")
def savatcha():
    zakazlar = obj.savatcha()
    return render_template("zakaz/savatcha.html" , zakazlar = zakazlar)

@app.route("/addsavat/<ovqatid>/")
def addsavat():
    pass
@app.route("/user/login")
def login():
    return render_template("users/login.html")
@app.route('/user/registration' , methods=['GET' , 'POST'])
def reg():
    if request.method =='GET':
        return render_template("users/register.html")
    elif request.method=='POST':
        ism = request.form['ism']
        familiya = request.form['familiya']
        login = request.form['login']
        pasword = request.form['pasword']

        obj.registratsiya(ism , familiya , login , pasword)
        return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)
