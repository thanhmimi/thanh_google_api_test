import pytest
import logging
from tests.fixtures.fixtures import *


LOGGER = logging.getLogger(__name__)
LOGGER.info('Test print log')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    # set an report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope='session')
def init_logger():
    LOGGER.info('call init_logger')
    return LOGGER



