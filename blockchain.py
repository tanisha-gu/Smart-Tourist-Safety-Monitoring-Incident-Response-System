import hashlib
import json
from datetime import datetime

blockchain = []

def generate_hash(data):
    encoded = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = {
            "index": self.index,
            "timestamp": str(self.timestamp),
            "data": self.data,
            "previous_hash": self.previous_hash
        }
        return generate_hash(block_data)

def create_genesis_block():
    return Block(0, datetime.utcnow(), "Genesis Block", "0")

blockchain.append(create_genesis_block())

def add_block(data):
    previous_block = blockchain[-1]

    new_block = Block(
        len(blockchain),
        datetime.utcnow(),
        data,
        previous_block.hash
    )

    blockchain.append(new_block)
    return new_block.__dict__
