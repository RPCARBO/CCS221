import matplotlib.pyplot as plt

def DDALine (x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
# tjhis is where we calculate the change in x and y

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
 #here calculate the 'steps' required for mamking the points for the DDALine

    Xinc = float(dx / steps)
    Yinc = float(dy / steps)
# This one calculates the x and y divided by the steps

#This is calculating the midline for the DDALine
    mid_x = x1 + (dx / 2)
    mid_y = y1 + (dy / 2)

    #This plots the line for DDALine
    for i in range(0, int(steps + 1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
    
    #Plotting the midpoint for the DDALine
    plt.plot(int(mid_x), int(mid_y), "g.")
    plt.title("DDA Line with Mid Point")
    plt.show()

def BresenhamLine(x1, y1, x2, y2, color):
    #Calculate the change in x and y(thr same as the DDAline code)
    dx = x2 - x1
    dy = y2 - y1

    # This one calculates the x and y divided by the steps(copy pasted from DDALine)
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

# This one calculates the x and y divided by the steps(copy pasted again from DDALine)
    Xinc = int(dx / steps)
    Yinc = int(dy / steps)

    #This is calculating the midline for the Bresenham line
    mid_x = x1 + (dx / 2)
    mid_y = y1 + (dy / 2)

    x = x1
    y = y1

    #Ploting the line for bresnham
    for i in range(0, int(steps + 1)):
        plt.plot(int(x), int(y), color)
        x += Xinc
        y += Yinc
    
    #Plotting the midpoint for the bresenham
    plt.plot(int(mid_x), int(mid_y), "g.")
    plt.title("Bresenham Line with Mid Point")
    plt.show()

def main():
    x = int(input("Enter X1: "))
    y = int(input("Enter Y1: "))
    xEnd = int(input("Enter X2: "))
    yEnd = int(input("Enter Y2: "))
    color = "r."

    #This create a new figure to plot the DDA line
    plt.figure()
    DDALine(x, y, xEnd, yEnd, color)
    
    #Create a new figure to plot the Bresenham line(same as above)
    plt.figure()
    BresenhamLine(x, y, xEnd, yEnd, color)

#Check if the program is run as standalone
if __name__ == '__main__':
    main()
