#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	String
%define		pnam	KeyboardDistanceXS
Summary:	String::KeyboardDistanceXS - string comparison algorithm
Summary(pl.UTF-8):	String::KeyboardDistanceXS - algorytm porównywania łańcuchów
Name:		perl-String-KeyboardDistanceXS
Version:	0.02
Release:	17
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/String/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	23daf2463e88297d7bc9ae72afc70e84
URL:		http://search.cpan.org/dist/String-KeyboardDistanceXS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an XS implementation of the main qwerty functions for
computing the distance and match probabilities from the
String::KeyboardDistance module. Please see the documentation for
String::KeyboardDistance for more about these functions.

%description -l pl.UTF-8
To jest implementacja XS głównych funkcji qwerty z modułu
String::KeyboardDistance, służących do obliczania odległości i
dopasowywania prawdopodobieństwa. Więcej o tych funkcjach w
dokumentacji do String::KeyboardDistance.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/String/*.pm
%dir %{perl_vendorarch}/auto/String/KeyboardDistanceXS
%attr(755,root,root) %{perl_vendorarch}/auto/String/KeyboardDistanceXS/*.so
%{perl_vendorarch}/auto/String/KeyboardDistanceXS/*.ix
%{_mandir}/man3/*
