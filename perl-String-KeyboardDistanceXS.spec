#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	KeyboardDistanceXS
Summary:	String::KeyboardDistanceXS - String Comparison Algorithm
Summary(pl):	String::KeyboardDistanceXS - algorytm por�wnywania �a�cuch�w
Name:		perl-String-KeyboardDistanceXS
Version:	0.02
Release:	2
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an XS implementation of the main qwerty functions for
computing the distance and match probabilities from the
String::KeyboardDistance module. Please see the documentation for
String::KeyboardDistance for more about these functions.

%description -l pl
To jest implementacja XS g��wnych funkcji qwerty z modu�u
String::KeyboardDistance, s�u��cych do obliczania odleg�o�ci i
dopasowywania prawdopodobie�stwa. Wi�cej o tych funkcjach w
dokumentacji do String::KeyboardDistance.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/%{pdir}/*.pm
%dir %{perl_sitearch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_sitearch}/auto/%{pdir}/%{pnam}/*.so
%{perl_sitearch}/auto/%{pdir}/%{pnam}/*.ix
%{perl_sitearch}/auto/%{pdir}/%{pnam}/*.bs
%{_mandir}/man3/*
