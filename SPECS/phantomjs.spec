%define name	phantomjs
%define version	2.0.0
%define release 1

Summary:	a headless WebKit with JavaScript API
Name:     phantomjs
Version:	2.0.0
Release:  1%{?dist}.qg
License:	BSD
Group:		Utilities/Misc
BuildRoot: %{_topdir}/BUILDROOT
Source:   https://bitbucket.org/ariya/phantomjs/downloads/%{name}-%{version}-source.zip

BuildRequires: pkgconfig
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: flex
BuildRequires: bison
BuildRequires: gperf
BuildRequires: ruby
BuildRequires: openssl-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libicu-devel
BuildRequires: sqlite-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: alsa-lib-devel
BuildRequires: cups-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: glib-devel
BuildRequires: libxkbcommon-devel
BuildRequires: systemd-devel
BuildRequires: mtdev-devel
Requires:      urw-fonts

%description
PhantomJS is a headless WebKit with JavaScript API. It has fast and native
support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG. PhantomJS is created by Ariya Hidayat.

%prep
%setup -q

%build
./build.sh --confirm

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp bin/%{name} %{buildroot}%{_bindir}/%{name}
cp examples/* %{buildroot}%{_datadir}/%{name}/examples/
cp CONTRIBUTING.md %{buildroot}%{_datadir}/%{name}/
cp ChangeLog %{buildroot}%{_datadir}/%{name}/
cp LICENSE.BSD %{buildroot}%{_datadir}/%{name}/
cp README.md %{buildroot}%{_datadir}/%{name}/

%files
%defattr(0444,root,root)
%attr(0555,root,root)%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
* Wed Jan 13 2016 <vitvegl@quintagroup.org>
- rebuilt for fc22

* Fri Jul 17 2015 <vitvegl@quintagroup.org>
- rebuilt for fc21

* Sat May 9 2015 Frankie Dintino <fdintino@gmail.com>
- updated to version 2.0, added BuildRequires directives

* Fri Apr 18 2014 Eric Heydenberk <heydenberk@gmail.com>
- add missing filenames for examples to files section

* Tue Apr 30 2013 Eric Heydenberk <heydenberk@gmail.com>
- add missing filenames for examples to files section

* Wed Apr 24 2013 Robin Helgelin <lobbin@gmail.com>
- updated to version 1.9

* Thu Jan 24 2013 Matthew Barr <mbarr@snap-interactive.com>
- updated to version 1.8

* Thu Nov 15 2012 Jan Schaumann <jschauma@etsy.com>
- first rpm version
