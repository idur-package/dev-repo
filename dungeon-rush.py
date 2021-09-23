Name="dungeon-rush"
Version="v0.1-beta"

Maintainer="Can202"
Contact="mgoopazo@gmail.com"

Arch="all"

Time="short"


License="https://github.com/rapiz1/DungeonRush/blob/master/LICENSE"
Depends=["libsdl2-dev", "libsdl2-image-dev", "libsdl2-mixer-dev", "libsdl2-net-dev", "libsdl2-ttf-dev"]
idurDepends=["idur-pkg"]
Conflict=["dungeon-rush"]
Description="""
A opensource game inspired by Snake,
written in pure C with SDL.

"""

Install="""

idur-pkg tmp dr
cd $(idur-pkg dp dr)
idur-pkg download https://github.com/rapiz1/DungeonRush/releases/download/v1.1-beta/DungeonRush-v1.1-beta-Linux.zip
idur-pkg uncompress -d dungeon-rush DungeonRush-v1.1-beta-Linux.zip
cp -r dungeon-rush /opt/
idur-pkg exec /opt/dungeon-rush/dungeon_rush
echo "#!/usr/bin/bash
cd /opt/dungeon-rush/
./dungeon_rush" > /usr/bin/dungeon-rush
idur-pkg exec /usr/bin/dungeon-rush
idur-pkg rm-tmp dr


"""

Remove="""
idur-pkg rm /usr/bin/dungeon-rush
idur-pkg rm /opt/dungeon-rush/

"""
