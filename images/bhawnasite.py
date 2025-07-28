import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors

def generate_star(ax, radius=3.0, color='gold'):
    """Creates a larger spherical star at the origin"""
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 50)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color=color, edgecolor='none', alpha=0.9)

def generate_wind(ax, num_streams=50):
    """Generates colorful outward-moving streamlines from the star"""
    theta = np.linspace(0, 2 * np.pi, num_streams)
    phi = np.linspace(0, np.pi, num_streams // 2)
    colors = plt.cm.plasma(np.linspace(0, 1, num_streams))
    
    for i, (t, c) in enumerate(zip(theta, colors)):
        for p in phi:
            r = np.linspace(3, 12, 50)  # Adjusted for larger star
            x = r * np.sin(p) * np.cos(t)
            y = r * np.sin(p) * np.sin(t)
            z = r * np.cos(p)
            ax.plot(x, y, z, color=mcolors.to_hex(c), alpha=0.6)

def generate_nebula(ax):
    """Adds a diffuse nebula effect using scattered points"""
    num_points = 500
    x = np.random.uniform(-12, 12, num_points)
    y = np.random.uniform(-12, 12, num_points)
    z = np.random.uniform(-12, 12, num_points)
    colors = plt.cm.magma(np.random.rand(num_points))
    ax.scatter(x, y, z, c=colors, s=10, alpha=0.3)

def plot_circumstellar_environment():
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-12, 12])
    ax.set_ylim([-12, 12])
    ax.set_zlim([-12, 12])
    
    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_frame_on(False)
    
    # Generate star, wind, and nebula
    generate_star(ax)
    generate_wind(ax)
    generate_nebula(ax)
    
    # Title
    ax.set_title("Massive Star Ejecting Winds in a Nebula", fontsize=14, color='white')
    ax.set_facecolor("black")
    
    plt.show()

plot_circumstellar_environment()
