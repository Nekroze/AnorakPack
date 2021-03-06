from pakpak import Modpack

forge = "minecraftforge-universal-1.6.4-9.11.1.916.jar"
server = "minecraft_server.1.6.4.jar"

Anorak = Modpack(forge, server)
Anorak.server += forge

#Files preceded by '@' are not in the lite version of the modpack
def Define():
    #UNIVERSAL
    Anorak.universal_mods += """
@[1.6.4]BlockBreaker.Forge.1.6.4.r02.Universal.jar
@[1.6.4]bspkrsCorev5.0.zip
@[1.6.4]TreeCapitator.Forge.1.6.4.r06.Universal.jar
@1.6.2_Jammy_Furniture_Mod_V4.5.zip
@1.6.4.BetterStorage_0.7.2.38.zip
appeng-rv14-finale-mc16x.jar
@ArchimedesShips.zip
Atomic_Science_v1.0.0.155.jar
@BiblioCraft[v1.5.3].zip
@BiblioWoods[Forestry][v1.3].zip
@BiblioWoods[Natura][v1.1].zip
@binnie-mods-1.8-dev2.jar
Carpenter's Blocks v1.9.5 - MC 1.6+.zip
ChickenChunks 1.3.3.3.jar
CodeChickenCore 0.9.0.6.jar
ComputerCraft1.57.zip
Dark-AssemblyLine_v0.2.0.124.jar
Dark-CoreMachine_v0.2.0.124.jar
Dark-FarmTech_v0.2.0.124.jar
Dark-FluidMechanics_v0.2.0.124.jar
Dark-GreaterSecurity_v0.2.0.124.jar
ExtraCells-1.5.6d.jar
forestry-A-2.3.0.7.jar
Galacticraft-1.6.4-2.0.6.895.jar
Galacticraft-Planets-1.6.4-2.0.6.895.jar
@iChunUtil2.3.0.zip
ICBM_Contraption_v1.3.4.272.jar
ICBM_Explosion_v1.3.4.272.jar
ICBM_Sentry_v1.3.4.272.jar
iguanatweakstconstruct-1.6.X-1n.zip
immibis-core-57.1.5.jar
immibis-microblocks-57.3.0.jar
immibis-peripherals-57.0.0.jar
Improved Mob Spawn 1.4.3.zip
InventoryTweaks-MC1.6.2-1.56-b77.jar
Mekanism-v5.6.0.459.jar
MekanismGenerators-v5.6.0.497.jar
MekanismInduction-v5.6.0.497.jar
MekanismTools-v5.6.0.497.jar
MFFS_v3.4.0.237.jar
MicdoodleCore-1.6.4-2.0.6.895.jar
Minechem4-12.jar
miscperipherals-3.4b2.zip
MobiusCore_1.0.2.jar
ModularPowersuits-1.6.2-0.8.0-44.jar
@MultiMine_1.6.4.jar
@Natura_1.6.X_2.1.12.2.jar
neiaddons-1.6.2-1.9.3.r47.jar
NEIPlugins-1.1.0.5.jar
NotEnoughItems 1.6.1.5.jar
Numina-1.6.2-0.0.1-32.jar
Opis_1.0.5b_alpha.zip
@parachute-2.0.2-1.6.4.jar
ProjectRedBase-1.6.4-4.1.0.13.jar
ProjectRedCompat-1.6.4-4.1.0.13.jar
ProjectRedIntegration-1.6.4-4.1.0.13.jar
ProjectRedLighting-1.6.4-4.1.0.13.jar
ProjectRedWorld-1.6.4-4.1.0.13.jar
@RopePlus_1.6.4.zip
slick-util.jar
SmoothBedrock-1.6.4-1.0.6.jar
TConstruct_1.6.4_1.5.1.jar
TMechworks_1.6.4_0.1.2.jar
@ToolBelts 1.6.4 v3.zip
@UpdateCheckerMod_1.6.4.zip
Waila_1.4.1.zip
WR-CBE 1.4.0.6.jar
"""

    Anorak.universal_data += """
data/config
"""

    #CLIENT
    Anorak.client_mods += """
[1.6.4] Mouse Tweaks 2.3.4.zip
@3DBlocksMod-1.6.4.1.jar
@BetterGrassAndLeavesMod[v1.6.4.D].jar
@BetterSignsMod[v1.6.4.B].jar
DynamicLights_1.6.4.jar
@MobAmputation2.0.0.zip
@MobDismemberment2.0.0.zip
NoJumpMod1.6_3.zip
noVoidFogNoDimmingModloaderForge1.6.4.zip
Zyins_HUD__1.6.4__v.1.1.0.zip
"""

    Anorak.client_data += """
data/options.txt
"""

    Anorak.modpack += """
"""

    #SERVER
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
