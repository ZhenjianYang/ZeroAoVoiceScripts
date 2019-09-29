from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1520.bin",                # FileName
        "t1520",                    # MapName
        "t1520",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 6, 0, 7],
    )

    BuildStringList((
        "t1520",                  # 0
        "阿修拉主任",             # 1
        "玛罗奈",                 # 2
        "实习医生夏鲁鲁",         # 3
        "实习医生利顿",           # 4
        "实习医生古恩",           # 5
        "梅菲尔护士",             # 6
        "诊断医生贝尔达因",       # 7
        "阿修拉主任",             # 8
        "塞茜尔",                 # 9
    ))

    AddCharChip((
        "apl/ch50146.itc",                   # 00
        "chr/ch25600.itc",                   # 01
        "chr/ch32800.itc",                   # 02
        "chr/ch29400.itc",                   # 03
        "chr/ch29500.itc",                   # 04
        "chr/ch29800.itc",                   # 05
        "chr/ch29300.itc",                   # 06
        "chr/ch05300.itc",                   # 07
        "chr/ch32900.itc",                   # 08
    ))

    DeclNpc(92529,   400,     49430,   315,  469,  0x0, 0,   0,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-5199,   0,       17700,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-47439,  0,       55720,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3630,    0,       54689,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(202830,  0,       340,     0,    389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(204669,  0,       53000,   90,   389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-98839,  0,       53500,   180,  389,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(94459,   0,       52029,   90,   389,  0x0, 0,   8,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)

    DeclActor(155770,  0,       53330,   1500,    155770,  1500,    53330,   0x007C, 0,  19, 0x0000)

    ScpFunction((
        "Function_0_228",          # 00, 0
        "Function_1_2E0",          # 01, 1
        "Function_2_341",          # 02, 2
        "Function_3_3A2",          # 03, 3
        "Function_4_3CD",          # 04, 4
        "Function_5_3F8",          # 05, 5
        "Function_6_40B",          # 06, 6
        "Function_7_6AC",          # 07, 7
        "Function_8_7F5",          # 08, 8
        "Function_9_CF3",          # 09, 9
        "Function_10_169F",        # 0A, 10
        "Function_11_1878",        # 0B, 11
        "Function_12_1AD8",        # 0C, 12
        "Function_13_1EE6",        # 0D, 13
        "Function_14_1FD8",        # 0E, 14
        "Function_15_21AC",        # 0F, 15
        "Function_16_2283",        # 10, 16
        "Function_17_2BF6",        # 11, 17
        "Function_18_2E7D",        # 12, 18
        "Function_19_3242",        # 13, 19
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

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_340")
    OP_95(0xFE, -310, 0, 17700, 2000, 0x0)
    OP_95(0xFE, -310, 0, 3650, 2000, 0x0)
    OP_95(0xFE, -310, 0, 17700, 2000, 0x0)
    OP_95(0xFE, -14660, 0, 17700, 2000, 0x0)
    Jump("Function_1_2E0")

    label("loc_340")

    Return()

    # Function_1_2E0 end

    def Function_2_341(): pass

    label("Function_2_341")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A1")
    OP_95(0xFE, 79630, 0, 11390, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 11390, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 2680, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 11390, 2000, 0x0)
    Jump("Function_2_341")

    label("loc_3A1")

    Return()

    # Function_2_341 end

    def Function_3_3A2(): pass

    label("Function_3_3A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CC")
    OP_94(0xFE, 0x3124A, 0x1CC, 0x31BC8, 0xE1A, 0x3E8)
    Sleep(400)
    Jump("Function_3_3A2")

    label("loc_3CC")

    Return()

    # Function_3_3A2 end

    def Function_4_3CD(): pass

    label("Function_4_3CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F7")
    OP_94(0xFE, 0xFFFE741A, 0xCD5A, 0xFFFE86D0, 0xD548, 0x3E8)
    Sleep(400)
    Jump("Function_4_3CD")

    label("loc_3F7")

    Return()

    # Function_4_3CD end

    def Function_5_3F8(): pass

    label("Function_5_3F8")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Return()

    # Function_5_3F8 end

    def Function_6_40B(): pass

    label("Function_6_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_44B")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 203030, 0, 4610, 0)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 154520, 0, 53680, 90)
    Jump("loc_6AB")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_475")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_49F")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 203030, 0, 4610, 0)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4CF")
    ClearChrFlags(0xE, 0x80)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_4E8")
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_6AB")

    label("loc_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_507")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 5)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_54D")
    ClearChrFlags(0xE, 0x80)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 154520, 0, 53680, 90)
    Jump("loc_6AB")

    label("loc_54D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_566")
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5A0")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5BF")
    ClearChrFlags(0xC, 0x80)
    BeginChrThread(0xC, 0, 0, 3)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_5BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5E3")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    BeginChrThread(0xC, 0, 0, 3)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_61E")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 154520, 0, 53680, 90)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_648")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_672")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_691")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 5)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6AB")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0x8, 0, 0, 5)

    label("loc_6AB")

    Return()

    # Function_6_40B end

    def Function_7_6AC(): pass

    label("Function_7_6AC")

    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6D8")
    OP_65(0x0, 0x1)
    Jump("loc_79A")

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6E6")
    Jump("loc_79A")

    label("loc_6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_701")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    Jump("loc_79A")

    label("loc_701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_71C")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    Jump("loc_79A")

    label("loc_71C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_72E")
    OP_65(0x0, 0x1)
    Jump("loc_79A")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_740")
    OP_65(0x0, 0x1)
    Jump("loc_79A")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_74E")
    Jump("loc_79A")

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_769")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    Jump("loc_79A")

    label("loc_769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_784")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    Jump("loc_79A")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_79A")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)

    label("loc_79A")

    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C1")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7F4")

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DD")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7F4")

    label("loc_7DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F4")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_7F4")

    Return()

    # Function_7_6AC end

    def Function_8_7F5(): pass

    label("Function_8_7F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_806")
    Jump("loc_CEF")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_814")
    Jump("loc_CEF")

    label("loc_814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_822")
    Jump("loc_CEF")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_830")
    Jump("loc_CEF")

    label("loc_830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_8EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A9")

    #C0001
    ChrTalk(
        0xFE,
        (
            "呼……呼……\x01",
            "早上好……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0002
    ChrTalk(
        0xFE,
        (
            "啊，不行！\x01",
            "今天必须要去\x01",
            "诊察室！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8E6")

    label("loc_8A9")


    #C0003
    ChrTalk(
        0xFE,
        (
            "夏鲁鲁早就去\x01",
            "诊察室了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "哇哇……该怎么办啊！？\x02",
    )

    CloseMessageWindow()

    label("loc_8E6")

    Jump("loc_CEF")

    label("loc_8EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_996")
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_947")

    #C0005
    ChrTalk(
        0xFE,
        "……呼……呼…………\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "……再、再睡五分钟……呼呼……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_97F")

    label("loc_947")


    #C0007
    ChrTalk(
        0xFE,
        (
            "再睡五分钟……\x01",
            "不，再睡十五分钟就起床……\x01",
            "呼呼……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97F")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_CEF")

    label("loc_996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9A4")
    Jump("loc_CEF")

    label("loc_9A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A35")
    OP_64(0xFE)

    #C0008
    ChrTalk(
        0xFE,
        "……呼……呼……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "哇……这就是最新式的\x01",
            "导力镭射手术刀…………\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "竟然开发了这样的东西……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_CEF")

    label("loc_A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A43")
    Jump("loc_CEF")

    label("loc_A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A51")
    Jump("loc_CEF")

    label("loc_A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A5F")
    Jump("loc_CEF")

    label("loc_A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A6D")
    Jump("loc_CEF")

    label("loc_A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_A7B")
    Jump("loc_CEF")

    label("loc_A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1D")

    #C0011
    ChrTalk(
        0xFE,
        "……呼呼……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0012
    ChrTalk(
        0xFE,
        "……啊呀，都已经这么晚了！？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "不·好·了～啊！\x01",
            "明明要在傍晚赶到\x01",
            "诊察室去的～！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B70")

    label("loc_B1D")


    #C0014
    ChrTalk(
        0xFE,
        (
            "因为通宵太累导致\x01",
            "睡得太熟了……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "不快点过去的话，\x01",
            "又要被盖里教授\x01",
            "训斥了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B70")

    Jump("loc_CEF")

    label("loc_B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_END)), "loc_BBB")

    #C0016
    ChrTalk(
        0xFE,
        "呼……呼……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#0000F……还是别吵醒她比较好吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEF")

    label("loc_BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_CBF")
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8E")

    #C0018
    ChrTalk(
        0xFE,
        "呼……呼……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "……哇呀！？\x01",
            "……爆炸了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "…………呼…………呼……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#0006F……到、到底在做什么梦呢……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x136,
        (
            "#1302F阿修拉主任\x01",
            "是个很忙的人……\x01",
            "现在就让她休息吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CA8")

    label("loc_C8E")


    #C0023
    ChrTalk(
        0xFE,
        "……呼…………呼……\x02",
    )

    CloseMessageWindow()

    label("loc_CA8")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_CEF")

    label("loc_CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_CEF")
    OP_64(0xFE)

    #C0024
    ChrTalk(
        0xFE,
        "呼……呼……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)

    label("loc_CEF")

    TalkEnd(0xFE)
    Return()

    # Function_8_7F5 end

    def Function_9_CF3(): pass

    label("Function_9_CF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA1")

    #C0025
    ChrTalk(
        0xFE,
        (
            "啊，你是昨天被送到\x01",
            "塞茜尔小姐房间里的……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        "#0203F……让您担心了。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "呼，当时确实很担心呢。\x01",
            "不过，你现在看起来倒是挺精神的，这就好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_DF4")

    label("loc_DA1")


    #C0028
    ChrTalk(
        0xFE,
        (
            "要是以后又觉得身体不舒服的话，\x01",
            "请马上再过来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "毕竟这里是专业的医院呢。\x02",
    )

    CloseMessageWindow()

    label("loc_DF4")

    Jump("loc_169B")

    label("loc_DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_E52")

    #C0030
    ChrTalk(
        0xFE,
        "哎呀，已经这么晚了！？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "啊哇哇，必须快点完成\x01",
            "今天的打扫工作啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169B")

    label("loc_E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_EC0")

    #C0032
    ChrTalk(
        0xFE,
        (
            "约亚西姆副教授也住在\x01",
            "这边的宿舍哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "他早上出门时永远都是那么邋遢，\x01",
            "所以我总是提醒他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169B")

    label("loc_EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F44")

    #C0034
    ChrTalk(
        0xFE,
        (
            "今天阿修拉主任竟然准时\x01",
            "去研究楼了，真是很少见。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "嗯，平时都是早上才回来睡一会的……\x01",
            "不知道她昨天休息了没有。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169B")

    label("loc_F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_F8D")

    #C0036
    ChrTalk(
        0xFE,
        (
            "小女孩？\x01",
            "我想没有来过这边哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "找过病房楼了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_169B")

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_109C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1036")

    #C0038
    ChrTalk(
        0xFE,
        (
            "这个时间，希伦护士\x01",
            "一般都会在楼顶\x01",
            "晒床单。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "前几天还在那边的露台上\x01",
            "悠闲地仰望天空……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "……我全都看到了呢。\x01",
            "得让她多注意一点……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1097")

    label("loc_1036")


    #C0041
    ChrTalk(
        0xFE,
        (
            "该说希伦是毫无防范意识\x01",
            "还是什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "总之，必须要对总是喜欢\x01",
            "往露台跑的男人\x01",
            "多加注意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1097")

    Jump("loc_169B")

    label("loc_109C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1173")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1120")

    #C0043
    ChrTalk(
        0x9,
        (
            "听说今天阿修拉主任\x01",
            "去参加教授会了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "因为她起得很早，\x01",
            "所以估计现在这个时候\x01",
            "也还是睡眼惺忪的吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_116E")

    label("loc_1120")


    #C0045
    ChrTalk(
        0x9,
        (
            "阿修拉主任是个\x01",
            "爱睡懒觉的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "不会在教授会上\x01",
            "也昏昏沉沉地打瞌睡吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116E")

    Jump("loc_169B")

    label("loc_1173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1277")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1210")

    #C0047
    ChrTalk(
        0xFE,
        (
            "好安静啊～……\x01",
            "医生也是，实习医生也是，护士也是，\x01",
            "大家似乎都出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "……啊！\x01",
            "这正是一个把所有角落\x01",
            "都打扫干净的机会呢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1272")

    label("loc_1210")


    #C0049
    ChrTalk(
        0xFE,
        (
            "呵呵，既然决定了……\x01",
            "在大家回来之前，\x01",
            "必须要让这个地方焕然一新呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "打扫打扫，打扫打扫！\x02",
    )

    CloseMessageWindow()

    label("loc_1272")

    Jump("loc_169B")

    label("loc_1277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_12EF")

    #C0051
    ChrTalk(
        0xFE,
        "这里是女子宿舍，男性禁止进入哦！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "……开玩笑的。\x01",
            "因为要去研究楼的话，\x01",
            "就必须经过这个职员宿舍……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169B")

    label("loc_12EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1374")

    #C0053
    ChrTalk(
        0xFE,
        (
            "打扫打扫……\x01",
            "职员宿舍真的很干净呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "医生也是，护士也是，\x01",
            "大家都会工作到很晚，\x01",
            "所以基本上都没怎么使用过这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169B")

    label("loc_1374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_146C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1427")

    #C0055
    ChrTalk(
        0xFE,
        (
            "利顿医生刚才\x01",
            "回房间去休息了。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "他因为上个月的魔兽事件休假了，\x01",
            "所以现在约亚西姆医生就\x01",
            "推了很多工作给他。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "但是，能休息时\x01",
            "就应该尽量休息吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1467")

    label("loc_1427")


    #C0058
    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "我也差不多该去吃午饭了吧。\x01",
            "只顾着打扫了，肚子好饿啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1467")

    Jump("loc_169B")

    label("loc_146C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_14CE")

    #C0059
    ChrTalk(
        0xFE,
        (
            "刚才，阿修拉主任\x01",
            "慌慌张张就出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "今天也跟以前一样，\x01",
            "好像又睡过头了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169B")

    label("loc_14CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1557")

    #C0061
    ChrTalk(
        0xFE,
        (
            "明明已经打扫过一次了，\x01",
            "结果还是因为在意小污渍，\x01",
            "所以又打扫了一次。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "……毕竟是女子宿舍，\x01",
            "一定要非常非常干净才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169B")

    label("loc_1557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_15BB")

    #C0063
    ChrTalk(
        0xFE,
        (
            "好了，打扫成这样就没问题了。\x01",
            "……应该是吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "但是那些小污渍\x01",
            "让我好在意啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169B")

    label("loc_15BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1656")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1626")

    #C0065
    ChrTalk(
        0xFE,
        (
            "今天男子宿舍的人\x01",
            "全部都出去了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "大概都去研究楼或者\x01",
            "病房楼工作了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1651")

    label("loc_1626")


    #C0067
    ChrTalk(
        0xFE,
        (
            "好，为了努力工作的大家，\x01",
            "打扫打扫～☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1651")

    Jump("loc_169B")

    label("loc_1656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_169B")

    #C0068
    ChrTalk(
        0xFE,
        "打扫打扫……打扫打扫……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "打～扫～真～开～心～啊☆\x02",
    )

    CloseMessageWindow()

    label("loc_169B")

    TalkEnd(0xFE)
    Return()

    # Function_9_CF3 end

    def Function_10_169F(): pass

    label("Function_10_169F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_16B0")
    Jump("loc_1874")

    label("loc_16B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_16BE")
    Jump("loc_1874")

    label("loc_16BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_16CC")
    Jump("loc_1874")

    label("loc_16CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_16DA")
    Jump("loc_1874")

    label("loc_16DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_16E8")
    Jump("loc_1874")

    label("loc_16E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_16F6")
    Jump("loc_1874")

    label("loc_16F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1704")
    Jump("loc_1874")

    label("loc_1704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1712")
    Jump("loc_1874")

    label("loc_1712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_179B")

    #C0070
    ChrTalk(
        0xFE,
        (
            "阿修拉主任出去工作，\x01",
            "而我在宿舍待着……\x01",
            "这也是很稀奇的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "……好不容易能放个假。\x01",
            "能休息的时候就必须尽量休息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1874")

    label("loc_179B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_17A9")
    Jump("loc_1874")

    label("loc_17A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_17B7")
    Jump("loc_1874")

    label("loc_17B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_17C5")
    Jump("loc_1874")

    label("loc_17C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_184F")

    #C0072
    ChrTalk(
        0xFE,
        (
            "本来还以为阿修拉主任\x01",
            "今天也会迟到的，\x01",
            "不过好像还是赶上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "因为她经常埋头研究到深夜，\x01",
            "所以早上迟到\x01",
            "也是常有的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1874")

    label("loc_184F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_185D")
    Jump("loc_1874")

    label("loc_185D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_186B")
    Jump("loc_1874")

    label("loc_186B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1874")

    label("loc_1874")

    TalkEnd(0xFE)
    Return()

    # Function_10_169F end

    def Function_11_1878(): pass

    label("Function_11_1878")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1889")
    Jump("loc_1AD4")

    label("loc_1889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1905")

    #C0074
    ChrTalk(
        0xFE,
        (
            "我今天本来是打算\x01",
            "回到房间之后就好好休息的……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "但考试也已经临近了，所以必须要\x01",
            "尽量挤出时间来学习啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD4")

    label("loc_1905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1913")
    Jump("loc_1AD4")

    label("loc_1913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1921")
    Jump("loc_1AD4")

    label("loc_1921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_192F")
    Jump("loc_1AD4")

    label("loc_192F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_193D")
    Jump("loc_1AD4")

    label("loc_193D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_194B")
    Jump("loc_1AD4")

    label("loc_194B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_19CB")

    #C0076
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "终于能放假了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "虽然还是跟以前一样，没什么安排。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "我也去向约亚西姆医生请教下，\x01",
            "开始钓鱼好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD4")

    label("loc_19CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_19D9")
    Jump("loc_1AD4")

    label("loc_19D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_19E7")
    Jump("loc_1AD4")

    label("loc_19E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1A93")

    #C0079
    ChrTalk(
        0xFE,
        (
            "约亚西姆医生的想法，\x01",
            "我到现在还是搞不清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "一开始还以为他是\x01",
            "为了让我多学点东西，\x01",
            "才塞给我很多工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "结果他好像只是\x01",
            "想让自己轻松一点而已……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD4")

    label("loc_1A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1AA1")
    Jump("loc_1AD4")

    label("loc_1AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1AAF")
    Jump("loc_1AD4")

    label("loc_1AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1ABD")
    Jump("loc_1AD4")

    label("loc_1ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1ACB")
    Jump("loc_1AD4")

    label("loc_1ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1AD4")

    label("loc_1AD4")

    TalkEnd(0xFE)
    Return()

    # Function_11_1878 end

    def Function_12_1AD8(): pass

    label("Function_12_1AD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BD1")

    #C0082
    ChrTalk(
        0xFE,
        (
            "……盖里·罗塞尔著……\x01",
            "这边的是……拉格·尼克松著……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "在我所持有的众多医书中，\x01",
            "有好几本是我们医院\x01",
            "教授们的著作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "虽然平时没有特别的感觉，\x01",
            "但那些教授们全都是不会辱及\x01",
            "最先进医疗研究机构之名的优秀人才呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C6F")

    label("loc_1BD1")


    #C0085
    ChrTalk(
        0xFE,
        (
            "对了，不知道有没有\x01",
            "约亚西姆医生写的书呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "约亚西姆·琼塔著……\x01",
            "……没有找到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "不过，那个人看上去\x01",
            "就对出书没什么兴趣，\x01",
            "所以我也并不觉得奇怪。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C6F")

    Jump("loc_1EE2")

    label("loc_1C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1C82")
    Jump("loc_1EE2")

    label("loc_1C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1CF0")

    #C0088
    ChrTalk(
        0xFE,
        (
            "离傍晚还有一段时间……\x01",
            "还是稍微学习一会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "因为我从家里带了一大堆\x01",
            "有用的医书过来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE2")

    label("loc_1CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1CFE")
    Jump("loc_1EE2")

    label("loc_1CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1D0C")
    Jump("loc_1EE2")

    label("loc_1D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1D1A")
    Jump("loc_1EE2")

    label("loc_1D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1D28")
    Jump("loc_1EE2")

    label("loc_1D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1D36")
    Jump("loc_1EE2")

    label("loc_1D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D44")
    Jump("loc_1EE2")

    label("loc_1D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1DA0")

    #C0090
    ChrTalk(
        0xFE,
        (
            "我预定在傍晚时\x01",
            "去诊察室进行现场实习。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "必须让教授看看我\x01",
            "优秀的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE2")

    label("loc_1DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5A")

    #C0092
    ChrTalk(
        0xFE,
        (
            "虽然今天休息……\x01",
            "但是也必须好好学习呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "同寝室的芙萝拉也是，\x01",
            "连吃饭时间\x01",
            "都一直在学习。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "我下个月\x01",
            "也要去现场实习了……\x01",
            "所以必须趁现在好好预习呢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E9C")

    label("loc_1E5A")


    #C0095
    ChrTalk(
        0xFE,
        (
            "为了在下次的现场实习中\x01",
            "取得好的评价，\x01",
            "现在必须要努力学习～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E9C")

    Jump("loc_1EE2")

    label("loc_1EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1EAF")
    Jump("loc_1EE2")

    label("loc_1EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1EBD")
    Jump("loc_1EE2")

    label("loc_1EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1ECB")
    Jump("loc_1EE2")

    label("loc_1ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1ED9")
    Jump("loc_1EE2")

    label("loc_1ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1EE2")

    label("loc_1EE2")

    TalkEnd(0xFE)
    Return()

    # Function_12_1AD8 end

    def Function_13_1EE6(): pass

    label("Function_13_1EE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F76")

    #C0096
    ChrTalk(
        0xFE,
        (
            "虽然昨天休息……\x01",
            "但是因为跟希伦在一起，\x01",
            "所以累死我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "随时都要担心她又惹出什么乱子来。\x01",
            "啊，真是让人担惊受怕……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1FD4")

    label("loc_1F76")


    #C0098
    ChrTalk(
        0xFE,
        (
            "……呃，虽然弄得我有点手忙脚乱，\x01",
            "但也缓解了不少压力。\x01",
            "应该也算是一个有意义的假日……吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FD4")

    TalkEnd(0xFE)
    Return()

    # Function_13_1EE6 end

    def Function_14_1FD8(): pass

    label("Function_14_1FD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1FE9")
    Jump("loc_21A8")

    label("loc_1FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1FF7")
    Jump("loc_21A8")

    label("loc_1FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2005")
    Jump("loc_21A8")

    label("loc_2005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2066")

    #C0099
    ChrTalk(
        0xFE,
        (
            "……今天要值夜班，\x01",
            "所以打算尽早小睡一会。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        "……明白了的话，就赶快出去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21A8")

    label("loc_2066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2074")
    Jump("loc_21A8")

    label("loc_2074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2082")
    Jump("loc_21A8")

    label("loc_2082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_20E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_209D")
    Call(0, 15)
    Jump("loc_20E2")

    label("loc_209D")


    #C0101
    ChrTalk(
        0xFE,
        (
            "呼呜……\x01",
            "没想到竟然连续休假了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        "还是工作的时候比较轻松……\x02",
    )

    CloseMessageWindow()

    label("loc_20E2")

    Jump("loc_21A8")

    label("loc_20E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_20F5")
    Jump("loc_21A8")

    label("loc_20F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_214B")

    #C0103
    ChrTalk(
        0xFE,
        (
            "随便进别人的房间\x01",
            "真是不礼貌。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "如果不是急诊患者，\x01",
            "就请出去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A8")

    label("loc_214B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2159")
    Jump("loc_21A8")

    label("loc_2159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2167")
    Jump("loc_21A8")

    label("loc_2167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2175")
    Jump("loc_21A8")

    label("loc_2175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2183")
    Jump("loc_21A8")

    label("loc_2183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2191")
    Jump("loc_21A8")

    label("loc_2191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_219F")
    Jump("loc_21A8")

    label("loc_219F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_21A8")

    label("loc_21A8")

    TalkEnd(0xFE)
    Return()

    # Function_14_1FD8 end

    def Function_15_21AC(): pass

    label("Function_15_21AC")


    #C0105
    ChrTalk(
        0xFE,
        (
            "我要来了有关医生的小说，\x01",
            "试着读了一遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "要是多写一些实用\x01",
            "技术之类的就好了……\x01",
            "算了，反正就是本娱乐小说。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "……这个给你们吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0108
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2CE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2CE, 1)
    SetScenarioFlags(0x9D, 0)
    Return()

    # Function_15_21AC end

    def Function_16_2283(): pass

    label("Function_16_2283")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2436")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A1")
    Call(0, 18)
    Jump("loc_2431")

    label("loc_22A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_239A")

    #C0109
    ChrTalk(
        0x10,
        (
            "#1304F……那么，今天是不是\x01",
            "应该多去陪陪米海尔呢～\x02\x03",

            "#1300F今天是小滴外出的日子，\x01",
            "他肯定会觉得很寂寞吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……塞茜尔姐姐\x01",
            "是大家的『姐姐』呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2392")

    #C0111
    ChrTalk(
        0x10A,
        "#0608F（……这位女性，记得是那家伙的……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEC, 6)

    label("loc_2392")

    SetScenarioFlags(0x0, 4)
    Jump("loc_2431")

    label("loc_239A")


    #C0112
    ChrTalk(
        0x10,
        (
            "#1304F那么，就去给米海尔\x01",
            "读读连环画吧。\x02\x03",

            "#1302F为了应对这种情况，\x01",
            "我特意把当年给罗伊德\x01",
            "读过的连环画带来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        "#0006F（总觉得有些难为情啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_2431")

    Jump("loc_2BF2")

    label("loc_2436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2444")
    Jump("loc_2BF2")

    label("loc_2444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_25B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245F")
    Call(0, 17)
    Jump("loc_25AB")

    label("loc_245F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_252F")

    #C0114
    ChrTalk(
        0x10,
        (
            "#1300F对了对了，我正要带小滴\x01",
            "去院子里散步呢。\x02\x03",

            "#1304F小滴的听力很好，\x01",
            "所以经常会告诉我一些\x01",
            "我察觉不到的动物们的动静呢。\x02\x03",

            "#1300F呵呵，虽然是护士工作的一部分，\x01",
            "但是这个真的很让我期待呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_25AB")

    label("loc_252F")


    #C0115
    ChrTalk(
        0x10,
        (
            "#1300F跟小滴一起散步的话，\x01",
            "就会有各种各样的发现，很有趣哦。\x02\x03",

            "呵呵，虽然是护士工作的一部分，\x01",
            "但是这个真的让我很期待呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25AB")

    Jump("loc_2BF2")

    label("loc_25B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_END)), "loc_29A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25CB")
    Call(0, 17)
    Jump("loc_299D")

    label("loc_25CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_291D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 0)), scpexpr(EXPR_END)), "loc_2670")

    #C0116
    ChrTalk(
        0x10,
        "#1309F呵呵，你们又来了呢。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0005F啊，说起来，塞茜尔姐姐……\x02\x03",

            "#0000F昨天和你进行过导力通讯的朋友，\x01",
            "指的就是彩虹剧团的伊莉娅小姐吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D5")

    label("loc_2670")


    #C0118
    ChrTalk(
        0x10,
        (
            "#1306F嗯，因为我也住在宿舍，\x01",
            "所以两个人\x01",
            "很少有机会见面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#0004F哈哈，说得也是啊。\x02\x03",

            "#0001F塞茜尔姐姐……\x01",
            "工作虽然忙，\x01",
            "但也别太勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x10,
        (
            "#1309F呵呵，我没有在勉强自己啊。\x02\x03",

            "有时会用导力通讯跟朋友们聊天，\x01",
            "借此来舒缓心情。\x02\x03",

            "#1302F昨天晚上也是，和一个久未联系\x01",
            "的朋友聊了很长时间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#0005F莫，莫非……\x01",
            "那个朋友就是彩虹剧团的伊莉娅小姐吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D5")


    #C0122
    ChrTalk(
        0x10,
        (
            "#1305F哎呀，你知道了吗？\x02\x03",

            "#1300F奇怪了呢，我什么时候告诉你的……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#0011F……咦！？\x02\x03",

            "（糟糕了，就算是对塞茜尔姐姐，\x01",
            "　也不能泄露调查的事情……）\x02\x03",

            "#0012F那、那个……\x01",
            "……大概是之前进行\x01",
            "导力通讯的时候告诉我的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x10,
        (
            "#1303F嗯…………\x02\x03",

            "#1300F……也是，你这么说的话，\x01",
            "好像是那样的……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#0006F（好、好危险……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 1)
    Jump("loc_299D")

    label("loc_291D")


    #C0126
    ChrTalk(
        0x10,
        (
            "#1306F啊啊，真有点遗憾。\x02\x03",

            "本来还打算下次偷偷带你去见伊莉娅，\x01",
            "让你大吃一惊的。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#0012F哈、哈哈……\x01",
            "（都已经见过了……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_299D")

    Jump("loc_2BF2")

    label("loc_29A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2BF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29BD")
    Call(0, 17)
    Jump("loc_2BF2")

    label("loc_29BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B95")

    #C0128
    ChrTalk(
        0x10,
        (
            "#1306F我也住在宿舍，\x01",
            "所以两个人\x01",
            "很少有机会见面。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#0004F哈哈，说得也是呢。\x02\x03",

            "#0001F塞茜尔姐姐……\x01",
            "工作虽然忙，\x01",
            "但也别太勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x10,
        (
            "#1309F呵呵，我没有在勉强自己啊。\x02\x03",

            "有时会用导力通讯跟朋友们聊天，\x01",
            "借此来舒缓心情。\x02\x03",

            "#1302F昨天晚上也是，和一个久未联系\x01",
            "的朋友聊了很长时间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#0009F哈哈，这样啊。\x02\x03",

            "#0000F那个朋友\x01",
            "是我认识的人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x10,
        (
            "#1304F呵呵……你猜呢。\x02\x03",

            "#1302F罗伊德你有着不通世事的\x01",
            "意外一面，所以可能会不认识她呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#0005F？？？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 0)
    Jump("loc_2BF2")

    label("loc_2B95")


    #C0134
    ChrTalk(
        0x10,
        (
            "#1304F她似乎也在拼命努力……\x01",
            "所以我也必须好好加油了。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#0005F（到底是在说谁呢……）\x02",
    )

    CloseMessageWindow()

    label("loc_2BF2")

    TalkEnd(0xFE)
    Return()

    # Function_16_2283 end

    def Function_17_2BF6(): pass

    label("Function_17_2BF6")

    EventBegin(0x0)
    Fade(500)
    OP_68(153900, 1000, 53760, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 153000, 0, 54180, 90)
    SetChrPos(0x102, 153000, 0, 53180, 90)
    SetChrPos(0x103, 151800, 0, 53180, 90)
    SetChrPos(0x104, 151800, 0, 54180, 90)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x10, 0x10E, 0x0)
    OP_0D()

    #C0136
    ChrTalk(
        0x10,
        (
            "#1302F哎呀，是大家啊。\x01",
            "呵呵，欢迎。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CE2")

    #C0137
    ChrTalk(
        0x101,
        (
            "#0005F啊，莫非这里是\x01",
            "塞茜尔姐姐的宿舍吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D0D")

    label("loc_2CE2")


    #C0138
    ChrTalk(
        0x101,
        (
            "#0005F这里果然是\x01",
            "塞茜尔姐姐的宿舍吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D0D")


    #C0139
    ChrTalk(
        0x10,
        (
            "#1300F嗯，没错。\x02\x03",

            "#1304F但是我平时经常睡在\x01",
            "病房楼和休息室，\x01",
            "所以这里的利用率只有一半左右呢。\x02",
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

    #C0140
    ChrTalk(
        0x102,
        "#0106F塞茜尔小姐……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x103,
        "#0208F……您工作努力过头了。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        (
            "#0306F请让我多帮你\x01",
            "分担一些事情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x10,
        (
            "#1309F没关系，没关系。\x01",
            "我并没有勉强自己。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153000, 0, 53680, 90)
    SetScenarioFlags(0xAE, 5)
    EventEnd(0x5)
    Return()

    # Function_17_2BF6 end

    def Function_18_2E7D(): pass

    label("Function_18_2E7D")

    EventBegin(0x0)
    Fade(500)
    OP_68(153900, 1000, 53760, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EDD")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, 150600, 0, 53680, 90)

    label("loc_2EDD")

    SetChrPos(0x101, 153000, 0, 54180, 90)
    SetChrPos(0x102, 153000, 0, 53180, 90)
    SetChrPos(0x103, 151800, 0, 53180, 90)
    SetChrPos(0x104, 151800, 0, 54180, 90)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x10, 0x5A, 0x0)
    OP_0D()

    #C0144
    ChrTalk(
        0x10,
        "#1308F………………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0145
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "塞茜尔正望着柜子上的照片。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FBD")

    #C0146
    ChrTalk(
        0x101,
        (
            "#0005F塞茜尔姐姐……？\x01",
            "（啊，那张照片是……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEA")

    label("loc_2FBD")


    #C0147
    ChrTalk(
        0x101,
        (
            "#0005F塞茜尔姐姐……\x01",
            "（那张照片是……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_302D")

    #C0148
    ChrTalk(
        0x10A,
        "#0608F（……这位女性，记得是那家伙的……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEC, 6)

    label("loc_302D")

    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x10, 0x10E, 0x1F4)

    #C0149
    ChrTalk(
        0x10,
        (
            "#1302F哎呀，欢迎大家。\x02\x03",

            "#1305F………？\x01",
            "看起来好像很急呢，\x01",
            "发生什么事情了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，是的。\x01",
            "现在正在调查，所以有点忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        "#0100F塞茜尔小姐是在休息吗？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x10,
        (
            "#1304F呵呵，算是吧。\x02\x03",

            "虽然你们的工作确实很重要，\x01",
            "但还是注意不要勉强自己哦。\x02\x03",

            "#1300F要是太勉强自己，\x01",
            "我会强行让你们住院治疗的。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        "#0011F我、我知道了。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        "#0100F呵呵，谨记于心。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        (
            "#0309F（嗯，如果动手的人是塞茜尔小姐，\x01",
            "　我很乐意啊～！）\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        "#0206F（……我就知道你会这么说。）\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153000, 0, 53680, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_323C")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_323C")

    SetScenarioFlags(0xEC, 5)
    EventEnd(0x5)
    Return()

    # Function_18_2E7D end

    def Function_19_3242(): pass

    label("Function_19_3242")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetChrName("")

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一张照片，\x01",
            "照片上是塞茜尔和罗伊德，\x01",
            "还有一个干练精神的青年。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3357")

    #A0158
    AnonymousTalk(
        0x101,
        (
            "#0008F（……和塞茜尔姐姐与\x01",
            "　大哥的合照。）\x02\x03",

            "（我一直随身带着……\x01",
            "　塞茜尔姐姐也将它放在房间中呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D6")

    label("loc_3357")


    #A0159
    AnonymousTalk(
        0x101,
        (
            "#0005F（啊……和塞茜尔姐姐与\x01",
            "　大哥的合照。）\x02\x03",

            "#0003F（这张照片会在这里，\x01",
            "　也就是说，这里莫非是\x01",
            "　塞茜尔姐姐的宿舍吗？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D6")

    SetScenarioFlags(0x69, 5)

    label("loc_33D9")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_19_3242 end

    SaveToFile()

Try(main)
