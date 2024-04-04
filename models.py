from pydantic import BaseModel



class PredSchema(BaseModel):
    age:str
    hypertension:str
    heart_disease:int
    avg_glucose_level:int
    bmi:int
    gender:str
    ever_married:str
    work_type:str
    Residence_type:str
    smoking_status:str
    class Config:
        json_schema_extra ={
            "example":{
                "age":"age ",
                "hypertension":"Hypertension (0 for No, 1 for Yes)",
                "heart_disease":"Heart disease (0 for No, 1 for Yes)",
                'avg_glucose_level':"Average glucose level",
                "bmi":"body max index",
                "gender":"Gender (Male, Female, Other)",
                "ever_married":"Marital status (Yes, No)",
                "work_type":"Type of work (Private, Self-employed, etc.)",
                "Residence_type":" Residence type (Urban, Rural)",
                "smoking_status":"Smoking status (formerly smoked, never smoked, etc.)"




            }
        }

