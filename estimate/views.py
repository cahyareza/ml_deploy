import pickle5 as pickle
from .forms import EstimateForm
from django.shortcuts import render
import pandas as pd
import numpy as np
from estimate import build_model
from sklearn import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

cols = ['Gender', 'Married', 'Dependents',
        'Education', 'Self_Employed', 'ApplicantIncome',
        'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
        'Credit_History', 'Property_Area']

def home(request):
    form = EstimateForm(request.POST or None)

    return render(request, "form.html", {"form": form})

def result(request):
    form = EstimateForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        int_features = [x for x in data.values()]
        final = np.array(int_features)
        df = pd.DataFrame([final], columns=cols)
        df['Gender'] = df['Gender'].astype('int8')
        df['Married'] = df['Married'].astype('int8')
        df['Dependents'] = df['Dependents'].astype('int8')
        df['Education'] = df['Education'].astype('int8')
        df['Self_Employed'] = df['Self_Employed'].astype('int8')
        df['Credit_History'] = df['Credit_History'].astype('int8')
        df['Property_Area'] = df['Property_Area'].astype('int8')
        df['ApplicantIncome'] = df['ApplicantIncome'].astype('int64')
        df['CoapplicantIncome'] = df['CoapplicantIncome'].astype('float64')
        df['LoanAmount'] = df['LoanAmount'].astype('float64')
        df['Loan_Amount_Term'] = df['Loan_Amount_Term'].astype('float64')
        df = build_model.ins_null(df)
        #df = build_model.encode(df)

        with open(BASE_DIR /'clf_model.pkl', 'rb') as file:
            model = pickle.load(file)

        result = model.predict(df)[0]


        return render(request, "result.html", {'result':result})

    form = EstimateForm()
    return render(request, "form.html", {"form": form})