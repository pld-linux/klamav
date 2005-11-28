# TODO
#  - kde html docs are empty
#
Summary:	ClamAV Anti-Virus protection for the KDE desktop
Summary(ru_RU.KOI8-R):KDE-ÏÂÏÌÏÞËÁ ÄÌÑ ÁÎÔÉ×ÉÒÕÓÎÏÇÏ ÓËÁÎÅÒÁ Clam AntiVirus
Summary(pl):	Antywirus ClamAV dla ¶rodowiska KDE
Name:		klamav
Version:	0.32
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/klamav/%{name}-%{version}.tar.bz2
# Source0-md5:	f0226c6b2f64f2e9d2c4099b1812fdb6
Patch0:		%{name}-desktop.patch
URL:		http://klamav.sourceforge.net/
BuildRequires:	automake
BuildRequires:	clamav-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	clamav
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClamAV Anti-Virus protection for the KDE desktop. Includes:
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
cd %{name}-%{version}
%patch0 -p1

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
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_bindir},%{_desktopdir}}

cd %{name}-%{version}

install src/*.desktop	       $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}/%{name}.lang
%defattr(644,root,root,755)
%doc %{name}-%{version}/{AUTHORS,ChangeLog,INSTALL,NEWS,README,TODO}
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_iconsdir}/hicolor/*/*/*.png
