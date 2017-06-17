from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0330.bin",                # FileName
        "c0330",                    # MapName
        "c0330",                    # Location
        0x002C,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 44, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0330",                  # 0
        "哈罗德",                 # 1
        "索菲亚",                 # 2
        "柯林",                   # 3
        "哈罗德",                 # 4
        "索菲亚",                 # 5
        "柯林",                   # 6
        "辛迪",                   # 7
        "库雷优",                 # 8
    ))

    AddCharChip((
        "chr/ch09300.itc",                   # 00
        "chr/ch09302.itc",                   # 01
        "chr/ch09400.itc",                   # 02
        "chr/ch09402.itc",                   # 03
        "chr/ch07200.itc",                   # 04
        "chr/ch07202.itc",                   # 05
        "chr/ch22100.itc",                   # 06
        "chr/ch33300.itc",                   # 07
    ))

    DeclNpc(-340,    0,       4409,    315,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(550,     0,       2039,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(37479,   0,       3799,    180,  257,  0x0, 0,   4,   0,   0,   1,   0,   15,  255,  0)
    DeclNpc(34450,   200,     3339,    225,  389,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(34340,   200,     519,     315,  389,  0x0, 0,   3,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(31280,   200,     3420,    135,  389,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(33299,   0,       -100,    0,    405,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(35319,   0,       1679,    277,  389,  0x0, 0,   7,   0,   0,   0,   0,   18,  255,  0)

    ScpFunction((
        "Function_0_1E4",          # 00, 0
        "Function_1_29C",          # 01, 1
        "Function_2_2C7",          # 02, 2
        "Function_3_2F2",          # 03, 3
        "Function_4_353",          # 04, 4
        "Function_5_75E",          # 05, 5
        "Function_6_7B1",          # 06, 6
        "Function_7_1202",         # 07, 7
        "Function_8_1511",         # 08, 8
        "Function_9_15C5",         # 09, 9
        "Function_10_2330",        # 0A, 10
        "Function_11_24F7",        # 0B, 11
        "Function_12_258D",        # 0C, 12
        "Function_13_2636",        # 0D, 13
        "Function_14_279D",        # 0E, 14
        "Function_15_29BE",        # 0F, 15
        "Function_16_32D5",        # 10, 16
        "Function_17_390A",        # 11, 17
        "Function_18_3A06",        # 12, 18
        "Function_19_3B4B",        # 13, 19
    ))


    def Function_0_1E4(): pass

    label("Function_0_1E4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_224"),
        (1, "loc_230"),
        (2, "loc_23C"),
        (3, "loc_248"),
        (4, "loc_254"),
        (5, "loc_260"),
        (6, "loc_26C"),
        (SWITCH_DEFAULT, "loc_278"),
    )


    label("loc_224")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_230")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_23C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_248")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_254")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_260")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_26C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_278")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_284")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_29B")

    Return()

    # Function_0_1E4 end

    def Function_1_29C(): pass

    label("Function_1_29C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C6")
    OP_94(0xFE, 0x9268, 0x157C, 0x8F48, 0x85C, 0x3E8)
    Sleep(300)
    Jump("Function_1_29C")

    label("loc_2C6")

    Return()

    # Function_1_29C end

    def Function_2_2C7(): pass

    label("Function_2_2C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F1")
    OP_94(0xFE, 0xFFFFF240, 0x80C, 0xC58, 0x139C, 0x3E8)
    Sleep(300)
    Jump("Function_2_2C7")

    label("loc_2F1")

    Return()

    # Function_2_2C7 end

    def Function_3_2F2(): pass

    label("Function_3_2F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_352")
    OP_95(0xFE, 35110, 0, 1240, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(2500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(100)
    OP_95(0xFE, 37510, 0, -1160, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(2500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(100)
    Jump("Function_3_2F2")

    label("loc_352")

    Return()

    # Function_3_2F2 end

    def Function_4_353(): pass

    label("Function_4_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_393")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, 0, 0, 5360, 180)
    SetChrPos(0xA, 0, 0, 3930, 360)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3A6")
    SetChrFlags(0x9, 0x80)
    Jump("loc_75D")

    label("loc_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3FE")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0x9, 35510, 0, 3010, 222)
    SetChrPos(0xA, 37530, 0, -1240, 89)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3F9")
    ClearChrFlags(0xE, 0x10)

    label("loc_3F9")

    Jump("loc_75D")

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_434")
    SetChrPos(0x9, -370, 0, -2190, 180)
    SetChrPos(0xA, -1230, 0, -1880, 135)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_45B")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_75D")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4A7")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 10, 0, -2230, 180)
    SetChrPos(0x9, 32350, 0, 7580, 270)
    SetChrPos(0xA, 30940, 0, 7580, 90)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4BF")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_75D")

    label("loc_4BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_519")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -490, 0, 5140, 180)
    SetChrPos(0x9, 790, 0, 4260, 270)
    SetChrPos(0xA, -690, 0, 3590, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_514")
    SetChrFlags(0x8, 0x10)

    label("loc_514")

    Jump("loc_75D")

    label("loc_519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_567")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x9, -1230, 0, 5370, 135)
    SetChrPos(0xA, -1670, 0, 3900, 45)
    BeginChrThread(0xA, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_562")
    SetChrFlags(0x8, 0x10)

    label("loc_562")

    Jump("loc_75D")

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5BD")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x8, 790, 0, 4260, 270)
    SetChrPos(0x9, -490, 0, 5140, 180)
    SetChrPos(0xA, -690, 0, 3590, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5D5")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_75D")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_61A")
    SetChrPos(0x9, 5170, 0, 3210, 360)
    SetChrPos(0xA, 34480, 0, 5610, 315)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_615")
    SetChrFlags(0x9, 0x10)

    label("loc_615")

    Jump("loc_75D")

    label("loc_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_639")
    SetChrPos(0x9, -370, 0, -2190, 180)
    Jump("loc_75D")

    label("loc_639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_695")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x9, 35510, 0, 3010, 222)
    SetChrPos(0xA, 38540, 0, 320, 180)
    SetChrPos(0xF, 35110, 0, 1240, 315)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xF, 0, 0, 3)
    Jump("loc_75D")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6CB")
    SetChrPos(0x9, 40930, 0, -1640, 90)
    SetChrPos(0xA, 40920, 0, -410, 135)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_703")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -1230, 0, 5370, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FE")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_6FE")

    Jump("loc_75D")

    label("loc_703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_735")
    SetChrPos(0x9, 4560, 0, 10380, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_730")
    SetChrFlags(0x9, 0x10)

    label("loc_730")

    Jump("loc_75D")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_75D")
    SetChrPos(0x9, 40930, 0, -1640, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_75D")
    SetChrFlags(0x9, 0x10)

    label("loc_75D")

    Return()

    # Function_4_353 end

    def Function_5_75E(): pass

    label("Function_5_75E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_777")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_77D")

    label("loc_777")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_799")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7B0")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7B0")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7B0")

    label("loc_7B0")

    Return()

    # Function_5_75E end

    def Function_6_7B1(): pass

    label("Function_6_7B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_83F")

    #C0001
    ChrTalk(
        0x8,
        (
            "#3600F这附近竟然有人失踪……\x01",
            "我也会尽全力提供帮助的。\x02\x03",

            "正是在这种时候，我们才更要\x01",
            "举全家之力来帮助和支持人家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F7")

    label("loc_83F")


    #C0002
    ChrTalk(
        0x8,
        (
            "#3600F我妻子好像一直都在\x01",
            "陪着库雷优夫人。\x02\x03",

            "#3603F……库雷优夫人是\x01",
            "我妻子的好朋友，\x01",
            "我妻子应该很担心她吧……\x02\x03",

            "#3600F我认为妻子现在最好\x01",
            "能多陪陪她，\x01",
            "我也会竭尽所能，提供帮助的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_8F7")

    Jump("loc_11FE")

    label("loc_8FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_CAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 7)), scpexpr(EXPR_END)), "loc_AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_99D")

    #C0003
    ChrTalk(
        0x8,
        (
            "#3603F昨天真是给你们添麻烦了……\x01",
            "还跟你们说了那么冗长无趣的话，\x01",
            "实在非常抱歉。\x02\x03",

            "#3601F不好意思，我得再去稍微\x01",
            "冷静一下头脑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0")

    label("loc_99D")


    #C0004
    ChrTalk(
        0x8,
        (
            "#3603F昨天真是给你们添麻烦了……\x01",
            "还跟你们说了那么冗长无趣的话，\x01",
            "实在非常抱歉。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0005
    ChrTalk(
        0x8,
        (
            "#3608F虽然只是我个人的臆想……\x01",
            "但昨天出手相助的那女孩\x01",
            "应该并没有自报姓名。\x02\x03",

            "#3603F所以，我觉得她会不会是\x01",
            "我在天国的女儿……\x02\x03",

            "#3600F……哈哈，我想得太美了。\x01",
            "不好意思，我必须再冷静一下头脑呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AD0")

    Jump("loc_CA5")

    label("loc_AD5")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0006
    ChrTalk(
        0x8,
        (
            "#3600F各位……\x02\x03",

            "昨天真是谢谢你们了。\x01",
            "一而再再而三的麻烦你们，\x01",
            "都不知道要怎么感谢才好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0000F您太客气了，那并不算什么。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0100F您的家人似乎也\x01",
            "都平静下来了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#3603F嗯，我让索菲亚和柯林\x01",
            "去好好休息了。\x02\x03",

            "#3600F不过柯林好像并没觉得害怕呢，\x01",
            "哈哈哈……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0010
    ChrTalk(
        0x8,
        (
            "#3608F但我们已经尝过苦头了。\x01",
            "不想再遇到那种可怕、悲痛的事，\x01",
            "也不想再失去什么……\x02\x03",

            "#3603F只想过上平静安稳的生活，\x01",
            "这就是我们如今唯一的愿望。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAE, 7)

    label("loc_CA5")

    Jump("loc_11FE")

    label("loc_CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_DAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D14")
    OP_4B(0xA, 0xFF)

    #C0011
    ChrTalk(
        0x8,
        (
            "#3600F柯林，你准备好了吗？\x02\x03",

            "要是口渴了就跟妈妈说啊，\x01",
            "妈妈带着水壶呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_DA8")

    label("loc_D14")


    #C0012
    ChrTalk(
        0x8,
        (
            "#3600F儿子说今天有庆典游行，\x01",
            "想出去玩。\x02\x03",

            "偶尔也要陪陪家人，\x01",
            "所以我今天要陪他们\x01",
            "好好玩个够。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#0000F哈哈哈……您也很辛苦啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 500)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_DA8")

    Jump("loc_11FE")

    label("loc_DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_EBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E39")
    OP_4B(0x9, 0xFF)

    #C0014
    ChrTalk(
        0x8,
        (
            "#3603F纪念庆典这几天，\x01",
            "市区内的交通都堵塞了，\x01",
            "没法开车啊……\x02\x03",

            "#3600F索菲亚，你还行吗？\x01",
            "累了的话要说哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_EB8")

    label("loc_E39")


    #C0015
    ChrTalk(
        0x8,
        (
            "#3600F柯林说他\x01",
            "无论如何也想去看看\x01",
            "港湾区的庆典活动。\x02\x03",

            "明明昨晚还\x01",
            "一直喊累的……\x01",
            "真是个不接受教训的孩子啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_EB8")

    Jump("loc_11FE")

    label("loc_EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1070")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F55")

    #C0016
    ChrTalk(
        0x8,
        (
            "#3600F不愧是七十周年庆典，\x01",
            "今年比往年都要热闹啊。\x02\x03",

            "不能让柯林玩得太累了，\x01",
            "所以就在这附近稍微逛一逛吧。\x02\x03",

            "各位，\x01",
            "工作加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106B")

    label("loc_F55")


    #C0017
    ChrTalk(
        0x8,
        (
            "#3605F哦，各位，你们正在工作吗？\x02\x03",

            "#3600F真是辛苦啊……\x01",
            "我们正要\x01",
            "出去玩玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0000F和家人共度纪念庆典……\x01",
            "这果然是最传统的\x01",
            "过节方式呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#0100F呵呵，请不必在意我们，\x01",
            "好好享受庆典吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#3600F那我们就不客气了。\x02\x03",

            "反正……柯林年纪还小，\x01",
            "出去转一圈应该\x01",
            "就足够了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_106B")

    Jump("loc_11FE")

    label("loc_1070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 4)), scpexpr(EXPR_END)), "loc_11F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10FB")

    #C0021
    ChrTalk(
        0x8,
        (
            "#3600F如果各位累了，\x01",
            "可以在我们家\x01",
            "休息休息。\x02\x03",

            "哈哈，请千万不要客气啊。\x01",
            "很多生意上的顾客\x01",
            "也经常暂住在我们家的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11EE")

    label("loc_10FB")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0022
    ChrTalk(
        0x8,
        (
            "#3605F啊，是各位……\x01",
            "你们来了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#0100F好像\x01",
            "打扰你们了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#3600F没有没有，没那回事。\x02\x03",

            "对了……你们\x01",
            "累了吧？\x02\x03",

            "不嫌弃的话，就在我们家\x01",
            "好好休息休息吧。\x02\x03",

            "哈哈，但是家里也没什么东西好招待的，\x01",
            "委屈各位了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_11EE")

    Jump("loc_11FE")

    label("loc_11F3")

    OP_4B(0x9, 0xFF)
    Call(0, 8)
    OP_4C(0x9, 0xFF)

    label("loc_11FE")

    TalkEnd(0xFE)
    Return()

    # Function_6_7B1 end

    def Function_7_1202(): pass

    label("Function_7_1202")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1296")
    Jump("loc_12E0")

    label("loc_1296")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12B6")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12E0")

    label("loc_12B6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12D6")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12E0")

    label("loc_12D6")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E0")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1509")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13B5")

    #C0025
    ChrTalk(
        0xB,
        (
            "#3608F这几年来，我还是第一次向别人\x01",
            "提起女儿的事……\x02\x03",

            "我思考了很多，果然还是想\x01",
            "先好好休息一段时间。\x02\x03",

            "现在不应该马上投入工作，\x01",
            "因为还是家人比较重要。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1509")

    label("loc_13B5")


    #C0026
    ChrTalk(
        0x101,
        (
            "#0000F哈罗德先生……\x01",
            "您在用餐吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        (
            "#3600F哈哈，其实我暂时\x01",
            "休业了。\x02\x03",

            "大概会休息两个星期左右，\x01",
            "利用这段时间来调整一下心情。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1463")

    #C0028
    ChrTalk(
        0x102,
        "#0102F这样啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B6")

    label("loc_1463")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_148E")

    #C0029
    ChrTalk(
        0x103,
        "#0202F这样啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B6")

    label("loc_148E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14B6")

    #C0030
    ChrTalk(
        0x104,
        "#0300F原来如此……\x02",
    )

    CloseMessageWindow()

    label("loc_14B6")


    #C0031
    ChrTalk(
        0xB,
        (
            "#3600F这一个星期都陪着家人，\x01",
            "真是其乐融融啊。\x02\x03",

            "所以我妻子和柯林\x01",
            "都很开心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1509")

    SetChrSubChip(0xB, 0x0)
    TalkEnd(0xB)
    Return()

    # Function_7_1202 end

    def Function_8_1511(): pass

    label("Function_8_1511")


    #C0032
    ChrTalk(
        0x8,
        (
            "#3600F抱歉，谈判时间拖长了。\x02\x03",

            "……柯林\x01",
            "还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            "#3700F嗯，他现在正在\x01",
            "画画呢。\x02\x03",

            "还说想要\x01",
            "新的画本哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "#3600F哈哈哈，这样啊……\x01",
            "那孩子的好奇心也很重呢。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x6A, 4)
    Return()

    # Function_8_1511 end

    def Function_9_15C5(): pass

    label("Function_9_15C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_165D")
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1648")

    #C0035
    ChrTalk(
        0x9,
        (
            "#3701F不过……她的丈夫那么温柔，\x01",
            "竟然也会口出秽语。\x02\x03",

            "真让人担心啊，\x01",
            "他不会\x01",
            "遇到什么事了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1650")

    label("loc_1648")

    Call(0, 13)
    ClearChrFlags(0xE, 0x10)

    label("loc_1650")

    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Jump("loc_232C")

    label("loc_165D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_174F")

    #C0036
    ChrTalk(
        0x9,
        (
            "#3700F最近工作很顺利。\x02\x03",

            "并不是指生意\x01",
            "有多好……\x01",
            "而是和丈夫一起工作，真的很快乐。\x02\x03",

            "#3708F……向各位倾吐后，\x01",
            "我好像释然了一些。\x02\x03",

            "#3700F我先生他今天去阿尔摩利卡村了，\x01",
            "如果各位看见他了，\x01",
            "就麻烦跟他打声招呼，说说话哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1892")

    label("loc_174F")


    #C0037
    ChrTalk(
        0x9,
        (
            "#3700F这不是支援科的各位吗……？\x01",
            "真是好久不见啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#0000F索菲亚夫人，\x01",
            "听说您家的生意又重新开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "#3700F嗯，老公当时说要休业一阵子的时候，\x01",
            "我实在是吃了一惊。\x02\x03",

            "#3708F但毕竟发生了这么多事……\x01",
            "我觉得他应该是想\x01",
            "调整一下心态，再开始工作吧。\x02\x03",

            "#3700F呵呵，应该是因为休息有了效果，\x01",
            "所以最近工作都很顺利哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1892")

    Jump("loc_232C")

    label("loc_1897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 0)), scpexpr(EXPR_END)), "loc_18FC")

    #C0040
    ChrTalk(
        0x9,
        (
            "#3700F今天我打算\x01",
            "一天都陪着柯林。\x02\x03",

            "真是太好了……\x01",
            "感谢您，爱德丝女神……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A54")

    label("loc_18FC")


    #C0041
    ChrTalk(
        0x9,
        (
            "#3700F啊……是警察局的各位啊。\x02\x03",

            "昨天真是\x01",
            "谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，\x01",
            "请不必这么客气，\x01",
            "因为这也是警察的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        (
            "#0300F哎，那也算是难得的\x01",
            "像点警察样的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#0100F如果还有什么需要帮忙的，\x01",
            "请不必客气，随时联络特别任务支援科。\x01",
            "我们会竭尽所能为您提供帮助的。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "#3700F好的，真是……\x02\x03",

            "十分感谢。\x01",
            "如果有需要，我会去麻烦各位的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 0)

    label("loc_1A54")

    Jump("loc_232C")

    label("loc_1A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1BB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1AB2")

    #C0046
    ChrTalk(
        0x9,
        (
            "#3700F游行是几点开始呢？\x01",
            "再不快点的话，\x01",
            "说不定就赶不上了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB3")

    label("loc_1AB2")


    #C0047
    ChrTalk(
        0x9,
        (
            "#3700F结果还是\x01",
            "拗不过柯林。\x02\x03",

            "呼，这孩子最近很任性，\x01",
            "好像也开始学会撒娇了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0048
    ChrTalk(
        0x9,
        (
            "#3708F……啊……………\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#0000F请问怎么了吗？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "#3708F不……没什么。\x02\x03",

            "#3700F呵呵，今天必须要\x01",
            "好好欣赏一下游行呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1BB3")

    Jump("loc_232C")

    label("loc_1BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C47")
    OP_4B(0x8, 0xFF)

    #C0051
    ChrTalk(
        0x9,
        (
            "#3701F柯林也真是的，不知道他从哪里听来\x01",
            "那个什么庆典活动的……\x02\x03",

            "总之我是有点担心他啊。\x02\x03",

            "本来这种时候人就已经很多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_232C")

    label("loc_1C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C60")
    OP_4B(0xA, 0xFF)
    Call(0, 12)
    OP_4C(0xA, 0xFF)
    Jump("loc_232C")

    label("loc_1C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1D78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1CD7")

    #C0052
    ChrTalk(
        0x9,
        (
            "#3700F今天是去教堂\x01",
            "祷告的日子。\x02\x03",

            "……柯林真是的，只是穿个袜子而已，\x01",
            "都不知道要花多长时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D73")

    label("loc_1CD7")

    SetChrPos(0xA, 9860, 4000, 23690, 45)

    #C0053
    ChrTalk(
        0x9,
        (
            "#3700F柯林～你准备好了吗～？\x02\x03",

            "不快点的话，\x01",
            "我就要把你一个人丢下了哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xA,
        "#100P#3805F嗯～等一下啦，妈妈～！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, 34480, 0, 5610, 315)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)

    label("loc_1D73")

    Jump("loc_232C")

    label("loc_1D78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1EB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1DE6")

    #C0055
    ChrTalk(
        0x9,
        (
            "#3700F我先生今天去\x01",
            "乌尔斯拉医院了。\x02\x03",

            "应该又会给那边\x01",
            "打点折扣吧，\x01",
            "……他总是这样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAE")

    label("loc_1DE6")


    #C0056
    ChrTalk(
        0x9,
        (
            "#3700F其实，自从上个月的那个事件以来，\x01",
            "我先生他与玛因兹的人们做生意时，\x01",
            "就会给他们打９折哦。\x02\x03",

            "所以我们在那边\x01",
            "并没有什么盈利。\x01",
            "……呵呵，真是个让人头痛的人啊。\x02\x03",

            "不过……这才正符合\x01",
            "他的性格呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1EAE")

    Jump("loc_232C")

    label("loc_1EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1F66")
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F5A")

    #C0057
    ChrTalk(
        0x9,
        (
            "#3700F对了对了，香芹就是要\x01",
            "像这样撒开。\x02\x03",

            "嗯，做得很棒哦。\x01",
            "辛迪将来\x01",
            "一定会是个好妻子的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0058
    ChrTalk(
        0xE,
        "啊，真的吗～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F5D")

    label("loc_1F5A")

    Call(0, 11)

    label("loc_1F5D")

    OP_4C(0xE, 0xFF)
    Jump("loc_232C")

    label("loc_1F66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_205E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2005")

    #C0059
    ChrTalk(
        0x9,
        (
            "#3700F今天是烹饪教室\x01",
            "上课的日子。\x02\x03",

            "虽说是上课，但也只是\x01",
            "和邻居们\x01",
            "一起开开心心地做菜而已……\x02\x03",

            "呵呵，我必须抓紧时间\x01",
            "做准备了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2059")

    label("loc_2005")


    #C0060
    ChrTalk(
        0x9,
        (
            "#3700F这真的不是什么重要活动，\x01",
            "只是邻居们肯\x01",
            "赏脸而已。\x02\x03",

            "那么，我得预先准备了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2059")

    Jump("loc_232C")

    label("loc_205E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_20D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 4)), scpexpr(EXPR_END)), "loc_20C6")

    #C0061
    ChrTalk(
        0x9,
        (
            "#3700F各位是我先生\x01",
            "的朋友吧。\x02\x03",

            "我是哈罗德的妻子，\x01",
            "名叫索菲亚。\x01",
            "请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D1")

    label("loc_20C6")

    OP_4B(0x8, 0xFF)
    Call(0, 8)
    OP_4C(0x8, 0xFF)

    label("loc_20D1")

    Jump("loc_232C")

    label("loc_20D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_2202")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2157")

    #C0062
    ChrTalk(
        0x9,
        (
            "#3700F我一点都不懂得做生意。\x01",
            "其实该说是\x01",
            "非常不擅长……\x02\x03",

            "呵呵，不过这也是\x01",
            "为了帮老公的忙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FD")

    label("loc_2157")


    #C0063
    ChrTalk(
        0x9,
        "#3700F嗯，这个发票是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    #C0064
    ChrTalk(
        0x9,
        (
            "#3700F我趁丈夫去采购的这段时间，\x01",
            "在整理发票。\x02\x03",

            "虽然我真的很\x01",
            "不擅长这个……\x02\x03",

            "不过这都是为了帮老公的忙。\x01",
            "必须努力呢。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)

    label("loc_21FD")

    Jump("loc_2211")

    label("loc_2202")

    Call(0, 10)
    OP_93(0x9, 0x0, 0x1F4)
    SetChrFlags(0x9, 0x10)

    label("loc_2211")

    Jump("loc_232C")

    label("loc_2216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_229A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_2286")

    #C0065
    ChrTalk(
        0x9,
        (
            "#3700F嗯，料理要像这样\x01",
            "装在盘子里才行哦。\x02\x03",

            "呵呵……我先生他\x01",
            "今天应该会\x01",
            "早点回来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2295")

    label("loc_2286")

    Call(0, 10)
    OP_93(0x9, 0x5A, 0x1F4)
    SetChrFlags(0x9, 0x10)

    label("loc_2295")

    Jump("loc_232C")

    label("loc_229A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_2329")

    #C0066
    ChrTalk(
        0x9,
        (
            "#3700F对不起啊，我弄错了。\x02\x03",

            "我先生他是贸易商，\x01",
            "所以经常会有顾客来。\x02\x03",

            "如果有什么需要，\x01",
            "随时都可以来找我，\x01",
            "我或许能帮上点忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232C")

    label("loc_2329")

    Call(0, 10)

    label("loc_232C")

    TalkEnd(0xFE)
    Return()

    # Function_9_15C5 end

    def Function_10_2330(): pass

    label("Function_10_2330")


    #C0067
    ChrTalk(
        0x9,
        (
            "#3700F啊……\x01",
            "各位是来找我先生的吧。\x02\x03",

            "抱歉，\x01",
            "哈罗德出门了，还没回来。\x02\x03",

            "有什么事的话可以告诉我，\x01",
            "等他回来了我会转告他。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0005F哎？那个……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0069
    ChrTalk(
        0x9,
        (
            "#3700F啊，对不起。\x01",
            "各位不是我先生的顾客吗……？\x02\x03",

            "呵呵……对哦。\x01",
            "各位这么年轻，\x01",
            "做生意有点太早了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#0100F您丈夫好像在\x01",
            "做与贸易有关的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "#3700F嗯，他是贸易商。\x01",
            "虽然生意规模不大。\x02\x03",

            "对不起啊，我弄错了。\x02\x03",

            "不过，如果有什么需要，\x01",
            "随时都可以来找我，\x01",
            "我或许能帮上点忙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 5)
    Return()

    # Function_10_2330 end

    def Function_11_24F7(): pass

    label("Function_11_24F7")


    #C0072
    ChrTalk(
        0x9,
        (
            "#3700F抱歉啊，\x01",
            "我明天有点事。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xE,
        "啊，明天是去教堂的日子吧。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xE,
        (
            "您每周\x01",
            "都会参加弥撒吧，\x01",
            "真是厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "#3708F不，这个……\x01",
            "您太过誉了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_24F7 end

    def Function_12_258D(): pass

    label("Function_12_258D")


    #C0076
    ChrTalk(
        0x9,
        (
            "#3700F柯林，别乱动啊……\x01",
            "不然外套就穿不上了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "#3800F嘿嘿，\x01",
            "我想吃冰激凌！\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#3700F好好好，冰激凌。\x01",
            "那我们找一找\x01",
            "冰激凌店吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        "#3800F嗯，去找去找～！\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_12_258D end

    def Function_13_2636(): pass

    label("Function_13_2636")


    #C0080
    ChrTalk(
        0xE,
        (
            "昨天我遇到了\x01",
            "库雷优夫人的丈夫了……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xE,
        (
            "不知为何，他最近的样子\x01",
            "好像有点奇怪呢。\x01",
            "怎么说呢，变得非常傲慢自大……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0082
    ChrTalk(
        0xF,
        "啊……真的吗？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xF,
        "嗯，这么说来……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xF,
        (
            "最近好像有听到他讲\x01",
            "粗话，也好像没有……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0085
    ChrTalk(
        0xE,
        "到、到底是有还是没有啊～？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "#3700F呵呵……库雷优总是\x01",
            "那么悠闲。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_13_2636 end

    def Function_14_279D(): pass

    label("Function_14_279D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2831")
    Jump("loc_287B")

    label("loc_2831")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2851")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_287B")

    label("loc_2851")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2871")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_287B")

    label("loc_2871")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_287B")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_28EB")

    #C0087
    ChrTalk(
        0xC,
        (
            "#3700F各位，有空再来啊。\x01",
            "我随时都会端出美食招待各位的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B6")

    label("loc_28EB")


    #C0088
    ChrTalk(
        0xC,
        (
            "#3700F啊，各位……\x02\x03",

            "不嫌弃的话，留下来一起用餐吧？\x01",
            "我做了很多哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#0000F哈哈哈，\x01",
            "今天还有点事……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x153,
        "#1110F下次吧！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        (
            "#3700F呵呵……这样啊，\x01",
            "那下次再来哦。\x01",
            "（是罗伊德警官的妹妹吗……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_29B6")

    SetChrSubChip(0xC, 0x0)
    TalkEnd(0xC)
    Return()

    # Function_14_279D end

    def Function_15_29BE(): pass

    label("Function_15_29BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A61")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29FC")
    Call(0, 19)
    Jump("loc_2A5C")

    label("loc_29FC")


    #C0092
    ChrTalk(
        0xA,
        (
            "#3800F那只小猫呀，经常\x01",
            "在围墙上走哦。\x02\x03",

            "#3809F我要是在窗户边看它的话，\x01",
            "它就会很快地跑过去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5C")

    Jump("loc_32D1")

    label("loc_2A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2AC9")

    #C0093
    ChrTalk(
        0xA,
        (
            "#3800F妈妈说她晚上\x01",
            "要在邻居家过夜。\x02\x03",

            "#3809F嘿嘿，所以爸爸\x01",
            "会代替妈妈，陪我一起睡哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D1")

    label("loc_2AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B0D")

    #C0094
    ChrTalk(
        0xA,
        (
            "#3800F妈妈说她要出去一会～\x02\x03",

            "不知道她去哪里了呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D1")

    label("loc_2B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2B53")

    #C0095
    ChrTalk(
        0xA,
        (
            "#3800F嘿嘿嘿，我在模仿\x01",
            "爸爸偷吃时的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDD")

    label("loc_2B53")


    #C0096
    ChrTalk(
        0xA,
        (
            "#3800F嘿嘿，爸爸\x01",
            "总是这样做哦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x59, 0x1F4)

    #C0097
    ChrTalk(
        0xA,
        (
            "#3800F『啊，这看起来很美味哦。\x01",
            "  索菲亚，我吃一个啊～』\x02\x03",

            "（偷偷拿一个，嚼嚼嚼）……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2BDD")

    Jump("loc_32D1")

    label("loc_2BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2C37")

    #C0098
    ChrTalk(
        0xA,
        (
            "#3800F今天我给妈妈帮忙了。\x02\x03",

            "我长大以后也要\x01",
            "像爸爸一样当一个商人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D1")

    label("loc_2C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2E1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 1)), scpexpr(EXPR_END)), "loc_2CB5")

    #C0099
    ChrTalk(
        0xA,
        (
            "#3800F我今天都要\x01",
            "跟妈妈在一起。\x02\x03",

            "#3809F哥哥姐姐们，\x01",
            "昨天谢谢你们了。\x02\x03",

            "也帮我跟那位姐姐\x01",
            "问声好啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_2CB5")


    #C0100
    ChrTalk(
        0xA,
        (
            "#3800F啊，是昨天\x01",
            "的哥哥姐姐们！\x02\x03",

            "告诉你们哦，妈妈今天\x01",
            "要和我一起看书哦。\x02\x03",

            "不过，我想去\x01",
            "外面玩……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，这小鬼还是\x01",
            "那么调皮啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#0000F柯林，别让\x01",
            "妈妈太担心你哦。\x02\x03",

            "昨天要不是那位姐姐\x01",
            "及时赶到的话，\x01",
            "你可就很危险了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "#3805F嗯……我知道了。\x01",
            "我今天都要跟妈妈在一起。\x02\x03",

            "#3809F哥哥姐姐们，谢谢你们。\x01",
            "也帮我跟那位姐姐问声好啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 1)

    label("loc_2E15")

    Jump("loc_32D1")

    label("loc_2E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2E82")

    #C0104
    ChrTalk(
        0xA,
        (
            "#3800F我去求爸爸妈妈了，\x01",
            "他们答应带我去看游行！\x02\x03",

            "#3809F太棒了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_32D1")

    label("loc_2E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2F1D")

    #C0105
    ChrTalk(
        0xA,
        (
            "#3800F嘿嘿，我昨天\x01",
            "遇到了一个外国人。\x02\x03",

            "他说在\x01",
            "港口那边\x01",
            "有很好玩的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0106
    ChrTalk(
        0xA,
        (
            "#3800F不知道是什么呢，\x01",
            "我真想去看看！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D1")

    label("loc_2F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2F36")
    OP_4B(0x9, 0xFF)
    Call(0, 12)
    OP_4C(0x9, 0xFF)
    Jump("loc_32D1")

    label("loc_2F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2F7F")

    #C0107
    ChrTalk(
        0xA,
        (
            "#3800F浇水，浇水……\x02\x03",

            "早上呀，我忘记\x01",
            "给花儿们浇水了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D1")

    label("loc_2F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_306E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3011")

    #C0108
    ChrTalk(
        0xA,
        (
            "#3800F如果我表现好的话……\x01",
            "纪念庆典的时候，爸爸应该会陪我\x01",
            "一起去玩吧。\x02\x03",

            "嗯，那我要好好表现！\x01",
            "然后和爸爸妈妈一起去玩！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3069")

    label("loc_3011")


    #C0109
    ChrTalk(
        0xA,
        (
            "#3800F爸爸今天也要工作。\x02\x03",

            "嗯……\x02\x03",

            "纪念庆典的时候，不知道\x01",
            "他能不能陪我一起去玩。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3069")

    Jump("loc_32D1")

    label("loc_306E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_30DC")

    #C0110
    ChrTalk(
        0xA,
        (
            "#3800F那个那个，今天\x01",
            "是烹饪教室上课的日子哦！\x02\x03",

            "#3809F非常开心哦。\x02\x03",

            "我也给\x01",
            "妈妈她们帮忙了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D1")

    label("loc_30DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3125")

    #C0111
    ChrTalk(
        0xA,
        (
            "#3800F嘿嘿，告诉你们哦……\x02\x03",

            "我也帮妈妈\x01",
            "做料理了哦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D1")

    label("loc_3125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_31D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_318C")

    #C0112
    ChrTalk(
        0xA,
        (
            "#3800F咦，我感觉\x01",
            "爸爸好像回来了！\x02\x03",

            "因为呀～我听到爸爸\x01",
            "车子的声音了哦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31CC")

    label("loc_318C")


    #C0113
    ChrTalk(
        0xA,
        (
            "#3800F希望爸爸能\x01",
            "快点上来啊～\x02\x03",

            "嘿嘿，因为我想\x01",
            "吓他一大跳。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31CC")

    Jump("loc_32D1")

    label("loc_31D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_322A")

    #C0114
    ChrTalk(
        0xA,
        (
            "#3800F今天呢，\x01",
            "爸爸出门前\x01",
            "亲了我一下哦～\x02\x03",

            "嘿嘿，还好我\x01",
            "早早就起床了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D1")

    label("loc_322A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_327F")

    #C0115
    ChrTalk(
        0xA,
        (
            "#3800F告诉你们哦，\x01",
            "爸爸是\x01",
            "贸易商人哦。\x02\x03",

            "每天早上都\x01",
            "很早就出门了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D1")

    label("loc_327F")


    #C0116
    ChrTalk(
        0xA,
        (
            "#3800F嗒啦啦，啦啦啦～嗯¤\x01",
            "今天我要画画玩！\x02\x03",

            "哥哥姐姐们也来\x01",
            "跟我一起玩吧～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D1")

    TalkEnd(0xFE)
    Return()

    # Function_15_29BE end

    def Function_16_32D5(): pass

    label("Function_16_32D5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3369")
    Jump("loc_33B3")

    label("loc_3369")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3389")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33B3")

    label("loc_3389")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33A9")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33B3")

    label("loc_33A9")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33B3")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3436")

    #C0117
    ChrTalk(
        0xD,
        (
            "#3809F姐姐的头发很柔软哦～！\x02\x03",

            "#3800F有空再来玩哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x153,
        "#1109F嗯，再见啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3902")

    label("loc_3436")

    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x153, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34CA")
    Jump("loc_3514")

    label("loc_34CA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34EA")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3514")

    label("loc_34EA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_350A")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3514")

    label("loc_350A")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3514")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)

    #C0119
    ChrTalk(
        0xD,
        (
            "#3805F咦…………？\x02\x03",

            "姐姐，你是谁啊～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)

    #C0120
    ChrTalk(
        0x153,
        (
            "#1111F……姐姐………？\x02\x03",

            "#1110F我说，罗伊德，\x01",
            "琪雅是姐姐吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    #C0121
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……在柯林眼里，\x01",
            "琪雅就是姐姐啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36EC")

    #C0122
    ChrTalk(
        0x153,
        (
            "#1108F这样啊。\x02\x03",

            "#1111F那在艾莉眼里，\x01",
            "罗伊德是弟弟？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C0123
    ChrTalk(
        0x102,
        (
            "#0112F那、那个……\x01",
            "（确实有点像\x01",
            "  弟弟……)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0124
    ChrTalk(
        0x101,
        "#0006F绝对不是。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        "#0108F（……是吗……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_36EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37FE")

    #C0126
    ChrTalk(
        0x153,
        (
            "#1108F这样啊。\x02\x03",

            "#1111F那在罗伊德眼里，\x01",
            "缇欧是妹妹？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x103, 0x153, 500)

    #C0127
    ChrTalk(
        0x103,
        "#0203F……嗯，应该没错。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0128
    ChrTalk(
        0x101,
        (
            "#0006F不，不是吧。\x01",
            "缇欧，你得否认啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0129
    ChrTalk(
        0x103,
        (
            "#0211F只是想偶尔调侃一下，\x01",
            "请不要那么煞风景。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_37FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38FF")

    #C0130
    ChrTalk(
        0x153,
        (
            "#1108F这样啊。\x02\x03",

            "#1111F那在兰迪眼里，\x01",
            "罗伊德是弟弟？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)

    #C0131
    ChrTalk(
        0x104,
        (
            "#0309F啊，有些方面确实很像呢～\x02\x03",

            "#0306F比如明明很年轻，\x01",
            "但却很固执、爱逞强……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0132
    ChrTalk(
        0x101,
        "#0006F兰迪，你又在装成熟了……\x02",
    )

    CloseMessageWindow()

    label("loc_38FF")

    SetScenarioFlags(0x0, 2)

    label("loc_3902")

    SetChrSubChip(0xD, 0x0)
    TalkEnd(0xD)
    Return()

    # Function_16_32D5 end

    def Function_17_390A(): pass

    label("Function_17_390A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_39B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3995")
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0133
    ChrTalk(
        0xE,
        (
            "库雷优夫人，怎么说呢……\x01",
            "好像有点迟钝……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xE,
        (
            "嗯，不过没关系。\x01",
            "反正她那么可爱。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39AD")

    label("loc_3995")

    OP_4B(0x9, 0xFF)
    OP_4B(0xF, 0xFF)
    Call(0, 13)
    OP_4C(0x9, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xE, 0x10)

    label("loc_39AD")

    Jump("loc_3A02")

    label("loc_39B2")

    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_39FB")

    #C0135
    ChrTalk(
        0xE,
        "啊，我帮忙装盘吧～\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xE,
        (
            "嘿嘿，我就\x01",
            "喜欢这种工作⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FE")

    label("loc_39FB")

    Call(0, 11)

    label("loc_39FE")

    OP_4C(0x9, 0xFF)

    label("loc_3A02")

    TalkEnd(0xFE)
    Return()

    # Function_17_390A end

    def Function_18_3A06(): pass

    label("Function_18_3A06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A7B")
    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3A66")

    #C0137
    ChrTalk(
        0xF,
        (
            "嗯、嗯……\x01",
            "说起来，最近\x01",
            "总觉得他……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xF,
        "……有点奇怪～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A6E")

    label("loc_3A66")

    Call(0, 13)
    ClearChrFlags(0xE, 0x10)

    label("loc_3A6E")

    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_3B47")

    label("loc_3A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3AE1")

    #C0139
    ChrTalk(
        0xF,
        (
            "烹饪教室的课程结束之后，\x01",
            "大家总会一起吃饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xF,
        (
            "呵呵，今天好像也\x01",
            "会聊得很愉快啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B47")

    label("loc_3AE1")


    #C0141
    ChrTalk(
        0xF,
        (
            "今天的烹饪教室\x01",
            "教的是帝国风味的\x01",
            "炖三文鱼。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xF,
        (
            "呵呵，能和朋友们聚在一起\x01",
            "做料理，真是开心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3B47")

    TalkEnd(0xFE)
    Return()

    # Function_18_3A06 end

    def Function_19_3B4B(): pass

    label("Function_19_3B4B")

    EventBegin(0x0)
    Fade(800)
    OP_4B(0xA, 0xFF)
    OP_68(36520, 1500, 4730, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(270, 0)
    SetCameraDistance(30020, 0)
    SetChrPos(0x101, 36580, 0, 5220, 180)
    SetChrPos(0x102, 37720, 0, 5220, 180)
    SetChrPos(0x103, 36580, 0, 6620, 180)
    SetChrPos(0x104, 37720, 0, 6620, 180)
    SetChrPos(0xA, 37190, 0, 3550, 0)
    OP_0D()

    #C0143
    ChrTalk(
        0x101,
        (
            "#5P#0000F打扰一下哦。\x02\x03",

            "你有没有\x01",
            "养小猫呢？\x01",
            "或者说，知不知道有谁在养？\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "#12P#3805F小猫咪……？\x01",
            "什么样的小猫咪啊～？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#5P#0000F嗯，就是这一只……\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0146
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德从外套里\x01",
            "抱出小猫给对方看。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Sound(823, 0, 100, 0)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    #C0147
    ChrTalk(
        0xA,
        "#12P#3805F啊，我见过！\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        "#5P#0105F真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xA,
        (
            "#12P#3800F嗯，我时常看到它\x01",
            "在围墙上走哦。\x02\x03",

            "说起来，最近\x01",
            "都没怎么见过了……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        (
            "#5P#0303F唔，这只猫\x01",
            "好像就是这附近的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x103,
        (
            "#5P#0200F那它的主人\x01",
            "住在住宅街的可能性很高呢，\x01",
            "我们去找找吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#5P#0000F谢谢啊，你帮大忙了哦。\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xA,
        (
            "#12P#3809F嗯，哥哥姐姐们，\x01",
            "再见呀！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 37320, 0, 5200, 180)
    BeginChrThread(0xA, 0, 0, 1)
    OP_29(0x8, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_19_3B4B end

    SaveToFile()

Try(main)
