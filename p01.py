# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:08:52 2023

@author: william
"""

import Mytime

# 要用到的模組建議放在與要import的主程式同個資料夾下
t1 = 777
print(Mytime.GetTime("%Y-%m-%d %H:%M:%S"))
print(Mytime.t1)
print(t1)
print(Mytime.time.time())   #import 自己的模組也能運用自己的模組(Mytime)中的模組(time)
