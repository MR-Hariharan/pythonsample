import numpy as np

# Given temperature data
data = np.array([[22.5, 19.0, 31.2, 28.7, 25.1],
                 [17.3, 22.8, 30.5, 26.4, 21.9],
                 [33.1, 29.6, 18.4, 24.0, 27.8],
                 [20.2, 23.5, 31.9, 28.1, 22.6]])

# -----------------------------
# Task 1: Shape and Mean per Station
# -----------------------------

print("Shape of data:", data.shape)

mean_per_station = np.mean(data, axis=1)
print("Mean temperature per station:", mean_per_station)


# -----------------------------
# Task 2: Boolean Mask (> 28°C)
# -----------------------------

mask = data > 28.0
high_temperatures = data[mask]

print("Temperatures above 28°C:", high_temperatures)


# -----------------------------
# Task 3: Normalize Data [0,1]
# -----------------------------

normalized = (data - data.min()) / (data.max() - data.min())

print("Normalized data (rounded to 2 decimals):")
print(np.round(normalized, 2))