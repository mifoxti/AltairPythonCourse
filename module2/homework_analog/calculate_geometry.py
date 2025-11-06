def calculate_geometry(shape, **params):
    if shape == "circle":
        radius = params.get("radius")
        area = round(3.14 * radius ** 2, 2)
        perimetr = round(2 * 3.14 * radius, 2)
        return {"area": area, "perimetr": perimetr}

    elif shape == "rectangle":
        lenght = params.get("lenght")
        width = params.get("width")
        area = lenght * width
        perimetr = 2 * (lenght + width)
        return {"area": area, "perimetr": perimetr}

    elif shape == "triangle":
        base = params.get("base", 0)
        height = params.get("height", 0)
        side1 = params.get("side1", 0)
        side2 = params.get("side2", 0)
        side3 = params.get("side3", 0)

        area = 0.5 * base * height
        perimetr = side1 + side2 + side3
        return {"area": area, "perimetr": perimetr}

    else:
        return {"error": "неизвестная фигура"}


print(calculate_geometry("circle", radius=5))
print(calculate_geometry("rectangle", lenght=4, width=6))
print(calculate_geometry("triangle", base=3, height=4, side1=3, side2=4, side3=5))