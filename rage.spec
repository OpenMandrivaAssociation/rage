%define efl_version 1.26.1

Epoch:	1
Summary: 	Enlightened media center
Name: 		rage
Version:	0.4.0
Release:	1
License:	BSD
Group:		Video
URL:		https://www.enlightenment.org/
Source0:	https://download.enlightenment.org/rel/apps/rage/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  efl >= %{efl_version}}
BuildRequires:	pkgconfig(efl) >= %{efl_version}}

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
