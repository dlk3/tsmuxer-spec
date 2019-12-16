%define debug_package %{nil}

Name:		tsmuxer
Version:	2.6.15
Release:	1%{?dist}
Summary:	tsMuxeR is a simple program to mux video to TS/M2TS files or create BD disks.

License:	Apache-2.0
URL:		https://bintray.com/justdan96/tsMuxer/tsMuxerGUI-Nightly/_latestVersion
Source0:	lnx-nightly-2019-12-16--01-10-10.zip
BuildArch:	x86_64


BuildRequires:	wget
BuildRequires:	unzip


%description
tsMuxer is a transport stream muxer for remuxing/muxing elementary
streams, EVO/VOB/MPG, MKV/MKA, MP4/MOV, TS, M2TS to TS to M2TS.
Supported video codecs H.264/AVC, H.265/HEVC, VC-1, MPEG2.
Supported audio codecs AAC, AC3 / E-AC3(DD+), DTS/ DTS-HD.


%prep
wget -q -O "%{SOURCE0}" "https://bintray.com/justdan96/tsMuxer/download_file?file_path=$(basename "%{SOURCE0}")"
cd %{_builddir}
rm -rf %{name}-%{version}
/usr/bin/unzip "%{SOURCE0}" -d "%{_builddir}/%{name}-%{version}/"
wget -q -O %{_builddir}/LICENSE "https://www.apache.org/licenses/LICENSE-2.0.txt"


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} %{name}-%{version}/bin/lnx/tsMuxeR
install -m 755 %{name}-%{version}/bin/lnx/tsMuxerGUI* %{buildroot}%{_bindir}/tsMuxerGUI


%files
%license LICENSE 
%{_bindir}/tsMuxeR
%{_bindir}/tsMuxerGUI


%changelog
* Mon Dec 16 2019 David King <dave@daveking.com> - 2.6.15-2
- Switch to downloading binaries from nightly build web site
- Add tsMuxeR-gui and create tsmuxer.desktop and txmuxer.png icon files
* Tue Dec 10 2019 David King <dave@daveking.com> - 2.6.15-1
- Initial Version
