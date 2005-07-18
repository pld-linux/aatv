Summary:	TV on text console
Summary(pl):	TV na terminalu
Name:		aatv
Version:	0.3
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/sourceforge/aatv/%{name}-%{version}.tgz
# Source0-md5:	de5ab31c3744e612ed764968dc0c759e
URL:		http://aatv.sourceforge.net/
BuildRequires:	aalib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aatv is a simple program to watch TV in a text-based console.

%description -l pl
aatv to prosty program do ogl±dania telewizji na tekstowej konsoli.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
cp -f /usr/share/automake/config.sub .
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}
install aatv.1 $RPM_BUILD_ROOT%{_mandir}/man1
install aatv.conf $RPM_BUILD_ROOT%{_sysconfdir}
install src/aatv $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
