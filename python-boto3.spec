#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	AWS SDK for Python 2
Summary(pl.UTF-8):	AWS SDK dla Pythona 2
Name:		python-boto3
Version:	1.17.1
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/boto3/
Source0:	https://files.pythonhosted.org/packages/source/b/boto3/boto3-%{version}.tar.gz
# Source0-md5:	a9436d49cf4a931327aebff158d72533
URL:		https://pypi.org/project/boto3/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-botocore >= 1.20.1
BuildRequires:	python-jmespath >= 0.7.1
BuildRequires:	python-mock >= 1.3.0
BuildRequires:	python-nose >= 1.3.3
BuildRequires:	python-s3transfer >= 0.3.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-botocore >= 1.20.1
BuildRequires:	python3-jmespath >= 0.7.1
BuildRequires:	python3-nose >= 1.3.3
BuildRequires:	python3-s3transfer >= 0.3.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK)
for Python, which allows Python developers to write software that
makes use of services like Amazon S3 and Amazon EC2.

%description -l pl.UTF-8
Boto3 to pakiet programistyczny (SDK) usług AWS (Amazon Web Services),
pozwalający na pisanie w Pythonie oprogramowania wykorzystującego
usługi takie jak Amazon S3 i Amazon EC2.

%package -n python3-boto3
Summary:	AWS SDK for Python 3
Summary(pl.UTF-8):	AWS SDK dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-boto3
Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK)
for Python, which allows Python developers to write software that
makes use of services like Amazon S3 and Amazon EC2.

%description -n python3-boto3 -l pl.UTF-8
Boto3 to pakiet programistyczny (SDK) usług AWS (Amazon Web Services),
pozwalający na pisanie w Pythonie oprogramowania wykorzystującego
usługi takie jak Amazon S3 i Amazon EC2.

%prep
%setup -q -n boto3-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver} tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} tests
%endif
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
%doc README.rst
%{py_sitescriptdir}/boto3
%{py_sitescriptdir}/boto3-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-boto3
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/boto3
%{py3_sitescriptdir}/boto3-%{version}-py*.egg-info
%endif
