import mock
from src.module import (
    main,
    dummy_module
)


def test_dummy_func():
    dummy_module.dummy_func()


@mock.patch('project_name.my_module.dummy_module.dummy_func')
def test_main(mock_dummy_func):
    main()
    mock_dummy_func.assert_called_once()