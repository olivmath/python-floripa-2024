from pytest import fixture


@fixture
def alice(accounts):
    return accounts[0]


@fixture
def flipper(project, alice):
    return alice.deploy(project.Flipper)
