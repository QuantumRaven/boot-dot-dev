#!/usr/bin/env python3


def countdown_to_start():

    for item in range(10, 0, -1):
        if item == 1:
            print(f"{item}...Fight!")
        else:
            print(f"{item}...")


# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()
