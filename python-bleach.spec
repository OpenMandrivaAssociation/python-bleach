%global srcname bleach

Name:           python-%{srcname}
Version:        4.1.0
Release:        6
Summary:        An easy whitelist-based HTML-sanitizing tool
Group:          Development/Python
License:        ASL 2.0
URL:            https://github.com/jsocol/bleach
Source0:        https://files.pythonhosted.org/packages/source/b/breathe/bleach-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(html5lib)
%{?python_provide:%python_provide python3-%{srcname}}

%description
Bleach is an HTML sanitizing library that escapes or strips markup and
attributes based on a white list.

%prep
%autosetup -n %{srcname}-%{version} -p1

# drop bundled egg-info
rm -rf *.egg-info

# Needed if we ever package python-pytest-runner...
sed -i 's/pytest-runner>=2.0,<3dev/pytest-runner/' setup.py

# Remove vendored libraries which were added for https://github.com/mozilla/bleach/issues/386
#rm -r bleach/_vendor/
# Bleach has a shim layer that references the vendored html5lib we just deleted.
# Let's patch up the imports to use the real html5lib.
#sed -i "s/bleach._vendor.html5lib/html5lib/g" bleach/html5lib_shim.py tests/test_clean.py bleach/sanitizer.py

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{srcname}-*.egg-info/
%{python_sitelib}/%{srcname}/
