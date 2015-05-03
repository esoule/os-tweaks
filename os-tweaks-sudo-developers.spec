%define _conf_filename         developers
Name:           os-tweaks-sudo-developers
Version:        1.0
Release:        1%{?dist}
Summary:        permit users in group developers to run certain commands as root

Group:          System Environment/Base
License:        WTFPL

URL:            https://github.com/esoule
Source0:        %{name}.conf
Source100:      COPYING
Source101:      README.md

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       sudo

%description
permit users in group developers to run certain commands as root


%prep
%setup -q  -c -T
install -pm 0644 %{SOURCE0} .
install -pm 0644 %{SOURCE100} .
install -pm 0644 %{SOURCE101} .

%build

%install
rm -rf $RPM_BUILD_ROOT

# yum
install -dm 0755 $RPM_BUILD_ROOT/etc/sudoers.d
install -pm 0644 %{name}.conf  $RPM_BUILD_ROOT/etc/sudoers.d/%{_conf_filename}


%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun


%files
%defattr(-,root,root,-)
%doc COPYING README.md
%config(noreplace) %attr(0440, root, root) /etc/sudoers.d/%{_conf_filename}


%changelog
* Sun May  3 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package

