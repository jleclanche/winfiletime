from calendar import timegm
from datetime import datetime, timezone

EPOCH_AS_FILETIME = 116444736000000000  # January 1, 1970 as filetime
HUNDREDS_OF_NS = 10000000


def from_datetime(dt: datetime) -> int:
	"""
	Converts a datetime to a Windows filetime. If the object is
	time zone-naive, it is forced to UTC before conversion.
	"""

	if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
		dt = dt.replace(tzinfo=timezone.utc)

	filetime = EPOCH_AS_FILETIME + (timegm(dt.timetuple()) * HUNDREDS_OF_NS)
	return filetime + (dt.microsecond * 10)


def to_datetime(filetime: int) -> datetime:
	"""
	Converts a Windows filetime number to a Python datetime. The new
	datetime object is timezone-naive but is equivalent to tzinfo=utc.
	"""

	# Get seconds and remainder in terms of Unix epoch
	s, ns100 = divmod(filetime - EPOCH_AS_FILETIME, HUNDREDS_OF_NS)
	# Convert to datetime object, with remainder as microseconds.
	return datetime.utcfromtimestamp(s).replace(microsecond=(ns100 // 10))
