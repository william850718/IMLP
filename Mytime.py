# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time

t1 = time.time()

def GetTime(fmt):
    lot = time.localtime(t1)
    st = time.strftime(fmt,lot)    #格式化輸出時間
    return st


if __name__ == "__main__":
    print(GetTime("%Y-%m-%d %H:%M:%S"))
    print(GetTime("%Y-%m-%d %H:%M:%S %a"))
    print(GetTime("%Y-%b-%d %H:%M:%S %a"))
    print(GetTime("%Y-%B-%d %H:%M:%S %A"))