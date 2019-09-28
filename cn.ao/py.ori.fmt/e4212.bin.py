from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4212.bin",                # FileName
        "e4212",                    # MapName
        "e4212",                    # Location
        0x00D2,                     # MapIndex
        "ed7251",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x07,                       # PreInitFunctionIndex
        b'\x00\xff\x00',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e4212",                  # 0
        "艾丝蒂尔",               # 1
        "约修亚",                 # 2
        "玲",                     # 3
        "神机３",                 # 4
        "帕蒂尔·玛蒂尔",         # 5
        "帕蒂尔·玛蒂尔影子",     # 6
        "短剑目标",               # 7
        "导弹目标",               # 8
        "导弹目标",               # 9
        "导弹目标",               # 10
        "导弹目标",               # 11
        "导弹目标",               # 12
        "导弹目标",               # 13
        "艾丝蒂尔",               # 14
        "空",                     # 15
        "SE控制",                 # 16
        "br1060",                 # 17
    ))

    ATBonus("ATBonus_398", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_4BCD", 5,   5,   5,   5,   5,   5,   5)

    MonsterBattlePostion("MonsterBattlePostion_3F8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_45C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_460", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_464", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_468", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_46C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_470", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 2, 13, 180)

    # monster count: 4

    BattleInfo(
        "BattleInfo_478", 0x0000, 50, 6, 60, 8, 1, 60, 0, "br1060", "Sepith_4BCD", 30, 40, 20, 10,
        (
            ("ms80800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F8", "MonsterBattlePostion_458", "ed7450", "ed7453", "ATBonus_398"),
            ("ms80800.dat", "ms80800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D8", "MonsterBattlePostion_458", "ed7450", "ed7453", "ATBonus_398"),
            ("ms80800.dat", "ms80800.dat", "ms80800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F8", "MonsterBattlePostion_458", "ed7450", "ed7453", "ATBonus_398"),
            ("ms80800.dat", "ms80800.dat", "ms80800.dat", "ms80800.dat", 0, 0, 0, 0, "MonsterBattlePostion_3D8", "MonsterBattlePostion_458", "ed7450", "ed7453", "ATBonus_398"),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch80850.itc",               # 10
        "monster/ch80851.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(880,     -1780,   0,       0x10100C3,    "BattleInfo_478", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-31040,  -10650,  0,       0x1010069,    "BattleInfo_478", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-50650,  -23740,  10,      0x101011D,    "BattleInfo_478", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-85890,  -28760,  0,       0x101004B,    "BattleInfo_478", 0,   16,  0xFFFF, 0,  1)

    DeclActor(-72300,  0,       -6700,   1200,    -72300,  1000,    -6700,   0x007C, 0,  3,  0x0000)
    DeclActor(10780,   100,     -16350,  1200,    10780,   1100,    -16350,  0x007C, 0,  4,  0x0000)
    DeclActor(-43270,  0,       -27850,  1500,    -43270,  1500,    -27850,  0x007C, 0,  72, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1

    ScpFunction((
        "Function_0_67C",          # 00, 0
        "Function_1_6AA",          # 01, 1
        "Function_2_6CB",          # 02, 2
        "Function_3_B77",          # 03, 3
        "Function_4_CB2",          # 04, 4
        "Function_5_DED",          # 05, 5
        "Function_6_E1C",          # 06, 6
        "Function_7_25C0",         # 07, 7
        "Function_8_2652",         # 08, 8
        "Function_9_267F",         # 09, 9
        "Function_10_2778",        # 0A, 10
        "Function_11_2800",        # 0B, 11
        "Function_12_28F0",        # 0C, 12
        "Function_13_29CF",        # 0D, 13
        "Function_14_29E3",        # 0E, 14
        "Function_15_2A01",        # 0F, 15
        "Function_16_2A33",        # 10, 16
        "Function_17_2A6F",        # 11, 17
        "Function_18_2AD6",        # 12, 18
        "Function_19_2B10",        # 13, 19
        "Function_20_2CD5",        # 14, 20
        "Function_21_2FB8",        # 15, 21
        "Function_22_306E",        # 16, 22
        "Function_23_30E0",        # 17, 23
        "Function_24_3104",        # 18, 24
        "Function_25_31BE",        # 19, 25
        "Function_26_327E",        # 1A, 26
        "Function_27_3356",        # 1B, 27
        "Function_28_337A",        # 1C, 28
        "Function_29_339D",        # 1D, 29
        "Function_30_3477",        # 1E, 30
        "Function_31_34B4",        # 1F, 31
        "Function_32_34F1",        # 20, 32
        "Function_33_351B",        # 21, 33
        "Function_34_3544",        # 22, 34
        "Function_35_35FE",        # 23, 35
        "Function_36_3618",        # 24, 36
        "Function_37_362A",        # 25, 37
        "Function_38_3734",        # 26, 38
        "Function_39_3762",        # 27, 39
        "Function_40_398B",        # 28, 40
        "Function_41_3A1C",        # 29, 41
        "Function_42_3A34",        # 2A, 42
        "Function_43_3DE3",        # 2B, 43
        "Function_44_3E46",        # 2C, 44
        "Function_45_3E91",        # 2D, 45
        "Function_46_3F64",        # 2E, 46
        "Function_47_3FD0",        # 2F, 47
        "Function_48_408D",        # 30, 48
        "Function_49_40AD",        # 31, 49
        "Function_50_418F",        # 32, 50
        "Function_51_4214",        # 33, 51
        "Function_52_4338",        # 34, 52
        "Function_53_4351",        # 35, 53
        "Function_54_4544",        # 36, 54
        "Function_55_472F",        # 37, 55
        "Function_56_4746",        # 38, 56
        "Function_57_4757",        # 39, 57
        "Function_58_4818",        # 3A, 58
        "Function_59_4842",        # 3B, 59
        "Function_60_488A",        # 3C, 60
        "Function_61_489D",        # 3D, 61
        "Function_62_497A",        # 3E, 62
        "Function_63_498F",        # 3F, 63
        "Function_64_49B3",        # 40, 64
        "Function_65_49D7",        # 41, 65
        "Function_66_4A09",        # 42, 66
        "Function_67_4A2D",        # 43, 67
        "Function_68_4A66",        # 44, 68
        "Function_69_4A8C",        # 45, 69
        "Function_70_4AA0",        # 46, 70
        "Function_71_4AC5",        # 47, 71
        "Function_72_4AEA",        # 48, 72
    ))


    def Function_0_67C(): pass

    label("Function_0_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_697")
    SetMapObjFlags(0x0, 0x2000000)
    SetMapObjFlags(0x1, 0x2000000)
    Jump("loc_6A9")

    label("loc_697")

    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)

    label("loc_6A9")

    Return()

    # Function_0_67C end

    def Function_1_6AA(): pass

    label("Function_1_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6B5")
    OP_E2(0x1)

    label("loc_6B5")

    ClearScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6CA")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 6)

    label("loc_6CA")

    Return()

    # Function_1_6AA end

    def Function_2_6CB(): pass

    label("Function_2_6CB")

    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A69")
    SetMapObjFrame(0xFF, "mae00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maewood", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekusa00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekusa01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekusa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekage", 0x0, 0x1)
    Jump("loc_AC3")

    label("loc_A69")

    SetMapObjFrame(0xFF, "ato00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "atokizu_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "atokumo_add", 0x0, 0x1)

    label("loc_AC3")

    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3E")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -43270, 0, -27850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5B")
    OP_70(0x7, 0x0)
    Jump("loc_B5F")

    label("loc_B5B")

    OP_70(0x7, 0x1E)

    label("loc_B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B72")
    OP_70(0x8, 0x0)
    Jump("loc_B76")

    label("loc_B72")

    OP_70(0x8, 0x1E)

    label("loc_B76")

    Return()

    # Function_2_6CB end

    def Function_3_B77(): pass

    label("Function_3_B77")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C69")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('爆灵宝玉', 1)"), scpexpr(EXPR_END)), "loc_BFA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F6, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_C64")

    label("loc_BFA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C64")

    Jump("loc_CA6")

    label("loc_C69")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_CA6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_B77 end

    def Function_4_CB2(): pass

    label("Function_4_CB2")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA4")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('邪恶胸甲', 1)"), scpexpr(EXPR_END)), "loc_D35")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5EE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F6, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_D9F")

    label("loc_D35")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x5EE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x5EE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D9F")

    Jump("loc_DE1")

    label("loc_DA4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_DE1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_CB2 end

    def Function_5_DED(): pass

    label("Function_5_DED")

    OP_8A(0x0)
    OP_8A(0x1)
    LoadEffect(0x0, "event/ev600_00.eff")
    LoadEffect(0x1, "event/ev600_01.eff")
    Return()

    # Function_5_DED end

    def Function_6_E1C(): pass

    label("Function_6_E1C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    OP_F3(100000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    LoadChrToIndex("apl/ch50547.itc", 0x22)
    LoadChrToIndex("apl/ch50338.itc", 0x23)
    LoadChrToIndex("chr/ch00650.itc", 0x24)
    LoadChrToIndex("chr/ch00651.itc", 0x25)
    LoadChrToIndex("chr/ch00750.itc", 0x26)
    LoadChrToIndex("chr/ch00701.itc", 0x27)
    LoadChrToIndex("chr/ch00752.itc", 0x28)
    LoadChrToIndex("apl/ch50338.itc", 0x29)
    LoadChrToIndex("chr/ch09556.itc", 0x2A)
    LoadChrToIndex("chr/ch00653.itc", 0x2B)
    LoadChrToIndex("chr/ch00753.itc", 0x2C)
    LoadChrToIndex("apl/ch51724.itc", 0x2D)
    LoadChrToIndex("apl/ch51725.itc", 0x2E)
    LoadEffect(0x2, "event/ev10018.eff")
    LoadEffect(0x0, "event/eva01_01.eff")
    LoadEffect(0x3, "event/ev17045.eff")
    LoadEffect(0x4, "event/ev17043.eff")
    LoadEffect(0x5, "event/ev17040.eff")
    LoadEffect(0x6, "event/ev17041.eff")
    LoadEffect(0x7, "battle/mgaria0.eff")
    LoadEffect(0x8, "event/ev17063.eff")
    LoadEffect(0x9, "event/ev15040.eff")
    LoadEffect(0xA, "event/ev17044.eff")
    SoundLoad(852)
    SoundLoad(979)
    SoundLoad(579)
    SoundLoad(931)
    SoundLoad(904)
    SoundLoad(996)
    SoundLoad(993)
    SoundLoad(288)
    SoundLoad(902)
    SoundLoad(1042)
    SoundLoad(1043)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x1, 0x1000)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -50000, 0, -15000, 0)
    OP_74(0x1, 0x1E)
    OP_78(0x1, 0xB)
    OP_93(0xB, 0x10E, 0x0)
    SetChrFlags(0xB, 0x1)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x172, 0x19A, 0x0, 0x20)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -66000, 0, -15000, 0)
    OP_74(0x0, 0x1E)
    OP_78(0x0, 0xC)
    OP_93(0xC, 0x5A, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x1)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1A5, 0x1CC, 0x1, 0x20)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x22)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x1000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, -56000, 2000, -35000, 0)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -54000, 2000, -37000, 0)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -58000, 2000, -37000, 0)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    OP_11(0xD0, 0xD0, 0xFF, 0x1E, 0xC8, 0x0)
    Sound(979, 2, 40, 0)
    FadeToBright(1000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1533")
    OP_68(-62000, 3000, -15000, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40380, 0)
    OP_68(-53000, 4000, -15000, 2500)
    MoveCamera(38, 11, 0, 2500)
    OP_6E(600, 2500)
    SetCameraDistance(23940, 2500)
    BeginChrThread(0xC, 0, 0, 8)
    BeginChrThread(0xB, 0, 0, 9)
    OP_6F(0x79)
    Sleep(500)
    OP_68(-57750, 5600, -5920, 700)
    MoveCamera(342, 9, 0, 700)
    OP_6E(600, 700)
    SetCameraDistance(26560, 700)
    OP_6F(0x79)
    WaitChrThread(0xB, 0)
    OP_68(-58600, 5800, -6520, 0)
    MoveCamera(315, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23030, 0)
    Fade(500)
    BeginChrThread(0xB, 0, 0, 14)
    Sleep(2500)
    OP_0D()
    EndChrThread(0xB, 0x0)
    BeginChrThread(0xB, 0, 0, 15)
    OP_68(-54000, 1000, -14000, 0)
    MoveCamera(5, 7, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(34750, 0)
    Fade(500)
    OP_68(-54000, 900, -14000, 6000)
    MoveCamera(5, 6, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(32750, 6000)
    OP_0D()

    #C0007
    ChrTalk(
        0x8,
        (
            "#00807F#12P呼……呼……\x01",
            "好厉害的家伙……！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "#00901F#6P莫非『至宝』给它\x01",
            "提供了无限的能源……！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xA,
        (
            "#03301F#6P绝不能输……『帕蒂尔·玛蒂尔』\x01",
            "才不会输给你这种东西……！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xA, 1, 0, 63)
    WaitChrThread(0xA, 1)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0010
    ChrTalk(
        0xA,
        (
            "#03307F#6P#4S玲、艾丝蒂尔和约修亚\x01",
            "也绝对不会输给你的！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0xB, 0x0)
    OP_68(-50160, 1900, 6630, 0)
    MoveCamera(13, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44520, 0)
    Fade(500)
    BlurSwitch(0x12C, 0x66FFFFFF, 0x0, 0x1, 0xA)
    EndChrThread(0xB, 0x0)
    BeginChrThread(0xB, 0, 0, 16)
    BeginChrThread(0xC, 0, 0, 17)
    Sleep(700)
    OP_68(-52350, 5000, -15600, 2800)
    MoveCamera(10, 4, 0, 2800)
    OP_6E(600, 2800)
    SetCameraDistance(18900, 2800)
    Sleep(1000)
    WaitChrThread(0xB, 0)
    Sound(955, 0, 100, 0)
    BeginChrThread(0xB, 0, 0, 18)
    OP_0D()
    OP_6F(0x79)
    CancelBlur(1000)
    OP_68(-52350, 4800, -15600, 1500)
    MoveCamera(10, -3, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(28620, 1500)
    Sleep(1400)

    #C0011
    ChrTalk(
        0xA,
        "#03305F#6P#N#8A啊……！\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        "#00813F#12P#6A呜……！\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        "#00907F#6P#6A啊！\x02",
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_15BC")

    label("loc_1533")

    OP_68(-52350, 4800, -15600, 0)
    MoveCamera(10, -3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28620, 0)
    SetChrPos(0xD, -59300, 0, -5200, 0)
    SetChrPos(0xC, -59300, 0, -5200, 0)
    OP_93(0xC, 0x96, 0x0)
    OP_70(0x0, 0x172)
    SetChrPos(0xB, -51790, 0, -13210, 0)
    OP_93(0xB, 0xBE, 0x0)
    BeginChrThread(0xB, 0, 0, 18)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x212, 0x23A, 0x1, 0x20)

    label("loc_15BC")

    EndChrThread(0xB, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB2")
    Fade(500)
    OP_68(-55340, 2300, -33310, 0)
    MoveCamera(9, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15200, 0)
    BeginChrThread(0xB, 0, 0, 20)
    OP_0D()
    BeginChrThread(0x8, 0, 0, 21)
    BeginChrThread(0x9, 0, 0, 26)
    Sleep(1300)
    OP_68(-58120, 2900, -30280, 2200)
    MoveCamera(31, 14, 0, 2200)
    OP_6E(600, 2200)
    SetCameraDistance(21710, 2200)
    Sleep(3100)
    StopSound(579, 500, 50)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xC, 0x1)
    BeginChrThread(0xC, 0, 0, 27)
    Sleep(100)
    OP_68(-52100, 1900, -4660, 2000)
    MoveCamera(24, 18, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(29090, 2000)
    Sleep(1000)
    EndChrThread(0xB, 0x0)
    BeginChrThread(0xB, 1, 0, 32)
    OP_6F(0x79)
    Sleep(900)
    OP_68(-54160, 4300, -12890, 2000)
    MoveCamera(18, 25, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(22290, 2000)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    WaitChrThread(0xC, 0)
    Fade(500)
    OP_68(-53020, 6100, -12900, 0)
    MoveCamera(29, 0, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11160, 0)
    OP_0D()
    BeginChrThread(0xC, 0, 0, 30)
    Sleep(150)
    Sound(833, 0, 100, 0)
    Sound(880, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -53870, 3600, -12640, 286, 90, 0, 1000, 1400, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 31)
    Sleep(700)
    BeginChrThread(0xC, 0, 0, 30)
    Sleep(150)
    Sound(833, 0, 100, 0)
    Sound(880, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -53490, 3600, -12980, 283, 90, 0, 1000, 1400, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 31)
    ClearMapObjFlags(0x1, 0x20)
    Sleep(700)
    Sound(655, 0, 50, 0)
    OP_87(0x8, 0xFF, 0x1, "Null_eyes(76)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1000)
    OP_68(-54250, 4900, -15110, 0)
    MoveCamera(40, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17850, 0)
    Fade(500)
    Sound(905, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_74(0x0, 0x1E)
    OP_71(0x1, 0x316, 0x334, 0x1, 0x0)
    OP_79(0x1)
    Sound(951, 0, 100, 0)
    OP_0D()
    Sound(833, 0, 100, 0)
    Sound(876, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -52750, 5300, -12960, 288, 90, 0, 1050, 2500, 1050, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x12C, 0x77FFFFFF, 0x0, 0x1, 0xA)
    BeginChrThread(0xC, 1, 0, 33)

    def lambda_18B0():
        OP_93(0xFE, 0x109, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_18B0)

    def lambda_18BD():
        OP_93(0xFE, 0xE1, 0xC8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_18BD)
    Sound(905, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x28B, 0x294, 0x1, 0x0)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    CancelBlur(500)
    BeginChrThread(0xC, 3, 0, 34)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x334, 0x348, 0x1, 0x0)
    OP_79(0x1)
    Sound(1019, 0, 100, 0)
    OP_74(0x1, 0xF)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x348, 0x366, 0x1, 0x0)
    OP_71(0x0, 0x294, 0x2B2, 0x1, 0x0)
    Sleep(400)
    OP_68(-55920, 4900, -15970, 1000)
    MoveCamera(21, 27, 0, 1000)
    OP_6E(600, 1000)
    SetCameraDistance(17850, 1000)
    Sleep(700)
    Sound(200, 0, 100, 0)
    Sound(902, 0, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x4B0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -57750, 150, -14660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0xD, -58930, 150, -15120, 0)
    ClearChrFlags(0xD, 0x8)
    OP_79(0x1)
    OP_79(0x0)
    OP_6F(0x79)
    Fade(500)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -65200, 4000, -40600, 30)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -66000, 4000, -39000, 30)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, -65750, 4000, -40000, 30)
    OP_68(-62830, 7700, -33780, 0)
    MoveCamera(26, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(10200, 0)
    OP_68(-62830, 4700, -33780, 2500)
    MoveCamera(25, 8, 0, 2500)
    OP_6E(600, 2500)
    SetCameraDistance(16610, 2500)
    OP_0D()
    Sleep(2000)

    #C0014
    ChrTalk(
        0x8,
        "#00807F#6P啊……！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xA,
        "#03311F#N#6P『帕蒂尔·玛蒂尔』！？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    #C0016
    ChrTalk(
        0xA,
        "#03307F#6P#5S你这混蛋！！！\x02",
    )

    CloseMessageWindow()
    OP_68(-62830, 3300, -33780, 700)
    MoveCamera(25, 14, 0, 700)
    OP_6E(600, 700)
    SetCameraDistance(16610, 700)
    Sleep(300)
    BeginChrThread(0xA, 0, 0, 37)
    Sleep(300)
    OP_68(-62700, 2700, -34780, 2500)
    MoveCamera(29, 26, 0, 2500)
    OP_6E(600, 2500)
    SetCameraDistance(15110, 2500)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(2400)

    #C0017
    ChrTalk(
        0x8,
        "#00813F#6P玲！不要啊！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        "#00907F#12P不要一个人上前……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 1, 0, 38)
    OP_68(-54690, 2900, -20410, 0)
    MoveCamera(28, -2, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21330, 0)
    Fade(500)
    OP_68(-54690, 2900, -20410, 2000)
    MoveCamera(28, -5, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(19250, 2000)
    OP_0D()
    BlurSwitch(0x2BC, 0x66FFFFFF, 0x0, 0x1, 0xA)
    WaitChrThread(0xB, 0)
    OP_A1(0xA, 0x0, 0x1, 0x0)
    EndChrThread(0xA, 0x3)
    BeginChrThread(0xA, 1, 0, 40)
    BeginChrThread(0xB, 0, 0, 18)
    Sleep(100)
    OP_68(-49300, 2600, -22900, 2200)
    MoveCamera(347, -8, 0, 2200)
    OP_6E(600, 2200)
    SetCameraDistance(14120, 2200)
    Sleep(800)
    CancelBlur(500)
    Sleep(1000)

    #C0019
    ChrTalk(
        0xA,
        "#03310F#11P#8A啊啊……！\x02",
    )
    #Auto

    WaitChrThread(0xA, 1)
    CloseMessageWindow()
    EndChrThread(0xB, 0x0)
    StopSound(579, 500, 50)
    BeginChrThread(0xB, 1, 0, 41)
    OP_68(-59770, 3900, -29280, 0)
    MoveCamera(27, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24150, 0)
    Fade(500)
    BeginChrThread(0xB, 0, 0, 42)
    OP_0D()
    BlurSwitch(0x12C, 0x66FFFFFF, 0x0, 0x1, 0xA)
    BeginChrThread(0x8, 0, 0, 43)
    BeginChrThread(0x9, 0, 0, 44)
    Sleep(900)
    OP_68(-62260, 1300, -36400, 800)
    MoveCamera(73, 22, 0, 800)
    OP_6E(600, 800)
    SetCameraDistance(24780, 800)
    Sleep(600)
    CancelBlur(500)

    #C0020
    ChrTalk(
        0x8,
        "#00806F#11P呀……！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        "#00907F#12P糟了……！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xB, 0x0)
    EndChrThread(0xB, 0x1)
    SetChrPos(0xB, -59000, 0, -19000, 0)
    OP_93(0xB, 0xD0, 0x0)
    Jump("loc_1E7F")

    label("loc_1DB2")

    OP_68(-62260, 1300, -36400, 0)
    MoveCamera(73, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24780, 0)
    SetChrPos(0xC, -55540, 150, -11980, 0)
    OP_93(0xC, 0xE1, 0x0)
    SetChrPos(0xB, -59000, 0, -19000, 0)
    OP_93(0xB, 0xD0, 0x0)
    SetChrPos(0xD, -58930, 150, -15120, 0)
    ClearChrFlags(0xD, 0x8)
    OP_70(0x0, 0x2B2)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x9, -55820, 2000, -42120, 120)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x1)
    SetChrPos(0x8, -74450, 2000, -39430, 300)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrSubChip(0xA, 0x3)
    SetChrPos(0xA, -48000, 0, -25500, 300)
    ClearChrFlags(0xA, 0x1000)
    ClearChrFlags(0xA, 0x2)

    label("loc_1E7F")

    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0x8, 0xA, 0)
    OP_74(0x0, 0x1E)
    OP_74(0x1, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2136")
    TurnDirection(0xA, 0xB, 0)
    OP_70(0x1, 0x2B2)
    Fade(500)
    OP_68(-52720, 3400, -21490, 0)
    MoveCamera(54, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25630, 0)
    OP_68(-48000, 800, -25500, 3000)
    MoveCamera(121, 41, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(35000, 1200)
    BeginChrThread(0xB, 0, 0, 46)
    Sleep(1800)
    SetChrFlags(0xA, 0x800)
    SetCameraDistance(22300, 1200)
    OP_0D()
    WaitChrThread(0xB, 0)
    BeginChrThread(0xB, 0, 0, 47)
    OP_0D()
    WaitChrThread(0xB, 0)

    #C0022
    ChrTalk(
        0xA,
        "#03305F#5P#30W………啊…………\x02",
    )

    CloseMessageWindow()
    OP_68(-51660, 2400, -24100, 0)
    MoveCamera(333, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19830, 0)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrFlags(0xA, 0x1000)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x16)
    Fade(500)
    OP_0D()

    #C0023
    ChrTalk(
        0x9,
        "#00907F#6P#N不行！已经来不及了！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xC, 0, 0, 50)
    BeginChrThread(0xB, 0, 0, 51)
    BlurSwitch(0x3E8, 0x88FFFFFF, 0x0, 0x1, 0xA)

    #C0024
    ChrTalk(
        0x8,
        "#00813F#6P#N#4S#12A玲————！！！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    OP_68(-57920, 2100, -15450, 800)
    MoveCamera(331, 15, 0, 800)
    OP_6E(600, 800)
    SetCameraDistance(24100, 800)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xB, 0)
    CancelBlur(0)
    FadeToDark(2500, 16777215, -1)
    OP_0D()
    ClearChrFlags(0xA, 0x800)
    Call(0, 45)
    OP_68(-56280, 3800, -20400, 0)
    MoveCamera(269, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22880, 0)
    OP_68(-53780, 4200, -21540, 2700)
    MoveCamera(170, 39, 0, 2700)
    OP_6E(600, 2700)
    SetCameraDistance(22880, 2700)
    SetChrPos(0xA, -48000, 100, -25500, 300)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrFlags(0xA, 0x1000)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x9)
    OP_70(0x0, 0x3C)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    FadeToBright(2000, 16777215)
    OP_0D()
    CancelBlur(1500)

    #C0025
    ChrTalk(
        0xA,
        "#03310F#6P#13A呀啊……！\x02",
    )
    #Auto

    Sleep(2000)
    CloseMessageWindow()
    StopSound(931, 1000, 50)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xB, 0xFF)
    Jump("loc_21D2")

    label("loc_2136")

    Call(0, 45)
    OP_68(-53780, 4900, -21540, 0)
    MoveCamera(159, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22880, 0)
    SetChrPos(0xC, -56570, 200, -20210, 0)
    OP_93(0xC, 0x128, 0x0)
    SetChrPos(0xB, -59000, 0, -19000, 0)
    OP_93(0xB, 0x78, 0x0)
    SetChrPos(0xA, -48000, 100, -25500, 300)
    OP_74(0x1, 0xF)
    OP_70(0x1, 0x3E8)
    OP_74(0x1, 0xF)
    OP_70(0x0, 0x28A)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrFlags(0xA, 0x1000)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x9)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xB, 0xFF)

    label("loc_21D2")

    BeginChrThread(0xC, 0, 0, 56)
    BeginChrThread(0xB, 0, 0, 58)
    BeginChrThread(0xB, 1, 0, 59)
    BeginChrThread(0x17, 1, 0, 60)
    Sound(904, 2, 80, 0)
    WaitChrThread(0xC, 0)
    OP_68(-46270, 400, -20250, 0)
    MoveCamera(69, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25140, 0)
    Fade(500)
    OP_70(0x0, 0x276)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x1000)
    SetChrSubChip(0xA, 0xB)
    OP_0D()
    Call(0, 5)
    Sound(903, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xB, 0)
    Sleep(500)
    Call(0, 53)
    BeginChrThread(0xC, 3, 0, 70)
    Fade(500)
    Sleep(500)
    OP_63(0xA, 0xFFFFFF06, 1150, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0026
    ChrTalk(
        0xA,
        "#03311F#12P哎——\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Call(0, 52)
    Call(0, 54)
    Fade(500)
    Sleep(2500)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    OP_68(-48240, 400, -23830, 0)
    MoveCamera(77, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18880, 0)
    Fade(500)
    BeginChrThread(0xA, 1, 0, 65)
    WaitChrThread(0xA, 1)

    #C0027
    ChrTalk(
        0xA,
        (
            "#03316F#12P#30W『帕蒂尔·玛蒂尔』……\x01",
            "你、你说什么……？\x02\x03",

            "#03307F#30W……不行……\x01",
            "绝对不行……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    EndChrThread(0xC, 0x3)
    Fade(500)
    OP_68(-64920, 3800, -1760, 0)
    MoveCamera(357, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(35630, 0)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x1000)
    SetChrSubChip(0xA, 0x16)
    SetChrFlags(0xC, 0x4)
    BeginChrThread(0xC, 3, 0, 71)
    OP_68(-53250, -1300, -4700, 0)
    MoveCamera(357, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40530, 0)
    OP_68(-53250, 7100, -4700, 4000)
    MoveCamera(346, 20, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(45990, 4000)
    Sound(994, 0, 100, 0)
    BeginChrThread(0xB, 0, 0, 61)
    BeginChrThread(0xC, 0, 0, 61)
    OP_0D()
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    EndChrThread(0x17, 0x1)
    StopSound(904, 2000, 70)
    OP_68(-56790, 17500, -21340, 0)
    MoveCamera(55, 59, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(41970, 0)
    SetChrPos(0xC, -56880, 9000, -17240, 0)
    OP_93(0xC, 0x5A, 0x0)
    SetChrPos(0xB, -54090, 9000, -17070, 0)
    OP_93(0xB, 0x10A, 0x0)
    OP_11(0xD0, 0xD0, 0xFF, 0x32, 0x258, 0x0)
    Fade(500)
    Sound(994, 0, 100, 0)
    OP_68(-56790, 19500, -21340, 5000)
    MoveCamera(74, 67, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(59280, 5000)
    BeginChrThread(0xB, 0, 0, 62)
    BeginChrThread(0xC, 0, 0, 62)
    OP_0D()
    Sleep(500)
    BlurSwitch(0x7D0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0028
    ChrTalk(
        0xA,
        "#03310F#12P#4S#20A不要啊！！！！！！\x02",
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0xA, 1, 0, 66)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    Sleep(1000)
    StopSound(993, 3000, 90)
    Sound(200, 0, 70, 0)
    Sound(1043, 0, 100, 0)
    Sleep(3000)
    OP_68(-13920, 1200, 76150, 0)
    MoveCamera(10, 4, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18900, 0)
    FadeToBright(1000, 16777215)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x354)
    OP_24(0x3D3)
    OP_24(0x243)
    OP_24(0x3A3)
    OP_24(0x388)
    OP_24(0x3E4)
    OP_24(0x3E1)
    SetScenarioFlags(0x22, 1)
    NewScene("c1510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_E1C end

    def Function_7_25C0(): pass

    label("Function_7_25C0")

    OP_74(0x0, 0x1E)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x3C, 0x44, 0x1, 0x0)
    OP_79(0x0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    OP_4B(0xFE, 0x1)
    Sound(902, 0, 70, 0)
    OP_71(0x0, 0x45, 0x49, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x4A, 0x58, 0x1, 0x0)
    OP_79(0x0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    OP_4B(0xFE, 0x1)
    Sound(902, 0, 70, 0)
    OP_71(0x0, 0x59, 0x5D, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x5E, 0x64, 0x1, 0x0)
    OP_79(0x0)
    Return()

    # Function_7_25C0 end

    def Function_8_2652(): pass

    label("Function_8_2652")

    OP_74(0x0, 0x1E)

    def lambda_265B():
        OP_9B(0x1, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_265B)

    label("loc_266B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_267E")
    Call(0, 7)
    Jump("loc_266B")

    label("loc_267E")

    Return()

    # Function_8_2652 end

    def Function_9_267F(): pass

    label("Function_9_267F")

    ClearMapObjFlags(0x1, 0x20)
    OP_79(0x1)
    Sound(905, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x1D6, 0x1ED, 0x1, 0x0)
    OP_79(0x1)
    BlurSwitch(0x12C, 0x77FFFFFF, 0x0, 0x1, 0xA)
    Sound(902, 0, 100, 0)
    Sound(1042, 0, 100, 0)
    Sound(196, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -54760, 5200, -17310, 149, 90, 0, 450, 850, 450, 0xFF, 0, 0, 0, 0)
    OP_FE(0x0)
    EndChrThread(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 10)
    OP_71(0x1, 0x1ED, 0x1F4, 0x1, 0x0)
    OP_79(0x1)
    CancelBlur(500)
    OP_71(0x1, 0x1F7, 0x1FE, 0x1, 0x0)
    OP_79(0x1)

    def lambda_273B():
        OP_93(0xFE, 0x141, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_273B)
    OP_71(0x1, 0x1AE, 0x1D6, 0x1, 0x0)
    OP_79(0x1)
    Sound(1019, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x24E, 0x276, 0x1, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA0, 0xFA0, 0x1)
    Return()

    # Function_9_267F end

    def Function_10_2778(): pass

    label("Function_10_2778")

    SetChrFlags(0xFE, 0x4)

    def lambda_2782():
        OP_93(0xFE, 0x96, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2782)
    OP_9D(0xFE, 0xFFFF185C, 0xF0A, 0xFFFFEBB0, 0xF3C, 0x3E8)
    SetChrPos(0xD, -59300, 0, -5200, 0)
    ClearChrFlags(0xFE, 0x1)
    ClearChrFlags(0xD, 0x8)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sound(833, 0, 100, 0)
    Sound(978, 0, 100, 0)
    OP_71(0x0, 0x136, 0x140, 0x1, 0x0)
    Sleep(700)
    OP_9C(0xFE, 0x0, 0xFFFFFEA2, 0x0, 0x0, 0x1E)
    Return()

    # Function_10_2778 end

    def Function_11_2800(): pass

    label("Function_11_2800")

    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x276, 0x280, 0x1, 0x0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -58950, 7780, -6090, 143, 90, 0, 150, 1250, 150, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -58950, 7780, -6090, 143, 90, 0, 1000, 2300, 1000, 0xFF, 0, 0, 0, 0)
    Sound(288, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xC, 0x4, 0, 4200, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xC8)
    BlurSwitch(0x12C, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_71(0x0, 0x136, 0x140, 0x1, 0x0)
    OP_79(0x1)
    CancelBlur(500)
    Return()

    # Function_11_2800 end

    def Function_12_28F0(): pass

    label("Function_12_28F0")

    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x276, 0x280, 0x1, 0x0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -58950, 7780, -6090, 143, 90, 0, 150, 1250, 150, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -58950, 7780, -6090, 143, 90, 0, 750, 1800, 750, 0xFF, 0, 0, 0, 0)
    Sound(288, 0, 60, 0)
    PlayEffect(0x0, 0xFF, 0xC, 0x4, 0, 4200, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x64, 0xBB8, 0xC8)
    OP_71(0x0, 0x136, 0x140, 0x1, 0x0)
    OP_79(0x1)
    Return()

    # Function_12_28F0 end

    def Function_13_29CF(): pass

    label("Function_13_29CF")

    OP_74(0x1, 0x3C)
    OP_71(0x1, 0x280, 0x276, 0x1, 0x0)
    OP_79(0x1)
    Return()

    # Function_13_29CF end

    def Function_14_29E3(): pass

    label("Function_14_29E3")

    OP_93(0xFE, 0x13A, 0x0)
    OP_79(0x1)

    label("loc_29ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A00")
    Call(0, 11)
    Jump("loc_29ED")

    label("loc_2A00")

    Return()

    # Function_14_29E3 end

    def Function_15_2A01(): pass

    label("Function_15_2A01")

    Call(0, 12)
    Call(0, 13)
    Call(0, 12)
    Call(0, 13)
    Call(0, 12)
    Call(0, 13)
    Call(0, 12)
    Call(0, 13)

    label("loc_2A19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A32")
    Call(0, 12)
    Sleep(800)
    Call(0, 13)
    Jump("loc_2A19")

    label("loc_2A32")

    Return()

    # Function_15_2A01 end

    def Function_16_2A33(): pass

    label("Function_16_2A33")

    Call(0, 11)
    Sleep(800)
    Call(0, 13)
    Sleep(500)
    Sound(905, 0, 100, 0)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x28A, 0x2B2, 0x1, 0x0)
    Sleep(1000)
    Sound(1019, 0, 100, 0)
    OP_79(0x1)
    BeginChrThread(0xFE, 3, 0, 67)
    TurnDirection(0xFE, 0xA, 75)
    Return()

    # Function_16_2A33 end

    def Function_17_2A6F(): pass

    label("Function_17_2A6F")

    Sleep(1500)
    OP_9C(0xFE, 0x0, 0xFFFFFF06, 0x0, 0x32, 0x1F4)
    Sound(996, 2, 40, 0)
    Sleep(500)
    OP_9C(0xFE, 0x0, 0xFFFFF34E, 0x0, 0x32, 0x3E8)
    OP_24(0x3E4)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    OP_71(0x0, 0x14A, 0x172, 0x1, 0x0)
    Return()

    # Function_17_2A6F end

    def Function_18_2AD6(): pass

    label("Function_18_2AD6")

    Sleep(500)
    Sound(622, 0, 70, 0)
    Sound(869, 0, 60, 0)
    Call(0, 19)
    Sleep(600)
    Sound(622, 0, 70, 0)
    Sound(869, 0, 60, 0)
    Call(0, 19)
    Sleep(600)
    Sound(622, 0, 70, 0)
    Sound(869, 0, 60, 0)
    Call(0, 19)
    Sleep(600)
    Return()

    # Function_18_2AD6 end

    def Function_19_2B10(): pass

    label("Function_19_2B10")

    PlayEffect(0x5, 0xFF, 0xB, 0x4, -1300, 8000, -2400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, 1300, 8000, -2400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, -1500, 8000, -2600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, 1500, 8000, -2600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, -1700, 8000, -2800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, 1700, 8000, -2800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, -1900, 8000, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xB, 0x4, 1900, 8000, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Return()

    # Function_19_2B10 end

    def Function_20_2CD5(): pass

    label("Function_20_2CD5")

    Sleep(300)
    SetChrPos(0xE, -55320, 3500, -27250, 0)

    label("loc_2CE9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FB7")
    SetChrPos(0xF, -50140, 100, -27050, 0)
    PlayEffect(0x6, 0xFF, 0xF, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x10, -61470, 100, -25970, 0)
    PlayEffect(0x6, 0xFF, 0x10, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 80, 0)
    Sleep(200)
    SetChrPos(0xF, -51220, 2100, -37310, 0)
    PlayEffect(0x6, 0xFF, 0xF, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x10, -62330, 2100, -35550, 0)
    PlayEffect(0x6, 0xFF, 0x10, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(350)
    SetChrPos(0x12, -49830, 2100, -44340, 0)
    Sound(200, 0, 80, 0)
    PlayEffect(0x6, 0xFF, 0x12, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x13, -57520, 2100, -45280, 0)
    PlayEffect(0x6, 0xFF, 0x13, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(300)
    SetChrPos(0x11, -54760, 2100, -39810, 0)
    PlayEffect(0x6, 0xFF, 0x11, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(200)
    SetChrPos(0xF, -51220, 2100, -37310, 0)
    PlayEffect(0x6, 0xFF, 0xF, 0x0, 0, 0, 0, 0, 105, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x10, -62330, 2100, -35550, 0)
    PlayEffect(0x6, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 105, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(300)
    Jump("loc_2CE9")

    label("loc_2FB7")

    Return()

    # Function_20_2CD5 end

    def Function_21_2FB8(): pass

    label("Function_21_2FB8")

    Sleep(200)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    TurnDirection(0xFE, 0xA, 0)
    OP_95(0xFE, -55500, 2000, -34780, 4000, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x64, 0x7D0, 0x1)
    BeginChrThread(0xA, 0, 0, 22)
    Sleep(30)
    OP_93(0xFE, 0xF0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0xBB8, 0x0)
    BeginChrThread(0xFE, 1, 0, 23)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF1794, 0x7D0, 0xFFFF699C, 0x15E, 0x3E8)
    Sleep(100)
    BeginChrThread(0xFE, 1, 0, 23)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF02E0, 0xFA0, 0xFFFF6488, 0x92E, 0x3E8)
    Sound(326, 0, 60, 0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_2FB8 end

    def Function_22_306E(): pass

    label("Function_22_306E")

    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    OP_93(0xFE, 0xF0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0xBB8, 0x0)
    BeginChrThread(0xFE, 1, 0, 23)
    OP_9D(0xFE, 0xFFFF1668, 0x7D0, 0xFFFF6870, 0x15E, 0x3E8)
    Sleep(150)
    BeginChrThread(0xFE, 1, 0, 23)
    OP_9D(0xFE, 0xFFFF0150, 0xFA0, 0xFFFF62F8, 0x92E, 0x3E8)
    Sleep(300)
    TurnDirection(0xFE, 0xC, 500)
    Return()

    # Function_22_306E end

    def Function_23_30E0(): pass

    label("Function_23_30E0")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(180)
    SetChrSubChip(0xFE, 0x3)
    Sleep(90)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    Return()

    # Function_23_30E0 end

    def Function_24_3104(): pass

    label("Function_24_3104")

    PlayEffect(0x6, 0xFF, 0xE, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_4B(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(200)
    Sound(308, 0, 100, 0)
    Sound(533, 0, 60, 0)
    Sound(859, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFE, 0x4, 0, 500, 0, 0, 1, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    OP_4C(0xFE, 0x0)
    Return()

    # Function_24_3104 end

    def Function_25_31BE(): pass

    label("Function_25_31BE")

    PlayEffect(0x6, 0xFF, 0xE, 0x0, 0, 0, 0, 105, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_4B(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(308, 0, 100, 0)
    Sound(533, 0, 60, 0)
    Sound(859, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFE, 0x4, 0, 500, 0, 0, 1, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(350)
    Sound(844, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    OP_4C(0xFE, 0x0)
    Return()

    # Function_25_31BE end

    def Function_26_327E(): pass

    label("Function_26_327E")

    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 1, 0, 23)
    Sound(250, 0, 60, 0)
    OP_9D(0xFE, 0xFFFF2216, 0x7D0, 0xFFFF7C84, 0x15E, 0x5DC)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 2, 0, 24)
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    BeginChrThread(0xFE, 2, 0, 24)
    OP_9D(0xFE, 0xFFFF153C, 0x7D0, 0xFFFF6FA0, 0x15E, 0x5DC)
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrPos(0xE, -59010, 4800, -28120, 0)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(200)
    BeginChrThread(0xFE, 2, 0, 25)
    OP_9D(0xFE, 0xFFFF052F, 0xFA0, 0xFFFF6154, 0x92E, 0x4B0)
    Sound(326, 0, 70, 0)
    Sound(540, 0, 60, 0)
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0x9, 0x26)
    TurnDirection(0xFE, 0xB, 500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_26_327E end

    def Function_27_3356(): pass

    label("Function_27_3356")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0x230, 0x258, 0x1, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    BeginChrThread(0xFE, 1, 0, 29)
    Call(0, 7)
    Call(0, 7)
    Return()

    # Function_27_3356 end

    def Function_28_337A(): pass

    label("Function_28_337A")

    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x262, 0x276, 0x1, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x276, 0x28A, 0x1, 0x20)
    OP_79(0x0)
    Return()

    # Function_28_337A end

    def Function_29_339D(): pass

    label("Function_29_339D")

    TurnDirection(0xFE, 0xB, 100)
    OP_9B(0x1, 0xFE, 0xF, 0xFA, 0x3E8, 0x0)
    OP_9B(0x1, 0xFE, 0xF, 0xFA, 0x7D0, 0x0)
    OP_9B(0x1, 0xFE, 0xF, 0xFA, 0xFA0, 0x0)
    OP_9B(0x1, 0xFE, 0xF, 0xFA0, 0x1770, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 28)
    OP_9D(0xFE, 0xFFFF27F2, 0x3E8, 0xFFFFD1C0, 0x41A, 0x4B0)
    Sound(288, 0, 50, 0)
    Sound(833, 0, 50, 0)
    Sound(1042, 0, 100, 0)
    OP_82(0x0, 0x1E, 0xBB8, 0x12C)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -53870, 3600, -11890, 288, 90, 0, 1000, 1800, 1000, 0xFF, 0, 0, 0, 0)
    OP_9C(0xFE, 0x0, 0xFFFFFCAE, 0x0, 0x32, 0x2EE)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_29_339D end

    def Function_30_3477(): pass

    label("Function_30_3477")

    OP_9B(0x1, 0xFE, 0x0, 0xC8, 0x7D0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x64, 0x3E8, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x64, 0x1F4, 0x0)
    Return()

    # Function_30_3477 end

    def Function_31_34B4(): pass

    label("Function_31_34B4")

    OP_9B(0x1, 0xFE, 0x31, 0xFFFFFF38, 0x7D0, 0x0)
    OP_9B(0x1, 0xFE, 0x31, 0xFFFFFF38, 0xBB8, 0x0)
    OP_9B(0x1, 0xFE, 0x31, 0xFFFFFF9C, 0x3E8, 0x0)
    OP_9B(0x1, 0xFE, 0x31, 0xFFFFFF9C, 0x1F4, 0x0)
    Return()

    # Function_31_34B4 end

    def Function_32_34F1(): pass

    label("Function_32_34F1")

    ClearMapObjFlags(0x1, 0x20)
    OP_79(0x1)
    BeginChrThread(0xFE, 3, 0, 68)
    WaitChrThread(0xFE, 3)
    OP_79(0x1)
    OP_71(0x1, 0x1AE, 0x1D6, 0x1, 0x20)
    OP_93(0xFE, 0x113, 0x4B)
    Return()

    # Function_32_34F1 end

    def Function_33_351B(): pass

    label("Function_33_351B")

    OP_96(0xFE, 0xFFFF2540, 0x96, 0xFFFFD440, 0x1388, 0x1)
    OP_96(0xFE, 0xFFFF27F2, 0x96, 0xFFFFD1C0, 0x1B58, 0x1)
    Return()

    # Function_33_351B end

    def Function_34_3544(): pass

    label("Function_34_3544")

    OP_FD(0xD, 0xFE)
    ClearChrFlags(0xD, 0x8)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -55540, 180, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 150, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 180, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 150, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 180, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 150, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 180, -11980, 225)
    Sleep(160)
    SetChrPos(0xFE, -55540, 150, -11980, 225)
    Sleep(160)
    ClearChrFlags(0xFE, 0x4)
    ClearChrFlags(0xD, 0x8)
    Return()

    # Function_34_3544 end

    def Function_35_35FE(): pass

    label("Function_35_35FE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3617")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_35_35FE")

    label("loc_3617")

    Return()

    # Function_35_35FE end

    def Function_36_3618(): pass

    label("Function_36_3618")

    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(802, 0, 100, 0)
    Return()

    # Function_36_3618 end

    def Function_37_362A(): pass

    label("Function_37_362A")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sound(811, 0, 50, 0)

    def lambda_363D():
        OP_9B(0x1, 0xFE, 0x14A, 0x96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_363D)

    def lambda_3652():
        OP_A6(0xFE, 0x1E, 0x1E, 0x12C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3652)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x1388, 0x1)
    Sound(844, 0, 60, 0)
    OP_9D(0xFE, 0xFFFF07F4, 0x7D0, 0xFFFF72FC, 0x28A, 0x5DC)
    Sound(326, 0, 60, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x1388, 0x1)
    Sound(809, 0, 70, 0)
    OP_9D(0xFE, 0xFFFF15A0, 0x0, 0xFFFF8A9E, 0x15E, 0x5DC)
    Sound(326, 0, 40, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(357, 0, 80, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x7, 0x0, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 3, 0, 35)
    Sleep(1000)
    Return()

    # Function_37_362A end

    def Function_38_3734(): pass

    label("Function_38_3734")

    BeginChrThread(0xFE, 3, 0, 67)

    def lambda_373F():
        TurnDirection(0xFE, 0xA, 50)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_373F)
    Sleep(500)
    BeginChrThread(0xB, 0, 0, 18)
    Sleep(1200)
    EndChrThread(0xB, 0x0)
    BeginChrThread(0xB, 0, 0, 39)
    WaitChrThread(0xB, 0)
    Return()

    # Function_38_3734 end

    def Function_39_3762(): pass

    label("Function_39_3762")

    Sleep(300)
    SetChrPos(0xE, -60950, 1500, -27780, 0)
    SetChrPos(0xF, -59690, 100, -21630, 0)
    PlayEffect(0x6, 0xFF, 0xF, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x10, -50140, 100, -27050, 0)
    PlayEffect(0x6, 0xFF, 0x10, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(200, 0, 80, 0)
    Sleep(150)
    SetChrPos(0x11, -63470, 100, -29700, 0)
    PlayEffect(0x6, 0xFF, 0x11, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x12, -56730, 100, -33430, 0)
    PlayEffect(0x6, 0xFF, 0x12, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(200)
    SetChrPos(0xF, -59690, 100, -21630, 0)
    PlayEffect(0x6, 0xFF, 0xF, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x10, -50140, 100, -27050, 0)
    PlayEffect(0x6, 0xFF, 0x10, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 80, 0)
    Sleep(150)
    PlayEffect(0x6, 0xFF, 0xE, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(500)
    Return()

    # Function_39_3762 end

    def Function_40_398B(): pass

    label("Function_40_398B")

    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    StopEffect(0x0, 0x2)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x2)
    OP_93(0xFE, 0x12C, 0x0)
    Sound(255, 0, 60, 0)
    Sound(556, 0, 100, 0)
    OP_24(0x354)
    OP_9D(0xFE, 0xFFFF4098, 0x0, 0xFFFF9CC8, 0x92E, 0x1F4)
    Sound(645, 0, 80, 0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFF4480, 0x0, 0xFFFF9C64, 0xFA, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sound(645, 0, 80, 0)
    Sound(514, 0, 100, 0)
    Sleep(300)
    Return()

    # Function_40_398B end

    def Function_41_3A1C(): pass

    label("Function_41_3A1C")

    Sleep(700)
    OP_96(0xFE, 0xFFFF1988, 0x0, 0xFFFFB5C8, 0x7D0, 0x1)
    Return()

    # Function_41_3A1C end

    def Function_42_3A34(): pass

    label("Function_42_3A34")

    SetChrPos(0x11, -53880, 100, -21770, 0)
    Sound(200, 0, 80, 0)
    PlayEffect(0x6, 0xFF, 0x11, 0x0, 0, 0, 0, 210, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrPos(0x12, -59060, 0, -25560, 0)
    PlayEffect(0x6, 0xFF, 0x12, 0x0, 0, 0, 0, 210, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrPos(0x13, -57380, 800, -30310, 0)
    PlayEffect(0x6, 0xFF, 0x13, 0x0, 0, 0, 0, 210, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sleep(300)
    SetChrPos(0x11, -64760, 4200, -39250, 0)
    Sound(196, 0, 80, 0)
    PlayEffect(0x6, 0xFF, 0x11, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrPos(0xF, -59090, 2000, -34600, 0)
    PlayEffect(0x6, 0xFF, 0xF, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrPos(0x10, -65250, 1300, -30840, 0)
    PlayEffect(0x6, 0xFF, 0x10, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sleep(300)
    SetChrPos(0x11, -64760, 4200, -39250, 0)
    Sound(200, 0, 80, 0)
    PlayEffect(0x6, 0xFF, 0x11, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrPos(0x12, -64709, 4200, -43100, 0)
    PlayEffect(0x6, 0xFF, 0x12, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrPos(0x13, -68160, 4200, -42540, 0)
    PlayEffect(0x6, 0xFF, 0x13, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 80, 0)
    Sleep(200)
    SetChrPos(0x11, -64760, 4200, -39250, 0)
    PlayEffect(0x6, 0xFF, 0x11, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sleep(200)
    SetChrPos(0x12, -64709, 4200, -43100, 0)
    PlayEffect(0x6, 0xFF, 0x12, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sound(200, 0, 80, 0)
    SetChrPos(0x13, -68160, 4200, -42540, 0)
    PlayEffect(0x6, 0xFF, 0x13, 0x0, 0, 0, 0, 210, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Return()

    # Function_42_3A34 end

    def Function_43_3DE3(): pass

    label("Function_43_3DE3")

    Sleep(600)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x12C, 0x1F4)
    BeginChrThread(0xFE, 1, 0, 23)
    Sound(255, 0, 70, 0)
    Sound(200, 0, 100, 0)
    OP_9D(0xFE, 0xFFFEDD2E, 0xFA0, 0xFFFF65FA, 0x3E8, 0x5DC)
    Sound(514, 0, 100, 0)
    Sound(645, 0, 80, 0)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sleep(300)
    Return()

    # Function_43_3DE3 end

    def Function_44_3E46(): pass

    label("Function_44_3E46")

    Sleep(500)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x78, 0x1F4)
    BeginChrThread(0xFE, 1, 0, 23)
    OP_9D(0xFE, 0xFFFF25F4, 0x7D0, 0xFFFF5B78, 0x3E8, 0x5DC)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sleep(300)
    Return()

    # Function_44_3E46 end

    def Function_45_3E91(): pass

    label("Function_45_3E91")

    SetMapObjFrame(0xFF, "ato00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "atokizu_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "atokumo_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mae00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maewood", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekusa00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekusa01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekusa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "maekage", 0x0, 0x1)
    Return()

    # Function_45_3E91 end

    def Function_46_3F64(): pass

    label("Function_46_3F64")

    Sound(1040, 0, 80, 0)
    OP_70(0x1, 0xF)
    OP_71(0x1, 0x2B2, 0x2DA, 0x0, 0x0)

    def lambda_3F7F():

        label("loc_3F7F")

        TurnDirection(0xFE, 0xA, 25)
        Yield()
        Jump("loc_3F7F")

    QueueWorkItem2(0xFE, 2, lambda_3F7F)
    Sleep(2500)
    Sound(304, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_79(0x1)
    Return()

    # Function_46_3F64 end

    def Function_47_3FD0(): pass

    label("Function_47_3FD0")

    Sleep(2000)
    BeginChrThread(0xA, 1, 0, 64)
    OP_68(-48000, 0, -25500, 1500)
    MoveCamera(121, 44, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(17100, 1500)
    Sleep(1500)
    BeginChrThread(0x17, 1, 0, 48)
    OP_87(0xA, 0x0, 0x1, "Null_b_cannon_r(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    OP_87(0xA, 0x1, 0x1, "Null_b_cannon_l(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    WaitChrThread(0xA, 1)
    Return()

    # Function_47_3FD0 end

    def Function_48_408D(): pass

    label("Function_48_408D")

    Sound(983, 0, 60, 0)

    label("loc_4093")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40AC")
    Sleep(1300)
    Sound(1041, 0, 50, 0)
    Jump("loc_4093")

    label("loc_40AC")

    Return()

    # Function_48_408D end

    def Function_49_40AD(): pass

    label("Function_49_40AD")

    OP_96(0xFE, 0xFFFF3C24, 0x190, 0xFFFFBD8E, 0x2710, 0x1)

    def lambda_40C6():

        label("loc_40C6")

        TurnDirection(0xFE, 0xB, 100)
        Yield()
        Jump("loc_40C6")

    QueueWorkItem2(0xFE, 2, lambda_40C6)
    OP_96(0xFE, 0xFFFF3878, 0xC8, 0xFFFFA38A, 0x2710, 0x1)
    PlayEffect(0x2, 0xFF, 0xC, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1042, 0, 100, 0)
    Sound(833, 0, 100, 0)
    Sound(951, 0, 100, 0)
    OP_82(0xC8, 0xC8, 0xBB8, 0x3E8)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D4, 0x3E8, 0x0, 0x0)
    OP_9D(0xFE, 0xFFFF24E6, 0xC8, 0xFFFFB078, 0x1F4, 0x7D0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x262, 0x276, 0x1, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0xBB8, 0x0)
    OP_79(0x0)
    EndChrThread(0xFE, 0x2)
    Return()

    # Function_49_40AD end

    def Function_50_418F(): pass

    label("Function_50_418F")

    Sound(902, 0, 100, 0)
    Sound(905, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -58260, 150, -14590, 0, 0, 0, 1200, 1500, 1200, 0xFF, 0, 0, 0, 0)
    OP_71(0x0, 0x2B2, 0x294, 0x1, 0x0)
    OP_79(0x0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)

    def lambda_41F7():
        OP_93(0xFE, 0x94, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41F7)
    OP_74(0x0, 0x3C)
    BeginChrThread(0xFE, 1, 0, 49)
    Call(0, 7)
    Call(0, 7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_50_418F end

    def Function_51_4214(): pass

    label("Function_51_4214")

    Sleep(1000)
    OP_87(0xA, 0x2, 0x1, "Null_b_cannon_r(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    OP_87(0xA, 0x3, 0x1, "Null_b_cannon_l(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    Sleep(2000)
    EndChrThread(0x17, 0x1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    Sound(984, 0, 100, 0)
    Sound(931, 2, 60, 0)
    OP_87(0x3, 0x2, 0x1, "Null_b_cannon_r(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    OP_87(0x3, 0x3, 0x1, "Null_b_cannon_l(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Return()

    # Function_51_4214 end

    def Function_52_4338(): pass

    label("Function_52_4338")

    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    StopEffect(0x5, 0x0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    Return()

    # Function_52_4338 end

    def Function_53_4351(): pass

    label("Function_53_4351")

    Sound(993, 2, 80, 0)
    Sound(994, 0, 50, 0)
    StopSound(979, 500, 30)
    OP_87(0x1, 0x0, 0x0, "Null_S_jet_r0(63)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x1, 0x0, "Null_S_jet_r2(64)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x2, 0x0, "Null_S_jet_l0(66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x3, 0x0, "Null_S_jet_l2(65)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x4, 0x0, "Null_S_jet_r1(61)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x5, 0x0, "Null_S_jet_l1(62)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x6, 0x0, "Null_kata_jet_r(53)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x7, 0x0, "Null_kata_jet_l(54)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_71(0x0, 0x2BC, 0x2E4, 0x1, 0x0)
    Return()

    # Function_53_4351 end

    def Function_54_4544(): pass

    label("Function_54_4544")

    OP_25(0x3E1, 0x64)
    Sound(994, 0, 100, 0)
    OP_87(0x1, 0x0, 0x0, "Null_S_jet_r0(63)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x1, 0x1, 0x0, "Null_S_jet_r2(64)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x1, 0x2, 0x0, "Null_S_jet_l0(66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x1, 0x3, 0x0, "Null_S_jet_l2(65)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x0, 0x4, 0x0, "Null_S_jet_r1(61)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x0, 0x5, 0x0, "Null_S_jet_l1(62)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x0, 0x6, 0x0, "Null_kata_jet_r(53)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_87(0x0, 0x7, 0x0, "Null_kata_jet_l(54)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0x1388, 0xBB8, 0x0)
    OP_71(0x0, 0x2BC, 0x2E4, 0x1, 0x0)
    Return()

    # Function_54_4544 end

    def Function_55_472F(): pass

    label("Function_55_472F")

    OP_93(0xFE, 0x5A, 0x20)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    Return()

    # Function_55_472F end

    def Function_56_4746(): pass

    label("Function_56_4746")

    BeginChrThread(0xFE, 1, 0, 55)
    OP_74(0x0, 0xA)
    Call(0, 57)
    Call(0, 57)
    Return()

    # Function_56_4746 end

    def Function_57_4757(): pass

    label("Function_57_4757")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4817")
    OP_4C(0xB, 0x0)
    OP_4C(0xB, 0x1)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x3C, 0x44, 0x1, 0x0)
    OP_79(0x0)
    Sound(902, 0, 70, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    OP_4B(0xB, 0x0)
    OP_4B(0xB, 0x1)
    OP_4B(0xFE, 0x1)
    OP_71(0x0, 0x45, 0x49, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xB, 0x0)
    OP_4C(0xB, 0x1)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x4A, 0x58, 0x1, 0x0)
    OP_79(0x0)
    Sound(902, 0, 70, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    OP_4B(0xB, 0x0)
    OP_4B(0xB, 0x1)
    OP_4B(0xFE, 0x1)
    OP_71(0x0, 0x59, 0x5D, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xB, 0x0)
    OP_4C(0xB, 0x1)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x5E, 0x64, 0x1, 0x0)
    OP_79(0x0)

    label("loc_4817")

    Return()

    # Function_57_4757 end

    def Function_58_4818(): pass

    label("Function_58_4818")

    OP_9E(0xFE, 0xFFFF2306, 0xFFFFB10E, 0x249F0, 0x5DC, 0x2)
    OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x1)
    Return()

    # Function_58_4818 end

    def Function_59_4842(): pass

    label("Function_59_4842")

    OP_74(0x1, 0x1E)

    label("loc_4846")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4889")
    OP_71(0x1, 0x3E8, 0x410, 0x0, 0x0)
    OP_79(0x1)
    Sleep(1000)
    OP_71(0x1, 0x3E8, 0x410, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x3E8, 0x410, 0x0, 0x0)
    OP_79(0x1)
    Sleep(1000)
    Jump("loc_4846")

    label("loc_4889")

    Return()

    # Function_59_4842 end

    def Function_60_488A(): pass

    label("Function_60_488A")

    Sound(905, 0, 40, 0)
    Sleep(500)
    Sound(951, 0, 40, 0)
    Sleep(500)
    Return()

    # Function_60_488A end

    def Function_61_489D(): pass

    label("Function_61_489D")

    OP_98(0xFE, 0xBB8, 0x1388, 0x0, 0x7D0, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0xBB8, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0xFA0, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0x1388, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0x1770, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0x1B58, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0x1F40, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0x2328, 0x1)
    OP_98(0xFE, 0x12C, 0x1F4, 0x0, 0x2710, 0x1)
    OP_98(0xFE, 0xE10, 0x1770, 0x0, 0x2AF8, 0x1)
    OP_98(0xFE, 0x2328, 0x3A98, 0x0, 0x2EE0, 0x1)
    Return()

    # Function_61_489D end

    def Function_62_497A(): pass

    label("Function_62_497A")

    OP_98(0xFE, 0x0, 0x7530, 0x0, 0x1388, 0x1)
    Return()

    # Function_62_497A end

    def Function_63_498F(): pass

    label("Function_63_498F")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(111)
    SetChrSubChip(0xFE, 0x1)
    Sleep(111)
    SetChrSubChip(0xFE, 0x2)
    Sleep(333)
    Return()

    # Function_63_498F end

    def Function_64_49B3(): pass

    label("Function_64_49B3")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(857)
    Return()

    # Function_64_49B3 end

    def Function_65_49D7(): pass

    label("Function_65_49D7")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xB)
    Sleep(125)
    SetChrSubChip(0xFE, 0xC)
    Sleep(125)
    SetChrSubChip(0xFE, 0xD)
    Sleep(125)
    SetChrSubChip(0xFE, 0xC)
    Sleep(125)
    SetChrSubChip(0xFE, 0xB)
    Sleep(500)
    Return()

    # Function_65_49D7 end

    def Function_66_4A09(): pass

    label("Function_66_4A09")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0xF)
    Sleep(571)
    Return()

    # Function_66_4A09 end

    def Function_67_4A2D(): pass

    label("Function_67_4A2D")

    ClearMapObjFlags(0x1, 0x20)
    OP_79(0x1)
    Sound(905, 0, 100, 0)
    OP_74(0x1, 0xA)
    OP_71(0x1, 0x1FE, 0x212, 0x0, 0x0)
    OP_79(0x1)
    Sound(579, 2, 60, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x212, 0x23A, 0x0, 0x20)
    Return()

    # Function_67_4A2D end

    def Function_68_4A66(): pass

    label("Function_68_4A66")

    Sound(905, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x20)
    OP_79(0x1)
    Sound(1019, 0, 100, 0)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x23A, 0x24E, 0x0, 0x0)
    Return()

    # Function_68_4A66 end

    def Function_69_4A8C(): pass

    label("Function_69_4A8C")

    OP_74(0x1, 0xF)
    OP_71(0x1, 0x3D4, 0x3E8, 0x0, 0x0)
    Sleep(3000)
    Return()

    # Function_69_4A8C end

    def Function_70_4AA0(): pass

    label("Function_70_4AA0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AC4")
    OP_82(0x32, 0x32, 0xBB8, 0x5DC)
    Sleep(1000)
    Jump("Function_70_4AA0")

    label("loc_4AC4")

    Return()

    # Function_70_4AA0 end

    def Function_71_4AC5(): pass

    label("Function_71_4AC5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AE9")
    OP_82(0x64, 0x64, 0xBB8, 0x5DC)
    Sleep(1000)
    Jump("Function_71_4AC5")

    label("loc_4AE9")

    Return()

    # Function_71_4AC5 end

    def Function_72_4AEA(): pass

    label("Function_72_4AEA")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    StopEffect(0x9, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0029
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('塞姆里亚石碎片', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 1)
    OP_65(0x2, 0x1)
    EventEnd(0x3)
    Return()

    # Function_72_4AEA end

    SaveToFile()

Try(main)
