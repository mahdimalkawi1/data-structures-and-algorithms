import pytest
from stack_and_queue.validate_brackets_used_stack import validateBrackets
def test_validate_brackets1():
    output = validateBrackets("{}")
    assert output == True
def test_validate_brackets2():
    output = validateBrackets("{}(){}")
    assert output == True
def test_validate_brackets3():
    output = validateBrackets("()[[Extra Characters]]")
    assert output == True
def test_validate_brackets4():
    output = validateBrackets("(){}[[]]")
    assert output == True
def test_validate_brackets5():
    output = validateBrackets("{}{Code}[Fellows](())")
    assert output == True
def test_validate_brackets6():
    output = validateBrackets("[({}]")
    assert output == False
def test_validate_brackets7():
    output = validateBrackets("(](")
    assert output == False
def test_validate_brackets8():
    output = validateBrackets("{(})")
    assert output == False