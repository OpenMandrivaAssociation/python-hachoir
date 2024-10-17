%define module_name hachoir

Summary:    Python library to edit binary file and metadata
Name: 		python-%{module_name}
Version: 	0.5.2
Release: 	4
Source0: 	%{module_name}-%{version}.tar.bz2
License:	GPL
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Url: 		https://hachoir.org/
BuildArch:  noarch
Requires:   python-urwid
BuildRequires: python

%description
Hachoir is a library written in Python which allows to see and edit a binary 
file (or any binary stream) field per field. 
A field is the most basic information: a number, a string of characters, 
a flag (yes/no), etc. Only supported formats can be opened, it's not a magic 
tool.
 
It can be used to extract some informations (eg. metadata), edit some fields 
of a file without original program, or convert a file from a format to another.
%prep
%setup -q -n %{module_name}-%version

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING BUGS  README INSTALL TODO
%doc doc/*
%{_bindir}/*
%py_puresitedir/*


%changelog
* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 0.5.2-3mdv2011.0
+ Revision: 593096
- fix file list

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.5.2-3mdv2010.0
+ Revision: 430846
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.5.2-2mdv2009.0
+ Revision: 222650
- buildrequires python-devel instead of python
- BuildRequires python for distutils/core
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Aug 23 2006 Michael Scherer <misc@mandriva.org> 0.5.2-1mdv2007.0
- First package

