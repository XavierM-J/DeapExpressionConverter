# DEAP expression converter

You are using DEAP and your result look like that `mul(cos(add(add(1,2),3)),add(4,5))` ?

You want a "regular" expression instead ? Such as `cos((1+2)+3)*(4+5)` ?

Then this repository has everything you need. This program will convert your Deap expression to a human readable one.

## How to use it ?

Simply import expression.py and use the get_result_expression function on your expression.

## Add more operator

If you need more operator you can add them to the binary/unary operator list at the start of expression.py.

You can also change the token associated with your operator by updating the value_to_token function.

## How does it work ?

This program will parse your expression and create a binary tree associated to it.
Once the tree is done it will parse it to create your result.

