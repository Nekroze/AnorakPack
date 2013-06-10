from pakpak import Modpack

forge = "minecraftforge-universal-1.5.2-7.8.0.725.zip"
server = "minecraft_server_1.5.2.jar"

Anorak = Modpack(forge, server)
Anorak.server += forge

#UNIVERSAL
Anorak.universal_coremods += """
[1.5.2]TreeCapitator.Forge.1.5.2.r01.Uni.CoreMod.jar
Chemcraft Core 1.3.0.jar
CodeChickenCore_0.8.6.12.jar
CoFHCore-1.5.2.2.jar
Galacticraft-1.5.2-a0.1.35.300.jar
immibis-microblocks-55.0.1.jar
MultiMine_1.5.2.jar
NotEnoughItems_1.5.2.21.jar
PowerCrystalsCore-1.1.6-107.jar
StalkerCreepers_1.5.2.jar
Snowfall 1.2.1.jar
"""

Anorak.universal_mods += """
1.5.2_Jammy_Furniture_Mod_V4.4.zip
1.5.2BetterBreeding.zip
AdvancedMachines_1.5.2.zip
AdvancedPowerManagement-1.2.68-IC2-1.115.jar
appeng-rv10-n.zip
AssemblyLine_v0.3.5.142.jar
Atomic_Science_v0.5.3.51.jar
BaMsDoubledoor_v2.0_for_1.5.2_ForgeMod.zip
BiblioCraft[v1.2.3].zip
Carpenter's_Slope_v1.25_-_MC_1.5+.zip
ChickenChunks_1.3.2.10.jar
chisel-1.5.2-1.4.4.jar
CompactWindmills+v.1.0.1.3.jar
ComplexMachines_v0.3.3.92.jar
ComputerCraft1.53.zip
ConfigMod_for_MC_v1.5.2.zip
coral-reef-universal-1.5.2-r2.zip
CoroAI_for_MC_v1.5.2.zip
DimensionalDoors-1.5.2R1.3.6RC1-71.zip
ElectricExpansion_v2.3.0.51.jar
enhanced-portals_2.1.2.jar
ExtrabiomesXL-universal-1.5.2-3.13.1.jar
Extra Doors by Zolandre[Forge][v1.3.1].zip
Factorization-0.7.37.jar
FluidMechanics_v0.5.1.99.jar
Frames-1.5.2-5.0.zip
GregsLighting-1.8.1-7.jar
HangableMaps_v1.5.2_1_MC1.5.2.zip
ICBM_Contraption_v1.2.0.130.jar
ICBM_Explosion_v1.2.0.130.jar
ICBM_Sentry_v1.2.0.130.jar
iChunUtil1.0.1.zip
immibis-core-55.1.3.jar
immibis-peripherals-55.0.1.jar
Improved_Mob_Spawn_1.4.0.zip
industrialcraft-2_1.115.340-lf.jar
industrialcraft2comboarmors-1.14.1.zip
InfernalMobs_1.5.2.zip
invasion_mod_0.11.7.zip
ironchest-universal-1.5.2-5.2.6.425.zip
Mekanism-v5.5.6.76.jar
MekanismGenerators-v5.5.6.76.jar
MekanismTools-v5.5.6.76.jar
MFFS_v3.0.2.124.jar
MineChem_v3.0.0.196.jar
MineFactoryReloaded-2.6.2-924.jar
MineForever_0.2.0b.jar
miscperipherals-3.3.jar
ModularPowersuits-0.7.0-534.jar
MPSA-0.2.3-144_MPS-531+.jar
More Pistons - 1.5.2 - 1.3.3 build Smeagol.zip
mod_AdvancedSolarPanels_3_3_7.zip
mod_zGraviSuite_1_9_2.zip
MoreGlowstone v1.0 (1.5.2).zip
Mutant_Creatures_v1.3.4_mc1.5.2.zip
Natura_2.0.21.jar
NetherOres-2.1.5-75.jar
OmniTools-3.1.4.0.jar
OpenCCSensors-1.5.2.0.jar
OpenPeripheral-0.0.7.jar
OpenXP-0.0.6.jar
Painter's_Flower_Pot_v1.56_-_MC_1.5+.zip
Panicle_Craft-v1.0.0.4b.zip
PortalGun1.5.2.zip
Railcraft_1.5.2-7.2.1.0.jar
RancraftPengForge_v152l.zip
Rotten_Flesh_To_Leather_MC_1.5.2.zip
SAP_ManPack_v142.jar
SecretRoomsMod-universal-4.6.0.283.zip
Securecraft 1.1.0.zip
SimplyHorses_1.5.2_pre6.3.zip
SkullForge.zip
StevesCarts2.0.0.a117.zip
TConstruct_1.3.3.15.jar
TurretMod_v3.0.1.jar
UpdateCheckerMod_1.5.2.zip
UsefulFood-1.5.1_1.4.2-universal.zip
Useful_Storage_(5-5)_v.1.8.1.zip
Wallpaper-1.5.2-5.0.zip
Weather_v1.5_Mod_for_MC_v1.5.2.zip
WildCaves3-0.4.2.zip
Zombie Awareness v1.85 Mod for MC v1.5.2.zip
[1.5.2]BetterStorage_0.6.1.18.zip
[1.5.2]bspkrsCorev2.04.zip
[1.5.2]ProjectBench-v1.7.5.zip
"""

Anorak.universal_data += """
data/config
"""

#CLIENT
Anorak.client_coremods += """
CustomPortForge.jar
DynamicLights_1.5.2.jar
ShoulderSurfing_1.4.0_1.5.2_COREMOD.jar
"""

Anorak.client_mods += """
[1.5.2]_Mouse_Tweaks_1.2.zip
[1.5.2]StatusEffectHUDv1.10.zip
ExtendedRenderer_for_MC_v1.5.2.zip
HUDini_152_019d.zip
InventoryTweaks-1.54b.jar
neiaddons-1.5.2-1.7.r17.jar
NEIPlugins-1.0.9.1a.jar
Animated Player v1.2.0 mc1.5.2.zip
ZansMinimap1.5.2.zip
data/VoxelMods
"""

Anorak.client_data += """
data/options.txt
data/optionsof.txt
data/HUDini.conf
"""

Anorak.modpack += """
OptiFine_1.5.2_HD_U_D3.zip
fps15.zip
NoInfiniteWaterMC152.zip
NoLightUpdateLagMC152.zip
BACR v4 MC1,5,2.zip
"""

#SERVER
Anorak.server_coremods += """
forgebackup-universal-coremod-1.5.2-1.1.2.98.jar
"""

Anorak.server_mods += """
Dynmap-1.7.1-forge-7.8.0.jar
"""

Anorak.server += """
NoInfiniteWaterMC152.zip
"""

#CONSTRUCT
Anorak.construct()
