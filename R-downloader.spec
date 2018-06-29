#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-downloader
Version  : 0.4
Release  : 1
URL      : https://cran.r-project.org/src/contrib/downloader_0.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/downloader_0.4.tar.gz
Summary  : Download Files over HTTP and HTTPS
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
making it possible to download files over HTTPS on Windows, Mac OS X, and
    other Unix-like platforms. The 'RCurl' package provides this functionality
    (and much more) but can be difficult to install because it must be compiled
    with external dependencies. This package has no external dependencies, so
    it is much easier to install.

%prep
%setup -q -c -n downloader

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530312039

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530312039
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library downloader
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library downloader
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library downloader
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library downloader|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/downloader/DESCRIPTION
/usr/lib64/R/library/downloader/INDEX
/usr/lib64/R/library/downloader/Meta/Rd.rds
/usr/lib64/R/library/downloader/Meta/features.rds
/usr/lib64/R/library/downloader/Meta/hsearch.rds
/usr/lib64/R/library/downloader/Meta/links.rds
/usr/lib64/R/library/downloader/Meta/nsInfo.rds
/usr/lib64/R/library/downloader/Meta/package.rds
/usr/lib64/R/library/downloader/NAMESPACE
/usr/lib64/R/library/downloader/NEWS
/usr/lib64/R/library/downloader/R/downloader
/usr/lib64/R/library/downloader/R/downloader.rdb
/usr/lib64/R/library/downloader/R/downloader.rdx
/usr/lib64/R/library/downloader/help/AnIndex
/usr/lib64/R/library/downloader/help/aliases.rds
/usr/lib64/R/library/downloader/help/downloader.rdb
/usr/lib64/R/library/downloader/help/downloader.rdx
/usr/lib64/R/library/downloader/help/paths.rds
/usr/lib64/R/library/downloader/html/00Index.html
/usr/lib64/R/library/downloader/html/R.css
/usr/lib64/R/library/downloader/tests/test-download.r
/usr/lib64/R/library/downloader/tests/test-sha.r
