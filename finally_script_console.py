import json
import pandas as pd
import sys
from sklearn.cluster import KMeans
import warnings


def warn(*args, **kwargs):
    pass


warnings.warn = warn


def finally_script(arr_str_json: str) -> list:
    if not isinstance(arr_str_json, str):
        print("TypeError: Parameter of function must be string")
        return []
        # raise TypeError('Parameter of function must be string')
    try:
        arr_json = json.loads(arr_str_json)
    except json.decoder.JSONDecodeError:
        print("ValueError: Incorrect json format")
        return []
    learning = pd.DataFrame(arr_json['learning']).T
    forecast = pd.DataFrame(arr_json['forecast']).T
    kmeans = KMeans(n_clusters=int(arr_json['params']['n_clusters']), n_init=int(arr_json['params']['n_init']),
                    max_iter=int(arr_json['params']['max_iter']),
                    tol=float(arr_json['params']['tol'])).fit(learning.drop(columns=0))
    answers = pd.DataFrame({'value': learning[0], 'clusters': kmeans.labels_})
    predict = pd.Series(kmeans.predict(forecast), name='predict')
    mean = answers.groupby('clusters').mean()
    result = list(mean.merge(predict, left_index=True, right_on='predict', how='right')['value'].values)
    return result


if __name__ == "__main__":
    print(finally_script(sys.argv[1]))
