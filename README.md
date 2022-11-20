This little project's main goal was to practice OOP, SOLID and RESTful API with Flask and Python. It also includes some Unit Testing with "unittest" library.

To run project:
Run the "run.sh" script file using git.

The output will instruct you to open http://127.0.0.1:5000, from there you can send HTTP requests with the desired input to the project, on path "http://127.0.0.1:5000/(mathematical-expression)/(extension)".

The only extension implemented ATM is "color" which will result with returning a JSON containing the result of the "mathematical-expression" and a color: green if the result is even, or red if it is odd. Of course, the main goal of that is to show that implementing new extensions and mathematical operations is possible while adhering to SOLID and not violating it (mainly regarding the Open/closed principle).

*Please do note that the division sign should be " : " and not " / " .

For Unit Testing run the "unitTesting.bat" script file.
