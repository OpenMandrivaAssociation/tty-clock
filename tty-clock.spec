######################################################
# SpecFile: tty-clock.spec 
# Generato: http://www.mandrivausers.ro/
# MRB-Falticska Florin
######################################################
%define use_ccache	1
%define ccachedir	~/.ccache-OOo%{mdvsuffix}
%{?_with_ccache: %global use_ccache 1}
%{?_without_ccache: %global use_ccache 0}
%define  distsuffix	mrb
%define debug_package	%{nil}
Vendor:		MandrivaUsers.Ro <http://www.mandrivausers.ro/>
Packager:	Falticska Florin <symbianflo@fastwebnet.it>
########################################################

%define oname xorg62-tty-clock-a82fd71
Summary:	Simple console clock
Name:		tty-clock
Version:	0.0
Release:	%mkrel 69
License:	GPLv2+
Group:		System Environment/Shells
URL:		http://github.com/xorg62/tty-clock
Source0:	https://github.com/xorg62/tty-clock/%{oname}.tar.gz
BuildRequires:	ncurses-devel
Requires:	ncurses
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
An analog clock in ncurses

%prep
%setup -q -n %{oname}


%build
%{make} 

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*


%changelog
* Sun Nov 23 2010 Falticska Florin <symbianflo@fastwebnet.it> 0.0-69mrb2010.1
- New porting for MRB
- MRB-Mandriva Users.Ro



