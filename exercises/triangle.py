'''
import math
import turtle
WIDTH = 1000
HEIGHT = 1000
turtle.bgcolor("white")
turtle.pencolor("black")
turtle.pensize(2)


def sier(n,d,p,q,r):
    """
    Función que traza la n-ésima iteración
    del triángulo de sierpinski.

    Parameters
    ----------
    n : (int) número de iteraciones
    d : (float) longitud del lado del
        triángulo equilatero
    p : (tuple) primer vértice del 
        triángulo
    q : (tuple) segundo vértice del 
        triángulo
    r : T(tuple) tercer vértice del 
        triángulo

    Returns
    -------
    Animación hecha con turtle de la
    n-ésima etapa de construcción
    del triángulo de sierpinski

    """
    turtle.penup()
    turtle.setpos(p[0],p[1])
    turtle.pendown()
    turtle.goto(q[0],q[1])
    turtle.goto(r[0],r[1])
    turtle.goto(p[0],p[1])
    medio_pq = ((p[0]+q[0])/2, (p[1]+q[1])/2)
    medio_qr = ((q[0]+r[0])/2, (q[1]+r[1])/2)
    medio_rp = ((r[0]+p[0])/2, (r[1]+p[1])/2)
    
    if n>1:
        sier(n-1,d/2,p,medio_pq,medio_rp)
        turtle.penup()
        sier(n-1,d/2,medio_pq,q,medio_qr)
        turtle.penup()
        sier(n-1,d/2,medio_rp,medio_qr,r)
        

sier(6,250,(-150,0),(100,0),
     (-25,math.sqrt((250**2)-(125**2))))
turtle.exitonclick()



'''
#--------------------------------------------------------------------
#in process
import turtle

WIDTH = 1000
HEIGHT = 1000


def draw_triangle(x, y, length):
    turtle.penup()
    turtle.setpos(x, y)
    
    turtle.pendown()
    turtle.forward(length)
    turtle.left(120)

    turtle.forward(length)
    turtle.left(120)

    turtle.forward(length)
    turtle.left(120)

def draw_carpet(offset_x, offset_y, length, level):
    if level > 0:
        sublength = length // 3
        draw_triangle(offset_x + sublength, offset_y - sublength, sublength)

        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    pass
                else:
                    draw_carpet(offset_x + i * sublength, offset_y - j * sublength, sublength, level - 1)

def main():
    screen = turtle.Screen()

    screen.setup(WIDTH, HEIGHT)
    screen.screensize(WIDTH, HEIGHT)

    screen.title("Sierpinski Carpet")

    turtle.bgcolor("black")
    turtle.pencolor("green")
    turtle.pensize(2)
    turtle.speed("fastest")
    draw_carpet(0, 0, 300, level=3)

    turtle.done()

if __name__ == '__main__':
    main()
