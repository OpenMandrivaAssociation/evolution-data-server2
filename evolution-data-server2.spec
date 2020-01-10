%define oname evolution-data-server
%define nspr_major 4
%define nss_major 3

%define _requires_exceptions nspr%{nspr_major}\\|plc%{nspr_major}\\|plds%{nspr_major}\\|nss%{nss_major}\\|smime%{nss_major}\\|softokn%{nss_major}\\|ssl%{nss_major}\\|nssutil%{nss_major}

%define api_version 1.2
%define base_version 2.32
%define lib_major 6
%define lib_name %mklibname %{oname} %{lib_major}

%define oldmajor 6
%define oldlibname %mklibname %{oname} %{oldmajor}

%define oldmajor2006 4
%define oldlibname2006 %mklibname %{oname} %{oldmajor2006}

%define camelmajor 19
%define camel_libname %mklibname camel %{camelmajor}

%define ebookmajor 10
%define ebook_libname %mklibname ebook %{ebookmajor}

%define ecalmajor 8
%define ecal_libname %mklibname ecal %{ecalmajor}

%define edatabookmajor 8
%define edatabook_libname %mklibname edata-book %{edatabookmajor}

%define edatacalmajor 10
%define edatacal_libname %mklibname edata-cal %{edatacalmajor}

%define edataservermajor 14
%define edataserver_libname %mklibname edataserver %{edataservermajor}
%define edataserver_libnamedev %mklibname -d edataserver2

%define edataserveruimajor 11
%define edataserverui_libname %mklibname edataserverui %{edataserveruimajor}

%define egroupwisemajor 13
%define egroupwise_libname %mklibname egroupwise %{egroupwisemajor}

%define ebackendmajor 0
%define ebackend_libname %mklibname ebackend %{ebackendmajor}

Name:		evolution-data-server2
Summary:	Evolution Data Server
Version:	2.32.3
Release:	6
License:	LGPLv2+
Group:		System/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.bz2
Patch0:		evolution-data-server-2.32.3-deprecated.patch
Patch1:		evolution-data-server-2.32.3-fix-linking.patch
Patch2:		evolution-data-server-2.32.3-automake1.12.patch
Patch3:		evolution-data-server-2.32.3-linkage2.patch
URL:		http://www.gnome.org/projects/evolution/

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gperf
BuildRequires:	gtk-doc
BuildRequires:	docbook-dtd412-xml
BuildRequires:	krb5-devel
BuildRequires:	libgweather2-devel >= 2.25.4
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	nss-devel
BuildRequires:	nspr-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	libgdata0.6-devel >= 0.6.3
BuildRequires:	openldap-devel
BuildRequires:	sqlite3-devel >= 3.5
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	GConf2
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	intltool
BuildRequires:	db-devel
Conflicts:	%{oname}
Obsoletes:	%{oldlibname} < 2.32.3-6


%description
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{camel_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{oldlibname2006} < 2.32.3-6

%description -n %{camel_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ebook_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries

%description -n %{ebook_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ecal_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries

%description -n %{ecal_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edatabook_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{oldlibname2006} < 2.32.3-6

%description -n %{edatabook_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edatacal_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{oldlibname2006} < 2.32.3-6

%description -n %{edatacal_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserver_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{oldlibname2006} < 2.32.3-6

%description -n %{edataserver_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserverui_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{_lib}edataserverui4 < 2.32.3-6

%description -n %{edataserverui_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{egroupwise_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries

%description -n %{egroupwise_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ebackend_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries

%description -n %{ebackend_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserver_libnamedev}
Summary:	Libraries and include files for using Evolution Data Server
Group:		Development/GNOME and GTK+
Requires:	%{camel_libname} = %{version}-%{release}
Requires:	%{ebook_libname} = %{version}-%{release}
Requires:	%{ecal_libname} = %{version}-%{release}
Requires:	%{edatabook_libname} = %{version}-%{release}
Requires:	%{edatacal_libname} = %{version}-%{release}
Requires:	%{edataserver_libname} = %{version}-%{release}
Requires:	%{edataserverui_libname} = %{version}-%{release}
Requires:	%{egroupwise_libname} = %{version}-%{release}
Requires:	%{ebackend_libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libedataserver-devel = %{version}-%{release}
Requires:	nss-devel
Requires:	nspr-devel
#gw libtool dep:
Requires:	libgdata0.6-devel
Obsoletes:	%{mklibname -d edataserver 9} < 2.32.3-6

%description -n %{edataserver_libnamedev}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%prep
%setup -q -n %{oname}-%{version}
%autopatch -p1
autoreconf -fi

%build
%configure2_5x --with-krb5=%{_prefix} --with-krb5-libs=%{_libdir} \
--with-libdb=%{_prefix} \
--with-openldap=yes --with-static-ldap=no --enable-gtk-doc=yes 
#--enable-gnome-keyring=yes
%make

%install
%makeinstall_std

%find_lang %{oname}-%{base_version}

%files -f %{oname}-%{base_version}.lang
%doc COPYING NEWS
%{_libexecdir}/%{oname}-%{api_version}
%{_libexecdir}/camel-index-control-%{api_version}
%{_libexecdir}/e-addressbook-factory
%{_libexecdir}/e-calendar-factory
%attr(2755,root,mail) %{_libexecdir}/camel-lock-helper-%{api_version}
%{_datadir}/%{oname}-%{base_version}
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.AddressBook.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.Calendar.service
%{_datadir}/pixmaps/%{oname}

%files -n %{camel_libname}
%{_libdir}/libcamel-%{api_version}.so.%{camelmajor}*
%{_libdir}/libcamel-provider-%{api_version}.so.%{camelmajor}*

%files -n %{ebook_libname}
%{_libdir}/libebook-%{api_version}.so.%{ebookmajor}*

%files -n %{ecal_libname}
%{_libdir}/libecal-%{api_version}.so.%{ecalmajor}*

%files -n %{edatabook_libname}
%{_libdir}/libedata-book-%{api_version}.so.%{edatabookmajor}*

%files -n %{edatacal_libname}
%{_libdir}/libedata-cal-%{api_version}.so.%{edatacalmajor}*

%files -n %{edataserver_libname}
%{_libdir}/libedataserver-%{api_version}.so.%{edataservermajor}*

%files -n %{edataserverui_libname}
%{_libdir}/libedataserverui-%{api_version}.so.%{edataserveruimajor}*

%files -n %{egroupwise_libname}
%{_libdir}/libegroupwise-%{api_version}.so.%{egroupwisemajor}*

%files -n %{ebackend_libname}
%{_libdir}/libebackend-%{api_version}.so.%{ebackendmajor}*

%files -n %{edataserver_libnamedev}
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/%{oname}-%{base_version}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so


%changelog
* Fri Dec 16 2011 Götz Waschk <waschk@mandriva.org> 2.32.3-5mdv2012.0
+ Revision: 743115
- fix deps and conflicts

* Thu Dec 15 2011 Götz Waschk <waschk@mandriva.org> 2.32.3-4
+ Revision: 741485
- fork out old e-d-s
- fix build
- rebuild for new libpng
- new version
- drop patch
- update to new version 2.32.2
- update to new version 2.32.1
- update devel deps
- update to new version 2.32.0
- update to new version 2.31.92.1
- new version
- new version
- new edataserverui major
- update to new version 2.31.90
- rebuild for new libproxy
- new version
- new major
- new base version
- new version
- new major
- depend on external libgdata
- rebuild for lost package
- update to new version 2.30.1
- update to new version 2.30.0
- remove old configure option
- update build deps
- update to new version 2.29.92
- update to new version 2.29.91
- update to new version 2.29.90
- update to new version 2.29.6
- new version
- new edata-cal major
- update to new version 2.29.4
- new version
- update build deps
- drop exchange-storage lib
- update file list
- update to new version 2.28.0
- update to new version 2.27.92
- update to new version 2.27.91
- update to new version 2.27.90
- update to new version 2.27.5
- update to new version 2.27.4
- update to new version 2.27.3
- update to new version 2.27.2
- new version
- new dir version
- update to new version 2.26.1.1
- update to new version 2.26.1
- update to new version 2.26.0
- new version
- drop patch 1
- update to new version 2.25.91
- new version
- update patch 1
- depend on libical
- new camel major
- update to new version 2.25.5
- new version
- bump libgweather dep
- update build deps
- new version
- fix build
- fix build deps
- rebuild to get rid of libtasn1 dep
- fix build deps
- update to new version 2.25.2
- new version
- new base ver
- new camel major
- new version
- new camel major
- drop patch 1
- new version
- new version
- update license
- new version
- fix previous fix
- new version
- drop patches 1 and 2
- patch to fix gtk-doc build
- fix buildrequires
- new version
- new camel major
- drop camel-provider package
- disable gtk-doc build
- new version
- bump major numbers
- add ebackend package
- new version
- drop patch 1
- update license
- fix buildrequires
- new version
- patch to fix linking
- new version
- rebuild for missing package on x86_64
- new version
- drop patch
- new version
- new version
- libsoup rebuild
- new version
- new version
- new camel major
- bump deps
- new version
- new version
- drop patch
- patch to fix bug #36319
- rebuild for db 4.6
- new version
- new version
- new version
- new version
- new base version
- add package for libgdata
- new version
- drop patch 2
- new version
- new version
- new version
- new version
- new version
- new devel name
- new version
- new version
- new version
- new version
- new base version
- update patch 1
- drop patch 3
- new version
- drop merged patches
- new version
- drop patch 0

  + mandrake <mandrake@mandriva.com>
    - %repsys markrelease
      version: 2.32.3
      release: 3
      revision: 705835
      Copying 2.32.3-3 to releases/ directory.

  + Oden Eriksson <oeriksson@mandriva.com>
    - avoid pulling 32 bit libraries on 64 bit arch
    - rebuilt against openssl-0.9.8m
    - rebuild
    - try to unbork stuff with the mozilla lib deps

  + Funda Wang <fwang@mandriva.org>
    - clean up BRs
    - build with db 5.1
    - fix build with gtk 2.24
    - rebuild for update libsoup libtool archive
    - now build correctly with our default link flags
    - rebuild

  + Frederic Crozat <fcrozat@mandriva.com>
    - Release 2.30.2.1
    - Remove patch1 (merged upstream)
    - Patch0 (GIT): revert invalid fix (GNOME bug #619347)
    - Release 2.30.2
    - Remove patch1 (merged upstream)
    - Update patch1 with many fixes from upstream GIT
    - Patch1 (GIT): various GIT fixes
    - Fix BR
    - Release 2.28.1
    - Patch1 (SVN): various bug fixes from SVN
    - Release 2.23.90.1
    - Release 2.23.90
    - Don't package changelog, package NEWS, more informative
    - disable over/under linking checks for now, Makefile.am patch prevent build
    - Patch1 : various IMAP bug fixes from SVN
    - Patch0: various fixes from SVN
    - Remove patch1, it was merged upstream
    - Patch2: fix e-d-s leak (GNOME bug #420167)
    - Patch4 (SVN): fix APOP vulnerability (CVE 2007-1558)

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild so that shared libraries are properly stripped again

  + Adam Williamson <awilliamson@mandriva.org>
    - rebuild for xcb changes

  + Pascal Terjan <pterjan@mandriva.org>
    - Upstream patch for a crash on startup (Upstream #544049)
    - Fix a crash when using timezones which do not include a TZNAME (GNOME bug #425129)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags

