import math
import sys
import numpy as np
import keyboard

class ComplexNumber():
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def size(self):
        return math.sqrt(self.real**2 + self.imaginary**2)
    
def add(x: ComplexNumber, y: ComplexNumber):
    return ComplexNumber(x.real + y.real, x.imaginary + y.imaginary)

def multiply(x: ComplexNumber, y: ComplexNumber):
    return ComplexNumber(x.real*y.real - x.imaginary*y.imaginary, x.real*y.imaginary + x.imaginary*y.real)

# f_c(z) := z^2 + c 
def squarez_and_addc(c: ComplexNumber, z: ComplexNumber):
    return add(multiply(z,z), c)

# returns True if f_c(z) := z^2 + c iterated n times starting with f_c(0) remains bounded and False otherwise
def mandlebrot(c: ComplexNumber, n = 100):
    z = ComplexNumber(0,0)
    for i in range(n):
        if z.size() > 5:
            return False
        z = squarez_and_addc(c, z)
    return True

#print(mandlebrot(ComplexNumber(0.1, 0.1)))
#print(mandlebrot(ComplexNumber(2.0, 2.0)))

def plot(r_low, r_high, i_low, i_high):
    print()
    width = 120
    height = 39

    for imaginary in np.linspace(i_high, i_low, height):
        for real in np.linspace(r_low, r_high, width):
            if mandlebrot(ComplexNumber(real, imaginary)):
                print('*', end='')
            else:
                print(' ', end='')
        print('')

if len(sys.argv) < 2 or sys.argv[1] != "-i":
    plot(-2.0, 1.0, -1.0, 1.0)
else:
    w = 0.001
    h = w
    x = (-3/4)+0.001
    y = 0.07

    plot(x, x+w, y, y+h)

    def interactive_plot(dx,dy,dw,dh):
        global x
        global y
        global w
        global h
        x += dx
        y += dy
        w = w*dw
        h = h*dh
        plot(x, x+w, y, y+h)
        

    keyboard.add_hotkey('up', interactive_plot, args=(0,h,1,1))
    keyboard.add_hotkey('down', interactive_plot, args=(0,-h,1,1))
    keyboard.add_hotkey('left', interactive_plot, args=(-w,0,1,1))
    keyboard.add_hotkey('right', interactive_plot, args=(w,0,1,1))
    zoom = 0.25
    zin = 1-zoom
    zout = 1+zoom
    keyboard.add_hotkey('q', interactive_plot, args=(0,0,zin,zin))
    keyboard.add_hotkey('a', interactive_plot, args=(0,0,zout,zout))
    keyboard.wait()