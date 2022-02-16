import numpy as np

def determinant(m):
    if m.ndim != 2:
        return "ERROR: matrix wrong dimensions number"
    row, col = m.shape
    if row != col:
        return "ERROR: matrix not square"
    if row == 1:
        return m[0][0]

    det = 0

    for cl in range(0,col):  # loop on the first row
        rg = 1
        mr = np.zeros((row - 1, col - 1))
        rrg = 0

        for irg in range(1,row):  # A for loop for row entries
            rcl = 0
            for icl in range(0,col):  # A for loop for column entries
                if icl  != cl:
                    mr[rrg][rcl] = m[irg][icl]
                    rcl += 1
            rrg += 1

        det = det + ((-1)**(cl)) * (m[0][cl]) * (determinant(mr))

    return det


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # A basic code for matrix input from user

    D = int(input("Enter the dimension of square Matrix: "))

    # Initialize matrix
    matrix = np.zeros((D, D))
    print("Enter the entries rowwise: ")

    # For user input
    for i in range(D):  # A for loop for row entries
        for j in range(D):  # A for loop for column entries
            matrix[i,j] = input("m(" + str(i+1) + "," + str(j+1) + ")? ")

    print(determinant(matrix))
