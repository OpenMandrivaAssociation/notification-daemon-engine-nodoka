Name:           notification-daemon-engine-nodoka
Version:        0.1.0
Release:        %mkrel 4
Summary:        The Nodoka theme engine for the notification daemon

Group:          System/X11
License:        GPLv3+
URL:            https://nodoka.fedorahosted.org/
Source0:        https://fedorahosted.org/releases/n/o/nodoka/notification-daemon-engine-nodoka-%{version}.tar.gz
Patch0:         notification-daemon-engine-nodoka-clipping.patch
Patch1:         notification-daemon-engine-nodoka-0.1.0-version-check.patch
Patch2:         notification-daemon-engine-nodoka-rtl.patch
Patch3:         notification-daemon-engine-nodoka-base-color.patch
# drop libsexy dep
Patch4:		sexy.patch
Patch5:		notification-daemon-engine-nodoka-window-type.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  gtk2-devel >= 2.17.1
BuildRequires:  libxml2-devel
BuildRequires:  autoconf automake libtool
Requires:       notification-daemon

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

autoreconf -i -f

%build
%configure2_5x
%make 


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#remove .la files
find $RPM_BUILD_ROOT -name *.la | xargs rm -f || true


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING Credits NEWS README
%{_libdir}/notification-daemon-1.0/engines/libnodoka.so

