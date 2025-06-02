import pytest
from aufgaben_package.rechen_operation import erhoehe_um_zwei,multipliziere_mit_drei,subtrahiere_zehn,teile_durch_vier

def test_erhoehe_um_zwei():
    assert erhoehe_um_zwei(2) == 4
    assert erhoehe_um_zwei(42) == 44
    assert erhoehe_um_zwei(-2) == 0

def test_multipliziere_mit_drei():
    assert multipliziere_mit_drei(3) == 9
    assert multipliziere_mit_drei(21) == 63
    assert multipliziere_mit_drei(1) == 3

def test_subtrahiere_zehn():
    assert subtrahiere_zehn(11) == 1
    assert subtrahiere_zehn(10) == 0
    assert subtrahiere_zehn(5) == -5

def test_teile_durch_vier():
    assert teile_durch_vier(4) == 1
    assert teile_durch_vier(16) == 4
    assert teile_durch_vier(2) == 0.5
