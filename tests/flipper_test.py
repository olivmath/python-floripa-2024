def test_flipper_initial_state(flipper):
    initial_state = flipper.get()
    assert initial_state == False


def test_flipper_change_state_with_flip(flipper, alice):
    assert flipper.get() == False

    flipper.flip(sender=alice)

    assert flipper.get() == True
