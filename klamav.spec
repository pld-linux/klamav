# TODO
#  - This package contails also unpackaged dazuko-2.0.4 (should be separate kernel-* package?)
#  - kde html docs are empty
#

%define	_klammail_ver 0.06

Summary:	ClamAV Anti-Virus protection for the KDE desktop
Summary(ru_RU.KOI8-R): KDE-ÏÂÏÌÏÞËÁ ÄÌÑ ÁÎÔÉ×ÉÒÕÓÎÏÇÏ ÓËÁÎÅÒÁ Clam AntiVirus
Summary(pl):	Antywirus ClamAV dla ¶rodowiska KDE
Name:		klamav
Version:	0.09
Release:	1.11
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/klamav/%{name}-%{version}.tar.bz2
# Source0-md5:	cef953c99117da0986c28554c3043dd9
Patch0:		%{name}-paths.patch
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
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
cp -f /usr/share/automake/config.sub src/klammail-%{_klammail_ver}
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}

%{__make}

cd src/klammail-%{_klammail_ver}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_bindir},%{_desktopdir}}

install src/*.desktop	       $RPM_BUILD_ROOT%{_desktopdir}

sed -i -e '
/Terminal=0/{
s/.*/Terminal=false/
a\
Categories=Qt;KDE;Utility;
}

' $RPM_BUILD_ROOT%{_desktopdir}/klamav.desktop

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

cd src/klammail-%{_klammail_ver}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_iconsdir}/*/*/*/*.png
