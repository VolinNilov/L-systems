import turtle

turtle.hideturtle()
turtle.tracer(1)
turtle.penup()
turtle.setposition(-300,340)
turtle.pendown()
turtle.pensize(1)

axiom = "F+F+F+F"
tempAx = ""
itr = 3 

#tranlate = {"+":"+", "-":"-", "F":"F + F - F - F + F"}
#for k in range(itr):
#    for ch in axiom:
#    	tempAx += translate[ch]
#    axiom = tempAx
#    tempAx = " "
#print(axiom)

#for k in range(itr):
#    for ch in axiom:
#        if ch == "+":
#            tempAx = tempAx + "  +"
#        elif ch == "-":
#            tempAx = tempAx + " - "
#        else: #F
#            tempAx = tempAx + "F + F - F - F + F"
#    axiom = tempAx
#   tempAx = " "
#print(axiom)

for k in range(itr):
    for ch in axiom:
        if ch == "+":
            tempAx = tempAx + "+"
        elif ch == "-":
            tempAx = tempAx + "-"
        elif ch == "F": #F
            tempAx = tempAx + "F+F-F-F+F"
        else: 
        	tempAx = tempAx + "f"
    axiom = tempAx
    tempAx = " "
print(axiom)
        
turtle.fillcolor("#99BBFF")
#turtle.begin_fill()
for ch in axiom:
    if ch == "+":
        turtle.right(45)
#        turtle.forward(10)
        turtle.right(45)
    elif ch == "-":
        turtle.left(45)
#        turtle.forward(10)
        turtle.left(45)
    else:
        turtle.forward(20)
#turtle.end_fill()

turtle.update()
turtle.done()