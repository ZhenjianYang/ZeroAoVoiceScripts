from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1440.bin",                # FileName
        "c1440",                    # MapName
        "c1440",                    # Location
        0x0031,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 49, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1440",                  # 0
        "亚修莉",                 # 1
        "金格",                   # 2
        "迪诺",                   # 3
        "寇奇",                   # 4
        "王",                     # 5
        "露茜",                   # 6
    ))

    AddCharChip((
        "chr/ch09200.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch06800.itc",                   # 02
        "chr/ch23000.itc",                   # 03
        "chr/ch24700.itc",                   # 04
        "chr/ch30800.itc",                   # 05
    ))

    DeclNpc(-2859,   0,       13750,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(5670,    29,      8649,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       15090,   225,  389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(2000,    0,       15090,   0,    389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(9640,    0,       850,     180,  389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10279,   0,       -550,    315,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)

    DeclEvent(0x0000, 0, 21,  9.899999618530273,     14.0,                  -0.5,                  16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.4749999046325684,   -7.0,                  0.10000000149011612,   1.0])

    DeclActor(4590,    0,       7540,    1000,    5670,    1500,    8650,    0x007E, 0,  6,  0x0000)
    DeclActor(-51020,  0,       6820,    1200,    -51020,  1150,    6820,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(596, 0)                                        # 0

    ScpFunction((
        "Function_0_254",          # 00, 0
        "Function_1_304",          # 01, 1
        "Function_2_4F2",          # 02, 2
        "Function_3_5BB",          # 03, 3
        "Function_4_660",          # 04, 4
        "Function_5_2291",         # 05, 5
        "Function_6_24BD",         # 06, 6
        "Function_7_24C1",         # 07, 7
        "Function_8_34B8",         # 08, 8
        "Function_9_375F",         # 09, 9
        "Function_10_37AB",        # 0A, 10
        "Function_11_39A9",        # 0B, 11
        "Function_12_39FD",        # 0C, 12
        "Function_13_3A57",        # 0D, 13
        "Function_14_3AA9",        # 0E, 14
        "Function_15_3BD7",        # 0F, 15
        "Function_16_3D46",        # 10, 16
        "Function_17_409D",        # 11, 17
        "Function_18_4504",        # 12, 18
        "Function_19_50AB",        # 13, 19
        "Function_20_53A7",        # 14, 20
        "Function_21_5B20",        # 15, 21
    ))


    def Function_0_254(): pass

    label("Function_0_254")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_28C"),
        (1, "loc_298"),
        (2, "loc_2A4"),
        (3, "loc_2B0"),
        (4, "loc_2BC"),
        (5, "loc_2C8"),
        (6, "loc_2D4"),
        (SWITCH_DEFAULT, "loc_2E0"),
    )


    label("loc_28C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_298")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_303")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_303")

    Return()

    # Function_0_254 end

    def Function_1_304(): pass

    label("Function_1_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_312")
    Jump("loc_4DB")

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_320")
    Jump("loc_4DB")

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32E")
    Jump("loc_4DB")

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346")
    SetChrFlags(0x8, 0x10)

    label("loc_346")

    Jump("loc_4DB")

    label("loc_34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_359")
    Jump("loc_4DB")

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A7")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, -2960, 20, 8530, 315)
    SetChrPos(0xD, -3010, 30, 7170, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A2")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_3A2")

    Jump("loc_4DB")

    label("loc_3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_441")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -2240, 20, 13000, 225)
    SetChrPos(0xB, -2630, 20, 11000, 0)
    SetChrPos(0xA, -3850, 0, 11830, 45)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_406")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_406")

    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, 4930, 0, 4600, 315)
    SetChrPos(0xD, 5930, 0, 4600, 315)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4DB")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_454")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4DB")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_491")
    SetChrPos(0x8, 1750, 30, 10220, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D")
    SetChrFlags(0x8, 0x10)

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C")
    SetChrFlags(0x9, 0x10)

    label("loc_48C")

    Jump("loc_4DB")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_49F")
    Jump("loc_4DB")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4AD")
    Jump("loc_4DB")

    label("loc_4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4BB")
    Jump("loc_4DB")

    label("loc_4BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D6")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_4D6")

    SetChrFlags(0x8, 0x10)

    label("loc_4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F1")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_4F1")

    Return()

    # Function_1_304 end

    def Function_2_4F2(): pass

    label("Function_2_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_505")
    OP_1B(0x0, 0x0, 0x13)

    label("loc_505")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_51E")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_524")

    label("loc_51E")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 7)), scpexpr(EXPR_END)), "loc_532")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_57B")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BA")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_5BA")

    Return()

    # Function_2_4F2 end

    def Function_3_5BB(): pass

    label("Function_3_5BB")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着《欢乐家庭午餐》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_65C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『行乐午餐盒饭』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_65C")

    TalkEnd(0xFF)
    Return()

    # Function_3_5BB end

    def Function_4_660(): pass

    label("Function_4_660")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_681")
    Call(0, 18)
    Return()

    label("loc_681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_693")
    Call(0, 20)
    Return()

    label("loc_693")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CD")

    #C0003
    ChrTalk(
        0xFE,
        (
            "总统被拘捕的同时，\x01",
            "竟然还出现了\x01",
            "那样的『大树』。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "结界已经消失，如今必须要对两大国\x01",
            "加强戒备，但偏偏在这种时期……\x01",
            "这片土地可真是多灾多难啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "呵呵……事情越来越有趣了。\x01",
            "既然如此，那我就以武器商人的\x01",
            "身份尽情大干一场吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#00300F哈哈，真是可靠啊。\x01",
            "……那就万事拜托了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_860")

    label("loc_7CD")


    #C0007
    ChrTalk(
        0xFE,
        (
            "在对两大国的戒备度越来越高的如今，\x01",
            "我的用武之地也会更多。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "呵呵……事情越来越有趣了啊。\x01",
            "既然如此，那我就以武器商人的\x01",
            "身份尽情大干一场吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_860")

    Jump("loc_228D")

    label("loc_865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B25")

    #C0009
    ChrTalk(
        0xFE,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "呵呵……好久不见了。\x01",
            "你们都挺有精神的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#00000F亚修莉女士，好久不见了。\x02\x03",

            "#00012F……面对这样的状况，\x01",
            "您依然如此镇定啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98F")

    #C0012
    ChrTalk(
        0x10A,
        (
            "#00600F我们一直都在委托她\x01",
            "协助警方的地下活动。\x02\x03",

            "#00603F她能提前预料到局势的发展，\x01",
            "也没什么好奇怪的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FE")

    label("loc_98F")


    #C0013
    ChrTalk(
        0xFE,
        "嗯，我早就隐约估计到事态会如此发展了。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "毕竟我一直都在协助达德利他们\x01",
            "进行地下活动，这没什么好奇怪的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FE")


    #C0015
    ChrTalk(
        0x102,
        "#00105F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        (
            "#00200F看来在民间也有不少\x01",
            "协助者呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#00300F反正你也早就习惯\x01",
            "和地下组织交易了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "呵呵，可以这么说。\x01",
            "我也因此而赚了不少钱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "……为了预防万一，\x01",
            "我们店正在做各种准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "之前刚从仓库中\x01",
            "翻出了不少好东西。\x01",
            "如果有需要，就去找金格交涉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 4)
    Jump("loc_B9A")

    label("loc_B25")


    #C0021
    ChrTalk(
        0xFE,
        (
            "……为了预防万一，\x01",
            "我们店正在做各种准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "之前刚从仓库中\x01",
            "翻出了不少好东西。\x01",
            "如果有需要，就去找金格交涉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9A")

    Jump("loc_228D")

    label("loc_B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF3")

    #C0023
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔独立吗……\x01",
            "哼，那个银行家居然做出了\x01",
            "这么惊人的决定。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "……呵呵，红毛，\x01",
            "你应该已经察觉到了吧？\x01",
            "那股正在逼近的战场气息。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#00301F……是啊，\x01",
            "两大国绝不会善罢甘休的……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "呵呵，我体内的武器商人之血\x01",
            "已经开始沸腾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "我也考虑过离开克洛斯贝尔，\x01",
            "不过，既然局势变成了这样，\x01",
            "我就见证到底吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D87")

    label("loc_CF3")


    #C0028
    ChrTalk(
        0xFE,
        (
            "战场的气息正在逼近……\x01",
            "呵呵，我体内的武器商人之血\x01",
            "已经开始沸腾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "我也考虑过离开克洛斯贝尔，\x01",
            "不过，既然局势变成了这样，\x01",
            "我就见证到底吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D87")

    Jump("loc_228D")

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1332")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1294")
    OP_4B(0xFE, 0xFF)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 0)

    #C0030
    ChrTalk(
        0xFE,
        "啊，是特别任务支援科啊。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "关于之前的袭击事件……\x01",
            "你们有什么看法？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00003F……怎么说呢。\x02\x03",

            "#00001F虽然还有很多问题\x01",
            "都没有搞清楚……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#00101F但是，引发事件的\x01",
            "是『赤色星座』，\x01",
            "这一点是毋庸置疑的。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#00203F如此一来，就会自然而然地联想到，\x01",
            "这是他们的雇主，\x01",
            "也就是帝国政府指使他们这样做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "嗯，市民间已经开始\x01",
            "流传这类传言了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "但他们撤退得也太干脆了，\x01",
            "这一点实在是让我无法释然……\x01",
            "哼，算了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#00305F说起来，你之前在这附近\x01",
            "和魔人化的瓦鲁多\x01",
            "大战了一场吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "哦，那个怪物果然\x01",
            "是瓦鲁多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "我当时真是陷入苦战了……\x01",
            "看来他是服用了那种药物吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "那种能把人变成怪物的药……\x01",
            "他到底是从哪里弄到手的？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        (
            "#10108F就是说啊……\x02\x03",

            "#10106F这方面的调查仍在继续，\x01",
            "但我们至今都没有查明\x01",
            "他得到那种药物的渠道……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "哈，连你们都没有搞清楚吗？\x01",
            "莫名其妙的事情实在是太多了，\x01",
            "真是让人心烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "总之，那起事件结束后，\x01",
            "自治州的治安问题被再次摆上了台面，\x01",
            "搞得我连生意都没法做了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "而且我长久以来的据点——\x01",
            "旧城区还变成了这个样子……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0045
    ChrTalk(
        0xFE,
        (
            "……看来我差不多也该\x01",
            "离开这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#00005F亚修莉女士……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x105,
        "#10303F……我可以理解你的想法。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#00300F反正你在别处\x01",
            "肯定也有不少人脉吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "嗯，但我还没有最终决定呢。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "毕竟还要考虑到金格，\x01",
            "我得尽快决定自己的立身之计。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x18D, 6)
    Jump("loc_132D")

    label("loc_1294")


    #C0051
    ChrTalk(
        0xFE,
        (
            "……看来我差不多也该\x01",
            "离开克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "莫名其妙的事情实在是太多了，\x01",
            "真是让人很不爽。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "但毕竟还要考虑到金格，\x01",
            "我得尽快决定自己的立身之计。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_132D")

    Jump("loc_228D")

    label("loc_1332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_13C8")

    #C0054
    ChrTalk(
        0xFE,
        (
            "如果你们准备和那群\x01",
            "危险人物正面交锋，\x01",
            "可一定要下定决心后再出发哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "你们应该也明白，\x01",
            "如果没有足够的觉悟，\x01",
            "肯定会被对方击溃的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228D")

    label("loc_13C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1466")

    #C0056
    ChrTalk(
        0xFE,
        (
            "虽说影响还不算太大，\x01",
            "但通商会议结束后，在克洛斯贝尔\x01",
            "订购外国货物比以前麻烦了一些。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "听说是因为两大国\x01",
            "开始在暗中限制了。\x01",
            "唉，饶了我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228D")

    label("loc_1466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1650")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A1")

    #C0058
    ChrTalk(
        0xFE,
        (
            "说起来，听说那些在通商会议上\x01",
            "发动袭击的『反移民政策主义』\x01",
            "残党已经在昨天被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "据说他们把黑月也卷了进去，\x01",
            "在列车上大闹了一场。\x01",
            "真是的，这些人做事就不能低调一点吗。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1570")

    #C0060
    ChrTalk(
        0x101,
        (
            "#00012F（不愧是亚修莉女士，\x01",
            "  消息真灵通啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1599")

    label("loc_1570")


    #C0061
    ChrTalk(
        0x101,
        "#00005F（原来还发生了那种事啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_1599")

    SetScenarioFlags(0x0, 0)
    Jump("loc_164B")

    label("loc_15A1")


    #C0062
    ChrTalk(
        0xFE,
        (
            "听说那些在通商会议上\x01",
            "发动袭击的『反移民政策主义』\x01",
            "残党已经在昨天被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "据说他们把黑月也卷了进去，\x01",
            "在列车上大闹了一场。\x01",
            "真是的，这些人做事就不能低调一点吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164B")

    Jump("loc_228D")

    label("loc_1650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_16C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166B")
    Call(0, 10)
    Jump("loc_16C0")

    label("loc_166B")


    #C0064
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "今天还真热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "这里什么时候变成\x01",
            "小鬼们的聚会所了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C0")

    Jump("loc_228D")

    label("loc_16C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16D3")
    Jump("loc_228D")

    label("loc_16D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1739")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16EE")
    Call(0, 5)
    Jump("loc_1734")

    label("loc_16EE")


    #C0066
    ChrTalk(
        0xFE,
        (
            "这么说，\x01",
            "是我自己搬走的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "看来我也上年纪了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1734")

    Jump("loc_228D")

    label("loc_1739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_196F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_18F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189B")

    #C0068
    ChrTalk(
        0xFE,
        (
            "有个家伙在我们店的屋顶上吵吵闹闹，\x01",
            "我本来想从这里\x01",
            "把他一炮轰下来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "但把屋顶打出个洞也不太好，\x01",
            "所以就交给金格处理了。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00006F如、如果您真的在市区里开炮，\x01",
            "我们就实在是不能坐视不管了。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "哼，所以我不是没那么干吗。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "说起来，那个金毛……\x01",
            "总觉得好像在哪里见过……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "算了，应该是我的心理作用吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18F0")

    label("loc_189B")


    #C0074
    ChrTalk(
        0xFE,
        (
            "说起来，那个金毛……\x01",
            "总觉得好像在哪里见过……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "算了，应该是我的心理作用吧。\x02",
    )

    CloseMessageWindow()

    label("loc_18F0")

    Jump("loc_196A")

    label("loc_18F5")


    #C0076
    ChrTalk(
        0xFE,
        (
            "各国首脑都聚集在了\x01",
            "克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "完全无法预测将会发生什么事啊，\x01",
            "不过，只要别把我牵扯到\x01",
            "什么事件里就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196A")

    Jump("loc_228D")

    label("loc_196F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1BC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2B")
    OP_4B(0xFE, 0xFF)

    #C0078
    ChrTalk(
        0xFE,
        "哎呀，这不是红毛吗。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "你已经回到\x01",
            "支援科了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#00300F是啊，托你的福。\x02\x03",

            "#00306F话说回来……\x01",
            "你的店里还是老样子，充满了火药味呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "哼，真不好意思。\x01",
            "我们这里是小本买卖，\x01",
            "没有细心清洁店面的闲工夫。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "对了，后巷那边……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "……唉，不说这些了。\x01",
            "多管闲事只会\x01",
            "给自己增添麻烦而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        (
            "#00303F（……哈，看来她\x01",
            "  已经调查过我和\x01",
            "  『赤色星座』的关系了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#00101F（到底知道了\x01",
            "  多少呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x14D, 4)
    Jump("loc_1BBF")

    label("loc_1B2B")


    #C0086
    ChrTalk(
        0xFE,
        (
            "话说回来，都怪那个什么通商会议，\x01",
            "平时从不来旧城区的警察\x01",
            "今天也跑来巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "如果他们跑到我的店里来，\x01",
            "要应付他们可是一件麻烦事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BBF")

    Jump("loc_228D")

    label("loc_1BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1FB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB3")
    OP_4B(0xFE, 0xFF)

    #C0088
    ChrTalk(
        0xFE,
        (
            "说起来……那个小不点\x01",
            "和红毛到哪里去了？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x109,
        "#10106F小、小不点和红毛……？\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#00000F啊……\x01",
            "您是指缇欧和兰迪吧？\x02\x03",

            "#00003F他们都还有其它的\x01",
            "工作需要完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        (
            "#00100F嗯，所以还要再过一段时间\x01",
            "才能回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "原来如此，我虽然不清楚\x01",
            "小不点有什么工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "但那个红毛，\x01",
            "现在多半是在协助警备队\x01",
            "进行复健训练吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0094
    ChrTalk(
        0x101,
        "#00005F您、您怎么会知道……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x105,
        "#10302F呵呵，还真是厉害呢。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "呵呵，既然干了这一行，\x01",
            "猜到这点事情不算什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        "不过………\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        "#00105F亚修莉女士？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        "啊……没什么，没什么。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "总之，能努力去完成自己的工作，\x01",
            "这是件好事。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "至于你们，如果不想被他\x01",
            "远远甩在后面，\x01",
            "就一定要努力锻炼自己哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#00000F好、好的。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x137, 6)
    Jump("loc_1FAC")

    label("loc_1EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F79")

    #C0103
    ChrTalk(
        0xFE,
        (
            "还有，别指望再从我这里\x01",
            "问出什么东西来了，\x01",
            "这是徒劳的。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "我不会告诉你们不确定的消息，\x01",
            "而且我也有义务为有交情的客人保密。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "总之，你们接下来就靠\x01",
            "自己的力量去追寻真相吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FAC")

    label("loc_1F79")


    #C0106
    ChrTalk(
        0xFE,
        (
            "总之，你们接下来就靠\x01",
            "自己的力量去追寻真相吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAC")

    Jump("loc_228D")

    label("loc_1FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_228D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222D")
    OP_4B(0xFE, 0xFF)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0107
    ChrTalk(
        0xFE,
        "哎呀，这不是特别任务支援科吗。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "有段时间没看见你们了呢，\x01",
            "都还挺精神的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#00009F哈哈……\x01",
            "好久不见。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)

    #C0110
    ChrTalk(
        0xFE,
        (
            "呵呵，我已经听到传闻了哦，\x01",
            "真没想到你会加入支援科啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "瓦吉·赫米斯菲亚，\x01",
            "这到底是怎么一回事啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x105,
        (
            "#10304F这个嘛，我也有我的打算啦。\x02\x03",

            "#10302F我们还是下次在『崔尼蒂』\x01",
            "边喝边聊吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "哼，也好。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "然后呢？\x01",
            "你们找我有什么事？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "要是想找从鲁巴彻流出的东西，\x01",
            "我这里倒是收集得挺齐全哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#00006F（她竟然还做了这种事……）\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        (
            "#00100F不，今天没什么特别的事，\x01",
            "不好意思，打扰您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "这样啊，\x01",
            "那你们就随便看看\x01",
            "店里的商品吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x137, 5)
    Jump("loc_228D")

    label("loc_222D")

    TurnDirection(0xFE, 0x105, 0)

    #C0119
    ChrTalk(
        0xFE,
        (
            "话说回来，瓦吉，你竟然\x01",
            "会加入特别任务支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "看来最近就要\x01",
            "下红雪了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)

    label("loc_228D")

    TalkEnd(0xFE)
    Return()

    # Function_4_660 end

    def Function_5_2291(): pass

    label("Function_5_2291")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x9, 0)

    #C0121
    ChrTalk(
        0x8,
        (
            "喂，金格。\x01",
            "你还记得昨天运来的\x01",
            "榴弹放到哪里去了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "我记得应该是\x01",
            "放到了这附近……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 0)

    #C0123
    ChrTalk(
        0x9,
        "妈妈，你不记得了吗？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "你说放在那里很碍事，\x01",
            "所以就亲手把那东西\x01",
            "搬到地下仓库了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0125
    ChrTalk(
        0x8,
        "哦哦，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "谢啦，金格，\x01",
            "养女儿就是贴心啊。\x02",
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

    #C0127
    ChrTalk(
        0x101,
        (
            "#00006F（只要忽略掉榴弹，\x01",
            "  这就是很普通的母女对话了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        (
            "#00200F（她们果然是一对\x01",
            "  非比寻常的母女啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_249A")
    OP_4C(0x9, 0xFF)

    label("loc_249A")

    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x87, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_5_2291 end

    def Function_6_24BD(): pass

    label("Function_6_24BD")

    Call(0, 7)
    Return()

    # Function_6_24BD end

    def Function_7_24C1(): pass

    label("Function_7_24C1")

    TalkBegin(0x9)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "交换（装备）\x01",      # 1
            "交换（回路）\x01",      # 2
            "交换（其它）\x01",      # 3
            "放弃\x01",              # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2554")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2554")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2574")
    OP_AF(0x8C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34AF")

    label("loc_2574")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2594")
    OP_AF(0x96)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34AF")

    label("loc_2594")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2631")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_25E0")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝14卷', 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AF(0xA3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝14卷', 0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25D8")
    ClearScenarioFlags(0x0, 1)

    label("loc_25D8")

    SetScenarioFlags(0x189, 5)

    label("loc_25DB")

    Jump("loc_2622")

    label("loc_25E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_25F0")
    OP_AF(0xA2)
    Jump("loc_2622")

    label("loc_25F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2600")
    OP_AF(0xA1)
    Jump("loc_2622")

    label("loc_2600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2610")
    OP_AF(0xA1)
    Jump("loc_2622")

    label("loc_2610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2620")
    OP_AF(0xA0)
    Jump("loc_2622")

    label("loc_2620")

    OP_AF(0xA0)

    label("loc_2622")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34AF")

    label("loc_2631")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2645")
    Jump("loc_34AF")

    label("loc_2645")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34AF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_END)), "loc_27BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_276C")

    #C0129
    ChrTalk(
        0x9,
        (
            "哦哦……\x01",
            "影丸的服饰果然\x01",
            "很威风啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "我记得仓库里应该有刀。\x01",
            "把那个也拿在手上就更完美了。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        (
            "让王和露茜都穿上这个，\x01",
            "然后打着玩吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#00006F这、这已经不能算是\x01",
            "小孩子的游戏了。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        (
            "#00200F影丸这个角色也被\x01",
            "微妙地扭曲了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27B6")

    label("loc_276C")


    #C0134
    ChrTalk(
        0x9,
        (
            "影丸的服饰果然\x01",
            "很威风啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x9,
        (
            "让王和露茜都穿上这个，\x01",
            "然后打着玩吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27B6")

    Jump("loc_2A1D")

    label("loc_27BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2872")

    #C0136
    ChrTalk(
        0x9,
        "客人，你知道黑猫吗？\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#00000F黑猫……？\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        (
            "#00200F……你指的莫非是\x01",
            "『影丸』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        "就是它～\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        "我正在寻找它的周边服饰呢。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        "你们帮我多收集一些吧～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x189, 6)
    Jump("loc_2A1D")

    label("loc_2872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B0")

    #C0142
    ChrTalk(
        0x9,
        "客人，你看到了那棵巨大的树了吗～？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x9,
        (
            "是不是很壮观～？\x01",
            "如果想把那棵树轰倒，\x01",
            "需要多少门导力炮呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0144
    ChrTalk(
        0x101,
        "#00006F（她看起来好兴奋……）\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        "#00106F（这孩子还是如此危险啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A1D")

    label("loc_29B0")


    #C0146
    ChrTalk(
        0x9,
        (
            "如果想把那棵树轰倒，\x01",
            "需要多少门导力炮呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "嘻嘻嘻……\x01",
            "不管有多少辆帝国战车，\x01",
            "恐怕也难以轰倒那棵树～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A1D")

    Jump("loc_34AF")

    label("loc_2A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2B87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B53")

    #C0148
    ChrTalk(
        0x9,
        "噢～来客人了吗？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            "外面现在好像很危险，\x01",
            "赶快买点东西护身吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "如果你想打飞大街上的那些铠甲兵，\x01",
            "那就要买些手榴弹了～\x02",
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

    #C0151
    ChrTalk(
        0x101,
        "#00006F（那好像已经超出了护身用品的范畴……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B82")

    label("loc_2B53")


    #C0152
    ChrTalk(
        0x9,
        (
            "外面现在好像很危险，\x01",
            "赶快买点东西护身吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B82")

    Jump("loc_34AF")

    label("loc_2B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2BF1")

    #C0153
    ChrTalk(
        0x9,
        (
            "我和妈妈商量过后，决定一起\x01",
            "留在克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        (
            "客人，你要是想买东西，\x01",
            "就和我说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_2BF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C6A")

    #C0155
    ChrTalk(
        0x9,
        (
            "大家还是老样子，\x01",
            "都在忙着进行重建工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        (
            "事关名誉，\x01",
            "我可要事先说清楚哦，\x01",
            "妈妈和我偶尔也会去帮忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_2C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D3F")

    #C0157
    ChrTalk(
        0x9,
        "呼～好困啊……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        (
            "昨天夜里，忽然来了宗紧急工作，\x01",
            "我和妈妈把仓库翻了个底朝天，\x01",
            "几乎没怎么睡。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x9,
        (
            "话说回来，妈妈竟然会接受\x01",
            "那么突然的订单。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x9,
        (
            "那位客人和妈妈的关系\x01",
            "有那么好吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D95")

    label("loc_2D3F")


    #C0161
    ChrTalk(
        0x9,
        (
            "话说回来，妈妈竟然会接受\x01",
            "那么突然的订单。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x9,
        (
            "那位客人和妈妈的关系\x01",
            "有那么好吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D95")

    Jump("loc_34AF")

    label("loc_2D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2DFA")

    #C0163
    ChrTalk(
        0x9,
        "讨厌，又在淅淅沥沥地下小雨～\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x9,
        (
            "既然要下雨，\x01",
            "索性就下一场\x01",
            "倾盆大雨才爽嘛～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_2DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2E62")
    OP_93(0x9, 0x10E, 0x0)

    #C0165
    ChrTalk(
        0x9,
        "那两个家伙还真是不长教训～\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "难道他们已经忘记之前\x01",
            "挨妈妈大巴掌的滋味了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_2E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2EC5")

    #C0167
    ChrTalk(
        0x9,
        (
            "哟，客人们。\x01",
            "你们不用介意\x01",
            "这两个家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x9,
        (
            "店里今天也有不少好东西，\x01",
            "来交换吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_2EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F4C")

    #C0169
    ChrTalk(
        0x9,
        "妈妈出去喝酒了～\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "她今天一大早就\x01",
            "忙着整理仓库的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "所以说要出去喝一杯，\x01",
            "好好慰劳一下自己。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F83")

    label("loc_2F4C")


    #C0172
    ChrTalk(
        0x9,
        (
            "妈妈虽然对店里的客人很凶，\x01",
            "但是对自己可是很好的～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F83")

    Jump("loc_34AF")

    label("loc_2F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA3")
    Call(0, 5)
    Jump("loc_2FF3")

    label("loc_2FA3")

    TurnDirection(0x9, 0x0, 0)

    #C0173
    ChrTalk(
        0x9,
        "妈妈有时候也会犯迷糊的～\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x9,
        (
            "嘻嘻嘻……\x01",
            "没有我在，果然还是不行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF3")

    Jump("loc_34AF")

    label("loc_2FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3114")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_306C")

    #C0175
    ChrTalk(
        0x9,
        (
            "那个金毛，\x01",
            "明明从屋顶上掉下来了，\x01",
            "却还是那么有精神呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x9,
        (
            "看来我应该\x01",
            "踢得再用力一些。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310F")

    label("loc_306C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E1")

    #C0177
    ChrTalk(
        0x9,
        (
            "今天上午，我和妈妈关了店，\x01",
            "一起去观看了揭幕式。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x9,
        (
            "那栋大楼\x01",
            "真是巨大啊～\x01",
            "连我都吓了一大跳。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_310F")

    label("loc_30E1")


    #C0179
    ChrTalk(
        0x9,
        (
            "那栋大楼\x01",
            "真是巨大啊～\x01",
            "连我都吓了一大跳。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310F")

    Jump("loc_34AF")

    label("loc_3114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31C9")

    #C0180
    ChrTalk(
        0x9,
        (
            "新来的修女姐姐\x01",
            "让我去听她读书……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x9,
        (
            "我像对待以前的那些修女一样，直接拒绝了。\x01",
            "但她竟然留了其它的书给我，说是作业。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x9,
        "真是个不能小瞧的家伙啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3223")

    label("loc_31C9")


    #C0183
    ChrTalk(
        0x9,
        (
            "那个修女姐姐还真是个\x01",
            "不能小瞧的家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        (
            "算了，反正有空……\x01",
            "就来读读这本书吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3223")

    Jump("loc_34AF")

    label("loc_3228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3416")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3243")
    Call(0, 8)
    Jump("loc_3411")

    label("loc_3243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339F")

    #C0185
    ChrTalk(
        0x9,
        (
            "这讨厌的雨，搞得到处都湿淋淋的，\x01",
            "烦死人了啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x9,
        (
            "用导力炮向天空来一炮，\x01",
            "蒸发掉积雨云，应该就会放晴了吧？\x02",
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

    #C0187
    ChrTalk(
        0x101,
        "#00005F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        (
            "#00106F（到底该怎么说\x01",
            "  这孩子呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x109,
        (
            "#10106F（嗯……让人有点\x01",
            "  不知该如何接话。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3411")

    label("loc_339F")


    #C0190
    ChrTalk(
        0x9,
        (
            "这讨厌的雨，搞得到处都湿淋淋的，\x01",
            "真是烦死人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x9,
        (
            "用导力炮向天空来一炮，\x01",
            "蒸发掉积雨云，应该就会放晴了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3411")

    Jump("loc_34AF")

    label("loc_3416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3431")
    Call(0, 8)
    Jump("loc_34AF")

    label("loc_3431")


    #C0192
    ChrTalk(
        0x9,
        (
            "我想你们应该明白，\x01",
            "我们只向客人们提供\x01",
            "交换服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        (
            "药品、回路、装饰品……\x01",
            "其它东西也姑且准备了一些，\x01",
            "你们可以看一下～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34AF")

    Jump("loc_24D8")

    label("loc_34B4")

    TalkEnd(0x9)
    Return()

    # Function_7_24C1 end

    def Function_8_34B8(): pass

    label("Function_8_34B8")


    #C0194
    ChrTalk(
        0x9,
        "哟，客人，好久不见了～\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x9,
        (
            "虽然不能把武器卖给你们，\x01",
            "不过可以交换些别的东西哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "普通货品的存货\x01",
            "也比之前充足了不少～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_355C")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_355C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3582")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3582")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35A8")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_35A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35CE")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_35CE")

    Sleep(1000)

    #C0197
    ChrTalk(
        0x101,
        "#00006F你的话还是一样充满危险气息啊。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x109,
        (
            "#10106F我说啊，我们真的可以\x01",
            "在这家店里买东西吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#00100F至、至少放在店面上交易的商品，\x01",
            "好像都不是违法的……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，不涉及太深的话，\x01",
            "我想应该就没什么问题哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x9,
        (
            "哦，对了，\x01",
            "我们店最近扩大生意范围了～\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "你们要是有什么好吃的东西，\x01",
            "就带过来给我吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x9,
        (
            "我会拿好东西\x01",
            "和你们交换的。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#00012F哈哈，知道了，\x01",
            "我们还会再来的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x137, 7)
    Return()

    # Function_8_34B8 end

    def Function_9_375F(): pass

    label("Function_9_375F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3774")
    Call(0, 10)
    Jump("loc_37A7")

    label("loc_3774")


    #C0205
    ChrTalk(
        0xFE,
        (
            "十、十万米拉吗……\x01",
            "我从来没见过这么贵的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A7")

    TalkEnd(0xFE)
    Return()

    # Function_9_375F end

    def Function_10_37AB(): pass

    label("Function_10_37AB")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0206
    ChrTalk(
        0x8,
        (
            "哦，你们说的是\x01",
            "这个艾尼格玛吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x8,
        (
            "看，把耳朵贴上去，\x01",
            "还能当通讯工具使用呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        "是、是啊，的确如此。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xA,
        (
            "说起来，警察和游击士……\x01",
            "还有瓦吉都在用这东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xA,
        (
            "亚修莉老板，顺便问一下。\x01",
            "这个东西在市场上的价格\x01",
            "大概是多少呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x8,
        (
            "嗯，因为一般都是定制品，\x01",
            "所以价格比较高。\x01",
            "最少也要十万米拉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "不过，我们店里的东西来路特别，\x01",
            "可以稍微便宜一些……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x8,
        (
            "莫非你们想买\x01",
            "这玩意吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xB,
        "十、十万……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xA,
        "可、可以买十万个一米拉的巧克力了……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "哈哈，你们的\x01",
            "反应还真有趣啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x16E, 5)
    Return()

    # Function_10_37AB end

    def Function_11_39A9(): pass

    label("Function_11_39A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39BE")
    Call(0, 10)
    Jump("loc_39F9")

    label("loc_39BE")


    #C0217
    ChrTalk(
        0xFE,
        (
            "可以买十万个一米拉的巧克力……\x01",
            "十、十万个该有多少啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39F9")

    TalkEnd(0xFE)
    Return()

    # Function_11_39A9 end

    def Function_12_39FD(): pass

    label("Function_12_39FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A1B")
    Call(0, 14)
    Jump("loc_3A42")

    label("loc_3A1B")


    #C0218
    ChrTalk(
        0xFE,
        (
            "可恶，金格的妈妈\x01",
            "还是这么可怕啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A42")

    Jump("loc_3A53")

    label("loc_3A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A53")
    Call(0, 15)

    label("loc_3A53")

    TalkEnd(0xFE)
    Return()

    # Function_12_39FD end

    def Function_13_3A57(): pass

    label("Function_13_3A57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A75")
    Call(0, 14)
    Jump("loc_3A94")

    label("loc_3A75")


    #C0219
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "作战又失败了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A94")

    Jump("loc_3AA5")

    label("loc_3A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3AA5")
    Call(0, 15)

    label("loc_3AA5")

    TalkEnd(0xFE)
    Return()

    # Function_13_3A57 end

    def Function_14_3AA9(): pass

    label("Function_14_3AA9")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0220
    ChrTalk(
        0xC,
        (
            "哇，这个不是导力枪吗！\x01",
            "真帅呀～\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xD,
        (
            "王～\x01",
            "这个可以用来烤肉吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xC,
        (
            "嗯～应该没问题吧？\x01",
            "嘻嘻，我们下次偷偷试一试吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x8,
        "……喂，小鬼头们。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 0)

    #C0224
    ChrTalk(
        0x8,
        (
            "你们不要随便\x01",
            "碰那边的东西哦。（眼放寒光）\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        "好、好的……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xD,
        (
            "嘻嘻……\x01",
            "金格的妈妈\x01",
            "真有压迫力啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_93(0x8, 0x0, 0x0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_14_3AA9 end

    def Function_15_3BD7(): pass

    label("Function_15_3BD7")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC6")

    #C0227
    ChrTalk(
        0xC,
        (
            "喂，金格。\x01",
            "我们来找你玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xC,
        "快给我们点东西～\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x9,
        (
            "哦，是你们啊。\x01",
            "带钱了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xC,
        (
            "嘻嘻，本来有一点，\x01",
            "但昨天已经花完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xD,
        (
            "嘻嘻……\x01",
            "拿去吃肉了哦，吃肉。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x9,
        (
            "唉～你们还是老样子，\x01",
            "一点计划性都没有。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D39")

    label("loc_3CC6")


    #C0233
    ChrTalk(
        0xC,
        (
            "别再啰嗦啦，\x01",
            "快给我们点东西，金格。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x9,
        (
            "嗯～？你们看起来还\x01",
            "蛮有精神的，所以不行～\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xD,
        (
            "嘻嘻……\x01",
            "金格真冷血。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D39")

    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_15_3BD7 end

    def Function_16_3D46(): pass

    label("Function_16_3D46")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_68(0, 1100, 12800, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -600, 0, 1800, 0)
    SetChrPos(0x102, 600, 0, 1800, 0)
    SetChrPos(0x109, 900, 0, 700, 0)
    SetChrPos(0x105, -900, 0, 700, 0)
    OP_68(0, 1100, 2800, 6000)
    MoveCamera(45, 19, 0, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0236
    ChrTalk(
        0x101,
        (
            "#12P#00001F唔……这家店看上去\x01",
            "还是那么可疑啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    #C0237
    ChrTalk(
        0x102,
        (
            "#6P#00108F又是小金格在\x01",
            "看店呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x109,
        (
            "#12P#10103F这家店的老板就是\x01",
            "克洛斯贝尔市的几名黑市掮客之一吧。\x02\x03",

            "#10101F我在警备队里听说过，\x01",
            "这里连武器弹药都在销售……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x105,
        (
            "#12P#10304F不过，跟其他同行比起来，\x01",
            "这位店主还算是比较有良心的。\x02\x03",

            "#10300F是个很厉害的女中豪杰。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F47():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F47)
    Sleep(50)

    def lambda_3F57():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3F57)
    Sleep(50)
    TurnDirection(0x102, 0x105, 500)

    #C0240
    ChrTalk(
        0x101,
        (
            "#5P#00003F我也这样觉得……\x02\x03",

            "#00001F总之，如果来这里有事，\x01",
            "就赶快办完吧。\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    SetChrName("")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※在交换店『纳因瓦利』，\x01",
            "　可以用特定的物品去换取\x01",
            "　比较稀有的道具。\x02\x03",

            "※与站在前台的金格交谈，\x01",
            "  选择『交换』，就会出现\x01",
            "　交易菜单，可进行道具交换。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 0, 0, 1000, 0)
    SetScenarioFlags(0x138, 4)
    EventEnd(0x5)
    Return()

    # Function_16_3D46 end

    def Function_17_409D(): pass

    label("Function_17_409D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, -600, 0, 1800, 0)
    SetChrPos(0x102, 600, 0, 1800, 0)
    SetChrPos(0x109, 900, 0, 700, 0)
    SetChrPos(0x105, -900, 0, 700, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43EF")
    OP_68(0, 1100, 12800, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(0, 1100, 2800, 6000)
    MoveCamera(45, 19, 0, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0242
    ChrTalk(
        0x101,
        (
            "#12P#00001F唔……这家店看上去\x01",
            "还是那么可疑啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    #C0243
    ChrTalk(
        0x102,
        (
            "#6P#00108F又是小金格在\x01",
            "看店呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x109,
        (
            "#12P#10103F这家店的老板就是\x01",
            "克洛斯贝尔市的几名黑市掮客之一吧。\x02\x03",

            "#10101F我在警备队里听说过，\x01",
            "这里连武器弹药都在销售……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x105,
        (
            "#12P#10304F不过，跟其他同行比起来，\x01",
            "这位店主还算是比较有良心的。\x02\x03",

            "#10300F是个很厉害的女中豪杰。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42A8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42A8)
    Sleep(50)

    def lambda_42B8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_42B8)
    Sleep(50)
    TurnDirection(0x102, 0x105, 500)

    #C0246
    ChrTalk(
        0x101,
        (
            "#5P#00003F我也这样觉得……\x02\x03",

            "#00001F总之，先去向亚修莉女士\x01",
            "询问一下那个男人的事情吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0247
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※在交换店『纳因瓦利』，\x01",
            "　可以用特定的物品去换取\x01",
            "　比较稀有的道具。\x02\x03",

            "※与站在前台的金格交谈，\x01",
            "  选择『交换』，就会出现\x01",
            "　交易菜单，可进行道具交换。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_44EA")

    label("loc_43EF")

    OP_68(0, 1100, 2800, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0248
    ChrTalk(
        0x101,
        (
            "#12P#00006F唔……这家店看上去\x01",
            "还是那么可疑啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        (
            "#12P#00106F是啊，不管来过多少次，\x01",
            "还是没法习惯……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0250
    ChrTalk(
        0x102,
        (
            "#11P#00101F总之，先向亚修莉女士\x01",
            "询问一下那个男人的事情吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_44EA")

    SetChrPos(0x0, 0, 0, 1000, 0)
    SetScenarioFlags(0x138, 5)
    SetScenarioFlags(0x128, 3)
    EventEnd(0x5)
    Return()

    # Function_17_409D end

    def Function_18_4504(): pass

    label("Function_18_4504")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-2860, 1000, 12800, 0)
    MoveCamera(37, 22, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -3100, 20, 11800, 0)
    SetChrPos(0x102, -4400, 20, 11000, 45)
    SetChrPos(0x109, -2900, 20, 10800, 0)
    SetChrPos(0x105, -1700, 20, 12000, 315)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47F4")

    #C0251
    ChrTalk(
        0x8,
        "#5P哎呀，这不是特别任务支援科吗。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x8,
        (
            "#5P有段时间没看见你们了呢，\x01",
            "都还挺精神的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        (
            "#12P#00012F哈哈……\x01",
            "好久不见。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)
    Sleep(300)

    #C0254
    ChrTalk(
        0x8,
        (
            "#5P呵呵，我已经听到传闻了哦，\x01",
            "真没想到你会加入支援科啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        (
            "#5P瓦吉·赫米斯菲亚，\x01",
            "这到底是怎么一回事啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x105,
        (
            "#10304F这个嘛，我也有我的打算啦。\x02\x03",

            "#10302F我们还是下次在『崔尼蒂』\x01",
            "边喝边聊吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        "#5P哼，也好。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    #C0258
    ChrTalk(
        0x8,
        (
            "#5P然后呢？\x01",
            "你们找我有什么事？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x8,
        (
            "#5P要是想找从鲁巴彻流出的东西，\x01",
            "我这里倒是收集得挺齐全哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        "#12P#00006F（她竟然还做了这种事……）\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x102,
        (
            "#6P#00103F其实我们有些事情\x01",
            "想询问您。\x02\x03",

            "#00100F因为您曾经是名武器商人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x137, 5)
    Jump("loc_487A")

    label("loc_47F4")


    #C0262
    ChrTalk(
        0x8,
        "#5P嗯？是特别任务支援科啊。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x8,
        "#5P找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        (
            "#6P#00103F其实我们有些事情\x01",
            "想询问您。\x02\x03",

            "#00100F因为您曾经是名武器商人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_487A")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0265
    ChrTalk(
        0x8,
        "#5P哦？是什么事？\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x8,
        (
            "#5P是有关曹他们准备开始\x01",
            "正式行动的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#12P#00003F您果然已经知道了啊。\x02\x03",

            "#00001F不过，我们想问的\x01",
            "并不是这件事……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_64(0x8)

    #C0268
    ChrTalk(
        0x8,
        "#5P独眼……而且是红色头发的壮汉吗……\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x8,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#12P#00001F您有什么头绪吗？\x02\x03",

            "我们觉得他肯定是\x01",
            "地下世界的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#5P我的确知道几个\x01",
            "符合这描述的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x8,
        (
            "#5P不过，会在这种时候来\x01",
            "克洛斯贝尔的，恐怕只有……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x8,
        "#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x102,
        "#6P#00108F怎、怎么了……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x105,
        (
            "#10305F哦？莫非想到了某个\x01",
            "极其危险的人物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x8,
        "#5P怎么说呢……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x8,
        (
            "#5P我想到的只是\x01",
            "最坏的可能性而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x8,
        (
            "#5P如果真是如此，那绝对是你们\x01",
            "无法应付的人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x102,
        "#6P#00101F那么厉害吗……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x109,
        (
            "#12P#10101F果、果然是猎兵\x01",
            "或恐怖分子吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        "#5P呵呵，这个嘛。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "#5P如果真是那个男人的话，\x01",
            "他和我也算有点交情。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x8,
        "#5P我就不好再多说些什么了。\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x109,
        "#12P#10107F可、可是……！\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#12P#00006F要是猎兵倒也罢了，\x01",
            "但如果是恐怖分子，我们绝不能放任不管。\x02\x03",

            "#00003F即使是克洛斯贝尔，\x01",
            "对于恐怖活动也是有相应的法律的。\x02\x03",

            "#00013F所以，能否请您提供\x01",
            "最低限度的情报？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        "#6P#00108F罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x8,
        "#5P呵呵，真不错啊。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x8,
        (
            "#5P你是盖伊的弟弟吧？\x01",
            "现在这个眼神真不错。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0289
    ChrTalk(
        0x101,
        (
            "#12P#00005F亚修莉女士，\x01",
            "您认识我大哥吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "#5P虽说达德利现在也会\x01",
            "偶尔来这里露个脸……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x8,
        (
            "#5P但在以前，会有闲情逸致\x01",
            "跑到旧城区这种偏僻地方来的\x01",
            "警察，也只有那家伙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        "#5P失去了一个有趣的男人啊。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        "#12P#00008F………………………………\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x8,
        (
            "#5P看在那笨蛋的份上，\x01",
            "我就稍微透露一些吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x8,
        (
            "#5P我想到的那个最棘手的家伙，\x01",
            "并不是恐怖分子。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x8,
        (
            "#5P不过，那却是如同食人虎\x01",
            "一般危险的男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x109,
        "#12P#10108F食、食人虎……\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x105,
        (
            "#10306F哎呀呀……\x01",
            "这实在是最可怕的对手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x8,
        (
            "#5P不过，也未必\x01",
            "就是他呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x8,
        (
            "#5P你们看到的那个男人，\x01",
            "当时是孤身一人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x8,
        (
            "#5P那家伙在大多数时候\x01",
            "都会带着部下一起行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        "#12P#00005F是、是吗？\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x102,
        (
            "#6P#00101F也就是说……\x01",
            "他是和军队有关的人物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x8,
        "#5P呵呵，只能告诉你们这么多了。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x8,
        (
            "#5P接下来的事，你们就亲自\x01",
            "去调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        "#12P#00006F……我明白了。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        "#6P#00104F非常感谢您提供情报。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -2860, 20, 11750, 180)
    SetScenarioFlags(0x128, 4)
    OP_1B(0x0, 0x0, 0x13)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_4504 end

    def Function_19_50AB(): pass

    label("Function_19_50AB")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(300, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_68(0, 1200, 500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    Sleep(500)
    OP_68(5100, 1200, 8100, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(150)

    #C0308
    ChrTalk(
        0x9,
        "#5P讨厌，又在淅淅沥沥地下小雨～\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(300)

    #C0309
    ChrTalk(
        0x9,
        (
            "#11P对了，妈妈，昨天送到的东西，\x01",
            "不需要拆封吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x0)

    #C0310
    ChrTalk(
        0x8,
        (
            "嗯，反正天气很差，\x01",
            "不用急着开封。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x8,
        "……比起这个，金格。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        (
            "你昨天上街的时候，\x01",
            "有没有看见什么奇怪的家伙？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x9,
        (
            "#11P奇怪的家伙？\x01",
            "看见了很多哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x9,
        (
            "#11P有一身度假装扮的年轻男人，\x01",
            "还有买了一大堆面包，\x01",
            "堆得像山一样高的修女姐姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x9,
        "#11P对了，瓦吉也是个奇怪的家伙呢～\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x8,
        "这样啊，那没事了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(-2860, 1200, 13750, 3500)
    MoveCamera(15, 26, 0, 3500)
    OP_6F(0x79)
    OP_64(0x8)
    Sleep(500)

    #C0317
    ChrTalk(
        0x8,
        "#5P（……算了，是我想太多了吧。）\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "#5P（要是那家伙真的来了，\x01",
            "  肯定会把女儿带在身边吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetScenarioFlags(0x22, 0)
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_50AB end

    def Function_20_53A7(): pass

    label("Function_20_53A7")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-2860, 1000, 12800, 0)
    MoveCamera(37, 22, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -3100, 20, 11800, 0)
    SetChrPos(0x102, -4400, 20, 11000, 45)
    SetChrPos(0x103, -3700, 20, 10500, 0)
    SetChrPos(0x109, -2600, 20, 10800, 0)
    SetChrPos(0x105, -1900, 20, 12000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0319
    ChrTalk(
        0x8,
        "#5P哎呀……\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x8,
        (
            "#5P……真是不简单啊，\x01",
            "这么快就找到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        (
            "#12P#00001F言下之意……\x01",
            "兰迪果然来过这里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        (
            "#5P嗯，他昨天晚上联系过我，\x01",
            "然后今天一大早就来提货了。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x8,
        (
            "#5P他还叮嘱我说，如果你们找了过来，\x01",
            "千万要替他保密。\x01",
            "但我可没有这种义务。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x105,
        "#10309F哈哈，说的没错。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x102,
        (
            "#6P#00101F请问……兰迪到底\x01",
            "订了什么东西？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x103,
        "#12P#00201F是导力式的来复枪吗？\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x8,
        (
            "#5P不，他订的可不是\x01",
            "那么正常的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x8,
        (
            "#5P炸裂弹、穿甲弹和榴弹\x01",
            "之类的东西就不用说了，\x01",
            "他连旧式火药弹药都订了……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        (
            "#5P几乎把我们店里的\x01",
            "存货都买光了。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        (
            "#5P另外，他还买了一部流进黑市，\x01",
            "尚未登记的『艾尼格玛Ⅱ』。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#12P#00006F原来如此……\x02\x03",

            "#00008F……还真是准备周到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        (
            "#12P#00206F是啊……如果使用未登录的艾尼格玛，\x01",
            "我们就查不出他的号码了。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x109,
        (
            "#12P#10105F不过，他并没有购买\x01",
            "重型火器吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        (
            "#5P嗯，虽然我们店里也有不少\x01",
            "威力强劲的导力式、火药式\x01",
            "来复枪……\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x8,
        (
            "#5P但终究还是入不了『赤色星座』\x01",
            "下任团长的法眼啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0336
    ChrTalk(
        0x101,
        "#12P#00011F亚修莉女士……\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x102,
        "#6P#00106F您已经知道了吗……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#5P哈，那当然。\x01",
            "干我们这行的，情报就是生命啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x8,
        (
            "#5P看样子，他是打算出其不意地\x01",
            "突袭老巢……\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x8,
        (
            "#5P但『赤色战鬼』和\x01",
            "『血腥谢莉』可都是\x01",
            "彻头彻尾的怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x8,
        (
            "#5P像他那种半桶水的原猎兵，\x01",
            "根本就是去白白送死。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        "#12P#00201F……不会的。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        (
            "#12P#00013F我们绝不会让\x01",
            "那样的事情发生。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，他们从一大早开始\x01",
            "就一直是这个样子。\x02\x03",

            "#10302F你就算出言挑拨，也是白费力气哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x8,
        "#5P哎呀呀，看来正如你所说。\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x8,
        (
            "#5P其实，就算那小子死了，\x01",
            "和我也没有多大关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "#5P但减少一位老顾客也不是什么有趣的事。\x01",
            "你们就努力去救他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x109,
        "#12P#10101F是……！\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        "#6P#00103F多谢您提供情报。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -2860, 20, 11750, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x165, 6)
    OP_29(0xAA, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_20_53A7 end

    def Function_21_5B20(): pass

    label("Function_21_5B20")

    EventBegin(0x1)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BDA")

    #C0350
    ChrTalk(
        0x9,
        "你们想进仓库吗？\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x9,
        (
            "嗯……\x01",
            "算了，既然是你们几个，我就不管了。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x9,
        (
            "不过，千万别乱碰奇怪的东西哦～\x01",
            "死了我可不负责～\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        "#00012F……多、多谢关心。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x189, 7)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_5CAB")

    label("loc_5BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C51")

    #C0354
    ChrTalk(
        0x9,
        (
            "……喂，客人，\x01",
            "你们逃不过我的眼睛哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x9,
        (
            "那边是地下仓库，\x01",
            "外人禁止入内。\x01",
            "要买东西就在这里买！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5CAB")

    label("loc_5C51")


    #C0356
    ChrTalk(
        0x9,
        (
            "喂，客人？\x01",
            "你没听到我的话吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x9,
        (
            "我都说了不准进地下仓库了！！\x01",
            "要买东西就在这里买！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CAB")

    Sleep(50)
    SetChrPos(0x0, 9940, 0, 11910, 180)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_21_5B20 end

    SaveToFile()

Try(main)
