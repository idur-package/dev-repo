Name="minetest-game"
Version="5.4.1"

Maintainer="Can202"
Contact="mgoopazo@gmail.com"

Arch="all"


License="https://raw.githubusercontent.com/minetest/minetest/master/LICENSE.txt"
Depends=["dialog", "git", "g++", "make", "libc6-dev", "cmake", "libpng-dev", "libjpeg-dev", "libxxf86vm-dev", "libgl1-mesa-dev", "libsqlite3-dev", "libogg-dev", "libvorbis-dev", "libopenal-dev", "libcurl4-gnutls-dev", "libfreetype6-dev", "zlib1g-dev", "libgmp-dev", "libjsoncpp-dev", "libzstd-dev"]
idurDepends=["idur-pkg"]
Conflict=["minetest-game"]
Description="""

description here

"""

Install="""

dialog --title "Compile minetest" --yesno "This version is compiled" 0 0
if [ $? = 1 ]
then
    idur-pkg tmp minetest
    cd $(idur-pkg dp minetest)
    git clone --depth 1 https://github.com/minetest/minetest
    cd minetest
    git checkout 5.4.1
    git clone --depth 1 --branch 5.4.1 https://github.com/minetest/minetest_game games/minetest_game
    git clone --depth 1 https://github.com/minetest/irrlicht.git lib/irrlichtmt
    cmake . -DRUN_IN_PLACE=TRUE
    make -j$(nproc)
    cd $(idur-pkg dp minetest)
    cp -r minetest/ /opt/
    

    echo "#!/bin/bash
    cd /opt/minetest/
    ./bin/minetest
    " > /usr/bin/minetest-game
    chmod a+x /usr/bin/minetest-game
    chmod a+rwx -R /opt/minetest/

else
    clear
    echo "aborting"
fi





"""

Remove="""

# Remove instructions here (bash)

"""
