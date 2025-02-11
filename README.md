
Simple Blockchain Simulation

Project Overview  
This project demonstrates a basic blockchain simulation with core functionalities such as block creation, proof-of-work, chain validation, and tampering detection.  

Features  
Block Structure – Each block contains an index, timestamp, transactions, previous block hash, proof-of-work, and its own hash.  
Proof-of-Work – Uses a simple computational puzzle to validate new blocks.  
Chain Integrity Check – Ensures blocks are correctly linked using cryptographic hashes.  
Tamper Detection – Modifying a block invalidates the entire blockchain.  

Installation & Setup 

1. Clone the Repository  
git clone https://github.com/yourusername/blockchain-simulation.git
cd blockchain-simulation
2. Install Dependencies
Python's built-in modules are sufficient, so no extra installations are required. Ensure you have Python 3 installed.

3. Run the Blockchain Simulation  
python blockchain.py


Code Explanation

1. Block Class  
- Defines the structure of each block.  
- Computes the hash using SHA-256.  

2. Blockchain Class
- Creates a genesis block (first block).  
- Adds new blocks with proof-of-work.  
- Validates the blockchain.  

3. Proof-of-Work
- A simple algorithm that finds a proof value making the hash start with "0000".  

4. Demonstration of Tampering 
- The program modifies a block’s transaction and checks if the blockchain remains valid.  

Example Output 

Blockchain before tampering:
Index: 0
Timestamp: 1707583200.123456
Transactions: Genesis Block
Previous Hash: 0
Current Hash: a1b2c3d4...
Proof: 0
----------------------------------------
Index: 1
Timestamp: 1707583201.567890
Transactions: ['Alice pays Bob 10 BTC', 'Charlie pays Dave 5 BTC']
Previous Hash: a1b2c3d4...
Current Hash: f5e6d7c8...
Proof: 12345
----------------------------------------

Is blockchain valid? True

Tampering with blockchain...

Blockchain after tampering:
Index: 1
Transactions: ['Alice pays Bob 100 BTC']
----------------------------------------

Is blockchain valid? False
Bonus Features
Simple proof-of-work implemented.  
Ability to add transactions before mining.  

Contributors 
samala Pranathi
