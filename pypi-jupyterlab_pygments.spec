#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyterlab_pygments
Version  : 0.2.2
Release  : 28
URL      : https://files.pythonhosted.org/packages/69/8e/8ae01f052013ee578b297499d16fcfafb892927d8e41c1a0054d2f99a569/jupyterlab_pygments-0.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/69/8e/8ae01f052013ee578b297499d16fcfafb892927d8e41c1a0054d2f99a569/jupyterlab_pygments-0.2.2.tar.gz
Summary  : Pygments theme using JupyterLab CSS variables
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyterlab_pygments-data = %{version}-%{release}
Requires: pypi-jupyterlab_pygments-license = %{version}-%{release}
Requires: pypi-jupyterlab_pygments-python = %{version}-%{release}
Requires: pypi-jupyterlab_pygments-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jupyter_packaging)
BuildRequires : pypi(jupyterlab)

%description
# JupyterLab Pygments Theme
This package contains a syntax coloring theme for [pygments](http://pygments.org/) making use of
the JupyterLab CSS variables.

%package data
Summary: data components for the pypi-jupyterlab_pygments package.
Group: Data

%description data
data components for the pypi-jupyterlab_pygments package.


%package license
Summary: license components for the pypi-jupyterlab_pygments package.
Group: Default

%description license
license components for the pypi-jupyterlab_pygments package.


%package python
Summary: python components for the pypi-jupyterlab_pygments package.
Group: Default
Requires: pypi-jupyterlab_pygments-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyterlab_pygments package.


%package python3
Summary: python3 components for the pypi-jupyterlab_pygments package.
Group: Default
Requires: python3-core
Provides: pypi(jupyterlab_pygments)

%description python3
python3 components for the pypi-jupyterlab_pygments package.


%prep
%setup -q -n jupyterlab_pygments-0.2.2
cd %{_builddir}/jupyterlab_pygments-0.2.2
pushd ..
cp -a jupyterlab_pygments-0.2.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666712927
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_pygments
cp %{_builddir}/jupyterlab_pygments-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_pygments/5dc7e0ef3878c3d4a92a7233208e6f91553de266 || :
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

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/labextensions/jupyterlab_pygments/install.json
/usr/share/jupyter/labextensions/jupyterlab_pygments/package.json
/usr/share/jupyter/labextensions/jupyterlab_pygments/static/568.1e2faa2ba0bbe59c4780.js
/usr/share/jupyter/labextensions/jupyterlab_pygments/static/747.8eb3ddccc7ec4987bff9.js
/usr/share/jupyter/labextensions/jupyterlab_pygments/static/remoteEntry.aa1060b2d1221f8e5688.js
/usr/share/jupyter/labextensions/jupyterlab_pygments/static/style.js
/usr/share/jupyter/labextensions/jupyterlab_pygments/static/third-party-licenses.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyterlab_pygments/5dc7e0ef3878c3d4a92a7233208e6f91553de266

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
