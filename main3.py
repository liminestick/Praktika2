import os
import json
import msgpack
from collections import defaultdict

# Загружаем данные из файла third_task.json
with open("third_task.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Агрегирование информации по каждому товару
aggregated_data = defaultdict(lambda: {"prices": [], "average_price": 0, "max_price": 0, "min_price": 0})

for item in data:
    name = item["name"]
    price = item["price"]
    aggregated_data[name]["prices"].append(price)

for name, stats in aggregated_data.items():
    prices = stats["prices"]
    aggregated_data[name]["average_price"] = round(sum(prices) / len(prices), 2)
    aggregated_data[name]["max_price"] = max(prices)
    aggregated_data[name]["min_price"] = min(prices)
    del aggregated_data[name]["prices"]  # Удаляем промежуточные данные

# Сохранение информации в JSON
json_path = "задание3/aggregated_data.json"
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(aggregated_data, json_file, ensure_ascii=False, indent=4)

# Сохранение информации в формате MessagePack
msgpack_path = "задание3/aggregated_data.msgpack"
with open(msgpack_path, "wb") as msgpack_file:
    msgpack.pack(aggregated_data, msgpack_file)

# Сравнение размеров файлов
size_json = os.path.getsize(json_path)
size_msgpack = os.path.getsize(msgpack_path)

print(f"Размер JSON файла: {size_json} байт")
print(f"Размер MessagePack файла: {size_msgpack} байт")
