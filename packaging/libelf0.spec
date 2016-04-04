Name:           libelf0
Version:        0.8.13
Release:        0
License:        LGPL-2.1+
Summary:        An ELF Object File Access Library
Url:            http://www.mr511.de/software/
Group:          System/Libraries
Source:         libelf-%{version}.tar.bz2
Source2:        baselibs.conf
Source1001: 	libelf0.manifest
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The libelf package contains a library for accessing ELF object files.
Libelf allows you to access the internals of the ELF object file
format, so you can see the different sections of an ELF file.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel,
Conflicts:      libelf1-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q -n libelf-%{version}
cp %{SOURCE1001} .

%build
export CFLAGS+=" -fvisibility=hidden"
  export CXXFLAGS+=" -fvisibility=hidden"
  
%configure --disable-nls
make %{?_smp_mflags}

%install
make install instroot=%{buildroot}
# remove the wrapper includes
rm -f %{buildroot}%{_includedir}/*.h
# remove unneeded *.la and *.a files
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING.LIB 
%{_libdir}/libelf.so.*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libelf.so
%{_libdir}/libelf.a
%{_libdir}/pkgconfig/libelf.pc
%{_includedir}/libelf

%changelog
