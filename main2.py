import os
import numpy as np

# Загружаем матрицу из файла
matrix = np.load("second_task.npy")

# Условие: значения > 579
indices = np.argwhere(matrix > 579)
x, y = indices[:, 0], indices[:, 1]
z = matrix[matrix > 579]

# Сохраняем массивы в файлы формата npz
np.savez("задание2/result.npz", x=x, y=y, z=z)
np.savez_compressed("задание2/result_compressed.npz", x=x, y=y, z=z)

# Получаем размеры файлов
size_regular = os.path.getsize("задание2/result.npz")
size_compressed = os.path.getsize("задание2/result_compressed.npz")

print(f"Размер обычного файла: {size_regular} байт")
print(f"Размер сжатого файла: {size_compressed} байт")
