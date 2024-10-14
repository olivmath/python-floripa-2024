from pytest import fixture

@fixture
def alice(accounts):
    return accounts[0]

@fixture
def bob(accounts):
    return accounts[1]

@fixture
def flipper(project, alice):
    return alice.deploy(project.Flipper)

@fixture
def flipper_v2(project, alice):
    return alice.deploy(project.FlipperV2)