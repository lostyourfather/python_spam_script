import json
import sys
import time


def forecast(arr_str_json: str) -> str:
    time.sleep(3)
    if not isinstance(arr_str_json, str):
        raise TypeError('Parameter of function must be string')
    try:
        arr_json = json.loads(arr_str_json)
    except json.decoder.JSONDecodeError:
        raise ValueError('Incorrect json format')

    res = json.dumps({"targetAgr": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0]})
    print(res)
    return 'Done'


if __name__ == "__main__":
    forecast(sys.argv[1])
