from discount import calculate_discounted_price
import pytest

def test_premium_discount():
    assert calculate_discounted_price(100, "premium") == 80.00

def test_holiday_discount():
    assert calculate_discounted_price(100, "guest", is_holiday=True) == 95.00