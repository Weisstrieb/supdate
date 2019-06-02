from hashlib import sha256 as _sha256
from pathlib import Path


def sha256_hexdigest(file: Path):
    if file.exists():
        raise FileNotFoundError(str(file))
    elif not file.is_file():
        raise FileExistsError((str(file)), "is not file")

    return _sha256(file.read_bytes()).hexdigest()


def is_same_file(a: Path, b: Path):
    if not a.exists() or not b.exists():
        return False

    return sha256_hexdigest(a) == sha256_hexdigest(b)
