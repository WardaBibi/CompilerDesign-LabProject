### Grammar Rules



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

### Explanation

These grammar rules define the syntax of the expression language, allowing for the construction of valid arithmetic expressions involving numbers, variables, and basic arithmetic operations. Each rule contributes to forming valid expressions by specifying the allowable combinations and order of elements in the language.
