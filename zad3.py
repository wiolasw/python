#!/usr/bin/env python3
import os, os.path
sciezka="/dev"

x=len([f for f in os.listdir(sciezka) if os.path.isfile(os.path.join(sciezka, f))])
print (x)
