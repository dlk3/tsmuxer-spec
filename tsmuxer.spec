%define debug_package %{nil}

Name:		tsmuxer
Version:	2.6.15
Release:	1%{?dist}
Summary:	tsMuxeR is a simple program to mux video to TS/M2TS files or create BD disks.

License:	Apache-2.0
URL:		https://github.com/justdan96/tsMuxer
Source0:	%{name}-%{version}.tar.gz
BuildArch:	x86_64


BuildRequires:	ninja-build


%description
tsMuxer is a transport stream muxer for remuxing/muxing elementary
streams, EVO/VOB/MPG, MKV/MKA, MP4/MOV, TS, M2TS to TS to M2TS.
Supported video codecs H.264/AVC, H.265/HEVC, VC-1, MPEG2.
Supported audio codecs AAC, AC3 / E-AC3(DD+), DTS/ DTS-HD.


%prep
%setup


%build
./rebuild_linux_with_gui.sh


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} build/tsMuxer/tsmuxer
install -m 755 -t %{buildroot}%{_bindir} build/tsMuxerGUI/tsMuxerGUI


%files
%license LICENSE
%doc README.md
%{_bindir}/tsmuxer
%{_bindir}/tsMuxerGUI


%changelog
* Mon Dec 16 2019 David King <dave@daveking.com> - 2.6.15-1
- Initial Version
- Add tsMuxerGUI along with associated desktop file
* Tue Dec 10 2019 David King <dave@daveking.com> - 2.6.15-1
- Initial Version
