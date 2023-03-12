import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf

tf.compat.v1.disable_eager_execution()

def plt_basic_object (points) :
     
     """" Plots a basic object, assuming its convex and not too complex"""

     tri = Delaunay (points).convex_hull

     fig = plt.figure (figsize = (8, 8))
     ax = fig.add_subplot (111, projection = '3d')
     S = ax.plot_trisurf (points [:,0], points [:,1], points [:,2], 
                            triangles = tri,
                            shade = True, cmap = cm.rainbow  , lw = 0.5)

     ax.set_xlim3d (-15,15)
     ax.set_ylim3d (-15,15)
     ax.set_zlim3d (-15,15)

     plt.show()

def _pyramid_(bottom_lower=(0, 0, 0), side_length=5, height=5): 

    """Create a pyramid starting from the given bottom-center point (x,y,z)"""
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([bottom_lower + [0, 0, 0], 
                        bottom_lower + [side_length, 0, 0], 
                        bottom_lower + [side_length, side_length, 0], 
                        bottom_lower + [0, side_length, 0], 
                        bottom_lower + [side_length/2, side_length/2, height]])

    return points

init_pyramid_ = _pyramid_(side_length=3, height=3) 
points = tf.constant(init_pyramid_, dtype=tf.float32)

plt_basic_object (init_pyramid_)

def translate_obj (points, amount): # pyramid translation
    return tf.add (points, amount)

translation_amount = tf.constant ([1,2,10], dtype=tf.float32)
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
     translated_pyramid = session.run (translated_object)

plt_basic_object (translated_pyramid)


# NEXT OBJECT


def cube (bottom_lower = (0,0,0,), side_length = 5):
     
     """ Create cube starting from the given bottom-lower point (lowest x,y,z values)"""
     bottom_lower = np.array (bottom_lower)

     points = np.vstack ([
          bottom_lower,
          bottom_lower + [0, side_length, 0],
          bottom_lower + [side_length, side_length, 0],
          bottom_lower + [side_length, 0, 0],
          bottom_lower + [0,0,side_length],
          bottom_lower + [0, side_length, side_length],
          bottom_lower + [side_length, side_length, side_length],
          bottom_lower + [side_length, 0, side_length],
          bottom_lower,
     ])

     return points

init_cube_ = cube (side_length=3)
points = tf.constant (init_cube_, dtype = tf.float32)

plt_basic_object (init_cube_)

def translate_obj (points, amount):
     return tf.add (points, amount)

translation_amount = tf.constant ([5,7,-8], dtype=tf.float32)
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
     translated_cube = session.run (translated_object)

plt_basic_object (translated_cube)


# NEXT OBJECT


def octahedron(bottom_lower=(0,0,0,), side_length=5):

    """ Create octahedron starting from the given bottom-lower point (lowest x,y,z values)"""
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower + [0, 0, side_length/2],
        bottom_lower + [0, side_length/2, 0],
        bottom_lower + [side_length/2, 0, 0],
        bottom_lower + [0, -side_length/2, 0],
        bottom_lower + [-side_length/2, 0, 0],
        bottom_lower + [0, 0, -side_length/2],
    ])

    return points

init_octahedron_ = octahedron (side_length=3)
points = tf.constant (init_octahedron_, dtype = tf.float32)

plt_basic_object (init_octahedron_)

def translate_obj (points, amount): # octahedron translation
    return tf.add (points, amount)

translation_amount = tf.constant ([-5,8,10], dtype=tf.float32)
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
     translated_octahedron = session.run (translated_object)

plt_basic_object (translated_octahedron)


# NEXT OBJECT


def hexagonal_prism(bottom_lower=(0,0,0,), side_length=5, height=5):

    """Create hexagonal prism starting from the given bottom-lower point (lowest x,y,z values)"""
    bottom_lower = np.array(bottom_lower)

    a = side_length/2
    b = np.sqrt(3)*side_length/2
    h = height

    points = np.vstack([
        bottom_lower + [a, 0, 0],
        bottom_lower + [a/2, b/2, 0],
        bottom_lower + [-a/2, b/2, 0],
        bottom_lower + [-a, 0, 0],
        bottom_lower + [-a/2, -b/2, 0],
        bottom_lower + [a/2, -b/2, 0],
        bottom_lower + [a, 0, h],
        bottom_lower + [a/2, b/2, h],
        bottom_lower + [-a/2, b/2, h],
        bottom_lower + [-a, 0, h],
        bottom_lower + [-a/2, -b/2, h],
        bottom_lower + [a/2, -b/2, h]
    ])

    return points

init_hexagonal_prism_ = hexagonal_prism (side_length=3)
points = tf.constant (init_hexagonal_prism_, dtype = tf.float32)

plt_basic_object (init_hexagonal_prism_)

def translate_obj (points, amount): # hexagonal_prism translation
    return tf.add (points, amount)

translation_amount = tf.constant ([-10,8,11], dtype=tf.float32)
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
     translated_hexagonal_prism = session.run (translated_object)

plt_basic_object (translated_hexagonal_prism)