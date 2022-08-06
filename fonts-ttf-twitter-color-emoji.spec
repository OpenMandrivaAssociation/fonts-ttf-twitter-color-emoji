Name: fonts-ttf-twitter-color-emoji
Version: 14.0.2
Release: 1
Source0: https://github.com/eosrei/twemoji-color-font/archive/refs/heads/master.tar.gz#/twemoji-color-font.tar.gz
Source1: https://github.com/twitter/twemoji/archive/refs/tags/v%{version}.tar.gz
Source2: https://github.com/13rac1/scfbuild/archive/refs/heads/master.tar.gz#/scfbuild.tar.gz
# Based on comments on https://github.com/googlefonts/noto-emoji/issues/36
Source3: twitter-color-emoji.conf
Summary: Color and Black-and-White Twitter emoji fonts
URL: https://twemoji.twitter.com/
License: CC-BY-4.0
Group: Fonts
BuildRequires: fonttools
BuildRequires: imagemagick
BuildRequires: inkscape
BuildRequires: potrace
BuildRequires: make
BuildRequires: python%{py_ver}dist(fonttools) >= 4.7.0
BuildRequires: python%{py_ver}dist(pyyaml)
BuildRequires: nodejs-svgo
BuildRequires: fontforge fontforge-python
BuildRequires: locales-extra-charsets
BuildArch: noarch

%description
Color and Black-and-White Twitter emoji fonts

%prep
%setup -n twemoji-color-font-master -b 1 -a 2
mv ../twemoji-%{version} ../twemoji
mv scfbuild-master SCFBuild
make update

%build
make build/TwitterColorEmoji-SVGinOT.ttf VERSION=%{version}

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF
install -c -m 644 build/TwitterColorEmoji-SVGinOT.ttf %{buildroot}%{_datadir}/fonts/TTF/

mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
install -c -m 644 %{S:3} %{buildroot}%{_sysconfdir}/fonts/conf.d/90-twitter-emoji.conf

%files
%{_sysconfdir}/fonts/conf.d/*
%{_datadir}/fonts/TTF/*
