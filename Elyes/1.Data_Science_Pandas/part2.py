from math import nan
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def display_info(df):
    print(df.info())

def display_columns(df):
    print(df.keys())

def display_percentage_missing(df):
    for i in df.keys():
        print(i, 100 - 100 * df[i].dropna().__len__() / df.__len__())

def display_missing_data(df):
    for i in df.keys():
        print(i,  df.__len__() - df[i].dropna().__len__())

def select_numerical_values(df):
    return df._get_numeric_data().keys()

def display_heatmap(df):
    sns.heatmap(df.corr(), annot=True)
    plt.show()

def remove_columns(df):
    print('Before ', df.shape)
    for i in ['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating']:
        del df[i]

    print('After ', df.shape)

def fill_NaN_values(df):
    print(df.mode())
    # return

if __name__ == '__main__':
    file = pd.read_csv("./video_games.csv")
    fill_NaN_values(file)