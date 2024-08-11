from flask import Flask, jsonify, request
from BLOCKCHAIN import Blockchain, GenChain  

app = Flask(__name__)
blockchain = Blockchain(name="MyBlockchain", description="A blockchain for data entries")
gen_chain = blockchain.gen_chain 

@app.route('/list_blocks', methods=['GET'])
def list_blocks():
    blocks = blockchain.list_blocks()
    return jsonify(blocks), 200

@app.route('/search_entries', methods=['GET'])
def search_entries():
    search_term = request.args.get('search_term')
    results = blockchain.search_entries(search_term)
    return jsonify(results), 200

@app.route('/validate_chain', methods=['GET'])
def validate_chain():
    is_valid = blockchain.validate_chain()
    return jsonify({'valid': is_valid}), 200

# Routes for GenChain
@app.route('/list_gen_chain_blocks', methods=['GET'])
def list_gen_chain_blocks():
    gen_chain_blocks = gen_chain.list_blocks()
    return jsonify(gen_chain_blocks), 200

@app.route('/get_gen_chain_block/<int:index>', methods=['GET'])
def get_gen_chain_block(index):
    try:
        block_details = gen_chain.get_block_details(index)
        return jsonify(block_details), 200
    except IndexError as e:
        return jsonify({'error': str(e)}), 404


if __name__ == '__main__':
    app.run(debug=True)
