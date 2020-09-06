Summary:	Thumbnailer for Krita and MyPaint images
Summary(pl.UTF-8):	Generator miniaturek do obrazów Krity i MyPainta
Name:		gnome-kra-ora-thumbnailer
Version:	1.4
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-kra-ora-thumbnailer/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	c94923893dd4d0a2c0ebea6c5bbdb806
URL:		https://gitlab.gnome.org/GNOME/gnome-kra-ora-thumbnailer
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libarchive-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thumbnailer for Krita and MyPaint images.

%description -l pl.UTF-8
Generator miniaturek do obrazów Krity i MyPainta.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-kra-thumbnailer
%attr(755,root,root) %{_bindir}/gnome-openraster-thumbnailer
%{_datadir}/thumbnailers/gnome-kra-thumbnailer.thumbnailer
%{_datadir}/thumbnailers/gnome-openraster-thumbnailer.thumbnailer
