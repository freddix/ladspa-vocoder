Summary:	LADSPA vocoder plugin
Name:		ladspa-vocoder
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://www.sirlab.de/linux/download/vocoder-ladspa-%{version}.tgz
# Source0-md5:	f802cc54b0e55b6764bf0a1f59820c40
URL:		http://www.sirlab.de/linux/descr_vocoder.html
BuildRequires:	ladspa-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A vocoder plugin for LADSPA.

%prep
%setup -qn vocoder-%{version}

sed -i -e "s|-O3|%{rpmcflags} -O3|" Makefile

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D vocoder.so $RPM_BUILD_ROOT%{_libdir}/ladspa/vocoder.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/ladspa/vocoder.so

