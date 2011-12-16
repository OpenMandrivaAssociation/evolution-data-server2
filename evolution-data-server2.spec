%define oname evolution-data-server
%define nspr_major 4
%define nss_major 3

%define _requires_exceptions nspr%{nspr_major}\\|plc%{nspr_major}\\|plds%{nspr_major}\\|nss%{nss_major}\\|smime%{nss_major}\\|softokn%{nss_major}\\|ssl%{nss_major}\\|nssutil%{nss_major}

%define version 2.32.3
%define libsoup_version_required 2.3.0
%define api_version 1.2
%define base_version 2.32
%define lib_major 6
%define lib_name %mklibname %{oname} %{lib_major}
%define firefox_version 1.0.1

%define oldmajor 6
%define oldlibname %mklibname %oname %oldmajor

%define oldmajor2006 4
%define oldlibname2006 %mklibname %oname %oldmajor2006

%define camelmajor 19
%define camel_libname %mklibname camel %camelmajor

%define ebookmajor 10
%define ebook_libname %mklibname ebook %ebookmajor

%define ecalmajor 8
%define ecal_libname %mklibname ecal %ecalmajor

%define edatabookmajor 8
%define edatabook_libname %mklibname edata-book %edatabookmajor

%define edatacalmajor 10
%define edatacal_libname %mklibname edata-cal %edatacalmajor

%define edataservermajor 14
%define edataserver_libname %mklibname edataserver %edataservermajor
%define edataserver_libnamedev %mklibname -d edataserver2

%define edataserveruimajor 11
%define edataserverui_libname %mklibname edataserverui %edataserveruimajor

%define egroupwisemajor 13
%define egroupwise_libname %mklibname egroupwise %egroupwisemajor

%define ebackendmajor 0
%define ebackend_libname %mklibname ebackend %ebackendmajor

Name:		evolution-data-server2
Summary:	Evolution Data Server
Version: %version
Release: %mkrel 5
License: 	LGPLv2+
Group:		System/Libraries
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.bz2
Patch0:		evolution-data-server-2.32.3-deprecated.patch
Patch1:		evolution-data-server-2.32.3-fix-linking.patch
URL: 		http://www.gnome.org/projects/evolution/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

BuildRequires: bison flex
BuildRequires: gperf
BuildRequires: gtk-doc docbook-dtd412-xml
BuildRequires: krb5-devel
BuildRequires: libgweather2-devel >= 2.25.4
BuildRequires: libsoup-devel >= %{libsoup_version_required}
BuildRequires: nss-devel >= %{firefox_version}
BuildRequires: nspr-devel >= %{firefox_version}
BuildRequires: gtk+2-devel >= 2.20.0
BuildRequires: libgdata0.6-devel >= 0.6.3
BuildRequires: openldap-devel 
BuildRequires: sqlite3-devel >= 3.5
BuildRequires: libical-devel
BuildRequires: libxml2-devel
BuildRequires: libGConf2-devel GConf2
BuildRequires: libgnome-keyring-devel
BuildRequires: intltool
BuildRequires: db-devel
Conflicts: %oname
Obsoletes: %oldlibname


%description
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{camel_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes: %oldlibname2006

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
Obsoletes: %oldlibname2006

%description -n %{edatabook_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edatacal_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes: %oldlibname2006

%description -n %{edatacal_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserver_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes: %oldlibname2006

%description -n %{edataserver_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserverui_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes: %{_lib}edataserverui4

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
Requires: %camel_libname = %version
Requires: %ebook_libname = %version
Requires: %ecal_libname = %version
Requires: %edatabook_libname = %version
Requires: %edatacal_libname = %version
Requires: %edataserver_libname = %version
Requires: %edataserverui_libname = %version
Requires: %egroupwise_libname = %version
Requires: %ebackend_libname = %version
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides: libedataserver-devel = %version-%release
Requires: nss-devel >= %{firefox_version}
Requires: nspr-devel >= %{firefox_version}
#gw libtool dep:
Requires: libgdata0.6-devel
Obsoletes: %mklibname -d edataserver 9

%description -n %{edataserver_libnamedev}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%prep
%setup -q -n %oname-%version
%apply_patches
autoreconf -fi

%build

%configure2_5x --with-krb5=%{_prefix} --with-krb5-libs=%{_libdir} \
--with-libdb=%{_prefix} \
--with-openldap=yes --with-static-ldap=no --enable-gtk-doc=yes 
#--enable-gnome-keyring=yes
%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall_std


%{find_lang} %{oname}-%{base_version}

rm -f %{buildroot}%{_libdir}/*.la

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT


%files -f %{oname}-%{base_version}.lang
%defattr(-, root, root)
%doc COPYING NEWS
%{_libexecdir}/%{oname}-%{api_version}
%{_libexecdir}/camel-index-control-%{api_version}
%_libexecdir/e-addressbook-factory
%_libexecdir/e-calendar-factory
%attr(2755,root,mail) %{_libexecdir}/camel-lock-helper-%{api_version}
%{_datadir}/%{oname}-%{base_version}
%_datadir/dbus-1/services/org.gnome.evolution.dataserver.AddressBook.service
%_datadir/dbus-1/services/org.gnome.evolution.dataserver.Calendar.service
%{_datadir}/pixmaps/%{oname}

%files -n %{camel_libname}
%defattr(-, root, root)
%{_libdir}/libcamel-%{api_version}.so.%{camelmajor}*
%{_libdir}/libcamel-provider-%{api_version}.so.%{camelmajor}*

%files -n %{ebook_libname}
%defattr(-, root, root)
%{_libdir}/libebook-%{api_version}.so.%{ebookmajor}*

%files -n %{ecal_libname}
%defattr(-, root, root)
%{_libdir}/libecal-%{api_version}.so.%{ecalmajor}*

%files -n %{edatabook_libname}
%defattr(-, root, root)
%{_libdir}/libedata-book-%{api_version}.so.%{edatabookmajor}*

%files -n %{edatacal_libname}
%defattr(-, root, root)
%{_libdir}/libedata-cal-%{api_version}.so.%{edatacalmajor}*

%files -n %{edataserver_libname}
%defattr(-, root, root)
%{_libdir}/libedataserver-%{api_version}.so.%{edataservermajor}*

%files -n %{edataserverui_libname}
%defattr(-, root, root)
%{_libdir}/libedataserverui-%{api_version}.so.%{edataserveruimajor}*

%files -n %{egroupwise_libname}
%defattr(-, root, root)
%{_libdir}/libegroupwise-%{api_version}.so.%{egroupwisemajor}*

%files -n %{ebackend_libname}
%defattr(-, root, root)
%{_libdir}/libebackend-%{api_version}.so.%{ebackendmajor}*

%files -n %{edataserver_libnamedev}
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/%{oname}-%{base_version}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
