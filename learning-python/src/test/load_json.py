from json import JSONEncoder
import json


def get_apps():
    return ['app1', 'app2', 'app3', 'app4']


def get_nodes(app):
    return ['nod1']


def print_json_file_content():
    json_file = open('test.json')
    with json_file as data:
        json_data = json.load(data)
    print json_data

    json_string = '{' + json.dumps(json_data) + '}'
    print json_string.format("mohanraj")

    pass


def print_string_with_quotes():
    string_with_quote = '{{"name": {}, "age": {} }}'.format('mohanraj', 32)
    print string_with_quote


print_json_file_content()
print_string_with_quotes()