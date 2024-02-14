# Python | Almost A Circle

This repository showcases a practical application of various Python skills and techniques. Mastering the object-oriented programming through the context of implementing and testing classes related to geometric shapes **(Rectangles and Squares)**.

## Overview

In this project, we are implementing three classes: 
- Base class: The foundational class serving as a common structure for the other geometric shapes.

- Rectangle class: Inherits from the Base class, representing rectangles and inheriting the fundamental properties defined in the Base class.

- Square class: Inherits from the Rectangle class, showcasing the principles of multi-level inheritance. This class specializes in representing squares, building upon the characteristics defined in both the Base and Rectangle classes.

These three classes make extensive use of various Python tools and features, including:

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

## Project Structure

1. models

    - [base.py](models/base.py)
    - [rectangle.py](models/rectangle.py)
    - [square.py](models/square.py)

2. tests

	- [general_tests.py](tests/general_tests.py)
	- [test_base.py](tests/test_base.py)
	- [test_rectangle.py](tests/test_rectangle.py)
	- [test_square.py](tests/test_square.py)

## Getting Started

This project is part of the [main repository](https://github.com/AhmadYousif89/alx-higher_level_programming) therefore you have two options:

1. Clone the entire repository to access this project as a sub-directory.

2. Follow these instructions to **only** clone this project/directory:

	- Open a terminal where you want to save this project.
	- Enter this command:
		```bash
		git clone --filter=blob:none --sparse https://github.com/AhmadYousif89/alx-higher_level_programming

		cd alx-higher_level_programming
		```
	- Optional command (you might skip this one):
		```bash
		git config core.sparseCheckout true
		```
	- Then after navigating to the new directory:
		```bash
		git sparse-checkout add 0x0C-python-almost_a_circle

		cd 0x0C-python-almost_a_circle
		```

## Testing

Running all tests at once with this command:

```bash
python3 -m unittest discover tests
```
Running specific test file with this command:

```bash
python3 -m unittest tests/<test_file>
```
For testing the general tests provided for each task run the **general_tests.py** file with this command:

```bash
python3 -m tests.general_tests
```

### Auther

- [Ahmad Yousif](https://github.com/AhmadYousif89)