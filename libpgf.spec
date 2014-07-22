%bcond_without	tests
Summary:	PGF image format library
Summary(pl.UTF-8):	Biblioteka obsługująca format plików PGF
Name:		libpgf
Version:	6.11.42
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libpgf/%{name}-%{version}-src.zip
# Source0-md5:	9a3c700f0b3e36755f9044a348d6e0ce
URL:		http://www.libpgf.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	libtool
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PGF is a new image file format, based on discrete, fast wavelet
transform with progressive coding features. Lossless and lossy
compression. Best for natural and aerial images. For such images with
a better compression efficiency than JPEG. PGF is one of the best
algorithms available these days for compression of natural images.

%description -l pl.UTF-8
PGF to nowy format plików obrazów, oparty na dyskretnej, szybkiej
transformacie falkowej połączonej z kodowaniem progresywnym. Kompresja
może być bezstratna, jak i stratna. Format jest najlepszy dla obrazów
naturalnych i lotniczych.  Dla takich obrazów osiąga się lepszą
wydajność kompresji niż format JPEG. PGF jest obecnie jednym z
najlepszych algorytmów dla obrazów naturalnych.

%package devel
Summary:	Header files for libpgf library
Summary(de.UTF-8):	libpgf Headers
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas estáticas
Summary(fr.UTF-8):	en-têtes et bibliothèques statiques
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpgf
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas estáticas
Summary(tr.UTF-8):	başlık dosyaları ve statik kitaplıklar
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The header files are only needed for development of programs using the
PGF library.

%description devel -l de.UTF-8
Die Header-Dateien werden nur zur Entwicklung von Programmen mit der
PGF-Library benötigt.

%description devel -l es.UTF-8
Archivos de inclusión y bibliotecas estáticas que son necesarios
solamente para el desarrollo de programas que usan la biblioteca PGF.

%description devel -l fr.UTF-8
Fichiers d'en-tete et les librairies qui sont requis seulement pour le
développement avec la librairie PGF.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających biblioteki PGF.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão e bibliotecas estáticas que são necessários
somente para o desenvolvimento de programas que usam a biblioteca PGF.

%description devel -l tr.UTF-8
PGF kitaplığını kullanan programlar geliştirmek için gereken
kitaplıklar ve başlık dosyaları.

%package static
Summary:	Static PGF library
Summary(de.UTF-8):	Statisch PGF Library
Summary(pl.UTF-8):	Biblioteka statyczna PGF
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libpgf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static PGF library.

%description static -l de.UTF-8
Statisch PGF Library.

%description static -l pl.UTF-8
Biblioteka statyczna PGF.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libpgf.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpgf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpgf.so.4

%files devel
%defattr(644,root,root,755)
%doc README doc/html/*
%attr(755,root,root) %{_libdir}/libpgf.so
%{_pkgconfigdir}/libpgf.pc
%{_includedir}/libpgf
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpgf.a
