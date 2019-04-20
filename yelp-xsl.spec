Summary:	XSL stylesheets for the Yelp help browser
Summary(pl.UTF-8):	Arkusze styli XSL dla przeglądarki pomocy Yelp
Name:		yelp-xsl
Version:	3.32.1
Release:	1
# depending on part, see COPYING
License:	GPL v2+, LGPL v2+, MIT (see COPYING)
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/yelp-xsl/3.32/%{name}-%{version}.tar.xz
# Source0-md5:	e5b800a872b50243570552402b56f0d6
URL:		https://wiki.gnome.org/Apps/Yelp
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11.2
BuildRequires:	gettext-tools
BuildRequires:	intltool >= 0.40.0
BuildRequires:	itstool >= 1.2.0
BuildRequires:	libxml2-progs >= 1:2.6.12
BuildRequires:	libxslt-progs >= 1.1.8
BuildRequires:	pkgconfig
BuildRequires:	python3-ducktype
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
yelp-xsl is a collection of programs and data files to help you build,
maintain, and distribute documentation. It provides XSLT stylesheets
that can be built upon for help viewers and publishing systems. These
stylesheets output JavaScript and CSS content, and reference images
provided by yelp-xsl. This package also redistributes copies of the
jQuery and jQuery.Syntax JavaScript libraries.

%description -l pl.UTF-8
yelp-xsl to zbiór plików programów i danych pomocnych przy budowaniu,
utrzymywaniu i dystrybucji dokumentacji. Zawiera arkusze styli XSLT,
w oparciu o które można zbudować przeglądarki pomocy i systemy
publikowania. Wyjściem arkuszy jest treść w JavaScripcie i CSS oraz
obrazki referencyjne zawarte w pakiecie. Pakiet zawiera także kopie
bibliotek JavaScriptu jQuery i jQuery.Syntax.

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
%doc AUTHORS COPYING ChangeLog NEWS README
%{_datadir}/yelp-xsl
%{_npkgconfigdir}/yelp-xsl.pc
