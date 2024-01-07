#!/usr/bin/python3
def main() -> None:
    def no_c(my_string: str) -> str:
        new_string = ""
        for i in my_string:
            if i != "c" and i != "C":
                new_string += i
        return new_string

    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))


if __name__ == "__main__":
    main()
