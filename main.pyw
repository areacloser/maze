from tkinter import *
from random import *

HEIGHT = 151
WIDTH = 151
CELLSIZE = int(750 / min(HEIGHT, WIDTH))

initmp = [[1 for _ in range(WIDTH)] for _ in range(HEIGHT)]
pos = [0, 0]

def prim(mapin):
    """
    0 -> Road point
    1 -> Wall
    2 -> Pre-road point
    3 -> ???

    -1 -> Player
    """
    prplist = []
    #rplist = []
    initrp = [0, 0]
    mapin[initrp[0]][initrp[1]] = 0
    #rplist.append(initrp)

    def addprp(m, n):
        global HEIGHT, WIDTH
        
        if m - 2 >= 0 and mapin[m-2][n] == 1:
            mapin[m-2][n] = 2
            prplist.append([m-2, n])
        if m + 2 < HEIGHT and mapin[m+2][n] == 1:
            mapin[m+2][n] = 2
            prplist.append([m+2, n])
        if n - 2 >= 0 and mapin[m][n-2] == 1:
            mapin[m][n-2] = 2
            prplist.append([m, n-2])
        if n + 2 < WIDTH and mapin[m][n+2] == 1:
            mapin[m][n+2] = 2
            prplist.append([m, n+2])

    addprp(initrp[0], initrp[1])

    while prplist != []:
        explist = []
        randprp = choice(prplist)
        if randprp[0] - 2 >= 0 and mapin[randprp[0]-2][randprp[1]] == 0:
            explist.append([randprp[0]-2, randprp[1]])
        if randprp[0] + 2 < HEIGHT and mapin[randprp[0]+2][randprp[1]] == 0:
            explist.append([randprp[0]+2, randprp[1]])
        if randprp[1] - 2 >= 0 and mapin[randprp[0]][randprp[1]-2] == 0:
            explist.append([randprp[0], randprp[1]-2])
        if randprp[1] + 2 < WIDTH and mapin[randprp[0]][randprp[1]+2] == 0:
            explist.append([randprp[0], randprp[1]+2])

        if explist != []:
            exprp = choice(explist)
            mapin[randprp[0]][randprp[1]] = 0
            mapin[int((randprp[0]+exprp[0]) // 2)][int((randprp[1]+exprp[1]) // 2)] = 0

        addprp(randprp[0], randprp[1])
        prplist.remove(randprp)
    
    return mapin

def main():
    global HEIGHT, WIDTH, CELLSIZE, initmp, pos

    mp = prim(initmp)
    mp[pos[0]][pos[1]] = -1
    
    win = Tk()
    win.title("Maze V0.0.3 -- By lanlan2_")
    win.resizable(0, 0)

    can = Canvas(win,
                 highlightthickness=0,
                 height=HEIGHT*CELLSIZE+1,
                 width=WIDTH*CELLSIZE+1)

    def redraw():
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if mp[i][j] == 0:
                    can.create_rectangle(j*CELLSIZE, i*CELLSIZE, j*CELLSIZE+CELLSIZE, i*CELLSIZE+CELLSIZE, fill="White", outline="White")
                elif mp[i][j] == 1:
                    can.create_rectangle(j*CELLSIZE, i*CELLSIZE, j*CELLSIZE+CELLSIZE, i*CELLSIZE+CELLSIZE, fill="Black", outline="Black")
                elif mp[i][j] == -1:
                    can.create_rectangle(j*CELLSIZE, i*CELLSIZE, j*CELLSIZE+CELLSIZE, i*CELLSIZE+CELLSIZE, fill="Green", outline="Green")

                if pos != [0, 0]:
                    can.create_rectangle(0, 0, CELLSIZE, CELLSIZE, fill="Red", outline="Red")
                if pos != [HEIGHT-1, WIDTH-1]:
                    can.create_rectangle(WIDTH*CELLSIZE-CELLSIZE, HEIGHT*CELLSIZE-CELLSIZE, WIDTH*CELLSIZE, HEIGHT*CELLSIZE, fill="Blue", outline="Blue")
    redraw()

    can.pack()

    def move(event):
        global pos
        if event.keysym == "Up":
            if pos[0] - 1 >= 0 and mp[pos[0]-1][pos[1]] == 0:
                mp[pos[0]][pos[1]], mp[pos[0]-1][pos[1]] = mp[pos[0]-1][pos[1]], mp[pos[0]][pos[1]]
                pos = [pos[0]-1, pos[1]]
        elif event.keysym == "Down":
            if pos[0] + 1 < HEIGHT and mp[pos[0]+1][pos[1]] == 0:
                mp[pos[0]][pos[1]], mp[pos[0]+1][pos[1]] = mp[pos[0]+1][pos[1]], mp[pos[0]][pos[1]]
                pos = [pos[0]+1, pos[1]]
        elif event.keysym == "Left":
            if pos[1] - 1 >= 0 and mp[pos[0]][pos[1]-1] == 0:
                mp[pos[0]][pos[1]], mp[pos[0]][pos[1]-1] = mp[pos[0]][pos[1]-1], mp[pos[0]][pos[1]]
                pos = [pos[0], pos[1]-1]
        elif event.keysym == "Right":
            if pos[1] + 1 >= 0 and mp[pos[0]][pos[1]+1] == 0:
                mp[pos[0]][pos[1]], mp[pos[0]][pos[1]+1] = mp[pos[0]][pos[1]+1], mp[pos[0]][pos[1]]
                pos = [pos[0], pos[1]+1]
        else:
            return
        redraw()
        if pos == [HEIGHT-1, WIDTH-1]:
            win.unbind("<KeyPress>")
        
    #win.bind("<KeyPress>", move) -> uncomment to let the player move!
    win.mainloop()

if __name__ == "__main__":
    main()
