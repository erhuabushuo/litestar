import logging
from typing import Generator

import pytest


@pytest.fixture()
def reset_httpx_logging() -> Generator[None, None, None]:
    # ensure that httpx logging is not interfering with our test client
    httpx_logger = logging.getLogger("httpx")
    initial_level = httpx_logger.level
    httpx_logger.setLevel(logging.WARNING)
    yield
    httpx_logger.setLevel(initial_level)
