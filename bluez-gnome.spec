Summary:	Bluetooth PIN manager for GNOME
Summary(pl.UTF-8):	Zarządca kodów PIN Bluetootha dla GNOME
Name:		bluez-gnome
Version:	0.6
Release:	1.1
License:	GPL
Group:		X11/Applications
#Source0Download: http://www.bluez.org/download.html
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	54334e3d7af70846eb4916191e46081c
Patch0:		%{name}-as-needed.patch
URL:		http://www.bluez.org/
BuildRequires:	GConf2-devel >= 2.6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libnotify-devel >= 0.3.2
BuildRequires:	pkgconfig
Requires:	dbus-glib >= 0.60
Requires:	gtk+2 >= 2:2.10.0
Obsoletes:	bluez-pin
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
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	autostartdir=%{_datadir}/gnome/autostart

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/bluetooth-applet
%attr(755,root,root) %{_bindir}/bluetooth-properties
%{_datadir}/gnome/autostart/bluetooth-applet.desktop
%{_desktopdir}/bluetooth-properties.desktop
