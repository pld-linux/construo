Summary:	Simple 2D construction programm
Summary(pl):	Prosty program do tworzenia dwuwymiarowych konstrukcji
Name:		construo
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://freesoftware.fsf.org/download/construo/construo.pkg/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f8c27c5f2d806fcdc68a253e254490df
URL:		http://www.nongnu.org/construo/
BuildRequires:	glut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		%{_prefix}/games

%description
Construo is a programm for constructing wire-frame objects and let
them react on physical forces, its neither a real simulation nor a
real game, its just a little toy app which can be a nice way to waste
time.

%prep
%setup -q

%build
%configure \
	--disable-debug
%{__make}

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/construo
