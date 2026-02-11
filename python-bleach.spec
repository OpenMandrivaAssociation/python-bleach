%global module bleach

Name:		python-bleach
Version:	6.3.0
Release:	1
Summary:	An easy whitelist-based HTML-sanitizing tool
Group:		Development/Python
License:	ASL-2.0
URL:		https://github.com/jsocol/bleach
Source0:	%{URL}/archive/v%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
# Upstream vendorised/internalised html5lib and dont seem keen to revert that choice.
# https://github.com/mozilla/bleach/issues/386
# https://github.com/mozilla/bleach/pull/438
# BuildRequires:	python%%{pyver}dist(html5lib)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(tinycss2)
BuildRequires:	python%{pyver}dist(webencodings)
BuildRequires:	python%{pyver}dist(wheel)

%description
Bleach is an HTML sanitizing library that escapes or strips markup and
attributes based on a white list.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

# Remove vendored libraries which were added for https://github.com/mozilla/bleach/issues/386
# rm -rf _vendor/
# Bleach has a shim layer that references the vendored html5lib we just deleted.
# Let's patch up the imports to use the real html5lib.
#sed -i "s/bleach._vendor.html5lib/html5lib/g" bleach/html5lib_shim.py tests/test_clean.py bleach/sanitizer.py

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
