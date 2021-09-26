Name="firefox"
Version="auto1"

Maintainer="Can202"
Contact="mgoopazo@gmail.com"

Arch="both"

Time="short"


License="https://www.mozilla.org/en-US/foundation/licensing/"
idurDepends=["idur-pkg", "idur-exec"]
Conflict=["firefox"]
Description="""

description here

"""

Install64="""

ARCH="x86_64"
VERSION="92.0.1"

idur-pkg tmp firefox
cd $(idur-pkg dp firefox)

idur-pkg download https://download-installer.cdn.mozilla.net/pub/firefox/releases/$VERSION/linux-$ARCH/en-US/firefox-$VERSION.tar.bz2

idur-pkg uncompress firefox-92.0.1.tar.bz2

idur-pkg copy firefox /opt/idur/share/program/firefox
idur-pkg mod /opt/idur/share/program/firefox

echo "#!/bin/bash
cd /opt/idur/share/program/firefox
arg="\$1 \$2 \$3 \$4 \$5 \$6 \$7 \$8 \$9"
./firefox $arg
" > /opt/idur/bin/firefox
idur-pkg exec /opt/idur/bin/firefox

echo "[Desktop Entry]
Name=Firefox
Exec=idur-exec firefox
Type=Application
Categories=Network
Icon=/opt/idur/share/program/firefox/browser/chrome/icons/default/default128.png" > /usr/share/applications/id-firefox.desktop
idur-pkg exec /usr/share/applications/id-firefox.desktop

idur-pkg rm-tmp firefox

"""

Install32="""

ARCH="i686"
VERSION="92.0.1"

idur-pkg tmp firefox
cd $(idur-pkg dp firefox)

idur-pkg download https://download-installer.cdn.mozilla.net/pub/firefox/releases/$VERSION/linux-$ARCH/en-US/firefox-$VERSION.tar.bz2

idur-pkg uncompress firefox-92.0.1.tar.bz2

idur-pkg copy firefox /opt/idur/share/program/firefox
idur-pkg mod /opt/idur/share/program/firefox

echo "#!/bin/bash
cd /opt/idur/share/program/firefox
arg="\$1 \$2 \$3 \$4 \$5 \$6 \$7 \$8 \$9"
./firefox $arg
" > /opt/idur/bin/firefox
idur-pkg exec /opt/idur/bin/firefox

echo "[Desktop Entry]
Name=Firefox
Exec=idur-exec firefox
Type=Application
Categories=Network
Icon=/opt/idur/share/program/firefox/browser/chrome/icons/default/default128.png" > /usr/share/applications/id-firefox.desktop
idur-pkg exec /usr/share/applications/id-firefox.desktop

idur-pkg rm-tmp firefox

"""

Remove="""
idur-pkg rm /opt/idur/bin/firefox
idur-pkg rm /opt/idur/share/program/firefox
idur-pkg rm /usr/share/applications/id-firefox.desktop

"""
