from web3 import Web3

# Kết nối với mạng Ethereum
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

# Triển khai DID Document lên blockchain (giả định sử dụng hợp đồng thông minh)
contract_address = "YOUR_CONTRACT_ADDRESS"
abi = [...]  # ABI của hợp đồng
contract = w3.eth.contract(address=contract_address, abi=abi)

# Gửi giao dịch lưu DID Document
def register_did(did, document):
    tx_hash = contract.functions.registerDID(did, json.dumps(document)).transact({
        'from': w3.eth.default_account
    })
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transaction receipt:", receipt)


# lưu DID Document trên Ethereum 
