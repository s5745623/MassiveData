#!/usr/bin/env python3
#
# ingest the TXT file generated by "mtr" and read it as records

import sys
import os,datetime,re
from datetime import datetime


#2015-12-10T08:40:10Z fnard:-1 fnok:-1 cark:-1 gnuck:-1
QUAZYILX_RE = r"^((\S+ \S+) fnard:(-?\d+) fnok:(-?\d+) cark:(-?\d+) gnuck:(-?\d+))"
quazyilx_re = re.compile(QUAZYILX_RE)

class Quazyilx():
    __slots__ = ['datetime','fnard','fnok','cark','gnuck']
    def __init__(self,line):
        # Parse line with the regular expression
        m = quazyilx_re.search(line)
        if not m:
            self.datetime = None
            self.fnard    = None
            self.fnok     = None
            self.cark     = None
            self.gnuck    = None
            return
        # Put your code here:
        self.datetime = m.group(2)
        self.fnard = m.group(3)
        self.fnok = m.group(4)
        self.cark = m.group(5)
        self.gnuck = m.group(6)
        self.datetime = datetime.strptime(self.datetime, '%Y-%m-%d %H:%M:%S').isoformat()
    def __str__(self):
        return "{} fnard:{} fnok:{} cark:{} gnuck:{}".format(self.datetime,self.fnard,self.fnok,self.cark,self.gnuck)
    def __repr__(self):
        return "{} fnard:{} fnok:{} cark:{} gnuck:{}".format(self.datetime,self.fnard,self.fnok,self.cark,self.gnuck)
    def Row(self):
        #return "{} {} {} {} {}".format(self.datetime, self.fnard, self.fnok, self.cark, self.gnuck)
        from pyspark.sql import Row
        return Row(datetime = self.datetime, fnard = self.fnard, fnok = self.fnok,cark = self.cark,gnuck = self.gnuck)

        
    
