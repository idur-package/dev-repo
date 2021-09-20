Name="tlauncher-lastest"
Version="1"

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="x86_64"

idurDepends=["jre-8u301", "idur-pkg"]
Conflict=["tlauncher-lastest"]
Description="""
Famous Minecraft Launcher
"""

Install64="""
idur-pkg tmp tl-l
cd /tmp/$(idur-pkg dir-tmp tl-l)

idur-pkg download https://tlauncher.org/jar
idur-pkg uncompress TLauncher-*

idur-pkg rm /opt/TLauncher/
mkdir -p /opt/TLauncher/

cp TLauncher-*.jar /opt/TLauncher/tlauncher.jar

idur-pkg read https://raw.githubusercontent.com/idur-package/media/7a3f426f95230de9658774a7e2701e2cca7221eb/tlauncher/tlauncher > /usr/bin/tlauncher
chmod a+x /usr/bin/tlauncher

idur-pkg download https://raw.githubusercontent.com/idur-package/media/7a3f426f95230de9658774a7e2701e2cca7221eb/tlauncher/tlauncher.ico
cp /tmp/$(idur-pkg dir-tmp tl-l)/tlauncher.ico /opt/TLauncher/tlauncher.ico

idur-pkg read https://raw.githubusercontent.com/idur-package/media/7a3f426f95230de9658774a7e2701e2cca7221eb/tlauncher/tlauncher.desktop > /usr/share/applications/tlauncher.desktop
chmod a+x /usr/share/applications/tlauncher.desktop



"""

Remove="""
idur-pkg rm /opt/TLauncher/
idur-pkg rm /usr/bin/tlauncher
idur-pkg rm /usr/share/applications/tlauncher.desktop

"""
