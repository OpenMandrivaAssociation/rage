Summary: 	Enlightened media center
Name: 		rage
Version: 	0.3.0.042
Release: 	%mkrel 4
Source:		%{name}-%{version}.tar.bz2
License: 	BSD
Group: 		Video
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://www.enlightenment.org/
BuildRequires:	evas-devel
BuildRequires:	ecore-devel
BuildRequires:	edje-devel, edje
BuildRequires:	emotion-devel

%description
This is a media center designed mostly for use on a television hooked up to
your pc via a remote control. see the key controls at the end to make your
remote send the right keystrokes - eventually this will be 100% configurable
via the gui.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/*
%{_datadir}/%name
