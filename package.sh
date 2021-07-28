#!/bin/sh

SRCDIR=src
BUILDDIR=build
COMPDIR=sdkappcollection

if [ ! -e $BUILDDIR ]; then mkdir $BUILDDIR; fi
rm -f build/*.tar

cd $SRCDIR
for appdir in `ls -1 .`; do
    tar -cf ../$BUILDDIR/$appdir.tar $appdir # create .tar for all apps
done
for appdir in `ls -1 .`; do
    tar -czf ../$BUILDDIR/$appdir.tgz $appdir # create .tgz for all apps
done

cd ..                                        # navigate to the root level of sdk-app-collection
cd ..                                        # navigate to one level up from sdk-app-collection

if [ -d $COMPDIR ]; then rm -Rf $COMPDIR; fi # remove if sdkappcollection already exists
mkdir $COMPDIR                               # create an sdkappcollection directory
cp -a ./sdk-app-collection/* ./$COMPDIR/     # copy the content from sdk-app-collection to sdkappcollection
tar -czf $COMPDIR.tgz $COMPDIR               # create a sdkappcollection.tgz from sdkappcollection
rm -Rf $COMPDIR                              # remove sdkappcollection

