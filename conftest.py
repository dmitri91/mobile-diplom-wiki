import pytest


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import helper.utils.selene.patch_selector_strategy  # noqa
    import helper.utils.selene.patch_element_mobile_commands  # noqa
