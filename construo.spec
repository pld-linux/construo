Summary:	Simple 2D construction programme
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
Construo is a programme for constructing wire-frame objects and let
them react on physical forces, its neither a real simulation nor a
real game, its just a little toy app which can be a nice way to waste
time.

%description -l pl
Construo to program do konstruowania obiektów w postaci modeli
drutowych i umo¿liwiania im reagowania na si³y fizyczne - nie jest to
prawdziwa symulacja ani prawdziwa gra, jedynie ma³a aplikacja do
zabawy, mog±ca byæ mi³ym sposobem marnowania czasu.

%prep
%setup -q

%build
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
%{_datadir}/games/construo
