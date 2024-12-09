import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung pi menggunakan Monte Carlo
def monte_carlo_pi(num_points):
    x = np.random.uniform(-1, 1, num_points)  # Titik acak pada sumbu x
    y = np.random.uniform(-1, 1, num_points)  # Titik acak pada sumbu y
    
    # Hitung jarak dari titik ke pusat (0, 0)
    distance = np.sqrt(x**2 + y**2)
    
    # Titik di dalam lingkaran (distance <= 1)
    inside_circle = distance <= 1
    
    # Estimasi nilai pi
    pi_estimate = 4 * np.sum(inside_circle) / num_points
    
    return pi_estimate, x, y, distance, inside_circle

# Jumlah titik acak
num_points = 10000

# Simulasi
pi_estimate, x, y, distance, inside_circle = monte_carlo_pi(num_points)

# Plotting scatter plot
plt.figure(figsize=(12, 6))

# Scatter plot
plt.subplot(1, 2, 1)
plt.scatter(x[inside_circle], y[inside_circle], color='blue', s=1, label='Inside Circle')
plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Outside Circle')
plt.title(f"Monte Carlo Simulation for Pi\nEstimated Pi: {pi_estimate:.5f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')

# Histogram of distances
plt.subplot(1, 2, 2)
plt.hist(distance, bins=30, color='green', alpha=0.7, edgecolor='black')
plt.axvline(1, color='red', linestyle='--', label='Circle Radius (1)')
plt.title("Histogram of Distances to Center")
plt.xlabel("Distance")
plt.ylabel("Frequency")
plt.legend()

# Tampilkan hasil
plt.tight_layout()
plt.show()
