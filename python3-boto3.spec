#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	AWS SDK for Python 2
Summary(pl.UTF-8):	AWS SDK dla Pythona 2
Name:		python3-boto3
Version:	1.42.67
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/boto3/
Source0:	https://files.pythonhosted.org/packages/source/b/boto3/boto3-%{version}.tar.gz
# Source0-md5:	ec6bb40dc706f2c7831f8ddf919e69ee
URL:		https://pypi.org/project/boto3/
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-botocore >= 1.42.67
BuildRequires:	python3-botocore < 1.43
BuildRequires:	python3-jmespath >= 0.7.1
BuildRequires:	python3-jmespath < 2
BuildRequires:	python3-pytest
BuildRequires:	python3-s3transfer >= 0.16.0
BuildRequires:	python3-s3transfer < 0.17
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.9
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

%prep
%setup -q -n boto3-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE README.rst
%{py3_sitescriptdir}/boto3
%{py3_sitescriptdir}/boto3-%{version}-py*.egg-info
