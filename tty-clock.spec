######################################################
# SpecFile: tty-clock.spec 
# Generato: http://www.mandrivausers.ro/
# MRB-Falticska Florin
######################################################
#empty debug 
%define debug_package	%{nil}

Summary:	Simple console clock
Name:		tty-clock
Version:	0.1
Release:	3
License:	GPLv2+
Group:		Shells
URL:		http://github.com/xorg62/tty-clock
Source0:	https://github.com/xorg62/tty-clock/archive/v0.1.tar.gz
BuildRequires:	pkgconfig(ncurses)
Requires:	ncurses

%description
An analog clock in ncurses

%prep
%setup -q 
chmod -x README

%build
%{make} 

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/

%files
%doc README
%{_bindir}/*





