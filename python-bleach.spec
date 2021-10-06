%global srcname bleach

Name:           python-%{srcname}
Version:        4.1.0
Release:        1
Summary:        An easy whitelist-based HTML-sanitizing tool
Group:          Development/Python
License:        ASL 2.0
URL:            http://github.com/jsocol/bleach
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Bleach is an HTML sanitizing library that escapes or strips markup and
attributes based on a white list.


%package -n python3-%{srcname}
Summary:        An easy whitelist-based HTML-sanitizing tool
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(html5lib)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Bleach is an HTML sanitizing library that escapes or strips markup and
attributes based on a white list.

%prep
%autosetup -n %{srcname}-%{version} -p1

# drop bundled egg-info
rm -rf *.egg-info

# Needed if we ever package python-pytest-runner...
sed -i 's/pytest-runner>=2.0,<3dev/pytest-runner/' setup.py

# Remove vendored libraries which were added for https://github.com/mozilla/bleach/issues/386
rm -r bleach/_vendor/
# Bleach has a shim layer that references the vendored html5lib we just deleted.
# Let's patch up the imports to use the real html5lib.
sed -i "s/bleach._vendor.html5lib/html5lib/g" bleach/html5lib_shim.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

