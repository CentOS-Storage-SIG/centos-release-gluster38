Summary: GlusterFS 3.8 packages from the CentOS Storage SIG repository
Name: centos-release-gluster38
Version: 1.0
Release: 1%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Gluster-3.8.repo

BuildArch: noarch

# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

# Users can install centos-release-gluster to get the latest
Provides: centos-release-gluster = 3.8
Conflicts: centos-release-gluster < 3.8
Obsoletes: centos-release-gluster < 3.8

%description
yum configuration for GlusterFS 3.8 packages as delivered via the CentOS
Storage SIG.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.8.repo

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.8.repo

%changelog
* Mon May 16 2016 Niels de Vos <ndevos@redhat.com> - 1.0-1
- Initial version based on centos-release-gluster37
