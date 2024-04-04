import os
import joblib
import pandas as pd
from fastapi import Depends, FastAPI
from models import PredSchema
from fastapi.responses import JSONResponse,HTMLResponse


app = FastAPI()


# Load the trained pipeline
pipeline_filename = os.path.join('trained_model', 'stroke_prediction_pipeline.pkl')
pipeline = joblib.load(pipeline_filename)

@app.post('/predict')
async def predict(user_data:PredSchema):
    age=user_data.age
    hypertension=user_data.hypertension
    heart_disease=user_data.heart_disease
    avg_glucose_level=user_data.avg_glucose_level
    bmi=user_data.bmi
    gender=user_data.gender
    ever_married=user_data.ever_married
    work_type=user_data.work_type
    Residence_type=user_data.Residence_type
    smoking_status=user_data.smoking_status

    try:
        data =  {
                "age":age,
                "hypertension":hypertension,
                "heart_disease":heart_disease,
                'avg_glucose_level':avg_glucose_level,
                "bmi":bmi,
                "gender":gender,
                "ever_married":ever_married,
                "work_type":work_type,
                "Residence_type":Residence_type,
                "smoking_status":smoking_status
            }
        

        # Convert data to a DataFrame
        new_data = pd.DataFrame(data, index=[0])

        # Make predictions using the pipeline
        prediction = pipeline.predict(new_data)

        pred_mapping = {
            0: 'No-Stroke',
            1: 'Stroke'
        }

        predicted_class = pred_mapping[prediction[0]]
        return JSONResponse(content={"message" : f"Model prediction is {predicted_class}"},
                            status_code= 201
               )
        return f"Model prediction is {predicted_class}"
    except Exception as e:
         return "Error in processing AI response"


if __name__ == '__main__':
    app.run(debug=True)