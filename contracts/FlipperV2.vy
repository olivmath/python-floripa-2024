# @version ^0.3.7


state: public(bool)

@external
def __init__():
    self.state = False

@external
def flip():
    self.state = not self.state

@external
@view
def get_state() -> bool:
    return self.state
