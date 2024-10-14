# @version ^0.3.7


state: bool

@external
def __init__():
    self.state = False

@external
def flip():
    self.state = not self.state

@external
@view
def get() -> bool:
    return self.state
