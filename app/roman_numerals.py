def parse(arg):
    # if arg == 'I': return 1
    # if arg == 'II': return 2
    # if arg == 'III': return 3
    # if arg == 'IV': return 4
    # if arg == 'V': return 5
    # if arg == 'VI': return 6
    # if arg == 'VII': return 7
    # if arg == 'VIII': return 8
    total = 0
    dict = {"I":1, "V":5, "X": 10, "L":50, "C": 100, "D":500, "M":1000}

    for index in range(len(arg) -1):
        if dict[arg[index]] >= dict[arg[index +1]]:
            total += dict[arg[index]]
        else:
            total -= dict[arg[index]]

    total += dict[arg[-1]]
    return total
