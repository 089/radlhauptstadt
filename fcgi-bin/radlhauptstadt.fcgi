#!/usr/local/bin/python3
import sys, os
sys.path.insert(0, os.getenv("HOME") + "/projekt/radlhauptstadt/REST")
  
from flipflop import WSGIServer
from REST import app

if __name__ == '__main__':
    WSGIServer(app).run()
