from mlproject.distance import haversine

def test_haversine():
    assert haversine(0, 0, 0, 0) == 0
