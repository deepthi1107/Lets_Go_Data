import os
import joblib
model = joblib.load(r'data_hack.pkl')

# importing Flask and other modules
from flask import Flask, request, render_template 
import numpy as np
## import pandas as pd
  
# Flask constructor
app = Flask(__name__)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods = ["GET", "POST"])
def adult_autism():
    if request.method == "POST":
       State = request.form.get("State")
       Literacy_rate= request.form.get("Literacy_rate")
       District = request.form.get("District_number")
       p = model.predict(pd.array([State, Literacy_rate, District_number]).reshape(-2,2))
       if p == 1:
           output = "aaa"
           return render_template('index.html', output=output)
       elif p == 2:
           output = "bbb"
           return render_template('index.html', output=output)
        
    return render_template('index.html')
  
if __name__=='__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)
