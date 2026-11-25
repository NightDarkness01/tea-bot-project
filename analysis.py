import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)

# 1. Загрузка данных 
df = pd.read_csv("tea_dataset_ru.csv", encoding="utf-8-sig")

print("Первые строки таблицы:")
print(df.head())

print("\nРазмер таблицы:", df.shape)

# Проверка на пропуски и дубликаты
print("\nПропущенные значения:")
print(df.isna().sum())
print("Полных дубликатов:", df.duplicated().sum())

# 2. Анализ категорий
category_count = df["category_ru"].value_counts()
print("\nКоличество сортов по категориям:")
print(category_count)

plt.figure(figsize=(10, 5))
plt.bar(category_count.index, category_count.values)
plt.title("Количество сортов чая по категориям")
plt.xlabel("Категория")
plt.ylabel("Количество сортов")
plt.xticks(rotation=30, ha='right')
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("images/categories.png")
plt.show()

# 3. Параметры заваривания по категориям 
print("\nСредние параметры заваривания по категориям:")
stats = df.groupby("category_ru", as_index=False).agg(
    count=('id', 'count'),
    mean_temp=('water_temp', 'mean'),
    mean_time=('steep_time', 'mean'),
    mean_infusions=('infusions', 'mean')
)
stats = stats.sort_values("mean_temp", ascending=False)
print(stats.round(2))

stats.to_csv("tea_stats_by_category.csv", index=False, encoding="utf-8-sig")

plt.figure(figsize=(10, 5))
plt.bar(stats["category_ru"], stats["mean_temp"])
plt.title("Средняя температура заваривания по категориям")
plt.xlabel("Категория")
plt.ylabel("Температура, °C")
plt.xticks(rotation=30, ha='right')
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("images/temperature.png")
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(stats["category_ru"], stats["mean_time"])
plt.title("Среднее время заваривания по категориям")
plt.xlabel("Категория")
plt.ylabel("Время, секунды")
plt.xticks(rotation=30, ha='right')
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("images/steeping_time.png")
plt.show()

# 4. Углублённый анализ температур
temps = df["water_temp"].to_numpy()
print("\n--- Анализ температур (NumPy) ---")
print("Среднее:", np.mean(temps))
print("Медиана:", np.median(temps))
print("Квартили (25%, 50%, 75%):", np.percentile(temps, [25, 50, 75]))
print("Сортов, требующих почти кипяток (>=95°C):", np.count_nonzero(temps >= 95))

plt.figure(figsize=(8, 5))
plt.hist(temps, bins=10, edgecolor="black")
plt.title("Распределение температуры заваривания")
plt.xlabel("Температура, °C")
plt.ylabel("Количество сортов")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("images/temp_distribution.png")
plt.show()

# 5. Зависимость температуры от степени окисления
plt.figure(figsize=(8, 5))
plt.scatter(df["oxidation_level"], df["water_temp"], alpha=0.7)
plt.title("Зависимость температуры от степени окисления")
plt.xlabel("Степень окисления")
plt.ylabel("Температура, °C")
plt.grid()
plt.tight_layout()
plt.savefig("images/oxidation_temperature.png")
plt.show()

# Корреляция
data_for_corr = df[["oxidation_level", "water_temp", "steep_time", "infusions"]].dropna().to_numpy()
correlation = np.corrcoef(data_for_corr, rowvar=False)

print("\nКорреляционная матрица:")
corr_df = pd.DataFrame(
    correlation,
    index=["Окисление", "Температура", "Время", "Проливы"],
    columns=["Окисление", "Температура", "Время", "Проливы"]
)
print(corr_df.round(2))

print("\n✅ Анализ завершён. Графики сохранены в папку 'images'.")
