from pakpak import Modpack

forge = "minecraftforge-universal-1.5.2-7.8.0.716.zip"
server = "minecraft_server_1.5.2.jar"

Anorak = Modpack(forge, server)
Anorak.server += forge

#UNIVERSAL
Anorak.universal_coremods += """
[1.5.2]TreeCapitator.Forge.1.5.2.r01.Uni.CoreMod.jar
CodeChickenCore_0.8.6.12.jar
CoFHCore-1.5.2.2.jar
immibis-microblocks-55.0.1.jar
MultiMine_1.5.2.jar
NotEnoughItems_1.5.2.21.jar
PowerCrystalsCore-1.1.6-107.jar
StalkerCreepers_1.5.2.jar
Snowfall 1.2.1.jar
Chemcraft Core 1.3.0.jar
"""

Anorak.universal_mods += """
1.5.2_Jammy_Furniture_Mod_V4.4.zip
AdditionalPipes2.3.0-BC3.5.3.jar
adv-repulsion-systems-55.1.2.jar
AdvancedMachines_1.5.2.zip
AdvancedPowerManagement-1.2.68-IC2-1.115.jar
appeng-rv10-n.zip
BaMsDoubledoor_v2.0_for_1.5.2_ForgeMod.zip
bcTools-v13c.zip
BiblioCraft[v1.2.3].zip
buildcraft-A-3.6.0.jar
buildcraft-Z-additional-buildcraft-objects-1.0.4.150.jar
Carpenter's_Slope_v1.25_-_MC_1.5+.zip
ChickenChunks_1.3.2.10.jar
CompactWindmills+v.1.0.1.3.jar
ComputerCraft1.53.zip
ConfigMod_for_MC_v1.5.2.zip
coral-reef-universal-1.5.2-r2.zip
CoroAI_for_MC_v1.5.2.zip
DimensionalDoors-1.5.2R1.3.6RC1-71.zip
EnderStorage_1.4.2.10.jar
enhanced-portals_2.1.2.jar
Extinguisher_V1.zip
extra-bees-1.6-pre10.jar
ExtrabiomesXL-universal-1.5.2-3.13.1.jar
Extra Doors by Zolandre[Forge][v1.3.1].zip
Factorization-0.7.37.jar
FlatBedrock-1.1.1-32.jar
forestry-A-2.2.6.2.jar
GregsLighting-1.8.1-7.jar
HangableMaps_v1.5.2_1_MC1.5.2.zip
HUDini_152_019d.zip
iChunUtil1.0.1.zip
immibis-core-55.1.2.jar
immibis-peripherals-55.0.1.jar
Improved_Mob_Spawn_1.4.0.zip
industrialcraft-2_1.115.340-lf.jar
industrialcraft2comboarmors-1.14.1.zip
InfernalMobs_1.5.2.zip
invasion_mod_0.11.7.zip
ironchest-universal-1.5.2-5.2.6.425.zip
Lanterns_1.3.4_Universal.zip
LiquidEnergy_Beta5.zip
LogisticsPipes-MC1.5.2-0.7.3.3.jar
mca_v3.3.5.zip
MineChem_v3.0.0.138.jar
MineFactoryReloaded-2.6.1-897.jar
MineForever_0.2.0b.jar
miscperipherals-3.3.jar
mod_AdvancedSolarPanels_3_3_7.zip
mod_zGraviSuite_1_9_2.zip
More Backpacks 2.1.0.zip
MoreGlowstone v1.0 (1.5.2).zip
Mutant_Creatures_v1.3.4_mc1.5.2.zip
Natura_2.0.21.jar
NetherOres-2.1.4-71.jar
OmniTools-3.1.4.0.jar
OpenCCSensors-1.5.2.0.jar
OpenPeripheral-0.0.7.jar
OpenXP-0.0.6.jar
Painter's_Flower_Pot_v1.56_-_MC_1.5+.zip
PortalGun1.5.2.zip
PowerConverters-2.3.0-54.jar
ProSthetics_v_0.0.1.8_(MC_1.5.2).zip
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
ThermalExpansion-2.4.3.0.jar
TurretMod_v3.0.1.jar
UpdateCheckerMod_1.5.2.zip
UsefulFood-1.5.1_1.4.2-universal.zip
Useful_Storage_(5-5)_v.1.8.1.zip
Weather_v1.5_Mod_for_MC_v1.5.2.zip
WildCaves3-0.4.2.zip
Zombie Awareness v1.85 Mod for MC v1.5.2.zip
[1.5.2]bspkrsCorev2.04.zip
[1.5.2]ProjectBench-v1.7.5.zip
"""

Anorak.universal_data += """
data/config
data/BODprops
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
InventoryTweaks-1.54b.jar
MobAmputation1.5.2v1.zip
MobDismemberment1.5.2v1.zip
neiaddons-1.5.2-1.7.r17.jar
NEIPlugins-1.0.9.1a.jar
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
Better_Ore_Distribution(V2.6)MC(1.5.2).zip
"""

#SERVER
Anorak.server_coremods += """
forgebackup-universal-coremod-1.5.2-1.1.2.98.jar
"""

Anorak.server_mods += """
Dynmap-1.7.1-forge-7.8.0.jar
"""

Anorak.server += """
Better_Ore_Distribution(V2.6_SMP)MC(1.5.2).zip
"""

#CONSTRUCT
Anorak.construct()
