from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1020.bin",                # FileName
        "t1020",                    # MapName
        "t1020",                    # Location
        0x0095,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 149, 0, 3, 0, 4],
    )

    BuildStringList((
        "t1020",                  # 0
        "艾丽洁",                 # 1
        "青年",                   # 2
        "游客",                   # 3
        "游客",                   # 4
        "女性",                   # 5
        "女孩",                   # 6
        "店员",                   # 7
    ))

    AddCharChip((
        "chr/ch23600.itc",                   # 00
        "chr/ch26700.itc",                   # 01
        "chr/ch21600.itc",                   # 02
        "chr/ch21100.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch33200.itc",                   # 05
        "chr/ch25900.itc",                   # 06
    ))

    DeclNpc(-24909,  0,       5570,    90,   257,  0x0, 0,   5,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(100139,  0,       18219,   0,    385,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4190,    0,       13079,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(97510,   0,       5429,    270,  385,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-23930,  0,       11470,   0,    385,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-22840,  0,       10689,   315,  401,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-18940,  0,       12609,   180,  385,  0x0, 0,   6,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 14,  26.5,                  8.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -8.833333969116211,    -0.800000011920929,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 15,  8.5,                   8.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.8333334922790527,   -0.800000011920929,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 15,  -11.0,                 8.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.6666667461395264,    -0.800000011920929,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 13,  -19.030000686645508,   11.899999618530273,    -1.0,                  2.4964001178741455,    [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.6329113841056824,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   9.515000343322754,     -7.53164529800415,     0.20000000298023224,   1.0])

    DeclActor(27660,   0,       10070,   1200,    27660,   1500,    10070,   0x007C, 0,  18, 0x0000)
    DeclActor(19000,   0,       11850,   2000,    19000,   1000,    11850,   0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_388",          # 00, 0
        "Function_1_440",          # 01, 1
        "Function_2_46B",          # 02, 2
        "Function_3_496",          # 03, 3
        "Function_4_566",          # 04, 4
        "Function_5_5CB",          # 05, 5
        "Function_6_6C0",          # 06, 6
        "Function_7_6F8",          # 07, 7
        "Function_8_815",          # 08, 8
        "Function_9_90E",          # 09, 9
        "Function_10_9EB",         # 0A, 10
        "Function_11_A38",         # 0B, 11
        "Function_12_A71",         # 0C, 12
        "Function_13_B64",         # 0D, 13
        "Function_14_FA0",         # 0E, 14
        "Function_15_1308",        # 0F, 15
        "Function_16_169F",        # 10, 16
        "Function_17_18B0",        # 11, 17
        "Function_18_18FB",        # 12, 18
    ))


    def Function_0_388(): pass

    label("Function_0_388")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3C8"),
        (1, "loc_3D4"),
        (2, "loc_3E0"),
        (3, "loc_3EC"),
        (4, "loc_3F8"),
        (5, "loc_404"),
        (6, "loc_410"),
        (SWITCH_DEFAULT, "loc_41C"),
    )


    label("loc_3C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_404")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_410")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_41C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_428")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_43F")

    Return()

    # Function_0_388 end

    def Function_1_440(): pass

    label("Function_1_440")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46A")
    OP_94(0xFE, 0x17D0E, 0x3F0C, 0x19154, 0x47A4, 0x3E8)
    Sleep(150)
    Jump("Function_1_440")

    label("loc_46A")

    Return()

    # Function_1_440 end

    def Function_2_46B(): pass

    label("Function_2_46B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_495")
    OP_94(0xFE, 0x3AC, 0x28D2, 0x12FC, 0x37E6, 0x3E8)
    Sleep(300)
    Jump("Function_2_46B")

    label("loc_495")

    Return()

    # Function_2_46B end

    def Function_3_496(): pass

    label("Function_3_496")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B8")
    Event(0, 15)

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4C6")
    Jump("loc_565")

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4D4")
    Jump("loc_565")

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_4E2")
    Jump("loc_565")

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4F0")
    Jump("loc_565")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_4FE")
    Jump("loc_565")

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_52E")
    SetChrPos(0x8, -13780, 0, 6020, 90)
    SetChrPos(0xA, -12240, 0, 6020, 270)
    Jump("loc_565")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_55C")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_565")

    label("loc_55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_565")

    label("loc_565")

    Return()

    # Function_3_496 end

    def Function_4_566(): pass

    label("Function_4_566")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_588")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A8")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_5A8")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C4")
    ClearMapObjFlags(0x3, 0x10)
    OP_66(0x1, 0x1)

    label("loc_5C4")

    ClearMapObjFlags(0x2, 0x10)
    Return()

    # Function_4_566 end

    def Function_5_5CB(): pass

    label("Function_5_5CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_5DC")
    Jump("loc_6BC")

    label("loc_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_5EA")
    Jump("loc_6BC")

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_5F8")
    Jump("loc_6BC")

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_606")
    Jump("loc_6BC")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_614")
    Jump("loc_6BC")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_65C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F")
    Call(0, 8)
    Jump("loc_657")

    label("loc_62F")


    #C0001
    ChrTalk(
        0xFE,
        "……真是的，一点教养都没有的游客。\x02",
    )

    CloseMessageWindow()

    label("loc_657")

    Jump("loc_6BC")

    label("loc_65C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_6B3")

    #C0002
    ChrTalk(
        0xFE,
        (
            "呼……真是的，\x01",
            "这里无论何时都很混乱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "想买个东西都那么辛苦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BC")

    label("loc_6B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6BC")

    label("loc_6BC")

    TalkEnd(0xFE)
    Return()

    # Function_5_5CB end

    def Function_6_6C0(): pass

    label("Function_6_6C0")

    TalkBegin(0xFE)

    #C0004
    ChrTalk(
        0xFE,
        (
            "唔啊啊啊啊！！！\x01",
            "等一下啊，咪西————！！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_6C0 end

    def Function_7_6F8(): pass

    label("Function_7_6F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_709")
    Jump("loc_811")

    label("loc_709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_717")
    Jump("loc_811")

    label("loc_717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_725")
    Jump("loc_811")

    label("loc_725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_733")
    Jump("loc_811")

    label("loc_733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_741")
    Jump("loc_811")

    label("loc_741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_7A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75C")
    Call(0, 8)
    Jump("loc_79E")

    label("loc_75C")


    #C0005
    ChrTalk(
        0xFE,
        (
            "怎么会这样……\x01",
            "仅仅是有钱的话，\x01",
            "是无法吸引这里的女孩子的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79E")

    Jump("loc_811")

    label("loc_7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_808")

    #C0006
    ChrTalk(
        0xFE,
        (
            "不愧是高级疗养地……\x01",
            "有好多大小姐类型\x01",
            "的女孩子啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "好……不如去\x01",
            "尝试搭讪吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_811")

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_811")

    label("loc_811")

    TalkEnd(0xFE)
    Return()

    # Function_7_6F8 end

    def Function_8_815(): pass

    label("Function_8_815")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0xA, 0x8, 0)

    #C0008
    ChrTalk(
        0xA,
        (
            "嘿，小姐……\x01",
            "不介意的话，一起去\x01",
            "那边的西餐厅吃个饭如何啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xA,
        (
            "放心，我带了\x01",
            "足够的米拉哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "……不用了，\x01",
            "我没有理由\x01",
            "让你请客哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "而且，要论米拉数量的话，\x01",
            "我带的也许\x01",
            "比你还多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        "#4S（打击！）#3S\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_8_815 end

    def Function_9_90E(): pass

    label("Function_9_90E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A7")

    #C0013
    ChrTalk(
        0xFE,
        (
            "这里是『幸运西餐厅』……\x01",
            "嗯，果然是家\x01",
            "豪华的餐厅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "……但重点是料理的味道！\x01",
            "身为美食家的我，\x01",
            "是不会被餐厅的装修迷惑的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_9E7")

    label("loc_9A7")


    #C0015
    ChrTalk(
        0xFE,
        (
            "来吧，著名疗养地的\x01",
            "西餐厅的料理……\x01",
            "就让我亲口品尝一下吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E7")

    TalkEnd(0xFE)
    Return()

    # Function_9_90E end

    def Function_10_9EB(): pass

    label("Function_10_9EB")

    TalkBegin(0xFE)

    #C0016
    ChrTalk(
        0xFE,
        (
            "这家珠宝店……\x01",
            "不允许我这种\x01",
            "普通的游客入内。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "啊！真不甘心！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_9EB end

    def Function_11_A38(): pass

    label("Function_11_A38")

    TalkBegin(0xFE)

    #C0018
    ChrTalk(
        0xFE,
        (
            "妈妈……\x01",
            "不要看宝石了，\x01",
            "我们去主题公园玩吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_A38 end

    def Function_12_A71(): pass

    label("Function_12_A71")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0019
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B46")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x7, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x7, 0x0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x7, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_B46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B62")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_B62")

    Return()

    # Function_12_A71 end

    def Function_13_B64(): pass

    label("Function_13_B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F51")
    EventBegin(0x0)
    Fade(1000)
    OP_68(-19000, 1000, 11800, 0)
    SetChrPos(0x101, -19330, 0, 8810, 0)
    SetChrPos(0x102, -17960, 0, 8810, 0)
    SetChrPos(0x103, -20760, 0, 10150, 45)
    SetChrPos(0x104, -16940, 0, 9380, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE9")
    SetChrPos(0x151, -18610, 0, 7180, 0)

    label("loc_BE9")

    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -19000, 0, 12900, 180)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)

    def lambda_C29():
        OP_96(0xFE, 0xFFFFB5C8, 0x0, 0x2C2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_C29)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
    WaitChrThread(0xE, 1)

    #C0020
    ChrTalk(
        0x101,
        "#0005F哇……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "#11P欢迎来到\x01",
            "珠宝店『亮饰』。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xE,
        (
            "#11P……不好意思，这位客人。\x01",
            "请问您持有\x01",
            "哪位贵宾的介绍信？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#0105F请问……\x01",
            "必须要持有介绍信吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xE,
        "#11P正是。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xE,
        (
            "#11P本店实行会员制，\x01",
            "非会员谢绝入内。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xE,
        "#11P那么，很抱歉……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)
    Sleep(100)

    def lambda_D4F():
        OP_96(0xFE, 0xFFFFB5C8, 0x0, 0x3264, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_D4F)
    Sleep(300)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    WaitChrThread(0xE, 1)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0xE, 0x80)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    #C0027
    ChrTalk(
        0x103,
        "#0211F……一眼就看出我们不是会员了吗。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        "#0310F感、感觉真不爽啊……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F06")

    #C0029
    ChrTalk(
        0x151,
        (
            "#5704F这种地方的店，\x01",
            "很多都是会员制的。\x02\x03",

            "要是能佩戴一些高级饰品，\x01",
            "正好就可以\x01",
            "与礼服搭配了……\x02\x03",

            "#5702F不过，没办法，这次就放弃吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#0006F说、说的也对啊……\x01",
            "总之，先去精品店看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F46")

    label("loc_F06")


    #C0031
    ChrTalk(
        0x101,
        (
            "#0006F总、总之……\x01",
            "进不去的话也没办法啊。\x01",
            "这次就先放弃吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F46")

    OP_5A()
    SetScenarioFlags(0xAE, 1)
    EventEnd(0x5)
    Jump("loc_F9F")

    label("loc_F51")

    EventBegin(0x1)

    #C0032
    ChrTalk(
        0x101,
        (
            "#0001F这家珠宝店\x01",
            "好像实行会员制，\x01",
            "这次就先放弃吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -18610, 0, 9950, 180)
    EventEnd(0x4)

    label("loc_F9F")

    Return()

    # Function_13_B64 end

    def Function_14_FA0(): pass

    label("Function_14_FA0")

    EventBegin(0x0)
    Fade(1000)
    OP_68(27100, 1600, 7920, 0)
    MoveCamera(315, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, 25000, 0, 7600, 90)
    SetChrPos(0x102, 23800, 0, 8900, 90)
    SetChrPos(0x103, 23800, 0, 7600, 90)
    SetChrPos(0x104, 25000, 0, 8900, 90)
    OP_68(25100, 1600, 7920, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0033
    ChrTalk(
        0x101,
        "#0001F#5P前方是……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#0105F#5P好像\x01",
            "被封锁了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x104,
        "#0305F#5P啊，好像写着什么。\x02",
    )

    CloseMessageWindow()
    OP_68(26500, 1600, 7920, 3000)

    def lambda_10B2():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10B2)
    Sleep(300)

    def lambda_10CA():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10CA)
    Sleep(100)

    def lambda_10E2():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10E2)
    Sleep(50)

    def lambda_10FA():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10FA)
    WaitChrThread(0x104, 1)

    def lambda_1113():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1113)
    WaitChrThread(0x101, 1)

    def lambda_1124():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1124)
    WaitChrThread(0x102, 1)

    def lambda_1135():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1135)
    WaitChrThread(0x103, 1)

    def lambda_1146():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1146)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "前方区域正在开发，\x01",
            "禁止入内。\x01",
            "　　　　──米修拉姆开发事业部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_0D()

    #C0037
    ChrTalk(
        0x103,
        (
            "#0200F#6P……看来前方\x01",
            "还在开发呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        (
            "#0103F#5P嗯，米修拉姆的开发计划\x01",
            "好像还在进行当中……\x02\x03",

            "#0100F说不定，这边以后也会\x01",
            "建造起一些设施呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#0306F#5P哎呀呀，真是够奢侈……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#0000F#6P总之，我们现在也不需要去那边，\x01",
            "还是先去别的地方转转吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 25630, 0, 8109, 270)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xA4, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1305")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1305")

    EventEnd(0x5)
    Return()

    # Function_14_FA0 end

    def Function_15_1308(): pass

    label("Function_15_1308")

    EventBegin(0x0)
    Fade(1000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_68(-50, 1100, 8000, 0)
    MoveCamera(335, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20090, 0)
    SetCameraDistance(18590, 2000)
    SetChrPos(0x101, 0, 0, 9300, 180)
    SetChrPos(0x102, 0, 0, 6700, 0)
    SetChrPos(0x103, 1200, 0, 8000, 270)
    SetChrPos(0x104, -1200, 0, 8000, 90)
    OP_6F(0x10)
    OP_0D()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0003F#11P已经绕了一圈了……\x02\x03",

            "#0001F看样子，要想进入拍卖会场，\x01",
            "果然还是需要想点办法。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#0301F#5P是啊，毕竟盘查人员好像\x01",
            "就是那些黑手党。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#0205F#12P说起来，那张邀请卡\x01",
            "应该可以用吧？\x02\x03",

            "#0201F虽然很有可能\x01",
            "会被核查身份……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#0103F#6P……的确如此。\x02\x03",

            "#0108F这方面的事情，如果之前\x01",
            "仔细向小玲咨询一下就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#0000F#11P算了，\x01",
            "仅仅是把邀请卡让给我们这一点，\x01",
            "就已经很值得感激了。\x02\x03",

            "#0006F不管怎么说……要先找到一个\x01",
            "安静的地方，以便考虑对策啊。\x02\x03",

            "#0008F西餐厅……\x01",
            "那里的人未免也太多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#0200F#12P那么，上面的酒店\x01",
            "没有空房间了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#0106F#6P嗯，在这种时期，\x01",
            "我想客房应该都被订满了……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0300F#5P不过，说不定也会有\x01",
            "客人取消预订而空出来的房间吧。\x02\x03",

            "去总服务台问问看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#0000F#11P说得对，去问下吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 400, 0, 7770, 0)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    SetScenarioFlags(0xA4, 4)
    OP_29(0x47, 0x1, 0x3)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_15_1308 end

    def Function_16_169F(): pass

    label("Function_16_169F")

    EventBegin(0x0)
    Fade(1000)
    OP_68(19000, 1000, 10600, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 19000, 0, 10600, 0)
    SetChrPos(0x102, 18350, 0, 9300, 0)
    SetChrPos(0x103, 19650, 0, 9300, 0)
    SetChrPos(0x104, 18350, 0, 8000, 0)
    SetChrPos(0x151, 19650, 0, 8000, 0)
    SetCameraDistance(19500, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0003F#5P（……换上正装之后，\x01",
            "　就不能在周围打探情况了。）\x02\x03",

            "#0001F（而且也需要决定带谁去会场才行，\x01",
            "　怎么办呢……？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【继续在周围打探情况】\x01",      # 0
            "【去精品店换正装】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1814"),
        (1, "loc_182C"),
        (SWITCH_DEFAULT, "loc_18AF"),
    )


    label("loc_1814")

    SetChrPos(0x0, 19000, 0, 9300, 180)
    EventEnd(0x5)
    Jump("loc_18AF")

    label("loc_182C")

    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_68(19000, 1000, 11600, 5000)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(300)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x103, 3, 0, 17)
    Sleep(300)
    BeginChrThread(0x104, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x151, 3, 0, 17)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x151, 0x3)
    NewScene("t1040", 100, 0, 0)
    IdleLoop()
    Jump("loc_18AF")

    label("loc_18AF")

    Return()

    # Function_16_169F end

    def Function_17_18B0(): pass

    label("Function_17_18B0")

    OP_95(0xFE, 19000, 0, 10600, 2000, 0x1)

    def lambda_18C9():
        OP_95(0xFE, 19000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18C9)
    Sleep(400)

    def lambda_18E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18E6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_18B0 end

    def Function_18_18FB(): pass

    label("Function_18_18FB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "前方区域正在开发，\x01",
            "禁止入内。\x01",
            "　　　　──米修拉姆开发事业部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_18FB end

    SaveToFile()

Try(main)
