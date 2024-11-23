import os
import numpy as np
import json

# Загружаем матрицу из файла
matrix = np.load("first_task.npy")

# Вычисления
sum_all = int(np.sum(matrix))
avr_all = float(np.mean(matrix))
main_diag = np.diag(matrix)
side_diag = np.diag(np.fliplr(matrix))
sum_md = int(np.sum(main_diag))
avr_md = float(np.mean(main_diag))
sum_sd = int(np.sum(side_diag))
avr_sd = float(np.mean(side_diag))
max_val = int(np.max(matrix))
min_val = int(np.min(matrix))

# Сохраняем результаты в JSON
results = {
    "sum": sum_all,
    "avr": avr_all,
    "sumMD": sum_md,
    "avrMD": avr_md,
    "sumSD": sum_sd,
    "avrSD": avr_sd,
    "max": max_val,
    "min": min_val,
}

with open("задание1/results.json", "w", encoding="utf-8") as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=4)

# Нормализуем матрицу
matrix_normalized = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))

# Сохраняем нормализованную матрицу
np.save("задание1/normalized_matrix.npy", matrix_normalized)

