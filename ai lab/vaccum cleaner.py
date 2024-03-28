def clean(floor): 
    cleaned_cells = 0  # Initialize a variable to count cleaned cells
    i, j, row, col = 0, 0, len(floor), len(floor[0])
    for i in range(row):
        if(i%2 == 0):
            for j in range(col):
                if(floor[i][j] == 1):
                    print_F(floor, i, j)
                    floor[i][j] = 0
                    cleaned_cells += 1  # Increment the count of cleaned cells
                print_F(floor, i, j)
        else:
            for j in range(col-1, -1, -1):
                if(floor[i][j] == 1):
                    print_F(floor, i, j)
                    floor[i][j] = 0
                    cleaned_cells += 1  # Increment the count of cleaned cells
                print_F(floor, i, j)
    print("Performance measure: Cleaned", cleaned_cells, "cells")

def print_F(floor, row, col): 
    print("The Floor matrix is as below:")
    for r in range(len(floor)):
        for c in range(len(floor[r])):
            if r == row and c == col:
                print(f" >{floor[r][c]}< ", end = '')
            else:
                print(f"  {floor[r][c]}  ", end = '')
        print(end = '\n')
    print(end = '\n')

def main():
    floor = []
    m = int(input("Enter the No. of Rows: "))
    n = int(input("Enter the No. of Columns: "))
    print("Enter clean status for each cell (1 - dirty, 0 - clean)")
    for i in range(m):
        f = list(map(int, input().split(" ")))
        floor.append(f)
    print()
    clean(floor)

main()
