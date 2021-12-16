import time
import json
import web3
from eth_account import Account
from web3.auto import w3
from web3.providers.websocket import WebsocketProvider
from web3 import Web3
from solc import compile_standard

with open("Greeter.sol") as c:
contractText=c.read()
with open(".pk") as pkfile:
privateKey=pkfile.read()
with open(".infura") as infurafile:
infuraKey=infurafile.read()

compiled_sol = compile_standard(contractText)

web3.py instance
w3 = Web3(Web3.EthereumTesterProvider())

set pre-funded account as sender
w3.eth.default_account = w3.eth.accounts[0]

get bytecode
bytecode = compiled_sol['contracts']['Greeter.sol']['Greeter']['evm']['bytecode']['object']

get abi
abi = json.loads(compiled_sol['contracts']['Greeter.sol']['Greeter']['metadata'])['output']['abi']

Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

greeter = w3.eth.contract(
address=tx_receipt.contractAddress,
abi=abi)

greeter.functions.greet().call()
'Hello'

tx_hash = greeter.functions.setGreeting('Nihao').transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
greeter.functions.greet().call()
'Nihao'
