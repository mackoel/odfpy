%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:		odfpy
Version:	0.9
Release:	3%{?dist}
Summary:	Python library for manipulating OpenDocument files

Group:		Development/Languages
License:	GPLv2+
URL:		http://forge.osor.eu/projects/odfpy/
# This changes every time, most recent downloads are at http://forge.osor.eu/frs/?group_id=33
# Source0:	http://forge.osor.eu/frs/download.php/286/odfpy-0.9.tar.gz
# Uploaded to github to be able to get anonymously from koji
# Source0:      https://github.com/mackoel/odfpy/blob/master/odfpy-0.9.tar.gz
Source0:      %{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
BuildRequires:	python-devel python-setuptools

%description
Odfpy aims to be a complete API for OpenDocument in Python. Unlike
other more convenient APIs, this one is essentially an abstraction
layer just above the XML format. The main focus has been to prevent
the programmer from creating invalid documents. It has checks that
raise an exception if the programmer adds an invalid element, adds an
attribute unknown to the grammar, forgets to add a required attribute
or adds text to an element that doesn't allow it.
 
These checks and the API itself were generated from the RelaxNG
schema, and then hand-edited. Therefore the API is complete and can
handle all ODF constructions, but could be improved in its
understanding of data types.


%prep
%setup -q


%build
CFLAGS="%{optflags}" %{__python} -c 'import setuptools; execfile("setup.py")' build


%install
rm -rf %{buildroot}
%{__python} -c 'import setuptools; execfile("setup.py")' install --skip-build --root %{buildroot}
sed -i '/#!\/usr\/bin\/python/d' %{buildroot}%{python_sitelib}/odf/*.py

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%docdir examples
%docdir contrib
%{_bindir}/*
%{_mandir}/man1/*
%{python_sitelib}/*egg-info
%{python_sitelib}/odf


%changelog
* Sat Mar 10 2012 Kozlov Konstantin <mackoel@gmail.com> - 0.9-3
- Uploaded tarball to github to be able to get anonymously from koji

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 20 2009 Ian Weller <ianweller@gmail.com> - 0.9-1
- Update upstream

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.8-2
- Rebuild for Python 2.6

* Fri Aug 22 2008 Ian Weller <ianweller@gmail.com> 0.8-1
- Update upstream

* Tue Jul 15 2008 Ian Weller <ianweller@gmail.com> 0.7-2
- Change macros
- Remove license file

* Sun Jul 13 2008 Ian Weller <ianweller@gmail.com> 0.7-1
- Add COPYING file
- Use setuptools instead
- sed out shebangs from module files
- Other minor fixes

* Sun Jul 13 2008 Paul W. Frields <stickster@gmail.com> - 0.7-0.1
- Initial RPM package
