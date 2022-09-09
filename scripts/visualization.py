# created by Hongyu Li at 20220905 23:47.
# 
# https://lhy.xyz

from tentacle_sampl import diff_model, quadrotor_model, sample_vel
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pyvista
import numpy as np

def vis_diff_model():
    plt.figure()
    
    init_pos = np.array([.0,.0,.0]) # x axis is towards the top
    for _ in range(10):
        init_pos = diff_model(init_pos, 1.1, -0.5, 0.1)
        plt.plot(init_pos[1], init_pos[0], "r.") # plt figure y axis towards the top, so we switch order
    
    plt.show()


def vis_quadrotor_model():
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    
    init_pos = np.array([.0,.0,.0]) # x axis is towards the top
    for _ in range(10):
        init_pos = quadrotor_model(init_pos, np.array([1.0,1.0,1.0]), 0.1)
        ax.plot3D(init_pos[0], init_pos[1], init_pos[2], "r.") # plt figure y axis towards the top, so we switch order
    
    plt.show()

def vis_quadrotor_with_sampling():
    # we only fly forward
    x_min = 0.0
    x_max = 1.0
    y_min = -1.0
    y_max = 1.0
    z_min = -1.0
    z_max = 1.0

    fpl = pyvista.Plotter()
    fpl.add_mesh(pyvista.Arrow([-0.1,0,0], [1,0,0], scale=0.4), color="red")
    fpl.add_mesh(pyvista.Arrow([-0.1,0,0], [0,1,0], scale=0.4), color="green")
    fpl.add_mesh(pyvista.Arrow([-0.1,0,0], [0,0,1], scale=0.4), color="blue")
    
    init_pos = np.array([.0,.0,.0]) # x axis is towards the top
    for x in sample_vel(x_min, x_max, 5):
        for y in sample_vel(y_min, y_max, 5):
            for z in sample_vel(z_min, z_max, 5):
                init_pos = np.array([.0,.0,.0])
                prev_pos = init_pos.copy()
                for _ in range(10):
                    init_pos = quadrotor_model(init_pos, np.array([x,y,z]), 0.1)
                    fpl.add_mesh(pyvista.Sphere(0.025, [prev_pos[0], prev_pos[1], prev_pos[2]]))
                    fpl.add_lines(np.array([[prev_pos[0], prev_pos[1], prev_pos[2]], [init_pos[0], init_pos[1], init_pos[2]]]))
                    prev_pos = init_pos
    
    fpl.show()

if __name__ == "__main__":
    # vis_diff_model()
    vis_quadrotor_with_sampling()