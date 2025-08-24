from typing import Union
import pandas as pd


def accuracy(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the accuracy
    """

    """
    The following assert checks if sizes of y_hat and y are equal.
    Students are required to add appropriate assert checks at places to
    ensure that the function does not fail in corner cases.
    """
    assert y_hat.size == y.size
    # TODO: Write here

    total_correct_pred = (y_hat == y).sum()
    total_instances = len(y)

    acc = float(total_correct_pred / total_instances)
    return acc

    # pass


def precision(y_hat: pd.Series, y: pd.Series, cls: Union[int, str]) -> float:
    """
    Function to calculate the precision
    """

    # Precision = True Positives / (True Positives + False Positives)

    true_pos = ((y_hat == cls) & (y == cls)).sum()
    pred_pos = (y_hat == cls).sum()

    assert pred_pos # Denominator should not be 0

    pre = float(true_pos / pred_pos)
    return pre
    # pass


def recall(y_hat: pd.Series, y: pd.Series, cls: Union[int, str]) -> float:
    """
    Function to calculate the recall
    """

    # Recall = True Positives / (True Positives + False Negatives)

    true_pos = ((y_hat == cls) & (y == cls)).sum()
    ground_pos = (y == cls).sum()

    assert ground_pos # Denominator should not be 0

    rec = float(true_pos / ground_pos)
    return rec
    # pass


def rmse(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the root-mean-squared-error(rmse)
    """

    # RMSE = ((1 / n) * Summation((y_pred - y_actual)^2))^0.5

    total_instances = len(y)
    y_hat_y_2_sum = ((y_hat - y) ** 2).sum()

    root_mean_se = y_hat_y_2_sum / total_instances
    return float(root_mean_se ** 0.5)
    # pass


def mae(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the mean-absolute-error(mae)
    """

    # MAE = Summation(|y_pred - y|) / n

    total_instances = len(y)
    y_hat_y_sum = (abs(y_hat - y)).sum()

    mean_ae = y_hat_y_sum / total_instances
    return float(mean_ae)
    # pass 
