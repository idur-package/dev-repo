Name="dunpress"
Version="v0.1"

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all"


License="https://raw.githubusercontent.com/Can202/dunpress/main/LICENSE"
Depends=["unzip", "tar", "python3"]
idurDepends=["idur-pkg"]
Conflict=["dunpress"]
Description="""
uncompress tarballs and zip with one command.

"""

Install="""

idur-pkg read https://raw.githubusercontent.com/Can202/dunpress/v0.1/src/dumpress.py > /usr/bin/dumpress
chmod a+x /usr/bin/dumpress

"""

Remove="""

idur-pkg rm /usr/bin/dumpress

"""
