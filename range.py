#!/usr/bin/python
from netaddr import *

#input for iplist and output
infile = raw_input('iplistpath: ')
outfile = raw_input('outputfile: ')

#open file objects
inf = open(infile, 'r').read().splitlines()
outf = open(outfile, 'w')

#converts the range as format 0.0.0.0 - 0.0.0.0 to 0.0.0.0/0 (cidr) and writes it into outf file object
for ip in inf:
    spip = ip.split(',')
    ip1 = spip[0]
    ip2 = spip[1]
    a = str(iprange_to_cidrs(ip1,ip2)[0]) + '\n'
    outf.write(a)
 





