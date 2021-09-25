Name="leafpad"
Version="0.8.17"

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all"

Time="almost-medium"


License="https://www.gnu.org/licenses/old-licenses/gpl-2.0.html"
Depends=["libgtk2.0-dev"]
idurDepends=["idur-pkg"]
Conflict=["leafpad"]
Description="""
leafpad is a simple text editor

"""

Install="""
idur-pkg tmp leafpad
cd $(idur-pkg dp leafpad)

idur-pkg download savannah.nongnu.org/download/leafpad/leafpad-0.8.17.tar.gz

idur-pkg uncompress leafpad-0.8.17.tar.gz

idur-pkg copy leafpad-0.8.17 /opt/idur/share/program/leafpad
cd /opt/idur/share/program/leafpad
./configure
make
make install

idur-pkg rm-tmp leafpad

"""

Remove="""
cd /opt/idur/share/program/leafpad
make uninstall
idur-pkg rm /opt/idur/share/program/leafpad

"""
