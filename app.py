from flask import Flask, redirect, url_for, request,render_template
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
  

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 8)
    loaded_model = pickle.load(open("exam.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result

          
@app.route("/")
def index():
    return render_template("index.html"); 
@app.route('/result',  methods =["GET", "POST"])
def result():
    if request.method == "POST":
       
       Gender = request.form.get("Gender")
       # getting input with name = lname in HTML form 
       Glucose = request.form.get("Glucose") 
       BP= request.form.get("BP") 
       SkinThickness= request.form.get("SkinThickness") 
       Insulin = request.form.get("Insulin") 
       BMI = request.form.get("BMI") 
       PedigreeFunction = request.form.get("PedigreeFunction") 
       Age = request.form.get("Age") 
        
       l1=[Gender,Glucose,BP,SkinThickness,Insulin,BMI,PedigreeFunction,Age]
       answer = ValuePredictor(l1)
    return render_template("result.html",Age=answer)
   
  
if __name__ == '__main__':
   app.run(debug = True)