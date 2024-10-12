%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
#define git 20240222
%define gitbranch Plasma/6.1
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary: Volume manager plasmoid
Name: plasma6-pa
Version: 6.2.0
Release: %{?git:0.%{git}.}1
License: GPLv2+
Group: Graphical desktop/KDE
Url: http://www.kde.org
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/plasma-pa/-/archive/%{gitbranch}/plasma-pa-%{gitbranchd}.tar.bz2#/plasma-pa-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/plasma-pa-%{version}.tar.xz
%endif
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(Plasma) >= 5.90.0
BuildRequires: cmake(PlasmaQuick)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Svg)
BuildRequires: cmake(KF6PulseAudioQt)
BuildRequires: sound-theme-freedesktop
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: gettext
BuildConflicts: pkgconfig(gconf-2.0)
Requires: pulseaudio
Requires: sound-theme-freedesktop
Recommends: pulseaudio-module-gsettings
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Volume manager plasmoid.

%files -f %{name}.lang
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_pulseaudio.so
%{_datadir}/applications/kcm_pulseaudio.desktop
%{_qtdir}/qml/org/kde/plasma/private/volume
%{_datadir}/metainfo/org.kde.plasma.volume.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.volume
%{_libdir}/libplasma-volume.so*
%{_qtdir}/plugins/kf6/kded/audioshortcutsservice.so
