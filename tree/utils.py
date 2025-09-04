"""
You can add your own functions here according to your decision tree implementation.
There is no restriction on following the below template, these fucntions are here to simply help you.
"""

import pandas as pd
import numpy as np

def one_hot_encoding(X: pd.DataFrame) -> pd.DataFrame:
    """
    Function to perform one hot encoding on the input data
    """

    X_encoded = X.copy()
    
    for feature in X.columns:
        if not check_ifreal(X[feature]):
            # Get unique values
            unique_vals = X[feature].unique()
            
            # Create dummy columns
            for val in unique_vals:
                X_encoded[f"{feature}_{val}"] = (X[feature] == val).astype(int)
            
            # Drop original categorical column
            X_encoded.drop(columns = [feature], inplace=True)
    
    return X_encoded
    # pass

def check_ifreal(y: pd.Series) -> bool:
    """
    Function to check if the given series has real or discrete values
    """
    threshold = 15

    # Coerce to numeric; non-numeric -> NaN -> dropped
    s = pd.to_numeric(y, errors = "coerce").dropna()
    if s.empty:
        return False

    # Any fractional part => real-valued
    if ((s % 1) != 0).any():
        return True

    # Fallback on cardinality
    return s.nunique() > threshold
    # pass


def entropy(Y: pd.Series) -> float:
    """
    Function to calculate the entropy
    """

    # Count occurrences of each unique value
    value_counts = Y.value_counts().values
    
    # Probabilities
    probs = value_counts / len(Y)
    
    # Entropy formula: -sum(p * log2(p))
    entropy_value = -np.sum(probs * np.log2(probs))
    
    return entropy_value
    # pass


def gini_index(Y: pd.Series) -> float:
    """
    Function to calculate the gini index
    """

    # Count occurrences of each unique value
    value_counts = Y.value_counts().values
    
    # Probabilities
    probs = value_counts / len(Y)

    # Gini Index Formula: 1 - sum(p ^ 2)
    gini_ind_value = 1 - np.sum(probs ** 2)

    return gini_ind_value
    # pass

def mse(Y: pd.Series) -> float:
    """
    Function to calculate the mean squared error
    """

    total_instances = len(Y)

    # mse_value = 

    pass

def information_gain(Y: pd.Series, attr: pd.Series, criterion: str) -> float:
    """
    Function to calculate the information gain using criterion (entropy, gini index or MSE)
    """



    pass


def opt_split_attribute(X: pd.DataFrame, y: pd.Series, criterion, features: pd.Series):
    """
    Function to find the optimal attribute to split about.
    If needed you can split this function into 2, one for discrete and one for real valued features.
    You can also change the parameters of this function according to your implementation.

    features: pd.Series is a list of all the attributes we have to split upon

    return: attribute to split upon
    """

    # According to wheather the features are real or discrete valued and the criterion, find the attribute from the features series with the maximum information gain (entropy or varinace based on the type of output) or minimum gini index (discrete output).

    pass


def split_data(X: pd.DataFrame, y: pd.Series, attribute, value):
    """
    Funtion to split the data according to an attribute.
    If needed you can split this function into 2, one for discrete and one for real valued features.
    You can also change the parameters of this function according to your implementation.

    attribute: attribute/feature to split upon
    value: value of that attribute to split upon

    return: splitted data(Input and output)
    """

    # Split the data based on a particular value of a particular attribute. You may use masking as a tool to split the data.

    pass
