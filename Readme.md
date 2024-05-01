# Simple Expression Language Compiler

## Overview

This repository contains the source code for a simple compiler designed to parse and evaluate expressions in a custom expression language. The compiler is implemented in Python and includes a graphical user interface (GUI) for interactive expression evaluation.

## Features

- **Parsing**: The compiler parses input expressions according to predefined grammar rules.
- **Evaluation**: Supports algebraic operations such as addition, subtraction, multiplication, division, and exponentiation.
- **Print and Input**: Includes support for printing results and taking user input.
- **Variable Assignment**: Allows users to assign and store results in variables for later use.
- **Graphical User Interface**: Provides a user-friendly interface for inputting expressions and viewing results.

## Project Structure

The project is organized into the following directories:

- **parser**: Contains the Python code for parsing input expressions according to the defined grammar rules.
- **gui**: Implements the graphical user interface using Python GUI frameworks such as Tkinter or PyQt.
- **tests**: Includes test cases to validate the correctness of parsing and evaluation.

## Installation and Usage

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/wardaBibi/compilerDesign-LabProject.git
   ```

2. Install dependencies (if any) by running:
   ```
   pip install -r requirements.txt
   ```

3. Run the compiler GUI:
   ```
   python gui/main.py
   ```

4. Input expressions in the GUI and observe the evaluated results.

## Documentation

- **Grammar Rules**: Detailed documentation of the grammar rules used for parsing expressions.
- **Design Choices**: Explanation of design choices, implementation details, and usage instructions.
- **Input Handling**: Description of the input handling mechanism, variable storage, and support for different data types.
- **Examples**: Usage examples of the compiler and GUI components are provided for reference.

## Testing

- **Input Testing**: Test cases for various input expressions, including valid and invalid cases.
- **Validation**: Tests to validate the correctness of parsing results and proper error handling.
- **Usability Testing**: Feedback gathered from usability testing of the GUI to improve user experience.

## Contribution

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
