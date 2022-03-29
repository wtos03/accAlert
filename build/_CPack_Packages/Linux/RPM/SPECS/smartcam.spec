# Restore old style debuginfo creation for rpm >= 4.14.
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# -*- rpm-spec -*-
BuildRoot:      %_topdir/smartcam-1.0.1-1.aarch64
Summary:        smartcam built using CMake
Name:           smartcam
Version:        1.0.1
Release:        1
License:        unknown
Group:          unknown
Vendor:         xilinx















Prefix: /





%define _rpmdir %_topdir/RPMS
%define _srcrpmdir %_topdir/SRPMS
%define _rpmfilename smartcam-1.0.1-1.aarch64.rpm
%define _unpackaged_files_terminate_build 0

%define _build_id_links none


%description
DESCRIPTION
===========

This is an installer created using CPack (https://cmake.org). No additional installation instructions provided.



# This is a shortcutted spec file generated by CMake RPM generator
# we skip _install step because CPack does that for us.
# We do only save CPack installed tree in _prepr
# and then restore it in build.
%prep
mv $RPM_BUILD_ROOT %_topdir/tmpBBroot

%install
if [ -e $RPM_BUILD_ROOT ];
then
  rm -rf $RPM_BUILD_ROOT
fi
mv %_topdir/tmpBBroot $RPM_BUILD_ROOT



%clean

%post



%posttrans


%postun


%pre


%pretrans


%preun


%files
%defattr(-,root,root,-)
%dir "/opt"
%dir "/opt/xilinx"
"/opt/xilinx/README_SMARTCAM"
%dir "/opt/xilinx/bin"
"/opt/xilinx/bin/01.mipi-rtsp.sh"
"/opt/xilinx/bin/02.mipi-dp.sh"
"/opt/xilinx/bin/03.file-file.sh"
"/opt/xilinx/bin/04.file-ssd-dp.sh"
"/opt/xilinx/bin/smartcam"
"/opt/xilinx/bin/smartcam-install.py"
%dir "/opt/xilinx/lib"
"/opt/xilinx/lib/libivas_airender.so"
"/opt/xilinx/lib/libivas_xpp.so"
%dir "/opt/xilinx/share"
%dir "/opt/xilinx/share/ivas"
%dir "/opt/xilinx/share/ivas/smartcam"
%dir "/opt/xilinx/share/ivas/smartcam/facedetect"
"/opt/xilinx/share/ivas/smartcam/facedetect/aiinference.json"
"/opt/xilinx/share/ivas/smartcam/facedetect/drawresult.json"
"/opt/xilinx/share/ivas/smartcam/facedetect/preprocess.json"
%dir "/opt/xilinx/share/ivas/smartcam/refinedet"
"/opt/xilinx/share/ivas/smartcam/refinedet/aiinference.json"
"/opt/xilinx/share/ivas/smartcam/refinedet/drawresult.json"
"/opt/xilinx/share/ivas/smartcam/refinedet/preprocess.json"
%dir "/opt/xilinx/share/ivas/smartcam/ssd"
"/opt/xilinx/share/ivas/smartcam/ssd/aiinference.json"
"/opt/xilinx/share/ivas/smartcam/ssd/drawresult.json"
"/opt/xilinx/share/ivas/smartcam/ssd/label.json"
"/opt/xilinx/share/ivas/smartcam/ssd/preprocess.json"
%dir "/opt/xilinx/share/notebooks"
%dir "/opt/xilinx/share/notebooks/smartcam"
"/opt/xilinx/share/notebooks/smartcam/LICENSE"
%dir "/opt/xilinx/share/notebooks/smartcam/images"
"/opt/xilinx/share/notebooks/smartcam/images/xilinx_logo.png"
"/opt/xilinx/share/notebooks/smartcam/smartcam.ipynb"
%dir "/opt/xilinx/share/vitis_ai_library"
%dir "/opt/xilinx/share/vitis_ai_library/models"
%dir "/opt/xilinx/share/vitis_ai_library/models/kv260-smartcam"
%dir "/opt/xilinx/share/vitis_ai_library/models/kv260-smartcam/ssd_adas_pruned_0_95"
"/opt/xilinx/share/vitis_ai_library/models/kv260-smartcam/ssd_adas_pruned_0_95/label.json"




%changelog
* Sun Jul 4 2010 Eric Noulard <eric.noulard@gmail.com> - 1.0.1-1
  Generated by CPack RPM (no Changelog file were provided)

