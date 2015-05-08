
Name:           os-tweaks-ls-color-extra
Version:        1.0
Release:        2%{?dist}
Summary:        provides lll alias for ls -la --color=auto

Group:          System Environment/Base
License:        WTFPL

URL:            https://github.com/esoule
Source0:        %{name}.sh
Source1:        %{name}.csh
Source100:      COPYING
Source101:      README.md

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       /etc/profile.d

%description
provides lll alias for ls -la --color=auto

%prep
%setup -q  -c -T
install -pm 0644 %{SOURCE0} .
install -pm 0644 %{SOURCE1} .
install -pm 0644 %{SOURCE100} .
install -pm 0644 %{SOURCE101} .

%build

%install
rm -rf $RPM_BUILD_ROOT

# yum
install -dm 755 $RPM_BUILD_ROOT/etc/profile.d
install -pm 644 %{name}.sh  $RPM_BUILD_ROOT/etc/profile.d
install -pm 644 %{name}.csh  $RPM_BUILD_ROOT/etc/profile.d


%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun


%files
%defattr(-,root,root,-)
%doc COPYING README.md
%config(noreplace) /etc/profile.d/%{name}.sh
%config(noreplace) /etc/profile.d/%{name}.csh


%changelog
* Thu May  7 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-2
- provide better package description

* Sun May  3 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.0-1
- Initial Package

