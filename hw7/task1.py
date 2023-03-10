def move_elephant(x1, y1, x2, y2):
    return (abs(x2 - x1) == 1 and abs(y2 - y1) == 2) or (abs(x2 - x1) == 2 and abs(y2 - y1) == 1)


def main():
    cell_1, cell_2 = input(), input()
    x1, y1 = int(ord(cell_1[0])), int(cell_1[1])
    x2, y2 = int(ord(cell_2[0])), int(cell_2[1])
    
    if move_elephant(x1, y1, x2, y2):
        print('Так, кінь потрапить на цю клітину за 1 хід')
    else:
        print('Ні, за один хід це неможливо')


main()




