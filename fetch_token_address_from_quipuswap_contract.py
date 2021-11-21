from pytezos import pytezos

quipu_contract = pytezos.using('https://rpc.tzbeta.net/')
quipu_contract = pair1.contract('KT1K4EwTpbvYN9agJdjpyJm4ZZdhpUNKB3F6')
token_contract = pair1.storage()['storage']['token_address']
