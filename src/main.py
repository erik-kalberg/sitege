from textnode import *
from htmlnode import *


def main():
    N = TextType('bold')
    test = TextNode("test", N, "boot.dev")
    print(test)

if __name__ == "__main__":
    main()