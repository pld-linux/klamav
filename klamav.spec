Summary:	ClamAV Anti-Virus protection for the KDE desktop
Name:		klamav
Version:	0.09
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/klamav/%{name}-%{version}.tar.bz2
# Source0-md5:	cef953c99117da0986c28554c3043dd9
URL:		http://klamav.sourceforge.net/
BuildRequires:	kdelibs-devel
Requires:	clamav
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClamAV Anti-Virus protection for the KDE desktop. Includes :

- 'On Access' Scanning
- Manual Scanning
- Quarantine Management
- Downloading Updates
- Mail Scanning (KMail/Evolution)
- Automated Installation
- ClamAV pre-packaged
- Dazuko pre-packaged

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_bindir},%{_desktopdir}}

install src/*.desktop	       $RPM_BUILD_ROOT%{_desktopdir}
install src/icons/*.png	       $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_desktopdir}/*
%attr(644,root,root) %{_pixmapsdir}/*
