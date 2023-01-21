"""
 * Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole
 * únicamente el tamaño del lado.
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
"""

# Print the pascal triangle (lists) with a better format so it can be easily visualized 
# With higher number of rows the triangle is not well visualised because numbers get longer
def print_pascal_triangle(pascal_triangle):
    print("---------------")
    print("PASCAL TRIANGLE")

    length = len(pascal_triangle)
    for row in pascal_triangle:
        length -= 1

        numbers = ""
        row_length = len(row)
        for i in range(row_length):
            numbers += f"{row[i]}"
            if i < (row_length-1):
                numbers += " "

        print("   " + (" " * length) + numbers)

# Calculate Pascal Triangle rows
def cal_triangle_rows(triangle_length):
    pascal_triangle = [[1]]

    last_row = None
    for i in range(1, triangle_length):
        if i > 1:
            current_len = i + 1
            new_row = [0] * current_len
            for j in range(current_len):
                if j > 0 and j < (current_len-1):
                    new_row[j] = last_row[j-1] + last_row[j]
                else:
                    new_row[j] = 1
            last_row = new_row     
        else:
            last_row = [1, 1]
            
        pascal_triangle.append(last_row)

    return pascal_triangle

def main():
    triangle_length = int(input("Insert number of rows of the Pascal Triangle:\n"))

    if triangle_length > 0:
        pascal_triangle = cal_triangle_rows(triangle_length)
        print_pascal_triangle(pascal_triangle)
    else:
        print("ERROR: Triangle length must be greater than 0!")

if __name__ == "__main__":
    main()