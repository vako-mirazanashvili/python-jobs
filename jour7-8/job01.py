def draw_rectangle(width, height):
    if width < 2 or height < 2:
        return
    print("|" + "-" * (width - 2) + "|")
    i = 0
    while i < height - 2:
        print("|" + " " * (width - 2) + "|")
        i = i + 1
    print("|" + "-" * (width - 2) + "|")

draw_rectangle(10, 3)
