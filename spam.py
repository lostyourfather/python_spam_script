import json


def spam_function(arr_str_json: str) -> str:
    if not isinstance(arr_str_json, str):
        raise TypeError('Parameter of function must be string')
    try:
        arr_json = json.loads(arr_str_json)
    except json.decoder.JSONDecodeError:
        raise ValueError('Incorrect json format')
    if 'arr' in arr_json:
        if len(arr_json['arr']) >= 2:
            if len(arr_json['arr'][1]) >= 3:
                print('The array changed')
                arr_json['arr'][1][2] = 9
    arr_json = json.dumps(arr_json)
    with open("result.json", 'w') as fw:
        fw.write(arr_json)
    return arr_json


print(spam_function('{"arr": [[1,2,3],[2,4,5]]}'))
