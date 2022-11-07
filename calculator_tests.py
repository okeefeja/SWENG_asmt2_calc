from decimal import DivisionByZero
from calculator import evaluate

def test_evaluate():
    # Tests for single operators with integers
    assert evaluate("0+11") == 11
    assert evaluate("0-11") == -11
    assert evaluate("11*2") == 22
    assert evaluate("10/5") == 2
    assert evaluate("0/10") == 0
    assert evaluate("10^0") == 1
    assert evaluate("10^1") == 10
    assert evaluate("10^2") == 100
    assert evaluate("10^-1") == 0.1
    assert evaluate("exp(4)") == 54.598
    assert evaluate("log(4)") == 0.602

    # Tests for single operators with floating-point numbers
    assert evaluate("0.53+2.343") == 2.873
    assert evaluate("4.594-1.23") == 3.364
    assert evaluate("3.46*2.1") == 7.266
    assert evaluate("3.46/2.1") == 1.648
    assert evaluate("10^1.75") == 56.234
    assert evaluate("exp(4.45)") == 85.627
    assert evaluate("log(4.45)") == 0.648

    # Tests for multiple operators without use of brackets
    assert evaluate("11+-3") == 8
    assert evaluate("11+1-3") == 9
    assert evaluate("11+1*3") == 14
    assert evaluate("11+1*3.4") == 14.4
    assert evaluate("11-1*3") == 8
    assert evaluate("11-1*3.4") == 7.6
    assert evaluate("11+4/2") == 13
    assert evaluate("12435+34569-12345*10+50") == eval("12435+34569-12345*10+50")

    # Tests for multiple operators with use of brackets
    assert evaluate("(11-7)+4") == 8
    assert evaluate("(11+7)-4") == 14
    assert evaluate("(11+1)*3") == 36
    assert evaluate("(11+1)/3") == 4
    assert evaluate("(10^2)^-1") == 0.01
    assert evaluate("3+5*exp(4.2)/(5+7)") == 30.786
