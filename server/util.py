import pickle
import json
import numpy as np

__models = None
__data_columns = None
__model = None

def get_estimated_price(model,km_driven,owner,car_age):

    try:
        loc_index = __data_columns.index(model.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = km_driven
    x[1] = owner
    x[2] = car_age
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)



def load_saved_artifacts():

    global  __data_columns
    global __models

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __models = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/used_car_price.pickle', 'rb') as f:
            __model = pickle.load(f)



def get_model_names():
    return __models


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()


