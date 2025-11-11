import matplotlib.pyplot as plt
import numpy as np

# Dummy data
x = np.arange(1, 11)
y = x * 2
z = x ** 2

# --------------------------------------
# 1. LINE PLOT
# --------------------------------------
plt.figure(figsize=(6,4))
plt.plot(x, y, label="y = 2x", marker='o')
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()