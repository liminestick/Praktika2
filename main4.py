import os
import json
import pickle

# Загрузка данных о товарах из файла pkl
with open("fourth_task_products.pkl", "rb") as pkl_file:
    products = pickle.load(pkl_file)

# Загрузка обновлений цен из файла json
with open("fourth_task_updates.json", "r", encoding="utf-8") as json_file:
    updates = json.load(json_file)

# Применение обновлений к товарам
for update in updates:
    name = update["name"]
    method = update["method"]
    param = update["param"]

    # Находим товар и обновляем цену
    for product in products:
        if product["name"] == name:
            if method == "add":
                product["price"] += param
            elif method == "sub":
                product["price"] -= param
            elif method == "percent+":
                product["price"] *= (1 + param)
            elif method == "percent-":
                product["price"] *= (1 - param)
            product["price"] = round(product["price"], 2)  # Округление до 2 знаков

# Сохранение модифицированных данных обратно в pkl
output_path = "задание4/modified_products.pkl"
with open(output_path, "wb") as pkl_file:
    pickle.dump(products, pkl_file)
