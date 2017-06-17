from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "受付嬢トリア",           # 1
        "マッケネン",             # 2
        "レインズ",               # 3
        "グレイス",               # 4
        "記者Ａ",                 # 5
        "記者Ｂ",                 # 6
        "記者Ｃ",                 # 7
        "記者Ｄ",                 # 8
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
        "Function_5_A6F",          # 05, 5
        "Function_6_BCC",          # 06, 6
        "Function_7_218E",         # 07, 7
        "Function_8_35C0",         # 08, 8
        "Function_9_424C",         # 09, 9
        "Function_10_4E5E",        # 0A, 10
        "Function_11_4F93",        # 0B, 11
        "Function_12_5238",        # 0C, 12
        "Function_13_6D7F",        # 0D, 13
        "Function_14_6F3F",        # 0E, 14
        "Function_15_80EB",        # 0F, 15
        "Function_16_856F",        # 10, 16
        "Function_17_8656",        # 11, 17
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

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7A3")

    #C0001
    ChrTalk(
        0x8,
        (
            "皆さん、\x01",
            "本当にお疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "グレイスさんも\x01",
            "大変喜んでいたようで\x01",
            "よかったです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A6")

    label("loc_7A3")

    Call(0, 6)

    label("loc_7A6")

    Jump("loc_A6E")

    label("loc_7AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_A57")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A52")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【話す】\x01",                # 0
            "【写真を提出する】\x01",      # 1
            "【やめる】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A2")
    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_890")

    #C0003
    ChrTalk(
        0x8,
        (
            "今回の観光ガイドの企画は\x01",
            "グレイスさんが発端なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "雑誌の刊行の為、\x01",
            "どうか頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_893")

    label("loc_890")

    Call(0, 6)

    label("loc_893")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A4D")

    label("loc_8A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3A")
    OP_60(0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_8D5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_8EC")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_903")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_903")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_91A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_931")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_931")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_948")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_948")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_95F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_976")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_976")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_98D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_98D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9A4")
    Call(0, 13)
    Jump("loc_A35")

    label("loc_9A4")


    #C0005
    ChrTalk(
        0x101,
        (
            "#0005F（おっと……\x01",
            "  グレイスさんに出された\x01",
            "  ノルマは５枚以上だ。）\x02\x03",

            "#0003F（今のままじゃ\x01",
            "  まだ提出はできないな……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A35")

    Jump("loc_A4D")

    label("loc_A3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A4D")
    OP_60(0x0)
    Return()

    label("loc_A4D")

    Jump("loc_7C2")

    label("loc_A52")

    Jump("loc_A6E")

    label("loc_A57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_A6B")
    Call(0, 11)
    Jump("loc_A6E")

    label("loc_A6B")

    Call(0, 6)

    label("loc_A6E")

    Return()

    # Function_4_72C end

    def Function_5_A6F(): pass

    label("Function_5_A6F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B03")
    Jump("loc_B4D")

    label("loc_B03")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B23")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B4D")

    label("loc_B23")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B43")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B4D")

    label("loc_B43")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B4D")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    #C0006
    ChrTalk(
        0x8,
        (
            "あ、みなさん\x01",
            "こっちは裏方ですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "ご用ならカウンターで\x01",
            "仰ってください。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_5_A6F end

    def Function_6_BCC(): pass

    label("Function_6_BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C9E")

    #C0008
    ChrTalk(
        0x8,
        (
            "グレイスさん、また\x01",
            "取材に行ってしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "レインズさんを連れて\x01",
            "あちこち調べまわっているみたい\x01",
            "なんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "今日は少し深刻そうでしたね。\x01",
            "何か悪い事件でもあったんでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218D")

    label("loc_C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CAC")
    Jump("loc_218D")

    label("loc_CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D26")

    #C0011
    ChrTalk(
        0x8,
        "……昨晩は大変だったんですよ……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "……今回はグレイスさんの\x01",
            "記事の所為じゃありませんよね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA7")

    label("loc_D26")


    #C0013
    ChrTalk(
        0x8,
        (
            "……本日のクロスベルタイムズは\x01",
            "臨時休刊となっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "読者の方々にはご迷惑をお掛けして\x01",
            "大変申し訳ございません……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_DA7")

    Jump("loc_218D")

    label("loc_DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E09")

    #C0015
    ChrTalk(
        0x8,
        (
            "グレイスさん……\x01",
            "もう少し大人しい記事を\x01",
            "書いてくれないかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E7A")

    label("loc_E09")


    #C0016
    ChrTalk(
        0x8,
        (
            "グレイスさんったら、\x01",
            "またあんな記事を書いて……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "連日議員の先生方から\x01",
            "クレームがくるんです、はあ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E7A")

    Jump("loc_218D")

    label("loc_E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_F03")

    #C0018
    ChrTalk(
        0x8,
        (
            "記念祭も終わって、\x01",
            "最近は街ものんびりしていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "……もっとも明日からは\x01",
            "また忙しくなりそうなんですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218D")

    label("loc_F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F62")

    #C0020
    ChrTalk(
        0x8,
        (
            "今日は臨時増刊号を発売しているんです。\x01",
            "皆さんもぜひご覧になってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218D")

    label("loc_F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_FCB")

    #C0021
    ChrTalk(
        0x8,
        "公園の方がまた騒がしいですね……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "パレードの続きに\x01",
            "催し物でもやっているのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218D")

    label("loc_FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1094")

    #C0023
    ChrTalk(
        0x8,
        (
            "今日はお祭りの目玉、\x01",
            "パレードがあるんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "記者の皆さんもカメラを持って\x01",
            "一目散に出かけてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "……お祭りに浮かれてしまうのは\x01",
            "クロスベル人の性なんでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218D")

    label("loc_1094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1450")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1296")

    #C0026
    ChrTalk(
        0x8,
        (
            "皆さん……昨日は\x01",
            "大変だったそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "詳しくは伺ってませんが、\x01",
            "グレイスさんがホクホク顔だったので\x01",
            "大体の事情は判ります。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        "#0300Fハハ、そうスか……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#0106FＭＣとして現れた段階で\x01",
            "覚悟はしていたけど……\x02\x03",

            "#0100F結局グレイスさんには\x01",
            "いいネタを提供しちゃったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        (
            "#0203F……ちょっと癪ですね。\x01",
            "今度お返ししてもらわないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#0009Fはは……そうだな。\x01",
            "今度情報でも奢ってもらうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "あはは……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "グレイスさん相手に\x01",
            "そんなことを言える方々は\x01",
            "初めてだと思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB3, 3)
    Jump("loc_144B")

    label("loc_1296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_131D")

    #C0034
    ChrTalk(
        0x8,
        (
            "グレイスさんなら\x01",
            "今日もホクホク顔で\x01",
            "出かけて行きましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "記念祭はネタが多いからって\x01",
            "嬉しそうに仰ってました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144B")

    label("loc_131D")


    #C0036
    ChrTalk(
        0x8,
        (
            "ふふ、ちょっと驚きました。\x01",
            "グレイスさんの記事に怒らないで\x01",
            "お返しを要求するなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "特務支援課って、きっと\x01",
            "とても大らかな職場なんですね。\x02",
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
            "#0006Fそ、そういうわけじゃ\x01",
            "無いんですけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_144B")

    Jump("loc_218D")

    label("loc_1450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_14BA")

    #C0039
    ChrTalk(
        0x8,
        (
            "なんだか外が\x01",
            "盛り上がっているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "ステージの催し物が\x01",
            "始まったのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218D")

    label("loc_14BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_15BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_153B")

    #C0041
    ChrTalk(
        0x8,
        (
            "今日は皆さん、本当に\x01",
            "楽しそうに出かけていきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "やっぱりお祭りの取材は\x01",
            "楽しいみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15BA")

    label("loc_153B")


    #C0043
    ChrTalk(
        0x8,
        "クロスベル通信社へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "いよいよ記念祭が始まって\x01",
            "記者の皆さんも特別忙しそうです。\x01",
            "街中を飛び回っていますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_15BA")

    Jump("loc_218D")

    label("loc_15BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_16D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1633")

    #C0045
    ChrTalk(
        0x8,
        (
            "はあ、Ｂ席でいいから\x01",
            "チケットが余っていないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "編集長に聞いてみようかしら……\x02",
    )

    CloseMessageWindow()
    Jump("loc_16D1")

    label("loc_1633")


    #C0047
    ChrTalk(
        0x8,
        (
            "アルカンシェルのプレ公演まで\x01",
            "もう２週間もありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "……取材に行く\x01",
            "記者さんが羨ましいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "私、結局チケットを\x01",
            "買い損ねてしまったので。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_16D1")

    Jump("loc_218D")

    label("loc_16D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_17EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1778")

    #C0050
    ChrTalk(
        0x8,
        (
            "記者になると、きっと\x01",
            "色々な事があるんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "うんうん、しょげないしょげない。\x01",
            "本物の記者になりたいなら\x01",
            "乗り越えていかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E5")

    label("loc_1778")


    #C0052
    ChrTalk(
        0x8,
        (
            "レインズ君、今日は何だか\x01",
            "しょげているみたいですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "珍しいですね、\x01",
            "いつも元気のいい子なのに。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_17E5")

    Jump("loc_218D")

    label("loc_17EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_187A")

    #C0054
    ChrTalk(
        0x8,
        (
            "ルバーチェ商会の黒服の人、\x01",
            "ときどき訪ねてくるんですよね。\x01",
            "はあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "平然と対応なさる\x01",
            "編集長のお気がしれません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_194E")

    label("loc_187A")


    #C0056
    ChrTalk(
        0x8,
        (
            "ルバーチェ商会の方は\x01",
            "ときどき訪ねてきて\x01",
            "編集長と話していかれます。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "暴力行為はないんですが、\x01",
            "脅し文句とか机を叩いたりとか\x01",
            "あからさまな脅しが多くて……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "はあ……やっぱり\x01",
            "ああいった人は怖いですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_194E")

    Jump("loc_218D")

    label("loc_1953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1A89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19D4")

    #C0059
    ChrTalk(
        0x8,
        (
            "グレイスさん、\x01",
            "最近忙しいみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "はあ……苦情が来るような\x01",
            "ネタでなければいいんですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A84")

    label("loc_19D4")


    #C0061
    ChrTalk(
        0x8,
        (
            "グレイスさん、最近\x01",
            "取材で忙しいみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "出張から戻ってからも\x01",
            "走り回っているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "また芸能人のスキャンダルみたいな\x01",
            "ネタを追い回しているのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A84")

    Jump("loc_218D")

    label("loc_1A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1BD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B2F")

    #C0064
    ChrTalk(
        0x8,
        (
            "……実はマスコミには\x01",
            "取材用のプレ公演チケットが\x01",
            "配られるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "でも私は記者じゃないですし、\x01",
            "行列に並んで買うしかなさそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_1B2F")


    #C0066
    ChrTalk(
        0x8,
        (
            "さっきチラッと\x01",
            "話を聞いてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "アルカンシェル新作公演の\x01",
            "チケット販売が始まるそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "はあ、いいなぁ……\x01",
            "私も見に行きたいところです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1BD3")

    Jump("loc_218D")

    label("loc_1BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1C46")

    #C0069
    ChrTalk(
        0x8,
        (
            "グレイスさんなら、\x01",
            "さっきニコニコしながら\x01",
            "出かけて行きましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        "また取材でしょうか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_218D")

    label("loc_1C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1D39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CAA")

    #C0071
    ChrTalk(
        0x8,
        (
            "あ……\x01",
            "クロスベル通信社にご用ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        "何かあれば仰ってくださいね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D34")

    label("loc_1CAA")


    #C0073
    ChrTalk(
        0x8,
        (
            "当社は昨年に\x01",
            "こちらの社屋へ引っ越したのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "まだ未整理の資料が\x01",
            "たくさん積んであるんですよね。\x01",
            "暇をみて整理しておかないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D34")

    Jump("loc_218D")

    label("loc_1D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1F32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DD9")

    #C0075
    ChrTalk(
        0x8,
        (
            "まあグレイスさんだけじゃ\x01",
            "ないんですけど……\x01",
            "苦情が多くて大変なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "皆さん、もう少し大人しい記事を\x01",
            "書いてくれないかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2D")

    label("loc_1DD9")


    #C0077
    ChrTalk(
        0x8,
        (
            "当社は経済面や国際面、社会面、\x01",
            "芸能面などに力を入れています。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "特に社会面では……スクープや\x01",
            "暴露物を扱う事が多いんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "はあ、グレイスさん……\x01",
            "もう少し大人しい記事を\x01",
            "書いてくれないかしら……\x02",
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
        "#0006F（あの人は……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F2D")

    Jump("loc_218D")

    label("loc_1F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FEA")

    #C0081
    ChrTalk(
        0x8,
        (
            "クロスベル通信社には……\x01",
            "記事の内容に怒って\x01",
            "怒鳴り込んでくる方が多いんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "あの、もし何かありましたら\x01",
            "どうぞ申し付けください。\x01",
            "編集長をお呼びしますので。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218D")

    label("loc_1FEA")


    #C0083
    ChrTalk(
        0x8,
        "クロスベル通信社へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "当社の記事に何か問題が\x01",
            "ありましたでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2072")

    #C0085
    ChrTalk(
        0x101,
        "#0005Fえ？　いえ、別に……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2106")

    label("loc_2072")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A5")

    #C0086
    ChrTalk(
        0x102,
        "#0105Fえ？　いえ、別に……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2106")

    label("loc_20A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D4")

    #C0087
    ChrTalk(
        0x103,
        "#0205F？　いえ別に……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2106")

    label("loc_20D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2106")

    #C0088
    ChrTalk(
        0x104,
        "#0305F……ん？　いやあ別に……\x02",
    )

    CloseMessageWindow()

    label("loc_2106")


    #C0089
    ChrTalk(
        0x8,
        "ほっ、そうでしたか……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "もし当社の記事に\x01",
            "ご意見がございましたら、\x01",
            "どうぞ申し付けください。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        "編集長をお呼びしますので。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_218D")

    Return()

    # Function_6_BCC end

    def Function_7_218E(): pass

    label("Function_7_218E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2214")

    #C0092
    ChrTalk(
        0xFE,
        (
            "ん……？\x01",
            "ウチの表彰状に何か用事かよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "眺めるのは構わねえが\x01",
            "あんま触んじゃねえぞ。\x01",
            "栄誉ある賞なんだからよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_2214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_232E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2293")

    #C0094
    ChrTalk(
        0xFE,
        (
            "空港が封鎖されてたようだが……\x01",
            "調べても何も出なかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "ったく近頃\x01",
            "おかしな事件が多いな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2329")

    label("loc_2293")


    #C0096
    ChrTalk(
        0xFE,
        (
            "空港が封鎖されてるってんで\x01",
            "取材に行って来たんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "捜査一課が張り込んでた割に\x01",
            "聞いても何でもないの一点張りだ。\x01",
            "どうも釈然としねえな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2329")

    Jump("loc_35BC")

    label("loc_232E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2420")

    #C0098
    ChrTalk(
        0x9,
        (
            "今朝から空港が臨時閉鎖\x01",
            "されてるってハナシらしいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "警察の発表なんざアテにならねえ。\x01",
            "ちょいと様子を見てくるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "っつーわけで、グレイスが\x01",
            "戻ったらデスクの写真を\x01",
            "見るよう言っといてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        "はい、わかりました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_2420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2596")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_24AA")

    #C0102
    ChrTalk(
        0xFE,
        (
            "この辺りはオフィス街だ。\x01",
            "治安がいいって\x01",
            "聞いていたんだがなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "念のためにまた\x01",
            "裏口を用意しとくべきか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2591")

    label("loc_24AA")


    #C0104
    ChrTalk(
        0xFE,
        (
            "相変わらずクロスベルってのは\x01",
            "一皮むけば物騒な街だなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "ちなみに前のビルじゃあ、\x01",
            "社が襲撃されたときのために\x01",
            "裏口が用意されていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "ビルが襲撃されようが\x01",
            "紙は止めねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "それが俺たちの誇りだったんでな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2591")

    Jump("loc_35BC")

    label("loc_2596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_262B")

    #C0108
    ChrTalk(
        0xFE,
        (
            "近頃マフィアどもが絡んだ\x01",
            "小競り合いみてえな事件が多いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "やれやれ……また\x01",
            "抗争でもしてやがんのか？\x01",
            "ったく懲りねえ連中だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_262B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_26A2")

    #C0110
    ChrTalk(
        0xFE,
        "おう、もう昼時じゃねえか……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "公園の屋台で一杯引っ掛けてくるか。\x01",
            "あそこの麺は拘ってるからなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_26A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2856")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_27A0")

    #C0112
    ChrTalk(
        0xFE,
        (
            "フューリッツァ賞は、\x01",
            "大陸全土で最も優れた記者に\x01",
            "与えられる賞なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "俺たち報道に携わる者にとって\x01",
            "間違いなく、最高の栄誉だと言えるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "ほれ、そこに立てかけてるのが\x01",
            "フューリッツア賞の表彰状だ。\x01",
            "よければ拝んでいきな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2851")

    label("loc_27A0")


    #C0115
    ChrTalk(
        0xFE,
        "フューリッツァ賞って知ってるか？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "毎年、大陸全土から選ばれた\x01",
            "最も優れた記者に与えられる賞だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "俺たち報道に携わる者にとって\x01",
            "間違いなく、最高の栄誉だと言えるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2851")

    Jump("loc_35BC")

    label("loc_2856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2944")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_28B9")

    #C0118
    ChrTalk(
        0xFE,
        (
            "現像してチェックかけて……\x01",
            "明日の特別号には\x01",
            "ぎりぎり間に合うかねえ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293F")

    label("loc_28B9")


    #C0119
    ChrTalk(
        0xFE,
        (
            "パレードで調子に乗って\x01",
            "撮りすぎちまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "他の連中も撮りまくったようだし……\x01",
            "現像を急がねえと\x01",
            "おっつかねえぞ、こりゃあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_293F")

    Jump("loc_35BC")

    label("loc_2944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_29CA")

    #C0121
    ChrTalk(
        0xFE,
        (
            "おう、パレードが始まるまで\x01",
            "まだ時間があるよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "先に腹ごしらえでもしておくか。\x01",
            "腹が減っては何とやら、だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_29CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2A2B")

    #C0123
    ChrTalk(
        0xFE,
        "おう、何か用事か？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "悪いがドタバタしててな。\x01",
            "来客の相手してる暇はねえぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_2A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_2A91")

    #C0125
    ChrTalk(
        0xFE,
        (
            "えーっと、この写真は……と。\x01",
            "皆バンバン撮ってきやがるから\x01",
            "現像すんのが大変だぜ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_2A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2BD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2B1C")

    #C0126
    ChrTalk(
        0xFE,
        (
            "さて……記念祭もこの調子で\x01",
            "バンバンスクープ飛ばすとすっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "……編集長のヤツの\x01",
            "思う壺な気もすっけどなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BCE")

    label("loc_2B1C")


    #C0128
    ChrTalk(
        0xFE,
        (
            "ふぅ、ったく……\x01",
            "前号の記事は締め切りギリギリだったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "編集長のヤツ、俺にまで\x01",
            "キャプション書かせやがって。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "……ま、お陰で大スクープを\x01",
            "モノに出来たわけだがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2BCE")

    Jump("loc_35BC")

    label("loc_2BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2CAE")

    #C0131
    ChrTalk(
        0xFE,
        (
            "そこにある表彰状な、\x01",
            "ウチの社がフューリッツァ賞を\x01",
            "取ったときのもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "当時ウチには伝説の記者が居てな、\x01",
            "その人のお陰で\x01",
            "栄えある賞を頂いたわけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "フッ……まあ俺たちの\x01",
            "目標みてえなもんだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_2CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2E05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D82")

    #C0134
    ChrTalk(
        0xFE,
        (
            "レインズのやつは\x01",
            "カメラマンとしての才能は大したもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "反射神経もあるし、柔軟で\x01",
            "記事に食いついてきやがる写真だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "アルカンシェルみてえな取材には\x01",
            "打ってつけの人材だろ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E00")

    label("loc_2D82")


    #C0137
    ChrTalk(
        0xFE,
        (
            "レインズのやつは\x01",
            "カメラの才能は大したもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "あの真面目な性格も、うまいこと\x01",
            "グレイスと噛み合ってるみてえだしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E00")

    Jump("loc_35BC")

    label("loc_2E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2E93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E8B")
    TurnDirection(0xFE, 0x0, 0)

    #C0139
    ChrTalk(
        0xFE,
        "（ま、新人研修みてえなもんだ。）\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "（間近で俺ら記者の\x01",
            "  仕事運びを見せてやらねえとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x0)
    Jump("loc_2E8E")

    label("loc_2E8B")

    Call(0, 10)

    label("loc_2E8E")

    Jump("loc_35BC")

    label("loc_2E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2FE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F68")

    #C0141
    ChrTalk(
        0xFE,
        (
            "レインズのヤツに\x01",
            "社会面を任せてたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "新人にしちゃ\x01",
            "いいモン上げてくるじゃねえか。\x01",
            "特に写真のデキはピカイチだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "へっ、もうちょい鍛えりゃ\x01",
            "いい記者になれるかもなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FE2")

    label("loc_2F68")


    #C0144
    ChrTalk(
        0xFE,
        "うっし、俺もそろそろ取材に行くか。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "来月にはアルカンシェルの公演に\x01",
            "自治州創立記念祭……\x01",
            "へっ、また忙しくなるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FE2")

    Jump("loc_35BC")

    label("loc_2FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3048")

    #C0146
    ChrTalk(
        0xFE,
        (
            "あー、ごたごた\x01",
            "言ってねえでさっさと決めろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "俺は手伝いしかしねえからな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_3048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_316D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_30D9")

    #C0148
    ChrTalk(
        0xFE,
        (
            "『ＩＢＣが進める新事業』か。\x01",
            "確かに押さえときてえ記事だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "よし、この段は総裁への\x01",
            "インタビューで纏めて、と……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3168")

    label("loc_30D9")


    #C0150
    ChrTalk(
        0xFE,
        (
            "おう、なんだい。\x01",
            "グレイスなら出張に行っちまったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "今頃は帝都でシャッター\x01",
            "切りまくってるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_9E(0x9, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x9, 0x10)

    label("loc_3168")

    Jump("loc_35BC")

    label("loc_316D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_332F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_329A")
    OP_4B(0xB, 0xFF)
    OP_93(0xFE, 0x10E, 0x0)

    #C0152
    ChrTalk(
        0x9,
        (
            "確かに映えるイベントだが、\x01",
            "《帝国時報》との提携記事で\x01",
            "済ませちまう手もあるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        "グレイス、それでも行くのか？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        (
            "#2104Fモチ、帝国の記念式典といえば\x01",
            "エレボニア皇室の面々が\x01",
            "直接拝めるチャンスだもの。\x02\x03",

            "#2102F一度は自分の手で\x01",
            "押さえておきたいのよね～。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_332A")

    label("loc_329A")

    OP_4B(0xB, 0xFF)
    OP_93(0xFE, 0x10E, 0x0)

    #C0155
    ChrTalk(
        0xFE,
        (
            "ま、編集長の許可もらってんなら\x01",
            "グダグダ言うことはねえ。\x01",
            "気張って行ってこいや。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "#2109Fサンキュ♪\x01",
            "こっちは任せたわよ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_332A")

    Jump("loc_35BC")

    label("loc_332F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_346F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3433")

    #C0157
    ChrTalk(
        0xFE,
        (
            "すぱー……\x01",
            "社会面の写真はこんなとこか。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "こっちの警察のナントカ課は……\x01",
            "まあ後回しでいいだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "グレイスがまた今度手がけるとか\x01",
            "言ってたしなぁ。\x02",
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
        "#0006F（何て書かれるか心配だ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_346A")

    label("loc_3433")


    #C0162
    ChrTalk(
        0xFE,
        (
            "警察に新設されたナントカ課は\x01",
            "……まあ後回しだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_346A")

    Jump("loc_35BC")

    label("loc_346F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_34E7")

    #C0163
    ChrTalk(
        0xFE,
        (
            "……なんだよ、本当に\x01",
            "殴り込みなわけじゃねえだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "用がないならさっさと帰んな。\x01",
            "仕事の邪魔だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_34E7")


    #C0165
    ChrTalk(
        0xFE,
        "すぱー……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "あン？　何だおめえらは。\x01",
            "殴り込みかなんかかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "へっへ、ここの編集部に\x01",
            "突貫しようなんざ百年早いぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "ヤクザだろうが何だろうが\x01",
            "クロスベルタイムズは倒せねえ。\x01",
            "坊主、よく覚えときな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_35BC")

    TalkEnd(0xFE)
    Return()

    # Function_7_218E end

    def Function_8_35C0(): pass

    label("Function_8_35C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_38EA")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_36A7")

    #C0169
    ChrTalk(
        0xB,
        (
            "#2103Fとりあえず議会を取材しつつ\x01",
            "ハルトマン議長を追っかけながら\x01",
            "マフィアの内部事情を洗って……\x02\x03",

            "クスリの方は注意しつつ\x01",
            "情報を集めて、と。\x02\x03",

            "#2100Fあ、何か分かったら\x01",
            "すぐに教えて頂戴ね～。\x01",
            "ヨロシク～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E2")

    label("loc_36A7")


    #C0170
    ChrTalk(
        0xB,
        (
            "#2103Fさてと、取材取材……\x02\x03",

            "………………………………\x02\x03",

            "#2102Fね、さっきのレクターって子、\x01",
            "あなた達とどういう関係なの？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x104,
        (
            "#0300Fあー、まあ\x01",
            "ただの行きずりっつーか。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#0006F……自分達も\x01",
            "よく知らないんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "#2100Fふーん、そっか。\x01",
            "……どこかで聞いたこと\x01",
            "ある気がするんだけどなぁ。\x02\x03",

            "#2103Fレクター、レクター……\x01",
            "うーん、どこだったっけ……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x102,
        (
            "#0100F帝国方面の人みたいですけど……\x01",
            "向こうの取材で聞いた事があるとか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0175
    ChrTalk(
        0xB,
        (
            "#2105Fあ～、そうかも。\x01",
            "どこで聞いたんだっけな～。\x02\x03",

            "#2103F……ま、今はいっか。\x01",
            "他にも沢山取材を抱えてるものね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCF, 0)

    label("loc_38E2")

    TalkEnd(0xFE)
    Jump("loc_424B")

    label("loc_38EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3E52")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3987")
    Jump("loc_39D1")

    label("loc_3987")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39A7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39D1")

    label("loc_39A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39C7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39D1")

    label("loc_39C7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39D1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 3)), scpexpr(EXPR_END)), "loc_3AD0")

    #C0176
    ChrTalk(
        0xB,
        (
            "#2100F諸君、最近のお仕事は\x01",
            "どんなカンジなのかな？\x02\x03",

            "#2109F面白おかしいネタがあったら\x01",
            "お姉さんに聞かせてくれて\x01",
            "いいのよん？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#0003Fさ、みんな。\x01",
            "仕事に戻ろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xB,
        "#2106Fううっ、反応が冷たいっ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E46")

    label("loc_3AD0")

    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0179
    ChrTalk(
        0xB,
        (
            "#2105Fあ、支援課の面々じゃない。\x02\x03",

            "#2102Fいや～、久しぶりねぇ。\x01",
            "先月の魔獣騒ぎの件、\x01",
            "読ませてもらったわよん？\x02\x03",

            "#2109Fうんうん。\x01",
            "頑張ってるみたいじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0000Fグレイスさん……\x01",
            "お久し振りですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x102,
        (
            "#0100Fそういえば、あの記事は\x01",
            "グレイスさんでは無かったんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xB,
        (
            "#2100Fうん、取材があって\x01",
            "クロスベルを離れててね。\x02\x03",

            "#2103F出来れば君たちの取材は\x01",
            "あたしがしたかったんだけどなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        "#0200F……結果的に正解かと。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x104,
        (
            "#0306Fま、いつもあの調子だと\x01",
            "こっちもヘコむッスからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        (
            "#2103Fやれやれ、君たちの成長を見守る\x01",
            "あたしの深い愛情が分からないかな～。\x02\x03",

            "#2109Fうふふん、ここで会ったのも何かの縁。\x01",
            "最近の面白おかしい仕事振りでも……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#0003F……グレイスさんは\x01",
            "休憩中のようですね。\x01",
            "どうもお邪魔しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x103,
        "#0203Fお仕事ガンバッテクダサイ。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xB,
        (
            "#2105Fえ、あ、あれ？\x01",
            "みんなもう行っちゃうの？\x02\x03",

            "#2106Fあーん、それはちょっと\x01",
            "冷たいんじゃないの～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 3)

    label("loc_3E46")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_424B")

    label("loc_3E52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4097")
    TurnDirection(0xB, 0x0, 0)

    #C0189
    ChrTalk(
        0xB,
        (
            "#2100Fあら、支援課の面々じゃない。\x02\x03",

            "#2109Fハロハロー、お元気～？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 1)), scpexpr(EXPR_END)), "loc_3F21")

    #C0190
    ChrTalk(
        0x101,
        "#0006Fハロハローじゃありませんよ。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x103,
        (
            "#0200F……また好き勝手な記事を\x01",
            "書いてくれたみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F8C")

    label("loc_3F21")


    #C0192
    ChrTalk(
        0x101,
        "#0006F本当に調子がいいですね……\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        (
            "#0100F先日の一件、また面白おかしく\x01",
            "書き立てたりしてませんよね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F8C")


    #C0194
    ChrTalk(
        0xB,
        (
            "#2102Fうふふ、怒らない怒らない。\x02\x03",

            "お姉さんこれでも\x01",
            "応援してるんだから。\x02\x03",

            "#2103Fあ、でもごめんねー。\x01",
            "今週はちょーっと忙しくなるから\x01",
            "相手してらんないかも。\x02\x03",

            "#2102Fあたしが戻るまでに\x01",
            "面白いネタ、仕入れといてね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        "#0006Fは、はあ……\x02",
    )

    CloseMessageWindow()
    OP_9E(0xB, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    SetScenarioFlags(0x6D, 1)
    Jump("loc_4248")

    label("loc_4097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_413A")
    TurnDirection(0xB, 0x0, 0)

    #C0196
    ChrTalk(
        0xB,
        (
            "#2102Fごめんねー、お姉さん\x01",
            "今週はちょーっと忙しくなるから\x01",
            "相手してらんないかも。\x02\x03",

            "あたしが戻るまでに\x01",
            "面白いネタ、仕入れといてね㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x0)
    Jump("loc_4248")

    label("loc_413A")

    OP_4B(0x9, 0xFF)

    #C0197
    ChrTalk(
        0x9,
        (
            "確かに映えるイベントだが、\x01",
            "《帝国時報》との提携記事で\x01",
            "済ませちまう手もあるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x9,
        "グレイス、それでも行くのか？\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        (
            "#2103Fモチ、帝国の記念式典といえば\x01",
            "エレボニア皇室の面々が\x01",
            "直接拝めるチャンスだもの。\x02\x03",

            "#2109F一度は自分の手で\x01",
            "押さえておきたいのよね～。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)

    label("loc_4248")

    TalkEnd(0xFE)

    label("loc_424B")

    Return()

    # Function_8_35C0 end

    def Function_9_424C(): pass

    label("Function_9_424C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_42D8")

    #C0200
    ChrTalk(
        0xFE,
        (
            "（マフィアの取材なんて\x01",
            "  絶対やりたくないですよ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "（荒れた議会の取材の方が\x01",
            "  何倍もマシですって！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4350")

    label("loc_42D8")

    OP_4B(0xB, 0xFF)

    #C0202
    ChrTalk(
        0xB,
        "ええっと、議会の取材取材っとお～♪\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "（ま、まさか僕も\x01",
            "  手伝わされるんじゃ……\x01",
            "  ビクビク……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xB, 0xFF)

    label("loc_4350")

    Jump("loc_4E5A")

    label("loc_4355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_43D8")

    #C0204
    ChrTalk(
        0xFE,
        (
            "先輩は今日は\x01",
            "何かの取材に行ってるみたいですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "議会の方は\x01",
            "僕に任されたんですよね……\x01",
            "はあ、頑張らないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E5A")

    label("loc_43D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_455C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4446")

    #C0206
    ChrTalk(
        0xFE,
        (
            "グレイス先輩、さっき\x01",
            "出かけちゃったんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "どこ行っちゃったのかなぁ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4557")

    label("loc_4446")


    #C0208
    ChrTalk(
        0xFE,
        (
            "よーし、今日は閉会式と\x01",
            "商工会のステージを取材して……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "あ、それから\x01",
            "ミシュラムに行く水上バスも\x01",
            "カメラに収めておこうかな。\x02",
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
            "そういえば……\x01",
            "グレイス先輩、さっき\x01",
            "出かけちゃったんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "先輩が居ないと\x01",
            "何だか調子が出ないですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4557")

    Jump("loc_4E5A")

    label("loc_455C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_469C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_45E9")

    #C0212
    ChrTalk(
        0xFE,
        (
            "ええと……中央広場か、\x01",
            "それとも港湾区のステージ……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "……先輩ならどっちも行ってこいって\x01",
            "言うんだろうなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4697")

    label("loc_45E9")


    #C0214
    ChrTalk(
        0xFE,
        "あ、支援課の皆さん……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "グレイス先輩なら２階で\x01",
            "記事を纏めている所ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "僕は足りない写真を\x01",
            "撮って来るように言われたんです。\x01",
            "ふう、もう一回りしてこないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4697")

    Jump("loc_4E5A")

    label("loc_469C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_47E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_471F")

    #C0217
    ChrTalk(
        0xFE,
        (
            "グレイス先輩、何か熱心に\x01",
            "調べ物をしているみたいですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "最近は社内でも\x01",
            "顔をあわせないんですよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47DF")

    label("loc_471F")


    #C0219
    ChrTalk(
        0xFE,
        (
            "そろそろプレ公演かぁ……\x01",
            "アルカンシェル取材のスケジュールは、と。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "……そういえばグレイス先輩、\x01",
            "最近何か調べ物をしてるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "社内でもあんまり\x01",
            "顔をあわせないんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_47DF")

    Jump("loc_4E5A")

    label("loc_47E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_493A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4875")

    #C0222
    ChrTalk(
        0xFE,
        (
            "まあ、あのアルカンシェルを\x01",
            "取材できるなら文句ないですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "僕はカメラマンじゃなくて\x01",
            "記者なのにな、ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4935")

    label("loc_4875")


    #C0224
    ChrTalk(
        0xFE,
        (
            "今度のアルカンシェルの取材、\x01",
            "撮影担当として\x01",
            "同行することになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "……編集長ったら酷いですよ、\x01",
            "『君は記事書かなくていいから』だなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        "ぶつぶつ……まあいいですけどー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4935")

    Jump("loc_4E5A")

    label("loc_493A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4998")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4990")

    #C0227
    ChrTalk(
        0xFE,
        (
            "ううっ、僕の唯一のコラム記事が……\x01",
            "そんなの無いですよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4993")

    label("loc_4990")

    Call(0, 10)

    label("loc_4993")

    Jump("loc_4E5A")

    label("loc_4998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4ACF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4A08")

    #C0228
    ChrTalk(
        0xFE,
        (
            "前回の狼事件の記事、\x01",
            "僕が担当したんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "よかったら読んでみてくださいね～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4ACA")

    label("loc_4A08")


    #C0230
    ChrTalk(
        0xFE,
        "あ、特務支援課の皆さんですよね。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "前回の狼事件の記事、\x01",
            "実は僕が担当したんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "担当した記事が\x01",
            "一面に載ったのは初めてなんで、\x01",
            "本当に嬉しいなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "まだ興奮が冷めませんよ～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4ACA")

    Jump("loc_4E5A")

    label("loc_4ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4BDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4B43")

    #C0234
    ChrTalk(
        0xFE,
        "僕みたいな新人が社会面だなんて……\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "どこから手を付けたらいいか\x01",
            "分かんないですよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD5")

    label("loc_4B43")


    #C0236
    ChrTalk(
        0xFE,
        (
            "グレイス先輩が出張なんで、\x01",
            "代わりに社会面を任されたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "うわあ、緊張するな～。\x01",
            "というかマッケネンさんも\x01",
            "無茶を言うんだから……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4BD5")

    Jump("loc_4E5A")

    label("loc_4BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4D48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4C55")

    #C0238
    ChrTalk(
        0xFE,
        (
            "グレイス先輩は今週は\x01",
            "出張なんですよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "先輩が居ないと静かで\x01",
            "……ちょっと寂しいですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D43")

    label("loc_4C55")


    #C0240
    ChrTalk(
        0xFE,
        (
            "今日はグレイス先輩がいないんで\x01",
            "編集会議が早く終わっちゃいましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "グレイス先輩は編集会議でも\x01",
            "パワー全開ですからね。\x01",
            "すごい論戦になったりするんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "まあそれで\x01",
            "いい記事ができるんですから\x01",
            "悪い事じゃないんですけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4D43")

    Jump("loc_4E5A")

    label("loc_4D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4DA5")

    #C0243
    ChrTalk(
        0xFE,
        (
            "小さい記事でも任されると\x01",
            "嬉しいものですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        "よーし、がんばるぞー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E5A")

    label("loc_4DA5")


    #C0245
    ChrTalk(
        0xFE,
        "よーし、次のコラムはっと……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "僕も最近ようやく\x01",
            "記事を書かせてもらえるように\x01",
            "なったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "わーい……！\x01",
            "文化面の小さいコラムだけですけど\x01",
            "それでも嬉しいもんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4E5A")

    TalkEnd(0xFE)
    Return()

    # Function_9_424C end

    def Function_10_4E5E(): pass

    label("Function_10_4E5E")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0248
    ChrTalk(
        0xA,
        "え……カメラマンですか？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x9,
        "ああ、お前撮影は得意だろ。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x9,
        (
            "今度のアルカンシェル取材、\x01",
            "カメラマンがいねえんだよ。\x01",
            "ちょっと俺のヘルプに回れや。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xA,
        (
            "あのー、でも僕には\x01",
            "お料理コラムの仕事がありまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x9,
        "そっちはしばらくナシだ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0253
    ChrTalk(
        0xA,
        "ええっ、そんなぁ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_10_4E5E end

    def Function_11_4F93(): pass

    label("Function_11_4F93")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5191")

    #C0254
    ChrTalk(
        0x8,
        "#11Pクロスベル通信社へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        "#11P本日はどのようなご用件でしょう？\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#12P#0000F特務支援課の者です。\x02\x03",

            "こちらから出されていた\x01",
            "支援要請を見て伺いました。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        (
            "#11Pまぁ、では皆様が……\x01",
            "ご足労頂き、ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "#11P依頼については\x01",
            "担当の者から直接、\x01",
            "ご説明差し上げたいそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x8,
        "#11Pお時間は大丈夫でしょうか？\x02",
    )

    CloseMessageWindow()
    OP_29(0x18, 0x1, 0x0)
    Call(0, 12)
    Jump("loc_5237")

    label("loc_5191")


    #C0260
    ChrTalk(
        0x8,
        (
            "#11P……用事はお済みに\x01",
            "なりましたでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "#11P依頼については\x01",
            "担当の者から直接、\x01",
            "ご説明差し上げたいそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        "#11Pお時間は大丈夫でしょうか？\x02",
    )

    CloseMessageWindow()
    Call(0, 12)

    label("loc_5237")

    Return()

    # Function_11_4F93 end

    def Function_12_5238(): pass

    label("Function_12_5238")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【はい】\x01",        # 0
            "【いいえ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5278"),
        (1, "loc_6C85"),
        (SWITCH_DEFAULT, "loc_6D65"),
    )


    label("loc_5278")

    OP_60(0x0)

    #C0263
    ChrTalk(
        0x101,
        "#12P#0000Fええ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x8,
        "#11P分かりましたわ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_532C")

    #C0265
    ChrTalk(
        0x8,
        (
            "#11Pそれではお手数ですが、\x01",
            "２階の方へ上がられてください。\x01",
            "担当者が待っていますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5384")

    label("loc_532C")


    #C0266
    ChrTalk(
        0x8,
        (
            "#11Pそれではお手数ですが、\x01",
            "２階の方へ上がられてください。\x01",
            "担当者をお呼びしますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5384")


    #C0267
    ChrTalk(
        0x101,
        (
            "#12P#0000Fはい、分かりました。\x02\x03",

            "#0003F（とにかく、行ってみるか……）\x02",
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

    def lambda_5518():
        OP_95(0xFE, 67320, 0, 5770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5518)
    WaitChrThread(0xC, 1)

    def lambda_5536():
        OP_95(0xFE, 55550, 0, 5030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5536)
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
            "#11P#2109Fハロハロー、\x01",
            "特務支援課の皆さん㈱\x02",
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
        "#12P#0003Fグ、グレイスさん……\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x102,
        "#5P#0106F予想はしてたけど……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_573A")

    #C0271
    ChrTalk(
        0xB,
        (
            "#11P#2105Fなによなによ～、\x01",
            "反応悪いじゃない。\x02\x03",

            "#2109Fこの忙しい中\x01",
            "わざわざ呼びつけたんだから\x01",
            "もっと喜んでよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x103,
        (
            "#12P#0203F意味が分かりません。\x02\x03",

            "#0200F……手短に依頼の内容を\x01",
            "説明していただけますか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DCC")

    label("loc_573A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_59FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5925")

    #C0273
    ChrTalk(
        0xB,
        (
            "#11P#2100Fふふ、昨日はお疲れさま！\x02\x03",

            "#2109F昨日のレースは早速、\x01",
            "面白い記事に仕上げといたわよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x104,
        (
            "#6P#0306Fやっぱり記事に\x01",
            "しちまうんスか……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xB,
        (
            "#11P#2100Fそそ、記念祭の最終日に出る\x01",
            "臨時特別号に載るはずよ。\x02\x03",

            "#2109F君たちの活躍もアピールしたから\x01",
            "楽しみにしといてね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        (
            "#12P#0006F（絶対、持ち上げといて\x01",
            "  落としそうな気がする……）\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x103,
        (
            "#12P#0203F（まあ、いつものパターンですね。）\x02\x03",

            "#0200F……そんなことより、\x01",
            "手短に依頼の内容を\x01",
            "説明していただけますか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 0)
    Jump("loc_59F5")

    label("loc_5925")


    #C0278
    ChrTalk(
        0xB,
        (
            "#11P#2105Fなによなによ～、\x01",
            "反応悪いじゃない。\x02\x03",

            "#2109Fこの忙しい中\x01",
            "わざわざ呼びつけたんだから\x01",
            "もっと喜んでよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        (
            "#12P#0203F意味が分かりません。\x02\x03",

            "#0200F……手短に依頼の内容を\x01",
            "説明していただけますか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59F5")

    Jump("loc_5DCC")

    label("loc_59FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CFC")

    #C0280
    ChrTalk(
        0xB,
        (
            "#11P#2109Fいや～、この前のスクープは\x01",
            "本当に有り難かったわ！\x02\x03",

            "これも全部、君たちのおかげね！\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        "#12P#0006Fはあ……調子いいですね。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x103,
        (
            "#12P#0200F別にグレイスさんのために\x01",
            "何かしたのではありませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x102,
        (
            "#5P#0106F……さすがに複雑ですけど……\x02\x03",

            "#0100Fおじいさまに同情的な\x01",
            "記事だったのは安心しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xB,
        (
            "#11P#2106Fま、帝国派のネタを書けないのに\x01",
            "市長だけ槍玉に上げるってのも\x01",
            "フェアじゃないしね～。\x02\x03",

            "#2100Fというか、貴方のお祖父様って\x01",
            "市民からの人気は高いし、\x01",
            "あたしも個人的に応援してるの。\x02\x03",

            "#2102F記者としては失格かもしれないけど\x01",
            "悪いことは書きたくないのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x102,
        "#5P#0100Fグレイスさん……\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x104,
        (
            "#6P#0300Fま、記者だって人の子だし\x01",
            "そのくらい良いんじゃないッスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x103,
        (
            "#12P#0200F……そんなことより、\x01",
            "手短に依頼の内容を\x01",
            "説明していただけますか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB5, 1)
    Jump("loc_5DCC")

    label("loc_5CFC")


    #C0288
    ChrTalk(
        0xB,
        (
            "#11P#2105Fなによなによ～、\x01",
            "反応悪いじゃない。\x02\x03",

            "#2109Fこの忙しい中\x01",
            "わざわざ呼びつけたんだから\x01",
            "もっと喜んでよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x103,
        (
            "#12P#0203F意味が分かりません。\x02\x03",

            "#0200F……手短に依頼の内容を\x01",
            "説明していただけますか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DCC")


    #C0290
    ChrTalk(
        0xB,
        (
            "#11P#2106Fんも～、相変わらずなんだから。\x02\x03",

            "#2100F……それじゃ、説明するわね。\x01",
            "すでに依頼は見たと思うけど……\x02\x03",

            "今度、クロスベルタイムズでは\x01",
            "別冊観光ガイドを刊行するの。\x02\x03",

            "#2109Fこれ、あたしの企画なのよ。\x01",
            "ね、ね、すごい？　すごい？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x104,
        "#6P#0309Fおお、そりゃすげえっす！\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        "#12P#0003F……続けてください。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xB,
        (
            "#11P#2100F……でね、あなた達に頼みたいのは\x01",
            "雑誌に使う写真の撮影なのよ。\x02\x03",

            "観光名所となりうる\x01",
            "美しい景色を、たくさん\x01",
            "撮ってきて欲しいわけ。\x02\x03",

            "#2106F街道の方には魔獣も出るし、\x01",
            "あたしたちだけじゃ\x01",
            "なかなか取材にいけないのよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x103,
        (
            "#12P#0200Fでも……素人のわたしたちが\x01",
            "撮って大丈夫なんですか？\x02\x03",

            "プロのカメラマンでもないですし\x01",
            "クオリティは保証できませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xB,
        (
            "#11P#2106F記念祭中は、レインズ君に\x01",
            "ずっと仕事が入っててねー。\x01",
            "ちょっと頼めそうにないのよ。\x02\x03",

            "#2100Fこの際、いい画が取れそうな場所の\x01",
            "メモがわりでいいから\x01",
            "撮ってきて欲しいってわけ。\x02\x03",

            "#2106Fまぁ、あなた達の中に\x01",
            "カメラの経験者でもいれば\x01",
            "言うことナシなんだけどねー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0296
    ChrTalk(
        0x102,
        "#5P#0106Fあの……私、経験あります。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6202():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6202)

    def lambda_620F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_620F)

    def lambda_621C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_621C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0297
    ChrTalk(
        0xB,
        "#11P#2105Fえ、ホント！？\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        "#12P#0005Fエリィが……？\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x104,
        "#6P#0300Fほー、そりゃ初耳だ。\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x103,
        (
            "#12P#0200Fオーバルカメラは\x01",
            "一朝一夕で使いこなせるものじゃ\x01",
            "ないと思うのですが……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_62EA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62EA)
    WaitChrThread(0x102, 1)

    #C0301
    ChrTalk(
        0x102,
        (
            "#5P#0112Fえ、えっとまぁ……\x01",
            "留学中に趣味にしていた\x01",
            "時期があってね。\x02\x03",

            "#0113Fちょっと前の話だから\x01",
            "カンを取り戻さないと\x01",
            "いけないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xB,
        (
            "#11P#2102F充分充分！\x01",
            "何も知らないよりは断然イイわ。\x02\x03",

            "#2100Fそれじゃあ……\x01",
            "引き受けてもらえるわね？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_63EE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63EE)

    def lambda_63FB():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_63FB)

    def lambda_6408():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6408)

    def lambda_6415():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6415)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)

    #C0303
    ChrTalk(
        0x101,
        (
            "#12P#0000F分かりました、\x01",
            "お引き受けします。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xB,
        (
            "#11P#2109Fううん、ありがと㈱\x01",
            "……それじゃ、ハイこれ。\x02",
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
            "を預かった。\x02",
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
            "#12P#0000F景色のよさそうなポイントを探して\x01",
            "こいつで写真を撮ってくれば\x01",
            "いいわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xB,
        (
            "#11P#2102Fそゆこと。\x01",
            "扱いには気を付けてよ～？\x02\x03",

            "#2105F……あ、そうそう。\x01",
            "一つだけ注意してほしい事があったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        "#6P#0305F注意すること？\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xB,
        (
            "#11P#2100Fベルガード門からは帝国の国境、\x01",
            "タングラム門からは共和国の国境が\x01",
            "それぞれ見れるのよね。\x02\x03",

            "#2100Fそこはちょっと\x01",
            "雑誌に使えないから、\x01",
            "写真には撮ってこないでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x102,
        "#5P#0105F政治的な問題……でしょうか？\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xB,
        (
            "#11P#2106Fまぁ、そゆコト。\x01",
            "ウチにも色々あんのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#12P#0000F国境門での撮影はＮＧ、と。\x01",
            "……他には何かありますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xB,
        (
            "#11P#2100F提出してもらうノルマとして、\x01",
            "最低、５枚以上をお願いするわ。\x02\x03",

            "記念祭いっぱいまで待つから、\x01",
            "出来るだけ沢山撮って来て頂戴。\x02\x03",

            "#2109Fもっと沢山撮ってくれれば\x01",
            "それだけ助かっちゃうわね。\x02\x03",

            "#2100F……ま、こんなトコかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x103,
        "#12P#0203F……把握しました。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        (
            "#11P#2100F写真を提出したいときは\x01",
            "受付のトリアちゃんに言って\x01",
            "あたしを呼びつけて頂戴ね。\x02\x03",

            "#2109F……じゃ、あたしは仕事が残ってるから。\x01",
            "後はヨロシク頼んだわね～。\x02",
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
            "#5P#0009Fはは……\x01",
            "グレイスさんも相変わらずだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x104,
        "#6P#0306Fやっぱ性格が惜しいんだよなぁ……\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x102,
        (
            "#11P#0100Fまあ、元気すぎる人である事は\x01",
            "確かよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x103,
        (
            "#12P#0206Fどこからあんな\x01",
            "バイタリティが湧くのやら。\x02\x03",

            "#0211F結局面倒くさそうな\x01",
            "仕事を押し付けられて\x01",
            "しまいましたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x104,
        (
            "#6P#0303Fま、そこまで急ぎの\x01",
            "仕事じゃないみたいだし……\x02\x03",

            "#0300F他の仕事をしながら\x01",
            "少しずつ進めるのがいいかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x103,
        (
            "#12P#0200F撮影はエリィさんに任せれば\x01",
            "よさそうですしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x102,
        (
            "#11P#0112Fあ、あまり期待しないでね。\x01",
            "あくまで趣味の範疇なんだから……\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#5P#0000F……それじゃ、いい景色を見かけたら\x01",
            "出来るだけ写真に\x01",
            "収めていくようにしよう。\x02",
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
            "クエスト【クロスベル百景の撮影】\x07\x00",
            "を開始した！\x02",
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
    Jump("loc_6D74")

    label("loc_6C85")

    OP_60(0x0)

    #C0325
    ChrTalk(
        0x101,
        (
            "#12P#0006Fすみません、今はちょっと……\x01",
            "別件の用が入っているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        (
            "あら、そうなのですか……\x01",
            "それではお待ちしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x8,
        (
            "依頼を受けてくださる場合は\x01",
            "出来るだけ早めにお越しくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2700, 20, -2000, 90)
    EventEnd(0x5)
    Jump("loc_6D74")

    label("loc_6D65")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D74")

    label("loc_6D74")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_5238 end

    def Function_13_6D7F(): pass

    label("Function_13_6D7F")

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
            "#11Pあら……\x01",
            "沢山の写真を撮ってきて\x01",
            "いただいたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        (
            "#11Pグレイスさんをお呼びして、\x01",
            "写真を提出しますか？\x02",
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
            "【まだ提出しない】\x01",      # 0
            "【提出する】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6ED4"),
        (1, "loc_6F2E"),
        (SWITCH_DEFAULT, "loc_6F39"),
    )


    label("loc_6ED4")

    OP_60(0x0)

    #C0330
    ChrTalk(
        0x8,
        (
            "#11P分かりました。\x01",
            "また宜しい時にお願いします。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 2710, 20, -1270, 90)
    EventEnd(0x5)
    Jump("loc_6F3E")

    label("loc_6F2E")

    OP_60(0x0)
    Call(0, 14)
    Jump("loc_6F3E")

    label("loc_6F39")

    Jump("loc_6F3E")

    label("loc_6F3E")

    Return()

    # Function_13_6D7F end

    def Function_14_6F3F(): pass

    label("Function_14_6F3F")


    #C0331
    ChrTalk(
        0x101,
        "#12P#0000Fはい、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        "#11P承りました。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x8,
        (
            "#11Pそれと、オーバルカメラを\x01",
            "ご返却いただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        "#11P今から現像にかけておきますわ。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあ、そうですね。\x01",
            "じゃあよろしくお願いします。\x02",
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
            "を返した。\x02",
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
        "#11Pはい、確かに。\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        "#11Pそれでは、２階の方へどうぞ。\x02",
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
            "#11P#2100Fさてと……まずはお疲れ様～。\x02\x03",

            "あなた達が撮ってきてくれた写真、\x01",
            "さっき現像されてきたわ。\x02\x03",

            "#2102Fそれじゃ、早速見てみましょっか㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x102,
        "#5P#0101F（ごくっ……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7435")
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #A0341
    AnonymousTalk(
        0xB,
        (
            "#2100Fふーむ、アルモリカ古道の田園風景ね。\x02\x03",

            "#2102Fのどかな雰囲気がたまらないわね！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    label("loc_7435")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_74CD")
    Sound(18, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)

    #A0342
    AnonymousTalk(
        0xB,
        (
            "#2100Fこれは、アルモリカ村の花畑ね。\x02\x03",

            "#2109Fあの村のハチミツはあたしも大好きなのよね～！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)

    label("loc_74CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_7576")
    Sound(18, 0, 100, 0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)

    #A0343
    AnonymousTalk(
        0xB,
        (
            "#2105Fおおっと、ルピナス川河口の遺跡かな？\x02\x03",

            "#2100F魔獣さえいなければデートスポットとして\x01",
            "最適の場所よね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)

    label("loc_7576")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_7602")
    Sound(18, 0, 100, 0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)

    #A0344
    AnonymousTalk(
        0xB,
        (
            "#2105Fわわ、こんなのどこで撮ったの？\x02\x03",

            "#2102F寂しげな雰囲気が逆にいいわね～。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)

    label("loc_7602")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_76B7")
    Sound(18, 0, 100, 0)
    OP_C9(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x4, 0x3)

    #A0345
    AnonymousTalk(
        0xB,
        (
            "#2109F出ました、マインツ山道の滝！\x02\x03",

            "#2100Fこれはホント、壮観よね～。\x01",
            "マインツへのバスに乗るとついつい見入っちゃうわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x4, 0x3)

    label("loc_76B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_7773")
    Sound(18, 0, 100, 0)
    OP_C9(0x7, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x7, 0x3)

    #A0346
    AnonymousTalk(
        0xB,
        (
            "#2102Fおー、鉄道の写真ね！\x01",
            "西クロスベル街道のあたりかしら。\x02\x03",

            "#2109F鉄道は一部のマニアに人気だから\x01",
            "一枚は欲しかったのよね～。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x7, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x7, 0x3)

    label("loc_7773")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_7826")
    Sound(18, 0, 100, 0)
    OP_C9(0x6, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x6, 0x3)

    #A0347
    AnonymousTalk(
        0xB,
        (
            "#2100Fこれは……星見の塔、だったかしら？\x02\x03",

            "#2102Fこの辺は森の中だから中々行かないけど、\x01",
            "静かでいい場所だとは思うわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x6, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x6, 0x3)

    label("loc_7826")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_78EC")
    Sound(18, 0, 100, 0)
    OP_C9(0x5, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x5, 0x3)

    #A0348
    AnonymousTalk(
        0xB,
        (
            "#2105F……ををっと！　なにこの遺跡！\x01",
            "マインツ山道にこんな場所があるの？\x02\x03",

            "#2102F古い寺院みたいだけど……\x01",
            "なんだか神秘的でグーよ、グー。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x5, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x5, 0x3)

    label("loc_78EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_79A3")
    Sound(18, 0, 100, 0)
    OP_C9(0x8, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x8, 0x3)

    #A0349
    AnonymousTalk(
        0xB,
        (
            "#2105F……へー、古戦場にこんな遺跡があんのね！\x02\x03",

            "#2109F中世の砦ってとこかしら。\x01",
            "遊撃士を護衛につければ観光もできそうね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x8, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x8, 0x3)

    label("loc_79A3")


    #C0350
    ChrTalk(
        0xB,
        (
            "#11P#2109F……んもぉ、どれもこれも\x01",
            "バッチリ綺麗に撮れてるわねぇ！\x02\x03",

            "正直、プロ顔負けの出来栄えよ？\x01",
            "おねーさん、ビックリしちゃったわ。\x02\x03",

            "#2106Fレインズ君の代わりに\x01",
            "エリィちゃんが撮影係に\x01",
            "なればいいのにな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x102,
        (
            "#5P#0111Fそれはさすがに\x01",
            "言い過ぎだと思いますけど……\x02\x03",

            "#0100F……とりあえず、安心しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x104,
        "#6P#0309Fははっ、やるじゃねぇかお嬢！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7BC2")
    OP_2C(0x18, 0x3)

    #C0353
    ChrTalk(
        0xB,
        (
            "#11P#2100Fその上、ノルマの倍近くの写真を\x01",
            "撮ってきてくれちゃって……\x02\x03",

            "うふふん㈱\x01",
            "これだけあればバッチリ。\x02\x03",

            "#2109Fあとは紹介文を添えれば\x01",
            "晴れて完成、万々歳よ！\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x18, 0x1, 0xB)
    Jump("loc_7C92")

    label("loc_7BC2")


    #C0354
    ChrTalk(
        0xB,
        (
            "#11P#2100Fノルマもキチンと達成して\x01",
            "くれちゃって助かったわ。\x02\x03",

            "ちょっと足りないけど、\x01",
            "あとでレインズ君が埋め合わせれば\x01",
            "充分な写真が揃うだろうし。\x02\x03",

            "#2102Fあとは紹介文を添えれば\x01",
            "晴れて完成、万々歳よ！\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x18, 0x1, 0xC)

    label("loc_7C92")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0355
    ChrTalk(
        0x101,
        "#12P#0000Fはは……それは良かったですね。\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xB,
        (
            "#11P#2100Fいやぁ、さすがは警察官の嗅覚ね。\x01",
            "よくぞまぁ名所を見つけたもんだわ。\x02\x03",

            "#2102F観光ガイドに転職した方が\x01",
            "いいんじゃないの、ねぇ？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        "#12P#0200Fねぇ、と言われても。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xB,
        (
            "#11P#2109Fや、ほんと感謝してるわ。\x01",
            "また何かあったらヨロシク～！\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#12P#0000Fええ、その時はまた\x01",
            "支援要請を出してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xB,
        (
            "#11P#2100Fうん、ありがと㈱\x02\x03",

            "#2109Fそれじゃ、忙しいからこの辺でね。\x02\x03",

            "バッハハ～イ♪\x02",
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
            "#5P#0006F結局クロスベル中を歩き回る\x01",
            "大掛かりな依頼だったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x102,
        (
            "#11P#0104Fまぁ、でも……\x01",
            "久しぶりにカメラを持てて\x01",
            "楽しかったわ。\x02\x03",

            "#0100Fたまにはこういう依頼があっても\x01",
            "いいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x104,
        "#6P#0300Fはは、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x103,
        (
            "#12P#0206Fグレイスさんのノリは\x01",
            "疲れますけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x101,
        "#5P#0000Fははは……言えてるな。\x02",
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
            "クエスト【クロスベル百景の撮影】\x07\x00",
            "を達成した！\x02",
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

    # Function_14_6F3F end

    def Function_15_80EB(): pass

    label("Function_15_80EB")

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
            "#5P#0100Fこれはフューリッツァ賞の\x01",
            "表彰状ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x103,
        (
            "#12P#0200Fフューリッツァ賞……\x01",
            "毎年最も優秀なジャーナリストに\x01",
            "贈られる栄誉ある賞ですね。\x02\x03",

            "#0203F『《百日戦役》を巡る戦場取材、\x01",
            "  ３ヶ月間に渡る報道連載は\x01",
            "  誠実で正義感溢れるものであった。』\x02\x03",

            "『その功績を讃え\x01",
            "  ここにフューリッツァ賞を贈る。\x01",
            "  Ｓ１１９２　１１月』\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        (
            "#12P#0005F……そうか、怪盗Ｂの言う\x01",
            "『栄えある伝達者の証』は……\x02",
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
            "表彰状の裏に\x01",
            "カードが貼り付けられていた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0371
    ChrTalk(
        0x104,
        "#6P#0300Fはは、ようやく見つかったか。\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 5650, 0, 53610, 1000, 0x0)

    def lambda_83BD():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_83BD)

    def lambda_83CA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_83CA)

    def lambda_83D7():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_83D7)

    def lambda_83E4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_83E4)
    Sleep(400)

    #C0372
    ChrTalk(
        0x101,
        "#12P#0005Fええと、なになに……\x02",
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
            " これが最後の謎掛けだ \x01",
            "　灰色の街、調停せし　\x01",
            "長老の庵を訪れるが良い\x02",
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
        "#12P#0200F『調停せし長老の庵』ですか……\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x102,
        (
            "#5P#0105F……………………\x01",
            "（ま、まさかね。）\x02",
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

    # Function_15_80EB end

    def Function_16_856F(): pass

    label("Function_16_856F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8585")
    Call(0, 15)
    Jump("loc_8655")

    label("loc_8585")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0376
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《百日戦役》を巡る戦場取材、\x01",
            "３ヶ月間に渡る報道連載は\x01",
            "誠実で正義感溢れるものであった。\x02\x03",

            "その功績を讃え\x01",
            "ここにフューリッツァ賞を贈る。\x01",
            "Ｓ１１９２　１１月\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)

    label("loc_8655")

    Return()

    # Function_16_856F end

    def Function_17_8656(): pass

    label("Function_17_8656")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87F6")

    #C0377
    ChrTalk(
        0x8,
        "あ、皆さん……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_86C8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_86C8)
    Sleep(50)

    def lambda_86D8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_86D8)
    Sleep(50)

    def lambda_86E8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_86E8)
    Sleep(50)

    def lambda_86F8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_86F8)
    Sleep(50)

    def lambda_8708():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x4, 2, lambda_8708)
    Sleep(50)

    def lambda_8718():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_8718)
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
            "すみません、編集部は\x01",
            "一般の方はお断り頂いているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        "御用なら私の方に仰ってください。\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        (
            "#0005Fそ、そうでしたか。\x01",
            "これは失礼しました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8839")

    label("loc_87F6")


    #C0381
    ChrTalk(
        0x101,
        (
            "#0003F２階は入っちゃいけないみたいだ。\x01",
            "立ち入らないでおこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8839")

    Sleep(50)
    SetChrPos(0x0, -6370, 20, 2470, 180)
    EventEnd(0x4)
    Return()

    # Function_17_8656 end

    SaveToFile()

Try(main)
