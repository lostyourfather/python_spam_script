import time
import sys
import json


def learning_model(input_data: str, target_data: str, params: str) -> None:
    try:
        input_data = json.loads(input_data)
    except json.decoder.JSONDecodeError:
        print("Type error: incorrect input data")
        return
    try:
        target_data = json.loads(target_data)
    except json.decoder.JSONDecodeError:
        print("Type error: incorrect target data")
        return
    try:
        params = json.loads(params)
    except json.decoder.JSONDecodeError:
        print("Type error: incorrect params")
    time.sleep(1)
    print("Status: learning finished")
    return


if __name__ == '__main__':
    learning_model(sys.argv[1], sys.argv[2], sys.argv[3])