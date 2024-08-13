from django.shortcuts import render
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI DiabetesPedigreeFunction  Age
        Pregnancies = request.POST.get('Pregnancies')
        Glucose = request.POST.get('Glucose')
        BloodPressure = request.POST.get('BloodPressure')
        SkinThickness = request.POST.get('SkinThickness')
        Insulin = request.POST.get('Insulin')
        BMI = request.POST.get('BMI')
        DiabetesPedigreeFunction = request.POST.get('DiabetesPedigreeFunction')
        Age = request.POST.get('Age')
        # Load the saved model & scaler
        loaded_model = pickle.load(open('Ml_model/Diabetes_prediction_model.sav','rb'))
        loaded_scaler = pickle.load(open('Ml_model/Diabetes_prediction_scaler.sav','rb'))

        input_data = (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,DiabetesPedigreeFunction,Age)
        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array as we are predicting for one instance {1d to 2d}
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        # standardize the input data
        std_data = loaded_scaler.transform(input_data_reshaped)
        print("std_data:",std_data)

        prediction = loaded_model.predict(std_data)
        print(prediction)

        if (prediction[0] == 0):
            return render(request,'diabetes_app/index.html',{'msg':'The person is not diabetic'})
        else:
            return render(request,'diabetes_app/index.html',{'msg':'The person is diabetic'})

        
    else:
        return render(request,'diabetes_app/index.html')

