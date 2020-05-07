"""
Sammy Howorth
FIRST PASS (animation tand improvements o follow)
July 5, 2020; (2:00pm - 2:45pm)
"""
import random

class life:

    def __init__(self, n):
        # for now just make it a square
        self.dim = n
        self.grid = [[random.randint(0,1) for i in range(n)] for j in range (n)]


    def n_neighbours(self, i, j):
        n_alive_neighbours = 0
        print("   checking for ij {} {}".format(i,j))
        for m in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                if i+m >= 0 and j+n >= 0 and not (m == 0 and n == 0):
                    try:
                        if self.grid[i+m][j+n] == 1:
                            n_alive_neighbours += 1
                    except:
                        continue
        return n_alive_neighbours

    def change_cell(self, i, j, state):
        self.grid[i][j] = state

    def next(self):
        # initialize empty next_stage grid (avoid making changes immediately and affecting upcoming n_neighbours checks)
        next_stage = life(self.dim)
        for i in range(self.dim):
            for j in range(self.dim):
                # if alive, check if n_neighbours < 2  =>  death
                #                                 > 3  =>  death
                #                                 == 2 or 3  =>  stayin' alive
                neighbs = self.n_neighbours(i,j)
                print(i, j, "---", neighbs)
                if self.grid[i][j] == 1:
                    if neighbs < 2:
                        next_stage.change_cell(i, j, 0)
                    elif neighbs > 3:
                        next_stage.change_cell(i,j, 0)
                    # else do nothing (stays alive)
                # if dead, check if n_neighbours == 3  =>  born
                elif self.grid[i][j] == 0:
                    if neighbs == 3:
                        next_stage.change_cell(i,j,1)
                else:
                    print("uh oh")
        return next_stage
                
                
    def __repr__(self):
        str = ""
        for i in range(self.dim):
            str += "{}\n".format(self.grid[i])
        return str

    

print()
testing = life(5)
print(testing)
xx = testing.next()
print(xx)