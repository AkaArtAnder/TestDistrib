""" Файл предназначен для удобного взаимодествия с классом TestDistrib """
import argparse
import sys

from classtest import TestDistrib


def create_parser():
    """ Функция разбора параметров из командной строки """

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", nargs="?",
                        choices=["norm"], default="norm")
    parser.add_argument("-fr", "--fileread", type=open, required=True)
    # parser.add_argument("-fw", "--folderwrite", nargs="?", default="")

    return parser


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    test = TestDistrib(fileread=str(namespace.fileread),
                       distrib=namespace.name)
    test.qqplot
