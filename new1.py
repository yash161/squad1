from pydruid.client import *
from pylab import plt

query = PyDruid("http://localhost:8888", 'druid/v2')

ts = query.scan(
    datasource='inline_data_test',
    granularity='day',
     intervals=[ "-146136543-09-08T08:23:32.096Z/146140482-04-24T15:36:27.903Z"],
   
)
df = query.export_pandas()
print(df)
# df['timestamp'] = df['timestamp'].map(lambda x: x.split('T')[0])
# df.plot(x='timestamp', y='avg_tweet_length', ylim=(80, 140), rot=20,
#         title='Sochi 2014')
# plt.ylabel('avg tweet length (chars)')
# plt.show()