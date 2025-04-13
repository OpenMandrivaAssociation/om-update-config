Summary: Tool for configuring automatic updates
Name: om-update-config
Version: 1.0
Release: 1
Url: https://openmandriva.org/
Source0: https://github.com/OpenMandrivaSoftware/om-update-config/archive/%{version}/%{name}-%{version}.tar.gz
Group: System
License: GPLv3
BuildRequires: cmake ninja
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildSystem: cmake
BuildRequires: cmake(ECM)
Requires: system-update = %{EVRD}

%description
Tool for configuring automatic updates

%package -n system-update
Summary: Service for nightly update installation
Group: System
Recommends: logrotate

%description -n system-update
Service for nightly update installation

%files
%{_bindir}/om-update-config
%{_bindir}/om-update-config-ui
%{_datadir}/applications/om-update-config.desktop
%{_datadir}/icons/*/*/*/*

%files -n system-update
%{_bindir}/update-system
%{_unitdir}/system-update.service
%{_unitdir}/system-update.timer
%{_sysconfdir}/logrotate.d/*
%ghost %{_localstatedir}/log/update.log
