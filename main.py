from blockchain import Blockchain

def main():
    # Create a Blockchain instance with desired difficulty (the number of leading zeroes required)
    my_blockchain = Blockchain(difficulty=4)
    
    # Add some blocks with dummy transactions
    my_blockchain.add_block(["Alice pays Bob 10 BTC"])
    my_blockchain.add_block(["Bob pays Charlie 5 BTC"])
    my_blockchain.add_block(["Charlie pays Dave 2 BTC"])

    # Print the blockchain details
    for block in my_blockchain.chain:
        print(f"Block {block.index}:")
        print(f"Timestamp: {block.timestamp}")
        print(f"Transactions: {block.transactions}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Nonce: {block.nonce}")
        print(f"Hash: {block.hash}")
        print("-" * 40)

    # Validate blockchain integrity before tampering
    print("Is blockchain valid?", my_blockchain.is_chain_valid())

    # Tamper with the blockchain to see if the integrity check fails
    print("\nTampering with block 1's data...")
    my_blockchain.chain[1].transactions = ["Alice pays Eve 100 BTC"]
    # Recalculate the block hash to simulate tampering effect
    my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash()

    # Validate blockchain integrity after tampering
    print("After tampering, is blockchain valid?", my_blockchain.is_chain_valid())

if __name__ == "__main__":
    main()
