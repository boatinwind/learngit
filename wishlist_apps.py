# author: fengzhou
#!/usr/bin/python

# -*- coding: UTF-8 -*-
#__author__="fengzhou"

#This is to test the branch function

import os,re,urllib2
from datetime import date
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

products={\
        "OmniFocus": "https://itunes.apple.com/cn/app/omnifocus-2/id867299399?mt=12",\
        "mindnode 2":"https://itunes.apple.com/cn/app/mindnode-2-delightful-mind/id992076693?mt=12",\
        "day one 2":"https://itunes.apple.com/cn/app/day-one/id1055511498?mt=12",\
}

# This is the reg pattern of the price
base_Pri_ptn=re.compile('\"basePrice\":(\d*),')
vol_Pri_ptn=re.compile('\"volumePrice\":(\d*),')

# get the price of each products
def get_price(the_url):
    req=urllib2.urlopen(the_url)
    html_src=req.read()
    s1=base_Pri_ptn.search(html_src)
    s2=vol_Pri_ptn.search(html_src)
    
    if s1:
        Base_Price=s1.group(1)
    else:
        Base_Price=0
    if s2:
        Volume_Price=s2.group(1)
    else:
        Volume_Price=0

    return(Base_Price, Volume_Price)


if __name__=='__main__':

    today_str=date.today().strftime("%Y/%m/%d,%A")

    for key in products.keys():
        the_url=products[key]

        (base_price,vol_price)=get_price(the_url)

        output_msg= "%-10s,%-20s,%-10s" % (today_str, key,base_price) 
        print output_msg
