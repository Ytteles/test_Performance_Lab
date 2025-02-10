import sys
import json


def load_json(file_path_json: str) -> dict:
    with open(file_path_json, 'r') as file:
        return json.load(file)


def save_json(path_file: str, data: dict) -> None:
    with open(path_file, 'w') as file:
        json.dump(data, file, indent=2)


def fill_values(data: dict, values_dict: dict) -> None:
    if isinstance(data, list):
        for item in data:
            fill_values(item, values_dict)
    elif isinstance(data, dict):
        test_id = data.get('id')
        if test_id in values_dict:
            data['value'] = values_dict[test_id]
        for key in ['tests', 'values']:
            if key in data and isinstance(data[key], list):
                fill_values(data[key], values_dict)


def create_report_json_file():
    tests_path, values_path, report_path = sys.argv[1], sys.argv[2], sys.argv[3]
    tests_data = load_json(tests_path)
    values_data = load_json(values_path)
    values_dict = {item['id']: item['value'] for item in values_data['values']}
    fill_values(tests_data, values_dict)
    save_json(report_path, tests_data)


main()
