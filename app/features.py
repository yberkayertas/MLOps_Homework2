import hashlib


def get_hashing_index(input_string: str, num_buckets: int = 1000):
    """High-cardinality veriler için hashing logic."""
    if not isinstance(input_string, str):
        input_string = str(input_string)
    hash_object = hashlib.md5(input_string.encode())
    return int(hash_object.hexdigest(), 16) % num_buckets


