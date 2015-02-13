Summary: NethServer smartd service
Name: nethserver-smartd
Version: 1.0.1
Release: 1
License: GPL
Source: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: nethserver-devtools
Requires: nethserver-base
Requires: smartmontools
AutoReq: no


%description
NethServer smartd management system.


%preun

%post

%prep
%setup

%build
perl createlinks


%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT   > %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}-%{version}-%{release}-filelist 
%defattr(-,root,root)

%changelog
* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.1-1.ns6
- Lib: synchronize service status prop and chkconfig - Feature #2067 [NethServer]
- Full automatic package install/upgrade/uninstall support - Feature #1870 [NethServer]

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1.ns6
- First release. #1870
