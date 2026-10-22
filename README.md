# Content Addressing

Canonical JSON fingerprints for repeatable content identity.

Sorted JSON keys and compact separators produce a stable SHA-256 fingerprint. Non-finite JSON numbers are rejected.

## Run

Python 3.11 or newer; no external packages.

```sh
python main.py
python -m unittest discover -s tests -v
```

The module exposes its calculation as an importable function and includes a runnable example.
