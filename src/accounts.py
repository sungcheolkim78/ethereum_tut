from web3 import Web3

w3 = Web3()

acct = w3.eth.account.create()

print(f"{acct.address=}")
print(f"{acct.key=}")
print("-" * 80)

w3 = Web3(Web3.EthereumTesterProvider())

print(f"{w3.eth.accounts=}")

acct_one = w3.eth.accounts[0]
print(f"{w3.eth.get_balance(acct_one)=}")

acct_two = w3.eth.account.create()
print(f"{acct_two.address=}")
print(f"{acct_two.key=}")

# account in EthereumTesterProvider is unlocked
tx_hash = w3.eth.send_transaction({
    'from': acct_one,
    'to': acct_two.address,
    'value': w3.to_wei(1, 'ether')
})
print(f"{tx_hash=}")

print('-' * 80)

# 1) mannually build a transaction
tx = {
    'to': acct_one,
    'value': 10_000_000,
    'gas': 21_000,
    'gasPrice': w3.eth.get_block('pending')['baseFeePerGas'],
    'nonce': 0
}
# 2) sign the transaction with the sender's private key
signed = w3.eth.account.sign_transaction(tx, acct_two.key)

# 3) send the raw transaction
tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
print(f"{tx_hash=}")

print('-' * 80)

# 1) write a message
msg = "this is a small step for mankind"

# 2) sign it with an account's private key
# signed_message = w3.eth.account.sign_message(msg, acct_two.key)

# 3) send `signed_message` over the wire

# 4) message receiver decodes sender's plublic address
# sender = w3.eth.account.decode_message_sender(msg, signed_message.signature)
# print(sender)
