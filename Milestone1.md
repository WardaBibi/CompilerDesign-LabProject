## Milestone 1: Understanding the Grammar and Implementing Input Handling



## Understanding the Grammar Rules



1. **Expression -> Term**
   - This rule states that an expression can be simply a term.
   - Example: `2`, `x`, `5 * y`

2. **Expression -> Term AddOp Expression**
   - This rule allows expressions to involve addition or subtraction operations between terms.
   - Example: `2 + 3`, `x - y`, `a + b - c`

3. **Expression -> Print Expression**
   - This rule enables the expression to start with a print operation followed by another expression.
   - Example: `PRINT 2`, `PRINT x + y`

4. **Expression -> Input Expression**
   - This rule allows the expression to start with an input operation followed by another expression.
   - Example: `INPUT x`, `INPUT y + 5`

5. **Expression -> Assign**
   - This rule indicates that an expression can be an assignment operation.
   - Example: `x = 2`, `y = x + 3`

6. **Term -> Factor**
   - A term can be a factor.
   - Example: `2 * 3`, `x / 4`

7. **Term -> Factor MulOp Term**
   - This rule allows terms to involve multiplication or division operations between factors.
   - Example: `2 * x`, `y / 4`, `a * b / c`

8. **Factor -> Primary**
   - A factor can be a primary expression.
   - Example: `(3 + x)`, `y ^ 2`

9. **Factor -> Primary ExpOp Factor**
   - This rule allows factors to involve exponentiation operations between primary expressions.
   - Example: `x ^ 2`, `(a + b) ^ 3`

10. **Primary -> Number**
    - A primary expression can be a number.
    - Example: `2`, `5`, `10`

11. **Primary -> ( Expression )**
    - This rule allows primary expressions to be enclosed in parentheses.
    - Example: `(2 + 3)`, `(x - 4)`

12. **Number -> Digit**
    - A number can be a single digit.
    - Example: `0`, `1`, `9`

13. **Number -> Digit Number**
    - This rule allows numbers to have multiple digits.
    - Example: `10`, `123`, `9876`

14. **Digit -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9**
    - This rule specifies that a digit can be any single digit from 0 to 9.
    - Example: `0`, `5`, `9`

15. **AddOp -> +**
    - An addition operation.
    - Example: `2 + 3`, `x + y`

16. **AddOp -> -**
    - A subtraction operation.
    - Example: `5 - 3`, `x - y`

17. **MulOp -> ***
    - A multiplication operation.
    - Example: `2 * 3`, `x * y`

18. **MulOp -> /**
    - A division operation.
    - Example: `6 / 3`, `x / y`

19. **ExpOp -> ^**
    - An exponentiation operation.
    - Example: `2 ^ 3`, `x ^ y`

20. **Print -> PRINT**
    - A print operation.
    - Example: `PRINT x`, `PRINT 5 + y`

21. **Input -> INPUT**
    - An input operation.
    - Example: `INPUT x`, `INPUT y + 5`

22. **Assign -> Identifier '=' Expression**
    - An assignment operation, where an identifier is assigned the value of an expression.
    - Example: `x = 2`, `y = x + 3`

23. **Identifier -> Letter**
    - An identifier starts with a letter.
    - Example: `x`, `y`, `result`

24. **Letter -> 'a' | 'b' | ... | 'z' | 'A' | 'B' | ... | 'Z'**
    - A letter can be any lowercase or uppercase alphabetical character.
    - Example: `a`, `b`, `c`, `X`, `Y`, `Z`

These grammar rules define the syntax of the expression language, allowing for the construction of valid arithmetic expressions involving numbers, variables, and basic arithmetic operations. Each rule contributes to forming valid expressions by specifying the allowable combinations and order of elements in the language.

# Input Handling and Tokenization Implementation Explanation

## Regular Expressions Setup:

We define regular expressions (regex) patterns to match various token types in the input expression. Each pattern is associated with a token type, such as numbers, operators, keywords (like `PRINT` and `INPUT`), identifiers, and parentheses.

## Tokenization Function (`tokenize`):

This function iterates over the input expression and attempts to match each part of the expression with the defined regex patterns to identify tokens. It uses a loop to continue processing the input expression until it's fully tokenized. Within the loop, it iterates over the list of regex patterns and tries to match each pattern with the beginning of the remaining input expression using the `match` method. If a match is found, it extracts the matched value and token type, adds them to the list of tokens, and removes the matched portion from the input expression using slicing. If no match is found for any pattern, it raises a `ValueError` indicating that the input expression is invalid.

## Token Storage:

The tokens are stored in a list (`tokens`) to keep track of the extracted tokens.

## Error Handling:

The function handles errors gracefully by raising a `ValueError` with an appropriate error message if the input expression contains invalid characters or syntax.

## Example Usage:

The example usage section prompts the user to enter an arithmetic expression. It calls the `tokenize` function to tokenize the input expression. If the tokenization is successful, it prints the resulting tokens; otherwise, it catches and handles any `ValueError` raised during the tokenization process.

This implementation efficiently tokenizes arithmetic expressions according to the provided grammar rules, enabling further processing such as parsing and evaluation. It utilizes regex patterns to match different token types, making the tokenization process flexible and extensible for handling various expressions.

