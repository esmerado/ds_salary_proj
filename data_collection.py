#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:06:55 2023

@author: javieresmeradovela
"""

import glassdoor_scraper as gs
import pandas as pd

path = "/Users/javieresmeradovela/Documents/dev/conda/ds_salary/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index=False)
