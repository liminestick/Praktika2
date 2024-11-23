import pandas as pd
import json
import pickle
import msgpack
import os

# Указание пути к файлу и настройка папки вывода
input_path = "car_prices.csv"  # Путь к вашему файлу
output_folder = "задание5"

# Загрузка данных
df = pd.read_csv(input_path)

# Отбор 7-10 полей для работы
selected_fields = [
    "year", "make", "model", "body", "odometer", "mmr", "sellingprice"
]
df = df[selected_fields]

# Вычисление характеристик для числовых данных
numerical_fields = df.select_dtypes(include=["number"]).columns
stats = {}

for field in numerical_fields:
    stats[field] = {
        "min": float(df[field].min()),
        "max": float(df[field].max()),
        "mean": float(df[field].mean()),
        "sum": float(df[field].sum()),
        "std": float(df[field].std())
    }

# Вычисление частоты встречаемости для категориальных данных
categorical_fields = df.select_dtypes(include=["object"]).columns

for field in categorical_fields:
    stats[field] = df[field].value_counts().to_dict()

# Преобразование ключей и значений для совместимости с JSON
stats = json.loads(json.dumps(stats))  # Автоматическое приведение к Python-типам

# Сохранение расчетов в JSON
stats_path = os.path.join(output_folder, "statistics.json")
with open(stats_path, "w", encoding="utf-8") as json_file:
    json.dump(stats, json_file, ensure_ascii=False, indent=4)

# Сохранение набора данных в разных форматах
csv_path = os.path.join(output_folder, "data.csv")
df.to_csv(csv_path, index=False)

json_path = os.path.join(output_folder, "data.json")
df.to_json(json_path, orient="records", force_ascii=False)

msgpack_path = os.path.join(output_folder, "data.msgpack")
with open(msgpack_path, "wb") as msgpack_file:
    msgpack.pack(df.to_dict(orient="records"), msgpack_file)

pkl_path = os.path.join(output_folder, "data.pkl")
with open(pkl_path, "wb") as pkl_file:
    pickle.dump(df, pkl_file)

# Сравнение размеров файлов
file_sizes = {
    "CSV": os.path.getsize(csv_path),
    "JSON": os.path.getsize(json_path),
    "MsgPack": os.path.getsize(msgpack_path),
    "Pickle": os.path.getsize(pkl_path)
}

print("Размеры файлов (в байтах):", file_sizes)
