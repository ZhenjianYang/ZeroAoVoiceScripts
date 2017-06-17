from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t0530.bin",                # FileName
        "t0530",                    # MapName
        "t0530",                    # Location
        0x0040,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x18,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 64, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0530",                  # 0
        "贝卡莱",                 # 1
        "奇米",                   # 2
        "哈罗德",                 # 3
    ))

    AddCharChip((
        "chr/ch23400.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch09300.itc",                   # 02
    ))

    DeclNpc(-129,    0,       3640,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-4530,   0,       4500,    320,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-3400,   0,       3559,    315,  389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(-40,     0,       2120,    1000,    -130,    1500,    3640,    0x007E, 0,  3,  0x0000)

    ChipFrameInfo(312, 0)                                        # 0

    ScpFunction((
        "Function_0_138",          # 00, 0
        "Function_1_1F0",          # 01, 1
        "Function_2_309",          # 02, 2
        "Function_3_342",          # 03, 3
        "Function_4_346",          # 04, 4
        "Function_5_11E8",         # 05, 5
        "Function_6_176A",         # 06, 6
        "Function_7_183B",         # 07, 7
    ))


    def Function_0_138(): pass

    label("Function_0_138")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_178"),
        (1, "loc_184"),
        (2, "loc_190"),
        (3, "loc_19C"),
        (4, "loc_1A8"),
        (5, "loc_1B4"),
        (6, "loc_1C0"),
        (SWITCH_DEFAULT, "loc_1CC"),
    )


    label("loc_178")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_184")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_190")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_19C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1EF")

    Return()

    # Function_0_138 end

    def Function_1_1F0(): pass

    label("Function_1_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FE")
    Jump("loc_308")

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_20C")
    Jump("loc_308")

    label("loc_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_21A")
    Jump("loc_308")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_245")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1000, 0, 1600, 315)
    TurnDirection(0x8, 0xA, 0)
    Jump("loc_308")

    label("loc_245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_253")
    Jump("loc_308")

    label("loc_253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_261")
    Jump("loc_308")

    label("loc_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_26F")
    Jump("loc_308")

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_282")
    SetChrFlags(0x9, 0x80)
    Jump("loc_308")

    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_290")
    Jump("loc_308")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A3")
    SetChrFlags(0x9, 0x80)
    Jump("loc_308")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2B1")
    Jump("loc_308")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D5")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    TurnDirection(0x9, 0xA, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_308")

    label("loc_2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E3")
    Jump("loc_308")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2F1")
    Jump("loc_308")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FF")
    Jump("loc_308")

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_308")

    label("loc_308")

    Return()

    # Function_1_1F0 end

    def Function_2_309(): pass

    label("Function_2_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_31B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_341")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_341")

    Return()

    # Function_2_309 end

    def Function_3_342(): pass

    label("Function_3_342")

    Call(0, 4)
    Return()

    # Function_3_342 end

    def Function_4_346(): pass

    label("Function_4_346")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3C2")
    OP_AF(0x58)
    Jump("loc_3E4")

    label("loc_3C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D2")
    OP_AF(0x57)
    Jump("loc_3E4")

    label("loc_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E2")
    OP_AF(0x56)
    Jump("loc_3E4")

    label("loc_3E2")

    OP_AF(0x55)

    label("loc_3E4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11DF")

    label("loc_3F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_407")
    Jump("loc_11DF")

    label("loc_407")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41F")
    TalkEnd(0x8)
    Return()

    label("loc_41F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11DF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_512")

    #C0001
    ChrTalk(
        0x8,
        (
            "矿山是我们玛因兹居民\x01",
            "无可替代的骄傲。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "不管发生什么异常事态，\x01",
            "只要我们不遗忘这种自豪之情，\x01",
            "就一定能顺利越过困境。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "你们心中肯定也存在着\x01",
            "某些无可替代的事物，\x01",
            "绝对不要将其遗忘啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5A6")

    label("loc_512")


    #C0004
    ChrTalk(
        0x8,
        (
            "不管发生什么异常事态，\x01",
            "只要我们不遗忘这种自豪之情，\x01",
            "就一定能顺利越过困境。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "你们心中肯定也存在着\x01",
            "某些无可替代的事物，\x01",
            "绝对不要将其遗忘啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A6")

    Jump("loc_11DF")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_686")

    #C0006
    ChrTalk(
        0x8,
        (
            "我没读过什么书，\x01",
            "所以并不是很理解\x01",
            "那个无效宣言……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "我只希望奇米和\x01",
            "其他的小家伙们\x01",
            "能过上安心的生活。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "……但因为这种理由，我们便把\x01",
            "那些危险的事情都交给了反抗军，\x01",
            "实在是很愧疚啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_70F")

    label("loc_686")


    #C0009
    ChrTalk(
        0x8,
        (
            "我们把危险的事情都交给了反抗军，\x01",
            "实在是很愧疚……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "但为了让奇米和其他的\x01",
            "小家伙们过上安心的生活，\x01",
            "希望反抗军的各位一定要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70F")

    Jump("loc_11DF")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83C")

    #C0011
    ChrTalk(
        0x8,
        (
            "在围剿反抗军之前，\x01",
            "那些猎兵好像曾去\x01",
            "镇长家拜访过。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "不知他们有什么企图，\x01",
            "竟然厚颜无耻地提出了『请让居民们\x01",
            "不要离开此镇』这样的要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "恐怕是想牵制向反抗军\x01",
            "提供援助的我们吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "啧，我当时要是在场的话，\x01",
            "一定会狠狠揍他们一顿，\x01",
            "以报占领事件时的一箭之仇。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8A0")

    label("loc_83C")


    #C0015
    ChrTalk(
        0x8,
        (
            "听说那些猎兵还在山道的\x01",
            "隧道内布下了地雷。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "啧，我当时要是在场的话，\x01",
            "一定会狠狠揍他们一顿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A0")

    Jump("loc_11DF")

    label("loc_8A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A0")

    #C0017
    ChrTalk(
        0x8,
        (
            "因为之前遭到那些猎兵的占领，\x01",
            "玛因兹的各位\x01",
            "直到现在都很沮丧。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "我也是当事人之一，\x01",
            "自然能理解他们的心情……\x01",
            "但一直这样消沉下去也无济于事。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "既然如此，我要连同已经恢复\x01",
            "精神的矿工们，想一些能让\x01",
            "大家重新振作的办法。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A19")

    label("loc_9A0")


    #C0020
    ChrTalk(
        0x8,
        (
            "那些猎兵确实很可怕……\x01",
            "但我们不能一直消沉下去。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "我要连同已经恢复精神的\x01",
            "矿工们，想一些能让\x01",
            "大家重新振作的办法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A19")

    Jump("loc_11DF")

    label("loc_A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A98")

    #C0022
    ChrTalk(
        0x8,
        (
            "我当年就是在这样的\x01",
            "雨天里腿部负伤，\x01",
            "并因此而辞去了矿工的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        "……当时的旧伤至今仍然隐隐作痛呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11DF")

    label("loc_A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4C")

    #C0024
    ChrTalk(
        0x8,
        (
            "奇米今天去找霍夫曼家的\x01",
            "那个小鬼一起玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "……和她年龄相近的小孩子很少，\x01",
            "交个朋友倒是没什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "但将来该不会发展成\x01",
            "恋爱交往的关系吧……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BCB")

    label("loc_B4C")


    #C0027
    ChrTalk(
        0x8,
        (
            "奇米和霍夫曼家的那个小鬼\x01",
            "将来绝不是没有发展成\x01",
            "那种关系的可能……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "……我必须得去叮嘱霍夫曼那家伙一下，\x01",
            "让他严加注意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCB")

    Jump("loc_11DF")

    label("loc_BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA6")

    #C0029
    ChrTalk(
        0x8,
        (
            "自不久前的那场通商会议之后，\x01",
            "有关独立的讨论好像\x01",
            "渐渐热烈了起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "新市长确实是个\x01",
            "很有想法的人啊。\x01",
            "嘿嘿，听起来真不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "独立之后，我们就再也不用\x01",
            "对帝国和共和国点头哈腰了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D02")

    label("loc_CA6")


    #C0032
    ChrTalk(
        0x8,
        "独立为自主国家……听起来真不错呢。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "我们克洛斯贝尔的人民\x01",
            "今后一定要活得\x01",
            "更加自豪。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D02")

    Jump("loc_11DF")

    label("loc_D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFA")

    #C0034
    ChrTalk(
        0x8,
        (
            "不久前，我因为太担心奇米，\x01",
            "最后没有忍住，\x01",
            "跑到主日学校的课堂去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "当时真是给大家添了不少麻烦。\x01",
            "孩子们都被我这张\x01",
            "凶巴巴的脸吓到了……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "以后可不能再去\x01",
            "给奇米丢人了，一定要忍住，\x01",
            "别再闯进主日学校的课堂。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E8A")

    label("loc_DFA")


    #C0037
    ChrTalk(
        0x8,
        (
            "不久前，我因为太担心奇米，\x01",
            "最后没有忍住，\x01",
            "跑到主日学校的课堂去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "以后可不能再去\x01",
            "给奇米丢人了，一定要忍住，\x01",
            "别再闯进主日学校的课堂。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8A")

    Jump("loc_11DF")

    label("loc_E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F09")

    #C0039
    ChrTalk(
        0x8,
        (
            "哦，哈罗德\x01",
            "那家伙来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "上次从他那里采购的食材\x01",
            "已经快卖完了。\x01",
            "嘿嘿，来得正是时候。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F54")

    label("loc_F09")


    #C0041
    ChrTalk(
        0x8,
        (
            "哈罗德\x01",
            "那家伙来得\x01",
            "真是时候。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "好，这次进货时\x01",
            "的出价我就放宽些吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F54")

    Jump("loc_11DF")

    label("loc_F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102D")

    #C0043
    ChrTalk(
        0x8,
        (
            "我没上过什么学，\x01",
            "搞不懂那些复杂的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "那场所谓的通商会议，\x01",
            "简要来说，就是一群头脑精明\x01",
            "的家伙聚在一起商讨的活动吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "为了广大年轻人\x01",
            "的未来，希望他们\x01",
            "能讨论出好的结果。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10B7")

    label("loc_102D")


    #C0046
    ChrTalk(
        0x8,
        (
            "那场所谓的通商会议，\x01",
            "简要来说，就是一群头脑精明\x01",
            "的家伙聚在一起商讨的活动吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "为了广大年轻人\x01",
            "的未来，希望他们\x01",
            "能讨论出好的结果。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B7")

    Jump("loc_11DF")

    label("loc_10BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_11DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1164")

    #C0048
    ChrTalk(
        0x8,
        (
            "最近这段时间，年轻矿工们\x01",
            "好像越来越有干劲了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "我原本还有点担心，\x01",
            "不知他们能否顺利完成工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "嘿嘿，看样子，\x01",
            "是我太多虑了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11DF")

    label("loc_1164")


    #C0051
    ChrTalk(
        0x8,
        (
            "在冈兹被卷进那起教团事件\x01",
            "的时候，我还很担心他，\x01",
            "不知道将来会怎么样……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "嘿嘿，但如今看来，\x01",
            "好像已经不用我担心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DF")

    Jump("loc_353")

    label("loc_11E4")

    TalkEnd(0x8)
    Return()

    # Function_4_346 end

    def Function_5_11E8(): pass

    label("Function_5_11E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1279")

    #C0053
    ChrTalk(
        0x9,
        (
            "虽然外面出现了一棵\x01",
            "很奇怪的大树……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "但因为矿山重新开放，\x01",
            "爸爸好像非常\x01",
            "高兴呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        "嘿嘿，奇米也很高兴。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12CF")

    label("loc_1279")


    #C0056
    ChrTalk(
        0x9,
        (
            "虽然外面出现了一棵\x01",
            "很奇怪的大树……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "但爸爸好像非常开心，\x01",
            "所以奇米也不在乎～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CF")

    Jump("loc_1766")

    label("loc_12D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_132A")

    #C0058
    ChrTalk(
        0x9,
        (
            "短时间内，好像不能再上\x01",
            "主日学校的课了～\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "希望修女\x01",
            "身体健康……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1766")

    label("loc_132A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_13A1")

    #C0060
    ChrTalk(
        0x9,
        (
            "自从独立之后，\x01",
            "爸爸就一直很愤怒。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "他以前明明说过\x01",
            "独立是件好事呢……\x01",
            "看来独立其实是件坏事吧～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1766")

    label("loc_13A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1479")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141B")

    #C0062
    ChrTalk(
        0x9,
        (
            "不管到了什么时候，\x01",
            "奇米都要微笑～微笑～¤\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "爸爸说过，\x01",
            "只要一直微笑，\x01",
            "就可以打起精神。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1474")

    label("loc_141B")


    #C0064
    ChrTalk(
        0x9,
        (
            "不管到了什么时候，\x01",
            "奇米都要微笑～微笑～¤\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "真希望镇上的\x01",
            "各位能早点恢复\x01",
            "精神啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1474")

    Jump("loc_1766")

    label("loc_1479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1554")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1509")

    #C0066
    ChrTalk(
        0x9,
        (
            "每到下雨天，\x01",
            "爸爸就显得很失落。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "看来爸爸一直都很想\x01",
            "继续从事矿工的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "可是奇米很喜欢\x01",
            "现在的爸爸！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_154F")

    label("loc_1509")


    #C0069
    ChrTalk(
        0x9,
        (
            "每到下雨天，\x01",
            "爸爸就显得很失落。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "奇米一定要让爸爸\x01",
            "打起精神。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_154F")

    Jump("loc_1766")

    label("loc_1554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1562")
    Jump("loc_1766")

    label("loc_1562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_15CC")

    #C0071
    ChrTalk(
        0x9,
        (
            "奇米还不明白\x01",
            "大家说的独立\x01",
            "是什么意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "但爸爸说\x01",
            "独立是件好事，\x01",
            "所以奇米也赞成～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1766")

    label("loc_15CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15DA")
    Jump("loc_1766")

    label("loc_15DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1610")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F5")
    Call(0, 6)
    Jump("loc_160B")

    label("loc_15F5")


    #C0073
    ChrTalk(
        0x9,
        "哇！是咪西玩偶！\x02",
    )

    CloseMessageWindow()

    label("loc_160B")

    Jump("loc_1766")

    label("loc_1610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1698")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167F")

    #C0074
    ChrTalk(
        0x9,
        (
            "等奇米长大以后，\x01",
            "要和爸爸一起经营这家商店。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "所以从现在开始\x01",
            "就要熟悉工作～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1693")

    label("loc_167F")


    #C0076
    ChrTalk(
        0x9,
        "帮忙～帮忙～¤\x02",
    )

    CloseMessageWindow()

    label("loc_1693")

    Jump("loc_1766")

    label("loc_1698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1766")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1716")

    #C0077
    ChrTalk(
        0x9,
        (
            "爸爸以前是镇上\x01",
            "最棒的矿工。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "所以，虽然他平时总是\x01",
            "对矿工们很严厉，\x01",
            "但其实是很关心大家的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1766")

    label("loc_1716")


    #C0079
    ChrTalk(
        0x9,
        (
            "爸爸以前是镇上\x01",
            "最棒的矿工。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "虽然他平时很严厉，\x01",
            "但其实是个很温和的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1766")

    TalkEnd(0xFE)
    Return()

    # Function_5_11E8 end

    def Function_6_176A(): pass

    label("Function_6_176A")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0081
    ChrTalk(
        0x9,
        "啊，是哈罗德叔叔。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        "您今天是来和爸爸做生意的吗？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "#03600F嗯，正是，\x01",
            "我带来了很多商品呢。\x02\x03",

            "#03609F呵呵，还把你之前\x01",
            "想要的咪西玩偶带来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "哇！真的吗！？\x01",
            "太棒了！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_6_176A end

    def Function_7_183B(): pass

    label("Function_7_183B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_19B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195A")

    #C0085
    ChrTalk(
        0x101,
        (
            "#00000F哈罗德先生……\x01",
            "您来玛因兹了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xA,
        (
            "#03600F嗯，我把从\x01",
            "阿尔摩利卡村收购的\x01",
            "农作物送到这里。\x02\x03",

            "#03603F……镇上的各位还没有\x01",
            "从袭击时的噩梦中恢复，\x01",
            "仍然生活在恐惧之中。\x02\x03",

            "#03608F虽说没有民间人士丧生，\x01",
            "但那起袭击事件还是\x01",
            "对玛因兹镇造成了很深的伤害……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_19AE")

    label("loc_195A")


    #C0087
    ChrTalk(
        0xA,
        (
            "#03603F我不过是一名商人，\x01",
            "帮不上什么大忙……\x02\x03",

            "#03600F只想尽力让大家\x01",
            "重振精神。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19AE")

    Jump("loc_19FB")

    label("loc_19B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_19FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CE")
    Call(0, 6)
    Jump("loc_19FB")

    label("loc_19CE")


    #C0088
    ChrTalk(
        0xA,
        (
            "#03609F哈哈……\x01",
            "小孩子就应该\x01",
            "这样活泼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FB")

    TalkEnd(0xFE)
    Return()

    # Function_7_183B end

    SaveToFile()

Try(main)
