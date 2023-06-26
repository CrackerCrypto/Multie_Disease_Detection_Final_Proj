import pandas as pd
import numpy as np

class ConvertToArray():
    @classmethod
    def dictToArray(cls, values):
        # for breast cancer
        if len(values) == 14:
            df = pd.read_csv('datasets/breast_cancer_dataset.csv')
            # store dataframe columns
            columns = list(df.columns)
            columns = columns[2:]

            # Initialize the dictionary with 0.0
            attrs_dict = {}
            attrs_dict = {columns[i]: df[columns[i]].mean() for i in range(len(columns))}

            attrs_dict.update(values)
            cal_array = np.asarray(list(attrs_dict.values()))
            return cal_array

        # for thyroid checking
        elif len(values) == 5:
            df = pd.read_csv('datasets/thyroid_checking_dataset.csv')
            columns = list(df.columns)
            columns = columns[2:27]

            # Initialize the dictionary with 0.0
            attrs_dict = {}
            attrs_dict = {columns[i]: df[columns[i]].mean() for i in range(len(columns))}

            attrs_dict.update(values)
            cal_array = np.asarray(list(attrs_dict.values()))
            return cal_array
        
        # for fetal health
        elif len(values) == 9:
            df = pd.read_csv('datasets/fetal_health.csv')
            columns = list(df.columns)
            columns = columns[:-1]

            # Initialize the dictionary with 0.0
            attrs_dict = {}
            attrs_dict = {columns[i]: df[columns[i]].mean() for i in range(len(columns))}

            attrs_dict.update(values)
            cal_array = np.asarray(list(attrs_dict.values()))
            return cal_array
