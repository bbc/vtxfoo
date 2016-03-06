Name: vtxfoo
Version: 0.0.1
Release: 1%{?dist}
Group: Application/Web
License: Internal BBC use only
Summary: vtxfoo
Source0: vtxfoo.tar.gz
Source1: bake-scripts.tar.gz
Requires: initscripts, chkconfig, java-1.8.0-openjdk
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python-setuptools, redhat-rpm-config

%description
vtxfoo built by the Magic Build Tool

%prep
%setup -q -n src

%build

%install
mkdir -p %{buildroot}/etc/vtxfoo
mkdir -p %{buildroot}/opt/vtxfoo
cp $RPM_BUILD_DIR/target/vtxfoo-fat.jar %{buildroot}/opt/vtxfoo/
cp $RPM_BUILD_DIR/src/etc/vtxfoo/application-conf.json %{buildroot}/etc/vtxfoo/
cp -r $RPM_BUILD_DIR/src/etc/init.d %{buildroot}/etc/


mkdir -p %{buildroot}/var/run/vtxfoo
mkdir -p %{buildroot}/var/log/vtxfoo
mkdir -p %{buildroot}/etc/bake-scripts/vtxfoo
tar -C %{buildroot}/etc/bake-scripts/vtxfoo -xzf %{SOURCE1}

%pre

getent group vtxfoo >/dev/null || groupadd -r vtxfoo
getent passwd vtxfoo >/dev/null || \
    useradd -r -g vtxfoo -G vtxfoo -d / -s /sbin/nologin \
            -c "vtxfoo service" vtxfoo

%preun

if [ $1 -eq 0 ]; then
    /sbin/service vtxfoo stop >/dev/null 2>&1
    /sbin/chkconfig --del vtxfoo
fi


%post
/sbin/chkconfig --add vtxfoo

%postun

%clean
rm -rf %{buildroot}

%files
%defattr(755, root, root, 755)
/etc/init.d/vtxfoo
/etc/vtxfoo/application-conf.json

%defattr(755, vtxfoo, vtxfoo, 755)
%dir /opt/vtxfoo
/opt/vtxfoo/vtxfoo-fat.jar

%defattr(644, root, vtxfoo, 2775)
%dir /var/run/vtxfoo
%dir /var/log/vtxfoo

%defattr(-, root, root, 755)
/etc/bake-scripts/vtxfoo
