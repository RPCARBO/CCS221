import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def DDALine (x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

    mid_x = x1 + (dx / 2)
    mid_y = y1 + (dy / 2)

    x = x1
    y = y1

    fig, ax = plt.subplots()
    for i in range(0, int(steps + 1)):
        ax.plot(int(x), int(y), color)
        x += Xinc
        y += Yinc

    ax.plot(int(mid_x), int(mid_y), "g.")
    ax.set_title("DDA Line with Mid Point")
    st.pyplot(fig)

def BresenhamLine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xinc = int(dx / steps)
    Yinc = int(dy / steps)

    mid_x = x1 + (dx / 2)
    mid_y = y1 + (dy / 2)

    x = x1
    y = y1

    fig, ax = plt.subplots()
    for i in range(0, int(steps + 1)):
        ax.plot(int(x), int(y), color)
        x += Xinc
        y += Yinc
    
    ax.plot(int(mid_x), int(mid_y), "g.")
    ax.set_title("Bresenham Line with Mid Point")
    st.pyplot(fig)

def main():
    x = int(input("Enter X1: "))
    y = int(input("Enter Y1: "))
    xEnd = int(input("Enter X2: "))
    yEnd = int(input("Enter Y2: "))
    color = "r."

    DDALine(x, y, xEnd, yEnd, color)

    BresenhamLine(x, y, xEnd, yEnd, color)

if __name__ == '__main__':
    main()