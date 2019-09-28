from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m0209.bin",                # FileName
        "m0209",                    # MapName
        "m0209",                    # Location
        0x00A7,                     # MapIndex
        "ed7300",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 167, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0209",                  # 0
        "约纳",                   # 1
        "故障机体Ｚ",             # 2
        "模型",                   # 3
        "罗伯兹主任",             # 4
        "SE控制",                 # 5
        "bm0220",                 # 6
        "bm0220",                 # 7
    ))

    ATBonus("ATBonus_3BC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_39C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_3FC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_460", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_464", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_468", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_46C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_470", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_474", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_47C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_48C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_4E0", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm0220", 0x00000000, 100, 0, 0, 0,
        (
            ("ms79101.dat", "ms79101.dat", "ms79101.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_45C", "ed7451", "ed7453", "ATBonus_3BC"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_49C", 0x0052, 3, 6, 45, 3, 3, 30, 0, "bm0220", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88200.dat", 0, 0, 0, 0, 0, "ms84900.dat", 0, "MonsterBattlePostion_47C", "MonsterBattlePostion_45C", "ed7453", "ed7453", "ATBonus_39C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50203.itc",                   # 00
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
        "monster/ch79150.itc",               # 10
        "monster/ch79151.itc",               # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(102500,  250,     0,       90,   389,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(0,       0,       0,       0x185010E,    "BattleInfo_4E0", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 11,  -8.0,                  0.0,                   -1.0,                  400.0,                 [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.09999999403953552,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   2.0,                   -0.0,                  0.19999998807907104,   1.0])
    DeclEvent(0x0040, 0, 6,   0.0,                   0.0,                   0.0,                   16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -0.0,                  -0.0,                  1.0])
    DeclEvent(0x0000, 0, 30,  -11.0,                 0.0,                   -2.0,                  81.0,                  [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1666666716337204,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.6666667461395264,    -0.0,                  0.4000000059604645,    1.0])

    DeclActor(112500,  0,       204000,  1200,    112500,  1000,    204000,  0x007C, 0,  7,  0x0000)
    DeclActor(-295500, 0,       1000,    1200,    -295500, 1000,    1000,    0x007C, 0,  9,  0x0000)
    DeclActor(-126000, 0,       -5000,   1200,    -126000, 1000,    -5000,   0x007C, 0,  2,  0x0000)
    DeclActor(96780,   0,       -5370,   1200,    96780,   780,     -5370,   0x007C, 0,  3,  0x0000)
    DeclActor(-28000,  -8000,   4000,    1200,    -28000,  -6500,   4000,    0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_5B8",          # 00, 0
        "Function_1_6AA",          # 01, 1
        "Function_2_A17",          # 02, 2
        "Function_3_B52",          # 03, 3
        "Function_4_BF5",          # 04, 4
        "Function_5_1409",         # 05, 5
        "Function_6_14ED",         # 06, 6
        "Function_7_1739",         # 07, 7
        "Function_8_18AC",         # 08, 8
        "Function_9_19E0",         # 09, 9
        "Function_10_1B53",        # 0A, 10
        "Function_11_1C87",        # 0B, 11
        "Function_12_2B29",        # 0C, 12
        "Function_13_2BB1",        # 0D, 13
        "Function_14_2BCD",        # 0E, 14
        "Function_15_3B30",        # 0F, 15
        "Function_16_3B49",        # 10, 16
        "Function_17_3B75",        # 11, 17
        "Function_18_407F",        # 12, 18
        "Function_19_40CD",        # 13, 19
        "Function_20_411B",        # 14, 20
        "Function_21_4170",        # 15, 21
        "Function_22_41C5",        # 16, 22
        "Function_23_421A",        # 17, 23
        "Function_24_426F",        # 18, 24
        "Function_25_46F8",        # 19, 25
        "Function_26_4715",        # 1A, 26
        "Function_27_472E",        # 1B, 27
        "Function_28_4746",        # 1C, 28
        "Function_29_47EF",        # 1D, 29
        "Function_30_4955",        # 1E, 30
    ))


    def Function_0_5B8(): pass

    label("Function_0_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_5CB")
    SetChrFlags(0x8, 0x80)
    Jump("loc_613")

    label("loc_5CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5EF")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_613")

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 7)), scpexpr(EXPR_END)), "loc_613")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_624")
    ClearScenarioFlags(0x22, 0)
    Jump("loc_661")

    label("loc_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_638")
    ClearScenarioFlags(0x22, 1)
    Event(0, 14)
    Jump("loc_661")

    label("loc_638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_652")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 24)
    Jump("loc_661")

    label("loc_652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_661")
    ClearScenarioFlags(0x22, 3)
    Event(0, 29)

    label("loc_661")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67B")
    Event(0, 17)

    label("loc_67B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_692")
    Event(0, 10)

    label("loc_692")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A9")
    Event(0, 8)

    label("loc_6A9")

    Return()

    # Function_0_5B8 end

    def Function_1_6AA(): pass

    label("Function_1_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6BF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_6BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x209), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F2")

    label("loc_6DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F2")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70A")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_70A")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_722")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_749")
    ClearChrFlags(0xD, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    SetChrFlags(0xD, 0x8000)

    label("loc_749")

    Jump("loc_758")

    label("loc_74E")

    SetChrFlags(0xD, 0x80)
    ModifyEventFlags(0, 1, 0x80)

    label("loc_758")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_862")
    SetMapObjFrame(0x8, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x8, "Null_color2", 0x1, 0x1)
    Jump("loc_887")

    label("loc_862")

    SetMapObjFrame(0x8, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x8, "Null_color2", 0x0, 0x1)

    label("loc_887")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C5")
    SetMapObjFrame(0x7, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x7, "Null_color2", 0x1, 0x1)
    Jump("loc_8EA")

    label("loc_8C5")

    SetMapObjFrame(0x7, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x7, "Null_color2", 0x0, 0x1)

    label("loc_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_928")
    SetMapObjFrame(0xFF, "yo_before", 0x0, 0x1)
    SetMapObjFrame(0xFF, "yo_after", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita_", 0x2, "off")
    Jump("loc_994")

    label("loc_928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_965")
    SetMapObjFrame(0xFF, "yo_before", 0x0, 0x1)
    SetMapObjFrame(0xFF, "yo_after", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita_", 0x2, "on")
    Jump("loc_994")

    label("loc_965")

    SetMapObjFrame(0xFF, "yo_before", 0x1, 0x1)
    SetMapObjFrame(0xFF, "yo_after", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita_", 0x2, "on")

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A7")
    OP_70(0xA, 0x0)
    Jump("loc_9AB")

    label("loc_9A7")

    OP_70(0xA, 0x1E)

    label("loc_9AB")

    SetMapObjFrame(0xFF, "ev_wall", 0x0, 0x1)
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9D7")
    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x6, 0x4)

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9F1")
    OP_24(0x85)
    Sound(134, 1, 100, 0)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_A16")

    label("loc_9F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0D")
    OP_24(0x85)
    Sound(134, 1, 100, 0)
    Jump("loc_A16")

    label("loc_A0D")

    Sound(133, 1, 100, 0)
    OP_24(0x86)

    label("loc_A16")

    Return()

    # Function_1_6AA end

    def Function_2_A17(): pass

    label("Function_2_A17")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B09")
    Sound(14, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅲ', 1)"), scpexpr(EXPR_END)), "loc_A9A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_B04")

    label("loc_A9A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_B04")

    Jump("loc_B46")

    label("loc_B09")

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

    label("loc_B46")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_A17 end

    def Function_3_B52(): pass

    label("Function_3_B52")

    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "比萨盒上贴着一张简单食谱。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_BF1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『热酪比萨』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_BF1")

    TalkEnd(0xFF)
    Return()

    # Function_3_B52 end

    def Function_4_BF5(): pass

    label("Function_4_BF5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FC")
    SetChrSubChip(0x8, 0x0)

    #C0006
    ChrTalk(
        0x8,
        (
            "#02301F（敲击键盘……）\x02\x03",

            "#02310F……可恶！这个方法也行不通吗！！\x01",
            "那就只好试试这个密码了……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        "#00105F（他好像很专注呢……）\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        "#00205F约纳……你在干什么？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D5A")
    Jump("loc_DA4")

    label("loc_D5A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D7A")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DA4")

    label("loc_D7A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D9A")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DA4")

    label("loc_D9A")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DA4")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Sleep(300)

    #C0009
    ChrTalk(
        0x8,
        (
            "#02305F……啊，是你们啊。\x02\x03",

            "#02302F没什么，只是发现了一些\x01",
            "令我比较在意的东西。\x02\x03",

            "#02306F现在正在\x01",
            "努力解析……\x01",
            "没想到难度还挺高呢。\x02\x03",

            "#02309F嘿嘿，天才技术员约纳大人的\x01",
            "热血已经沸腾起来啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00006F是、是吗……这个话题就先放到一边吧。\x02\x03",

            "#00001F……约纳，你看那场演讲了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#02305F啊……\x01",
            "就是那个说什么独立的？\x02\x03",

            "#02303F我在终端上看了现场直播……\x01",
            "但老实说，我现在对那件事完全没兴趣。\x02\x03",

            "#02301F总之，如果你们没有什么要事，\x01",
            "能不能先离开？\x02\x03",

            "我现在想集中精神，\x01",
            "专心解析这些数据。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0012
    ChrTalk(
        0x104,
        (
            "#00303F（唔……\x01",
            "  看来他已经完全投入到\x01",
            "  自己的世界了呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#00203F（约纳这小子，居然敢这么嚣张……\x01",
            "  之后可要好好教训他一顿。）\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00012F（算、算啦算啦……\x01",
            "  我们继续打扰他也不太好，\x01",
            "  还是以后有机会再来吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 1)
    Jump("loc_11CF")

    label("loc_10FC")

    SetChrSubChip(0x8, 0x0)

    #C0015
    ChrTalk(
        0x8,
        (
            "#02301F（敲击键盘……）\x02\x03",

            "#02310F唔……如果这样做……\x01",
            "……哇哇，果然还是不行。\x02\x03",

            "#02303F既然如此，那就再试试别的方法吧……\x01",
            "……（嘀嘀咕咕）……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00003F（完全沉浸其中了呢……\x01",
            "  还是下次再来找他吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CF")

    Jump("loc_1405")

    label("loc_11D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 7)), scpexpr(EXPR_END)), "loc_1405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1389")

    #C0017
    ChrTalk(
        0x8,
        (
            "#02304F完善的空调设备，最高级的网络环境，\x01",
            "还有这种与外界完全隔绝的感觉……\x02\x03",

            "#02302F嗯～果然如我所料，\x01",
            "第四控制终端真是太棒了。\x02\x03",

            "#02309F好，先把这个终端的运行环境\x01",
            "设定成我喜欢的样子吧¤\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00006F（唔……总有种纵容他\x01",
            "  开始散漫生活的感觉，\x01",
            "  实在是有些不安……）\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#00203F（算啦，凭他的自理能力，\x01",
            "  至少可以照顾好自己，\x01",
            "  应该不会出什么问题。）\x02\x03",

            "#00200F（之后就由我去联系主任，\x01",
            "  把这件事告诉他吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1405")

    label("loc_1389")


    #C0020
    ChrTalk(
        0x8,
        (
            "#02305F……嗯？你们还没走啊？\x02\x03",

            "#02306F我现在很忙的，\x01",
            "快走快走，你们赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#00006F（让、让人有些不爽呢……）\x02",
    )

    CloseMessageWindow()

    label("loc_1405")

    TalkEnd(0xFE)
    Return()

    # Function_4_BF5 end

    def Function_5_1409(): pass

    label("Function_5_1409")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0022
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DE")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x9, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x9, 0x0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x9)
    OP_71(0x9, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x9, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_14DE")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_5_1409 end

    def Function_6_14ED(): pass

    label("Function_6_14ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 1)), scpexpr(EXPR_END)), "loc_14F7")
    Return()

    label("loc_14F7")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    #A0023
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【消灭】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_15C3"),
        (SWITCH_DEFAULT, "loc_15DC"),
    )


    label("loc_15C3")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -5000, 0, 0, 270)
    EventEnd(0x5)
    Return()

    label("loc_15DC")

    Battle("BattleInfo_4E0", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-5000, 1000, 0, 0)
    OP_90(0x0, -5000, 0, 0, 270)
    OP_90(0x1, -5000, 0, 0, 270)
    OP_90(0x2, -5000, 0, 0, 270)
    OP_90(0x3, -5000, 0, 0, 270)
    OP_90(0x4, -5000, 0, 0, 270)
    OP_90(0x5, -5000, 0, 0, 270)
    OP_90(0x6, -5000, 0, 0, 270)
    OP_90(0x7, -5000, 0, 0, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_169E"),
        (1, "loc_16A3"),
        (SWITCH_DEFAULT, "loc_16A6"),
    )


    label("loc_169E")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_16A3")

    OP_B9(0x0)
    Return()

    label("loc_16A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xD, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "消灭了通缉魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xBC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber('缚魔', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21D, 1)
    OP_29(0x94, 0x4, 0x2)
    OP_29(0x94, 0x4, 0x10)
    OP_29(0x94, 0x1, 0x0)
    OP_E2(0x2)
    ModifyEventFlags(0, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_6_14ED end

    def Function_7_1739(): pass

    label("Function_7_1739")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有升降机的控制面板。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A4")
    Fade(500)
    SetChrPos(0x0, 111500, 0, 203500, 90)
    SetChrPos(0x1, 111500, 0, 204500, 90)
    SetChrPos(0x2, 110500, 0, 203500, 90)
    SetChrPos(0x3, 110500, 0, 204500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17FD")
    SetChrPos(0x13E, 109500, 0, 204000, 90)

    label("loc_17FD")

    OP_68(109500, 0, 204560, 0)
    MoveCamera(52, 51, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(125000, 2000, 204560, 3800)
    MoveCamera(62, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(7000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0200", 124, 0, 0)
    IdleLoop()

    label("loc_18A4")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_1739 end

    def Function_8_18AC(): pass

    label("Function_8_18AC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x64)
    Sleep(1)
    OP_68(114800, 2750, 201540, 0)
    MoveCamera(72, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26940, 0)
    OP_90(0x0, 123000, 2750, 201500, 180)
    OP_90(0x1, 122000, 2750, 201500, 180)
    OP_90(0x2, 123000, 2750, 202500, 180)
    OP_90(0x3, 122000, 2750, 202500, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_195D")
    SetChrPos(0x13E, 122500, 2750, 203500, 180)

    label("loc_195D")

    Sound(145, 0, 100, 0)
    OP_68(107500, 0, 202000, 3200)
    MoveCamera(21, 45, 0, 3200)
    OP_71(0x8, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x8)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x8, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x8, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_18AC end

    def Function_9_19E0(): pass

    label("Function_9_19E0")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有升降机的控制面板。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4B")
    Fade(500)
    SetChrPos(0x0, -296500, 0, 500, 90)
    SetChrPos(0x1, -296500, 0, 1500, 90)
    SetChrPos(0x2, -297500, 0, 500, 90)
    SetChrPos(0x3, -297500, 0, 1500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AA4")
    SetChrPos(0x13E, -298500, 0, 1000, 90)

    label("loc_1AA4")

    OP_68(-296650, 0, 650, 0)
    MoveCamera(52, 51, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(-283000, 2000, 650, 3800)
    MoveCamera(62, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0202", 101, 0, 0)
    IdleLoop()

    label("loc_1B4B")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_19E0 end

    def Function_10_1B53(): pass

    label("Function_10_1B53")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_74(0x7, 0x1E)
    OP_70(0x7, 0x64)
    Sleep(1)
    OP_68(-295800, 2750, -1500, 0)
    MoveCamera(72, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26940, 0)
    OP_90(0x0, -285000, 2750, -1500, 180)
    OP_90(0x1, -286000, 2750, -1500, 180)
    OP_90(0x2, -285000, 2750, -500, 180)
    OP_90(0x3, -286000, 2750, -500, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C04")
    SetChrPos(0x13E, -285500, 2750, 500, 180)

    label("loc_1C04")

    Sound(145, 0, 100, 0)
    OP_68(-300160, 0, -1500, 3200)
    MoveCamera(9, 44, 0, 3200)
    OP_71(0x7, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x7)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x7, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x7, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1B53 end

    def Function_11_1C87(): pass

    label("Function_11_1C87")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch03051.itc", 0x29)
    SoundLoad(904)
    OP_68(-12500, 900, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_90(0x101, -11500, 0, -700, 90)
    OP_90(0x102, -11500, 0, 700, 90)
    OP_90(0x103, -12500, 0, -1500, 90)
    OP_90(0x104, -12500, 0, 1500, 90)
    OP_90(0x109, -13500, 0, -950, 90)
    OP_90(0x105, -13500, 0, 950, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x13E, -14500, 0, 0, 90)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    SetChrPos(0x9, 3000, 20000, 0, 270)
    OP_D5(0x9, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x96)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "ev_wall", 0x1, 0x1)
    OP_68(-7500, 900, 0, 3000)
    SetCameraDistance(18000, 3000)

    def lambda_1E3C():
        OP_97(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E3C)
    Sleep(50)

    def lambda_1E59():
        OP_97(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1E59)
    Sleep(50)

    def lambda_1E76():
        OP_97(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1E76)
    Sleep(50)

    def lambda_1E93():
        OP_97(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1E93)
    Sleep(50)

    def lambda_1EB0():
        OP_97(0x109, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1EB0)
    Sleep(50)

    def lambda_1ECD():
        OP_97(0x105, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1ECD)
    Sleep(50)

    def lambda_1EEA():
        OP_97(0x13E, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 0, lambda_1EEA)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x13E, 0)
    OP_63(0x13E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0028
    ChrTalk(
        0x13E,
        "#6P#02305F啊……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(29500, 1500, 0, 4000)
    MoveCamera(42, 27, 0, 4000)
    SetCameraDistance(24500, 4000)

    def lambda_1F6F():
        OP_95(0xFE, -1500, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_1F6F)
    WaitChrThread(0x13E, 1)
    OP_6F(0x79)

    #C0029
    ChrTalk(
        0x13E,
        (
            "#02302F到了到了！\x01",
            "那里就是『第四控制终端』！\x02\x03",

            "#02309F呼～真是漫长的路途啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-3120, 900, 170, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(16149, 0)

    def lambda_2016():
        OP_97(0x101, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2016)
    Sleep(50)

    def lambda_2033():
        OP_97(0x102, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2033)
    Sleep(50)

    def lambda_2050():
        OP_97(0x103, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2050)
    Sleep(50)

    def lambda_206D():
        OP_97(0x104, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_206D)
    Sleep(50)

    def lambda_208A():
        OP_97(0x109, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_208A)
    Sleep(50)

    def lambda_20A7():
        OP_97(0x105, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_20A7)
    OP_0D()
    WaitChrThread(0x104, 0)

    #C0030
    ChrTalk(
        0x104,
        (
            "#00306F真是的，明明是我们\x01",
            "比较累吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20F0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13E, 2, lambda_20F0)

    #C0031
    ChrTalk(
        0x109,
        (
            "#6P#10112F呵呵，算了算了。\x02\x03",

            "#10100F毕竟他不习惯这种长途跋涉，\x01",
            "光是跟上我们的步调就已经很辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00104F说的也是……\x01",
            "我们以前也曾累得气喘吁吁呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        (
            "#6P#00202F而且约纳基本足不出户，\x01",
            "比以前的我还要夸张……\x02\x03",

            "#00204F能跟上我们，\x01",
            "说明他已经相当努力了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x13E,
        "#02310F#11P唔唔……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x105,
        (
            "#10306F#6P不过，你平时好像只喜欢吃\x01",
            "比萨和甜点啊。\x02\x03",

            "#10302F现在年纪小还无所谓，\x01",
            "等长大之后可怎么办啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#6P#00005F约纳，如果你愿意，\x01",
            "以后要不要和我一起晨跑？\x02\x03",

            "#00000F就算一周只跑一次也可以哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0037
    ChrTalk(
        0x13E,
        (
            "#02311F#11P啊啊！够了！你们别管这么多！\x02\x03",

            "#02301F总之，我现在已经快热死了，\x01",
            "先去终端室把空调给——\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0038
    ChrTalk(
        0x103,
        "#6P#00207F#4S约纳！到这边来！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    Fade(250)
    OP_68(3000, 12500, 0, 0)
    MoveCamera(90, 63, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    Sound(834, 0, 100, 0)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_68(3000, 2000, 0, 1500)
    MoveCamera(90, 25, 0, 1500)
    ClearMapObjFlags(0x0, 0x4)
    SetChrFlags(0x9, 0x1)

    def lambda_2422():
        OP_96(0xFE, 0xBB8, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2422)
    WaitChrThread(0x9, 1)
    CancelBlur(0)
    OP_63(0x13E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_245D():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_245D)
    Sound(833, 0, 100, 0)
    Sound(902, 0, 100, 0)
    SetCameraDistance(19500, 1000)
    OP_82(0x0, 0x2BC, 0xBB8, 0x3E8)
    Sleep(2000)
    Fade(250)
    OP_68(-1600, 2000, 0, 0)
    MoveCamera(47, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    Sound(904, 2, 100, 0)
    BeginChrThread(0x9, 3, 0, 13)
    BeginChrThread(0x101, 3, 0, 12)
    OP_63(0x13E, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_24FB():

        label("loc_24FB")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_24FB")

    QueueWorkItem2(0x13E, 2, lambda_24FB)

    def lambda_250D():
        OP_96(0xFE, 0xFFFFF31C, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_250D)
    WaitChrThread(0x13E, 1)
    EndChrThread(0x13E, 0x2)
    OP_64(0x13E)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7453", 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0039
    ChrTalk(
        0x13E,
        "#02307F#4S#6P#N什、什什什什么！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    #C0040
    ChrTalk(
        0x101,
        "#00010F#6P#N这家伙是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0041
    ChrTalk(
        0x104,
        (
            "#00307F#6P#N是在Ｂ区域四处徘徊的\x01",
            "那种扫除机器人的加大版吗……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0042
    ChrTalk(
        0x103,
        (
            "#00201F#6P#N不，似乎并不是那种\x01",
            "可以轻易对付的对手……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0043
    ChrTalk(
        0x102,
        "#00107F#5P约纳，你快退后！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13E, 0x102, 500)

    #C0044
    ChrTalk(
        0x13E,
        "#02310F#12P#N我、我知道啦……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x13E, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x13E, 0x10E, 0x1F4)

    def lambda_26C9():
        OP_95(0xFE, -6500, 0, -2500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_26C9)
    WaitChrThread(0x13E, 1)
    OP_68(-1600, 2000, 0, 10000)
    MoveCamera(64, 13, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(15500, 10000)

    def lambda_2715():
        OP_95(0xFE, -9000, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_2715)
    WaitChrThread(0x13E, 1)

    def lambda_2733():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_2733)
    WaitChrThread(0x13E, 1)
    OP_64(0x13E)
    Sound(903, 0, 100, 0)
    SetMessageWindowPos(270, 90, -1, -1)
    SetChrName("电子音")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＰＰＰＰ……\x01",
            "发现目标……\x02",
        )
    )

    CloseMessageWindow()

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……连接网络数据库……\x02",
        )
    )

    CloseMessageWindow()

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "确定对象身份……\x01",
            "克洛斯贝尔警察局·特别任务支援科……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0048
    ChrTalk(
        0x101,
        "#00011F#6P#N这、这家伙是怎么回事！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0049
    ChrTalk(
        0x103,
        "#00205F#6P#N……难道说……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0050
    ChrTalk(
        0x105,
        (
            "#10310F#6P#N它还特地通过网络\x01",
            "确定了我们的身份吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_6F(0x79)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(5040, 2200, 1900, 1500)
    MoveCamera(64, 12, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(15500, 1500)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(500)
    Sound(903, 0, 100, 0)
    SetMessageWindowPos(260, 70, -1, -1)
    SetChrName("电子音")

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＰＰＰ……\x01",
            "危险程度判定为３级……\x02",
        )
    )

    CloseMessageWindow()

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "总而言之，先将目标排除……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0053
    ChrTalk(
        0x102,
        "#00111F#6P#N居、居然说什么总而言之……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0054
    ChrTalk(
        0x104,
        (
            "#00310F#6P#N身为一台机械，\x01",
            "这种言行也太随便了吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0055
    ChrTalk(
        0x109,
        "#10107F#6P#N我们准备迎击吧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_6F(0x79)
    OP_68(5040, 2200, 0, 1500)
    MoveCamera(90, 20, 0, 1500)
    SetCameraDistance(17500, 1500)
    Sound(576, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x136, 0x14A, 0x0, 0x0)
    Sleep(500)
    Sound(905, 0, 100, 0)
    OP_79(0x0)
    StopSound(904, 500, 100)
    OP_6F(0x79)
    Sleep(500)
    Sound(579, 2, 100, 0)
    Sound(594, 2, 100, 0)
    Sound(378, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x14A, 0x172, 0x0, 0x20)
    BlurSwitch(0x384, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    MoveCamera(90, 13, 0, 900)
    SetCameraDistance(11500, 900)
    Sleep(900)
    StopSound(579, 300, 100)
    StopSound(594, 300, 100)
    OP_24(0x388)
    SetChrBattleFlags(0x13E, 0x8)
    Battle("BattleInfo_49C", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    Call(0, 14)
    Return()

    # Function_11_1C87 end

    def Function_12_2B29(): pass

    label("Function_12_2B29")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Return()

    # Function_12_2B29 end

    def Function_13_2BB1(): pass

    label("Function_13_2BB1")

    OP_71(0x0, 0x96, 0xAA, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0xA, 0x31, 0x0, 0x20)
    Return()

    # Function_13_2BB1 end

    def Function_14_2BCD(): pass

    label("Function_14_2BCD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch03051.itc", 0x29)
    LoadChrToIndex("apl/ch51770.itc", 0x2A)
    OP_68(-1900, 1000, 0, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(18000, 0)
    OP_90(0x101, -3300, 0, -700, 90)
    OP_90(0x102, -3300, 0, 700, 90)
    OP_90(0x103, -4400, 0, -1500, 90)
    OP_90(0x104, -4400, 0, 1500, 90)
    OP_90(0x109, -5500, 0, -1100, 90)
    OP_90(0x105, -5500, 0, 1100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x13E, -15000, 0, 0, 90)
    SetChrPos(0xA, -4500, 0, 0, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    OP_68(-3900, 1000, 0, 2000)
    SetCameraDistance(17000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0056
    ChrTalk(
        0x101,
        "#00013F#6P刚刚那台机器是……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#00106F#5P不、不管怎么看，\x01",
            "都不可能是非法丢弃的\x01",
            "普通机械吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#6P#00206F很可能与『结社』\x01",
            "存在一定关联呢……\x02\x03",

            "#00201F而且它的反应与那台看守\x01",
            "鲁巴彻会长室的智能兵器很相似。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    def lambda_2E68():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2E68)
    Sleep(50)

    def lambda_2E78():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2E78)
    Sleep(50)

    def lambda_2E88():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2E88)
    Sleep(50)

    def lambda_2E98():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E98)
    Sleep(50)

    def lambda_2EA8():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2EA8)
    Sleep(50)

    def lambda_2EB8():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2EB8)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    #C0059
    ChrTalk(
        0x104,
        (
            "#00306F#5P是说那台像武士一样的大家伙吗……\x02\x03",

            "#00301F不过，这台的性能\x01",
            "似乎比那台更高呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x105,
        (
            "#10308F嗯，而且好像还连接\x01",
            "了导力网络。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x109,
        (
            "#6P#10101F这显然是『结社』\x01",
            "动的手脚吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x13E,
        (
            "#02304F#2P好啦，想那么多\x01",
            "也无济于事吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2FBF():
        OP_96(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_2FBF)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-5400, 1000, 0, 2500)

    def lambda_305F():

        label("loc_305F")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_305F")

    QueueWorkItem2(0x109, 2, lambda_305F)

    def lambda_3071():

        label("loc_3071")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_3071")

    QueueWorkItem2(0x105, 2, lambda_3071)
    Sleep(50)

    def lambda_3086():

        label("loc_3086")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_3086")

    QueueWorkItem2(0x103, 2, lambda_3086)

    def lambda_3098():

        label("loc_3098")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_3098")

    QueueWorkItem2(0x104, 2, lambda_3098)
    Sleep(50)

    def lambda_30AD():

        label("loc_30AD")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_30AD")

    QueueWorkItem2(0x101, 2, lambda_30AD)

    def lambda_30BF():

        label("loc_30BF")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_30BF")

    QueueWorkItem2(0x102, 2, lambda_30BF)
    WaitChrThread(0x13E, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)

    #C0063
    ChrTalk(
        0x13E,
        (
            "#6P#02306F与其讨论这些，还不如\x01",
            "赶快去终端室享受冷气。\x02\x03",

            "#02302F至于那些家伙的动向，\x01",
            "约纳大人会帮你们调查的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0064
    ChrTalk(
        0x101,
        (
            "#00006F#11P你可真是……该说你从容不迫呢，\x01",
            "还是精力旺盛呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x109,
        (
            "#12P#10112F呵呵，总之是个\x01",
            "很有胆量的孩子。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(133, 1000, 100)
    StopBGM(0xFA0)
    WaitBGM()
    SoundLoad(134)
    SoundLoad(938)
    OP_68(100700, 4500, 0, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 100500, 0, 200, 90)
    SetChrPos(0x102, 100500, 0, -1000, 90)
    SetChrPos(0x103, 101600, 0, 1200, 180)
    SetChrPos(0x104, 100400, 0, 1700, 135)
    SetChrPos(0x109, 99300, 0, 400, 90)
    SetChrPos(0x105, 99300, 0, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x13E, 0x4)
    SetChrFlags(0x13E, 0x20)
    SetChrFlags(0x13E, 0x10)
    SetChrFlags(0x13E, 0x2)
    SetChrPos(0x13E, 102500, 250, -100, 90)
    SetChrChipByIndex(0x13E, 0x2A)
    SetChrSubChip(0x13E, 0x2)
    BeginChrThread(0x13E, 2, 0, 15)
    SetMapObjFrame(0xFF, "monita_", 0x2, "on")
    SetMapObjFrame(0xFF, "yo_before", 0x1, 0x1)
    SetMapObjFrame(0xFF, "yo_after", 0x0, 0x1)
    Sound(134, 2, 100, 0)
    Sound(938, 2, 100, 0)
    Sleep(1000)
    PlayBGM("ed7521", 0)
    Sleep(2500)
    OP_68(100700, 1500, 0, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(102380, 1000, 220, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    OP_24(0x3AA)
    EndChrThread(0x13E, 0x2)

    #C0066
    ChrTalk(
        0x13E,
        (
            "#02305F#5P嗯……\x01",
            "刚才那台机器似乎是在\x01",
            "一个月之前投放在这里的。\x02\x03",

            "#02303F而且还装设了可以无线连接到\x01",
            "导力网络的装置……\x02\x03",

            "#02301F在记录中留下了\x01",
            "管理者的名字：『诺华提斯』。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        "#6P#00008F诺华提斯……是那个白衣男人啊。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#6P#00108F那个人在『结社』中\x01",
            "好像拥有相当高的地位。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_350D():
        TurnDirection(0x104, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_350D)
    Sleep(50)

    def lambda_351D():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_351D)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0069
    ChrTalk(
        0x104,
        (
            "#00301F#5P那个大叔看起来有些疯狂……\x01",
            "给人一种不舒服的诡异感呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x103,
        (
            "#5P#00206F……他说不定是抱着恶作剧的心态，\x01",
            "放出了这种试验作品吧。\x02\x03",

            "#00211F该怎么说呢，他看起来就很像是\x01",
            "喜欢做这种事的性格。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x105,
        "#6P#10306F嗯，确实有那种感觉。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x109,
        (
            "#6P#10108F他恐怕是一个比外表看起来\x01",
            "更加危险的人物……\x02",
        )
    )

    CloseMessageWindow()
    Sound(938, 2, 100, 0)
    BeginChrThread(0x13E, 2, 0, 15)

    #C0073
    ChrTalk(
        0x13E,
        (
            "#02304F#5P不过，似乎只在\x01",
            "这里放置了一台……\x02\x03",

            "#02302F既然如此，我就可以毫无顾虑地\x01",
            "驻扎在这里啦！\x02\x03",

            "嘿嘿～这里离兰花塔很近，\x01",
            "不但连接速度极快，\x01",
            "而且几乎没有任何限制……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0074
    ChrTalk(
        0x13E,
        (
            "#02309F#5P#4S哈哈！\x01",
            "第四控制终端太棒了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_3783():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3783)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_37C0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_37C0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0075
    ChrTalk(
        0x101,
        "#6P#00012F他很开心呢。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#00306F他果然打算\x01",
            "窝在这里不出门啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        (
            "#5P#00203F约纳……我会把这里的事情\x01",
            "报告给主任哦。\x02\x03",

            "#00211F你可不要太乱来。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x13E,
        (
            "#02304F#5P好啦，我知道的。\x02\x03",

            "#02302F接下来有我一个人就够了，\x01",
            "你们赶快走吧。\x02\x03",

            "#02305F哦哦，这种地方竟然有\x01",
            "新的服务器。\x02\x03",

            "#02309F哎呀，克洛斯贝尔的网络环境\x01",
            "真是有了大幅度的改善啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x105,
        (
            "#6P#10304F哎呀呀……\x01",
            "他完全沉浸其中了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x109,
        (
            "#6P#10102F呵呵……\x01",
            "看样子，应该不会有什么问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        (
            "#6P#00108F嗯，但『结社』的动向\x01",
            "还是有些让人担心……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0082
    ChrTalk(
        0x101,
        (
            "#5P#00004F以后定期\x01",
            "来这里看看吧。\x02\x03",

            "#00000F我怕他会一直窝在这里，\x01",
            "连门都不出。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A43():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3A43)
    Sleep(50)

    def lambda_3A53():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3A53)
    Sleep(50)

    def lambda_3A63():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3A63)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    #C0083
    ChrTalk(
        0x103,
        "#5P#00202F是啊。\x02",
    )

    CloseMessageWindow()
    StopSound(938, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    OP_37()
    EndChrThread(0x13E, 0xFF)
    SetChrChipByIndex(0x13E, 0xFF)
    SetChrSubChip(0x13E, 0x0)
    RemoveParty(0x3D, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x0, 98000, 0, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetMapObjFrame(0xFF, "ev_wall", 0x0, 0x1)
    SetScenarioFlags(0x181, 7)
    OP_29(0xAC, 0x1, 0x9)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_14_2BCD end

    def Function_15_3B30(): pass

    label("Function_15_3B30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B48")
    OP_A1(0xFE, 0x7D0, 0x2, 0x2, 0x3)
    Jump("Function_15_3B30")

    label("loc_3B48")

    Return()

    # Function_15_3B30 end

    def Function_16_3B49(): pass

    label("Function_16_3B49")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B74")
    Sound(836, 0, 100, 0)
    Sleep(600)
    Sound(836, 0, 100, 0)
    Sleep(600)
    Sound(836, 0, 100, 0)
    Sleep(800)
    Jump("Function_16_3B49")

    label("loc_3B74")

    Return()

    # Function_16_3B49 end

    def Function_17_3B75(): pass

    label("Function_17_3B75")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(29200, 900, -400, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 31000, 0, -400, 270)
    SetChrPos(0x102, 31000, 0, -400, 270)
    SetChrPos(0x103, 31000, 0, -400, 270)
    SetChrPos(0x104, 31000, 0, -400, 270)
    SetChrPos(0x109, 31000, 0, -400, 270)
    SetChrPos(0x105, 31000, 0, -400, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(28200, 900, -400, 4500)
    SetCameraDistance(18000, 4500)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(102, 0, 100, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x3)
    BeginChrThread(0x101, 3, 0, 18)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 19)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 21)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 22)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    BeginChrThread(0x105, 3, 0, 23)
    Sleep(1000)
    Sound(102, 0, 100, 0)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    #C0084
    ChrTalk(
        0x101,
        (
            "#11P#00005F对了……\x02\x03",

            "#00000F约纳之前好像说过吧，\x01",
            "这附近有个直接通向\x01",
            "出口的升降机。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0085
    ChrTalk(
        0x103,
        "#12P#00202F是的，就在那边。\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1100, 25500, 4000)
    MoveCamera(30, 25, 0, 4000)
    SetCameraDistance(26000, 4000)

    def lambda_3DC2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3DC2)
    Sleep(50)

    def lambda_3DD2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3DD2)
    Sleep(50)

    def lambda_3DE2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3DE2)
    Sleep(50)

    def lambda_3DF2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3DF2)
    Sleep(50)

    def lambda_3E02():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3E02)
    OP_6F(0x79)
    Sleep(300)

    #A0086
    AnonymousTalk(
        0x103,
        (
            "#00204F看来这个地方\x01",
            "位于兰花塔的\x01",
            "地基附近。\x02\x03",

            "#00202F搭乘那里的升降机，就可以\x01",
            "直达港湾区的灯塔了。\x02",
        )
    )

    CloseMessageWindow()

    #A0087
    AnonymousTalk(
        0x102,
        "#00106F呼，那真是太好了。\x02",
    )

    CloseMessageWindow()

    #A0088
    AnonymousTalk(
        0x104,
        (
            "#00306F如果回程还要再走一次那条\x01",
            "热得要人命的道路，就太麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #A0089
    AnonymousTalk(
        0x105,
        "#10309F呵呵，确实。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(28200, 900, -400, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    TurnDirection(0x105, 0x101, 500)

    #C0090
    ChrTalk(
        0x105,
        (
            "#10300F#5P话说回来……\x01",
            "现在已是黄昏时分了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F68():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F68)
    Sleep(50)

    def lambda_3F78():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3F78)
    Sleep(50)

    def lambda_3F88():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3F88)
    Sleep(50)

    def lambda_3F98():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3F98)
    Sleep(50)

    def lambda_3FA8():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3FA8)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)

    #C0091
    ChrTalk(
        0x109,
        "#12P#10106F嗯，是啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0092
    ChrTalk(
        0x109,
        (
            "#10112F#11P……那我们这就搭乘升降机，\x01",
            "回到地面如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#6P#00002F嗯……好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 28000, 0, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 0)
    ModifyEventFlags(1, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_17_3B75 end

    def Function_18_407F(): pass

    label("Function_18_407F")


    def lambda_4084():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4084)

    def lambda_409E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_409E)
    WaitChrThread(0xFE, 1)

    def lambda_40B3():
        OP_96(0xFE, 0x6A40, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40B3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_407F end

    def Function_19_40CD(): pass

    label("Function_19_40CD")


    def lambda_40D2():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40D2)

    def lambda_40EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40EC)
    WaitChrThread(0xFE, 1)

    def lambda_4101():
        OP_96(0xFE, 0x6A40, 0x0, 0xC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4101)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_40CD end

    def Function_20_411B(): pass

    label("Function_20_411B")


    def lambda_4120():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4120)

    def lambda_413A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_413A)
    WaitChrThread(0xFE, 1)

    def lambda_414F():
        OP_95(0xFE, 28200, 0, -1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_414F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_20_411B end

    def Function_21_4170(): pass

    label("Function_21_4170")


    def lambda_4175():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4175)

    def lambda_418F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_418F)
    WaitChrThread(0xFE, 1)

    def lambda_41A4():
        OP_95(0xFE, 28200, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41A4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_4170 end

    def Function_22_41C5(): pass

    label("Function_22_41C5")


    def lambda_41CA():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41CA)

    def lambda_41E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41E4)
    WaitChrThread(0xFE, 1)

    def lambda_41F9():
        OP_95(0xFE, 29200, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41F9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_22_41C5 end

    def Function_23_421A(): pass

    label("Function_23_421A")


    def lambda_421F():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_421F)

    def lambda_4239():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4239)
    WaitChrThread(0xFE, 1)

    def lambda_424E():
        OP_95(0xFE, 29200, 0, 200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_424E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_23_421A end

    def Function_24_426F(): pass

    label("Function_24_426F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(938)
    LoadChrToIndex("apl/ch51770.itc", 0x1E)
    LoadChrToIndex("apl/ch51523.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis421.itp")
    OP_68(103460, 1000, -170, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 102500, 250, -100, 90)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrPos(0x8, 102500, 250, -100, 90)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 15)
    ClearScenarioFlags(0x0, 2)
    Sleep(500)
    Sound(938, 2, 100, 0)
    Sleep(2000)
    PlayBGM("ed7521", 0)
    SetCameraDistance(15000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    StopSound(938, 300, 100)
    EndChrThread(0x8, 0x2)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    Sleep(110)
    SetChrSubChip(0x8, 0x1)
    Sleep(110)
    SetChrSubChip(0x8, 0x2)
    Sleep(110)
    SetChrSubChip(0x8, 0x1)
    Sleep(110)
    SetChrSubChip(0x8, 0x2)
    Sleep(110)
    SetChrSubChip(0x8, 0x1)
    Sleep(110)
    SetChrSubChip(0x8, 0x2)

    #C0094
    ChrTalk(
        0x8,
        (
            "#5P#02306F嗯……！\x02\x03",

            "#02301F嗯？现在几点了……\x02\x03",

            "#02305F……哇，已经是早上了吗！？\x02",
        )
    )

    CloseMessageWindow()
    Sound(906, 0, 100, 0)
    Sleep(800)
    OP_63(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0095
    ChrTalk(
        0x8,
        (
            "#5P#02306F唉……\x01",
            "肚子饿得咕咕叫了。\x02\x03",

            "#02300F对了，那家比萨店\x01",
            "从几点开始营业来着？\x02",
        )
    )

    CloseMessageWindow()
    Sound(938, 2, 100, 0)
    BeginChrThread(0x8, 2, 0, 26)
    OP_68(103460, 1000, -170, 1800)
    MoveCamera(53, 28, 0, 1800)
    SetCameraDistance(13500, 1800)
    OP_6F(0x79)
    SetCameraDistance(13000, 20000)
    Sleep(300)

    #C0096
    ChrTalk(
        0x8,
        (
            "#6P#02302F我记得那家店说过\x01",
            "要导入导力网络呢……\x02\x03",

            "#02309F嘿嘿，只要调查一下就知道了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0097
    ChrTalk(
        0x8,
        (
            "#6P#02305F咦……？\x02\x03",

            "#02301F……这是什么？\x01",
            "这些像垃圾一样的数据……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 1, 0, 25)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 27)
    Sleep(500)

    #C0098
    ChrTalk(
        0x8,
        "#6P#02310F不对，这好像并不是数据。\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    SetScenarioFlags(0x0, 2)
    WaitChrThread(0x8, 2)
    Fade(500)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x5)
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    BeginChrThread(0x8, 2, 0, 28)
    Sleep(1000)

    #C0099
    ChrTalk(
        0x8,
        (
            "#6P#02310F……构造体……？\x01",
            "不对，这程度远远超越构造体……\x02\x03",

            "#02305F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    SetCameraDistance(12000, 4000)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    EndChrThread(0xC, 0x1)
    StopSound(938, 1000, 100)
    StopSound(134, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_64(0x8)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0100
    AnonymousTalk(
        0x8,
        "这是怎么回事啊！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)
    Sound(6, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    ReplaceBGM(-1, -1)
    OP_24(0x3AA)
    OP_24(0x86)
    SetScenarioFlags(0x23, 4)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_426F end

    def Function_25_46F8(): pass

    label("Function_25_46F8")

    Sleep(2200)

    label("loc_46FB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4714")
    Sound(836, 0, 50, 0)
    Sleep(700)
    Jump("loc_46FB")

    label("loc_4714")

    Return()

    # Function_25_46F8 end

    def Function_26_4715(): pass

    label("Function_26_4715")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_472D")
    OP_A1(0xFE, 0x5DC, 0x2, 0x3, 0x4)
    Jump("Function_26_4715")

    label("loc_472D")

    Return()

    # Function_26_4715 end

    def Function_27_472E(): pass

    label("Function_27_472E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4745")
    OP_A1(0xFE, 0x7D0, 0x2, 0x2, 0x3)
    Jump("Function_27_472E")

    label("loc_4745")

    Return()

    # Function_27_472E end

    def Function_28_4746(): pass

    label("Function_28_4746")

    OP_A1(0xFE, 0x7D0, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x7D0, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x834, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x834, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x834, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x834, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x898, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x898, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x898, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x898, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x8FC, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x8FC, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x8FC, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x8FC, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x960, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x960, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x960, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x960, 0x2, 0x5, 0x6)

    label("loc_47D6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47EE")
    OP_A1(0xFE, 0x9C4, 0x2, 0x5, 0x6)
    Jump("loc_47D6")

    label("loc_47EE")

    Return()

    # Function_28_4746 end

    def Function_29_47EF(): pass

    label("Function_29_47EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch29300.itc", 0x1E)
    SoundLoad(825)
    SoundLoad(931)
    OP_68(102700, 1000, 0, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 102500, 250, -100, 90)
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 102300, 0, 900, 135)
    Sound(825, 2, 100, 0)
    Sound(931, 2, 50, 0)
    SetCameraDistance(15000, 2000)
    FadeToBright(2000, 0)
    Sleep(100)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0101
    ChrTalk(
        0x8,
        (
            "#6P#02307F这、这是怎么回事……！？\x02\x03",

            "#02310F经过转换的导力能源\x01",
            "正在流向兰花塔！？\x02",
        )
    )

    CloseMessageWindow()
    StopSound(825, 2000, 100)
    StopSound(931, 2000, 50)
    SetCameraDistance(14500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_64(0x8)
    OP_64(0xB)
    SetScenarioFlags(0x22, 1)
    NewScene("t1490", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_47EF end

    def Function_30_4955(): pass

    label("Function_30_4955")

    EventBegin(0x1)

    #C0102
    ChrTalk(
        0x101,
        (
            "#00005F不对，这边通往我们来时的道路。\x02\x03",

            "#00000F难得有近路可走，\x01",
            "我们就乘坐直达升降机回到地面上吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -8310, -10, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_30_4955 end

    SaveToFile()

Try(main)
