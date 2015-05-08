%define _conf_filename           ipv4-forward
Name:           os-tweaks-sysctl-ipv4-forward
Version:        1.0
Release:        2%{?dist}
Summary:        enable IPv4 forwarding in sysctl

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
enables IPv4 forwarding in sysctl.

Please note that IPv4 forwarding must also be enabled
in firewall configuration.

See also: package firstinst-firewall-config will configure
the firewall for IPv4 forwarding, on first boot of the
installed system.

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
* Thu May  7 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-2
- provide better package description

* Sun May  3 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package

