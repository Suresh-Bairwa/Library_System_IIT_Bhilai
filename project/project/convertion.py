import json
import smtplib
from datetime import datetime
from email.message import EmailMessage
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home/")
def home1():
    return render_template("home.html")       
    
@app.route("/iss/")
def home5():
    return render_template("iss.html")

@app.route("/return/")
def home4():
    return render_template("return.html")    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    # temp1=jsonObj['temp1']
    # temp2=jsonObj['temp2']
    # response+="<b> The input temparatures in Celcius are: <b>"+temp1+" and "+temp2+"</b><br>"
        
    
    
    	    
    return response


@app.route("/submitJSON2", methods=["POST",'GET'])
def processJSON1(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    response = ""
    name=jsonObj['name']
    roll=jsonObj['roll']
    gmail=jsonObj['gmail']
    Book_name=jsonObj['book_issued']
    # response+="<b>  <b>"+name+" and "+roll+"</b><br>"
    

    
   
    # temp1=jsonObj['temp1']
    # temp2=jsonObj['temp2']
    # response+="<b> The input temparatures in Celcius are: <b>"+temp1+" and "+temp2+"</b><br>"
        
    
    
    	    
    return response    
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
