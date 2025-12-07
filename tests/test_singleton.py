from core.singleton import Singleton

def test_singleton():
    assert Singleton.instance() is Singleton.instance()
