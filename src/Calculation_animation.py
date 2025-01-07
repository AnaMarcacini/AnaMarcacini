import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from IPython.display import display

# Definindo a função 3D
def func(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Criando os dados para o gráfico
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = func(x, y)

# Criando a animação
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    ax.clear()
    # ax.set_title("Função 3D: $f(x, y) = \\sin(\\sqrt{x^2 + y^2})$")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Animando a função
    ax.plot_surface(x, y, func(x, y + frame*0.1), cmap='viridis')

# Configurando a animação
ani = animation.FuncAnimation(fig, update, frames=100, interval=100)

# Salvando a animação como gif
ani.save('animation.gif', writer='imagemagick')
