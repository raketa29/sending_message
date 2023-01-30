import time

from email_validate import validate, validate_or_fail
import datetime
from progressbar import ProgressBar


print(validate(
    email_address="ezhidudek98@gmail.com",
    check_format=True,
    check_blacklist=True,
    check_dns=True,
    dns_timeout=10,
    check_smtp=False,
    smtp_debug=False
))

today = datetime.datetime.today()

print(f"{today:%Y-%m-%d}")
print(f"{today:%Y}")


pbar = ProgressBar(maxval=5)
pbar.start()

for i in range(4):
    pbar.update(i)
    time.sleep(5)

pbar.finish()
