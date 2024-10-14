def test_flipper_v2_initial_state(flipper_v2):
    initial_state = flipper_v2.get()
    assert initial_state == False


def test_flipper_v2_change_state_with_flip(flipper_v2, alice):
    assert flipper_v2.get() == False

    flipper_v2.flip(sender=alice)

    assert flipper_v2.get() == True
