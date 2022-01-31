from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


# brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=5777
# brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork='https://eth-mainnet.alchemyapi.io/v2/zX9AB7BRFrB-_BHdkLw-zqjLRxPTBF97' accounts=10 mnemonic=brownie port=8545


def deploy_mocks():
    print(f" the active network is {network.show_active()}")
    print("deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    price_feed_address = MockV3Aggregator[-1].address
    print("mocks deployed")
