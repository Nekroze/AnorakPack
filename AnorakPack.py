from pakpak import Modpack

forge = "minecraftforge-universal-1.6.4-9.11.1.916.jar"
server = "minecraft_server.1.6.4.jar"

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
