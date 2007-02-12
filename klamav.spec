# TODO
#  - kde html docs are empty
#
Summary:	ClamAV Anti-Virus protection for the KDE desktop
Summary(pl.UTF-8):   Antywirus ClamAV dla środowiska KDE
Summary(ru.UTF-8):   KDE-оболочка для антивирусного сканера Clam AntiVirus
Name:		klamav
Version:	0.40
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/klamav/%{name}-%{version}-source.tar.gz
# Source0-md5:	65818ece1115848602c87ab878784fea
Patch0:		%{name}-desktop.patch
URL:		http://klamav.sourceforge.net/
BuildRequires:	automake
BuildRequires:	clamav-devel >= 0.90-0.rc2.1
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClamAV Anti-Virus protection for the KDE desktop. It includes:
- 'On Access' Scanning
- Manual Scanning
- Quarantine Management
- Downloading Updates
- Mail Scanning (KMail/Evolution)

%description -l pl.UTF-8
Antywirus ClamAV dla środowiska KDE. Zawiera:
- skanowanie przy dostępie
- ręczne skanowanie
- obsługę kwarantanny
- ściąganie uaktualnień
- skanowanie poczty (KMail/Evolution).

%prep
%setup -q -n %{name}-%{version}-source
#%patch0 -p1

%build
cd %{name}-%{version}
cp -f /usr/share/automake/config.sub admin
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
cd %{name}-%{version}
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_bindir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}
mv $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/klamav.desktop $RPM_BUILD_ROOT%{_desktopdir}
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}/%{name}.lang
%defattr(644,root,root,755)
%doc %{name}-%{version}/AUTHORS %{name}-%{version}/ChangeLog %{name}-%{version}/INSTALL %{name}-%{version}/NEWS %{name}-%{version}/README %{name}-%{version}/TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_datadir}/apps/%{name}
%{_datadir}/apps/konqueror/servicemenus/klamav-dropdown.desktop
%{_datadir}/config.kcfg/*
