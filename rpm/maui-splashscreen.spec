# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       maui-splashscreen

# >> macros
# << macros

Summary:    Maui splash screen
Version:    0.1.0
Release:    1
Group:      Applications/Multimedia
License:    CC-BY-SA 3.0
BuildArch:  noarch
URL:        http://www.maui-project.org
Source0:    maui-splashscreen-%{version}.tar.xz
Source100:  maui-splashscreen.yaml
Provides:   boot-splash-screen
Provides:   generic-logos
Provides:   system-logos
Obsoletes:   generic-backgrounds
Obsoletes:   generic-logos
Obsoletes:   system-logos

%description
The %{name} package contains artwork for Maui.


%prep
%setup -q -n %{name}-%{version}/images

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
install -D -m 644 splash-maui-startup-640x480.png %{buildroot}%{_datadir}/plymouth/splash-maui-startup-640x480.png
install -D -m 644 splash-maui-shutdown-640x480.png %{buildroot}%{_datadir}/plymouth/splash-maui-shutdown-640x480.png
ln -s splash-maui-startup-640x480.png %{buildroot}%{_datadir}/plymouth/splash.png
ln -s splash-maui-shutdown-640x480.png %{buildroot}%{_datadir}/plymouth/halt.png
ln -s splash-maui-shutdown-640x480.png %{buildroot}%{_datadir}/plymouth/poweroff.png
ln -s splash-maui-shutdown-640x480.png %{buildroot}%{_datadir}/plymouth/reboot.png

install -D -m 644 livecd-splash.png %{buildroot}%{_libdir}/anaconda-runtime/syslinux-vesa-splash.png
install -D -m 644 livecd-splash.jpg %{buildroot}%{_libdir}/anaconda-runtime/syslinux-vesa-splash.jpg
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/plymouth/splash-maui-startup-640x480.png
%{_datadir}/plymouth/splash-maui-shutdown-640x480.png
%{_datadir}/plymouth/splash.png
%{_datadir}/plymouth/halt.png
%{_datadir}/plymouth/poweroff.png
%{_datadir}/plymouth/reboot.png
%{_libdir}/anaconda-runtime/syslinux-vesa-splash.png
%{_libdir}/anaconda-runtime/syslinux-vesa-splash.jpg
# >> files
# << files
