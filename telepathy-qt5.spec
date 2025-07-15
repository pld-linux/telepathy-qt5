# "telepathy_qt" name is occupied by earlier work under the same name from different project;
# we used original "telepathy-qt4" name of this project (used before 0.9.0 release) until 0.9.7
# (the last version with qt4 support), then we moved to "telepathy-qt5".
%define		orgname	telepathy-qt
%define		qt5_ver		5.6.0

Summary:	Library for Qt5-based Telepathy clients
Summary(pl.UTF-8):	Biblioteka dla klientów Telepathy opartych na Qt5
Name:		telepathy-qt5
Version:	0.9.8
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://telepathy.freedesktop.org/releases/telepathy-qt/%{orgname}-%{version}.tar.gz
# Source0-md5:	2d55d477778ff7be9115746759bc398f
Patch0:		telepathy-qt-warnings.patch
URL:		https://telepathy.freedesktop.org/components/telepathy-qt/
BuildRequires:	Qt5Core-devel >= %{qt5_ver}
BuildRequires:	Qt5DBus-devel >= %{qt5_ver}
BuildRequires:	Qt5Network-devel >= %{qt5_ver}
BuildRequires:	Qt5Test-devel >= %{qt5_ver}
BuildRequires:	Qt5Xml-devel >= %{qt5_ver}
BuildRequires:	cmake >= 3.5
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	farstream-devel >= 0.2.0
BuildRequires:	glib2-devel >= 1:2.16
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	python3-dbus
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-pygobject3
BuildRequires:	qt5-assistant >= %{qt5_ver}
BuildRequires:	qt5-build >= %{qt5_ver}
BuildRequires:	qt5-qmake >= %{qt5_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	telepathy-farstream-devel >= 0.6.0
BuildRequires:	telepathy-glib-devel >= 0.18.0
Requires:	Qt5Core >= %{qt5_ver}
Requires:	Qt5DBus >= %{qt5_ver}
Requires:	Qt5Network >= %{qt5_ver}
Requires:	Qt5Xml >= %{qt5_ver}
Requires:	telepathy-farstream >= 0.6.0
Requires:	telepathy-glib >= 0.18.0
Obsoletes:	telepathy-qt4-yell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for Qt5-based Telepathy clients.

%description -l pl.UTF-8
Biblioteka dla klientów Telepathy opartych na Qt5.

%package devel
Summary:	Header files for telepathy-qt5 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki telepathy-qt5
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qt5_ver}
Requires:	Qt5DBus-devel >= %{qt5_ver}
Requires:	Qt5Network-devel >= %{qt5_ver}
Requires:	Qt5Xml-devel >= %{qt5_ver}

%description devel
Header files for telepathy-qt5 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki telepathy-qt5.

%package apidocs
Summary:	API documentation for telepathy-qt4 and telepathy-qt5 libraries
Summary(pl.UTF-8):	Dokumentacja API bibliotek telepathy-qt5 i telepathy-qt5
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for telepathy-qt4 and telepathy-qt5 libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek telepathy-qt5 i telepathy-qt5.

%prep
%setup -q -n %{orgname}-%{version}
%patch -P0 -p1

%build
install -d build-qt5
cd build-qt5
%cmake .. \
	-DENABLE_FARSTREAM:BOOL=ON \
	-DDESIRED_QT_VERSION=5 \
	-DQT_QMAKE_EXECUTABLE_FINDQT=%{_libdir}/qt5/bin/qmake

%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-qt5 install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libtelepathy-qt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-qt5.so.0
%attr(755,root,root) %{_libdir}/libtelepathy-qt5-farstream.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-qt5-farstream.so.0
%attr(755,root,root) %{_libdir}/libtelepathy-qt5-service.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-qt5-service.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy-qt5.so
%attr(755,root,root) %{_libdir}/libtelepathy-qt5-farstream.so
%attr(755,root,root) %{_libdir}/libtelepathy-qt5-service.so
%{_libdir}/cmake/TelepathyQt5
%{_libdir}/cmake/TelepathyQt5Farstream
%{_libdir}/cmake/TelepathyQt5Service
%{_includedir}/telepathy-qt5
%{_pkgconfigdir}/TelepathyQt5.pc
%{_pkgconfigdir}/TelepathyQt5Farstream.pc
%{_pkgconfigdir}/TelepathyQt5Service.pc

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
