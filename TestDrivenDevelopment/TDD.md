# TEST DRIVEN DEVELOPMENT
Also known as Unit Testing

The practice of writing your tests before you write the code, making sure that the code fits the tasks that it needs to do

It forces you to consider the design of the code

Makes sure that all your code is covered by tests, nothing is left out - At any point, you can test out the scrips meaning that you can make more changes without worrying if you've broken something.

### Three rules of TDD
- You can't write any production code until you've written failing tests
- You can't write more of a test than is required for it to fail (Keep it consise)
- You can't write any more code than is required to pass the tests

This builds into clean code and easily-readable/composed code.

Naming convention is to name the testing file "test_filename" so that you can see which file that page is testing

If you find a new problem that isn't covered in unit testing, it's a good practice to add a test for this problem so that you don't revisit the same issues. 

In this repo, we're using the unittest module in python to test our script

There are a bunch of assert types included in this module, found (here)[https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug]

##### Running Tests
Instead of just running the file in terminal like standard `python3 test_calc.py`, instead you need to do `python3 -m unittest test_calc.py` to tell python to run it as a testing file

Otherwise, you can use the first command if you have the "dunder name == dunder main" statement in the test_calc.py page

##### Setup and Teardown methods
These have to be camel case, setUp() and tearDown()
These will run before and after every single test
They're useful for keeping your code DRY
You can also create setUpClass() and tearDownClass() classmethods

##### Mocking
If your code relies on something external (IE pulling info down from a website), mocking is a technique that is  used to make sure that the test is testing your code, not testing that external feature

For example, Mocking can return fake information from a website you're trying to pull from if the website is down

This uses a separate part of the unittest module `from unittest.mock import patch`

Patch can be used as a decorator or as a context manager.

While a good tool, it's a good idea to try and avoid using it unless you have to. You don't want to rely on faking responses
