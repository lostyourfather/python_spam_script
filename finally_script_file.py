import json
import pandas as pd
import sys
from sklearn.cluster import KMeans
import warnings
import uuid


def warn(*args, **kwargs):
    pass


warnings.warn = warn


def finally_script(arr_str_json: str) -> None:
    if not isinstance(arr_str_json, str):
        print("TypeError: Parameter of function must be string")
        return
        # raise TypeError('Parameter of function must be string')
    try:
        arr_json = json.loads(arr_str_json)
    except json.decoder.JSONDecodeError:
        print("ValueError: Incorrect json format")
        return
    learning = pd.DataFrame(arr_json['learning']).T
    forecast = pd.DataFrame(arr_json['forecast']).T
    kmeans = KMeans(n_clusters=int(arr_json['params']['N_CLUSTERS']), n_init=int(arr_json['params']['N_INIT']),
                    max_iter=int(arr_json['params']['MAX_ITER'])).fit(learning.drop(columns=0))
    answers = pd.DataFrame({'value': learning[0], 'clusters': kmeans.labels_})
    predict = pd.Series(kmeans.predict(forecast), name='predict')
    mean = answers.groupby('clusters').mean()
    result = list(mean.merge(predict, left_index=True, right_on='predict', how='right')['value'].values)
    my_uuid = uuid.uuid1()
    with open(f'{my_uuid.__str__()}.json', 'w') as fw:
        json.dump(result, fw)
    return


if __name__ == "__main__":
    with open(sys.argv[1], 'r', encoding='utf-8') as fr:
        finally_script(fr.read())
