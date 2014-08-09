#
# spec file for package how-simple-wallpaper
#
# Copyright (c) 2014 Kamarada Project, Aracaju, Brazil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


Name:           how-simple-wallpaper
Version:        1.0
Release:        1
Summary:        How simple wallpaper
License:        CC-BY-NC-SA-3.0
Group:          System/Fhs
Source0:        LICENSE
Source1:        How_simple____by_lassekongo83.7z
Url:            http://lassekongo83.deviantart.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  ImageMagick
BuildRequires:  p7zip


%description
A simple wallpaper designed by Mattias

http://lassekongo83.deviantart.com/art/How-simple-137101524


%prep
cp -a %{SOURCE0} COPYING
7za x %{SOURCE1}


%build
mkdir -p How_Simple_Blue/contents/images
mkdir -p How_Simple_Darker_Blue/contents/images
mkdir -p How_Simple_Green/contents/images
mkdir -p How_Simple_Pink/contents/images

cat >How_Simple_Blue/metadata.desktop <<EOF
[Desktop Entry]
Name=How Simple Blue

X-KDE-PluginInfo-Name=How-Simple-Blue
X-KDE-PluginInfo-Author=Mattias
X-KDE-PluginInfo-License=CC-BY-NC-SA-3.0
EOF

mv "How simple/howsimple-2560x1600-blue.jpg" How_Simple_Blue/contents/images/2560x1600.jpeg

convert "How_Simple_Blue/contents/images/2560x1600.jpeg" \
-resize 400x250 \
How_Simple_Blue/screenshot.jpeg

cat >How_Simple_Darker_Blue/metadata.desktop <<EOF
[Desktop Entry]
Name=How Simple Darker Blue

X-KDE-PluginInfo-Name=How-Simple-Darker-Blue
X-KDE-PluginInfo-Author=Mattias
X-KDE-PluginInfo-License=CC-BY-NC-SA-3.0
EOF

convert "How simple/howsimple-2560x1600-darkerblue.png" How_Simple_Darker_Blue/contents/images/2560x1600.jpeg

convert "How simple/howsimple-2560x1600-darkerblue.png" \
-resize 400x250 \
How_Simple_Darker_Blue/screenshot.jpeg

cat >How_Simple_Green/metadata.desktop <<EOF
[Desktop Entry]
Name=How Simple Green

X-KDE-PluginInfo-Name=How-Simple-Green
X-KDE-PluginInfo-Author=Mattias
X-KDE-PluginInfo-License=CC-BY-NC-SA-3.0
EOF

mv "How simple/howsimple-2560x1600-green.jpg" How_Simple_Green/contents/images/2560x1600.jpeg

convert "How_Simple_Green/contents/images/2560x1600.jpeg" \
-resize 400x250 \
How_Simple_Green/screenshot.jpeg

cat >How_Simple_Pink/metadata.desktop <<EOF
[Desktop Entry]
Name=How Simple Pink

X-KDE-PluginInfo-Name=How-Simple-Pink
X-KDE-PluginInfo-Author=Mattias
X-KDE-PluginInfo-License=CC-BY-NC-SA-3.0
EOF

mv "How simple/howsimple-2560x1600-pink.jpg" How_Simple_Pink/contents/images/2560x1600.jpeg

convert "How_Simple_Pink/contents/images/2560x1600.jpeg" \
-resize 400x250 \
How_Simple_Pink/screenshot.jpeg


%install
mkdir -p $RPM_BUILD_ROOT/usr/share/wallpapers
cp -R $RPM_BUILD_DIR/How_Simple_* $RPM_BUILD_ROOT/usr/share/wallpapers/


%files
%defattr(-,root,root)
%doc COPYING
/usr/share/wallpapers/
/usr/share/wallpapers/How_Simple_Blue/
/usr/share/wallpapers/How_Simple_Darker_Blue/
/usr/share/wallpapers/How_Simple_Green/
/usr/share/wallpapers/How_Simple_Pink/


%changelog
* Sat Aug 09 2014 kamaradalinux@gmail.com
- Initial import from deviantART
