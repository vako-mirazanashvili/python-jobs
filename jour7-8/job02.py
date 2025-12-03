def draw_triangle(height):
    if height < 1:
        return
    i = 0
    while i < height:
        spaces = height - 1 - i
        if i == height - 1:
            line = "/" + "_" * (2 * i) + "\\"
        else:
            line = "/" + " " * (2 * i) + "\\"
        print(" " * spaces + line)
        i = i + 1

draw_triangle(5)
