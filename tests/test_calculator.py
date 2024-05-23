import pytest
from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_substract(self):
        # arrange
        a = 3
        b = 1
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected =2
        assert result == expected
    
    def test_multiply(self):
        # arrange
        a = 3
        b = 1
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected =3
        assert result == expected
    
    def test_divide(self):
        # arrange
        a = 3
        b = 1
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected =3
        assert result == expected
        
    def test_divide2(self):
        # arrange
        a = 3
        b = 0
        cal = Calculator()

        # assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)
            