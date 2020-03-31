from datetime import datetime

for _ in range(500):
    dt = datetime.now()
    print(dt.microsecond)
