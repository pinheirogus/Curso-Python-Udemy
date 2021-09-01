
from datetime import datetime, timedelta
#
# data = datetime(2019, 4, 20, 10, 53, 20)
#
# String format time
# print(data.strftime('%d/%m/%Y %H:%M:%S'))
#
# Time from string , time stamp from date
# data = datetime.strptime('20/04/2019', '%d/%m/%Y').timestamp()
#
# print(data)

# Date from time stamp
# data = datetime.fromtimestamp(1555729200)
#
# print(data)
#
#
# data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
#
# data = data + timedelta(days = 5, seconds=2 * 60, minutes=5)
#
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

# d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
# d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')
#
# diff = d2 - d1
#
# print(diff)
# print(diff.days)
# print(diff.seconds)
# print(diff.total_seconds())
#
# print(d1.time())