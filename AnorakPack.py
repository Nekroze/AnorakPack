from pakpak import Modpack

forge = "minecraftforge-universal-1.5.2-7.8.1.737.zip"
server = "minecraft_server_1.5.2.jar"

Anorak = Modpack(forge, server)
Anorak.server += forge

#Files preceded by '@' are not in the lite version of the modpack
def Define():
    #UNIVERSAL
    Anorak.universal_coremods += """
Chemcraft_Core_1.4.1.jar
CodeChickenCore 0.8.7.3.jar
CoFHCore-1.5.2.5.jar
denLib-1.5.2-3.0.14.jar
Galacticraft-1.5.2-a0.1.36.407.jar
immibis-microblocks-55.0.5.jar
@MultiMine_1.5.2.jar
NotEnoughItems 1.5.2.28.jar
PowerCrystalsCore-1.1.6-107.jar
"""

    Anorak.universal_mods += """
@1.5.2_Jammy_Furniture_Mod_V4.4.zip
appeng-rv11-b.zip
Atomic_Science_v0.6.0.73.jar
BaMsDoubledoor_v2.0_for_1.5.2_ForgeMod.zip
@BiblioCraft[v1.3.1].zip
@binnie-mods-1.7.0.jar
buildcraft-A-3.7.1.jar
@buildcraft-Z-additional-buildcraft-objects-1.0.4.150.jar
@Carpenter's Blocks v1.5 - MC 1.5+.zip
ChickenChunks 1.3.2.14.jar
@chisel-1.5.2-1.4.4.jar
ComplexMachines_v0.3.3.119.jar
ComputerCraft1.53.zip
ConfigMod_for_MC_v1.5.2.zip
@coral-reef-universal-1.5.2-r2.zip
cpm-rec-1.5.2.zip
@CraftHeraldry 1.0.2.zip
DenPipes-1.5.2-2.0.7.jar
DenPipes-Forestry-1.5.2-1.0.3.jar
ElectricExpansion_v2.3.0.51.jar
EnderStorage 1.4.2.16.jar
@ExtraCells-universal-1.2.2b.jar
Factorization-0.7.37.jar
forestry-A-2.2.8.3.jar
@GateCopy-1.5.2-3.0.2.jar
GregsLighting-1.8.1-mc1.5.1.jar
ICBM_Contraption_v1.2.0.155.jar
ICBM_Explosion_v1.2.0.155.jar
ICBM_Sentry_v1.2.0.155.jar
iChunUtil1.0.1.zip
immibis-core-55.1.5.jar
immibis-peripherals-55.0.4.jar
Improved_Mob_Spawn_1.4.0.zip
@invasion_mod_0.11.7.zip
ironchest-universal-1.5.2-5.2.8.446.zip
KBI Tinkers Construct Recovery Addon 1.2.1.zip
Mekanism-v5.5.6.103.jar
MekanismGenerators-v5.5.6.103.jar
MekanismTools-v5.5.6.103.jar
MFFS_v3.1.0.160.jar
MineChem_v3.0.0.239.jar
MineFactoryReloaded-2.6.4-975.jar
@MineForever_0.2.0b.jar
miscperipherals-3.3.jar
ModularPowersuits-0.7.1-565.jar
@More Backpacks 2.1.4.zip
@MoreStorage.zip
MPSA-0.3.0-175_MPS-561+.jar
Natura_2.1.1.jar
NetherOres-2.1.5-75.jar
OmniTools-3.1.6.0.jar
OpenCCSensors-1.5.2.0.jar
OpenPeripheral-0.0.7.jar
@Panicle_Craft-v1.0.0.4c.zip
PluginsforForestry-1.5.2-3.0.17.jar
@PortalGun1.5.2.zip
Railcraft_1.5.2-7.2.3.0.jar
redlogic-55.3.3.jar
@RedstoneInMotion_1.1.1.0_mc1.5.zip
Rotten_Flesh_To_Leather_MC_1.5.2.zip
SAP_ManPack_v142.jar
SecretRoomsMod-universal-4.6.0.283.zip
@Securecraft_1.1.1.zip
SGCraft-0.5.2-mc1.5.1.jar
SkullForge.zip
SlimevoidLib-Universal-v2.0.1.1.zip
@StevesCarts2.0.0.a122.zip
@taverns-21-Jun-2013.zip
TConstruct_1.3.6.7.jar
ThermalExpansion-2.4.6.0.jar
@TurretMod_v3.0.1.jar
UpdateCheckerMod_1.5.2.zip
@Useful_Storage_(5-5)_v.1.8.1.zip
@WildCaves3-0.4.2.zip
WirelessRedstone-Universal-v1.7.zip
WirelessRedstone-PowerConfig-v1.0.zip
WirelessRedstone-Remote-v2.1.zip
WirelessRedstone-SlimeVoidAdditions-v1.0.zip
[1.5.2]bspkrsCorev2.04.zip
[1.5.2][Forge]Cartographer_1.3.zip
"""

    Anorak.universal_data += """
data/config
"""

    #CLIENT
    Anorak.client_coremods += """
CustomPortForge.jar
DynamicLights_1.5.2.jar
"""

    Anorak.client_mods += """
[1.5.2]_Mouse_Tweaks_1.2.zip
[1.5.2]StatusEffectHUDv1.10.zip
ExtendedRenderer_for_MC_v1.5.2.zip
HUDini_0-1-93_152.zip
InventoryTweaks-1.54b.jar
neiaddons-1.5.2-1.8.0.r23.jar
NEIPlugins-1.0.9.3.jar
ZansMinimap1.5.2.zip
data/VoxelMods
"""

    Anorak.client_data += """
data/options.txt
data/HUDini.conf
"""

    Anorak.modpack += """
fps15.zip
NoInfiniteWaterMC152.zip
NoLightUpdateLagMC152.zip
BACR v4 MC1,5,2.zip
"""

    #SERVER
    Anorak.server_coremods += """
forgebackup-universal-coremod-1.5.2-1.1.2.98.jar
"""

    Anorak.server_plugins += """
"""

    Anorak.server_mods += """
@Dynmap-1.7.1-forge-7.8.0.jar
"""

    Anorak.server += """
NoInfiniteWaterMC152.zip
"""

if __name__ == "__main__":
    #CONSTRUCT
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1].lower() != "false":
            Anorak.skipable(False)
    Define()
    Anorak.construct()
