# TODO
#  - kde html docs are empty
#  - build on amd64 fails
#

%define	_klammail_ver 0.06

Summary:	ClamAV Anti-Virus protection for the KDE desktop
Summary(ru_RU.KOI8-R):KDE-ÏÂÏÌÏÞËÁ ÄÌÑ ÁÎÔÉ×ÉÒÕÓÎÏÇÏ ÓËÁÎÅÒÁ Clam AntiVirus
Summary(pl):	Antywirus ClamAV dla ¶rodowiska KDE
Name:		klamav
Version:	0.20
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/klamav/%{name}-%{version}.tar.bz2
# Source0-md5:	f6da1399191be7019351bd603a5d12f3
Patch0:		%{name}-paths.patch
Patch1:		%{name}-desktop.patch
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
#%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
cp -f /usr/share/automake/config.sub src/klammail
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

install src/*.desktop	       $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

#cd src/klammail
#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_iconsdir}/*/*/*/*.png
