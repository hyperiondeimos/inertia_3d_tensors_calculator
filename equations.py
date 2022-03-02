import numpy as np
import math

class Inertials:
    
    @staticmethod
    def solid_sphere(m, r):
        ixx = (2/5) * m * math.pow(r, 2)
        ixy = 0
        ixz = 0
        iyx = 0
        iyy = (2/5) * m * math.pow(r, 2)
        iyz = 0
        izx = 0
        izy = 0
        izz = (2/5) * m * math.pow(r, 2)
        inertia = np.array([[ixx, ixy, ixz],
                            [iyx, iyy, iyz],                
                            [izx, izy, izz]]                
                                            )
        return inertia
    
    @staticmethod
    def hollow_sphere(m, r):
        ixx = (2/3) * m * math.pow(r, 2)
        ixy = 0
        ixz = 0
        iyx = 0
        iyy = (2/3) * m * math.pow(r, 2)
        iyz = 0
        izx = 0
        izy = 0
        izz = (2/3) * m * math.pow(r, 2)
        inertia = np.array([[ixx, ixy, ixz],
                            [iyx, iyy, iyz],                
                            [izx, izy, izz]]                
                                            )
        return inertia
    
    @staticmethod
    def solid_ellipsoid(m, a, b, c):
        ixx = (1/5) * m * (math.pow(b, 2) + math.pow(c, 2))
        ixy = 0
        ixz = 0
        iyx = 0
        iyy = (1/5) * m * (math.pow(a, 2) + math.pow(c, 2))
        iyz = 0
        izx = 0
        izy = 0
        izz = (1/5) * m * (math.pow(a, 2) + math.pow(b, 2))
        inertia = np.array([[ixx, ixy, ixz],
                            [iyx, iyy, iyz],                
                            [izx, izy, izz]]               
                                            )
        return inertia

    @staticmethod
    def right_circular_cone(m, r, h):
        ixx = ((3/5) * m * math.pow(h, 2)) + ((3/20) * m * math.pow(r, 2))
        ixy = 0
        ixz = 0
        iyx = 0
        iyy = ((3/5) * m * math.pow(h, 2)) + ((3/20) * m * math.pow(r, 2))
        iyz = 0
        izx = 0
        izy = 0
        izz = (3/10) * m * math.pow(r, 2)
        inertia = np.array([[ixx, ixy, ixz],
                            [iyx, iyy, iyz],                
                            [izx, izy, izz]]                
                                            )
        return inertia

    @staticmethod
    def solid_cuboid(m, w, h, d):
        ixx = (1/12) * m * (math.pow(h, 2) + math.pow(d, 2))
        ixy = 0
        ixz = 0
        iyx = 0
        iyy = (1/12) * m * (math.pow(w, 2) + math.pow(d, 2))
        iyz = 0
        izx = 0
        izy = 0
        izz = (1/12) * m * (math.pow(w, 2) + math.pow(h, 2))
        inertia = np.array([[ixx, ixy, ixz],
                            [iyx, iyy, iyz],                
                            [izx, izy, izz]]                
                                            )
        return inertia

    @staticmethod
    def slender_rod_end(m, l):
        ixx = (1/3) * m * math.pow(l, 2)
        ixy = 0
        ixz = 0
        iyx = 0
        iyy = 0
        iyz = 0
        izx = 0
        izy = 0
        izz = (1/3) * m * math.pow(l, 2)
        inertia = np.array([[ixx, ixy, ixz],
                            [iyx, iyy, iyz],                
                            [izx, izy, izz]]                
                                            )
        return inertia

    @staticmethod
    def slender_rod_center(m, l):
        ixx = (1/12) * m * math.pow(l, 2)
        ixy = 0
        ixz = 0
        iyx = 0
        iyy = 0
        iyz = 0
        izx = 0
        izy = 0
        izz = (1/12) * m * math.pow(l, 2)
        inertia = np.array([[ixx, ixy, ixz],
                            [iyx, iyy, iyz],                
                            [izx, izy, izz]]                
                                            )
        return inertia

    @staticmethod
    def solid_cylinder(m, h, r):
        ixx = (1/12) * m * (3 * math.pow(r, 2) + math.pow(h, 2))
        ixy = 0
        ixz = 0
        iyx = 0
        iyy = (1/12) * m * (3 * math.pow(r, 2) + math.pow(h, 2))
        iyz = 0
        izx = 0
        izy = 0
        izz = (1/2) * m * math.pow(r, 2)
        inertia = np.array([[ixx, ixy, ixz],
                            [iyx, iyy, iyz],                
                            [izx, izy, izz]]                
                                            )
        return inertia

    @staticmethod
    def thick_walled_tube(m, r1, r2, h):
        ixx = (1/12) * m * (3 * (math.pow(r2, 2) + math.pow(r1, 2)) + math.pow(h, 2))
        ixy = 0
        ixz = 0
        iyx = 0
        iyy = (1/12) * m * (3 * (math.pow(r2, 2) + math.pow(r1, 2)) + math.pow(h, 2))
        iyz = 0
        izx = 0
        izy = 0
        izz = (1/2) * m * (math.pow(r2, 2) + math.pow(r1, 2))
        inertia = np.array([[ixx, ixy, ixz],
                            [iyx, iyy, iyz],               
                            [izx, izy, izz]]                
                                            )
        return inertia
