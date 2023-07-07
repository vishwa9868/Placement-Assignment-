#!/usr/bin/env python
# coding: utf-8

# # Assignment-2

# 1:-What are the two values of the Boolean data type? How do you write them?
#     
#     ANS:-TRUE and FALSE
#         

# 2. What are the three different types of Boolean operators?
# 
# 
# ANS:-
# AND operator: The AND operator returns True if both operands are True, and False otherwise. In programming, it is commonly represented by the symbol and. For example:
# 
# True and True evaluates to True
# True and False evaluates to False
# False and False evaluates to False
# OR operator: The OR operator returns True if at least one of the operands is True, and False otherwise. In programming, it is commonly represented by the symbol or. For example:
# 
# True or False evaluates to True
# False or False evaluates to False
# True or True evaluates to True
# NOT operator: The NOT operator negates the value of the operand. If the operand is True, it returns False, and if the operand is False, it returns True. In programming, it is commonly represented by the keyword not. For example:
# 
# not True evaluates to False
# not False evaluates to True

# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
# 
# ANS:- AND operator('and)
#         
# | Operand 1 | Operand 2 | Result |
# |-----------|-----------|--------|
# |   False   |   False   | False  |
# |   False   |   True    | False  |
# |   True    |   False   | False  |
# |   True    |   True    | True   |
# 
# 
#         OR operator('or)
#         
# | Operand 1 | Operand 2 | Result |
# |-----------|-----------|--------|
# |   False   |   False   | False  |
# |   False   |   True    | True   |
# |   True    |   False   | True   |
# |   True    |   True    | True   |
# 
#  
#  NOT operator('not')
#  
# | Operand | Result |
# |---------|--------|
# |  False  |  True  |
# |  True   | False  |
# 
# 
# 
# These truth tables show all the possible combinations of Boolean values for each operator and the resulting Boolean value when the operator is applied to those operands.
# 
# 

# 4. What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)
# 
# 
# (5 > 4) and (3 == 5)
# 
# The expression (5 > 4) evaluates to True.
# The expression (3 == 5) evaluates to False.
# The and operator returns True only if both operands are True.
# Therefore, (5 > 4) and (3 == 5) evaluates to False.
# not (5 > 4)
# 
# The expression (5 > 4) evaluates to True.
# The not operator negates the value of the operand.
# Therefore, not (5 > 4) evaluates to False.
# (5 > 4) or (3 == 5)
# 
# The expression (5 > 4) evaluates to True.
# The expression (3 == 5) evaluates to False.
# The or operator returns True if at least one of the operands is True.
# Therefore, (5 > 4) or (3 == 5) evaluates to True.
# not ((5 > 4) or (3 == 5))
# 
# The expression (5 > 4) or (3 == 5) evaluates to True.
# The not operator negates the value of the operand.
# Therefore, not ((5 > 4) or (3 == 5)) evaluates to False.
# (True and True) and (True == False)
# 
# The expression (True and True) evaluates to True.
# The expression (True == False) evaluates to False.
# The and operator returns True only if both operands are True.
# Therefore, (True and True) and (True == False) evaluates to False.
# (not False) or (not True)
# 
# The expression not False evaluates to True.
# The expression not True evaluates to False.
# The or operator returns True if at least one of the operands is True.
# Therefore, (not False) or (not True) evaluates to True
# 
# 
# 

# 5. What are the six comparison operators?
# 
# ANS:-Equal to (==): This operator checks if two values are equal and returns True if they are, and False otherwise.
# 
# Not equal to (!=): This operator checks if two values are not equal and returns True if they are not, and False if they are equal.
# 
# Greater than (>): This operator checks if the left operand is greater than the right operand and returns True if it is, and False otherwise.
# 
# Less than (<): This operator checks if the left operand is less than the right operand and returns True if it is, and False otherwise.
# 
# Greater than or equal to (>=): This operator checks if the left operand is greater than or equal to the right operand and returns True if it is, and False otherwise.
# 
# Less than or equal to (<=): This operator checks if the left operand is less than or equal to the right operand and returns True if it is, and False otherwise.

# 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.The equal to operator (==) and the assignment operator (=) serve different purposes and are used in different contexts.
# 
# Equal to operator (==): The equal to operator is used for comparison. It checks whether the values on the left and right sides of the operator are equal. It returns a Boolean value (True or False) based on the comparison result.
# 
# Example:
# 
# python
# Copy code
# x = 5
# y = 10
# result = (x == y)  # Comparing if x is equal to y
# In this example, the expression (x == y) compares the values of x and y to check if they are equal. The result will be False because x is not equal to y.
# 
# Assignment operator (=): The assignment operator is used to assign a value to a variable. It assigns the value on the right-hand side to the variable on the left-hand side.
# 
# Example:
# 
# python
# Copy code
# x = 5  # Assigning the value 5 to the variable x
# y = x  # Assigning the value of x to the variable y
# In this example, the assignment operator (=) is used to assign the value 5 to the variable x. Later, the value of x is assigned to the variable y

# 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')
# 
# ANS:-spam = 0
# if spam == 10:
#     print('eggs')  # Block 1: Inside the "if" statement
# 
# if spam > 5:
#     print('bacon')  # Block 2: Inside the first "if" statement
# 
# else:
#     print('ham')  # Block 3: Inside the "else" statement
# 
# print('spam')  # Outside any conditional block
# print('spam')  # Outside any conditional block
# 
# 
# In this modified code, we have three identified blocks:
# 
# Block 1: Inside the first if statement (if spam == 10). It contains the line print('eggs').
# 
# Block 2: Inside the second if statement (if spam > 5). It contains the line print('bacon').
# 
# Block 3: Inside the else statement that follows the second if statement. It contains the line print('ham').
# 
# The lines print('spam') that appear after the blocks are not part of any conditional block and will be executed unconditionally.
# 

# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
# 
# ANS:-spam = 1  # Assume 1 is stored in spam
# 
# if spam == 1:
#     print("Hello")
# elif spam == 2:
#     print("Howdy")
# else:
#     print("Greetings!")
