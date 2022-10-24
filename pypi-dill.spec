#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-dill
Version  : 0.3.6
Release  : 23
URL      : https://github.com/uqfoundation/dill/releases/download/dill-0.3.6/dill-0.3.6.tar.gz
Source0  : https://github.com/uqfoundation/dill/releases/download/dill-0.3.6/dill-0.3.6.tar.gz
Summary  : serialize all of python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-dill-bin = %{version}-%{release}
Requires: pypi-dill-license = %{version}-%{release}
Requires: pypi-dill-python = %{version}-%{release}
Requires: pypi-dill-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
dill
====
serialize all of python
About Dill
----------
``dill`` extends python's ``pickle`` module for serializing and de-serializing
python objects to the majority of the built-in python types. Serialization
is the process of converting an object to a byte stream, and the inverse
of which is converting a byte stream back to a python object hierarchy.

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
%setup -q -n dill-0.3.6
cd %{_builddir}/dill-0.3.6
pushd ..
cp -a dill-0.3.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666630080
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-dill
cp %{_builddir}/dill-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-dill/89215dbe96039235796b31ac8e2aa8f659d5c12b || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/get_objgraph
/usr/bin/undill

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-dill/89215dbe96039235796b31ac8e2aa8f659d5c12b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
