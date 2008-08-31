# TODO locale file
Summary:	Bluetooth PIN manager for GNOME
Summary(pl.UTF-8):	Zarządca kodów PIN Bluetootha dla GNOME
Name:		bluez-gnome
Version:	1.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
#Source0Download: http://www.bluez.org/download.html
Source0:	http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.gz
# Source0-md5:	645fdd6bc201fc54984da87cbefe3f70
URL:		http://www.bluez.org/
BuildRequires:	GConf2-devel >= 2.6
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	hal-devel >= 0.5.8
BuildRequires:	libnotify-devel >= 0.3.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,preun):	GConf2 >= 2.6
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires:	dbus-glib >= 0.60
Requires:	gtk+2 >= 2:2.10.0
Requires:	obex-data-server >= 0.3
Suggests:	gnome-vfs-obexftp
Obsoletes:	bluez-pin
Obsoletes:	gnome-bluetooth
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple program which takes care of the PIN numbers used
to pair Bluetooth devices. When a PIN is required for either an
incoming or outgoing connection, it pops up a window to allow the code
to be entered. PINs can optionally be saved in a persistent database,
for use with dumb devices that are unable to remember pairing
information across sessions.

%description -l pl.UTF-8
Bardzo prosty program pilnujący numerów PIN używanych do parowania
urządzeń Bluetooth. Kiedy wymagany jest PIN dla przychodzącego lub
wychodzącego połączenia, pokazuje okienko umożliwiające wprowadzenie
kodu. PIN-y opcjonalnie mogą być przechowywane w bazie danych do
używania z prymitywnymi urządzeniami nie potrafiącymi zapamiętać
informacji o parowaniu między sesjami.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-desktop-update \
	--disable-mime-update
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	autostartdir=%{_sysconfdir}/xdg/autostart

# error: bluez-gnome-0.28-1: req /usr/share/locale/mus/LC_MESSAGES not found
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/mus/LC_MESSAGES

%find_lang bluetooth-manager

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install bluetooth-manager.schemas
%update_mime_database
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall bluetooth-manager.schemas

%postun
%update_mime_database
%update_icon_cache hicolor

%files -f bluetooth-manager.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/bluetooth-analyzer
%attr(755,root,root) %{_bindir}/bluetooth-applet
%attr(755,root,root) %{_bindir}/bluetooth-properties
%attr(755,root,root) %{_bindir}/bluetooth-sendto
%attr(755,root,root) %{_bindir}/bluetooth-wizard
%{_sysconfdir}/xdg/autostart/bluetooth-applet.desktop
%{_desktopdir}/bluetooth-properties.desktop
%{_sysconfdir}/gconf/schemas/bluetooth-manager.schemas
%{_mandir}/man1/bluetooth-analyzer.1*
%{_mandir}/man1/bluetooth-applet.1*
%{_mandir}/man1/bluetooth-properties.1*
%{_mandir}/man1/bluetooth-sendto.1*
%{_mandir}/man1/bluetooth-wizard.1*
%{_desktopdir}/bluetooth-analyzer.desktop
%{_datadir}/mime/packages/*.xml
%{_iconsdir}/hicolor/*/apps/bluetooth.png
%{_iconsdir}/hicolor/*/apps/bluetooth.svg
