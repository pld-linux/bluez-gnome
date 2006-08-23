Summary:	Bluetooth PIN manager for GNOME
Summary(pl):	Zarz±dca kodów PIN dla Bluetooth
Name:		bluez-gnome
Version:	0.2
Release:	1
License:	GPL
Group:		Applications
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	36e9b25d4afa841950afb0676ff376d5
URL:		http://bluez.sourceforge.net/
BuildRequires:	dbus-glib-devel >= 0.50
BuildRequires:	gtk+2-devel >= 1:2.0.0
Obsoletes:		bluez-pin
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
