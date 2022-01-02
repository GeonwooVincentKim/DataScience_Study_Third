import pymysql

import matplotlib
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm
import seaborn as sns

print("matplotlib", matplotlib.__version__)
print("seaborn", sns.__version__)


STATISTICS_EXAMPLE_DB = pymysql.connect(
    user='root',
    passwd='1234',
    host='127.0.0.1',
    db='STATISTICS_EXAMPLE_DB',
    charset='UTF8'
)

cursor = STATISTICS_EXAMPLE_DB.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM `CONTINUOUS_EXAMPLE`";
cursor.execute(sql)

result = cursor.fetchall()

for x in result:
    print(x)

figure, (axes1) = plt.subplots(nrows=1, ncols=1)
plt.show()

# plt.plot(result)
# fig = plt.figure()
# ax = plt.axes(projection='3d')

# ax.plot(xs='')

# plt.show()