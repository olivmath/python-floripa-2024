def test_flipper_initial_state(flipper):
    initial_state = flipper.get()
    assert initial_state == True


def test_flipper_change_state_with_flip(flipper, alice):
    assert flipper.get() == True

    flipper.flip(sender=alice)

    assert flipper.get() == False
