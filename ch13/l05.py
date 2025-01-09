def area_sum(rectangles):
    sum = 0

    for shape in rectangles:
        sum += shape["height"] * shape["width"]

    return sum
