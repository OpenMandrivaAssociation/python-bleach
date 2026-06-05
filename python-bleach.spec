%define module bleach

Name:		python-bleach
Version:	6.4.0
Release:	1
Summary:	An easy whitelist-based HTML-sanitizing tool
Group:		Development/Python
License:	Apache-2.0
URL:		https://github.com/mozilla/bleach
Source0:	%{URL}/archive/v%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(tinycss2)
BuildRequires:	python%{pyver}dist(webencodings)
BuildRequires:	python%{pyver}dist(wheel)

%description
Bleach is an HTML sanitizing library that escapes or strips markup and
attributes based on a white list.

NOTE: 2026-06-05: Bleach is no longer maintained.
https://github.com/mozilla/bleach/issues/698#issuecomment-4631783739

This package only is provided for packages that consume it and backwards-
compatibility, it should not be relied on or used in new projects.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
