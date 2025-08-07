# Roman Numeral Converter

This project provides a Python implementation for converting **Roman numerals to integers** and **integers to Roman numerals**, following the **minimal form rules** for Roman numerals.

---

## About Roman Numerals

Traditional Roman numerals use the following symbols and values:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

To be considered **valid**, Roman numerals must follow these basic rules:

- Numerals are arranged in descending order of size.
- Symbols **M, C, and X** cannot be equalled or exceeded by smaller denominations.
- Symbols **D, L, and V** can each appear only once.
- Subtractive notation is used for compact representation (e.g., `IV` for 4, `IX` for 9).
- Only one `I`, `X`, or `C` can be used as the leading numeral in a subtractive pair.
- `I` can only precede `V` and `X`.
- `X` can only precede `L` and `C`.
- `C` can only precede `D` and `M`.

Our implementation **enforces these minimal form rules**, ensuring that input Roman numerals are valid and outputs are in the minimal canonical form.

---

## Source and Inspiration

This implementation is based on the minimal Roman numeral form as described in the Project Euler explanation of Roman numerals:

[Project Euler: About Roman Numerals](https://projecteuler.net/about=roman_numerals)

---

## How to Use

### Prerequisites

- Python 3.6 or higher

### Running the Converter

1. Clone this repository or download the source files.
2. Run the interactive script to convert Roman numerals to integers and vice versa:

python3 RomanToInt.py

### Generating Valid Cases

The IntToRoman.py script automatically generates the validcases.txt file inside the tests directory. This file contains Roman numerals in minimal canonical form for all integers from 1 to 3999.

### Running Tests

Before running the tests, make sure to generate the validcases.txt file by running the integer-to-Roman converter script first. This ensures that the valid test cases are up-to-date.

Run the commands in this order:

python3 IntToRoman.py

python3 -m unittest tests/test_python-d.py
