#!/usr/bin/env python
# coding:utf8
# -*- coding: utf-8 -*-
"""
Module: write RRTM shortwave aerosol inputfile (INPUT_AER_RRTM_sw)

Created on 2019

@author: Jianyu Zheng
"""

import os 
import numpy as np
import fortranformat as ff

def write_IN_AER_RRTM_sw(fname,NLAY, LAY, AOD, SSA, PHASE):
		
	NBAND = 14
	NAER = 1 # number of different aerosol types
	#NLAY = 1 # number of layers containing the aerosol with the specified properties
	IAOD = 1 # = 1     aerosol optical depths directly input for each layer and band
	ISSA = 1 # = 1     spectrally dependent SSA (for band IB, equal to SSA(IB))   
	IPHA = 1 # = 1 uses Henyey-Greenstein phase function
	AERPAR = [0.0, 0.0, 0.0] # (only used if IAOD = 0) array of parameters for obtaining aerosol optical depth
	
	#AOD = make_array(NBAND,NLAY,/float)
	#SSA = make_array(NBAND,/float)
	#PHASE = make_array(NBAND,/float)
	#LAY = make_array(NLAY,/INTEGER)
	
	#LAY[0] = 4
	#AOD[*,*]=0.01
	#SSA[*]=0.80
	#PHASE[*]=0.75
	
	# write the INPUT_CLD_RRTM file
	#print('***INPUT w/ aero***')
	#print(NLAY, IAOD, ISSA, IPHA, AERPAR)
	#print('***INPUT w/ aero***')
	file = open(fname,'w+')
	
	form = ff.FortranRecordWriter('(I5)')
	file.writelines(form.write([NAER]))
	
	form = ff.FortranRecordWriter('(I5, I5, I5, I5,3F8.2)')
	file.writelines('\n'+form.write([NLAY, IAOD, ISSA, IPHA,*AERPAR]))
	
	for i in range(NLAY):
		form = ff.FortranRecordWriter('(I5, 14F7.4)')
		file.writelines('\n'+form.write([LAY[i],*AOD[:,i]]))
	
	form = ff.FortranRecordWriter('(14F5.2)')
	file.writelines('\n'+form.write([*SSA]))
	file.writelines('\n'+form.write([*PHASE]))
	
	file.close()


