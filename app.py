from flask import Flask,render_template,redirect,request
#from sklearn.externals import joblib
import joblib
model=joblib.load("model1.pkl")
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def result():
    if request.method=='POST':
        t1= int(request.form['t1'])
        t2=int(request.form['t2'])
        t3=int(request.form['t3'])
        t4=int(request.form['t4'])
        result=str(model.predict([[t1,t2,t3,t4]])[0])
        return render_template("index.html",play=result)


if __name__=='__main__':
    app.run(debug=True)

