# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:32:13 2021

@author: Administrator
"""

import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd

data = pd.read_csv('./AlDep',sep = '\t')

md = smf.mixedlm("AlScore ~ ADR",data,groups = data["Hospital"])
mdf = md.fit()
print(mdf.summary())

md = smf.mixedlm("AlScore ~ Time",data,groups = data["Phys"])
mdf = md.fit()
print(mdf.summary())