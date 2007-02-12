Summary:	Administrative tool for working with clusters of machines
Summary(pl.UTF-8):   Narzędzie administracyjne do pracy z klastrami maszyn
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

%description -l pl.UTF-8
pconsole umożliwia połączenie się z każdym węzłem klastra jednocześnie
i pisanie poleceń administracyjnych w specjalnym oknie
"zwielokrotniającym" wejście na każde otwarte połączenie.

pconsole najlepiej uruchamiać z poziomu X Window System, choć możliwe
jest także uruchomienie go bez X (w trybie konsolowym).

Wystarczy zainstalować pconsole na tylko jednej maszynie w klastrze,
zazwyczaj robi się to na centralnym, administracyjnym węźle.

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
