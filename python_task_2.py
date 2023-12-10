import pandas as pd
import numpy as np

def calculate_distance_matrix():
    #Load the dataset into a dataframe
    df = pd.read_csv(r'C:\Users\deepi\Desktop\test\MapUp-Data-Assessment-F\datasets\dataset-3.csv')

    #create an empty Dataframe with the unique IDs as both the index and column
    ids = df['id'].unique()
    distance_matrix = pd.DataFrame(np.inf, index=ids, columns=ids)

    #calculate the distances between each pair of IDs
    for i in ids:
        for j in ids:
            if i == j:
                distance_matrix.loc[i, j] = 0
            else:
                #calculate the distance from ID i to ID j
                distance = df[(df['id'] == i) & (df['id_2'] == j)]['distance'].sum()
                if distance > 0:
                    distance_matrix.loc[i, j] = distance

    #ensure the matrix is symmetric
    distance_matrix = distance_matrix.combine(distance_matrix.T, np.minumim)

    return distance_matrix


