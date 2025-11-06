import pytest


def test_import_sab_rt():
    try:
        import sab_rt           # noqa
    except ImportError:
        pytest.fail('import sab_rt failed')
