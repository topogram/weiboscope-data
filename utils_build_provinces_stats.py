#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv,os,json
from lib.users import UserAPI

api=UserAPI()

data_path=os.path.join(os.getcwd(),"data")

nb_of_users_by_provinces_file=data_path+"nb_of_users_by_provinces.json"
population_file=data_path+"ChineseProvincesPopulation2010Census.csv"
gdp_file=data_path+"ChineseProvincesGDP_PPP.csv"

provinces=["Gansu","Qinghai","Guangxi","Guizhou","Chongqing","Beijing","Fujian","Anhui","Guangdong","Xizang","Xinjiang","Hainan","Ningxia","Shaanxi","Shanxi","Hubei","Hunan","Sichuan","Yunnan","Hebei","Henan","Liaoning","Shandong","Tianjin","Jiangxi","Jiangsu","Shanghai","Zhejiang","Jilin","Inner Mongol","Heilongjiang","Taiwan","Xianggang","Aomen"]


# corpus stats
nb_of_users_by_provinces={}
total=0

# count
for i,province in enumerate(api.provinces):
    # if i==1: break
    c=api.db.find({"province": province}).count()
    nb_of_users_by_provinces[province]=c
    print "%d users in %s"%(c,api.provinces[province])
    total+=c

print "%d users in %d provinces"%(total,i+1)

# percent
percent_of_users_by_provinces={}
total_percent=0
for province in api.provinces:
    p=(float(nb_of_users_by_provinces[province])/total)*100
    percent_of_users_by_provinces[province]=p
    total_percent+=p
print "%d total percent"%total_percent

# parse data
pop={}
with open(population_file, 'rb') as csvpopulation:

    poplist=csv.reader(csvpopulation, delimiter=";")
    poplist.next() # skip headers

    for p in poplist : pop[p[0]]=p[1]

gdp={}
with open(gdp_file, 'rb') as csvgdp:

    gdplist=csv.reader(csvgdp, delimiter=";")
    gdplist.next() # skip headers

    for p in gdplist : gdp[p[0]]=p[1] 


data=[]
for province in api.provinces:
 
    # if province not in pop : raise KeyError(province) 
    # if province not in gdp : raise KeyError(province) 

    province_name=api.provinces[province]
    if province_name in provinces:  # avoid useless

        clean_name=province_name 

        if province=="Xianggang"  : clean_name="Hong Kong"
        elif province=="Aomen" : clean_name="Macau"
        elif province=="Inner Mongol" : clean_name="Inner Mongolia"
        

        data.append({
            "weibo_id":province, 
            "name": province_name,
            "clean_name": clean_name, 
            "percent":percent_of_users_by_provinces[province],
            "count":nb_of_users_by_provinces[province],
            "gdp":gdp[province_name],
            "population":pop[province_name],
            })

# write json data
with open(nb_of_users_by_provinces_file, 'w') as outfile:
    json.dump({"nb_of_users_by_provinces":data}, outfile)
    print "json data have been saved to %s"%(nb_of_users_by_provinces_file)