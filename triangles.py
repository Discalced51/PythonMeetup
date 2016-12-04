def printTriangle(num_rows, direction="left"):
    ''' A method for creating a triangle out of asterisks (*)s.
        @rows determines how many rows the triangle will be.
        @direction can be "left" or "right" '''
    
    lines_to_print = []
    for (row) in range(1, num_rows + 1):
        stars = row * "*"
        spaces = (num_rows - row) * " "
        lines_to_print.append(stars + spaces)
    
    for line in lines_to_print:
        if (direction == "left"):
            print line
        elif (direction == "right"):
            print line[::-1]
            
printTriangle(10, "left")
printTriangle(10,"right")

def printTree(num_rows):
    ''' A method for creating an isoceles triangle out of asterisks (*)s.
        @rows determines how many rows the triangle will be.'''
    
    for row in range(1, num_rows + 1, 2):
        line = (row * "*").center(num_rows, " ")
        print(line)

printTree(20)