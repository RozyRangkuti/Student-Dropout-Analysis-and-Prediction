import joblib

def model_predict(df):
    """Making prediction

    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data

    Returns:
        str: Prediction result (Graduate or Dropout)
    """
    
    model = joblib.load("model/rdf_model.joblib")
    return model.predict(df)