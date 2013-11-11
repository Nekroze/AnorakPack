from pakpak import Modpack

forge = "minecraftforge-universal-1.5.2-7.8.1.737.zip"
server = "minecraft_server_1.5.2.jar"

Anorak = Modpack(forge, server)
Anorak.server += forge

#Files preceded by '@' are not in the lite version of the modpack
def Define():
    #UNIVERSAL
    Anorak.universal_coremods += """
"""

    Anorak.universal_mods += """

"""

    Anorak.universal_data += """
data/config
"""

    #CLIENT
    Anorak.client_coremods += """

"""

    Anorak.client_mods += """

"""

    Anorak.client_data += """
"""

    Anorak.modpack += """

"""

    #SERVER
    Anorak.server_coremods += """
forgebackup-universal-coremod-1.5.2-1.1.2.98.jar
"""

    Anorak.server_plugins += """
"""

    Anorak.server_mods += """
"""

    Anorak.server += """
"""

if __name__ == "__main__":
    #CONSTRUCT
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1].lower() != "false":
            Anorak.skipable(False)
    Define()
    Anorak.construct()
