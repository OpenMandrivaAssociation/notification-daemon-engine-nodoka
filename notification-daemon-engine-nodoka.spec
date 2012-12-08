Name:		notification-daemon-engine-nodoka
Version:	0.1.0
Release:	7
Summary:	The Nodoka theme engine for the notification daemon

Group:		System/X11
License:	GPLv3+
URL:		https://nodoka.fedorahosted.org/
Source0:	https://fedorahosted.org/releases/n/o/nodoka/notification-daemon-engine-nodoka-%{version}.tar.gz
Patch0:		notification-daemon-engine-nodoka-clipping.patch
Patch1:		notification-daemon-engine-nodoka-0.1.0-version-check.patch
Patch2:		notification-daemon-engine-nodoka-rtl.patch
Patch3:		notification-daemon-engine-nodoka-base-color.patch
# drop libsexy dep
Patch4:		sexy.patch
Patch5:		notification-daemon-engine-nodoka-window-type.patch
Patch6:		notification-daemon-engine-nodoka-0.1.0-automake.patch

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	autoconf automake libtool
Requires:	notification-daemon

%description
The Nodoka theme engine for the notification daemon.

%prep
%setup -q
%patch0 -p1 -b .clipping
%patch1 -p1 -b .version-check
%patch2 -p1 -b .rtl
%patch3 -p1 -b .base-color
%patch4 -p1 -b .sexy
%patch5 -p1 -b .window-type
%patch6 -p1 -b .automake

autoreconf -fi

%build
%configure2_5x
%make

%install
%makeinstall_std

#remove .la files
find %{buildroot} -name *.la | xargs rm -f || true

%files
%doc AUTHORS ChangeLog COPYING Credits NEWS README
%{_libdir}/notification-daemon-1.0/engines/libnodoka.so

%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-4mdv2011.0
+ Revision: 666621
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-3mdv2011.0
+ Revision: 606825
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-2mdv2010.1
+ Revision: 523442
- rebuilt for 2010.1

* Fri Sep 25 2009 Frederic Crozat <fcrozat@mandriva.com> 0.1.0-1mdv2010.0
+ Revision: 448825
- import notification-daemon-engine-nodoka

