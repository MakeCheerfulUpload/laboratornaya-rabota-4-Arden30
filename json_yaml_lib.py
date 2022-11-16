import json
import yaml

def json_to_yaml_lib():
    j, y = open("timetable.json", 'r'), open("timetable_lib.yaml", 'w')
    js_load = json.load(j)
    ym_res = yaml.dump(js_load, allow_unicode=True)
    y.write(ym_res)
json_to_yaml_lib()

