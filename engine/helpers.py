import math
import pygame
DEGTORAD = 0.017453

class Helpers(object):
    def __init__(self):
        pass

    @staticmethod
    def super_isinstance(i, cls):
        mro = i.__class__.__mro__
        thisclass = i.__thisclass__
        return cls in mro and mro.index(thisclass) < mro.index(cls)

    @staticmethod
    def is_colliding(x1,y1,w1,h1,x2,y2,w2,h2):
        r1 = pygame.Rect(x1,y1,w1,h1)
        r2 = pygame.Rect(x2,y2,w2,h2)
        return r1.colliderect(r2)


    @staticmethod
    def distance_between_two_points(x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    @staticmethod
    def get_target_point_from_point_angle_distance(x1,y1,angle , distance):
        x2 = x1 + distance * math.cos(angle)
        y2 = y1 + distance * math.sin(angle)

        return x2,y2

    @staticmethod
    def move_with_angle(alpha,dt):
        dx = math.cos(alpha * DEGTORAD) * 0.2 * dt
        dy = math.sin(alpha * DEGTORAD) * 0.2 * dt
        factor = 100

        return abs(dx)*factor, abs(dy)* factor

    @staticmethod
    def get_slope_between_two_points(x1,y1,x2,y2):
        if x2 == x1:
            return y2-y1
        return (y2-y1)/(x2-x1)

    @staticmethod
    def find_angle_from_slope(m):
        return math.atan(m)

    @staticmethod
    def move_between_two_points(x1,y1,x2,y2, dt):
        slope = Helpers.get_slope_between_two_points(x1, y1, x2, y2)
        angle = Helpers.find_angle_from_slope(slope)
        dx,dy = Helpers.move_with_angle(angle,dt)

        return dx,dy

    @staticmethod
    def get_direction_between_two_points(x1,y1,x2,y2, old_direction):
        direction = old_direction
        if x1 == x2 and y1 == y2:
            direction = old_direction
        elif x1 == x2 and y1 > y2:
            direction = 2
        elif x1 < x2 and y1 > y2:
            direction = 3
        elif x2 > x1 and y1 == y2:
            direction = 4
        elif x1 < x2 and y1 < y2:
            direction = 5
        elif x1 == x2 and y1 < y2:
            direction = 6
        elif x1 > x2 and y1 > y2:
            direction = 7
        elif x1 < x2 and y1 == y2:
            direction = 0
        elif x1< x2 and y1 < y2:
            direction = 1
        return direction



    @staticmethod
    def linear_move_between_two_points(x1,y1,x2,y2, dt,speed_x , speed_y):
        dx = 0
        if x2 > x1:
            dx = speed_x
        elif x1 > x2:
            dx = -speed_x

        dy = 0
        if y2 > y1:
            dy = speed_y
        elif y1 > y2:
            dy = -speed_y


        return dx * dt ,dy * dt

    @staticmethod
    def get_angle_between_two_points(x1,y1,x2,y2):
        slope = Helpers.get_slope_between_two_points(x1,y1,x2,y2)
        alpha = Helpers.find_angle_from_slope(slope)
        return alpha


    @staticmethod
    def intersects(rect, r, center):
        circle_distance_x = abs(center[0] - rect.centerx)
        circle_distance_y = abs(center[1] - rect.centery)
        if circle_distance_x > rect.w / 2.0 + r or circle_distance_y > rect.h / 2.0 + r:
            return False
        if circle_distance_x <= rect.w / 2.0 or circle_distance_y <= rect.h / 2.0:
            return True
        corner_x = circle_distance_x - rect.w / 2.0
        corner_y = circle_distance_y - rect.h / 2.0
        corner_distance_sq = corner_x ** 2.0 + corner_y ** 2.0
        return corner_distance_sq <= r ** 2.0