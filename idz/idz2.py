import os
import argparse
def tree(dirr, lev, incFiles, indent):
    print("|   " * indent + "|-- " + os.path.basename(dirr) + "/")
    if incFiles:
        for f in os.listdir(dirr):
            if os.path.isfile(os.path.join(dirr, f)):
                print("|   " * (indent+1) + "|-- " + f)
    if lev > 1:
        for d in os.listdir(dirr):
            if os.path.isdir(os.path.join(dirr, d)):
                tree(os.path.join(dirr, d), lev-1, incFiles, indent+1)
parser = argparse.ArgumentParser(description="An analogue of the tree utility in Linux.")
parser.add_argument("directory", type=str, nargs="?", default=".", help="каталог для отображения дерева")
parser.add_argument("-l", "--le", type=int, default=3, help="максимальная глубина дерева")
parser.add_argument("-f", "--fil", action="store_true", help="включить файлы в дерево")
parser.add_argument("-i", "--ind", type=int, default=0, help="величина начального отступа")
args = parser.parse_args()

if __name__ == "__main__":
    tree(args.directory, args.le, args.fil, args.ind)