from pakpak import Modpack

forge = "minecraftforge-universal-1.5.2-7.8.0.734.zip"
server = "minecraft_server_1.5.2.jar"

Anorak = Modpack(forge, server)
Anorak.server += forge


def Define():
	#UNIVERSAL
	Anorak.universal_coremods += """
[1.5.2]TreeCapitator.Forge.1.5.2.r01.Uni.CoreMod.jar
Chemcraft Core 1.3.0.jar
CodeChickenCore 0.8.7.jar
CoFHCore-1.5.2.4.jar
denLib-1.5.2-3.0.14.jar
Galacticraft-1.5.2-a0.1.35.309.jar
immibis-microblocks-55.0.1.jar
MultiMine_1.5.2.jar
NotEnoughItems 1.5.2.28.jar
PowerCrystalsCore-1.1.6-107.jar
@StalkerCreepers_1.5.2.jar
Snowfall 1.2.1.jar
"""

	Anorak.universal_mods += """
1.5.2_Jammy_Furniture_Mod_V4.4.zip
1.5.2BetterBreeding.zip
appeng-rv10-n.zip
Atomic_Science_v0.5.3.51.jar
BaMsDoubledoor_v2.0_for_1.5.2_ForgeMod.zip
BiblioCraft[v1.2.3].zip
Carpenter's_Slope_v1.25_-_MC_1.5+.zip
ChickenChunks 1.3.2.12.jar
chisel-1.5.2-1.4.4.jar
ComplexMachines_v0.3.3.93.jar
ComputerCraft1.53.zip
ConfigMod_for_MC_v1.5.2.zip
coral-reef-universal-1.5.2-r2.zip
CoroAI_for_MC_v1.5.2.zip
DimensionalDoors-1.5.2R1.3.6RC1-71.zip
Dungeon Mobs v2.6.0.zip
DungeonPack 1.5.2 v3 Universal.zip
enhanced-portals_2.1.2.jar
extra-bees-1.6-pre13.jar
Extra Doors by Zolandre[Forge][v1.3.1].zip
Factorization-0.7.37.jar
forestry-A-2.2.6.3.jar
Frames-1.5.2-5.0.zip
GregsLighting-1.8.1-7.jar
growthcraft-apples-1.5.2-4.0.zip
growthcraft-core-1.5.2-1.0.zip
growthcraft-core-booze-1.5.2-1.1.zip
growthcraft-fishnet-1.5.2-4.1.zip
growthcraft-flowers-1.5.2-5.2.zip
growthcraft-grapes-1.5.2-4.0.zip
growthcraft-hops-1.5.2-2.0.zip
HangableMaps_v1.5.2_1_MC1.5.2.zip
ICBM_Contraption_v1.2.0.133.jar
ICBM_Explosion_v1.2.0.133.jar
ICBM_Sentry_v1.2.0.133.jar
iChunUtil1.0.1.zip
immibis-core-55.1.3.jar
immibis-peripherals-55.0.1.jar
Improved_Mob_Spawn_1.4.0.zip
InfernalMobs_1.5.2.zip
invasion_mod_0.11.7.zip
ironchest-universal-1.5.2-5.2.6.425.zip
Lanterns_1.3.4_Universal.zip
Mekanism-v5.5.6.76.jar
MekanismGenerators-v5.5.6.76.jar
MekanismTools-v5.5.6.76.jar
MFFS_v3.0.3.129.jar
MineChem_v3.0.0.214.jar
MineFactoryReloaded-2.6.2-924.jar
MineForever_0.2.0b.jar
miscperipherals-3.3.jar
ModularPowersuits-0.7.0-534.jar
MPSA-0.2.3-144_MPS-531+.jar
More Pistons - 1.5.2 - 1.3.3 build Smeagol.zip
MoreGlowstone v1.0 (1.5.2).zip
Mutant_Creatures_v1.3.4_mc1.5.2.zip
Natura_2.0.21.jar
NetherOres-2.1.5-75.jar
OmniTools-3.1.5.0.jar
OpenCCSensors-1.5.2.0.jar
OpenPeripheral-0.0.7.jar
OpenXP-0.0.6.jar
Painter's_Flower_Pot_v1.56_-_MC_1.5+.zip
Panicle_Craft-v1.0.0.4b.zip
PluginsforForestry-1.5.2-3.0.16.jar
PortalGun1.5.2.zip
Railcraft_1.5.2-7.2.1.0.jar
RancraftPengForge_v152l.zip
Rotten_Flesh_To_Leather_MC_1.5.2.zip
SAP_ManPack_v142.jar
SecretRoomsMod-universal-4.6.0.283.zip
Securecraft 1.1.0.zip
SGCraft-0.5.1-mc1.5.1.jar
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
HUDini_152_019d.zip
InventoryTweaks-1.54b.jar
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
@fps15.zip
@NoInfiniteWaterMC152.zip
@NoLightUpdateLagMC152.zip
@BACR v4 MC1,5,2.zip
"""

	#SERVER
	Anorak.server_coremods += """
forgebackup-universal-coremod-1.5.2-1.1.2.98.jar
"""

	Anorak.server_mods += """
@Dynmap-1.7.1-forge-7.8.0.jar
"""

	Anorak.server += """
@NoInfiniteWaterMC152.zip
"""

if __name__ == "__main__":
	#CONSTRUCT
	import sys
	if len(sys.argv) > 1:
		if sys.argv[1].lower() == "false":
			Anorak.skipable(False)
	Define()
	Anorak.construct()
