# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 17:55:34 2022

@author: Yue Sun
"""
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
