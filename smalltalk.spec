%define	name    smalltalk
%define	version	3.0.1
%define	release	%mkrel 2

Summary:	Smalltalk free language implementation
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+ and LGPLv2+ and GFDL
Group:		Development/Other
Source0:	ftp://ftp.gnu.org/gnu/smalltalk/%{name}-%{version}.tar.bz2
# Build against system libsigsegv
Patch0:		smalltalk-3.0.1-sigsegv.patch
# Don't save image at gst-blox startup, otherwise you get a permission denied
# error (patch from Debian)
Patch1:		smalltalk-3.0.1-blox-startup.patch
URL:		http://smalltalk.gnu.org/
BuildRequires:	gtk+2-devel emacs-bin
BuildRequires:	readline-devel termcap-devel
BuildRequires:	tcl tcl-devel tk tk-devel
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel
BuildRequires:	sqlite3-devel
BuildRequires:	texinfo
BuildRequires:	libpq-devel
BuildRequires:	zlib-devel
BuildRequires:	zip
BuildRequires:	libsigsegv-devel
BuildRequires:	ffi-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GNU Smalltalk is a Free (or Open Source) implementation that closely 
follows the Smalltalk-80 language as described in the book Smalltalk-80: 
the Language and its Implementation by Adele Goldberg and David          
Robson. GNUSmalltalk runs on most versions of Unix or Unix like 
systems (GNU/Linux, FreeBSD, etc...).        
There is even a version for commercial operating systems like MS-NT.

%package emacs
Summary:      Smalltalk mode for Emacs
Group:        Development/Other
Requires:     %{name} = %{version}-%{release}
Conflicts:    smalltalk < 3.0.1-1

%description emacs
GNU Smalltalk is a Free (or Open Source) implementation that closely
follows the Smalltalk-80 language as described in the book Smalltalk-80:
the Language and its Implementation by Adele Goldberg and David
Robson. GNUSmalltalk runs on most versions of Unix or Unix like
systems (GNU/Linux, FreeBSD, etc...).
There is even a version for commercial operating systems like MS-NT.

This Package contains the Smalltalk mode for Emacs.

%package devel
Summary:      Development files for GNU Smalltalk
Group:        Development/Other
Requires:     %{name} = %{version}-%{release}
Conflicts:    smalltalk < 3.0.1-2

%description devel
GNU Smalltalk is a Free (or Open Source) implementation that closely
follows the Smalltalk-80 language as described in the book Smalltalk-80:
the Language and its Implementation by Adele Goldberg and David
Robson. GNUSmalltalk runs on most versions of Unix or Unix like
systems (GNU/Linux, FreeBSD, etc...).
There is even a version for commercial operating systems like MS-NT.

This Package contains header files and other stuff provided by
GNU Smalltalk. You will need this package, if you want to extent GNU
Smalltalk with functions written in C.

%prep
%setup -q
%patch0 -p1 -b .sigsegv
%patch1 -p1 -b .blox-startup

%build
autoreconf
%configure --disable-static --with-imagedir=%{_libdir}/%{name}
%make

%install
%{makeinstall_std}

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/gst-config

%post
%_install_info gst.info

%preun
%_remove_install_info gst.info

%files 
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_bindir}/gst
%{_bindir}/gst-blox
%{_bindir}/gst-convert
%{_bindir}/gst-doc
%{_bindir}/gst-load
%{_bindir}/gst-package
%{_bindir}/gst-reload
%{_bindir}/gst-sunit
%multiarch %{multiarch_bindir}/gst-config
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_libdir}/*.so.*
%{_libdir}/smalltalk
%{_infodir}/*.info*
%{_mandir}/man1/*

%files devel                                                                                                                                                                       
%defattr(-,root,root,-)                                                                                                                                                            
%{_bindir}/gst-config                                                                                                                                                              
%{_libdir}/libgst.so                                                                                                                                                               
%{_libdir}/pkgconfig/gnu-smalltalk.pc                                                                                                                                              
%{_datadir}/aclocal/*.m4                                                                                                                                                           
%{_includedir}/gst.h                                                                                                                                                               
%{_includedir}/gstpub.h    
%{_libdir}/*.la

%files emacs
%{_datadir}/emacs/site-lisp/*
