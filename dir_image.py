#!/usr/bin/python

import os
from optparse import OptionParser

def mparse():
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="source", help="source dir")
    parser.add_option("-d", "--dest", dest="dest", help="destination dir")

    (options, args) = parser.parse_args()

    return (options, args)


def main():
    (options, args) = mparse()
    src  = os.path.realpath (options.source)
    dest = os.path.realpath (options.dest)

    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.mkdir(dest)
        for (spath, sdirs, sfiles) in os.walk(src):
            #print os.path.relpath(spath, src), sdirs, sfiles
            relpath     = os.path.relpath(spath, src)
            destpath = dest + os.sep + relpath

            if not os.path.isdir(destpath):
                os.mkdir (destpath)

            for sfile in sfiles:
                sfilepath = spath + os.sep + sfile
                dfilepath = destpath + os.sep + sfile

                if os.path.exists(dfilepath):
                    os.unlink (dfilepath)

                print "creating symlink", sfilepath, dfilepath
                os.symlink (sfilepath, dfilepath)



if __name__ == '__main__':
    print "calling main..."
    main()
