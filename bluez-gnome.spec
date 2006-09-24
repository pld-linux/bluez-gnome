Summary:	Bluetooth PIN manager for GNOME
Summary(pl):	Zarz±dca kodów PIN Bluetootha dla GNOME
Name:		bluez-gnome
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Applications
#Source0Download: http://www.bluez.org/download.html
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	fbb04989c550bfbcf284d1744ff23f6a
URL:		http://www.bluez.org/
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	gtk+2-devel >= 2:2.10.0
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

%description -l pl
Bardzo prosty program pilnuj±cy numerów PIN u¿ywanych do parowania
urz±dzeñ Bluetooth. Kiedy wymagany jest PIN dla przychodz±cego lub
wychodz±cego po³±czenia, pokazuje okienko umo¿liwiaj±ce wprowadzenie
kodu. PIN-y opcjonalnie mog± byæ przechowywane w bazie danych do
u¿ywania z prymitywnymi urz±dzeniami nie potrafi±cymi zapamiêtaæ
informacji o parowaniu miêdzy sesjami.

%prep
%setup -q

%build
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
%attr(755,root,root) %{_bindir}/bt-applet
%{_datadir}/gnome/autostart/bt-applet.desktop
