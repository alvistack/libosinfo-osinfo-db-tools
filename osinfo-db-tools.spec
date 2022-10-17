# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: osinfo-db-tools
Epoch: 100
Version: 1.9.0
Release: 1%{?dist}
Summary: Tools for managing the osinfo database
License:  GPL-2.0-or-later
URL: https://gitlab.com/libosinfo/osinfo-db-tools/-/tags
Source0: %{name}_%{version}.orig.tar.gz
%if 0%{?suse_version} > 1500 || 0%{?sle_version} == 150400
BuildRequires: libsoup2-devel
%endif
%if 0%{?sle_version} == 150300
BuildRequires: libsoup-devel
%endif
%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
BuildRequires: libsoup-devel
%endif
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: glib2-devel
BuildRequires: json-glib-devel
BuildRequires: libarchive-devel
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: libxslt-devel >= 1.0.0
BuildRequires: meson

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%dir %{_datadir}/locale/*
%dir %{_datadir}/locale/*/LC_MESSAGES
%{_bindir}/osinfo-db-export
%{_bindir}/osinfo-db-import
%{_bindir}/osinfo-db-path
%{_bindir}/osinfo-db-validate
%{_datadir}/locale/*/LC_MESSAGES/osinfo-db-tools.mo
%{_mandir}/man1/osinfo-db-export.1*
%{_mandir}/man1/osinfo-db-import.1*
%{_mandir}/man1/osinfo-db-path.1*
%{_mandir}/man1/osinfo-db-validate.1*

%changelog
