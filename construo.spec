Summary:	Simple 2D construction programme
Summary(pl.UTF-8):   Prosty program do tworzenia dwuwymiarowych konstrukcji
Name:		construo
Version:	0.2.2
Release:	3
License:	GPL
Group:		X11/Amusements
Source0:	http://freesoftware.fsf.org/download/construo/construo.pkg/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c18144898f98929b67245c5f703f9f39
Patch0:		%{name}-no_games.patch
URL:		http://www.nongnu.org/construo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glut-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Construo is a programme for constructing wire-frame objects and let
them react on physical forces, its neither a real simulation nor a
real game, its just a little toy app which can be a nice way to waste
time.

%description -l pl.UTF-8
Construo to program do konstruowania obiektów w postaci modeli
drutowych i umożliwiania im reagowania na siły fizyczne - nie jest to
prawdziwa symulacja ani prawdziwa gra, jedynie mała aplikacja do
zabawy, mogąca być miłym sposobem marnowania czasu.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-debug
%{__make}

%install
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
