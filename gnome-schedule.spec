Summary:	GNOME scheduler
Name:		gnome-schedule
Version:	0.9.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-schedule/%{name}-%{version}.tar.bz2
# Source0-md5:	08c3f7680fe95fc4088289ed25552618
Patch0:		%{name}-pyc.patch
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libgnomeui-devel >= 2.6.0
%pyrequires_eq  python-modules
BuildRequires:  python
Requires:	yelp
Requires:	crondaemon
Requires:	at
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome-schedule is a GNOME GUI for configuring a users crontab. It was
made for Vixie cron whom comes with Fedora Linux, but should work with
other cron servers aswell if the format of the config file is similar.

%prep
%setup  -q
%patch0 -p1

%build
%configure \
	GNOMEHELP_CONFIG=/usr/bin/gnome-help \
	CRONTAB_CONFIG=/usr/bin/crontab \
	AT_CONFIG=/usr/bin/at \
	ATQ_CONFIG=/usr/bin/atq \
	ATRM_CONFIG=/usr/bin/atrm \
	BATCH_CONFIG=/usr/bin/batch \
	PYTHON_CONFIG=/usr/bin/python

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/*.py

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py[oc]
%{_datadir}/%{name}/*.glade
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
