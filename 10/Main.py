import sys
from os import listdir
from os.path import isfile, isdir
from Compilation import CompilationEngine


def file_list(args):
    files_list = []
    if len(args) == 2:
        if isfile(args[1]) and args[1].endswith(".jack"):
            files_list.append(args[1])
        elif isdir(args[1]):
            for file in listdir(args[1]):
                if file.endswith(".jack"):
                    files_list.append(args[1] + "/" + file)
        return files_list
    else:
        print("Bad input")
        exit()


def file_output_path(path):
    return path.rsplit(".jack", 1)[0] + ".xml"


if __name__ == "__main__":
    files = file_list(sys.argv)
    for path in files:
        current_code = CompilationEngine(path, file_output_path(path))
        current_code.compile_class()
