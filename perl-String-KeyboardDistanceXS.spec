#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	KeyboardDistanceXS
Summary:	String::KeyboardDistanceXS - String Comparison Algorithm
Summary(pl):	String::KeyboardDistanceXS - algorytm porównywania ³añcuchów
Name:		perl-String-KeyboardDistanceXS
Version:	0.02
Release:	3
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	23daf2463e88297d7bc9ae72afc70e84
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an XS implementation of the main qwerty functions for
computing the distance and match probabilities from the
String::KeyboardDistance module. Please see the documentation for
String::KeyboardDistance for more about these functions.

%description -l pl
To jest implementacja XS g³ównych funkcji qwerty z modu³u
String::KeyboardDistance, s³u¿±cych do obliczania odleg³o¶ci i
dopasowywania prawdopodobieñstwa. Wiêcej o tych funkcjach w
dokumentacji do String::KeyboardDistance.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/%{pdir}/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.so
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.ix
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.bs
%{_mandir}/man3/*
