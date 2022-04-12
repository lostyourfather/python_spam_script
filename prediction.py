import time
import sys
import json


def prediction(input_data: str) -> list[[float]]:
    try:
        input_data = json.loads(input_data)
    except json.decoder.JSONDecodeError:
        print("Type error: incorrect input data")
        return [[0.0], [0.0]]
    time.sleep(1)
    result = [[2.3, 5.2], [532.21, 13.22]]
    print(result)
    return result


if __name__ == '__main__':
    prediction(sys.argv[1])
