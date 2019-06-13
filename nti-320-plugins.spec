Name:		nti-320-plugins
Version: 	0.1
Release:	1%{?dist}
Summary: 	NTI-320 NRPE plugins

Group:		NTI-320
License:	GPL2+
URL:		https://github.com/nic-instruction/NTI-320
Source0:	https://github.com/nic-instruction/nti-320-plugins-0.1.tar.gz

BuildRequires:	gcc, python >= 1.3
Requires:	nrpe, nagios-plugins-all, bash, net-snmp, net-snmp-utils

%description
'nti-320-plugins' provides custom NRPE plugins
written by the NTI-320 class of 2017 with some additional fixes for our gcloud/centos 7 
environment.

%prep								

%setup -q	
		
%build					
%define _unpackaged_files_terminate_build 0

%install

rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib64/nagios/plugins/
mkdir -p %{buildroot}/etc/nrpe.d/

install -m 0755 * %{buildroot}/usr/lib64/nagios/plugins/

install -m 0744 nti320.cfg %{buildroot}/etc/nrpe.d/

%clean

%files					
%defattr(-,root,root)	
/usr/lib64/nagios/plugins/apachectl_config_example.sh
/usr/lib64/nagios/plugins/connectiontest.sh
/usr/lib64/nagios/plugins/monitor_postgres.sh
/usr/lib64/nagios/plugins/nfs-mount-test
/usr/lib64/nagios/plugins/nrpe_plugin_python_version.sh
/usr/lib64/nagios/plugins/nti-sanity.sh
/usr/lib64/nagios/plugins/rsyslogtest.sh


%config
/etc/nrpe.d/nti320.cfg

%doc			

%post

touch /thisworked

systemctl restart nrpe


%postun
rm /etc/nrpe.d/nti320.cfg
rm /thisworked
%changelog				# changes you (and others) have made and why
