#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	ResolveLink
Summary:	HTML::ResolveLink - Resolve relative links in (X)HTML into absolute URI
Summary(pl.UTF-8):	HTML::ResolveLink - rozwiązywanie odnośników względnych w (X)HTML-u do bezwzględnych URI
Name:		perl-HTML-ResolveLink
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a87ff3445b30b7fa51fae422ebb46001
URL:		http://search.cpan.org/dist/HTML-ResolveLink/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Parser >= 3.26
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::ResolveLink is a module to rewrite relative links in XHTML or
HTML into absolute URI.

For example. when you have

  <a href="foo.html">foo</a>
  <img src="/bar.gif" />

and use http://www.example.com/foo/bar as base URL, you'll get:

  <a href="http://www.example.com/foo/foo.html">foo</a>
  <img src="http://www.example.com/bar.gif" />

%description -l pl.UTF-8
HTML::ResolveLink to moduł do przepisywania odnośników względnych w
XHTML-u lub HTML-u na bezwzględne URI.

Na przykład dla:

  <a href="foo.html">foo</a>
  <img src="/bar.gif" />

i użycia http://www.example.com/foo/bar jako URL-a bazowego
otrzymujemy:

  <a href="http://www.example.com/foo/foo.html">foo</a>
  <img src="http://www.example.com/bar.gif" />

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/HTML/*.pm
%{_mandir}/man3/*
