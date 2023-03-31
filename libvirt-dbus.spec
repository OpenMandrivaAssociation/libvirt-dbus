%global system_user libvirtdbus

Name: libvirt-dbus
Version: 1.4.1
Release: 3
Group:	System/Libraries
Summary: libvirt D-Bus API binding
License: LGPLv2+
URL: https://libvirt.org/
Source0: https://libvirt.org/sources/dbus/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libvirt)
BuildRequires: pkgconfig(libvirt-glib-1.0)
BuildRequires: pkgconfig(systemd)
BuildRequires: /usr/bin/pod2man
BuildRequires: meson
BuildRequires: python-docutils

Requires: dbus
Requires: glib2
Requires: polkit

Requires(pre): shadow-utils

%description
This package provides D-Bus API for libvirt

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%pre
getent group %{system_user} >/dev/null || groupadd -r %{system_user}
getent passwd %{system_user} >/dev/null || \
    useradd -r -g %{system_user} -d / -s /sbin/nologin \
    -c "Libvirt D-Bus bridge" %{system_user}
exit 0

%files
%license COPYING
%{_sbindir}/libvirt-dbus
%{_datadir}/dbus-1/services/org.libvirt.service
%{_datadir}/dbus-1/system-services/org.libvirt.service
%{_datadir}/dbus-1/system.d/org.libvirt.conf
%{_datadir}/dbus-1/interfaces/org.libvirt.*.xml
%{_datadir}/polkit-1/rules.d/libvirt-dbus.rules
%{_mandir}/man8/libvirt-dbus.8*
/lib/systemd/system/libvirt-dbus.service
%{_prefix}/lib/systemd/user/libvirt-dbus.service
