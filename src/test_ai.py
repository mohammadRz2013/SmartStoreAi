import pytest
from main import ai
from main import database

def test_mobile_s():
    assert 'Samsung Galaxy S25' in ai('samsungMobile')

def test_mobile_ap():
    assert 'iphone16' in ai('i phone 16 mobile')

def test_short():
    assert 'Nike Running Shorts' in ai('Lightweight running shorts from Nike')

def test_db():
    data = database()
    for i in data:
        assert type(i) == tuple
