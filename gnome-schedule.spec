Summary:	GNOME scheduler
Summary(pl.UTF-8):	Narzędzie do planowania dla GNOME
Name:		gnome-schedule
Version:	1.0.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-schedule/%{name}-%{version}.tar.gz
# Source0-md5:	52b179c43135048ede51579a3e048019
Patch0:		%{name}-pyc.patch
BuildRequires:	docbook-dtd42-xml
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libxslt-progs
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-pygtk-devel
BuildRequires:	rarian-compat
BuildRequires:	rpm-pythonprov
%pyrequires_eq  python-modules
Requires:	at
Requires:	crondaemon
Requires:	python
Requires:	yelp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome-schedule is a GNOME GUI for configuring a users crontab. It was
made for Vixie cron which comes with Fedora Linux, but should work
with other cron daemons as well if the format of the config file is
similar.

%description -l pl.UTF-8
Gnome-schedule to graficzny interfejs użytkownika dla GNOME do
konfigurowania crontaba użytkownika. Zostało stworzone dla Vixie crona
przychodzącego z Fedora Linuksem, ale powinien działać z także innymi
demonami cron, o ile mają podobny format pliku konfiguracyjnego.

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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py[oc]
%{_datadir}/%{name}/*.glade
%{_datadir}/%{name}/*.xml
%{_desktopdir}/*.desktop
%{_libdir}/bonobo/servers/*
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/%{name}/%{name}-C.omf
%lang(es) %{_omf_dest_dir}/%{name}/%{name}-es.omf
%{_pixmapsdir}/*.png
