Summary: NethServer smartd service
Name: nethserver-smartd
Version: 1.1.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
URL: %{url_prefix}/%{name}

BuildArch: noarch
BuildRequires: nethserver-devtools
Requires: nethserver-base
Requires: smartmontools

%description
NethServer smartd management system.

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist 
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.1.0-1
- First NS7 release

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.1-1.ns6
- Lib: synchronize service status prop and chkconfig - Feature #2067 [NethServer]
- Full automatic package install/upgrade/uninstall support - Feature #1870 [NethServer]

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1.ns6
- First release. #1870
