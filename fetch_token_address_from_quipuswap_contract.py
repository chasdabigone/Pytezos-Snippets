from pytezos import pytezos

quipu_contract = pytezos.using('TEZOS_NODE')
quipu_contract = quipu_contract.contract('QUIPUSWAP_DEX_CONTRACT')
token_contract = quipu_contract.storage()['storage']['token_address']
