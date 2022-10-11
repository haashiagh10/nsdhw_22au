import math
import pytest
import _vector
from _vector import pyb11_cal_angle


def test_zero_len():
	with pytest.raises(RuntimeError):
		angle([0,0], [0,0])

def test_zero_ang():
	assert angle([1,1], [1,1]) == pytest.approx(0)

def test_right_ang():
	assert angle([0,1], [1,0]) == pytest.approx(math.pi / 2)
