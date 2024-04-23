import numpy as np
import sympy as sp

def rotate_x(theta):
    cos_theta = sp.cos(theta)
    sin_theta = sp.sin(theta)
    rot_matrix_x = sp.Matrix([[1, 0, 0, 0],
                              [0, cos_theta, -sin_theta, 0],
                              [0, sin_theta, cos_theta, 0],
                              [0, 0, 0, 1]])
    return rot_matrix_x

def rotate_y(theta):
    cos_theta = sp.cos(theta)
    sin_theta = sp.sin(theta)
    rot_matrix_y = sp.Matrix([[cos_theta, 0, sin_theta, 0],
                              [0, 1, 0, 0],
                              [-sin_theta, 0, cos_theta, 0],
                              [0, 0, 0, 1]])
    return rot_matrix_y

def rotate_z(theta):
    cos_theta = sp.cos(theta)
    sin_theta = sp.sin(theta)
    rot_matrix_z = sp.Matrix([[cos_theta, -sin_theta, 0, 0],
                              [sin_theta, cos_theta, 0, 0],
                              [0, 0, 1, 0],
                              [0, 0, 0, 1]])
    return rot_matrix_z

def translate_x(dx):
    translation_matrix_x = sp.Matrix([[1, 0, 0, dx],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [0, 0, 0, 1]])
    return translation_matrix_x

def translate_y(dy):
    translation_matrix_y = sp.Matrix([[1, 0, 0, 0],
                                      [0, 1, 0, dy],
                                      [0, 0, 1, 0],
                                      [0, 0, 0, 1]])
    return translation_matrix_y

def translate_z(dz):
    translation_matrix_z = sp.Matrix([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, dz],
                                      [0, 0, 0, 1]])
    return translation_matrix_z


import sympy as sp

theta1, theta2, theta3, theta4, theta5, theta6, l1, l2, l3, l4, l5, l6, pi = sp.symbols('theta1 theta2 theta3 theta4 theta5 theta6 l1 l2 l3 l4 l5 l6 pi')


T_01 = rotate_z(theta1) * translate_z(l1) * rotate_z(pi/2) * rotate_x(pi/2)
T_12 = rotate_z(theta2) * translate_x(l2)
T_23 = rotate_z(theta3) * translate_x(l3) * rotate_y(pi/2) * rotate_z(pi/2)

T_01*T_12*T_23