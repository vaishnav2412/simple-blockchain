import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions, previous_hash, timestamp=None):
        self.index = index
        self.timestamp = timestamp if timestamp is not None else time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0  # Nonce for Proof-of-Work
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Create a SHA-256 hash of the block's content.
        Any change in the block data will change the hash.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        """
        Implements a simple Proof-of-Work algorithm.
        Increases the nonce until the hash starts with a number of zeroes defined by 'difficulty'.
        """
        prefix = '0' * difficulty
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block {self.index} mined: {self.hash}")

class Blockchain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block of the blockchain: the Genesis Block.
        """
        genesis_block = Block(0, ["Genesis Block"], "0")
        genesis_block.mine_block(self.difficulty)
        return genesis_block

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        """
        Creates and adds a new block with the given transactions.
        The new block is mined to satisfy the Proof-of-Work requirement.
        """
        previous_block = self.get_last_block()
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the blockchain integrity by checking:
        - Every block's hash is correctly calculated.
        - Every block's previous_hash matches the hash of the preceding block.
        - Every block meets the Proof-of-Work requirement.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Verify the current block's hash is correct
            if current.hash != current.calculate_hash():
                print(f"Block {i} has an invalid hash.")
                return False

            # Verify current block's link to the previous block
            if current.previous_hash != previous.hash:
                print(f"Block {i} has an invalid previous hash.")
                return False

            # Verify Proof-of-Work requirement (hash starts with 'difficulty' number of zeroes)
            if not current.hash.startswith('0' * self.difficulty):
                print(f"Block {i} fails the Proof-of-Work requirement.")
                return False

        return True
