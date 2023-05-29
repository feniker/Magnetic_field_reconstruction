import numpy as np
import matplotlib.pyplot as plt
import magpylib as magpy

# 1. define sources and observers as objects
cube = magpy.magnet.Cuboid(magnetization=(0,0,100), dimension=(1,1,1))
loop = magpy.current.Loop(current=5, diameter=3, position=(0,0,-3))
sensor = magpy.Sensor(position=(0,0,2), style_size=1.8)

# 2. move objects and display graphically
sensor.rotate_from_rotvec((0,0,225), degrees=True)
cube.position = np.linspace((-3,0,0), (3,0,0), 50)
loop.move(np.linspace((0,0,0), (0,0,6), 50), start=0)

magpy.show(loop, cube, sensor, backend='plotly', animation=2, style_path_show=False)

# 3. compute field at sensor (and plot with Matplotlib)
B = sensor.getB(cube, loop, sumup=True)

plt.plot(B, label=['Bx', 'By', 'Bz'])
plt.legend()
plt.grid(color='.8')
plt.show()