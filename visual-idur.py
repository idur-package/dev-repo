Name="visual-idur"
Version="v0.1"

Maintainer="Can202"
Contact="mgoopazo@gmail.com"

Arch="x86_64"

Time="almost-medium"

Depends=["xterm", "python3"]
idurDepends=["idur-pkg", "idur-exec", "idur-stable idur-dev"]
Conflict=["visual-idur"]
License="https://github.com/idur-package/Visual-Idur/blob/master/LICENSE"
Description="""
Visual Idur

"""

Install64="""
idur-pkg tmp visual-idur
cd $(idur-pkg dp visual-idur)

idur-pkg download https://github.com/idur-package/Visual-Idur/releases/download/v0.1/visual-idur-x86_64.tar.xz

idur-pkg uncompress visual-idur-x86_64.tar.xz

mkdir -p /opt/idur/share/program/visual-idur/
idur-pkg copy visual-idur /opt/idur/share/program/visual-idur/

idur-pkg exec /opt/idur/share/program/visual-idur/visual-idur

ln /opt/idur/share/program/visual-idur/visual-idur /opt/idur/bin/visual-idur

idur-pkg rm-tmp visual-idur

"""

Remove="""
# Remove instructions here (bash)

# Remove Files and directories
idur-pkg rm /opt/idur/bin/visual-idur
idur-pkg rm /opt/idur/share/program/visual-idur/

"""
