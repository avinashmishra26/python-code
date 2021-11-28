#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:25:38 2021

@author: avinashkumarmishra
"""

import torch
import numpy as np


if torch.cuda.is_available():
    device = torch.device('cuda')
    
    x = torch.ones(5, device=device)
    
    y = torch.ones(5)
    y = y.to(device)
    
    z = x + y
    z = z.to('cpu')