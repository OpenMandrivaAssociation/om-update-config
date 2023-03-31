Summary: Tool for configuring automatic updates
Name: om-update-config
Version: 0.2
Release: 2
Url: http://openmandriva.org/
Source0: https://github.com/OpenMandrivaSoftware/om-update-config/archive/%{version}/%{name}-%{version}.tar.gz
License: GPLv3
BuildRequires: cmake ninja
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
# Only for the cmake_kde5 rpm macro
BuildRequires: cmake(ECM)
Requires: dnf-automatic

%description
Tool for configuring automatic updates

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/om-update-config
%{_bindir}/om-update-config-ui
%{_datadir}/applications/om-update-config.desktop
%{_datadir}/icons/*/*/*/*
