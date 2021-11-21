from pytezos import pytezos
import requests
import json

token = pytezos.using('NODE_ADDRESS')
token = token.contract('TOKEN_ADDRESS')
token_id = 'TOKEN_ID'

token_metadata = list(token.storage['token_metadata'][token_id]()['token_info'].values())[0].decode()
pair1_metadata = pair1_metadata.replace('ipfs://','https://ipfs.io/ipfs/')
pair1_metadata = requests.get(pair1_metadata).json()
