from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1420.bin",                # FileName
        "c1420",                    # MapName
        "c1420",                    # Location
        0x002F,                     # MapIndex
        "ed7116",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 47, 0, 5, 0, 6],
    )

    BuildStringList((
        "c1420",                  # 0
        "ヴァルド",               # 1
        "ルガノフ",               # 2
        "ジェド",                 # 3
        "ヒューイ",               # 4
        "スラッシュ",             # 5
        "コウキ",                 # 6
        "ディーノ",               # 7
        "ヴァルド",               # 8
        "ルガノフ",               # 9
        "ヒューイ",               # 10
        "ドラム缶",               # 11
        "叩かれたドラム缶",       # 12
        "bc1420",                 # 13
    ))

    ATBonus("ATBonus_288", 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_378", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 4, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 9, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 11, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 12, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_35C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_360", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_364", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_368", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_36C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_370", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_398", 0x0002, 6, 6, 180, 0, 0, 0, 0, "bc1420", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_378", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_288"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch02100.itc",                   # 00
        "apl/ch50018.itc",                   # 01
        "chr/ch06800.itc",                   # 02
        "chr/ch30800.itc",                   # 03
        "chr/ch31700.itc",                   # 04
        "chr/ch30802.itc",                   # 05
        "chr/ch31702.itc",                   # 06
        "apl/ch50019.itc",                   # 07
    ))

    DeclNpc(16829,   1000,    -600,    315,  389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(17079,   1000,    -2579,   225,  261,  0x0, 0,   3,   0,   0,   1,   0,   15,  255,  0)
    DeclNpc(12189,   0,       -5269,   270,  261,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(18700,   4000,    -8210,   315,  261,  0x0, 0,   4,   0,   0,   2,   0,   20,  255,  0)
    DeclNpc(1779,    0,       -5260,   90,   261,  0x0, 0,   3,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(11420,   0,       7809,    0,    261,  0x0, 0,   3,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(2920,    0,       6769,    89,   389,  0x0, 0,   2,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(17600,   1100,    -180,    270,  261,  0x0, 0,   1,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(14000,   699,     3279,    270,  389,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(8250,    200,     -6360,   270,  389,  0x0, 0,   6,   0,   255, 255, 0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  13.130000114440918,    -0.0,                  0.0,                   16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.565000057220459,    0.0,                   -0.0,                  1.0])

    DeclActor(19430,   1000,    70,      1000,    20000,   2500,    -40,     0x007C, 0,  33, 0x0000)

    ScpFunction((
        "Function_0_464",          # 00, 0
        "Function_1_51C",          # 01, 1
        "Function_2_547",          # 02, 2
        "Function_3_5BC",          # 03, 3
        "Function_4_5E7",          # 04, 4
        "Function_5_612",          # 05, 5
        "Function_6_C7C",          # 06, 6
        "Function_7_CED",          # 07, 7
        "Function_8_12AE",         # 08, 8
        "Function_9_26D8",         # 09, 9
        "Function_10_2867",        # 0A, 10
        "Function_11_2D03",        # 0B, 11
        "Function_12_301B",        # 0C, 12
        "Function_13_30FC",        # 0D, 13
        "Function_14_31F5",        # 0E, 14
        "Function_15_3331",        # 0F, 15
        "Function_16_3E59",        # 10, 16
        "Function_17_3F9E",        # 11, 17
        "Function_18_4BF4",        # 12, 18
        "Function_19_4CEF",        # 13, 19
        "Function_20_4D3E",        # 14, 20
        "Function_21_5C1C",        # 15, 21
        "Function_22_5E66",        # 16, 22
        "Function_23_5F08",        # 17, 23
        "Function_24_5F77",        # 18, 24
        "Function_25_623A",        # 19, 25
        "Function_26_71EE",        # 1A, 26
        "Function_27_72F2",        # 1B, 27
        "Function_28_7EE4",        # 1C, 28
        "Function_29_801F",        # 1D, 29
        "Function_30_80D9",        # 1E, 30
        "Function_31_85C9",        # 1F, 31
        "Function_32_9BDD",        # 20, 32
        "Function_33_ADA5",        # 21, 33
    ))


    def Function_0_464(): pass

    label("Function_0_464")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4A4"),
        (1, "loc_4B0"),
        (2, "loc_4BC"),
        (3, "loc_4C8"),
        (4, "loc_4D4"),
        (5, "loc_4E0"),
        (6, "loc_4EC"),
        (SWITCH_DEFAULT, "loc_4F8"),
    )


    label("loc_4A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_504")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_51B")

    Return()

    # Function_0_464 end

    def Function_1_51C(): pass

    label("Function_1_51C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_546")
    OP_94(0xFE, 0x38C2, 0xFFFFF1B4, 0x4902, 0xFFFFF984, 0x3E8)
    Sleep(300)
    Jump("Function_1_51C")

    label("loc_546")

    Return()

    # Function_1_51C end

    def Function_2_547(): pass

    label("Function_2_547")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BB")
    OP_95(0xFE, 20920, 4000, -8210, 1000, 0x0)
    OP_95(0xFE, 20920, 4000, 760, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0xC8)
    Sleep(2500)
    OP_95(0xFE, 20920, 4000, -8210, 1000, 0x0)
    OP_95(0xFE, 18700, 4000, -8210, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0xC8)
    Sleep(4500)
    Jump("Function_2_547")

    label("loc_5BB")

    Return()

    # Function_2_547 end

    def Function_3_5BC(): pass

    label("Function_3_5BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E6")
    OP_94(0xFE, 0x2DAA, 0xFFFFEF98, 0x2526, 0xFFFFDA8A, 0x3E8)
    Sleep(300)
    Jump("Function_3_5BC")

    label("loc_5E6")

    Return()

    # Function_3_5BC end

    def Function_4_5E7(): pass

    label("Function_4_5E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_611")
    OP_94(0xFE, 0x1266, 0xC94, 0x636, 0xFFFFF43E, 0x3E8)
    Sleep(300)
    Jump("Function_4_5E7")

    label("loc_611")

    Return()

    # Function_4_5E7 end

    def Function_5_612(): pass

    label("Function_5_612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_628")
    SetMapFlags(0x10000000)
    Event(0, 31)

    label("loc_628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_637")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 32)

    label("loc_637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_687")
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 17200, 1000, 0, 45)
    SetChrPos(0xB, 10340, 0, -9190, 315)
    OP_93(0xD, 0xE1, 0x0)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0x7)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_C7B")

    label("loc_687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6D3")
    SetChrPos(0xD, 16360, 990, -40, 90)
    SetChrPos(0xB, 9090, 0, -4900, 315)
    SetChrPos(0xC, 8109, 0, -3920, 135)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_C7B")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_71A")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xB, 16180, 3180, -8260, 315)
    SetChrPos(0xE, 12190, 0, -5270, 270)
    OP_93(0xD, 0xE1, 0x0)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_C7B")

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_786")
    SetChrPos(0xA, 16360, 990, -40, 90)
    SetChrPos(0xB, 9090, 0, -4900, 315)
    SetChrPos(0xC, 8109, 0, -3920, 135)
    OP_93(0xD, 0x87, 0x0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_781")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_781")

    Jump("loc_C7B")

    label("loc_786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7F9")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, 8000, 0, -200, 270)
    SetChrPos(0xE, 6200, 0, -200, 90)
    SetChrPos(0xB, 11180, 0, -7240, 315)
    OP_93(0xC, 0x2D, 0x0)
    OP_93(0xD, 0xE1, 0x0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xE, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F4")
    SetChrFlags(0xB, 0x10)

    label("loc_7F4")

    Jump("loc_C7B")

    label("loc_7F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_853")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xA, 12600, 0, 4190, 135)
    SetChrPos(0xC, 7520, 0, -4660, 180)
    SetChrPos(0xD, 17920, 1000, 1070, 225)
    SetChrFlags(0xA, 0x10)
    Jump("loc_C7B")

    label("loc_853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8B2")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x8, 11640, 0, 270, 270)
    SetChrPos(0xA, 10370, 0, 1010, 135)
    SetChrPos(0xC, 10260, 0, -800, 45)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_C7B")

    label("loc_8B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_906")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 3640, 0, 2640, 225)
    SetChrPos(0xE, 17110, 1000, -40, 90)
    BeginChrThread(0xD, 0, 0, 4)
    Jump("loc_C7B")

    label("loc_906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_963")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 9090, 0, -4900, 315)
    SetChrPos(0xE, 8109, 0, -3920, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95E")
    SetChrFlags(0xD, 0x10)

    label("loc_95E")

    Jump("loc_C7B")

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9AD")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xB, 5260, 0, -1000, 0)
    SetChrPos(0xC, 5260, 0, 600, 180)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_C7B")

    label("loc_9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_A04")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3840, 0, -200, 90)
    BeginChrThread(0xE, 0, 0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FF")
    SetChrFlags(0xE, 0x10)

    label("loc_9FF")

    Jump("loc_C7B")

    label("loc_A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A7B")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xA, 16390, 1000, 410, 135)
    SetChrPos(0x9, 16200, 1000, -1090, 45)
    SetChrPos(0xB, 5260, 0, -1000, 0)
    SetChrPos(0xC, 5260, 0, 600, 180)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_C7B")

    label("loc_A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_AB5")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 6170, 0, -890, 315)
    SetChrPos(0xD, 5200, 0, 80, 135)
    Jump("loc_C7B")

    label("loc_AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B44")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 8290, 0, 10, 270)
    SetChrPos(0xB, 6500, 0, 10, 90)
    SetChrPos(0xC, 10490, 0, -7280, 315)
    SetChrPos(0xD, 3640, 0, 2640, 225)
    BeginChrThread(0xB, 0, 0, 0)
    BeginChrThread(0xC, 0, 0, 3)
    BeginChrThread(0xD, 0, 0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2D")
    SetChrFlags(0xA, 0x10)

    label("loc_B2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3F")
    SetChrFlags(0xB, 0x10)

    label("loc_B3F")

    Jump("loc_C7B")

    label("loc_B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_B7C")
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, 15960, 1000, 350, 135)
    SetChrFlags(0x9, 0x10)
    Jump("loc_C7B")

    label("loc_B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B8A")
    Jump("loc_C7B")

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_C1C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x9, 12600, 0, 3440, 315)
    SetChrPos(0xA, 11540, 0, 4580, 135)
    SetChrPos(0xD, 16360, 990, -40, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF1")
    SetChrFlags(0xD, 0x10)

    label("loc_BF1")

    Jump("loc_C17")

    label("loc_BF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_C0D")
    SetChrFlags(0x9, 0x10)
    Jump("loc_C17")

    label("loc_C0D")

    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_C17")

    Jump("loc_C7B")

    label("loc_C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_C34")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x10)
    Jump("loc_C7B")

    label("loc_C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_C47")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_C7B")

    label("loc_C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_C5F")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x10)
    Jump("loc_C7B")

    label("loc_C5F")

    SetChrFlags(0xD, 0x80)
    SetChrPos(0x9, 12540, 0, 2950, 225)
    BeginChrThread(0x9, 0, 0, 0)

    label("loc_C7B")

    Return()

    # Function_5_612 end

    def Function_6_C7C(): pass

    label("Function_6_C7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C95")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_C9B")

    label("loc_C95")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_C9B")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_CAE")
    Jump("loc_CC6")

    label("loc_CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC6")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_CC6")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEC")
    OP_66(0x0, 0x1)

    label("loc_CEC")

    Return()

    # Function_6_C7C end

    def Function_7_CED(): pass

    label("Function_7_CED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_E45")

    #C0001
    ChrTalk(
        0x8,
        (
            "#1601F祭りだからって\x01",
            "羽目外してんじゃねえぞ。\x02\x03",

            "#1607F俺の席の後ろで\x01",
            "何をしてやがった。\x01",
            "アア……？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#0003Fいや、君の迷惑になる事は\x01",
            "何もしてないよ。\x02\x03",

            "#0005F（そういやヴァルドの席の後ろだな。\x01",
            "  ……ヴァルドには気付かれずに\x01",
            "  カードを貼り付けたのか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        (
            "#0100Fというか、そちらもお祭りで\x01",
            "羽目を外しすぎないようにね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12AA")

    label("loc_E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EA7")

    #C0004
    ChrTalk(
        0x8,
        (
            "#1601Fチッ……\x01",
            "どいつもコイツも……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        "#0000F（長居は無用だな……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF1")

    label("loc_EA7")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x0, 750)
    Sleep(750)

    #C0006
    ChrTalk(
        0x8,
        (
            "#1600Fオイ……\x02\x03",

            "#1607F喧嘩売ってんのか？\x01",
            "アア？　ヨオ？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0001Fちょ、ちょっと待った！\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x104,
        (
            "#0306Fおいおい……\x01",
            "いきなり何だってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#0101F（……相当苛立っているみたいね。\x01",
            "  長居しない方がいいかも。）\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#0200F（ワジさんが計らってくれるはずです。\x01",
            "  お任せしておきましょう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x0)
    SetScenarioFlags(0x0, 0)

    label("loc_FF1")

    Jump("loc_12AA")

    label("loc_FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1007")
    Call(0, 12)
    Jump("loc_12AA")

    label("loc_1007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 2)), scpexpr(EXPR_END)), "loc_10BE")

    #C0011
    ChrTalk(
        0x8,
        (
            "#1603F黒服ども、最近は\x01",
            "コソコソ動いてやがるらしいな。\x02\x03",

            "#1604Fクク、ウチのメンバーにも\x01",
            "見回りをさせている……\x02\x03",

            "#1602Fこの旧市街に一歩でも入れば\x01",
            "フクロにしてやるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12AA")

    label("loc_10BE")


    #C0012
    ChrTalk(
        0x8,
        (
            "#1600F近頃黒服どもが妙な気配でな。\x02\x03",

            "ウチのメンバーにも\x01",
            "見回りをさせている所だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#0305F黒服……ルバーチェの連中か。\x02\x03",

            "#0303Fそういや最近は\x01",
            "活発に動いてるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#1603Fケッ、前みたく\x01",
            "デカイ顔で出てこねえ代わりに\x01",
            "コソコソ動いてやがるらしい。\x02\x03",

            "#1602F……見つけ次第サンドバッグだ。\x01",
            "クク、楽しみだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0006Fおいおい……\x01",
            "大事#4Rおおごと#にはしないでくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#0101Fでも最近は\x01",
            "大きな事件も増えているし……\x02\x03",

            "マフィア同士の抗争が\x01",
            "激しくなっているのは\x01",
            "確かみたいね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 2)

    label("loc_12AA")

    TalkEnd(0xFE)
    Return()

    # Function_7_CED end

    def Function_8_12AE(): pass

    label("Function_8_12AE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1342")
    Jump("loc_138C")

    label("loc_1342")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1362")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_138C")

    label("loc_1362")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1382")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_138C")

    label("loc_1382")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_138C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_13C2")
    Call(0, 9)
    Jump("loc_26D0")

    label("loc_13C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_141A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 4)), scpexpr(EXPR_END)), "loc_1412")

    #C0017
    ChrTalk(
        0xF,
        (
            "#1601F何だテメエら……\x01",
            "うろちょろしてんじゃねえぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1415")

    label("loc_1412")

    Call(0, 11)

    label("loc_1415")

    Jump("loc_26D0")

    label("loc_141A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1468")

    #C0018
    ChrTalk(
        0xF,
        (
            "#1601F……とっとと失せろや。\x01",
            "脳天カチ割るぞコラ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1740")

    label("loc_1468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_END)), "loc_15B8")

    #C0019
    ChrTalk(
        0x101,
        (
            "#0001Fヴァルド、仲間同士で\x01",
            "喧嘩したって聞いたけど……\x02\x03",

            "何とか収まったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xF,
        (
            "#1600Fアア？\x01",
            "……てめえらに首を突っ込まれる\x01",
            "筋合いはねえんだよ。\x02\x03",

            "#1601Fとっとと失せろや。\x01",
            "脳天カチ割るぞコラ？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#0303F（相当イラついてやがんな……）\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#0101F（この人が\x01",
            "  手下の統率に苦労するなんて\x01",
            "  珍しいこともあるものね……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173D")

    label("loc_15B8")


    #C0023
    ChrTalk(
        0x101,
        (
            "#0005F（今日はみんな\x01",
            "  様子がおかしいな……）\x02\x03",

            "#0001Fヴァルド、何かあったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xF,
        (
            "#1600Fアア？\x01",
            "……てめえらに首を突っ込まれる\x01",
            "筋合いはねえんだよ。\x02\x03",

            "#1603Fウチの舎弟どもの間で\x01",
            "ゴタゴタがあったってだけの話だ。\x02\x03",

            "#1601F……とっとと失せろや。\x01",
            "脳天カチ割るぞコラ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#0305F（仲間同士で喧嘩か……\x01",
            "  珍しい話だな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#0101F（ええ、いつもならこの人が\x01",
            "  睨みを利かせているものね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_173D")

    SetScenarioFlags(0x0, 0)

    label("loc_1740")

    Jump("loc_26D0")

    label("loc_1745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_17CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17C4")

    #C0027
    ChrTalk(
        0xF,
        (
            "#1600Fオイ……人のシマ\x01",
            "荒らしてんじゃねえぞ。\x02\x03",

            "テメエらには関係のねえハナシだ。\x01",
            "とっとと失せろや。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C7")

    label("loc_17C4")

    Call(0, 13)

    label("loc_17C7")

    Jump("loc_26D0")

    label("loc_17CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_185B")

    #C0028
    ChrTalk(
        0xF,
        (
            "#1600Fチッ……\x02\x03",

            "ここを誰のシマだと思ってやがる。\x01",
            "気楽に顔出してんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#0001F（今日はやけに殺気立ってるな……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_26D0")

    label("loc_185B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_19FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_END)), "loc_19F7")
    SetChrSubChip(0xF, 0x0)
    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x153, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1905")
    Jump("loc_194F")

    label("loc_1905")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1925")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_194F")

    label("loc_1925")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1945")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_194F")

    label("loc_1945")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_194F")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0030
    ChrTalk(
        0xF,
        (
            "#1604Fクク、なかなか度胸の\x01",
            "据わったガキみてぇだな。\x02\x03",

            "#1602F気に入ったぜ、チビ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x153,
        (
            "#1110Fチビじゃなくて\x01",
            "キーアだよー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FA")

    label("loc_19F7")

    Call(0, 10)

    label("loc_19FA")

    Jump("loc_26D0")

    label("loc_19FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A0D")
    Jump("loc_26D0")

    label("loc_1A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A1E")
    Call(0, 14)
    Jump("loc_26D0")

    label("loc_1A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1C45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AB4")

    #C0032
    ChrTalk(
        0xF,
        (
            "#1600F近頃、警察だの役人だのが\x01",
            "ウロチョロしてやがる。\x02\x03",

            "度胸もねえクソどもが……\x01",
            "旧市街で舐めた真似\x01",
            "してんじゃねえぞコラ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C40")

    label("loc_1AB4")


    #C0033
    ChrTalk(
        0xF,
        (
            "#1603F……チッ、テメエらか。\x02\x03",

            "#1600Fオイ、人の縄張りに\x01",
            "勝手に顔出してんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#0001F今日は機嫌が悪いな……\x01",
            "何かあったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xF,
        (
            "#1603Fどうもこうもねえ。\x01",
            "近頃、記念祭の準備とかいって\x01",
            "サツや役人がウロウロしてやがる。\x02\x03",

            "#1601Fクソどもが……\x01",
            "まとめてシバくぞコラ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#0306F俺たちも支援要請が\x01",
            "増えてるくらいだからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        (
            "#0100Fそこは我慢してもらうしか\x01",
            "ないんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C40")

    Jump("loc_26D0")

    label("loc_1C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1F11")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D72")

    #C0038
    ChrTalk(
        0xF,
        (
            "#1601F……何見てやがる。\x02\x03",

            "#1607Fいい気になってんじゃねえぞ。\x01",
            "アア？　やんのかァ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0001Fいや、そういうつもりじゃ……\x01",
            "（助けられたのが\x01",
            "  よっぽど気に障ったのかな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x103,
        (
            "#0200F（後から段々腹が立って\x01",
            "  きたのではないでしょうか。\x01",
            "  ……長居しない方がいいかと。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_1D72")

    SetChrSubChip(0xF, 0x0)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E2A")

    #C0041
    ChrTalk(
        0xF,
        "#1600Fよし、なら何か買ってこいや。\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0042
    ChrTalk(
        0xD,
        "さ、早速パシリっすか！？\x02",
    )

    CloseMessageWindow()
    OP_64(0xD)

    #C0043
    ChrTalk(
        0xD,
        (
            "わ、分かりやしたっ！\x01",
            "パシリのコウキ、\x01",
            "ひとっ走り行ってきやす！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F08")

    label("loc_1E2A")


    #C0044
    ChrTalk(
        0xF,
        (
            "#1600Fオウ、コウキ。\x01",
            "具合はどうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xD,
        (
            "もうゼンゼン平気です！\x01",
            "ご心配をおかけしやした！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xF,
        (
            "#1600F明日は通院するとか\x01",
            "言ってやがったな。\x02\x03",

            "完治するまで\x01",
            "無茶すんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xD,
        (
            "は、はい！\x01",
            "ありがとうございやすッ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F08")

    OP_4C(0xD, 0xFF)

    label("loc_1F0C")

    Jump("loc_26D0")

    label("loc_1F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2020")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F8C")

    #C0048
    ChrTalk(
        0xF,
        (
            "#1600Fコウキの奴は\x01",
            "もうしばらく病院通いだ。\x02\x03",

            "#1601Fマフィアどもが……\x01",
            "いい気になりやがって……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_201B")

    label("loc_1F8C")


    #C0049
    ChrTalk(
        0xF,
        (
            "#1600F退院はしたが、コウキの奴は\x01",
            "もうしばらく病院通いだ。\x02\x03",

            "#1601F…………クソが………\x02\x03",

            "《ルバーチェ》ども……\x01",
            "いい気になりやがって……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_201B")

    Jump("loc_26D0")

    label("loc_2020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_22FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20BA")

    #C0050
    ChrTalk(
        0xF,
        (
            "#1600F俺はまだケジメを\x01",
            "付けたとは思っちゃいねえ。\x02\x03",

            "#1601Fまた連中が何かしやがったら\x01",
            "絶対に潰す……\x01",
            "テメエらも良く覚えとけや。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F7")

    label("loc_20BA")


    #C0051
    ChrTalk(
        0xF,
        "#1600Fなんだ……てめえらか。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#0000Fどうやら今日は\x01",
            "機嫌も悪くないみたいだな。\x02\x03",

            "……ヴァルド、この前は\x01",
            "協力してくれてありがとう。\x01",
            "お陰で助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#0300F入院してた仲間も\x01",
            "戻ってきたんだろ？\x01",
            "ま、良かったじゃねか。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xF,
        (
            "#1603Fフン……\x01",
            "まだルバーチェの連中には\x01",
            "ケジメを付けたわけじゃねえ。\x02\x03",

            "てめえらとワジの手前、\x01",
            "あの時は納得してやったんだよ。\x02\x03",

            "#1600Fいいか、あの薄汚ぇマフィアどもが\x01",
            "次に俺のシマに顔出しやがったら……\x02\x03",

            "#1601Fマジで血ダルマにしてやるからな。\x01",
            "テメエらも弁#2Rわきま#えとけや。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#0200F……やれやれです。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        "#0106F穏やかじゃないわねえ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_22F7")

    Jump("loc_26D0")

    label("loc_22FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2442")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_238A")

    #C0057
    ChrTalk(
        0xF,
        (
            "#1600Fテスタメンツの\x01",
            "坊主どもには俺が直々に\x01",
            "落とし前を付けさせてやる。\x02\x03",

            "#1601Fテメエら、\x01",
            "邪魔しやがったら潰すぞ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243D")

    label("loc_238A")


    #C0058
    ChrTalk(
        0xF,
        (
            "#1600Fチッ、まだこの辺りを\x01",
            "うろついてやがったのか。\x02\x03",

            "#1603F……テスタメンツの\x01",
            "坊主どもには俺が直々に\x01",
            "落とし前を付けさせてやる。\x02\x03",

            "#1601Fテメエら、\x01",
            "邪魔しやがったら潰すぞ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_243D")

    Jump("loc_26D0")

    label("loc_2442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_24D9")

    #C0059
    ChrTalk(
        0xF,
        (
            "#1600Fてめえらの捜査とやらが\x01",
            "どう転ぼうと知ったことじゃねえ。\x02\x03",

            "#1602Fクク、近いうちに\x01",
            "この辺りは血の雨が降るぜ。\x01",
            "……覚悟してろや。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D0")

    label("loc_24D9")


    #C0060
    ChrTalk(
        0xF,
        (
            "#1600F俺はな、とにかく\x01",
            "暴れられりゃあいいんだよ。\x02\x03",

            "てめえらの捜査とやらが\x01",
            "どう転ぼうと知ったことじゃねえ。\x02\x03",

            "#1602Fクク、近いうちに\x01",
            "この辺りは血の雨が降るぜ。\x01",
            "……覚悟してろや。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CD")

    #C0061
    ChrTalk(
        0xF,
        (
            "#1603F……それと…………\x02\x03",

            "#1601Fおいそこの女ども、\x01",
            "いつまで旧市街#6Rこ  こ#に\x01",
            "居残ってるつもりだ。\x02\x03",

            "#1602F旧市街が気に入りましたってか？\x01",
            "ゴロツキに取って食われる\x01",
            "覚悟はあんだろうなァ？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        "#0203F（……無駄に威圧的ですね。）\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        (
            "#0100F（どうやら忠告してくれている\x01",
            "  みたいだけど……乱暴な人ねぇ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 4)

    label("loc_26CD")

    SetScenarioFlags(0x0, 0)

    label("loc_26D0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_12AE end

    def Function_9_26D8(): pass

    label("Function_9_26D8")

    OP_4B(0xF, 0xFF)
    OP_4B(0xD, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0064
    ChrTalk(
        0xD,
        "す、すみませんヴァルドさん！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xD,
        (
            "ディ、ディーノのやつ、\x01",
            "どこ探してもいなくて……っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xF,
        (
            "#1601Fチッ……\x02\x03",

            "#1603F……何してやがんだ、\x01",
            "あの馬鹿野郎が…………\x02\x03",

            "#1601Fマジで妙なモンでも\x01",
            "キメたんじゃねえだろうな……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285B")

    #C0067
    ChrTalk(
        0x10A,
        (
            "#0600F（ヴァルド・ヴァレス……\x01",
            "  久々に見たが変わったな。）\x02\x03",

            "#0603F（前よりも手下の面倒見が\x01",
            "  良くなったようだが……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_285B")

    OP_64(0xD)
    OP_4C(0xF, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_26D8 end

    def Function_10_2867(): pass

    label("Function_10_2867")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(17000, 2000, -290, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 15520, 990, -630, 90)
    SetChrPos(0xEF, 15520, 990, 320, 90)
    SetChrPos(0x153, 16170, 1000, -1660, 45)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(750)

    #C0068
    ChrTalk(
        0xF,
        (
            "#1600Fおう、サツの連中じゃねえか。\x02\x03",

            "#1602Fクク……タイマンでも\x01",
            "張りに来たのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#0006Fなんでそう好戦的なんだ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29B5")

    #C0070
    ChrTalk(
        0x102,
        (
            "#0100F今日は宴会みたいね。\x01",
            "記念祭から日もたってないのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4E")

    label("loc_29B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A01")

    #C0071
    ChrTalk(
        0x103,
        (
            "#0200F今日は皆さん飲んでますね。\x01",
            "……宴会ですか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4E")

    label("loc_2A01")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A4E")

    #C0072
    ChrTalk(
        0x104,
        (
            "#0306Fつうか今日は宴会か？\x01",
            "記念祭の後なのによくやるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A4E")

    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x153)

    #C0073
    ChrTalk(
        0x153,
        (
            "#1111Fじー……\x02\x03",

            "#1110Fねえロイドー、このヒトも\x01",
            "ロイドのシリアイ？\x02\x03",

            "#1109Fなんかニワトリみたいな\x01",
            "カミしてるねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#0011Fちょ、キーア……！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x153, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B92")
    Jump("loc_2BDC")

    label("loc_2B92")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BB2")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BDC")

    label("loc_2BB2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BD2")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BDC")

    label("loc_2BD2")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BDC")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0075
    ChrTalk(
        0xF,
        (
            "#1609Fクカカ、面白ぇ。\x02\x03",

            "#1602Fおいガキ、この髪型は\x01",
            "ニワトリなんかじゃねぇ……\x02\x03",

            "#1607F泣く子も黙る不死鳥！\x01",
            "フェニックスの髪型ってヤツだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x153,
        "#1110Fおー。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#0006F（剣のマムシ#10Rサーベルバイパー#のくせに\x01",
            "  不死鳥ってのもどうかと思うけど……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 5)
    EventEnd(0x5)
    Return()

    # Function_10_2867 end

    def Function_11_2D03(): pass

    label("Function_11_2D03")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0xF, 0xFF)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x101, 11500, 0, -750, 90)
    SetChrPos(0x102, 11500, 0, 750, 90)
    SetChrPos(0x103, 10000, 0, -750, 90)
    SetChrPos(0x104, 10000, 0, 750, 90)
    FadeToBright(1000, 0)
    OP_68(16940, 2500, -170, 3000)
    MoveCamera(45, 30, 0, 3000)
    SetCameraDistance(14000, 3000)
    OP_0D()
    OP_6F(0x79)

    #C0078
    ChrTalk(
        0xF,
        (
            "#1603Fオイ……居なかったってのは\x01",
            "どういうことだ？\x02\x03",

            "#1601F俺は連れて来いと言ったんだ。\x01",
            "聞こえなかったのか、アア？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xD,
        (
            "そ、そのう……\x01",
            "ディーノの奴、家にも\x01",
            "帰ってないらしくて……\x02",
        )
    )

    CloseMessageWindow()
    Fade(200)
    SetChrChipByIndex(0xF, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, 17200, 1000, -180, 270)
    Sound(819, 0, 100, 0)
    Sleep(500)
    OP_82(0xC8, 0x0, 0x1388, 0x1F4)

    #C0080
    ChrTalk(
        0xF,
        "#1607F#4S#11Pならとっとと探して来いやァ！！\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_98(0xD, 0xFFFFFF38, 0x0, 0x0, 0x1F4, 0x0)

    #C0081
    ChrTalk(
        0xD,
        "オ、オッス……！！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0xF, 0x1)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, 17600, 1100, -180, 270)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_64(0xD)
    Fade(500)
    OP_68(10750, 1250, 0, 0)
    MoveCamera(46, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14000, 0)
    OP_0D()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0008F#6P（ディーノって……まさか\x01",
            "  一課のリストにあったパシリの？）\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0301F#6P（よく分からんが……\x01",
            "  行方不明ってことか……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 11500, 0, 0, 90)
    SetChrPos(0xD, 16360, 990, -40, 90)
    OP_4C(0xF, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetScenarioFlags(0xCD, 4)
    EventEnd(0x5)
    Return()

    # Function_11_2D03 end

    def Function_12_301B(): pass

    label("Function_12_301B")

    SetChrSubChip(0xF, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0084
    ChrTalk(
        0x8,
        (
            "#1602Fクク、最後はパーっと\x01",
            "打ち上げするとして……\x02\x03",

            "ジェド、いい場所は\x01",
            "見つかったかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "オス、今ヒューイの奴に\x01",
            "様子を見に行かせてます。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xA,
        (
            "百貨店の屋上辺りが\x01",
            "よさそうかと思いますが……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_12_301B end

    def Function_13_30FC(): pass

    label("Function_13_30FC")

    OP_4B(0xF, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrSubChip(0xF, 0x0)

    #C0087
    ChrTalk(
        0xF,
        "#1600Fジェド、お前病院行ってこい。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        "いえ平気です。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xA,
        (
            "この程度で医者掛かってたんじゃ\x01",
            "バイパーの名前にも傷が……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xF,
        (
            "#1601F何度も言わせんじゃねえ。\x01",
            "俺にぶっ飛ばされてえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        "……すんません、そうします。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xF, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_13_30FC end

    def Function_14_31F5(): pass

    label("Function_14_31F5")

    SetChrSubChip(0xF, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0092
    ChrTalk(
        0xF,
        (
            "#1604Fハッ、昨日は結構\x01",
            "盛り上がったからなァ……\x02\x03",

            "#1602F今日はちょっくら別の場所に\x01",
            "繰り出すとするかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        "オス、ご一緒します。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "ひゃひゃひゃ～っ！\x01",
            "今日も全開だぜ～っ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3324")

    #C0095
    ChrTalk(
        0x102,
        "#0106F（ちょっと心配ねぇ……）\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#0003F（うーん、面倒を\x01",
            "  起こさないといいんだが……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3324")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_14_31F5 end

    def Function_15_3331(): pass

    label("Function_15_3331")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_33B4")

    #C0097
    ChrTalk(
        0x9,
        (
            "ヴァルドさんがよぉ？\x01",
            "ちょっと黙ってろって言うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "つまんねえよォ……\x01",
            "歌わせてくれよォ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4A")

    label("loc_33B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_343F")

    #C0099
    ChrTalk(
        0x9,
        (
            "#4Sヴオ゛オ゛ォォォ……\x01",
            "……オレにも喧嘩させろォ～～～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "ぶっ殺すゥ、ぶっ殺すゥ！！\x01",
            "ヤァ、見てやがれェ～～ッ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4A")

    label("loc_343F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_34FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3497")

    #C0101
    ChrTalk(
        0x9,
        (
            "勝負がタイマンだったんなら\x01",
            "ヴァルドさんも口は挟めねえな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F8")

    label("loc_3497")


    #C0102
    ChrTalk(
        0x9,
        (
            "勝負がタイマン\x01",
            "だったんなら仕方ねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "元々バイパーじゃ\x01",
            "弱肉強食が基本だかンな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_34F8")

    Jump("loc_3E4A")

    label("loc_34FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3599")

    #C0104
    ChrTalk(
        0x9,
        "#4Sイェ、イェ～～～ッ！！\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "アリエネエ、アリエネエ～ッ！！\x01",
            "ジェドが負ける、アリエネ～～～ッ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        "でも勝負は勝負ゥ、ヒャッホゥ！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E4A")

    label("loc_3599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_35F2")

    #C0107
    ChrTalk(
        0x9,
        "なンだなンだ～、空気悪ィな～。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "歌う気まで\x01",
            "失せンじゃねえかよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4A")

    label("loc_35F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3807")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_36E9")

    #C0109
    ChrTalk(
        0x9,
        "ン～、こんなんどうだ？\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "祭りィ、祭りィ～……！\x01",
            "わた菓子ィィ、食べさせろォ！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0111
    ChrTalk(
        0x101,
        "#0006F（……これ、歌なのかな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3802")

    label("loc_36E9")


    #C0112
    ChrTalk(
        0x9,
        (
            "#4Sオゥ、イェ～～ッッ！\x01",
            "まだ歌い足りねえぜ～ッ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        "祭りも今日で最後だもんな～。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "ここいらで祭り用の新曲、\x01",
            "考えてみっかな～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0115
    ChrTalk(
        0x103,
        "#0200F考え付くのが遅いのでは……？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3802")

    Jump("loc_3E4A")

    label("loc_3807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3818")
    Call(0, 14)
    Jump("loc_3E4A")

    label("loc_3818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3898")

    #C0116
    ChrTalk(
        0x9,
        "#4S……ヒュー、ヤァヤ～～ッ！！\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "連中ゥ～、ここでェ～、ボコボコォ！\x01",
            "ヒュー、オレ様にィィ……任せろォ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4A")

    label("loc_3898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3977")

    #C0118
    ChrTalk(
        0x9,
        (
            "なンだよ～。\x01",
            "オレの邪魔すんなよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "今日のマイクの\x01",
            "テスト中なんだからよ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0120
    ChrTalk(
        0x9,
        (
            "イェイェイェ～イェ\x01",
            "イェイェイェイェイェッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "#4S……オゥ、イェ～～ッ！！\x01",
            "今日も絶好調だぜェ～～ッ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4A")

    label("loc_3977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3A76")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_39EF")

    #C0122
    ChrTalk(
        0x9,
        (
            "オウ、ヤァヤァ～！！\x01",
            "……なンかあったのか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "ヴァルドさん、\x01",
            "ちょっと不機嫌だぞ～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A71")

    label("loc_39EF")

    OP_4B(0xA, 0xFF)

    #C0124
    ChrTalk(
        0x9,
        (
            "なンだよジェド～。\x01",
            "幹部会議なら後にしろよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            "オウ、ヤァヤァ、オ～ウ～ッ！！\x01",
            "……いま新曲考えてンだからよ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_3A71")

    Jump("loc_3E4A")

    label("loc_3A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3AF0")

    #C0126
    ChrTalk(
        0x9,
        "#4S……イェ～、ヤァヤ～～ッ！！\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "オレ様ァ～、オレ様アァ～ッッ！！\x01",
            "ヒューッ、腹ァッ減ったァァ～ッ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4A")

    label("loc_3AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3CA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3B72")

    #C0128
    ChrTalk(
        0x9,
        (
            "ドンジャン××××ンジャカン\x01",
            "ガンド××ン××ドン……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0129
    ChrTalk(
        0x9,
        "#4S……イェ～ッッッ！！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C9D")

    label("loc_3B72")


    #C0130
    ChrTalk(
        0x9,
        (
            "ドンジャン××××ンジャカン\x01",
            "ガンド××ン××ドン……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0131
    ChrTalk(
        0x9,
        "#4S……イェ～ッッッ！！！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#0003F（うーむ、大声過ぎて……\x01",
            "  何を歌ってるのか判らないな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        (
            "#0200F（仲間が退院した歓迎会……\x01",
            "  と言っている気がします。）\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        (
            "#0100F（ティオちゃん、\x01",
            "  よく分かるわねぇ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3C9D")

    Jump("loc_3E4A")

    label("loc_3CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3D1A")

    #C0135
    ChrTalk(
        0x9,
        "#4S……イェ～、イェ～ッ！！\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "１００倍返し、１００倍返しィ～……\x01",
            "御ン礼参りィ～ヒャホ～ウッッ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4A")

    label("loc_3D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3D9A")

    #C0137
    ChrTalk(
        0x9,
        (
            "卑怯な真似しやがった\x01",
            "テスタメンツの連中は潰す。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "テメエらもチョット話通したからって\x01",
            "いい気になンなよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4A")

    label("loc_3D9A")


    #C0139
    ChrTalk(
        0x9,
        (
            "この旧市街で\x01",
            "俺らに逆らう馬鹿なんざ\x01",
            "テスタメンツしかいねえンだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        "ま、それもすぐに潰す。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        (
            "テメエらもいい気になンなよ～。\x01",
            "次はフクロにしちまうかもしンねえぞ～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3E4A")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFE)
    Return()

    # Function_15_3331 end

    def Function_16_3E59(): pass

    label("Function_16_3E59")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EED")
    Jump("loc_3F37")

    label("loc_3EED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F0D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F37")

    label("loc_3F0D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F2D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F37")

    label("loc_3F2D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F37")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0142
    ChrTalk(
        0x10,
        "ん～……んめェ～！\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x10,
        "やっぱ酒はスコッチだよな～。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_3E59 end

    def Function_17_3F9E(): pass

    label("Function_17_3F9E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_400B")

    #C0144
    ChrTalk(
        0xFE,
        (
            "サツが俺たちの縄張りに\x01",
            "入ってくるんじゃねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "ヴァルドさんに\x01",
            "ぶっ殺されたいのか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF0")

    label("loc_400B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_409B")

    #C0146
    ChrTalk(
        0xA,
        (
            "ディーノの奴は許さん。\x01",
            "見つけ次第フルボッコだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0147
    ChrTalk(
        0xA,
        (
            "#4S……サツがうろちょろ\x01",
            "してんじゃねえぞコラァ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF0")

    label("loc_409B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_40DF")

    #C0148
    ChrTalk(
        0xA,
        "俺が留守の間に……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xA,
        "…………クソが……ッ！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BF0")

    label("loc_40DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4133")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_412B")

    #C0150
    ChrTalk(
        0xA,
        (
            "……サツの犬っころが\x01",
            "うろついてんじゃねえぞ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_412E")

    label("loc_412B")

    Call(0, 13)

    label("loc_412E")

    Jump("loc_4BF0")

    label("loc_4133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_41B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_41AC")
    OP_4B(0xE, 0xFF)

    #C0151
    ChrTalk(
        0xA,
        (
            "チッ……そいつは\x01",
            "ヴァルドさんが決める事だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        "#4S出しゃばってんじゃねえぞコラァ！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    Jump("loc_41AF")

    label("loc_41AC")

    Call(0, 18)

    label("loc_41AF")

    Jump("loc_4BF0")

    label("loc_41B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4223")
    OP_4B(0x9, 0xFF)

    #C0153
    ChrTalk(
        0xA,
        (
            "テスタメンツの連中が\x01",
            "はびこってもう２年だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        "そろそろケリを付けるべきだろうが。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_4BF0")

    label("loc_4223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4234")
    Call(0, 12)
    Jump("loc_4BF0")

    label("loc_4234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4245")
    Call(0, 14)
    Jump("loc_4BF0")

    label("loc_4245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_42AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 7)), scpexpr(EXPR_END)), "loc_42A7")

    #C0155
    ChrTalk(
        0xA,
        "青坊主どもが……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xA,
        (
            "いずれヴァルドさんに言って\x01",
            "ケジメ付けてやるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42AA")

    label("loc_42A7")

    Call(0, 19)

    label("loc_42AA")

    Jump("loc_4BF0")

    label("loc_42AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_44AC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4388")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 7)), scpexpr(EXPR_END)), "loc_4372")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4310")

    #C0157
    ChrTalk(
        0xA,
        (
            "邪魔してんじゃねえ。\x01",
            "ここから先は俺らの稽古だ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436D")

    label("loc_4310")

    OP_4B(0xB, 0xFF)

    #C0158
    ChrTalk(
        0xA,
        "#4Sもう一丁いくぞコラァ！\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0159
    ChrTalk(
        0xB,
        "オ、オッス……！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_64(0xB)
    OP_4C(0xB, 0xFF)

    label("loc_436D")

    Jump("loc_4383")

    label("loc_4372")

    TurnDirection(0xA, 0x0, 0)
    Call(0, 19)
    OP_93(0xA, 0x10E, 0x0)

    label("loc_4383")

    Jump("loc_44A7")

    label("loc_4388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_442E")

    #C0160
    ChrTalk(
        0xA,
        (
            "今日は大事な日でな。\x01",
            "ヴァルドさんにお願いして\x01",
            "朝稽古だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        (
            "終わったとたんにヘタりやがって。\x01",
            "スラッシュとヒューイは\x01",
            "最近気が抜けてきてやがるな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44A7")

    label("loc_442E")

    OP_4B(0xB, 0xFF)

    #C0162
    ChrTalk(
        0xA,
        "ヒューイ、気合入れろやコラ。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "お前この前の抗争#4Rケンカ#でも\x01",
            "青坊主どもに遅れを取ってたろうが。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xB, 0xFF)

    label("loc_44A7")

    Jump("loc_4BF0")

    label("loc_44AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_458E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4508")

    #C0164
    ChrTalk(
        0xA,
        (
            "人の縄張り近くを\x01",
            "ウロチョロしやがって……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        "気に入らねえぜ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4589")

    label("loc_4508")


    #C0166
    ChrTalk(
        0xA,
        (
            "最近この近くでも\x01",
            "例の黒バンを見かける事がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        "クソが……\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "旧市街に手を出す気は\x01",
            "ないようだが、気に入らねえぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4589")

    Jump("loc_4BF0")

    label("loc_458E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_46B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_45F4")

    #C0169
    ChrTalk(
        0xA,
        "俺は孤児だったんでな。\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xA,
        (
            "役人だの警察だのは\x01",
            "聞いただけで反吐が出るぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46B4")

    label("loc_45F4")


    #C0171
    ChrTalk(
        0xA,
        (
            "役人も警察も、結局は\x01",
            "何もするつもりはねえんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "旧市街のために\x01",
            "手間を割くことなんざねえのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "なのにてめえらの都合の\x01",
            "いい時だけしゃしゃり出やがって……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        "ハッ、胸糞悪ぃ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_46B4")

    Jump("loc_4BF0")

    label("loc_46B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_48C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_47A8")

    #C0175
    ChrTalk(
        0xA,
        (
            "テメエら、ヴァルドさんに\x01",
            "何をしやがった……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xA,
        (
            "事と次第によっては\x01",
            "この場で締めるぞコラ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47A3")

    #C0177
    ChrTalk(
        0x104,
        (
            "#0306Fいや、全然\x01",
            "大したことじゃねえんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        (
            "#0103F（相変わらず\x01",
            "  血の気の多いメンバーねぇ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_47A3")

    Jump("loc_48BB")

    label("loc_47A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_483F")

    #C0179
    ChrTalk(
        0xA,
        (
            "オイ、サツども。\x01",
            "イグニスの近くで\x01",
            "何かやってやがるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "どたばた煩えぞ。\x01",
            "幹部会議の邪魔すんじゃねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48BB")

    label("loc_483F")

    OP_4B(0x9, 0xFF)

    #C0181
    ChrTalk(
        0xA,
        (
            "スラッシュとヒューイのやつ、\x01",
            "最近気が抜けてやがる。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        (
            "俺ら幹部が根性入れ直して\x01",
            "やんねえといけねえだろうが。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)

    label("loc_48BB")

    Jump("loc_4BF0")

    label("loc_48C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4A00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4938")

    #C0183
    ChrTalk(
        0xA,
        (
            "旧市街は俺たちの縄張りだ。\x01",
            "誰にもデカイ顔をさせるかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xA,
        "勿論テスタメンツの連中にもな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_49FB")

    label("loc_4938")


    #C0185
    ChrTalk(
        0xA,
        (
            "時々この旧市街にも\x01",
            "役人どもがやってきやがる。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        "再開発の調査とか抜かしながらな。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        (
            "はっ、寝ぼけた連中だぜ。\x01",
            "勿論俺が脅して追い返したがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        "……役人どもは帰ってクソして寝ろや。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_49FB")

    Jump("loc_4BF0")

    label("loc_4A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4B0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4A44")

    #C0189
    ChrTalk(
        0xA,
        (
            "まさか真犯人が\x01",
            "マフィアだったとはな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B05")

    label("loc_4A44")


    #C0190
    ChrTalk(
        0xA,
        (
            "チッ、まさか真犯人が\x01",
            "マフィアだったとはな……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xA,
        "俺とした事がしくったぜ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0192
    ChrTalk(
        0xA,
        (
            "フン、別にてめえらに\x01",
            "礼は言わねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "その、サツは\x01",
            "それが仕事なんだろうがよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4B05")

    Jump("loc_4BF0")

    label("loc_4B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4B98")

    #C0194
    ChrTalk(
        0xA,
        (
            "性根の腐った青坊主どもが……\x01",
            "今のうちに首でも洗ってろや。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xA,
        (
            "ウチの若いモンに手を出した代償は\x01",
            "たっぷり支払ってもらうぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF0")

    label("loc_4B98")


    #C0196
    ChrTalk(
        0xA,
        (
            "……サツの犬に\x01",
            "話す事なんざねえんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xA,
        (
            "さっさと失せな、\x01",
            "能無しのチワワども。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF0")

    TalkEnd(0xFE)
    Return()

    # Function_17_3F9E end

    def Function_18_4BF4(): pass

    label("Function_18_4BF4")

    OP_4B(0xA, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0198
    ChrTalk(
        0xA,
        (
            "……おいディーノ、\x01",
            "調子こいてんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xA,
        "お前にはまだ早いんだよ。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xE,
        (
            "見張りは飽きたって\x01",
            "言ってるだけじゃないスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xE,
        (
            "ジェドさん、そろそろ俺にも\x01",
            "稽古つけてくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#0005F（？  ……何だか険悪なムードだ。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_18_4BF4 end

    def Function_19_4CEF(): pass

    label("Function_19_4CEF")


    #C0203
    ChrTalk(
        0xA,
        "……今後は朝稽古を強化する。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xA,
        (
            "二度と舐めた真似\x01",
            "されねえようにな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 7)
    Return()

    # Function_19_4CEF end

    def Function_20_4D3E(): pass

    label("Function_20_4D3E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4D7A")

    #C0205
    ChrTalk(
        0xB,
        (
            "あの野郎……\x01",
            "一体どこ行きやがった……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C18")

    label("loc_4D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4E7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4DE8")

    #C0206
    ChrTalk(
        0xB,
        "ディーノは今日は来てねえぜ。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xB,
        (
            "ハッ、当然だ。\x01",
            "どのツラ下げて来る気だコラァ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E78")

    label("loc_4DE8")


    #C0208
    ChrTalk(
        0xB,
        (
            "ディーノのヤツは\x01",
            "ケタケタ笑いながら\x01",
            "出て行きやがった……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xB,
        "今日は来てねえぜ。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xB,
        (
            "ハッ、当然だぜ……\x01",
            "次見つけたらフルボッコだァ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4E78")

    Jump("loc_5C18")

    label("loc_4E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4F06")

    #C0211
    ChrTalk(
        0xB,
        (
            "……ジェドさんの\x01",
            "場所をヌケヌケと……\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xB,
        (
            "クソがァ……\x01",
            "ヴァルドさんさえ止めなきゃ\x01",
            "俺がブチのめしてやんのによォ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C18")

    label("loc_4F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4F9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_4F97")

    #C0213
    ChrTalk(
        0xB,
        (
            "ジェドさんはバイパーの幹部だ。\x01",
            "ヴァルドさんの次に強いってのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xB,
        (
            "ディーノの野郎……\x01",
            "舐めた真似しやがって……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F9A")

    label("loc_4F97")

    Call(0, 21)

    label("loc_4F9A")

    Jump("loc_5C18")

    label("loc_4F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4FFC")

    #C0215
    ChrTalk(
        0xB,
        "アア？　なんだテメエら。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xB,
        "とっとと失せろや、しばくぞコラァ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_504E")

    label("loc_4FFC")


    #C0217
    ChrTalk(
        0xB,
        "ハッ、ディーノの野郎、また……\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        "最近でけえ態度しやがってよ……！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 3)

    label("loc_504E")

    Jump("loc_5C18")

    label("loc_5053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5165")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_50AE")

    #C0219
    ChrTalk(
        0xB,
        "昨日のバトルは納得いかねえぜ。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xB,
        "もう一度やらせろってんだ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5160")

    label("loc_50AE")


    #C0221
    ChrTalk(
        0xB,
        (
            "クソが……ヴァルドさんが\x01",
            "負けるなんて納得いかねえぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xB,
        (
            "あれは絶対、ワジなんかと\x01",
            "組んでたせいに違いねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xB,
        (
            "ヴァルドさんの実力なら\x01",
            "ぶっちぎり一着、間違いなしだぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5160")

    Jump("loc_5C18")

    label("loc_5165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5176")
    Call(0, 22)
    Jump("loc_5C18")

    label("loc_5176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_52A4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 0)), scpexpr(EXPR_END)), "loc_5220")

    #C0224
    ChrTalk(
        0xB,
        (
            "最近テスタメンツの連中と\x01",
            "よく鉢合わせするんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xB,
        (
            "チッ……戦争してやりてえが\x01",
            "あの大男とカチ合うと\x01",
            "どうも気が抜けちまうぜェ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5223")

    label("loc_5220")

    Call(0, 23)

    label("loc_5223")

    Jump("loc_529F")

    label("loc_5228")


    #C0226
    ChrTalk(
        0xB,
        (
            "こちとらヴァルドさんの\x01",
            "朝稽古で鍛えられてんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xB,
        (
            "ハッ、青坊主との\x01",
            "決戦なら臨むところだァ！\x01",
            "いつでも来いやァ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_529F")

    Jump("loc_5C18")

    label("loc_52A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_534A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_530F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 0)), scpexpr(EXPR_END)), "loc_5307")

    #C0228
    ChrTalk(
        0xB,
        (
            "ハッ、いずれお前らも\x01",
            "ぶっ潰してやる。\x01",
            "覚悟しとけやァ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_530A")

    label("loc_5307")

    Call(0, 23)

    label("loc_530A")

    Jump("loc_5345")

    label("loc_530F")

    OP_4B(0xA, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0229
    ChrTalk(
        0xB,
        "オ、オッス……！\x02",
    )

    CloseMessageWindow()
    OP_64(0xB)
    OP_4C(0xA, 0xFF)

    label("loc_5345")

    Jump("loc_5C18")

    label("loc_534A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5472")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_53BB")

    #C0230
    ChrTalk(
        0xB,
        (
            "チッ、最近サツが\x01",
            "多くてイライラすんぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xB,
        (
            "おうおう、舐めてっと\x01",
            "シバくぞコラァ！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_546D")

    label("loc_53BB")


    #C0232
    ChrTalk(
        0xB,
        (
            "昨日も東通りを歩いてたら\x01",
            "警官が絡んできやがったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xB,
        (
            "おうおう、人の顔みるなり\x01",
            "いちゃもん付けてきやがって……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xB,
        (
            "舐めてんじゃねえぞ？\x01",
            "サツだろうがシバくぞコラァ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_546D")

    Jump("loc_5C18")

    label("loc_5472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_55AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_54EA")

    #C0235
    ChrTalk(
        0xB,
        (
            "ロータスハイツの空き部屋に\x01",
            "女が一人で越してきやがったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xB,
        "クカカ……マヌケな女だぜ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_55A7")

    label("loc_54EA")


    #C0237
    ChrTalk(
        0xB,
        (
            "知ってるか？\x01",
            "ロータスハイツの空き部屋に\x01",
            "女が一人で越してきたらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xB,
        (
            "ハハ、信じられっかよ？\x01",
            "この旧市街で女一人だぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xB,
        (
            "クカカ……俺も見たが\x01",
            "結構なマヌケ面してやがったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_55A7")

    Jump("loc_5C18")

    label("loc_55AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_570C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5635")

    #C0240
    ChrTalk(
        0xB,
        (
            "コウキのヤローが帰ってきたら\x01",
            "こっちのもんだろうがよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xB,
        (
            "ハッ、見てろや青坊主ども！\x01",
            "次こそは潰してやらァ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5707")

    label("loc_5635")


    #C0242
    ChrTalk(
        0xB,
        (
            "っしゃあ！\x01",
            "コウキが帰ってきやがった！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xB,
        (
            "おうおうおう、ようやく\x01",
            "フルメンバーじゃねえかよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xB,
        (
            "これでテスタメンツの連中とも\x01",
            "存分に戦えらァ！\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        "#0005Fおいおい……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x103,
        "#0203F学習能力ゼロですね……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5707")

    Jump("loc_5C18")

    label("loc_570C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5B9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 6)), scpexpr(EXPR_END)), "loc_5789")

    #C0247
    ChrTalk(
        0xB,
        (
            "青坊主どもが\x01",
            "クソみてえな真似しやがって……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xB,
        (
            "こんな事ならあの場で\x01",
            "ボコしとくんだったぜ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B99")

    label("loc_5789")


    #C0249
    ChrTalk(
        0xB,
        (
            "クソが……やっぱあん時に\x01",
            "やってりゃよかったぜ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xB,
        (
            "コウキを救急車まで運んだとき\x01",
            "あの青坊主どもとばったり出会ってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xB,
        (
            "連中も、意識がねえとかいって\x01",
            "仲間を救急車に運び込んでやがったんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 5)), scpexpr(EXPR_END)), "loc_58F3")

    #C0252
    ChrTalk(
        0x101,
        (
            "#0005Fああ、そうか。\x01",
            "テスタメンツの子と\x01",
            "同じ救急車になったんだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A1A")

    label("loc_58F3")


    #C0253
    ChrTalk(
        0x101,
        "#0005Fえ……そうだったのか？\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x104,
        (
            "#0300Fなんともまあ、\x01",
            "タイミングのいいことだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0255
    ChrTalk(
        0xB,
        "し、仕方ねえだろうが！\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xB,
        (
            "コウキを介抱したのは夜中だったし\x01",
            "朝イチで救急車を呼んだら……\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)

    #C0257
    ChrTalk(
        0x102,
        (
            "#0105Fそう、テスタメンツも\x01",
            "同じような状況で……\x01",
            "それでかち合ってしまったようね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 5)

    label("loc_5A1A")


    #C0258
    ChrTalk(
        0x102,
        (
            "#0105Fでもそれだと、あなた達も\x01",
            "テスタメンツの子の\x01",
            "怪我のことは知っていたのよね？\x02\x03",

            "#0100Fほら、あなた達の釘付き棍棒で\x01",
            "付けられた怪我だって……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xB,
        (
            "ハッ、あんなの\x01",
            "連中の小細工に決まってんだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xB,
        (
            "自分らで汚ぇ真似しやがったのよ。\x01",
            "普段から知性派とか\x01",
            "言いふらしてる連中だからよォ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xB,
        (
            "……クソッ、あん時は\x01",
            "ついそのまま帰ってきちまったが……\x01",
            "あの場でボコしとくんだったぜ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 6)

    label("loc_5B99")

    Jump("loc_5C18")

    label("loc_5B9E")


    #C0262
    ChrTalk(
        0xB,
        (
            "お前らがなんと言おうが\x01",
            "犯人はテスタメンツの連中だァ！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xB,
        (
            "ヴァルドさんの命令さえありゃあ\x01",
            "すぐにでも潰してやるぜェ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C18")

    TalkEnd(0xFE)
    Return()

    # Function_20_4D3E end

    def Function_21_5C1C(): pass

    label("Function_21_5C1C")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0264
    ChrTalk(
        0xB,
        "ディ、ディーノの野郎……！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xC,
        (
            "でもよォ、タイマン勝負だし……\x01",
            "ヴァルドさんもケチ付けんなって……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xB,
        "だ、だがよォ……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0267
    ChrTalk(
        0x101,
        "#0001F……何かあったのか？\x02",
    )

    CloseMessageWindow()

    def lambda_5D2B():
        TurnDirection(0xB, 0x0, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5D2B)

    def lambda_5D38():
        TurnDirection(0xC, 0x0, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5D38)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xC, 1)

    #C0268
    ChrTalk(
        0xB,
        (
            "どうもこうもねえ！\x01",
            "……ディーノのヤツが……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xC,
        (
            "あいつ、幹部のジェドさんに\x01",
            "タイマン挑んでよォ？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xC,
        (
            "ガチンコで殴りあった上に\x01",
            "最後はエルボー決めやがって……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xB,
        (
            "新米のくせにジェドさんを\x01",
            "叩きのめすなんざ……\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xB,
        "ありえねえ、許されねえぜェ！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 7)
    OP_93(0xB, 0x13B, 0x0)
    OP_93(0xC, 0x87, 0x0)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_21_5C1C end

    def Function_22_5E66(): pass

    label("Function_22_5E66")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0273
    ChrTalk(
        0xB,
        "ハッ、串焼きかオムライスだろ。\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "でもよー、三色アイスとか\x01",
            "食ってみたくねェ？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xB,
        (
            "ば、馬鹿ヤロウ……\x01",
            "アイスなんざ軟弱者の\x01",
            "食いモンだァ！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_22_5E66 end

    def Function_23_5F08(): pass

    label("Function_23_5F08")


    #C0276
    ChrTalk(
        0xB,
        (
            "クソ、あの青坊主の大男が。\x01",
            "いつもイミ判んねえ事しやがって……！\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xB,
        "連中、いつかぶっ潰してやんぜェ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 0)
    Return()

    # Function_23_5F08 end

    def Function_24_5F77(): pass

    label("Function_24_5F77")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_600B")
    Jump("loc_6055")

    label("loc_600B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_602B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6055")

    label("loc_602B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_604B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6055")

    label("loc_604B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6055")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_60CF")

    #C0278
    ChrTalk(
        0x11,
        "ハァ？　サツの連中かよ。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x11,
        (
            "今日は宴会だ。\x01",
            "邪魔すんじゃねえぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6232")

    label("loc_60CF")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    SetChrSubChip(0x11, 0x0)

    #C0280
    ChrTalk(
        0xC,
        (
            "そういやよお？\x01",
            "この前、リーシャの奴を\x01",
            "からかってやろうとしたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xC,
        (
            "あいつ、ヒラヒラ～って\x01",
            "軽くかわしやがってよォ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xC,
        "ハァ、全然捕まらねェ～！\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x11,
        "チッ、実は俺もかわされたぜ。\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x11,
        (
            "脅しても全然ビビらねえしな。\x01",
            "何なんだ、あいつはよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#0000F（ハハハ、リーシャはあれで\x01",
            "  アルカンシェルの\x01",
            "  アーティストだもんな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)

    label("loc_6232")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_5F77 end

    def Function_25_623A(): pass

    label("Function_25_623A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6295")

    #C0286
    ChrTalk(
        0xC,
        "ディーノのやつ、帰ってこねえ。\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xC,
        "……ヒャハ、何やってやがんだ～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_71EA")

    label("loc_6295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_63BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6318")

    #C0288
    ChrTalk(
        0xC,
        (
            "何だかよォ、ディーノのヤツも\x01",
            "様子おかしかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xC,
        (
            "ハイになっちまって、\x01",
            "目が血走ってやがったァ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63B9")

    label("loc_6318")


    #C0290
    ChrTalk(
        0xC,
        (
            "ヒャハ、ディーノのやつがよォ……！\x01",
            "ディーノのやつがよォ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xC,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xC,
        (
            "や、やっぱ言えねえ……\x01",
            "ヴァルドさんの前だしなァ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_63B9")

    Jump("loc_71EA")

    label("loc_63BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_6478")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_63FE")

    #C0293
    ChrTalk(
        0xC,
        (
            "ハァ、なんで\x01",
            "こうなっちまたんだァ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6473")

    label("loc_63FE")


    #C0294
    ChrTalk(
        0xC,
        "今日はみんなピリピリしてんだァ。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xC,
        (
            "ヴァルドさんなんざ\x01",
            "オーラ纏っててヨォ？\x01",
            "ちょー怒ってる気がすんぜェ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6473")

    Jump("loc_71EA")

    label("loc_6478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6513")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_650B")

    #C0296
    ChrTalk(
        0xC,
        (
            "ディーノのヤツ、\x01",
            "急に態度でかくなりやがってよォ……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xC,
        (
            "でもジェドさんを伸ばすなんて……\x01",
            "……はァ、どうなってんだァ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_650E")

    label("loc_650B")

    Call(0, 21)

    label("loc_650E")

    Jump("loc_71EA")

    label("loc_6513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_65C7")

    #C0298
    ChrTalk(
        0xC,
        "ハァ、こんな時にサツかァ？\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xC,
        (
            "シャア～～～、失せやがれェ！\x01",
            "邪魔すっとボコボコにすんぞォ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x109,
        (
            "#0501F（旧市街の不良……？\x01",
            "  気が立っているみたいですが……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71EA")

    label("loc_65C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_671F")

    #C0301
    ChrTalk(
        0xC,
        "お、この酒うめェ～。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xC,
        "ヒャハ、一気飲みしてやんぜェ？\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#0006F……ちゃんと\x01",
            "成人してるんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6687")

    #C0304
    ChrTalk(
        0x102,
        (
            "#0100F１８歳は超えてそうだから\x01",
            "大丈夫じゃない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_671A")

    label("loc_6687")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66D7")

    #C0305
    ChrTalk(
        0x103,
        (
            "#0203F１８歳は超えてそうですね。\x01",
            "ぎりぎり大丈夫かと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_671A")

    label("loc_66D7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_671A")

    #C0306
    ChrTalk(
        0x104,
        (
            "#0304Fま、１８は超えてそうだから\x01",
            "大丈夫だろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_671A")

    Jump("loc_71EA")

    label("loc_671F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6791")

    #C0307
    ChrTalk(
        0xC,
        (
            "最終日の宴会は\x01",
            "サーベルバイパーのお決まりだァ！\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xC,
        (
            "邪魔すっとテメエらも\x01",
            "ボコボコにすんぞォ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71EA")

    label("loc_6791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6885")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_67F6")

    #C0309
    ChrTalk(
        0xC,
        "次のバトルレース、いつやるんだ～？\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xC,
        "ヒャハ、次は俺らも混ぜさせろォ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_6880")

    label("loc_67F6")


    #C0311
    ChrTalk(
        0xC,
        (
            "昨日のバトルレース、\x01",
            "凄かったじゃねえ？\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xC,
        (
            "俺もヒューイも\x01",
            "寝付けなくてよォ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xC,
        (
            "つい夜中に暴れちまったぜェ。\x01",
            "ヒャハハァ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6880")

    Jump("loc_71EA")

    label("loc_6885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6896")
    Call(0, 22)
    Jump("loc_71EA")

    label("loc_6896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_69AD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6952")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 2)), scpexpr(EXPR_END)), "loc_694A")

    #C0314
    ChrTalk(
        0xC,
        (
            "いよいよ青坊主どもと戦争かァ？\x01",
            "ヒャハ、やってやんぜェ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xC,
        (
            "……って言いてえトコだけどよ？\x01",
            "今日は何か疲れちまったァ、\x01",
            "明日にするかァ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_694D")

    label("loc_694A")

    Call(0, 26)

    label("loc_694D")

    Jump("loc_69A8")

    label("loc_6952")


    #C0316
    ChrTalk(
        0xC,
        (
            "ヒャハ！\x01",
            "いよいよ青坊主どもと戦争かァ？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        (
            "望む所だァ！\x01",
            "最近目障りなんだよォ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69A8")

    Jump("loc_71EA")

    label("loc_69AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6A93")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6A40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 2)), scpexpr(EXPR_END)), "loc_6A38")

    #C0318
    ChrTalk(
        0xC,
        (
            "あの大男、いっつも\x01",
            "説教しやがってよ？\x01",
            "マジでイミ判かんね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xC,
        "ハア、何か気が抜けちまったァ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A3B")

    label("loc_6A38")

    Call(0, 26)

    label("loc_6A3B")

    Jump("loc_6A8E")

    label("loc_6A40")


    #C0320
    ChrTalk(
        0xC,
        (
            "ぜーぜー……\x01",
            "もうだめだァ～……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xC,
        (
            "ルガノフさん、\x01",
            "ケンカ強すぎだぞォ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A8E")

    Jump("loc_71EA")

    label("loc_6A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6BBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6B05")

    #C0322
    ChrTalk(
        0xC,
        (
            "よォよォ、兄ちゃんたち～。\x01",
            "俺とケンカしねえ？\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xC,
        "ヒャハ、退屈してたトコだかんよ～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BB6")

    label("loc_6B05")


    #C0324
    ChrTalk(
        0xC,
        (
            "よォよォ、なんだ兄ちゃんたち～。\x01",
            "殴りこみかァ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xC,
        (
            "ヒャハ、いいぜ～？\x01",
            "俺が相手してやらァ！\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xC,
        (
            "最近、青坊主どもとも\x01",
            "ケンカしてなくてよ？\x01",
            "退屈してたトコだかんよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6BB6")

    Jump("loc_71EA")

    label("loc_6BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6CF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6C34")

    #C0327
    ChrTalk(
        0xC,
        (
            "ヒャハッ、旧市街で\x01",
            "女が一人暮らしかよォ！\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xC,
        (
            "こいつは傑作だぜェ～？\x01",
            "ウヒャヒャヒャヒャッ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CEC")

    label("loc_6C34")


    #C0329
    ChrTalk(
        0xC,
        (
            "例の女、やっぱ\x01",
            "ロータスハイツに越してきたらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xC,
        (
            "ヒャハッ、バッカじゃねーッ！？\x01",
            "旧市街で女が一人暮らしかよォ！\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xC,
        (
            "ヒャハハッ、胸もでけえしな！\x01",
            "ウヒャヒャヒャヒャッ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6CEC")

    Jump("loc_71EA")

    label("loc_6CF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6E66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6D62")

    #C0332
    ChrTalk(
        0xC,
        (
            "表の通りで\x01",
            "見慣れねえ女を見かけたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xC,
        (
            "ヒャヒャ、ありゃ\x01",
            "旧市街の新入りかなァ～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E61")

    label("loc_6D62")


    #C0334
    ChrTalk(
        0xC,
        (
            "この前、表の通りで\x01",
            "見慣れねえ女を見かけてよォ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xC,
        "ヒャヒャ、ぼけ～っとした女でよ？\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xC,
        "……胸、胸でけえんだぜ！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0337
    ChrTalk(
        0x102,
        "#0106F（男の子ねぇ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6E61")

    Jump("loc_71EA")

    label("loc_6E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_70AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6ECA")

    #C0338
    ChrTalk(
        0xC,
        "ハァ！　覚えてやがれ！\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xC,
        (
            "いずれテメエらも\x01",
            "ボコボコにしてやるゼェェ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70AA")

    label("loc_6ECA")


    #C0340
    ChrTalk(
        0xC,
        (
            "……そういやお前らよォ、\x01",
            "前に俺と闘#2Rや#ったりしてねぇ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0341
    ChrTalk(
        0xC,
        (
            "やっぱそうじゃねえか！\x01",
            "俺をボコしやがった連中じゃん！？\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xC,
        (
            "ハァ！　覚えてやがれ！\x01",
            "いずれテメエらにも\x01",
            "借りは返してやるゼェェ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0343
    ChrTalk(
        0x103,
        (
            "#0206F（今ごろ絡んでくるなんて……\x01",
            "  テンションが高い割に\x01",
            "  呆けていますね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x104,
        (
            "#0300F（こういう連中は３歩歩けば\x01",
            "  大抵の事は忘れるからなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_70AA")

    Jump("loc_71EA")

    label("loc_70AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7123")

    #C0345
    ChrTalk(
        0xC,
        "犯人は青坊主の連中だァ～！\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xC,
        (
            "ヒャハハ……！\x01",
            "連中はいつもウジ虫みてえに\x01",
            "クソ汚ェんだからよォ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71EA")

    label("loc_7123")


    #C0347
    ChrTalk(
        0xC,
        (
            "よォよォ兄ちゃんたち～、\x01",
            "なに難しい顔してんだ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xC,
        (
            "ヒャハ、ヴァルドさんの話を\x01",
            "疑ってんじゃねえだろうなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xC,
        (
            "武闘派の俺たちが\x01",
            "ンな事するわけねえだろがよォ！\x01",
            "犯人は青坊主の連中だァ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_71EA")

    TalkEnd(0xFE)
    Return()

    # Function_25_623A end

    def Function_26_71EE(): pass

    label("Function_26_71EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_7268")

    #C0350
    ChrTalk(
        0xC,
        (
            "ヴァルドさんが留守の間に\x01",
            "負けちまったァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xC,
        (
            "あとで怒られねえかな。\x01",
            "ハア、オレらやべえじゃん？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72EE")

    label("loc_7268")


    #C0352
    ChrTalk(
        0xC,
        (
            "お前らに勝ったはいいけどよ？\x01",
            "あの大男、いっつも説教しやがって……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xC,
        (
            "マジでイミ判かんね～！？\x01",
            "ハア、何か気が抜けちまったァ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72EE")

    SetScenarioFlags(0x8F, 2)
    Return()

    # Function_26_71EE end

    def Function_27_72F2(): pass

    label("Function_27_72F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_737E")

    #C0354
    ChrTalk(
        0xD,
        (
            "もう一回り、ディーノを\x01",
            "探しに行こうかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xD,
        (
            "でもヴァルドさんは\x01",
            "キレちまってるしな……\x01",
            "絶対ぶん殴られちまうぜ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE0")

    label("loc_737E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_73DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 4)), scpexpr(EXPR_END)), "loc_73D6")

    #C0356
    ChrTalk(
        0xD,
        "な、なんだお前ら……\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xD,
        (
            "こんな時に\x01",
            "入ってくんじゃねえよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73D9")

    label("loc_73D6")

    Call(0, 11)

    label("loc_73D9")

    Jump("loc_7EE0")

    label("loc_73DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_7441")

    #C0358
    ChrTalk(
        0xD,
        "ジェド先輩は病院に行ってるんだ。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xD,
        (
            "ディーノ……\x01",
            "一体どうしちまったんだよ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE0")

    label("loc_7441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_74C1")

    #C0360
    ChrTalk(
        0xD,
        (
            "ジェドさんは俺たちメンバーの\x01",
            "教育係もやってる幹部なんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xD,
        (
            "それをあんな風に\x01",
            "叩きのめしちまうなんて……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE0")

    label("loc_74C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7581")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7515")

    #C0362
    ChrTalk(
        0xD,
        (
            "ディーノは一番下っ端なんだ。\x01",
            "度胸も無い奴だったのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_757C")

    label("loc_7515")


    #C0363
    ChrTalk(
        0xD,
        (
            "ディーノのヤツ、\x01",
            "最近様子がおかしいんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xD,
        (
            "前はあんな事を\x01",
            "言い出す奴じゃなかったのに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_757C")

    Jump("loc_7EE0")

    label("loc_7581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7618")

    #C0365
    ChrTalk(
        0xD,
        (
            "今日は週に一度の\x01",
            "宴会の日なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xD,
        (
            "あとでディーノにも\x01",
            "何か持っていってやらねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x101,
        (
            "#0006F週に一度……\x01",
            "そんなに頻繁に……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE0")

    label("loc_7618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7670")

    #C0368
    ChrTalk(
        0xD,
        "あーあ、留守番は退屈だぜ。\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xD,
        "先輩たち、今ごろ何してんだろうな～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EE0")

    label("loc_7670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7794")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7707")

    #C0370
    ChrTalk(
        0xD,
        (
            "ディーノは一番下っ端だからな。\x01",
            "祭りの間もずっと留守番なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xD,
        (
            "……ちょっと可哀相だぜ。\x01",
            "１日くらい代わってやろうかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_778F")

    label("loc_7707")

    OP_4B(0xE, 0xFF)

    #C0372
    ChrTalk(
        0xD,
        "ほらよ、これは土産だ。\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xD,
        (
            "さっきひとっ走り\x01",
            "買ってきてやったぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xE,
        (
            "わ～、たこ焼きだあ！\x01",
            "お祭りって感じっすね！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    OP_4C(0xE, 0xFF)

    label("loc_778F")

    Jump("loc_7EE0")

    label("loc_7794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_77CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_77C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 3)), scpexpr(EXPR_END)), "loc_77BA")
    Call(0, 28)
    Jump("loc_77BD")

    label("loc_77BA")

    Call(0, 29)

    label("loc_77BD")

    Jump("loc_77C5")

    label("loc_77C2")

    Call(0, 28)

    label("loc_77C5")

    Jump("loc_7EE0")

    label("loc_77CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7984")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_785D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 3)), scpexpr(EXPR_END)), "loc_7855")

    #C0375
    ChrTalk(
        0xD,
        (
            "きょ、今日は朝稽古もあったし\x01",
            "疲れちまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xD,
        (
            "……よし、今日は休憩日だ。\x01",
            "一日ダラダラするぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7858")

    label("loc_7855")

    Call(0, 29)

    label("loc_7858")

    Jump("loc_797F")

    label("loc_785D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_78CF")

    #C0377
    ChrTalk(
        0xD,
        (
            "ディーノにはまだ\x01",
            "朝稽古は無理だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xD,
        (
            "ヴァルドさんも幹部のお２人も\x01",
            "滅茶苦茶つえーんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_797F")

    label("loc_78CF")


    #C0379
    ChrTalk(
        0xD,
        "あ、朝稽古はつれぇぜ……\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xD,
        (
            "そういや、ディーノにも\x01",
            "そろそろ俺たちの戦い方を\x01",
            "教えてやんねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xD,
        (
            "でもディーノは泣き虫だからな……\x01",
            "実戦でちゃんと戦えるかなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_797F")

    Jump("loc_7EE0")

    label("loc_7984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7A91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7A03")

    #C0382
    ChrTalk(
        0xD,
        (
            "先週から交代で\x01",
            "見回りをする事になったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xD,
        (
            "今日はヒューイさんと\x01",
            "スラッシュさんが行ってるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A8C")

    label("loc_7A03")


    #C0384
    ChrTalk(
        0xD,
        (
            "先週から交代で\x01",
            "この辺りの見回りを\x01",
            "する事になったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xD,
        (
            "……俺にはパシリで\x01",
            "鍛えた足があるからな。\x01",
            "見回りくらい屁でもないぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7A8C")

    Jump("loc_7EE0")

    label("loc_7A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7B7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7AE7")

    #C0386
    ChrTalk(
        0xD,
        (
            "最近先輩達がピリピリしててな。\x01",
            "こっちまでとばっちりだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B7A")

    label("loc_7AE7")


    #C0387
    ChrTalk(
        0xD,
        (
            "最近先輩達が\x01",
            "ピリピリしてるんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xD,
        (
            "昨日もパシリの買い物を間違えて\x01",
            "ジェドさんにひどく叱られたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xD,
        "とほほ……とばっちりだぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7B7A")

    Jump("loc_7EE0")

    label("loc_7B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7DA6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7C97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7C0C")

    #C0390
    ChrTalk(
        0xD,
        (
            "（お、お前ら……\x01",
            "  ヴァルドさんに何をしたんだよ！）\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xD,
        (
            "（超不機嫌に\x01",
            "  なっちまったじゃねえかッ！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C92")

    label("loc_7C0C")

    OP_4B(0x8, 0xFF)

    #C0392
    ChrTalk(
        0x8,
        (
            "#1601F……コウキ、酒買ってこいや。\x02\x03",

            "#1607Fグズグズすんなやオラァ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0393
    ChrTalk(
        0xD,
        "は、は、はいっ！\x02",
    )

    CloseMessageWindow()
    OP_64(0xD)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    OP_4C(0x8, 0xFF)

    label("loc_7C92")

    Jump("loc_7DA1")

    label("loc_7C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7D19")

    #C0394
    ChrTalk(
        0xD,
        (
            "見張りの仕事は厳しいけど\x01",
            "新米の訓練みたいなもんだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xD,
        (
            "ディーノのやつ、\x01",
            "しっかりやってるといいんだが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DA1")

    label("loc_7D19")


    #C0396
    ChrTalk(
        0xD,
        (
            "ディーノのやつ、\x01",
            "ちゃんと見張りしてやがるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xD,
        (
            "俺、明日は病院に\x01",
            "行かなくちゃいけねえんだ。\x01",
            "しっかりやってるといいんだが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7DA1")

    Jump("loc_7EE0")

    label("loc_7DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7E09")

    #C0398
    ChrTalk(
        0xD,
        (
            "これ以上ヴァルドさんに\x01",
            "心配は掛けらんねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xD,
        "病院でおちおち寝てられっかよ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EE0")

    label("loc_7E09")


    #C0400
    ChrTalk(
        0xD,
        "痛っ……まだズキズキしやがる。\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        (
            "#0005F怪我……大丈夫か？\x02\x03",

            "確か全治一ヶ月って聞いたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xD,
        (
            "はっ、おちおち寝てられっかよ！\x01",
            "ムリヤリ退院してきてやったぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x104,
        (
            "#0306F……ま、元気が\x01",
            "あっていいんじゃね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7EE0")

    TalkEnd(0xFE)
    Return()

    # Function_27_72F2 end

    def Function_28_7EE4(): pass

    label("Function_28_7EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7F9A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7F44")

    #C0404
    ChrTalk(
        0xD,
        "くそっ、デカイ顔しやがって……\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xD,
        "い、いずれぶっ潰してやるぜ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F95")

    label("loc_7F44")


    #C0406
    ChrTalk(
        0xD,
        "くそっ、デカイ顔しやがって……\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xD,
        (
            "ムカつくぜ。\x01",
            "こうなったら全面戦争だな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F95")

    Jump("loc_801E")

    label("loc_7F9A")


    #C0408
    ChrTalk(
        0xD,
        (
            "この前見回りをしていたら\x01",
            "テスタメンツの連中と\x01",
            "鉢合わせしちまったんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xD,
        (
            "だから、今日はその会議なんだ。\x01",
            "邪魔すんなよ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_801E")

    Return()

    # Function_28_7EE4 end

    def Function_29_801F(): pass

    label("Function_29_801F")


    #C0410
    ChrTalk(
        0xD,
        (
            "ヘッド抜きの４対４勝負なんざ、\x01",
            "おかしいと思ったんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xD,
        (
            "くそっ、お、お前らも\x01",
            "覚えてろよっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x103,
        "#0200F何か悪い事をしたでしょうか。\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x104,
        "#0300Fま、粋がるのも程ほどにな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 3)
    Return()

    # Function_29_801F end

    def Function_30_80D9(): pass

    label("Function_30_80D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_81DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_814A")

    #C0414
    ChrTalk(
        0xE,
        (
            "ジェド先輩のポジションは\x01",
            "俺が頂いてやったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xE,
        "ヒャハハ、実力ってやつだなァ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_81D5")

    label("loc_814A")


    #C0416
    ChrTalk(
        0xE,
        "アア？　なんだテメエら。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xE,
        "この俺に文句でもあんのかよ。\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xE,
        (
            "何ならこの場で\x01",
            "叩きのめしてやってもいいんだぜ。\x01",
            "ヒャハハハ……ッ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_81D5")

    Jump("loc_85C5")

    label("loc_81DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_826B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8263")
    OP_4B(0xA, 0xFF)

    #C0419
    ChrTalk(
        0xE,
        (
            "ジェドさん、そろそろ俺にも\x01",
            "稽古つけてくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xE,
        (
            "ハッ……それとも\x01",
            "俺に抜かれるのが怖いんスか？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_8266")

    label("loc_8263")

    Call(0, 18)

    label("loc_8266")

    Jump("loc_85C5")

    label("loc_826B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_837D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_82D4")

    #C0421
    ChrTalk(
        0xE,
        (
            "やっぱり\x01",
            "ヴァルドさんはカッコいいや。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xE,
        (
            "はあ、俺も早く\x01",
            "強くなりたいなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8378")

    label("loc_82D4")


    #C0423
    ChrTalk(
        0xE,
        "ここがヴァルドさんの席なんだよな……\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xE,
        (
            "へへ……やっぱ\x01",
            "ヴァルドさんはカッコいいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xE,
        (
            "俺もいつか\x01",
            "ヴァルドさんに認められるくらい\x01",
            "強くなりたいなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_8378")

    Jump("loc_85C5")

    label("loc_837D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_83E5")

    #C0426
    ChrTalk(
        0xE,
        (
            "コウキさんは\x01",
            "いつも良くしてくれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xE,
        (
            "えへへ、ぐす……\x01",
            "俺ホントにうれしいや。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85C5")

    label("loc_83E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_850D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_843E")

    #C0428
    ChrTalk(
        0xE,
        "先輩たちならいないぞ！\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xE,
        "朝から出かけちまったんだからな！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8508")

    label("loc_843E")


    #C0430
    ChrTalk(
        0xE,
        (
            "先輩たち、どこまで\x01",
            "行っちまったのかなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xE,
        "帰ってくるの、遅いなぁ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0xE, 0x0, 0)
    Sleep(1000)

    #C0432
    ChrTalk(
        0xE,
        (
            "わっ……！？\x01",
            "な、なんだよ、驚かすなよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xE,
        "ぶ、ぶ、ぶっ飛ばすぞっ！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 6)

    label("loc_8508")

    Jump("loc_85C5")

    label("loc_850D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_8575")
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0434
    ChrTalk(
        0xE,
        (
            "あっ……\x01",
            "こら、勝手に入ってくるなよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xE,
        "ぶ、ぶっとばすぞっ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_85C5")

    label("loc_8575")


    #C0436
    ChrTalk(
        0xE,
        "コウキさんが帰ってきたんだ！\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xE,
        (
            "やったぁ！\x01",
            "ありがとう、女神さま～っ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_85C5")

    TalkEnd(0xFE)
    Return()

    # Function_30_80D9 end

    def Function_31_85C9(): pass

    label("Function_31_85C9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30850.itc", 0x1E)
    LoadChrToIndex("chr/ch31750.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch02150.itc", 0x21)
    LoadChrToIndex("chr/ch02152.itc", 0x22)
    LoadChrToIndex("chr/ch02151.itc", 0x23)
    LoadChrToIndex("apl/ch50030.itc", 0x24)
    OP_68(1400, 1000, 0, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 2400, 0, -700, 90)
    SetChrPos(0x102, 2400, 0, 700, 90)
    SetChrPos(0x103, 1100, 0, -700, 90)
    SetChrPos(0x104, 1100, 0, 700, 90)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 17650, 1050, 0, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    SetChrPos(0x9, 12600, 0, 3000, 315)
    SetChrPos(0xA, 11400, 0, 3800, 135)
    SetChrPos(0xB, 12600, 0, -4300, 270)
    SetChrPos(0xC, 11000, 0, -4300, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    OP_78(0x0, 0x12)
    OP_78(0x1, 0x13)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    OP_49()
    SetChrPos(0x12, 16000, 1000, 1600, 0)
    OP_D3(0x12, 0x0, 0xAFC8, 0x0, 0x0)
    SetChrPos(0x13, 16000, 1000, 1600, 0)
    OP_D3(0x13, 0x0, 0xAFC8, 0x0, 0x0)
    LoadEffect(0x0, "battle\\ms00001.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01600.itp")
    ClearMapFlags(0x10000000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_68(3400, 1000, 0, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0438
    ChrTalk(
        0x102,
        "#0101Fここは……\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x103,
        "#6P#0211F……耳障りですね……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x101,
        "#6P#0001Fなるほど、ライブハウスか……\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x104,
        (
            "#0309Fはは、イカした場所を\x01",
            "溜まり場にしてやがるな。\x02",
        )
    )

    CloseMessageWindow()

    #N0442
    NpcTalk(
        0x8,
        "獰猛そうな声",
        "クク、待ってたぜ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(14700, 1100, 0, 2500)
    MoveCamera(50, 19, 0, 2500)
    SetCameraDistance(26500, 2500)

    def lambda_89AA():

        label("loc_89AA")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_89AA")

    QueueWorkItem2(0x9, 2, lambda_89AA)

    def lambda_89BC():

        label("loc_89BC")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_89BC")

    QueueWorkItem2(0xA, 2, lambda_89BC)

    def lambda_89CE():

        label("loc_89CE")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_89CE")

    QueueWorkItem2(0xB, 2, lambda_89CE)

    def lambda_89E0():

        label("loc_89E0")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_89E0")

    QueueWorkItem2(0xC, 2, lambda_89E0)
    OP_6F(0x79)

    #N0443
    NpcTalk(
        0x9,
        "赤ジャージの青年",
        (
            "#11Pこ、こいつら\x01",
            "よくもヌケヌケと……\x02",
        )
    )

    CloseMessageWindow()

    #N0444
    NpcTalk(
        0xB,
        "赤ジャージの青年",
        (
            "#11Pハッ、わざわざフクロに\x01",
            "されに来やがったのか……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A7C():
        OP_95(0xFE, 10800, 0, -700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A7C)
    Sleep(50)

    def lambda_8A99():
        OP_95(0xFE, 10800, 0, 700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8A99)
    Sleep(50)

    def lambda_8AB6():
        OP_95(0xFE, 9500, 0, -700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8AB6)
    Sleep(50)

    def lambda_8AD3():
        OP_95(0xFE, 9500, 0, 700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8AD3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xC, 0x2)
    Sound(1805, 255, 100, 0)    #voice#Wald
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0445
    AnonymousTalk(
        0x8,
        (
            "どうやら青坊主どもからは\x01",
            "一通り話は聞いたみてぇだな。\x02\x03",

            "それで、どうした？\x01",
            "俺たちを逮捕しに来たのかよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0446
    ChrTalk(
        0x101,
        (
            "#0003Fいや……捜査に\x01",
            "協力してもらいたいだけさ。\x02\x03",

            "#0001F君たちが本気で潰し合う理由……\x02\x03",

            "それを、君たちの方からも\x01",
            "聞かせてもらいたいんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8CAA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8CAA)
    Sleep(100)

    def lambda_8CBA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8CBA)
    Sleep(50)

    def lambda_8CCA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8CCA)
    WaitChrThread(0x102, 2)

    #C0447
    ChrTalk(
        0x104,
        "#0305Fおい、どういう事だ？\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x103,
        (
            "#0205Fテスタメンツの事情聴取で\x01",
            "理由は分かったはずでは……？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0449
    ChrTalk(
        0x101,
        (
            "#5P#0003F真実は、見ている人間によって\x01",
            "様々な姿形に捉えられる……\x02\x03",

            "だからいくつもの証言を\x01",
            "照らし合わせてみないと\x01",
            "本当の真実は見極められない。\x02\x03",

            "#0000Fそれも捜査官の仕事だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x104,
        "#0300Fなるほどねぇ……\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x103,
        (
            "#0203F情報の多角的分析が\x01",
            "必要という事ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x8,
        (
            "#1604F#12Pクク……妙な小僧だぜ。\x02\x03",

            "#1602F素直に俺たちを悪役にしときゃ\x01",
            "話は簡単だったのによ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #N0453
    NpcTalk(
        0x9,
        "赤ジャージの青年",
        "#5Pヴァ、ヴァルドさん……！\x02",
    )

    CloseMessageWindow()

    def lambda_8EDC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8EDC)
    Sleep(50)

    def lambda_8EEC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8EEC)
    Sleep(50)

    def lambda_8EFC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8EFC)
    WaitChrThread(0x102, 2)

    #C0454
    ChrTalk(
        0x8,
        (
            "#1603F#12P──なあ、警察の小僧。\x02\x03",

            "仮にお前らの知りたい情報を\x01",
            "俺たちが持っているとして……\x02\x03",

            "#1600Fそれを渡す見返りに、\x01",
            "お前たちは何をくれるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x101,
        (
            "#0005F……それは……\x02\x03",

            "#0001Fどうやら、あんたには\x01",
            "『真実』じゃ不足みたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x8,
        (
            "#1604F#12Pクク、当たり前だ……\x02\x03",

            "俺はな、とにかく\x01",
            "暴れられりゃあいいんだよ。\x02\x03",

            "#1602Fこの血のたぎりを\x01",
            "スカッとさせてくれるんなら\x01",
            "何だって構わねぇんだ！！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(14200, 1000, 0, 1000)
    MoveCamera(57, 19, 0, 1000)
    SetCameraDistance(27500, 1000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    Sound(808, 0, 100, 0)
    SetChrPos(0x8, 16800, 1000, 0, 270)
    Sleep(500)
    Fade(250)

    def lambda_90ED():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_90ED)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_913B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_913B)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9163():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9163)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_918B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_918B)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_91B3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_91B3)
    Sleep(1000)

    #C0457
    ChrTalk(
        0x101,
        "#5P#0011Fな……\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x104,
        "#0301Fチッ……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x8,
        (
            "#1602F#12P俺たち全員相手に勝てりゃあ\x01",
            "何だって話してやるよ。\x02\x03",

            "クク、悪い取引じゃねえだろ？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0460
    ChrTalk(
        0x101,
        (
            "#0007Fくっ……駄目だ。\x02\x03",

            "正当防衛ならともかく、\x01",
            "俺たちに私闘は許されない！\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        (
            "#1604F#12Pおいおい、甘ちゃんな事を\x01",
            "抜かしてんじゃねえよ。\x02\x03",

            "#1602F喧嘩がイヤだってんなら……\x01",
            "そうだな、その女どもを\x01",
            "しばらく預けてもらおうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x101,
        "#0001F！！\x02",
    )

    CloseMessageWindow()

    def lambda_9344():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9344)
    Sleep(50)

    def lambda_9354():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9354)
    Sleep(50)

    def lambda_9364():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9364)
    WaitChrThread(0x104, 2)

    #C0463
    ChrTalk(
        0x103,
        "#0201F#5P……っ………\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x102,
        "#0101F………………………………\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x104,
        "#0301Fこいつら……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    OP_0D()

    def lambda_93F5():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_93F5)

    def lambda_9402():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_9402)

    def lambda_940F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_940F)

    def lambda_941C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_941C)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)

    #N0466
    NpcTalk(
        0x9,
        "赤ジャージの青年",
        "#5Pちょっ、マジっすか！？\x02",
    )

    CloseMessageWindow()

    #N0467
    NpcTalk(
        0xB,
        "赤ジャージの青年",
        (
            "さ、さすがにそれは\x01",
            "マズイいんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x8,
        (
            "#1600F#12Pるせえ、黙ってろ。\x02\x03",

            "#1604F──なに、２時間くらい\x01",
            "どこかに行ってくれりゃあいい。\x02\x03",

            "そうすりゃ、知りたいことは\x01",
            "何だって話をしてやるよ。\x02\x03",

            "#1602Fククク……\x01",
            "そんな取引ってのはどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x101,
        "#0013F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0470
    ChrTalk(
        0x101,
        (
            "#0004F……そうだな。\x01",
            "もう一つ、いい提案がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(14700, 1100, -300, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22500, 0)

    def lambda_961F():
        OP_96(0xFE, 0x2D50, 0x0, 0xFFFFFDA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_961F)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 80, 0)
    OP_0D()
    Sleep(500)

    #C0471
    ChrTalk(
        0x101,
        (
            "#6P#0001F一対一のタイマン……\x01",
            "あくまで練習試合の名目だ。\x02\x03",

            "俺が凌#2Rしの#いだら、\x01",
            "あんたが知ってることを\x01",
            "洗いざらい喋ってもらう。\x02\x03",

            "そんな趣向はどうだ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x8,
        "#1605F#12P………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_9722():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9722)
    Sleep(100)

    def lambda_9732():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9732)
    Sleep(50)

    def lambda_9742():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9742)
    WaitChrThread(0x102, 2)

    #C0473
    ChrTalk(
        0x102,
        "#0105Fちょ、ちょっと……？\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x104,
        "#0305Fおいおい……\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x103,
        "#3P#0206F……無茶苦茶です。\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x8,
        (
            "#1601F#12Pアホかお前……\x02\x03",

            "そこの赤毛ならともかく\x01",
            "どれだけの体格差だと思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x101,
        (
            "#6P#0003Fこれでも捜査官だ。\x01",
            "それなりに訓練を受けている。\x02\x03",

            "#0000F街のチンピラ風情に\x01",
            "遅れを取るつもりはないさ。\x02",
        )
    )

    CloseMessageWindow()
    #Sound(1809, 255, 100, 0)    #voice#Wald
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #C0478
    ChrTalk(
        0x8,
        "#1609F#4Sハハハハハハハハッ！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(1810, 255, 100, 0)    #voice#Wald
    OP_68(15500, 1500, 0, 1000)
    MoveCamera(43, 17, 0, 1000)
    SetCameraDistance(21000, 1000)

    def lambda_98DB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_98DB)

    def lambda_98E8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_98E8)

    def lambda_98F5():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_98F5)
    SetChrChipByIndex(0x8, 0x7)
    SetChrSubChip(0x8, 0x0)

    def lambda_990A():
        OP_96(0xFE, 0x3DB8, 0x3E8, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_990A)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    Sleep(800)
    StopBGM(0xBB8)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sleep(80)
    SetChrSubChip(0x8, 0x3)
    SetCameraDistance(23000, 1000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0x0, 0xFF, 0x8, 0x0, 0, 1000, 2000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(826, 0, 100, 0)
    OP_82(0x190, 0x190, 0xBB8, 0x12C)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)

    def lambda_99CE():
        OP_9D(0xFE, 0x3C8C, 0x3E8, 0x1F40, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_99CE)

    def lambda_99EB():
        OP_D3(0xFE, 0x0, 0xAFC8, 0xFFFFB1E0, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_99EB)
    WaitChrThread(0x13, 2)
    WaitChrThread(0x13, 1)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)

    def lambda_9A1D():
        OP_9D(0xFE, 0x3E80, 0x1C2, 0x157C, 0x64, 0x9C4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9A1D)

    def lambda_9A3A():
        OP_D3(0xFE, 0x0, 0x20F58, 0xFFFEA070, 0x190)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_9A3A)
    WaitChrThread(0x13, 2)
    WaitChrThread(0x13, 1)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    Sleep(200)
    OP_6F(0x10)
    Fade(500)
    CancelBlur(0)
    Sleep(500)

    #C0479
    ChrTalk(
        0x103,
        "#0210F……っ…………\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x101,
        "#0013F……………………………\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    Sleep(1000)

    #C0481
    ChrTalk(
        0x8,
        (
            "#11P#1604Fまさかヤツ以外に\x01",
            "この俺様にタイマンを売る\x01",
            "大馬鹿野郎がいるとはな……\x02\x03",

            "#1602Fいいだろう、小僧！！\x02\x03",

            "サーベルバイパーのヘッド、\x01",
            "ヴァルド・ヴァレスの鬼砕き……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    #C0482
    ChrTalk(
        0x8,
        "#11P#1607F#4S凌げるもんなら凌いでみやがれ！\x02",
    )

    CloseMessageWindow()
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x103, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    Battle("BattleInfo_398", 0x0, 0x0, 0x0, 0x12, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 32)
    Return()

    # Function_31_85C9 end

    def Function_32_9BDD(): pass

    label("Function_32_9BDD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30850.itc", 0x1E)
    LoadChrToIndex("chr/ch31750.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch02150.itc", 0x21)
    LoadChrToIndex("chr/ch02152.itc", 0x22)
    LoadChrToIndex("chr/ch02153.itc", 0x23)
    LoadChrToIndex("chr/ch02154.itc", 0x24)
    LoadChrToIndex("chr/ch00056.itc", 0x25)
    ClearChrBattleFlags(0x102, 0x8)
    ClearChrBattleFlags(0x103, 0x8)
    ClearChrBattleFlags(0x104, 0x8)
    OP_68(14700, 1100, -300, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 11600, 0, -600, 90)
    SetChrPos(0x102, 10800, 0, 700, 90)
    SetChrPos(0x103, 9500, 0, -700, 90)
    SetChrPos(0x104, 9500, 0, 700, 90)

    def lambda_9CA7():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9CA7)

    def lambda_9CB4():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9CB4)

    def lambda_9CC1():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9CC1)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 15800, 1000, 0, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    SetChrPos(0x9, 12600, 0, 3000, 315)
    SetChrPos(0xA, 11400, 0, 3800, 135)
    SetChrPos(0xB, 12600, 0, -4300, 270)
    SetChrPos(0xC, 11000, 0, -4300, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)

    def lambda_9DA3():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9DA3)

    def lambda_9DB0():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_9DB0)

    def lambda_9DBD():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_9DBD)

    def lambda_9DCA():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_9DCA)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    OP_78(0x0, 0x12)
    OP_78(0x1, 0x13)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    OP_49()
    SetChrPos(0x12, 16000, 1000, 1600, 0)
    OP_D3(0x12, 0x0, 0xAFC8, 0x0, 0x0)
    SetChrPos(0x13, 16000, 450, 5500, 0)
    OP_D3(0x13, 0x0, 0x20F58, 0xFFFEA070, 0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E79")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E79")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9E8F"),
        (1, "loc_9EA4"),
        (SWITCH_DEFAULT, "loc_9EB1"),
    )


    label("loc_9E8F")

    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    Jump("loc_9EB1")

    label("loc_9EA4")

    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x3)
    Jump("loc_9EB1")

    label("loc_9EB1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EC2")
    SetScenarioFlags(0x4E, 6)

    label("loc_9EC2")

    SetCameraDistance(22500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9EED"),
        (1, "loc_9FE6"),
        (SWITCH_DEFAULT, "loc_A28A"),
    )


    label("loc_9EED")

    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0483
    ChrTalk(
        0x101,
        "#6P#0010Fはあはあ……\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x8,
        (
            "#12P#1601Fフン……\x01",
            "なかなかやるみてぇだな。\x02\x03",

            "#1604F本当だったら本格的に\x01",
            "やり合ってるところだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0485
    ChrTalk(
        0x8,
        (
            "#12P#1602Fヤツとの決戦が近づいてるし、\x01",
            "このくらいで勘弁してやるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A28A")

    label("loc_9FE6")

    OP_2C(0x3E, 0x3)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0486
    ChrTalk(
        0x102,
        "#0105F#5Pあ……\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x103,
        "#5P#0205F……勝った……\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x104,
        "#5P#0309Fははっ、やるじゃん。\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x101,
        "#6P#0007Fはあはあ……これでどうだ！\x02",
    )

    CloseMessageWindow()

    def lambda_A077():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A077)
    WaitChrThread(0x8, 2)

    #C0490
    ChrTalk(
        0x8,
        (
            "#1603F#11Pチッ、やりやがったな……\x02\x03",

            "まさかここまで\x01",
            "喰い下がってくるとは……\x02",
        )
    )

    CloseMessageWindow()

    #N0491
    NpcTalk(
        0x9,
        "赤ジャージの青年",
        "#5Pヴァ、ヴァルドさん……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #N0492
    NpcTalk(
        0xB,
        "赤ジャージの青年",
        (
            "てめえ……！\x01",
            "よくもヴァルドさんを！\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x8,
        (
            "#1600F#11Pるせえ……\x01",
            "足を滑らせただけだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_A188():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_A188)
    SetChrSubChip(0x8, 0x2)
    Sound(808, 0, 100, 0)
    Sleep(50)
    Fade(250)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)

    #C0494
    ChrTalk(
        0x101,
        (
            "#6P#0001Fくっ……\x01",
            "（化物か、こいつ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x8,
        (
            "#1604F#12Pクク、なかなか\x01",
            "いい肩慣らしになったぜ。\x02\x03",

            "本当だったら本格的に\x01",
            "やり合ってるところだが……\x02\x03",

            "#1602Fヤツとの決戦が近づいてるし、\x01",
            "このくらいで勘弁してやるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A28A")

    label("loc_A28A")


    #C0496
    ChrTalk(
        0x101,
        (
            "#6P#0006Fふう……\x01",
            "そりゃ、ありがたいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0497
    ChrTalk(
        0x101,
        (
            "#6P#0001Fそれで……\x01",
            "話は聞かせてくれるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x8,
        "#1602F#12Pフン、いいだろう──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(14700, 1100, 0, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(26500, 0)

    def lambda_A363():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A363)

    def lambda_A370():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A370)

    def lambda_A37D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A37D)

    def lambda_A38A():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A38A)

    def lambda_A397():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_A397)

    def lambda_A3A4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_A3A4)

    def lambda_A3B1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_A3B1)
    SetChrChipByIndex(0x8, 0x7)
    SetChrSubChip(0x8, 0x0)

    def lambda_A3C6():
        OP_96(0xFE, 0x4268, 0x3E8, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A3C6)
    Sleep(500)

    def lambda_A3E3():
        OP_96(0xFE, 0x2A30, 0x0, 0xFFFFFD44, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A3E3)
    WaitChrThread(0x8, 1)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sound(819, 0, 100, 0)
    SetChrPos(0x8, 17650, 1050, 0, 270)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sleep(500)

    #C0499
    ChrTalk(
        0x8,
        (
            "#1603F#12P──５日前の夜のことだ。\x02\x03",

            "#1601Fウチのメンバーの１人が\x01",
            "青坊主どもの闇討ちに遭った。\x02\x03",

            "ここを出てすぐの場所だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0500
    ChrTalk(
        0x101,
        "#0005Fなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x102,
        "#0105Fそ、それって……！？\x02",
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x8,
        (
            "#1602F#12Pフン、奴らも似たような事を\x01",
            "言ってたんだろうが……\x02\x03",

            "こちらに言わせりゃ\x01",
            "とんだ言いがかりってもんだ。\x02\x03",

            "#1603F俺たちサーベルバイパーは\x01",
            "武闘派で鳴らしている……\x02\x03",

            "#1601F闇討ちなんて汚ねぇマネ、\x01",
            "するわけがねえだろうが？\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x101,
        (
            "#0003F…………………………………\x02\x03",

            "#0001Fその、闇討ちにあったメンバーは\x01",
            "どのくらいの怪我だったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x8,
        (
            "#1603F#12P打撲による骨折で\x01",
            "全治一ヶ月の入院だとよ。\x02\x03",

            "まあ、青坊主のところみたいに\x01",
            "意識不明ってわけじゃねえが……\x02\x03",

            "#1601Fケガだけって事なら\x01",
            "むしろ重たいくらいだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        "#0008Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x104,
        (
            "#0301Fしかし、テスタメンツの連中に\x01",
            "やられたってのは確かなのか？\x02\x03",

            "意識が戻ってるのなら\x01",
            "目撃証拠はあるんだろうが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(50)
    OP_64(0x9)
    OP_64(0xA)
    OP_64(0xB)
    OP_64(0xC)

    #C0507
    ChrTalk(
        0x101,
        (
            "#0005F？？？\x02\x03",

            "まさか、見ていないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x8,
        (
            "#1603F#12P……まあな。\x02\x03",

            "#1601Fだが、青坊主どもが\x01",
            "やったのは間違いねえ。\x02\x03",

            "いきなり遠くの方から\x01",
            "石が飛んできたらしいからな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0509
    ChrTalk(
        0x102,
        "#0101F石って……\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x103,
        (
            "#0201Fテスタメンツの人が使っていた\x01",
            "スリングショットですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x8,
        (
            "#1603F#12Pああ、それだ。\x02\x03",

            "それを喰らって倒れたところを\x01",
            "タコ殴りにされたらしくてな。\x02\x03",

            "#1601Fあとは気を失ったらしいが……\x01",
            "犯人は言うまでもないだろうが？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0512
    ChrTalk(
        0x8,
        (
            "#1604F#12Pクク、話は終わりだ。\x02\x03",

            "#1600F──さっきも言ったように\x01",
            "細かい事情はどうだっていい。\x02\x03",

            "青坊主どもと……\x01",
            "ヤツとケリが付けられるなら\x01",
            "もう何だっていいんだよ。\x02\x03",

            "#1602F邪魔するってんなら、いいぜ。\x02\x03",

            "青坊主どもとまとめて\x01",
            "叩き潰してやるからよォ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        (
            "#0003F……挑発には乗らないさ。\x02\x03",

            "#0000F捜査協力、感謝する。\x01",
            "色々と参考になりそうだ。\x02\x03",

            "何か判明したら\x01",
            "一応、連絡させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x8,
        (
            "#1604F#12Pフン……\x01",
            "まあ、勝手にしやがれ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetChrPos(0x9, 12540, 0, 2950, 225)
    SetChrPos(0xA, 12190, 0, -5270, 270)
    SetChrPos(0xB, 18700, 4000, -8210, 315)
    SetChrPos(0xC, 1780, 0, -5260, 90)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_68(10000, 1000, 0, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x0, 10000, 0, 0, 270)
    SetChrPos(0x1, 10000, 0, 0, 270)
    SetChrPos(0x2, 10000, 0, 0, 270)
    SetChrPos(0x3, 10000, 0, 0, 270)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetScenarioFlags(0x42, 3)
    OP_29(0x3E, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_32_9BDD end

    def Function_33_ADA5(): pass

    label("Function_33_ADA5")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(19530, 2000, 1510, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 19690, 1000, 770, 135)
    SetChrPos(0x102, 18360, 1000, 2260, 135)
    SetChrPos(0x103, 18160, 1000, 1260, 135)
    SetChrPos(0x104, 19350, 1000, 2060, 135)
    SetChrPos(0x9, 14700, 1000, -3550, 270)
    EndChrThread(0x9, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0515
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スピーカーの裏には\x01",
            "カードが貼り付けられていた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0516
    ChrTalk(
        0x101,
        (
            "#11P#0005Fあった……！\x01",
            "やっぱりここだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x103,
        (
            "#6P#0200F『９－７－１４－９－１９』。\x01",
            "アルファベット順で言えば\x01",
            "ＩＧＮＩＳ#10Rイ   グ   ニ   ス#ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x104,
        (
            "#5P#0300Fんでもって\x01",
            "『粗野なる調べ響かせる』ってのは\x01",
            "こいつの事なワケだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x102,
        (
            "#6P#0100Fでも、まだ盗まれた彫像は\x01",
            "見つかってないわよね。\x02\x03",

            "……ロイド、カードには\x01",
            "何て書いてあるの？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    #C0520
    ChrTalk(
        0x101,
        "#11P#0003Fああ、ええと……\x02",
    )

    CloseMessageWindow()

    def lambda_B05A():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B05A)

    def lambda_B067():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B067)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(700)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0521
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　 次なる鍵は 　　　\x01",
            "白ハヤブサに通ずる玄関口\x01",
            "　　時が運び去る場所　　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #C0522
    ChrTalk(
        0x101,
        (
            "#11P#0006F白ハヤブサに通ずる……\x01",
            "ま、また難解な……\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x102,
        (
            "#6P#0100F白ハヤブサといえば、\x01",
            "《不戦条約》を締結した\x01",
            "リベール王国の国鳥として有名よ。\x02\x03",

            "リベールに関係していることは\x01",
            "まず間違いないと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x104,
        (
            "#5P#0303F……まさか、リベールまで\x01",
            "行けってことじゃあねぇよな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0525
    ChrTalk(
        0x101,
        "#11P#0012Fま、まっさかぁ……\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x103,
        (
            "#6P#0203F……そんなの、\x01",
            "さすがに付き合いきれません。\x02\x03",

            "#0200F今までのパターンからして、\x01",
            "わたしたちが何とか辿りつける\x01",
            "レベルかと思われますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x8,
        (
            "#2P#1601Fオイてめえら……\x01",
            "何やってやがんだ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B39B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B39B)

    def lambda_B3A8():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B3A8)

    def lambda_B3B5():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B3B5)

    def lambda_B3C2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B3C2)
    Sleep(300)
    TurnDirection(0x8, 0x101, 0)
    TurnDirection(0xA, 0x101, 0)
    TurnDirection(0xC, 0x101, 0)
    BeginChrThread(0x9, 0, 0, 1)
    OP_68(15660, 2000, 1080, 3000)
    MoveCamera(41, 21, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(21520, 3000)
    Sleep(3000)

    #C0528
    ChrTalk(
        0x101,
        (
            "#0000Fあ、悪い。\x01",
            "邪魔してるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x103,
        (
            "#0203Fもう用事は済んだので\x01",
            "気にしないでください。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x4)

    def lambda_B47F():
        OP_95(0xFE, 14200, 1000, 580, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B47F)

    #C0530
    ChrTalk(
        0x8,
        (
            "#1607Fハァ……？\x01",
            "舐めてんのかコラァ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x104,
        (
            "#0300Fははは……こじれる前に\x01",
            "退散するとすっか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1250, 1000, -150, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    EndChrThread(0x8, 0x1)
    SetChrPos(0x0, 1250, 0, -150, 270)
    SetChrPos(0x8, 11640, 0, 270, 270)
    SetChrPos(0xA, 10370, 0, 1010, 135)
    SetChrPos(0xC, 10260, 0, -800, 45)
    SetChrFlags(0x8, 0x4)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_CA(0x1, 0xFF, 0x0)
    OP_65(0x0, 0x1)
    OP_29(0x22, 0x1, 0x3)
    ClearScenarioFlags(0xBF, 1)
    SetScenarioFlags(0x0, 7)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_33_ADA5 end

    SaveToFile()

Try(main)
