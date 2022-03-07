import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    # temp1=jsonObj['temp1']
    # temp2=jsonObj['temp2']
    # response+="<b> The input temparatures in Celcius are: <b>"+temp1+" and "+temp2+"</b><br>"
        
    
    
    	    
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
