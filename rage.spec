%define efl_version 1.23.3

Epoch:	1
Summary: 	Enlightened media center
Name: 		rage
Version:	0.3.1
Release:	1
License:	BSD
Group:		Video
URL:		http://www.enlightenment.org/
Source0:	https://download.enlightenment.org/rel/apps/rage/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:	pkgconfig(ecore) >= %{efl_version}
BuildRequires:	pkgconfig(edje) >= %{efl_version}
BuildRequires:	pkgconfig(emotion) >= %{efl_version}
BuildRequires:	pkgconfig(evas) => %{efl_version}
BuildRequires:	pkgconfig(elementary) >= %{efl_version}

%description
This is a media center designed mostly for use on a television hooked up to
your pc via a remote control. see the key controls at the end to make your
remote send the right keystrokes - eventually this will be 100% configurable
via the gui.

This is a WORK IN PROGRESS - it is NOT COMPLETE. do not expect everything to
work and do what you want.

%prep
%setup -qn %{name}-%{version}
%meson

%build

%meson_build

%install
%meson_install

%files
%doc AUTHORS README TODO
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*x*/apps/%{name}.png
%{_libdir}/%{name}/*
