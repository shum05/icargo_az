from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)  # entry

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])

def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            level_of_education=request.form.get('level_of_education'),
            language_proficiency=request.form.get('language_proficiency'),
            training_manuals=request.form.get('training_manuals'),
            pre_exams_average=float(request.form.get('pre_exams_average'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("after Prediction")
        
        # Modify the following lines to return 'PASS' or 'FAIL' based on results[0]
        if results[0] == 1.0:
            result_text = 'PASS'
        elif results[0] == 0.0:
            result_text = 'FAIL'
        else:
            result_text = 'UNKNOWN'  # Handle other cases if needed
        
        return render_template('home.html', results=result_text)
    
# run app.py
if __name__=="__main__":
    app.run(host="0.0.0.0",port=80)        


