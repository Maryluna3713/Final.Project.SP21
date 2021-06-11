import pytest
import mock
import builtins

from my_module_classes import Billy 

def chat_w_Billy():
    
     
    billy = Billy()
    billy.hi_billy()
    
def test_high_intensity():
    billy = Billy()
    assert callable(billy.high_intensity)
    assert isinstance(billy.high_intensity(),str)
    assert billy.high_intensity() == "Hmm, maybe getting a massage is more up your alley?\n"

def test_low_intensity():
    billy = Billy()
    assert callable(billy.low_intensity)
    assert isinstance(billy.low_intensity(),str)
    assert billy.low_intensity() == 'Would you be open to meditating?\n'
    
#use stack overflows reccommendations for input assert
def test_hi_billy():
    billy = Billy()
    assert callable(billy.hi_billy)
    with mock.patch.object(builtins, 'input', lambda _: 'Maria'):
        assert (billy.hi_billy() == None  )
