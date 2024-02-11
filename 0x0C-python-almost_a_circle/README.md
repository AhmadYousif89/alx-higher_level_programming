# Python | Almost A Circle

This repository showcases a practical application of various Python skills and techniques. Mastering the object-oriented programming through the context of implementing and testing classes related to geometric shapes **(Rectangles and Squares)**.

These three classes extensively utilize a range of Python tools, including:

- Import statements
- Exception handling
- Private attributes
- Getter and setter methods
- Class and static methods
- Inheritance principles
- File Input/Output operations
- Arguments **(args)** and keyword arguments **(kwargs)**
- Serialization and deserialization using **JSON** and **CSV** formats
- Going beyond abstract programming concepts by incorporating the **Turtle** module to visually represent the geometric shapes. 
- Thorough unit testing with the **unittest** module

## Table of Content

1. models

    - [base.py](base.py)
    - [rectangle.py](rectangle.py)
    - [square.py](square.py)

2. tests

	- [general_tests.py](general_tests.py)
	- [test_base.py](test_base.py)
	- [test_rectangle.py](test_rectangle.py)
	- [test_square.py](test_square.py)

### Testing

Running all tests at once with this command:

```bash
python3 -m unittest discover tests
```
Running specific test file:

```bash
python3 -m unittest tests/<test_file>
```