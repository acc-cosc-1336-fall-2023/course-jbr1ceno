import unittest
import value_return

from datetime import datetime

hour = str(value_return.get_hour(3800)).zfill(2)
minute = str(value_return.get_minutes(3800)).zfill(2)
second = str(value_return.get_seconds(3800)).zfill(2)

print(hour + ":" + minute + ":" + second)