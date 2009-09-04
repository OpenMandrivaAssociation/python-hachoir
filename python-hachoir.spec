%define module_name hachoir

Summary:    Python library to edit binary file and metadata
Name: 		python-%{module_name}
Version: 	0.5.2
Release: 	%mkrel 3
Source0: 	%{module_name}-%{version}.tar.bz2
License:	GPL
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Url: 		http://hachoir.org/
BuildArch:  noarch
Requires:   python-urwid
BuildRequires: python-devel

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

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc AUTHORS COPYING BUGS  README INSTALL TODO
%doc doc/* 
%dir %py_puresitedir/%module_name

