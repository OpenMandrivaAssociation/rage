#%define git	20150504
%define efl_version 1.19.1

Epoch:	1
Summary: 	Enlightened media center
Name: 		rage
Version:	0.2.1
Release:	1
License:	BSD
Group:		Video
URL:		http://www.enlightenment.org/
Source0:	%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildRequires:	edje
BuildRequires:	evas
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

%build
#NOCONFIGURE=yes ./autogen.sh
%configure
%make

%install
%makeinstall_std

%files
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_iconsdir}/%name.png
%{_libdir}/%{name}/*