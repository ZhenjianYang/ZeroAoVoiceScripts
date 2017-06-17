from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t2100.bin",                # FileName
        "t2100",                    # MapName
        "t2100",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2100",                  # 0
        "布鲁德队员",             # 1
        "达利亚队员",             # 2
        "艾丝蒂尔",               # 3
        "约修亚",                 # 4
        "游客迪恩",               # 5
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch34100.itc",                   # 01
        "chr/ch00600.itc",                   # 02
        "chr/ch00700.itc",                   # 03
        "chr/ch26700.itc",                   # 04
    ))

    DeclNpc(-13829,  10000,   -2960,   270,  389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-14060,  10000,   2900,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-15819,  5000,    -16600,  265,  405,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-16780,  5000,    -17700,  315,  405,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-17709,  5000,    -18780,  220,  385,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(-100,    10000,   -260,    1000,    -100,    10000,   -260,    0x007C, 0,  11, 0x0000)
    DeclActor(-1690,   10000,   -9200,   1000,    -1690,   10000,   -9200,   0x007C, 0,  12, 0x0000)
    DeclActor(8710,    10000,   -11130,  1000,    8710,    10000,   -11130,  0x007C, 0,  13, 0x0000)
    DeclActor(-16000,  10000,   0,       2000,    -16000,  10000,   0,       0x007C, 0,  14, 0x0000)
    DeclActor(15480,   10000,   4880,    1000,    19930,   7500,    5800,    0x007C, 0,  16, 0x0000)
    DeclActor(1500,    5050,    -20000,  1200,    1500,    6050,    -20000,  0x007C, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_250",          # 00, 0
        "Function_1_308",          # 01, 1
        "Function_2_369",          # 02, 2
        "Function_3_40D",          # 03, 3
        "Function_4_4D2",          # 04, 4
        "Function_5_608",          # 05, 5
        "Function_6_B19",          # 06, 6
        "Function_7_17A3",         # 07, 7
        "Function_8_19FA",         # 08, 8
        "Function_9_1A80",         # 09, 9
        "Function_10_1B4E",        # 0A, 10
        "Function_11_1D45",        # 0B, 11
        "Function_12_1F3B",        # 0C, 12
        "Function_13_2131",        # 0D, 13
        "Function_14_22CF",        # 0E, 14
        "Function_15_2B51",        # 0F, 15
        "Function_16_2CB6",        # 10, 16
    ))


    def Function_0_250(): pass

    label("Function_0_250")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_290"),
        (1, "loc_29C"),
        (2, "loc_2A8"),
        (3, "loc_2B4"),
        (4, "loc_2C0"),
        (5, "loc_2CC"),
        (6, "loc_2D8"),
        (SWITCH_DEFAULT, "loc_2E4"),
    )


    label("loc_290")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_29C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2A8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2B4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2C0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2CC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_307")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_307")

    Return()

    # Function_0_250 end

    def Function_1_308(): pass

    label("Function_1_308")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_368")
    OP_95(0xFE, -13830, 10000, -2960, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -14060, 10000, 2900, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    Jump("Function_1_308")

    label("loc_368")

    Return()

    # Function_1_308 end

    def Function_2_369(): pass

    label("Function_2_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_381")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_399")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_39F")

    label("loc_399")

    BeginChrThread(0x9, 0, 0, 1)

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9")
    SetChrPos(0x8, -8560, 5000, -19100, 175)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_3F9")

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F9")
    Event(0, 10)

    label("loc_3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40C")
    ClearChrFlags(0xC, 0x80)

    label("loc_40C")

    Return()

    # Function_2_369 end

    def Function_3_40D(): pass

    label("Function_3_40D")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    OP_66(0x4, 0x1)
    Jump("loc_4BA")

    label("loc_465")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_4BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_484")
    OP_66(0x0, 0x1)

    label("loc_484")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_496")
    OP_66(0x1, 0x1)

    label("loc_496")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A8")
    OP_66(0x2, 0x1)

    label("loc_4A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA")
    OP_66(0x3, 0x1)

    label("loc_4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD")
    OP_70(0x2, 0x0)
    Jump("loc_4D1")

    label("loc_4CD")

    OP_70(0x2, 0x1E)

    label("loc_4D1")

    Return()

    # Function_3_40D end

    def Function_4_4D2(): pass

    label("Function_4_4D2")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BF")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('弹簧跑鞋', 1)"), scpexpr(EXPR_END)), "loc_551")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '弹簧跑鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x113, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_5BA")

    label("loc_551")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '弹簧跑鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '弹簧跑鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_5BA")

    Jump("loc_5FC")

    label("loc_5BF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_5FC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4D2 end

    def Function_5_608(): pass

    label("Function_5_608")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_684")

    #C0004
    ChrTalk(
        0xFE,
        (
            "真是少见呢，达利亚今天\x01",
            "竟然主动和我搭话了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "……但是她说的内容太深奥，\x01",
            "我没能听懂。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6BE")

    label("loc_684")


    #C0006
    ChrTalk(
        0xFE,
        (
            "哎呀，明明是个增进\x01",
            "关系的机会呢，\x01",
            "真恨自己那么无知。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE")

    Jump("loc_B15")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_80E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78C")

    #C0007
    ChrTalk(
        0xFE,
        (
            "两个人就这么傻站在这里的话，\x01",
            "会有点不好意思吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "尤其是像达利亚\x01",
            "那么端庄有礼的人，\x01",
            "也不能总是和她随便闲聊家常……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "哎呀，真想一个人待一会，\x01",
            "我再去休息一下好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_809")

    label("loc_78C")


    #C0010
    ChrTalk(
        0xFE,
        (
            "我和在唐古拉姆门工作的巴雷尔\x01",
            "认识很长时间了，\x01",
            "所以在一起时比较轻松……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "但我怎么也没法适应\x01",
            "和女同事一起单独工作呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_809")

    Jump("loc_B15")

    label("loc_80E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88A")

    #C0012
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "果然还是待在这里才能让人内心平静。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "再稍微休息一下，我就要回去继续守卫国境了……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8D6")

    label("loc_88A")


    #C0014
    ChrTalk(
        0xFE,
        (
            "我是征得了达利亚的同意，\x01",
            "才在这休息的。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "……可绝对不是在\x01",
            "偷懒哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D6")

    Jump("loc_B15")

    label("loc_8DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B15")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AE")

    #C0016
    ChrTalk(
        0xFE,
        "哎？你们说那个启动钥匙应该在屋顶上？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "这……我和达利亚明明已经\x01",
            "把各个角落都仔细搜寻了一遍呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "……不过，或许可能是\x01",
            "我们看漏了吧。\x01",
            "搜索就拜托诸位了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A09")

    label("loc_9AE")


    #C0019
    ChrTalk(
        0xFE,
        (
            "我们也寻找过那个启动钥匙……\x01",
            "但也许是看漏了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "不好意思，就拜托你们继续搜寻了。\x02",
    )

    CloseMessageWindow()

    label("loc_A09")

    Jump("loc_B15")

    label("loc_A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC3")

    #C0021
    ChrTalk(
        0xFE,
        (
            "我在唐古拉姆门那边\x01",
            "有一个叫做巴雷尔的朋友。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "说实话，我很羡慕那家伙呢……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "这里一旦出现什么紧急情况的话，\x01",
            "我们的司令却很可能会不在，\x01",
            "让人很不放心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B15")

    label("loc_AC3")


    #C0024
    ChrTalk(
        0xFE,
        (
            "我好羡慕在唐古拉姆门\x01",
            "工作的巴雷尔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "我被派遣到这个地方，\x01",
            "真是倒霉……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B15")

    TalkEnd(0xFE)
    Return()

    # Function_5_608 end

    def Function_6_B19(): pass

    label("Function_6_B19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C39")

    #C0026
    ChrTalk(
        0xFE,
        (
            "在几年前，帝国曾经发生了\x01",
            "多处游击士协会同时遭受\x01",
            "猎兵团袭击的事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "虽然在一位很有威望的游击士\x01",
            "的领导下，事态顺利平息了……\x01",
            "但仍然还流传着各种传言。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "有人说，\x01",
            "其实那场袭击事件本身也只是\x01",
            "为了声东击西而演的一场戏……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "……总觉得有什么内情呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_C88")

    label("loc_C39")


    #C0030
    ChrTalk(
        0xFE,
        (
            "几年前发生的那场\x01",
            "帝国游击士协会遭袭事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "……总觉得有什么内情呢。\x02",
    )

    CloseMessageWindow()

    label("loc_C88")

    Jump("loc_179F")

    label("loc_C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_D30")

    #C0032
    ChrTalk(
        0xFE,
        (
            "一看到帝国那边的守备那么坚固……\x01",
            "就会对我们这个毫无防备，\x01",
            "形同虚设的国境门感到痛心疾首。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "如果帝国真的有心要打过来，\x01",
            "我们这个关卡肯定就……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179F")

    label("loc_D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DE4")

    #C0034
    ChrTalk(
        0xFE,
        (
            "以前，在利贝尔曾经\x01",
            "发生过导力停止现象……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "那时候，帝国的奥斯本宰相阁下\x01",
            "大胆出动了原本已经废弃的\x01",
            "蒸气驱动式战车。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "如此周密的准备……\x01",
            "真是个可怕的男人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179F")

    label("loc_DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBB")

    #C0037
    ChrTalk(
        0xFE,
        (
            "毕竟我们是在同一个地方担任警备工作，\x01",
            "我为了搞好关系，拉近距离，\x01",
            "就试着谈了谈这个话题——\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "关于前一阵在利贝尔发生的异变，\x01",
            "你是怎么想的……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "突然问了这样的问题，\x01",
            "果然不太好吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F3D")

    label("loc_EBB")


    #C0040
    ChrTalk(
        0xFE,
        (
            "唉……怕生的人真是很辛苦啊。\x01",
            "一旦话题中断了，\x01",
            "气氛就会莫名地尴尬起来……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "没办法，\x01",
            "今天还是不聊了，\x01",
            "集中精力专心工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3D")

    Jump("loc_179F")

    label("loc_F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_10A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1021")

    #C0042
    ChrTalk(
        0xFE,
        (
            "我和布鲁德先生很少聊天，\x01",
            "就算说话，也说不上几句。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "和女队员们在一起的时候，\x01",
            "我倒不是这样的……\x01",
            "可能是因为我比较害羞吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "大家同样在做着守卫国境的工作，\x01",
            "还是希望能相处得更融洽一些呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_10A1")

    label("loc_1021")


    #C0045
    ChrTalk(
        0xFE,
        (
            "如果是米蕾优准尉的话，\x01",
            "既容易与她亲近，\x01",
            "又很好说话……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "但和男性单独在一起，\x01",
            "我实在是很难习惯呢。\x01",
            "我是个很怕生的人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A1")

    Jump("loc_179F")

    label("loc_10A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_11EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118B")

    #C0047
    ChrTalk(
        0xFE,
        (
            "布鲁德先生说他\x01",
            "想休息一会，\x01",
            "所以我暂时要独自站岗。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "这本来是违反规定的行为……\x01",
            "不过反正司令也不在，就装作没看见吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "虽说是工作，但日复一日地望着这\x01",
            "毫无变化的相同景色，多少也会有些厌倦呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11E7")

    label("loc_118B")


    #C0050
    ChrTalk(
        0xFE,
        (
            "……再过一会，\x01",
            "我也去休息一下好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "尝尝在工作时间偷懒的感觉，\x01",
            "或许也是一种乐趣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E7")

    Jump("loc_179F")

    label("loc_11EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1447")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1287")

    #C0052
    ChrTalk(
        0xFE,
        "……呼……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "昨天晚上，司令跑到屋顶上\x01",
            "大声唱歌……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "我们最近都已经这么忙了，\x01",
            "他却连个安稳觉都不让我们睡好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1442")

    label("loc_1287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1389")

    #C0055
    ChrTalk(
        0xFE,
        (
            "因为警备队里的\x01",
            "女队员数量并不多，\x01",
            "所以有时候会引起别人的好奇呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "唐古拉姆门的索妮亚副司令和\x01",
            "诺艾尔上士都是漂亮的美人，\x01",
            "我猜她们会更加辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "『美女警备队员的独家专访！』\x01",
            "被那种新闻搅扰的日子可真是……\x01",
            "哎呀，完全不敢想象……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1442")

    label("loc_1389")


    #C0058
    ChrTalk(
        0xFE,
        (
            "这么说来，\x01",
            "在利贝尔发生了\x01",
            "那次异变之后……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "有位名叫尤莉亚的王室亲卫队队长\x01",
            "也被大肆炒作了一番呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "我看到过她的照片，\x01",
            "也是一位英气十足的人呢……\x01",
            "当时一定是辛苦了一阵子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1442")

    Jump("loc_179F")

    label("loc_1447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_15F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1562")

    #C0061
    ChrTalk(
        0xFE,
        (
            "直到前年为止，\x01",
            "那边那个卡雷利亚要塞，\x01",
            "一直都有一门巨大的列车炮瞄准着这边。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "真有种一触即发的感觉呢……\x01",
            "看那种严守戒备的态势，简直就像是要\x01",
            "再次爆发大规模的争端一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "虽然托互不侵犯条约的福，\x01",
            "这里最近十分和平……\x01",
            "但那种恐惧感终究是难以忘怀的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15EE")

    label("loc_1562")


    #C0064
    ChrTalk(
        0xFE,
        (
            "多亏了前年签署的互不侵犯条约，\x01",
            "克洛斯贝尔才得以从极度紧张的状态下解放。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "提出条约的人是利贝尔的艾莉茜雅女王，\x01",
            "她实在是让人敬佩啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15EE")

    Jump("loc_179F")

    label("loc_15F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_179F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1723")

    #C0066
    ChrTalk(
        0xFE,
        (
            "那个看上去很像岩壁的，是帝国引以为傲的\x01",
            "『卡雷利亚要塞』的一角。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "帝国的军事力量对我们来说是一大威胁，\x01",
            "所以在任何时候都不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#0300F嗯～不过，绷得太紧也不好哦。\x02\x03",

            "#0304F认真工作自然是很好，\x01",
            "但我觉得，适度放松也是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "……兰迪前辈是放松过头了！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_179F")

    label("loc_1723")


    #C0070
    ChrTalk(
        0xFE,
        (
            "……不过，的确是这样，\x01",
            "太过紧张也是不好的。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "再过一会，我就去和\x01",
            "布鲁德先生换个班吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        "#0306F（认真的家伙……）\x02",
    )

    CloseMessageWindow()

    label("loc_179F")

    TalkEnd(0xFE)
    Return()

    # Function_6_B19 end

    def Function_7_17A3(): pass

    label("Function_7_17A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_19F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1952")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0073
    ChrTalk(
        0xA,
        (
            "#0805F哇～好壮观……\x02\x03",

            "#0801F那就是帝国那边的国境吧。\x01",
            "至今为止，好像一直都没有\x01",
            "机会好好观察一下呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "#0901F帝国那边的设施是叫做\x01",
            "『卡雷利亚要塞』吧。\x02\x03",

            "那可是帝国最重要的军事据点之一，\x01",
            "是个建造得滴水不漏的要塞呢。\x02\x03",

            "#0903F因为，不管怎么说……\x01",
            "这里都是离共和国最近的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        (
            "#0806F这样啊，看来帝国和共和国\x01",
            "可真是水火不容。\x02\x03",

            "#0808F……克洛斯贝尔的压力\x01",
            "果然也不小呢～\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_19F6")

    label("loc_1952")


    #C0076
    ChrTalk(
        0xA,
        (
            "#0805F啊，罗伊德，你们也来了呀。\x02\x03",

            "#0806F看到这些之后，对帝国的威严感\x01",
            "又有了更加深刻的体会呢。\x02\x03",

            "#0802F……虽说我认识的帝国人之中\x01",
            "也有很好的人，还有很奇怪的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F6")

    TalkEnd(0xFE)
    Return()

    # Function_7_17A3 end

    def Function_8_19FA(): pass

    label("Function_8_19FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A18")
    Call(0, 7)
    Jump("loc_1A7C")

    label("loc_1A18")


    #C0077
    ChrTalk(
        0xB,
        (
            "#0904F哈哈……\x01",
            "我们只是顺路过来看看。\x02\x03",

            "#0900F要想了解克洛斯贝尔，\x01",
            "一定要到各处都看一看才行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A7C")

    TalkEnd(0xFE)
    Return()

    # Function_8_19FA end

    def Function_9_1A80(): pass

    label("Function_9_1A80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF0")

    #C0078
    ChrTalk(
        0xFE,
        (
            "哇！！真高啊。\x01",
            "要是脚底不小心滑一下，\x01",
            "可就要跌入谷底了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xDC, 0x1F4)

    #C0079
    ChrTalk(
        0xFE,
        "……好可怕！！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1B4A")

    label("loc_1AF0")


    #C0080
    ChrTalk(
        0xFE,
        (
            "掉下去的话，绝对死定了……\x01",
            "好，再看一次吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xDC, 0x1F4)

    #C0081
    ChrTalk(
        0xFE,
        "…………果然好可怕啊！！！\x02",
    )

    CloseMessageWindow()

    label("loc_1B4A")

    TalkEnd(0xFE)
    Return()

    # Function_9_1A80 end

    def Function_10_1B4E(): pass

    label("Function_10_1B4E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6670, 11000, 3120, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18620, 0)
    SetChrPos(0x101, 7300, 10000, 2500, 180)
    SetChrPos(0x102, 6000, 10000, 2500, 180)
    SetChrPos(0x103, 7300, 10000, 3800, 180)
    SetChrPos(0x104, 6000, 10000, 3800, 180)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0082
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯……\x01",
            "到达屋顶了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        (
            "#12P#0200F按照米蕾优准尉的说法，\x01",
            "司令是在这里尽情高歌了一番吧。\x02\x03",

            "来到这里的时候，他应该\x01",
            "正处于酒劲达到顶点的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x102,
        (
            "#5P#0106F最大的问题，\x01",
            "就是他根本就不记得\x01",
            "把钥匙丢在哪里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#11P#0300F嗯，不过他把钥匙\x01",
            "丢在这里的可能性似乎很高。\x02\x03",

            "总之，我们先调查一遍吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 7300, 10000, 2500, 180)
    OP_29(0x19, 0x1, 0x5)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_1B4E end

    def Function_11_1D45(): pass

    label("Function_11_1D45")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB7")

    #C0086
    ChrTalk(
        0x101,
        (
            "#0005F嗯……？\x01",
            "这个发光的东西难道是……\x02\x03",

            "#0006F……是十米拉的硬币。\x01",
            "也许是司令丢的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F01")

    label("loc_1DB7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E28")

    #C0087
    ChrTalk(
        0x102,
        (
            "#0105F呀……\x01",
            "这个发光的东西莫非是……\x02\x03",

            "#0106F……是十米拉的硬币啊。\x01",
            "大概是司令掉的吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F01")

    label("loc_1E28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E93")

    #C0088
    ChrTalk(
        0x103,
        (
            "#0205F啊……\x01",
            "这个发光的东西是……\x02\x03",

            "#0211F……是十米拉的硬币吧。\x01",
            "应该是司令掉的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F01")

    label("loc_1E93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F01")

    #C0089
    ChrTalk(
        0x104,
        (
            "#0305F嗯……？\x01",
            "这个发光的东西是……\x02\x03",

            "#0306F……这不是十米拉的硬币吗，\x01",
            "什么嘛，真够添乱的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F01")

    OP_65(0x0, 0x1)
    OP_29(0x19, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F37")
    Call(0, 15)
    OP_66(0x4, 0x1)

    label("loc_1F37")

    TalkEnd(0xFF)
    Return()

    # Function_11_1D45 end

    def Function_12_1F3B(): pass

    label("Function_12_1F3B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FB0")

    #C0090
    ChrTalk(
        0x101,
        (
            "#0005F啊……这里好像有什么东西。\x02\x03",

            "#0006F……是罐装果汁的拉环啊。\x01",
            "稍后扔到垃圾箱里去吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20F7")

    label("loc_1FB0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_201C")

    #C0091
    ChrTalk(
        0x102,
        (
            "#0105F啊……这里有东西哦。\x02\x03",

            "#0106F……是罐装果汁的拉环呢。\x01",
            "稍后要扔进垃圾箱才行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20F7")

    label("loc_201C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_208C")

    #C0092
    ChrTalk(
        0x103,
        (
            "#0205F啊……这里好像有什么东西。\x02\x03",

            "#0203F……是罐装果汁的拉环。\x01",
            "稍后要扔进垃圾箱才行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20F7")

    label("loc_208C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20F7")

    #C0093
    ChrTalk(
        0x104,
        (
            "#0305F哦……这里好像有东西。\x02\x03",

            "#0306F……只是个罐装果汁的拉环啊。\x01",
            "真是的，白高兴了一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20F7")

    OP_29(0x19, 0x1, 0x7)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_212D")
    Call(0, 15)
    OP_66(0x4, 0x1)

    label("loc_212D")

    TalkEnd(0xFF)
    Return()

    # Function_12_1F3B end

    def Function_13_2131(): pass

    label("Function_13_2131")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_218C")

    #C0094
    ChrTalk(
        0x101,
        (
            "#0005F这个是……\x02\x03",

            "#0006F……是普通的铁丝啊。\x01",
            "嗯，找不到钥匙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2295")

    label("loc_218C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E6")

    #C0095
    ChrTalk(
        0x102,
        (
            "#0105F这是……\x02\x03",

            "#0106F……只是普通的铁丝嘛。\x01",
            "唔，找不到钥匙呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2295")

    label("loc_21E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223C")

    #C0096
    ChrTalk(
        0x103,
        (
            "#0205F这是……\x02\x03",

            "#0203F……普通的铁丝吗。\x01",
            "好像找不到钥匙呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2295")

    label("loc_223C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2295")

    #C0097
    ChrTalk(
        0x104,
        (
            "#0305F噢，这是……\x02\x03",

            "#0301F……只是根铁丝啊。\x01",
            "嘁，钥匙还是找不到啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2295")

    OP_29(0x19, 0x1, 0x8)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22CB")
    Call(0, 15)
    OP_66(0x4, 0x1)

    label("loc_22CB")

    TalkEnd(0xFF)
    Return()

    # Function_13_2131 end

    def Function_14_22CF(): pass

    label("Function_14_22CF")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -10400, 10000, -650, 270)
    SetChrPos(0x102, -10400, 10000, 650, 270)
    SetChrPos(0x103, -9400, 10000, -1300, 270)
    SetChrPos(0x104, -9400, 10000, 1300, 270)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(-29750, 13600, 710, 0)
    MoveCamera(256, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(35900, 0)
    SetCameraDistance(45900, 5000)
    OP_6F(0x10)

    #C0098
    ChrTalk(
        0x101,
        "#5P#0005F那边是……通向帝国的国境隧道吗？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#11P#0103F嗯，没错。\x02\x03",

            "#0101F正确来说，是将隧道与包含隧道\x01",
            "的岩壁进行一体化建造的要塞都市——\x01",
            "『卡雷利亚要塞』。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        (
            "#5P#0208F作为帝国最东部的要塞，\x01",
            "是用来牵制共和国的堤坝……\x02\x03",

            "#0206F像这样眺望的话……\x01",
            "不知为何，总有种莫名的强大压迫感呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-9200, 11500, -580, 0)
    MoveCamera(294, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19210, 0)
    OP_68(-9200, 11500, -580, 0)
    MoveCamera(294, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17710, 0)
    OP_0D()

    def lambda_24E5():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_24E5)
    Sleep(300)

    #C0101
    ChrTalk(
        0x104,
        (
            "#11P#0304F哈哈，阿缇会有这种感觉\x01",
            "也不奇怪啦。\x02\x03",

            "#0301F那面墙的里面，藏着\x01",
            "一种被称为『列车炮』的可怕东西。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2563():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2563)

    def lambda_2570():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2570)

    def lambda_257D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_257D)
    Sleep(300)

    #C0102
    ChrTalk(
        0x101,
        (
            "#5P#0005F列车炮……\x01",
            "好像在哪里听说过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#11P#0303F帝国军引以为傲的最强兵器之一。\x02\x03",

            "#0301F据说是个能发射８０里矩炮弹，\x01",
            "像怪物一样可怕的大炮。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x103,
        (
            "#6P#0201F原来如此……\x01",
            "是莱恩福尔特公司的战略兵器吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_265E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_265E)
    Sleep(300)

    #C0105
    ChrTalk(
        0x102,
        (
            "#11P#0103F大约在两年之前……\x01",
            "帝国与共和国之间的紧张局势\x01",
            "达到了顶点。\x02\x03",

            "#0101F在两国正在进行大规模演习的时候，\x01",
            "我们对面的那个关卡大门突然打开了，\x01",
            "里面现出了两门巨大的列车炮。\x02\x03",

            "#0108F那种武器的射程连克洛斯贝尔市\x01",
            "都能覆盖在内，如果使用的话……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#6P#0006F……会酿成一场大灾难吧。\x02\x03",

            "#0008F（在我订阅的克洛斯贝尔时代周刊里，\x01",
            "  倒是没写得这么详细……）\x02\x03",

            "#0013F（但当时的情况竟然那么危急，\x01",
            "  真是难以置信……)\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        (
            "#11P#0304F不过正如你所见，\x01",
            "列车炮现在已经被收起来了。\x02\x03",

            "#0300F这多亏了倡导缔结《互不侵犯条约》\x01",
            "的利贝尔女王陛下。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#6P#0006F是啊……\x01",
            "虽然早就听说过她是一位杰出的女王，\x01",
            "但说实话，这次又有了新的认识。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    #C0109
    ChrTalk(
        0x101,
        (
            "#6P#0005F……啊，一不小心就闲聊起来了。\x01",
            "得抓紧时间，赶快寻找钥匙才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x19, 0x1, 0x9)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B34")

    #C0110
    ChrTalk(
        0x102,
        (
            "#11P#0105F嗯，不过……\x01",
            "屋顶上的可疑地点\x01",
            "基本都已经找过一遍了。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x104,
        (
            "#11P#0306F但司令的确来过这里，\x01",
            "这点应该没错。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        (
            "#6P#0203F会不会是『钥匙丢在了屋顶上』\x01",
            "这个前提本身就错了呢……\x02\x03",

            "#0200F或许，有可能\x01",
            "是被某个警备队员\x01",
            "捡到了也说不定。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#6P#0003F似乎应该像迪塔总裁之前说的那样，\x01",
            "稍微变换一下视角比较好。\x02\x03",

            "#0001F或许……钥匙并没有掉在\x01",
            "很容易被人捡到的地方。\x02\x03",

            "我们再把各个角落重新搜寻一遍吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_66(0x4, 0x1)
    OP_29(0x19, 0x1, 0x1F)

    label("loc_2B34")

    OP_5A()
    SetChrPos(0x0, -10400, 10000, -650, 270)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_14_22CF end

    def Function_15_2B51(): pass

    label("Function_15_2B51")


    #C0114
    ChrTalk(
        0x102,
        "#0105F嗯，找不到呢……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x104,
        (
            "#0306F但司令的确来过这里，\x01",
            "这点应该没错。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x103,
        (
            "#0203F会不会是『钥匙丢在了屋顶上』\x01",
            "这个前提本身就错了呢……\x02\x03",

            "#0200F或许，有可能\x01",
            "是被某个警备队员\x01",
            "捡到了也说不定。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0003F似乎应该像迪塔总裁之前说的那样，\x01",
            "稍微变换一下视角比较好。\x02\x03",

            "#0001F或许……钥匙并没有掉在\x01",
            "很容易被人捡到的地方。\x02\x03",

            "我们再把各个角落重新搜寻一遍吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x19, 0x1, 0x1F)
    Return()

    # Function_15_2B51 end

    def Function_16_2CB6(): pass

    label("Function_16_2CB6")

    EventBegin(0x0)
    LoadEffect(0x9, "event\\eva00_00.eff")
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(15330, 11000, 4890, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 15000, 10000, 4700, 90)
    SetChrPos(0x102, 15000, 10000, 3400, 90)
    SetChrPos(0x103, 15000, 10000, 2100, 90)
    SetChrPos(0x104, 15000, 10000, 800, 90)
    SetCameraDistance(19000, 2000)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0118
    ChrTalk(
        0x101,
        "#5P#0001F…………嗯？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0119
    ChrTalk(
        0x103,
        "#5P#0205F……罗伊德前辈？\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        "#5P#0105F啊，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#5P#0005F……有了……！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(24460, 11000, 1930, 3000)
    MoveCamera(310, 33, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(15440, 3000)
    OP_6F(0x79)
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 19510, 7000, 5830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(860, 0, 100, 0)
    Sleep(3000)

    #C0122
    ChrTalk(
        0x104,
        (
            "#5P#0306F#N喂喂，真的假的啊……\x01",
            "竟然挂在那种地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0123
    ChrTalk(
        0x103,
        (
            "#5P#0206F#N怪不得把整个国境门内部\x01",
            "全部找遍了，也都一无所获呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0124
    ChrTalk(
        0x101,
        (
            "#5P#0000F#N总之，赶快去报告给准尉吧。\x02\x03",

            "只要借个梯子什么的过来，\x01",
            "应该就可以拿到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0125
    ChrTalk(
        0x102,
        "#5P#0100F#N嗯，走吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    SetScenarioFlags(0x5C, 0)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2CB6 end

    SaveToFile()

Try(main)
