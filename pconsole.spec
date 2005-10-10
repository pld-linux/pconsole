Summary:	Administrative tool for working with clusters of machines
Summary(pl):	Narzêdzie administracyjne do pracy z klastrami maszyn
Name:		pconsole
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		Networking
Source0:	http://www.xs4all.nl/~walterj/pconsole/%{name}-%{version}.tar.gz
# Source0-md5:	b0a170284c3272e2e403fc8f2ccfdd53
URL:		http://www.heiho.net/pconsole/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pconsole allows you to connect to each node of your cluster
simultaneously, and you can type your administrative commands in a
specialized window that 'multiplies' the input to each to the
connections you have opened.

pconsole is best run from within X Window System, although it is
possible to employ it without X (in console mode) as well.

You need to install pconsole on only 1 machine in the cluster, this
would usually be your central administrative node.

%description -l pl
pconsole umo¿liwia po³±czenie siê z ka¿dym wêz³em klastra jednocze¶nie
i pisanie poleceñ administracyjnych w specjalnym oknie
"zwielokrotniaj±cym" wej¶cie na ka¿de otwarte po³±czenie.

pconsole najlepiej uruchamiaæ z poziomu X Window System, choæ mo¿liwe
jest tak¿e uruchomienie go bez X (w trybie konsolowym).

Wystarczy zainstalowaæ pconsole na tylko jednej maszynie w klastrze,
zazwyczaj robi siê to na centralnym, administracyjnym wê¼le.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install pconsole pconsole.sh ssh.sh $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.pconsole
%attr(4755,root,root) %{_bindir}/*
