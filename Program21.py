import time
print(time.asctime())
print(time.timezone)

from time import asctime
print(asctime())

from time import asctime,sleep
print(asctime())
sleep(3)
print(asctime())

import sys
for path in sys.path:
    print(path)