Summary:	XSL stylesheets for the Yelp help browser
Summary(pl.UTF-8):	Arkusze styli XSL dla przeglądarki pomocy Yelp
Name:		yelp-xsl
Version:	3.20.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/yelp-xsl/3.20/%{name}-%{version}.tar.xz
# Source0-md5:	2332716e6e39125a942bc761a6f94211
URL:		http://projects.gnome.org/yelp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-tools
BuildRequires:	intltool >= 0.40.0
BuildRequires:	itstool >= 1.2.0
BuildRequires:	libxml2-progs >= 1:2.6.12
BuildRequires:	libxslt-progs >= 1.1.8
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
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
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/yelp-xsl
%{_npkgconfigdir}/yelp-xsl.pc
