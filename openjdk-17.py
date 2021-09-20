
Name="openjdk-17"
Version="35"


Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="x86_64"


License="https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt"
Depends=["tar", "python3"]
idurDepends= ["idur-pkg"]
Conflict= ["openjdk-17"]
Description="""

description here

"""

Install64="""
idur-pkg tmp jdk17
cd /tmp/idur-jdk17-tmp/
idur-pkg download https://download.java.net/java/GA/jdk17/0d483333a00540d886896bac774ff48b/35/GPL/openjdk-17_linux-x64_bin.tar.gz
tar -xvzf openjdk-17_linux-x64_bin.tar.gz
cp -r /tmp/idur-jdk17-tmp/jdk-17/ /opt/openjdk-17
idur-pkg read https://raw.githubusercontent.com/idur-package/media/b0d031a2c2bd52406446d8521704faa67075e811/openjdk-17/openjdk-17 > /usr/bin/openjdk-17
chmod a+x /usr/bin/openjdk-17
cd ..
idur-pkg rm-tmp jdk17
"""

Remove="""
idur-pkg rm /opt/openjdk-17
idur-pkg rm /usr/bin/openjdk-17

"""
