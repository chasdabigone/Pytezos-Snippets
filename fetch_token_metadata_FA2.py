from pytezos import pytezos
import requests
import json

token = pytezos.using('NODE_ADDRESS')
token = token.contract('TOKEN_ADDRESS')
token_id = 'TOKEN_ID'

token_metadata = list(token.storage['token_metadata'][token_id]()['token_info'].values())[0].decode()
token_metadata = token_metadata.replace('ipfs://','https://ipfs.io/ipfs/')
token_metadata = requests.get(token_metadata).json()
