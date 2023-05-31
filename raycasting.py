import math

def scaling_factor(slope):
    return math.sqrt(1 + (slope ** 2))

def DDA(dx, dy, current_pos, map, tile_size):
    if dx == 0:
        dx = 1e-30
    if dy == 0:
        dy = 1e-30

    scaling_x = scaling_factor(dy/dx)
    scaling_y = scaling_factor(dx/dy)

    current_point = current_pos
    current_tile = (current_pos[0] // tile_size, current_pos[1] // tile_size)

    A_x = current_point[0] - ((current_point[0] // tile_size) * tile_size)
    A_y = current_point[1] - ((current_point[1] // tile_size) * tile_size)

    if dx > 0:
        A_x = tile_size - A_x
    if dy > 0:
        A_y = tile_size - A_y

    step_x = A_x * scaling_x
    step_y = A_y * scaling_y
    
    x_length = step_x
    y_length = step_y

    x_point = (current_point[0] + (dx/abs(dx) * A_x), current_point[1] + (abs(dy/dx) * A_x * (dy / abs(dy))))
    y_point = (current_point[0] + (abs(dx/dy) * A_y * (dx/ abs(dx))), current_point[1] + (dy/abs(dy) * A_y))
    
    if x_length < y_length:
        current_point = x_point
        current_tile = (current_tile[0] + int((dx / abs(dx))), current_tile[1])
    else:
        current_point = y_point
        current_tile = (current_tile[0], current_tile[1] + int((dy/abs(dy))))
    
    if current_tile[0] < 0 or current_tile[0] > len(map[0]) - 1:
        return current_point
    if current_tile[1] < 0 or current_tile[1] > len(map) - 1:
        return current_point
    while not map[int(current_tile[1])][int(current_tile[0])]:
        if x_length < y_length:
            x_length += scaling_x * tile_size
            x_point = (x_point[0] + (dx/abs(dx) * tile_size), x_point[1] + (abs(dy/dx) * tile_size * (dy / abs(dy))))
        else:
            y_length += scaling_y * tile_size
            y_point = (y_point[0] + (abs(dx/dy) * tile_size * (dx/ abs(dx))), y_point[1] + (dy/abs(dy) * tile_size))

        if x_length < y_length:
            current_point = x_point
            current_tile = (current_tile[0] + int((dx / abs(dx))), current_tile[1])
        else:
            current_point = y_point 
            current_tile = (current_tile[0], current_tile[1] + int((dy/abs(dy))))

        if current_tile[0] < 0 or current_tile[0] > len(map[0]) - 1:
            break
        if current_tile[1] < 0 or current_tile[1] > len(map) - 1:
            break
    return current_point