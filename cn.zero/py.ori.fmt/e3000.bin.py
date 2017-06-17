from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "e3000.bin",                # FileName
        "e3000",                    # MapName
        "e3000",                    # Location
        0x00A1,                     # MapIndex
        "ed7104",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 2, 0, 3],
    )

    BuildStringList((
        "e3000",                  # 0
        "雷克特",                 # 1
        "男孩",                   # 2
        "男性",                   # 3
        "女性",                   # 4
        "游客",                   # 5
        "SE控制",                 # 6
    ))

    AddCharChip((
        "chr/ch07400.itc",                   # 00
        "chr/ch20602.itc",                   # 01
        "chr/ch20202.itc",                   # 02
        "chr/ch20302.itc",                   # 03
        "chr/ch21600.itc",                   # 04
        "apl/ch50352.itc",                   # 05
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

    DeclNpc(2950,    4099,    -7750,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-1169,   4250,    899,     180,  341,  0x0, 0,   1,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(1029,    4250,    899,     180,  341,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(2210,    4250,    899,     180,  341,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       4099,    12760,   0,    257,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_285",          # 01, 1
        "Function_2_2A5",          # 02, 2
        "Function_3_2CB",          # 03, 3
        "Function_4_2E3",          # 04, 4
        "Function_5_2F2",          # 05, 5
        "Function_6_4B9",          # 06, 6
        "Function_7_644",          # 07, 7
        "Function_8_82E",          # 08, 8
        "Function_9_9A4",          # 09, 9
        "Function_10_A43",         # 0A, 10
        "Function_11_BD1",         # 0B, 11
        "Function_12_1D3B",        # 0C, 12
        "Function_13_1D5C",        # 0D, 13
        "Function_14_1D7D",        # 0E, 14
    ))


    def Function_0_1F0(): pass

    label("Function_0_1F0")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_213")
    Sleep(600)
    Jump("loc_23C")

    label("loc_213")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22A")
    Sleep(400)
    Jump("loc_23C")

    label("loc_22A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23C")
    Sleep(200)

    label("loc_23C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_284")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Jump("loc_23C")

    label("loc_284")

    Return()

    # Function_0_1F0 end

    def Function_1_285(): pass

    label("Function_1_285")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A4")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1)
    Jump("Function_1_285")

    label("loc_2A4")

    Return()

    # Function_1_285 end

    def Function_2_2A5(): pass

    label("Function_2_2A5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BB")
    Event(0, 14)

    label("loc_2BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_2CA")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 10)

    label("loc_2CA")

    Return()

    # Function_2_2A5 end

    def Function_3_2CB(): pass

    label("Function_3_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC")
    Call(0, 4)

    label("loc_2DC")

    Sound(479, 1, 100, 0)
    Return()

    # Function_3_2CB end

    def Function_4_2E3(): pass

    label("Function_4_2E3")

    SetChrChipByIndex(0x8, 0x5)
    SetChrSubChip(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 1)
    Return()

    # Function_4_2E3 end

    def Function_5_2F2(): pass

    label("Function_5_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_308")
    Call(0, 11)
    Jump("loc_4B8")

    label("loc_308")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_475")

    #C0001
    ChrTalk(
        0x8,
        (
            "#3506F话说回来，那个老头子\x01",
            "只和我说过代理出席\x01",
            "竞拍会这件事而已。\x02\x03",

            "#3500F要是知道有什么\x01",
            "主题公园，我肯定\x01",
            "一大早就会来克洛斯贝尔了～\x02",
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

    #C0002
    ChrTalk(
        0x101,
        "#0012F骨子里就是个游手好闲的公子哥呢……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#3504F唔，这说法真是没礼貌啊。\x01",
            "我只是忠于自己的欲望而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4B5")

    label("loc_475")


    #C0004
    ChrTalk(
        0x8,
        (
            "#3510F等到靠岸之后，\x01",
            "我马上就去传说中的\x01",
            "那个主题公园看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B5")

    TalkEnd(0x8)

    label("loc_4B8")

    Return()

    # Function_5_2F2 end

    def Function_6_4B9(): pass

    label("Function_6_4B9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_54D")
    Jump("loc_597")

    label("loc_54D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_597")

    label("loc_56D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_597")

    label("loc_58D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_597")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_618")

    #C0005
    ChrTalk(
        0xFE,
        (
            "哇～哇～这就是水上巴士啊！\x01",
            "好快，好快～呀！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_613")
    SetScenarioFlags(0xB6, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_613")

    Jump("loc_63C")

    label("loc_618")


    #C0006
    ChrTalk(
        0xFE,
        "还要多久才能到达米修拉姆呢～？\x02",
    )

    CloseMessageWindow()

    label("loc_63C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_4B9 end

    def Function_7_644(): pass

    label("Function_7_644")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6D8")
    Jump("loc_722")

    label("loc_6D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6F8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_722")

    label("loc_6F8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_718")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_722")

    label("loc_718")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_722")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EA")

    #C0007
    ChrTalk(
        0xFE,
        (
            "纪念庆典期间虽然很忙，\x01",
            "但总算是挤出了一些陪伴家人的时间啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "今天我们全家准备游玩一天，\x01",
            "好好享受一下天伦之乐。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E5")
    SetScenarioFlags(0xB6, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E5")

    Jump("loc_826")

    label("loc_7EA")


    #C0009
    ChrTalk(
        0xFE,
        (
            "今天打算暂时忘记工作，\x01",
            "好好享受一下\x01",
            "和家人团聚的快乐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_826")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_644 end

    def Function_8_82E(): pass

    label("Function_8_82E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C2")
    Jump("loc_90C")

    label("loc_8C2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8E2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90C")

    label("loc_8E2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_902")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90C")

    label("loc_902")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_90C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0010
    ChrTalk(
        0xFE,
        (
            "老公能抽出时间来陪儿子，\x01",
            "我也很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "希望能给这孩子\x01",
            "留下愉快的回忆。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99C")
    SetScenarioFlags(0xB6, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_99C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_82E end

    def Function_9_9A4(): pass

    label("Function_9_9A4")

    TalkBegin(0xFE)

    #C0012
    ChrTalk(
        0xFE,
        (
            "听说米修拉姆有个\x01",
            "很高级的西餐厅呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "不断寻找、品尝美食是我多年的兴趣……\x01",
            "希望在克洛斯贝尔也能发现\x01",
            "一些美味的料理啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3F")
    SetScenarioFlags(0xB6, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A3F")

    TalkEnd(0xFE)
    Return()

    # Function_9_9A4 end

    def Function_10_A43(): pass

    label("Function_10_A43")

    EventBegin(0x0)
    OP_E5()
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    Call(0, 4)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B09")
    FadeToBright(1000, 0)
    OP_68(80, 2300, -22430, 0)
    MoveCamera(11, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(85880, 0)
    OP_68(570, 2300, 64420, 18000)
    SetCameraDistance(45950, 13500)
    MoveCamera(11, 16, 0, 13500)
    Sleep(12000)
    OP_0D()

    label("loc_B09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B5C")
    Fade(2000)
    OP_68(60, 4500, -16129, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25520, 0)
    OP_68(60, 4500, 20650, 15000)
    Sleep(12000)
    OP_0D()

    label("loc_B5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB8")
    Fade(2000)
    OP_68(-5400, 4500, -20850, 0)
    MoveCamera(152, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29350, 0)
    OP_68(-5400, 4500, 49430, 15000)
    SetCameraDistance(69180, 9000)
    Sleep(12000)
    OP_0D()

    label("loc_BB8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("e0510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_A43 end

    def Function_11_BD1(): pass

    label("Function_11_BD1")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("apl/ch50351.itc", 0x1E)
    SetCameraDistance(18440, 0)
    OP_68(2260, 5800, -6790, 0)
    MoveCamera(136, 20, 0, 0)
    OP_6E(500, 0)
    SetChrPos(0x101, 2350, 4100, -6500, 180)
    SetChrPos(0x102, 3550, 4100, -6500, 180)
    SetChrPos(0x103, 2350, 4100, -5500, 180)
    SetChrPos(0x104, 3550, 4100, -5500, 180)
    SetChrPos(0x8, 2950, 4100, -8150, 0)
    FadeToBright(1000, 0)
    StopBGM(0xBB8)
    BeginChrThread(0xD, 0, 0, 12)
    SetCameraDistance(16940, 3000)
    OP_6F(0x10)
    OP_0D()
    EndChrThread(0xD, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7525", 1)

    #C0014
    ChrTalk(
        0x8,
        (
            "#3509F#11P#0W#67A在前方等待着我们的，\x01",
            "是一座美丽的乐园～¤\x02\x03",

            "#67A来啊，让我们手拉着手，\x01",
            "一同乘风破浪～¤\x02\x03",

            "#3510F#48A乘着白色小船，向着那座岛屿进发～¤\x02\x03",

            "#46A麦色的肌肤充满魅力～¤\x02\x03",

            "#42A遮阳伞、椰树，还有刨冰～¤\x02\x03",

            "#3504F#60A有你所在的地方，\x01",
            "就是我的乐园～¤\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    BeginChrThread(0xD, 0, 0, 13)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x20)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x3E8)
    EndChrThread(0xD, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7104", 0)

    #C0015
    ChrTalk(
        0x101,
        (
            "#0012F#6P总觉得……\x01",
            "他好像十分陶醉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#0306F#6P不过，演奏技术虽然意外地高明，\x01",
            "却反而让人觉得更☆不爽呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#3507F#11P噢，青春就是需要爆发啊。\x02\x03",

            "#3509F在旅途中歌唱演奏，\x01",
            "可并不是某位皇子\x01",
            "独有的专利哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        "#0211F#6P完全不明白你在说什么……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#0100F#5P那个，雷克特先生\x01",
            "去米修拉姆有什么事情呢？\x02\x03",

            "看起来，你似乎并不是\x01",
            "为了主题公园而来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#3503F#11P是啊～正如刚才所说，\x01",
            "我只是以代理人的身份而来的啊。\x02\x03",

            "#3501F代替那个讨厌的\x01",
            "狡猾大叔啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#0005F#6P狡猾大叔……？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "#3501F#11P嗯～我想你们应该\x01",
            "听说过他的名字吧？\x02\x03",

            "一位名叫吉利亚斯·奥斯本\x01",
            "的狡猾大叔。\x02",
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0023
    ChrTalk(
        0x101,
        "#0011F#6P#4S哎！？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#3505F#11P啊～果然知道啊。\x02\x03",

            "#3506F那位大叔也就是外表看上去\x01",
            "还算风度翩翩啦。\x02\x03",

            "总是精心修剪自己那把小胡子，\x01",
            "莫非是想装成一名与蔷薇相配的\x01",
            "魅力美中年吗～\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#0001F#6P埃雷波尼亚帝国的宰相，\x01",
            "吉利亚斯·奥斯本……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        "#0203F#6P……人称『铁血宰相』啊。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#0101F#5P难、难道……\x01",
            "你是帝国政府方面的人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#3504F#11P呵，我不过只是个二等书记官而已。\x02\x03",

            "#3500F克洛斯贝尔的领袖人物之中，\x01",
            "好像有个叫哈尔特曼的大叔吧？\x02\x03",

            "那家伙去年曾和吉利亚斯大叔进行过一次极其\x01",
            "机密的会谈……虽说是机密，但这事早已经闹得\x01",
            "众所周知了……总之，两人借此建立了秘密联系。\x02\x03",

            "正是为了加深这种联系，\x01",
            "他才会派我前来。\x02\x03",

            "#3506F哎呀～在政府部门工作可真够累人的。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0003F#6P是、是这样啊……\x02\x03",

            "#0005F不过，连这种事情都告诉我们，\x01",
            "真的不要紧吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#3500F#11P哈，当然不要紧啊。\x02\x03",

            "#3509F反正你们全部\x01",
            "都要葬身于此。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x0, 0x7D0)
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

    #C0031
    ChrTalk(
        0x101,
        "#0007F#6P什么──\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        "#0301F#6P你这家伙……\x02",
    )

    CloseMessageWindow()
    OP_68(2380, 5800, -6400, 1200)

    def lambda_14CE():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14CE)
    Sleep(50)

    def lambda_14E6():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14E6)
    Sleep(100)

    def lambda_14FE():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14FE)
    Sleep(50)

    def lambda_1516():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1516)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0033
    ChrTalk(
        0x8,
        (
            "#3504F#11P你们觉得，在这辆水上巴士里\x01",
            "一共埋伏着多少名\x01",
            "我的部下呢……？\x02\x03",

            "#3500F恐怕你们数\x01",
            "都数不过来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        "#0101F#5P唔，你究竟有何目的……！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        "#0208F#6P……是陷阱吗？\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        "#3504F#11P呵呵……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    VolumeBGM(0x64, 0xBB8)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0037
    ChrTalk(
        0x8,
        (
            "#3509F#4S#11P哇哈哈哈哈哈哈哈哈！\x02\x03",

            "#3504F呵呵……\x01",
            "呀哈哈～很不错的反应哦。\x02\x03",

            "#3502F竟然这么容易就上当，\x01",
            "你们还真是够纯朴啊！\x02",
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

    #C0038
    ChrTalk(
        0x101,
        "#0011F#6P莫非……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#0301F#6P……刚才那都是在演戏吗？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#3509F#11P哎呀～该怎么说呢～\x02\x03",

            "我来克洛斯贝尔时，在列车上\x01",
            "读的那本谍战小说中有这样的情节，\x01",
            "所以刚才就照搬照抄地说出来了。\x02\x03",

            "不过，你们居然会有那么精彩的反应，\x01",
            "这倒是真有点出乎本少爷的预料～\x02\x03",

            "#3502F该不会是出于礼貌，\x01",
            "而在故意配合我吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#0012F#6P哎，那个，哈哈。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#0106F#5P……你的演技实在是太逼真了，\x01",
            "我们不由自主就中了圈套。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#3504F#11P哈哈，看你们的反应那么强烈，\x01",
            "我甚至都以为你们是要潜入\x01",
            "『竞拍会』进行调查的警察呢……\x02\x03",

            "#3500F不过，像这种典型的谍战小说式情节，\x01",
            "再怎么说，也不会轻易被我遇见吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#0012F#6P呃……哈哈哈。\x01",
            "是啊，怎么可能会有那种事嘛。\x02\x03",

            "#0005F对了，那……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#0201F#6P那么，你也要出席\x01",
            "那个『竞拍会』吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#3504F#11P嗯，正是如此。\x02\x03",

            "#3505F顺便一说，刚才我自称是铁血宰相\x01",
            "的代理人，那也只是在开玩笑而已哦。\x02\x03",

            "#3500F其实我只是某个\x01",
            "帝国贵族家庭的少爷。\x02\x03",

            "这次是准备代替无暇分身的老爸\x01",
            "来出席那个『竞拍会』的。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#0103F#5P……是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0300F#6P抱歉，说句实话，看你这身打扮，\x01",
            "实在是不像什么帝国贵族的公子哥啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#3505F#11P喂喂，你这家伙真是失礼啊～\x02\x03",

            "#3504F两位小姐也就算了，\x01",
            "你们这两个臭男人看起来\x01",
            "也不像是什么有钱少爷吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#0006F#6P呜……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        "#0309F#6P哈哈，说得倒没错。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        (
            "#0104F#5P……不过，\x01",
            "我们也是有邀请卡的。\x02\x03",

            "#0100F或许还能在会场中\x01",
            "再次碰面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#3500F#11P……呵呵。\x02\x03",

            "#3504F算了，你们也挺有趣的，\x01",
            "如果看到我的话，记得来打声招呼哦。\x02\x03",

            "总是和那些大叔打交道，\x01",
            "会把我烦死的。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#0003F#6P……明白了。\x02\x03",

            "#0000F那么，如果有机会，\x01",
            "今晚在会场再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        "#3509F#11P噢，到时多指教啦～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetCameraDistance(17190, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x20)
    OP_49()
    OP_D5(0x1E)
    SetChrPos(0x0, 2780, 4100, -6430, 180)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x8, 2950, 4100, -7750, 180)
    SetScenarioFlags(0xA3, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_BD1 end

    def Function_12_1D3B(): pass

    label("Function_12_1D3B")

    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Return()

    # Function_12_1D3B end

    def Function_13_1D5C(): pass

    label("Function_13_1D5C")

    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x64)
    Return()

    # Function_13_1D5C end

    def Function_14_1D7D(): pass

    label("Function_14_1D7D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Sound(801, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──让您久等了。\x02",
        )
    )

    CloseMessageWindow()

    #A0057
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本水上巴士即将\x01",
            "到达『米修拉姆』。\x02",
        )
    )

    CloseMessageWindow()

    #A0058
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请各位乘客不要丢失随身物品，\x01",
            "注意安全，小心下船。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_25(0x1DF, 0x0)
    WaitBGM()
    SetScenarioFlags(0x5C, 0)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1D7D end

    SaveToFile()

Try(main)
