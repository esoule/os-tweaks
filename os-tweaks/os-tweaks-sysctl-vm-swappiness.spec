%define _conf_filename           vm-swappiness
Name:           os-tweaks-sysctl-vm-swappiness
Version:        1.0
Release:        1%{?dist}
Summary:        set vm.swappiness = 1 in sysctl

Group:          System Environment/Base
License:        WTFPL

URL:            https://github.com/esoule
Source0:        %{name}.conf
Source100:      COPYING
Source101:      README.md

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       procps

%description
set vm.swappiness = 1 in sysctl

%prep
%setup -q  -c -T
install -pm 0644 %{SOURCE0} .
install -pm 0644 %{SOURCE100} .
install -pm 0644 %{SOURCE101} .

%build

%install
rm -rf $RPM_BUILD_ROOT

# yum
install -dm 755 $RPM_BUILD_ROOT/etc/sysctl.d
install -pm 644 %{name}.conf  $RPM_BUILD_ROOT/etc/sysctl.d/%{_conf_filename}.conf


%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun


%files
%defattr(-,root,root,-)
%doc COPYING README.md
%config(noreplace) /etc/sysctl.d/%{_conf_filename}.conf


%changelog
* Sun May  3 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package

