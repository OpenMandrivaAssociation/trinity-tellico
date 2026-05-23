%bcond clang 1
%bcond gamin 1

# TDE variables
%define tde_pkg tellico
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	Icollection manager for books, videos, music [Trinity]
Group:		Applications/Utilities
URL:		http://periapsis.org/tellico/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/office/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_LIBKCDDB=ON
BuildOption:    -DWITH_LIBKCAL=ON
BuildOption:    -DWITH_LIBBTPARSE=OFF
BuildOption:    -DWITH_SAX_LOADER=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tdemultimedia-devel >= %{version}
BuildRequires:	trinity-libkcal-devel >= %{version}
BuildRequires:	trinity-libpoppler-tqt-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils
BuildRequires:	gettext


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


Requires:		%{name}-data = %{EVRD}
Requires:		%{name}-scripts = %{EVRD}


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
%{tde_prefix}/bin/tellico
%{tde_prefix}/share/applications
%config(noreplace) %{_sysconfdir}/trinity/tellicorc
%{tde_prefix}/share/man/man1/tellico.1*

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
%dir %{tde_prefix}/share/apps/tellico
%{tde_prefix}/share/apps/tellico/*.xsl
%{tde_prefix}/share/apps/tellico/*.xml
%{tde_prefix}/share/apps/tellico/*.png
%{tde_prefix}/share/apps/tellico/entry-templates
%{tde_prefix}/share/apps/tellico/*.py*
%{tde_prefix}/share/apps/tellico/pics
%{tde_prefix}/share/apps/tellico/report-templates
%{tde_prefix}/share/apps/tellico/tellico.dtd
%{tde_prefix}/share/apps/tellico/tellico.tips
%{tde_prefix}/share/apps/tellico/tellico2html.js
%{tde_prefix}/share/apps/tellico/tellicoui.rc
%{tde_prefix}/share/apps/tellico/welcome.html
%{tde_prefix}/share/config.kcfg
%{tde_prefix}/share/doc/tde/HTML/*/tellico/
%{tde_prefix}/share/icons/hicolor/*/apps/tellico.png
%{tde_prefix}/share/icons/hicolor/*/mimetypes/application-x-tellico.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/tellico.svg
%{tde_prefix}/share/icons/hicolor/scalable/mimetypes/application-x-tellico.svg
%{tde_prefix}/share/mime/packages/tellico.xml
%{tde_prefix}/share/mimelnk/application/x-tellico.desktop
%{tde_prefix}/share/apps/tdeconf_update/tellico-1-3-update.pl
%{tde_prefix}/share/apps/tdeconf_update/tellico-rename.upd
%{tde_prefix}/share/apps/tdeconf_update/tellico.upd

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
%{tde_prefix}/share/apps/tellico/data-sources
%{tde_prefix}/share/apps/tellico/z3950-servers.cfg


%prep -a
if [ -r /usr/include/libv4l1-videodev.h ]; then
%__sed -i "src/barcode/barcode_v4l.h" -e "s|linux/videodev.h|libv4l1.h|"
fi


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
# Add svg icons to xdg directories
%__install -D -c -p -m 644 "icons/tellico.svg" "%{?buildroot}%{tde_prefix}/share/icons/hicolor/scalable/apps/tellico.svg"
%__install -D -c -p -m 644 "icons/tellico_mime.svg" "%{?buildroot}%{tde_prefix}/share/icons/hicolor/scalable/mimetypes/application-x-tellico.svg"

%find_lang %{tde_pkg}

