#!/usr/bin/env python
# coding:utf8
# -*- coding: utf-8 -*-
"""
Module: Read RRTM OUTPUT data 

converd to Python by Jianyu Zheng on 2019
"""

import numpy  as np
import pandas as pd
import fortranformat as ff
import sys

def read_OUTPUT_RRTM(fname_sw_cl, fname_sw_ae,fname_lw_cl, fname_lw_ae, IMMAX):
	#file = open(fname_sw_cl,'w+')	
	#print('****')
	#print(pd.read_csv(fname_sw_cl,skiprows=5,header=None,\
        #           nrows=IMMAX,usecols=[1,2,3,4,5,6],delim_whitespace=True))
	data = np.array(pd.read_csv(fname_sw_cl,skiprows=5,header=None,\
		   nrows=IMMAX,usecols=[1,2,3,4,5,6],delim_whitespace=True)).astype(np.float)
	#print('*****')
	#print(data)
	#sys.exit()
	#form = ff.FortranRecordWriter('(F10.4,F10.4,F10.4,F10.4,F10.4,F10.4,F10.4)')
	#for i in range(IMMAX):
	#	fname_sw_cl.writelines(form.write([*data[i]]) + '\n')
	# Variables we need for the plot
	TOA_sw_cl_upflux_bb = data[0,1]
	TOA_sw_cl_dwflux_bb = data[0,4]
	SUF_sw_cl_upflux_bb = data[IMMAX-1,1]
	SUF_sw_cl_dwflux_bb = data[IMMAX-1,4]

	#file = open(fname_sw_ae,'w+')	
	data = np.array(pd.read_csv(fname_sw_ae,header=None,skiprows=5,\
		   nrows=IMMAX,usecols=[1,2,3,4,5,6],delim_whitespace=True)).astype(np.float)
	#form = ff.FortranRecordWriter('(F10.4,F10.4,F10.4,F10.4,F10.4,F10.4,F10.4)')
	#for i in range(IMMAX):
	#	fname_sw_ae.writelines(form.write([*data[i]]) + '\n')
	# Variables we need for the plot
	TOA_sw_ae_upflux_bb = data[0,1]
	TOA_sw_ae_dwflux_bb = data[0,4]
	SUF_sw_ae_upflux_bb = data[IMMAX-1,1]
	SUF_sw_ae_dwflux_bb = data[IMMAX-1,4]
	#file = open(fname_lw_cl,'w+')	
	data = np.array(pd.read_csv(fname_lw_cl,header=None,skiprows=3,\
		   nrows=IMMAX,usecols=[1,2,3,4],delim_whitespace=True)).astype(np.float)
	#form = ff.FortranRecordWriter('(F10.4,F10.4,F10.4,F10.4,F10.4)')
	#for i in range(IMMAX):
	#	fname_lw_cl.writelines(form.write([*data[i]]) + '\n')
	# Variables we need for the plot
	TOA_lw_cl_upflux_bb = data[0,1]
	TOA_lw_cl_dwflux_bb = data[0,2]
	SUF_lw_cl_upflux_bb = data[IMMAX-1,1]
	SUF_lw_cl_dwflux_bb = data[IMMAX-1,2]

	#file = open(fname_lw_ae,'w+')	
	data = np.array(pd.read_csv(fname_lw_ae,header=None,skiprows=3,usecols=[1,2,3,4],\
		   nrows=IMMAX,delim_whitespace=True)).astype(np.float)
	#form = ff.FortranRecordWriter('(F10.4,F10.4,F10.4,F10.4,F10.4)')
	#for i in range(IMMAX):
	#	fname_lw_ae.writelines(form.write([*data[i]]) + '\n')
	# Variables we need for the plot
	TOA_lw_cd_upflux_bb = data[0,1]
	TOA_lw_cd_dwflux_bb = data[0,2]
	SUF_lw_cd_upflux_bb = data[IMMAX-1,1]
	SUF_lw_cd_dwflux_bb = data[IMMAX-1,2]
	return TOA_sw_cl_upflux_bb, TOA_sw_cl_dwflux_bb, TOA_sw_ae_upflux_bb, TOA_sw_ae_dwflux_bb,\
		   SUF_sw_cl_upflux_bb, SUF_sw_cl_dwflux_bb, SUF_sw_ae_upflux_bb, SUF_sw_ae_dwflux_bb,\
                   TOA_lw_cl_upflux_bb, TOA_lw_cl_dwflux_bb, TOA_lw_cd_upflux_bb, TOA_lw_cd_dwflux_bb,\
                   SUF_lw_cl_upflux_bb, SUF_lw_cl_dwflux_bb, SUF_lw_cd_upflux_bb, SUF_lw_cd_dwflux_bb


