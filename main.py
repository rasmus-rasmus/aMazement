from window import *
from drawables import *
from maze import *

def main():
    win = Window(1600, 1600)
    num_cols = 25
    num_rows = 25
    maze = Maze(50, 50, num_rows, num_cols, 50, 50, win)
    maze.create_cells()
    win.wait_for_close()
    
    
    
if __name__ == "__main__":
    main()