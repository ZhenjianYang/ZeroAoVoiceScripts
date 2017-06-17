from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0350.bin",                # FileName
        "c0350",                    # MapName
        "c0350",                    # Location
        0x002D,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 45, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0350",                  # 0
        "ボンド",                 # 1
        "クレイユ",               # 2
        "サニータ",               # 3
        "マリー",                 # 4
        "ボンド",                 # 5
        "サニータ",               # 6
        "ソフィア",               # 7
    ))

    AddCharChip((
        "chr/ch27600.itc",                   # 00
        "chr/ch27602.itc",                   # 01
        "chr/ch33300.itc",                   # 02
        "chr/ch34400.itc",                   # 03
        "chr/ch34402.itc",                   # 04
        "chr/ch39000.itc",                   # 05
        "chr/ch09400.itc",                   # 06
    ))

    DeclNpc(-850,    0,       2529,    180,  261,  0x0, 0,   0,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(5590,    0,       -2119,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6920,    4000,    10069,   0,    261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(5179,    4000,    5559,    315,  261,  0x0, 0,   5,   0,   0,   4,   0,   12,  255,  0)
    DeclNpc(7800,    4500,    7300,    0,    389,  0x0, 0,   1,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(7099,    4500,    7300,    0,    389,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-2150,   0,       3400,    90,   389,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)

    ScpFunction((
        "Function_0_1BC",          # 00, 0
        "Function_1_274",          # 01, 1
        "Function_2_29F",          # 02, 2
        "Function_3_2CA",          # 03, 3
        "Function_4_2F5",          # 04, 4
        "Function_5_320",          # 05, 5
        "Function_6_81B",          # 06, 6
        "Function_7_8B8",          # 07, 7
        "Function_8_F8D",          # 08, 8
        "Function_9_20D6",         # 09, 9
        "Function_10_2880",        # 0A, 10
        "Function_11_37E2",        # 0B, 11
        "Function_12_39F3",        # 0C, 12
        "Function_13_3C2A",        # 0D, 13
        "Function_14_4067",        # 0E, 14
        "Function_15_48AF",        # 0F, 15
        "Function_16_4BA8",        # 10, 16
        "Function_17_524B",        # 11, 17
    ))


    def Function_0_1BC(): pass

    label("Function_0_1BC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1FC"),
        (1, "loc_208"),
        (2, "loc_214"),
        (3, "loc_220"),
        (4, "loc_22C"),
        (5, "loc_238"),
        (6, "loc_244"),
        (SWITCH_DEFAULT, "loc_250"),
    )


    label("loc_1FC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_208")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_214")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_220")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_22C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_238")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_244")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_250")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_25C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_273")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_273")

    Return()

    # Function_0_1BC end

    def Function_1_274(): pass

    label("Function_1_274")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29E")
    OP_94(0xFE, 0x51E, 0xF6E, 0xFFFFF704, 0x154, 0x3E8)
    Sleep(300)
    Jump("Function_1_274")

    label("loc_29E")

    Return()

    # Function_1_274 end

    def Function_2_29F(): pass

    label("Function_2_29F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C9")
    OP_94(0xFE, 0xFFFFF2EA, 0x30C0, 0x3E8, 0x39C6, 0x3E8)
    Sleep(300)
    Jump("Function_2_29F")

    label("loc_2C9")

    Return()

    # Function_2_29F end

    def Function_3_2CA(): pass

    label("Function_3_2CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F4")
    OP_94(0xFE, 0x884, 0xFFFFFAEC, 0x1784, 0x168, 0x3E8)
    Sleep(300)
    Jump("Function_3_2CA")

    label("loc_2F4")

    Return()

    # Function_3_2CA end

    def Function_4_2F5(): pass

    label("Function_4_2F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31F")
    OP_94(0xFE, 0x119E, 0xDA2, 0x1716, 0x1BBC, 0x3E8)
    Sleep(300)
    Jump("Function_4_2F5")

    label("loc_31F")

    Return()

    # Function_4_2F5 end

    def Function_5_320(): pass

    label("Function_5_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_336")
    Event(0, 14)

    label("loc_336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_386")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 5350, 4000, 6980, 180)
    SetChrPos(0xA, 5350, 4000, 6410, 0)
    SetChrPos(0xE, 5590, 0, -2120, 180)
    SetChrFlags(0xA, 0x10)
    Jump("loc_80B")

    label("loc_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3CE")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, -1000, 0, 3400, 270)
    SetChrPos(0xA, -1060, 4000, 13010, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3C9")
    SetChrFlags(0xE, 0x10)

    label("loc_3C9")

    Jump("loc_80B")

    label("loc_3CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_425")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -1210, 4000, 13380, 135)
    SetChrPos(0xA, 5230, 4000, 6980, 180)
    SetChrPos(0xB, 5230, 4000, 6250, 0)
    BeginChrThread(0xB, 0, 0, 0)
    BeginChrThread(0x8, 0, 0, 2)
    SetChrFlags(0xA, 0x10)
    Jump("loc_80B")

    label("loc_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_46F")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -2100, 4000, 17500, 270)
    SetChrPos(0xA, 1450, 4000, 9960, 315)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46A")
    SetChrFlags(0xA, 0x10)

    label("loc_46A")

    Jump("loc_80B")

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4A5")
    SetChrPos(0x8, -1210, 4000, 13380, 135)
    BeginChrThread(0x8, 0, 0, 2)
    SetChrPos(0xA, 3490, 4000, 8150, 315)
    Jump("loc_80B")

    label("loc_4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4DF")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrPos(0xA, 3490, 4000, 8150, 315)
    Jump("loc_80B")

    label("loc_4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_501")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_80B")

    label("loc_501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_54B")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, -1210, 4000, 13380, 135)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_80B")

    label("loc_54B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5A1")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrPos(0xA, 5230, 4000, 6980, 180)
    SetChrPos(0xB, 5230, 4000, 6250, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    Jump("loc_80B")

    label("loc_5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5FC")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 5230, 4000, 6980, 180)
    SetChrPos(0xB, 5230, 4000, 6250, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    Jump("loc_80B")

    label("loc_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_61B")
    SetChrPos(0xA, 3310, 4000, 4760, 270)
    Jump("loc_80B")

    label("loc_61B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_67C")
    SetChrPos(0x8, -1210, 4000, 13380, 135)
    BeginChrThread(0x8, 0, 0, 2)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 5230, 4000, 6980, 180)
    SetChrPos(0xB, 5230, 4000, 6420, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_677")
    SetChrFlags(0xA, 0x10)

    label("loc_677")

    Jump("loc_80B")

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6C7")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrPos(0xA, 5250, 4000, 8250, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6C2")
    SetChrFlags(0xA, 0x10)

    label("loc_6C2")

    Jump("loc_80B")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_77A")
    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_721")
    SetChrPos(0xA, 5250, 4000, 8250, 180)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71C")
    SetChrFlags(0xA, 0x10)

    label("loc_71C")

    Jump("loc_775")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_END)), "loc_754")
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_775")

    label("loc_754")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrSubChip(0xC, 0x1)
    SetChrSubChip(0xD, 0x2)

    label("loc_775")

    Jump("loc_80B")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7BF")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xA, 3760, 0, -450, 270)
    BeginChrThread(0xA, 0, 0, 3)
    Jump("loc_80B")

    label("loc_7BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7F2")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_80B")

    label("loc_7F2")

    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80B")
    SetChrFlags(0xA, 0x10)

    label("loc_80B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_81A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 16)

    label("loc_81A")

    Return()

    # Function_5_320 end

    def Function_6_81B(): pass

    label("Function_6_81B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_834")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_83A")

    label("loc_834")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_856")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_86D")

    label("loc_856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_86D")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_86D")

    label("loc_86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_897")
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B7")
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_8B7")

    Return()

    # Function_6_81B end

    def Function_7_8B8(): pass

    label("Function_7_8B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_9A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_93E")

    #C0001
    ChrTalk(
        0x8,
        (
            "チッ、専務のヤロー\x01",
            "俺の態度がデカイだと？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "誰のお陰であのピンチを\x01",
            "乗り切れたと思ってやがるんだ！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99E")

    label("loc_93E")


    #C0003
    ChrTalk(
        0x8,
        "アア？　なんだ貴様らは……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "今俺は気が立ってるんだ。\x01",
            "さっさと出て行ってもらおうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_99E")

    Jump("loc_F89")

    label("loc_9A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_AB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A11")

    #C0005
    ChrTalk(
        0x8,
        "いや……俺が凄すぎるのか？\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "ハハ、まあいい。\x01",
            "どちらでも同じことさ、ハハハッ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAC")

    label("loc_A11")


    #C0007
    ChrTalk(
        0x8,
        (
            "ははっ、馬鹿め……\x01",
            "その証券は３日で値が落ちる。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "そんな事も予測できないのか？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "クロスベル通信社の経済誌も\x01",
            "落ちたものだな、ハハハハッ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AAC")

    Jump("loc_F89")

    label("loc_AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B0E")

    #C0010
    ChrTalk(
        0x8,
        (
            "ミラならたんまりある……\x01",
            "導力車の一台くらい\x01",
            "買っておくとするか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB8")

    label("loc_B0E")


    #C0011
    ChrTalk(
        0x8,
        (
            "ウーン、いいねェ。\x01",
            "カタログを取り寄せた甲斐があったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "この導力車のフォルムには\x01",
            "惚れ惚れするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "ハハ、証券マンなら\x01",
            "導力車の一台くらいは欲しい所だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_BB8")

    Jump("loc_F89")

    label("loc_BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_BCB")
    Jump("loc_F89")

    label("loc_BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_BD9")
    Jump("loc_F89")

    label("loc_BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_BE7")
    Jump("loc_F89")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C85")
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x8,
        (
            "ああもキッパリ言われると\x01",
            "妻の事が判らなくなってくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "僕にどうして欲しいとかは\x01",
            "ないんだろうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1B")

    label("loc_C85")


    #C0016
    ChrTalk(
        0x8,
        "……妻は良家の出身でね。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "その、こういった事には疎いんだよ。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "しかしまあ、嫌だとかＯＫだとか\x01",
            "そのくらいの返事は期待していたんだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D1B")

    Jump("loc_F89")

    label("loc_D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D92")

    #C0019
    ChrTalk(
        0x8,
        "これは大きなチャンスだが……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "いやいや、やはりここは\x01",
            "妻の意見を聞いてからだな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E67")

    label("loc_D92")


    #C0021
    ChrTalk(
        0x8,
        "我が社の業績も上々でね。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "来月から帝国東部\x01",
            "クロイツェン州にも\x01",
            "支部を構えることになったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "…………………………\x01",
            "……どうしようか………\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "上からは支部長をやらないかと\x01",
            "言われているんだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E67")

    Jump("loc_F89")

    label("loc_E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_E7A")
    Jump("loc_F89")

    label("loc_E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_E88")
    Jump("loc_F89")

    label("loc_E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_E96")
    Jump("loc_F89")

    label("loc_E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_EA4")
    Jump("loc_F89")

    label("loc_EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F01")

    #C0025
    ChrTalk(
        0x8,
        "妻は何かとのんびり屋なんだ。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "仕方がない……\x01",
            "紅茶は自分で淹れようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F89")

    label("loc_F01")


    #C0027
    ChrTalk(
        0x8,
        (
            "仕事の方もようやく一息ついた。\x01",
            "妻の淹れた紅茶でも飲もうかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "と思ったら妻がいないよ。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        "まだ水遣りをしているのかな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F89")

    TalkEnd(0xFE)
    Return()

    # Function_7_8B8 end

    def Function_8_F8D(): pass

    label("Function_8_F8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FAF")
    Call(0, 15)
    Return()

    label("loc_FAF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1043")
    Jump("loc_108D")

    label("loc_1043")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1063")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_108D")

    label("loc_1063")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1083")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_108D")

    label("loc_1083")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_108D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_122E")
    OP_64(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A5")

    #C0030
    ChrTalk(
        0xFE,
        "……マズイ、何てことだ……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "記念祭の間に１日だけ休みを取ったら、\x01",
            "その日に損失が出てしまったんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "これはマズイ……　\x01",
            "お得意先の証券だったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "明るみになる前に\x01",
            "何としても穴埋めしなければ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1217")

    label("loc_11A5")


    #C0034
    ChrTalk(
        0xFE,
        (
            "うちは信用第一の証券会社なんだ……\x01",
            "明るみにはできない……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "何としても今週のうちに\x01",
            "穴埋めをしなければ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1217")

    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_20CE")

    label("loc_122E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_128B")

    #C0036
    ChrTalk(
        0xC,
        "は、腹が減ったな……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xC,
        (
            "妻と娘も帰ってこないし\x01",
            "ピザの出前でも頼むか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20CE")

    label("loc_128B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1324")

    #C0038
    ChrTalk(
        0xC,
        "さて、ラインフォルト社の株は……と。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xC,
        (
            "みんなが浮かれているときこそ\x01",
            "チャンスがあったりするものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        "証券マンは気が抜けないよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20CE")

    label("loc_1324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_147A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13B0")

    #C0041
    ChrTalk(
        0xC,
        (
            "今年は予想以上に\x01",
            "景気のいい出足だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "もっとも証券ディーラーの\x01",
            "正念場はこれからだ。\x01",
            "慎重に見守らないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1475")

    label("loc_13B0")


    #C0043
    ChrTalk(
        0xC,
        (
            "記念祭の間は\x01",
            "どこの株も大きく値を上げたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xC,
        (
            "アルカンシェルも大成功と言えるし\x01",
            "ミシュラムのテーマパークも好調だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xC,
        (
            "ホテルや飲食業は\x01",
            "満席になった所もあるようだね。\x01",
            "これも興味深いよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1475")

    Jump("loc_20CE")

    label("loc_147A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_155E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14C6")

    #C0046
    ChrTalk(
        0xC,
        (
            "つ、妻も娘もいなくて寂しいが、\x01",
            "仕事を頑張るよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1559")

    label("loc_14C6")


    #C0047
    ChrTalk(
        0xC,
        (
            "妻が退屈そうにしているから、\x01",
            "出かけてきなさいと言ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        "そうしたら喜んで支度を始めたよ。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xC,
        (
            "そんなに祭りを\x01",
            "見たかったのかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1559")

    Jump("loc_20CE")

    label("loc_155E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_16AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15DB")

    #C0050
    ChrTalk(
        0xC,
        (
            "記念祭は証券ディーラーに\x01",
            "とっても正念場だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xC,
        (
            "……当然休みなんてない。\x01",
            "毎日が真剣勝負だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AA")

    label("loc_15DB")


    #C0052
    ChrTalk(
        0xC,
        (
            "創立記念祭の間は\x01",
            "さまざまな株価指数が動くんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xC,
        (
            "記念祭を当て込んだ\x01",
            "投資も過熱しているからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xC,
        (
            "クロスベル中で激しい\x01",
            "ヒートアップとクールダウンが\x01",
            "繰り返されるだろう……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xC,
        "目が離せないよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_16AA")

    Jump("loc_20CE")

    label("loc_16AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1823")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1736")

    #C0056
    ChrTalk(
        0xC,
        (
            "帝国の支部長にならなくても\x01",
            "大きな仕事は山ほどある。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xC,
        (
            "家族の事も心配だし\x01",
            "クロスベルで頑張る事にしたよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181E")

    label("loc_1736")


    #C0058
    ChrTalk(
        0xC,
        (
            "帝国支部の支部長の件……\x01",
            "結局断ってしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xC,
        (
            "妻はあの調子だし、\x01",
            "僕も気が抜けてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xC,
        (
            "証券ディーラーとしては\x01",
            "大きなチャンスだったと思うが……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xC,
        (
            "よく考えれば\x01",
            "別に帝国に行かなくとも\x01",
            "仕事は山ほどあるからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_181E")

    Jump("loc_20CE")

    label("loc_1823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1AA8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1974")

    #C0062
    ChrTalk(
        0xFE,
        (
            "昨日遊撃士の人が訪ねてきてね。\x01",
            "我が家で仔猫を飼えないかって\x01",
            "相談にきたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "突然の事で僕も驚いたんだが……\x01",
            "どうやらサニータが\x01",
            "こっそり世話をしていた仔猫らしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "あの子は、自分だけじゃ\x01",
            "話を切り出せないでいたんだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "遊撃士さんのお陰で\x01",
            "家族が１人増えてしまったよ。\x01",
            "ははは。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A07")

    label("loc_1974")


    #C0066
    ChrTalk(
        0xFE,
        (
            "遊撃士さんの提案でね、\x01",
            "サニータの望みどおり、\x01",
            "野良の仔猫を飼う事にしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "はは、あの様子を見ていると\x01",
            "やっぱり飼う事にして良かったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A07")

    Jump("loc_1AA3")

    label("loc_1A0C")


    #C0068
    ChrTalk(
        0xFE,
        (
            "サニータは昨日から\x01",
            "仔猫につきっきりなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "ペットの世話は大変だし、\x01",
            "根を上げるんじゃないかと思ったけど……\x01",
            "あの様子じゃ心配無さそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA3")

    Jump("loc_20CE")

    label("loc_1AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1E91")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B84")

    #C0070
    ChrTalk(
        0xFE,
        (
            "サニータは早速\x01",
            "仔猫に首ったけみたいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "そんなに好きなら\x01",
            "相談してくれれば良かったのに……\x01",
            "と思うんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "まあ、あの子なりに\x01",
            "悩んでいたんだろうな。\x01",
            "悪い事をしたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BDB")

    label("loc_1B84")


    #C0073
    ChrTalk(
        0xFE,
        "ともあれ、君達には礼を言うよ。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "はは、サニータが\x01",
            "散々お世話になっちゃったね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDB")

    Jump("loc_1E8C")

    label("loc_1BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_END)), "loc_1CBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6C")

    #C0075
    ChrTalk(
        0xFE,
        (
            "サニータはまたどこかへ\x01",
            "出かけてしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "おかしいな、いつもは\x01",
            "本を読んでくれと\x01",
            "せがむんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CB8")

    label("loc_1C6C")


    #C0077
    ChrTalk(
        0xFE,
        (
            "サニータは最近\x01",
            "様子がおかしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "ひょっとして\x01",
            "反抗期かなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB8")

    Jump("loc_1E8C")

    label("loc_1CBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_1D31")

    #C0079
    ChrTalk(
        0xFE,
        (
            "我が家ではペットは\x01",
            "飼っていないね……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "役に立てなかったようで\x01",
            "申し訳ないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xC, 0x1)
    Return()

    label("loc_1D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEF")

    #C0081
    ChrTalk(
        0xFE,
        (
            "仕事の息抜きに\x01",
            "娘に本を読んでやっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "……ところで君たち、\x01",
            "僕の書類を荒らしたりは\x01",
            "してないよね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "……いや、気にしないでくれ。\x01",
            "こちらの話なんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E80")

    label("loc_1DEF")


    #C0084
    ChrTalk(
        0xFE,
        (
            "時折、机に置いていた書類が\x01",
            "破られたりしていてね……\x01",
            "仕事がはかどらないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "サニータはそんな事しないし、\x01",
            "一体誰の仕業だろうなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E80")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xC, 0x1)
    Return()

    label("loc_1E8C")

    Jump("loc_20CE")

    label("loc_1E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1F65")
    SetChrSubChip(0xC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F25")

    #C0086
    ChrTalk(
        0xFE,
        "ええと、あの証券の書類は……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "……そうだった。\x01",
            "先週に破られていたんだっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "うーむ、しかし一体誰が……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F60")

    label("loc_1F25")


    #C0089
    ChrTalk(
        0xFE,
        (
            "こう立て続けに書類がだめになると\x01",
            "仕事が出来ないな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F60")

    Jump("loc_20CE")

    label("loc_1F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_20CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FEA")

    #C0090
    ChrTalk(
        0xC,
        (
            "近年は様々な金融商品が\x01",
            "開発されていて、\x01",
            "取引にも専門知識が必要だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        "ま、素人にはオススメできないな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20CE")

    label("loc_1FEA")


    #C0092
    ChrTalk(
        0xC,
        (
            "知っているかい？\x01",
            "クロスベルでは昔から\x01",
            "証券や先物取引が盛んなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xC,
        (
            "我が社では特に証券を扱っている。\x01",
            "いわゆる証券取引会社だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xC,
        (
            "特に近年は様々な金融商品が\x01",
            "開発されているからね。\x01",
            "取引にも専門知識が必要なんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20CE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_F8D end

    def Function_9_20D6(): pass

    label("Function_9_20D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_21E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2130")

    #C0095
    ChrTalk(
        0x9,
        "そんな……主人に限って……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        "あの人は実直でしたのに……\x02",
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_2130")


    #C0097
    ChrTalk(
        0x9,
        "主人はまだ帰ってきませんの。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "あのぅ、もしかして\x01",
            "主人は行方不明なのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "そんな……主人に限って……\x01",
            "ううっ、心配ですの……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_21E3")

    Jump("loc_287C")

    label("loc_21E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2282")

    #C0101
    ChrTalk(
        0x9,
        (
            "あの、あの……\x01",
            "主人が居ないんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        "主人は見つかるでしょうか。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#0003Fすみません、警察の方でも\x01",
            "全力を尽くしてみますので……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_2282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_23AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_22FB")

    #C0104
    ChrTalk(
        0x9,
        (
            "明日はソフィアさんのお宅で\x01",
            "お料理がありますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "うふふ、ばっちり\x01",
            "世間話をしてきますの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23A5")

    label("loc_22FB")


    #C0106
    ChrTalk(
        0x9,
        (
            "娘のサニータは\x01",
            "ソフィアさんの所のコリン君と\x01",
            "同い年なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        "ふふ、世間話も弾んじゃいますの。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "明日はお料理教室の日ですし\x01",
            "ばっちりお話ができそうですの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_23A5")

    Jump("loc_287C")

    label("loc_23AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_23F8")

    #C0109
    ChrTalk(
        0x9,
        "主人がなんだか塞ぎこんでいますの。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        "どうしたのかしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_23F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2462")

    #C0111
    ChrTalk(
        0xFE,
        (
            "サニータが\x01",
            "猫ちゃんと遊んでいますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "羨ましいですわ。\x01",
            "私も一緒に遊びたいですの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_2462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_25A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_24DB")

    #C0113
    ChrTalk(
        0x9,
        (
            "私、お仕事の事は\x01",
            "よく分からないんですもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "主人の好きなように\x01",
            "するといいと思いますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_259E")

    label("loc_24DB")


    #C0115
    ChrTalk(
        0x9,
        (
            "主人が帝国に単身赴任\x01",
            "するかもしれないと言うんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "……もちろん『お好きなように』\x01",
            "と言っておきましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "だって主人の仕事ですもの。\x01",
            "主人の思うように\x01",
            "するといいと思いますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_259E")

    Jump("loc_287C")

    label("loc_25A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2730")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2692")

    #C0118
    ChrTalk(
        0xFE,
        (
            "サニータが突然\x01",
            "かわいい仔猫を飼い始めたんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "主人はもう\x01",
            "知っていたみたいですけど……\x01",
            "私とっても驚きましたの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    #C0120
    ChrTalk(
        0xFE,
        (
            "サニータと仔猫は\x01",
            "とても仲が良さそうですの。\x01",
            "羨ましいですの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_272B")

    label("loc_2692")


    #C0121
    ChrTalk(
        0xFE,
        (
            "あら……いけませんの。\x01",
            "今日はソフィアさんのお宅で\x01",
            "お料理を教わる約束なんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "うふふ、猫ちゃんの事はともかく\x01",
            "急がないと遅れてしまいますの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_272B")

    Jump("loc_287C")

    label("loc_2730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_273E")
    Jump("loc_287C")

    label("loc_273E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_27C0")

    #C0123
    ChrTalk(
        0x9,
        (
            "主人は家にいても仕事仕事ですの。\x01",
            "うふふ、おかしな人。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "それとも世の中の男の人は\x01",
            "みんなそうなのでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_27C0")


    #C0125
    ChrTalk(
        0xFE,
        "主人は家にいても仕事仕事ですの。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "お休みもとらないし、\x01",
            "趣味といってもたまに娘に\x01",
            "本を読んでやるくらいですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "……よほど仕事が好きなんですのね。\x01",
            "うふふ、おかしな人ですの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_287C")

    TalkEnd(0xFE)
    Return()

    # Function_9_20D6 end

    def Function_10_2880(): pass

    label("Function_10_2880")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_28C0")

    #C0128
    ChrTalk(
        0xA,
        (
            "うぐ、うぐ……\x01",
            "………お父さまぁ～………！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DE")

    label("loc_28C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2A71")
    OP_63(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0129
    ChrTalk(
        0xA,
        (
            "お父さまが……お父さまが\x01",
            "いなくなってしまったの！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "うぐ、うぐ……\x01",
            "ふ、ふえぇ～～～んっ……！！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A69")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A10")

    #C0131
    ChrTalk(
        0x103,
        (
            "#0200F確か以前、相談に乗ってあげて\x01",
            "仔猫を飼うことにしたご家庭ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        (
            "#0108Fご主人も\x01",
            "優しそうな人だったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#0001Fああ……先を急いだ方が\x01",
            "良さそうだな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A69")

    label("loc_2A10")


    #C0134
    ChrTalk(
        0x103,
        "#0200Fお子さんもいたんですね……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#0001Fああ……先を急いだ方が\x01",
            "良さそうだな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A69")

    SetScenarioFlags(0x0, 2)
    Jump("loc_37DE")

    label("loc_2A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_2AF6")
    OP_4B(0xB, 0xFF)

    #C0136
    ChrTalk(
        0xA,
        (
            "ねえマリー……お父さまは\x01",
            "どうしちゃったのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        "マリーはなにかしらない……？\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        "フニャン……？\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_37DE")

    label("loc_2AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2DD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_END)), "loc_2C26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2B93")

    #C0139
    ChrTalk(
        0xA,
        (
            "お母さまは\x01",
            "きょうはおりょうりきょうしつだし……\x01",
            "いつも少しのんびりですもの……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "サニータが\x01",
            "しっかりしなくちゃ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C21")

    label("loc_2B93")


    #C0141
    ChrTalk(
        0xA,
        (
            "お、お父さまはきっと\x01",
            "つかれてらっしゃるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xA,
        (
            "なんだかおかしいのは\x01",
            "きっとそのせいだわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "サニータが\x01",
            "なんとかしなくちゃ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2C21")

    Jump("loc_2DCE")

    label("loc_2C26")

    OP_64(0xA)

    #C0144
    ChrTalk(
        0xA,
        "………お父さま………………\x02",
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

    #C0145
    ChrTalk(
        0x101,
        "#0005Fどうかしたのかい？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0xA, 0x0, 750)
    Sleep(750)

    #C0146
    ChrTalk(
        0xA,
        "な、なんでもありませんわ。\x02",
    )

    CloseMessageWindow()
    OP_64(0xA)

    #C0147
    ChrTalk(
        0xA,
        (
            "ただ、その……\x01",
            "この前からお父さまが……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        "ハハハッ、馬鹿どもめ……！\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x13B, 0x2EE)

    #C0149
    ChrTalk(
        0xA,
        (
            "お父さま……\x01",
            "どうしちゃったのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#0005F（？？？\x01",
            "  何か様子が\x01",
            "  おかしいみたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0xCD, 0)

    label("loc_2DCE")

    Jump("loc_37DE")

    label("loc_2DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2E56")
    OP_93(0xFE, 0x13B, 0x0)

    #C0151
    ChrTalk(
        0xFE,
        (
            "お父様……\x01",
            "どうしちゃったのかしら……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    #C0152
    ChrTalk(
        0xFE,
        "な、なんでもありませんわ。\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x13B, 0x0)
    Jump("loc_37DE")

    label("loc_2E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2EDA")

    #C0153
    ChrTalk(
        0xFE,
        (
            "お父さま、きょうはあそんでくれるって\x01",
            "おっしゃっていたのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "おしごといそがしいのかしら……\x01",
            "しょんぼり……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DE")

    label("loc_2EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2F4A")

    #C0155
    ChrTalk(
        0xA,
        (
            "ダメよ、マリー。\x01",
            "きょうはおふろの日なんだから！\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xA,
        (
            "ちゃんと水あびして、\x01",
            "きれいになるのよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DE")

    label("loc_2F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_309B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2FFE")
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0xA, 0x0, 750)
    Sleep(750)

    #C0157
    ChrTalk(
        0xA,
        "あっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0xA, 0xB, 750)
    Sleep(750)
    OP_64(0xA)

    #C0158
    ChrTalk(
        0xA,
        (
            "コホン、いいことマリー。\x01",
            "おきゃくさまの前では、\x01",
            "おぎょうぎよくするのよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3096")

    label("loc_2FFE")


    #C0159
    ChrTalk(
        0xA,
        (
            "ねえマリー、\x01",
            "ミルクをもってきたわよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xA,
        (
            "きょうのはアルモリカむらの\x01",
            "じょーとーなミルクなんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        (
            "きっととっても\x01",
            "おいちいんだから～♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3096")

    Jump("loc_37DE")

    label("loc_309B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3111")

    #C0162
    ChrTalk(
        0xA,
        (
            "お父さまとお母さま、\x01",
            "なにをはなしていたのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "サニータがきいちゃ\x01",
            "いけないお話かしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DE")

    label("loc_3111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3182")

    #C0164
    ChrTalk(
        0xA,
        (
            "マリーはとっても\x01",
            "あまえんぼうなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        (
            "サニータがなでてあげなきゃ\x01",
            "ダメなんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_325D")

    label("loc_3182")

    OP_4B(0xB, 0xFF)
    Sound(823, 0, 100, 0)

    #C0166
    ChrTalk(
        0xA,
        (
            "きゃっ、マリーったら……\x01",
            "くすぐったいじゃないの……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 750)
    Sleep(750)

    #C0167
    ChrTalk(
        0xA,
        (
            "マ、マリーはとっても\x01",
            "あまえんぼうなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "ときどきなでてあげないと、\x01",
            "さみちくなってしまうんだから。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_325D")

    Jump("loc_37DE")

    label("loc_3262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3423")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_337E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3334")
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0169
    ChrTalk(
        0xA,
        (
            "マリー、マリー！\x01",
            "いっしょにあそびましょ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 750)
    Sleep(750)

    #C0170
    ChrTalk(
        0xA,
        "あ……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xA,
        (
            "コ、コホン……\x01",
            "マリーはきょうもげんきですわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x2EE)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_3379")

    label("loc_3334")


    #C0172
    ChrTalk(
        0xA,
        "コ、コホン……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "おかげさまで\x01",
            "マリーはきょうもげんきですわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3379")

    Jump("loc_341E")

    label("loc_337E")


    #C0174
    ChrTalk(
        0xA,
        "マリーがかえってきたの！\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        (
            "ゆーげきしのお姉さんが\x01",
            "つれてきてくれたのですわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    TurnDirection(0xA, 0xB, 750)
    Sleep(750)

    #C0176
    ChrTalk(
        0xA,
        (
            "マリー、マリー！\x01",
            "いっしょにあそびましょ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_341E")

    Jump("loc_37DE")

    label("loc_3423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3553")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_349A")

    #C0177
    ChrTalk(
        0xA,
        (
            "マリーのめんどうは\x01",
            "サニータがみるんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "コホン、これは\x01",
            "じゃれてるのではないのよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354E")

    label("loc_349A")


    #C0179
    ChrTalk(
        0xA,
        (
            "マリー、マリー！\x01",
            "こっちむいてちょうだい～♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 500)
    Sleep(500)

    #C0180
    ChrTalk(
        0xA,
        "コ、コホン……\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xA,
        (
            "きょうのことは\x01",
            "サニータかんしゃしますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        "そ、それだけですもの！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_354E")

    Jump("loc_37DE")

    label("loc_3553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_35E1")

    #C0183
    ChrTalk(
        0xA,
        (
            "お父さま、だいじなしょるいが\x01",
            "だめになってこまってるみたい……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xA,
        (
            "…………………………\x01",
            "わ、わたしはなんにも知らないもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DE")

    label("loc_35E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_36FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3650")

    #C0185
    ChrTalk(
        0xA,
        (
            "サニータだってきょうは\x01",
            "あそんでもらえないんだもの。\x01",
            "じゃまをしちゃダメなんだから！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F8")

    label("loc_3650")


    #C0186
    ChrTalk(
        0xA,
        (
            "お父さまはむずかしい\x01",
            "おちごとをなさっているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        (
            "しょうけんディーラーという\x01",
            "とてもえらい方なんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        (
            "じゃまをしたら、\x01",
            "サニータがゆるしませんわよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_36F8")

    Jump("loc_37DE")

    label("loc_36FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_376D")

    #C0189
    ChrTalk(
        0xA,
        "あら、なにかごよう？\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xA,
        (
            "みしらぬレディに声をかけるなんて、\x01",
            "しつれいなかたね。\x01",
            "……ぷんっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DE")

    label("loc_376D")


    #C0191
    ChrTalk(
        0xA,
        "パジャマはたたんでひきだしに……\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xA,
        (
            "お母さまはどこかたよりないから、\x01",
            "サニータがしっかりしないと。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_37DE")

    TalkEnd(0xFE)
    Return()

    # Function_10_2880 end

    def Function_11_37E2(): pass

    label("Function_11_37E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3804")
    Call(0, 15)
    Return()

    label("loc_3804")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3898")
    Jump("loc_38E2")

    label("loc_3898")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_38B8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38E2")

    label("loc_38B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38D8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38E2")

    label("loc_38D8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38E2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_398E")

    #C0193
    ChrTalk(
        0xD,
        (
            "サ、サニータは\x01",
            "なにもしりませんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xD,
        (
            "ぷんっ、お、お父さまと\x01",
            "ご本をよんでいるの。\x01",
            "じゃましないでくださる！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39E7")

    label("loc_398E")


    #C0195
    ChrTalk(
        0xD,
        (
            "あら、お父さまにご本を\x01",
            "よんでもらっているんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xD,
        "じゃましないでくださる！？\x02",
    )

    CloseMessageWindow()

    label("loc_39E7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xD, 0x2)
    Return()

    # Function_11_37E2 end

    def Function_12_39F3(): pass

    label("Function_12_39F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3A18")

    #C0197
    ChrTalk(
        0xB,
        "フニャアン……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3A3E")

    #C0198
    ChrTalk(
        0xB,
        "フニャアニャア……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3A60")

    #C0199
    ChrTalk(
        0xB,
        "フニャン……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A80")

    #C0200
    ChrTalk(
        0xB,
        "フニャア……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3AA0")

    #C0201
    ChrTalk(
        0xB,
        "フニャン……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3AC2")

    #C0202
    ChrTalk(
        0xB,
        "ニャーオ……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3AE2")

    #C0203
    ChrTalk(
        0xB,
        "ニャーオ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3B04")

    #C0204
    ChrTalk(
        0xB,
        "ニャオン……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B22")

    #C0205
    ChrTalk(
        0xB,
        "ニャー……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3B42")

    #C0206
    ChrTalk(
        0xB,
        "ニャーオ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3B80")
    OP_63(0xB, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0207
    ChrTalk(
        0xB,
        "フニャァァン……！\x02",
    )

    CloseMessageWindow()
    OP_64(0xB)
    Jump("loc_3C26")

    label("loc_3B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3BA8")

    #C0208
    ChrTalk(
        0xB,
        "ンニャンニャン……♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3BC8")

    #C0209
    ChrTalk(
        0xB,
        "ニャーオ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3BF0")

    #C0210
    ChrTalk(
        0xB,
        "ンニャンニャン……♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3C12")

    #C0211
    ChrTalk(
        0xB,
        "ニャオン……♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C26")

    label("loc_3C12")


    #C0212
    ChrTalk(
        0xB,
        "フニャア……♪\x02",
    )

    CloseMessageWindow()

    label("loc_3C26")

    TalkEnd(0xFE)
    Return()

    # Function_12_39F3 end

    def Function_13_3C2A(): pass

    label("Function_13_3C2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3E13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3CB9")

    #C0213
    ChrTalk(
        0xE,
        (
            "#3701Fご主人、どこへ\x01",
            "行ってしまったのでしょうか……\x02\x03",

            "とても家族を置いて\x01",
            "出て行く人じゃ\x01",
            "ありませんでしたのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E0E")

    label("loc_3CB9")


    #C0214
    ChrTalk(
        0xE,
        (
            "#3701F支援課の皆さん……\x02\x03",

            "クレイユさんとサニータちゃんは\x01",
            "落ち着いたのですけれど、\x01",
            "やっぱり不安なのだと思います。\x02\x03",

            "#3708F無理もありません……\x01",
            "私もコリンが居なくなったときは\x01",
            "取り乱してしまいましたから……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        (
            "#0000Fすみません、もう少し\x01",
            "傍に居てあげてもらえますか。\x02\x03",

            "警察の方も\x01",
            "全力を挙げていますので……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xE,
        "#3700Fはい、それはもう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3E0E")

    Jump("loc_4063")

    label("loc_3E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3E7F")
    OP_4B(0x9, 0xFF)

    #C0217
    ChrTalk(
        0xE,
        (
            "#3700Fクレイユさん、\x01",
            "落ち着いて下さいな。\x02\x03",

            "きっとご主人は大丈夫ですわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_4063")

    label("loc_3E7F")


    #C0218
    ChrTalk(
        0xE,
        (
            "#3708Fクレイユさんとは付き合いがあって、\x01",
            "何度かご主人にも会っています。\x02\x03",

            "……まさか……何かの事件に\x01",
            "巻き込まれてしまったのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#0103Fソフィアさん、できるだけ\x01",
            "深刻な顔はなさらないで下さい。\x02\x03",

            "#0100Fご家族の方も\x01",
            "心配になるでしょうし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0220
    ChrTalk(
        0xE,
        (
            "#3705Fそ、そうですね。\x01",
            "ごめんなさい、つい……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x104,
        (
            "#0304Fこんな時は\x01",
            "深く考えないのが一番ッスよ。\x02\x03",

            "#0300Fお茶でも淹れてあげると\x01",
            "いいんじゃないスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xE,
        (
            "#3700Fはい、そうですね。\x01",
            "そうしてみます。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x9, 750)
    SetChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 3)

    label("loc_4063")

    TalkEnd(0xFE)
    Return()

    # Function_13_3C2A end

    def Function_14_4067(): pass

    label("Function_14_4067")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_68(1000, 1400, -3250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 1500, 50, -6500, 360)
    SetChrPos(0x102, 500, 50, -6750, 360)
    SetChrPos(0x103, 1500, 50, -7750, 360)
    SetChrPos(0x104, 500, 50, -8000, 360)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_411E():
        OP_97(0xFE, 0x0, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_411E)

    def lambda_4138():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4138)
    Sleep(50)

    def lambda_414C():
        OP_97(0xFE, 0x0, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_414C)

    def lambda_4166():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4166)
    Sleep(50)

    def lambda_417A():
        OP_97(0xFE, 0x0, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_417A)

    def lambda_4194():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4194)
    Sleep(50)

    def lambda_41A8():
        OP_97(0xFE, 0x0, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_41A8)

    def lambda_41C2():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_41C2)
    SetCameraDistance(21000, 2500)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0223
    ChrTalk(
        0x101,
        (
            "#0001F#11P一課の資料によると\x01",
            "たしかこの家のはずだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0224
    ChrTalk(
        0x103,
        "#0205Fあれは……\x02",
    )

    CloseMessageWindow()
    OP_68(-1750, 1400, 3120, 3000)
    OP_6F(0x79)

    #C0225
    ChrTalk(
        0x9,
        "あの、あの……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x9,
        "わたくし、一体どうしたら……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xE,
        (
            "#3701Fクレイユさん、\x01",
            "どうか落ち着いてください。\x02\x03",

            "こうなったら誰かに\x01",
            "相談するしかないでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1750, 1400, 2120, 3000)

    def lambda_4355():
        OP_95(0x101, -750, 0, 1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4355)
    Sleep(50)

    def lambda_4372():
        OP_95(0x102, -1750, 0, 1250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4372)
    Sleep(50)

    def lambda_438F():
        OP_95(0x103, -750, 0, 250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_438F)
    Sleep(50)

    def lambda_43AC():
        OP_95(0x104, -1750, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43AC)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x0)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x0)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x0)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x0)
    OP_6F(0x79)

    #C0228
    ChrTalk(
        0x101,
        (
            "#0005Fあなたは\x01",
            "ハロルドさんの奥さんの……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_4447():
        TurnDirection(0xE, 0x101, 350)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4447)
    Sleep(50)

    def lambda_4457():
        TurnDirection(0x9, 0x101, 350)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4457)
    Sleep(1000)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x9, 1)

    #C0229
    ChrTalk(
        0xE,
        (
            "#3705Fあ……支援課の皆さん！\x02\x03",

            "#3700Fよかった……\x01",
            "実は困った事がありまして\x01",
            "どなたかに相談しようかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        (
            "#0101F……それはもしかして……\x01",
            "証券マンをなさっている\x01",
            "こちらのご主人の事とか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x9,
        "#5Pそうなんですの……\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x9,
        (
            "#5P今朝目を覚ましたら、\x01",
            "主人がいないんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x9,
        (
            "#5Pソフィアさんと２人で\x01",
            "ご近所を探してみたのですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#0003Fそ、そうですか……\x02\x03",

            "#0013Fあの、ご主人は最近\x01",
            "様子がおかしかったのでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x9,
        (
            "#5Pあ……そうかもしれませんの。\x01",
            "娘はずっと心配していましたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x104,
        (
            "#0303F……予想的中か。\x02\x03",

            "#0301F夜の間に消えたって事は\x01",
            "目撃者を見つけんのは難しそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4702")

    #C0237
    ChrTalk(
        0x101,
        (
            "#0008Fああ、今はともかく\x01",
            "失踪者の全員の確認を取ろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_472C")

    label("loc_4702")


    #C0238
    ChrTalk(
        0x101,
        "#0008Fああ、何か方法を考えないと……\x02",
    )

    CloseMessageWindow()

    label("loc_472C")

    TurnDirection(0x101, 0xE, 500)
    Sleep(300)

    #C0239
    ChrTalk(
        0x101,
        (
            "#0000Fソフィアさんは\x01",
            "こちらのご家族の方と\x01",
            "面識があるみたいですね。\x02\x03",

            "#0003Fあの……\x01",
            "警察の方でも捜索してみますが\x01",
            "時間が掛かるかもしれません。\x02\x03",

            "#0001Fしばらくご家族の方に\x01",
            "付き添っていて頂けますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xE,
        (
            "#3700Fええ、喜んで。\x02\x03",

            "主人もじきに\x01",
            "仕事から戻るはずですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        (
            "#0004Fすみません、では\x01",
            "この場はよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x9, 0xE, 0)
    TurnDirection(0xE, 0x9, 0)
    SetChrPos(0x0, -750, 0, 1550, 360)
    SetScenarioFlags(0xC8, 2)
    OP_29(0x4C, 0x1, 0xA)
    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_14_4067 end

    def Function_15_48AF(): pass

    label("Function_15_48AF")

    EventBegin(0x0)
    Fade(500)
    OP_68(6990, 5400, 8640, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(250, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x101, 6520, 4000, 8470, 135)
    SetChrPos(0x102, 5180, 4000, 9390, 135)
    SetChrPos(0x103, 4850, 4000, 8420, 135)
    SetChrPos(0x104, 6210, 4000, 9940, 135)
    OP_0D()

    #C0242
    ChrTalk(
        0x101,
        (
            "#5P#0000F（この家には小さい子が\x01",
            "  いるみたいだな……）\x02\x03",

            "あの、ちょっといい……ですか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)
    Sleep(300)

    #C0243
    ChrTalk(
        0xC,
        "#11Pおっと、何か御用かな。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#5P#0000Fはは、実は警察の方で\x01",
            "聞き込みをしていまして……\x02\x03",

            "こちらのお宅では\x01",
            "猫を飼ってらっしゃったり\x01",
            "しませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xC,
        "#11Pいや、そのような事は……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xC,
        "#11Pサニータ、何か知っているかい？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x2)

    #C0247
    ChrTalk(
        0xD,
        "#6Pな、なんにもしりませんわ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)
    Sleep(300)

    #C0248
    ChrTalk(
        0xD,
        (
            "#12Pぷんっ、お、お父さまと\x01",
            "ご本をよんでいるの。\x01",
            "じゃましないでくださる！？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x104,
        "#0306Fうーん、空振りか……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x103,
        (
            "#0200Fもう少し付近を\x01",
            "捜してみましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        (
            "#0100Fそうね、見落としが\x01",
            "あるかもしれないし。\x01",
            "一度戻ってみた方がいいかも。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 5580, 4000, 8480, 180)
    SetChrSubChip(0xD, 0x2)
    OP_29(0x8, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_15_48AF end

    def Function_16_4BA8(): pass

    label("Function_16_4BA8")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(-700, 1400, 560, 0)
    MoveCamera(46, 28, 0, 0)
    OP_6E(190, 0)
    SetCameraDistance(43500, 0)
    SetChrPos(0x101, -1260, 0, -1250, 0)
    SetChrPos(0x102, -1260, 0, -2800, 0)
    SetChrPos(0x103, -100, 0, -1250, 0)
    SetChrPos(0x104, -100, 0, -2800, 0)
    SetChrPos(0x8, -120, 0, 2930, 180)
    SetChrPos(0xA, -410, 0, 70, 0)
    SetChrPos(0xB, -1270, 0, 370, 45)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xA, 0x40)
    FadeToBright(2000, 0)
    OP_0D()

    #C0252
    ChrTalk(
        0x8,
        "#5Pうちで仔猫を飼いたい……？\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "#5Pなんだ……\x01",
            "そういうことだったのか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0254
    ChrTalk(
        0xA,
        "#12Pえっ……？\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        (
            "#5P最近サニータの様子がおかしいから\x01",
            "心配していたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x8,
        (
            "#5P勝手にどこかに\x01",
            "出かけちゃったりするしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        (
            "#5P書類も破られていたけど……\x01",
            "まあ大して重要な物ではなかったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xA,
        (
            "#12Pそれではお父さま、\x01",
            "マリーのこと、おこってませんの？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xA,
        (
            "#12Pマリーをおうちで\x01",
            "かってもいいんですの？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "#5Pああ、もちろんさ。\x01",
            "家族が増えるのは僕も大歓迎だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "#5Pただし……マリーの面倒は\x01",
            "ちゃんとサニータが見るんだよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xA,
        (
            "#12Pも、もちろんですわ。\x01",
            "ありがとう、お父さまっ……！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xA, 2, 0, 17)
    Sleep(600)
    OP_95(0xA, -210, 0, 2170, 6000, 0x0)
    Sound(804, 0, 100, 0)
    OP_A6(0x8, 0x0, 0x1E, 0x1F4, 0x9C4)
    OP_95(0xB, -1010, 0, 1980, 1000, 0x0)
    OP_93(0xB, 0x2D, 0x12C)
    Sleep(800)
    OP_68(-550, 1400, -890, 2500)
    Sleep(2500)

    #C0263
    ChrTalk(
        0x104,
        "#11P#0300Fハナシ、纏まったみてえだな。\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        (
            "#11P#0100Fいいお父さんで\x01",
            "よかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#11P#0200Fええ……\x01",
            "あの仔猫も幸せかと。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0266
    ChrTalk(
        0x103,
        (
            "#11P#0200Fでもロイドさん、\x01",
            "警察がここまでする\x01",
            "必要はなかったのでは？\x02\x03",

            "#0203F途中から遊撃士みたいに\x01",
            "なっていた気が……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x190)
    Sleep(300)

    #C0267
    ChrTalk(
        0x101,
        (
            "#6P#0012Fハハ、そうだな。\x01",
            "人助けになってたみたいだ。\x02\x03",

            "#0000Fでもまあ俺たちは\x01",
            "『特務支援課』だし。\x01",
            "悪くないんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_50E7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_50E7)

    def lambda_50F4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_50F4)

    def lambda_5101():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5101)

    def lambda_510E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_510E)
    Sleep(500)

    #C0268
    ChrTalk(
        0x101,
        (
            "#0000F#6Pここは邪魔をしないように\x01",
            "おいとましよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x104,
        "#0304F#11Pへっ、そうすっかね。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【仔猫の飼い主探し】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    EndChrThread(0xA, 0x2)
    SetChrPos(0x0, -200, 0, -1320, 180)
    SetChrPos(0xA, 5250, 4000, 8250, 180)
    SetChrPos(0xB, 5180, 4000, 5560, 315)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x40)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_29(0x8, 0x4, 0x10)
    OP_29(0x8, 0x1, 0x9)
    OP_C7(0x1, 0x1000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_4BA8 end

    def Function_17_524B(): pass

    label("Function_17_524B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5270")
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_17_524B")

    label("loc_5270")

    Return()

    # Function_17_524B end

    SaveToFile()

Try(main)
