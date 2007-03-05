# TODO
#  - kde html docs are empty
#
Summary:	ClamAV Anti-Virus protection for the KDE desktop
Summary(pl):	Antywirus ClamAV dla ¶rodowiska KDE
Summary(ru):	KDE-ÏÂÏÌÏÞËÁ ÄÌÑ ÁÎÔÉ×ÉÒÕÓÎÏÇÏ ÓËÁÎÅÒÁ Clam AntiVirus
Name:		klamav
Version:	0.41
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/klamav/%{name}-%{version}-source.tar.gz
# Source0-md5:	4878b88f6b069dcef0f5825f9bca624a
Patch0:		%{name}-desktop.patch
URL:		http://klamav.sourceforge.net/
BuildRequires:	automake
BuildRequires:	clamav-devel >= 0.90
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
