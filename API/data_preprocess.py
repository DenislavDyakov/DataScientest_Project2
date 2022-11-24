import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler


def input_data(df):
    df_base = pd.read_csv('https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/strokes.csv', index_col='id')
    df_base.rename(columns = {'Residence_type': 'residence_type'}, inplace = True)
    df_base[['hypertension','heart_disease', 'stroke']] = df_base[['hypertension','heart_disease', 'stroke']].astype('O')
    idx = list(pd.Series(np.arange(-10000, (-10000 + len(df)), +1)))
    df["new_id"] = idx
    df = df.set_index(["new_id"])
    df_concat = pd.concat([df_base, df])
    df_concat = df_concat.drop('stroke', axis=1)
    return df_concat


def imput_missing_values(df):
    nan_columns = df[df.columns[df.isnull().any()]].columns

    for col in nan_columns:
        imputer = SimpleImputer(missing_values=np.nan, strategy='median')
        imputer.fit(df[[col]])
        df[col] = imputer.transform(df[[col]])
        df[col] = df[col].round(2)
    return df


def encode_values(df):
    label_encode = preprocessing.LabelEncoder()
    df['hypertension'] = label_encode.fit_transform(df['hypertension'])
    df['gender'] = label_encode.fit_transform(df['gender'])
    df['ever_married'] = label_encode.fit_transform(df['ever_married'])
    df['residence_type'] = label_encode.fit_transform(df['residence_type'])
    df = pd.get_dummies(df, prefix=['work_type'], columns=['work_type'], drop_first=True)
    df = pd.get_dummies(df, prefix=['smoking_status'], columns=['smoking_status'], drop_first=True)
    df.rename(columns=
              {'smoking_status_never smoked': 'smoking_status_never_smoked',
               'smoking_status_formerly smoked': 'smoking_status_formerly_smoked'}, inplace=True)
    return df


def scale_values(df):
    scaler = MinMaxScaler()
    df[['age', 'avg_glucose_level', 'bmi']] = scaler.fit_transform(df[['age', 'avg_glucose_level', 'bmi']])
    return df


def data_preprocessing(df):
    df = df[df.index < 0]
    return df
