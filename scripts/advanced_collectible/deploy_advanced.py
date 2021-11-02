from brownie import AdvancedCollectible, accounts, network, config


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(dev)
    print(network.show_active())
