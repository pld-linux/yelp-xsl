Summary:	XSL stylesheets for the Yelp help browser
Summary(pl.UTF-8):	Arkusze styli XSL dla przeglądarki pomocy Yelp
Name:		yelp-xsl
Version:	42.4
Release:	1
# depending on part, see COPYING
License:	GPL v2+, LGPL v2+, MIT (see COPYING)
Group:		Libraries
Source0:	https://download.gnome.org/sources/yelp-xsl/42/%{name}-%{version}.tar.xz
# Source0-md5:	e0f6ed43c206bb205057d0adf76e83bd
URL:		https://apps.gnome.org/Yelp/
BuildRequires:	gettext-tools >= 0.19.4
BuildRequires:	itstool >= 1.2.0
BuildRequires:	libxml2-progs >= 1:2.6.12
BuildRequires:	libxslt-progs >= 1.1.8
BuildRequires:	meson >= 1.3
BuildRequires:	ninja >= 1.5
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
%meson \
	-Ddita=true

# TODO (requires xsltdoc-scan and mal2cache tools; they used to be included, but are no longer):
# -Dyelp_manual=true

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.md
%{_datadir}/yelp-xsl
%{_npkgconfigdir}/yelp-xsl.pc
