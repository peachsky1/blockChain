# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import logging
import sys
import time

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


class BlockChain(object):
    def __init__(self):
        # generating transction pool list
        self.transaction_pool = []
        # Chain list
        self.chain = []
        # self hash
        self.create_block(0, 'init hash')

    def create_block(self, nonce, previous_hash):
        block = {
            'timestamp': time.time(),
            'transactions': self.transaction_pool,
            'nonce': nonce,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        self.transaction_pool = []
        return block

def pprint(chains):
    for i, chain in enumerate(chains):
        print(f'{"="*25} Chain {i} {"="*25}')
        for k, v in chain.items():
            #lenght 15 for some width space val of 15
            print(f'{k:15}{v}')
    print(f'{"*"*25}')


if __name__ == '__main__':
    block_chain = BlockChain()
    pprint(block_chain.chain)
    block_chain.create_block(5, 'hash1')
    pprint(block_chain.chain)
    block_chain.create_block(3, 'hash2')
    pprint(block_chain.chain)
