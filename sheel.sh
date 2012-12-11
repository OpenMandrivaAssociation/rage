#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

svn co http://svn.enlightenment.org/svn/e/trunk/rage rage; \
cd rage; \
SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
VERSION=$(cat configure.ac | grep "rage" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
PKG_VERSION=$VERSION.$SVNREV; \
cd ..; \
tar -Jcf rage-$PKG_VERSION.tar.xz rage/ --exclude .svn --exclude .*ignore

