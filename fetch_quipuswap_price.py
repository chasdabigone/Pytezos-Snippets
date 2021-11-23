from pytezos import pytezos
import json
import requests

quipu_contract = pytezos.using('TEZOS_NODE')
quipu_contract = quipu_contract.contract('QUIPUSWAP_DEX_CONTRACT')

# get token contract address
token_addr = quipu_contract.storage()['storage']['token_address']
token_contract = pytezos.using('TEZOS_NODE')
token_contract = pair1_token.contract(token_addr)

# this will check if it is FA1 or FA2 token
token_id = None
try: 
    token_id = token_contract.storage()['storage']['token_id']
except KeyError:
    pass
    
if token_id is None: # grab metadata if FA1
    token_metadata = token_contract.storage['token_metadata'][0]()[1]
    
else: # grab metadata if FA2
    token_metadata = list(token_contract.storage['token_metadata'][token_id]()['token_info'].values())[0].decode()
    token_metadata = token_metadata.replace('ipfs://','https://ipfs.io/ipfs/')
    token_metadata = requests.get(token_metadata).json()
    
# fetch token mantissa
token_decimals = int(token_metadata['decimals'].decode())
    
# compute token price
price = (quipu_contract.storage()['storage']['token_pool'] / Math.pow(10, token_decimals)) / (quipu_contract.storage()['storage']['tez_pool'] / 1e6)
