def test_user_not_is_staff(user):
    assert user.is_staff == 0


def test_user_get_full_name(user):
    assert user.get_full_name() == f'{user.first_name} {user.last_name}'.strip()


def test_user_get_short_name(user):
    assert user.get_short_name() == f'{user.first_name}'
