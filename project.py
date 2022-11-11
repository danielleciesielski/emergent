import tkinter
import random
import time

GRID_DIM = 100
CANVAS_SIZE = GRID_DIM * 10
SIZE = CANVAS_SIZE / GRID_DIM

def make_canvas(width, height, title = None):
    """
    Creates and returns a drawing canvas
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width = width, height = height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width = width, height = height)
    canvas.pack()
    return canvas

def draw_square(canvas, row, col, color):
    x = col * SIZE
    y = row * SIZE
    canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill = color)

def initialize_ant(GRID_DIM):
    border_width = GRID_DIM // 3
    init_row = random.randint(border_width, 2*border_width)
    init_col = random.randint(border_width, 2*border_width)
    init_dir = random.randint(0,3)
    return [init_row, init_col, init_dir]

def find_coords(location):
    if location[2] == 0: # 12 o'clock
        points = [
            location[1] * SIZE,
            location[0] * SIZE + SIZE,
            location[1] * SIZE + SIZE,
            location[0] * SIZE + SIZE,
            location[1] * SIZE + SIZE / 2,
            location[0] * SIZE
        ]
    elif location[2] == 1: # 3 o'clock
        points = [
            location[1] * SIZE,
            location[0] * SIZE,
            location[1] * SIZE,
            location[0] * SIZE + SIZE,
            location[1] * SIZE + SIZE,
            location[0] * SIZE + SIZE / 2
        ]
    elif location[2] == 2: # 6 o'clock
        points = [
            location[1] * SIZE,
            location[0] * SIZE,
            location[1] * SIZE + SIZE,
            location[0] * SIZE,
            location[1] * SIZE + SIZE / 2,
            location[0] * SIZE + SIZE
        ]
    else: # 9 o'clock
        points = [
            location[1] * SIZE + SIZE,
            location[0] * SIZE + SIZE,
            location[1] * SIZE + SIZE,
            location[0] * SIZE,
            location[1] * SIZE,
            location[0] * SIZE + SIZE / 2
        ]
    return points

def move_ant(ant, ant_tracker):
    if ant_tracker[ant[0]][ant[1]] == 'b':
        ant[2] = (ant[2] + 1) % 4
    else:
        ant[2] = (ant[2] - 1) % 4
    if ant[2] == 0:
        ant[0] = ant[0] - 1
        ant[1] = ant[1]
    elif ant[2] == 1:
        ant[0] = ant[0]
        ant[1] = ant[1] + 1
    elif ant[2] == 2:
        ant[0] = ant[0] + 1
        ant[1] = ant[1]
    else:
        ant[0] = ant[0]
        ant[1] = ant[1] - 1
    return ant


def main():
    ant_tracker = [['w' for x in range(GRID_DIM)] for y in range(GRID_DIM)]
    ant = initialize_ant(GRID_DIM)
    coords = find_coords(ant)
    canvas = make_canvas(CANVAS_SIZE, CANVAS_SIZE, "Langton's Ant")
    for row in range(GRID_DIM):
        for col in range(GRID_DIM):
            draw_square(canvas, row, col, 'white')
    canvas.create_polygon(coords, fill = 'magenta', width = 3)
    canvas.update()
    time.sleep(1/50)
    count = 1
    while ant[0] != -1 and ant[0] != GRID_DIM and ant[1] != -1 and ant[1] != GRID_DIM:
        if ant_tracker[ant[0]][ant[1]] == 'w':
            draw_square(canvas, ant[0], ant[1], 'black')
            ant_tracker[ant[0]][ant[1]] = 'b'
        else:
            draw_square(canvas, ant[0], ant[1], 'white')
            ant_tracker[ant[0]][ant[1]] = 'w'
        ant = move_ant(ant, ant_tracker)
        coords = find_coords(ant)
        canvas.create_polygon(coords, fill = 'magenta', width = 3)
        canvas.update()
        time.sleep(1/50)
        count += 1
    message = "The ant fell off the edge after " + str(count) + " steps!"
    tkinter.messagebox.showinfo("Oops!", message)
    canvas.mainloop()

if __name__ == '__main__':
    main()