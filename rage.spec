Summary: 	Enlightened media center
Name: 		rage
Version: 	0.3.0.042
Release: 	%mkrel 1
Source:		%{name}-%{version}.tar.bz2
License: 	BSD
Group: 		Video
URL: 		http://www.enlightenment.org/
BuildRequires:	evas-devel
BuildRequires:	ecore-devel
BuildRequires:	edje-devel, edje
BuildRequires:	emotion-devel

%description
Emprint is a utility for taking screenshots of the entire screen, a specific
window, or a specific region. It is written with the Enlightenment Foundation
Libraries.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/*
%{_datadir}/%name
