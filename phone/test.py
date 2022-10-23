import sys

from model import Mobiltelefon
from model import Okostelefon

def main() -> None:

    n = int(sys.argv[1])

    lista = []
    for i in range(n):
        line = input()
        tokens = line.split(";")
        if len(tokens) == 3:
            lista.append(Mobiltelefon(tokens[0], tokens[1], int(tokens[2])))
        elif len(tokens) == 4:
            lista.append(Okostelefon(tokens[0], tokens[1], int(tokens[2]), tokens[3]))
        else:
            print("Hiba")

    lista.sort()

    for i in lista:
        print(i)


if __name__ == "__main__":
    main()
