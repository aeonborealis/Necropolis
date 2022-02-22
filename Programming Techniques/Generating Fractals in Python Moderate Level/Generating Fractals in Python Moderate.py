# Python Code for Generating Basic Fractals 

# Koch Snowflake

import turtle
            x_offset = -(width / 2 - margin) + min_x * length
        else:
            x_offset = -(width / 2) + (width - width_ * length) / 2 + min_x * length
    
    if y_offset is None:
        if height_ >= width_ and (height - height_) <= height_ - 2 * margin :
            y_offset = -(height / 2 - margin) + min_y * length
        else:
            y_offset = -(height / 2) + (height - height_ * length) / 2 + min_y * length

    if inverted:
        inst = inst.replace('+', '$')
        inst = inst.replace('-', '+')
        inst = inst.replace('$', '-')
        inst = inst.replace('F', '$')
        inst = inst.replace('B', 'F')
        inst = inst.replace('$', 'B')
    
    if flip_h:
        inst = inst.replace('F', '$')
        inst = inst.replace('B', 'F')
        inst = inst.replace('$', 'B')
        y_offset *= -1

    if flip_v:
        inst = inst.replace('+', '$')
        inst = inst.replace('-', '+')
        inst = inst.replace('$', '-')
        y_offset *= -1

    if size is None:
        if length < 3:
            size = 1
        elif length < 12:
            size = 2
        elif length < 25:
            size = 3
        else:            
            size = 5

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()    
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    
    wn.exitonclick()

# Global parameters

width = 450

title = "Koch-Snowflake" 
axiom = "F--F--F"
rules = {"F":"F+F--F+F"}
iterations = 3 # TOP: 7
angle = 60

main(iterations, axiom, rules, angle, aspect_ratio=1, width=width)


# Drawing Levy-C-Curve with Python and Turtle

import turtle
from math import cos, sin, radians

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

def draw_l_system(t, instructions, angle, distance):
    steps = len([i for i in instructions if i in "FB"])
    step = 1 / steps
    i = 0
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == 'B':
            t.backward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

def calc_length_height(instructions, angle, correction_angle):
    current_angle = correction_angle
    x_offset = 0
    y_offset = 0
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for inst in instructions:
        if inst == "F":
            x_offset += cos(radians(current_angle))
            y_offset += sin(radians(current_angle))
        elif inst == "B":
            x_offset -= cos(radians(current_angle))
            y_offset -= sin(radians(current_angle))
        elif inst == "+":
            current_angle -= angle
        elif inst == "-":
            current_angle += angle
        max_x = max(max_x, x_offset)
        min_x = min(min_x, x_offset)
        max_y = max(max_y, y_offset)
        min_y = min(min_y, y_offset)
    
    width = abs(max_x) + abs(min_x)
    height = abs(max_y) + abs(min_y)


    return width, height, abs(min_x), abs(min_y)

def main(iterations, axiom, rules, angle, length=None, size=None, correction_angle=0,
        y_offset=None, x_offset=None, offset_angle=None, inverted=False, flip_h=False, 
        flip_v=False, width=None, height=None, margin=None, aspect_ratio=None):

    inst = create_l_system(iterations, axiom, rules)

    width_, height_, min_x, min_y = calc_length_height(inst, angle, correction_angle)

    if width_ == 0 and height_ == 0:
        return

    if aspect_ratio is None:
        if 0 in [width_, height_]:
            aspect_ratio = 1
        else:
            aspect_ratio = width_ / height_

    if width is None and height:
        width = height / aspect_ratio

    if height is None and width:
        height = width / aspect_ratio
    
    if margin is None:
        margin = 35

    if offset_angle is None:
        offset_angle = -90

    if length is None:
        if width_ > height_:
            length = (width - 2 * margin) / width_
        else:
            length = (height - 2 * margin) / height_
    
    if width_ * length > width:
        length = (width - 2 * margin) / width_
    elif height_ * length > height:
        length = (height - 2 * margin) / height_
    
    if x_offset is None:
        if width_ >= height_  and (width - width_) <= width_ - 2 * margin :
            x_offset = -(width / 2 - margin) + min_x * length
        else:
            x_offset = -(width / 2) + (width - width_ * length) / 2 + min_x * length
    
    if y_offset is None:
        if height_ >= width_ and (height - height_) <= height_ - 2 * margin :
            y_offset = -(height / 2 - margin) + min_y * length
        else:
            y_offset = -(height / 2) + (height - height_ * length) / 2 + min_y * length

    if inverted:
        inst = inst.replace('+', '$')
        inst = inst.replace('-', '+')
        inst = inst.replace('$', '-')
        inst = inst.replace('F', '$')
        inst = inst.replace('B', 'F')
        inst = inst.replace('$', 'B')
    
    if flip_h:
        inst = inst.replace('F', '$')
        inst = inst.replace('B', 'F')
        inst = inst.replace('$', 'B')
        y_offset *= -1

    if flip_v:
        inst = inst.replace('+', '$')
        inst = inst.replace('-', '+')
        inst = inst.replace('$', '-')
        y_offset *= -1

    if size is None:
        if length < 3:
            size = 1
        elif length < 12:
            size = 2
        elif length < 25:
            size = 3
        else:            
            size = 5

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()    
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    
    wn.exitonclick()

# Global parameters

width = 450

title = "Levy-C-Curve" 
axiom = "F"
rules = {"F":"+F--F+"}
iterations = 7 # TOP: 16
angle = 45

main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, height=width)

# Krishna's Anklets 

import turtle
from math import cos, sin, radians

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

def draw_l_system(t, instructions, angle, distance):
    steps = len([i for i in instructions if i in "FB"])
    step = 1 / steps
    i = 0
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == 'B':
            t.backward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

def calc_length_height(instructions, angle, correction_angle):
    current_angle = correction_angle
    x_offset = 0
    y_offset = 0
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for inst in instructions:
        if inst == "F":
            x_offset += cos(radians(current_angle))
            y_offset += sin(radians(current_angle))
        elif inst == "B":
            x_offset -= cos(radians(current_angle))
            y_offset -= sin(radians(current_angle))
        elif inst == "+":
            current_angle -= angle
        elif inst == "-":
            current_angle += angle
        max_x = max(max_x, x_offset)
        min_x = min(min_x, x_offset)
        max_y = max(max_y, y_offset)
        min_y = min(min_y, y_offset)
    
    width = abs(max_x) + abs(min_x)
    height = abs(max_y) + abs(min_y)


    return width, height, abs(min_x), abs(min_y)

def main(iterations, axiom, rules, angle, length=None, size=None, correction_angle=0,
        y_offset=None, x_offset=None, offset_angle=None, inverted=False, flip_h=False, 
        flip_v=False, width=None, height=None, margin=None, aspect_ratio=None):

    inst = create_l_system(iterations, axiom, rules)

    width_, height_, min_x, min_y = calc_length_height(inst, angle, correction_angle)

    if width_ == 0 and height_ == 0:
        return

    if aspect_ratio is None:
        if 0 in [width_, height_]:
            aspect_ratio = 1
        else:
            aspect_ratio = width_ / height_

    if width is None and height:
        width = height / aspect_ratio

    if height is None and width:
        height = width / aspect_ratio
    
    if margin is None:
        margin = 35

    if offset_angle is None:
        offset_angle = -90

    if length is None:
        if width_ > height_:
            length = (width - 2 * margin) / width_
        else:
            length = (height - 2 * margin) / height_
    
    if width_ * length > width:
        length = (width - 2 * margin) / width_
    elif height_ * length > height:
        length = (height - 2 * margin) / height_
    
    if x_offset is None:
        if width_ >= height_  and (width - width_) <= width_ - 2 * margin :
            x_offset = -(width / 2 - margin) + min_x * length
        else:
            x_offset = -(width / 2) + (width - width_ * length) / 2 + min_x * length
    
    if y_offset is None:
        if height_ >= width_ and (height - height_) <= height_ - 2 * margin :
            y_offset = -(height / 2 - margin) + min_y * length
        else:
            y_offset = -(height / 2) + (height - height_ * length) / 2 + min_y * length

    if inverted:
        inst = inst.replace('+', '$')
        inst = inst.replace('-', '+')
        inst = inst.replace('$', '-')
        inst = inst.replace('F', '$')
        inst = inst.replace('B', 'F')
        inst = inst.replace('$', 'B')
    
    if flip_h:
        inst = inst.replace('F', '$')
        inst = inst.replace('B', 'F')
        inst = inst.replace('$', 'B')
        y_offset *= -1

    if flip_v:
        inst = inst.replace('+', '$')
        inst = inst.replace('-', '+')
        inst = inst.replace('$', '-')
        y_offset *= -1

    if size is None:
        if length < 3:
            size = 1
        elif length < 12:
            size = 2
        elif length < 25:
            size = 3
        else:            
            size = 5

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()    
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    
    wn.exitonclick()

# Global parameters

width = 450

title = "Krishna-Anklets"
axiom = " -X--X"
rules = {"X":"XFX--XFX"}
iterations = 3 # TOP: 9
angle = 45

main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, flip_v=True)

# Peano Gosper Curve 

import turtle
from math import cos, sin, radians

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

def draw_l_system(t, instructions, angle, distance):
    steps = len([i for i in instructions if i in "FB"])
    step = 1 / steps
    i = 0
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == 'B':
            t.backward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

def calc_length_height(instructions, angle, correction_angle):
    current_angle = correction_angle
    x_offset = 0
    y_offset = 0
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for inst in instructions:
        if inst == "F":
            x_offset += cos(radians(current_angle))
            y_offset += sin(radians(current_angle))
        elif inst == "B":
            x_offset -= cos(radians(current_angle))
            y_offset -= sin(radians(current_angle))
        elif inst == "+":
            current_angle -= angle
        elif inst == "-":
            current_angle += angle
        max_x = max(max_x, x_offset)
        min_x = min(min_x, x_offset)
        max_y = max(max_y, y_offset)
        min_y = min(min_y, y_offset)
    
    width = abs(max_x) + abs(min_x)
    height = abs(max_y) + abs(min_y)


    return width, height, abs(min_x), abs(min_y)

def main(iterations, axiom, rules, angle, length=None, size=None, correction_angle=0,
        y_offset=None, x_offset=None, offset_angle=None, inverted=False, flip_h=False, 
        flip_v=False, width=None, height=None, margin=None, aspect_ratio=None):

    inst = create_l_system(iterations, axiom, rules)

    width_, height_, min_x, min_y = calc_length_height(inst, angle, correction_angle)

    if width_ == 0 and height_ == 0:
        return

    if aspect_ratio is None:
        if 0 in [width_, height_]:
            aspect_ratio = 1
        else:
            aspect_ratio = width_ / height_

    if width is None and height:
        width = height / aspect_ratio

    if height is None and width:
        height = width / aspect_ratio
    
    if margin is None:
        margin = 35

    if offset_angle is None:
        offset_angle = -90

    if length is None:
        if width_ > height_:
            length = (width - 2 * margin) / width_
        else:
            length = (height - 2 * margin) / height_
    
    if width_ * length > width:
        length = (width - 2 * margin) / width_
    elif height_ * length > height:
        length = (height - 2 * margin) / height_
    
    if x_offset is None:
        if width_ >= height_  and (width - width_) <= width_ - 2 * margin :
            x_offset = -(width / 2 - margin) + min_x * length
        else:
            x_offset = -(width / 2) + (width - width_ * length) / 2 + min_x * length
    
    if y_offset is None:
        if height_ >= width_ and (height - height_) <= height_ - 2 * margin :
            y_offset = -(height / 2 - margin) + min_y * length
        else:
            y_offset = -(height / 2) + (height - height_ * length) / 2 + min_y * length

    if inverted:
        inst = inst.replace('+', '$')
        inst = inst.replace('-', '+')
        inst = inst.replace('$', '-')
        inst = inst.replace('F', '$')
        inst = inst.replace('B', 'F')
        inst = inst.replace('$', 'B')
    
    if flip_h:
        inst = inst.replace('F', '$')
        inst = inst.replace('B', 'F')
        inst = inst.replace('$', 'B')
        y_offset *= -1

    if flip_v:
        inst = inst.replace('+', '$')
        inst = inst.replace('-', '+')
        inst = inst.replace('$', '-')
        y_offset *= -1

    if size is None:
        if length < 3:
            size = 1
        elif length < 12:
            size = 2
        elif length < 25:
            size = 3
        else:            
            size = 5

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()    
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    
    wn.exitonclick()

# Global parameters

width = 450

title = "Peano-Gosper-Curve" 
axiom = "FX"
rules = {"X":"X+YF++YF-FX--FXFX-YF+", "Y":"-FX+YFYF++YF+FX--FX-Y"}
iterations = 3 # TOP: 6
angle = 60

offset_angle = -90 + 15 * iterations
correction_angle = 15 * iterations

main(iterations, axiom, rules, angle, correction_angle=correction_angle, 
    offset_angle=offset_angle, aspect_ratio=1, width=width)

# Dragon Curve

import turtle
from math import cos, sin, radians

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

def draw_l_system(t, instructions, angle, distance):
    steps = len([i for i in instructions if i in "FB"])
    step = 1 / steps
    i = 0
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == 'B':
            t.backward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

def calc_length_height(instructions, angle, correction_angle):
    current_angle = correction_angle
    x_offset = 0
    y_offset = 0
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for inst in instructions:
        if inst == "F":
            x_offset += cos(radians(current_angle))
            y_offset += sin(radians(current_angle))
        elif inst == "B":
            x_offset -= cos(radians(current_angle))
            y_offset -= sin(radians(current_angle))
        elif inst == "+":
            current_angle -= angle
        elif inst == "-":
            current_angle += angle
        max_x = max(max_x, x_offset)
        min_x = min(min_x, x_offset)
        max_y = max(max_y, y_offset)
        min_y = min(min_y, y_offset)
    
    width = abs(max_x) + abs(min_x)
    height = abs(max_y) + abs(min_y)


    return width, height, abs(min_x), abs(min_y)

def main(iterations, axiom, rules, angle, length=None, size=None, correction_angle=0,
        y_offset=None, x_offset=None, offset_angle=None, inverted=False, flip_h=False, 
        flip_v=False, width=None, height=None, margin=None, aspect_ratio=None):

    inst = create_l_system(iterations, axiom, rules)

    width_, height_, min_x, min_y = calc_length_height(inst, angle, correction_angle)

    if width_ == 0 and height_ == 0:
        return

    if aspect_ratio is None:
        if 0 in [width_, height_]:
            aspect_ratio = 1
        else:
            aspect_ratio = width_ / height_

    if width is None and height:
        width = height / aspect_ratio

    if height is None and width:
        height = width / aspect_ratio
    
    if margin is None:
        margin = 35

    if offset_angle is None:
        offset_angle = -90

    if length is None:
        if width_ > height_:
            length = (width - 2 * margin) / width_
        else:
            length = (height - 2 * margin) / height_
    
    if width_ * length > width:
        length = (width - 2 * margin) / width_
    elif height_ * length > height:
        length = (height - 2 * margin) / height_
    
    if x_offset is None:
        if width_ >= height_  and (width - width_) <= width_ - 2 * margin :
            x_offset = -(width / 2 - margin) + min_x * length
        else:
            x_offset = -(width / 2) + (width - width_ * length) / 2 + min_x * length
    
    if y_offset is None:
        if height_ >= width_ and (height - height_) <= height_ - 2 * margin :
            y_offset = -(height / 2 - margin) + min_y * length
        else:
            y_offset = -(height / 2) + (height - height_ * length) / 2 + min_y * length

    if inverted:
        inst = inst.replace('+', '$')
        inst = inst.replace('-', '+')
        inst = inst.replace('$', '-')
        inst = inst.replace('F', '$')
        inst = inst.replace('B', 'F')
        inst = inst.replace('$', 'B')
    
    if flip_h:
        inst = inst.replace('F', '$')
        inst = inst.replace('B', 'F')
        inst = inst.replace('$', 'B')
        y_offset *= -1

    if flip_v:
        inst = inst.replace('+', '$')
        inst = inst.replace('-', '+')
        inst = inst.replace('$', '-')
        y_offset *= -1

    if size is None:
        if length < 3:
            size = 1
        elif length < 12:
            size = 2
        elif length < 25:
            size = 3
        else:            
            size = 5

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()    
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    
    wn.exitonclick()

# Global parameters

width = 450

title = "32-Segment-Curve"
axiom = "F+F+F+F"
rules = {"F":"-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+"}
iterations = 4 # TOP: 3
angle = 90

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width)

title = "Box-Fractal"
axiom = "F-F-F-F"
rules = {"F":"F-F+F+F-F"}
iterations = 4 # TOP: 6
angle = 90

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width)

title = "Dragon-Curve"
axiom = "FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 7 # TOP: 16
angle = 90

offset_angle = -90 + 45 * iterations
correction_angle = 45 * iterations

main(iterations, axiom, rules, angle, correction_angle=correction_angle, 
    offset_angle=offset_angle, width=width, height=width) 

title = "Twin-Dragon-Curve"
axiom = "FX+FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 6 # TOP: 16
angle = 90

offset_angle = -90 + 45 * iterations
correction_angle = 45 * iterations

# main(iterations, axiom, rules, angle, correction_angle=correction_angle, 
#     offset_angle=offset_angle, width=width, height=width) 

title = "ThreeDragon-Curve"
axiom = "FX+FX+FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 7 # TOP: 15
angle = 90

offset_angle = -90 + 45 * iterations
correction_angle = 45 * iterations

# main(iterations, axiom, rules, angle, correction_angle=correction_angle, 
#     offset_angle=offset_angle, width=width, height=width) 

title = "TerDragon-Curve" 
axiom = "F"
rules = {"F":"F-F+F"}
iterations = 5 # TOP: 10
angle = 120

offset_angle = 90 - 30 * iterations
correction_angle = 180 - 30 * iterations

# main(iterations, axiom, rules, angle, correction_angle=correction_angle,
#     offset_angle=offset_angle, width=width, height=width) 

title = "Levy-C-Curve" 
axiom = "F"
rules = {"F":"+F--F+"}
iterations = 10 # TOP: 16
angle = 45

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, height=width)

title = "Hilberts-Curve" 
axiom = "L"
rules = {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"}
iterations = 8 # TOP: 9
angle = 90
y_offset = -190
angle_offset = 90

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, 
#      inverted=True, offset_angle=angle_offset, y_offset=y_offset)

title = "Hilbert-Curve-II"
axiom = "X"
rules = {"X":"XFYFX+F+YFXFY-F-XFYFX", "Y":"YFXFY-F-XFYFX+F+YFXFY"}
iterations = 4 # TOP: 6
angle = 90
y_offset = -190
angle_offset = 0

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, 
#         offset_angle=angle_offset, y_offset=y_offset)

title = "Koch-Snowflake" 
axiom = "F--F--F"
rules = {"F":"F+F--F+F"}
iterations = 4 # TOP: 7
angle = 60

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width)

title = "Peano-Curve" 
axiom = "F"
rules = {"F":"F+F-F-F-F+F+F+F-F"}
iterations = 2 # TOP: 5
angle = 90

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width)

title = "Peano-Gosper-Curve" 
axiom = "FX"
rules = {"X":"X+YF++YF-FX--FXFX-YF+", "Y":"-FX+YFYF++YF+FX--FX-Y"}
iterations = 4 # TOP: 6
angle = 60

offset_angle = -90 + 15 * iterations
correction_angle = 15 * iterations

# main(iterations, axiom, rules, angle, correction_angle=correction_angle, 
#     offset_angle=offset_angle, aspect_ratio=1, width=width)

title = "Quadratic-Koch-Island"
axiom = "F+F+F+F"
rules = {"F":"F-F+F+FFF-F-F+F"}
iterations = 2 # TOP: 4
angle = 90

offset_angle = -105 + 15 * iterations
correction_angle = -15 + 15 * iterations

# main(iterations, axiom, rules, angle, correction_angle=correction_angle, 
#     offset_angle=offset_angle, aspect_ratio=1, width=width)

title = "Sierpinski-Arrowhead"
axiom = "YF"
rules = {"X":"YF+XF+Y", "Y":"XF-YF-X"}
iterations = 1 # TOP: 10
angle = 60

flip_v = True
correction_angle = 0 if iterations % 2 == 0 else -60
offset_angle = -90 if iterations % 2 == 0 else -30
    
# main(iterations, axiom, rules, angle, aspect_ratio=1, flip_v=True, height=width,
#      correction_angle=correction_angle, offset_angle=offset_angle, width=width)

title = "Sierpinski-Curve"
axiom = "F+XF+F+XF"
rules = {"X":"XF-F+F-XF+F+XF-F+F-X"}
iterations = 4 # TOP: 8
angle = 90

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width)

title = "Siepinski-Sieve"
axiom = "FXF--FF--FF"
rules = {"F":"FF", "X":"--FXF++FXF++FXF--"}
iterations = 7 # TOP: 8
angle = 60

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width)

title = "Quadratic-Snowflake"
axiom = "F--F"
rules = {"F":"F-F+F+F-F"}
iterations = 4 # TOP: 6
angle = 90
angle_offset = -90

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, height=width)

title = "Board"
axiom = "F+F+F+F"
rules = {"F":"FF+F+F+F+FF"}
iterations = 3 # TOP: 5
angle = 90

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width)

title = "Cross"
axiom = "F+F+F+F"
rules = {"F":"F+FF++F+F"}
iterations = 3 # TOP: 6
angle = 90

offset_angle = -120 + 30 * iterations
correction_angle = -30 + 30 * iterations

# main(iterations, axiom, rules, angle, correction_angle=correction_angle, 
#     offset_angle=offset_angle, aspect_ratio=1, width=width)

title = "Cross-2"
axiom = "F+F+F+F"
rules = {"F":"F+F-F+F+F"}
iterations = 3 # TOP: 6
angle = 90

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width)

title = "Pentaplexity"
axiom = "F++F++F++F++F"
rules = {"F":"F++F++F+++++F-F++F"}
iterations = 1 # TOP: 5
angle = 36

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, flip_v=True)

title = "Tiles"
axiom = "F+F+F+F"
rules = {"F":"FF+F-F+F+FF"}
iterations = 3 # TOP: 4
angle = 90

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, flip_v=True)

title = "Rings"
axiom = "F+F+F+F"
rules = {"F":"FF+F+F+F+F+F-F"}
iterations = 2 # TOP: 4
angle = 90

offset_angle = -90 + 15 * iterations
correction_angle = 15 * iterations

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, flip_v=True)

title = "Krishna-Anklets"
axiom = " -X--X"
rules = {"X":"XFX--XFX"}
iterations = 3 # TOP: 9
angle = 45

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, flip_v=True)

title = "Triangle"
axiom = "F+F+F"
rules = {"F":"F-F+F"}
iterations = 2 # TOP: 9
angle = 120

offset_angle = -90 - 30 * iterations
correction_angle = -30 * iterations

# main(iterations, axiom, rules, angle, correction_angle=correction_angle, 
#     offset_angle=offset_angle, aspect_ratio=1, width=width)

title = "Quadratic-Gosper"
axiom = "YF"
rules = {"X": "XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-", 
         "Y": "+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY"}
iterations = 2 # TOP: 3
angle = 90

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, flip_v=True)

title = "Crystal"
axiom = "F+F+F+F"
rules = {"F":"FF+F++F+F"}
iterations = 3 # TOP: 6
angle = 90

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, flip_v=True)

title = "Moore-Curve"
axiom = "LFL-F-LFL"
rules = {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"}
iterations = 0 # TOP: 8
angle = 90
y_offset = 190
angle_offset = 0
margin = 35

# Original: -width / 2 + margin + (width - 2 * margin) / (2**(iterations+1) - 1) * (2**(iterations) - 1)
x_offset = - (width - 2 * margin) / (2 * (2 ** (iterations + 1) - 1))
if iterations == 0:
    x_offset = -190

# main(iterations, axiom, rules, angle, aspect_ratio=1, width=width, flip_v=True,
#     offset_angle=angle_offset, y_offset=y_offset, x_offset=x_offset)


