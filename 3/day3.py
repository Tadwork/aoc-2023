def create_matrix(schematic):
    matrix = []
    for line in schematic.splitlines():
        if not line.strip():
            continue
        matrix.append(list(line.strip()))
    return matrix

## Part 1
def has_symbol(matrix, row, col):
    if row<0 or col<0 or row>=len(matrix) or col>=len(matrix[row]):
        return False
    else:
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

## Part 2
def get_full_part_number_from_coord(matrix,row,col):
    begin = col
    while begin >=0 and matrix[row][begin].isnumeric():
        begin-=1
    end=col
    while end < len(matrix[row]) and matrix[row][end].isnumeric():
        end+=1
    return int(''.join(matrix[row][begin+1:end])),end

def is_part_num(matrix, row, col):
    if row<0 or col<0 or row>=len(matrix) or col>=len(matrix[row]):
        return False
    else:
        return matrix[row][col].isnumeric()
    
def get_prod_of_adjacent_part_numbers_to_gear(matrix, row, col):
    part_numbers = []
    c=col-1
    while c < col+2:
        if is_part_num(matrix,row+1,c):
            num, end = get_full_part_number_from_coord(matrix,row+1,c)
            part_numbers.append(num)
            c=end
        else:
            c+=1
    c=col-1
    while c < col+2:
        if is_part_num(matrix,row-1,c):
            num, end = get_full_part_number_from_coord(matrix,row-1,c)
            part_numbers.append(num)
            c=end
        else:
            c+=1
    if is_part_num(matrix,row,col-1):
        part_numbers.append(get_full_part_number_from_coord(matrix,row,col-1)[0])
    if is_part_num(matrix,row,col+1):
        part_numbers.append(get_full_part_number_from_coord(matrix,row,col+1)[0])
    if len(part_numbers) == 2:
        return part_numbers[0] * part_numbers[1]
    return 0

def get_all_gear_coordinates(schematic):
    matrix = create_matrix(schematic)
    total = 0
    for i,row in enumerate(matrix):
        for j,_ in enumerate(row):
            if matrix[i][j] == '*':
                total+=get_prod_of_adjacent_part_numbers_to_gear(matrix,i,j)
    return total
            
if __name__ == '__main__':
    with open('3/schematic.txt', encoding='utf-8') as f:
        schematic = f.read()
        print(sum_of_partnumbers(schematic))
        print(get_all_gear_coordinates(schematic))
    