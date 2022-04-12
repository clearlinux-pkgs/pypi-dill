#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-dill
Version  : 0.3.4
Release  : 15
URL      : https://github.com/uqfoundation/dill/releases/download/dill-0.3.4/dill-0.3.4.tar.gz
Source0  : https://github.com/uqfoundation/dill/releases/download/dill-0.3.4/dill-0.3.4.tar.gz
Summary  : serialize all of python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-dill-bin = %{version}-%{release}
Requires: pypi-dill-license = %{version}-%{release}
Requires: pypi-dill-python = %{version}-%{release}
Requires: pypi-dill-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
-----------------------------
dill: serialize all of python
-----------------------------

%package bin
Summary: bin components for the pypi-dill package.
Group: Binaries
Requires: pypi-dill-license = %{version}-%{release}

%description bin
bin components for the pypi-dill package.


%package license
Summary: license components for the pypi-dill package.
Group: Default

%description license
license components for the pypi-dill package.


%package python
Summary: python components for the pypi-dill package.
Group: Default
Requires: pypi-dill-python3 = %{version}-%{release}

%description python
python components for the pypi-dill package.


%package python3
Summary: python3 components for the pypi-dill package.
Group: Default
Requires: python3-core
Provides: pypi(dill)

%description python3
python3 components for the pypi-dill package.


%prep
%setup -q -n dill-0.3.4
cd %{_builddir}/dill-0.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649737582
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-dill
cp %{_builddir}/dill-0.3.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-dill/5a4d5da357f0df5d1be0dd74d0e4cc9830053a7c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/get_objgraph
/usr/bin/undill

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-dill/5a4d5da357f0df5d1be0dd74d0e4cc9830053a7c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
