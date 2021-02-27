#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	API reference documentation generator for FreeType
Summary(pl.UTF-8):	Generator dokumentacji referencyjnej API do biblioteki FreeType
Name:		python-docwriter
Version:	1.1.1
Release:	4
License:	FreeType
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/docwriter/
Source0:	https://files.pythonhosted.org/packages/source/d/docwriter/docwriter-%{version}.tar.gz
# Source0-md5:	b02be7127b31966f761af9798168155f
Patch0:		%{name}-requirements.patch
URL:		https://github.com/freetype/docwriter
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-PyYAML >= 5.1
BuildRequires:	python-mistune >= 0.8.4
BuildRequires:	python-mkdocs >= 1.0.4
BuildRequires:	python-mkdocs-material >= 4.0.2
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-PyYAML >= 5.1
BuildRequires:	python3-mistune >= 0.8.4
BuildRequires:	python3-mkdocs >= 1.0.4
BuildRequires:	python3-mkdocs-material >= 4.0.2
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Docwriter is an API documentation generator for the FreeType Library
that extracts and builds Markdown docs from the FreeType header files.

%description -l pl.UTF-8
Docwriter to generator dokumentacji API dla biblioteki FreeType,
wydobywający i tworzący dokumentację Markdown z plików nagłówkowych
FreeType.

%package -n python3-docwriter
Summary:	API reference documentation generator for FreeType
Summary(pl.UTF-8):	Generator dokumentacji referencyjnej API do biblioteki FreeType
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-docwriter
Docwriter is an API documentation generator for the FreeType Library
that extracts and builds Markdown docs from the FreeType header files.

%description -n python3-docwriter -l pl.UTF-8
Docwriter to generator dokumentacji API dla biblioteki FreeType,
wydobywający i tworzący dokumentację Markdown z plików nagłówkowych
FreeType.

%prep
%setup -q -n docwriter-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/docwriter
%{py_sitescriptdir}/docwriter-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-docwriter
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/docwriter
%{py3_sitescriptdir}/docwriter-%{version}-py*.egg-info
%endif
