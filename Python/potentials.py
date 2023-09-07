import math


def u(pos):
    return 0.5 * pos ** 2 + 0.25 * pos ** 4


def u2(pos):
    return 0.5 * pos ** 2


def u4(pos):
    return 0.25 * pos ** 4


def u_bound(pos):
    floor = math.floor(abs(pos))
    ceiling = math.ceil(abs(pos))
    u_floor = 0
    for n in range(floor + 1):
        u_floor += n + n ** 3
    u_ceiling = u_floor + ceiling + ceiling ** 3
    u_pos = u_floor
    if floor != abs(pos):
        m = (u_ceiling - u_floor) / (ceiling - floor)
        u_pos = m * (abs(pos) - floor) + u_floor
    return u_pos


def u_bound2(pos):
    floor = math.floor(abs(pos))
    ceiling = math.ceil(abs(pos))
    u_floor = 0
    for n in range(floor + 1):
        u_floor += n
    u_ceiling = u_floor + ceiling
    u_pos = u_floor
    if floor != abs(pos):
        m = (u_ceiling - u_floor) / (ceiling - floor)
        u_pos = m * (abs(pos) - floor) + u_floor
    return u_pos


def u_bound4(pos):
    floor = math.floor(abs(pos))
    ceiling = math.ceil(abs(pos))
    u_floor = 0
    for n in range(floor + 1):
        u_floor += n ** 3
    u_ceiling = u_floor + ceiling ** 3
    u_pos = u_floor
    if floor != abs(pos):
        m = (u_ceiling - u_floor) / (ceiling - floor)
        u_pos = m * (abs(pos) - floor) + u_floor
    return u_pos
