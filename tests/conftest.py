import pytest
from backend.utils.timezone import now_cet
from datetime import timedelta


@pytest.fixture
def sample_start_time():
    return now_cet()


@pytest.fixture
def sample_end_time(sample_start_time):
    return sample_start_time + timedelta(hours=8, minutes=30)
