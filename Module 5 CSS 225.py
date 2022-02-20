
#Elizabeth Montero
#02/20/22

#Problem 1
#It prints out hello world 100 times

for i in range(100) :
    print( "Hello World" )


#Problem 2
# A program that gives each number on a lew line and square
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

print("Printing the numbers..")

for i in xs:
    print(i)

print("\nNumber and its square")

for i in xs:
    print(i, i ** 2)



#Problem 3
#the program asks to enter the numbner of sides, lengths
#After choosing the color of line and fill color it makes the polygon into those colors. 
 
import turtle    

wn = turtle.Screen()    
alex = turtle.Turtle()    
sides = int(input("Enter the number of sides: "))    
angle = 360 / sides    
length = int(input("Enter the length of sides: "))    
line_color = input("Enter the color of the lines: ") 
alex.color(line_color)    
fill_color = input("Enter the fill color for the polygon:" )    
alex.fillcolor(fill_color)    
alex.begin_fill()    
for i in range(sides):    
        alex.forward(44)  
        alex.left(angle)    
alex.end_fill()
 
#Problem 4
#Prints the integers from 1 to 50 and multiplies by three 

for i in range(1,51):
    if(i%3==0 and i%5==0):
        print(str(i)+" is Divisible by both three and five")
    elif(i%5==0):
        print(str(i)+" is Divisible by five")
    elif(i%3==0):
        print(str(i)+" is Divisble by three")
    else:
        print("",end="")

#Problem 5
#A program that draws a picture.
#This program draws a star.
import turtle

turing = turtle.Turtle()

for i in range(5):
    turing.forward(110)
    turing.left(216)

        

