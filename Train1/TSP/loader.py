def read_tsp_file(path="Train1/data/kroB200.txt"):
    """Reads a TSP file and returns the coordinates of the cities."""

    with open(path, "r") as f:
        lines = f.readlines()

    coords = []
    reading_coords = False
    for line in lines:
        line = line.strip()
        if line == "NODE_COORD_SECTION":
            reading_coords = True
            continue
        if line == "EOF":
            break
        if reading_coords:
            parts = line.split()
            if len(parts) >= 3:
                x, y = int(parts[1]), int(parts[2])
                coords.append((x, y))

    return coords
