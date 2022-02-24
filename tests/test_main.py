from app.main import developer_name


def test_developer_name_success():
    assert developer_name() == 'Felix'


def test_developer_name_error():
    assert developer_name() != 'John'
