%define specrelease 1
%if 0%{?openeuler}
%define specrelease 1%{?dist}
%endif

Name:           uos-manual-content
Version:        5.0.0.1
Release:        %{specrelease}
Summary:        protocol files copy
License:        GPLv3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: cmake

%description
%{summary}.

%prep
%autosetup

%build

# cmake_minimum_required version is too high
sed -i "s|^cmake_minimum_required.*|cmake_minimum_required(VERSION 3.0)|" $(find . -name "CMakeLists.txt")
mkdir build && pushd build
%cmake ../
%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

%files
%{_datadir}/src/assets/dde

