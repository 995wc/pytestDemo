import pytest
from operation.user import register_user


def test_register_user(delete_register_user):
    result = register_user("wintest10", "123456", "13599999999", sex="1", address="深圳市宝安区")
    # print(result.__dict__)
    assert result.success is True, result.error


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_register.py"])
