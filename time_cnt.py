import time

from json_yaml import json_to_yaml
from json_yaml_lib import json_to_yaml_lib
from json_yaml_reg import json_to_yaml_reg

start_time = time.time()
for i in range(100):
    json_to_yaml()
print("Время стократного выполнения для обычного парсера:", round(time.time() - start_time, 3), "секунды")

start_time_lib = time.time()
for i in range(100):
    json_to_yaml_lib()
print("Время стократного выполнения для библиотечного парсера:", round(time.time() - start_time_lib, 3), "секунды")

start_time_reg = time.time()
for i in range(100):
    json_to_yaml_reg()
print("Время стократного выполнения для парсера с регулярками:", round(time.time() - start_time_reg, 3), "секунды")