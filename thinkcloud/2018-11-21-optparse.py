#! /usr/bin/env python

from optparse import OptionParser


MSG_USAGE = "myprog[ -f <filename>][-s <xyz>] arg1[,arg2..]"

optParser = OptionParser(MSG_USAGE)


optParser.add_option("-f","--file",action = "store",type="string",dest = "fileName")

optParser.add_option("-v","--vison", action="store_false", dest="verbose",default='gggggg',

                     help="make lots of noise [default]")


fakeArgs = ['-f','file.txt','-v','good luck to you', 'arg2', 'arge']

options, args = optParser.parse_args(fakeArgs)


print options.fileName

print options.verbose

print options

print args

print optParser.print_help()