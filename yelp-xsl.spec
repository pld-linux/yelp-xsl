Summary:	XSL stylesheets for the Yelp help browser
Summary(pl.UTF-8):	Arkusze styli XSL dla przeglądarki pomocy Yelp
Name:		yelp-xsl
Version:	2.91.92
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/yelp-xsl/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	66b7f5e930f7aa55de36b0fd59ee28e7
URL:		http://projects.gnome.org/yelp/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libxml2-devel >= 1:2.6.12
BuildRequires:	libxslt-devel >= 1.1.8
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains XSL stylesheets that are used by the Yelp help
browser.

%description -l pl.UTF-8
Ten pakiet zawiera arkusze styli, które są używane przez przeglądarkę
pomocy Yelp.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang yelp-xsl

%clean
rm -rf $RPM_BUILD_ROOT

%files -f yelp-xsl.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/yelp-xsl
%{_npkgconfigdir}/yelp-xsl.pc
