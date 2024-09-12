from web3 import Web3

wei = Web3.to_wei(1, 'ether')
print(wei)

gwei = Web3.from_wei(500000000, 'gwei')
print(gwei)

w3 = Web3(Web3.EthereumTesterProvider())

print(w3.is_connected())

print(w3.eth.accounts)

balance = w3.eth.get_balance(w3.eth.accounts[0])
balance_ether = w3.from_wei(balance, 'ether')
print(balance_ether)

print(w3.eth.get_block('latest'))

tx_hash = w3.eth.send_transaction({
    'from': w3.eth.accounts[0],
    'to': w3.eth.accounts[1],
    'value': w3.to_wei(3, 'ether')
})
w3.eth.wait_for_transaction_receipt(tx_hash)
print(w3.eth.get_transaction(tx_hash))

for i in range(2):
    balance = w3.eth.get_balance(w3.eth.accounts[i])
    balance_ether = w3.from_wei(balance, 'ether')
    print(balance_ether)
