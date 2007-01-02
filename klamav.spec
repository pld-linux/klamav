# TODO
#  - kde html docs are empty
#
Summary:	ClamAV Anti-Virus protection for the KDE desktop
Summary(pl):	Antywirus ClamAV dla ¶rodowiska KDE
Summary(ru):	KDE-ÏÂÏÌÏÞËÁ ÄÌÑ ÁÎÔÉ×ÉÒÕÓÎÏÇÏ ÓËÁÎÅÒÁ Clam AntiVirus
Name:		klamav
Version:	0.38
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/klamav/%{name}-%{version}.tar.bz2
# Source0-md5:	396af3834145e4413a4d207857d86f47
Patch0:		%{name}-desktop.patch
URL:		http://klamav.sourceforge.net/
BuildRequires:	automake
BuildRequires:	clamav-devel
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

%description -l pl
Antywirus ClamAV dla ¶rodowiska KDE. Zawiera:
- skanowanie przy dostêpie
- rêczne skanowanie
- obs³ugê kwarantanny
- ¶ci±ganie uaktualnieñ
- skanowanie poczty (KMail/Evolution).

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_datadir}/apps/%{name}
%{_datadir}/apps/konqueror/servicemenus/klamav-dropdown.desktop
%{_datadir}/config.kcfg/*
