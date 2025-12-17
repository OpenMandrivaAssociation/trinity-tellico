%bcond clang 1
%bcond gamin 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 3

%define tde_pkg tellico
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.3.2.1
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Icollection manager for books, videos, music [Trinity]
Group:		Applications/Utilities
URL:		http://periapsis.org/tellico/

License:	GPLv2+

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/office/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_NO_BUILTIN_CHRPATH=ON
BuildOption:    -DBIN_INSTALL_DIR=%{tde_bindir}
BuildOption:    -DCONFIG_INSTALL_DIR="%{tde_confdir}"
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir}
BuildOption:    -DLIB_INSTALL_DIR=%{tde_libdir}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_datadir}
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_LIBKCDDB=ON
BuildOption:    -DWITH_LIBKCAL=ON
BuildOption:    -DWITH_LIBBTPARSE=OFF
BuildOption:    -DWITH_SAX_LOADER=ON

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-tdemultimedia-devel >= %{tde_version}
BuildRequires:	trinity-libkcal-devel >= %{tde_version}
BuildRequires:	trinity-libpoppler-tqt-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

# POPPLER support
BuildRequires:  pkgconfig(poppler)

# YAZ support
BuildRequires:	pkgconfig(yaz)

# XML2 support
BuildRequires:  pkgconfig(libxml-2.0)

# XSLT support
BuildRequires:  pkgconfig(libxslt)

# V4L support
BuildRequires:	%{_lib}v4l-devel

# EXEMPI support
BuildRequires:  pkgconfig(exempi-2.0)

# PCRE2 support
BuildRequires:  pkgconfig(libpcre2-posix)

# IDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# ACL support
BuildRequires:  pkgconfig(libacl)

# ATTR support
BuildRequires:  pkgconfig(libattr)

# PYTHON support
%global python python3
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel

# Readline support
BuildRequires:	readline-devel

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


Requires:		%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-scripts = %{?epoch:%{epoch}:}%{version}-%{release}


%description
Tellico is a collection manager for TDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections; with unlimited
user-defined fields allowed. Automatically formatted names, sorting by any
property, filters, automatic ISBN validation and full customization for
printing or display through XSLT files are some of the features present. It
can import CSV, RIS, BibTeX, and BibTeXML files; and export CSV, HTML, BibTeX,
BibTeXML, and PilotDB. Tellico can also import data from Amazon, IMDb, CDDB,
or any US-MARC compliant z39.50 server.

The files are stored in XML format, avoiding the need for database server.
It also makes it easy for other softwares to use the Tellico data.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/tellico
%{tde_datadir}/applications
%config(noreplace) %{tde_confdir}/tellicorc
%{tde_mandir}/man1/tellico.1*

##########

%package data
Group:			Applications/Utilities
Summary:		collection manager for books, videos, music [data] [Trinity]

%description data
Tellico is a collection manager for TDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections; with unlimited
user-defined fields allowed. Automatically formatted names, sorting by any
property, filters, automatic ISBN validation and full customization for
printing or display through XSLT files are some of the features present. It
can import CSV, RIS, BibTeX, and BibTeXML files; and export CSV, HTML, BibTeX,
BibTeXML, and PilotDB. Tellico can also import data from Amazon, IMDb, CDDB,
or any US-MARC compliant z39.50 server.

The files are stored in XML format, avoiding the need for database server.
It also makes it easy for other softwares to use the Tellico data.

This package contains the architecture independent files, such data files and
documentation.

%files data
%defattr(-,root,root,-)
%dir %{tde_datadir}/apps/tellico
%{tde_datadir}/apps/tellico/*.xsl
%{tde_datadir}/apps/tellico/*.xml
%{tde_datadir}/apps/tellico/*.png
%{tde_datadir}/apps/tellico/entry-templates
%{tde_datadir}/apps/tellico/*.py*
%{tde_datadir}/apps/tellico/pics
%{tde_datadir}/apps/tellico/report-templates
%{tde_datadir}/apps/tellico/tellico.dtd
%{tde_datadir}/apps/tellico/tellico.tips
%{tde_datadir}/apps/tellico/tellico2html.js
%{tde_datadir}/apps/tellico/tellicoui.rc
%{tde_datadir}/apps/tellico/welcome.html
%{tde_datadir}/config.kcfg
%{tde_tdedocdir}/HTML/*/tellico/
%{tde_datadir}/icons/hicolor/*/apps/tellico.png
%{tde_datadir}/icons/hicolor/*/mimetypes/application-x-tellico.png
%{tde_datadir}/icons/hicolor/scalable/apps/tellico.svg
%{tde_datadir}/icons/hicolor/scalable/mimetypes/application-x-tellico.svg
%{tde_datadir}/mime/packages/tellico.xml
%{tde_datadir}/mimelnk/application/x-tellico.desktop
%{tde_datadir}/apps/tdeconf_update/tellico-1-3-update.pl
%{tde_datadir}/apps/tdeconf_update/tellico-rename.upd
%{tde_datadir}/apps/tdeconf_update/tellico.upd

##########

%package scripts
Group:			Applications/Utilities
Summary:		collection manager for books, videos, music [scripts] [Trinity]

%description scripts
Tellico is a collection manager for TDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections; with unlimited
user-defined fields allowed. Automatically formatted names, sorting by any
property, filters, automatic ISBN validation and full customization for
printing or display through XSLT files are some of the features present. It
can import CSV, RIS, BibTeX, and BibTeXML files; and export CSV, HTML, BibTeX,
BibTeXML, and PilotDB. Tellico can also import data from Amazon, IMDb, CDDB,
or any US-MARC compliant z39.50 server.

The files are stored in XML format, avoiding the need for database server.
It also makes it easy for other softwares to use the Tellico data.

This package contains the scripts to import data from external sources, such
as websites. As the format of the data may change, these scripts are provided
as a separate package which can be updated through debian-volatile.

%files scripts
%defattr(-,root,root,-)
%{tde_datadir}/apps/tellico/data-sources
%{tde_datadir}/apps/tellico/z3950-servers.cfg


%prep -a
if [ -r /usr/include/libv4l1-videodev.h ]; then
%__sed -i "src/barcode/barcode_v4l.h" -e "s|linux/videodev.h|libv4l1.h|"
fi


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"


%install -a
# Add svg icons to xdg directories
%__install -D -c -p -m 644 "icons/tellico.svg" "%{?buildroot}%{tde_datadir}/icons/hicolor/scalable/apps/tellico.svg"
%__install -D -c -p -m 644 "icons/tellico_mime.svg" "%{?buildroot}%{tde_datadir}/icons/hicolor/scalable/mimetypes/application-x-tellico.svg"

%find_lang %{tde_pkg}

