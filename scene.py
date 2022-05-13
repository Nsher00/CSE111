# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_grid(canvas, scene_width, scene_height, 50)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_grid(canvas, width, height, interval):

    for x in range(0, width, interval):
        label_y = 15
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

    for y in range(0, height, interval):
        label_x = 15
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{x}")



# Define your functions such as
# draw_sky and draw_ground here.



# Call the main function so that
# this program will start executing.
main()