import pickle
import pandas as pd

# insert null values
def ins_null(df):
    attr = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Credit_History', 'Property_Area']
    for i in df.columns:
        if i in attr:
            df[i] = df[i].fillna(df[i].mode()[0])
        else:
            df[i] = df[i].fillna(df[i].median())
    return df
#one hot encoding nominal categorical
def encode(df):
    attr = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Credit_History', 'Property_Area']
    for i in attr:
        df[i] = df[i].cat.codes
    return df










