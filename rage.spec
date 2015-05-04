%define git	20150504

Epoch:	1
Summary: 	Enlightened media center
Name: 		rage
Version:	0.1.0
Release:	1.%{git}.1
License:	BSD
Group:		Video
URL:		http://www.enlightenment.org/
Source0:	%{name}-%{git}.tar.xz

BuildRequires:	edje
BuildRequires:	evas
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(elementary)

%description
This is a media center designed mostly for use on a television hooked up to
your pc via a remote control. see the key controls at the end to make your
remote send the right keystrokes - eventually this will be 100% configurable
via the gui.

This is a WORK IN PROGRESS - it is NOT COMPLETE. do not expect everything to
work and do what you want.

%prep
%setup -qn %{name}-%{git}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_iconsdir}/%name.png
