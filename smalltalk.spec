%define	name	smalltalk
%define	version	2.3.3
%define	release	%mkrel 3

Summary:	Smalltalk free language implementation
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL & LGPL
Group:		Development/Other
Source0:	ftp://ftp.gnu.org/gnu/smalltalk/%{name}-%{version}.tar.bz2
#Patch0:		smalltalk-amd64.patch
Patch1:		smalltalk-proc.patch
URL:		http://www.smalltalk.org/
BuildRequires:	gtk+2-devel termcap-devel emacs-bin
BuildRequires:	tcl tcl-devel tk tk-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GNU Smalltalk is a Free (or Open Source) implementation that closely 
follows the Smalltalk-80 language as described in the book Smalltalk-80: 
the Language and its Implementation by Adele Goldberg and David          
Robson. GNUSmalltalk runs on most versions of Unix or Unix like 
systems (GNU/Linux, FreeBSD, etc...).        
There is even a version for commercial operating systems like MS-NT.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1

%build
%configure2_5x	
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/gst-config

%post
%_install_info gst.info

%preun
%_remove_install_info gst.info

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog NEWS README
%{_bindir}/*
%multiarch %{multiarch_bindir}/gst-config
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/emacs/site-lisp/*
%{_datadir}/aclocal/*
%{_libdir}/*
%{_includedir}/*
%{_infodir}/*.info*
%{_mandir}/man1/*


