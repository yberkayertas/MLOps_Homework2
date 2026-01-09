# tests/test_code.py
from app.features import get_hashing_index

def test_hashing_consistency():
    # Aynı girdi her zaman aynı sonucu vermeli
    assert get_hashing_index("user_1") == get_hashing_index("user_1")

def test_hashing_range():
    # Sonuç belirlenen aralıkta (0-49) olmalı
    index = get_hashing_index("test", num_buckets=50)
    assert 0 <= index < 50