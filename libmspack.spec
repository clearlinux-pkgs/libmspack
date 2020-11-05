#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmspack
Version  : 0.10.1alpha
Release  : 11
URL      : https://www.cabextract.org.uk/libmspack/libmspack-0.10.1alpha.tar.gz
Source0  : https://www.cabextract.org.uk/libmspack/libmspack-0.10.1alpha.tar.gz
Summary  : Compressors and decompressors for Microsoft formats
Group    : Development/Tools
License  : LGPL-2.1
Requires: libmspack-lib = %{version}-%{release}
Requires: libmspack-license = %{version}-%{release}

%description
libmspack 0.10.1alpha
The purpose of libmspack is to provide compressors and decompressors,
archivers and dearchivers for Microsoft compression formats: CAB, CHM, WIM,
LIT, HLP, KWAJ and SZDD. It is also designed to be easily embeddable,
stable, robust and resource-efficient.

%package dev
Summary: dev components for the libmspack package.
Group: Development
Requires: libmspack-lib = %{version}-%{release}
Provides: libmspack-devel = %{version}-%{release}
Requires: libmspack = %{version}-%{release}

%description dev
dev components for the libmspack package.


%package lib
Summary: lib components for the libmspack package.
Group: Libraries
Requires: libmspack-license = %{version}-%{release}

%description lib
lib components for the libmspack package.


%package license
Summary: license components for the libmspack package.
Group: Default

%description license
license components for the libmspack package.


%prep
%setup -q -n libmspack-0.10.1alpha
cd %{_builddir}/libmspack-0.10.1alpha

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604610977
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604610977
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmspack
cp %{_builddir}/libmspack-0.10.1alpha/COPYING.LIB %{buildroot}/usr/share/package-licenses/libmspack/e60c2e780886f95df9c9ee36992b8edabec00bcc
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/mspack.h
/usr/lib64/libmspack.so
/usr/lib64/pkgconfig/libmspack.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmspack.so.0
/usr/lib64/libmspack.so.0.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmspack/e60c2e780886f95df9c9ee36992b8edabec00bcc
