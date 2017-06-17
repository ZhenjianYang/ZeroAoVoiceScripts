from ZeroScenarioHelper import *

def main():
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
        "瓦鲁多",                 # 1
        "诺加诺夫",               # 2
        "杰德",                   # 3
        "修伊",                   # 4
        "斯拉修",                 # 5
        "寇奇",                   # 6
        "迪诺",                   # 7
        "瓦鲁多",                 # 8
        "诺加诺夫",               # 9
        "修伊",                   # 10
        "铁桶",                   # 11
        "被打过的铁桶",           # 12
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
        "Function_8_1236",         # 08, 8
        "Function_9_24E8",         # 09, 9
        "Function_10_265F",        # 0A, 10
        "Function_11_2AB6",        # 0B, 11
        "Function_12_2D9C",        # 0C, 12
        "Function_13_2E4D",        # 0D, 13
        "Function_14_2F36",        # 0E, 14
        "Function_15_3046",        # 0F, 15
        "Function_16_3A46",        # 10, 16
        "Function_17_3B87",        # 11, 17
        "Function_18_4779",        # 12, 18
        "Function_19_4856",        # 13, 19
        "Function_20_48A3",        # 14, 20
        "Function_21_5681",        # 15, 21
        "Function_22_58A9",        # 16, 22
        "Function_23_5945",        # 17, 23
        "Function_24_59AA",        # 18, 24
        "Function_25_5C43",        # 19, 25
        "Function_26_6A8B",        # 1A, 26
        "Function_27_6B81",        # 1B, 27
        "Function_28_7645",        # 1C, 28
        "Function_29_775A",        # 1D, 29
        "Function_30_7814",        # 1E, 30
        "Function_31_7C36",        # 1F, 31
        "Function_32_91EA",        # 20, 32
        "Function_33_A362",        # 21, 33
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_E2D")

    #C0001
    ChrTalk(
        0x8,
        (
            "#1601F就算是庆典，\x01",
            "也不能忘乎所以吧。\x02\x03",

            "#1607F你们在我的\x01",
            "座位后面干什么啊。\x01",
            "嗯……？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#0003F不，我们并没有做什么\x01",
            "会给你添麻烦的事。\x02\x03",

            "#0005F（说起来，那里是瓦鲁多的座位后面啊。\x01",
            "  ……竟然能在瓦鲁多毫无察觉的情况下，\x01",
            "  把卡片贴在上面吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        (
            "#0100F话说回来，你们也不要在\x01",
            "庆典中闹得太过火啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1232")

    label("loc_E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_FAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E91")

    #C0004
    ChrTalk(
        0x8,
        (
            "#1601F嘁……\x01",
            "一个一个，全都是这种德性……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        "#0000F（久留无益啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_FA7")

    label("loc_E91")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x0, 750)
    Sleep(750)

    #C0006
    ChrTalk(
        0x8,
        (
            "#1600F喂……\x02\x03",

            "#1607F想打架吗？\x01",
            "啊？嗯？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0001F等、等一下啊！\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x104,
        (
            "#0306F喂喂……\x01",
            "干什么啊，怎么突然就生气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#0101F（……他好像相当焦躁呢，\x01",
            "  还是不要在此久留了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#0200F（瓦吉先生应该会设法处理的，\x01",
            "  就交给他好了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x0)
    SetScenarioFlags(0x0, 0)

    label("loc_FA7")

    Jump("loc_1232")

    label("loc_FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_FBD")
    Call(0, 12)
    Jump("loc_1232")

    label("loc_FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 2)), scpexpr(EXPR_END)), "loc_1064")

    #C0011
    ChrTalk(
        0x8,
        (
            "#1603F那些黑衣人，最近好像\x01",
            "一直在鬼鬼祟祟地干些什么呢。\x02\x03",

            "#1604F呵呵，我也让我的部下们\x01",
            "出去巡逻了……\x02\x03",

            "#1602F只要敢踏进这旧城区一步，\x01",
            "就要他们好看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1232")

    label("loc_1064")


    #C0012
    ChrTalk(
        0x8,
        (
            "#1600F那些黑衣人最近给人的感觉很奇怪。\x02\x03",

            "所以我也让部下们\x01",
            "出去巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#0305F黑衣人……是鲁巴彻的家伙们吗？\x02\x03",

            "#0303F说起来，他们最近\x01",
            "的活动好像很频繁呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#1603F嘁，之前来的时候，\x01",
            "态度嚣张得惹人不爽，现在\x01",
            "却又鬼鬼祟祟地行动。\x02\x03",

            "#1602F……要是被我抓到，一定把他们当沙袋打。\x01",
            "呵呵，真是期待啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0006F喂喂……\x01",
            "尽量适可而止啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#0101F不过，最近这段时间，\x01",
            "重大事件的数量明显有所增加……\x02\x03",

            "黑手党组织之间的争斗，\x01",
            "确实也开始变得激烈\x01",
            "起来了呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 2)

    label("loc_1232")

    TalkEnd(0xFE)
    Return()

    # Function_7_CED end

    def Function_8_1236(): pass

    label("Function_8_1236")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12CA")
    Jump("loc_1314")

    label("loc_12CA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12EA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1314")

    label("loc_12EA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_130A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1314")

    label("loc_130A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1314")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_134A")
    Call(0, 9)
    Jump("loc_24E0")

    label("loc_134A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_13A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 4)), scpexpr(EXPR_END)), "loc_139A")

    #C0017
    ChrTalk(
        0xF,
        (
            "#1601F你们在搞什么……\x01",
            "别在这里转来转去，太碍眼了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_139D")

    label("loc_139A")

    Call(0, 11)

    label("loc_139D")

    Jump("loc_24E0")

    label("loc_13A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1685")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13F4")

    #C0018
    ChrTalk(
        0xF,
        (
            "#1601F……赶快从我眼前消失。\x01",
            "不然我就打碎你们的脑壳！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1680")

    label("loc_13F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_END)), "loc_1518")

    #C0019
    ChrTalk(
        0x101,
        (
            "#0001F瓦鲁多，听说你们同伴之间\x01",
            "发生了争斗……\x02\x03",

            "最后顺利平息了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xF,
        (
            "#1600F嗯？\x01",
            "……这种事情没理由\x01",
            "要跟你们说吧？\x02\x03",

            "#1601F赶快从我眼前消失，\x01",
            "想让我把你们的脑壳敲碎啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#0303F（好像相当暴躁呢……）\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#0101F（这样的人竟然也会\x01",
            "  辛苦地统率部下，\x01",
            "  可真是稀奇呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167D")

    label("loc_1518")


    #C0023
    ChrTalk(
        0x101,
        (
            "#0005F（大家今天的样子\x01",
            "  好像都很奇怪啊……）\x02\x03",

            "#0001F瓦鲁多，发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xF,
        (
            "#1600F嗯？\x01",
            "……这种事情没理由\x01",
            "要跟你们说吧？\x02\x03",

            "#1603F只不过是我们自己人之间\x01",
            "发生了一点小磨擦而已。\x02\x03",

            "#1601F……赶快从我眼前消失。\x01",
            "不然我就打碎你们的脑壳！\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#0305F（内斗吗……\x01",
            "  还真是少见呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#0101F（是啊，一般说来，普通成员们\x01",
            "  在他的威压之下都不敢放肆呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167D")

    SetScenarioFlags(0x0, 0)

    label("loc_1680")

    Jump("loc_24E0")

    label("loc_1685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_16FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16F4")

    #C0027
    ChrTalk(
        0xF,
        (
            "#1600F喂……不要在别人\x01",
            "的地盘上随意乱转。\x02\x03",

            "这些事情和你们没有关系，\x01",
            "赶快给我消失。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F7")

    label("loc_16F4")

    Call(0, 13)

    label("loc_16F7")

    Jump("loc_24E0")

    label("loc_16FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1777")

    #C0028
    ChrTalk(
        0xF,
        (
            "#1600F嘁……\x02\x03",

            "你们以为这里是谁的地盘啊，\x01",
            "不要随随便便就闯进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#0001F（今天的杀气特别强烈呢……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_24E0")

    label("loc_1777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_190B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_END)), "loc_1903")
    SetChrSubChip(0xF, 0x0)
    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x153, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1821")
    Jump("loc_186B")

    label("loc_1821")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1841")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_186B")

    label("loc_1841")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1861")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_186B")

    label("loc_1861")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_186B")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0030
    ChrTalk(
        0xF,
        (
            "#1604F呵呵，这小鬼看上去\x01",
            "胆量倒不小啊。\x02\x03",

            "#1602F我很欣赏你，小矮子。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x153,
        (
            "#1110F我不是小矮子，\x01",
            "是琪雅哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1906")

    label("loc_1903")

    Call(0, 10)

    label("loc_1906")

    Jump("loc_24E0")

    label("loc_190B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1919")
    Jump("loc_24E0")

    label("loc_1919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_192A")
    Call(0, 14)
    Jump("loc_24E0")

    label("loc_192A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1B29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19AE")

    #C0032
    ChrTalk(
        0xF,
        (
            "#1600F最近，警察和政府官员\x01",
            "经常跑来随便转悠。\x02\x03",

            "这群胆小如鼠的窝囊废……\x01",
            "有什么资格看不起\x01",
            "我们旧城区啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B24")

    label("loc_19AE")


    #C0033
    ChrTalk(
        0xF,
        (
            "#1603F……嘁，是你们啊。\x02\x03",

            "#1600F喂，不要随随便便\x01",
            "就跑到别人的地盘来。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#0001F你今天的情绪不太好啊……\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xF,
        (
            "#1603F没什么大不了的。\x01",
            "最近，为了准备什么纪念庆典，\x01",
            "总有警察和政府官员跑到这里来转悠。\x02\x03",

            "#1601F那群混蛋……\x01",
            "早晚要把他们全都暴打一顿。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#0306F因为纪念庆典，我们收到的\x01",
            "支援请求也逐渐增加了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        (
            "#0100F所以，还是请你\x01",
            "尽量忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B24")

    Jump("loc_24E0")

    label("loc_1B29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1DA5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C3A")

    #C0038
    ChrTalk(
        0xF,
        (
            "#1601F……看什么，有什么好看的。\x02\x03",

            "#1607F不要太得意忘形了啊。\x01",
            "嗯？要打架吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0001F不，完全没有这种打算……\x01",
            "（被我们救下，他大概\x01",
            "  相当耿耿于怀吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x103,
        (
            "#0200F（接下来恐怕还会\x01",
            "  不断对我们发脾气吧。\x01",
            "  ……还是不要在此地久留为好。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA0")

    label("loc_1C3A")

    SetChrSubChip(0xF, 0x0)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CE6")

    #C0041
    ChrTalk(
        0xF,
        "#1600F好，那就去买点什么吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0042
    ChrTalk(
        0xD,
        "刚、刚从医院回来就要去跑腿吗！？\x02",
    )

    CloseMessageWindow()
    OP_64(0xD)

    #C0043
    ChrTalk(
        0xD,
        (
            "知、知道了！\x01",
            "跑腿小弟寇奇这就出发，\x01",
            "去买东西啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D9C")

    label("loc_1CE6")


    #C0044
    ChrTalk(
        0xF,
        (
            "#1600F哦，寇奇。\x01",
            "身体怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xD,
        (
            "已经完全不要紧了！\x01",
            "让您担心啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xF,
        (
            "#1600F你明天好像还要\x01",
            "去医院复查吧。\x02\x03",

            "在彻底痊愈之前，\x01",
            "可不要勉强乱来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xD,
        (
            "是、是的！\x01",
            "多谢关心！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D9C")

    OP_4C(0xD, 0xFF)

    label("loc_1DA0")

    Jump("loc_24E0")

    label("loc_1DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1E96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E0C")

    #C0048
    ChrTalk(
        0xF,
        (
            "#1600F寇奇那家伙\x01",
            "还要再去几次医院。\x02\x03",

            "#1601F那群黑手党……\x01",
            "竟敢如此嚣张……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E91")

    label("loc_1E0C")


    #C0049
    ChrTalk(
        0xF,
        (
            "#1600F虽然已经出院了，但寇奇那家伙\x01",
            "最近还需要再回去复查几次。\x02\x03",

            "#1601F…………可恶………\x02\x03",

            "鲁巴彻的混蛋们……\x01",
            "竟敢如此嚣张……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E91")

    Jump("loc_24E0")

    label("loc_1E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_213A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F30")

    #C0050
    ChrTalk(
        0xF,
        (
            "#1600F别以为这笔账这么轻易\x01",
            "就算了结啊。\x02\x03",

            "#1601F要是那些家伙再敢搞什么阴谋，\x01",
            "我绝对会把他们都干掉……\x01",
            "你们几个也给我好好记住。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2135")

    label("loc_1F30")


    #C0051
    ChrTalk(
        0xF,
        "#1600F怎么……是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#0000F看起来，你今天的心情\x01",
            "好像不太好呢。\x02\x03",

            "……瓦鲁多，之前多谢\x01",
            "你的协助了。\x01",
            "多亏了你，我们才能顺利解决事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#0300F你们那个住院的同伴好像也\x01",
            "已经回来了吧？\x01",
            "呵，结果还算不错吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xF,
        (
            "#1603F哼……\x01",
            "这笔账，还没和鲁巴彻\x01",
            "的那些家伙们算清呢。\x02\x03",

            "至于你们和瓦吉，\x01",
            "我倒是可以不再追究。\x02\x03",

            "#1600F听好，如果那些肮脏可恶的黑手党胆敢\x01",
            "再次大摇大摆地出现在我的面前……\x02\x03",

            "#1601F本大爷一定会把他们削成人棍的。\x01",
            "你们几个也给我记清楚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#0200F……哎呀哎呀。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        "#0106F性格真是暴躁危险呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2135")

    Jump("loc_24E0")

    label("loc_213A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_226C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21C6")

    #C0057
    ChrTalk(
        0xF,
        (
            "#1600F至于圣书会的\x01",
            "那些家伙，我会亲自过去，\x01",
            "把账讨回来的。\x02\x03",

            "#1601F你们几个，要是敢妨碍我，\x01",
            "我就把你们全部干掉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2267")

    label("loc_21C6")


    #C0058
    ChrTalk(
        0xF,
        (
            "#1600F嘁，你们怎么还在\x01",
            "这附近闲逛。\x02\x03",

            "#1603F……至于圣书会的\x01",
            "那些家伙，我会亲自过去，\x01",
            "把账讨回来的。\x02\x03",

            "#1601F你们几个，要是敢妨碍我，\x01",
            "我就把你们全部干掉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2267")

    Jump("loc_24E0")

    label("loc_226C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_22FF")

    #C0059
    ChrTalk(
        0xF,
        (
            "#1600F你们那些所谓的调查行动会怎样，\x01",
            "我可是一点都不关心。\x02\x03",

            "#1602F呵呵，就在不久之后，\x01",
            "这一带可就要降下血雨了。\x01",
            "……做好觉悟吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E0")

    label("loc_22FF")


    #C0060
    ChrTalk(
        0xF,
        (
            "#1600F我这个人，不管做什么，\x01",
            "只要能尽情大闹一场就满足了。\x02\x03",

            "你们那些所谓的调查行动会怎样，\x01",
            "我可是一点都不关心。\x02\x03",

            "#1602F呵呵，过不了多久，\x01",
            "这一带可就要降下血雨了。\x01",
            "……做好觉悟吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24DD")

    #C0061
    ChrTalk(
        0xF,
        (
            "#1603F……还有…………\x02\x03",

            "#1601F喂，那边的女人，\x01",
            "你们究竟想在旧城区\x01",
            "滞留多久啊。\x02\x03",

            "#1602F难道你们很喜欢旧城区吗？\x01",
            "待在这里的话，可要做好被流氓们\x01",
            "纠缠骚扰的觉悟哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        "#0203F（……压迫感确实很强，但没什么效果。）\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        (
            "#0100F（虽然感觉上像是善意的\x01",
            "  忠告……但方法真是粗暴呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 4)

    label("loc_24DD")

    SetScenarioFlags(0x0, 0)

    label("loc_24E0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_1236 end

    def Function_9_24E8(): pass

    label("Function_9_24E8")

    OP_4B(0xF, 0xFF)
    OP_4B(0xD, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0064
    ChrTalk(
        0xD,
        "对、对不起，瓦鲁多大哥！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xD,
        (
            "我、我四处全都找遍了，\x01",
            "但不管怎样都找不到迪诺那家伙……！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xF,
        (
            "#1601F嘁……\x02\x03",

            "#1603F……到底在干什么呢，\x01",
            "那个蠢货…………\x02\x03",

            "#1601F难道是头脑发热\x01",
            "做出了什么蠢事吗……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2653")

    #C0067
    ChrTalk(
        0x10A,
        (
            "#0600F（瓦鲁多·瓦雷斯……\x01",
            "  很久没见到他了，变化不小啊。）\x02\x03",

            "#0603F（和以前相比，好像对手下们\x01",
            "  更加关照了……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2653")

    OP_64(0xD)
    OP_4C(0xF, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_24E8 end

    def Function_10_265F(): pass

    label("Function_10_265F")

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
            "#1600F噢，这不是警察一伙嘛。\x02\x03",

            "#1602F呵呵……难道是来\x01",
            "找我单挑的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#0006F为什么会如此好战啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_279B")

    #C0070
    ChrTalk(
        0x102,
        (
            "#0100F你们今天好像在开宴会啊。\x01",
            "纪念庆典才刚结束没多久呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_283A")

    label("loc_279B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27E5")

    #C0071
    ChrTalk(
        0x103,
        (
            "#0200F大家今天在一起喝酒啊。\x01",
            "……是在开宴会吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_283A")

    label("loc_27E5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_283A")

    #C0072
    ChrTalk(
        0x104,
        (
            "#0306F噢，你们今天在开宴会吗？\x01",
            "纪念庆典都结束了，还真有兴致啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_283A")

    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x153)

    #C0073
    ChrTalk(
        0x153,
        (
            "#1111F（盯着看）……\x02\x03",

            "#1110F我说，罗伊德～这个人\x01",
            "也是你的朋友吗？\x02\x03",

            "#1109F他的发型为什么\x01",
            "像只公鸡呀～\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#0011F琪、琪雅……！\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_296E")
    Jump("loc_29B8")

    label("loc_296E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_298E")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29B8")

    label("loc_298E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29AE")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29B8")

    label("loc_29AE")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29B8")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0075
    ChrTalk(
        0xF,
        (
            "#1609F哈哈哈，有意思。\x02\x03",

            "#1602F喂，小鬼，这个发型\x01",
            "可不是什么公鸡……\x02\x03",

            "#1607F这可是能让哭泣的小孩子都吓得闭嘴的\x01",
            "不死鸟——凤凰的发型啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x153,
        "#1110F噢～\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#0006F（明明是剑蛇帮，\x01",
            "  和不死鸟有什么关系……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 5)
    EventEnd(0x5)
    Return()

    # Function_10_265F end

    def Function_11_2AB6(): pass

    label("Function_11_2AB6")

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
            "#1603F喂……不在家\x01",
            "算什么意思啊？\x02\x03",

            "#1601F我不是让你把他带来吗！\x01",
            "你难道没听到吗，嗯？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xD,
        (
            "那、那个……\x01",
            "迪诺那家伙，\x01",
            "好像连家都没有回……\x02",
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
        "#1607F#4S#11P那就赶快去找啊！！\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_98(0xD, 0xFFFFFF38, 0x0, 0x0, 0x1F4, 0x0)

    #C0081
    ChrTalk(
        0xD,
        "明、明白了……！！\x02",
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
            "#0008F#6P（迪诺……难道就是记录在\x01",
            "  一科资料上的那个跑腿小弟…？）\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0301F#6P（虽然并不了解详情……\x01",
            "  但好像是行踪不明了啊……？）\x02",
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

    # Function_11_2AB6 end

    def Function_12_2D9C(): pass

    label("Function_12_2D9C")

    SetChrSubChip(0xF, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0084
    ChrTalk(
        0x8,
        (
            "#1602F呵呵，最后『啪』的一声\x01",
            "就发射出去……\x02\x03",

            "杰德，找到\x01",
            "好位置了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "噢，已经让修伊那家伙\x01",
            "去找了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xA,
        (
            "我觉得百货店的屋顶\x01",
            "好像还不错……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_12_2D9C end

    def Function_13_2E4D(): pass

    label("Function_13_2E4D")

    OP_4B(0xF, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrSubChip(0xF, 0x0)

    #C0087
    ChrTalk(
        0xF,
        "#1600F杰德，你去趟医院吧。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        "不用，我不要紧的。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xA,
        (
            "这种程度的小伤根本不值得去看医生，\x01",
            "不然也有损我们剑蛇帮的荣……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xF,
        (
            "#1601F别让我再说第二遍！\x01",
            "难道你想挨打吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        "……十分抱歉，我会照办的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xF, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_13_2E4D end

    def Function_14_2F36(): pass

    label("Function_14_2F36")

    SetChrSubChip(0xF, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0092
    ChrTalk(
        0xF,
        (
            "#1604F呵，昨天可真是\x01",
            "玩得够热闹的……\x02\x03",

            "#1602F今天就找点新地方\x01",
            "继续闹吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        "是，我们也一起去找。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "哈哈哈～！\x01",
            "今天也要尽兴呀～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3039")

    #C0095
    ChrTalk(
        0x102,
        "#0106F（稍微有点令人担心呢……）\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#0003F（嗯～但愿他们不要\x01",
            "  惹出什么麻烦呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3039")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_14_2F36 end

    def Function_15_3046(): pass

    label("Function_15_3046")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_30AF")

    #C0097
    ChrTalk(
        0x9,
        (
            "瓦鲁多大哥他啊～\x01",
            "要我稍微安静一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "好无聊啊……\x01",
            "让我唱首歌吧……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A37")

    label("loc_30AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3118")

    #C0099
    ChrTalk(
        0x9,
        (
            "#4S哇噢噢噢噢……\x01",
            "……我也要打架～～～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "干掉你！干掉你！！\x01",
            "呀！看着吧～～！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A37")

    label("loc_3118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_31B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3162")

    #C0101
    ChrTalk(
        0x9,
        (
            "既然是公平单挑，\x01",
            "就算是瓦鲁多大哥也不能干涉～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B3")

    label("loc_3162")


    #C0102
    ChrTalk(
        0x9,
        (
            "既然是公平单挑，\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "剑蛇帮原本就是以\x01",
            "弱肉强食为准则的～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_31B3")

    Jump("loc_3A37")

    label("loc_31B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3242")

    #C0104
    ChrTalk(
        0x9,
        "#4SＹＥＡＨ、ＹＥＡＨ～～～！！\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "不可能，不可能～！！\x01",
            "杰德输了，不可能啊～～～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        "不过战斗就是战斗，呀哈！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A37")

    label("loc_3242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_328D")

    #C0107
    ChrTalk(
        0x9,
        "怎么回事～气氛好恶劣啊～\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "连唱歌的兴致\x01",
            "都没有了啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A37")

    label("loc_328D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3488")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3374")

    #C0109
    ChrTalk(
        0x9,
        "嗯～这首如何啊？\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "庆典，庆典～……！\x01",
            "棉花糖啊！让我吃点吧！！\x02",
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
        "#0006F（……这也算是在唱歌吗。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3483")

    label("loc_3374")


    #C0112
    ChrTalk(
        0x9,
        (
            "#4S噢，ＹＥＡＨ～～！\x01",
            "我还没唱够呢～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        "今天就是庆典的最后一天了～\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "现在是不是应该创作一首\x01",
            "庆典时使用的新曲呢～？\x02",
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
        "#0200F现在才创作不会有点晚吗……？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3483")

    Jump("loc_3A37")

    label("loc_3488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3499")
    Call(0, 14)
    Jump("loc_3A37")

    label("loc_3499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_350F")

    #C0116
    ChrTalk(
        0x9,
        "#4S……哈～呀呀～～！！\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "把那群家伙～在此地～打得落花流水！\x01",
            "咻～就把一切都交给……本大爷吧！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A37")

    label("loc_350F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_35F2")

    #C0118
    ChrTalk(
        0x9,
        (
            "什么嘛～\x01",
            "不要打扰我啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "我正在测试今天\x01",
            "要使用的话筒呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0120
    ChrTalk(
        0x9,
        (
            "ＹＥＡＨ、ＹＥＡＨ～ＹＥＡＨ！\x01",
            "ＹＥＡＨ～ＹＥＡＨ、ＹＥＡＨ、ＹＥＡＨ！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "#4S……噢，ＹＥＡＨ～～！！\x01",
            "今天也是绝佳状态啊～～！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A37")

    label("loc_35F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_36C9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_365E")

    #C0122
    ChrTalk(
        0x9,
        (
            "哦，呀呀～！！\x01",
            "……发生什么事了吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "瓦鲁多大哥的心情\x01",
            "好像不是很好啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C4")

    label("loc_365E")

    OP_4B(0xA, 0xFF)

    #C0124
    ChrTalk(
        0x9,
        (
            "怎么了，杰德～\x01",
            "干部会议就晚点再开吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            "噢，呀呀，噢～～！！\x01",
            "……我正在创作新曲呢～！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_36C4")

    Jump("loc_3A37")

    label("loc_36C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3727")

    #C0126
    ChrTalk(
        0x9,
        "#4S……ＹＥＡＨ～呀～～！！\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "本大爷～本大爷啊啊～！！\x01",
            "咻～肚子饿啦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A37")

    label("loc_3727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_389F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3797")

    #C0128
    ChrTalk(
        0x9,
        (
            "咚咔××××咚咔咔\x01",
            "咔咚××××咚……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0129
    ChrTalk(
        0x9,
        "#4S……ＹＥＡＨ～！！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_389A")

    label("loc_3797")


    #C0130
    ChrTalk(
        0x9,
        (
            "咚咔××××咔啪\x01",
            "咔咚××××咚……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0131
    ChrTalk(
        0x9,
        "#4S……ＹＥＡＨ～！！！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#0003F（嗯～声音实在是太大了……\x01",
            "  根本听不出他在唱些什么。）\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        (
            "#0200F（伙伴出院的欢迎会……\x01",
            "  他好像是这么唱的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        (
            "#0100F（缇欧，你居然能\x01",
            "  听得懂呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_389A")

    Jump("loc_3A37")

    label("loc_389F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3907")

    #C0135
    ChrTalk(
        0x9,
        "#4S……ＹＥＡＨ～ＹＥＡＨ～！！\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "百倍偿还，百倍偿还啊～……\x01",
            "礼尚往来～呀～啊！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A37")

    label("loc_3907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3981")

    #C0137
    ChrTalk(
        0x9,
        (
            "要把圣书会那群卑鄙\x01",
            "龌龊的家伙全部干掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "你们好像也和他们有过来往吧？\x01",
            "最好别太得意忘形，自找麻烦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A37")

    label("loc_3981")


    #C0139
    ChrTalk(
        0x9,
        (
            "在这旧城区中，\x01",
            "胆敢忤逆我们的蠢货也只有\x01",
            "圣书会的那群家伙而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        "哈，不过我们很快就会把他们打垮。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        (
            "你们最好也不要太得意忘形了～\x01",
            "不然，说不定下一个被围殴的就是你们了～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3A37")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFE)
    Return()

    # Function_15_3046 end

    def Function_16_3A46(): pass

    label("Function_16_3A46")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3ADA")
    Jump("loc_3B24")

    label("loc_3ADA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3AFA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B24")

    label("loc_3AFA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B1A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B24")

    label("loc_3B1A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B24")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0142
    ChrTalk(
        0x10,
        "嗯～……好酒啊～！\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x10,
        "酒果然还是要喝威士忌啊～\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_3A46 end

    def Function_17_3B87(): pass

    label("Function_17_3B87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3BF2")

    #C0144
    ChrTalk(
        0xFE,
        (
            "你们这些警察，\x01",
            "竟然随意进入我们的地盘。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "难道是嫌命太长，想被\x01",
            "瓦鲁多大哥打死吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4775")

    label("loc_3BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3C7C")

    #C0146
    ChrTalk(
        0xA,
        (
            "饶不了迪诺那家伙。\x01",
            "等找到他后，一定要把他打扁。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0147
    ChrTalk(
        0xA,
        (
            "#4S……警察不要大摇大摆地\x01",
            "在这里转来转去！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4775")

    label("loc_3C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3CC2")

    #C0148
    ChrTalk(
        0xA,
        "竟敢趁我不在的时候……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xA,
        "…………可恶……呃！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4775")

    label("loc_3CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3D0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D02")

    #C0150
    ChrTalk(
        0xA,
        (
            "……警察局的走狗\x01",
            "不要在这里转悠……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D05")

    label("loc_3D02")

    Call(0, 13)

    label("loc_3D05")

    Jump("loc_4775")

    label("loc_3D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3D7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D73")
    OP_4B(0xE, 0xFF)

    #C0151
    ChrTalk(
        0xA,
        (
            "嘁……那是由瓦鲁多\x01",
            "大哥决定的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        "#4S不要自作主张，目无尊长啊！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    Jump("loc_3D76")

    label("loc_3D73")

    Call(0, 18)

    label("loc_3D76")

    Jump("loc_4775")

    label("loc_3D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3DF4")
    OP_4B(0x9, 0xFF)

    #C0153
    ChrTalk(
        0xA,
        (
            "从圣书会的家伙们开始在这里\x01",
            "驻扎势力算起，都已经有两年了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        "差不多也该和他们做个了结了吧。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_4775")

    label("loc_3DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3E05")
    Call(0, 12)
    Jump("loc_4775")

    label("loc_3E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3E16")
    Call(0, 14)
    Jump("loc_4775")

    label("loc_3E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3E88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 7)), scpexpr(EXPR_END)), "loc_3E80")

    #C0155
    ChrTalk(
        0xA,
        "那群蓝衣服的家伙……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xA,
        (
            "总有一天要和瓦鲁多大哥商量一下，\x01",
            "跟他们把总账算清。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E83")

    label("loc_3E80")

    Call(0, 19)

    label("loc_3E83")

    Jump("loc_4775")

    label("loc_3E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4049")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 7)), scpexpr(EXPR_END)), "loc_3F31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3ED9")

    #C0157
    ChrTalk(
        0xA,
        (
            "别来捣乱。\x01",
            "我们接下来该练习了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F2C")

    label("loc_3ED9")

    OP_4B(0xB, 0xFF)

    #C0158
    ChrTalk(
        0xA,
        "#4S好，再来一次！\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0159
    ChrTalk(
        0xB,
        "是、是的……！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_64(0xB)
    OP_4C(0xB, 0xFF)

    label("loc_3F2C")

    Jump("loc_3F42")

    label("loc_3F31")

    TurnDirection(0xA, 0x0, 0)
    Call(0, 19)
    OP_93(0xA, 0x10E, 0x0)

    label("loc_3F42")

    Jump("loc_4044")

    label("loc_3F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3FDF")

    #C0160
    ChrTalk(
        0xA,
        (
            "今天可是很重要的一天。\x01",
            "我们拜托瓦鲁多大哥\x01",
            "指导我们进行了晨练。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        (
            "刚一结束，竟然马上就累趴下了。\x01",
            "斯拉修和修伊\x01",
            "最近总是半死不活的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4044")

    label("loc_3FDF")

    OP_4B(0xB, 0xFF)

    #C0162
    ChrTalk(
        0xA,
        "修伊，拿出干劲来啊。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "在上次的争斗中，你就被那群\x01",
            "蓝衣服的家伙占到了上风啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xB, 0xFF)

    label("loc_4044")

    Jump("loc_4775")

    label("loc_4049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_412D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_40A1")

    #C0164
    ChrTalk(
        0xA,
        (
            "竟然在别人的地盘附近\x01",
            "大摇大摆地晃荡……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        "真让人不爽啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4128")

    label("loc_40A1")


    #C0166
    ChrTalk(
        0xA,
        (
            "最近，在这一带也总能看到\x01",
            "之前那辆黑车。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        "那群混蛋……\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "虽然他们好像并没有打算要插手\x01",
            "旧城区的事情，但还是让人很不爽啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4128")

    Jump("loc_4775")

    label("loc_412D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4258")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4195")

    #C0169
    ChrTalk(
        0xA,
        "我原本就是个孤儿。\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xA,
        (
            "像政府官员，警察这类人，\x01",
            "我光是听到就恶心得想吐了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4253")

    label("loc_4195")


    #C0171
    ChrTalk(
        0xA,
        (
            "政府官员也好，警察也好，\x01",
            "最后还不是什么都不打算做。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "不会有人愿意花费时间，\x01",
            "为旧城区做些什么的。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "只有在谋取自己的利益时，\x01",
            "才会一趟接一趟地跑过来……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        "哼，真让人看不惯。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4253")

    Jump("loc_4775")

    label("loc_4258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4457")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_434F")

    #C0175
    ChrTalk(
        0xA,
        (
            "你们几个，对瓦鲁多大哥\x01",
            "做了什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xA,
        (
            "如果大哥出了什么事情，\x01",
            "我可是会在这里结果你们的！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_434A")

    #C0177
    ChrTalk(
        0x104,
        (
            "#0306F不，没有啊，\x01",
            "完全不是什么大不了的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        (
            "#0103F（还是一点都没变，\x01",
            "  真是一群血气方刚的成员呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_434A")

    Jump("loc_4452")

    label("loc_434F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43DE")

    #C0179
    ChrTalk(
        0xA,
        (
            "喂，你们这群警察。\x01",
            "在『鬼火』的附近\x01",
            "干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "走来走去的，烦死人了。\x01",
            "不要打搅我们的干部会议。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4452")

    label("loc_43DE")

    OP_4B(0x9, 0xFF)

    #C0181
    ChrTalk(
        0xA,
        (
            "斯拉修和修伊那两个家伙\x01",
            "最近总是半死不活的。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        (
            "我们这些当干部的，必须要让他们\x01",
            "重新拿出毅力和干劲啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)

    label("loc_4452")

    Jump("loc_4775")

    label("loc_4457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_45A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_44C9")

    #C0183
    ChrTalk(
        0xA,
        (
            "旧城区是我们的地盘，\x01",
            "谁也没资格在这里指手划脚。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xA,
        "当然，圣书会的那些家伙也不例外。\x02",
    )

    CloseMessageWindow()
    Jump("loc_45A0")

    label("loc_44C9")


    #C0185
    ChrTalk(
        0xA,
        (
            "偶尔也会有一些政府官员\x01",
            "来到这个旧城区。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        "说是要对再开发之类的计划进行调查。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        (
            "哈，真是一群白日做梦的家伙啊。\x01",
            "结果当然是反被我恐吓了一顿，夹着尾巴回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        "……官员们还是乖乖滚回家里去睡大头觉吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_45A0")

    Jump("loc_4775")

    label("loc_45A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_469D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_45EB")

    #C0189
    ChrTalk(
        0xA,
        (
            "没想到，真正的犯人\x01",
            "竟然是那些黑手党啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4698")

    label("loc_45EB")


    #C0190
    ChrTalk(
        0xA,
        (
            "嘁，没想到真凶\x01",
            "竟然是那些黑手党啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xA,
        "我这次还真是大意了。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0192
    ChrTalk(
        0xA,
        (
            "哼，并不是在向\x01",
            "你们道谢啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "那个，这些本来就是你们警察的\x01",
            "本职工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4698")

    Jump("loc_4775")

    label("loc_469D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4727")

    #C0194
    ChrTalk(
        0xA,
        (
            "那群性格扭曲的蓝衣小子们……\x01",
            "趁现在赶快洗干净脖子等着吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xA,
        (
            "竟然敢对我们的新人下手，\x01",
            "我一定会让他们付出沉重的代价。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4775")

    label("loc_4727")


    #C0196
    ChrTalk(
        0xA,
        (
            "……警察局的走狗，\x01",
            "我和你们没话可说。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xA,
        (
            "快滚，\x01",
            "你们这群无能的吉娃娃。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4775")

    TalkEnd(0xFE)
    Return()

    # Function_17_3B87 end

    def Function_18_4779(): pass

    label("Function_18_4779")

    OP_4B(0xA, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0198
    ChrTalk(
        0xA,
        (
            "……喂，迪诺，\x01",
            "不要太得意忘形啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xA,
        "你还远远不够格呢。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xE,
        (
            "我只是说自己看门已经\x01",
            "看烦了而已啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xE,
        (
            "杰德前辈，差不多也该\x01",
            "让我参加训练了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#0005F（怎么回事？总觉得气氛好像很紧张啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_18_4779 end

    def Function_19_4856(): pass

    label("Function_19_4856")


    #C0203
    ChrTalk(
        0xA,
        "……从今以后，要强化早晨的训练。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xA,
        (
            "绝不能第二次\x01",
            "遭受到这种屈辱。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 7)
    Return()

    # Function_19_4856 end

    def Function_20_48A3(): pass

    label("Function_20_48A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_48D7")

    #C0205
    ChrTalk(
        0xB,
        (
            "那个混蛋……\x01",
            "到底去哪里了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_567D")

    label("loc_48D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_49B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4931")

    #C0206
    ChrTalk(
        0xB,
        "迪诺他今天没来。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xB,
        (
            "哈，这也很正常。\x01",
            "他已经没脸露面了吧！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49AF")

    label("loc_4931")


    #C0208
    ChrTalk(
        0xB,
        (
            "迪诺那家伙，\x01",
            "就那么傻笑着\x01",
            "离开了……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xB,
        "然后今天就没有来。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xB,
        (
            "哈，这也是当然的吧……\x01",
            "要是被我找到，一定打扁他！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_49AF")

    Jump("loc_567D")

    label("loc_49B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4A39")

    #C0211
    ChrTalk(
        0xB,
        (
            "……竟敢厚颜无耻地\x01",
            "站在杰德前辈的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xB,
        (
            "那个混蛋……\x01",
            "要不是瓦鲁多大哥制止，\x01",
            "我一定会给他点颜色看看的……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_567D")

    label("loc_4A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4ACA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_4AC2")

    #C0213
    ChrTalk(
        0xB,
        (
            "杰德前辈是我们剑蛇帮的干部。\x01",
            "实力之强，仅次于瓦鲁多大哥，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xB,
        (
            "迪诺那个混蛋……\x01",
            "居然敢小看前辈……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AC5")

    label("loc_4AC2")

    Call(0, 21)

    label("loc_4AC5")

    Jump("loc_567D")

    label("loc_4ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4B72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4B1F")

    #C0215
    ChrTalk(
        0xB,
        "嗯？你们想干什么！？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xB,
        "赶快滚到一边去，小心我揍你们！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B6D")

    label("loc_4B1F")


    #C0217
    ChrTalk(
        0xB,
        "呼，迪诺那混蛋，竟然又……\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        "他最近的态度实在是很嚣张啊……！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 3)

    label("loc_4B6D")

    Jump("loc_567D")

    label("loc_4B72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4C68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4BC5")

    #C0219
    ChrTalk(
        0xB,
        "昨天的比赛结果我实在是无法接受。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xB,
        "重新再来一次吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C63")

    label("loc_4BC5")


    #C0221
    ChrTalk(
        0xB,
        (
            "可恶……瓦鲁多大哥竟然会输，\x01",
            "我无论如何也无法接受啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xB,
        (
            "肯定都是因为和瓦吉组合，\x01",
            "所以才会输吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xB,
        (
            "瓦鲁多大哥的实力可是\x01",
            "无可置疑地强，绝对没错！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4C63")

    Jump("loc_567D")

    label("loc_4C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4C79")
    Call(0, 22)
    Jump("loc_567D")

    label("loc_4C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4D97")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4D1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 0)), scpexpr(EXPR_END)), "loc_4D17")

    #C0224
    ChrTalk(
        0xB,
        (
            "最近经常和圣书会的家伙们\x01",
            "狭路相逢。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xB,
        (
            "嘁……本来是想直接开战的，\x01",
            "但和那个魁梧的光头一对视，\x01",
            "我的气势一下就没了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D1A")

    label("loc_4D17")

    Call(0, 23)

    label("loc_4D1A")

    Jump("loc_4D92")

    label("loc_4D1F")


    #C0226
    ChrTalk(
        0xB,
        (
            "我们现在要和瓦鲁多大哥\x01",
            "一起进行晨间训练。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xB,
        (
            "哈，和那些蓝衣小子们\x01",
            "的决战可是正合我意，\x01",
            "随时都可以放马过来！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D92")

    Jump("loc_567D")

    label("loc_4D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4E31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 0)), scpexpr(EXPR_END)), "loc_4DF0")

    #C0228
    ChrTalk(
        0xB,
        (
            "哈，早晚会把你们几个\x01",
            "也干掉的。\x01",
            "做好觉悟吧……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF3")

    label("loc_4DF0")

    Call(0, 23)

    label("loc_4DF3")

    Jump("loc_4E2C")

    label("loc_4DF8")

    OP_4B(0xA, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0229
    ChrTalk(
        0xB,
        "噢、噢噢……！\x02",
    )

    CloseMessageWindow()
    OP_64(0xB)
    OP_4C(0xA, 0xFF)

    label("loc_4E2C")

    Jump("loc_567D")

    label("loc_4E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4F39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4EA2")

    #C0230
    ChrTalk(
        0xB,
        (
            "哼，最近怎么有\x01",
            "这么多警察啊，让人不爽。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xB,
        (
            "噢噢，要是敢挑衅，\x01",
            "我可会把你们打扁哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F34")

    label("loc_4EA2")


    #C0232
    ChrTalk(
        0xB,
        (
            "昨天，我只是走在东街，\x01",
            "就被一个警官给叫住了。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xB,
        (
            "哼，只是看了外表，\x01",
            "就来找我的茬……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xB,
        (
            "这也太看不起人了吧？\x01",
            "就算是警察，我也敢打！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4F34")

    Jump("loc_567D")

    label("loc_4F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_505B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4F9D")

    #C0235
    ChrTalk(
        0xB,
        (
            "有一个女人独自搬进了\x01",
            "莲花公馆的空房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xB,
        "哇哈哈……真是个蠢女人啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5056")

    label("loc_4F9D")


    #C0237
    ChrTalk(
        0xB,
        (
            "你知道吗？\x01",
            "好像有个女人独身一人搬进了\x01",
            "莲花公馆的空房间哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xB,
        (
            "哈哈，你能相信吗？\x01",
            "一个女人，竟然敢独自住在这旧城区？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xB,
        (
            "哇哈哈……我已经见过她了，\x01",
            "是个看上去就很蠢的女人啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5056")

    Jump("loc_567D")

    label("loc_505B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_51B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_50EE")

    #C0240
    ChrTalk(
        0xB,
        (
            "既然寇奇那小子回来了，\x01",
            "优势就算是回到我们这边了吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xB,
        (
            "哼，蓝衣服的小子们，你们等着瞧吧！\x01",
            "接下来就该把你们给干掉了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51AE")

    label("loc_50EE")


    #C0242
    ChrTalk(
        0xB,
        (
            "太好了！\x01",
            "寇奇已经回来了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xB,
        (
            "喔喔喔，我们的成员\x01",
            "总算是全部到齐了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xB,
        (
            "这样一来，就可以和圣书会的那些家伙\x01",
            "彻底放手一搏啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        "#0005F喂喂……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x103,
        "#0203F学习能力完全为零啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_51AE")

    Jump("loc_567D")

    label("loc_51B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_560B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 6)), scpexpr(EXPR_END)), "loc_522E")

    #C0247
    ChrTalk(
        0xB,
        (
            "那些蓝衣服的混蛋\x01",
            "竟然做出了如此卑鄙的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xB,
        (
            "早知如此，当时就应该\x01",
            "和他们大干一场才对……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5606")

    label("loc_522E")


    #C0249
    ChrTalk(
        0xB,
        (
            "可恶……现在回想起来，\x01",
            "当时要是直接和他们开战就好了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xB,
        (
            "我们把寇奇抬上急救车时，\x01",
            "正好遇到了那些蓝衣服的家伙们。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xB,
        (
            "他们说自己的同伴也昏迷不醒，\x01",
            "然后把那家伙也抬进了急救车。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 5)), scpexpr(EXPR_END)), "loc_5384")

    #C0252
    ChrTalk(
        0x101,
        (
            "#0005F啊，是吗，\x01",
            "最后你们就和圣书会的人\x01",
            "用了同一辆急救车啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54AB")

    label("loc_5384")


    #C0253
    ChrTalk(
        0x101,
        "#0005F哎……还有这种事啊？\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x104,
        (
            "#0300F怎么说呢，呼，\x01",
            "这时机也真够巧啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0255
    ChrTalk(
        0xB,
        "这、这也是没办法的事吧！\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xB,
        (
            "我们给寇奇处理伤口的时候都已经是深夜了，\x01",
            "然后等到早上就立刻叫来了救护车……\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)

    #C0257
    ChrTalk(
        0x102,
        (
            "#0105F是啊，圣书会的人\x01",
            "也处于同样的状况……\x01",
            "所以你们就在急救车里撞上了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 5)

    label("loc_54AB")


    #C0258
    ChrTalk(
        0x102,
        (
            "#0105F不过，既然如此，\x01",
            "你们应该也知道了吧？\x01",
            "圣书会的人受袭负伤的事。\x02\x03",

            "#0100F而且，从伤势来看，\x01",
            "正是被你们的钉棍打伤的……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xB,
        (
            "哼，那明显是那群家伙\x01",
            "自己搞出来的小伎俩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xB,
        (
            "他们就爱耍这种肮脏卑鄙的小手段，\x01",
            "因为他们平时就总宣扬\x01",
            "自己是什么计谋派。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xB,
        (
            "……可恶，当时是形势所迫，\x01",
            "最终还是让他们就那么回去了……\x01",
            "应该当场就干掉他们的啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 6)

    label("loc_5606")

    Jump("loc_567D")

    label("loc_560B")


    #C0262
    ChrTalk(
        0xB,
        (
            "虽然你们说了这么多，\x01",
            "但犯人绝对就是圣书会的家伙们！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xB,
        (
            "只要瓦鲁多大哥一声令下，\x01",
            "我们马上就把他们彻底打垮！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_567D")

    TalkEnd(0xFE)
    Return()

    # Function_20_48A3 end

    def Function_21_5681(): pass

    label("Function_21_5681")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0264
    ChrTalk(
        0xB,
        "迪、迪诺那混蛋……！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xC,
        (
            "但是，那毕竟是单挑比赛……\x01",
            "瓦鲁多大哥也说了不要找他麻烦……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xB,
        "可、可是……！\x02",
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
        "#0001F……发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    def lambda_5780():
        TurnDirection(0xB, 0x0, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5780)

    def lambda_578D():
        TurnDirection(0xC, 0x0, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_578D)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xC, 1)

    #C0268
    ChrTalk(
        0xB,
        (
            "没你们的事！\x01",
            "……迪诺那家伙……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xC,
        (
            "竟然向身为干部的杰德前辈\x01",
            "提出单挑比赛。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xC,
        (
            "他不但竭尽全力殴打对手，\x01",
            "而且最后还用凶狠的肘击结束了战斗……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xB,
        (
            "明明只是个新人，竟然\x01",
            "把杰德前辈打成那样……\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xB,
        "这不可能，我绝对不能原谅！！\x02",
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

    # Function_21_5681 end

    def Function_22_58A9(): pass

    label("Function_22_58A9")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0273
    ChrTalk(
        0xB,
        "哈，是吃串烧还是蛋包饭呢？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "我说啊～你不想尝尝\x01",
            "三色冰激凌吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xB,
        (
            "说、说什么蠢话……\x01",
            "冰激凌这种东西，只有软弱\x01",
            "的家伙才喜欢吃呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_22_58A9 end

    def Function_23_5945(): pass

    label("Function_23_5945")


    #C0276
    ChrTalk(
        0xB,
        (
            "可恶，那个蓝衣服的粗壮光头\x01",
            "总说一些让人听不懂的话……！\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xB,
        "总有一天，会把他们彻底击溃的！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 0)
    Return()

    # Function_23_5945 end

    def Function_24_59AA(): pass

    label("Function_24_59AA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A3E")
    Jump("loc_5A88")

    label("loc_5A3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A5E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A88")

    label("loc_5A5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A7E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A88")

    label("loc_5A7E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A88")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5AF8")

    #C0278
    ChrTalk(
        0x11,
        "哈？是警察啊。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x11,
        (
            "我们今天在开宴会呢，\x01",
            "不要来碍事啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C3B")

    label("loc_5AF8")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    SetChrSubChip(0x11, 0x0)

    #C0280
    ChrTalk(
        0xC,
        (
            "对了，\x01",
            "就在不久前，我曾经\x01",
            "试图调戏那个莉夏……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xC,
        (
            "结果她居然灵活敏捷～\x01",
            "轻松自若地就避开了我。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xC,
        "呼，完全都抓不到她啊～！\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x11,
        "哼，其实……我捉她的时候，也被她躲开了。\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x11,
        (
            "威胁她，她也完全不害怕。\x01",
            "这女人，到底是怎么回事……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#0000F（哈哈哈，莉夏她\x01",
            "  毕竟是彩虹剧团的\x01",
            "  实力派艺人啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)

    label("loc_5C3B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_59AA end

    def Function_25_5C43(): pass

    label("Function_25_5C43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5C8E")

    #C0286
    ChrTalk(
        0xC,
        "迪诺那家伙，还没回来啊。\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xC,
        "……呼，在干什么呢～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A87")

    label("loc_5C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5D8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5CFF")

    #C0288
    ChrTalk(
        0xC,
        (
            "怎么回事啊，迪诺那家伙\x01",
            "当时的样子变得很奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xC,
        (
            "不但情绪激动，而且\x01",
            "双眼充血……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D88")

    label("loc_5CFF")


    #C0290
    ChrTalk(
        0xC,
        (
            "哇，迪诺那家伙……！\x01",
            "迪诺那家伙他……！\x02",
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
            "我、我实在是说不出口啊……\x01",
            "在瓦鲁多大哥的面前……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5D88")

    Jump("loc_6A87")

    label("loc_5D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_5E2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5DC3")

    #C0293
    ChrTalk(
        0xC,
        (
            "呼，为什么会\x01",
            "变成这样呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E28")

    label("loc_5DC3")


    #C0294
    ChrTalk(
        0xC,
        "大家今天都紧绷着神经。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xC,
        (
            "瓦鲁多大哥今天给人的感觉\x01",
            "好像有些不太正常啊。\x01",
            "看上去相当恼怒……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5E28")

    Jump("loc_6A87")

    label("loc_5E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5EB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_5EAC")

    #C0296
    ChrTalk(
        0xC,
        (
            "迪诺那家伙，\x01",
            "态度突然就变得那么嚣张……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xC,
        (
            "不过，竟然能把杰德前辈……\x01",
            "……呼，到底是怎么回事啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EAF")

    label("loc_5EAC")

    Call(0, 21)

    label("loc_5EAF")

    Jump("loc_6A87")

    label("loc_5EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5F68")

    #C0298
    ChrTalk(
        0xC,
        "呼，这种时候，竟然来了警察？\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xC,
        (
            "真烦人～～～快滚回去吧！\x01",
            "敢捣乱的话，小心我把你们给打扁哦！？\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x109,
        (
            "#0501F（旧城区的不良团伙……？\x01",
            "  他们看上去好像很生气……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A87")

    label("loc_5F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_60A8")

    #C0301
    ChrTalk(
        0xC,
        "噢，好酒～\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xC,
        "哈哈，一口气喝光吧。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#0006F……他应该已经\x01",
            "成年了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6008")

    #C0304
    ChrTalk(
        0x102,
        (
            "#0100F看上去已经超过十八岁了，\x01",
            "应该没问题吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60A3")

    label("loc_6008")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6050")

    #C0305
    ChrTalk(
        0x103,
        (
            "#0203F看起来已经超过十八岁了，\x01",
            "大概没问题吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60A3")

    label("loc_6050")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60A3")

    #C0306
    ChrTalk(
        0x104,
        (
            "#0304F算了，看他的样子，应该超过十八岁了，\x01",
            "应该没什么关系吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60A3")

    Jump("loc_6A87")

    label("loc_60A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_610C")

    #C0307
    ChrTalk(
        0xC,
        (
            "在最后一天召开宴会\x01",
            "是我们剑蛇帮的惯例！\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xC,
        (
            "敢碍事的话，我可会把\x01",
            "你们都打扁哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A87")

    label("loc_610C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_61E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_616B")

    #C0309
    ChrTalk(
        0xC,
        "下次的赛跑活动，要等到什么时候啊～？\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xC,
        "哈哈，下次我们也要加入！\x02",
    )

    CloseMessageWindow()
    Jump("loc_61DB")

    label("loc_616B")


    #C0311
    ChrTalk(
        0xC,
        (
            "昨天的赛跑可真是\x01",
            "很精彩啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xC,
        (
            "我和修伊都兴奋得\x01",
            "睡不着觉呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xC,
        (
            "最后在大半夜又闹了一番。\x01",
            "哈哈哈～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_61DB")

    Jump("loc_6A87")

    label("loc_61E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_61F1")
    Call(0, 22)
    Jump("loc_6A87")

    label("loc_61F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_62F4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_629B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 2)), scpexpr(EXPR_END)), "loc_6293")

    #C0314
    ChrTalk(
        0xC,
        (
            "终于要和蓝衣服的小子们开战了吗？\x01",
            "哈，终于等到了！！\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xC,
        (
            "……我本来是想这么说的啦。\x01",
            "但今天已经很累了，\x01",
            "还是明天再说吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6296")

    label("loc_6293")

    Call(0, 26)

    label("loc_6296")

    Jump("loc_62EF")

    label("loc_629B")


    #C0316
    ChrTalk(
        0xC,
        (
            "哈！\x01",
            "终于要和蓝衣服的小子们开战了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        (
            "正合我意！\x01",
            "他们最近实在是太碍眼了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62EF")

    Jump("loc_6A87")

    label("loc_62F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_63D6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6387")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 2)), scpexpr(EXPR_END)), "loc_637F")

    #C0318
    ChrTalk(
        0xC,
        (
            "那个大个子光头，\x01",
            "平时总是说教个没完。\x01",
            "但根本听不懂他在讲什么啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xC,
        "哈，好像一下就没有干劲了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6382")

    label("loc_637F")

    Call(0, 26)

    label("loc_6382")

    Jump("loc_63D1")

    label("loc_6387")


    #C0320
    ChrTalk(
        0xC,
        (
            "完全～……\x01",
            "已经不行了～……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xC,
        (
            "诺加诺夫前辈\x01",
            "打架可是非常厉害的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63D1")

    Jump("loc_6A87")

    label("loc_63D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_64DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6430")

    #C0322
    ChrTalk(
        0xC,
        (
            "哟哟，小兄弟们～\x01",
            "要不要和我打一场？\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xC,
        "哈，我正闲得无聊呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_64D7")

    label("loc_6430")


    #C0324
    ChrTalk(
        0xC,
        (
            "哟哟，小兄弟们，你们这是干什么啊～？\x01",
            "想来打架吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xC,
        (
            "哈哈，很好哦～\x01",
            "我可以当你们的对手哟！\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xC,
        (
            "最近都没有再和那些\x01",
            "蓝衣服的小子们打架了。\x01",
            "我正闲得无聊呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_64D7")

    Jump("loc_6A87")

    label("loc_64DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_65E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6545")

    #C0327
    ChrTalk(
        0xC,
        (
            "哈哈，一个女人，\x01",
            "居然独自生活在旧城区！\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xC,
        (
            "这个真是天赐良机啊～\x01",
            "哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65DD")

    label("loc_6545")


    #C0329
    ChrTalk(
        0xC,
        (
            "那个女人，好像真的\x01",
            "搬进莲花公馆了。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xC,
        (
            "哈哈，她难道是傻瓜吗～！？\x01",
            "一个女人，居然独自生活在旧城区！\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xC,
        (
            "哈哈哈，而且她还很丰满！\x01",
            "哇哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_65DD")

    Jump("loc_6A87")

    label("loc_65E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_664B")

    #C0332
    ChrTalk(
        0xC,
        (
            "我在街上看见了一个\x01",
            "不认识的女人。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xC,
        (
            "哈哈，莫非是新入住\x01",
            "到旧城区的人吗～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6740")

    label("loc_664B")


    #C0334
    ChrTalk(
        0xC,
        (
            "不久之前，我在街上看见了\x01",
            "一个不认识的女人。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xC,
        "哈哈～那女人看上去就一副呆样哦。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xC,
        "……好、好丰满啊！！\x02",
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
        "#0106F（男人可真是……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6740")

    Jump("loc_6A87")

    label("loc_6745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6797")

    #C0338
    ChrTalk(
        0xC,
        "哼！给我记住！\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xC,
        (
            "早晚有一天，\x01",
            "会把你们也收拾掉的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_694F")

    label("loc_6797")


    #C0340
    ChrTalk(
        0xC,
        (
            "……说起来，你们不就是\x01",
            "之前和我打架的那些家伙吗？\x02",
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
            "果然没错！\x01",
            "你们就是当时把我痛打一顿的人吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xC,
        (
            "哼！给我记住！\x01",
            "这笔账，早晚有一天\x01",
            "要找你们算清楚！\x02",
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
            "#0206F（居然到现在才发现……\x01",
            "  性格如此冲动，\x01",
            "  反应却这么迟钝啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x104,
        (
            "#0300F（像这种家伙，不出三秒钟，\x01",
            "  就会把所有的事情都抛到脑后了……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_694F")

    Jump("loc_6A87")

    label("loc_6954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_69CA")

    #C0345
    ChrTalk(
        0xC,
        "犯人就是那些蓝衣服的家伙～！\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xC,
        (
            "哈哈……！\x01",
            "那些家伙就是一群鼠辈，专门\x01",
            "干这种见不得人的肮脏勾当！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A87")

    label("loc_69CA")


    #C0347
    ChrTalk(
        0xC,
        (
            "哟哟，小兄弟们～\x01",
            "为什么要摆出一副苦瓜脸啊～？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xC,
        (
            "哈，该不会是在怀疑\x01",
            "瓦鲁多大哥说的话吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xC,
        (
            "我们这种光明正大的武斗派，\x01",
            "不可能会耍那么卑鄙的手段吧！\x01",
            "犯人就是蓝衣服的那些家伙～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6A87")

    TalkEnd(0xFE)
    Return()

    # Function_25_5C43 end

    def Function_26_6A8B(): pass

    label("Function_26_6A8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_6AFD")

    #C0350
    ChrTalk(
        0xC,
        (
            "在瓦鲁多大哥离开的时候，\x01",
            "竟然输掉了……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xC,
        (
            "到时会被怒斥吧。\x01",
            "呼，我们的处境好像很危险啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B7D")

    label("loc_6AFD")


    #C0352
    ChrTalk(
        0xC,
        (
            "只要赢过你们就可以了吧？\x01",
            "那个大个子光头，总是喜欢说教……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xC,
        (
            "但根本听不懂他在讲什么啊～！\x01",
            "呼，总觉得一下就没了干劲啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B7D")

    SetScenarioFlags(0x8F, 2)
    Return()

    # Function_26_6A8B end

    def Function_27_6B81(): pass

    label("Function_27_6B81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6BFF")

    #C0354
    ChrTalk(
        0xD,
        (
            "不然就再去找一找\x01",
            "迪诺吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xD,
        (
            "不过，瓦鲁多大哥\x01",
            "好像很生气啊……\x01",
            "要是还找不到的话，绝对会被他揍的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7641")

    label("loc_6BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6C5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 4)), scpexpr(EXPR_END)), "loc_6C55")

    #C0356
    ChrTalk(
        0xD,
        "干、干什么啊，你们几个……\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xD,
        (
            "竟然在这种时候\x01",
            "随便进来！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C58")

    label("loc_6C55")

    Call(0, 11)

    label("loc_6C58")

    Jump("loc_7641")

    label("loc_6C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_6CA4")

    #C0358
    ChrTalk(
        0xD,
        "杰德前辈去医院了。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xD,
        (
            "迪诺……\x01",
            "究竟是怎么了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7641")

    label("loc_6CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6D0E")

    #C0360
    ChrTalk(
        0xD,
        (
            "杰德前辈是组织中的干部，\x01",
            "负责教育我们这些成员……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xD,
        (
            "而迪诺竟然会把前辈\x01",
            "打成那样……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7641")

    label("loc_6D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6DB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6D58")

    #C0362
    ChrTalk(
        0xD,
        (
            "迪诺是组织中地位最低的家伙，\x01",
            "而且胆子又小……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DB1")

    label("loc_6D58")


    #C0363
    ChrTalk(
        0xD,
        (
            "迪诺那家伙，\x01",
            "最近的样子很奇怪啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xD,
        (
            "如果是以前的他，\x01",
            "肯定不会说出那种话……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6DB1")

    Jump("loc_7641")

    label("loc_6DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6E35")

    #C0365
    ChrTalk(
        0xD,
        (
            "今天是每周一次\x01",
            "的宴会日。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xD,
        (
            "稍后也要让迪诺\x01",
            "带点什么东西回去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x101,
        (
            "#0006F每周一次……\x01",
            "竟然这么频繁……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7641")

    label("loc_6E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6E83")

    #C0368
    ChrTalk(
        0xD,
        "啊啊～留下看守可真是无聊啊。\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xD,
        "前辈们现在正在干什么呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_7641")

    label("loc_6E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6F83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6F14")

    #C0370
    ChrTalk(
        0xD,
        (
            "迪诺是组织中地位最低的新人。\x01",
            "所以，在庆典期间，他要一直留下来看守。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xD,
        (
            "……稍微有点可怜呢，\x01",
            "不然我就代他一天好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F7E")

    label("loc_6F14")

    OP_4B(0xE, 0xFF)

    #C0372
    ChrTalk(
        0xD,
        "看啊，这是礼物。\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xD,
        (
            "刚才特意给你\x01",
            "买来的！\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xE,
        (
            "哇～是章鱼丸子！\x01",
            "真有庆典的感觉啊！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    OP_4C(0xE, 0xFF)

    label("loc_6F7E")

    Jump("loc_7641")

    label("loc_6F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6FB9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6FB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 3)), scpexpr(EXPR_END)), "loc_6FA9")
    Call(0, 28)
    Jump("loc_6FAC")

    label("loc_6FA9")

    Call(0, 29)

    label("loc_6FAC")

    Jump("loc_6FB4")

    label("loc_6FB1")

    Call(0, 28)

    label("loc_6FB4")

    Jump("loc_7641")

    label("loc_6FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7157")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_704C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 3)), scpexpr(EXPR_END)), "loc_7044")

    #C0375
    ChrTalk(
        0xD,
        (
            "今、今天早上做了晨间训练，\x01",
            "实在是累死了。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xD,
        (
            "……好，今天是休息日，\x01",
            "接下来就随便闲晃一整天好了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7047")

    label("loc_7044")

    Call(0, 29)

    label("loc_7047")

    Jump("loc_7152")

    label("loc_704C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_70B8")

    #C0377
    ChrTalk(
        0xD,
        (
            "对迪诺来说，早上的训练\x01",
            "还是有些勉强啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xD,
        (
            "因为瓦鲁多大哥和两位干部\x01",
            "的实力都强得过分。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7152")

    label("loc_70B8")


    #C0379
    ChrTalk(
        0xD,
        "啊，晨间训练真是好累啊……\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xD,
        (
            "说起来，差不多\x01",
            "也该把我们的战斗方法\x01",
            "教给迪诺了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xD,
        (
            "不过，迪诺是个爱哭鬼……\x01",
            "能否顺利进行实战还是个未知数……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7152")

    Jump("loc_7641")

    label("loc_7157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_725A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_71CA")

    #C0382
    ChrTalk(
        0xD,
        (
            "我们上周决定，\x01",
            "全部成员都要轮流参加巡逻。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xD,
        (
            "今天负责巡逻的是修伊前辈与\x01",
            "斯拉修前辈。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7255")

    label("loc_71CA")


    #C0384
    ChrTalk(
        0xD,
        (
            "我们上周决定，\x01",
            "全部成员都要\x01",
            "轮流在附近巡逻。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xD,
        (
            "……我可是资深跑腿小弟，\x01",
            "脚力经受过足够的锻炼。\x01",
            "像巡逻这种事，简直就是小菜一碟。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7255")

    Jump("loc_7641")

    label("loc_725A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_732E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_72A2")

    #C0386
    ChrTalk(
        0xD,
        (
            "前辈们最近都紧绷着神经啊。\x01",
            "连我都受牵连了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7329")

    label("loc_72A2")


    #C0387
    ChrTalk(
        0xD,
        (
            "前辈们最近都\x01",
            "紧绷着神经啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xD,
        (
            "昨天给前辈们跑腿，结果买错了东西，\x01",
            "然后就被杰德前辈狠狠骂了一顿。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xD,
        "呵呵……真是够受的啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7329")

    Jump("loc_7641")

    label("loc_732E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_74F9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7428")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_73A9")

    #C0390
    ChrTalk(
        0xD,
        (
            "（你、你们……\x01",
            "  对瓦鲁多大哥做了什么啊！）\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xD,
        (
            "（大哥好像变得\x01",
            "  相当不高兴啊！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7423")

    label("loc_73A9")

    OP_4B(0x8, 0xFF)

    #C0392
    ChrTalk(
        0x8,
        (
            "#1601F……寇奇，去给我买酒。\x02\x03",

            "#1607F磨磨蹭蹭得干什么呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0393
    ChrTalk(
        0xD,
        "是、是、是的！\x02",
    )

    CloseMessageWindow()
    OP_64(0xD)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    OP_4C(0x8, 0xFF)

    label("loc_7423")

    Jump("loc_74F4")

    label("loc_7428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7494")

    #C0394
    ChrTalk(
        0xD,
        (
            "看守大门的工作虽然很辛苦，\x01",
            "但却是新人必须接受的训练。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xD,
        (
            "希望迪诺那家伙\x01",
            "能认真完成啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74F4")

    label("loc_7494")


    #C0396
    ChrTalk(
        0xD,
        (
            "迪诺那家伙，\x01",
            "有没有认真地看守呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xD,
        (
            "我明天必须\x01",
            "要去医院一趟。\x01",
            "希望他能把工作干好啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_74F4")

    Jump("loc_7641")

    label("loc_74F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7556")

    #C0398
    ChrTalk(
        0xD,
        (
            "不能再让瓦鲁多大哥\x01",
            "为我担心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xD,
        "我才不会在医院里安安稳稳地睡大觉呢！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7641")

    label("loc_7556")


    #C0400
    ChrTalk(
        0xD,
        "好痛……还能感觉到一阵阵刺痛呢。\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        (
            "#0005F你的伤……已经好了吗？\x02\x03",

            "听说彻底痊愈需要一个月呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xD,
        (
            "哈，我怎么可以一直躺在床上睡大觉！\x01",
            "当然是态度强硬地坚持提前出院啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x104,
        (
            "#0306F……算了，看起来倒是很有精神，\x01",
            "这样也挺好的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7641")

    TalkEnd(0xFE)
    Return()

    # Function_27_6B81 end

    def Function_28_7645(): pass

    label("Function_28_7645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_76F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_769F")

    #C0404
    ChrTalk(
        0xD,
        "可恶，竟敢这么嚣张狂妄……\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xD,
        "总、总有一天要把他们做掉！\x02",
    )

    CloseMessageWindow()
    Jump("loc_76F2")

    label("loc_769F")


    #C0406
    ChrTalk(
        0xD,
        "可恶，竟敢这么嚣张狂妄……\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xD,
        (
            "真是让人不爽。\x01",
            "既然如此，就要进入全面战争了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76F2")

    Jump("loc_7759")

    label("loc_76F7")


    #C0408
    ChrTalk(
        0xD,
        (
            "之前巡逻的时候，\x01",
            "和圣书会的家伙们\x01",
            "狭路相逢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xD,
        (
            "所以，今天就要召开会议。\x01",
            "不要碍事啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7759")

    Return()

    # Function_28_7645 end

    def Function_29_775A(): pass

    label("Function_29_775A")


    #C0410
    ChrTalk(
        0xD,
        (
            "四对四的单挑比赛，双方首领不参加，\x01",
            "当时一听就觉得有点奇怪……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xD,
        (
            "可恶，你、你们\x01",
            "也给我记住！\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x103,
        "#0200F我们做了什么惹到他的事吗？\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x104,
        "#0300F算了，阿缇，嚣张也要有个限度嘛。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 3)
    Return()

    # Function_29_775A end

    def Function_30_7814(): pass

    label("Function_30_7814")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_78F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_786F")

    #C0414
    ChrTalk(
        0xE,
        (
            "杰德前辈的位置\x01",
            "由我来顶替了。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xE,
        "哈哈，这就是所谓的实力！\x02",
    )

    CloseMessageWindow()
    Jump("loc_78F4")

    label("loc_786F")


    #C0416
    ChrTalk(
        0xE,
        "嗯？　你们几个，干什么啊。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xE,
        "对本大爷有什么意见吗？\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xE,
        (
            "有什么不满的话，\x01",
            "我就在这里把你们都收拾掉如何？\x01",
            "哇哈哈哈……呃！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_78F4")

    Jump("loc_7C32")

    label("loc_78F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_796C")
    OP_4B(0xA, 0xFF)

    #C0419
    ChrTalk(
        0xE,
        (
            "杰德前辈，差不多也该\x01",
            "让我参加训练了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xE,
        (
            "哈……还是说，\x01",
            "你害怕被我超越呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_796F")

    label("loc_796C")

    Call(0, 18)

    label("loc_796F")

    Jump("loc_7C32")

    label("loc_7974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7A56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_79C7")

    #C0421
    ChrTalk(
        0xE,
        (
            "瓦鲁多大哥\x01",
            "果然很帅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xE,
        (
            "呼，我也很想\x01",
            "早点变强啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A51")

    label("loc_79C7")


    #C0423
    ChrTalk(
        0xE,
        "这里是瓦鲁多大哥的座位啊……\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xE,
        (
            "嘿嘿……瓦鲁多大哥\x01",
            "果然很帅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xE,
        (
            "我希望自己有朝一日\x01",
            "也能变得很强，得到\x01",
            "瓦鲁多大哥的认可……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_7A51")

    Jump("loc_7C32")

    label("loc_7A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7AA8")

    #C0426
    ChrTalk(
        0xE,
        (
            "寇奇前辈平时总是\x01",
            "很关照我。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xE,
        (
            "嘿嘿，呜……\x01",
            "我真的很高兴啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C32")

    label("loc_7AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_7B9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7AEF")

    #C0428
    ChrTalk(
        0xE,
        "前辈他们都不在啦！\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xE,
        "一大早就都出门了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B99")

    label("loc_7AEF")


    #C0430
    ChrTalk(
        0xE,
        (
            "前辈们到底\x01",
            "去了什么地方呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xE,
        "回来得好晚啊……\x02",
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
            "哇……！？\x01",
            "干、干什么啊，别吓我啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xE,
        "小、小、小心我揍你啊！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 6)

    label("loc_7B99")

    Jump("loc_7C32")

    label("loc_7B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7BFA")
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0434
    ChrTalk(
        0xE,
        (
            "啊……\x01",
            "喂，不要擅自进来啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xE,
        "小、小心我揍你啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C32")

    label("loc_7BFA")


    #C0436
    ChrTalk(
        0xE,
        "寇奇前辈回来了！\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xE,
        (
            "太好啦！\x01",
            "谢谢您，女神～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_7C32")

    TalkEnd(0xFE)
    Return()

    # Function_30_7814 end

    def Function_31_7C36(): pass

    label("Function_31_7C36")

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
        "#0101F这里是……\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x103,
        "#6P#0211F……好吵啊……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x101,
        "#6P#0001F原来如此，是小剧场吗……\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x104,
        (
            "#0309F哈哈，把废弃的车库\x01",
            "改造成了据点啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0442
    NpcTalk(
        0x8,
        "凶狠的声音",
        "哼哼，我正等着你们呢。\x02",
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

    def lambda_8005():

        label("loc_8005")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_8005")

    QueueWorkItem2(0x9, 2, lambda_8005)

    def lambda_8017():

        label("loc_8017")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_8017")

    QueueWorkItem2(0xA, 2, lambda_8017)

    def lambda_8029():

        label("loc_8029")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8029")

    QueueWorkItem2(0xB, 2, lambda_8029)

    def lambda_803B():

        label("loc_803B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_803B")

    QueueWorkItem2(0xC, 2, lambda_803B)
    OP_6F(0x79)

    #N0443
    NpcTalk(
        0x9,
        "穿红色外套的青年",
        (
            "#11P这、这些家伙，\x01",
            "竟敢大摇大摆地……\x02",
        )
    )

    CloseMessageWindow()

    #N0444
    NpcTalk(
        0xB,
        "穿红色外套的青年",
        (
            "#11P哈，你们居然真的主动\x01",
            "送上门来了啊……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_80CD():
        OP_95(0xFE, 10800, 0, -700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80CD)
    Sleep(50)

    def lambda_80EA():
        OP_95(0xFE, 10800, 0, 700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_80EA)
    Sleep(50)

    def lambda_8107():
        OP_95(0xFE, 9500, 0, -700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8107)
    Sleep(50)

    def lambda_8124():
        OP_95(0xFE, 9500, 0, 700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8124)
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
            "看起来，你们已经从蓝衣小子们\x01",
            "那里听过事情经过了吧。\x02\x03",

            "那么，来这里要干什么？\x01",
            "是想来逮捕我们吗？\x02",
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
            "#0003F不……只是希望\x01",
            "你们能协助我们进行调查。\x02\x03",

            "#0001F互不相容，定要彻底打垮对方的理由……\x02\x03",

            "我们已经听那边说过了，\x01",
            "所以也想听你们说一说。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_82F3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_82F3)
    Sleep(100)

    def lambda_8303():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8303)
    Sleep(50)

    def lambda_8313():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8313)
    WaitChrThread(0x102, 2)

    #C0447
    ChrTalk(
        0x104,
        "#0305F喂，这是什么意思啊？\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x103,
        (
            "#0205F通过圣书会那边的证言，\x01",
            "理由不是已经了解得很充分了吗……？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0449
    ChrTalk(
        0x101,
        (
            "#5P#0003F所谓的真相，在不同的目击者眼中，\x01",
            "会呈现出大相径庭的形态……\x02\x03",

            "所以，只有把多方面的\x01",
            "证言放在一起对照分析，\x01",
            "才能得出真正的真相。\x02\x03",

            "#0000F这也是搜查官的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x104,
        "#0300F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x103,
        (
            "#0203F也就是说，必须要从\x01",
            "多个角度分析来得到情报吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x8,
        (
            "#1604F#12P哼哼……真是个奇怪的小子。\x02\x03",

            "#1602F只要直接把我们当成坏蛋来处理，\x01",
            "事情明明就会轻松很多呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #N0453
    NpcTalk(
        0x9,
        "穿红色外套的青年",
        "#5P瓦、瓦鲁多大哥……！\x02",
    )

    CloseMessageWindow()

    def lambda_8527():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8527)
    Sleep(50)

    def lambda_8537():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8537)
    Sleep(50)

    def lambda_8547():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8547)
    WaitChrThread(0x102, 2)

    #C0454
    ChrTalk(
        0x8,
        (
            "#1603F#12P──喂，警察小子。\x02\x03",

            "就算我手里真的有你们想知道的情报，\x01",
            "而且可以告诉你们……\x02\x03",

            "#1600F作为回报，你们又能\x01",
            "给我什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x101,
        (
            "#0005F……这个……\x02\x03",

            "#0001F看起来，对你来说，\x01",
            "光有『真相』恐怕还不够吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x8,
        (
            "#1604F#12P呵呵，当然不够……\x02\x03",

            "我这个人，不管做什么，\x01",
            "只要能尽情大闹一场就满足了。\x02\x03",

            "#1602F只要你们能用实力\x01",
            "让我沸腾的热血平息下来，\x01",
            "其它事情全都好说！！\x02",
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

    def lambda_871E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_871E)
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

    def lambda_876C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_876C)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8794():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8794)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_87BC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_87BC)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_87E4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_87E4)
    Sleep(1000)

    #C0457
    ChrTalk(
        0x101,
        "#5P#0011F什、什么……\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x104,
        "#0301F嘁……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x8,
        (
            "#1602F#12P以我们全员为对手，来场大群殴吧，\x01",
            "只要你们能打赢，想让我说什么都没问题。\x02\x03",

            "哼哼，怎么样，这交易不错吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0460
    ChrTalk(
        0x101,
        (
            "#0007F这……不行。\x02\x03",

            "如果是正当防卫也就罢了，\x01",
            "我们是绝对不能私下斗殴的！\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        (
            "#1604F#12P喂喂，不要说这种\x01",
            "假正经的无聊话嘛。\x02\x03",

            "#1602F要是实在不想打架……\x01",
            "对了，那就把这两个女人\x01",
            "暂时留在我们这里如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x101,
        "#0001F！！\x02",
    )

    CloseMessageWindow()

    def lambda_8977():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8977)
    Sleep(50)

    def lambda_8987():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8987)
    Sleep(50)

    def lambda_8997():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8997)
    WaitChrThread(0x104, 2)

    #C0463
    ChrTalk(
        0x103,
        "#0201F#5P……！………\x02",
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
        "#0301F这些家伙……\x02",
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

    def lambda_8A28():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8A28)

    def lambda_8A35():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_8A35)

    def lambda_8A42():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_8A42)

    def lambda_8A4F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_8A4F)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)

    #N0466
    NpcTalk(
        0x9,
        "穿红色外套的青年",
        "#5P等、等一下，您是认真的吗！？\x02",
    )

    CloseMessageWindow()

    #N0467
    NpcTalk(
        0xB,
        "穿红色外套的青年",
        (
            "再、再怎么说，\x01",
            "这也有点……\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x8,
        (
            "#1600F#12P吵死了，闭嘴。\x02\x03",

            "#1604F──无所谓吧，只要两个小时左右就行了。\x01",
            "把女人留下，你们随便找地方去逛逛就好啦。\x02\x03",

            "如果愿意照办，我就可以把\x01",
            "你们想知道的事情全部告诉你们哦。\x02\x03",

            "#1602F哼哼哼……\x01",
            "这交易如何啊？\x02",
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
            "#0004F……对了，\x01",
            "我还有一个好提议。\x02",
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

    def lambda_8C52():
        OP_96(0xFE, 0x2D50, 0x0, 0xFFFFFDA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C52)
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
            "#6P#0001F一对一单挑……\x01",
            "就以练习赛为名义好了。\x02\x03",

            "如果我占了上风，\x01",
            "你就要把自己知道的\x01",
            "全部事情都告诉我。\x02\x03",

            "意下如何……？\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x8,
        "#1605F#12P………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_8D31():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8D31)
    Sleep(100)

    def lambda_8D41():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8D41)
    Sleep(50)

    def lambda_8D51():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8D51)
    WaitChrThread(0x102, 2)

    #C0473
    ChrTalk(
        0x102,
        "#0105F等、等一下……\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x104,
        "#0305F喂喂……\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x103,
        "#3P#0206F……太乱来了。\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x8,
        (
            "#1601F#12P你的脑子有问题吗……\x02\x03",

            "如果是那个红毛也就罢了，\x01",
            "就凭你，也不想想体格差距有多悬殊？\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x101,
        (
            "#6P#0003F再怎么说，我也是个搜查官，\x01",
            "曾接受过很系统的战斗训练。\x02\x03",

            "#0000F以街头混混为对手，\x01",
            "我想自己还是不会输的。\x02",
        )
    )

    CloseMessageWindow()
    #Sound(1809, 255, 100, 0)    #voice#Wald
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #C0478
    ChrTalk(
        0x8,
        "#1609F#4S哈哈哈哈哈哈哈哈！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(1810, 255, 100, 0)    #voice#Wald
    OP_68(15500, 1500, 0, 1000)
    MoveCamera(43, 17, 0, 1000)
    SetCameraDistance(21000, 1000)

    def lambda_8EEC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8EEC)

    def lambda_8EF9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8EF9)

    def lambda_8F06():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8F06)
    SetChrChipByIndex(0x8, 0x7)
    SetChrSubChip(0x8, 0x0)

    def lambda_8F1B():
        OP_96(0xFE, 0x3DB8, 0x3E8, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8F1B)
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

    def lambda_8FDF():
        OP_9D(0xFE, 0x3C8C, 0x3E8, 0x1F40, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8FDF)

    def lambda_8FFC():
        OP_D3(0xFE, 0x0, 0xAFC8, 0xFFFFB1E0, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8FFC)
    WaitChrThread(0x13, 2)
    WaitChrThread(0x13, 1)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)

    def lambda_902E():
        OP_9D(0xFE, 0x3E80, 0x1C2, 0x157C, 0x64, 0x9C4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_902E)

    def lambda_904B():
        OP_D3(0xFE, 0x0, 0x20F58, 0xFFFEA070, 0x190)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_904B)
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
        "#0210F……！…………\x02",
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
            "#11P#1604F真是没想到，\x01",
            "除了那个家伙之外，居然还会有\x01",
            "胆敢和本大爷单挑的超级大蠢货……\x02\x03",

            "#1602F好，小子，我就答应你！！\x02\x03",

            "剑蛇帮的老大，\x01",
            "瓦鲁多·瓦雷斯的碎鬼……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    #C0482
    ChrTalk(
        0x8,
        "#11P#1607F#4S如果觉得自己赢得了，就放马过来吧！\x02",
    )

    CloseMessageWindow()
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x103, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    Battle("BattleInfo_398", 0x0, 0x0, 0x0, 0x12, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 32)
    Return()

    # Function_31_7C36 end

    def Function_32_91EA(): pass

    label("Function_32_91EA")

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

    def lambda_92B4():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_92B4)

    def lambda_92C1():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_92C1)

    def lambda_92CE():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_92CE)
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

    def lambda_93B0():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_93B0)

    def lambda_93BD():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_93BD)

    def lambda_93CA():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_93CA)

    def lambda_93D7():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_93D7)
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9486")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9486")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_949C"),
        (1, "loc_94B1"),
        (SWITCH_DEFAULT, "loc_94BE"),
    )


    label("loc_949C")

    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    Jump("loc_94BE")

    label("loc_94B1")

    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x3)
    Jump("loc_94BE")

    label("loc_94BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94CF")
    SetScenarioFlags(0x4E, 6)

    label("loc_94CF")

    SetCameraDistance(22500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_94FA"),
        (1, "loc_95EB"),
        (SWITCH_DEFAULT, "loc_9881"),
    )


    label("loc_94FA")

    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0483
    ChrTalk(
        0x101,
        "#6P#0010F呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x8,
        (
            "#12P#1601F哼……\x01",
            "好像还有点能耐啊。\x02\x03",

            "#1604F其实我是想拿出真本事，\x01",
            "和你战个痛快的……\x02",
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
            "#12P#1602F不过，和那家伙的决战日期已经临近了，\x01",
            "这次就放过你，到此为止好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9881")

    label("loc_95EB")

    OP_2C(0x3E, 0x3)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0486
    ChrTalk(
        0x102,
        "#0105F#5P啊……\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x103,
        "#5P#0205F……赢了……\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x104,
        "#5P#0309F哈哈，干得不错嘛。\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x101,
        "#6P#0007F呼、呼……怎么样！\x02",
    )

    CloseMessageWindow()

    def lambda_9670():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9670)
    WaitChrThread(0x8, 2)

    #C0490
    ChrTalk(
        0x8,
        (
            "#1603F#11P嘁，还真有点本事啊……\x02\x03",

            "实在是没想到，竟然会\x01",
            "被你压制到如此地步……\x02",
        )
    )

    CloseMessageWindow()

    #N0491
    NpcTalk(
        0x9,
        "穿红色外套的青年",
        "#5P瓦、瓦鲁多大哥……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #N0492
    NpcTalk(
        0xB,
        "穿红色外套的青年",
        (
            "你小子……！\x01",
            "竟敢对瓦鲁多大哥……！\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x8,
        (
            "#1600F#11P住嘴……\x01",
            "我只是脚底滑了一下而已。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_9781():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_9781)
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
            "#6P#0001F唔……\x01",
            "（这家伙……是怪物吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x8,
        (
            "#1604F#12P哼哼，真是一场\x01",
            "不错的热身运动啊。\x02\x03",

            "其实我是想拿出真本事，\x01",
            "和你战个痛快的……\x02\x03",

            "#1602F不过，和那家伙的决战日期已经临近了，\x01",
            "这次就放过你，到此为止好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9881")

    label("loc_9881")


    #C0496
    ChrTalk(
        0x101,
        (
            "#6P#0006F呼……\x01",
            "这还真是多谢了啊。\x02",
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
            "#6P#0001F那么……\x01",
            "可以把情况告诉我们了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x8,
        "#1602F#12P哼，好吧──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(14700, 1100, 0, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(26500, 0)

    def lambda_994A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_994A)

    def lambda_9957():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9957)

    def lambda_9964():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9964)

    def lambda_9971():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9971)

    def lambda_997E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_997E)

    def lambda_998B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_998B)

    def lambda_9998():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_9998)
    SetChrChipByIndex(0x8, 0x7)
    SetChrSubChip(0x8, 0x0)

    def lambda_99AD():
        OP_96(0xFE, 0x4268, 0x3E8, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_99AD)
    Sleep(500)

    def lambda_99CA():
        OP_96(0xFE, 0x2A30, 0x0, 0xFFFFFD44, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_99CA)
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
            "#1603F#12P──事情发生在五天前的晚上。\x02\x03",

            "#1601F我们的一名成员\x01",
            "被那群蓝衣小子暗算了。\x02\x03",

            "就在离这里不远的地方。\x02",
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
        "#0005F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x102,
        "#0105F然、然后呢……！？\x02",
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x8,
        (
            "#1602F#12P哼，他们声称自己的人\x01",
            "也遭到了类似的暗算……\x02\x03",

            "但在我看来，\x01",
            "根本就是在找借口推脱责任而已。\x02\x03",

            "#1603F我们剑蛇帮可是\x01",
            "光明正大的武斗派……\x02\x03",

            "#1601F像偷袭暗算这种肮脏卑鄙的事，\x01",
            "我们怎么可能会去做？\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x101,
        (
            "#0003F…………………………………\x02\x03",

            "#0001F那个，遭到偷袭的那位成员，\x01",
            "伤势大概有多严重呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x8,
        (
            "#1603F#12P被打到骨折，已经住院了，\x01",
            "想彻底痊愈的话，大约需要一个月左右吧。\x02\x03",

            "哼，不过和蓝衣小子那边的人不同，\x01",
            "他受袭之后并没有立刻失去意识……\x02\x03",

            "#1601F但光从表面伤势来看，\x01",
            "伤得也许比那边的人更重呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        "#0008F是吗……\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x104,
        (
            "#0301F不过，你们能确定是被\x01",
            "圣书会的人暗算的吗？\x02\x03",

            "既然他当时意识清醒，\x01",
            "应该可以提供目击证言吧……\x02",
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

            "难道，没有看到凶手吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x8,
        (
            "#1603F#12P……算是吧。\x02\x03",

            "#1601F不过，肯定是那些蓝衣服的\x01",
            "家伙干的，绝不会有错。\x02\x03",

            "因为他是被突然从远处飞射\x01",
            "而来的石弹打伤的。\x02",
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
        "#0101F石弹……\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x103,
        (
            "#0201F就是圣书会的人\x01",
            "使用的那种弹弓的子弹吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x8,
        (
            "#1603F#12P嗯，就是那个。\x02\x03",

            "被击中之后倒地不起，\x01",
            "接着就被冲上来的人狂殴了一顿。\x02\x03",

            "#1601F然后好像就失去意识了……\x01",
            "犯人究竟是谁，也就不必多说了吧？\x02",
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
            "#1604F#12P哼哼，就这么多了。\x02\x03",

            "#1600F──就如我刚才所说的，\x01",
            "这些细枝末节的情况根本无关紧要。\x02\x03",

            "反正我一定要和蓝衣服的小子们……\x01",
            "还有那个家伙做个彻底了结。\x01",
            "至于其它事情，我可不管。\x02\x03",

            "#1602F如果你们想妨碍我，倒也无所谓。\x02\x03",

            "因为那样的话，我就会把你们和那些\x01",
            "蓝衣服的小子们一起击溃……\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        (
            "#0003F……挑衅对我们是没用的。\x02\x03",

            "#0000F感谢你协助我们进行调查，\x01",
            "这些证言很有参考价值。\x02\x03",

            "如果有什么发现，\x01",
            "会再次与你们联络的。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x8,
        (
            "#1604F#12P哼……\x01",
            "算了，随你们高兴吧。\x02",
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

    # Function_32_91EA end

    def Function_33_A362(): pass

    label("Function_33_A362")

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
            "扬声器的背面\x01",
            "贴着卡片。\x02",
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
            "#11P#0005F有了……！\x01",
            "果然是这里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x103,
        (
            "#6P#0200F『９－７－１４－９－１９』。\x01",
            "如果这是指字母顺序的话，\x01",
            "答案就是鬼火（ＩＧＮＩＳ）了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x104,
        (
            "#5P#0300F嗯，话说回来，\x01",
            "『发出喑哑响声』，\x01",
            "指的应该就是这个了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x102,
        (
            "#6P#0100F不过，还是没有发现\x01",
            "被盗的雕像啊。\x02\x03",

            "……罗伊德，卡片上\x01",
            "写着什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    #C0520
    ChrTalk(
        0x101,
        "#11P#0003F啊，我看看……\x02",
    )

    CloseMessageWindow()

    def lambda_A5CB():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A5CB)

    def lambda_A5D8():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A5D8)
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
            " 　　　下一把钥匙在 　　　\x01",
            "      通向白隼的大门\x01",
            "　　   时间搬离之地　　\x02",
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
            "#11P#0006F通向白隼……\x01",
            "又、又是一道难题啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x102,
        (
            "#6P#0100F说起白隼，\x01",
            "那是缔结了《互不侵犯条约》的利贝尔\x01",
            "王国的国鸟，非常有名的。\x02\x03",

            "我想，这提示肯定与利贝尔有关，\x01",
            "这点应该可以确定。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x104,
        (
            "#5P#0303F……该不会是\x01",
            "要让我们跑到利贝尔去吧？\x02",
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
        "#11P#0012F不、不可能吧……\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x103,
        (
            "#6P#0203F……如果是那样的话，\x01",
            "我们也就无能为力了。\x02\x03",

            "#0200F从至今为止的模式来看，\x01",
            "每一道谜题的难度都保持在\x01",
            "我们可以解开的范围内，这次应该也是……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x8,
        (
            "#2P#1601F喂，你们几个……\x01",
            "在干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A8E3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A8E3)

    def lambda_A8F0():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A8F0)

    def lambda_A8FD():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A8FD)

    def lambda_A90A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A90A)
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
            "#0000F啊，抱歉，\x01",
            "打扰你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x103,
        (
            "#0203F我们的事已经办完了，\x01",
            "请不用介意。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x4)

    def lambda_A9B9():
        OP_95(0xFE, 14200, 1000, 580, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A9B9)

    #C0530
    ChrTalk(
        0x8,
        (
            "#1607F啊……？\x01",
            "你们这是在挑衅吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x104,
        (
            "#0300F哈哈哈……在打起来之前，\x01",
            "还是赶快撤退吧。\x02",
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

    # Function_33_A362 end

    SaveToFile()

Try(main)
