from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1220.bin",                # FileName
        "c1220",                    # MapName
        "c1220",                    # Location
        0x0020,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 32, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1220",                  # 0
        "接待小姐托莉亚",         # 1
        "马凯奈",                 # 2
        "雷因兹",                 # 3
        "格蕾丝",                 # 4
        "记者Ａ",                 # 5
        "记者Ｂ",                 # 6
        "记者Ｃ",                 # 7
        "记者Ｄ",                 # 8
    ))

    AddCharChip((
        "chr/ch26602.itc",                   # 00
        "chr/ch28100.itc",                   # 01
        "chr/ch06000.itc",                   # 02
        "chr/ch06002.itc",                   # 03
        "chr/ch26700.itc",                   # 04
    ))

    DeclNpc(5789,    0,       -430,    270,  341,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(5099,    0,       60020,   0,    261,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-519,    0,       360,     0,    261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 17,  -6.510000228881836,    5.110000133514404,     -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.255000114440918,     -2.555000066757202,    0.10000000149011612,   1.0])

    DeclActor(4100,    0,       -520,    1500,    5500,    1800,    -470,    0x007E, 0,  3,  0x0000)
    DeclActor(7270,    0,       54230,   1000,    7270,    1400,    54230,   0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_278",          # 00, 0
        "Function_1_330",          # 01, 1
        "Function_2_56E",          # 02, 2
        "Function_3_608",          # 03, 3
        "Function_4_72C",          # 04, 4
        "Function_5_A49",          # 05, 5
        "Function_6_B9A",          # 06, 6
        "Function_7_1E94",         # 07, 7
        "Function_8_3150",         # 08, 8
        "Function_9_3D1E",         # 09, 9
        "Function_10_477C",        # 0A, 10
        "Function_11_487D",        # 0B, 11
        "Function_12_4ACE",        # 0C, 12
        "Function_13_64D7",        # 0D, 13
        "Function_14_6671",        # 0E, 14
        "Function_15_7775",        # 0F, 15
        "Function_16_7BAB",        # 10, 16
        "Function_17_7C88",        # 11, 17
    ))


    def Function_0_278(): pass

    label("Function_0_278")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2B8"),
        (1, "loc_2C4"),
        (2, "loc_2D0"),
        (3, "loc_2DC"),
        (4, "loc_2E8"),
        (5, "loc_2F4"),
        (6, "loc_300"),
        (SWITCH_DEFAULT, "loc_30C"),
    )


    label("loc_2B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_300")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_30C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_318")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_32F")

    Return()

    # Function_0_278 end

    def Function_1_330(): pass

    label("Function_1_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_343")
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_36C")
    SetChrPos(0x9, 3100, 20, -890, 90)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3AA")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 820, 0, 220, 0)
    ClearChrFlags(0xB, 0x40)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    Jump("loc_56D")

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3B8")
    Jump("loc_56D")

    label("loc_3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3CB")
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3DE")
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3EC")
    Jump("loc_56D")

    label("loc_3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3FA")
    Jump("loc_56D")

    label("loc_3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_40D")
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_420")
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_438")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x10)
    Jump("loc_56D")

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_44B")
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_459")
    Jump("loc_56D")

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_467")
    Jump("loc_56D")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_497")
    OP_93(0xA, 0x10E, 0x0)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x9, -2140, 0, 450, 90)
    SetChrFlags(0x9, 0x10)
    Jump("loc_56D")

    label("loc_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4D7")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 470, 0, 56880, 180)
    Jump("loc_56D")

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_502")
    OP_93(0xA, 0x10E, 0x0)
    SetChrPos(0x9, -2140, 0, 450, 90)
    SetChrFlags(0x9, 0x10)
    Jump("loc_56D")

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_510")
    Jump("loc_56D")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_550")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 3580, 0, 60060, 90)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    OP_93(0x9, 0x10E, 0x0)
    Jump("loc_56D")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_568")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x10)
    Jump("loc_56D")

    label("loc_568")

    SetChrFlags(0xA, 0x80)

    label("loc_56D")

    Return()

    # Function_1_330 end

    def Function_2_56E(): pass

    label("Function_2_56E")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_590")
    OP_66(0x1, 0x1)

    label("loc_590")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A9")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    Jump("loc_5AF")

    label("loc_5A9")

    OP_10(0x0, 0x1)
    OP_10(0x5, 0x0)

    label("loc_5AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CB")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5E2")

    label("loc_5CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5E2")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5E2")

    label("loc_5E2")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_END)), "loc_5F5")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_607")
    OP_65(0x0, 0x1)

    label("loc_607")

    Return()

    # Function_2_56E end

    def Function_3_608(): pass

    label("Function_3_608")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_69C")
    Jump("loc_6E6")

    label("loc_69C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6BC")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E6")

    label("loc_6BC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DC")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E6")

    label("loc_6DC")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E6")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_721")
    Call(0, 4)
    Jump("loc_724")

    label("loc_721")

    Call(0, 6)

    label("loc_724")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_3_608 end

    def Function_4_72C(): pass

    label("Function_4_72C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_795")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_78D")

    #C0001
    ChrTalk(
        0x8,
        (
            "各位，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "格蕾丝小姐好像\x01",
            "也非常高兴，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_790")

    label("loc_78D")

    Call(0, 6)

    label("loc_790")

    Jump("loc_A48")

    label("loc_795")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_A31")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2C")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【对话】\x01",          # 0
            "【交付照片】\x01",      # 1
            "【放弃】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87A")
    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_868")

    #C0003
    ChrTalk(
        0x8,
        (
            "这期的观光指南企划案\x01",
            "是格蕾丝小姐提出的。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "为了刊物的顺利出版，\x01",
            "无论如何，请多多加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86B")

    label("loc_868")

    Call(0, 6)

    label("loc_86B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A27")

    label("loc_87A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A14")
    OP_60(0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_8AD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_8C4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_8DB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_8F2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_909")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_909")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_920")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_920")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_937")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_937")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_94E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_94E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_965")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_965")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_97C")
    Call(0, 13)
    Jump("loc_A0F")

    label("loc_97C")


    #C0005
    ChrTalk(
        0x101,
        (
            "#0005F（啊……\x01",
            "  格蕾丝小姐委托我们拍摄的\x01",
            "  照片数量是五张以上。）\x02\x03",

            "#0003F（现在手中的照片数量不够，\x01",
            "  还不能交付呢……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A0F")

    Jump("loc_A27")

    label("loc_A14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A27")
    OP_60(0x0)
    Return()

    label("loc_A27")

    Jump("loc_7AC")

    label("loc_A2C")

    Jump("loc_A48")

    label("loc_A31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_A45")
    Call(0, 11)
    Jump("loc_A48")

    label("loc_A45")

    Call(0, 6)

    label("loc_A48")

    Return()

    # Function_4_72C end

    def Function_5_A49(): pass

    label("Function_5_A49")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ADD")
    Jump("loc_B27")

    label("loc_ADD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AFD")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B27")

    label("loc_AFD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1D")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B27")

    label("loc_B1D")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B27")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    #C0006
    ChrTalk(
        0x8,
        (
            "啊，各位，\x01",
            "这边是后台啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "如果有什么需要，\x01",
            "请去柜台正面吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_5_A49 end

    def Function_6_B9A(): pass

    label("Function_6_B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C42")

    #C0008
    ChrTalk(
        0x8,
        (
            "格蕾丝小姐\x01",
            "又出去采访了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "虽然她平时也总是带着\x01",
            "雷因兹到处去调查采访，\x01",
            "不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "今天看上去好像稍微有些严肃呢，\x01",
            "是不是发生了什么恶性事件啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E93")

    label("loc_C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C50")
    Jump("loc_1E93")

    label("loc_C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_D28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CC0")

    #C0011
    ChrTalk(
        0x8,
        "……昨天晚上可真是不得了……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "……这次的事态不会是由\x01",
            "格蕾丝小姐的报道造成的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D23")

    label("loc_CC0")


    #C0013
    ChrTalk(
        0x8,
        (
            "……今天的克洛斯贝尔时代周刊\x01",
            "临时休刊了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "给读者们带来了诸多不便，\x01",
            "实在是非常抱歉……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D23")

    Jump("loc_1E93")

    label("loc_D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D7B")

    #C0015
    ChrTalk(
        0x8,
        (
            "格蕾丝小姐……\x01",
            "能不能尽量写一些\x01",
            "不会惹麻烦的报道啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE2")

    label("loc_D7B")


    #C0016
    ChrTalk(
        0x8,
        (
            "格蕾丝小姐可真是的，\x01",
            "又写了那样的新闻报道……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "已经连续好几天都有议员先生\x01",
            "前来上门问罪……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_DE2")

    Jump("loc_1E93")

    label("loc_DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_E53")

    #C0018
    ChrTalk(
        0x8,
        (
            "纪念庆典结束了，\x01",
            "最近街上真是很宁静啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "……不过，从明天开始，\x01",
            "可能就又要忙起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E93")

    label("loc_E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E92")

    #C0020
    ChrTalk(
        0x8,
        (
            "今天发行了临时增刊，\x01",
            "请大家一定要买来看啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E93")

    label("loc_E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_EEB")

    #C0021
    ChrTalk(
        0x8,
        "公园那边好像又有骚乱呢……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "继游行之后，难道\x01",
            "又要召开什么活动吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E93")

    label("loc_EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_F98")

    #C0023
    ChrTalk(
        0x8,
        (
            "今天要举行庆典的重头戏——\x01",
            "游行活动了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "各位记者都备好相机，\x01",
            "一溜烟地跑出去报道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "……喜欢这种热闹欢快的庆典，\x01",
            "大概是克洛斯贝尔人的天性吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E93")

    label("loc_F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_132A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118C")

    #C0026
    ChrTalk(
        0x8,
        (
            "各位……听说昨天\x01",
            "发生了不得了的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "虽然具体情况我没有细问，\x01",
            "但看格蕾丝小姐那一脸兴奋的表情，\x01",
            "也就基本可以想象得到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        "#0300F哈哈，是吗……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#0106F虽然早就做好了\x01",
            "被曝光的觉悟……\x02\x03",

            "#0100F不过，最后还是给格蕾丝小姐\x01",
            "提供了好的新闻素材啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        (
            "#0203F……稍微有些不愉快呢，\x01",
            "下次必须要让她给我们点补偿才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#0009F哈哈……说得也是啊。\x01",
            "下次就让她无偿为我们提供情报好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "面对着格蕾丝小姐\x01",
            "还能说出这种话的人，\x01",
            "我还是第一次见到呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB3, 3)
    Jump("loc_1325")

    label("loc_118C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1207")

    #C0034
    ChrTalk(
        0x8,
        (
            "格蕾丝小姐今天\x01",
            "也一脸兴奋地\x01",
            "出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "她很开心地说过，那是因为在纪念庆典期间\x01",
            "有很多可供报道的消息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1325")

    label("loc_1207")


    #C0036
    ChrTalk(
        0x8,
        (
            "呵呵，稍微吃了一惊呢。\x01",
            "被格蕾丝小姐报道之后不但不生气，\x01",
            "反而还要求回礼……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "特别任务支援科一定是个非常了不起的\x01",
            "地方，所以大家才如此豁达吧。\x02",
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

    #C0038
    ChrTalk(
        0x101,
        (
            "#0006F也、也并不算是\x01",
            "这样……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1325")

    Jump("loc_1E93")

    label("loc_132A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_1382")

    #C0039
    ChrTalk(
        0x8,
        (
            "不知为什么，外面好像\x01",
            "很吵闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "是不是舞台那里\x01",
            "的活动开始了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E93")

    label("loc_1382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1461")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13E7")

    #C0041
    ChrTalk(
        0x8,
        (
            "大家今天都十分开心地\x01",
            "出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "纪念庆典期间的采访报道\x01",
            "好像很有趣呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145C")

    label("loc_13E7")


    #C0043
    ChrTalk(
        0x8,
        "欢迎来到克洛斯贝尔通讯社。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "纪念庆典终于要开始了，\x01",
            "各位记者看上去也都特别忙碌。\x01",
            "整天都在街上四处奔走呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_145C")

    Jump("loc_1E93")

    label("loc_1461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_154A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14C5")

    #C0045
    ChrTalk(
        0x8,
        (
            "呼，Ｂ席票就可以了，\x01",
            "不知道还有没有剩下的。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "不然就去问问总编吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1545")

    label("loc_14C5")


    #C0047
    ChrTalk(
        0x8,
        (
            "距离彩虹剧团的预演，\x01",
            "已经只剩不到两周的时间了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "……真羡慕那些\x01",
            "能去采访的记者啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "因为我最后\x01",
            "也没有买到票。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1545")

    Jump("loc_1E93")

    label("loc_154A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1646")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15E4")

    #C0050
    ChrTalk(
        0x8,
        (
            "干记者这一行，总会\x01",
            "遇到各种各样的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "嗯嗯，不要沮丧，不要沮丧。\x01",
            "如果想成为一名真正的记者，\x01",
            "就必须要克服这些困难啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1641")

    label("loc_15E4")


    #C0052
    ChrTalk(
        0x8,
        (
            "不知为何，雷因兹今天\x01",
            "看起来好像很沮丧……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "真是少见啊，\x01",
            "平时一向都很有精神的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1641")

    Jump("loc_1E93")

    label("loc_1646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_177B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16C2")

    #C0054
    ChrTalk(
        0x8,
        (
            "鲁巴彻商会的黑衣人\x01",
            "经常会前来拜访。\x01",
            "唉……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "真不理解总编为什么可以\x01",
            "那么泰然自若地应对他们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1776")

    label("loc_16C2")


    #C0056
    ChrTalk(
        0x8,
        (
            "鲁巴彻商会的人\x01",
            "经常会前来拜访。\x01",
            "和总编谈一些事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "虽然没有出现暴力行为，\x01",
            "但口头威吓，或是敲桌子之类，\x01",
            "公然的威胁行为却是屡见不鲜……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "呼……那些人\x01",
            "果然很可怕啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1776")

    Jump("loc_1E93")

    label("loc_177B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1877")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17E2")

    #C0059
    ChrTalk(
        0x8,
        (
            "格蕾丝小姐最近\x01",
            "好像很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "唉……只希望她别再写些\x01",
            "惹人不满的报道了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1872")

    label("loc_17E2")


    #C0061
    ChrTalk(
        0x8,
        (
            "格蕾丝小姐最近的采访工作\x01",
            "好像很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "似乎是出差刚刚回来，\x01",
            "马上就开始四处奔波了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "她大概又要去调查那些艺人丑闻\x01",
            "之类的素材吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1872")

    Jump("loc_1E93")

    label("loc_1877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1980")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1903")

    #C0064
    ChrTalk(
        0x8,
        (
            "……其实，为了进行宣传，\x01",
            "彩虹已经向各大媒体派发了\x01",
            "预演的门票。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "但我并不是记者，\x01",
            "所以只能自己排队去买票了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197B")

    label("loc_1903")


    #C0066
    ChrTalk(
        0x8,
        (
            "刚才无意中\x01",
            "听到了一件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "彩虹剧团新剧的公演门票\x01",
            "好像就要开始出售了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "呼，真好啊……\x01",
            "我也好想去看呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_197B")

    Jump("loc_1E93")

    label("loc_1980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_19C8")

    #C0069
    ChrTalk(
        0x8,
        (
            "格蕾丝小姐\x01",
            "刚才微笑着\x01",
            "出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        "又要去采访吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E93")

    label("loc_19C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1A9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A30")

    #C0071
    ChrTalk(
        0x8,
        (
            "啊……\x01",
            "请问各位来克洛斯贝尔通讯社有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        "有事的话，请尽管吩咐哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_1A30")


    #C0073
    ChrTalk(
        0x8,
        (
            "本社是去年搬进\x01",
            "这个办公地点的。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "所以还堆积着很多的\x01",
            "资料没有整理呢。\x01",
            "必须要找点时间整理好啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A9A")

    Jump("loc_1E93")

    label("loc_1A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1C7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B3D")

    #C0075
    ChrTalk(
        0x8,
        (
            "呼，虽然并不都是格蕾丝小姐\x01",
            "一个人造成的……\x01",
            "但投诉太多的话，实在是应付不了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "真希望他们能多写点\x01",
            "不会惹麻烦的新闻报道啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C77")

    label("loc_1B3D")


    #C0077
    ChrTalk(
        0x8,
        (
            "本社主要面向经济、国际、社会、\x01",
            "演艺等方面进行报道。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "特别是社会方面……登载过很多\x01",
            "爆炸性消息，揭露过很多秘闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "唉，格蕾丝小姐……\x01",
            "能不能尽量写一些\x01",
            "不会惹麻烦的报道啊……\x02",
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

    #C0080
    ChrTalk(
        0x101,
        "#0006F（那个人啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C77")

    Jump("loc_1E93")

    label("loc_1C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D20")

    #C0081
    ChrTalk(
        0x8,
        (
            "在我们克洛斯贝尔通讯社……\x01",
            "经常会有被报道内容惹怒，\x01",
            "前来怒骂抗议的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "那个，如果有什么意见，\x01",
            "请不要客气，尽量提出。\x01",
            "我会帮您把总编叫来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E93")

    label("loc_1D20")


    #C0083
    ChrTalk(
        0x8,
        "欢迎来到克洛斯贝尔通讯社。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "本社的报道对您造成了\x01",
            "什么不便吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D98")

    #C0085
    ChrTalk(
        0x101,
        "#0005F哎？不，并没有……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E28")

    label("loc_1D98")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DC9")

    #C0086
    ChrTalk(
        0x102,
        "#0105F哎？不，没有的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E28")

    label("loc_1DC9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DF8")

    #C0087
    ChrTalk(
        0x103,
        "#0205F哎？不，没有……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E28")

    label("loc_1DF8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E28")

    #C0088
    ChrTalk(
        0x104,
        "#0305F……嗯？不，没有啦……\x02",
    )

    CloseMessageWindow()

    label("loc_1E28")


    #C0089
    ChrTalk(
        0x8,
        "呵，是吗……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "如果对本社的报道\x01",
            "有什么意见，\x01",
            "请不要客气，尽量提出。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        "我会帮您把总编叫来的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E93")

    Return()

    # Function_6_B9A end

    def Function_7_1E94(): pass

    label("Function_7_1E94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1F12")

    #C0092
    ChrTalk(
        0xFE,
        (
            "嗯……？\x01",
            "为什么一直盯着我们的奖状看啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "看看倒是没关系，\x01",
            "但最好不要碰。\x01",
            "因为这是宝贵的荣誉证明啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_314C")

    label("loc_1F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_201C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F87")

    #C0094
    ChrTalk(
        0xFE,
        (
            "空港好像被封锁了……\x01",
            "虽然去调查了，但还是一无所获。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "真是的，最近的\x01",
            "怪事可真多啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2017")

    label("loc_1F87")


    #C0096
    ChrTalk(
        0xFE,
        (
            "因为空港被封锁了，\x01",
            "所以我前去采访……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "结果看到搜查一科的人把守在那里，\x01",
            "但不管怎么问，他们却坚称什么都没发生，\x01",
            "真是让人无法释然啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2017")

    Jump("loc_314C")

    label("loc_201C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_20F4")

    #C0098
    ChrTalk(
        0x9,
        (
            "听说空港从今天早上开始\x01",
            "就被临时封锁了……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "但警察局的官方消息并不可信啊，\x01",
            "我还是过去稍微看看好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "那么，要是格蕾丝小姐\x01",
            "回来了，就帮我和她说一声，\x01",
            "照片就放在办公桌上。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        "好的，明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_314C")

    label("loc_20F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2264")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_216E")

    #C0102
    ChrTalk(
        0xFE,
        (
            "这一带是办公区。\x01",
            "听说这里的治安很好，\x01",
            "不过呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "为了保险起见，是不是\x01",
            "应该再设个后门呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225F")

    label("loc_216E")


    #C0104
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔还是一样，在安宁的表皮\x01",
            "之下，其实是个很危险的城市呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "顺便一说，周刊社还在以前的那个大楼时，\x01",
            "为了防止受到袭击，\x01",
            "特意开设了后门呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "虽然会有遭到袭击的可能性，\x01",
            "但我们是不会停笔的……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "因为这就是我们的荣耀啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_225F")

    Jump("loc_314C")

    label("loc_2264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_22E3")

    #C0108
    ChrTalk(
        0xFE,
        (
            "最近，关于黑手党之间\x01",
            "冲突摩擦的事件好像很多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "哎呀呀……难道又要\x01",
            "开战了吗？\x01",
            "真是些死不悔改的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_314C")

    label("loc_22E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2344")

    #C0110
    ChrTalk(
        0xFE,
        "噢，都已经中午了吗……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "到公园的露天店吃点东西吧，\x01",
            "我很喜欢那里的面条呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_314C")

    label("loc_2344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_24B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2412")

    #C0112
    ChrTalk(
        0xFE,
        (
            "菲利策奖\x01",
            "是颁发给全大陆\x01",
            "最优秀记者的奖项。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "对我们这些靠写报道为生的人而言，\x01",
            "那是无可置疑的最高荣誉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "看啊，摆放在那里的就是\x01",
            "菲利策奖的奖状。\x01",
            "愿意的话，可以靠近看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24AF")

    label("loc_2412")


    #C0115
    ChrTalk(
        0xFE,
        "你们知道菲利策奖吗？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "那是每年，从整个大陆选出最优秀\x01",
            "的记者，并向其颁发的奖项。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "对我们这些靠写报道为生的人而言，\x01",
            "那是无可置疑的最高荣誉啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_24AF")

    Jump("loc_314C")

    label("loc_24B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2586")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2513")

    #C0118
    ChrTalk(
        0xFE,
        (
            "将照片显像，然后再检查一下……\x01",
            "总算是勉强能赶上\x01",
            "明天的特别刊啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2581")

    label("loc_2513")


    #C0119
    ChrTalk(
        0xFE,
        (
            "看游行时因为太过兴奋，\x01",
            "照片拍多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "其他人好像也都拍了不少……\x01",
            "不赶快显像的话，\x01",
            "可就用不上了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2581")

    Jump("loc_314C")

    label("loc_2586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_25F8")

    #C0121
    ChrTalk(
        0xFE,
        (
            "哦，距离游行开始，\x01",
            "还有一些时间啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "不如先把肚子填饱吧。\x01",
            "肚子要是一饿，干什么都干不好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_314C")

    label("loc_25F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2659")

    #C0123
    ChrTalk(
        0xFE,
        "哦，有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "不好意思，我已经忙得焦头烂额了。\x01",
            "实在是没空接待客人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_314C")

    label("loc_2659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_26B5")

    #C0125
    ChrTalk(
        0xFE,
        (
            "嗯～这张照片……还有……\x01",
            "大家都拍了一大堆照片，\x01",
            "光是显像就要累死人了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_314C")

    label("loc_26B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_27E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2742")

    #C0126
    ChrTalk(
        0xFE,
        (
            "那么……在纪念庆典期间，也保持住\x01",
            "这种势头，多来点爆炸性的大新闻吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "……这样一来，倒是\x01",
            "正合了总编的心意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_2742")


    #C0128
    ChrTalk(
        0xFE,
        (
            "呼，真是的……\x01",
            "上一期的报道就是勉强赶上截稿期限的。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "总编那家伙，竟然还让我\x01",
            "来写照片说明。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "……算啦，也多亏如此，\x01",
            "才能刊登出爆炸性的大消息啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_27E2")

    Jump("loc_314C")

    label("loc_27E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_28A8")

    #C0131
    ChrTalk(
        0xFE,
        (
            "贴在那里的奖状\x01",
            "是我们周刊社以前取得的\x01",
            "菲利策奖。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "当时，我们周刊社有一位传说中的记者，\x01",
            "全靠那个人，才能得到\x01",
            "这份荣誉无比的表彰啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "呼……那个人\x01",
            "也算是我们的目标吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_314C")

    label("loc_28A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_29DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2970")

    #C0134
    ChrTalk(
        0xFE,
        (
            "雷因兹那家伙，\x01",
            "摄影的才能相当了得。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "而且反射神经也很不错，能拍出\x01",
            "和新闻报道搭配得天衣无缝的好照片。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "在采访彩虹剧团这类重要的任务中，\x01",
            "他也算是个难得的人才啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_29D8")

    label("loc_2970")


    #C0137
    ChrTalk(
        0xFE,
        (
            "雷因兹那家伙，\x01",
            "玩相机的技术非常厉害。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "而且那种一丝不苟的认真性格，\x01",
            "好像也与格蕾丝相当默契呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D8")

    Jump("loc_314C")

    label("loc_29DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2A71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A69")
    TurnDirection(0xFE, 0x0, 0)

    #C0139
    ChrTalk(
        0xFE,
        "（呵，不过目前还是个正在进修的新人啊。）\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "（必须要让他好好熟悉一下\x01",
            "  我们记者的工作流程啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x0)
    Jump("loc_2A6C")

    label("loc_2A69")

    Call(0, 10)

    label("loc_2A6C")

    Jump("loc_314C")

    label("loc_2A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B50")

    #C0141
    ChrTalk(
        0xFE,
        (
            "我们把社会方面的新闻\x01",
            "交给雷因兹那家伙负责了……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "虽然只是个新人，但交上来\x01",
            "的东西还真是不错嘛。\x01",
            "特别是照片的质量，简直堪称一流啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "嘿，再多锻炼一下的话，\x01",
            "也许能成为一名很棒的记者呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2BC0")

    label("loc_2B50")


    #C0144
    ChrTalk(
        0xFE,
        "好，我差不多也该出去采访了。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "下个月有彩虹剧团的公演，\x01",
            "还有自治州的创立纪念庆典……\x01",
            "嘿，又有得忙了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC0")

    Jump("loc_314C")

    label("loc_2BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2C20")

    #C0146
    ChrTalk(
        0xFE,
        (
            "啊～不要再嘀咕个没完没了，\x01",
            "赶快决定吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "我能做的也只是帮把手而已。\x02",
    )

    CloseMessageWindow()
    Jump("loc_314C")

    label("loc_2C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2D15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2CA5")

    #C0148
    ChrTalk(
        0xFE,
        (
            "『ＩＢＣ推行的新事业』吗？\x01",
            "确实是令人很感兴趣的题材呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "好，在目前的阶段，先是要\x01",
            "采访总裁，然后……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D10")

    label("loc_2CA5")


    #C0150
    ChrTalk(
        0xFE,
        (
            "哦，有什么事吗，\x01",
            "格蕾丝出差了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "眼下，她应该正在\x01",
            "帝都狂按快门吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_9E(0x9, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x9, 0x10)

    label("loc_2D10")

    Jump("loc_314C")

    label("loc_2D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2EC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E3C")
    OP_4B(0xB, 0xFF)
    OP_93(0xFE, 0x10E, 0x0)

    #C0152
    ChrTalk(
        0x9,
        (
            "确实是个很令人瞩目的事件，\x01",
            "但我们已经准备好，要与《帝国时报》\x01",
            "进行联合报道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        "格蕾丝，即使如此，你也要去吗？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        (
            "#2104F当然啦，既然是帝国的纪念仪式，\x01",
            "自然也就是一次可以直接拜会\x01",
            "埃雷波尼亚皇室成员的绝佳机会。\x02\x03",

            "#2102F我还是想亲自\x01",
            "前去采访啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EC2")

    label("loc_2E3C")

    OP_4B(0xB, 0xFF)
    OP_93(0xFE, 0x10E, 0x0)

    #C0155
    ChrTalk(
        0xFE,
        (
            "也是，既然总编已经同意，\x01",
            "那我也就没必要多说什么了。\x01",
            "你就充满干劲地出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "#2109F多谢¤\x01",
            "这件事就交给我吧～！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_2EC2")

    Jump("loc_314C")

    label("loc_2EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3009")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC7")

    #C0157
    ChrTalk(
        0xFE,
        (
            "（啪啪）……\x01",
            "社会方面的照片就是这些吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "关于警察局的那个什么什么科……\x01",
            "算了，延后再处理就是了。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "而且格蕾丝也说过以后\x01",
            "再报道之类的话了。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        "#0106F（…………………………）\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        "#0006F（真担心她会写出些什么啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3004")

    label("loc_2FC7")


    #C0162
    ChrTalk(
        0xFE,
        (
            "关于警察局新设立的那个什么什么科\x01",
            "……算了，延后处理吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3004")

    Jump("loc_314C")

    label("loc_3009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3077")

    #C0163
    ChrTalk(
        0xFE,
        (
            "……怎么，你们真的\x01",
            "不是来闹事的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "要是没什么事，就赶快回去吧。\x01",
            "会打扰到我们工作的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_314C")

    label("loc_3077")


    #C0165
    ChrTalk(
        0xFE,
        "（啪啪）……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "嗯？你们几个是来干什么的？\x01",
            "是来闹事的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "嘿嘿，想来我们编辑部闹事，\x01",
            "你们还早了一百年呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "不管是黑道势力还是其它什么，\x01",
            "都别想打垮我们克洛斯贝尔时代周刊社。\x01",
            "小家伙，好好记住吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_314C")

    TalkEnd(0xFE)
    Return()

    # Function_7_1E94 end

    def Function_8_3150(): pass

    label("Function_8_3150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3458")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_323F")

    #C0169
    ChrTalk(
        0xB,
        (
            "#2103F总之，在采访议会状况的同时，\x01",
            "也要跟踪报道哈尔特曼议长，\x01",
            "还要查明黑手党的内部秘情……\x02\x03",

            "嗯，收集情报的途中，\x01",
            "要随时留意关于药物的情报。\x02\x03",

            "#2100F啊，要是了解到什么情况，\x01",
            "马上就会告诉你们的～\x01",
            "请多多指教～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3450")

    label("loc_323F")


    #C0170
    ChrTalk(
        0xB,
        (
            "#2103F那么，采访采访……\x02\x03",

            "………………………………\x02\x03",

            "#2102F喂，刚才那个叫雷克特的孩子，\x01",
            "和你们是什么关系啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x104,
        (
            "#0300F啊～这个嘛，\x01",
            "只是有过一面之缘而已吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#0006F……我们和他\x01",
            "也不是很熟呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "#2100F哼～是这样啊。\x01",
            "……好像在什么地方听到过这个名字，\x01",
            "让我有点在意呢。\x02\x03",

            "#2103F雷克特，雷克特……\x01",
            "嗯～在哪里听过呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x102,
        (
            "#0100F他好像是帝国的人……\x01",
            "您是不是在那边采访时听到过呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0175
    ChrTalk(
        0xB,
        (
            "#2105F啊～也许吧。\x01",
            "不过究竟是在哪里听到的呢～\x02\x03",

            "#2103F……算了，先不管了。\x01",
            "还有其它堆积如山的采访任务要处理呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCF, 0)

    label("loc_3450")

    TalkEnd(0xFE)
    Jump("loc_3D1D")

    label("loc_3458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_395A")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34F5")
    Jump("loc_353F")

    label("loc_34F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3515")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_353F")

    label("loc_3515")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3535")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_353F")

    label("loc_3535")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_353F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 3)), scpexpr(EXPR_END)), "loc_3622")

    #C0176
    ChrTalk(
        0xB,
        (
            "#2100F各位，最近的工作\x01",
            "进展如何啊？\x02\x03",

            "#2109F要是有什么有趣奇怪的消息，\x01",
            "可一定要告诉\x01",
            "姐姐我哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#0003F好了，各位。\x01",
            "我们快点回去工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xB,
        "#2106F呜呜，反应好冷淡啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_394E")

    label("loc_3622")

    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0179
    ChrTalk(
        0xB,
        (
            "#2105F啊，这不是支援科的各位嘛。\x02\x03",

            "#2102F哎呀～好久不见呢。\x01",
            "关于上个月那起魔兽骚乱事件的报道，\x01",
            "我已经读过了哦。\x02\x03",

            "#2109F嗯嗯，\x01",
            "看来你们很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0000F格蕾丝小姐……\x01",
            "好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x102,
        (
            "#0100F说起来，那篇报道好像\x01",
            "不是格蕾丝小姐写的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xB,
        (
            "#2100F嗯，我当时要外出采访，\x01",
            "所以不在克洛斯贝尔哦。\x02\x03",

            "#2103F如果可以的话，倒是\x01",
            "真希望由我来采访你们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        "#0200F……没采访成也许是幸运呢。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x104,
        (
            "#0306F哈，如果总是给我们写那种报道，\x01",
            "实在是让人泄气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        (
            "#2103F哎呀呀，我一直都在默默守护你们的成长，\x01",
            "如此深切的感情，你们怎么就不能体会呢～\x02\x03",

            "#2109F呵呵，在此相遇，也算是缘分。\x01",
            "你们在最近的工作中有没有遇到一些有趣奇怪的……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#0003F……格蕾丝小姐\x01",
            "好像正在休息呢。\x01",
            "我们实在是打搅了，走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x103,
        "#0203F请加油工作。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xB,
        (
            "#2105F哎，咦？\x01",
            "大家这就要走了吗？\x02\x03",

            "#2106F啊～这也未免\x01",
            "太冷淡了吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 3)

    label("loc_394E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_3D1D")

    label("loc_395A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7F")
    TurnDirection(0xB, 0x0, 0)

    #C0189
    ChrTalk(
        0xB,
        (
            "#2100F哎呀，这不是支援科的各位嘛。\x02\x03",

            "#2109FＨｅｌｌｏ、ｈｅｌｌｏ，最近还好吗～？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 1)), scpexpr(EXPR_END)), "loc_3A39")

    #C0190
    ChrTalk(
        0x101,
        "#0006F什么『Ｈｅｌｌｏ、ｈｅｌｌｏ』啊。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x103,
        (
            "#0200F……您好像又自作主张地\x01",
            "乱写一些报道文章了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A96")

    label("loc_3A39")


    #C0192
    ChrTalk(
        0x101,
        "#0006F还真是坦然自若呢……\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        (
            "#0100F您没打算把前几天的那件事\x01",
            "又写成那么奇怪的报道吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A96")


    #C0194
    ChrTalk(
        0xB,
        (
            "#2102F呵呵，别生气，别生气嘛。\x02\x03",

            "姐姐我一直\x01",
            "都在声援你们啦。\x02\x03",

            "#2103F啊，不过，真抱歉啊～\x01",
            "这周稍微有点忙，\x01",
            "就没法顾及你们啦。\x02\x03",

            "#2102F在我回来之前，你们就多创造\x01",
            "一点有趣的新闻素材吧⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        "#0006F唉……\x02",
    )

    CloseMessageWindow()
    OP_9E(0xB, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    SetScenarioFlags(0x6D, 1)
    Jump("loc_3D1A")

    label("loc_3B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3C10")
    TurnDirection(0xB, 0x0, 0)

    #C0196
    ChrTalk(
        0xB,
        (
            "#2102F不好意思啊～姐姐我\x01",
            "这周稍微有点忙，\x01",
            "就没法顾及你们啦。\x02\x03",

            "在我回来之前，你们就多创造\x01",
            "一点有趣的新闻素材吧⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x0)
    Jump("loc_3D1A")

    label("loc_3C10")

    OP_4B(0x9, 0xFF)

    #C0197
    ChrTalk(
        0x9,
        (
            "那确实是个很令人瞩目的事件，\x01",
            "但我们已经准备好，要与《帝国时报》\x01",
            "进行联合报道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x9,
        "格蕾丝，即使如此，你也要去吗？\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        (
            "#2103F当然啦，既然是帝国的纪念仪式，\x01",
            "自然也就是一次可以直接拜会\x01",
            "埃雷波尼亚皇室成员的绝佳机会。\x02\x03",

            "#2109F我还是想亲自\x01",
            "前去采访啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)

    label("loc_3D1A")

    TalkEnd(0xFE)

    label("loc_3D1D")

    Return()

    # Function_8_3150 end

    def Function_9_3D1E(): pass

    label("Function_9_3D1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3E13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3DB0")

    #C0200
    ChrTalk(
        0xFE,
        (
            "（采访黑手党之类的事情，\x01",
            "  我可绝对不想去做……）\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "（相比之下，去报道那乱七八糟的议会\x01",
            "  可就要轻松好几倍了！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E0E")

    label("loc_3DB0")

    OP_4B(0xB, 0xFF)

    #C0202
    ChrTalk(
        0xB,
        "那个，要去报道议会～¤\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "（难、难道要让我\x01",
            "  也去帮忙吗……\x01",
            "  这……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xB, 0xFF)

    label("loc_3E0E")

    Jump("loc_4778")

    label("loc_3E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3E88")

    #C0204
    ChrTalk(
        0xFE,
        (
            "前辈出去了，今天好像\x01",
            "是要去采访些什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "议会那方面的报道\x01",
            "就交付给我了……\x01",
            "呼，必须要加油啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4778")

    label("loc_3E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3FBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3ED6")

    #C0206
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈刚才\x01",
            "出门了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "到底去哪里了呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FB5")

    label("loc_3ED6")


    #C0208
    ChrTalk(
        0xFE,
        (
            "好～今天就去报道闭幕式\x01",
            "和工商协会的舞台活动……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "啊，之后也可以给开往\x01",
            "米修拉姆的水上巴士\x01",
            "拍几张照片。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0210
    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "格蕾丝前辈刚才\x01",
            "出门了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "前辈不在的时候，\x01",
            "我总是很不在状态呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3FB5")

    Jump("loc_4778")

    label("loc_3FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_40C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_403F")

    #C0212
    ChrTalk(
        0xFE,
        (
            "嗯……是先去中央广场，\x01",
            "还是去港湾区的舞台呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "……如果去问前辈的话，她肯定会说\x01",
            "两个地方都去吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40BF")

    label("loc_403F")


    #C0214
    ChrTalk(
        0xFE,
        "啊，支援科的各位……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈正在二楼\x01",
            "忙着写新闻报道呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "她让我去拍摄\x01",
            "目前缺少的照片。\x01",
            "呼，还要再跑一趟啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_40BF")

    Jump("loc_4778")

    label("loc_40C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_41E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4131")

    #C0217
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈好像正在\x01",
            "着迷地调查些什么东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "最近基本都不在\x01",
            "周刊社里露面了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41DB")

    label("loc_4131")


    #C0219
    ChrTalk(
        0xFE,
        (
            "差不多该到预演的日子了啊……\x01",
            "必须要准备好采访彩虹剧团的行程表。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "……说起来，格蕾丝前辈最近\x01",
            "好像正在调查些什么东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "这段时间基本都不在\x01",
            "社内露面了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_41DB")

    Jump("loc_4778")

    label("loc_41E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_42F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4265")

    #C0222
    ChrTalk(
        0xFE,
        (
            "算了，只要能把采访彩虹剧团的事情做好，\x01",
            "我也就没什么意见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "我并不是摄影师，\x01",
            "而是记者啊，真是的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F3")

    label("loc_4265")


    #C0224
    ChrTalk(
        0xFE,
        (
            "这次去采访彩虹剧团，\x01",
            "我将以摄影师的身份\x01",
            "随行前往。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "……总编真是过分啊，\x01",
            "竟然说『你就不用写报道了』。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        "真是郁闷……唉，算了～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_42F3")

    Jump("loc_4778")

    label("loc_42F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_434E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4346")

    #C0227
    ChrTalk(
        0xFE,
        (
            "呜呜，我唯一的专栏报道就这么……\x01",
            "怎么可以这样～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4349")

    label("loc_4346")

    Call(0, 10)

    label("loc_4349")

    Jump("loc_4778")

    label("loc_434E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4473")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_43BC")

    #C0228
    ChrTalk(
        0xFE,
        (
            "上次狼形魔兽事件的报道，\x01",
            "就是由我负责的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "如果不嫌弃，请各位也读一读吧～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_446E")

    label("loc_43BC")


    #C0230
    ChrTalk(
        0xFE,
        "啊，是特别任务支援科的各位吧。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "上次的狼形魔兽事件，\x01",
            "是由我来负责报道的。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "我负责的报道还是第一次\x01",
            "登上刊物的头版呢，\x01",
            "真是很开心啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "兴奋感一直持续到现在呢～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_446E")

    Jump("loc_4778")

    label("loc_4473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4554")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_44D5")

    #C0234
    ChrTalk(
        0xFE,
        "竟然让我这种新人负责社会版块……\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "到底该从何下手呢，\x01",
            "完全不懂啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_454F")

    label("loc_44D5")


    #C0236
    ChrTalk(
        0xFE,
        (
            "因为格蕾丝前辈出差去了，\x01",
            "所以我就代为负责社会版块。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "呜哇，好紧张啊～\x01",
            "说起来，马凯奈先生\x01",
            "也真是够乱来的啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_454F")

    Jump("loc_4778")

    label("loc_4554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_469E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_45C3")

    #C0238
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈这个星期\x01",
            "出差去了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "前辈不在的时候真安静，\x01",
            "……稍微有点寂寞呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4699")

    label("loc_45C3")


    #C0240
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈今天不在，\x01",
            "编辑会议很快就结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈在编辑会议上\x01",
            "也是马力全开，精神十足呢，\x01",
            "经常会发起一些很激烈的论战。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "哈，不过，正因如此，\x01",
            "才能写出那么多优秀的报道，\x01",
            "所以也不是什么坏事哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4699")

    Jump("loc_4778")

    label("loc_469E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_46F5")

    #C0243
    ChrTalk(
        0xFE,
        (
            "即使只分到一些琐碎的报道，\x01",
            "我也是很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        "好～要加油干啦～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4778")

    label("loc_46F5")


    #C0245
    ChrTalk(
        0xFE,
        "好～接下来的专栏是……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "我最近总算\x01",
            "可以开始写\x01",
            "新闻报道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "哇～……！\x01",
            "虽然只是文化方面的小专栏，\x01",
            "但还是很高兴啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4778")

    TalkEnd(0xFE)
    Return()

    # Function_9_3D1E end

    def Function_10_477C(): pass

    label("Function_10_477C")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0248
    ChrTalk(
        0xA,
        "哎……摄影师吗？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x9,
        "嗯，你不是很擅长摄影吗？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x9,
        (
            "这次采访彩虹剧团的任务，\x01",
            "我还缺一名摄影师。\x01",
            "你就来帮个忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xA,
        (
            "那个～可是我还有\x01",
            "烹饪专栏的工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x9,
        "那个暂时就先别管啦。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0253
    ChrTalk(
        0xA,
        "咦咦，怎么可以这样……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_10_477C end

    def Function_11_487D(): pass

    label("Function_11_487D")

    EventBegin(0x0)
    Fade(500)
    OP_68(3050, 1520, -1840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20950, 0)
    SetChrPos(0x101, 2700, 20, -2000, 90)
    SetChrPos(0x102, 2700, 20, -700, 90)
    SetChrPos(0x103, 1400, 20, -2000, 90)
    SetChrPos(0x104, 1400, 20, -700, 90)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A41")

    #C0254
    ChrTalk(
        0x8,
        "#11P欢迎来到克洛斯贝尔通讯社。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        "#11P今天有何贵干呢？\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#12P#0000F我们是特别任务支援科的人。\x02\x03",

            "前来受理贵社提出的\x01",
            "支援请求。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        (
            "#11P哦，各位就是……\x01",
            "远道而来，实在是感激不尽。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "#11P关于委托的内容，\x01",
            "相关人员希望能面对面\x01",
            "向你们直接交代……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x8,
        "#11P时间方面没什么问题吧？\x02",
    )

    CloseMessageWindow()
    OP_29(0x18, 0x1, 0x0)
    Call(0, 12)
    Jump("loc_4ACD")

    label("loc_4A41")


    #C0260
    ChrTalk(
        0x8,
        (
            "#11P……要办的事已经\x01",
            "都办完了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "#11P关于委托的内容，\x01",
            "相关人员希望能面对面\x01",
            "向你们直接交代……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        "#11P时间方面没什么问题吧？\x02",
    )

    CloseMessageWindow()
    Call(0, 12)

    label("loc_4ACD")

    Return()

    # Function_11_487D end

    def Function_12_4ACE(): pass

    label("Function_12_4ACE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4B08"),
        (1, "loc_63F5"),
        (SWITCH_DEFAULT, "loc_64BD"),
    )


    label("loc_4B08")

    OP_60(0x0)

    #C0263
    ChrTalk(
        0x101,
        "#12P#0000F嗯，那烦请带路吧。\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x8,
        "#11P明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B8C")

    #C0265
    ChrTalk(
        0x8,
        (
            "#11P那么，就麻烦各位\x01",
            "上二楼吧。\x01",
            "负责人在等着你们呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BCC")

    label("loc_4B8C")


    #C0266
    ChrTalk(
        0x8,
        (
            "#11P那么，就麻烦各位\x01",
            "到二楼稍等片刻吧，\x01",
            "我去将负责人叫来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BCC")


    #C0267
    ChrTalk(
        0x101,
        (
            "#12P#0000F好的，明白了。\x02\x03",

            "#0003F（总之，先上去看看吧……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(63810, 1500, -70, 0)
    MoveCamera(38, 27, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(27050, 0)
    LoadChrToIndex("chr/ch20200.itc", 0x1E)
    LoadChrToIndex("chr/ch30202.itc", 0x1F)
    LoadChrToIndex("chr/ch23600.itc", 0x20)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xC, 67320, 0, 12770, 0)
    SetChrPos(0xD, 57840, 0, 6320, 0)
    SetChrPos(0xE, 67050, 0, -170, 135)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 60010, 150, 10690, 270)
    SetChrPos(0x101, 58200, 0, 11760, 135)
    SetChrPos(0x102, 58650, 0, 12660, 135)
    SetChrPos(0x103, 57000, 0, 11920, 135)
    SetChrPos(0x104, 57480, 0, 13060, 135)
    OP_68(58950, 1500, 9840, 8000)
    FadeToBright(500, 0)
    OP_0D()

    def lambda_4D56():
        OP_95(0xFE, 67320, 0, 5770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4D56)
    WaitChrThread(0xC, 1)

    def lambda_4D74():
        OP_95(0xFE, 55550, 0, 5030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4D74)
    OP_6F(0x1)
    Fade(1000)
    OP_68(57910, 1500, 11780, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(20010, 0)
    OP_0D()

    #C0268
    ChrTalk(
        0xB,
        (
            "#11P#2109FＨｅｌｌｏ、ｈｅｌｌｏ～\x01",
            "特别任务支援科的各位⊥\x02",
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

    #C0269
    ChrTalk(
        0x101,
        "#12P#0003F格、格蕾丝小姐……\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x102,
        "#5P#0106F虽然早有预料……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4F84")

    #C0271
    ChrTalk(
        0xB,
        (
            "#11P#2105F什么嘛～\x01",
            "你们这种反应也太差劲了吧。\x02\x03",

            "#2109F难得我在如此百忙之中\x01",
            "还特意把你们给叫来，\x01",
            "你们应该再高兴一点才对嘛～\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x103,
        (
            "#12P#0203F不明白您在说什么。\x02\x03",

            "#0200F……能不能尽量简洁地\x01",
            "向我们说明委托内容呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E2")

    label("loc_4F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5232")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5159")

    #C0273
    ChrTalk(
        0xB,
        (
            "#11P#2100F呵呵，昨天真是辛苦啦！\x02\x03",

            "#2109F我会尽快将昨天的竞赛\x01",
            "写成一篇有趣的报道哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x104,
        (
            "#6P#0306F果然要将那个\x01",
            "写成报道吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xB,
        (
            "#11P#2100F对对，应该会登在纪念庆典最终日\x01",
            "发行的临时特别刊上。\x02\x03",

            "#2109F到时一定会把你们的活跃展示给大家，\x01",
            "请尽情期待吧⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        (
            "#12P#0006F（她的文章，表面上像是在赞扬我们，\x01",
            "  其实绝对是想让我们难堪吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x103,
        (
            "#12P#0203F（算了，反正一向如此。）\x02\x03",

            "#0200F……比起那些，\x01",
            "还是请您先将委托内容\x01",
            "做个简洁的说明如何？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 0)
    Jump("loc_522D")

    label("loc_5159")


    #C0278
    ChrTalk(
        0xB,
        (
            "#11P#2105F什么嘛～\x01",
            "你们这种反应也太差劲了吧。\x02\x03",

            "#2109F难得我在如此百忙之中\x01",
            "还特意把你们给叫来，\x01",
            "你们应该再高兴一点才对嘛～\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        (
            "#12P#0203F不明白您在说什么。\x02\x03",

            "#0200F……能不能尽量简洁地\x01",
            "向我们说明委托内容呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_522D")

    Jump("loc_55E2")

    label("loc_5232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_550E")

    #C0280
    ChrTalk(
        0xB,
        (
            "#11P#2109F哎呀～之前的爆炸性大新闻，\x01",
            "可真是多谢你们了啊！\x02\x03",

            "全靠你们，才能写出那种引人注目的报道。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        "#12P#0006F呼……还真是得意忘形啊。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x103,
        (
            "#12P#0200F我们那么做并不是为了\x01",
            "给格蕾丝小姐提供什么新闻素材。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x102,
        (
            "#5P#0106F……虽然心情有些复杂……\x02\x03",

            "#0100F但那篇报道的立场总算是\x01",
            "对外公表示同情，我也就安心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xB,
        (
            "#11P#2106F哈，关于帝国派的新闻都不能写，\x01",
            "如果光把矛头指向市长，\x01",
            "就未免太不公平了～\x02\x03",

            "#2100F而且，你的外公在市民中\x01",
            "也有着相当高的人气与威望，\x01",
            "就我个人而言，也很支持他呢。\x02\x03",

            "#2102F身为记者，这样做也许有些不称职，\x01",
            "但我实在是不愿意写他的坏话～\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x102,
        "#5P#0100F格蕾丝小姐……\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x104,
        (
            "#6P#0300F嗯，记者也是人啊，\x01",
            "你这种做法不是很好嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x103,
        (
            "#12P#0200F……比起那些，\x01",
            "还是请您先将委托内容\x01",
            "向我们做个简洁的说明吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB5, 1)
    Jump("loc_55E2")

    label("loc_550E")


    #C0288
    ChrTalk(
        0xB,
        (
            "#11P#2105F什么嘛～\x01",
            "你们这种反应也太差劲了吧。\x02\x03",

            "#2109F难得我在如此百忙之中\x01",
            "还特意把你们给叫来，\x01",
            "你们应该再高兴一点才对嘛～\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x103,
        (
            "#12P#0203F不明白您在说什么。\x02\x03",

            "#0200F……能不能尽量简洁地\x01",
            "向我们说明委托内容呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55E2")


    #C0290
    ChrTalk(
        0xB,
        (
            "#11P#2106F哼，真是的～你们还是一点都没变呢。\x02\x03",

            "#2100F……那，我就开始说明啦。\x01",
            "其实，正如我发出的请求内容所说……\x02\x03",

            "接下来，我们克洛斯贝尔时代周刊将会\x01",
            "附赠以观光导游为主题的副刊。\x02\x03",

            "#2109F这可是我的企划哦。\x01",
            "怎么样，怎么样，厉害吧？很厉害吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x104,
        "#6P#0309F噢噢，确实很棒呢！\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        "#12P#0003F……请继续说吧。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xB,
        (
            "#11P#2100F……嗯，其实想要委托你们的，\x01",
            "就是去拍摄杂志中需要用到的照片。\x02\x03",

            "希望你们能去那些著名的观光点，\x01",
            "还有其它一些景色优美的地方，\x01",
            "多拍摄一些照片。\x02\x03",

            "#2106F市外还有不少魔兽出没，\x01",
            "光凭我一个人，实在是没办法\x01",
            "外出拍摄啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x103,
        (
            "#12P#0200F不过……让我们这些外行人来拍照片，\x01",
            "真的没问题吗？\x02\x03",

            "我们都不是专业的摄影师，\x01",
            "恐怕无法保证照片的质量……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xB,
        (
            "#11P#2106F在纪念庆典期间，雷因兹\x01",
            "一直有很多工作缠身呢～\x01",
            "实在是无法找他来帮忙。\x02\x03",

            "#2100F那些有可能拍到好照片的地点\x01",
            "都已经记在笔记上了，\x01",
            "你们只要过去按下快门就好。\x02\x03",

            "#2106F哈，要是在你们之中，\x01",
            "有人拥有摄影经验的话，\x01",
            "那就再好不过了～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0296
    ChrTalk(
        0x102,
        "#5P#0106F那个……我倒是，有一点经验。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_59EA():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59EA)

    def lambda_59F7():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_59F7)

    def lambda_5A04():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A04)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0297
    ChrTalk(
        0xB,
        "#11P#2105F哎，真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        "#12P#0005F艾莉……？\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x104,
        "#6P#0300F哦～好像还是第一次听你说起啊。\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x103,
        (
            "#12P#0200F导力相机的操作，\x01",
            "好像并不是一朝一夕\x01",
            "就能熟练掌握的啊……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5ACA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5ACA)
    WaitChrThread(0x102, 1)

    #C0301
    ChrTalk(
        0x102,
        (
            "#5P#0112F嗯，那个……\x01",
            "留学的时候，我有一阵子\x01",
            "对这个比较感兴趣。\x02\x03",

            "#0113F不过距离现在已经有一段时间了，\x01",
            "所以，我必须得先找回当时的\x01",
            "技术和感觉……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xB,
        (
            "#11P#2102F足够啦，足够啦！\x01",
            "比起一窍不通，这就已经强太多了。\x02\x03",

            "#2100F那么……\x01",
            "你们决定受理委托了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5BD8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BD8)

    def lambda_5BE5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5BE5)

    def lambda_5BF2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BF2)

    def lambda_5BFF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5BFF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)

    #C0303
    ChrTalk(
        0x101,
        (
            "#12P#0000F明白了，\x01",
            "我们接受。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xB,
        (
            "#11P#2109F嗯，多谢了⊥\x01",
            "……那么，把这个收下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0305
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "拿到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33B, 1)

    #C0306
    ChrTalk(
        0x101,
        (
            "#12P#0000F寻找景色优美的地点，\x01",
            "然后用这个东西拍下风景照\x01",
            "就可以了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xB,
        (
            "#11P#2102F没错，\x01",
            "使用的时候可要多加小心哦～\x02\x03",

            "#2105F……啊，对了对了，\x01",
            "有一件事情，希望你们一定要注意。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        "#6P#0305F需要注意的事情？\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xB,
        (
            "#11P#2100F贝尔加德门是帝国的国境门，\x01",
            "唐古拉姆门是共和国的国境门，\x01",
            "从这两处地方分别能看到两国的国境吧。\x02\x03",

            "#2100F但是，这两处场所的照片\x01",
            "是不能使用在杂志中的，\x01",
            "所以你们就别拍了。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x102,
        "#5P#0105F是政治方面的原因……吗？\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xB,
        (
            "#11P#2106F哈，正是如此。\x01",
            "我们这行也是有很多禁忌的哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#12P#0000F不能在国境大门拍照……\x01",
            "……其它还有什么问题需要注意吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xB,
        (
            "#11P#2100F然后就是照片的数量，\x01",
            "希望你们最少拍摄五张以上。\x02\x03",

            "当然了，纪念庆典时的照片需求量非常之大，\x01",
            "所以，希望你们能多拍一些就多拍一些吧。\x02\x03",

            "#2109F如果你们能拍到更多的照片，\x01",
            "可就帮了我的大忙了。\x02\x03",

            "#2100F……哈，大概就是这些吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x103,
        "#12P#0203F……明白了。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        (
            "#11P#2100F想提交照片的时候，\x01",
            "就去找接待处的托莉亚，\x01",
            "让她来叫我就行了。\x02\x03",

            "#2109F……那么，我还有一些工作没做完呢。\x01",
            "接下来就拜托你们啦～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5850, 1500, 940, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18590, 0)
    SetChrPos(0x101, -4700, 0, 2100, 225)
    SetChrPos(0x102, -4700, 0, 800, 315)
    SetChrPos(0x103, -6000, 0, 800, 45)
    SetChrPos(0x104, -6000, 0, 2100, 135)
    FadeToBright(500, 0)
    OP_0D()

    #C0316
    ChrTalk(
        0x101,
        (
            "#5P#0009F哈哈……\x01",
            "格蕾丝小姐真是一点都没变呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x104,
        "#6P#0306F那种性格果然是一大缺憾啊……\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x102,
        (
            "#11P#0100F呵呵，确实是个精力过剩\x01",
            "的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x103,
        (
            "#12P#0206F那种惊人的活力究竟是从\x01",
            "什么地方涌现出来的呢？\x02\x03",

            "#0211F到最后，还是把\x01",
            "这些棘手的麻烦工作\x01",
            "推给了我们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x104,
        (
            "#6P#0303F不过，这好像也并不是\x01",
            "什么十万火急的工作……\x02\x03",

            "#0300F一边处理其它任务，\x01",
            "一边慢慢做就可以啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x103,
        (
            "#12P#0200F摄影方面的事情只要交给\x01",
            "艾莉前辈就可以了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x102,
        (
            "#11P#0112F可、可不要对我抱有太高的期待哦。\x01",
            "毕竟这只是我的业余爱好而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#5P#0000F……那么，以后要是\x01",
            "发现了景色不错的地方，\x01",
            "就尽量拍下照片吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【克洛斯贝尔百景的摄影】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetChrPos(0x0, -4930, 0, 1860, 90)
    OP_29(0x18, 0x1, 0x1)
    SetScenarioFlags(0x0, 5)
    EventEnd(0x5)
    Jump("loc_64CC")

    label("loc_63F5")

    OP_60(0x0)

    #C0325
    ChrTalk(
        0x101,
        (
            "#12P#0006F对不起，现在稍微有点不太方便……\x01",
            "我们还有其它工作在身。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        (
            "哎呀，是这样啊……\x01",
            "那我们就等一等好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x8,
        (
            "当各位有空接受委托的时候，\x01",
            "请尽早来这里和我联系哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2700, 20, -2000, 90)
    EventEnd(0x5)
    Jump("loc_64CC")

    label("loc_64BD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_64CC")

    label("loc_64CC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_4ACE end

    def Function_13_64D7(): pass

    label("Function_13_64D7")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(3050, 1520, -1840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18370, 0)
    SetChrPos(0x101, 2700, 20, -2000, 90)
    SetChrPos(0x102, 2700, 20, -700, 90)
    SetChrPos(0x103, 1400, 20, -2000, 90)
    SetChrPos(0x104, 1400, 20, -700, 90)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0328
    ChrTalk(
        0x8,
        (
            "#11P啊……\x01",
            "看起来，各位好像拍摄了\x01",
            "很多照片啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        (
            "#11P要把格蕾丝小姐叫来，\x01",
            "向她交付照片吗？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【暂时不交】\x01",      # 0
            "【交付照片】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6610"),
        (1, "loc_6660"),
        (SWITCH_DEFAULT, "loc_666B"),
    )


    label("loc_6610")

    OP_60(0x0)

    #C0330
    ChrTalk(
        0x8,
        (
            "#11P明白了，\x01",
            "等各位方便的时候再来吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 2710, 20, -1270, 90)
    EventEnd(0x5)
    Jump("loc_6670")

    label("loc_6660")

    OP_60(0x0)
    Call(0, 14)
    Jump("loc_6670")

    label("loc_666B")

    Jump("loc_6670")

    label("loc_6670")

    Return()

    # Function_13_64D7 end

    def Function_14_6671(): pass

    label("Function_14_6671")


    #C0331
    ChrTalk(
        0x101,
        "#12P#0000F好的，麻烦你了。\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        "#11P明白了。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x8,
        (
            "#11P那么，可以将导力相机\x01",
            "还给我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        "#11P我要拿去将相片显像。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        (
            "#12P#0005F啊，也是呢。\x01",
            "好的，那就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0336
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x33B, 1)

    #C0337
    ChrTalk(
        0x8,
        "#11P好的，相机已归还。\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        "#11P那么，就请上二楼吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis181.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis180.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis182.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis183.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis184.itp")
    CreatePortrait(5, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis185.itp")
    CreatePortrait(6, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis186.itp")
    CreatePortrait(7, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis187.itp")
    CreatePortrait(8, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis188.itp")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 60010, 150, 10690, 270)
    SetChrPos(0x101, 58200, 0, 11760, 135)
    SetChrPos(0x102, 58650, 0, 12660, 135)
    SetChrPos(0x103, 57000, 0, 11920, 135)
    SetChrPos(0x104, 57480, 0, 13060, 135)
    OP_68(57910, 1500, 11780, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(20010, 0)
    SetCameraDistance(19010, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x10)

    #C0339
    ChrTalk(
        0xB,
        (
            "#11P#2100F那么……首先要说的是，辛苦大家啦～\x02\x03",

            "你们拍摄的那些照片，\x01",
            "刚才已经显像出来了呢。\x02\x03",

            "#2102F好，那我们就赶快来欣赏一下吧⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x102,
        "#5P#0101F（紧张……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_6B19")
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #A0341
    AnonymousTalk(
        0xB,
        (
            "#2100F嗯～这是阿尔摩利卡古道的田园风景啊。\x02\x03",

            "#2102F宁静祥和的氛围真是很不错呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    label("loc_6B19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_6BA5")
    Sound(18, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)

    #A0342
    AnonymousTalk(
        0xB,
        (
            "#2100F这是……阿尔摩利卡村的花田吧？\x02\x03",

            "#2109F我也很喜欢那个村子产的蜂蜜呢～！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)

    label("loc_6BA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_6C3C")
    Sound(18, 0, 100, 0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)

    #A0343
    AnonymousTalk(
        0xB,
        (
            "#2105F啊，这是羽扇河口的遗迹吧？\x02\x03",

            "#2100F如果没有魔兽出没，可就真是\x01",
            "最佳的约会圣地了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)

    label("loc_6C3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_6CCA")
    Sound(18, 0, 100, 0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)

    #A0344
    AnonymousTalk(
        0xB,
        (
            "#2105F哇哇，这张照片是在哪里拍的啊？\x02\x03",

            "#2102F这种孤寂荒凉的气氛真是意外地棒呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)

    label("loc_6CCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_6D77")
    Sound(18, 0, 100, 0)
    OP_C9(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x4, 0x3)

    #A0345
    AnonymousTalk(
        0xB,
        (
            "#2109F出现了呢，玛因兹山道的瀑布！\x02\x03",

            "#2100F这景色可真是壮观啊～\x01",
            "乘坐前往玛因兹的巴士时，在途中就会欣赏到入迷。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x4, 0x3)

    label("loc_6D77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_6E39")
    Sound(18, 0, 100, 0)
    OP_C9(0x7, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x7, 0x3)

    #A0346
    AnonymousTalk(
        0xB,
        (
            "#2102F噢～铁轨的照片啊！\x01",
            "是在西克洛斯贝尔街道那边拍的吧？\x02\x03",

            "#2109F我们的读者中也有一些狂热的铁道爱好者，\x01",
            "这种照片正好可以用上一张～\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x7, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x7, 0x3)

    label("loc_6E39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_6EE4")
    Sound(18, 0, 100, 0)
    OP_C9(0x6, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x6, 0x3)

    #A0347
    AnonymousTalk(
        0xB,
        (
            "#2100F这个是……星见之塔吧？\x02\x03",

            "#2102F这座塔位于森林之中，所以我一般都不会去。\x01",
            "不过，也算是个安静的好地方啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x6, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x6, 0x3)

    label("loc_6EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_6FAE")
    Sound(18, 0, 100, 0)
    OP_C9(0x5, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x5, 0x3)

    #A0348
    AnonymousTalk(
        0xB,
        (
            "#2105F……噢噢噢！这遗迹是什么啊？！\x01",
            "玛因兹山道中还有这种地方吗？\x02\x03",

            "#2102F看起来像是很古老的寺院……\x01",
            "总觉得这种神秘感非常棒呢。嗯～非常棒～\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x5, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x5, 0x3)

    label("loc_6FAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_7063")
    Sound(18, 0, 100, 0)
    OP_C9(0x8, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x8, 0x3)

    #A0349
    AnonymousTalk(
        0xB,
        (
            "#2105F……嘿～古战场里竟然还有这种遗迹吗！\x02\x03",

            "#2109F大概是中世纪建造的堡垒吧。\x01",
            "如果有游击士做护卫，应该就可以去观光了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x8, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x8, 0x3)

    label("loc_7063")


    #C0350
    ChrTalk(
        0xB,
        (
            "#11P#2109F……真是的，你们拍的这些照片，\x01",
            "每一张都美得让人赞叹啊！\x02\x03",

            "说实话，水准绝不输给专业人士哦！\x01",
            "姐姐我可是大吃一惊呢。\x02\x03",

            "#2106F要不，艾莉你\x01",
            "干脆就取代雷因兹，\x01",
            "做我的摄影师，怎么样啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x102,
        (
            "#5P#0111F这个，我觉得\x01",
            "您实在是有些过奖了……\x02\x03",

            "#0100F……不过，总算是松了口气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x104,
        "#6P#0309F哈哈，干得不错嘛，大小姐！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7274")
    OP_2C(0x18, 0x3)

    #C0353
    ChrTalk(
        0xB,
        (
            "#11P#2100F不仅如此，照片的数量\x01",
            "还比规定的张数多了将近一倍……\x02\x03",

            "嘿嘿嘿⊥\x01",
            "只要有这些照片，副刊就不愁没配图啦。\x02\x03",

            "#2109F接下来，只要再配上介绍文字，\x01",
            "就算是彻底大功告成了，万岁！\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x18, 0x1, 0xB)
    Jump("loc_7342")

    label("loc_7274")


    #C0354
    ChrTalk(
        0xB,
        (
            "#11P#2100F正好交付了规定的数量，\x01",
            "真是帮了我的大忙呢。\x02\x03",

            "虽然还是不太够，\x01",
            "但稍后可以让雷因兹再去拍一些，\x01",
            "把不足的部分补齐就可以了。\x02\x03",

            "#2102F接下来，只要再配上介绍文字，\x01",
            "就算是彻底大功告成了，万岁！\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x18, 0x1, 0xC)

    label("loc_7342")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0355
    ChrTalk(
        0x101,
        "#12P#0000F哈哈……这就好。\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xB,
        (
            "#11P#2100F呵呵，警官的嗅觉可真是名不虚传啊。\x01",
            "果然敏锐，竟然探查到了这么多的优美景点。\x02\x03",

            "#2102F要不然，你们干脆改行\x01",
            "去当导游如何啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        "#12P#0200F就算您这么问……\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xB,
        (
            "#11P#2109F哎呀，总之，真是十分感谢。\x01",
            "以后要是再有什么事情，还请继续关照哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯，到时候，\x01",
            "就请再次提出支援请求吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xB,
        (
            "#11P#2100F嗯，谢谢了⊥\x02\x03",

            "#2109F那么，我还很忙，就先这样吧。\x02\x03",

            "Ｂｙｅｂｙｅ～¤\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5850, 1500, 940, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18590, 0)
    SetChrPos(0x101, -4700, 0, 2100, 225)
    SetChrPos(0x102, -4700, 0, 800, 315)
    SetChrPos(0x103, -6000, 0, 800, 45)
    SetChrPos(0x104, -6000, 0, 2100, 135)
    FadeToBright(500, 0)
    OP_0D()

    #C0361
    ChrTalk(
        0x101,
        (
            "#5P#0006F这可真是个够麻烦的委托啊，\x01",
            "要在克洛斯贝尔各地东奔西跑。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x102,
        (
            "#11P#0104F是啊，不过……\x01",
            "已经很久都没有碰过相机了，\x01",
            "也挺开心的呢。\x02\x03",

            "#0100F偶尔接一些这样的委托\x01",
            "好像也不错呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x104,
        "#6P#0300F哈哈，说得也是。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x103,
        (
            "#12P#0206F只是，和格蕾丝小姐打交道\x01",
            "真是有点累人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x101,
        "#5P#0000F哈哈哈……真是一针见血啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0366
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【克洛斯贝尔百景的摄影】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -4930, 0, 1860, 90)
    SetChrPos(0x1, -4930, 0, 1860, 90)
    SetChrPos(0x2, -4930, 0, 1860, 90)
    SetChrPos(0x3, -4930, 0, 1860, 90)
    OP_29(0x18, 0x4, 0x10)
    SetScenarioFlags(0x0, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_6671 end

    def Function_15_7775(): pass

    label("Function_15_7775")

    EventBegin(0x0)
    Fade(500)
    OP_68(6050, 1400, 53360, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19570, 0)
    SetChrPos(0x101, 5650, 0, 53610, 90)
    SetChrPos(0x102, 5650, 0, 54540, 90)
    SetChrPos(0x103, 4400, 0, 53610, 90)
    SetChrPos(0x104, 4400, 0, 54540, 90)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    OP_0D()

    #C0367
    ChrTalk(
        0x102,
        (
            "#5P#0100F这就是菲利策奖\x01",
            "的奖状啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x103,
        (
            "#12P#0200F菲利策奖……\x01",
            "这是每年颁发给最优秀记者的\x01",
            "荣誉奖项哦。\x02\x03",

            "#0203F『赶赴「百日战役」的战地现场，\x01",
            "  进行了长达三个月的连载报道，\x01",
            "  报道内容诚实可信，充满正义感。』\x02\x03",

            "『为赞扬此功绩，\x01",
            "  特此颁发菲利策奖。\x01",
            "  Ｓ１１９２　１１月』\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        (
            "#12P#0005F……原来如此，怪盗Ｂ所说的\x01",
            "『象征荣耀的传播者之证』就是……\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, 6440, 0, 53840, 1000, 0x0)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0370
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "奖状的背面\x01",
            "贴着一张卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0371
    ChrTalk(
        0x104,
        "#6P#0300F哈哈，总算找到了啊。\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 5650, 0, 53610, 1000, 0x0)

    def lambda_7A07():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A07)

    def lambda_7A14():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7A14)

    def lambda_7A21():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A21)

    def lambda_7A2E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7A2E)
    Sleep(400)

    #C0372
    ChrTalk(
        0x101,
        "#12P#0005F嗯，我来看看……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0373
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "  这是最后的谜题了\x01",
            "　去拜访灰色城市之中\x01",
            "调停的长老所在之庵吧\x02",
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

    #C0374
    ChrTalk(
        0x103,
        "#12P#0200F『调停的长老所在之庵』吗……\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x102,
        (
            "#5P#0105F……………………\x01",
            "（难、难道说……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5420, 0, 54040, 90)
    OP_CA(0x1, 0xFF, 0x0)
    OP_29(0x22, 0x1, 0x6)
    SetScenarioFlags(0x0, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_7775 end

    def Function_16_7BAB(): pass

    label("Function_16_7BAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BC1")
    Call(0, 15)
    Jump("loc_7C87")

    label("loc_7BC1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0376
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赶赴「百日战役」的战地现场，\x01",
            "进行了长达三个月的连载报道，\x01",
            "报道内容诚实可信，充满正义感。\x02\x03",

            "为赞扬此功绩，\x01",
            "特此颁发菲利策奖。\x01",
            "Ｓ１１９２　１１月\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)

    label("loc_7C87")

    Return()

    # Function_16_7BAB end

    def Function_17_7C88(): pass

    label("Function_17_7C88")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E04")

    #C0377
    ChrTalk(
        0x8,
        "啊，各位……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7CF8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_7CF8)
    Sleep(50)

    def lambda_7D08():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_7D08)
    Sleep(50)

    def lambda_7D18():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_7D18)
    Sleep(50)

    def lambda_7D28():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_7D28)
    Sleep(50)

    def lambda_7D38():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x4, 2, lambda_7D38)
    Sleep(50)

    def lambda_7D48():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_7D48)
    WaitChrThread(0x0, 2)
    Fade(1000)
    OP_68(-2860, 1510, 720, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25500, 0)
    OP_0D()

    #C0378
    ChrTalk(
        0x8,
        (
            "不好意思，编辑部\x01",
            "一般是不接待外客的。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        "如果有什么吩咐，就请和我说吧。\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        (
            "#0005F啊，这样啊。\x01",
            "真是失礼了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7E3B")

    label("loc_7E04")


    #C0381
    ChrTalk(
        0x101,
        (
            "#0003F二楼好像是不能随便上去的，\x01",
            "还是不要上去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E3B")

    Sleep(50)
    SetChrPos(0x0, -6370, 20, 2470, 180)
    EventEnd(0x4)
    Return()

    # Function_17_7C88 end

    SaveToFile()

Try(main)
