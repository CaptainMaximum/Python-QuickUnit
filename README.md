# Python-QuickUnit
Create simple unit tests in Python using function decorators

## Why
This is meant mostly to be a toy project to practice using (and abusing) Python function decorators.  QuickUnit provides a framework that allows you to write unit tests for functions as decorators.  This lets you (for better or worse) write unit tests as part of your code in a way that does not disrupt the functionality of the original functions.

## How
Using QuickUnit is pretty simple.  Take, for example, a function that adds two numbers and returns the sum:
```python
def Add(a,b):
    return (a + b)
```
To check that the sum of 2 & 2 is in fact 4 you would simply add the following:
```python
import quickunitlib as quickunit

@quickunit.Equal(expect=4,2,2)
def Add(a,b):
    return (a + b)
```
Currently QuickUnit only provides three types of unit tests:
* `NoException(*args)` takes a list of arguments to pass to the function. Returns a pass if no exception was raised.
* `Equal(expect,*args)` takes an expected value and a list of arguments.  Returns a pass if the function output equals the expected value.
* `NotEqual(notexpect,*args)` takes a value that we explicitly expect not to be returned and a list of arguments.  Returns a pass if the function output does not equal the not-expected value.

Right now class methods cannot be unit tested (since the first argument of a method needs to be an instance of the class, but the class can't be referenced within itself).

## Use
Once you have a source file *test.py* that has functions marked with unit tests, move to the directory of your source code and execute the following:
```
# export PYTHONPATH=/path/to/Python-QuickUnit/src
# export PATH=$PATH:/path/to/Python-QuickUnit/
# quickunit test.py
```
The *quickunit* program is the test runner for the framework that kicks off tests in the order that they were added in the source code, and prints out a quick summary of the tests run.  Do keep in mind that *quickunit* will import your file as a module, so any code that is not bound inside of a function will be executed.

## What it is good at
Testing functions that take very little setup and rely only on input to provide output.  In short, simple stuff.

## What it is not good at
Testing complex setup procedures before calling a function (Need to initialize 5 classes and compute the 341st Fibonacci number before calling your function?  You should just use normal unit tests for that)
Testing any sort of side-effects that your code might produce (There's not really a way to generalize this type of thing, you would have to use something more specific for this)
