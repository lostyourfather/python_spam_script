import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import sys
import warnings
import json
import uuid


def warn(*args, **kwargs):
    pass


warnings.warn = warn


def KNNR_forecast(arr_str_json):
    if not isinstance(arr_str_json, str):
        print("TypeError: Parameter of function must be string")
        return
    try:
        arr_json = json.loads(arr_str_json)
    except json.decoder.JSONDecodeError:
        print("ValueError: Incorrect json format")
        return
    learning = pd.DataFrame(arr_json['learning']).T
    forecast = pd.DataFrame(arr_json['forecast']).T

    neigh = KNeighborsRegressor(n_neighbors=arr_json['params']['n_neighbors'],
                                weights=arr_json['params']['weights']).fit(learning.drop(columns=0), learning[0])
    my_uuid = uuid.uuid1()
    with open(f'{my_uuid.__str__()}.json', 'w') as fw:
        json.dump(neigh.predict(forecast).tolist(), fw)
    return


if __name__ == "__main__":
    with open(sys.argv[1], 'r', encoding='utf-8') as fr:
        KNNR_forecast(fr.read())
