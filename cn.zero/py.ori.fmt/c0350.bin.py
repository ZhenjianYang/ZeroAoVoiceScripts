from ZeroScenarioHelper import *

def main():
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
        "本德",                   # 1
        "库雷优",                 # 2
        "萨妮塔",                 # 3
        "玛丽",                   # 4
        "本德",                   # 5
        "萨妮塔",                 # 6
        "索菲亚",                 # 7
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
        "Function_8_EB3",          # 08, 8
        "Function_9_1E16",         # 09, 9
        "Function_10_2496",        # 0A, 10
        "Function_11_30B0",        # 0B, 11
        "Function_12_3281",        # 0C, 12
        "Function_13_346C",        # 0D, 13
        "Function_14_37A5",        # 0E, 14
        "Function_15_3EF3",        # 0F, 15
        "Function_16_4172",        # 10, 16
        "Function_17_4761",        # 11, 17
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_97D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_932")

    #C0001
    ChrTalk(
        0x8,
        (
            "嘁，那个可恶的专务，\x01",
            "竟然说我的态度傲慢？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "也不想想是多亏了谁，\x01",
            "公司才能度过危机的！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_978")

    label("loc_932")


    #C0003
    ChrTalk(
        0x8,
        "啊？你们有什么事吗……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "现在我正火大。\x01",
            "你们快点给我出去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_978")

    Jump("loc_EAF")

    label("loc_97D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9EB")

    #C0005
    ChrTalk(
        0x8,
        "哎呀……我是不是太厉害了？\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "哈哈，算了算了，反正那些\x01",
            "废物都一样无能，哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A72")

    label("loc_9EB")


    #C0007
    ChrTalk(
        0x8,
        (
            "哈哈，那些白痴……\x01",
            "那支股票不出三天就会跌。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "连这也看不出来吗？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔通讯社的经济杂志\x01",
            "也不行了啊，哈哈哈哈……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_A72")

    Jump("loc_EAF")

    label("loc_A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AC2")

    #C0010
    ChrTalk(
        0x8,
        (
            "钱我有的是……\x01",
            "我正在想要不要\x01",
            "去买一辆导力车。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4C")

    label("loc_AC2")


    #C0011
    ChrTalk(
        0x8,
        (
            "嗯，好像不错。\x01",
            "没白拿这本产品目录啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "这辆导力车的外形\x01",
            "真是令人神往。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "哈哈，身为证券经理，\x01",
            "确实也应该要有一辆导力车啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B4C")

    Jump("loc_EAF")

    label("loc_B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_B5F")
    Jump("loc_EAF")

    label("loc_B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_B6D")
    Jump("loc_EAF")

    label("loc_B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B7B")
    Jump("loc_EAF")

    label("loc_B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_CA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C0F")
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x8,
        (
            "妻子像那样斩钉截铁地断言后，\x01",
            "我都不懂她在想什么了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "她就不能直接告诉我\x01",
            "希望我怎么做吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9F")

    label("loc_C0F")


    #C0016
    ChrTalk(
        0x8,
        "……我老婆出身很好。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "所以，并不太了解工作的事情。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "但我还是希望她能给我一个明确的建议，\x01",
            "像是去或不去这种简单的回答就可以了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C9F")

    Jump("loc_EAF")

    label("loc_CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_DBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D02")

    #C0019
    ChrTalk(
        0x8,
        "这是一个绝佳的机会……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "不不不，还是得去\x01",
            "问问老婆的意见啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB5")

    label("loc_D02")


    #C0021
    ChrTalk(
        0x8,
        "我们公司的业绩正蒸蒸日上哦。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "下个月准备在\x01",
            "帝国东部的克鲁琴州\x01",
            "也开个分公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "…………………………\x01",
            "……怎么办啊………\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "上面在问我要不要\x01",
            "过去当分公司的经理……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_DB5")

    Jump("loc_EAF")

    label("loc_DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_DC8")
    Jump("loc_EAF")

    label("loc_DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_DD6")
    Jump("loc_EAF")

    label("loc_DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_DE4")
    Jump("loc_EAF")

    label("loc_DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_DF2")
    Jump("loc_EAF")

    label("loc_DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E49")

    #C0025
    ChrTalk(
        0x8,
        "我老婆是一个悠闲自在的人。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "真没办法啊……\x01",
            "我自己去泡杯红茶吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAF")

    label("loc_E49")


    #C0027
    ChrTalk(
        0x8,
        (
            "工作也能暂时喘口气了。\x01",
            "我想让老婆给我泡杯红茶……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "但她竟然不在。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        "应该又去浇花了吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_EAF")

    TalkEnd(0xFE)
    Return()

    # Function_7_8B8 end

    def Function_8_EB3(): pass

    label("Function_8_EB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED5")
    Call(0, 15)
    Return()

    label("loc_ED5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F69")
    Jump("loc_FB3")

    label("loc_F69")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F89")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FB3")

    label("loc_F89")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FA9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FB3")

    label("loc_FA9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FB3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_113C")
    OP_64(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B9")

    #C0030
    ChrTalk(
        0xFE,
        "……真糟糕，居然发生了这种事……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "我只在纪念庆典里休息了一天，\x01",
            "那一天就出现了损失！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "这真是糟糕了……　\x01",
            "那可是一个老主顾的股票啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "在事情暴露之前，\x01",
            "我得想办法补上那笔损失……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1125")

    label("loc_10B9")


    #C0034
    ChrTalk(
        0xFE,
        (
            "我们可是最重视信用的证券公司……\x01",
            "这事可不能暴露了……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "不管怎么样，在这星期内\x01",
            "必须补上那笔损失……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1125")

    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1E0E")

    label("loc_113C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_118D")

    #C0036
    ChrTalk(
        0xC,
        "啊，肚子好饿……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xC,
        (
            "老婆和女儿都还没回来，\x01",
            "我叫份披萨吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E0E")

    label("loc_118D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_121C")

    #C0038
    ChrTalk(
        0xC,
        "莱恩福尔特公司的股票……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xC,
        (
            "现在股票市场一片欣欣向荣，\x01",
            "正是这种时候才充满机遇。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        "我身为一个证券经理，可不能放松注意。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E0E")

    label("loc_121C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_133E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1292")

    #C0041
    ChrTalk(
        0xC,
        (
            "今年经济的起步要比\x01",
            "预想中更高。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "接下来可是证券经理的\x01",
            "关键时刻。\x01",
            "必须慎重地关注情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1339")

    label("loc_1292")


    #C0043
    ChrTalk(
        0xC,
        (
            "纪念庆典期间，\x01",
            "无论哪只股票都大涨了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xC,
        (
            "彩虹剧团也可以说是大获成功，\x01",
            "米修拉姆的主题公园也生意兴隆。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xC,
        (
            "酒店和饮食业的店铺\x01",
            "也都家家客满。\x01",
            "真是令人感兴趣。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1339")

    Jump("loc_1E0E")

    label("loc_133E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1394")

    #C0046
    ChrTalk(
        0xC,
        (
            "老婆和女儿都不在，一个人挺寂寞的，\x01",
            "但我还是会努力工作的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140F")

    label("loc_1394")


    #C0047
    ChrTalk(
        0xC,
        (
            "老婆看起来好像很无聊，\x01",
            "所以我就叫她出去外面走走。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        "她一听到就马上开心地去准备，\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xC,
        (
            "就那么想\x01",
            "去参观庆典吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_140F")

    Jump("loc_1E0E")

    label("loc_1414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_155B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_148B")

    #C0050
    ChrTalk(
        0xC,
        (
            "对证券经理来说，\x01",
            "纪念庆典期间可是关键时刻。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xC,
        (
            "……当然不能休息了，\x01",
            "每天都必须认真工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1556")

    label("loc_148B")


    #C0052
    ChrTalk(
        0xC,
        (
            "创立纪念庆典期间，\x01",
            "各支股票的价格指数都会浮动。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xC,
        (
            "因为大家都瞄准着纪念庆典\x01",
            "这个投资机会，所以造成了投资过热。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔证券市场\x01",
            "应该会反复出现\x01",
            "大幅度的震荡吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xC,
        "可不能放松警惕啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1556")

    Jump("loc_1E0E")

    label("loc_155B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_16AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15DE")

    #C0056
    ChrTalk(
        0xC,
        (
            "就算不去做帝国的分公司经理，\x01",
            "我也能接到很多大生意。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xC,
        (
            "因为放不下家人，\x01",
            "所以决定留在克洛斯贝尔工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AA")

    label("loc_15DE")


    #C0058
    ChrTalk(
        0xC,
        (
            "至于帝国分公司经理一职……\x01",
            "最后我还是拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xC,
        (
            "既然我老婆是那种态度，\x01",
            "我也只能对她妥协了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xC,
        (
            "虽然这对证券经理来说\x01",
            "是一个绝佳的机会……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xC,
        (
            "但仔细想想，\x01",
            "就算不去帝国，\x01",
            "我也能接到很多生意。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_16AA")

    Jump("loc_1E0E")

    label("loc_16AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_18D0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1846")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B2")

    #C0062
    ChrTalk(
        0xFE,
        (
            "昨天有游击士来拜访我呢，\x01",
            "问我们家能不能\x01",
            "养只小猫。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "这事太突然了，所以我吃了一惊……\x01",
            "那只好像是萨妮塔\x01",
            "偷偷喂养的小猫。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "那孩子，总是不会\x01",
            "自己提出要求……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "托游击士的福，\x01",
            "我们家又多了一个成员。\x01",
            "哈哈哈。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1841")

    label("loc_17B2")


    #C0066
    ChrTalk(
        0xFE,
        (
            "在那位游击士小姐的劝说下，\x01",
            "终于如萨妮塔所愿，\x01",
            "把那只小野猫收养在了我们家。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "哈哈，看萨妮塔那高兴的样子，\x01",
            "收养小猫果然是正确的选择啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1841")

    Jump("loc_18CB")

    label("loc_1846")


    #C0068
    ChrTalk(
        0xFE,
        (
            "萨妮塔昨天一整天\x01",
            "都跟那只小猫形影不离哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "照顾宠物比较麻烦，\x01",
            "所以还担心她会不会喊苦喊累……\x01",
            "不过，看样子似乎没必要担心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CB")

    Jump("loc_1E0E")

    label("loc_18D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1BFF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1990")

    #C0070
    ChrTalk(
        0xFE,
        (
            "萨妮塔好像已经\x01",
            "迷上了那只小猫。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "那么喜欢的话，\x01",
            "早点跟我说就好了……\x01",
            "虽然我是这么想，\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "但那孩子应该\x01",
            "也有自己的烦恼吧。\x01",
            "感觉对她挺抱歉的呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19D9")

    label("loc_1990")


    #C0073
    ChrTalk(
        0xFE,
        "不管怎么说，都得谢谢你们。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "哈哈，萨妮塔给你们\x01",
            "添了不少麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D9")

    Jump("loc_1BFA")

    label("loc_19DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_END)), "loc_1A85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A46")

    #C0075
    ChrTalk(
        0xFE,
        (
            "萨妮塔不知道\x01",
            "又跑去哪里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "真奇怪啊，\x01",
            "平时都会缠着我\x01",
            "讲故事的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A80")

    label("loc_1A46")


    #C0077
    ChrTalk(
        0xFE,
        (
            "萨妮塔最近\x01",
            "的样子有点奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "难道是\x01",
            "叛逆期吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A80")

    Jump("loc_1BFA")

    label("loc_1A85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_1AE3")

    #C0079
    ChrTalk(
        0xFE,
        (
            "我们家没有\x01",
            "养宠物……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "帮不上各位的忙，\x01",
            "真不好意思哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xC, 0x1)
    Return()

    label("loc_1AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B75")

    #C0081
    ChrTalk(
        0xFE,
        (
            "工作闲暇之余\x01",
            "我都会给女儿读故事听。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "……对了，\x01",
            "你们没有毁坏\x01",
            "我的文件吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "……没事，别介意。\x01",
            "我自言自语而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BEE")

    label("loc_1B75")


    #C0084
    ChrTalk(
        0xFE,
        (
            "我放在桌子上的文件，\x01",
            "时不时就会被毁坏……\x01",
            "害我都没办法顺利工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "萨妮塔绝对不会做那种事，\x01",
            "那到底是谁做的呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BEE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xC, 0x1)
    Return()

    label("loc_1BFA")

    Jump("loc_1E0E")

    label("loc_1BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1CBB")
    SetChrSubChip(0xC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C83")

    #C0086
    ChrTalk(
        0xFE,
        "我想想看啊，那份证券的文件是……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "……对了。\x01",
            "是上星期被毁坏的。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "嗯，到底是谁做的呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CB6")

    label("loc_1C83")


    #C0089
    ChrTalk(
        0xFE,
        (
            "如果文件像这样不断被毁坏，\x01",
            "会没法工作的啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB6")

    Jump("loc_1E0E")

    label("loc_1CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1E0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D3C")

    #C0090
    ChrTalk(
        0xC,
        (
            "近几年，新的\x01",
            "金融商品不断涌现，\x01",
            "想做这行必须具备丰富的专业知识。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        "嗯，所以我可不推荐外行人来做。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E0E")

    label("loc_1D3C")


    #C0092
    ChrTalk(
        0xC,
        (
            "你们知道吗？\x01",
            "克洛斯贝尔从很早以前开始，\x01",
            "证券和期货交易就很火爆。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xC,
        (
            "我们公司做的是证券交易，\x01",
            "也就是所谓的证券交易公司了。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xC,
        (
            "特别是近几年开发出来\x01",
            "好多新的金融商品，\x01",
            "想做这行必须得有过硬的专业知识。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E0E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_EB3 end

    def Function_9_1E16(): pass

    label("Function_9_1E16")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E70")

    #C0095
    ChrTalk(
        0x9,
        "怎么会这样……为什么偏偏是我老公……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        "他是那么耿直……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F09")

    label("loc_1E70")


    #C0097
    ChrTalk(
        0x9,
        "我老公还没有回来。\x02",
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
            "他不会是\x01",
            "失踪了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "怎么会这样……为什么偏偏是我老公……\x01",
            "呜呜，好让人担心啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1F09")

    Jump("loc_2492")

    label("loc_1F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F8E")

    #C0101
    ChrTalk(
        0x9,
        (
            "那个，那个……\x01",
            "我老公不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        "能找得到我老公吗……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#0003F您放心，我们警察\x01",
            "也一定会尽全力搜索的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2492")

    label("loc_1F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2082")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1FF1")

    #C0104
    ChrTalk(
        0x9,
        (
            "明天烹饪教室\x01",
            "会在索菲亚家开课。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "呵呵，我打算\x01",
            "去那里跟她们聊个够。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207D")

    label("loc_1FF1")


    #C0106
    ChrTalk(
        0x9,
        (
            "我女儿萨妮塔\x01",
            "和索菲亚她儿子柯林\x01",
            "是同岁哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        "呵呵，我们应该能聊得很开心哦。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "明天是烹饪教室开课的日子，\x01",
            "又能和大家聊个够了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_207D")

    Jump("loc_2492")

    label("loc_2082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_20CC")

    #C0109
    ChrTalk(
        0x9,
        "我老公不知道为什么一直闷闷不乐，\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        "发生什么事了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2492")

    label("loc_20CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_211C")

    #C0111
    ChrTalk(
        0xFE,
        (
            "萨妮塔正在\x01",
            "和小猫咪玩耍哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "真是羡慕啊，\x01",
            "我也想一起玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2492")

    label("loc_211C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_222D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2181")

    #C0113
    ChrTalk(
        0x9,
        (
            "工作上的事情\x01",
            "我都不太懂。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "我觉得老公只要按他自己\x01",
            "所想的去做就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2228")

    label("loc_2181")


    #C0115
    ChrTalk(
        0x9,
        (
            "我老公说他有可能要\x01",
            "一个人去帝国工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "……我当然还是跟他说，\x01",
            "『按你自己喜欢的去做』。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "因为那是他的工作啊，\x01",
            "所以我觉得只要按他自己\x01",
            "所想的去做就行了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2228")

    Jump("loc_2492")

    label("loc_222D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2376")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22EE")

    #C0118
    ChrTalk(
        0xFE,
        (
            "萨妮塔突然养了\x01",
            "一只很可爱的小猫咪。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "我老公\x01",
            "好像已经知道了……\x01",
            "我真是吃了一惊呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    #C0120
    ChrTalk(
        0xFE,
        (
            "萨妮塔跟小猫咪\x01",
            "好像相处得很不错……\x01",
            "真是羡慕啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2371")

    label("loc_22EE")


    #C0121
    ChrTalk(
        0xFE,
        (
            "啊……糟糕了，\x01",
            "我今天和索菲亚夫人约好了\x01",
            "要去她的烹饪教室上课的。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "呵呵，先不管小猫咪的事了，\x01",
            "我必须快点去，不然就迟到了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2371")

    Jump("loc_2492")

    label("loc_2376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2384")
    Jump("loc_2492")

    label("loc_2384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23F4")

    #C0123
    ChrTalk(
        0x9,
        (
            "我老公在家的时候也总是工作。\x01",
            "呵呵，真是奇怪的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "还是说，这世上所有\x01",
            "男人都是那样的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2492")

    label("loc_23F4")


    #C0125
    ChrTalk(
        0xFE,
        "我老公在家的时候也总是工作。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "一秒也不休息，\x01",
            "就算再怎么喜欢工作，至少也要\x01",
            "给女儿讲讲故事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "……他也太喜欢工作了吧。\x01",
            "呵呵，真是奇怪的人啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2492")

    TalkEnd(0xFE)
    Return()

    # Function_9_1E16 end

    def Function_10_2496(): pass

    label("Function_10_2496")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_24CA")

    #C0128
    ChrTalk(
        0xA,
        (
            "呜呜……\x01",
            "………爸爸～………！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30AC")

    label("loc_24CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2641")
    OP_63(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0129
    ChrTalk(
        0xA,
        (
            "爸爸……爸爸\x01",
            "不见了！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "呜呜……\x01",
            "呜哇哇哇～！！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2639")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25E6")

    #C0131
    ChrTalk(
        0x103,
        (
            "#0200F我们以前曾经拜访过这里，\x01",
            "就是收养小猫的那一家吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        (
            "#0108F那位先生看起来是个\x01",
            "很温柔的人啊，怎么会……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#0001F嗯……我们最好抓紧时间，\x01",
            "尽快调查清楚……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2639")

    label("loc_25E6")


    #C0134
    ChrTalk(
        0x103,
        "#0200F孩子也在家呢……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#0001F是啊……我们最好抓紧时间，\x01",
            "尽快调查清楚……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2639")

    SetScenarioFlags(0x0, 2)
    Jump("loc_30AC")

    label("loc_2641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_26A6")
    OP_4B(0xB, 0xFF)

    #C0136
    ChrTalk(
        0xA,
        (
            "玛丽……爸爸他\x01",
            "到底怎么了……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        "玛丽知道点什么吗……？\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        "喵呜……？\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_30AC")

    label("loc_26A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_291D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_END)), "loc_27A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_272D")

    #C0139
    ChrTalk(
        0xA,
        (
            "妈妈今天\x01",
            "去烹饪教室上课了……\x01",
            "她一向都很悠闲的……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "所以萨妮塔必须得\x01",
            "坚强起来，学着独立……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279F")

    label("loc_272D")


    #C0141
    ChrTalk(
        0xA,
        (
            "爸、爸爸他一定\x01",
            "是累了。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xA,
        (
            "一定是因为那样，\x01",
            "所以爸爸才会有点奇怪……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "……萨妮塔必须\x01",
            "做点什么……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_279F")

    Jump("loc_2918")

    label("loc_27A4")

    OP_64(0xA)

    #C0144
    ChrTalk(
        0xA,
        "………爸爸………………\x02",
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
        "#0005F怎么了？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0xA, 0x0, 750)
    Sleep(750)

    #C0146
    ChrTalk(
        0xA,
        "没、没什么。\x02",
    )

    CloseMessageWindow()
    OP_64(0xA)

    #C0147
    ChrTalk(
        0xA,
        (
            "只是，那个……\x01",
            "从不久前开始，爸爸他就……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        "哈哈哈，那些白痴……！\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x13B, 0x2EE)

    #C0149
    ChrTalk(
        0xA,
        (
            "爸爸他……\x01",
            "到底怎么了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#0005F（？？？\x01",
            "  情况好像有点\x01",
            "  奇怪啊……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0xCD, 0)

    label("loc_2918")

    Jump("loc_30AC")

    label("loc_291D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2988")
    OP_93(0xFE, 0x13B, 0x0)

    #C0151
    ChrTalk(
        0xFE,
        (
            "爸爸他……\x01",
            "到底怎么了呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    #C0152
    ChrTalk(
        0xFE,
        "没、没什么。\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x13B, 0x0)
    Jump("loc_30AC")

    label("loc_2988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_29E6")

    #C0153
    ChrTalk(
        0xFE,
        (
            "爸爸他明明说过今天要\x01",
            "陪我玩的……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "是因为工作太忙了吗……\x01",
            "真是失望……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30AC")

    label("loc_29E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2A42")

    #C0155
    ChrTalk(
        0xA,
        (
            "这样可不行哦，玛丽，\x01",
            "今天是洗澡日啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xA,
        (
            "要好好洗澡，\x01",
            "洗得干干净净哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30AC")

    label("loc_2A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2B4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2AE0")
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0xA, 0x0, 750)
    Sleep(750)

    #C0157
    ChrTalk(
        0xA,
        "啊……\x02",
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
            "咳咳，玛丽，听好了哦。\x01",
            "在客人面前，\x01",
            "一定要有礼貌哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B46")

    label("loc_2AE0")


    #C0159
    ChrTalk(
        0xA,
        (
            "玛丽，\x01",
            "我给你拿牛奶来了哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xA,
        (
            "听说这是阿尔摩利卡产的\x01",
            "高品质牛奶。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        (
            "一定\x01",
            "很好喝的哦～¤\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2B46")

    Jump("loc_30AC")

    label("loc_2B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2B97")

    #C0162
    ChrTalk(
        0xA,
        (
            "爸爸和妈妈\x01",
            "刚才在说什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "是我不能\x01",
            "听的话吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30AC")

    label("loc_2B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2C8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2BE6")

    #C0164
    ChrTalk(
        0xA,
        (
            "玛丽很喜欢\x01",
            "撒娇哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        (
            "我必须得\x01",
            "给它顺顺毛才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C87")

    label("loc_2BE6")

    OP_4B(0xB, 0xFF)
    Sound(823, 0, 100, 0)

    #C0166
    ChrTalk(
        0xA,
        (
            "呀，玛丽你真是的……\x01",
            "人家会痒啦……！\x02",
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
            "玛、玛丽很喜欢\x01",
            "撒娇哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "不经常给它顺毛的话，\x01",
            "它会寂寞的。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_2C87")

    Jump("loc_30AC")

    label("loc_2C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2DF7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D42")
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0169
    ChrTalk(
        0xA,
        (
            "玛丽～玛丽！\x01",
            "我们来玩吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 750)
    Sleep(750)

    #C0170
    ChrTalk(
        0xA,
        "啊……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xA,
        (
            "咳、咳咳……\x01",
            "玛丽今天也很精神哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x2EE)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D7B")

    label("loc_2D42")


    #C0172
    ChrTalk(
        0xA,
        "咳、咳咳……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "托你们的福，\x01",
            "玛丽今天也很精神哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7B")

    Jump("loc_2DF2")

    label("loc_2D80")


    #C0174
    ChrTalk(
        0xA,
        "玛丽回来了！\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        (
            "是游击士的大姐姐\x01",
            "把它送回来的。\x02",
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
            "玛丽，玛丽！\x01",
            "我们来玩吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF2")

    Jump("loc_30AC")

    label("loc_2DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2ECF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2E4A")

    #C0177
    ChrTalk(
        0xA,
        (
            "玛丽由\x01",
            "萨妮塔来照顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "咳咳，这可不是\x01",
            "在玩游戏哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECA")

    label("loc_2E4A")


    #C0179
    ChrTalk(
        0xA,
        (
            "玛丽，玛丽！\x01",
            "看这边～¤\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 500)
    Sleep(500)

    #C0180
    ChrTalk(
        0xA,
        "咳、咳咳……\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xA,
        (
            "今天\x01",
            "谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        "就、就这样而已！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_2ECA")

    Jump("loc_30AC")

    label("loc_2ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2F3F")

    #C0183
    ChrTalk(
        0xA,
        (
            "爸爸好像因为重要的文件被毁，\x01",
            "所以很苦恼……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xA,
        (
            "…………………………\x01",
            "我、我什么都不知道哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30AC")

    label("loc_2F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2F84")

    #C0185
    ChrTalk(
        0xA,
        (
            "爸爸今天也没有\x01",
            "陪我玩。\x01",
            "我不能去打扰他！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF2")

    label("loc_2F84")


    #C0186
    ChrTalk(
        0xA,
        (
            "爸爸正在做\x01",
            "很难的工作哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        (
            "他是证券经理哦，\x01",
            "很厉害的。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        (
            "你们要是吵到他的话，\x01",
            "我可不原谅你们！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2FF2")

    Jump("loc_30AC")

    label("loc_2FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3053")

    #C0189
    ChrTalk(
        0xA,
        "哎呀，有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xA,
        (
            "竟然向陌生的淑女搭讪，\x01",
            "真是不知礼仪呢。\x01",
            "……哼！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30AC")

    label("loc_3053")


    #C0191
    ChrTalk(
        0xA,
        "睡衣要叠好放在抽屉里……\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xA,
        (
            "妈妈比较靠不住，\x01",
            "所以萨妮塔自己必须成熟一点。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_30AC")

    TalkEnd(0xFE)
    Return()

    # Function_10_2496 end

    def Function_11_30B0(): pass

    label("Function_11_30B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30D2")
    Call(0, 15)
    Return()

    label("loc_30D2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3166")
    Jump("loc_31B0")

    label("loc_3166")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3186")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31B0")

    label("loc_3186")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31A6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31B0")

    label("loc_31A6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31B0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_323A")

    #C0193
    ChrTalk(
        0xD,
        (
            "萨、萨妮塔\x01",
            "什么都不知道。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xD,
        (
            "哼，爸爸正在\x01",
            "给我讲故事呢。\x01",
            "请不要打扰我们哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3275")

    label("loc_323A")


    #C0195
    ChrTalk(
        0xD,
        (
            "哎呀，爸爸正在\x01",
            "给我讲故事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xD,
        "请不要打扰我们哦！\x02",
    )

    CloseMessageWindow()

    label("loc_3275")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xD, 0x2)
    Return()

    # Function_11_30B0 end

    def Function_12_3281(): pass

    label("Function_12_3281")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_32A0")

    #C0197
    ChrTalk(
        0xB,
        "喵呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_32A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_32C0")

    #C0198
    ChrTalk(
        0xB,
        "喵呜喵呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_32C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_32DE")

    #C0199
    ChrTalk(
        0xB,
        "喵呜……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_32DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_32FA")

    #C0200
    ChrTalk(
        0xB,
        "喵呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_32FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3314")

    #C0201
    ChrTalk(
        0xB,
        "喵……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_3314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3332")

    #C0202
    ChrTalk(
        0xB,
        "喵呜……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_3332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_334E")

    #C0203
    ChrTalk(
        0xB,
        "喵呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_334E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_336C")

    #C0204
    ChrTalk(
        0xB,
        "喵呜……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_336C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3386")

    #C0205
    ChrTalk(
        0xB,
        "喵……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_3386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_33A2")

    #C0206
    ChrTalk(
        0xB,
        "喵呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_33A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_33DA")
    OP_63(0xB, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0207
    ChrTalk(
        0xB,
        "喵喵呜……！\x02",
    )

    CloseMessageWindow()
    OP_64(0xB)
    Jump("loc_3468")

    label("loc_33DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_33FC")

    #C0208
    ChrTalk(
        0xB,
        "喵呜喵呜……¤\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_33FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3418")

    #C0209
    ChrTalk(
        0xB,
        "喵呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_3418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_343A")

    #C0210
    ChrTalk(
        0xB,
        "喵呜喵呜……¤\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_343A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3458")

    #C0211
    ChrTalk(
        0xB,
        "喵呜……¤\x02",
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_3458")


    #C0212
    ChrTalk(
        0xB,
        "喵呜……¤\x02",
    )

    CloseMessageWindow()

    label("loc_3468")

    TalkEnd(0xFE)
    Return()

    # Function_12_3281 end

    def Function_13_346C(): pass

    label("Function_13_346C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_35CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_34D3")

    #C0213
    ChrTalk(
        0xE,
        (
            "#3701F她丈夫\x01",
            "到底去哪里了呢……\x02\x03",

            "他看起来不像\x01",
            "是会把家人丢下\x01",
            "的人啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C6")

    label("loc_34D3")


    #C0214
    ChrTalk(
        0xE,
        (
            "#3701F支援科的各位……\x02\x03",

            "库雷优和萨妮塔\x01",
            "都冷静下来了，\x01",
            "不过她们还是很不安。\x02\x03",

            "#3708F这也难怪……\x01",
            "柯林不见了的时候，\x01",
            "我也一样心乱如麻……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，\x01",
            "能不能请您再陪陪她们呢？\x02\x03",

            "警察正在\x01",
            "全力进行搜索……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xE,
        "#3700F嗯，当然可以。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_35C6")

    Jump("loc_37A1")

    label("loc_35CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_37A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_361F")
    OP_4B(0x9, 0xFF)

    #C0217
    ChrTalk(
        0xE,
        (
            "#3700F库雷优，\x01",
            "你要冷静啊。\x02\x03",

            "你丈夫一定没事的。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_37A1")

    label("loc_361F")


    #C0218
    ChrTalk(
        0xE,
        (
            "#3708F我经常与库雷优夫人来往，\x01",
            "所以见过她丈夫几次。\x02\x03",

            "……他不会是……被卷入\x01",
            "什么事件里了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#0103F索菲亚夫人，\x01",
            "表情请尽量不要太凝重。\x02\x03",

            "#0100F他的家人看到的话，\x01",
            "可能会更加担心的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0220
    ChrTalk(
        0xE,
        (
            "#3705F也、也是。\x01",
            "不好意思，我不禁就……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x104,
        (
            "#0304F这种时候\x01",
            "最好不要想太多。\x02\x03",

            "#0300F给她们泡杯茶\x01",
            "应该会好点吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xE,
        (
            "#3700F嗯，说得也是，\x01",
            "我去泡点茶吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x9, 750)
    SetChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 3)

    label("loc_37A1")

    TalkEnd(0xFE)
    Return()

    # Function_13_346C end

    def Function_14_37A5(): pass

    label("Function_14_37A5")

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

    def lambda_385C():
        OP_97(0xFE, 0x0, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_385C)

    def lambda_3876():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3876)
    Sleep(50)

    def lambda_388A():
        OP_97(0xFE, 0x0, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_388A)

    def lambda_38A4():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_38A4)
    Sleep(50)

    def lambda_38B8():
        OP_97(0xFE, 0x0, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_38B8)

    def lambda_38D2():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_38D2)
    Sleep(50)

    def lambda_38E6():
        OP_97(0xFE, 0x0, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_38E6)

    def lambda_3900():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3900)
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
            "#0001F#11P根据一科的资料，\x01",
            "应该就是这家没错……\x02",
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
        "#0205F那是……\x02",
    )

    CloseMessageWindow()
    OP_68(-1750, 1400, 3120, 3000)
    OP_6F(0x79)

    #C0225
    ChrTalk(
        0x9,
        "那个、那个……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x9,
        "我到底该怎么办啊……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xE,
        (
            "#3701F库雷优，\x01",
            "你一定要冷静啊。\x02\x03",

            "既然情况如此，\x01",
            "现在也只能找人来帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1750, 1400, 2120, 3000)

    def lambda_3A69():
        OP_95(0x101, -750, 0, 1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A69)
    Sleep(50)

    def lambda_3A86():
        OP_95(0x102, -1750, 0, 1250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A86)
    Sleep(50)

    def lambda_3AA3():
        OP_95(0x103, -750, 0, 250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AA3)
    Sleep(50)

    def lambda_3AC0():
        OP_95(0x104, -1750, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AC0)
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
            "#0005F您是\x01",
            "哈罗德先生的夫人……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_3B51():
        TurnDirection(0xE, 0x101, 350)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3B51)
    Sleep(50)

    def lambda_3B61():
        TurnDirection(0x9, 0x101, 350)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3B61)
    Sleep(1000)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x9, 1)

    #C0229
    ChrTalk(
        0xE,
        (
            "#3705F啊……是支援科的各位啊！\x02\x03",

            "#3700F太好了……\x01",
            "其实发生了一件很麻烦的事情，\x01",
            "正想找人帮忙呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        (
            "#0101F……莫非……\x01",
            "是与这座宅邸的男主人，\x01",
            "那位证券经理有关？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x9,
        "#5P正是……\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x9,
        (
            "#5P今天早上醒来，\x01",
            "我老公就不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x9,
        (
            "#5P我和索菲亚夫人两个人\x01",
            "把附近都找遍了，也没找到……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#0003F这、这样啊……\x02\x03",

            "#0013F那个，您丈夫\x01",
            "最近是不是有点奇怪……？\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x9,
        (
            "#5P啊……好像是的，\x01",
            "我女儿一直很担心他。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x104,
        (
            "#0303F……不出所料啊。\x02\x03",

            "#0301F他是在晚上失踪的……\x01",
            "也就是说，很难找到目击者啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DA6")

    #C0237
    ChrTalk(
        0x101,
        (
            "#0008F嗯，总之，现在要去\x01",
            "确认一下所有失踪者的情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC8")

    label("loc_3DA6")


    #C0238
    ChrTalk(
        0x101,
        "#0008F是啊，必须想点办法……\x02",
    )

    CloseMessageWindow()

    label("loc_3DC8")

    TurnDirection(0x101, 0xE, 500)
    Sleep(300)

    #C0239
    ChrTalk(
        0x101,
        (
            "#0000F索菲亚夫人，\x01",
            "您好像和这一家的\x01",
            "人认识吧？\x02\x03",

            "#0003F那个……\x01",
            "警察现在正在进行搜索，\x01",
            "但可能会花点时间。\x02\x03",

            "#0001F能不能请您\x01",
            "暂时陪陪她们呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xE,
        (
            "#3700F嗯，当然可以。\x02\x03",

            "我先生应该\x01",
            "也快回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        (
            "#0004F不好意思，\x01",
            "那这里就拜托您了。\x02",
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

    # Function_14_37A5 end

    def Function_15_3EF3(): pass

    label("Function_15_3EF3")

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
            "#5P#0000F（这家好像\x01",
            "  有小孩子啊……）\x02\x03",

            "那个，能……打扰一下吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)
    Sleep(300)

    #C0243
    ChrTalk(
        0xC,
        "#11P啊，请问有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#5P#0000F哈哈，其实我们是警察，\x01",
            "现在正在打听一点事情……\x02\x03",

            "请问府上\x01",
            "有没有\x01",
            "养猫呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xC,
        "#11P啊，应该没有……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xC,
        "#11P萨妮塔，你知道些什么吗？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x2)

    #C0247
    ChrTalk(
        0xD,
        "#6P我、我可什么都不知道。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)
    Sleep(300)

    #C0248
    ChrTalk(
        0xD,
        (
            "#12P哼，爸爸正在\x01",
            "给我讲故事呢。\x01",
            "请不要打扰我们哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x104,
        "#0306F唔，还是没线索啊……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x103,
        (
            "#0200F再在这附近\x01",
            "稍微找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        (
            "#0100F是啊，说不定\x01",
            "有什么遗漏的地方。\x01",
            "再回头重新找一找吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 5580, 4000, 8480, 180)
    SetChrSubChip(0xD, 0x2)
    OP_29(0x8, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_15_3EF3 end

    def Function_16_4172(): pass

    label("Function_16_4172")

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
        "#5P想在家里养小猫……？\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "#5P什么嘛……\x01",
            "原来是这么一回事啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0254
    ChrTalk(
        0xA,
        "#12P哎……？\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        (
            "#5P最近萨妮塔的样子有点奇怪，\x01",
            "让我很担心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x8,
        (
            "#5P经常会一个人\x01",
            "不知跑去哪里。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        (
            "#5P虽然文件都被毁坏了……\x01",
            "但是算了，也不是什么重要的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xA,
        (
            "#12P爸爸，\x01",
            "你不生玛丽的气吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xA,
        (
            "#12P玛丽可以放在\x01",
            "我们家养吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "#5P嗯，当然可以。\x01",
            "家里添了新成员，我也很欢迎啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "#5P不过……萨妮塔要\x01",
            "好好照顾玛丽哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xA,
        (
            "#12P当、当然啦。\x01",
            "爸爸，谢谢您……！\x02",
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
        "#11P#0300F事情好像解决了啊。\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        (
            "#11P#0100F有个通情达理的爸爸，\x01",
            "真好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#11P#0200F是啊……\x01",
            "我想，那只小猫也很幸福。\x02",
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
            "#11P#0200F不过，罗伊德前辈，\x01",
            "警察连这些事\x01",
            "也要亲力亲为吗？\x02\x03",

            "#0203F总觉得我们好像\x01",
            "在途中就变成了游击士一样……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x190)
    Sleep(300)

    #C0267
    ChrTalk(
        0x101,
        (
            "#6P#0012F哈哈，对哦。\x01",
            "好像是变得在助人为乐了呢。\x02\x03",

            "#0000F不过我们是\x01",
            "『特别任务支援科』哦，\x01",
            "偶尔做做助人为乐的事也不错啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4621():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4621)

    def lambda_462E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_462E)

    def lambda_463B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_463B)

    def lambda_4648():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4648)
    Sleep(500)

    #C0268
    ChrTalk(
        0x101,
        (
            "#0000F#6P我们先走吧，\x01",
            "别打扰人家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x104,
        "#0304F#11P嘿，也对。\x02",
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
            "任务【寻找小猫的饲主】\x07\x00",
            "完成！\x02",
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

    # Function_16_4172 end

    def Function_17_4761(): pass

    label("Function_17_4761")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4786")
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_17_4761")

    label("loc_4786")

    Return()

    # Function_17_4761 end

    SaveToFile()

Try(main)
