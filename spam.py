import json


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
    '''print(f"{arr_json['learning']=}")
    print(f"{arr_json['forecast']=}")
    print(f"{arr_json['params']=}")'''
    if len(arr_json['learning']) >= 2:
        if len(arr_json['learning'][1]) >= 3:
            arr_json['learning'][1][2] = 9.0
    result = {"targetAgr": [1.0, 2.0, 3.0, 11.0, 1.0, 2.0, 3.0, 11.0, 1.0, 2.0, 3.0, 11.0, 1.0, 2.0, 3.0, 11.0, 1.0, 2.0, 3.0, 111.0, 2.0, 3.0, 11.0, 1.0, 2.0, 3.0, 11.0]}
    with open("result.json", 'w') as fw:
        json.dump(result, fw)
    return arr_json


if __name__ == "__main__":
    with open("data.json", 'r', encoding='utf-8') as fr:
        spam_function(fr.read())
