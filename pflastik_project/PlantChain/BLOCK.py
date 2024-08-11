from typing import List, Union, Dict, Any
from hashlib import sha256
import json
import time
from DATAENTERY import DiseaseReport , SciencePaper, Dataset

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: List[Union[DiseaseReport, SciencePaper, Dataset]], block_type: str, public_keys: List[str], hash_value: str,
                 creator: str = "", description: str = "", additional_info: Dict[str, Any] = None) -> None:
        self.index: int = index
        self.previous_hash: str = previous_hash
        self.timestamp: float = timestamp
        self.data: List[Union[DiseaseReport, SciencePaper, Dataset]] = data
        self.block_type: str = block_type
        self.public_keys: List[str] = public_keys
        self.hash_value: str = hash_value  # Ensure hash_value is initialized in constructor
        self.creator: str = creator
        self.description: str = description
        self.additional_info: Dict[str, Any] = additional_info if additional_info else {}

    def to_dict(self) -> Dict[str, Any]:
        block_dict = {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": [entry.to_dict() if hasattr(entry, 'to_dict') else entry.__dict__ for entry in self.data],
            "block_type": self.block_type,
            "public_keys": self.public_keys,
            "hash_value": self.hash_value,  # Include hash_value in the dictionary
            "creator": self.creator,
            "description": self.description,
            "additional_info": self.additional_info
        }
        return block_dict

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block.
        """
        serialized_data = []
        for entry in self.data:
            if hasattr(entry, 'to_dict'):
                serialized_data.append(json.dumps(entry.to_dict()))
            else:
                serialized_data.append(json.dumps(entry.__dict__))

        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{''.join(serialized_data)}{self.block_type}{json.dumps(self.public_keys)}{self.creator}{self.description}{json.dumps(self.additional_info)}"
        return sha256(block_string.encode()).hexdigest()

    @staticmethod
    def create_genesis_block(name: str, description: str) -> 'Block':
        """
        Creates the genesis block of the blockchain.
        """
        index = 0
        previous_hash = "0" * 64  # Initial hash for the first block
        timestamp = time.time()
        data = []  # Genesis block typically has no data initially
        block_type = "genesis"
        public_keys = []
        creator = ""
        additional_info = {
            "name": name,
            "description": description
        }
        # Calculate hash for the genesis block
        hash_value = Block.hash_block(index, previous_hash, timestamp, data, block_type, public_keys, creator, description, additional_info)
        return Block(index, previous_hash, timestamp, data, block_type, public_keys, hash_value, creator, description, additional_info)

    @staticmethod
    def hash_block(index: int, previous_hash: str, timestamp: float, data: List[Union[DiseaseReport, SciencePaper, Dataset]], block_type: str, public_keys: List[str],
                   creator: str = "", description: str = "", additional_info: Dict[str, Any] = None) -> str:
        """
        Computes the hash of a block.
        """
        serialized_data = []
        for entry in data:
            if hasattr(entry, 'to_dict'):
                serialized_data.append(json.dumps(entry.to_dict()))
            else:
                serialized_data.append(json.dumps(entry.__dict__))

        block_string = f"{index}{previous_hash}{timestamp}{''.join(serialized_data)}{block_type}{json.dumps(public_keys)}{creator}{description}{json.dumps(additional_info)}"
        return sha256(block_string.encode()).hexdigest()
    
class GenChainBlock:
    def __init__(self, index: int, previous_hash: str, timestamp: float, dna_sequence: str, hash_value: str) -> None:
        self.index: int = index
        self.previous_hash: str = previous_hash
        self.timestamp: float = timestamp
        self.dna_sequence: str = dna_sequence
        self.hash: str = hash_value

    def to_dict(self) -> Dict[str, Any]:
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "dna_sequence": self.dna_sequence,
            "hash": self.hash
        }
