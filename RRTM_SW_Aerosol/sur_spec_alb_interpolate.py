#!/usr/bin/env python
# coding:utf8
# -*- coding: utf-8 -*-
"""
Convert surface spectral albedo from C3M to RRTM bands 

Created on 2019

@author: Qianqian
"""

from __future__ import print_function,division
import numpy as np
import sys
from scipy import interpolate

def sur_spec_alb_interpolate(yr,iss):  
	# surface albedo (Indirect) wrt 14 c3m bands. 

	alb_c3m = np.load('/home/cd11735/zzbatmos_user/work_Global_DRE/Global_DRE/rrtm_input/CCCM_2007/Rc3m_ave_y{:d}_ss{:d}.npy'.format(yr,iss))
	print('****',yr,iss)	
	band_c3m =np.array([57000.0, 31007.0,
		    31008.0, 27971.0,
		    27972.0, 22856.0,
		    22857.0, 20100.0,
		    20101.0, 16806.0,
		    16807.0, 14499.0,
		    14500.0, 12599.0,
		    12600.0, 11249.0,
		    11250.0, 9599.00,
		    9600.00, 7089.00,
		    7090.00, 5249.00,
		    5250.00, 3999.00,
		    4000.00, 2849.00,
		    2850.00, 2500.00])

	alb_rrtm= np.zeros((1,4,72,90,14))
	iy=0
	
	for ilon in range(72):
	    for ilat in range(90):
	        alb_c3m_band = np.repeat(alb_c3m[iy,iss,ilon,ilat,:],2)
	        f_interp = interpolate.interp1d(band_c3m,alb_c3m_band)         
	        wn_new   = np.linspace(2500,57000,1000)
	        alb_interp = f_interp(wn_new)
	        underone_mask = (alb_interp<1.0)
	        alb_rrtm_band29 = alb_interp[(wn_new<2600) & underone_mask].mean()
	        alb_rrtm_band28 = alb_interp[(wn_new>= 38000) & (wn_new < 50000)  & underone_mask].mean()
	        alb_rrtm_band27 = alb_interp[(wn_new>= 29000) & (wn_new < 38000)  & underone_mask].mean()
	        alb_rrtm_band26 = alb_interp[(wn_new>= 22650) & (wn_new < 29000) & underone_mask].mean()
	        alb_rrtm_band25 = alb_interp[(wn_new>= 16000) & (wn_new < 22650) & underone_mask].mean()
	        alb_rrtm_band24 = alb_interp[(wn_new>= 12850) & (wn_new < 16000) & underone_mask].mean()
	        alb_rrtm_band23 = alb_interp[(wn_new>= 8050) & (wn_new < 12850) & underone_mask].mean()
	        alb_rrtm_band22 = alb_interp[(wn_new>= 7700) & (wn_new < 8050) & underone_mask].mean()
	        alb_rrtm_band21 = alb_interp[(wn_new>= 6150) & (wn_new < 7700) & underone_mask].mean()
	        alb_rrtm_band20 = alb_interp[(wn_new>= 5150) & (wn_new < 6150) & underone_mask].mean()
	        alb_rrtm_band19 = alb_interp[(wn_new>= 4650) & (wn_new < 5150) & underone_mask].mean()
	        alb_rrtm_band18 = alb_interp[(wn_new>= 4000) & (wn_new < 4650) & underone_mask].mean()
	        alb_rrtm_band17 = alb_interp[(wn_new>= 3250) & (wn_new < 4000) & underone_mask].mean()
	        alb_rrtm_band16 = alb_interp[(wn_new>= 2600) & (wn_new < 3250) & underone_mask].mean()
	        alb_rrtm[iy,iss,ilon,ilat,:]= np.array([alb_rrtm_band16,alb_rrtm_band17,alb_rrtm_band18,alb_rrtm_band19,alb_rrtm_band20,alb_rrtm_band21,\
					alb_rrtm_band22,alb_rrtm_band23,alb_rrtm_band24,alb_rrtm_band25,alb_rrtm_band26,alb_rrtm_band27,\
					alb_rrtm_band28,alb_rrtm_band29])

	np.save('surf_spec_albedo_c3m_rrtm_{:d}_{:d}'.format(yr,iss),alb_rrtm)

