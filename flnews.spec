Name: flnews
Version: 1.2.1
Release: 1
Summary: Graphical USENET newsreader
License: BSD-2-Clause
Group: Networking/News
URL: https://micha.freeshell.org/flnews/
Source0: http://micha.freeshell.org/flnews/src/%{name}-%{version}.tar.bz2

BuildRequires: fltk-devel
BuildRequires: hicolor-icon-theme
BuildRequires: libopenssl-devel
BuildRequires: zlib-devel
Requires: xdg-utils

%description
flnews is a FLTK-based client with a graphical user interface to read
USENET newsgroups.

%prep
%autosetup
sed -i 's|CFG_XDG_DISABLE=1|CFG_XDG_DISABLE=0|g' CONFIG

%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc CHANGELOG README
%{_bindir}/flnews
%dir %{_datadir}/flnews/
%{_datadir}/flnews/license.txt
%dir %{_prefix}/lib/flnews/nls
%{_prefix}/lib/flnews/nls/de_DE.cat
%{_prefix}/lib/flnews/nls/fr_FR.cat
%{_mandir}/man1/flnews.1*
%{_datadir}/applications/flnews.desktop
%{_datadir}/icons/hicolor/*/apps/flnews.png
