import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions, previous_hash, proof):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "proof": self.proof
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0", 0)
        self.chain.append(genesis_block)
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        while True:
            hash_attempt = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_attempt[:4] == "0000":  # Simple Proof-of-Work Condition
                return new_proof
            new_proof += 1
    
    def add_block(self, transactions):
        last_block = self.chain[-1]
        proof = self.proof_of_work(last_block.proof)
        new_block = Block(len(self.chain), transactions, last_block.hash, proof)
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.previous_hash != previous_block.hash:
                return False
            if current_block.hash != current_block.calculate_hash():
                return False
        return True
    
    def print_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Current Hash: {block.hash}")
            print(f"Proof: {block.proof}")
            print("-" * 40)
    
# Running the Blockchain Simulation
blockchain = Blockchain()
blockchain.add_block(["Alice pays Bob 10 BTC", "Charlie pays Dave 5 BTC"])
blockchain.add_block(["Eve pays Frank 2 BTC"])

print("Blockchain before tampering:")
blockchain.print_chain()

print("Is blockchain valid?", blockchain.is_chain_valid())

# Tampering with blockchain
tampered_block = blockchain.chain[1]
tampered_block.transactions = ["Alice pays Bob 100 BTC"]  # Changing transaction data

print("\nBlockchain after tampering:")
blockchain.print_chain()

print("Is blockchain valid?", blockchain.is_chain_valid())
