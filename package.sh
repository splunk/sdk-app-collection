#!/bin/sh

SRCDIR=src
BUILDDIR=build

if [ ! -e $BUILDDIR ]; then mkdir $BUILDDIR; fi
rm -f build/*.tar
cd $SRCDIR
for appdir in `ls -1 .`; do
    tar -czf ../$BUILDDIR/$appdir.tgz $appdir
done
