#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# another-test.py
# Created at 2021-08-30 by Song Xue <songxue AT outlook-com>
# Git CLI uploading test
# Last Change: Tue 08/31/2021, 11:23 am.

import existingUsers
import newUsers
import streamlit as st
import pandas as pd

PAGES = {
    "Exisiting Users": existingUsers,
    "New Users": newUsers
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()