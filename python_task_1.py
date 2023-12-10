import pandas as pd
import numpy as np

def generate_car_matrix():
    # Load the dataset
    df = pd.read_csv(r'C:\Users\deepi\Desktop\test\MapUp-Data-Assessment-F\datasets\dataset-1.csv')

    # Create the new Dataframe
    new_df = df.pivot(index='id_1', columns='id_2', values='car')

    # Set diagonal values to zero
    np.fill_diagonal(new_df.values, 0)

    return new_df


def get_type_count():
    #Load the dataset
    df = pd.read_csv(r'C:\Users\deepi\Desktop\test\MapUp-Data-Assessment-F\datasets\dataset-1.csv')

    #create the new column
    df['car_type'] = pd.cut(df['car'], bins=[-1, 15, 25, float('inf')], labels=['low', 'medium', 'high'])

    # Calculate the count of occurrences
    car_type_counts = df['car_type'].value_counts()

    #sort the dictionary
    car_type_counts_dict = dict(sorted(car_type_counts.items()))

    return car_type_counts_dict


def get_bus_indexes():
    #Load the dataset into a dataframe
    df = pd.read_csv(r'C:\Users\deepi\Desktop\test\MapUp-Data-Assessment-F\datasets\dataset-1.csv')

    # Calculate the mean of the 'bus' Column
    mean_bus = df['bus'].mean()

    #identify the indicies where the 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes


def filter_routes():
    #Load the dataset into a dataframe
    df = pd.read_csv(r'C:\Users\deepi\Desktop\test\MapUp-Data-Assessment-F\datasets\dataset-1.csv')

    #group the dataframe by 'route' and calculate the mean of 'truck' for each group
    grouped = df.groupby('route')['truck'].mean()

    #filter the groups where the average 'truck' value is greater than 7
    filtered_routes = grouped[grouped > 7].index.tolist()

    #sort the routes in ascending order
    filtered_routes.sort()

    return filtered_routes


def multiply_matrix():
    #load the dataset of question1 to this dataframe
    df = generate_car_matrix()

    #To modify the values in the dataframe accoording to the given logic
    df = df.map(lambda x:x * 0.75 if x > 20 else x * 1.25)

    #Round the modified values to 1 decimal place
    df = df.round(1)

    return df


def check_timestamps():
    #to load the dataset-2 into dataframe
    df = pd.read_csv(r'C:\Users\deepi\Desktop\test\MapUp-Data-Assessment-F\datasets\dataset-2.csv')

    #To convert the 'startday', starttime, endday, endtime colums to datetime format
    df['start'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    #create a new dataframe with multi-index and a boolean column
    result = pd.DataFrame(index=df.set_index(['id', 'id_2']).index.drop_duplicates())

    #check if the timestamp for each ('id', 'id_2') pair cover a full 24 hour period and span all 7 days of the week
    result['incorrect'] = df.groupby(['id', 'id_2']).apply(lambda group:group['start'].dt.hour.min() > 0 or group['end'].dt.hour.max() < 23 or group['start'].dt.dayofweek.nunique() < 7)

    return result

    
    