Name="telegram"
Version="automatic.1"

Maintainer="Can202"
Contact="mgoopazo@gmail.com"

Arch="x86_64"


License="https://raw.githubusercontent.com/telegramdesktop/tdesktop/dev/LICENSE"
idurDepends=["idur-pkg"]
Conflict=["telegram", "telegram-desktop"]
Description="""
Telegram Desktop:
Fast and secure desktop app,
perfectly synced with your
mobile phone.

"""

Install64="""
idur-pkg tmp tl
cd $(idur-pkg dp tl)
idur-pkg download https://telegram.org/dl/desktop/linux
mv linux linux.tar.xz
idur-pkg uncompress linux.tar.xz
cp -r Telegram/ /opt/

idur-pkg download https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Telegram_2019_Logo.svg/150px-Telegram_2019_Logo.svg.png
cp 150px-Telegram_2019_Logo.svg.png /opt/Telegram/icon.png

echo "#!/usr/bin/bash
cd /opt/Telegram/
./Updater" > /usr/bin/telegram
chmod a+x /usr/bin/telegram

echo "[Desktop Entry]
Name=Telegram
Exec=telegram
Type=Application
Categories=Network" > /usr/share/applications/telegram.desktop
chmod a+x /usr/share/applications/telegram.desktop
chmod a+rwx -R /opt/Telegram/

idur-pkg rm-tmp tl
"""

Remove="""
idur-pkg rm /usr/share/applications/telegram.desktop
idur-pkg rm /opt/Telegram/
idur-pkg rm /usr/bin/telegram

"""
