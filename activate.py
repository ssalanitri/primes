#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess


def main():
   
   completed  = subprocess.run(['cd', 'env/Scripts']) 
   print('returncode:', completed.returncode)
   
   completed = subprocess.run(['./activate'])
   print('returncode:', completed.returncode)
    

if __name__ == '__main__':
    main()
