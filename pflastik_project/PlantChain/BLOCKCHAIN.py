from typing import List, Union, Dict, Any
import threading
import time
import logging
import json
from hashlib import sha256
from queue import Queue
from BLOCK import Block , GenChainBlock
from DATAENTERY import DiseaseReport, SciencePaper, Dataset, DataEntry
from crypto_utils import generate_key_pair, sign_data, verify_signature
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.backends import default_backend
from colorama import Fore, Style 

# Initialize colorama
Fore.GREEN = '\033[92m'  # Define green color for console output
Style.RESET_ALL = '\033[0m'  # Reset colorama style


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GenChain:
    def __init__(self, name: str, description: str = "", version: float = 1.00) -> None:
        self.name: str = name
        self.description: str = description
        self.version = version
        self.chain: List[GenChainBlock] = []
        self.running = True
        self.thread: threading.Thread = None


    def create_genesis_block(self) -> None:
            """
            Creates the genesis block (first block in the blockchain).
            """
            genesis_block = Block(
                index=0,
                previous_hash="",
                timestamp=time.time(),
                data=[],
                hash="",
                public_keys=[]
            )
            self.chain.append(genesis_block)

    def add_block(self, block: GenChainBlock) -> None:
        self.chain.append(block)

    def mine_block(self, block_data: str, previous_hash: str) -> GenChainBlock:
        index = len(self.chain)
        timestamp = time.time()
        dna_sequence = self.tokenize_to_dna(block_data)
        hash_value = self.hash_block(index, previous_hash, timestamp, dna_sequence)
        block = GenChainBlock(index, previous_hash, timestamp, dna_sequence, hash_value)
        return block

    def hash_block(self, index: int, previous_hash: str, timestamp: float, dna_sequence: str) -> str:
        block_string = f"{index}{previous_hash}{timestamp}{dna_sequence}"
        return sha256(block_string.encode()).hexdigest()

    def tokenize_to_dna(self, data: str) -> str:
        binary_data = ''.join(format(ord(char), '08b') for char in data)
        dna_sequence = ''
        for i in range(0, len(binary_data), 2):
            if binary_data[i:i+2] == '00':
                dna_sequence += 'A'
            elif binary_data[i:i+2] == '01':
                dna_sequence += 'C'
            elif binary_data[i:i+2] == '10':
                dna_sequence += 'G'
            elif binary_data[i:i+2] == '11':
                dna_sequence += 'T'
        return dna_sequence
    
    def list_blocks(self, max_blocks: int = 1000) -> List[Dict[str, Any]]:
        """
        Provides a summary of the last `max_blocks` blocks in the GenChain.
        """
        start_index = max(0, len(self.chain) - max_blocks)
        block_summaries = []
        for block in self.chain[start_index:]:
            block_summaries.append({
                "index": block.index,
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(block.timestamp)),
                "dna_sequence": block.dna_sequence,
                "previous_hash": block.previous_hash,
                "hash": block.hash,
            })
        return block_summaries
    

    def get_block_details(self, index: int) -> Dict[str, Any]:
        """
        Retrieves details of a specific block in the GenChain identified by index.
        """
        if 0 <= index < len(self.chain):
            block = self.chain[index]
            return {
                "index": block.index,
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(block.timestamp)),
                "dna_sequence": block.dna_sequence,
                "previous_hash": block.previous_hash,
                "hash": block.hash,
            }
        else:
            raise IndexError("Block index out of range")

    def __repr__(self) -> str:
        return f"GenChain(name={self.name}, description={self.description}, chain_length={len(self.chain)})"

class Blockchain:
    def __init__(self, name: str, description: str = "", version: float = 1.00, gen_chain: bool = False) -> None:
        self.name: str = name
        self.description: str = description
        self.chain: List[Block] = []
        self.pending_data: Queue = Queue()
        self.pending_public_keys: Dict[str, List[DataEntry]] = {}
        self.running = True
        self.version = version
        self.birth_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.create_genesis_block()
        self.start_block_generation()

        if gen_chain:
            self.gen_chain = GenChain(name="GenChain for " + name)
            self.thread_gen_chain = threading.Thread(target=self.generate_gen_chain_blocks)
            self.thread_gen_chain.start()
        else:
            self.gen_chain = None
            self.thread_gen_chain = None

    def create_genesis_block(self) -> None:
        """
        Creates the genesis block (first block in the blockchain).
        """
        genesis_block = Block.create_genesis_block(self.name, self.description)
        self.chain.append(genesis_block)


    def generate_gen_chain_blocks(self):
        try:
            while self.running:
                time.sleep(2)
                
                if not self.gen_chain.chain:
                    previous_hash = "0" * 64
                    print("No blocks in genetic chain. Setting previous_hash to all zeros.")
                else:
                    previous_hash = self.gen_chain.chain[-1].hash
                    print(f"Previous hash set to last block hash in genetic chain: {previous_hash}")

                if self.chain:
                    latest_block = self.chain[-1]
                    block_data = json.dumps(latest_block.to_dict())
                    # print(f"Latest block in main chain: {block_data}")
                else:
                    block_data = "No blocks in main chain"
                    print("No blocks in main chain")

                try:
                    block_data_hash = sha256(block_data.encode()).hexdigest()
                    print(f"Hash of block data: {block_data_hash}")

                    concatenated_data = f"{block_data_hash}{block_data}"
                    
                    binary_data = ''.join(format(ord(char), '08b') for char in concatenated_data)

                    #  B2DNA
                    dna_sequence = self.gen_chain.tokenize_to_dna(binary_data)
                    # print(f"Generated DNA sequence: {dna_sequence}")

                    new_block = self.gen_chain.mine_block(dna_sequence, previous_hash)

                    self.gen_chain.add_block(new_block)
                    # print(f"Added new block to genetic chain: {new_block}")

                    dna_icon = "🧬"
                    logger.debug(Fore.GREEN + f"Generated new {dna_icon} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}" + Style.RESET_ALL)

                except Exception as e:
                    logger.error(f"Error generating genetic chain block: {str(e)}")
                    print(f"Error generating genetic chain block: {str(e)}")

        except Exception as e:
            logger.error(f"Unexpected error in generate_gen_chain_blocks: {str(e)}")
            print(f"Unexpected error in generate_gen_chain_blocks: {str(e)}")


    def create_block(self, data: Dict[str, List[DataEntry]], block_type: str, previous_hash: str) -> Block:
        index = len(self.chain)
        timestamp = time.time()
        block_hash = Block.hash_block(index, previous_hash, timestamp, data, block_type, [])
        return Block(index, previous_hash, timestamp, data, block_type, [], block_hash)

    def add_block(self, data: Dict[str, List[DataEntry]], block_type: str) -> Block:
        previous_block = self.chain[-1]
        new_block = self.create_block(data, block_type, previous_block.hash_value)
        self.chain.append(new_block)
        return new_block

    def mine_pending_data(self) -> None:
        """
        Mines the pending data into a new block.
        """
        if not self.pending_data.empty():
            data_entries = {}
            while len(data_entries) < 1000 and not self.pending_data.empty():  # Assuming a block can hold up to 1000 public key entries
                public_key, entry = self.pending_data.get()
                if public_key not in data_entries:
                    data_entries[public_key] = []
                data_entries[public_key].append(entry)
            if data_entries:
                new_block = self.add_block(data_entries, "data")
                logger.debug(f"Generated new block with index {new_block.index} and hash {new_block.hash_value} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")

    def generate_empty_block(self) -> None:
        """
        Generates an empty block every 2 seconds if there are no pending data entries.
        """
        while self.running:
            time.sleep(2)
            if self.pending_data.empty():
                previous_block = self.chain[-1]
                empty_block = self.create_block({}, "empty", previous_block.hash_value)
                self.chain.append(empty_block)
                logger.debug(f"Generated new empty block with index {empty_block.index} and hash {empty_block.hash_value} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")

    def start_block_generation(self) -> None:
        """
        Starts the continuous block generation process in a separate thread.
        """
        self.thread = threading.Thread(target=self.generate_empty_block)
        self.thread.start()

    def stop_block_generation(self) -> None:
        """
        Stops the continuous block generation process.
        """
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()

    def validate_chain(self) -> bool:
        """
        Validates the entire blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash_value != Block.hash_block(current_block.index, previous_block.hash_value, current_block.timestamp, current_block.data, current_block.block_type, current_block.public_keys):
                logger.error(f"Block {current_block.index} hash mismatch detected.")
                return False

            if current_block.previous_hash != previous_block.hash_value:
                logger.error(f"Block {current_block.index} previous hash mismatch detected.")
                return False

        return True

    def submit_data(self, data_entries: List[DataEntry], public_key_str: str, private_key_str: str) -> None:
        """
        Submits multiple data entries to the blockchain. The data is signed with the user's private key and verified with the public key.
        """
        private_key = load_pem_private_key(private_key_str.encode(), password=None, backend=default_backend())
        public_key = load_pem_public_key(public_key_str.encode(), backend=default_backend())

        for data_entry in data_entries:
            # Serialize and sign each data entry
            data_str = json.dumps(data_entry.to_dict())
            signature = sign_data(private_key, data_str)

            # Verify the signature
            if verify_signature(public_key, data_str, signature):
                self.pending_data.put((public_key_str, data_entry))
            else:
                raise ValueError("Invalid signature. Data entry cannot be submitted.")

    def search_entries(self, search_term: str) -> List[Dict[str, Any]]:
        """
        Searches for entries matching the search term across all blocks.
        """
        results = []
        for block in self.chain:
            for public_key, entries in block.data.items():
                for entry in entries:
                    if isinstance(entry, DiseaseReport) and (search_term.lower() in entry.plant_type.lower() or search_term.lower() in entry.symptoms.lower()):
                        results.append(entry.to_dict())
                    elif isinstance(entry, SciencePaper) and (search_term.lower() in entry.title.lower() or search_term.lower() in entry.authors):
                        results.append(entry.to_dict())
                    elif isinstance(entry, Dataset) and (search_term.lower() in entry.name.lower() or search_term.lower() in entry.description.lower()):
                        results.append(entry.to_dict())
        return results

    def list_blocks(self) -> List[Dict[str, Any]]:
        """
        Provides a summary of all blocks in the blockchain.
        """
        block_summaries = []
        for block in self.chain:
            block_summaries.append({
                "index": block.index,
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(block.timestamp)),
                "block_type": block.block_type,
                "data_count": sum(len(entries) for entries in block.data.values()),
                "previous_hash": block.previous_hash,
                "hash": block.hash_value,
                "creator": block.creator,
                "description": block.description,
                "additional_info": block.additional_info
            })
        return block_summaries

    def __repr__(self) -> str:
        return f"Blockchain(name={self.name}, description={self.description}, chain_length={len(self.chain)}, birth_date={self.birth_date}, version={self.version})"
