def create_matrix(schematic):
    matrix = []
    for line in schematic.splitlines():
        if not line.strip():
            continue
        matrix.append(list(line.strip()))
    return matrix

def has_symbol(matrix, row, col):
    if row<0 or col<0 or row>=len(matrix) or col>=len(matrix[row]):
        return False
    else:
        print(matrix[row][col])
        return not matrix[row][col].isnumeric() and matrix[row][col] != '.'
    
def check_for_symbol_and_return_part(matrix, row, begin, end):
    num = int(''.join(matrix[row][begin:end]))
    for col in range(begin-1,end+1):
        if has_symbol(matrix,row-1,col) or has_symbol(matrix,row+1,col):
            return num
    if has_symbol(matrix,row,begin-1) or has_symbol(matrix,row,end):
        return num
    return 0
    
def sum_of_partnumbers(schematic):
    matrix = create_matrix(schematic)
    total=0
    row = 0
    while row < len(matrix):
        col = 0
        while col < len(matrix[row]):
            while col < len(matrix[row]) and matrix[row][col] == '.':
                col+=1
            begin = col
            while col < len(matrix[row]) and matrix[row][col].isnumeric():
                col+=1
            end = col
            if begin != end:
                total+=check_for_symbol_and_return_part(matrix, row, begin, end)
            col+=1
        row+=1
    return total
                
            
if __name__ == '__main__':
    with open('3/schematic.txt', encoding='utf-8') as f:
        schematic = f.read()
        print(sum_of_partnumbers(schematic))
    