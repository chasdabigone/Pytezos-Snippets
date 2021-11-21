from pytezos import pytezos

token = pytezos.using('NODE_ADDRESS')
token = token.contract('TOKEN_ADDRESS')
token_metadata = token.storage['token_metadata'][0]()[1]
