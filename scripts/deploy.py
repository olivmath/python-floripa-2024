from ape import project, accounts

def main():

    owner = accounts.load("my_wallet")
    owner.deploy(project.Flipper)
    owner.deploy(project.FlipperV2)