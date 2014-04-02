######################################################
# SpecFile: tty-clock.spec 
# Generato: http://www.mandrivausers.ro/
# MRB-Falticska Florin
######################################################
#empty debug 
%define debug_package	%{nil}
%define oname xorg62-tty-clock-a82fd71
Summary:	Simple console clock
Name:		tty-clock
Version:	0.1
Release:	1
License:	GPLv2+
Group:		Shells
URL:		http://github.com/xorg62/tty-clock
Source0:	https://github.com/xorg62/tty-clock/%{oname}.tar.gz
BuildRequires:	ncurses-devel
Requires:	ncurses

%description
An analog clock in ncurses

%prep
%setup -q -n %{oname}


%build
%{make} 

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/

%files
%doc README
%{_bindir}/*


%changelog




