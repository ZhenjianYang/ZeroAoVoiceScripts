from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "e0510.bin",                # FileName
        "e0510",                    # MapName
        "e0510",                    # Location
        0x00A1,                     # MapIndex
        "ed7104",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0510",                  # 0
        "雾香",                   # 1
        "乘务员萨尔莎",           # 2
        "少女",                   # 3
        "青年",                   # 4
        "男性",                   # 5
        "青年",                   # 6
        "游客",                   # 7
    ))

    AddCharChip((
        "chr/ch07302.itc",                   # 00
        "chr/ch28400.itc",                   # 01
        "chr/ch21302.itc",                   # 02
        "chr/ch21202.itc",                   # 03
        "chr/ch27702.itc",                   # 04
        "chr/ch23602.itc",                   # 05
        "chr/ch26702.itc",                   # 06
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

    DeclNpc(0,       -899,    7349,    0,    341,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(-100,    0,       -15420,  0,    257,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-3660,   150,     -8829,   180,  341,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(-2450,   150,     -8829,   180,  341,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(3049,    150,     -6349,   180,  341,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-2450,   150,     -3799,   180,  341,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(2180,    150,     -8829,   180,  341,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)

    ScpFunction((
        "Function_0_204",          # 00, 0
        "Function_1_299",          # 01, 1
        "Function_2_2BF",          # 02, 2
        "Function_3_2C6",          # 03, 3
        "Function_4_541",          # 04, 4
        "Function_5_64D",          # 05, 5
        "Function_6_81B",          # 06, 6
        "Function_7_9F0",          # 07, 7
        "Function_8_B4D",          # 08, 8
        "Function_9_D4F",          # 09, 9
        "Function_10_EF0",         # 0A, 10
        "Function_11_11B8",        # 0B, 11
        "Function_12_1DF8",        # 0C, 12
    ))


    def Function_0_204(): pass

    label("Function_0_204")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_227")
    Sleep(600)
    Jump("loc_250")

    label("loc_227")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23E")
    Sleep(400)
    Jump("loc_250")

    label("loc_23E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_250")
    Sleep(200)

    label("loc_250")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_298")
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
    Jump("loc_250")

    label("loc_298")

    Return()

    # Function_0_204 end

    def Function_1_299(): pass

    label("Function_1_299")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AF")
    Event(0, 12)

    label("loc_2AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_2BE")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 10)

    label("loc_2BE")

    Return()

    # Function_1_299 end

    def Function_2_2BF(): pass

    label("Function_2_2BF")

    Sound(480, 1, 100, 0)
    Return()

    # Function_2_2BF end

    def Function_3_2C6(): pass

    label("Function_3_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC")
    Call(0, 11)
    Jump("loc_540")

    label("loc_2DC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_370")
    Jump("loc_3BA")

    label("loc_370")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_390")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BA")

    label("loc_390")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B0")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BA")

    label("loc_3B0")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BA")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_504")

    #C0001
    ChrTalk(
        0x8,
        (
            "#3404F呵呵，抱歉，突然说起了\x01",
            "难懂的话题呢。\x02\x03",

            "#3400F难得要去疗养地……\x01",
            "我虽然还有些琐事要处理，\x01",
            "但希望你们能尽情享受哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        "#0309F这个是当然的啦！\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        (
            "#0211F（……兰迪前辈，你难道忘了\x01",
            "  我们此行的目的吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x104,
        (
            "#0306F（我、我知道啦～\x01",
            "  别用那种目光看我啦，阿缇……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_539")

    label("loc_504")


    #C0005
    ChrTalk(
        0x8,
        (
            "#3400F难得要去疗养地……\x01",
            "希望你们能尽情享受哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_539")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)

    label("loc_540")

    Return()

    # Function_3_2C6 end

    def Function_4_541(): pass

    label("Function_4_541")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EE")

    #C0006
    ChrTalk(
        0xFE,
        (
            "客人，您是第一次\x01",
            "乘坐水上巴士吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "距离到达米修拉姆还需要一点时间，\x01",
            "请您先暂时享受一下这趟\x01",
            "在波涛中稳稳行进的旅途吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E9")
    SetScenarioFlags(0xB5, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E9")

    Jump("loc_649")

    label("loc_5EE")


    #C0008
    ChrTalk(
        0xFE,
        (
            "……莫非您\x01",
            "晕船了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "我们这里常备有止晕药，\x01",
            "如果感到不舒服，\x01",
            "请尽管向我们索要。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_649")

    TalkEnd(0xFE)
    Return()

    # Function_4_541 end

    def Function_5_64D(): pass

    label("Function_5_64D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E1")
    Jump("loc_72B")

    label("loc_6E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_701")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_72B")

    label("loc_701")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_721")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_72B")

    label("loc_721")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_72B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CE")

    #C0010
    ChrTalk(
        0xFE,
        "今天终于要去期待已久的米修拉姆了⊥\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "一定要去精品店和珠宝店\x01",
            "尽情购物一番⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C9")
    SetScenarioFlags(0xB5, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7C9")

    Jump("loc_813")

    label("loc_7CE")


    #C0012
    ChrTalk(
        0xFE,
        (
            "我的男朋友今天好像\x01",
            "带了很多米拉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "呵呵，要玩个痛快哦～⊥\x02",
    )

    CloseMessageWindow()

    label("loc_813")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_64D end

    def Function_6_81B(): pass

    label("Function_6_81B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8AF")
    Jump("loc_8F9")

    label("loc_8AF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8CF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F9")

    label("loc_8CF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F9")

    label("loc_8EF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A5")

    #C0014
    ChrTalk(
        0xFE,
        (
            "为了今天，我把所有\x01",
            "存款都拿出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "……必须要充分注意她那\x01",
            "铺张浪费的坏习惯啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A0")
    SetScenarioFlags(0xB5, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A0")

    Jump("loc_9E8")

    label("loc_9A5")


    #C0016
    ChrTalk(
        0xFE,
        "我的女朋友浪费成性。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "但愿她别把我这些储蓄\x01",
            "全部花光啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_81B end

    def Function_7_9F0(): pass

    label("Function_7_9F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE8")

    #C0018
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "为了今晚的拍卖会，\x01",
            "我追加了不少资金呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "因为超出预算，而没有拍到\x01",
            "中意商品的那份屈辱……\x01",
            "这次一定要彻底洗刷。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0001F（看起来，这个人好像也是\x01",
            "  被邀请至黑之竞拍会的\x01",
            "  客人呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE3")
    SetScenarioFlags(0xB5, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AE3")

    Jump("loc_B49")

    label("loc_AE8")


    #C0021
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "为了今晚的拍卖会，\x01",
            "我追加了不少资金呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "那些传闻中的商品……\x01",
            "我一定要弄到手。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B49")

    TalkEnd(0xFE)
    Return()

    # Function_7_9F0 end

    def Function_8_B4D(): pass

    label("Function_8_B4D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BE1")
    Jump("loc_C2B")

    label("loc_BE1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C01")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C2B")

    label("loc_C01")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C21")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C2B")

    label("loc_C21")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C2B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D14")

    #C0023
    ChrTalk(
        0xFE,
        (
            "我就是为了主题公园而来的。\x01",
            "随身带着宣传手册，可以说是准备万全了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "……一个男人独自去那里，也没什么\x01",
            "奇怪的吧？我纯粹就是想去\x01",
            "主题公园玩玩而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0F")
    SetScenarioFlags(0xB5, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D0F")

    Jump("loc_D47")

    label("loc_D14")


    #C0025
    ChrTalk(
        0xFE,
        (
            "……看什么？一个男人自己去\x01",
            "主题公园玩不行吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D47")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_B4D end

    def Function_9_D4F(): pass

    label("Function_9_D4F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DE3")
    Jump("loc_E2D")

    label("loc_DE3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E03")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E2D")

    label("loc_E03")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E23")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E2D")

    label("loc_E23")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E2D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0026
    ChrTalk(
        0xFE,
        (
            "我说，你们看见了吗？\x01",
            "坐在后边的那个美人……\x01",
            "她的那身打扮可真是绝妙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "哎呀，真是撩人心弦啊，\x01",
            "这次果然是来对了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE8")
    SetScenarioFlags(0xB5, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EE8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_D4F end

    def Function_10_EF0(): pass

    label("Function_10_EF0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x102, 3000, 150, -13830, 180)
    SetChrPos(0x101, 2120, 150, -13830, 180)
    SetChrPos(0x103, 3120, 150, -11330, 180)
    SetChrPos(0x104, 2120, 150, -11330, 180)
    OP_68(-600, 1100, -8060, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    OP_68(2560, 1100, -12450, 8000)
    OP_6F(0x1)
    OP_0D()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0028
    ChrTalk(
        0x101,
        (
            "#0000F#5P水上巴士吗……\x02\x03",

            "好像还是第一次乘坐，\x01",
            "内部装修可真够豪华的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)

    #C0029
    ChrTalk(
        0x102,
        (
            "#0104F#11P呵呵，和普通巴士不同，\x01",
            "这是完全由ＩＢＣ来运营的。\x02\x03",

            "#0102F乘船费用一般也都是免收的。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        "#0205F#5P还真是慷慨呢……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0304F#5P哈，不过，如果没有米拉，\x01",
            "就算到了目的地，也是什么都干不了啊。\x02\x03",

            "#0300F大概还有二十分钟左右才能到……\x01",
            "我们就适当放松一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetChrPos(0x0, -200, 0, -11700, 0)
    SetScenarioFlags(0xA3, 5)
    OP_29(0x44, 0x4, 0x10)
    OP_29(0x47, 0x4, 0x2)
    OP_29(0x47, 0x1, 0x0)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_EF0 end

    def Function_11_11B8(): pass

    label("Function_11_11B8")

    EventBegin(0x0)
    Fade(1000)
    OP_68(1260, 300, 7490, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18060, 0)
    SetCameraDistance(17060, 2000)
    SetChrPos(0x101, 1890, -1000, 8970, 225)
    SetChrPos(0x102, 2920, -1000, 8620, 225)
    SetChrPos(0x103, 2580, -1000, 7410, 270)
    SetChrPos(0x104, 3530, -1000, 7820, 270)
    SetChrSubChip(0x8, 0x2)
    OP_6F(0x10)
    OP_0D()

    #C0032
    ChrTalk(
        0x8,
        (
            "#3404F#6P米修拉姆……\x01",
            "真是个让人深感兴趣的地方呢。\x02\x03",

            "#3400F如果时间再充裕一点的话，\x01",
            "本来还想去主题公园看看呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0033
    ChrTalk(
        0x101,
        (
            "#0005F#5P那个……原来您不是\x01",
            "要去主题公园啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "#3404F#6P不是哦，因为还有些琐事要办呢。\x02\x03",

            "#3400F算了，反正这也不是\x01",
            "最后一次来克洛斯贝尔……\x02\x03",

            "等以后有机会再去慢慢玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        "#0109F#5P呵呵，请一定要再来啊。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#0300F#11P说起来……\x01",
            "您觉得彩虹剧团\x01",
            "的新剧怎么样呢？\x02\x03",

            "昨天应该去看过了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#3404F#6P嗯，看的是夜场。\x02\x03",

            "#3402F我也曾经欣赏过\x01",
            "各种各样的舞台演出……\x02\x03",

            "但也许从没见过\x01",
            "哪个舞台，\x01",
            "能保持着那种奇迹般的平衡感。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        "#0205F#11P奇迹般的平衡感吗……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#3400F#6P脚本、导演、服装、音乐……\x02\x03",

            "再加上豪华的舞台设备，\x01",
            "以及各种高难度的特技表演……\x02\x03",

            "虽然每一项的水准都非常高，\x01",
            "但与其它那些著名剧团相比，\x01",
            "倒也没有强到鹤立鸡群的程度。\x02\x03",

            "#3404F可是，伊莉娅·普拉提耶……\x02\x03",

            "当以她的存在为核心，\x01",
            "各个要素被有机结合到一起时，\x01",
            "舞台仿佛就变得有了生命一般呢。\x02\x03",

            "#3402F让我感觉，简直就像是\x01",
            "见证了一个生命的诞生啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#0002F#5P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#0104F#5P生命的诞生……\x01",
            "这确实可以算得上是奇迹吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#0309F#11P呀～！\x01",
            "真不愧是演艺界的制作人啊！\x02\x03",

            "听您这么一说，\x01",
            "感觉确实就是这么一回事呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#3404F#6P呵呵……\x02\x03",

            "只是，在这次的新剧中，\x01",
            "缔造奇迹的还另有人在哦。\x02\x03",

            "#3400F饰演『月之姬』的超级新星\x01",
            "——莉夏·毛。\x02\x03",

            "浑身散发着死亡气息的她，\x01",
            "使舞台表演的效果又上了一层楼。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0044
    ChrTalk(
        0x101,
        "#0005F#5P莉夏她……？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        "#0105F#5P死亡的气息……吗？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#3400F#6P这也只是我的直觉而已。\x02\x03",

            "#3404F太阳与月亮，金与银，光与暗，\x01",
            "还有生与死……\x02\x03",

            "她与伊莉娅·普拉提耶\x01",
            "形成了完美对照，\x01",
            "两个人拥有着截然相反的『气息』呢。\x02\x03",

            "#3400F可以说，在这两个人的身上，\x01",
            "体现出了『阴阳』和『太极』的规律呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        "#0205F#11P『阴阳』、『太极』……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0300F#11P好像是在东方武术中\x01",
            "所使用的概念吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#3400F#6P呵呵……\x01",
            "其实这些概念并不只限于武术。\x02\x03",

            "#3404F总之，她们两个人的相逢，\x01",
            "大概可以算是命中注定的偶然吧。\x02\x03",

            "而引导她们相逢的，\x01",
            "则是克洛斯贝尔这个都市\x01",
            "所拥有的『气场』的特异性……\x02\x03",

            "#3400F或许可以这样说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#0001F#5P引导命运的『气场』……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        (
            "#0103F#5P……虽然道理很复杂，\x01",
            "但感觉也能够理解呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#3404F#6P算了，也没有必要\x01",
            "那么认真地去思索哦。\x02\x03",

            "#3400F只是，彩虹剧团的魅力\x01",
            "与克洛斯贝尔这座都市\x01",
            "有着密不可分的联系。\x02\x03",

            "如果不解决这个问题，\x01",
            "在自治州以外地区的公演\x01",
            "恐怕就不会有这么完美了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        (
            "#0205F#11P那么，在共和国进行公演的计划，\x01",
            "您是准备就此取消吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#3402F#6P不，那样的话，未免也太遗憾了。\x02\x03",

            "想在克洛斯贝尔以外的地区\x01",
            "引发出彩虹剧团的魅力，\x01",
            "应该也是有办法的。\x02\x03",

            "#3404F在今后的交涉工作中，\x01",
            "这方面的规划活动大概也会\x01",
            "成为谈判的关键吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#0202F#11P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#0302F#11P好厉害啊……\x01",
            "竟然考虑得那么长远。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#3404F#6P呵呵，我毕竟也是专业人士。\x02\x03",

            "#3400F凭借自己的力量来看穿事物的本质，\x01",
            "考虑到各种状况，并制定出应有的目标，\x01",
            "为了实现它，而想出最恰当的手段。\x02\x03",

            "不管从事何种工作，\x01",
            "这些都是专业人士应有的做法。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#0000F#5P专业人士的做法……\x01",
            "原来如此，真是受教了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        (
            "#0109F#5P呵呵，这对我们来说，\x01",
            "或许也是必不可少的精神准备呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 2970, -1000, 6660, 180)
    SetScenarioFlags(0xA3, 7)
    SetChrSubChip(0x8, 0x0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_11_11B8 end

    def Function_12_1DF8(): pass

    label("Function_12_1DF8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Sound(801, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    #A0060
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──让您久等了。\x02",
        )
    )

    CloseMessageWindow()

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本水上巴士即将\x01",
            "到达『米修拉姆』。\x02",
        )
    )

    CloseMessageWindow()

    #A0062
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
    OP_25(0x1E0, 0x5A)
    Sleep(100)
    OP_25(0x1E0, 0x50)
    Sleep(100)
    OP_25(0x1E0, 0x46)
    Sleep(100)
    OP_25(0x1E0, 0x3C)
    Sleep(100)
    OP_25(0x1E0, 0x32)
    Sleep(100)
    OP_25(0x1E0, 0x28)
    Sleep(100)
    OP_25(0x1E0, 0x1E)
    Sleep(100)
    OP_25(0x1E0, 0x14)
    Sleep(100)
    OP_25(0x1E0, 0xA)
    Sleep(100)
    OP_25(0x1E0, 0x0)
    WaitBGM()
    SetScenarioFlags(0x5C, 0)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1DF8 end

    SaveToFile()

Try(main)
