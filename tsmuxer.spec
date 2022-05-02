%define debug_package %{nil}

Name:		tsMuxer
Version:	2.6.16
Release:	1%{?dist}
Summary:	tsMuxer is a simple program to mux video to TS/M2TS files or create BD disks.

License:	Apache-2.0
URL:		https://github.com/justdan96/tsMuxer
Source0:	%{name}-%{version}.tar.gz
Source1:	https://github.com/dlk3/tsmuxer-spec/blob/master/tsMuxerGUI.desktop
BuildArch:	x86_64


BuildRequires:	ninja-build
BuildRequires:	cmake
BuildRequires:	zlib-devel
BuildRequires:	freetype-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtdeclarative-devel


%description
tsMuxer is a transport stream muxer for remuxing/muxing elementary
streams, EVO/VOB/MPG, MKV/MKA, MP4/MOV, TS, M2TS to TS to M2TS.
Supported video codecs H.264/AVC, H.265/HEVC, VC-1, MPEG2.
Supported audio codecs AAC, AC3 / E-AC3(DD+), DTS/ DTS-HD.


%prep
%setup
cp "%{SOURCE1}" %{_builddir}/%{name}-%{version}/

%build
cd %{_builddir}/%{name}-%{version}
./rebuild_linux_with_gui.sh


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} build/tsMuxer/tsmuxer
ln -s tsmuxer %{buildroot}%{_bindir}/tsMuxer
install -m 755 -t %{buildroot}%{_bindir} build/tsMuxerGUI/tsMuxerGUI
ln -s tsMuxerGUI %{buildroot}%{_bindir}/tsmuxergui
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 -t %{buildroot}%{_datadir}/applications tsMuxerGUI.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128
install -m 644 tsMuxerGUI/images/icon.png %{buildroot}%{_datadir}/icons/hicolor/128x128/tsMuxerGUI.png


%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_bindir}/tsmuxer
%{_bindir}/tsMuxer
%{_bindir}/tsMuxerGUI
%{_bindir}/tsmuxergui
%{_datadir}/applications/tsMuxerGUI.desktop
%{_datadir}/icons/hicolor/128x128/tsMuxerGUI.png


%post
[ -f %{_datadir}/icons/hicolor/icon-theme.cache ] && %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor -q
exit 0


%postun
[ -f %{_datadir}/icons/hicolor/icon-theme.cache ] && %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor -q
exit 0


%changelog
* Fri Apr 3 2020 David King <dave@daveking.com> - 2.6.16-1
- tsMuxer 2.6.16 release
* Mon Dec 16 2019 David King <dave@daveking.com> - 2.6.15-2
- Add tsMuxerGUI along with associated desktop file
* Tue Dec 10 2019 David King <dave@daveking.com> - 2.6.15-1
- Initial Version
