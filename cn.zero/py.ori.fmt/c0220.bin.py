from ZeroScenarioHelper import *

def main():
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
        "伊安律师",               # 1
        "伊安律师",               # 2
        "皮特",                   # 3
        "工商协会干部",           # 4
        "哈罗德",                 # 5
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
        "Function_11_E96",         # 0B, 11
        "Function_12_2FB8",        # 0C, 12
        "Function_13_3138",        # 0D, 13
        "Function_14_321F",        # 0E, 14
        "Function_15_45CB",        # 0F, 15
        "Function_16_46D9",        # 10, 16
        "Function_17_477E",        # 11, 17
        "Function_18_48FD",        # 12, 18
        "Function_19_4DD6",        # 13, 19
        "Function_20_4DFC",        # 14, 20
        "Function_21_6AF2",        # 15, 21
        "Function_22_6B47",        # 16, 22
        "Function_23_6B9C",        # 17, 23
        "Function_24_6BF1",        # 18, 24
        "Function_25_6C46",        # 19, 25
        "Function_26_881C",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_939")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AA")
    Call(0, 18)
    Jump("loc_934")

    label("loc_8AA")


    #C0001
    ChrTalk(
        0xFE,
        (
            "#2200F有关鲁巴彻商会\x01",
            "的咨询问题\x01",
            "都由我来负责。\x02\x03",

            "我想应该可以暂时\x01",
            "避免混乱扩散。\x02\x03",

            "但是，最多也只能维持一天……\x01",
            "你们也要动作快点才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_934")

    Jump("loc_E92")

    label("loc_939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_947")
    Jump("loc_E92")

    label("loc_947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_A3A")

    #C0002
    ChrTalk(
        0xFE,
        (
            "#2200F接下来，\x01",
            "我还有工作……\x01",
            "但黑月那边的事果然让人在意啊。\x02\x03",

            "#2203F关于袭击者相当异常的体能，\x01",
            "我好像曾在『教团』事件中\x01",
            "有所耳闻……\x02\x03",

            "#2200F哈哈，大概是记错了吧。\x01",
            "抱歉，说了些奇怪的话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        "#0208F………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_E92")

    label("loc_A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A48")
    Jump("loc_E92")

    label("loc_A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A56")
    Jump("loc_E92")

    label("loc_A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_CE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C50")

    #C0004
    ChrTalk(
        0x8,
        (
            "#2200F啊，是你们啊。\x01",
            "我听哈罗德先生说了，\x02\x03",

            "你们好像成功\x01",
            "救出了柯林啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0012F嗯，总算是平安解决了。\x02\x03",

            "#0005F说起来……伊安律师。\x02\x03",

            "#0000F哈罗德先生所说的那位\x01",
            "曾经关照过他的律师，莫非就是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#2202F哈哈，只是帮他\x01",
            "做了下债务整理而已。\x02\x03",

            "#2203F那个时候，以黑手党做后台的\x01",
            "无德高利贷者找他麻烦。\x02\x03",

            "#2200F因为利息高得太离谱了，\x01",
            "所以我就稍微帮了他一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        "#0100F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x104,
        (
            "#0306F不过，竟然在这种事情中\x01",
            "都能看到鲁巴彻的影子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        "#0211F他们还真是坏事做尽呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CE2")

    label("loc_C50")


    #C0010
    ChrTalk(
        0xFE,
        (
            "#2200F唔，钱包带了吧……\x02\x03",

            "今天毕竟是最后一天啊，\x01",
            "我打算和皮特\x01",
            "一起去逛一逛。\x02\x03",

            "从明天开始，又要有一大堆的工作了。\x01",
            "偶尔也要\x01",
            "养精蓄锐一下才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE2")

    Jump("loc_E92")

    label("loc_CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_E1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC1")

    #C0011
    ChrTalk(
        0x8,
        (
            "#2200F啊，不好。\x01",
            "找不到要用的资料了。\x02\x03",

            "#2203F今天也还有工作呢，\x01",
            "再这样下去会迟到的。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#0000F伊安律师，您好像很忙啊。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#2200F嗯……因为下个月就是纪念庆典，\x01",
            "找我咨询的人也变多了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E17")

    label("loc_DC1")


    #C0014
    ChrTalk(
        0x8,
        (
            "#2200F我并不是很擅长处理\x01",
            "这类整理文件的工作呢。\x02\x03",

            "呼……还是让皮特\x01",
            "和我一起找吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E17")

    Jump("loc_E92")

    label("loc_E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_E92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E37")
    Call(0, 12)
    Jump("loc_E92")

    label("loc_E37")

    TurnDirection(0x8, 0xA, 0)

    #C0015
    ChrTalk(
        0xFE,
        (
            "#2203F那个……\x01",
            "事情大概就是这样。\x02\x03",

            "#2200F啊啊，是、是我的错。\x01",
            "原谅我吧，皮特。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E92")

    TalkEnd(0xFE)
    Return()

    # Function_10_88C end

    def Function_11_E96(): pass

    label("Function_11_E96")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F2A")
    Jump("loc_F74")

    label("loc_F2A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F4A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F74")

    label("loc_F4A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F6A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F74")

    label("loc_F6A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F74")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_FA7")
    Jump("loc_2FB0")

    label("loc_FA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1049")

    #C0016
    ChrTalk(
        0xFE,
        (
            "#2200F以后如果又有失踪者方面的咨询，\x01",
            "我会联络赛尔盖的。\x02\x03",

            "#2203F……但是，看你们的反应，\x01",
            "似乎不像是普通的失踪事件啊。\x02\x03",

            "嗯……希望是我多虑了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB0")

    label("loc_1049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_14B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1417")

    #C0017
    ChrTalk(
        0xFE,
        (
            "#2200F哎呀，今天你们还真早啊。\x02\x03",

            "是碰到什么麻烦事了吗？\x01",
            "如果要找我商量的话，正好有时间呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0008F不，那个。\x02\x03",

            "#0001F伊安律师，其实是\x01",
            "『黑月』的事务所\x01",
            "好像遭到袭击了。\x02",
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
            "#2205F怎么会……\x01",
            "这是真的吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B9")

    #C0020
    ChrTalk(
        0x104,
        (
            "#0300F我们打算马上\x01",
            "就去现场看一下。\x02\x03",

            "感觉应该是鲁巴彻的\x01",
            "那帮家伙忍耐不住，\x01",
            "终于下手了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1224")

    label("loc_11B9")


    #C0021
    ChrTalk(
        0x104,
        (
            "#0300F我们之前去稍微\x01",
            "查看了一下。\x02\x03",

            "鲁巴彻那帮家伙\x01",
            "还用上了重型机关枪，\x01",
            "看来是忍耐不住，终于下手了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1224")


    #C0022
    ChrTalk(
        0xFE,
        (
            "#2203F唔，竟然在那种闹市区里……\x02\x03",

            "#2201F而且……总觉得很难理解……\x02",
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
            "#2201F鲁巴彻的行动方式似乎很奇怪。\x02\x03",

            "虽然能够理解他们决定去\x01",
            "袭击竞争对手黑月，\x01",
            "但总感觉这次的行动毫无计划性……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#0000F说得对……\x01",
            "我也是这么想的。\x02\x03",

            "看起来，也不像是两派黑手党\x01",
            "的全力火并。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "#2201F嗯……总之，\x01",
            "我也会留心的。\x02\x03",

            "既然发生了这种事情，\x01",
            "来我这里咨询的公司也会变多，\x01",
            "说不定能了解到什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#0100F真不好意思，\x01",
            "一直麻烦您。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 6)
    Jump("loc_14AC")

    label("loc_1417")


    #C0027
    ChrTalk(
        0xFE,
        (
            "#2203F竟然在闹市区发生袭击事件……\x01",
            "实在让人难以理解啊……\x02\x03",

            "#2201F总之，担心治安恶化\x01",
            "的企业有很多，\x01",
            "而黑月那边也有可能进行报复……\x02\x03",

            "我会留心的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14AC")

    Jump("loc_2FB0")

    label("loc_14B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_18F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182F")

    #C0028
    ChrTalk(
        0xFE,
        "#2200F哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0000F伊安律师，好久不见了。\x02\x03",

            "……律师，您最近\x01",
            "好像异常繁忙啊。\x01",
            "今天也要出门吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "#2201F嗯，最近这段时间，和黑手党\x01",
            "有关的纠纷变多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        "#0105F黑手党……是鲁巴彻吗？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "#2203F嗯，而且很多\x01",
            "都是非常危险的事件……\x02\x03",

            "地产投机，或是在欢乐街上当保镖……\x02\x03",

            "#2200F在进行这种『交易』时，\x01",
            "会突然对一般民众动用私刑，\x01",
            "最后害得他们被送进医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#0301F嘁……那些黑手党们\x01",
            "就是恐吓方面的专家啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "#2201F嗯，虽然的确如此……\x01",
            "但总觉得情况有些奇怪……\x02",
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
            "#2201F你们是在市区里巡逻吗？\x01",
            "那么，请你们支援科\x01",
            "也多注意一下吧。\x02\x03",

            "#2203F虽然大部分事情\x01",
            "都会由各位游击士\x01",
            "负责解决。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1758")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1758")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_177E")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_177E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17A4")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_17A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17CA")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_17CA")

    Sleep(1000)

    #C0036
    ChrTalk(
        0x101,
        (
            "#0000F是、是这样啊，\x01",
            "我们会尽量留心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x109,
        (
            "#0500F（支援科的各位\x01",
            "  也很辛苦啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 5)
    Jump("loc_18ED")

    label("loc_182F")


    #C0038
    ChrTalk(
        0xFE,
        (
            "#2200F今天要去见那个\x01",
            "遭到恐吓的公司经理。\x02\x03",

            "#2203F除此之外还有好几件事情……\x01",
            "嗯，差不多要到\x01",
            "傍晚才能回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#0000F（真的很忙啊……）\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#0100F（我们也注意一下\x01",
            "  市区的状况为好。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18ED")

    Jump("loc_2FB0")

    label("loc_18F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_1903")
    Call(0, 13)
    Jump("loc_2FB0")

    label("loc_1903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1B8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2D")

    #C0041
    ChrTalk(
        0xFE,
        (
            "#2205F是罗伊德啊。\x01",
            "今天没和其他人在一起吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#0002F嗯，我们暂时分头行动……\x02\x03",

            "#0000F（对了，也问问\x01",
            "  伊安律师吧。）\x02",
        )
    )

    CloseMessageWindow()

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0044
    ChrTalk(
        0xFE,
        (
            "#2201F哦，是哈罗德先生\x01",
            "的孩子走丢了啊……\x02",
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
            "#2203F抱歉……\x01",
            "在游行开始之前，\x01",
            "就有人过来找我咨询。\x02\x03",

            "#2201F所以我没有\x01",
            "注意外面的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#0003F是这样啊……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "#2203F……他的夫人\x01",
            "肯定相当担心吧。\x02\x03",

            "#2201F罗伊德，\x01",
            "请一定要找到那个孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#0005F好、好的。\x01",
            "（似乎有什么隐情啊？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    Jump("loc_1B85")

    label("loc_1B2D")


    #C0049
    ChrTalk(
        0xFE,
        (
            "#2203F哈罗德先生的夫人\x01",
            "肯定会相当担心吧。\x02\x03",

            "#2201F罗伊德，\x01",
            "请务必要找到那个孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B85")

    Jump("loc_2FB0")

    label("loc_1B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1B9B")
    Call(0, 13)
    Jump("loc_2FB0")

    label("loc_1B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1DBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D61")

    #C0050
    ChrTalk(
        0xFE,
        (
            "#2203F嗯，昨晚\x01",
            "一时兴起，\x01",
            "所以喝多了……\x02\x03",

            "明明今天还有工作呢，\x01",
            "感觉真不舒服啊……\x02",
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
            "#0303F（在警备队的时候，\x01",
            "  我遇到过真正的熊……）\x02\x03",

            "#0300F（伊安律师不舒服的时候，\x01",
            "  样子还真像熊一样呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB3")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1CB3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CD9")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1CD9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CFF")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1CFF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D25")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1D25")

    Sleep(1000)

    #C0052
    ChrTalk(
        0x101,
        (
            "#0006F（兰迪，这样说\x01",
            "　实在是太失礼了……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DB8")

    label("loc_1D61")


    #C0053
    ChrTalk(
        0xFE,
        (
            "#2203F嗯，昨晚\x01",
            "一时兴起，\x01",
            "所以喝多了……\x02\x03",

            "明明今天还有工作呢，\x01",
            "感觉真不舒服啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB8")

    Jump("loc_2FB0")

    label("loc_1DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1E24")

    #C0054
    ChrTalk(
        0xFE,
        (
            "#2200F嗯，原稿这样就行了……\x02\x03",

            "今天下午有\x01",
            "一些重要人物找我过去。\x02\x03",

            "呼，感觉很紧张啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB0")

    label("loc_1E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2168")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D9")

    #C0055
    ChrTalk(
        0xFE,
        (
            "#2200F哦哦，是你们啊，\x01",
            "是在为纪念庆典巡逻吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#0000F嗯，算是吧。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "#2200F哦，这样啊。\x02\x03",

            "有你们这些阻止了暗杀市长\x01",
            "阴谋的英雄们巡逻，\x01",
            "市民们就能安心下来了。\x02",
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
        "#0302F不，没那么夸张啦……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        "#0203F……太、太让人难为情了。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0012F伊安律师，请不要给我们\x01",
            "戴高帽子啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "#2202F哈哈，这不是事实吗，\x01",
            "没必要那么谦虚哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#0100F那么……伊安律师，\x01",
            "您不去逛逛纪念庆典吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "#2200F嗯，\x01",
            "因为接到了一些工作。\x02\x03",

            "#2203F克洛斯贝尔有很多国际企业。\x01",
            "即使是在创立纪念庆典期间，\x01",
            "也有一些公司不放假呢。\x02\x03",

            "#2200F不过，我打算\x01",
            "有空时就去逛逛。\x01",
            "毕竟是难得的节日啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 6)
    Jump("loc_2163")

    label("loc_20D9")


    #C0064
    ChrTalk(
        0xFE,
        (
            "#2200F终究还是有工作要做，\x01",
            "所以事务所也不能放假。\x02\x03",

            "不过，我打算\x01",
            "有空时就去逛逛。\x02\x03",

            "#2202F毕竟是难得的节日，\x01",
            "皮特也想\x01",
            "偶尔出去玩玩吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2163")

    Jump("loc_2FB0")

    label("loc_2168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2354")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2307")

    #C0065
    ChrTalk(
        0xFE,
        (
            "#2200F哦哦，是你们啊……\x02\x03",

            "#2201F有关恐吓信的调查，\x01",
            "听说已经移交给搜查一科处理了。\x02",
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
        "#0105F嗯，您的消息还真灵通啊……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "#2200F达德利刚刚来过了。\x02\x03",

            "他来确认了一下\x01",
            "银和黑月的最新情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#0001F这、这样啊。\x02\x03",

            "#0003F……搜查一科的动作\x01",
            "好像也挺快的。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0303F算啦，在意也没用。\x01",
            "我们也展开\x01",
            "自己的行动吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 6)
    Jump("loc_234F")

    label("loc_2307")


    #C0070
    ChrTalk(
        0xFE,
        (
            "#2201F彩虹剧团\x01",
            "陷入了危机吗……\x02\x03",

            "#2203F哎，希望只是个\x01",
            "恶作剧吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_234F")

    Jump("loc_2FB0")

    label("loc_2354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2431")

    #C0071
    ChrTalk(
        0xFE,
        (
            "#2203F『银』和『黑月贸易公司』……\x01",
            "的确还不能断言\x01",
            "两者之间没有关系。\x02\x03",

            "#2201F另外，我认为黑月贸易公司的\x01",
            "分公司经理也是个相当厉害的人物。\x02\x03",

            "他们的真实身份其实是个\x01",
            "很有势力的庞大犯罪组织，\x01",
            "所以请务必小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB0")

    label("loc_2431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_26B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2620")

    #C0072
    ChrTalk(
        0xFE,
        (
            "#2200F哦哦，是你们啊，\x01",
            "好久不见了。\x02\x03",

            "我听到了很多传闻，\x01",
            "你们好像也很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#0000F啊哈哈……但还是\x01",
            "比不过律师您啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#0301F像之前抓住的鲁巴彻成员，\x01",
            "也很快就被保释了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "#2203F嗯……\x01",
            "黑手党的问题已经根深蒂固了，\x01",
            "特别是在这个克洛斯贝尔市里。\x02\x03",

            "#2200F不过，你们的活跃\x01",
            "也让市民们的心中\x01",
            "稍稍有了些希望之光啊。\x02\x03",

            "说实话，\x01",
            "也让我清醒了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        (
            "#0100F律师……\x01",
            "谢谢您。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "#2200F哈哈，要说谢谢的人\x01",
            "应该是我吧。\x02\x03",

            "特别任务支援科──\x01",
            "请一定要继续加油啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 5)
    Jump("loc_26B4")

    label("loc_2620")


    #C0078
    ChrTalk(
        0xFE,
        (
            "#2200F老实说，我从赛尔盖那里\x01",
            "第一次听说你们的事情时，\x01",
            "还曾抱有怀疑，不过……\x02\x03",

            "特别任务支援科──\x01",
            "你们做得真是很出色啊。\x02\x03",

            "今后也请\x01",
            "继续加油啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B4")

    Jump("loc_2FB0")

    label("loc_26B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_27F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2787")

    #C0079
    ChrTalk(
        0xFE,
        (
            "#2200F我所受理的案件主要局限于\x01",
            "克洛斯贝尔市的范围内……\x02\x03",

            "不过，大概是因为最近比较景气吧，\x01",
            "去阿尔摩利卡和玛因兹做生意\x01",
            "的商人好像也变多了呢。\x02\x03",

            "拜其所赐，我的出差次数也增加了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27EB")

    label("loc_2787")


    #C0080
    ChrTalk(
        0xFE,
        (
            "#2200F我一般奉行现场主义，\x01",
            "一定会去和委托有关的\x01",
            "现场看一看。\x02\x03",

            "拜其所赐，我的出差次数也增加了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27EB")

    Jump("loc_2FB0")

    label("loc_27F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2D7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C21")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0081
    ChrTalk(
        0xFE,
        (
            "#2200F哎呀，是支援科的各位啊。\x02\x03",

            "又遇到\x01",
            "什么困难了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0000F啊，不，\x01",
            "不是这样的……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#0100F不过，罗伊德，\x01",
            "还是先咨询一下伊安律师吧？\x01",
            "或许能发现些什么情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "#2200F嗯，正是如此！\x02\x03",

            "有事情就说出来听听。\x01",
            "不管是什么事，都可以问我！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#0000F哈哈哈……那么，\x01",
            "就稍微占用您一点时间吧……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将狼形魔兽出现在各地\x01",
            "的情况向伊安律师做了说明。\x07\x00\x02",
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
            "#2200F嗯，狼形魔兽啊……\x01",
            "的确有所耳闻……\x02\x03",

            "#2203F但很抱歉，这不是我精通的范围呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        "#0300F哈哈，果然是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x103,
        (
            "#0200F顺便问一下，\x01",
            "您说的有所耳闻是指……？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "#2200F噢噢……\x02\x03",

            "有位玛因兹的商人因为\x01",
            "做不成生意而感到很头疼，\x01",
            "所以想来和我商量。\x02\x03",

            "#2203F不过那之后，警备队似乎开始\x01",
            "巡逻警戒，魔兽就没有再出现过了。\x01",
            "所以之后他也没有来找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#0005F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x102,
        (
            "#0101F和报告书里的内容很吻合啊。\x01",
            "好像没有出现新的受害情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#0001F嗯，按照原定计划，\x01",
            "先从阿尔摩利卡村开始调查吧。\x02\x03",

            "#0000F律师，谢谢您了。\x01",
            "您的情报很值得参考。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "#2200F不不，我什么忙都没帮上，\x01",
            "应该说声抱歉才是啊。\x02\x03",

            "以后要是再遇到什么问题，就过来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 0)
    Jump("loc_2D7A")

    label("loc_2C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D16")

    #C0095
    ChrTalk(
        0xFE,
        (
            "#2201F真抱歉，魔兽这种东西并不在\x01",
            "我的精通范围之内。\x02\x03",

            "#2203F不过，在克洛斯贝尔各地区\x01",
            "出现魔兽，这件事还真是奇怪啊。\x02\x03",

            "一般的魔兽，是不会这样\x01",
            "四处奔波于各地的吧……\x02\x03",

            "#2200F……总之，\x01",
            "你们要加油调查啊。\x01",
            "我会在背后支持你们的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2D7A")

    label("loc_2D16")


    #C0096
    ChrTalk(
        0xFE,
        (
            "#2200F抱歉，魔兽这种东西并不在\x01",
            "我的精通范围之内。\x02\x03",

            "各位，调查要加油啊。\x01",
            "我会在背后支持你们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7A")

    Jump("loc_2FB0")

    label("loc_2D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_2FA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F09")

    #C0097
    ChrTalk(
        0xFE,
        (
            "#2200F如果我说的这些话能\x01",
            "给你们带来一点启发就好了。\x02\x03",

            "以后要是再遇到什么困难，\x01",
            "请不要客气，随时过来找我。\x01",
            "说不定能帮上你们呢。\x02\x03",

            "#2203F……啊，当然了，\x01",
            "也可能根本帮不上什么忙。\x01",
            "但总而言之，遇到事情先来找我商量吧！\x02\x03",

            "#2201F光是烦恼也解决不了任何问题……\x01",
            "法律问题\x01",
            "一般都是这样的！\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#0012F嗯……\x01",
            "那么，以后有机会的话，\x01",
            "会再来麻烦您的。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        "#2202F嗯，我等着你们！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2FA2")

    label("loc_2F09")


    #C0100
    ChrTalk(
        0xFE,
        (
            "#2210F以后要是再遇到什么困难，\x01",
            "请不要客气，随时过来找我。\x02\x03",

            "#2200F如果我不在的话，\x01",
            "就让我的助手皮特传话好了。\x02\x03",

            "皮特处理事务的能力\x01",
            "比我要优秀许多啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FA2")

    Jump("loc_2FB0")

    label("loc_2FA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2FB0")

    label("loc_2FB0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_E96 end

    def Function_12_2FB8(): pass

    label("Function_12_2FB8")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0xA, 0x8, 0)

    #C0101
    ChrTalk(
        0xA,
        (
            "伊安律师，上个月那件事的\x01",
            "报酬金额好像不对啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "#2200F……哦，那个吗？\x01",
            "因为他的经济状况不太好，\x01",
            "所以我就没有收取报酬。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        "哎，又是这样啊！？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "再不适可而止的话，\x01",
            "我们可就要出现赤字了啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#2205F那、那个……\x02\x03",

            "#2203F是、是我不好。\x01",
            "原谅我吧，皮特。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        (
            "就算向我道歉也\x01",
            "没有用啊，伊安律师。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "您明明是律师，\x01",
            "却这么没有经济意识！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_12_2FB8 end

    def Function_13_3138(): pass

    label("Function_13_3138")

    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xB, 0x0)

    #C0108
    ChrTalk(
        0xB,
        (
            "嗯，露天店铺的收入\x01",
            "被偷走了……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "虽然事件最终所幸得到了顺利解决，\x01",
            "但还是给各位店主添了很多麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xB,
        (
            "所以工商协会希望\x01",
            "能给相关人员\x01",
            "提供一些补偿。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "#2200F原来如此，\x01",
            "真是诚恳啊。\x02\x03",

            "嗯，我很乐意\x01",
            "接受相关咨询。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_13_3138 end

    def Function_14_321F(): pass

    label("Function_14_321F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_338D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3346")

    #C0112
    ChrTalk(
        0x101,
        (
            "#0000F那个，可以稍微打扰一下吗？\x02\x03",

            "请问这里有没有\x01",
            "养小猫呢？\x01",
            "或者有没有什么有关小猫主人的线索……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "小猫……吗？\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "那个……各位，这里可是\x01",
            "伊安律师的法律事务所啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "事务所里\x01",
            "是不会养猫的。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x104,
        "#0300F哈哈，也是啊……\x02",
    )

    CloseMessageWindow()
    OP_29(0x8, 0x1, 0x5)
    Jump("loc_3388")

    label("loc_3346")


    #C0117
    ChrTalk(
        0xFE,
        (
            "事务所里\x01",
            "可没有养猫哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "各位今天问的事情\x01",
            "还真是奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3388")

    Jump("loc_45C7")

    label("loc_338D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_344A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_340F")

    #C0119
    ChrTalk(
        0xFE,
        "情况好像有点奇怪……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "从刚刚开始，\x01",
            "就不断接到通讯。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "鲁巴彻商会那边难道\x01",
            "发生了什么事吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3445")

    label("loc_340F")


    #C0122
    ChrTalk(
        0xFE,
        "心里总感觉很不安啊……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        "各位，请一定要小心。\x02",
    )

    CloseMessageWindow()

    label("loc_3445")

    Jump("loc_45C7")

    label("loc_344A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3499")

    #C0124
    ChrTalk(
        0xFE,
        "伊安律师稍后还有工作。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "各位也要去工作了吗？\x01",
            "请加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45C7")

    label("loc_3499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_355F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F4")

    #C0126
    ChrTalk(
        0xFE,
        (
            "啊，早上好。\x01",
            "找伊安律师有事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "他正好刚刚\x01",
            "开始工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_355A")

    label("loc_34F4")


    #C0128
    ChrTalk(
        0xFE,
        (
            "（忙忙碌碌）……\x01",
            "早上的扫除是助手的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "伊安律师他不太注重小节，\x01",
            "所以我必须要好好干才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_355A")

    Jump("loc_45C7")

    label("loc_355F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_368F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_362C")

    #C0130
    ChrTalk(
        0xFE,
        "伊安律师今天也要工作。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "他要去拜访的\x01",
            "市里的公司有五家之多……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)

    #C0132
    ChrTalk(
        0xFE,
        "伊安律师，请快点准备，该出门了！\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "#2203F我、我知道了，皮特。\x01",
            "不过，先让我把文件写完吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_368A")

    label("loc_362C")


    #C0134
    ChrTalk(
        0xFE,
        (
            "各位，真抱歉。\x01",
            "伊安律师马上就要出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "如果没有什么急事的话，\x01",
            "请傍晚时分再过来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_368A")

    Jump("loc_45C7")

    label("loc_368F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_386C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3801")

    #C0136
    ChrTalk(
        0xFE,
        (
            "哎，是支援科的各位啊……\x01",
            "伊安律师出差了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "最近有很多来自外国的咨询。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#0000F这样啊，真遗憾……\x01",
            "本来想找他商量一下\x01",
            "关于保护琪雅的事情……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3780")

    #C0139
    ChrTalk(
        0x102,
        (
            "#0100F真是没办法啊，\x01",
            "还是下次再来拜访伊安律师吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37F9")

    label("loc_3780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_37C1")

    #C0140
    ChrTalk(
        0x103,
        (
            "#0200F真没办法，\x01",
            "还是下次再来拜访伊安律师吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37F9")

    label("loc_37C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_37F9")

    #C0141
    ChrTalk(
        0x104,
        (
            "#0300F没办法啦，\x01",
            "下次再来拜访伊安律师吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37F9")

    SetScenarioFlags(0x0, 1)
    Jump("loc_3867")

    label("loc_3801")


    #C0142
    ChrTalk(
        0xFE,
        (
            "律师出差了哦，\x01",
            "最近有很多来自外国的咨询。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "……自从纪念庆典开始，\x01",
            "我们这边又开始忙碌了起来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3867")

    Jump("loc_45C7")

    label("loc_386C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_38E8")
    TurnDirection(0xA, 0x8, 0)

    #C0144
    ChrTalk(
        0xFE,
        "咳咳……\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "伊安律师，您忘了带\x01",
            "观光指南。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "我已经把逛露天店铺的\x01",
            "顺序写好了，\x01",
            "请不要搞错了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45C7")

    label("loc_38E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_39C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397D")

    #C0147
    ChrTalk(
        0xFE,
        (
            "今年的游行队伍\x01",
            "非常华丽啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        "我也感到有些吃惊。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "律师也真是的，至少今天应该\x01",
            "先放下工作，稍微休息一下嘛……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_39BB")

    label("loc_397D")


    #C0150
    ChrTalk(
        0xFE,
        (
            "如果没有什么工作的话，\x01",
            "真希望伊安律师也\x01",
            "能稍微休息一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BB")

    Jump("loc_45C7")

    label("loc_39C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3A44")

    #C0151
    ChrTalk(
        0xFE,
        "迷路的孩子吗……？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "不清楚啊，\x01",
            "我和伊安律师都没有去看游行。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "虽然游行的欢快音乐\x01",
            "在室内也听得非常清楚……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45C7")

    label("loc_3A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3B1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ADB")

    #C0154
    ChrTalk(
        0xFE,
        (
            "今年的游行队伍\x01",
            "非常华丽啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        "我也有些为之惊叹呢。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "律师也真是的，至少今天应该\x01",
            "先放下工作，稍微休息一下嘛……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B19")

    label("loc_3ADB")


    #C0157
    ChrTalk(
        0xFE,
        (
            "如果没有什么工作的话，\x01",
            "真希望伊安律师也\x01",
            "能稍微休息一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B19")

    Jump("loc_45C7")

    label("loc_3B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3BFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB7")

    #C0158
    ChrTalk(
        0xFE,
        (
            "在昨天的国际研讨会结束后，\x01",
            "我们和几位有识之士一起聚餐……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        "伊安律师不太能喝酒的。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "但还是喝了不少，\x01",
            "真是散漫啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BF5")

    label("loc_3BB7")

    TurnDirection(0xA, 0x9, 0)

    #C0161
    ChrTalk(
        0xFE,
        "伊安律师，该醒醒酒了！\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "太散漫了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BF5")

    Jump("loc_45C7")

    label("loc_3BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD9")

    #C0163
    ChrTalk(
        0xFE,
        (
            "今天下午，在市政厅的大会堂里\x01",
            "将召开国际研讨会。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "主题是『克洛斯贝尔的现状与未来』……\x01",
            "好像除了金融和商业之外，\x01",
            "也会讨论防治犯罪方面的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "伊安律师也会出席呢，\x01",
            "我得提醒他注意时间。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3D1B")

    label("loc_3CD9")


    #C0166
    ChrTalk(
        0xFE,
        (
            "伊安律师他\x01",
            "下午要出席\x01",
            "国际研讨会。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "我得提醒他注意时间。\x02",
    )

    CloseMessageWindow()

    label("loc_3D1B")

    Jump("loc_45C7")

    label("loc_3D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3E4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DCE")

    #C0168
    ChrTalk(
        0xFE,
        (
            "伊安律师也真是的，\x01",
            "总把我当小孩子看待……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "我、我对庆典这种活动\x01",
            "才没有什么兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "不过，如果伊安律师很想去的话，\x01",
            "我当然会陪同啦……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E48")

    label("loc_3DCE")


    #C0171
    ChrTalk(
        0xFE,
        (
            "咳咳，我要好好学习法律知识，\x01",
            "尽早成为一名可以独当一面的律师。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "如果伊安律师无论如何都想去，\x01",
            "我当然也会陪同啦……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E48")

    Jump("loc_45C7")

    label("loc_3E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3ECF")

    #C0173
    ChrTalk(
        0xFE,
        "伊安律师下周也要出差。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "……总觉得最近\x01",
            "非常繁忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "为了不让伊安律师手忙脚乱，\x01",
            "要趁现在做好准备才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45C7")

    label("loc_3ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3FD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F69")

    #C0176
    ChrTalk(
        0xFE,
        (
            "如果伊莉娅·普拉提耶\x01",
            "小姐真的出了\x01",
            "什么事情的话……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔一定会陷入巨大混乱的……\x01",
            "在纪念庆典前夕这种特殊时期……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FD1")

    label("loc_3F69")


    #C0178
    ChrTalk(
        0xFE,
        (
            "那件事我也稍微\x01",
            "听说了一些。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "伊安律师会担心，也不是没有道理。\x01",
            "因为这很可能会导致一场重大混乱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD1")

    Jump("loc_45C7")

    label("loc_3FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_40BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403C")

    #C0180
    ChrTalk(
        0xFE,
        "要找伊安律师咨询吗？\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "他的工作\x01",
            "也正好告一段落了。\x01",
            "请各位到里面去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40B7")

    label("loc_403C")


    #C0182
    ChrTalk(
        0xFE,
        (
            "黑月的分公司经理，应该是个\x01",
            "叫曹·李的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "据伊安律师说，\x01",
            "他是个绝不容小觑的人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "请各位一定要\x01",
            "多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40B7")

    Jump("loc_45C7")

    label("loc_40BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_419C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4157")

    #C0185
    ChrTalk(
        0xFE,
        (
            "呼……最近这段时间，\x01",
            "来咨询的人急剧增加。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "事故和纠纷……\x01",
            "这类事情，今年好像特别多。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "伊安律师因此也变得相当忙呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4197")

    label("loc_4157")


    #C0188
    ChrTalk(
        0xFE,
        (
            "今年好像有很多\x01",
            "事故和纠纷……\x01",
            "伊安律师因此也变得相当忙呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4197")

    Jump("loc_45C7")

    label("loc_419C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4235")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B7")
    Call(0, 12)
    Jump("loc_4230")

    label("loc_41B7")

    TurnDirection(0xA, 0x8, 0)

    #C0189
    ChrTalk(
        0xFE,
        (
            "不过，伊安律师也真是的，\x01",
            "有时居然还会忘记找人家收取报酬。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "这种事就不能记牢一点吗！？\x01",
            "我已经哑口无言了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4230")

    Jump("loc_45C7")

    label("loc_4235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_434A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F6")

    #C0191
    ChrTalk(
        0xFE,
        (
            "像这样整理资料，也是为了\x01",
            "成为律师的一种学习。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "如果遇到什么不懂的地方，\x01",
            "伊安律师就会耐心地教导我。\x01",
            "我真的很感激他。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "……不过，希望他\x01",
            "能够更有条理一些。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4345")

    label("loc_42F6")


    #C0194
    ChrTalk(
        0xFE,
        (
            "伊安律师就算再忙，\x01",
            "也会抽出时间\x01",
            "来关心我的学业。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "我真的\x01",
            "很感激他啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4345")

    Jump("loc_45C7")

    label("loc_434A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4431")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_439D")

    #C0196
    ChrTalk(
        0xFE,
        "是客人吗？\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "想找伊安律师的话，\x01",
            "他就在办公桌那边。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_442C")

    label("loc_439D")


    #C0198
    ChrTalk(
        0xFE,
        (
            "唉，伊安律师也真是的，\x01",
            "做事太没有条理了。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "这个架子上的资料，如果不按照案例和\x01",
            "年代的顺序排列，以方便查询的话，\x01",
            "也就相当于没有价值了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_442C")

    Jump("loc_45C7")

    label("loc_4431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_44C6")

    #C0200
    ChrTalk(
        0xFE,
        (
            "我听说，伊安律师好像\x01",
            "要到下午才会回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "真是奇怪啊，\x01",
            "是不是又有工作了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "呼，伊安律师非常忙，所以我\x01",
            "很担心他的身体。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45C7")

    label("loc_44C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_45C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4550")

    #C0203
    ChrTalk(
        0xFE,
        "哎呀……是客人吗？\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "不好意思，\x01",
            "伊安律师出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "如果有事找他的话，\x01",
            "请在那边的接待室里\x01",
            "稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_45C7")

    label("loc_4550")


    #C0206
    ChrTalk(
        0xFE,
        (
            "啊……还没有进行自我介绍。\x01",
            "我是伊安律师的助手——皮特。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "为了成为不输给\x01",
            "先生的成功律师，\x01",
            "我正在不断努力学习。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45C7")

    TalkEnd(0xFE)
    Return()

    # Function_14_321F end

    def Function_15_45CB(): pass

    label("Function_15_45CB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_465F")
    Jump("loc_46A9")

    label("loc_465F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_467F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46A9")

    label("loc_467F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_469F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46A9")

    label("loc_469F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46A9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Call(0, 13)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_45CB end

    def Function_16_46D9(): pass

    label("Function_16_46D9")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_477D")
    OP_29(0x46, 0x1, 0xB)

    #C0208
    ChrTalk(
        0x101,
        (
            "#0001F（这样一来，西街\x01",
            "  也都调查过了……）\x02\x03",

            "#0003F（……不知大家的\x01",
            "  调查状况怎么样了。）\x02",
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

    label("loc_477D")

    Return()

    # Function_16_46D9 end

    def Function_17_477E(): pass

    label("Function_17_477E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4812")
    Jump("loc_485C")

    label("loc_4812")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4832")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_485C")

    label("loc_4832")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4852")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_485C")

    label("loc_4852")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_485C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0210
    ChrTalk(
        0xC,
        (
            "#3608F利泽罗先生到底去哪里了……\x02\x03",

            "#3610F身为商业人士，\x01",
            "竟然没有任何联络就直接消失，\x01",
            "这真是太让人难以想象了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_477E end

    def Function_18_48FD(): pass

    label("Function_18_48FD")

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
            "#2200F您好，这里是法律事务所……\x02\x03",

            "#2203F嗯，您这么问我也不太清楚……\x01",
            "……是的，我也是第一次听说……\x01",
            "…………嗯……是的………\x02\x03",

            "#2200F不不，我才应该深表歉意。\x01",
            "如果还有什么问题的话，请再联络我。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x101,
        "#0005F伊安律师，刚刚的通讯是……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    #C0213
    ChrTalk(
        0x8,
        (
            "#2200F哦哦，是你们啊。\x02\x03",

            "实际上，现在和鲁巴彻商会\x01",
            "根本联系不上……\x02\x03",

            "和他们有交易的公司，\x01",
            "还有和他们打官司的企业，\x01",
            "都陆续来咨询了呢。\x02\x03",

            "真是的，到底是怎么回事……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x103,
        "#0200F会是因为那件事吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0215
    ChrTalk(
        0x8,
        (
            "#2205F你们……\x01",
            "难道知道些什么吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#0003F不，很遗憾，详情我们也不清楚……\x02\x03",

            "#0001F不过简单来说，鲁巴彻商会\x01",
            "现在只剩下一个空壳了。\x02\x03",

            "所有成员都不知消失到哪去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x8,
        "#2205F是、是真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#0001F……这件事情\x01",
            "还请您暂时保密。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#0101F警方现在\x01",
            "也在着手处理，以求弄清事态。\x02\x03",

            "离判明状况，\x01",
            "好像还需要一点时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        (
            "#2203F嗯，但随着时间的推移，\x01",
            "混乱也会渐渐扩散的……\x02\x03",

            "#2201F……明白了。\x01",
            "有关鲁巴彻商会的问题，\x01",
            "我会继续接受咨询的。\x02\x03",

            "为了不让混乱扩散，\x01",
            "我也来尽自己的一份力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#0000F真是十分感谢，\x01",
            "那就拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x104,
        (
            "#0301F黑手党的事情\x01",
            "不能耽搁太久……\x01",
            "我们也得抓紧时间了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 7200, 1000, 17000, 0)
    SetScenarioFlags(0xED, 3)
    EventEnd(0x5)
    Return()

    # Function_18_48FD end

    def Function_19_4DD6(): pass

    label("Function_19_4DD6")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0223
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门好像锁着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_19_4DD6 end

    def Function_20_4DFC(): pass

    label("Function_20_4DFC")

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
        "男性的声音",
        "是不是忘了什么东西呢？\x02",
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

    def lambda_4FFA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4FFA)
    Sleep(50)

    def lambda_500A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_500A)
    Sleep(50)

    def lambda_501A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_501A)
    Sleep(50)

    def lambda_502A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_502A)
    OP_68(12600, 1500, 5600, 2000)
    OP_6F(0x1)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0225
    NpcTalk(
        0x8,
        "留着络腮胡的男性",
        (
            "#6P#2200F啊，真是失礼了。\x02\x03",

            "欢迎来到格里姆伍德法律事务所。\x01",
            "您有什么问题需要咨询吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        "#0000F啊，不……\x02",
    )

    CloseMessageWindow()

    def lambda_50E4():
        OP_95(0xFE, 9500, 1000, -400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_50E4)
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

    def lambda_5154():
        OP_95(0xFE, 4900, 0, -400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5154)
    WaitChrThread(0x8, 1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("留着络腮胡的男性")

    #A0227
    AnonymousTalk(
        0xFF,
        (
            "不不，\x01",
            "不用客气。\x02\x03",

            "各位看起来还很年轻，\x01",
            "是有贷款方面的问题吗？\x02\x03",

            "还是准备寻找合伙人，\x01",
            "一起创业呢？\x02\x03",

            "不管什么事情都可以，\x01",
            "请尽管向我咨询！\x02",
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
        "#6P#0005F不，那个……\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x104,
        (
            "#3P#0305F（真、真是一位\x01",
            "  精力充沛的大叔啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x103,
        "#6P#0205F（这个人就是『大胡子熊先生』啊……）\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x102,
        (
            "#0102F（呵呵……\x01",
            "  果然和传闻中说的一样啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0232
    NpcTalk(
        0x8,
        "留着络腮胡的男性",
        (
            "#11P#2205F……哎呀……\x02\x03",

            "仔细一看，好像……\x01",
            "以前曾在哪里见过你呢。\x02\x03",

            "#2200F应该是住在\x01",
            "这附近的孩子吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#6P#0012F啊哈哈……\x01",
            "您竟然还记得我啊。\x02\x03",

            "#0000F嗯，大概在三年前，\x01",
            "我就住在这附近的\x01",
            "公寓里。\x02\x03",

            "#0004F正式自我介绍一下──\x01",
            "我叫罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()

    #N0234
    NpcTalk(
        0x8,
        "留着络腮胡的男性",
        (
            "#11P#2202F哦哦，这样啊。\x01",
            "难怪我觉得眼熟。\x02\x03",

            "#2205F嗯……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0235
    NpcTalk(
        0x8,
        "留着络腮胡的男性",
        (
            "#11P#2205F班宁斯……！？\x02\x03",

            "难道你是……\x01",
            "盖伊·班宁斯的弟弟吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊……是的。\x02\x03",

            "#0000F莫非，您也认识\x01",
            "我哥哥吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0237
    NpcTalk(
        0x8,
        "留着络腮胡的男性",
        "#11P#2203F何止是认识啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #N0238
    NpcTalk(
        0x8,
        "留着络腮胡的男性",
        (
            "#11P#2200F……嗯，看样子，\x01",
            "你们来此是有正事要谈吧。\x02\x03",

            "别站在这里说话了，\x01",
            "到里面来坐吧。\x02\x03",

            "#2203F对了对了……\x01",
            "先自我介绍一下。\x02\x03",

            "#2202F我叫伊安·格里姆伍德。\x01",
            "是这家法律事务所的律师。\x02",
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
            "#2203F原来如此……\x01",
            "你们就是赛尔盖说的\x01",
            "『特别任务支援科』的新人啊。\x02",
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
            "#11P#2202F说起来，我在最新一期的\x01",
            "克洛斯贝尔时代周刊上也看到过关于你们的报道。\x02\x03",

            "刚一上任，你们就\x01",
            "表现活跃，十分努力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_END)), "loc_586E")

    #C0241
    ChrTalk(
        0x101,
        (
            "#6P#0012F哈哈，不过那篇文章\x01",
            "把我们写得很不堪啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58AC")

    label("loc_586E")


    #C0242
    ChrTalk(
        0x101,
        (
            "#6P#0012F哈哈，不过，听说那篇文章\x01",
            "把我们写得很不堪啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58AC")


    #C0243
    ChrTalk(
        0x8,
        (
            "#11P#2203F话说回来……\x01",
            "那个盖伊的弟弟也成为警察了啊……\x02\x03",

            "总觉得这是空之女神\x01",
            "安排的命运呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#6P#0005F那个……\x01",
            "请问律师您与哥哥是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x8,
        (
            "#11P#2202F哦，就像现在的你们一样，\x01",
            "他偶尔会过来和我交换一些情报。\x02\x03",

            "不过，因为他是一位\x01",
            "非常优秀的搜查官。\x02\x03",

            "反倒是我经常会\x01",
            "得到他的帮助呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    #C0246
    ChrTalk(
        0x102,
        (
            "#6P#0105F请、请\x01",
            "稍等一下……！\x02",
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
            "#12P#0105F罗伊德……你……\x01",
            "还有个当搜查官的哥哥吗？\x02",
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
            "#5P#0302F什么嘛，你这家伙好见外啊。\x01",
            "怎么都不告诉我们一声？\x02",
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
            "#6P#0000F哈哈，抱歉。\x01",
            "只是一直都没想起来说。\x02\x03",

            "#0004F而且……\x01",
            "他都已经去世了。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        "#12P#0101F哎……\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#6P#0008F是在工作中殉职的。\x02\x03",

            "#0002F到现在正好已经三年了。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x102,
        "#12P#0108F……啊………\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x104,
        (
            "#5P#0301F是吗，所以你才\x01",
            "离开了这座城市一段时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        (
            "#11P#2203F……盖伊的事情，我深表遗憾。\x02\x03",

            "#2201F我个人也曾\x01",
            "调查过那件事情……\x02\x03",

            "但很遗憾，\x01",
            "并没有找到任何线索。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#6P#0008F……是、是吗……\x02\x03",

            "#0003F──不，\x01",
            "现在先不提哥哥的事了。\x02\x03",

            "#0001F话说回来，伊安律师。\x01",
            "情况就像刚才说的那样。\x02\x03",

            "如果您知道什么关于\x01",
            "『鲁巴彻』的事情，\x01",
            "能不能告诉我们呢？\x02",
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
        "#11P#2203F嗯……『鲁巴彻』吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0258
    ChrTalk(
        0x8,
        (
            "#11P#2201F……关于他们，有很多负面传闻呢。\x02\x03",

            "与帝国以及共和国进行地下非法交易。\x02\x03",

            "贩卖赃物、洗黑钱，\x02\x03",

            "甚至还涉及到猎兵团的中介和武器走私等……\x02\x03",

            "无论哪项活动，都可以说是利用了\x01",
            "克洛斯贝尔的特殊性。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        "#6P#0005F克洛斯贝尔的特殊性……？\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        (
            "#6P#0103F近些年来，贸易业和\x01",
            "金融业飞速发展……\x02\x03",

            "#0101F相对的，政治根基却与之形成反比，\x01",
            "一直在不断弱化吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "#11P#2201F对……克洛斯贝尔自治州的\x01",
            "政治根基相当脆弱。\x02\x03",

            "许多政治家不是帝国派，\x01",
            "就是共和国派，\x01",
            "大多都是争权夺利之徒。\x02\x03",

            "#2203F而且就算提出了取缔\x01",
            "黑手党在地下活动的法案，\x01",
            "也会被与他们勾结的议员们否决。\x02",
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
        "#5P#0301F怎么会……这是真的吗？\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        (
            "#6P#0106F……很遗憾，千真万确。\x02\x03",

            "#0101F据说和鲁巴彻有利害关系的\x01",
            "议员还为数不少呢。\x02\x03",

            "恐怕这也是警察一直都\x01",
            "不敢有所作为的最大理由吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#1P#0203F……这就是大人的世界吧。\x02\x03",

            "#0201F那么，也就表示鲁巴彻实际上\x01",
            "可以为所欲为地犯罪了？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x8,
        (
            "#11P#2200F不，倒也没有那么夸张。\x02\x03",

            "如果明目张胆地犯罪，市民们\x01",
            "和周边各国也会产生不满的吧……\x02\x03",

            "如今的鲁巴彻，至少会坚守着\x01",
            "这道底线，不会给市民们的生活\x01",
            "造成直接的麻烦。\x02\x03",

            "#2203F反过来看，只要他们不跨越这条界线，\x01",
            "警察们也就束手无策，无法采取任何行动……\x02\x03",

            "#2201F所以，他们总是摆着一副\x01",
            "居高临下的姿态。\x02",
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
        "#6P#0013F……竟然是这样………\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x104,
        (
            "#5P#0306F原来如此啊。\x02\x03",

            "#0302F充满活力的光鲜都市的背后，竟然暗藏着\x01",
            "魑魅魍魉们蠢蠢欲动的影子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x103,
        (
            "#1P#0208F……真想看看那些高机密等级的情报中\x01",
            "包含了多少肮脏交易……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#11P#2203F总之，关于鲁巴彻的基本情况，\x01",
            "大致上就是这些了……\x02\x03",

            "#2201F──不过就在最近，\x01",
            "局势却稍微出现了一些变化。\x02",
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
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        "#6P#0101F怎么回事？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x8,
        (
            "#11P#2201F这好像也是警方\x01",
            "刚刚才得到的情报……\x02\x03",

            "最近，出现了一股\x01",
            "和鲁巴彻对抗的新势力。\x02\x03",

            "而且似乎还相当强大呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        (
            "#6P#0005F对抗势力……\x01",
            "难道是游击士协会吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x8,
        (
            "#11P#2203F不，虽说是对抗势力，\x01",
            "但这里也是带有贬义的。\x02\x03",

            "#2201F在卡尔瓦德共和国的东方人街，\x01",
            "盘踞着一个很有势力的组织……\x02\x03",

            "这个组织好像开始\x01",
            "打入克洛斯贝尔了。\x02",
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
        "#6P#0007F什、什么……\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x102,
        "#6P#0101F是、是真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x8,
        (
            "#11P#2203F嗯……\x01",
            "之前就有过这样的传闻，\x01",
            "看起来应该是真的。\x02\x03",

            "#2201F──组织的名字叫『黑月』。\x02\x03",

            "而且就在最近，\x01",
            "在克洛斯贝尔的港湾区，成立了一家\x01",
            "名叫『黑月贸易公司』的新企业。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        "#6P#0001F『黑月』……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        "#1P#0201F……很有东方风格的名字啊。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x104,
        (
            "#5P#0303F不过，这可是黑手党之间的抗争啊……\x02\x03",

            "#0301F已经不是不良团伙们那种\x01",
            "小打小闹程度的骚动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x8,
        (
            "#11P#2203F应该说是不幸中的万幸吧……\x02\x03",

            "他们之间的争斗目前好像\x01",
            "还没有公开化。\x02\x03",

            "#2201F不过在近期之内，他们很有可能\x01",
            "会以各种形式展开暗斗……\x02\x03",

            "警方的搜察一科\x01",
            "好像也在密切关注这件事呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0284
    ChrTalk(
        0x101,
        "#6P#0005F搜察一科……！\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x102,
        (
            "#6P#0105F难道说，刚刚来这里\x01",
            "的那位戴眼镜的男性就是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "#11P#2200F嗯，他就是隶属搜查一科\x01",
            "的达德利搜查官。\x02\x03",

            "正巧，他刚才也是来向我\x01",
            "询问同一件事的。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x102,
        "#6P#0103F是这样啊……\x02",
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
            "#1P#0205F罗伊德前辈……？\x02\x03",

            "你怎么了？\x01",
            "表情这么严肃……\x02",
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
            "#5P#0301F难道说，\x01",
            "你发现了什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯……虽然还没有\x01",
            "全部整理清楚。\x02",
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
            "#6P#0000F──伊安律师，\x01",
            "谢谢您了。\x02\x03",

            "多亏了您的情报，\x01",
            "让我找到了解决事件的头绪。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        (
            "#11P#2203F是吗……那可太好了。\x02\x03",

            "#2202F我也经常受赛尔盖的关照，\x01",
            "以个人感情来说，也是很支持你们的。\x02\x03",

            "以后再遇到什么问题的话，\x01",
            "随时都可以来找我。\x02",
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

    # Function_20_4DFC end

    def Function_21_6AF2(): pass

    label("Function_21_6AF2")


    def lambda_6AF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6AF7)

    def lambda_6B08():
        OP_95(0xFE, 300, 0, -200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B08)
    WaitChrThread(0x101, 1)

    def lambda_6B26():
        OP_95(0xFE, 2500, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B26)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_21_6AF2 end

    def Function_22_6B47(): pass

    label("Function_22_6B47")


    def lambda_6B4C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6B4C)

    def lambda_6B5D():
        OP_95(0xFE, 300, 0, -200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B5D)
    WaitChrThread(0x102, 1)

    def lambda_6B7B():
        OP_95(0xFE, 2500, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B7B)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_22_6B47 end

    def Function_23_6B9C(): pass

    label("Function_23_6B9C")


    def lambda_6BA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6BA1)

    def lambda_6BB2():
        OP_95(0xFE, 300, 0, -200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BB2)
    WaitChrThread(0x103, 1)

    def lambda_6BD0():
        OP_95(0xFE, 1200, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BD0)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_23_6B9C end

    def Function_24_6BF1(): pass

    label("Function_24_6BF1")


    def lambda_6BF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6BF6)

    def lambda_6C07():
        OP_95(0xFE, 300, 0, -200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C07)
    WaitChrThread(0x104, 1)

    def lambda_6C25():
        OP_95(0xFE, 1200, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C25)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_24_6BF1 end

    def Function_25_6C46(): pass

    label("Function_25_6C46")

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

    def lambda_6DCD():

        label("loc_6DCD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6DCD")

    QueueWorkItem2(0x101, 2, lambda_6DCD)
    WaitChrThread(0x102, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_6DF5():

        label("loc_6DF5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6DF5")

    QueueWorkItem2(0x102, 2, lambda_6DF5)
    WaitChrThread(0x103, 3)

    def lambda_6E0B():

        label("loc_6E0B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6E0B")

    QueueWorkItem2(0x103, 2, lambda_6E0B)
    WaitChrThread(0x104, 3)

    def lambda_6E21():

        label("loc_6E21")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6E21")

    QueueWorkItem2(0x104, 2, lambda_6E21)
    OP_6F(0x10)

    #C0294
    ChrTalk(
        0x101,
        "#12P#0000F──打扰了。\x02",
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
        "#2205F哦哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    def lambda_6EA2():
        OP_95(0xFE, 6200, 0, 1400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6EA2)
    Sleep(1500)
    Fade(500)
    OP_68(3700, 900, -600, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    WaitChrThread(0x8, 1)

    def lambda_6EF6():
        OP_95(0xFE, 4900, 0, -400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6EF6)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x10E, 0x1F4)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 5)), scpexpr(EXPR_END)), "loc_6FD7")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0296
    AnonymousTalk(
        0x8,
        (
            "辛苦了，\x01",
            "你们好像很努力啊。\x02",
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
        "#6P#0009F哈哈……您才是呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_70A5")

    label("loc_6FD7")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0298
    AnonymousTalk(
        0x8,
        (
            "好久不见了啊。\x02\x03",

            "我听到了很多传闻，\x01",
            "你们好像也很努力啊。\x02",
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
            "#6P#0009F哈哈……不过还是\x01",
            "比不过律师您啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A5")


    #C0300
    ChrTalk(
        0x102,
        (
            "#0102F您好像还是\x01",
            "一如既往地忙碌啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x8,
        (
            "#2202F#11P哈哈，都习惯啦。\x02\x03",

            "#2201F先不说这些了……\x01",
            "今天有何贵干呢？\x02\x03",

            "看你们的样子，好像\x01",
            "有事要找我商量吧？\x02",
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
        "#6P#0205F……真让人吃惊。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x104,
        "#3P#0300F哈哈，果然能看得出来吗？\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x8,
        (
            "#2203F#11P哈哈，因为我见过无数来找我商谈的\x01",
            "委托人了，当然是能看出来的。\x02\x03",

            "#2200F我手上的工作也正好告一段落，\x01",
            "应该可以和你们谈谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        (
            "#6P#0004F伊安律师……\x01",
            "谢谢您。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x102,
        (
            "#0100F那么就\x01",
            "恭敬不如从命了。\x02",
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
            "#11P#2201F原来如此……\x01",
            "彩虹剧团收到了恐吓信啊。\x02\x03",

            "疑问点是，名叫『银』的寄件人\x01",
            "和鲁巴彻的关系吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0308
    ChrTalk(
        0x101,
        "#6P#0001F您……有什么线索吗？\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "#11P#2203F不，很不巧，\x01",
            "我也不太清楚……\x02\x03",

            "不过，『银』这个名字\x01",
            "我倒是听说过。\x02",
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
        "#6P#0005F哎……！\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x102,
        "#6P#0101F是真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        (
            "#11P#2201F嗯，虽然不知道\x01",
            "指的是不是同一个人……\x02\x03",

            "即使这样也没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        "#6P#0000F嗯，当然！\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x104,
        (
            "#5P#0300F如今这种状况，任何线索都很重要，\x01",
            "哪怕只是一点也好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x8,
        (
            "#11P#2203F嗯……之前出差\x01",
            "去共和国的时候，\x02\x03",

            "听当地人说了个\x01",
            "非常奇异的都市传说。\x02\x03",

            "#2201F好像是有个名为\x01",
            "『银』的，传说中的刺客。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        "#6P#0001F『银』……\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x102,
        "#6P#0101F很东方的叫法啊……\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x103,
        "#1P#0205F所谓的『刺客』是……？\x02",
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
            "#11P#0303F应该是指杀手、\x01",
            "暗杀者这类意思吧。\x02\x03",

            "#0300F刺客这种叫法\x01",
            "在东方比较普遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x8,
        (
            "#11P#2200F嗯，你知道得不少啊。\x02\x03",

            "#2203F总之，这就和把优秀的佣兵\x01",
            "称作『猎兵』的\x01",
            "习惯差不多吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)

    #C0321
    ChrTalk(
        0x101,
        (
            "#6P#0001F话说回来……\x01",
            "那个都市传说究竟是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        (
            "#11P#2201F嗯，实际上，\x01",
            "似乎没人能够确定\x01",
            "他是否真正存在。\x02\x03",

            "传言说，那个刺客戴着面具、穿着黑衣，\x01",
            "绝对不会让人看到他的真面目。\x02\x03",

            "#2203F像影子般出现，又像影子般消失，\x01",
            "绝不放过盯上的猎物……\x02\x03",

            "#2201F他被视为亡灵一般的存在，\x01",
            "街头巷尾广泛流传着他的传闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        "#6P#0005F亡灵……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x104,
        "#5P#0301F真是个荒唐的传说啊……\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x103,
        (
            "#1P#0203F原来如此……\x01",
            "所以才说是都市传说啊。\x02\x03",

            "#0200F可是，那个传说中的刺客\x01",
            "为什么要寄恐吓信给伊莉娅小姐呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x102,
        (
            "#6P#0108F……是啊，\x01",
            "虽然一时也想不出两者之间的关联……\x02",
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
        "#12P#0101F难道是……『黑月』？\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        "#6P#0001F嗯……我也是这么想的。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        (
            "#11P#2201F嗯……的确，\x01",
            "『黑月』在卡尔瓦德的东方人街\x01",
            "是一个势力非常强大的组织。\x02\x03",

            "即使和传说中的刺客有所关联，\x01",
            "也没什么好奇怪的……\x02",
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
            "#11P#0300F原来如此……\x01",
            "我总算明白鲁巴彻的那个副头目\x01",
            "为什么会有那种反应了。\x02\x03",

            "#0303F『鲁巴彻』和『黑月』，\x01",
            "如今在这个城市中保持着对峙的局势……\x02\x03",

            "#0301F如果『黑月』和『银』\x01",
            "有所关联……\x02",
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
            "#5P#0205F那么，鲁巴彻就算和此事无关，\x01",
            "也会很重视他的存在。\x02\x03",

            "#0202F这也就能证实\x01",
            "罗伊德前辈的推理了。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        (
            "#11P#2203F嗯……这真是耐人寻味啊。\x02\x03",

            "#2200F但是──那个『银』到底为什么\x01",
            "要威胁彩虹剧团的大明星──\x01",
            "伊莉娅·普拉提耶呢？\x02",
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
            "#6P#0008F这……\x01",
            "说得也是呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x103,
        (
            "#1P#0200F伊莉娅小姐和鲁巴彻的会长\x01",
            "曾在酒宴上闹翻过……\x02\x03",

            "也许和此事有关？\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x102,
        (
            "#12P#0106F不……那似乎\x01",
            "并不是什么大事……\x02\x03",

            "#0101F和鲁巴彻对立的敌人\x01",
            "更不会因此而威胁她。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x104,
        (
            "#11P#0306F也是……\x02\x03",

            "#0301F这样的话，只能认为那个寄出恐吓信的『银』\x01",
            "和刚刚说的那个刺客并不是同一个人？\x02",
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
            "#6P#0003F不……\x01",
            "情报和推理有很多吻合的地方。\x02\x03",

            "要断言他们之间完全没有联系，\x01",
            "未免还为时过早。\x02\x03",

            "#0001F──我说，各位。\x02\x03",

            "虽然这么说有点唐突……\x01",
            "我们要不要去『黑月』拜访一下呢？\x02",
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
        "#12P#0105F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x104,
        (
            "#11P#0301F喂喂……\x01",
            "又这么突然吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#6P#0006F你们想想看。\x02\x03",

            "那可是能让『鲁巴彻』\x01",
            "都如此戒备的庞大势力。\x02\x03",

            "#0008F这样的组织，已经进入了这个城市，\x01",
            "并企图夺取黑道势力的霸权……\x02\x03",

            "#0013F说不定，那是个比鲁巴彻\x01",
            "还要危险的组织呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x102,
        "#12P#0108F这个……\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        (
            "#1P#0201F……原来如此，\x01",
            "我们正好趁这个机会探探虚实吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        (
            "#11P#0306F不过……\x01",
            "突然造访真的没问题吗？\x02\x03",

            "#0301F我们根本不知道\x01",
            "对方有多么危险吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x8,
        (
            "#11P#2203F嗯……\x02\x03",

            "#2200F其实我在前段时间，\x01",
            "曾和『黑月贸易公司』的分公司经理见过面。\x02",
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
        "#6P#0005F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x102,
        "#6P#0105F是真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "#11P#2200F他来委托我监察\x01",
            "他们在克洛斯贝尔的贸易\x01",
            "是否存在什么法律方面的问题。\x02\x03",

            "#2203F因为并没有涉及到违法行为，\x01",
            "所以我就接受了委托……\x02\x03",

            "#2201F我就是在那个时候见到了那位分公司经理。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        "#6P#0001F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        (
            "#6P#0101F……请问……\x01",
            "他是什么样的人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x8,
        (
            "#11P#2203F嗯……\x01",
            "简而言之，就是个『很精明的人』。\x02\x03",

            "虽然年纪轻轻，却很擅长用巧妙\x01",
            "的言行来拉拢对方……\x02\x03",

            "#2200F总之，我感觉他的头脑非常灵活，\x01",
            "绝非易与之辈。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        "#1P#0201F计谋派吗……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x104,
        "#5P#0306F看来是个挺麻烦的家伙啊。\x02",
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
            "#11P#0301F我们要专程\x01",
            "去见这样一位厉害人物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯……\x01",
            "毕竟有很好的借口。\x02\x03",

            "#0000F怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x104,
        (
            "#11P#0302F哈……\x01",
            "这不是挺有趣的吗？\x02",
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
            "#5P#0202F我也一样……\x01",
            "有点兴趣呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    #C0357
    ChrTalk(
        0x102,
        (
            "#12P#0103F我虽然对『鲁巴彻』\x01",
            "还算有一定程度的了解，\x01",
            "但对『黑月』就一无所知了……\x02\x03",

            "#0101F这的确是个好机会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        "#6P#0004F那就决定了。\x02",
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
            "#6P#0000F──伊安律师，\x01",
            "非常感谢您。\x02\x03",

            "这样一来，总算能\x01",
            "继续调查下去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x8,
        (
            "#11P#2203F是吗……\x02\x03",

            "#2202F……呵呵，看你这么努力，\x01",
            "又让我想起了盖伊啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0361
    ChrTalk(
        0x101,
        "#6P#0005F……啊…………\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#11P#2203F对方毕竟在表面上\x01",
            "伪装成了一家合法的贸易公司。\x02\x03",

            "因此，如果只是前去拜访，\x01",
            "应该还不至于有什么危险……\x02\x03",

            "#2201F但是不要忘记，他们真正的身份\x01",
            "确实是势力非常庞大的犯罪组织。\x02\x03",

            "所以请务必小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        "#6P#0001F是……！\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x102,
        "#6P#0104F谢谢您的忠告。\x02",
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

    # Function_25_6C46 end

    def Function_26_881C(): pass

    label("Function_26_881C")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8904")
    SetChrPos(0x10A, -1310, 0, -430, 90)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_8904")

    SetCameraDistance(19000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0365
    ChrTalk(
        0xC,
        "#3601F或许该去报警比较好吧……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x9,
        (
            "#2203F#11P嗯，但如果搞错了，\x01",
            "可能会造成对方的损失呢。\x02\x03",

            "#2201F还是先确认一下现状吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xC,
        "#3608F说得也是……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A38")
    BeginChrThread(0x10A, 3, 0, 7)

    label("loc_8A38")

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
        "#2205F#5P啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xC,
        (
            "#3600F#5P哦哦，各位……\x02\x03",

            "#3609F哈哈，你们来得正好。\x01",
            "和你们商量一下，\x01",
            "说不定就能解决了。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x9,
        (
            "#2202F#5P嗯，你们来得\x01",
            "正是时候啊。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B7A")
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_8B7A")

    Sleep(1000)

    #C0371
    ChrTalk(
        0x102,
        "#0105F#12P那个，我们有些弄不清状况……\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x104,
        "#0305F#12P到底发生了什么事呢？\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x9,
        (
            "#2203F#5P嗯，其实是关于昨天和你们说的\x01",
            "那位贸易公司的经营者……\x02\x03",

            "#2201F从今天早上开始，就联系不上他了。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CCA")
    OP_63(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_8CCA")

    Sleep(1000)

    #C0374
    ChrTalk(
        0x101,
        "#0005F#12P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xC,
        (
            "#3603F#5P他经营着一家名叫『利泽罗贸易』的公司，\x01",
            "和我也算有点交情……\x02\x03",

            "#3601F他不在自己的家里，\x01",
            "公司里的人也都不知道他去了哪里。\x02\x03",

            "所以正在和律师商量，\x01",
            "是不是应该去报警……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 500)
    Sleep(150)

    #C0376
    ChrTalk(
        0x101,
        "#0006F#11P是、是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x103,
        "#0208F#12P果然……失踪了呢……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F37")
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10A)

    #C0378
    ChrTalk(
        0x10A,
        (
            "#0603F#11P……因为某些原因，\x01",
            "警方或许无法马上采取行动。\x02\x03",

            "#0600F所以，这件事能不能\x01",
            "交给支援科来解决呢？\x02\x03",

            "我也会找机会\x01",
            "向警察局总部转达情况的。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x9,
        (
            "#2202F#5P嗯……既然达德利\x01",
            "都这样说了，那自然没问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xC,
        (
            "#3600F#5P我明白了……\x01",
            "那么，这件事就交给各位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        "#0000F#11P嗯，包在我们身上。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9058")

    label("loc_8F37")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0382
    ChrTalk(
        0x101,
        (
            "#0003F#11P哈罗德先生，\x01",
            "警方因为某些原因，\x01",
            "可能无法立刻展开行动。\x02\x03",

            "#0001F所以，这件事能不能\x01",
            "交给我们支援科来解决呢？\x02\x03",

            "我们也会找机会\x01",
            "向警察局总部转达情况的。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xC,
        (
            "#3600F#5P我明白了……\x01",
            "那调查工作就拜托各位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        (
            "#0001F#11P嗯，但也许还要\x01",
            "稍微花上一些时间……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9058")

    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    #C0385
    ChrTalk(
        0x101,
        (
            "#0001F#12P伊安律师，如果以后又出现了\x01",
            "有关失踪人士方面的咨询，\x01",
            "能请您联系我们科长吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x9,
        (
            "#2201F#5P嗯……明白了，\x01",
            "我会留意的。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        "#0004F#12P不好意思，拜托您了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0388
    ChrTalk(
        0x104,
        (
            "#0308F#6P（这件事情，我们还是\x01",
            "  抓紧一点比较好……）\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#0013F#11P（嗯……现在可不是\x01",
            "  到处闲逛的时候。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91B8")

    #C0390
    ChrTalk(
        0x10A,
        "#11P#0601F（哼……赶快解决正事吧！）\x02",
    )

    CloseMessageWindow()

    label("loc_91B8")

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

    # Function_26_881C end

    SaveToFile()

Try(main)
