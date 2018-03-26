
#importing datetime and using a method from it
from datetime import datetime

now = datetime.now()
print now
print now.month()
print now.day()
print now.day()

print '%02d/%02d/%04d' % (now.month, now.day, now.year)