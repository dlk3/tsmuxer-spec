# Fedora RPM Package For tsMuxer Application

`tsMuxer` is a simple program to mux video to TS/M2TS files or create BD
disks. See the [home page](https://github.com/justdan96/tsMuxer) for details.

This repository contains a `tsmuxer.spec` file that helps me build
an installation RPM file for `tsMuxer` for my Fedora desktop.

I have created a Fedora COPR repository to support the installation of
the RPMs I created.  To install tsMuxer from this repository do:
```
$ sudo dnf copr enable dlk/rpms
$ sudo dnf install tsMuxer
