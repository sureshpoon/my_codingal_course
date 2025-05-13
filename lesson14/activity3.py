import turtle 
sp = turtle.Screen().bgcolor("light blue")
# sp.Title("Turtle")
# sp.setup (width = 500 , height = 500)
pen = turtle.Turtle()
size = 0
while True : 
    for i in range (4) :
        pen.fd(size + 1)
        pen.left(90)
        size = size - 5

    size = size + 1

  

        
    

