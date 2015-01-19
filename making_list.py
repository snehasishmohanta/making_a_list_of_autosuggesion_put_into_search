"""
i am having two files
i) search.txt
ii) autosuggest.txt

here what i need to do is, i have to find all the autosuggesion quesry of any search query between the time interval of 
15 second prior to search query.and make  list of all the partial query and put into search.txt with the new column for each query.
search.txt
-----------
19:00:15  , mouse , FALSE
19:00:15  , branded luggage bags and trolley , TRUE
19:00:15  , Leather shoes for men , FALSE
19:00:15  , printers , TRUE
19:00:15  , REPLACEMENT BACK HARD FLIP CASE COVER FOR Micromax Canvas Nitro A310[BLACK] , FALSE
19:00:16  , adidas watches for men , TRUE
19:00:16  , Mobile Charger Stand/Holder black , FALSE
19:00:16  , watches for men , TRUE

autosuggest.txt
----------------
19:00:00 ,  trakjkfsa,
19:00:00 ,  door,
19:00:00 ,  sweater,
19:00:00 ,  sweater,
19:00:00 ,  sweater,
19:00:00 ,  dis,
19:00:01 ,  not,
19:00:01 ,  nokia,
19:00:01 ,  collar,
19:00:01 ,  nokia,
19:00:01 ,  collar,
19:00:01 ,  gsm,
19:00:01 ,  sweater,
19:00:01 ,  sweater,
19:00:01 ,  gsm,
19:00:02 ,  gsm,
19:00:02 ,  show,
19:00:02 ,  wayfreyerv,
19:00:02 ,  door,
19:00:02 ,  collar,
19:00:02 ,  or,
19:00:02 ,  harman,
19:00:02 ,  women's,
19:00:02 ,  collar,
19:00:02 ,  sweater,
19:00:02 ,  head,
19:00:03 ,  womanw,
19:00:03 ,  com.shopclues.utils.k@42233ff0,
19:00:03 ,  samsu,
19:00:03 ,  adidas,
19:00:03 ,  collar,
19:00:04 ,  ambas,
19:00:04 ,  harman,
19:00:04 ,  mi,
19:00:04 ,  nor,
19:00:04 ,  airtel,
19:00:04 ,  ,
19:00:04 ,  adid,
19:00:05 ,  harman,
19:00:05 ,  collar,
19:00:05 ,  flip,
19:00:05 ,  brass,
19:00:05 ,  laptop,
19:00:05 ,  collar,
19:00:05 ,  wayfreyer,
19:00:05 ,  head,
19:00:05 ,  adidas,
19:00:05 ,  discn,
19:00:05 ,  head,
19:00:05 ,  adidas,
19:00:05 ,  collar,
19:00:05 ,  collar,
19:00:06 ,  disco,
19:00:06 ,  head,
19:00:06 ,  harman,
19:00:06 ,  nigh,
19:00:06 ,  microsoft,
19:00:06 ,  ambassado,
19:00:07 ,  salwar,
19:00:07 ,  bb,
19:00:07 ,  harman,
19:00:07 ,  ambassador,
19:00:07 ,  ambassador,
19:00:07 ,  salwar,
19:00:08 ,  microsoft,
19:00:08 ,  ac,
19:00:08 ,  jea,
19:00:08 ,  gens,
19:00:08 ,  ambassador,
19:00:08 ,  orpa,
19:00:09 ,  ac,
19:00:09 ,  black,
19:00:09 ,  asus,
19:00:09 ,  salwar,
19:00:09 ,  salwar,
19:00:09 ,  ac,
19:00:10 ,  whechains,
19:00:10 ,  gens,
19:00:10 ,  ambassador,
19:00:10 ,  sony,
19:00:10 ,  salwa,
19:00:10 ,  ac,
19:00:10 ,  woman,
19:00:10 ,  li,
19:00:11 ,  boxers,
19:00:11 ,  harman,
19:00:11 ,  sal,
19:00:11 ,  ambassador,
19:00:11 ,  sony,
19:00:11 ,  ,
19:00:11 ,  boxers,
19:00:12 ,  adidas,
19:00:12 ,  samsung,
19:00:12 ,  boxer,
19:00:12 ,  boxers,
19:00:12 ,  com.shopclues.utils.k@427b9538,
19:00:12 ,  harman,
19:00:12 ,  wechains#002,
19:00:12 ,  collar,
19:00:13 ,  collar,
19:00:13 ,  collar,
19:00:13 ,  one,
19:00:13 ,  collar,
19:00:13 ,  ambassador,
19:00:13 ,  hitech,
19:00:13 ,  fanc,
19:00:13 ,  adidas,
19:00:13 ,  bp,
19:00:13 ,  asus,
19:00:13 ,  ambassador,
19:00:13 ,  harman,
19:00:14 ,  lin,
19:00:14 ,  one,
19:00:14 ,  samsung,
19:00:14 ,  cond,
19:00:14 ,  atx,
19:00:15 ,  blackles#002,
19:00:15 ,  woman,
19:00:15 ,  asus,
19:00:15 ,  airtel,
19:00:15 ,  weel,
19:00:15 ,  aenglish,
19:00:15 ,  orpat,
19:00:15 ,  one,
19:00:15 ,  condom,
19:00:15 ,  one,
19:00:15 ,  ling,
19:00:15 ,  fancy,
19:00:15 ,  orpat,
19:00:15 ,  woman,

for this out put should look like this.

Out_put
--------
19:00:15  , mouse , FALSE , []
19:00:15  , branded luggage bags and trolley , TRUE , []
19:00:15  , Leather shoes for men , FALSE , []
19:00:15  , printers , TRUE , []
19:00:15  , REPLACEMENT BACK HARD FLIP CASE COVER FOR Micromax Canvas Nitro A310[BLACK] , FALSE , []
19:00:16  , adidas watches for men , TRUE , ['adid', 'adidas', 'adidas', 'adidas', 'adidas', 'adidas']
19:00:16  , Mobile Charger Stand/Holder black , FALSE , []
19:00:16  , watches for men , TRUE , []


below is the code to find the above output:
--------------------------------------------
"""

import datetime
from collections import defaultdict

def getting_partial_queries(querylist):
    basequery = ' '.join(querylist)
    querylist = []
    for n in range(2,len(basequery)+1):
        querylist.append(basequery[:n])
    return querylist

queries_time = defaultdict(list)  
with open('logs.txt') as f:
    for line in f:
        fields = [ x.strip() for x in line.split(',') ]
        timestamp = datetime.datetime.strptime(fields[0], "%H:%M:%S")
        queries_time[fields[1]].append(timestamp)  

with open('search.txt') as inputf, open('search_output.txt', 'w') as outputf:
    for line in inputf:
        fields = [ x.strip() for x in line.split(',') ]
        timestamp = datetime.datetime.strptime(fields[0], "%H:%M:%S")
        queries = getting_partial_queries(fields[1].split())  
        results = []
        for q in queries:
            poss_timestamps = queries_time[q]
            for ts in poss_timestamps:
                if timestamp - datetime.timedelta(seconds=15) <= ts <= timestamp:
                    results.append(q)
        outputf.write(line.strip() + " , {}\n".format(results))





