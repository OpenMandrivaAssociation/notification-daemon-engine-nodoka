Summary:	The Nodoka theme engine for the notification daemon
Name:		notification-daemon-engine-nodoka
Version:	0.1.0
Release:	10
Group:		System/X11
License:	GPLv3+
Url:		https://nodoka.fedorahosted.org/
Source0:	https://fedorahosted.org/releases/n/o/nodoka/notification-daemon-engine-nodoka-%{version}.tar.gz
Patch0:		notification-daemon-engine-nodoka-clipping.patch
Patch1:		notification-daemon-engine-nodoka-0.1.0-version-check.patch
Patch2:		notification-daemon-engine-nodoka-rtl.patch
Patch3:		notification-daemon-engine-nodoka-base-color.patch
# drop libsexy dep
Patch4:		sexy.patch
Patch5:		notification-daemon-engine-nodoka-window-type.patch
Patch6:		notification-daemon-engine-nodoka-0.1.0-automake.patch

BuildRequires:	libtool
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
Requires:	notification-daemon

%description
The Nodoka theme engine for the notification daemon.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING Credits NEWS README
%{_libdir}/notification-daemon-1.0/engines/libnodoka.so

