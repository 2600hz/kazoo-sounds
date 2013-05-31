%define packagelayout   FH
%define SOUNDSDIR       %{_prefix}/share/freeswitch/sounds

Name:           kazoo-prompts
Summary:        Audio prompts for the Kazoo platform
License:        MPL1.1
Group:          Productivity/Telephony
Version:        v2.13
Release:        2600hz
URL:            http://www.2600hz.org/
Packager:       Karl Anderson
Vendor:         http://www.2600hz.org/

Source0:        Kazoo-Prompts.tar

BuildArch:    noarch
BuildRoot:    %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Audo prompts files to match the voice streamed from Kazoo Media Manager.

######################################################################################################################
# Prepare for the build
######################################################################################################################
%prep
%setup -b0 -q -n Kazoo-Prompts

%{__mkdir} -p %{buildroot}%{SOUNDSDIR}

cp -r %{_builddir}/Kazoo-Prompts/* %{buildroot}%{SOUNDSDIR}/
rm %{buildroot}%{SOUNDSDIR}/kazoo-prompts.spec

######################################################################################################################
# Bootstrap, Configure and Build the whole enchilada
######################################################################################################################
%build

######################################################################################################################
# Install it to the build root
######################################################################################################################
%install

######################################################################################################################
# Executed when RPM is installed
######################################################################################################################
%pre

%post
find %{SOUNDSDIR} -type d -exec chmod 755 {} +

######################################################################################################################
# Executed when the RPM is uninstalled
######################################################################################################################
%postun

######################################################################################################################
# List of files/directories to include
######################################################################################################################
%files                                                                                                                                                                                                                                                                                             
%defattr(0644,freeswitch,daemon)
%dir %attr(0755,freeswitch,daemon) %{SOUNDSDIR}
%{SOUNDSDIR}/*

