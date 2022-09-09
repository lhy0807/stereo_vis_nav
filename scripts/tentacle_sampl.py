# created by Hongyu Li at 20220905 23:37.
# 
# https://lhy.xyz

import numpy as np

def diff_model(init_pos: np.ndarray, lat_vel: float, ang_vel: float, dt: float):
    '''
    calculate kinematics for differential drive model
    init_pos: initial position before this move defined by [x y theta]
    lat_vel: lateral velocity (m/s)
    ang_vel: angular velocity (rad/s)
    dt: time step, for example 0.1s
    '''
    final_pos = init_pos.copy().astype(float)
    final_pos[2] += ang_vel * dt
    final_pos[0] += lat_vel * np.cos(final_pos[2]) * dt
    final_pos[1] += lat_vel * np.sin(final_pos[2]) * dt

    return final_pos

def quadrotor_model(init_pos: np.ndarray, lat_vel: np.ndarray, dt:float):
    '''
    calculate displacement, ignoring roll, pitch, yaw
    '''
    final_pos = init_pos.copy().astype(float)
    return final_pos + lat_vel*dt 

def sample_vel(min_vel: float, max_vel: float, n_count:int):
    '''
    sample velocity evenly
    This can be either lateral vel or angular vel
    '''
    return np.linspace(min_vel, max_vel, n_count)