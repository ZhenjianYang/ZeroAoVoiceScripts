from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0220.bin",                # FileName
        "c0220",                    # MapName
        "c0220",                    # Location
        0x000D,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 13, 0, 8, 0, 9],
    )

    BuildStringList((
        "c0220",                  # 0
        "イアン弁護士",           # 1
        "イアン弁護士",           # 2
        "ピート",                 # 3
        "商工会役員",             # 4
        "ハロルド",               # 5
    ))

    AddCharChip((
        "chr/ch05900.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch05902.itc",                   # 02
        "chr/ch27602.itc",                   # 03
        "chr/ch09302.itc",                   # 04
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
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
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

    DeclNpc(0,       0,       0,       0,    385,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4510,    1169,    15779,   180,  341,  0x0, 0,   2,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(12869,   1000,    4809,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2259,    140,     5500,    90,   469,  0x0, 0,   3,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(2259,    140,     5500,    90,   389,  0x0, 0,   4,   0,   255, 255, 0,   17,  255,  0)

    DeclActor(14350,   1000,    -70,     2000,    14350,   2500,    -70,     0x007C, 0,  19, 0x0000)

    ScpFunction((
        "Function_0_228",          # 00, 0
        "Function_1_2E0",          # 01, 1
        "Function_2_355",          # 02, 2
        "Function_3_380",          # 03, 3
        "Function_4_3D8",          # 04, 4
        "Function_5_430",          # 05, 5
        "Function_6_488",          # 06, 6
        "Function_7_4E0",          # 07, 7
        "Function_8_51A",          # 08, 8
        "Function_9_839",          # 09, 9
        "Function_10_88C",         # 0A, 10
        "Function_11_FA4",         # 0B, 11
        "Function_12_3554",        # 0C, 12
        "Function_13_36FE",        # 0D, 13
        "Function_14_3817",        # 0E, 14
        "Function_15_4E9B",        # 0F, 15
        "Function_16_4FA9",        # 10, 16
        "Function_17_505A",        # 11, 17
        "Function_18_51D5",        # 12, 18
        "Function_19_56FE",        # 13, 19
        "Function_20_5730",        # 14, 20
        "Function_21_7771",        # 15, 21
        "Function_22_77C6",        # 16, 22
        "Function_23_781B",        # 17, 23
        "Function_24_7870",        # 18, 24
        "Function_25_78C5",        # 19, 25
        "Function_26_97AB",        # 1A, 26
    ))


    def Function_0_228(): pass

    label("Function_0_228")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_268"),
        (1, "loc_274"),
        (2, "loc_280"),
        (3, "loc_28C"),
        (4, "loc_298"),
        (5, "loc_2A4"),
        (6, "loc_2B0"),
        (SWITCH_DEFAULT, "loc_2BC"),
    )


    label("loc_268")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_274")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_280")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_28C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_298")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2A4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2DF")

    Return()

    # Function_0_228 end

    def Function_1_2E0(): pass

    label("Function_1_2E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_354")
    OP_95(0xFE, 6850, 1000, 14410, 2000, 0x0)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 10890, 1000, 14410, 2000, 0x0)
    OP_95(0xFE, 10890, 1000, 17280, 2000, 0x0)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, 10890, 1000, 14410, 2000, 0x0)
    Jump("Function_1_2E0")

    label("loc_354")

    Return()

    # Function_1_2E0 end

    def Function_2_355(): pass

    label("Function_2_355")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37F")
    OP_94(0xFE, 0x2684, 0x321E, 0x32BE, 0x3D86, 0x3E8)
    Sleep(300)
    Jump("Function_2_355")

    label("loc_37F")

    Return()

    # Function_2_355 end

    def Function_3_380(): pass

    label("Function_3_380")


    def lambda_385():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_385)

    def lambda_396():
        OP_95(0xFE, 3850, 30, 680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_396)
    WaitChrThread(0x101, 1)

    def lambda_3B4():
        OP_95(0xFE, 5780, 30, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B4)
    WaitChrThread(0x101, 1)
    Sleep(100)
    OP_93(0x101, 0x0, 0x3E8)
    Return()

    # Function_3_380 end

    def Function_4_3D8(): pass

    label("Function_4_3D8")


    def lambda_3DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3DD)

    def lambda_3EE():
        OP_95(0xFE, 3800, 30, -350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EE)
    WaitChrThread(0x102, 1)

    def lambda_40C():
        OP_95(0xFE, 4820, 30, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40C)
    WaitChrThread(0x102, 1)
    Sleep(100)
    OP_93(0x102, 0x0, 0x3E8)
    Return()

    # Function_4_3D8 end

    def Function_5_430(): pass

    label("Function_5_430")


    def lambda_435():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_435)

    def lambda_446():
        OP_95(0xFE, 2990, 30, 650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_446)
    WaitChrThread(0x103, 1)

    def lambda_464():
        OP_95(0xFE, 3680, 30, 1810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_464)
    WaitChrThread(0x103, 1)
    Sleep(100)
    OP_93(0x103, 0x0, 0x3E8)
    Return()

    # Function_5_430 end

    def Function_6_488(): pass

    label("Function_6_488")


    def lambda_48D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_48D)

    def lambda_49E():
        OP_95(0xFE, 1820, 30, -550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_49E)
    WaitChrThread(0x104, 1)

    def lambda_4BC():
        OP_95(0xFE, 2840, 30, 2150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4BC)
    WaitChrThread(0x104, 1)
    Sleep(100)
    OP_93(0x104, 0x0, 0x3E8)
    Return()

    # Function_6_488 end

    def Function_7_4E0(): pass

    label("Function_7_4E0")


    def lambda_4E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4E5)

    def lambda_4F6():
        OP_95(0xFE, 2910, 30, 430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F6)
    WaitChrThread(0xFE, 1)
    Sleep(100)
    OP_93(0xFE, 0x0, 0x3E8)
    Return()

    # Function_7_4E0 end

    def Function_8_51A(): pass

    label("Function_8_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_554")
    SetChrPos(0x8, 7200, 1000, 18560, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 6750, 1020, 14000, 270)
    Jump("loc_7EC")

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_57D")
    SetChrPos(0x9, 6600, 140, 5500, 270)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_7EC")

    label("loc_57D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_5B7")
    SetChrPos(0x8, 1930, 1020, 17480, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 930, 1000, 16580, 0)
    Jump("loc_7EC")

    label("loc_5B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5DC")
    SetChrPos(0xA, 11280, 1000, 14370, 0)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_7EC")

    label("loc_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5FB")
    SetChrPos(0xA, 5010, 1020, 12770, 0)
    Jump("loc_7EC")

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_60E")
    SetChrFlags(0x9, 0x80)
    Jump("loc_7EC")

    label("loc_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_648")
    SetChrPos(0x8, 5270, 1020, 12800, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 4180, 1020, 12800, 90)
    Jump("loc_7EC")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_66C")
    SetChrPos(0x9, 6600, 140, 5500, 270)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_7EC")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_690")
    SetChrPos(0x9, 6600, 140, 5500, 270)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_7EC")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6AF")
    SetChrPos(0xA, 6020, 1020, 15940, 270)
    Jump("loc_7EC")

    label("loc_6AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6BD")
    Jump("loc_7EC")

    label("loc_6BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6DC")
    SetChrPos(0xA, 5130, 1020, 12990, 0)
    Jump("loc_7EC")

    label("loc_6DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_716")
    SetChrPos(0x8, 1930, 1020, 17480, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 13280, 1000, -1500, 180)
    Jump("loc_7EC")

    label("loc_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_724")
    Jump("loc_7EC")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_732")
    Jump("loc_7EC")

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_740")
    Jump("loc_7EC")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_77A")
    SetChrPos(0x8, 5270, 1020, 12800, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 4180, 1020, 12800, 90)
    Jump("loc_7EC")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7AA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A5")
    SetChrFlags(0x9, 0x80)

    label("loc_7A5")

    Jump("loc_7EC")

    label("loc_7AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7B8")
    Jump("loc_7EC")

    label("loc_7B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_7CB")
    SetChrFlags(0xA, 0x80)
    Jump("loc_7EC")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7DE")
    SetChrFlags(0x9, 0x80)
    Jump("loc_7EC")

    label("loc_7DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7EC")
    SetChrFlags(0x9, 0x80)

    label("loc_7EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_807")
    Event(0, 26)
    Jump("loc_838")

    label("loc_807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_822")
    SetMapFlags(0x10000000)
    Event(0, 20)
    Jump("loc_838")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_838")
    SetMapFlags(0x10000000)
    Event(0, 25)

    label("loc_838")

    Return()

    # Function_8_51A end

    def Function_9_839(): pass

    label("Function_9_839")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_852")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_858")

    label("loc_852")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_874")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_88B")

    label("loc_874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_88B")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_88B")

    label("loc_88B")

    Return()

    # Function_9_839 end

    def Function_10_88C(): pass

    label("Function_10_88C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_951")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AA")
    Call(0, 18)
    Jump("loc_94C")

    label("loc_8AA")


    #C0001
    ChrTalk(
        0xFE,
        (
            "#2200Fルバーチェ商会に\x01",
            "関する問い合わせは\x01",
            "私の方で引き受けよう。\x02\x03",

            "しばらくは混乱が広がるのを\x01",
            "抑えられるだろう。\x02\x03",

            "だが、持って１日だ……\x01",
            "君たちも急ぎたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94C")

    Jump("loc_FA0")

    label("loc_951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_95F")
    Jump("loc_FA0")

    label("loc_95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_A7A")

    #C0002
    ChrTalk(
        0xFE,
        (
            "#2200F私はこれから\x01",
            "仕事があるんだが……\x01",
            "黒月の一件はやはり気になるね。\x02\x03",

            "#2203F異常な身体能力だったという話、\x01",
            "そういえば『教団』の件でも\x01",
            "耳にしたような気がしてね……\x02\x03",

            "#2200Fハハ、まあ気のせいだろう。\x01",
            "変な話を聞かせてしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        "#0208F………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_FA0")

    label("loc_A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A88")
    Jump("loc_FA0")

    label("loc_A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A96")
    Jump("loc_FA0")

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEE")

    #C0004
    ChrTalk(
        0x8,
        (
            "#2200Fやあ、君たち。\x01",
            "ハロルドさんから話は聞いたよ。\x02\x03",

            "無事、コリン君を\x01",
            "保護してくれたそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0012Fええ、何とか。\x02\x03",

            "#0005Fそう言えば……イアン先生。\x02\x03",

            "#0000Fハロルドさんが昔お世話になった\x01",
            "先生というのは、もしかして……？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#2202Fはは、単に債務整理の\x01",
            "手伝いをしたというだけだよ。\x02\x03",

            "#2203F当時彼は、マフィアの息が掛かった\x01",
            "悪徳金融業者に引っかかっていてね。\x02\x03",

            "#2200Fあまりに不当な金利だったから\x01",
            "少々、力を貸したというわけなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        "#0100Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x104,
        (
            "#0306Fしかし、そんな所にも\x01",
            "ルバーチェの影アリかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        "#0211F本当にロクな事をしてませんね……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D98")

    label("loc_CEE")


    #C0010
    ChrTalk(
        0xFE,
        (
            "#2200Fええと、財布は持ったな……\x02\x03",

            "今日が最終日だからね。\x01",
            "ピート君と回ろうと\x01",
            "思っているんだよ。\x02\x03",

            "明日からはまだ仕事が山積みだ。\x01",
            "たまには英気を\x01",
            "養っておかないとねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D98")

    Jump("loc_FA0")

    label("loc_D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA1")

    #C0011
    ChrTalk(
        0x8,
        (
            "#2200Fはあ、いかんな。\x01",
            "必要な資料が見つからないよ。\x02\x03",

            "#2203F今日も仕事があるというのに\x01",
            "このままでは遅れてしまう。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#0000Fイアン先生、お忙しそうですね。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#2200Fうむ……来月は記念祭だからね。\x01",
            "色々相談事も増えているんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F11")

    label("loc_EA1")


    #C0014
    ChrTalk(
        0x8,
        (
            "#2200F私はこういった整理が\x01",
            "いまいち得意でなくてねぇ。\x02\x03",

            "ふう……やはりピート君に\x01",
            "一緒に探してもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F11")

    Jump("loc_FA0")

    label("loc_F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_FA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F31")
    Call(0, 12)
    Jump("loc_FA0")

    label("loc_F31")

    TurnDirection(0x8, 0xA, 0)

    #C0015
    ChrTalk(
        0xFE,
        (
            "#2203Fそのう……\x01",
            "そんなこともあったかな。\x02\x03",

            "#2200Fああ、わ、私が悪かったよ。\x01",
            "許してくれ、ピート君。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA0")

    TalkEnd(0xFE)
    Return()

    # Function_10_88C end

    def Function_11_FA4(): pass

    label("Function_11_FA4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1038")
    Jump("loc_1082")

    label("loc_1038")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1058")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1082")

    label("loc_1058")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1078")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1082")

    label("loc_1078")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1082")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_10B5")
    Jump("loc_354C")

    label("loc_10B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1177")

    #C0016
    ChrTalk(
        0xFE,
        (
            "#2200F今後も失踪者の相談があれば\x01",
            "セルゲイ君に連絡を回しておくよ。\x02\x03",

            "#2203F……しかし君たちの反応を見るに\x01",
            "ただの行方不明事件ではないようだな。\x02\x03",

            "ふむ……まさかとは思うんだが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354C")

    label("loc_1177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1671")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B5")

    #C0017
    ChrTalk(
        0xFE,
        (
            "#2200Fおや、今日は朝から早いな。\x02\x03",

            "何か困った事でもあったのかね？\x01",
            "相談なら乗るが……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0008Fいえ、あの。\x02\x03",

            "#0001Fイアン先生、実は\x01",
            "《黒月》の事務所が\x01",
            "襲撃されたそうなんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0019
    ChrTalk(
        0xFE,
        (
            "#2205Fなんと……\x01",
            "それは本当かね！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FD")

    #C0020
    ChrTalk(
        0x104,
        (
            "#0300F俺たちもこれから\x01",
            "見に行く所なんスけど。\x02\x03",

            "ルバーチェの連中が\x01",
            "ついにやっちまったって\x01",
            "感じッスね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1382")

    label("loc_12FD")


    #C0021
    ChrTalk(
        0x104,
        (
            "#0300F俺たちも少し\x01",
            "様子を見てきたトコっすけど。\x02\x03",

            "重機関銃まで持ち出して、\x01",
            "ルバーチェの連中もついに\x01",
            "やっちまったって感じッスね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1382")


    #C0022
    ChrTalk(
        0xFE,
        (
            "#2203Fううむ、あんな市街地で……\x02\x03",

            "#2201Fそれに……どうも腑に落ちないな……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0023
    ChrTalk(
        0xFE,
        (
            "#2201Fルバーチェの行動だよ。\x02\x03",

            "ライバルである黒月を\x01",
            "襲うのは分かるが、\x01",
            "計画的でないというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#0000Fそうですね……\x01",
            "それは自分も感じていました。\x02\x03",

            "両マフィアの総力戦、という\x01",
            "わけでもなかったようですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "#2201Fふむ……ともかく\x01",
            "こちらも気をつけておくよ。\x02\x03",

            "そんな事件があったとあれば\x01",
            "相談に来る会社も多そうだ。\x01",
            "何か判るかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#0100Fすみません、いつも\x01",
            "お世話になってしまって。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 6)
    Jump("loc_166C")

    label("loc_15B5")


    #C0027
    ChrTalk(
        0xFE,
        (
            "#2203F市街地で襲撃事件を起こすとは……\x01",
            "どうも腑に落ちないな……\x02\x03",

            "#2201Fともかく、治安の悪化を\x01",
            "気にしている企業も多いし\x01",
            "黒月側の報復の可能性もある……\x02\x03",

            "こちらも気をつけておくよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_166C")

    Jump("loc_354C")

    label("loc_1671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6F")

    #C0028
    ChrTalk(
        0xFE,
        "#2200Fおっと、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0000Fイアン先生、ご無沙汰しています。\x02\x03",

            "……先生は最近輪を掛けて\x01",
            "お忙しそうですね。\x01",
            "今日もお出掛けですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "#2201Fああ、最近マフィア絡みの\x01",
            "トラブルが増えているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        "#0105Fマフィア……ルバーチェの？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "#2203Fああ、それも\x01",
            "凶暴なものが多くてね……\x02\x03",

            "地上げや歓楽街での用心棒……\x02\x03",

            "#2200Fそういった“ビジネス”の最中に\x01",
            "突発的に民間人をリンチにして\x01",
            "病院送りにしてしまうといった話だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#0301Fチッ……マフィアなんざ\x01",
            "要は恐喝のプロだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "#2201Fああ、それはそうなんだが……\x01",
            "どうも様子がおかしいというか……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0035
    ChrTalk(
        0xFE,
        (
            "#2201F君達は市街の巡回かな？\x01",
            "それなら、支援課の方でも\x01",
            "気を付けておいてくれないか。\x02\x03",

            "#2203F大抵のケースでは\x01",
            "遊撃士の諸君が\x01",
            "駆けつけてはいるんだが。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1988")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1988")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19AE")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_19AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D4")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_19D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19FA")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_19FA")

    Sleep(1000)

    #C0036
    ChrTalk(
        0x101,
        (
            "#0000Fそ、そうですね。\x01",
            "なるべく気を配っておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x109,
        (
            "#0500F（支援課の皆さんも\x01",
            "  大変ですね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 5)
    Jump("loc_1B6B")

    label("loc_1A6F")


    #C0038
    ChrTalk(
        0xFE,
        (
            "#2200F今日は恐喝に遭ったという\x01",
            "会社の社長さんに会いに行くんだ。\x02\x03",

            "#2203Fその他にも何件か回るから……\x01",
            "うーん、夕方には\x01",
            "戻りたい所なんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#0000F（本当にお忙しそうだな……）\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#0100F（私達も市街の様子に\x01",
            "  気を配っておいた方がよさそうね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6B")

    Jump("loc_354C")

    label("loc_1B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_1B81")
    Call(0, 13)
    Jump("loc_354C")

    label("loc_1B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1E7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E15")

    #C0041
    ChrTalk(
        0xFE,
        (
            "#2205Fおや、ロイド君か。\x01",
            "今日は皆と一緒ではないのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#0002Fええ、一時別行動でして……\x02\x03",

            "#0000F（そうだ、イアン先生にも\x01",
            "  聞いてみよう。）\x02",
        )
    )

    CloseMessageWindow()

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0044
    ChrTalk(
        0xFE,
        (
            "#2201Fふむ、あのハロルドさんの\x01",
            "お子さんが迷子とは……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFE)

    #C0045
    ChrTalk(
        0xFE,
        (
            "#2203Fすまないな……\x01",
            "パレードの前から\x01",
            "相談の方が来ていてね。\x02\x03",

            "#2201F外の様子までは\x01",
            "見ていなかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#0003Fそうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "#2203F……奥さんも随分と\x01",
            "不安がっているだろう。\x02\x03",

            "#2201Fロイド君。\x01",
            "どうか見つけてあげてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#0005Fは、はい。\x01",
            "（何か事情を知ってるのかな？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    Jump("loc_1E79")

    label("loc_1E15")


    #C0049
    ChrTalk(
        0xFE,
        (
            "#2203F奥さんも随分と\x01",
            "不安がっているだろう。\x02\x03",

            "#2201Fロイド君。\x01",
            "どうか見つけてあげてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E79")

    Jump("loc_354C")

    label("loc_1E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1E8F")
    Call(0, 13)
    Jump("loc_354C")

    label("loc_1E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_20F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2085")

    #C0050
    ChrTalk(
        0xFE,
        (
            "#2203Fうーむ、昨晩は\x01",
            "調子に乗って\x01",
            "飲みすぎてしまった……\x02\x03",

            "今日は仕事があるというのに\x01",
            "気分が優れないよ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x104)

    #C0051
    ChrTalk(
        0x104,
        (
            "#0303F（警備隊時代に本物の熊と\x01",
            "  出くわした事があるんだが……）\x02\x03",

            "#0300F（先生が具合悪そうにしてっと\x01",
            "  本当に熊みたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FD1")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1FD1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF7")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1FF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_201D")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_201D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2043")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2043")

    Sleep(1000)

    #C0052
    ChrTalk(
        0x101,
        (
            "#0006F（ランディ、それは\x01",
            "  さすがに失礼だぞ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20F4")

    label("loc_2085")


    #C0053
    ChrTalk(
        0xFE,
        (
            "#2203Fうーむ、昨晩は\x01",
            "調子に乗って\x01",
            "飲みすぎてしまった……\x02\x03",

            "今日は仕事があるというのに\x01",
            "気分が優れないよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20F4")

    Jump("loc_354C")

    label("loc_20F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2178")

    #C0054
    ChrTalk(
        0xFE,
        (
            "#2200Fええと、原稿はこれでよし……\x02\x03",

            "今日は午後から\x01",
            "偉い人たちに呼ばれていてね。\x02\x03",

            "ふう、さすがに緊張するよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354C")

    label("loc_2178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2558")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2491")

    #C0055
    ChrTalk(
        0xFE,
        (
            "#2200Fおお、君たちか。\x01",
            "記念祭の見回りかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#0000Fええ、そんな所です。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "#2200Fふむふむ、そうか。\x02\x03",

            "市長暗殺を食い止めた\x01",
            "ヒーロー達が見回りとくれば\x01",
            "市民も安心だねえ。\x02",
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

    #C0058
    ChrTalk(
        0x104,
        "#0302Fいやあ、さすがにそいつは……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        "#0203F……こっ恥ずかしいです。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0012F先生、へんなおだて方を\x01",
            "しないで下さいよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "#2202Fはは、本当のことじゃないか。\x01",
            "謙遜することはないと思うがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#0100Fそれで……先生は\x01",
            "記念祭は回らないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "#2200Fああ、うむ、一応\x01",
            "仕事なども入っているんだ。\x02\x03",

            "#2203Fクロスベルには国際企業も多い。\x01",
            "創立記念祭だからといって\x01",
            "休みにならない会社もあるからね。\x02\x03",

            "#2200Fでもまあ、暇を見て\x01",
            "回ってみようと思っているよ。\x01",
            "折角のお祭りだからねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 6)
    Jump("loc_2553")

    label("loc_2491")


    #C0064
    ChrTalk(
        0xFE,
        (
            "#2200F一応仕事も入っていてね。\x01",
            "事務所を休むわけにはいかないんだ。\x02\x03",

            "でもまあ、暇を見て\x01",
            "回ってみようと思っているよ。\x02\x03",

            "#2202F折角のお祭りだし、\x01",
            "ピート君もたまには\x01",
            "遊びに行きたいだろうからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2553")

    Jump("loc_354C")

    label("loc_2558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2790")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2725")

    #C0065
    ChrTalk(
        0xFE,
        (
            "#2200Fおお、君たちか……\x02\x03",

            "#2201F脅迫状の調査は\x01",
            "捜査一課に移管されたそうだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0066
    ChrTalk(
        0x102,
        "#0105Fええ、よくご存知ですね……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "#2200Fさっきダドリー君が訪ねてきてね。\x02\x03",

            "銀と黒月の最新情報を\x01",
            "確認していったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#0001Fそ、そうでしたか。\x02\x03",

            "#0003F……捜査一課も\x01",
            "早速動いてるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0303Fま、気にしても仕方ねえ。\x01",
            "こっちも好きに\x01",
            "動かせてもらおうぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 6)
    Jump("loc_278B")

    label("loc_2725")


    #C0070
    ChrTalk(
        0xFE,
        (
            "#2201F劇団アルカンシェルに\x01",
            "危機迫る、か……\x02\x03",

            "#2203Fううむ、ただのいたずらで\x01",
            "あればいいんだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_278B")

    Jump("loc_354C")

    label("loc_2790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_287F")

    #C0071
    ChrTalk(
        0xFE,
        (
            "#2203F《銀》と《黒月貿易公司》……\x01",
            "確かに両者に関係がないとは\x01",
            "言い切れないだろう。\x02\x03",

            "#2201Fしかし黒月貿易公司の\x01",
            "支社長は相当のキレ者だと思うよ。\x02\x03",

            "彼らの本体は\x01",
            "巨大な勢力を誇る犯罪組織でもある。\x01",
            "くれぐれも気をつけたまえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354C")

    label("loc_287F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2B63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB8")

    #C0072
    ChrTalk(
        0xFE,
        (
            "#2200Fおお、君たちか。\x01",
            "久しぶりだね。\x02\x03",

            "話は色々聞いているが\x01",
            "頑張っているようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#0000Fあはは……先生ほどじゃ\x01",
            "ないと思いますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#0301F例のとっ捕まえたルバーチェも\x01",
            "すぐに保釈されちまったしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "#2203Fうむ……\x01",
            "マフィアの問題は根深い。\x01",
            "ことにこのクロスベル市ではね。\x02\x03",

            "#2200Fだが、君達の活躍は\x01",
            "少なからず市民の心に\x01",
            "光をもたらしたと思うよ。\x02\x03",

            "かく言う私も\x01",
            "目が覚める思いだったからねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        (
            "#0100F先生……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "#2200Fはは、礼を言うのは\x01",
            "こちらの方だ。\x02\x03",

            "特務支援課──\x01",
            "どうか頑張ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 5)
    Jump("loc_2B5E")

    label("loc_2AB8")


    #C0078
    ChrTalk(
        0xFE,
        (
            "#2200Fセルゲイ君から\x01",
            "初めて話を聞いたときは\x01",
            "私も半信半疑だったが……\x02\x03",

            "特務支援課──\x01",
            "どうして素晴らしい活躍じゃないか。\x02\x03",

            "どうかこれからも\x01",
            "頑張ってくれたまえよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B5E")

    Jump("loc_354C")

    label("loc_2B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2CB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C39")

    #C0079
    ChrTalk(
        0xFE,
        (
            "#2200F私はクロスベル市を中心に\x01",
            "仕事を請け負っているのだが……\x02\x03",

            "最近は好景気のせいか、\x01",
            "アルモリカやマインツへ向かう\x01",
            "商人さんも増えているようだね。\x02\x03",

            "お陰で出張が多くなってしまったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CB1")

    label("loc_2C39")


    #C0080
    ChrTalk(
        0xFE,
        (
            "#2200F私は現場主義なのでね、\x01",
            "依頼に関係する現場は\x01",
            "必ず見ることにしているんだ。\x02\x03",

            "お陰で出張が多くなってしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CB1")

    Jump("loc_354C")

    label("loc_2CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_32E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3167")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0081
    ChrTalk(
        0xFE,
        (
            "#2200Fおや、支援課の諸君か。\x02\x03",

            "また何か困ったことでも\x01",
            "あったのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0000Fあ、いえ、そういう\x01",
            "わけじゃないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#0100Fでもロイド、一応話だけでも\x01",
            "お聞きしてみたらどう？\x01",
            "情報が掴めるかも知れないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "#2200Fああ、その通りだよ！\x02\x03",

            "物事はまずは相談。\x01",
            "何でも聞いてくれたまえ！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#0000Fははは……それじゃあ\x01",
            "少し伺いたいんですが……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは各地に現れている\x01",
            "狼型魔獣について説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0087
    ChrTalk(
        0xFE,
        (
            "#2200Fふむ、狼型魔獣か……\x01",
            "確かに耳にした事はあるが……\x02\x03",

            "#2203Fすまない、私の専門外だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        "#0300Fはは、やっぱそうっすよね。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x103,
        (
            "#0200Fちなみに、その\x01",
            "耳にした話というのは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "#2200Fああ……\x02\x03",

            "マインツの商人の方から\x01",
            "商売が出来ずに困っているから\x01",
            "相談したいという話があったんだ。\x02\x03",

            "#2203Fしかし、その後の警備隊の\x01",
            "見回りのお陰で現れなくなったらしい。\x01",
            "結局相談は受けずじまいだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#0005Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x102,
        (
            "#0101F報告書の内容を裏付けるものね。\x01",
            "新しい被害も出ていないみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#0001Fああ、予定通り\x01",
            "アルモリカ村の調査から始めよう。\x02\x03",

            "#0000F先生、ありがとうございました。\x01",
            "参考になりましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "#2200Fいやいや、こちらこそ\x01",
            "大した役に立てなくてすまない。\x02\x03",

            "また何かあれば来てくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 0)
    Jump("loc_32DE")

    label("loc_3167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3270")

    #C0095
    ChrTalk(
        0xFE,
        (
            "#2201Fすまない、魔獣については\x01",
            "私の専門外だよ。\x02\x03",

            "#2203Fしかしクロスベルの各地に\x01",
            "現れているとは妙な話だね。\x02\x03",

            "ただの魔獣が、それほどに\x01",
            "移動を繰り返すものだろうか……\x02\x03",

            "#2200F……ともかく、\x01",
            "調査の方は頑張ってくれたまえ。\x01",
            "陰ながら応援しているよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_32DE")

    label("loc_3270")


    #C0096
    ChrTalk(
        0xFE,
        (
            "#2200Fすまない、魔獣については\x01",
            "私の専門外だよ。\x02\x03",

            "調査の方は頑張ってくれたまえ。\x01",
            "陰ながら応援しているよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32DE")

    Jump("loc_354C")

    label("loc_32E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_3543")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_348F")

    #C0097
    ChrTalk(
        0xFE,
        (
            "#2200F私の話がヒントに\x01",
            "なったのなら幸いだよ。\x02\x03",

            "また何かあれば\x01",
            "遠慮なく訪ねてきてくれたまえ。\x01",
            "力になれるかもしれない。\x02\x03",

            "#2203F……いや、私が力になれるか\x01",
            "どうか判らなくても、\x01",
            "まずは相談に来てくれたまえ！\x02\x03",

            "#2201F悩んでいるだけでは解決しない……\x01",
            "法律問題とは往々にして\x01",
            "そういったものだからね！\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#0012Fは、はあ……\x01",
            "それじゃ機会があれば\x01",
            "お言葉に甘えさせて貰います。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        "#2202Fああ、待っているよ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_353E")

    label("loc_348F")


    #C0100
    ChrTalk(
        0xFE,
        (
            "#2210Fまた何かあれば\x01",
            "遠慮なく訪ねてきてくれたまえ。\x02\x03",

            "#2200F私が留守の場合は、助手の\x01",
            "ピート君に伝言してくれるといい。\x02\x03",

            "ピート君の事務能力は\x01",
            "私よりはるかに優秀だからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_353E")

    Jump("loc_354C")

    label("loc_3543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_354C")

    label("loc_354C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_FA4 end

    def Function_12_3554(): pass

    label("Function_12_3554")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0xA, 0x8, 0)

    #C0101
    ChrTalk(
        0xA,
        (
            "先生、先月のこの件で\x01",
            "報酬額が合いませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "#2200F……ああ、その方か。\x01",
            "財政状況が思わしくないので\x01",
            "報酬はまけてあげたのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        "えっ、またですか！？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "いい加減にしないと\x01",
            "赤字になっちゃいますよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#2205Fそ、その……\x02\x03",

            "#2203Fわ、私が悪かった。\x01",
            "許してくれピート君。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        (
            "僕に謝っても\x01",
            "仕方ありませんよ、先生！\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "だいだい先生は弁護士なのに\x01",
            "お金のことに疎すぎるんですッ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_12_3554 end

    def Function_13_36FE(): pass

    label("Function_13_36FE")

    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xB, 0x0)

    #C0108
    ChrTalk(
        0xB,
        (
            "ええ、出店の売り上げが\x01",
            "盗まれてしまいまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "幸い事件は解決したのですが、\x01",
            "出店の方にも迷惑を掛けました。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xB,
        (
            "関係者には商工会から\x01",
            "何らかの補償をしたいと\x01",
            "思いましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "#2200Fなるほど、それは\x01",
            "誠実なご相談だ。\x02\x03",

            "ええ、喜んで相談に\x01",
            "乗らせていただきますよ。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_13_36FE end

    def Function_14_3817(): pass

    label("Function_14_3817")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39A1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_394A")

    #C0112
    ChrTalk(
        0x101,
        (
            "#0000Fあの、ちょっといいかな。\x02\x03",

            "ここで猫を\x01",
            "飼ってたりしないかな？\x01",
            "もしくは心当たりとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "仔猫……ですか？\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "あの皆さん、ここは\x01",
            "イアン先生の法律事務所ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "事務所で猫なんて\x01",
            "飼っていません。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x104,
        "#0300Fはは、だよなぁ……\x02",
    )

    CloseMessageWindow()
    OP_29(0x8, 0x1, 0x5)
    Jump("loc_399C")

    label("loc_394A")


    #C0117
    ChrTalk(
        0xFE,
        (
            "事務所で猫なんて\x01",
            "飼っていませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "今日は妙な事を\x01",
            "お聞きになりますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399C")

    Jump("loc_4E97")

    label("loc_39A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3A88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A3F")

    #C0119
    ChrTalk(
        0xFE,
        "何だか様子が変です……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "さっきから引っ切り無しに\x01",
            "通信が入ってくるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "ルバーチェ商会に\x01",
            "何かあったんでしょうか……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A83")

    label("loc_3A3F")


    #C0122
    ChrTalk(
        0xFE,
        "何だか嫌な胸騒ぎがします……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        "皆さん、どうかお気をつけて。\x02",
    )

    CloseMessageWindow()

    label("loc_3A83")

    Jump("loc_4E97")

    label("loc_3A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3AEB")

    #C0124
    ChrTalk(
        0xFE,
        "先生はこれからお仕事なんです。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "皆さんもお仕事ですか？\x01",
            "頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E97")

    label("loc_3AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3BC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B5E")

    #C0126
    ChrTalk(
        0xFE,
        (
            "あ、おはようございます。\x01",
            "先生に御用ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "丁度お仕事を\x01",
            "始められた所ですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BC2")

    label("loc_3B5E")


    #C0128
    ChrTalk(
        0xFE,
        (
            "せっせ……\x01",
            "朝の掃除は助手の勤めです。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "先生は無頓着なので\x01",
            "僕がしっかりしないといけません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BC2")

    Jump("loc_4E97")

    label("loc_3BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3D35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB6")

    #C0130
    ChrTalk(
        0xFE,
        "先生は今日もお仕事なんです。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "市内の会社を５つほど\x01",
            "回らなくちゃいけなくて……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)

    #C0132
    ChrTalk(
        0xFE,
        "ほら先生、早く支度をしてください！\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "#2203Fわ、分かっているよピート君。\x01",
            "その前に書類を書かせてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3D30")

    label("loc_3CB6")


    #C0134
    ChrTalk(
        0xFE,
        (
            "皆さん、すみません。\x01",
            "先生はこれからお出掛けなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "お急ぎのご用じゃなければ\x01",
            "また夕方にでもいらしてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D30")

    Jump("loc_4E97")

    label("loc_3D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3F52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED3")

    #C0136
    ChrTalk(
        0xFE,
        (
            "あれ、支援課の皆さん……\x01",
            "先生ならご出張ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "最近は外国からの相談も多いんです。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#0000Fそっか、残念だな……\x01",
            "キーアの保護について\x01",
            "一言相談したかったんだが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3E40")

    #C0139
    ChrTalk(
        0x102,
        (
            "#0100F仕方ないわね、先生は\x01",
            "また今度訪ねてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ECB")

    label("loc_3E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3E8B")

    #C0140
    ChrTalk(
        0x103,
        (
            "#0200F仕方ないですね、先生は\x01",
            "また今度訪ねてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ECB")

    label("loc_3E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3ECB")

    #C0141
    ChrTalk(
        0x104,
        (
            "#0300F仕方ねえな、先生は\x01",
            "また今度訪ねてみようぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ECB")

    SetScenarioFlags(0x0, 1)
    Jump("loc_3F4D")

    label("loc_3ED3")


    #C0142
    ChrTalk(
        0xFE,
        (
            "先生ならご出張ですよ。\x01",
            "最近は外国からの相談も多いんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "……記念祭からこちら\x01",
            "またお忙しくなってしまいました。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F4D")

    Jump("loc_4E97")

    label("loc_3F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3FEA")
    TurnDirection(0xA, 0x8, 0)

    #C0144
    ChrTalk(
        0xFE,
        "こほん……\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "先生、案内の\x01",
            "パンフレットを忘れています。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "出店を回る順番も\x01",
            "書き込んでありますから\x01",
            "間違えないで下さいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E97")

    label("loc_3FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_40D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_408D")

    #C0147
    ChrTalk(
        0xFE,
        (
            "今年のパレードは\x01",
            "とても華やかでしたね……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        "僕も少し驚いてしまいました。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "先生も今日くらいは\x01",
            "お仕事を休まれてもいいのに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_40CF")

    label("loc_408D")


    #C0150
    ChrTalk(
        0xFE,
        (
            "お仕事がなければ\x01",
            "先生にも休息を取って\x01",
            "頂きたい所なんですが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40CF")

    Jump("loc_4E97")

    label("loc_40D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4176")

    #C0151
    ChrTalk(
        0xFE,
        "迷子の子供、ですか……？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "さあ、僕も先生も\x01",
            "パレードは見ていなかったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "パレードの楽しげな音楽は\x01",
            "ここまで聞こえてきたんですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E97")

    label("loc_4176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4219")

    #C0154
    ChrTalk(
        0xFE,
        (
            "今年のパレードは\x01",
            "とても華やかでしたね……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        "僕も少し驚いてしまいました。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "先生も今日くらいは\x01",
            "お仕事を休まれてもいいのに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_425B")

    label("loc_4219")


    #C0157
    ChrTalk(
        0xFE,
        (
            "お仕事がなければ\x01",
            "先生にも休息を取って\x01",
            "頂きたい所なんですが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_425B")

    Jump("loc_4E97")

    label("loc_4260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_436A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4311")

    #C0158
    ChrTalk(
        0xFE,
        (
            "昨日の国際シンポジウムの後、\x01",
            "識者の方々と会食なさったんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        "先生はお酒に弱いんです。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "そのくせ飲むんだから。\x01",
            "だらしがありません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4365")

    label("loc_4311")

    TurnDirection(0xA, 0x9, 0)

    #C0161
    ChrTalk(
        0xFE,
        "ほら先生、酔い覚ましです！\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "まったくもう、\x01",
            "だらしがないんだから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4365")

    Jump("loc_4E97")

    label("loc_436A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_44CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4469")

    #C0163
    ChrTalk(
        0xFE,
        (
            "午後から市庁舎のセレモニーホールで\x01",
            "国際シンポジウムがあるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "『クロスベルの現状と将来』……\x01",
            "金融や商業のお話の他、\x01",
            "犯罪問題も取り扱われるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "先生も出席なさるんですよ。\x01",
            "お時間を忘れないようにしないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_44C9")

    label("loc_4469")


    #C0166
    ChrTalk(
        0xFE,
        (
            "先生は午後から\x01",
            "国際シンポジウムに\x01",
            "出席なさるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "お時間を忘れないようにしないと。\x02",
    )

    CloseMessageWindow()

    label("loc_44C9")

    Jump("loc_4E97")

    label("loc_44CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_460F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4582")

    #C0168
    ChrTalk(
        0xFE,
        (
            "先生ときたら、\x01",
            "僕を子供扱いして……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "ぼ、僕は別にお祭りなんて\x01",
            "興味ありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "先生が見たいとおっしゃるなら\x01",
            "モチロンご一緒しますけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_460A")

    label("loc_4582")


    #C0171
    ChrTalk(
        0xFE,
        (
            "コホン、僕は法律の勉強をして\x01",
            "早く一人前の弁護士になりたいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "先生がどうしてもとおっしゃるなら\x01",
            "モチロンご一緒しますけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_460A")

    Jump("loc_4E97")

    label("loc_460F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_46B9")

    #C0173
    ChrTalk(
        0xFE,
        "先生は来週も出張のご予定なんです。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "……何だか最近、\x01",
            "特に立て込んでいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "先生が慌てなくてもいいように\x01",
            "今のうちに準備をしてさしあげないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E97")

    label("loc_46B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_47CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4755")

    #C0176
    ChrTalk(
        0xFE,
        (
            "もし本当に\x01",
            "イリア・プラティエさんの身に\x01",
            "何かあったら……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "きっとクロスベルは大混乱ですね……\x01",
            "記念祭前のこんな時期に……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_47C7")

    label("loc_4755")


    #C0178
    ChrTalk(
        0xFE,
        (
            "僕も少しお話を\x01",
            "聞いてしまったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "先生が心配なさるのも道理です。\x01",
            "きっと大混乱になるでしょうから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47C7")

    Jump("loc_4E97")

    label("loc_47CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_48D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4840")

    #C0180
    ChrTalk(
        0xFE,
        "先生にご相談ですか？\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "ちょうど仕事も\x01",
            "一区切り付けられた所です。\x01",
            "どうぞ、奥の方へ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48D3")

    label("loc_4840")


    #C0182
    ChrTalk(
        0xFE,
        (
            "黒月の支社長は、たしか\x01",
            "ツァオ・リーという人です。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "先生が仰るには\x01",
            "とても油断ならない人物だとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "どうか皆さんも\x01",
            "気を付けてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48D3")

    Jump("loc_4E97")

    label("loc_48D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_49D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4981")

    #C0185
    ChrTalk(
        0xFE,
        (
            "ふう……最近急に\x01",
            "相談に来る方が増えているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "事故とか揉め事とか……\x01",
            "今年は妙に多いみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "お陰で先生も大忙しですよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_49D3")

    label("loc_4981")


    #C0188
    ChrTalk(
        0xFE,
        (
            "事故とか揉め事とか……\x01",
            "今年は妙に多いみたいです。\x01",
            "お陰で先生も大忙しですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49D3")

    Jump("loc_4E97")

    label("loc_49D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4A73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49F3")
    Call(0, 12)
    Jump("loc_4A6E")

    label("loc_49F3")

    TurnDirection(0xA, 0x8, 0)

    #C0189
    ChrTalk(
        0xFE,
        (
            "先生ときたら、報酬を\x01",
            "受け取り忘れた事まであるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "覚えてらっしゃいますか！？\x01",
            "僕は呆れてしまいます！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A6E")

    Jump("loc_4E97")

    label("loc_4A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B66")

    #C0191
    ChrTalk(
        0xFE,
        (
            "こうして資料を整理するのも\x01",
            "弁護士になるための勉強です。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "分からない所があれば\x01",
            "先生が丁寧に教えてくれるんです。\x01",
            "僕、先生には本当に感謝しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "……もう少し整理した状態に\x01",
            "しておいてほしい所ですけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4BD7")

    label("loc_4B66")


    #C0194
    ChrTalk(
        0xFE,
        (
            "先生はお忙しいときでも\x01",
            "僕の勉強のために\x01",
            "時間を割いてくれるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "僕、先生には\x01",
            "本当に感謝しています。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BD7")

    Jump("loc_4E97")

    label("loc_4BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4CB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C33")

    #C0196
    ChrTalk(
        0xFE,
        "お客様ですか？\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "先生ならデスクに\x01",
            "いらっしゃいますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_4C33")


    #C0198
    ChrTalk(
        0xFE,
        (
            "やれやれ、先生ときたら\x01",
            "整理が悪いんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "この棚は判例別・年代順に\x01",
            "見やすく並べなおさないと\x01",
            "資料の価値がありません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB4")

    Jump("loc_4E97")

    label("loc_4CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4D68")

    #C0200
    ChrTalk(
        0xFE,
        (
            "先生のお帰りは\x01",
            "午後だと聞いていたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "おかしいですね、またお仕事が\x01",
            "入ってしまったんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "ふう、先生はお忙しいので\x01",
            "お体が心配です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E97")

    label("loc_4D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4E97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E12")

    #C0203
    ChrTalk(
        0xFE,
        "あれ……お客さまですか？\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "すみません、先生は\x01",
            "出掛けてしまっているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "先生に御用なら\x01",
            "どうぞそちらの応接室で\x01",
            "お待ちください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4E97")

    label("loc_4E12")


    #C0206
    ChrTalk(
        0xFE,
        (
            "あ……申し遅れました。\x01",
            "僕、先生の助手のピートといいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "先生に負けない\x01",
            "立派な弁護士になるため\x01",
            "頑張っていこうと思います。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E97")

    TalkEnd(0xFE)
    Return()

    # Function_14_3817 end

    def Function_15_4E9B(): pass

    label("Function_15_4E9B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F2F")
    Jump("loc_4F79")

    label("loc_4F2F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4F4F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F79")

    label("loc_4F4F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F6F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F79")

    label("loc_4F6F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F79")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Call(0, 13)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_4E9B end

    def Function_16_4FA9(): pass

    label("Function_16_4FA9")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5059")
    OP_29(0x46, 0x1, 0xB)

    #C0208
    ChrTalk(
        0x101,
        (
            "#0001F（これで西通りも\x01",
            "  一通り回ったけど……）\x02\x03",

            "#0003F（……みんなの捜索状況は\x01",
            "  どうなってるかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x160,
        "#3308F（…………………………）\x02",
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 7)

    label("loc_5059")

    Return()

    # Function_16_4FA9 end

    def Function_17_505A(): pass

    label("Function_17_505A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_50EE")
    Jump("loc_5138")

    label("loc_50EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_510E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5138")

    label("loc_510E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_512E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5138")

    label("loc_512E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5138")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0210
    ChrTalk(
        0xC,
        (
            "#3608Fリゼロさん、一体どこへ……\x02\x03",

            "#3610F商売に携わる者が\x01",
            "連絡もなしに消えるなんて\x01",
            "考えられないんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_505A end

    def Function_18_51D5(): pass

    label("Function_18_51D5")

    EventBegin(0x0)
    Fade(500)
    OP_68(7200, 2320, 17750, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 6800, 1000, 17000, 0)
    SetChrPos(0x102, 7600, 1000, 16850, 0)
    SetChrPos(0x103, 6800, 1000, 15750, 0)
    SetChrPos(0x104, 7600, 1000, 15600, 0)
    OP_93(0x8, 0x0, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    #C0211
    ChrTalk(
        0x8,
        (
            "#2200Fはい、こちら法律事務所……\x02\x03",

            "#2203Fええ、そう言われましても……\x01",
            "……ええ、私の方でも初耳で……\x01",
            "…………ええ……ええ………\x02\x03",

            "#2200Fいやいや、こちらこそ申し訳ない。\x01",
            "また何かあればご連絡ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x101,
        "#0005F先生、今の通信は……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    #C0213
    ChrTalk(
        0x8,
        (
            "#2200Fおお、君たちか。\x02\x03",

            "実はその、ルバーチェ商会と\x01",
            "連絡が取れなくなったとかで……\x02\x03",

            "取引のあった会社や\x01",
            "係争中の企業から問い合わせが\x01",
            "相次いでいるんだよ。\x02\x03",

            "まったくどうなっているのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x103,
        "#0200Fその件でしたか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0215
    ChrTalk(
        0x8,
        (
            "#2205F君たち……\x01",
            "何か知っているのかね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#0003Fいや、残念ながら詳しい事は……\x02\x03",

            "#0001Fただ、ルバーチェ商会は\x01",
            "今もぬけの殻です。\x02\x03",

            "全員どこかへ消えてしまいまして。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x8,
        "#2205Fほ、本当かね……！？\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#0001F……これはまだ内密に\x01",
            "お願いしたいんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#0101F警察の方も体制を\x01",
            "組み直している所です。\x02\x03",

            "状況が判明するまで\x01",
            "まだ時間が掛かりそうですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        (
            "#2203Fううむ、しかし\x01",
            "時間と共に混乱が広がるだろう……\x02\x03",

            "#2201F……判った。\x01",
            "ルバーチェに関する\x01",
            "問い合わせは私が引き受けよう。\x02\x03",

            "混乱が広がらないよう\x01",
            "何とかしてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#0000F助かります。\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x104,
        (
            "#0301Fマフィアの方も\x01",
            "長くは放っておけねえな……\x01",
            "こっちも先を急ごうぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 7200, 1000, 17000, 0)
    SetScenarioFlags(0xED, 3)
    EventEnd(0x5)
    Return()

    # Function_18_51D5 end

    def Function_19_56FE(): pass

    label("Function_19_56FE")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0223
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "鍵が掛かっているようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_19_56FE end

    def Function_20_5730(): pass

    label("Function_20_5730")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    OP_68(3700, 900, -600, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, 12600, 1000, 5600, 225)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrPos(0x101, -900, 0, -200, 90)
    SetChrPos(0x102, -900, 0, -200, 90)
    SetChrPos(0x103, -900, 0, -200, 90)
    SetChrPos(0x104, -900, 0, -200, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02200.itp")
    SetCameraDistance(23500, 3000)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(650)
    BeginChrThread(0x102, 3, 0, 22)
    Sleep(650)
    BeginChrThread(0x103, 3, 0, 23)
    Sleep(650)
    BeginChrThread(0x104, 3, 0, 24)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x10)

    #N0224
    NpcTalk(
        0x8,
        "男性の声",
        "おや、忘れ物かね？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5928():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5928)
    Sleep(50)

    def lambda_5938():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5938)
    Sleep(50)

    def lambda_5948():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5948)
    Sleep(50)

    def lambda_5958():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5958)
    OP_68(12600, 1500, 5600, 2000)
    OP_6F(0x1)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0225
    NpcTalk(
        0x8,
        "髭面の男性",
        (
            "#6P#2200Fおっと、これは失礼した。\x02\x03",

            "グリムウッド法律事務所へようこそ。\x01",
            "今日は何か相談事でも？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        "#0000Fあ、いや……\x02",
    )

    CloseMessageWindow()

    def lambda_5A18():
        OP_95(0xFE, 9500, 1000, -400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5A18)
    Sleep(1500)
    Fade(500)
    OP_68(3700, 1100, -600, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x103, 0x5A, 0x0)
    WaitChrThread(0x8, 1)

    def lambda_5A88():
        OP_95(0xFE, 4900, 0, -400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5A88)
    WaitChrThread(0x8, 1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("髭面の男性")

    #A0227
    AnonymousTalk(
        0xFF,
        (
            "いやいや。\x01",
            "遠慮することはないよ。\x02\x03",

            "まだ若いようだが\x01",
            "借金などで困ったことでも？\x02\x03",

            "それとも仲間を集めて\x01",
            "事業でも起こしたいのかね？\x02\x03",

            "何でもいい、\x01",
            "どーんと相談してくれたまえ！\x02",
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

    #C0228
    ChrTalk(
        0x101,
        "#6P#0005Fいや、そのですね……\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x104,
        (
            "#3P#0305F（な、なんか凄い\x01",
            "  精力的なオッサンだな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x103,
        "#6P#0205F（この人が『熊ヒゲ先生』ですか……）\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x102,
        (
            "#0102F（ふふっ……\x01",
            "  噂どおりの方みたいね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0232
    NpcTalk(
        0x8,
        "髭面の男性",
        (
            "#11P#2205F……おや……\x02\x03",

            "よく見れば、君の顔……\x01",
            "どこかで見たことがあるな。\x02\x03",

            "#2200F確かこのあたりに\x01",
            "住んでいた子じゃなかったかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#6P#0012Fあはは……\x01",
            "覚えててくれたみたいですね。\x02\x03",

            "#0000Fええ、３年くらい前に\x01",
            "近くのアパルトメントで\x01",
            "暮らしていました。\x02\x03",

            "#0004F改めまして──\x01",
            "ロイド・バニングスといいます。\x02",
        )
    )

    CloseMessageWindow()

    #N0234
    NpcTalk(
        0x8,
        "髭面の男性",
        (
            "#11P#2202Fおお、そうか。\x01",
            "道理で見覚えがあると思ったんだ。\x02\x03",

            "#2205Fん……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0235
    NpcTalk(
        0x8,
        "髭面の男性",
        (
            "#11P#2205Fバニングス……！？\x02\x03",

            "ひょっとして……\x01",
            "ガイ・バニングスの弟さんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        (
            "#6P#0005Fあ……はい。\x02\x03",

            "#0000Fひょっとして、兄のことも\x01",
            "ご存知だったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #N0237
    NpcTalk(
        0x8,
        "髭面の男性",
        "#11P#2203Fご存知もなにも……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #N0238
    NpcTalk(
        0x8,
        "髭面の男性",
        (
            "#11P#2200F……ふむ、どうやら\x01",
            "事情があって来たようだね。\x02\x03",

            "こんな所で立ち話もなんだ。\x01",
            "座って話をしようじゃないか。\x02\x03",

            "#2203Fそうそう……\x01",
            "一応、名乗っておこうか。\x02\x03",

            "#2202F私の名は、イアン・グリムウッド。\x01",
            "この法律事務所で弁護士をしている。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x7D0)
    OP_68(4600, 1000, 5600, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 6600, 140, 5500, 270)
    SetChrChipByIndex(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 2320, 140, 5800, 90)
    SetChrPos(0x102, 2320, 140, 4700, 90)
    SetChrPos(0x103, 4100, 140, 7400, 180)
    SetChrPos(0x104, 5000, 140, 7400, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    WaitBGM()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0239
    AnonymousTalk(
        0x8,
        (
            "#2203Fなるほど……\x01",
            "君たちがセルゲイ君の言ってた\x01",
            "『特務支援課』の新人だったのか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    SetCameraDistance(20500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0240
    ChrTalk(
        0x8,
        (
            "#11P#2202Fそういえば最新の\x01",
            "クロスベルタイムズも読んだよ。\x02\x03",

            "着任早々、なかなか\x01",
            "頑張ってるみたいじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_END)), "loc_6262")

    #C0241
    ChrTalk(
        0x101,
        (
            "#6P#0012Fはは、何だか散々なことを\x01",
            "書かれちゃってますけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62AA")

    label("loc_6262")


    #C0242
    ChrTalk(
        0x101,
        (
            "#6P#0012Fはは、何だか散々なことを\x01",
            "書かれちゃったみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62AA")


    #C0243
    ChrTalk(
        0x8,
        (
            "#11P#2203Fしかしそうか……\x01",
            "あのガイ君の弟さんが警察に。\x02\x03",

            "何だかこう、空の女神#8Rエ イ ド ス#の\x01",
            "巡り合わせを感じるねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#6P#0005Fあの……\x01",
            "先生と兄はどういう？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x8,
        (
            "#11P#2202Fああ、今の君たちと同じく\x01",
            "たまに情報交換に来てくれたんだ。\x02\x03",

            "もっとも、彼は非常に\x01",
            "優秀な捜査官だったからね。\x02\x03",

            "逆に私の方が色々と\x01",
            "助けてもらったくらいだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    #C0246
    ChrTalk(
        0x102,
        (
            "#6P#0105Fちょ、ちょっと\x01",
            "待ってください……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 0x1)
    Sleep(200)

    #C0247
    ChrTalk(
        0x102,
        (
            "#12P#0105Fロイド……あなた、\x01",
            "捜査官のお兄さんがいるの？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)

    #C0248
    ChrTalk(
        0x104,
        (
            "#5P#0302Fなんだよ、水臭ぇな。\x01",
            "そんなこと一言も聞いてないぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x103,
        "#1P#0200F………………………………\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#6P#0000Fはは、ゴメン。\x01",
            "つい言いそびれててさ。\x02\x03",

            "#0004Fそれに……\x01",
            "もう亡くなった人だから。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        "#12P#0101Fえ……\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#6P#0008F仕事中に殉職したんだ。\x02\x03",

            "#0002Fちょうど３年前になるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x102,
        "#12P#0108F……あ………\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x104,
        (
            "#5P#0301Fそうか、それでお前、\x01",
            "しばらくこの街を離れて……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        (
            "#11P#2203F……ガイ君のことは残念だった。\x02\x03",

            "#2201F私も個人的に、あの事件のことは\x01",
            "調べてみたこともあったが……\x02\x03",

            "残念ながら、手がかりすら\x01",
            "見つかっていない状況でね……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#6P#0008F……そう、ですか。\x02\x03",

            "#0003F──いや。\x01",
            "今は兄のことはいいんです。\x02\x03",

            "#0001Fそれよりも先生。\x01",
            "事情は先ほど説明した通りです。\x02\x03",

            "『ルバーチェ』について、\x01",
            "何かご存知のことがあれば\x01",
            "教えていただけませんか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)

    #C0257
    ChrTalk(
        0x8,
        "#11P#2203Fふむ……『ルバーチェ』か。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0258
    ChrTalk(
        0x8,
        (
            "#11P#2201F……彼らにまつわる黒い噂は多い。\x02\x03",

            "帝国と共和国にまたがる密貿易。\x02\x03",

            "盗品売買に、ミラ・ロンダリング。\x02\x03",

            "猟兵団の斡旋や武器の密売まで……\x02\x03",

            "そのどれもが、クロスベルの特殊性を\x01",
            "利用したものと言えるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        "#6P#0005Fクロスベルの特殊性……？\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        (
            "#6P#0103F近年ますます盛んになっている\x01",
            "貿易業と金融業の発展……\x02\x03",

            "#0101Fそれと反比例するかのように\x01",
            "脆弱きわまる政治基盤ですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "#11P#2201Fそう……このクロスベル自治州の\x01",
            "政治基盤は極めて弱い。\x02\x03",

            "多くの政治家は、帝国派か\x01",
            "共和国派のどちらかに属しており、\x01",
            "利権をむさぼる者が多いんだ。\x02\x03",

            "#2203Fそして、マフィアの暗躍を\x01",
            "取り締まる法案が出されたとしても\x01",
            "彼らと癒着した議員に潰される。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        "#6P#0001F……！\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x104,
        "#5P#0301Fなんだそりゃ……本当なのか？\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        (
            "#6P#0106F……残念だけど、本当よ。\x02\x03",

            "#0101Fルバーチェの利権と繋がっている\x01",
            "議員は相当多いと言われているわ。\x02\x03",

            "おそらく、警察が動けないのも\x01",
            "それが最大の理由でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#1P#0203F……大人の事情、ですか。\x02\x03",

            "#0201Fそれではルバーチェは実質上、\x01",
            "犯罪を起こし放題なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x8,
        (
            "#11P#2200Fいや、さすがにそれはない。\x02\x03",

            "あからさまな犯罪を放置すれば\x01",
            "市民や周辺諸国も騒ぐだろうし……\x02\x03",

            "今のところは、市民生活に\x01",
            "直接迷惑はかけない一線だけは\x01",
            "ルバーチェ側も守っているようだ。\x02\x03",

            "#2203F逆にその一線を越えなければ\x01",
            "何をやっても警察は動かない……\x02\x03",

            "#2201Fそう高を括#2Rくく#っているところも\x01",
            "あるみたいだがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x102,
        "#6P#0108F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x101,
        "#6P#0013F……そこまで………\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x104,
        (
            "#5P#0306Fなるほどなぁ。\x02\x03",

            "#0302F活気ある華やかな都市の裏側に、\x01",
            "魑魅魍魎#8Rちみもうりょう#のうごめく影アリか。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x103,
        (
            "#1P#0208F……機密レベルの高い情報を\x01",
            "チェックしておきたいですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#11P#2203Fまあ、ルバーチェの基礎知識は\x01",
            "大体そんなところだが……\x02\x03",

            "#2201F──しかし、ここ最近、\x01",
            "少し風向きが変わってきていてね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0272
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        "#6P#0101Fどういうことですか？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x8,
        (
            "#11P#2201Fこれはまだ、警察の方でも\x01",
            "掴んだばかりの情報らしいが……\x02\x03",

            "最近、どうやらルバーチェの\x01",
            "対抗勢力が現れたらしいんだ。\x02\x03",

            "それもかなり強力な、ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        (
            "#6P#0005F対抗勢力……\x01",
            "まさか遊撃士協会ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x8,
        (
            "#11P#2203Fいや、対抗勢力といっても\x01",
            "悪い意味でだよ。\x02\x03",

            "#2201Fカルバード共和国の東方人街に\x01",
            "一大勢力を構えている組織……\x02\x03",

            "その組織が、このクロスベルに\x01",
            "進出し始めているらしいんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0277
    ChrTalk(
        0x101,
        "#6P#0007Fなっ……\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x102,
        "#6P#0101Fほ、本当ですか！？\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x8,
        (
            "#11P#2203Fああ……\x01",
            "以前からそんな噂はあったが、\x01",
            "どうやら事実だったらしい。\x02\x03",

            "#2201F──組織の名は、『黒月#4Rヘイユエ#』。\x02\x03",

            "そしてつい最近、\x01",
            "クロスベルの港湾区に出来たのが\x01",
            "『黒月貿易公司』という。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        "#6P#0001F『黒月#4Rヘイユエ#』……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        "#1P#0201F……いかにも東方風の名前ですね。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x104,
        (
            "#5P#0303Fしかしマフィア同士の抗争か……\x02\x03",

            "#0301Fこりゃ、不良同士の\x01",
            "喧嘩どころの騒ぎじゃないぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x8,
        (
            "#11P#2203F幸いにしてというべきか……\x02\x03",

            "まだ、その抗争そのものは\x01",
            "表立っては始まっていないらしい。\x02\x03",

            "#2201Fしかし近いうちに何らかの形で\x01",
            "暗闘が始まるかもしれない……\x02\x03",

            "警察の捜査一課などは\x01",
            "それを警戒しているようでね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0284
    ChrTalk(
        0x101,
        "#6P#0005F捜査一課って……！\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x102,
        (
            "#6P#0105Fもしかして、先ほどこちらを\x01",
            "訪ねていた眼鏡の男性は……？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "#11P#2200Fああ、捜査一課に所属する\x01",
            "ダドリー君という捜査官だ。\x02\x03",

            "ちょうど、今話している事と\x01",
            "同じような話をしに来たのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x102,
        "#6P#0103Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        "#6P#0008F…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetChrSubChip(0x103, 0x2)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0289
    ChrTalk(
        0x103,
        (
            "#1P#0205Fロイドさん……？\x02\x03",

            "どうしたんですか？\x01",
            "そんな難しそうな顔をして……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)

    #C0290
    ChrTalk(
        0x104,
        (
            "#5P#0301Fひょっとして、\x01",
            "何か気付いた事でもあるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#6P#0003Fああ……まだ完全には\x01",
            "まとまってはいないけどね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 3300, 0, 5800, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0292
    ChrTalk(
        0x101,
        (
            "#6P#0000F──先生。\x01",
            "ありがとうございました。\x02\x03",

            "先生の情報のおかげで\x01",
            "解決の糸口が見えた気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        (
            "#11P#2203Fそうか……それは何よりだ。\x02\x03",

            "#2202Fセルゲイ君には世話になっているし\x01",
            "君たちの事は個人的に応援している。\x02\x03",

            "また何かあったら\x01",
            "いつでも訪ねてきてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_5730 end

    def Function_21_7771(): pass

    label("Function_21_7771")


    def lambda_7776():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7776)

    def lambda_7787():
        OP_95(0xFE, 300, 0, -200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7787)
    WaitChrThread(0x101, 1)

    def lambda_77A5():
        OP_95(0xFE, 2500, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77A5)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_21_7771 end

    def Function_22_77C6(): pass

    label("Function_22_77C6")


    def lambda_77CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_77CB)

    def lambda_77DC():
        OP_95(0xFE, 300, 0, -200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77DC)
    WaitChrThread(0x102, 1)

    def lambda_77FA():
        OP_95(0xFE, 2500, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77FA)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_22_77C6 end

    def Function_23_781B(): pass

    label("Function_23_781B")


    def lambda_7820():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7820)

    def lambda_7831():
        OP_95(0xFE, 300, 0, -200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7831)
    WaitChrThread(0x103, 1)

    def lambda_784F():
        OP_95(0xFE, 1200, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_784F)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_23_781B end

    def Function_24_7870(): pass

    label("Function_24_7870")


    def lambda_7875():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7875)

    def lambda_7886():
        OP_95(0xFE, 300, 0, -200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7886)
    WaitChrThread(0x104, 1)

    def lambda_78A4():
        OP_95(0xFE, 1200, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_78A4)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_24_7870 end

    def Function_25_78C5(): pass

    label("Function_25_78C5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    OP_68(3700, 900, -600, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 6200, 0, 8000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrPos(0x101, -900, 0, -200, 90)
    SetChrPos(0x102, -900, 0, -200, 90)
    SetChrPos(0x103, -900, 0, -200, 90)
    SetChrPos(0x104, -900, 0, -200, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02200.itp")
    SetCameraDistance(23500, 3000)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(650)
    BeginChrThread(0x102, 3, 0, 22)
    Sleep(650)
    BeginChrThread(0x103, 3, 0, 23)
    Sleep(650)
    BeginChrThread(0x104, 3, 0, 24)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_7A4C():

        label("loc_7A4C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7A4C")

    QueueWorkItem2(0x101, 2, lambda_7A4C)
    WaitChrThread(0x102, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_7A74():

        label("loc_7A74")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7A74")

    QueueWorkItem2(0x102, 2, lambda_7A74)
    WaitChrThread(0x103, 3)

    def lambda_7A8A():

        label("loc_7A8A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7A8A")

    QueueWorkItem2(0x103, 2, lambda_7A8A)
    WaitChrThread(0x104, 3)

    def lambda_7AA0():

        label("loc_7AA0")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7AA0")

    QueueWorkItem2(0x104, 2, lambda_7AA0)
    OP_6F(0x10)

    #C0294
    ChrTalk(
        0x101,
        "#12P#0000F──失礼します。\x02",
    )

    CloseMessageWindow()
    OP_68(6200, 900, 8000, 1500)
    OP_6F(0x1)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0xE1, 0x1F4)

    #C0295
    ChrTalk(
        0x8,
        "#2205Fおお、君たちか。\x02",
    )

    CloseMessageWindow()

    def lambda_7B25():
        OP_95(0xFE, 6200, 0, 1400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7B25)
    Sleep(1500)
    Fade(500)
    OP_68(3700, 900, -600, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    WaitChrThread(0x8, 1)

    def lambda_7B79():
        OP_95(0xFE, 4900, 0, -400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7B79)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x10E, 0x1F4)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 5)), scpexpr(EXPR_END)), "loc_7C64")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0296
    AnonymousTalk(
        0x8,
        (
            "お疲れさまだ。\x01",
            "頑張っているようだね。\x02",
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

    #C0297
    ChrTalk(
        0x101,
        "#6P#0009Fはは……先生こそ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D44")

    label("loc_7C64")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0298
    AnonymousTalk(
        0x8,
        (
            "久しぶりだね。\x02\x03",

            "話は色々聞いているが\x01",
            "頑張っているようじゃないか。\x02",
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

    #C0299
    ChrTalk(
        0x101,
        (
            "#6P#0009Fはは……先生ほどじゃ\x01",
            "ないと思いますけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D44")


    #C0300
    ChrTalk(
        0x102,
        (
            "#0102F相変わらずお忙しく\x01",
            "してらっしゃるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x8,
        (
            "#2202F#11Pはは、もう慣れっこだよ。\x02\x03",

            "#2201Fそれはそうと……\x01",
            "どうかしたのかね？\x02\x03",

            "何やら相談事があるような\x01",
            "顔つきをしているが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0302
    ChrTalk(
        0x103,
        "#6P#0205F……驚きました。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x104,
        "#3P#0300Fはは、やっぱ分かるもんスかね？\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x8,
        (
            "#2203F#11Pまあ、そういった依頼人を\x01",
            "それこそ山ほど見ているからね。\x02\x03",

            "#2200F仕事も一区切り付いた所だし、\x01",
            "相談くらいには乗れると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        (
            "#6P#0004F先生……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x102,
        (
            "#0100Fそれではお言葉に\x01",
            "甘えさせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x7D0)
    OP_68(4600, 1000, 5600, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 6600, 140, 5500, 270)
    SetChrChipByIndex(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 2320, 140, 5800, 90)
    SetChrPos(0x102, 2320, 140, 4700, 90)
    SetChrPos(0x103, 4100, 140, 7400, 180)
    SetChrPos(0x104, 5000, 140, 7400, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    SetCameraDistance(20500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0307
    ChrTalk(
        0x8,
        (
            "#11P#2201Fなるほど……\x01",
            "アルカンシェルに脅迫状が。\x02\x03",

            "そして《銀》という差出人と\x01",
            "ルバーチェとの関係か……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0308
    ChrTalk(
        0x101,
        "#6P#0001F何か……心当たりでも？\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "#11P#2203Fいや、あいにくそれらを\x01",
            "結びつける情報は知らないが……\x02\x03",

            "《銀》という名前ならば\x01",
            "心当たりがないわけではない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0310
    ChrTalk(
        0x101,
        "#6P#0005Fえ……！\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x102,
        "#6P#0101F本当ですか……？\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        (
            "#11P#2201Fああ、同じ人物を指しているか\x01",
            "どうかは判らないが……\x02\x03",

            "それでも構わないかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        "#6P#0000Fええ、もちろんです！\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x104,
        (
            "#5P#0300F今は少しでも手がかりが\x01",
            "欲しいところッスから。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x8,
        (
            "#11P#2203Fふむ……前に出張で\x01",
            "共和国に行った時なんだが。\x02\x03",

            "奇妙な都市伝説を\x01",
            "現地の人に聞かされてね。\x02\x03",

            "#2201F《銀#2Rイン#》と呼ばれている\x01",
            "伝説の凶手がいるらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        "#6P#0001F《銀#2Rイン#》……\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x102,
        "#6P#0101Fいわゆる東方読みですね……\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x103,
        "#1P#0205Fその《凶手#4Rきょうしゅ#》というのは……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    #C0319
    ChrTalk(
        0x104,
        (
            "#11P#0303F確か刺客とか、\x01",
            "暗殺者って意味だったはずだ。\x02\x03",

            "#0300F主に東の方で\x01",
            "使われてる呼び方らしいが。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x8,
        (
            "#11P#2200Fふむ、よく知っているね。\x02\x03",

            "#2203Fまあ、優秀な傭兵のことを\x01",
            "《猟兵#4Rイェーガー#》と呼ぶのと\x01",
            "似たような習わしなんだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)

    #C0321
    ChrTalk(
        0x101,
        (
            "#6P#0001Fしかし……\x01",
            "その都市伝説というのは？\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        (
            "#11P#2201Fああ、どうやら本当に\x01",
            "実在しているのかどうか\x01",
            "分からないらしくてね。\x02\x03",

            "噂では、仮面と黒衣で身を包み\x01",
            "決して素顔を見せないという。\x02\x03",

            "#2203F影のように現れ、影のように消え、\x01",
            "狙った獲物は絶対に逃がさない……\x02\x03",

            "#2201Fそんな亡霊のような存在として\x01",
            "噂されているみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        "#6P#0005F亡霊……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x104,
        "#5P#0301Fずいぶん荒唐無稽な話だな……\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x103,
        (
            "#1P#0203Fなるほど……\x01",
            "だから都市伝説ですか。\x02\x03",

            "#0200Fですが、その伝説の刺客が\x01",
            "どうしてイリアさんに脅迫状を？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x102,
        (
            "#6P#0108F……そうね。\x01",
            "すぐには繋がらないけれど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    #C0327
    ChrTalk(
        0x102,
        "#12P#0101Fもしかして……《黒月#4Rヘイユエ#》？\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        "#6P#0001Fああ……俺もそれは思った。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        (
            "#11P#2201Fふむ……確かに《黒月》は\x01",
            "カルバードの東方人街に\x01",
            "一大勢力を構えている組織だ。\x02\x03",

            "伝説の凶手と何らかの関係が\x01",
            "あっても不思議ではないが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(100)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    #C0330
    ChrTalk(
        0x104,
        (
            "#11P#0300Fなるほど……\x01",
            "あの若頭が反応した理由が\x01",
            "何となく見えてきたな。\x02\x03",

            "#0303F《ルバーチェ》と《黒月》は\x01",
            "現在、この街で対立している……\x02\x03",

            "#0301Fその《黒月》と《銀》ってのが\x01",
            "結びついているとしたら……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    #C0331
    ChrTalk(
        0x103,
        (
            "#5P#0205Fルバーチェと無関係でありながら\x01",
            "彼らが強く意識している存在──\x02\x03",

            "#0202Fロイドさんの推測を\x01",
            "裏付ける事にはなりそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        (
            "#11P#2203Fふむ……興味深いな。\x02\x03",

            "#2200Fしかし──その《銀#2Rイン#》がどうして\x01",
            "アルカンシェルの大スター、\x01",
            "イリア・プラティエを脅すのかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0333
    ChrTalk(
        0x101,
        (
            "#6P#0008Fそれは……\x01",
            "確かにそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x103,
        (
            "#1P#0200Fイリアさんとルバーチェの会長が\x01",
            "酒の席でトラブルを起こした件……\x02\x03",

            "それが関係している可能性は？\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x102,
        (
            "#12P#0106Fううん……どうやら大した話では\x01",
            "無かったみたいだし……\x02\x03",

            "#0101Fルバーチェの対立相手が\x01",
            "彼女を脅す理由にはならないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x104,
        (
            "#11P#0306Fだな……\x02\x03",

            "#0301Fとなると、脅迫状の《銀》ってのは\x01",
            "全くの別人って考えた方がいいのかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0337
    ChrTalk(
        0x101,
        (
            "#6P#0003Fいや……\x01",
            "これだけ符号が揃ってるんだ。\x02\x03",

            "全く関係がないと\x01",
            "切り捨てるのは早計だろう。\x02\x03",

            "#0001F──なあ、みんな。\x02\x03",

            "さっきの今で何だけど……\x01",
            "一度、《黒月#4Rヘイユエ#》も訪ねてみないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0338
    ChrTalk(
        0x102,
        "#12P#0105Fええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x104,
        (
            "#11P#0301Fおいおい……\x01",
            "またしてもいきなりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#6P#0006F考えてもみてくれ。\x02\x03",

            "あの《ルバーチェ》に\x01",
            "警戒されているほどの勢力だ。\x02\x03",

            "#0008Fそんな相手がこの街に進出して\x01",
            "裏社会の覇権を奪おうとしている……\x02\x03",

            "#0013F場合によっては、ルバーチェより\x01",
            "危険な組織かもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x102,
        "#12P#0108Fそれは……\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        (
            "#1P#0201F……なるほど。\x01",
            "これを機会に確かめるわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        (
            "#11P#0306Fしかし……\x01",
            "いきなり訪ねても大丈夫かよ？\x02\x03",

            "#0301Fどんだけ危険な相手だか\x01",
            "こっちには情報もねぇんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x8,
        (
            "#11P#2203Fふむ……\x02\x03",

            "#2200F《黒月貿易公司》の支社長だが\x01",
            "実はこの前、会ったばかりでね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    #C0345
    ChrTalk(
        0x101,
        "#6P#0005Fえ……！？\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x102,
        "#6P#0105F本当ですか……？\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "#11P#2200Fクロスベルでの商取引について\x01",
            "法的に問題ないか\x01",
            "監査を依頼してきたんだ。\x02\x03",

            "#2203F違法なところは無かったから\x01",
            "結局、引き受ける事になったが……\x02\x03",

            "#2201Fその時に、その支社長と会ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        "#6P#0001Fそ、そうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        (
            "#6P#0101F……その……\x01",
            "どういった人物でしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x8,
        (
            "#11P#2203Fふむ……\x01",
            "一言で言うと『キレ者』だね。\x02\x03",

            "まだ若いのに、飄々#4Rひょうひょう#とした言動で\x01",
            "相手を絡め取っていくというか……\x02\x03",

            "#2200Fとにかく一筋縄ではいかない\x01",
            "頭脳の持ち主だと感じさせられたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        "#1P#0201F頭脳派、ですか……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x104,
        "#5P#0306Fなかなか厄介そうな相手だな。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(100)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    #C0353
    ChrTalk(
        0x104,
        (
            "#11P#0301Fそんなキレ者に\x01",
            "わざわざ面会を申し込むのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x101,
        (
            "#6P#0003Fああ……\x01",
            "せっかく口実もある事だしね。\x02\x03",

            "#0000Fどうかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x104,
        (
            "#11P#0302Fハッ……\x01",
            "面白そうじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    #C0356
    ChrTalk(
        0x103,
        (
            "#5P#0202Fわたしも……\x01",
            "少し興味があります。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    #C0357
    ChrTalk(
        0x102,
        (
            "#12P#0103F私も《ルバーチェ》については\x01",
            "ある程度は知識があるけど\x01",
            "《黒月》は殆んど知らないから……\x02\x03",

            "#0101F確かにいい機会かもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        "#6P#0004F決まりだな。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(300)

    #C0359
    ChrTalk(
        0x101,
        (
            "#6P#0000F──イアン先生。\x01",
            "どうも有難うございました。\x02\x03",

            "これで何とか捜査を\x01",
            "続けることが出来そうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x8,
        (
            "#11P#2203Fそうか……\x02\x03",

            "#2202F……ふふ、そうしていると\x01",
            "少しガイ君のことを思い出すな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0361
    ChrTalk(
        0x101,
        "#6P#0005F……あ…………\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#11P#2203F相手は一応、真っ当な\x01",
            "貿易会社を装ってはいる。\x02\x03",

            "その意味で、訪ねるだけであれば\x01",
            "そこまで危険はないだろうが……\x02\x03",

            "#2201Fだが、彼らの本体は\x01",
            "巨大な勢力を誇る犯罪組織だ。\x02\x03",

            "くれぐれも気をつけたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        "#6P#0001Fはい……！\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x102,
        "#6P#0104Fご忠告、感謝します。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_68(4000, 1330, 2800, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 4000, 30, 2800, 180)
    SetChrPos(0x1, 4000, 30, 2800, 180)
    SetChrPos(0x2, 4000, 30, 2800, 180)
    SetChrPos(0x3, 4000, 30, 2800, 180)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x81, 0)
    OP_29(0x42, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_25_78C5 end

    def Function_26_97AB(): pass

    label("Function_26_97AB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(4200, 1300, 5210, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, -1310, 0, 460, 90)
    SetChrPos(0x102, -1310, 0, -430, 90)
    SetChrPos(0x103, -1310, 0, 460, 90)
    SetChrPos(0x104, -1310, 0, -430, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9893")
    SetChrPos(0x10A, -1310, 0, -430, 90)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_9893")

    SetCameraDistance(19000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0365
    ChrTalk(
        0xC,
        "#3601Fやはり報せた方がいいでしょうか……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x9,
        (
            "#2203F#11Pうーむ、しかし間違いだった場合\x01",
            "先方の不利益になりかねない。\x02\x03",

            "#2201Fまずは事実関係を確認してからだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xC,
        "#3608Fそうですね……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(103, 0, 100, 0)
    Fade(500)
    OP_68(640, 1300, 70, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 3)
    Sleep(800)
    OP_68(4330, 1300, 4160, 4000)
    BeginChrThread(0x102, 3, 0, 4)
    Sleep(950)
    BeginChrThread(0x103, 3, 0, 5)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    BeginChrThread(0x104, 3, 0, 6)
    Sleep(950)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99EF")
    BeginChrThread(0x10A, 3, 0, 7)

    label("loc_99EF")

    Sleep(50)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0xC, 0x2)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    #C0368
    ChrTalk(
        0x9,
        "#2205F#5Pおや、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xC,
        (
            "#3600F#5Pおお、皆さん……\x02\x03",

            "#3609Fはは、丁度よかった。\x01",
            "皆さんに相談すれば\x01",
            "解決するかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x9,
        (
            "#2202F#5Pああ、いいタイミングで\x01",
            "来てくれたものだ。\x02",
        )
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B4F")
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_9B4F")

    Sleep(1000)

    #C0371
    ChrTalk(
        0x102,
        "#0105F#12Pあの、話が見えないのですが……\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x104,
        "#0305F#12P一体、何があったんスか？\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x9,
        (
            "#2203F#5Pいや、実は昨日話していた\x01",
            "貿易会社の経営者なんだが……\x02\x03",

            "#2201F今朝から連絡が取れないらしいんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CA7")
    OP_63(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_9CA7")

    Sleep(1000)

    #C0374
    ChrTalk(
        0x101,
        "#0005F#12Pえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xC,
        (
            "#3603F#5P『リゼロ貿易』という会社をお持ちで\x01",
            "私も少しお付き合いがあったんですが……\x02\x03",

            "#3601F自宅にはいらっしゃらず、\x01",
            "会社の方でも行方が判らないそうなんです。\x02\x03",

            "それで警察に届けようかと\x01",
            "先生に相談していた所なんですが……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 500)
    Sleep(150)

    #C0376
    ChrTalk(
        0x101,
        "#0006F#11Pそ、そうでしたか……\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x103,
        "#0208F#12Pやっぱり失踪……でしょうか。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F90")
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10A)

    #C0378
    ChrTalk(
        0x10A,
        (
            "#0603F#11P……少々、事情があって\x01",
            "すぐに警察は動けないかもしれません。\x02\x03",

            "#0600Fこの件は支援課に回すという形を\x01",
            "取っていただけますか？\x02\x03",

            "警察本部には折を見て\x01",
            "私の方から話を通しておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x9,
        (
            "#2202F#5Pふむ……ダドリー君が\x01",
            "そう言うなら間違いなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xC,
        (
            "#3600F#5P分かりました……\x01",
            "それではこの件はお任せします。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        "#0000F#11Pはい、任せてください。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A0E9")

    label("loc_9F90")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0382
    ChrTalk(
        0x101,
        (
            "#0003F#11Pハロルドさん、\x01",
            "警察の方は少々事情があって\x01",
            "動けないかもしれません。\x02\x03",

            "#0001Fこの件は支援課に回すという形を\x01",
            "取っていただけますか？\x02\x03",

            "警察本部には折を見て\x01",
            "話を通すことになると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xC,
        (
            "#3600F#5P分かりました……\x01",
            "皆さんが捜査してくださるんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        (
            "#0001F#11Pええ、少し時間が\x01",
            "掛かるかもしれませんが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0E9")

    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    #C0385
    ChrTalk(
        0x101,
        (
            "#0001F#12Pイアン先生も、もし今後\x01",
            "失踪者の相談があれば\x01",
            "課長に連絡を回してもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x9,
        (
            "#2201F#5Pああ……分かった。\x01",
            "気を付けておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        "#0004F#12Pすみません、お願いします。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0388
    ChrTalk(
        0x104,
        (
            "#0308F#6P（こりゃあ\x01",
            "  急いだ方がいいかもな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#0013F#11P（ああ……寄り道してる\x01",
            "  場合じゃ無さそうだ。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A25D")

    #C0390
    ChrTalk(
        0x10A,
        "#11P#0601F（フン……先を急ぐぞ！）\x02",
    )

    CloseMessageWindow()

    label("loc_A25D")

    OP_5A()
    SetChrPos(0x0, 5780, 30, 2800, 0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0xC8, 3)
    OP_29(0x4C, 0x1, 0xB)
    EventEnd(0x5)
    Return()

    # Function_26_97AB end

    SaveToFile()

Try(main)
