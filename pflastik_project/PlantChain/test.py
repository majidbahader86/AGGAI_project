import json
import time
from typing import List, Dict, Any
from BLOCK import Block , GenChainBlock
from BLOCKCHAIN import Blockchain, GenChain
from DATAENTERY import DiseaseReport, Dataset, SciencePaper , DataEntry


# Example usage
if __name__ == "__main__":
    # Create instances of each class
    disease_report = DiseaseReport(
        disease_id="D001",
        plant_type="Tomato",
        symptoms="Yellowing leaves, stunted growth",
        diagnosis="Early blight",
        treatment="Use fungicides, prune infected parts",
        date_of_incident="2024-07-01",
        latitude=40.7128,
        longitude=-74.0060,
        submitted_by="John Doe",
        notes="Symptoms observed in greenhouse environment.",
        severity="Moderate",
        environmental_conditions={"temperature": 25, "humidity": 60}
    )

    science_paper = SciencePaper(
        paper_id="P001",
        title="Impact of Climate Change on Crop Yield",
        authors=["Jane Smith", "Michael Johnson"],
        abstract="This paper investigates the effects of climate change on agricultural crop yields.",
        publication_date="2023-05-15",
        journal="Nature Climate Change",
        url="https://example.com/p001",
        keywords=["climate change", "crop yield", "agriculture", "environment"],
        citation_count=100,
        related_topics=["Climate Science", "Agricultural Economics"],
        doi="10.1234/example.doi",
        research_field="Climate Change Science",
        methodology="Statistical analysis of crop yield data"
    )

    dataset = Dataset(
        dataset_id="DS001",
        name="COVID-19 Dataset",
        description="Dataset containing COVID-19 statistics worldwide.",
        creation_date="2020-03-01",
        url="https://example.com/ds001",
        creator="John Doe",
        data_format="CSV",
        size_bytes=1024 * 1024 * 10,  # 10 MB
        license="Open Data License",
        tags=["COVID-19", "pandemic", "public health"],
        version="1.0",
        data_sources=["John Hopkins University", "World Health Organization"],
        data_quality_metrics={"completeness": 0.95, "accuracy": 0.98},
        hash_value="541616511161161651616"  # Hash value will be calculated later
    )

    # Calculate hash value for the dataset
    #dataset.update_hash()

    # Store instances in a list
    data_entries: List[DataEntry] = [disease_report, science_paper, dataset]

    # Iterate through data entries and print their attributes as dictionaries
    for entry in data_entries:
        print(entry.to_dict())
        print("---")

    # Create a block containing these entries
    block_data = [disease_report, science_paper, dataset]

    # Create a genesis block
    genesis_block = Block.create_genesis_block("Genesis Block", "First block in the chain")


    # Create a blockchain instance
    blockchain = Blockchain(name="Test Blockchain", description="A blockchain for testing", gen_chain=True)

    # Create a new block on the main chain 
    new_block = Block(
        index=1,
        previous_hash=genesis_block.hash_value,
        timestamp=time.time(),
        data=block_data,
        block_type="data",
        public_keys=["public_key_1", "public_key_2"],
        hash_value="",  # Hash will be calculated below
        creator="Alice",
        description="Block containing disease report, science paper, and dataset",
        additional_info={"some_info": "additional data"}
    )

     # Calculate hash for the new block
    new_block.hash_value = new_block.calculate_hash()

    # Add the new block to the blockchain
    blockchain.chain.append(new_block)

    # Print the new block as a dictionary
    print(json.dumps(new_block.to_dict(), indent=2))

    # Create a GenChainBlock
    gen_block = GenChainBlock(
        index=0,
        previous_hash="0" * 64,  # Genesis block previous hash
        timestamp=time.time(),
        dna_sequence="ATCGATCGATCG",
        hash_value="examplehashvalue"
    )

    # Print the block's dictionary representation
    print("GenChainBlock:")
    print(json.dumps(gen_block.to_dict(), indent=2))

    # Print the GenChain
    print("GenChain:")
    print(json.dumps(blockchain.gen_chain.list_blocks(), indent=2))

    # Stop the blockchain threads
    blockchain.stop_block_generation()
    if blockchain.gen_chain:
        blockchain.gen_chain.running = False
        if blockchain.thread_gen_chain:
            blockchain.thread_gen_chain.join()
