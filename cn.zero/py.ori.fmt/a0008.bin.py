from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "a0008.bin",                # FileName
        "a0000",                    # MapName
        "a0008",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 320, 0, 13720, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "a0008",                  # 0
        "bttest03",               # 1
        "bttest03",               # 2
    ))

    ATBonus("ATBonus_114", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_154", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1D8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_1DC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_1E0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_1E4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 5, 5, 45)

    # monster count: 3

    BattleInfo(
        "BattleInfo_234", 0x0000, 3, 6, 90, 6, 1, 55, 0, "bttest03", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_1D4", "ed7400", "ed7000", "ATBonus_114"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_278", 0x0000, 3, 6, 45, 6, 1, 85, 0, "bttest03", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_1D4", "ed7400", "ed7000", "ATBonus_114"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "monster/ch60050.itc",               # 00
        "monster/ch60051.itc",               # 01
        "monster/ch60950.itc",               # 02
        "monster/ch60950.itc",               # 03
    ))

    DeclMonster(8990,    28620,   0,       0x1010000,    "BattleInfo_234", 0,   0,   0xFFFF, 0,  0)
    DeclMonster(10130,   30420,   0,       0x101002D,    "BattleInfo_278", 0,   0,   0xFFFF, 0,  0)
    DeclMonster(-46000,  74980,   0,       0x1010000,    "BattleInfo_278", 0,   2,   0xFFFF, 1,  1)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 1

    ScpFunction((
        "Function_0_2DC",          # 00, 0
        "Function_1_2DD",          # 01, 1
    ))


    def Function_0_2DC(): pass

    label("Function_0_2DC")

    Return()

    # Function_0_2DC end

    def Function_1_2DD(): pass

    label("Function_1_2DD")

    Return()

    # Function_1_2DD end

    SaveToFile()

Try(main)
