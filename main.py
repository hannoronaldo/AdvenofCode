# part1 day8


with open("day8.in") as file:
    tree_lines = file.read().split()
    rows = len(tree_lines)
    columns = len(tree_lines[0])
    edges = (rows* 2) + (columns- 2)*2
    total_trees_visible = edges
    for row in range(1, rows-1):
        for col in range(1, columns-1):
            tree = tree_lines[row][col]

            left = [tree_lines[row][col-1] for i in range(1, col+1)]
            print(left)
