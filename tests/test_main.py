from datetime import datetime

from filetime import from_datetime, to_datetime, utc


def test_from_datetime():
	assert from_datetime(datetime(2009, 7, 25, 23, 0)) == 128930364000000000
	assert from_datetime(datetime(1970, 1, 1, 0, 0, tzinfo=utc)) == 116444736000000000
	assert from_datetime(datetime(1970, 1, 1, 0, 0)) == 116444736000000000
	assert from_datetime(datetime(2009, 7, 25, 23, 0, 0, 100)) == 128930364000001000


def test_to_datetime():
	assert to_datetime(116444736000000000) == datetime(1970, 1, 1, 0, 0)
	assert to_datetime(128930364000000000) == datetime(2009, 7, 25, 23, 0)
	assert to_datetime(128930364000001000) == datetime(2009, 7, 25, 23, 0, 0, 100)
