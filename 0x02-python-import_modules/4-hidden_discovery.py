#!/usr/bin/python3
import hidden_4


def main() -> None:
    statments: list[str] = dir(hidden_4)

    for statment in statments:
        if statment[:2] == ("__"):
            continue
        print(statment)


if __name__ == "__main__":
    main()
