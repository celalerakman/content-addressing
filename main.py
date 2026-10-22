"""Canonical JSON content addresses for idempotent artifact handling."""
import hashlib
import json


def content_key(payload):
    encoded = json.dumps(payload, sort_keys=True, separators=(',', ':'), allow_nan=False)
    return hashlib.sha256(encoded.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    print(content_key({'project':'school-a', 'revision':3}))
