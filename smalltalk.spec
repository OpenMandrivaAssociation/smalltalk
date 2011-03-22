%define	name    smalltalk
%define	version	3.2.4
%define	release	%mkrel 1

Summary:	Smalltalk free language implementation
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+ and LGPLv2+ and GFDL
Group:		Development/Other
Source0:	ftp://ftp.gnu.org/gnu/smalltalk/%{name}-%{version}.tar.xz
# Fix for Tcl 8.6 (interp->result, TIP #330) - AdamW 2008/12
Patch2:		smalltalk-3.1-tcl86.patch
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
BuildRequires:	ffi5-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	mesaglut-devel
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
%patch2 -p1 -b .tcl86

%build
%configure2_5x --disable-static \
           --disable-rpath \
	   --with-tcl=%{_libdir} --with-tk=%{_libdir} \
           --with-system-libsigsegv \
           --with-system-libffi=yes \
           --with-imagedir=%{_libdir}/%{name}
%make

cd doc
for i in gst*;
do
  sed -i -e 's!%{_libdir}!/usr/lib(64)!g' \
         -e 's!/usr/lib!/usr/lib(64)!g' \
         -e 's!/usr/share/smalltalk/kernel!/usr/lib(64)/smalltalk/kernel!g' $i
done

%install
rm -fr %buildroot
%{makeinstall_std}

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/gst-config

%clean
rm -fr %buildroot

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
%{_bindir}/gst-remote
%{_bindir}/gst-sunit
%{_bindir}/gst-browser
%{_bindir}/gst-profile
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_libdir}/*.so.*
%{_libdir}/smalltalk
%{_infodir}/*.info*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_bindir}/gst-config
%multiarch %{multiarch_bindir}/gst-config
%{_libdir}/libgst.so
%{_libdir}/pkgconfig/gnu-smalltalk.pc
%{_datadir}/aclocal/*.m4
%{_includedir}/gst.h
%{_includedir}/gstpub.h
%{_libdir}/*.la

%files emacs
%defattr(-,root,root)
%{_datadir}/emacs/site-lisp/*
%{_sysconfdir}/emacs/site-start.d/**
