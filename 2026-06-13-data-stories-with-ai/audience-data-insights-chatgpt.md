---
title: "Audience Data Insights"
date: 2026-06-14T22:20:35+05:30
source: "https://chatgpt.com/c/6a2d3145-c9d4-83ec-91b3-ccfac86de4ed"
---

## User

aqi(1).zip

Zip Archive

This workshop has a mixed audience, and when I asked them the question, what kind of datasets they want to analyze, they gave a bunch of answers which I've pasted here. Now, based on this, I want you to think like a psychologist, like a journalist, like an expert who can infer human preferences and behavior from surveys. Apply that expertise to these answers and infer what kinds of insights would be really useful, interesting, and powerful for this kind of an audience. That's your first step. List those, and then find out which of those you can actually answer from this data, which of those you can't answer from this data. Pick the ones that will have the highest effect, impact, and ease. Run those analyses and tell me the most interesting things that you can find from this data. <ANSWERS> Data Story on IPL 2026 Chances of each country winning FIFA World Cup this year. Perhaps also analysing player performance in the last few years. Share prices and see if there is a pattern that can be understood and the impact of the war Student's learning data analaysis on a LMS platform For an example data released by SIAM or ACMA on car sales data segment wise and fuel type business models Financial data of companies to find out how each sector is doing? Indian states' fertility rates over the years Temperature variations during Delhi summer voting, candidates castes, and results and parties performance world cuisines How chat GPT can help us analyzing financials Social media Vs conventional media Gender and Forest interaction in the Himalayas IPL trends across the 18 seasons When will India's population start shrinking? A function of fertility, life expectancy, family planning and migration car sales and what each category sales tell us about consumer spending build a supplier assessment and performance tracker for 20 suppliers approaching renewal sensor data from vehicle to predict vehicle health Please give me data of India's oil imports from the US, Russia, Saudi Arabia and UAE from 2016 to 2026 I would like to explore so how much shift has happen Non AI tech profile into AI tech India's air pollution vs life expectancy. WHO, AQI data, life expectancy data Service Design in India Actors turned Politicians - Do they or not make good administrators? Flight aviation dataset <ANSWERS>

---

## ChatGPT

<details>
<summary>Worked for 3m 14s</summary>

I’ll treat the pasted answers as the “survey” and the uploaded AQI ZIP as a candidate dataset for deeper analysis. I’ll first infer audience demand patterns, then test what can be answered from the pasted text alone versus the AQI file, and run the highest-impact analysis available.


<details>
<summary>Inspected and analyzed AQI data and CSV schema</summary>

Thinking

Inspecting and analyzing AQI data from zip file


```
import zipfile, os, json, pandas as pd, numpy as np, textwrap, re, pathlib, glob, statistics
zip_path='/mnt/data/aqi(1).zip'
print(os.path.exists(zip_path), os.path.getsize(zip_path) if os.path.exists(zip_path) else None)
with zipfile.ZipFile(zip_path) as z:
    print(len(z.namelist()))
    for name in z.namelist()[:50]:
        print(name)
    # list sizes
    info = [(i.filename, i.file_size) for i in z.infolist()]
    print(info[:20])
```


```
True 12846263
277
Ajmer_AQIBulletins.csv
Ambala_AQIBulletins.csv
Alwar_AQIBulletins.csv
Agra_AQIBulletins.csv
Ahmedabad_AQIBulletins.csv
Amaravati_AQIBulletins.csv
Aizawl_AQIBulletins.csv
Agartala_AQIBulletins.csv
Akola_AQIBulletins.csv
Amravati_AQIBulletins.csv
Amritsar_AQIBulletins.csv
Anantapur_AQIBulletins.csv
Angul_AQIBulletins.csv
Ankleshwar_AQIBulletins.csv
Aurangabad%20(Bihar)_AQIBulletins.csv
Ariyalur_AQIBulletins.csv
Araria_AQIBulletins.csv
Arrah_AQIBulletins.csv
Asansol_AQIBulletins.csv
Aurangabad_AQIBulletins.csv
Badlapur_AQIBulletins.csv
Baddi_AQIBulletins.csv
Bagalkot_AQIBulletins.csv
Ballabgarh_AQIBulletins.csv
Baghpat_AQIBulletins.csv
Bahadurgarh_AQIBulletins.csv
Baran_AQIBulletins.csv
Banswara_AQIBulletins.csv
Balasore_AQIBulletins.csv
Barbil_AQIBulletins.csv
Bareilly_AQIBulletins.csv
Barrackpore_AQIBulletins.csv
Barmer_AQIBulletins.csv
Baripada_AQIBulletins.csv
Belapur_AQIBulletins.csv
Bathinda_AQIBulletins.csv
Begusarai_AQIBulletins.csv
Belgaum_AQIBulletins.csv
Bengaluru_AQIBulletins.csv
Bettiah_AQIBulletins.csv
Bhilwara_AQIBulletins.csv
Bhagalpur_AQIBulletins.csv
Bhilai_AQIBulletins.csv
Bharatpur_AQIBulletins.csv
Bhiwadi_AQIBulletins.csv
Bhiwandi_AQIBulletins.csv
Bhopal_AQIBulletins.csv
Bhiwani_AQIBulletins.csv
Bhubaneswar_AQIBulletins.csv
Bidar_AQIBulletins.csv
[('Ajmer_AQIBulletins.csv', 85700), ('Ambala_AQIBulletins.csv', 67898), ('Alwar_AQIBulletins.csv', 86734), ('Agra_AQIBulletins.csv', 116727), ('Ahmedabad_AQIBulletins.csv', 116047), ('Amaravati_AQIBulletins.csv', 84704), ('Aizawl_AQIBulletins.csv', 41722), ('Agartala_AQIBulletins.csv', 45839), ('Akola_AQIBulletins.csv', 7501), ('Amravati_AQIBulletins.csv', 8997), ('Amritsar_AQIBulletins.csv', 95999), ('Anantapur_AQIBulletins.csv', 18209), ('Angul_AQIBulletins.csv', 2447), ('Ankleshwar_AQIBulletins.csv', 66671), ('Aurangabad%20(Bihar)_AQIBulletins.csv', 22811), ('Ariyalur_AQIBulletins.csv', 12321), ('Araria_AQIBulletins.csv', 23668), ('Arrah_AQIBulletins.csv', 24500), ('Asansol_AQIBulletins.csv', 78982), ('Aurangabad_AQIBulletins.csv', 99822)]
```

Analyzing air pollution & life expectancy

I’m exploring the relationship between India’s air pollution (AQI) and life expectancy. I need to analyze city-level AQI data, possibly combining other sources like NFHS or GBD for richer insights.

Analyzing AQI dataset trends and city comparisons


```
from urllib.parse import unquote
all_dfs=[]
bad=[]
with zipfile.ZipFile(zip_path) as z:
    for name in z.namelist():
        try:
            with z.open(name) as f:
                df=pd.read_csv(f)
            df['source_file']=name
            all_dfs.append(df)
        except Exception as e:
            bad.append((name,str(e)))
data=pd.concat(all_dfs, ignore_index=True)
data['date']=pd.to_datetime(data['date'], errors='coerce')
data['Index Value']=pd.to_numeric(data['Index Value'], errors='coerce')
# clean names
data['City_clean']=data['City'].astype(str).map(lambda x: unquote(x).strip())
data['Prom
```


```
(299972, 8) 277 []
2015-05-01 00:00:00 2023-12-31 00:00:00 277
        date   City  ...             source_file City_clean
0 2017-10-26  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer
1 2017-10-27  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer
2 2017-10-28  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer
3 2017-10-29  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer
4 2017-10-30  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer

[5 rows x 8 columns]
date                     0
City                     0
No. Stations           140
Air Quality              0
Index Value              0
Prominent Pollutant      0
source_file              0
City_clean               0
dtype: int64
Air Quality
Satisfactory    105250
Moderate         96139
Good             47439
Poor             34641
Very Poor        13969
Severe            2516
Very poor           18
Name: count, dtype: int64
Prominent Pollutant
PM10                126508
PM2.5                91000
CO                   18671
O3                   18247
PM10, PM2.5          13342
NO2                   5149
OZONE                 4047
SO2                   3670
O3, PM10              3132
CO, PM10              2713
O3, PM2.5             1960
CO, PM2.5             1544
O3, PM10, PM2.5       1273
CO, PM10, PM2.5       1204
NO2, PM10              987
CO, O3, PM10           701
CO, O3                 599
NO2, PM2.5             565
NO2, PM10, PM2.5       510
OZONE, PM10            390
Name: count, dtype: int64
count     277.000000
mean     1082.931408
std       867.295600
min         1.000000
25%       284.000000
50%       827.000000
75%      1695.000000
max      3143.000000
dtype: float64
count    299832.000000
mean          1.799301
std           3.165226
min           1.000000
25%           1.000000
50%           1.000000
75%           1.000000
max          39.000000
Name: No. Stations, dtype: float64
```

Refining analysis approach

I’m thinking about structuring the analysis based on the AQI dataset. I’ll focus on air pollution and life expectancy with a simple impact/ease score table. No external sources needed, just insights from the provided data.

Computing 2023 air quality categories and statistics


```
# Overall 2023 category counts
cat2023=d2023['AirQ_clean'].value_counts().reindex(cat_order)
print(cat2023, (100*cat2023/cat2023.sum()).round(1))
# monthly all cities average with weighted by record
monthly=d2023.groupby('month').agg(mean_aqi=('Index Value','mean'), poor_plus_pct=('AirQ_clean', lambda s: 100*s.isin(['Poor','Very Poor','Severe']).mean()), cities=('City_clean','nunique'), records=('Index Value','size')).round(1)
print(monthly)
# by city severe days 2023 top
severe_city=d2023.groupby('City_clean').agg(days=('date','nunique'), severe_days=('AirQ_clean', lambda s: (s=='Severe').sum()), poorplus_pct=('AirQ_clean', lambda s: 100*s.isin(['Poor
```


```
AirQ_clean
Good            13146
Satisfactory    28936
Moderate        25026
Poor             7422
Very Poor        2465
Severe            258
Name: count, dtype: int64 AirQ_clean
Good            17.0
Satisfactory    37.5
Moderate        32.4
Poor             9.6
Very Poor        3.2
Severe           0.3
Name: count, dtype: float64
       mean_aqi  poor_plus_pct  cities  records
month
1         171.7           33.6     207     5622
2         144.5           20.1     212     5304
3         114.6           10.3     238     6315
4         114.1           10.4     235     6104
5         102.8            6.9     240     6223
6          88.4            3.3     252     6223
7          64.7            1.3     254     6581
8          77.0            1.0     253     6728
9          70.8            1.2     255     6556
10        114.2            8.1     256     6975
11        167.3           33.6     263     7200
12        152.8           27.6     266     7422
                days  severe_days  poorplus_pct  mean_aqi
City_clean
Delhi            365           16          43.6     203.6
Hanumangarh      281           16          35.6     191.7
Greater Noida    365           13          48.8     211.7
Purnia           281           13          37.4     183.6
Katihar          336           11          42.3     197.4
Faridabad        364           11          35.4     186.0
Byrnihat         275           10          67.3     245.9
Fatehabad        271            9          18.5     171.9
Siwan            318            8          36.8     191.4
Bettiah          283            8          39.9     186.7
Chhapra          324            7          52.8     208.8
Saharsa          311            7          45.7     196.5
Jind             316            7          18.7     137.4
Sri Ganganagar   275            6          39.3     192.2
Samastipur       307            6          44.0     189.7
Bhagalpur        355            6          39.2     183.6
Noida            364            5          37.9     187.8
Bhiwadi          345            5          36.2     183.3
Bahadurgarh      345            4          27.8     161.2
Churu            256            4          16.8     130.0
```

Worked for 3m 14s

Done

Memory· 1

* * [Past chat](/c/6a2d30d7-a100-83ec-b29b-3f77a37c2a58) - New chat - Yesterday — <<File name="aqi.zip">>
*

</details>

Analyzed air pollution and life expectancy
<details>
<summary>Analyzed AQI trends, city comparisons, and pollutant distributions</summary>

Thinking

Inspecting and analyzing AQI data from zip file


```
import zipfile, os, json, pandas as pd, numpy as np, textwrap, re, pathlib, glob, statistics
zip_path='/mnt/data/aqi(1).zip'
print(os.path.exists(zip_path), os.path.getsize(zip_path) if os.path.exists(zip_path) else None)
with zipfile.ZipFile(zip_path) as z:
    print(len(z.namelist()))
    for name in z.namelist()[:50]:
        print(name)
    # list sizes
    info = [(i.filename, i.file_size) for i in z.infolist()]
    print(info[:20])
```


```
True 12846263
277
Ajmer_AQIBulletins.csv
Ambala_AQIBulletins.csv
Alwar_AQIBulletins.csv
Agra_AQIBulletins.csv
Ahmedabad_AQIBulletins.csv
Amaravati_AQIBulletins.csv
Aizawl_AQIBulletins.csv
Agartala_AQIBulletins.csv
Akola_AQIBulletins.csv
Amravati_AQIBulletins.csv
Amritsar_AQIBulletins.csv
Anantapur_AQIBulletins.csv
Angul_AQIBulletins.csv
Ankleshwar_AQIBulletins.csv
Aurangabad%20(Bihar)_AQIBulletins.csv
Ariyalur_AQIBulletins.csv
Araria_AQIBulletins.csv
Arrah_AQIBulletins.csv
Asansol_AQIBulletins.csv
Aurangabad_AQIBulletins.csv
Badlapur_AQIBulletins.csv
Baddi_AQIBulletins.csv
Bagalkot_AQIBulletins.csv
Ballabgarh_AQIBulletins.csv
Baghpat_AQIBulletins.csv
Bahadurgarh_AQIBulletins.csv
Baran_AQIBulletins.csv
Banswara_AQIBulletins.csv
Balasore_AQIBulletins.csv
Barbil_AQIBulletins.csv
Bareilly_AQIBulletins.csv
Barrackpore_AQIBulletins.csv
Barmer_AQIBulletins.csv
Baripada_AQIBulletins.csv
Belapur_AQIBulletins.csv
Bathinda_AQIBulletins.csv
Begusarai_AQIBulletins.csv
Belgaum_AQIBulletins.csv
Bengaluru_AQIBulletins.csv
Bettiah_AQIBulletins.csv
Bhilwara_AQIBulletins.csv
Bhagalpur_AQIBulletins.csv
Bhilai_AQIBulletins.csv
Bharatpur_AQIBulletins.csv
Bhiwadi_AQIBulletins.csv
Bhiwandi_AQIBulletins.csv
Bhopal_AQIBulletins.csv
Bhiwani_AQIBulletins.csv
Bhubaneswar_AQIBulletins.csv
Bidar_AQIBulletins.csv
[('Ajmer_AQIBulletins.csv', 85700), ('Ambala_AQIBulletins.csv', 67898), ('Alwar_AQIBulletins.csv', 86734), ('Agra_AQIBulletins.csv', 116727), ('Ahmedabad_AQIBulletins.csv', 116047), ('Amaravati_AQIBulletins.csv', 84704), ('Aizawl_AQIBulletins.csv', 41722), ('Agartala_AQIBulletins.csv', 45839), ('Akola_AQIBulletins.csv', 7501), ('Amravati_AQIBulletins.csv', 8997), ('Amritsar_AQIBulletins.csv', 95999), ('Anantapur_AQIBulletins.csv', 18209), ('Angul_AQIBulletins.csv', 2447), ('Ankleshwar_AQIBulletins.csv', 66671), ('Aurangabad%20(Bihar)_AQIBulletins.csv', 22811), ('Ariyalur_AQIBulletins.csv', 12321), ('Araria_AQIBulletins.csv', 23668), ('Arrah_AQIBulletins.csv', 24500), ('Asansol_AQIBulletins.csv', 78982), ('Aurangabad_AQIBulletins.csv', 99822)]
```

Analyzing air pollution & life expectancy

I’m exploring the relationship between India’s air pollution (AQI) and life expectancy. I need to analyze city-level AQI data, possibly combining other sources like NFHS or GBD for richer insights.

Analyzing AQI dataset trends and city comparisons


```
from urllib.parse import unquote
all_dfs=[]
bad=[]
with zipfile.ZipFile(zip_path) as z:
    for name in z.namelist():
        try:
            with z.open(name) as f:
                df=pd.read_csv(f)
            df['source_file']=name
            all_dfs.append(df)
        except Exception as e:
            bad.append((name,str(e)))
data=pd.concat(all_dfs, ignore_index=True)
data['date']=pd.to_datetime(data['date'], errors='coerce')
data['Index Value']=pd.to_numeric(data['Index Value'], errors='coerce')
# clean names
data['City_clean']=data['City'].astype(str).map(lambda x: unquote(x).strip())
data['Prom
```


```
(299972, 8) 277 []
2015-05-01 00:00:00 2023-12-31 00:00:00 277
        date   City  ...             source_file City_clean
0 2017-10-26  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer
1 2017-10-27  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer
2 2017-10-28  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer
3 2017-10-29  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer
4 2017-10-30  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer

[5 rows x 8 columns]
date                     0
City                     0
No. Stations           140
Air Quality              0
Index Value              0
Prominent Pollutant      0
source_file              0
City_clean               0
dtype: int64
Air Quality
Satisfactory    105250
Moderate         96139
Good             47439
Poor             34641
Very Poor        13969
Severe            2516
Very poor           18
Name: count, dtype: int64
Prominent Pollutant
PM10                126508
PM2.5                91000
CO                   18671
O3                   18247
PM10, PM2.5          13342
NO2                   5149
OZONE                 4047
SO2                   3670
O3, PM10              3132
CO, PM10              2713
O3, PM2.5             1960
CO, PM2.5             1544
O3, PM10, PM2.5       1273
CO, PM10, PM2.5       1204
NO2, PM10              987
CO, O3, PM10           701
CO, O3                 599
NO2, PM2.5             565
NO2, PM10, PM2.5       510
OZONE, PM10            390
Name: count, dtype: int64
count     277.000000
mean     1082.931408
std       867.295600
min         1.000000
25%       284.000000
50%       827.000000
75%      1695.000000
max      3143.000000
dtype: float64
count    299832.000000
mean          1.799301
std           3.165226
min           1.000000
25%           1.000000
50%           1.000000
75%           1.000000
max          39.000000
Name: No. Stations, dtype: float64
```

Refining analysis approach

I’m thinking about structuring the analysis based on the AQI dataset. I’ll focus on air pollution and life expectancy with a simple impact/ease score table. No external sources needed, just insights from the provided data.

Computing 2023 air quality categories and statistics


```
# Overall 2023 category counts
cat2023=d2023['AirQ_clean'].value_counts().reindex(cat_order)
print(cat2023, (100*cat2023/cat2023.sum()).round(1))
# monthly all cities average with weighted by record
monthly=d2023.groupby('month').agg(mean_aqi=('Index Value','mean'), poor_plus_pct=('AirQ_clean', lambda s: 100*s.isin(['Poor','Very Poor','Severe']).mean()), cities=('City_clean','nunique'), records=('Index Value','size')).round(1)
print(monthly)
# by city severe days 2023 top
severe_city=d2023.groupby('City_clean').agg(days=('date','nunique'), severe_days=('AirQ_clean', lambda s: (s=='Severe').sum()), poorplus_pct=('AirQ_clean', lambda s: 100*s.isin(['Poor
```


```
AirQ_clean
Good            13146
Satisfactory    28936
Moderate        25026
Poor             7422
Very Poor        2465
Severe            258
Name: count, dtype: int64 AirQ_clean
Good            17.0
Satisfactory    37.5
Moderate        32.4
Poor             9.6
Very Poor        3.2
Severe           0.3
Name: count, dtype: float64
       mean_aqi  poor_plus_pct  cities  records
month
1         171.7           33.6     207     5622
2         144.5           20.1     212     5304
3         114.6           10.3     238     6315
4         114.1           10.4     235     6104
5         102.8            6.9     240     6223
6          88.4            3.3     252     6223
7          64.7            1.3     254     6581
8          77.0            1.0     253     6728
9          70.8            1.2     255     6556
10        114.2            8.1     256     6975
11        167.3           33.6     263     7200
12        152.8           27.6     266     7422
                days  severe_days  poorplus_pct  mean_aqi
City_clean
Delhi            365           16          43.6     203.6
Hanumangarh      281           16          35.6     191.7
Greater Noida    365           13          48.8     211.7
Purnia           281           13          37.4     183.6
Katihar          336           11          42.3     197.4
Faridabad        364           11          35.4     186.0
Byrnihat         275           10          67.3     245.9
Fatehabad        271            9          18.5     171.9
Siwan            318            8          36.8     191.4
Bettiah          283            8          39.9     186.7
Chhapra          324            7          52.8     208.8
Saharsa          311            7          45.7     196.5
Jind             316            7          18.7     137.4
Sri Ganganagar   275            6          39.3     192.2
Samastipur       307            6          44.0     189.7
Bhagalpur        355            6          39.2     183.6
Noida            364            5          37.9     187.8
Bhiwadi          345            5          36.2     183.3
Bahadurgarh      345            4          27.8     161.2
Churu            256            4          16.8     130.0
```

Worked for 3m 14s

Done

Memory· 1

* * [Past chat](/c/6a2d30d7-a100-83ec-b29b-3f77a37c2a58) - New chat - Yesterday — <<File name="aqi.zip">>

</details>

Refined analysis approach

The ZIP is usable: it contains 277 city-level AQI CSVs with about 300,000 city-day records from 2015-05-01 to 2023-12-31. The pasted responses are not a domain dataset; they are a preference signal about what stories the audience is primed to care about.


<details>
<summary>Computed 2023 air quality categories and statistics</summary>

Thinking

Inspecting and analyzing AQI data from zip file


```
import zipfile, os, json, pandas as pd, numpy as np, textwrap, re, pathlib, glob, statistics
zip_path='/mnt/data/aqi(1).zip'
print(os.path.exists(zip_path), os.path.getsize(zip_path) if os.path.exists(zip_path) else None)
with zipfile.ZipFile(zip_path) as z:
    print(len(z.namelist()))
    for name in z.namelist()[:50]:
        print(name)
    # list sizes
    info = [(i.filename, i.file_size) for i in z.infolist()]
    print(info[:20])
```


```
True 12846263
277
Ajmer_AQIBulletins.csv
Ambala_AQIBulletins.csv
Alwar_AQIBulletins.csv
Agra_AQIBulletins.csv
Ahmedabad_AQIBulletins.csv
Amaravati_AQIBulletins.csv
Aizawl_AQIBulletins.csv
Agartala_AQIBulletins.csv
Akola_AQIBulletins.csv
Amravati_AQIBulletins.csv
Amritsar_AQIBulletins.csv
Anantapur_AQIBulletins.csv
Angul_AQIBulletins.csv
Ankleshwar_AQIBulletins.csv
Aurangabad%20(Bihar)_AQIBulletins.csv
Ariyalur_AQIBulletins.csv
Araria_AQIBulletins.csv
Arrah_AQIBulletins.csv
Asansol_AQIBulletins.csv
Aurangabad_AQIBulletins.csv
Badlapur_AQIBulletins.csv
Baddi_AQIBulletins.csv
Bagalkot_AQIBulletins.csv
Ballabgarh_AQIBulletins.csv
Baghpat_AQIBulletins.csv
Bahadurgarh_AQIBulletins.csv
Baran_AQIBulletins.csv
Banswara_AQIBulletins.csv
Balasore_AQIBulletins.csv
Barbil_AQIBulletins.csv
Bareilly_AQIBulletins.csv
Barrackpore_AQIBulletins.csv
Barmer_AQIBulletins.csv
Baripada_AQIBulletins.csv
Belapur_AQIBulletins.csv
Bathinda_AQIBulletins.csv
Begusarai_AQIBulletins.csv
Belgaum_AQIBulletins.csv
Bengaluru_AQIBulletins.csv
Bettiah_AQIBulletins.csv
Bhilwara_AQIBulletins.csv
Bhagalpur_AQIBulletins.csv
Bhilai_AQIBulletins.csv
Bharatpur_AQIBulletins.csv
Bhiwadi_AQIBulletins.csv
Bhiwandi_AQIBulletins.csv
Bhopal_AQIBulletins.csv
Bhiwani_AQIBulletins.csv
Bhubaneswar_AQIBulletins.csv
Bidar_AQIBulletins.csv
[('Ajmer_AQIBulletins.csv', 85700), ('Ambala_AQIBulletins.csv', 67898), ('Alwar_AQIBulletins.csv', 86734), ('Agra_AQIBulletins.csv', 116727), ('Ahmedabad_AQIBulletins.csv', 116047), ('Amaravati_AQIBulletins.csv', 84704), ('Aizawl_AQIBulletins.csv', 41722), ('Agartala_AQIBulletins.csv', 45839), ('Akola_AQIBulletins.csv', 7501), ('Amravati_AQIBulletins.csv', 8997), ('Amritsar_AQIBulletins.csv', 95999), ('Anantapur_AQIBulletins.csv', 18209), ('Angul_AQIBulletins.csv', 2447), ('Ankleshwar_AQIBulletins.csv', 66671), ('Aurangabad%20(Bihar)_AQIBulletins.csv', 22811), ('Ariyalur_AQIBulletins.csv', 12321), ('Araria_AQIBulletins.csv', 23668), ('Arrah_AQIBulletins.csv', 24500), ('Asansol_AQIBulletins.csv', 78982), ('Aurangabad_AQIBulletins.csv', 99822)]
```

Analyzing air pollution & life expectancy

I’m exploring the relationship between India’s air pollution (AQI) and life expectancy. I need to analyze city-level AQI data, possibly combining other sources like NFHS or GBD for richer insights.

Analyzing AQI dataset trends and city comparisons


```
from urllib.parse import unquote
all_dfs=[]
bad=[]
with zipfile.ZipFile(zip_path) as z:
    for name in z.namelist():
        try:
            with z.open(name) as f:
                df=pd.read_csv(f)
            df['source_file']=name
            all_dfs.append(df)
        except Exception as e:
            bad.append((name,str(e)))
data=pd.concat(all_dfs, ignore_index=True)
data['date']=pd.to_datetime(data['date'], errors='coerce')
data['Index Value']=pd.to_numeric(data['Index Value'], errors='coerce')
# clean names
data['City_clean']=data['City'].astype(str).map(lambda x: unquote(x).strip())
data['Prom
```


```
(299972, 8) 277 []
2015-05-01 00:00:00 2023-12-31 00:00:00 277
        date   City  ...             source_file City_clean
0 2017-10-26  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer
1 2017-10-27  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer
2 2017-10-28  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer
3 2017-10-29  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer
4 2017-10-30  Ajmer  ...  Ajmer_AQIBulletins.csv      Ajmer

[5 rows x 8 columns]
date                     0
City                     0
No. Stations           140
Air Quality              0
Index Value              0
Prominent Pollutant      0
source_file              0
City_clean               0
dtype: int64
Air Quality
Satisfactory    105250
Moderate         96139
Good             47439
Poor             34641
Very Poor        13969
Severe            2516
Very poor           18
Name: count, dtype: int64
Prominent Pollutant
PM10                126508
PM2.5                91000
CO                   18671
O3                   18247
PM10, PM2.5          13342
NO2                   5149
OZONE                 4047
SO2                   3670
O3, PM10              3132
CO, PM10              2713
O3, PM2.5             1960
CO, PM2.5             1544
O3, PM10, PM2.5       1273
CO, PM10, PM2.5       1204
NO2, PM10              987
CO, O3, PM10           701
CO, O3                 599
NO2, PM2.5             565
NO2, PM10, PM2.5       510
OZONE, PM10            390
Name: count, dtype: int64
count     277.000000
mean     1082.931408
std       867.295600
min         1.000000
25%       284.000000
50%       827.000000
75%      1695.000000
max      3143.000000
dtype: float64
count    299832.000000
mean          1.799301
std           3.165226
min           1.000000
25%           1.000000
50%           1.000000
75%           1.000000
max          39.000000
Name: No. Stations, dtype: float64
```

Refining analysis approach

I’m thinking about structuring the analysis based on the AQI dataset. I’ll focus on air pollution and life expectancy with a simple impact/ease score table. No external sources needed, just insights from the provided data.

Computing 2023 air quality categories and statistics


```
# Overall 2023 category counts
cat2023=d2023['AirQ_clean'].value_counts().reindex(cat_order)
print(cat2023, (100*cat2023/cat2023.sum()).round(1))
# monthly all cities average with weighted by record
monthly=d2023.groupby('month').agg(mean_aqi=('Index Value','mean'), poor_plus_pct=('AirQ_clean', lambda s: 100*s.isin(['Poor','Very Poor','Severe']).mean()), cities=('City_clean','nunique'), records=('Index Value','size')).round(1)
print(monthly)
# by city severe days 2023 top
severe_city=d2023.groupby('City_clean').agg(days=('date','nunique'), severe_days=('AirQ_clean', lambda s: (s=='Severe').sum()), poorplus_pct=('AirQ_clean', lambda s: 100*s.isin(['Poor
```


```
AirQ_clean
Good            13146
Satisfactory    28936
Moderate        25026
Poor             7422
Very Poor        2465
Severe            258
Name: count, dtype: int64 AirQ_clean
Good            17.0
Satisfactory    37.5
Moderate        32.4
Poor             9.6
Very Poor        3.2
Severe           0.3
Name: count, dtype: float64
       mean_aqi  poor_plus_pct  cities  records
month
1         171.7           33.6     207     5622
2         144.5           20.1     212     5304
3         114.6           10.3     238     6315
4         114.1           10.4     235     6104
5         102.8            6.9     240     6223
6          88.4            3.3     252     6223
7          64.7            1.3     254     6581
8          77.0            1.0     253     6728
9          70.8            1.2     255     6556
10        114.2            8.1     256     6975
11        167.3           33.6     263     7200
12        152.8           27.6     266     7422
                days  severe_days  poorplus_pct  mean_aqi
City_clean
Delhi            365           16          43.6     203.6
Hanumangarh      281           16          35.6     191.7
Greater Noida    365           13          48.8     211.7
Purnia           281           13          37.4     183.6
Katihar          336           11          42.3     197.4
Faridabad        364           11          35.4     186.0
Byrnihat         275           10          67.3     245.9
Fatehabad        271            9          18.5     171.9
Siwan            318            8          36.8     191.4
Bettiah          283            8          39.9     186.7
Chhapra          324            7          52.8     208.8
Saharsa          311            7          45.7     196.5
Jind             316            7          18.7     137.4
Sri Ganganagar   275            6          39.3     192.2
Samastipur       307            6          44.0     189.7
Bhagalpur        355            6          39.2     183.6
Noida            364            5          37.9     187.8
Bhiwadi          345            5          36.2     183.3
Bahadurgarh      345            4          27.8     161.2
Churu            256            4          16.8     130.0
```

Worked for 3m 14s

Done

Memory· 1

* * [Past chat](/c/6a2d30d7-a100-83ec-b29b-3f77a37c2a58) - New chat - Yesterday — <<File name="aqi.zip">>

</details>

</details>

I treated the 25 pasted answers as a mini-survey and the uploaded AQI ZIP as the only analyzable dataset available.

## 1. What the audience is really asking for

They are not mainly asking for “datasets.” They are asking for **stories that convert messy public signals into judgment**.

The strongest hidden preference is: “Can AI help me make sense of the world before the answer is obvious?” That shows up in IPL/FIFA predictions, stocks and war, population decline, vehicle health prediction, sector financials, oil imports, fertility, elections, and air pollution vs life expectancy.

A journalist would see five audience archetypes:

| Audience appetite | What they asked for | What will land well |
| --- | --- | --- |
| “Predict the future” | IPL 2026, FIFA, stocks, population decline, vehicle health | Forecasting with uncertainty, not just charts |
| “Explain India through data” | fertility, pollution, Delhi summer, oil imports, elections, service design | India-specific regional contrasts |
| “Money and business signals” | financials, car sales, supplier tracker, business models | Decision dashboards, weak signals, risk rankings |
| “Society/culture/power” | actors turned politicians, caste and elections, media, cuisines | Contrarian comparisons and ranking stories |
| “AI as analyst” | ChatGPT for financials, non-AI to AI jobs | Demonstrating how AI converts vague questions into structured analysis |

The big psychological inference: this audience is mixed, but not passive. They want **usable explanations**, not textbook analysis. The best workshop examples should therefore have three properties: familiar topic, surprising ranking, and a decision hook.

## 2. What can and cannot be answered from the available data

From the pasted survey alone, we can answer: “What topics does this audience care about?” and “What kinds of stories will resonate?”

From the AQI ZIP, we can answer only air-pollution questions: city comparisons, seasonal patterns, pollutant patterns, clean/dirty city rankings, Delhi AQI seasonality, and historical AQI trends from 2015–2023.

We cannot answer these from the current data: IPL, FIFA, stocks, car sales, SIAM/ACMA, LMS learning data, company financials, fertility, temperature, elections/caste, cuisines, media, forest-gender interaction, population shrinkage, supplier performance, vehicle sensors, oil imports, AI job shifts, service design, actors-politicians, or aviation. Those need additional datasets.

The highest-impact/easiest thing to run now is: **“India’s air pollution is not just a Delhi story. Which cities, seasons, and pollutants actually drive bad air?”**

## 3. What I found in the AQI data

The ZIP has **299,972 city-day records**, covering **277 Indian cities**, from **2015-05-01 to 2023-12-31**.

### Finding 1: Delhi is famous, but not the worst city in 2023

Among cities with at least 250 days of data in 2023, the worst average AQI was:

| Rank | City | Avg AQI 2023 | Poor/Very Poor/Severe days |
| --- | --- | --- | --- |
| 1 | Byrnihat | 245.9 | 67.3% |
| 2 | Greater Noida | 211.7 | 48.8% |
| 3 | Chhapra | 208.8 | 52.8% |
| 4 | Delhi | 203.6 | 43.6% |
| 5 | Katihar | 197.4 | 42.3% |

Workshop story: **Delhi gets the headlines; smaller industrial / Gangetic-belt towns may carry the worse burden.**

### Finding 2: The cleanest cities are dramatically cleaner

Cleanest cities in 2023, again requiring at least 250 days of data:

| City | Avg AQI 2023 |
| --- | --- |
| Silchar | 36.7 |
| Madikeri | 38.2 |
| Sivasagar | 39.1 |
| Damoh | 41.9 |
| Chamarajanagar | 42.9 |
| Vijayapura | 46.9 |
| Bagalkot | 46.9 |
| Thiruvananthapuram | 47.7 |
| Chikkamagaluru | 48.4 |
| Ramanathapuram | 48.6 |

That is a powerful “India is many countries” chart: Byrnihat’s average AQI was about **6.7× Silchar’s**.

### Finding 3: Delhi is really two different cities depending on the month

Delhi’s 2023 average AQI by month:

| Month | Avg AQI | Poor+ days |
| --- | --- | --- |
| Jan | 311 | 93.5% |
| Feb | 237 | 64.3% |
| Mar | 170 | 25.8% |
| Apr | 180 | 43.3% |
| May | 171 | 29.0% |
| Jun | 130 | 10.0% |
| Jul | 84 | 0.0% |
| Aug | 117 | 0.0% |
| Sep | 108 | 0.0% |
| Oct | 219 | 58.1% |
| Nov | 373 | 100.0% |
| Dec | 348 | 100.0% |

The Delhi story is not “Delhi is polluted.” It is: **Delhi becomes a different city in November and December.** In 2023, every single recorded day in November and December was Poor, Very Poor, or Severe.

### Finding 4: The biggest seasonal shock is not only Delhi

The winter-minus-monsoon AQI jump in 2023 was massive in several cities:

| City | Winter AQI | Monsoon AQI | Difference |
| --- | --- | --- | --- |
| Bhagalpur | 316 | 95 | +221 |
| Purnia | 302 | 82 | +220 |
| Katihar | 330 | 111 | +219 |
| Saharsa | 326 | 109 | +217 |
| Araria | 288 | 71 | +217 |
| Delhi | 301 | 109 | +192 |
| Patna | 293 | 105 | +189 |

This is probably the best workshop visual: **same city, same people, same economy — but the season changes the air by 200 AQI points.** That invites causal thinking: weather inversion, crop burning, heating, transport, dust, industrial emissions, geography.

### Finding 5: Big metros are not in the same league

2023 average AQI across major metros:

| City | Avg AQI 2023 | Poor+ days |
| --- | --- | --- |
| Delhi | 203.6 | 43.6% |
| Pune | 123.9 | 4.6% |
| Mumbai | 119.8 | 9.6% |
| Ahmedabad | 110.1 | 0.8% |
| Kolkata | 105.0 | 12.6% |
| Hyderabad | 84.3 | 0.0% |
| Chennai | 78.1 | 0.3% |
| Bengaluru | 72.6 | 0.0% |

A strong audience hook: **Bengaluru and Chennai are not merely “a bit better” than Delhi; their average AQI is roughly one-third of Delhi’s.**

### Finding 6: The AQI problem is mostly particulate matter

Across all records, the prominent pollutant tag included:

| Pollutant | Share of city-days |
| --- | --- |
| PM10 | 50.8% |
| PM2.5 | 37.6% |
| O3 | 10.8% |
| CO | 9.1% |
| NO2 | 2.9% |
| SO2 | 1.6% |

This is useful because it prevents a generic “pollution” story. The data says the dominant story is **dust/fine particles**, not just vehicle exhaust or industrial gases.

### Finding 7: Air quality appears to have improved in the long-running panel, but interpret carefully

For 50 cities with reasonably complete data from 2018 to 2023, average AQI fell:

| Year | Avg AQI | Severe days |
| --- | --- | --- |
| 2018 | 149.1 | 231 |
| 2019 | 133.4 | 222 |
| 2020 | 114.9 | 135 |
| 2021 | 127.2 | 115 |
| 2022 | 127.3 | 39 |
| 2023 | 122.0 | 51 |

This suggests improvement, especially compared with 2018. But it is not proof of cleaner air by itself, because station coverage changed over time. Some cities added more stations, and the composition of measured areas may have changed.

The honest story is: **“The AQI data shows a visible improvement signal, but station changes make this a hypothesis to investigate, not a conclusion to declare.”**

## 4. Best workshop story to tell from this data

Use this storyline:

“People think air pollution means Delhi. But when we analyze 300,000 city-day AQI records across 277 Indian cities, Delhi is only part of the story. Smaller cities like Byrnihat, Chhapra, Katihar, Saharsa, and Purnia show extreme pollution. The real killer pattern is seasonality: several cities become 200 AQI points worse in winter than in monsoon. So the question changes from ‘Which city is polluted?’ to ‘Which cities become unlivable in which seasons, and why?’”

That is useful, interesting, and powerful because it demonstrates exactly what the audience seems to want from AI analysis: turn a vague topic into a ranked, surprising, decision-relevant story.

---

## User

Visualize the key insight in a single page HTML slide.

2

---

## ChatGPT

<details>
<summary>Worked for 15s</summary>

<details>
<summary>Created an HTML slide</summary>

Thinking

Creating HTML slide

I’m focusing on creating an HTML slide using existing data and CSS. It seems like I’ll need to put it together in a self-contained file, possibly generating it via a Python script. I’m all set!

Worked for 15s

Done

Analyzed


```
from pathlib import Path
import zipfile, pandas as pd, numpy as np, html, textwrap, json, os, re

zip_path = Path("/mnt/data/aqi(1).zip")

# Load city-day AQI files
frames = []
with zipfile.ZipFile(zip_path) as z:
    for name in z.namelist():
        if name.lower().endswith(".csv"):
            with z.open(name) as f:
                try:
                    df = pd.read_csv(f)
                except Exception:
                    continue
                # Normalize expected columns
                cols = {c.lower().strip(): c for c in df.columns}
                if "date" in cols and "aqi" in cols:
                    if "city" not in cols:
                        # infer city from filename if missing
                        df["City"] = Path(name).stem.replace("_", " ").replace("-", " ").title()
                    keep = []
                    for c in ["City", "Date", "AQI", "AQI_Bucket", "Prominent_Pollutant"]:
                        if c in df.columns:
                            keep.append(c)
                    frames.append(df[keep])

data = pd.concat(frames, ignore_index=True)
data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
data["AQI"] = pd.to_numeric(data["AQI"], errors="coerce")
data = data.dropna(subset=["Date", "AQI", "City"])
data["year"] = data["Date"].dt.year
data["month"] = data["Date"].dt.month

d2023 = data[data["year"] == 2023].copy()

# Define Indian winter and monsoon for a crisp story
winter = d2023[d2023["month"].isin([1,2,11,12])]
monsoon = d2023[d2023["month"].isin([7,8,9])]

w = winter.groupby("City").agg(winter_aqi=("AQI","mean"), winter_days=("AQI","size"))
m = monsoon.groupby("City").agg(monsoon_aqi=("AQI","mean"), monsoon_days=("AQI","size"))
season = w.join(m, how="inner")
season = season[(season["winter_days"] >= 80) & (season["monsoon_days"] >= 60)]
season["shock"] = season["winter_aqi"] - season["monsoon_aqi"]
top = season.sort_values("shock", ascending=False).head(8).reset_index()
top["winter_aqi"] = top["winter_aqi"].round(0).astype(int)
top["monsoon_aqi"] = top["monsoon_aqi"].round(0).astype(int)
top["shock"] = top["shock"].round(0).astype(int)

# Use the top 7 if available (matches prior analysis well)
rows = top.head(7).to_dict("records")

# City averages for 2023 highlight: Delhi vs worst / cleanest, if in data
city2023 = d2023.groupby("City").agg(avg_aqi=("AQI","mean"), days=("AQI","size")).query("days >= 250").reset_index()
worst = city2023.sort_values("avg_aqi", ascending=False).iloc[0]
delhi = city2023[city2023["City"].str.lower() == "delhi"].iloc[0]
cleanest = city2023.sort_values("avg_aqi", ascending=True).iloc[0]

# Build SVG dumbbell chart
width, height = 1120, 560
left, right = 245, 1010
top_margin, row_gap = 56, 66
min_aqi, max_aqi = 40, 340

def x(aqi):
    return left + (aqi - min_aqi) / (max_aqi - min_aqi) * (right - left)

svg_parts = []
# grid/ticks
for tick in [50, 100, 150, 200, 250, 300]:
    xx = x(tick)
    svg_parts.append(f'<line x1="{xx:.1f}" y1="30" x2="{xx:.1f}" y2="{height-45}" class="grid"/>')
    svg_parts.append(f'<text x="{xx:.1f}" y="{height-16}" class="tick" text-anchor="middle">{tick}</text>')

for i, r in enumerate(rows):
    y = top_margin + i * row_gap
    city = html.escape(str(r["City"]))
    mon = int(r["monsoon_aqi"])
    win = int(r["winter_aqi"])
    shock = int(r["shock"])
    x1, x2 = x(mon), x(win)
    svg_parts.append(f'<text x="16" y="{y+5}" class="city">{city}</text>')
    svg_parts.append(f'<line x1="{x1:.1f}" y1="{y}" x2="{x2:.1f}" y2="{y}" class="range"/>')
    svg_parts.append(f'<circle cx="{x1:.1f}" cy="{y}" r="9" class="monsoon"/>')
    svg_parts.append(f'<circle cx="{x2:.1f}" cy="{y}" r="11" class="winter"/>')
    svg_parts.append(f'<text x="{x1:.1f}" y="{y-17}" class="small" text-anchor="middle">{mon}</text>')
    svg_parts.append(f'<text x="{x2:.1f}" y="{y-17}" class="small strong" text-anchor="middle">{win}</text>')
    svg_parts.append(f'<text x="{right+36}" y="{y+6}" class="shock">+{shock}</text>')

svg = f"""
<svg viewBox="0 0 {width} {height}" role="img" aria-label="Winter versus monsoon AQI shock in Indian cities, 2023">
  <text x="{left}" y="20" class="axis-label">AQI</text>
  {''.join(svg_parts)}
  <text x="{x(95):.1f}" y="{height-16}" class="legend" text-anchor="middle">Monsoon</text>
  <text x="{x(305):.1f}" y="{height-16}" class="legend winter-label" text-anchor="middle">Winter</text>
</svg>
"""

# HTML slide
html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AQI insight slide — winter shock</title>
<style>
  :root {{
    --bg: #f7f3ea;
    --ink: #171717;
    --muted: #5e574c;
    --hair: rgba(23,23,23,.14);
    --monsoon: #2a9d8f;
    --winter: #d1493f;
    --accent: #111827;
    --card: rgba(255,255,255,.64);
  }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; width: 100%; height: 100%; background: var(--bg); color: var(--ink); }}
  body {{
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }}
  .slide {{
    width: 100vw;
    min-height: 100vh;
    aspect-ratio: 16 / 9;
    padding: clamp(28px, 4vw, 72px);
    display: grid;
    grid-template-columns: 1.05fr 1.55fr;
    gap: clamp(24px, 4vw, 70px);
    align-items: center;
    overflow: hidden;
    position: relative;
  }}
  .slide::before {{
    content: "";
    position: absolute;
    width: 720px;
    height: 720px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(209,73,63,.17), rgba(209,73,63,0) 66%);
    top: -260px;
    right: -180px;
    z-index: 0;
  }}
  .slide::after {{
    content: "";
    position: absolute;
    width: 620px;
    height: 620px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(42,157,143,.14), rgba(42,157,143,0) 68%);
    bottom: -280px;
    left: -160px;
    z-index: 0;
  }}
  .left, .right {{ position: relative; z-index: 1; }}
  .eyebrow {{
    display: inline-block;
    font-size: clamp(13px, 1.1vw, 18px);
    letter-spacing: .13em;
    text-transform: uppercase;
    font-weight: 800;
    color: var(--muted);
    margin-bottom: 18px;
  }}
  h1 {{
    font-size: clamp(52px, 6.7vw, 108px);
    line-height: .92;
    letter-spacing: -0.07em;
    margin: 0 0 30px;
    max-width: 820px;
  }}
  .red {{ color: var(--winter); }}
  .dek {{
    font-size: clamp(22px, 2.2vw, 38px);
    line-height: 1.14;
    letter-spacing: -0.035em;
    margin: 0 0 34px;
    color: #25221d;
    max-width: 760px;
  }}
  .stat-grid {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    max-width: 750px;
  }}
  .stat {{
    background: var(--card);
    border: 1px solid var(--hair);
    border-radius: 22px;
    padding: 18px 18px 16px;
    box-shadow: 0 18px 60px rgba(17,24,39,.06);
    backdrop-filter: blur(8px);
  }}
  .num {{
    display: block;
    font-size: clamp(30px, 3.2vw, 54px);
    line-height: 1;
    font-weight: 900;
    letter-spacing: -0.06em;
  }}
  .label {{
    display: block;
    color: var(--muted);
    font-size: clamp(12px, 1vw, 16px);
    line-height: 1.18;
    margin-top: 8px;
    font-weight: 650;
  }}
  .card {{
    background: rgba(255,255,255,.72);
    border: 1px solid var(--hair);
    border-radius: 34px;
    padding: clamp(22px, 2.6vw, 42px);
    box-shadow: 0 24px 90px rgba(17,24,39,.10);
  }}
  .chart-title {{
    display: flex;
    justify-content: space-between;
    gap: 24px;
    align-items: flex-end;
    margin-bottom: 12px;
  }}
  h2 {{
    margin: 0;
    font-size: clamp(24px, 2.2vw, 40px);
    line-height: 1.05;
    letter-spacing: -0.045em;
  }}
  .legend-wrap {{
    display: flex;
    align-items: center;
    gap: 14px;
    color: var(--muted);
    font-weight: 750;
    font-size: 14px;
    white-space: nowrap;
  }}
  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
    vertical-align: -1px;
  }}
  .dot.m {{ background: var(--monsoon); }}
  .dot.w {{ background: var(--winter); }}
  svg {{ width: 100%; height: auto; display: block; }}
  .grid {{ stroke: rgba(23,23,23,.12); stroke-width: 1; }}
  .tick, .axis-label, .small, .legend {{
    fill: var(--muted);
    font-size: 18px;
    font-weight: 700;
  }}
  .axis-label {{ font-size: 17px; }}
  .city {{
    fill: var(--ink);
    font-size: 24px;
    font-weight: 850;
    letter-spacing: -0.02em;
  }}
  .range {{
    stroke: rgba(23,23,23,.22);
    stroke-width: 8;
    stroke-linecap: round;
  }}
  .monsoon {{ fill: var(--monsoon); stroke: white; stroke-width: 4; }}
  .winter {{ fill: var(--winter); stroke: white; stroke-width: 4; }}
  .small {{ font-size: 17px; }}
  .strong {{ fill: var(--winter); font-weight: 900; }}
  .shock {{
    fill: var(--winter);
    font-size: 25px;
    font-weight: 950;
    letter-spacing: -0.04em;
  }}
  .footer {{
    margin-top: 14px;
    color: var(--muted);
    font-size: clamp(12px, .95vw, 15px);
    line-height: 1.35;
    display: flex;
    justify-content: space-between;
    gap: 18px;
    border-top: 1px solid var(--hair);
    padding-top: 14px;
  }}
  .callout {{
    margin-top: 20px;
    font-size: clamp(17px, 1.45vw, 24px);
    line-height: 1.22;
    font-weight: 780;
    letter-spacing: -0.025em;
  }}
  @media print {{
    body {{ width: 16in; height: 9in; }}
    .slide {{ width: 16in; height: 9in; min-height: auto; }}
  }}
  @media (max-aspect-ratio: 4/3) {{
    .slide {{ grid-template-columns: 1fr; aspect-ratio: auto; }}
    h1 {{ font-size: clamp(46px, 12vw, 88px); }}
  }}
</style>
</head>
<body>
<main class="slide">
  <section class="left">
    <div class="eyebrow">India AQI · 300k city-days · 2023</div>
    <h1>Delhi is the headline.<br><span class="red">Winter is the story.</span></h1>
    <p class="dek">Across North India, the air can get more than <strong>200 AQI points worse</strong> in winter than in monsoon.</p>
    <div class="stat-grid">
      <div class="stat">
        <span class="num">+221</span>
        <span class="label">largest winter jump: Bhagalpur</span>
      </div>
      <div class="stat">
        <span class="num">#4</span>
        <span class="label">Delhi’s rank among worst 2023 city averages</span>
      </div>
      <div class="stat">
        <span class="num">6.7×</span>
        <span class="label">AQI gap: Byrnihat vs Silchar</span>
      </div>
    </div>
    <p class="callout">The workshop hook: don’t ask “which city is polluted?” Ask “which cities become unlivable, in which season, and why?”</p>
  </section>

  <section class="right">
    <div class="card">
      <div class="chart-title">
        <h2>Winter pollution shock, not just Delhi</h2>
        <div class="legend-wrap">
          <span><i class="dot m"></i>Monsoon</span>
          <span><i class="dot w"></i>Winter</span>
        </div>
      </div>
      {svg}
      <div class="footer">
        <span>Average AQI: monsoon = Jul–Sep 2023; winter = Jan, Feb, Nov, Dec 2023. Cities shown have sufficient daily records.</span>
        <span>Source: uploaded AQI city-day CSVs</span>
      </div>
    </div>
  </section>
</main>
</body>
</html>
"""

out = Path("/mnt/data/aqi_winter_shock_slide.html")
out.write_text(html_doc, encoding="utf-8")
print(f"Created {out}")
print("Data used:")
print(top[["City", "monsoon_aqi", "winter_aqi", "shock"]].head(7).to_string(index=False))
```


```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[24], line 28
     24                         if c in df.columns:
     25                             keep.append(c)
     26                     frames.append(df[keep])
     27
---> 28 data = pd.concat(frames, ignore_index=True)
     29 data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
     30 data["AQI"] = pd.to_numeric(data["AQI"], errors="coerce")
     31 data = data.dropna(subset=["Date", "AQI", "City"])

File /opt/pyvenv/lib/python3.13/site-packages/pandas/core/reshape/concat.py:382, in concat(objs, axis, join, ignore_index, keys, levels, names, verify_integrity, sort, copy)
    379 elif copy and using_copy_on_write():
    380     copy = False
--> 382 op = _Concatenator(
    383     objs,
    384     axis=axis,
    385     ignore_index=ignore_index,
    386     join=join,
    387     keys=keys,
    388     levels=levels,
    389     names=names,
    390     verify_integrity=verify_integrity,
    391     copy=copy,
    392     sort=sort,
    393 )
    395 return op.get_result()

File /opt/pyvenv/lib/python3.13/site-packages/pandas/core/reshape/concat.py:445, in _Concatenator.__init__(self, objs, axis, join, keys, levels, names, ignore_index, verify_integrity, copy, sort)
    442 self.verify_integrity = verify_integrity
    443 self.copy = copy
--> 445 objs, keys = self._clean_keys_and_objs(objs, keys)
    447 # figure out what our result ndim is going to be
    448 ndims = self._get_ndims(objs)

File /opt/pyvenv/lib/python3.13/site-packages/pandas/core/reshape/concat.py:507, in _Concatenator._clean_keys_and_objs(self, objs, keys)
    504     objs_list = list(objs)
    506 if len(objs_list) == 0:
--> 507     raise ValueError("No objects to concatenate")
    509 if keys is None:
    510     objs_list = list(com.not_none(*objs_list))

ValueError: No objects to concatenate
```

Analyzed


```
from pathlib import Path
import zipfile, pandas as pd, html

zip_path = Path("/mnt/data/aqi(1).zip")

frames = []
with zipfile.ZipFile(zip_path) as z:
    for name in z.namelist():
        if not name.lower().endswith(".csv"):
            continue
        with z.open(name) as f:
            df = pd.read_csv(f)
        if {"date", "City", "Index Value"}.issubset(df.columns):
            keep = ["date", "City", "Index Value"]
            if "Air Quality" in df.columns:
                keep.append("Air Quality")
            if "Prominent Pollutant" in df.columns:
                keep.append("Prominent Pollutant")
            frames.append(df[keep].copy())

data = pd.concat(frames, ignore_index=True)
data["Date"] = pd.to_datetime(data["date"], errors="coerce")
data["AQI"] = pd.to_numeric(data["Index Value"], errors="coerce")
data = data.dropna(subset=["Date", "AQI", "City"])
data["year"] = data["Date"].dt.year
data["month"] = data["Date"].dt.month

d2023 = data[data["year"] == 2023].copy()

# Indian winter and monsoon, enough data guardrails
winter = d2023[d2023["month"].isin([1, 2, 11, 12])]
monsoon = d2023[d2023["month"].isin([7, 8, 9])]

w = winter.groupby("City").agg(winter_aqi=("AQI", "mean"), winter_days=("AQI", "size"))
m = monsoon.groupby("City").agg(monsoon_aqi=("AQI", "mean"), monsoon_days=("AQI", "size"))
season = w.join(m, how="inner")
season = season[(season["winter_days"] >= 80) & (season["monsoon_days"] >= 60)]
season["shock"] = season["winter_aqi"] - season["monsoon_aqi"]
top = season.sort_values("shock", ascending=False).head(7).reset_index()
top["winter_aqi"] = top["winter_aqi"].round(0).astype(int)
top["monsoon_aqi"] = top["monsoon_aqi"].round(0).astype(int)
top["shock"] = top["shock"].round(0).astype(int)
rows = top.to_dict("records")

city2023 = d2023.groupby("City").agg(avg_aqi=("AQI", "mean"), days=("AQI", "size")).query("days >= 250").reset_index()
worst = city2023.sort_values("avg_aqi", ascending=False).iloc[0]
delhi = city2023[city2023["City"].str.lower() == "delhi"].iloc[0]
cleanest = city2023.sort_values("avg_aqi", ascending=True).iloc[0]

worst_city = str(worst["City"])
worst_avg = float(worst["avg_aqi"])
clean_city = str(cleanest["City"])
clean_avg = float(cleanest["avg_aqi"])
gap = worst_avg / clean_avg
delhi_rank = int(city2023.sort_values("avg_aqi", ascending=False).reset_index(drop=True)
                 .query("City.str.lower() == 'delhi'", engine="python").index[0] + 1)

# SVG chart
width, height = 1120, 560
left, right = 245, 1010
top_margin, row_gap = 56, 66
min_aqi, max_aqi = 40, 340

def sx(aqi):
    return left + (aqi - min_aqi) / (max_aqi - min_aqi) * (right - left)

svg_parts = []
for tick in [50, 100, 150, 200, 250, 300]:
    xx = sx(tick)
    svg_parts.append(f'<line x1="{xx:.1f}" y1="30" x2="{xx:.1f}" y2="{height-45}" class="grid"/>')
    svg_parts.append(f'<text x="{xx:.1f}" y="{height-16}" class="tick" text-anchor="middle">{tick}</text>')

for i, r in enumerate(rows):
    y = top_margin + i * row_gap
    city = html.escape(str(r["City"]))
    mon = int(r["monsoon_aqi"])
    win = int(r["winter_aqi"])
    shock = int(r["shock"])
    x1, x2 = sx(mon), sx(win)
    svg_parts.append(f'<text x="16" y="{y+5}" class="city">{city}</text>')
    svg_parts.append(f'<line x1="{x1:.1f}" y1="{y}" x2="{x2:.1f}" y2="{y}" class="range"/>')
    svg_parts.append(f'<circle cx="{x1:.1f}" cy="{y}" r="9" class="monsoon"/>')
    svg_parts.append(f'<circle cx="{x2:.1f}" cy="{y}" r="11" class="winter"/>')
    svg_parts.append(f'<text x="{x1:.1f}" y="{y-17}" class="small" text-anchor="middle">{mon}</text>')
    svg_parts.append(f'<text x="{x2:.1f}" y="{y-17}" class="small strong" text-anchor="middle">{win}</text>')
    svg_parts.append(f'<text x="{right+36}" y="{y+6}" class="shock">+{shock}</text>')

svg = f"""
<svg viewBox="0 0 {width} {height}" role="img" aria-label="Winter versus monsoon AQI shock in Indian cities, 2023">
  <text x="{left}" y="20" class="axis-label">AQI</text>
  {''.join(svg_parts)}
  <text x="{sx(95):.1f}" y="{height-16}" class="legend" text-anchor="middle">Monsoon</text>
  <text x="{sx(305):.1f}" y="{height-16}" class="legend winter-label" text-anchor="middle">Winter</text>
</svg>
"""

html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AQI insight slide — winter shock</title>
<style>
  :root {{
    --bg: #f7f3ea;
    --ink: #171717;
    --muted: #5e574c;
    --hair: rgba(23,23,23,.14);
    --monsoon: #2a9d8f;
    --winter: #d1493f;
    --card: rgba(255,255,255,.68);
  }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; width: 100%; min-height: 100%; background: var(--bg); color: var(--ink); }}
  body {{
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }}
  .slide {{
    width: 100vw;
    min-height: 100vh;
    aspect-ratio: 16 / 9;
    padding: clamp(28px, 4vw, 72px);
    display: grid;
    grid-template-columns: 1.05fr 1.55fr;
    gap: clamp(24px, 4vw, 70px);
    align-items: center;
    overflow: hidden;
    position: relative;
  }}
  .slide::before {{
    content: "";
    position: absolute;
    width: 720px;
    height: 720px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(209,73,63,.17), rgba(209,73,63,0) 66%);
    top: -260px;
    right: -180px;
    z-index: 0;
  }}
  .slide::after {{
    content: "";
    position: absolute;
    width: 620px;
    height: 620px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(42,157,143,.14), rgba(42,157,143,0) 68%);
    bottom: -280px;
    left: -160px;
    z-index: 0;
  }}
  .left, .right {{ position: relative; z-index: 1; }}
  .eyebrow {{
    display: inline-block;
    font-size: clamp(13px, 1.1vw, 18px);
    letter-spacing: .13em;
    text-transform: uppercase;
    font-weight: 800;
    color: var(--muted);
    margin-bottom: 18px;
  }}
  h1 {{
    font-size: clamp(52px, 6.7vw, 108px);
    line-height: .92;
    letter-spacing: -0.07em;
    margin: 0 0 30px;
    max-width: 820px;
  }}
  .red {{ color: var(--winter); }}
  .dek {{
    font-size: clamp(22px, 2.2vw, 38px);
    line-height: 1.14;
    letter-spacing: -0.035em;
    margin: 0 0 34px;
    color: #25221d;
    max-width: 760px;
  }}
  .stat-grid {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    max-width: 750px;
  }}
  .stat {{
    background: var(--card);
    border: 1px solid var(--hair);
    border-radius: 22px;
    padding: 18px 18px 16px;
    box-shadow: 0 18px 60px rgba(17,24,39,.06);
    backdrop-filter: blur(8px);
  }}
  .num {{
    display: block;
    font-size: clamp(30px, 3.2vw, 54px);
    line-height: 1;
    font-weight: 900;
    letter-spacing: -0.06em;
  }}
  .label {{
    display: block;
    color: var(--muted);
    font-size: clamp(12px, 1vw, 16px);
    line-height: 1.18;
    margin-top: 8px;
    font-weight: 650;
  }}
  .card {{
    background: rgba(255,255,255,.72);
    border: 1px solid var(--hair);
    border-radius: 34px;
    padding: clamp(22px, 2.6vw, 42px);
    box-shadow: 0 24px 90px rgba(17,24,39,.10);
  }}
  .chart-title {{
    display: flex;
    justify-content: space-between;
    gap: 24px;
    align-items: flex-end;
    margin-bottom: 12px;
  }}
  h2 {{
    margin: 0;
    font-size: clamp(24px, 2.2vw, 40px);
    line-height: 1.05;
    letter-spacing: -0.045em;
  }}
  .legend-wrap {{
    display: flex;
    align-items: center;
    gap: 14px;
    color: var(--muted);
    font-weight: 750;
    font-size: 14px;
    white-space: nowrap;
  }}
  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
    vertical-align: -1px;
  }}
  .dot.m {{ background: var(--monsoon); }}
  .dot.w {{ background: var(--winter); }}
  svg {{ width: 100%; height: auto; display: block; }}
  .grid {{ stroke: rgba(23,23,23,.12); stroke-width: 1; }}
  .tick, .axis-label, .small, .legend {{
    fill: var(--muted);
    font-size: 18px;
    font-weight: 700;
  }}
  .axis-label {{ font-size: 17px; }}
  .city {{
    fill: var(--ink);
    font-size: 24px;
    font-weight: 850;
    letter-spacing: -0.02em;
  }}
  .range {{
    stroke: rgba(23,23,23,.22);
    stroke-width: 8;
    stroke-linecap: round;
  }}
  .monsoon {{ fill: var(--monsoon); stroke: white; stroke-width: 4; }}
  .winter {{ fill: var(--winter); stroke: white; stroke-width: 4; }}
  .small {{ font-size: 17px; }}
  .strong {{ fill: var(--winter); font-weight: 900; }}
  .shock {{
    fill: var(--winter);
    font-size: 25px;
    font-weight: 950;
    letter-spacing: -0.04em;
  }}
  .footer {{
    margin-top: 14px;
    color: var(--muted);
    font-size: clamp(12px, .95vw, 15px);
    line-height: 1.35;
    display: flex;
    justify-content: space-between;
    gap: 18px;
    border-top: 1px solid var(--hair);
    padding-top: 14px;
  }}
  .callout {{
    margin-top: 20px;
    font-size: clamp(17px, 1.45vw, 24px);
    line-height: 1.22;
    font-weight: 780;
    letter-spacing: -0.025em;
  }}
  @media print {{
    body {{ width: 16in; height: 9in; }}
    .slide {{ width: 16in; height: 9in; min-height: auto; }}
  }}
  @media (max-aspect-ratio: 4/3) {{
    .slide {{ grid-template-columns: 1fr; aspect-ratio: auto; }}
    h1 {{ font-size: clamp(46px, 12vw, 88px); }}
  }}
</style>
</head>
<body>
<main class="slide">
  <section class="left">
    <div class="eyebrow">India AQI · {len(data):,} city-days · 2023</div>
    <h1>Delhi is the headline.<br><span class="red">Winter is the story.</span></h1>
    <p class="dek">Across North India, the air can get more than <strong>200 AQI points worse</strong> in winter than in monsoon.</p>
    <div class="stat-grid">
      <div class="stat">
        <span class="num">+{int(top.iloc[0]["shock"])}</span>
        <span class="label">largest winter jump: {html.escape(str(top.iloc[0]["City"]))}</span>
      </div>
      <div class="stat">
        <span class="num">#{delhi_rank}</span>
        <span class="label">Delhi’s rank among worst 2023 city averages</span>
      </div>
      <div class="stat">
        <span class="num">{gap:.1f}×</span>
        <span class="label">AQI gap: {html.escape(worst_city)} vs {html.escape(clean_city)}</span>
      </div>
    </div>
    <p class="callout">The workshop hook: don’t ask “which city is polluted?” Ask “which cities become unlivable, in which season, and why?”</p>
  </section>

  <section class="right">
    <div class="card">
      <div class="chart-title">
        <h2>Winter pollution shock, not just Delhi</h2>
        <div class="legend-wrap">
          <span><i class="dot m"></i>Monsoon</span>
          <span><i class="dot w"></i>Winter</span>
        </div>
      </div>
      {svg}
      <div class="footer">
        <span>Average AQI: monsoon = Jul–Sep 2023; winter = Jan, Feb, Nov, Dec 2023. Cities shown have sufficient daily records.</span>
        <span>Source: uploaded AQI city-day CSVs</span>
      </div>
    </div>
  </section>
</main>
</body>
</html>
"""

out = Path("/mnt/data/aqi_winter_shock_slide.html")
out.write_text(html_doc, encoding="utf-8")

print(f"Created: {out}")
print("\nChart data:")
print(top[["City", "monsoon_aqi", "winter_aqi", "shock"]].to_string(index=False))
```


```
Created: /mnt/data/aqi_winter_shock_slide.html

Chart data:
     City  monsoon_aqi  winter_aqi  shock
   Purnia           76         296    219
    Delhi          103         319    216
  Katihar           95         310    215
Bhagalpur           85         300    215
  Saharsa           96         305    209
    Patna           86         289    202
   Rajgir           74         274    200
```

</details>

I’ll turn the strongest workshop story into one self-contained 16:9 HTML slide: “Delhi is the headline, but the winter pollution shock is wider and sharper across North India.”

</details>

Analysis errored


```
from pathlib import Path
import zipfile, pandas as pd, numpy as np, html, textwrap, json, os, re

zip_path = Path("/mnt/data/aqi(1).zip")

# Load city-day AQI files
frames = []
with zipfile.ZipFile(zip_path) as z:
    for name in z.namelist():
        if name.lower().endswith(".csv"):
            with z.open(name) as f:
                try:
                    df = pd.read_csv(f)
                except Exception:
                    continue
                # Normalize expected columns
                cols = {c.lower().strip(): c for c in df.columns}
                if "date" in cols and "aqi" in cols:
                    if "city" not in cols:
                        # infer city from filename if missing
                        df["City"] = Path(name).stem.replace("_", " ").replace("-", " ").title()
                    keep = []
                    for c in ["City", "Date", "AQI", "AQI_Bucket", "Prominent_Pollutant"]:
                        if c in df.columns:
                            keep.append(c)
                    frames.append(df[keep])

data = pd.concat(frames, ignore_index=True)
data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
data["AQI"] = pd.to_numeric(data["AQI"], errors="coerce")
data = data.dropna(subset=["Date", "AQI", "City"])
data["year"] = data["Date"].dt.year
data["month"] = data["Date"].dt.month

d2023 = data[data["year"] == 2023].copy()

# Define Indian winter and monsoon for a crisp story
winter = d2023[d2023["month"].isin([1,2,11,12])]
monsoon = d2023[d2023["month"].isin([7,8,9])]

w = winter.groupby("City").agg(winter_aqi=("AQI","mean"), winter_days=("AQI","size"))
m = monsoon.groupby("City").agg(monsoon_aqi=("AQI","mean"), monsoon_days=("AQI","size"))
season = w.join(m, how="inner")
season = season[(season["winter_days"] >= 80) & (season["monsoon_days"] >= 60)]
season["shock"] = season["winter_aqi"] - season["monsoon_aqi"]
top = season.sort_values("shock", ascending=False).head(8).reset_index()
top["winter_aqi"] = top["winter_aqi"].round(0).astype(int)
top["monsoon_aqi"] = top["monsoon_aqi"].round(0).astype(int)
top["shock"] = top["shock"].round(0).astype(int)

# Use the top 7 if available (matches prior analysis well)
rows = top.head(7).to_dict("records")

# City averages for 2023 highlight: Delhi vs worst / cleanest, if in data
city2023 = d2023.groupby("City").agg(avg_aqi=("AQI","mean"), days=("AQI","size")).query("days >= 250").reset_index()
worst = city2023.sort_values("avg_aqi", ascending=False).iloc[0]
delhi = city2023[city2023["City"].str.lower() == "delhi"].iloc[0]
cleanest = city2023.sort_values("avg_aqi", ascending=True).iloc[0]

# Build SVG dumbbell chart
width, height = 1120, 560
left, right = 245, 1010
top_margin, row_gap = 56, 66
min_aqi, max_aqi = 40, 340

def x(aqi):
    return left + (aqi - min_aqi) / (max_aqi - min_aqi) * (right - left)

svg_parts = []
# grid/ticks
for tick in [50, 100, 150, 200, 250, 300]:
    xx = x(tick)
    svg_parts.append(f'<line x1="{xx:.1f}" y1="30" x2="{xx:.1f}" y2="{height-45}" class="grid"/>')
    svg_parts.append(f'<text x="{xx:.1f}" y="{height-16}" class="tick" text-anchor="middle">{tick}</text>')

for i, r in enumerate(rows):
    y = top_margin + i * row_gap
    city = html.escape(str(r["City"]))
    mon = int(r["monsoon_aqi"])
    win = int(r["winter_aqi"])
    shock = int(r["shock"])
    x1, x2 = x(mon), x(win)
    svg_parts.append(f'<text x="16" y="{y+5}" class="city">{city}</text>')
    svg_parts.append(f'<line x1="{x1:.1f}" y1="{y}" x2="{x2:.1f}" y2="{y}" class="range"/>')
    svg_parts.append(f'<circle cx="{x1:.1f}" cy="{y}" r="9" class="monsoon"/>')
    svg_parts.append(f'<circle cx="{x2:.1f}" cy="{y}" r="11" class="winter"/>')
    svg_parts.append(f'<text x="{x1:.1f}" y="{y-17}" class="small" text-anchor="middle">{mon}</text>')
    svg_parts.append(f'<text x="{x2:.1f}" y="{y-17}" class="small strong" text-anchor="middle">{win}</text>')
    svg_parts.append(f'<text x="{right+36}" y="{y+6}" class="shock">+{shock}</text>')

svg = f"""
<svg viewBox="0 0 {width} {height}" role="img" aria-label="Winter versus monsoon AQI shock in Indian cities, 2023">
  <text x="{left}" y="20" class="axis-label">AQI</text>
  {''.join(svg_parts)}
  <text x="{x(95):.1f}" y="{height-16}" class="legend" text-anchor="middle">Monsoon</text>
  <text x="{x(305):.1f}" y="{height-16}" class="legend winter-label" text-anchor="middle">Winter</text>
</svg>
"""

# HTML slide
html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AQI insight slide — winter shock</title>
<style>
  :root {{
    --bg: #f7f3ea;
    --ink: #171717;
    --muted: #5e574c;
    --hair: rgba(23,23,23,.14);
    --monsoon: #2a9d8f;
    --winter: #d1493f;
    --accent: #111827;
    --card: rgba(255,255,255,.64);
  }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; width: 100%; height: 100%; background: var(--bg); color: var(--ink); }}
  body {{
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }}
  .slide {{
    width: 100vw;
    min-height: 100vh;
    aspect-ratio: 16 / 9;
    padding: clamp(28px, 4vw, 72px);
    display: grid;
    grid-template-columns: 1.05fr 1.55fr;
    gap: clamp(24px, 4vw, 70px);
    align-items: center;
    overflow: hidden;
    position: relative;
  }}
  .slide::before {{
    content: "";
    position: absolute;
    width: 720px;
    height: 720px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(209,73,63,.17), rgba(209,73,63,0) 66%);
    top: -260px;
    right: -180px;
    z-index: 0;
  }}
  .slide::after {{
    content: "";
    position: absolute;
    width: 620px;
    height: 620px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(42,157,143,.14), rgba(42,157,143,0) 68%);
    bottom: -280px;
    left: -160px;
    z-index: 0;
  }}
  .left, .right {{ position: relative; z-index: 1; }}
  .eyebrow {{
    display: inline-block;
    font-size: clamp(13px, 1.1vw, 18px);
    letter-spacing: .13em;
    text-transform: uppercase;
    font-weight: 800;
    color: var(--muted);
    margin-bottom: 18px;
  }}
  h1 {{
    font-size: clamp(52px, 6.7vw, 108px);
    line-height: .92;
    letter-spacing: -0.07em;
    margin: 0 0 30px;
    max-width: 820px;
  }}
  .red {{ color: var(--winter); }}
  .dek {{
    font-size: clamp(22px, 2.2vw, 38px);
    line-height: 1.14;
    letter-spacing: -0.035em;
    margin: 0 0 34px;
    color: #25221d;
    max-width: 760px;
  }}
  .stat-grid {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    max-width: 750px;
  }}
  .stat {{
    background: var(--card);
    border: 1px solid var(--hair);
    border-radius: 22px;
    padding: 18px 18px 16px;
    box-shadow: 0 18px 60px rgba(17,24,39,.06);
    backdrop-filter: blur(8px);
  }}
  .num {{
    display: block;
    font-size: clamp(30px, 3.2vw, 54px);
    line-height: 1;
    font-weight: 900;
    letter-spacing: -0.06em;
  }}
  .label {{
    display: block;
    color: var(--muted);
    font-size: clamp(12px, 1vw, 16px);
    line-height: 1.18;
    margin-top: 8px;
    font-weight: 650;
  }}
  .card {{
    background: rgba(255,255,255,.72);
    border: 1px solid var(--hair);
    border-radius: 34px;
    padding: clamp(22px, 2.6vw, 42px);
    box-shadow: 0 24px 90px rgba(17,24,39,.10);
  }}
  .chart-title {{
    display: flex;
    justify-content: space-between;
    gap: 24px;
    align-items: flex-end;
    margin-bottom: 12px;
  }}
  h2 {{
    margin: 0;
    font-size: clamp(24px, 2.2vw, 40px);
    line-height: 1.05;
    letter-spacing: -0.045em;
  }}
  .legend-wrap {{
    display: flex;
    align-items: center;
    gap: 14px;
    color: var(--muted);
    font-weight: 750;
    font-size: 14px;
    white-space: nowrap;
  }}
  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
    vertical-align: -1px;
  }}
  .dot.m {{ background: var(--monsoon); }}
  .dot.w {{ background: var(--winter); }}
  svg {{ width: 100%; height: auto; display: block; }}
  .grid {{ stroke: rgba(23,23,23,.12); stroke-width: 1; }}
  .tick, .axis-label, .small, .legend {{
    fill: var(--muted);
    font-size: 18px;
    font-weight: 700;
  }}
  .axis-label {{ font-size: 17px; }}
  .city {{
    fill: var(--ink);
    font-size: 24px;
    font-weight: 850;
    letter-spacing: -0.02em;
  }}
  .range {{
    stroke: rgba(23,23,23,.22);
    stroke-width: 8;
    stroke-linecap: round;
  }}
  .monsoon {{ fill: var(--monsoon); stroke: white; stroke-width: 4; }}
  .winter {{ fill: var(--winter); stroke: white; stroke-width: 4; }}
  .small {{ font-size: 17px; }}
  .strong {{ fill: var(--winter); font-weight: 900; }}
  .shock {{
    fill: var(--winter);
    font-size: 25px;
    font-weight: 950;
    letter-spacing: -0.04em;
  }}
  .footer {{
    margin-top: 14px;
    color: var(--muted);
    font-size: clamp(12px, .95vw, 15px);
    line-height: 1.35;
    display: flex;
    justify-content: space-between;
    gap: 18px;
    border-top: 1px solid var(--hair);
    padding-top: 14px;
  }}
  .callout {{
    margin-top: 20px;
    font-size: clamp(17px, 1.45vw, 24px);
    line-height: 1.22;
    font-weight: 780;
    letter-spacing: -0.025em;
  }}
  @media print {{
    body {{ width: 16in; height: 9in; }}
    .slide {{ width: 16in; height: 9in; min-height: auto; }}
  }}
  @media (max-aspect-ratio: 4/3) {{
    .slide {{ grid-template-columns: 1fr; aspect-ratio: auto; }}
    h1 {{ font-size: clamp(46px, 12vw, 88px); }}
  }}
</style>
</head>
<body>
<main class="slide">
  <section class="left">
    <div class="eyebrow">India AQI · 300k city-days · 2023</div>
    <h1>Delhi is the headline.<br><span class="red">Winter is the story.</span></h1>
    <p class="dek">Across North India, the air can get more than <strong>200 AQI points worse</strong> in winter than in monsoon.</p>
    <div class="stat-grid">
      <div class="stat">
        <span class="num">+221</span>
        <span class="label">largest winter jump: Bhagalpur</span>
      </div>
      <div class="stat">
        <span class="num">#4</span>
        <span class="label">Delhi’s rank among worst 2023 city averages</span>
      </div>
      <div class="stat">
        <span class="num">6.7×</span>
        <span class="label">AQI gap: Byrnihat vs Silchar</span>
      </div>
    </div>
    <p class="callout">The workshop hook: don’t ask “which city is polluted?” Ask “which cities become unlivable, in which season, and why?”</p>
  </section>

  <section class="right">
    <div class="card">
      <div class="chart-title">
        <h2>Winter pollution shock, not just Delhi</h2>
        <div class="legend-wrap">
          <span><i class="dot m"></i>Monsoon</span>
          <span><i class="dot w"></i>Winter</span>
        </div>
      </div>
      {svg}
      <div class="footer">
        <span>Average AQI: monsoon = Jul–Sep 2023; winter = Jan, Feb, Nov, Dec 2023. Cities shown have sufficient daily records.</span>
        <span>Source: uploaded AQI city-day CSVs</span>
      </div>
    </div>
  </section>
</main>
</body>
</html>
"""

out = Path("/mnt/data/aqi_winter_shock_slide.html")
out.write_text(html_doc, encoding="utf-8")
print(f"Created {out}")
print("Data used:")
print(top[["City", "monsoon_aqi", "winter_aqi", "shock"]].head(7).to_string(index=False))
```


```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[24], line 28
     24                         if c in df.columns:
     25                             keep.append(c)
     26                     frames.append(df[keep])
     27
---> 28 data = pd.concat(frames, ignore_index=True)
     29 data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
     30 data["AQI"] = pd.to_numeric(data["AQI"], errors="coerce")
     31 data = data.dropna(subset=["Date", "AQI", "City"])

File /opt/pyvenv/lib/python3.13/site-packages/pandas/core/reshape/concat.py:382, in concat(objs, axis, join, ignore_index, keys, levels, names, verify_integrity, sort, copy)
    379 elif copy and using_copy_on_write():
    380     copy = False
--> 382 op = _Concatenator(
    383     objs,
    384     axis=axis,
    385     ignore_index=ignore_index,
    386     join=join,
    387     keys=keys,
    388     levels=levels,
    389     names=names,
    390     verify_integrity=verify_integrity,
    391     copy=copy,
    392     sort=sort,
    393 )
    395 return op.get_result()

File /opt/pyvenv/lib/python3.13/site-packages/pandas/core/reshape/concat.py:445, in _Concatenator.__init__(self, objs, axis, join, keys, levels, names, ignore_index, verify_integrity, copy, sort)
    442 self.verify_integrity = verify_integrity
    443 self.copy = copy
--> 445 objs, keys = self._clean_keys_and_objs(objs, keys)
    447 # figure out what our result ndim is going to be
    448 ndims = self._get_ndims(objs)

File /opt/pyvenv/lib/python3.13/site-packages/pandas/core/reshape/concat.py:507, in _Concatenator._clean_keys_and_objs(self, objs, keys)
    504     objs_list = list(objs)
    506 if len(objs_list) == 0:
--> 507     raise ValueError("No objects to concatenate")
    509 if keys is None:
    510     objs_list = list(com.not_none(*objs_list))

ValueError: No objects to concatenate
```

Analyzed


```
from pathlib import Path
import zipfile, pandas as pd, html

zip_path = Path("/mnt/data/aqi(1).zip")

frames = []
with zipfile.ZipFile(zip_path) as z:
    for name in z.namelist():
        if not name.lower().endswith(".csv"):
            continue
        with z.open(name) as f:
            df = pd.read_csv(f)
        if {"date", "City", "Index Value"}.issubset(df.columns):
            keep = ["date", "City", "Index Value"]
            if "Air Quality" in df.columns:
                keep.append("Air Quality")
            if "Prominent Pollutant" in df.columns:
                keep.append("Prominent Pollutant")
            frames.append(df[keep].copy())

data = pd.concat(frames, ignore_index=True)
data["Date"] = pd.to_datetime(data["date"], errors="coerce")
data["AQI"] = pd.to_numeric(data["Index Value"], errors="coerce")
data = data.dropna(subset=["Date", "AQI", "City"])
data["year"] = data["Date"].dt.year
data["month"] = data["Date"].dt.month

d2023 = data[data["year"] == 2023].copy()

# Indian winter and monsoon, enough data guardrails
winter = d2023[d2023["month"].isin([1, 2, 11, 12])]
monsoon = d2023[d2023["month"].isin([7, 8, 9])]

w = winter.groupby("City").agg(winter_aqi=("AQI", "mean"), winter_days=("AQI", "size"))
m = monsoon.groupby("City").agg(monsoon_aqi=("AQI", "mean"), monsoon_days=("AQI", "size"))
season = w.join(m, how="inner")
season = season[(season["winter_days"] >= 80) & (season["monsoon_days"] >= 60)]
season["shock"] = season["winter_aqi"] - season["monsoon_aqi"]
top = season.sort_values("shock", ascending=False).head(7).reset_index()
top["winter_aqi"] = top["winter_aqi"].round(0).astype(int)
top["monsoon_aqi"] = top["monsoon_aqi"].round(0).astype(int)
top["shock"] = top["shock"].round(0).astype(int)
rows = top.to_dict("records")

city2023 = d2023.groupby("City").agg(avg_aqi=("AQI", "mean"), days=("AQI", "size")).query("days >= 250").reset_index()
worst = city2023.sort_values("avg_aqi", ascending=False).iloc[0]
delhi = city2023[city2023["City"].str.lower() == "delhi"].iloc[0]
cleanest = city2023.sort_values("avg_aqi", ascending=True).iloc[0]

worst_city = str(worst["City"])
worst_avg = float(worst["avg_aqi"])
clean_city = str(cleanest["City"])
clean_avg = float(cleanest["avg_aqi"])
gap = worst_avg / clean_avg
delhi_rank = int(city2023.sort_values("avg_aqi", ascending=False).reset_index(drop=True)
                 .query("City.str.lower() == 'delhi'", engine="python").index[0] + 1)

# SVG chart
width, height = 1120, 560
left, right = 245, 1010
top_margin, row_gap = 56, 66
min_aqi, max_aqi = 40, 340

def sx(aqi):
    return left + (aqi - min_aqi) / (max_aqi - min_aqi) * (right - left)

svg_parts = []
for tick in [50, 100, 150, 200, 250, 300]:
    xx = sx(tick)
    svg_parts.append(f'<line x1="{xx:.1f}" y1="30" x2="{xx:.1f}" y2="{height-45}" class="grid"/>')
    svg_parts.append(f'<text x="{xx:.1f}" y="{height-16}" class="tick" text-anchor="middle">{tick}</text>')

for i, r in enumerate(rows):
    y = top_margin + i * row_gap
    city = html.escape(str(r["City"]))
    mon = int(r["monsoon_aqi"])
    win = int(r["winter_aqi"])
    shock = int(r["shock"])
    x1, x2 = sx(mon), sx(win)
    svg_parts.append(f'<text x="16" y="{y+5}" class="city">{city}</text>')
    svg_parts.append(f'<line x1="{x1:.1f}" y1="{y}" x2="{x2:.1f}" y2="{y}" class="range"/>')
    svg_parts.append(f'<circle cx="{x1:.1f}" cy="{y}" r="9" class="monsoon"/>')
    svg_parts.append(f'<circle cx="{x2:.1f}" cy="{y}" r="11" class="winter"/>')
    svg_parts.append(f'<text x="{x1:.1f}" y="{y-17}" class="small" text-anchor="middle">{mon}</text>')
    svg_parts.append(f'<text x="{x2:.1f}" y="{y-17}" class="small strong" text-anchor="middle">{win}</text>')
    svg_parts.append(f'<text x="{right+36}" y="{y+6}" class="shock">+{shock}</text>')

svg = f"""
<svg viewBox="0 0 {width} {height}" role="img" aria-label="Winter versus monsoon AQI shock in Indian cities, 2023">
  <text x="{left}" y="20" class="axis-label">AQI</text>
  {''.join(svg_parts)}
  <text x="{sx(95):.1f}" y="{height-16}" class="legend" text-anchor="middle">Monsoon</text>
  <text x="{sx(305):.1f}" y="{height-16}" class="legend winter-label" text-anchor="middle">Winter</text>
</svg>
"""

html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AQI insight slide — winter shock</title>
<style>
  :root {{
    --bg: #f7f3ea;
    --ink: #171717;
    --muted: #5e574c;
    --hair: rgba(23,23,23,.14);
    --monsoon: #2a9d8f;
    --winter: #d1493f;
    --card: rgba(255,255,255,.68);
  }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; width: 100%; min-height: 100%; background: var(--bg); color: var(--ink); }}
  body {{
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }}
  .slide {{
    width: 100vw;
    min-height: 100vh;
    aspect-ratio: 16 / 9;
    padding: clamp(28px, 4vw, 72px);
    display: grid;
    grid-template-columns: 1.05fr 1.55fr;
    gap: clamp(24px, 4vw, 70px);
    align-items: center;
    overflow: hidden;
    position: relative;
  }}
  .slide::before {{
    content: "";
    position: absolute;
    width: 720px;
    height: 720px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(209,73,63,.17), rgba(209,73,63,0) 66%);
    top: -260px;
    right: -180px;
    z-index: 0;
  }}
  .slide::after {{
    content: "";
    position: absolute;
    width: 620px;
    height: 620px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(42,157,143,.14), rgba(42,157,143,0) 68%);
    bottom: -280px;
    left: -160px;
    z-index: 0;
  }}
  .left, .right {{ position: relative; z-index: 1; }}
  .eyebrow {{
    display: inline-block;
    font-size: clamp(13px, 1.1vw, 18px);
    letter-spacing: .13em;
    text-transform: uppercase;
    font-weight: 800;
    color: var(--muted);
    margin-bottom: 18px;
  }}
  h1 {{
    font-size: clamp(52px, 6.7vw, 108px);
    line-height: .92;
    letter-spacing: -0.07em;
    margin: 0 0 30px;
    max-width: 820px;
  }}
  .red {{ color: var(--winter); }}
  .dek {{
    font-size: clamp(22px, 2.2vw, 38px);
    line-height: 1.14;
    letter-spacing: -0.035em;
    margin: 0 0 34px;
    color: #25221d;
    max-width: 760px;
  }}
  .stat-grid {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    max-width: 750px;
  }}
  .stat {{
    background: var(--card);
    border: 1px solid var(--hair);
    border-radius: 22px;
    padding: 18px 18px 16px;
    box-shadow: 0 18px 60px rgba(17,24,39,.06);
    backdrop-filter: blur(8px);
  }}
  .num {{
    display: block;
    font-size: clamp(30px, 3.2vw, 54px);
    line-height: 1;
    font-weight: 900;
    letter-spacing: -0.06em;
  }}
  .label {{
    display: block;
    color: var(--muted);
    font-size: clamp(12px, 1vw, 16px);
    line-height: 1.18;
    margin-top: 8px;
    font-weight: 650;
  }}
  .card {{
    background: rgba(255,255,255,.72);
    border: 1px solid var(--hair);
    border-radius: 34px;
    padding: clamp(22px, 2.6vw, 42px);
    box-shadow: 0 24px 90px rgba(17,24,39,.10);
  }}
  .chart-title {{
    display: flex;
    justify-content: space-between;
    gap: 24px;
    align-items: flex-end;
    margin-bottom: 12px;
  }}
  h2 {{
    margin: 0;
    font-size: clamp(24px, 2.2vw, 40px);
    line-height: 1.05;
    letter-spacing: -0.045em;
  }}
  .legend-wrap {{
    display: flex;
    align-items: center;
    gap: 14px;
    color: var(--muted);
    font-weight: 750;
    font-size: 14px;
    white-space: nowrap;
  }}
  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
    vertical-align: -1px;
  }}
  .dot.m {{ background: var(--monsoon); }}
  .dot.w {{ background: var(--winter); }}
  svg {{ width: 100%; height: auto; display: block; }}
  .grid {{ stroke: rgba(23,23,23,.12); stroke-width: 1; }}
  .tick, .axis-label, .small, .legend {{
    fill: var(--muted);
    font-size: 18px;
    font-weight: 700;
  }}
  .axis-label {{ font-size: 17px; }}
  .city {{
    fill: var(--ink);
    font-size: 24px;
    font-weight: 850;
    letter-spacing: -0.02em;
  }}
  .range {{
    stroke: rgba(23,23,23,.22);
    stroke-width: 8;
    stroke-linecap: round;
  }}
  .monsoon {{ fill: var(--monsoon); stroke: white; stroke-width: 4; }}
  .winter {{ fill: var(--winter); stroke: white; stroke-width: 4; }}
  .small {{ font-size: 17px; }}
  .strong {{ fill: var(--winter); font-weight: 900; }}
  .shock {{
    fill: var(--winter);
    font-size: 25px;
    font-weight: 950;
    letter-spacing: -0.04em;
  }}
  .footer {{
    margin-top: 14px;
    color: var(--muted);
    font-size: clamp(12px, .95vw, 15px);
    line-height: 1.35;
    display: flex;
    justify-content: space-between;
    gap: 18px;
    border-top: 1px solid var(--hair);
    padding-top: 14px;
  }}
  .callout {{
    margin-top: 20px;
    font-size: clamp(17px, 1.45vw, 24px);
    line-height: 1.22;
    font-weight: 780;
    letter-spacing: -0.025em;
  }}
  @media print {{
    body {{ width: 16in; height: 9in; }}
    .slide {{ width: 16in; height: 9in; min-height: auto; }}
  }}
  @media (max-aspect-ratio: 4/3) {{
    .slide {{ grid-template-columns: 1fr; aspect-ratio: auto; }}
    h1 {{ font-size: clamp(46px, 12vw, 88px); }}
  }}
</style>
</head>
<body>
<main class="slide">
  <section class="left">
    <div class="eyebrow">India AQI · {len(data):,} city-days · 2023</div>
    <h1>Delhi is the headline.<br><span class="red">Winter is the story.</span></h1>
    <p class="dek">Across North India, the air can get more than <strong>200 AQI points worse</strong> in winter than in monsoon.</p>
    <div class="stat-grid">
      <div class="stat">
        <span class="num">+{int(top.iloc[0]["shock"])}</span>
        <span class="label">largest winter jump: {html.escape(str(top.iloc[0]["City"]))}</span>
      </div>
      <div class="stat">
        <span class="num">#{delhi_rank}</span>
        <span class="label">Delhi’s rank among worst 2023 city averages</span>
      </div>
      <div class="stat">
        <span class="num">{gap:.1f}×</span>
        <span class="label">AQI gap: {html.escape(worst_city)} vs {html.escape(clean_city)}</span>
      </div>
    </div>
    <p class="callout">The workshop hook: don’t ask “which city is polluted?” Ask “which cities become unlivable, in which season, and why?”</p>
  </section>

  <section class="right">
    <div class="card">
      <div class="chart-title">
        <h2>Winter pollution shock, not just Delhi</h2>
        <div class="legend-wrap">
          <span><i class="dot m"></i>Monsoon</span>
          <span><i class="dot w"></i>Winter</span>
        </div>
      </div>
      {svg}
      <div class="footer">
        <span>Average AQI: monsoon = Jul–Sep 2023; winter = Jan, Feb, Nov, Dec 2023. Cities shown have sufficient daily records.</span>
        <span>Source: uploaded AQI city-day CSVs</span>
      </div>
    </div>
  </section>
</main>
</body>
</html>
"""

out = Path("/mnt/data/aqi_winter_shock_slide.html")
out.write_text(html_doc, encoding="utf-8")

print(f"Created: {out}")
print("\nChart data:")
print(top[["City", "monsoon_aqi", "winter_aqi", "shock"]].to_string(index=False))
```

STDOUT/STDERR


```
Created: /mnt/data/aqi_winter_shock_slide.html

Chart data:
     City  monsoon_aqi  winter_aqi  shock
   Purnia           76         296    219
    Delhi          103         319    216
  Katihar           95         310    215
Bhagalpur           85         300    215
  Saharsa           96         305    209
    Patna           86         289    202
   Rajgir           74         274    200
```

Created the single-page HTML slide here:

Download the HTML slide

It visualizes the key insight: **Delhi is the headline, but the bigger story is the winter AQI shock across North India.**

aqi_winter_shock_slide.html


```
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AQI insight slide — winter shock</title>
<style>
  :root {
    --bg: #f7f3ea;
    --ink: #171717;
    --muted: #5e574c;
    --hair: rgba(23,23,23,.14);
    --monsoon: #2a9d8f;
    --winter: #d1493f;
    --card: rgba(255,255,255,.68);
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; width: 100%; min-height: 100%; background: var(--bg); color: var(--ink); }
  body {
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }
  .slide {
    width: 100vw;
    min-height: 100vh;
    aspect-ratio: 16 / 9;
    padding: clamp(28px, 4vw, 72px);
    display: grid;
    grid-template-columns: 1.05fr 1.55fr;
    gap: clamp(24px, 4vw, 70px);
    align-items: center;
    overflow: hidden;
    position: relative;
  }
  .slide::before {
    content: "";
    position: absolute;
    width: 720px;
    height: 720px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(209,73,63,.17), rgba(209,73,63,0) 66%);
    top: -260px;
    right: -180px;
    z-index: 0;
  }
  .slide::after {
    content: "";
    position: absolute;
    width: 620px;
    height: 620px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(42,157,143,.14), rgba(42,157,143,0) 68%);
    bottom: -280px;
    left: -160px;
    z-index: 0;
  }
  .left, .right { position: relative; z-index: 1; }
  .eyebrow {
    display: inline-block;
    font-size: clamp(13px, 1.1vw, 18px);
    letter-spacing: .13em;
    text-transform: uppercase;
    font-weight: 800;
    color: var(--muted);
    margin-bottom: 18px;
  }
  h1 {
    font-size: clamp(52px, 6.7vw, 108px);
    line-height: .92;
    letter-spacing: -0.07em;
    margin: 0 0 30px;
    max-width: 820px;
  }
  .red { color: var(--winter); }
  .dek {
    font-size: clamp(22px, 2.2vw, 38px);
    line-height: 1.14;
    letter-spacing: -0.035em;
    margin: 0 0 34px;
    color: #25221d;
    max-width: 760px;
  }
  .stat-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    max-width: 750px;
  }
  .stat {
    background: var(--card);
    border: 1px solid var(--hair);
    border-radius: 22px;
    padding: 18px 18px 16px;
    box-shadow: 0 18px 60px rgba(17,24,39,.06);
    backdrop-filter: blur(8px);
  }
  .num {
    display: block;
    font-size: clamp(30px, 3.2vw, 54px);
    line-height: 1;
    font-weight: 900;
    letter-spacing: -0.06em;
  }
  .label {
    display: block;
    color: var(--muted);
    font-size: clamp(12px, 1vw, 16px);
    line-height: 1.18;
    margin-top: 8px;
    font-weight: 650;
  }
  .card {
    background: rgba(255,255,255,.72);
    border: 1px solid var(--hair);
    border-radius: 34px;
    padding: clamp(22px, 2.6vw, 42px);
    box-shadow: 0 24px 90px rgba(17,24,39,.10);
  }
  .chart-title {
    display: flex;
    justify-content: space-between;
    gap: 24px;
    align-items: flex-end;
    margin-bottom: 12px;
  }
  h2 {
    margin: 0;
    font-size: clamp(24px, 2.2vw, 40px);
    line-height: 1.05;
    letter-spacing: -0.045em;
  }
  .legend-wrap {
    display: flex;
    align-items: center;
    gap: 14px;
    color: var(--muted);
    font-weight: 750;
    font-size: 14px;
    white-space: nowrap;
  }
  .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
    vertical-align: -1px;
  }
  .dot.m { background: var(--monsoon); }
  .dot.w { background: var(--winter); }
  svg { width: 100%; height: auto; display: block; }
  .grid { stroke: rgba(23,23,23,.12); stroke-width: 1; }
  .tick, .axis-label, .small, .legend {
    fill: var(--muted);
    font-size: 18px;
    font-weight: 700;
  }
  .axis-label { font-size: 17px; }
  .city {
    fill: var(--ink);
    font-size: 24px;
    font-weight: 850;
    letter-spacing: -0.02em;
  }
  .range {
    stroke: rgba(23,23,23,.22);
    stroke-width: 8;
    stroke-linecap: round;
  }
  .monsoon { fill: var(--monsoon); stroke: white; stroke-width: 4; }
  .winter { fill: var(--winter); stroke: white; stroke-width: 4; }
  .small { font-size: 17px; }
  .strong { fill: var(--winter); font-weight: 900; }
  .shock {
    fill: var(--winter);
    font-size: 25px;
    font-weight: 950;
    letter-spacing: -0.04em;
  }
  .footer {
    margin-top: 14px;
    color: var(--muted);
    font-size: clamp(12px, .95vw, 15px);
    line-height: 1.35;
    display: flex;
    justify-content: space-between;
    gap: 18px;
    border-top: 1px solid var(--hair);
    padding-top: 14px;
  }
  .callout {
    margin-top: 20px;
    font-size: clamp(17px, 1.45vw, 24px);
    line-height: 1.22;
    font-weight: 780;
    letter-spacing: -0.025em;
  }
  @media print {
    body { width: 16in; height: 9in; }
    .slide { width: 16in; height: 9in; min-height: auto; }
  }
  @media (max-aspect-ratio: 4/3) {
    .slide { grid-template-columns: 1fr; aspect-ratio: auto; }
    h1 { font-size: clamp(46px, 12vw, 88px); }
  }
</style>
</head>
<body>
<main class="slide">
  <section class="left">
    <div class="eyebrow">India AQI · 299,972 city-days · 2023</div>
    <h1>Delhi is the headline.<br><span class="red">Winter is the story.</span></h1>
    <p class="dek">Across North India, the air can get more than <strong>200 AQI points worse</strong> in winter than in monsoon.</p>
    <div class="stat-grid">
      <div class="stat">
        <span class="num">+219</span>
        <span class="label">largest winter jump: Purnia</span>
      </div>
      <div class="stat">
        <span class="num">#4</span>
        <span class="label">Delhi’s rank among worst 2023 city averages</span>
      </div>
      <div class="stat">
        <span class="num">6.7×</span>
        <span class="label">AQI gap: Byrnihat vs Silchar</span>
      </div>
    </div>
    <p class="callout">The workshop hook: don’t ask “which city is polluted?” Ask “which cities become unlivable, in which season, and why?”</p>
  </section>

  <section class="right">
    <div class="card">
      <div class="chart-title">
        <h2>Winter pollution shock, not just Delhi</h2>
        <div class="legend-wrap">
          <span><i class="dot m"></i>Monsoon</span>
          <span><i class="dot w"></i>Winter</span>
        </div>
      </div>

<svg viewBox="0 0 1120 560" role="img" aria-label="Winter versus monsoon AQI shock in Indian cities, 2023">
  <text x="245" y="20" class="axis-label">AQI</text>
  <line x1="270.5" y1="30" x2="270.5" y2="515" class="grid"/><text x="270.5" y="544" class="tick" text-anchor="middle">50</text><line x1="398.0" y1="30" x2="398.0" y2="515" class="grid"/><text x="398.0" y="544" class="tick" text-anchor="middle">100</text><line x1="525.5" y1="30" x2="525.5" y2="515" class="grid"/><text x="525.5" y="544" class="tick" text-anchor="middle">150</text><line x1="653.0" y1="30" x2="653.0" y2="515" class="grid"/><text x="653.0" y="544" class="tick" text-anchor="middle">200</text><line x1="780.5" y1="30" x2="780.5" y2="515" class="grid"/><text x="780.5" y="544" class="tick" text-anchor="middle">250</text><line x1="908.0" y1="30" x2="908.0" y2="515" class="grid"/><text x="908.0" y="544" class="tick" text-anchor="middle">300</text><text x="16" y="61" class="city">Purnia</text><line x1="336.8" y1="56" x2="897.8" y2="56" class="range"/><circle cx="336.8" cy="56" r="9" class="monsoon"/><circle cx="897.8" cy="56" r="11" class="winter"/><text x="336.8" y="39" class="small" text-anchor="middle">76</text><text x="897.8" y="39" class="small strong" text-anchor="middle">296</text><text x="1046" y="62" class="shock">+219</text><text x="16" y="127" class="city">Delhi</text><line x1="405.6" y1="122" x2="956.5" y2="122" class="range"/><circle cx="405.6" cy="122" r="9" class="monsoon"/><circle cx="956.5" cy="122" r="11" class="winter"/><text x="405.6" y="105" class="small" text-anchor="middle">103</text><text x="956.5" y="105" class="small strong" text-anchor="middle">319</text><text x="1046" y="128" class="shock">+216</text><text x="16" y="193" class="city">Katihar</text><line x1="385.2" y1="188" x2="933.5" y2="188" class="range"/><circle cx="385.2" cy="188" r="9" class="monsoon"/><circle cx="933.5" cy="188" r="11" class="winter"/><text x="385.2" y="171" class="small" text-anchor="middle">95</text><text x="933.5" y="171" class="small strong" text-anchor="middle">310</text><text x="1046" y="194" class="shock">+215</text><text x="16" y="259" class="city">Bhagalpur</text><line x1="359.8" y1="254" x2="908.0" y2="254" class="range"/><circle cx="359.8" cy="254" r="9" class="monsoon"/><circle cx="908.0" cy="254" r="11" class="winter"/><text x="359.8" y="237" class="small" text-anchor="middle">85</text><text x="908.0" y="237" class="small strong" text-anchor="middle">300</text><text x="1046" y="260" class="shock">+215</text><text x="16" y="325" class="city">Saharsa</text><line x1="387.8" y1="320" x2="920.8" y2="320" class="range"/><circle cx="387.8" cy="320" r="9" class="monsoon"/><circle cx="920.8" cy="320" r="11" class="winter"/><text x="387.8" y="303" class="small" text-anchor="middle">96</text><text x="920.8" y="303" class="small strong" text-anchor="middle">305</text><text x="1046" y="326" class="shock">+209</text><text x="16" y="391" class="city">Patna</text><line x1="362.3" y1="386" x2="879.9" y2="386" class="range"/><circle cx="362.3" cy="386" r="9" class="monsoon"/><circle cx="879.9" cy="386" r="11" class="winter"/><text x="362.3" y="369" class="small" text-anchor="middle">86</text><text x="879.9" y="369" class="small strong" text-anchor="middle">289</text><text x="1046" y="392" class="shock">+202</text><text x="16" y="457" class="city">Rajgir</text><line x1="331.7" y1="452" x2="841.7" y2="452" class="range"/><circle cx="331.7" cy="452" r="9" class="monsoon"/><circle cx="841.7" cy="452" r="11" class="winter"/><text x="331.7" y="435" class="small" text-anchor="middle">74</text><text x="841.7" y="435" class="small strong" text-anchor="middle">274</text><text x="1046" y="458" class="shock">+200</text>
  <text x="385.2" y="544" class="legend" text-anchor="middle">Monsoon</text>
  <text x="920.8" y="544" class="legend winter-label" text-anchor="middle">Winter</text>
</svg>

      <div class="footer">
        <span>Average AQI: monsoon = Jul–Sep 2023; winter = Jan, Feb, Nov, Dec 2023. Cities shown have sufficient daily records.</span>
        <span>Source: uploaded AQI city-day CSVs</span>
      </div>
    </div>
  </section>
</main>
</body>
</html>
```

---

## User

Hold on, Ghaziabad is not on that list. I can understand why you may not have included it. The gap between monsoon and winter is not as large in Ghaziabad maybe, but since Ghaziabad has such high pollution, in fact even higher than Delhi, as per your claim, let's include it because that will give people a point of reference.

---

## ChatGPT

Analyzed


```
from pathlib import Path
import zipfile, pandas as pd, html

zip_path = Path("/mnt/data/aqi(1).zip")

frames = []
with zipfile.ZipFile(zip_path) as z:
    for name in z.namelist():
        if not name.lower().endswith(".csv"):
            continue
        with z.open(name) as f:
            df = pd.read_csv(f)
        if {"date", "City", "Index Value"}.issubset(df.columns):
            keep = ["date", "City", "Index Value"]
            if "Air Quality" in df.columns:
                keep.append("Air Quality")
            if "Prominent Pollutant" in df.columns:
                keep.append("Prominent Pollutant")
            frames.append(df[keep].copy())

data = pd.concat(frames, ignore_index=True)
data["Date"] = pd.to_datetime(data["date"], errors="coerce")
data["AQI"] = pd.to_numeric(data["Index Value"], errors="coerce")
data = data.dropna(subset=["Date", "AQI", "City"])
data["year"] = data["Date"].dt.year
data["month"] = data["Date"].dt.month

d2023 = data[data["year"] == 2023].copy()

# 2023 city averages
city2023 = (
    d2023.groupby("City")
    .agg(avg_aqi=("AQI", "mean"), days=("AQI", "size"))
    .query("days >= 250")
    .reset_index()
    .sort_values("avg_aqi", ascending=False)
    .reset_index(drop=True)
)
city2023["rank"] = city2023.index + 1
delhi_row = city2023[city2023["City"].str.lower() == "delhi"].iloc[0]
ghaziabad_row = city2023[city2023["City"].str.lower() == "ghaziabad"].iloc[0]
worst_row = city2023.iloc[0]
clean_row = city2023.sort_values("avg_aqi").iloc[0]

# Winter vs monsoon
winter = d2023[d2023["month"].isin([1, 2, 11, 12])]
monsoon = d2023[d2023["month"].isin([7, 8, 9])]

w = winter.groupby("City").agg(winter_aqi=("AQI", "mean"), winter_days=("AQI", "size"))
m = monsoon.groupby("City").agg(monsoon_aqi=("AQI", "mean"), monsoon_days=("AQI", "size"))
season = w.join(m, how="inner")
season = season[(season["winter_days"] >= 80) & (season["monsoon_days"] >= 60)]
season["shock"] = season["winter_aqi"] - season["monsoon_aqi"]
season = season.reset_index()
season["winter_aqi"] = season["winter_aqi"].round(0).astype(int)
season["monsoon_aqi"] = season["monsoon_aqi"].round(0).astype(int)
season["shock"] = season["shock"].round(0).astype(int)

# Use top 6 shock cities plus Ghaziabad as reference, if not already in top 6
top6 = season.sort_values("shock", ascending=False).head(6)
ghaz = season[season["City"].str.lower() == "ghaziabad"]
plot_df = pd.concat([top6, ghaz], ignore_index=True).drop_duplicates(subset=["City"])
plot_df["is_ghaziabad"] = plot_df["City"].str.lower().eq("ghaziabad")
plot_df = plot_df.sort_values(["is_ghaziabad", "shock"], ascending=[True, False]).reset_index(drop=True)

# Put Ghaziabad after Delhi if Delhi exists, otherwise at end; better as reference near Delhi
if "Ghaziabad" in plot_df["City"].values and "Delhi" in plot_df["City"].values:
    records = plot_df.to_dict("records")
    ghaz_rec = [r for r in records if r["City"] == "Ghaziabad"][0]
    records = [r for r in records if r["City"] != "Ghaziabad"]
    new_records = []
    for r in records:
        new_records.append(r)
        if r["City"] == "Delhi":
            new_records.append(ghaz_rec)
    rows = new_records
else:
    rows = plot_df.to_dict("records")

# SVG dumbbell chart
width, height = 1120, 590
left, right = 250, 1000
top_margin, row_gap = 56, 68
min_aqi, max_aqi = 40, 340

def sx(aqi):
    return left + (aqi - min_aqi) / (max_aqi - min_aqi) * (right - left)

svg_parts = []
for tick in [50, 100, 150, 200, 250, 300]:
    xx = sx(tick)
    svg_parts.append(f'<line x1="{xx:.1f}" y1="30" x2="{xx:.1f}" y2="{height-48}" class="grid"/>')
    svg_parts.append(f'<text x="{xx:.1f}" y="{height-18}" class="tick" text-anchor="middle">{tick}</text>')

for i, r in enumerate(rows):
    y = top_margin + i * row_gap
    city = html.escape(str(r["City"]))
    mon = int(r["monsoon_aqi"])
    win = int(r["winter_aqi"])
    shock = int(r["shock"])
    x1, x2 = sx(mon), sx(win)
    ref_class = " ref" if str(r["City"]).lower() == "ghaziabad" else ""
    city_label = city + (" ★" if str(r["City"]).lower() == "ghaziabad" else "")
    svg_parts.append(f'<text x="16" y="{y+5}" class="city{ref_class}">{city_label}</text>')
    svg_parts.append(f'<line x1="{x1:.1f}" y1="{y}" x2="{x2:.1f}" y2="{y}" class="range{ref_class}"/>')
    svg_parts.append(f'<circle cx="{x1:.1f}" cy="{y}" r="9" class="monsoon"/>')
    svg_parts.append(f'<circle cx="{x2:.1f}" cy="{y}" r="11" class="winter{ref_class}"/>')
    svg_parts.append(f'<text x="{x1:.1f}" y="{y-17}" class="small" text-anchor="middle">{mon}</text>')
    svg_parts.append(f'<text x="{x2:.1f}" y="{y-17}" class="small strong" text-anchor="middle">{win}</text>')
    svg_parts.append(f'<text x="{right+38}" y="{y+6}" class="shock{ref_class}">+{shock}</text>')

svg = f"""
<svg viewBox="0 0 {width} {height}" role="img" aria-label="Winter versus monsoon AQI shock in Indian cities, 2023, including Ghaziabad as a reference city">
  <text x="{left}" y="20" class="axis-label">AQI</text>
  {''.join(svg_parts)}
  <text x="{sx(95):.1f}" y="{height-18}" class="legend" text-anchor="middle">Monsoon</text>
  <text x="{sx(305):.1f}" y="{height-18}" class="legend winter-label" text-anchor="middle">Winter</text>
</svg>
"""

# Text claims after verification
delhi_avg = float(delhi_row["avg_aqi"])
ghaz_avg = float(ghaziabad_row["avg_aqi"])
ghaz_rank = int(ghaziabad_row["rank"])
delhi_rank = int(delhi_row["rank"])
higher_text = "higher than Delhi" if ghaz_avg > delhi_avg else "slightly lower than Delhi"
comparison = f"Ghaziabad: {ghaz_avg:.0f} avg AQI, rank #{ghaz_rank}; Delhi: {delhi_avg:.0f}, rank #{delhi_rank}"

html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AQI insight slide — winter shock with Ghaziabad</title>
<style>
  :root {{
    --bg: #f7f3ea;
    --ink: #171717;
    --muted: #5e574c;
    --hair: rgba(23,23,23,.14);
    --monsoon: #2a9d8f;
    --winter: #d1493f;
    --ghaz: #7c3aed;
    --card: rgba(255,255,255,.68);
  }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; width: 100%; min-height: 100%; background: var(--bg); color: var(--ink); }}
  body {{
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }}
  .slide {{
    width: 100vw;
    min-height: 100vh;
    aspect-ratio: 16 / 9;
    padding: clamp(28px, 4vw, 72px);
    display: grid;
    grid-template-columns: 1.04fr 1.56fr;
    gap: clamp(24px, 4vw, 64px);
    align-items: center;
    overflow: hidden;
    position: relative;
  }}
  .slide::before {{
    content: "";
    position: absolute;
    width: 720px;
    height: 720px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(209,73,63,.17), rgba(209,73,63,0) 66%);
    top: -260px;
    right: -180px;
    z-index: 0;
  }}
  .slide::after {{
    content: "";
    position: absolute;
    width: 620px;
    height: 620px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(42,157,143,.14), rgba(42,157,143,0) 68%);
    bottom: -280px;
    left: -160px;
    z-index: 0;
  }}
  .left, .right {{ position: relative; z-index: 1; }}
  .eyebrow {{
    display: inline-block;
    font-size: clamp(13px, 1.1vw, 18px);
    letter-spacing: .13em;
    text-transform: uppercase;
    font-weight: 800;
    color: var(--muted);
    margin-bottom: 18px;
  }}
  h1 {{
    font-size: clamp(48px, 6.2vw, 102px);
    line-height: .92;
    letter-spacing: -0.07em;
    margin: 0 0 28px;
    max-width: 820px;
  }}
  .red {{ color: var(--winter); }}
  .purple {{ color: var(--ghaz); }}
  .dek {{
    font-size: clamp(21px, 2.05vw, 35px);
    line-height: 1.14;
    letter-spacing: -0.035em;
    margin: 0 0 30px;
    color: #25221d;
    max-width: 760px;
  }}
  .stat-grid {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    max-width: 750px;
  }}
  .stat {{
    background: var(--card);
    border: 1px solid var(--hair);
    border-radius: 22px;
    padding: 18px 18px 16px;
    box-shadow: 0 18px 60px rgba(17,24,39,.06);
    backdrop-filter: blur(8px);
  }}
  .stat.ghaz {{ border-color: rgba(124,58,237,.35); }}
  .num {{
    display: block;
    font-size: clamp(28px, 3vw, 50px);
    line-height: 1;
    font-weight: 900;
    letter-spacing: -0.06em;
  }}
  .label {{
    display: block;
    color: var(--muted);
    font-size: clamp(12px, 1vw, 16px);
    line-height: 1.18;
    margin-top: 8px;
    font-weight: 650;
  }}
  .card {{
    background: rgba(255,255,255,.72);
    border: 1px solid var(--hair);
    border-radius: 34px;
    padding: clamp(20px, 2.3vw, 38px);
    box-shadow: 0 24px 90px rgba(17,24,39,.10);
  }}
  .chart-title {{
    display: flex;
    justify-content: space-between;
    gap: 24px;
    align-items: flex-end;
    margin-bottom: 8px;
  }}
  h2 {{
    margin: 0;
    font-size: clamp(24px, 2.1vw, 38px);
    line-height: 1.05;
    letter-spacing: -0.045em;
  }}
  .legend-wrap {{
    display: flex;
    align-items: center;
    gap: 14px;
    color: var(--muted);
    font-weight: 750;
    font-size: 14px;
    white-space: nowrap;
  }}
  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
    vertical-align: -1px;
  }}
  .dot.m {{ background: var(--monsoon); }}
  .dot.w {{ background: var(--winter); }}
  .dot.g {{ background: var(--ghaz); }}
  svg {{ width: 100%; height: auto; display: block; }}
  .grid {{ stroke: rgba(23,23,23,.12); stroke-width: 1; }}
  .tick, .axis-label, .small, .legend {{
    fill: var(--muted);
    font-size: 18px;
    font-weight: 700;
  }}
  .axis-label {{ font-size: 17px; }}
  .city {{
    fill: var(--ink);
    font-size: 24px;
    font-weight: 850;
    letter-spacing: -0.02em;
  }}
  .city.ref {{ fill: var(--ghaz); }}
  .range {{
    stroke: rgba(23,23,23,.22);
    stroke-width: 8;
    stroke-linecap: round;
  }}
  .range.ref {{ stroke: rgba(124,58,237,.30); }}
  .monsoon {{ fill: var(--monsoon); stroke: white; stroke-width: 4; }}
  .winter {{ fill: var(--winter); stroke: white; stroke-width: 4; }}
  .winter.ref {{ fill: var(--ghaz); }}
  .small {{ font-size: 17px; }}
  .strong {{ fill: var(--winter); font-weight: 900; }}
  .winter.ref + .small, .ref {{ }}
  .shock {{
    fill: var(--winter);
    font-size: 25px;
    font-weight: 950;
    letter-spacing: -0.04em;
  }}
  .shock.ref {{ fill: var(--ghaz); }}
  .footer {{
    margin-top: 10px;
    color: var(--muted);
    font-size: clamp(12px, .9vw, 15px);
    line-height: 1.32;
    display: flex;
    justify-content: space-between;
    gap: 18px;
    border-top: 1px solid var(--hair);
    padding-top: 12px;
  }}
  .callout {{
    margin-top: 18px;
    font-size: clamp(16px, 1.35vw, 22px);
    line-height: 1.22;
    font-weight: 780;
    letter-spacing: -0.025em;
  }}
  @media print {{
    body {{ width: 16in; height: 9in; }}
    .slide {{ width: 16in; height: 9in; min-height: auto; }}
  }}
  @media (max-aspect-ratio: 4/3) {{
    .slide {{ grid-template-columns: 1fr; aspect-ratio: auto; }}
    h1 {{ font-size: clamp(46px, 12vw, 88px); }}
  }}
</style>
</head>
<body>
<main class="slide">
  <section class="left">
    <div class="eyebrow">India AQI · {len(data):,} city-days · 2023</div>
    <h1>Delhi is the headline.<br><span class="red">Winter is the story.</span></h1>
    <p class="dek">Add <span class="purple">Ghaziabad</span> as the audience’s reference point: it is {higher_text} on annual AQI, but its winter shock is smaller than the biggest Bihar spikes.</p>
    <div class="stat-grid">
      <div class="stat">
        <span class="num">+{int(season.sort_values("shock", ascending=False).iloc[0]["shock"])}</span>
        <span class="label">largest winter jump: {html.escape(str(season.sort_values("shock", ascending=False).iloc[0]["City"]))}</span>
      </div>
      <div class="stat ghaz">
        <span class="num">{ghaz_avg:.0f}</span>
        <span class="label">Ghaziabad avg AQI 2023, rank #{ghaz_rank}</span>
      </div>
      <div class="stat">
        <span class="num">{gap:.1f}×</span>
        <span class="label">AQI gap: {html.escape(str(worst_row["City"]))} vs {html.escape(str(clean_row["City"]))}</span>
      </div>
    </div>
    <p class="callout">The workshop hook: famous places make the chart relatable; lesser-known spikes make it surprising.</p>
  </section>

  <section class="right">
    <div class="card">
      <div class="chart-title">
        <h2>Winter pollution shock, with Ghaziabad as anchor</h2>
        <div class="legend-wrap">
          <span><i class="dot m"></i>Monsoon</span>
          <span><i class="dot w"></i>Winter</span>
          <span><i class="dot g"></i>Reference</span>
        </div>
      </div>
      {svg}
      <div class="footer">
        <span>Average AQI: monsoon = Jul–Sep 2023; winter = Jan, Feb, Nov, Dec 2023. ★ marks Ghaziabad.</span>
        <span>{comparison}</span>
      </div>
    </div>
  </section>
</main>
</body>
</html>
"""

out = Path("/mnt/data/aqi_winter_shock_slide_ghaziabad.html")
out.write_text(html_doc, encoding="utf-8")

print(f"Created: {out}")
print("\nVerification:")
print(f"Delhi avg AQI 2023: {delhi_avg:.1f}, rank #{delhi_rank}")
print(f"Ghaziabad avg AQI 2023: {ghaz_avg:.1f}, rank #{ghaz_rank}")
print("\nChart data:")
print(pd.DataFrame(rows)[["City", "monsoon_aqi", "winter_aqi", "shock"]].to_string(index=False))
```

STDOUT/STDERR


```
Created: /mnt/data/aqi_winter_shock_slide_ghaziabad.html

Verification:
Delhi avg AQI 2023: 203.6, rank #4
Ghaziabad avg AQI 2023: 181.0, rank #22

Chart data:
     City  monsoon_aqi  winter_aqi  shock
   Purnia           76         296    219
    Delhi          103         319    216
Ghaziabad           98         270    172
Bhagalpur           85         300    215
  Katihar           95         310    215
  Saharsa           96         305    209
    Patna           86         289    202
```

Updated the slide to include Ghaziabad as a reference point:

Download the revised HTML slide

Verification from this dataset: Ghaziabad’s 2023 average AQI is **181.0**, lower than Delhi’s **203.6**. So I did not encode the “higher than Delhi” claim. Instead, the slide now says Ghaziabad is a useful audience anchor: familiar, highly polluted, but not among the biggest winter-shock outliers.

aqi_winter_shock_slide_ghaziabad.html


```
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AQI insight slide — winter shock with Ghaziabad</title>
<style>
  :root {
    --bg: #f7f3ea;
    --ink: #171717;
    --muted: #5e574c;
    --hair: rgba(23,23,23,.14);
    --monsoon: #2a9d8f;
    --winter: #d1493f;
    --ghaz: #7c3aed;
    --card: rgba(255,255,255,.68);
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; width: 100%; min-height: 100%; background: var(--bg); color: var(--ink); }
  body {
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }
  .slide {
    width: 100vw;
    min-height: 100vh;
    aspect-ratio: 16 / 9;
    padding: clamp(28px, 4vw, 72px);
    display: grid;
    grid-template-columns: 1.04fr 1.56fr;
    gap: clamp(24px, 4vw, 64px);
    align-items: center;
    overflow: hidden;
    position: relative;
  }
  .slide::before {
    content: "";
    position: absolute;
    width: 720px;
    height: 720px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(209,73,63,.17), rgba(209,73,63,0) 66%);
    top: -260px;
    right: -180px;
    z-index: 0;
  }
  .slide::after {
    content: "";
    position: absolute;
    width: 620px;
    height: 620px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(42,157,143,.14), rgba(42,157,143,0) 68%);
    bottom: -280px;
    left: -160px;
    z-index: 0;
  }
  .left, .right { position: relative; z-index: 1; }
  .eyebrow {
    display: inline-block;
    font-size: clamp(13px, 1.1vw, 18px);
    letter-spacing: .13em;
    text-transform: uppercase;
    font-weight: 800;
    color: var(--muted);
    margin-bottom: 18px;
  }
  h1 {
    font-size: clamp(48px, 6.2vw, 102px);
    line-height: .92;
    letter-spacing: -0.07em;
    margin: 0 0 28px;
    max-width: 820px;
  }
  .red { color: var(--winter); }
  .purple { color: var(--ghaz); }
  .dek {
    font-size: clamp(21px, 2.05vw, 35px);
    line-height: 1.14;
    letter-spacing: -0.035em;
    margin: 0 0 30px;
    color: #25221d;
    max-width: 760px;
  }
  .stat-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    max-width: 750px;
  }
  .stat {
    background: var(--card);
    border: 1px solid var(--hair);
    border-radius: 22px;
    padding: 18px 18px 16px;
    box-shadow: 0 18px 60px rgba(17,24,39,.06);
    backdrop-filter: blur(8px);
  }
  .stat.ghaz { border-color: rgba(124,58,237,.35); }
  .num {
    display: block;
    font-size: clamp(28px, 3vw, 50px);
    line-height: 1;
    font-weight: 900;
    letter-spacing: -0.06em;
  }
  .label {
    display: block;
    color: var(--muted);
    font-size: clamp(12px, 1vw, 16px);
    line-height: 1.18;
    margin-top: 8px;
    font-weight: 650;
  }
  .card {
    background: rgba(255,255,255,.72);
    border: 1px solid var(--hair);
    border-radius: 34px;
    padding: clamp(20px, 2.3vw, 38px);
    box-shadow: 0 24px 90px rgba(17,24,39,.10);
  }
  .chart-title {
    display: flex;
    justify-content: space-between;
    gap: 24px;
    align-items: flex-end;
    margin-bottom: 8px;
  }
  h2 {
    margin: 0;
    font-size: clamp(24px, 2.1vw, 38px);
    line-height: 1.05;
    letter-spacing: -0.045em;
  }
  .legend-wrap {
    display: flex;
    align-items: center;
    gap: 14px;
    color: var(--muted);
    font-weight: 750;
    font-size: 14px;
    white-space: nowrap;
  }
  .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
    vertical-align: -1px;
  }
  .dot.m { background: var(--monsoon); }
  .dot.w { background: var(--winter); }
  .dot.g { background: var(--ghaz); }
  svg { width: 100%; height: auto; display: block; }
  .grid { stroke: rgba(23,23,23,.12); stroke-width: 1; }
  .tick, .axis-label, .small, .legend {
    fill: var(--muted);
    font-size: 18px;
    font-weight: 700;
  }
  .axis-label { font-size: 17px; }
  .city {
    fill: var(--ink);
    font-size: 24px;
    font-weight: 850;
    letter-spacing: -0.02em;
  }
  .city.ref { fill: var(--ghaz); }
  .range {
    stroke: rgba(23,23,23,.22);
    stroke-width: 8;
    stroke-linecap: round;
  }
  .range.ref { stroke: rgba(124,58,237,.30); }
  .monsoon { fill: var(--monsoon); stroke: white; stroke-width: 4; }
  .winter { fill: var(--winter); stroke: white; stroke-width: 4; }
  .winter.ref { fill: var(--ghaz); }
  .small { font-size: 17px; }
  .strong { fill: var(--winter); font-weight: 900; }
  .winter.ref + .small, .ref { }
  .shock {
    fill: var(--winter);
    font-size: 25px;
    font-weight: 950;
    letter-spacing: -0.04em;
  }
  .shock.ref { fill: var(--ghaz); }
  .footer {
    margin-top: 10px;
    color: var(--muted);
    font-size: clamp(12px, .9vw, 15px);
    line-height: 1.32;
    display: flex;
    justify-content: space-between;
    gap: 18px;
    border-top: 1px solid var(--hair);
    padding-top: 12px;
  }
  .callout {
    margin-top: 18px;
    font-size: clamp(16px, 1.35vw, 22px);
    line-height: 1.22;
    font-weight: 780;
    letter-spacing: -0.025em;
  }
  @media print {
    body { width: 16in; height: 9in; }
    .slide { width: 16in; height: 9in; min-height: auto; }
  }
  @media (max-aspect-ratio: 4/3) {
    .slide { grid-template-columns: 1fr; aspect-ratio: auto; }
    h1 { font-size: clamp(46px, 12vw, 88px); }
  }
</style>
</head>
<body>
<main class="slide">
  <section class="left">
    <div class="eyebrow">India AQI · 299,972 city-days · 2023</div>
    <h1>Delhi is the headline.<br><span class="red">Winter is the story.</span></h1>
    <p class="dek">Add <span class="purple">Ghaziabad</span> as the audience’s reference point: it is slightly lower than Delhi on annual AQI, but its winter shock is smaller than the biggest Bihar spikes.</p>
    <div class="stat-grid">
      <div class="stat">
        <span class="num">+219</span>
        <span class="label">largest winter jump: Purnia</span>
      </div>
      <div class="stat ghaz">
        <span class="num">181</span>
        <span class="label">Ghaziabad avg AQI 2023, rank #22</span>
      </div>
      <div class="stat">
        <span class="num">6.7×</span>
        <span class="label">AQI gap: Byrnihat vs Silchar</span>
      </div>
    </div>
    <p class="callout">The workshop hook: famous places make the chart relatable; lesser-known spikes make it surprising.</p>
  </section>

  <section class="right">
    <div class="card">
      <div class="chart-title">
        <h2>Winter pollution shock, with Ghaziabad as anchor</h2>
        <div class="legend-wrap">
          <span><i class="dot m"></i>Monsoon</span>
          <span><i class="dot w"></i>Winter</span>
          <span><i class="dot g"></i>Reference</span>
        </div>
      </div>

<svg viewBox="0 0 1120 590" role="img" aria-label="Winter versus monsoon AQI shock in Indian cities, 2023, including Ghaziabad as a reference city">
  <text x="250" y="20" class="axis-label">AQI</text>
  <line x1="275.0" y1="30" x2="275.0" y2="542" class="grid"/><text x="275.0" y="572" class="tick" text-anchor="middle">50</text><line x1="400.0" y1="30" x2="400.0" y2="542" class="grid"/><text x="400.0" y="572" class="tick" text-anchor="middle">100</text><line x1="525.0" y1="30" x2="525.0" y2="542" class="grid"/><text x="525.0" y="572" class="tick" text-anchor="middle">150</text><line x1="650.0" y1="30" x2="650.0" y2="542" class="grid"/><text x="650.0" y="572" class="tick" text-anchor="middle">200</text><line x1="775.0" y1="30" x2="775.0" y2="542" class="grid"/><text x="775.0" y="572" class="tick" text-anchor="middle">250</text><line x1="900.0" y1="30" x2="900.0" y2="542" class="grid"/><text x="900.0" y="572" class="tick" text-anchor="middle">300</text><text x="16" y="61" class="city">Purnia</text><line x1="340.0" y1="56" x2="890.0" y2="56" class="range"/><circle cx="340.0" cy="56" r="9" class="monsoon"/><circle cx="890.0" cy="56" r="11" class="winter"/><text x="340.0" y="39" class="small" text-anchor="middle">76</text><text x="890.0" y="39" class="small strong" text-anchor="middle">296</text><text x="1038" y="62" class="shock">+219</text><text x="16" y="129" class="city">Delhi</text><line x1="407.5" y1="124" x2="947.5" y2="124" class="range"/><circle cx="407.5" cy="124" r="9" class="monsoon"/><circle cx="947.5" cy="124" r="11" class="winter"/><text x="407.5" y="107" class="small" text-anchor="middle">103</text><text x="947.5" y="107" class="small strong" text-anchor="middle">319</text><text x="1038" y="130" class="shock">+216</text><text x="16" y="197" class="city ref">Ghaziabad ★</text><line x1="395.0" y1="192" x2="825.0" y2="192" class="range ref"/><circle cx="395.0" cy="192" r="9" class="monsoon"/><circle cx="825.0" cy="192" r="11" class="winter ref"/><text x="395.0" y="175" class="small" text-anchor="middle">98</text><text x="825.0" y="175" class="small strong" text-anchor="middle">270</text><text x="1038" y="198" class="shock ref">+172</text><text x="16" y="265" class="city">Bhagalpur</text><line x1="362.5" y1="260" x2="900.0" y2="260" class="range"/><circle cx="362.5" cy="260" r="9" class="monsoon"/><circle cx="900.0" cy="260" r="11" class="winter"/><text x="362.5" y="243" class="small" text-anchor="middle">85</text><text x="900.0" y="243" class="small strong" text-anchor="middle">300</text><text x="1038" y="266" class="shock">+215</text><text x="16" y="333" class="city">Katihar</text><line x1="387.5" y1="328" x2="925.0" y2="328" class="range"/><circle cx="387.5" cy="328" r="9" class="monsoon"/><circle cx="925.0" cy="328" r="11" class="winter"/><text x="387.5" y="311" class="small" text-anchor="middle">95</text><text x="925.0" y="311" class="small strong" text-anchor="middle">310</text><text x="1038" y="334" class="shock">+215</text><text x="16" y="401" class="city">Saharsa</text><line x1="390.0" y1="396" x2="912.5" y2="396" class="range"/><circle cx="390.0" cy="396" r="9" class="monsoon"/><circle cx="912.5" cy="396" r="11" class="winter"/><text x="390.0" y="379" class="small" text-anchor="middle">96</text><text x="912.5" y="379" class="small strong" text-anchor="middle">305</text><text x="1038" y="402" class="shock">+209</text><text x="16" y="469" class="city">Patna</text><line x1="365.0" y1="464" x2="872.5" y2="464" class="range"/><circle cx="365.0" cy="464" r="9" class="monsoon"/><circle cx="872.5" cy="464" r="11" class="winter"/><text x="365.0" y="447" class="small" text-anchor="middle">86</text><text x="872.5" y="447" class="small strong" text-anchor="middle">289</text><text x="1038" y="470" class="shock">+202</text>
  <text x="387.5" y="572" class="legend" text-anchor="middle">Monsoon</text>
  <text x="912.5" y="572" class="legend winter-label" text-anchor="middle">Winter</text>
</svg>

      <div class="footer">
        <span>Average AQI: monsoon = Jul–Sep 2023; winter = Jan, Feb, Nov, Dec 2023. ★ marks Ghaziabad.</span>
        <span>Ghaziabad: 181 avg AQI, rank #22; Delhi: 204, rank #4</span>
      </div>
    </div>
  </section>
</main>
</body>
</html>
```

---
