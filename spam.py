import json
import sys


def spam_function(arr_str_json: str) -> None:
    if not isinstance(arr_str_json, str):
        print("TypeError: Parameter of function must be string")
        return
        # raise TypeError('Parameter of function must be string')
    try:
        arr_json = json.loads(arr_str_json)
    except json.decoder.JSONDecodeError:
        print("ValueError: Incorrect json format")
        return
        # raise ValueError('Incorrect json format')
    if 'arr' in arr_json:
        if len(arr_json['arr']) >= 2:
            if len(arr_json['arr'][1]) >= 3:
                arr_json['arr'][1][2] = 9
    arr_json = json.dumps(arr_json)
    with open("result.json", 'w') as fw:
        fw.write(arr_json)
    print(arr_json)
    return arr_json


if __name__ == "__main__":
    with open("data.txt", 'r', encoding='utf-8') as fr:
        spam_function(fr.read())
    #spam_function(sys.argv[1])
