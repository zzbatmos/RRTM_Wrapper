#!/usr/bin/env python3
# coding:utf8
# -*- coding: utf-8 -*-
"""
Module: write RRTM shortwave cloud inputfile (INPUT_CLD_RRTM_sw)

Created on 2019

@author: Jianyu Zheng
"""

import os 
import numpy as np
import fortranformat as ff

def write_IN_CLD_RRTM_sw(fname, NLAY, LAY, CWP, EFFSIZELIQ):
		
	INFLAG  = 2 #  = 2 calculation of separate ice and liquid cloud optical depths, with
	            #           parameterizations determined by values of ICEFLAG and LIQFLAG.
	ICEFLAG = 3 # = 3 the optical properties are computed by a method based on the parameterization
		    #		of ice clouds due to Q. Fu, J. Clim., 9, 2058 (1996).
	LIQFLAG = 1 #  LIQFLAG = 1 the optical depths (non-gray) due to water clouds are computed by a method
	            #            based on the parameterization of water clouds due to Y.X. Hu and K. Stamnes,
	            #            J. Clim., 6, 728-742 (1993).
	
	#LAY     = 2 #layer number of cloudy layer. ****
	CLDFRAC = 1.0
	#CWP  = 100.0  #cloud water path  ******
	FRACICE = 0.0
	EFFSIZEICE = 0.0
	#EFFSIZELIQ =14.0  #liquid droplet effective radius, Reff (microns). Valid size are 2.5-60.0 microns ****
	TESTCHAR = 'C'
	
	# write the INPUT_CLD_RRTM file
	file = open(fname,'w+')
	
	form = ff.FortranRecordWriter('(I5, I5, I5)')
	file.writelines(form.write([INFLAG, ICEFLAG, LIQFLAG]))

	for i in range(NLAY):
		print('***',LAY[i], CWP[LAY[i]],EFFSIZELIQ[LAY[i]])
		form = ff.FortranRecordWriter('(A1, I4, 5F10.5)')
		file.writelines('\n'+form.write([TESTCHAR, LAY[i], CLDFRAC, CWP[LAY[i]], FRACICE, EFFSIZEICE, EFFSIZELIQ[LAY[i]]]))

	form = ff.FortranRecordWriter('(A1)')
	file.writelines('%')
		
	file.close()


