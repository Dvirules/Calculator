@echo off
cd Calculator Python
echo A dot (.) indicates a test that has successfully passed.
echo An F indicates a test that has failed (will be shown alongside with the given failure text message set in the testing function)."
echo An E indicates a test that couldn't run due to an error (will be shown alongside with the error message).
python -m unittest unit_testing.py
pause
