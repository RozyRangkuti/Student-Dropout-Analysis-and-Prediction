import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def data_preprocessing(data_input, single_data, n):
    """Preprocessing data

    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    
    df = pd.read_csv('selection_student_data.csv')
    df = df.drop(columns=['Status'], axis=1)
    df = pd.concat([data_input, df])

    df = StandardScaler().fit_transform(df)

    if single_data:
        return df[[n]]
    else:
        return df[0 : n]


