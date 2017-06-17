from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t0010.bin",                # FileName
        "t0010",                    # MapName
        "t0010",                    # Location
        0x0037,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x19,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 55, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0010",                  # 0
        "米莉亚",                 # 1
        "多纳尔德",               # 2
        "安洁",                   # 3
        "特鲁塔村长",             # 4
        "艾娜夫人",               # 5
        "迪利克",                 # 6
        "艾尔琴",                 # 7
        "哈罗德",                 # 8
        "皮特",                   # 9
        "特鲁塔村长",             # 10
        "盖巴尔",                 # 11
        "阿鲁姆",                 # 12
        "艾娅莉",                 # 13
    ))

    AddCharChip((
        "chr/ch24002.itc",                   # 00
        "chr/ch45400.itc",                   # 01
        "chr/ch09302.itc",                   # 02
        "chr/ch24300.itc",                   # 03
        "chr/ch32300.itc",                   # 04
        "chr/ch23702.itc",                   # 05
        "chr/ch24202.itc",                   # 06
        "chr/ch24100.itc",                   # 07
        "chr/ch24400.itc",                   # 08
        "chr/ch22200.itc",                   # 09
        "chr/ch24302.itc",                   # 0A
        "chr/ch24000.itc",                   # 0B
        "chr/ch47700.itc",                   # 0C
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

    DeclNpc(519,     180,     -1850,   180,  261,  0x0, 0,   5,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(38409,   180,     540,     180,  261,  0x0, 0,   6,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(33700,   0,       -2619,   204,  261,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-38479,  180,     -1779,   90,   325,  0x0, 0,   0,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-81620,  0,       3410,    0,    261,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-38049,  0,       -140,    180,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-1139,   0,       2380,    90,   389,  0x0, 0,   8,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(-34200,  180,     -1529,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-34400,  0,       -300,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(76569,   0,       -2180,   0,    389,  0x0, 0,   11,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(75800,   0,       2000,    0,    389,  0x0, 0,   12,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(792, 0)                                        # 0

    ScpFunction((
        "Function_0_318",          # 00, 0
        "Function_1_3D0",          # 01, 1
        "Function_2_3FB",          # 02, 2
        "Function_3_65A",          # 03, 3
        "Function_4_693",          # 04, 4
        "Function_5_1428",         # 05, 5
        "Function_6_1F6C",         # 06, 6
        "Function_7_2036",         # 07, 7
        "Function_8_290D",         # 08, 8
        "Function_9_384B",         # 09, 9
        "Function_10_3B3F",        # 0A, 10
        "Function_11_3D86",        # 0B, 11
        "Function_12_4869",        # 0C, 12
        "Function_13_4BA0",        # 0D, 13
        "Function_14_4D5A",        # 0E, 14
        "Function_15_4E3D",        # 0F, 15
        "Function_16_524E",        # 10, 16
        "Function_17_535B",        # 11, 17
        "Function_18_53F3",        # 12, 18
        "Function_19_5D05",        # 13, 19
        "Function_20_61BB",        # 14, 20
        "Function_21_62C9",        # 15, 21
        "Function_22_6B79",        # 16, 22
        "Function_23_6E41",        # 17, 23
        "Function_24_797D",        # 18, 24
        "Function_25_84B3",        # 19, 25
        "Function_26_8AAD",        # 1A, 26
        "Function_27_9BA9",        # 1B, 27
        "Function_28_9BF4",        # 1C, 28
        "Function_29_9C3F",        # 1D, 29
        "Function_30_9C8A",        # 1E, 30
        "Function_31_9CD5",        # 1F, 31
        "Function_32_9D20",        # 20, 32
        "Function_33_9D6B",        # 21, 33
        "Function_34_9DCA",        # 22, 34
        "Function_35_9DF9",        # 23, 35
        "Function_36_9E10",        # 24, 36
        "Function_37_9E27",        # 25, 37
        "Function_38_A44A",        # 26, 38
        "Function_39_A495",        # 27, 39
    ))


    def Function_0_318(): pass

    label("Function_0_318")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_358"),
        (1, "loc_364"),
        (2, "loc_370"),
        (3, "loc_37C"),
        (4, "loc_388"),
        (5, "loc_394"),
        (6, "loc_3A0"),
        (SWITCH_DEFAULT, "loc_3AC"),
    )


    label("loc_358")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_364")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_370")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_37C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_388")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_394")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_3A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_3AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_3B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_3CF")

    Return()

    # Function_0_318 end

    def Function_1_3D0(): pass

    label("Function_1_3D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FA")
    OP_94(0xFE, 0xFFFFF326, 0xB68, 0x100E, 0xFFFFFEDE, 0x7D0)
    Sleep(250)
    Jump("Function_1_3D0")

    label("loc_3FA")

    Return()

    # Function_1_3D0 end

    def Function_2_3FB(): pass

    label("Function_2_3FB")

    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0x8, 0x5)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4CB")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -47480, 0, -1230, 90)
    SetChrChipByIndex(0xB, 0xB)
    ClearChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x40)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, -46490, 0, -1230, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490")
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_490")

    SetChrChipByIndex(0xA, 0xA)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 38320, 180, -2250, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C6")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_4C6")

    Jump("loc_5FA")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4D9")
    Jump("loc_5FA")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_4E7")
    Jump("loc_5FA")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4F5")
    Jump("loc_5FA")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_51E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_519")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_519")

    Jump("loc_5FA")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_540")
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_5FA")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_584")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_57A")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x2)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_57F")

    label("loc_57A")

    SetChrFlags(0xB, 0x80)

    label("loc_57F")

    Jump("loc_5FA")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_5AF")
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x2)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)

    label("loc_5AF")

    Jump("loc_5FA")

    label("loc_5B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C2")
    Jump("loc_5FA")

    label("loc_5C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5D5")
    SetChrFlags(0xA, 0x80)
    Jump("loc_5FA")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E3")
    Jump("loc_5FA")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5F1")
    Jump("loc_5FA")

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5FA")

    label("loc_5FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_60E")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)
    Jump("loc_659")

    label("loc_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_622")
    ClearScenarioFlags(0x22, 1)
    Event(0, 23)
    Jump("loc_659")

    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_636")
    ClearScenarioFlags(0x22, 2)
    Event(0, 24)
    Jump("loc_659")

    label("loc_636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_64A")
    ClearScenarioFlags(0x22, 3)
    Event(0, 26)
    Jump("loc_659")

    label("loc_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_659")
    ClearScenarioFlags(0x22, 4)
    Event(0, 37)

    label("loc_659")

    Return()

    # Function_2_3FB end

    def Function_3_65A(): pass

    label("Function_3_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_66C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_692")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_692")

    Return()

    # Function_3_65A end

    def Function_4_693(): pass

    label("Function_4_693")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_766")

    #C0001
    ChrTalk(
        0xFE,
        (
            "听说总统在\x01",
            "克洛斯贝尔市被拘捕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "协会的游击士们在\x01",
            "重新获得行动自由之后，\x01",
            "立刻就赶到村子来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "虽然现在的状况很严峻，\x01",
            "但克洛斯贝尔的所有人\x01",
            "一定要齐心协力，共渡难关。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7F4")

    label("loc_766")


    #C0004
    ChrTalk(
        0xFE,
        (
            "协会的游击士们在\x01",
            "重新获得行动自由之后，\x01",
            "立刻就赶到村子来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "虽然现在的状况很严峻，\x01",
            "但克洛斯贝尔的所有人\x01",
            "一定要齐心协力，共渡难关。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F4")

    Jump("loc_1424")

    label("loc_7F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_932")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B2")

    #C0006
    ChrTalk(
        0xFE,
        (
            "迪利克最近经常拜访各位村民，\x01",
            "确认大家是否平安。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "在这种特殊状况下，\x01",
            "单是看到熟人的面孔，\x01",
            "就能让我安心不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "真不愧是迪利克，\x01",
            "又认真又可靠啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_92D")

    label("loc_8B2")


    #C0009
    ChrTalk(
        0xFE,
        (
            "迪利克最近经常拜访各位村民，\x01",
            "确认大家是否平安。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "单是看到熟人的面孔，\x01",
            "就能让我安心不少呢。\x01",
            "呵呵，真不愧是迪利克。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92D")

    Jump("loc_1424")

    label("loc_932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A09")

    #C0011
    ChrTalk(
        0xFE,
        (
            "我弟弟艾尔琴\x01",
            "每天都在唉声叹气，\x01",
            "抱怨没法出去兜风。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "现在的情况本来就\x01",
            "够让人郁闷的了，\x01",
            "他还一个劲地念叨个不停……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "我觉得在这种时候，\x01",
            "每天还能吃到新鲜的食物，\x01",
            "就很值得庆幸了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A83")

    label("loc_A09")


    #C0014
    ChrTalk(
        0xFE,
        (
            "我弟弟艾尔琴\x01",
            "每天都在唉声叹气，\x01",
            "抱怨没法出去兜风。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "我觉得在这种时候，\x01",
            "每天还能吃到新鲜的食物，\x01",
            "就很值得庆幸了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A83")

    Jump("loc_1424")

    label("loc_A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AFD")

    #C0016
    ChrTalk(
        0xFE,
        (
            "最近在古战场附近\x01",
            "能看到一些穿戴着\x01",
            "盔甲的奇怪魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "是不是哪个有钱人饲养的\x01",
            "魔兽逃出来了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1424")

    label("loc_AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B94")

    #C0018
    ChrTalk(
        0xFE,
        (
            "对我们这些农民来说，\x01",
            "可以滋润农作物的雨水\x01",
            "是来自上天的恩赐。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "多亏女神赐福，\x01",
            "我们才有饭吃。\x01",
            "必须要好好感谢女神啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BF3")

    label("loc_B94")


    #C0020
    ChrTalk(
        0xFE,
        (
            "对我们这些农民来说，\x01",
            "可以滋润农作物的雨水\x01",
            "是来自上天的恩赐。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "必须要\x01",
            "好好感谢女神啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF3")

    Jump("loc_1424")

    label("loc_BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E2B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCF")

    #C0022
    ChrTalk(
        0xFE,
        (
            "我对迪利克推行的\x01",
            "村庄改革没什么兴趣呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "把导力器引入田地里，\x01",
            "确实会使工作变得更轻松……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "但我还是喜欢在田地里耕作。\x01",
            "自己的工作要是被机器抢走了，肯定心情复杂。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D4A")

    label("loc_CCF")


    #C0025
    ChrTalk(
        0xFE,
        (
            "推行村庄改革会让\x01",
            "生活变得更方便，\x01",
            "这是件好事……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "但我还是喜欢在田地里耕作。\x01",
            "如果生活过于便利，也会让人心情复杂。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4A")

    Jump("loc_E26")

    label("loc_D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDC")

    #C0027
    ChrTalk(
        0xFE,
        (
            "我们全村的人都被那个\x01",
            "叫敏涅斯的家伙给骗了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "原来这个世上还真有\x01",
            "能够面不改色地\x01",
            "说谎的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "我算是长见识了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E26")

    label("loc_DDC")


    #C0030
    ChrTalk(
        0xFE,
        (
            "原来这个世上还真有\x01",
            "能够面不改色地\x01",
            "说谎的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "我算是长见识了。\x02",
    )

    CloseMessageWindow()

    label("loc_E26")

    Jump("loc_1424")

    label("loc_E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF3")

    #C0032
    ChrTalk(
        0xFE,
        (
            "艾尔琴载着农作物\x01",
            "到市里送货去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "他最近好像很开心呢，\x01",
            "老是绕路兜一圈风\x01",
            "才回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "不过，能以那么便宜的价格\x01",
            "买到那么好的车，\x01",
            "心情愉快也是可以理解的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F3B")

    label("loc_EF3")


    #C0035
    ChrTalk(
        0xFE,
        (
            "艾尔琴载着农作物\x01",
            "到市里送货去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "再过一会，\x01",
            "应该就会回来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3B")

    Jump("loc_FE0")

    label("loc_F40")


    #C0037
    ChrTalk(
        0xFE,
        (
            "艾尔琴那家伙，自从村里买下了敏涅斯先生\x01",
            "低价出让的那辆导力卡车之后，\x01",
            "就一直兴奋得不得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "我也理解他的心情……\x01",
            "但还是得经常提醒他\x01",
            "注意安全，别出事故。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE0")

    Jump("loc_1424")

    label("loc_FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1158")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10EB")

    #C0039
    ChrTalk(
        0xFE,
        (
            "这个村子的每任村长都是村民们\x01",
            "以投票的方式选出来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "虽然大家都觉得村长的儿子迪利克\x01",
            "很适合当下任村长……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "但他太爱较真了，\x01",
            "总是把事情想得过于复杂。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "为村子的将来着想，\x01",
            "这当然是件好事……\x01",
            "但也希望他能多依赖我们一些啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1153")

    label("loc_10EB")


    #C0043
    ChrTalk(
        0xFE,
        (
            "迪利克太爱较真了，\x01",
            "总是把事情想得过于复杂。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "真希望他不要一个人钻牛角尖，\x01",
            "最后造成不好的结果。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1153")

    Jump("loc_1424")

    label("loc_1158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1305")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1273")

    #C0045
    ChrTalk(
        0xFE,
        (
            "艾尔琴讲话时带的口音\x01",
            "是『阿尔摩利卡方言』。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "这是一种流传很久的方言，\x01",
            "在我们村子里，只有多纳尔德叔叔\x01",
            "和艾尔琴会讲了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "这种方言给人一种\x01",
            "『这才是阿尔摩利卡村民』的感觉，\x01",
            "所以我觉得不用特地去纠正……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "男人总爱为一些鸡毛蒜皮的小事\x01",
            "而烦恼呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1300")

    label("loc_1273")


    #C0049
    ChrTalk(
        0xFE,
        (
            "从某种意义上来说，艾尔琴的\x01",
            "阿尔摩利卡口音是非常珍贵的，\x01",
            "毕竟是流传很久的方言嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "我完全不讨厌这种口音，\x01",
            "他根本不需要特地去纠正啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1300")

    Jump("loc_1424")

    label("loc_1305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1424")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C4")

    #C0051
    ChrTalk(
        0xFE,
        (
            "最近的日子过得真是平稳，\x01",
            "降雨十分适度，\x01",
            "农作物也长得非常好……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "像今天这样的好天气，\x01",
            "晒晒太阳是最舒服的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "嗯～在导力卡车上铺些稻草，\x01",
            "来睡个午觉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1424")

    label("loc_13C4")


    #C0054
    ChrTalk(
        0xFE,
        (
            "像今天这样的好天气，\x01",
            "晒晒太阳是最舒服的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "嗯～在导力卡车上铺些稻草，\x01",
            "来睡个午觉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1424")

    TalkEnd(0xFE)
    Return()

    # Function_4_693 end

    def Function_5_1428(): pass

    label("Function_5_1428")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_14A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1446")
    Call(0, 6)
    Jump("loc_14A2")

    label("loc_1446")


    #C0056
    ChrTalk(
        0xFE,
        "唉，安洁说的完全没错。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "为了维持村子里的粮食供应，\x01",
            "俺们农民一定得\x01",
            "努力种田才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A2")

    Jump("loc_1F68")

    label("loc_14A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_15F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1584")

    #C0058
    ChrTalk(
        0xFE,
        (
            "自从发表了独立宣言，\x01",
            "俺们村的卡车都没法\x01",
            "开到克洛斯贝尔市里去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市里绝对\x01",
            "有人在期待着俺们的\x01",
            "新鲜蔬菜哇。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "竟然不能把农作物\x01",
            "送到他们的手上，\x01",
            "身为生产者，真是很难过啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15EF")

    label("loc_1584")


    #C0061
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市里绝对\x01",
            "有人在期待着俺们的\x01",
            "新鲜蔬菜哇。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "真希望这次的无效宣言\x01",
            "能让俺重新开始做生意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15EF")

    Jump("loc_1F68")

    label("loc_15F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1758")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E4")

    #C0063
    ChrTalk(
        0xFE,
        (
            "那种叫『幻兽』的怪物\x01",
            "会摧毁村外的田地。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "受出行限制的影响，\x01",
            "农作物的收成本来就已经陷入低谷，\x01",
            "老实说，现在的生意实在是没法做了哇。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "但即使如此，\x01",
            "村内还是能够保持自给自足的状态。\x01",
            "必须得感谢女神才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1753")

    label("loc_16E4")


    #C0066
    ChrTalk(
        0xFE,
        (
            "村内现在还是能勉强\x01",
            "保持自给自足的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "只是，这种状况\x01",
            "到底还能持续多久呢……\x01",
            "老实说，俺也不知道啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1753")

    Jump("loc_1F68")

    label("loc_1758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1804")

    #C0068
    ChrTalk(
        0xFE,
        (
            "没想到市内遭到了袭击，\x01",
            "真是吓了俺一跳。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "而且听说那些袭击犯\x01",
            "到现在都没有被逮捕呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "他们不会逃到阿尔摩利卡村来了吧，\x01",
            "真让人担心哇。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1854")

    label("loc_1804")


    #C0071
    ChrTalk(
        0xFE,
        (
            "自从市内发生了袭击事件，\x01",
            "就一直觉得很不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "唉……都没法\x01",
            "专心下田了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1854")

    Jump("loc_1F68")

    label("loc_1859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1918")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18DB")

    #C0073
    ChrTalk(
        0xFE,
        (
            "卡米尤他们今天去酒馆\x01",
            "听主日学校的课了。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "俺只学过一些\x01",
            "农耕方面的技术，\x01",
            "真希望他们能好好学习。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1913")

    label("loc_18DB")


    #C0075
    ChrTalk(
        0xFE,
        "唔，难得今天不用做农活。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "就在家里放松一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1913")

    Jump("loc_1F68")

    label("loc_1918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1AE0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19AD")

    #C0077
    ChrTalk(
        0xFE,
        (
            "听说敏涅斯先生\x01",
            "打算在古道的私有地\x01",
            "建造什么设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "那里本来是用来置放\x01",
            "耕作工具的……\x01",
            "看来只好把那些东西搬走了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ADB")

    label("loc_19AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5D")

    #C0079
    ChrTalk(
        0xFE,
        (
            "那个叫敏涅斯的男人\x01",
            "真是个大坏蛋啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "俺也被他那爽朗的笑容\x01",
            "和友善的态度彻底欺骗了。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "……迪利克身为当事人，\x01",
            "一定更受打击。\x01",
            "希望他不要想不开啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ADB")

    label("loc_1A5D")


    #C0082
    ChrTalk(
        0xFE,
        (
            "竟然欺骗最为村子\x01",
            "着想的迪利克，\x01",
            "那家伙真是个大坏蛋哇。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "如果俺以后能再见到\x01",
            "那个叫敏涅斯的男人，\x01",
            "一定要狠狠揍他一顿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADB")

    Jump("loc_1F68")

    label("loc_1AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B52")

    #C0084
    ChrTalk(
        0xFE,
        (
            "最近时常到村里来的那个外国人\x01",
            "是个非常爽朗的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "总是乐呵呵地笑着，\x01",
            "那个笑容真让人安心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F68")

    label("loc_1B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1C98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1A")

    #C0086
    ChrTalk(
        0xFE,
        (
            "艾尔琴找俺\x01",
            "商量了一下\x01",
            "关于导力卡车的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "那辆卡车应该快到使用寿命了，\x01",
            "就算修好了，肯定也会很快坏掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "艾尔琴平时\x01",
            "特别爱惜那辆卡车，\x01",
            "希望他不要因此而沮丧啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C93")

    label("loc_1C1A")


    #C0089
    ChrTalk(
        0xFE,
        (
            "村里的导力卡车\x01",
            "已经快到使用寿命了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "村里的资金不是很充足，\x01",
            "所以很难向村长开口……\x01",
            "但还是得早日买辆新的才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C93")

    Jump("loc_1F68")

    label("loc_1C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D69")

    #C0091
    ChrTalk(
        0xFE,
        (
            "这世上有一些导力器\x01",
            "是农耕专用的。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "比如说，耕田用的导力耕田机，\x01",
            "还有收割用的导力拖拉机……\x01",
            "都是农耕中必不可少的工具。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "不过，阿尔摩利卡村里的\x01",
            "都是些破旧不堪的旧式机器。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E01")

    label("loc_1D69")


    #C0094
    ChrTalk(
        0xFE,
        (
            "导力耕田机、导力拖拉机……\x01",
            "在现在这个时代，\x01",
            "搞农耕可少不了导力器啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "说句贪婪的话，俺真想\x01",
            "要些更便利的最新型机器啊。\x01",
            "不过，那实在是太奢侈了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E01")

    Jump("loc_1F68")

    label("loc_1E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1F68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE5")

    #C0096
    ChrTalk(
        0xFE,
        (
            "俺在村里的田地上\x01",
            "栽种了各种各样的蔬菜。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡种植的蔬菜\x01",
            "都沐浴着自然阳光而成长，\x01",
            "所以特别好吃哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "我们会把农作物送到克洛斯贝尔市出售，\x01",
            "如果市里的人也觉得好吃，那就再好不过了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F68")

    label("loc_1EE5")


    #C0099
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡产的蔬菜，\x01",
            "都沐浴着自然阳光而成长，\x01",
            "所以特别好吃哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "虽说最近的进口货越来越多，\x01",
            "但我们的蔬菜绝对不比它们差哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F68")

    TalkEnd(0xFE)
    Return()

    # Function_5_1428 end

    def Function_6_1F6C(): pass

    label("Function_6_1F6C")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0101
    ChrTalk(
        0x9,
        (
            "唉唉……\x01",
            "没想到克洛斯贝尔\x01",
            "会出现那种东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "我担心得\x01",
            "都没法好好耕种了……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "唉，你在说什么\x01",
            "丧气话啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "越是在这种时候，\x01",
            "就越得为卡米尤和普莉\x01",
            "拼命工作啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_6_1F6C end

    def Function_7_2036(): pass

    label("Function_7_2036")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_20C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2054")
    Call(0, 6)
    Jump("loc_20BC")

    label("loc_2054")


    #C0105
    ChrTalk(
        0xFE,
        (
            "我老公的性格比较怯懦，\x01",
            "所以我必须得时常\x01",
            "鞭策他一下才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "正是在这种时候，\x01",
            "才更需要\x01",
            "拼命工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BC")

    Jump("loc_2909")

    label("loc_20C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_21DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2145")

    #C0107
    ChrTalk(
        0xFE,
        (
            "柯林今天\x01",
            "也来找我们家的\x01",
            "小不点一起玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "平日受到哈罗德先生那么多关照，\x01",
            "今天我要请他大吃一顿。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_21D6")

    label("loc_2145")


    #C0109
    ChrTalk(
        0xFE,
        (
            "平日受到哈罗德先生那么多关照，\x01",
            "今天我要请柯林大吃一顿。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "哈哈，但柯林每天都能享用\x01",
            "索菲亚女士烹调的美食，\x01",
            "我做的饭菜也许不能让他满意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D6")

    Jump("loc_2909")

    label("loc_21DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_22D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_227C")

    #C0111
    ChrTalk(
        0xFE,
        (
            "哈罗德先生的夫人\x01",
            "十分擅长烹饪。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "听说她还在\x01",
            "市内的家里\x01",
            "开了个烹饪教室呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "要不是现在的状况如此糟糕，\x01",
            "我也很想去参加呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_22D4")

    label("loc_227C")


    #C0114
    ChrTalk(
        0xFE,
        (
            "哈罗德先生的夫人\x01",
            "十分擅长烹饪。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "两家的孩子也年龄相当，\x01",
            "所以我们相处得很好呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D4")

    Jump("loc_2909")

    label("loc_22D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2395")

    #C0116
    ChrTalk(
        0xFE,
        (
            "听说袭击事件\x01",
            "造成的损失非常惨重。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "……唉，算了。\x01",
            "还是别说这个话题了，\x01",
            "心情都变差了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "越是在这种时候，\x01",
            "越得像平时一样，\x01",
            "精神饱满地好好过日子才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2400")

    label("loc_2395")


    #C0119
    ChrTalk(
        0xFE,
        (
            "一听到关于袭击事件造成的损失，\x01",
            "我心情就会变差。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "像平时一样好好过日子\x01",
            "才是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2400")

    Jump("loc_2909")

    label("loc_2405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2510")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B7")

    #C0121
    ChrTalk(
        0xFE,
        (
            "通过昨天那件事，\x01",
            "村长和迪利克\x01",
            "已经和好如初了。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "他们两人都是\x01",
            "把村子放在第一位的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "这个最近已经有些萧条的村子\x01",
            "今后一定能\x01",
            "变得越来越好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_250B")

    label("loc_24B7")


    #C0124
    ChrTalk(
        0xFE,
        (
            "村长和迪利克都是把\x01",
            "村子放在第一位的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "这个村子今后一定能\x01",
            "变得越来越好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_250B")

    Jump("loc_2909")

    label("loc_2510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257E")

    #C0126
    ChrTalk(
        0xFE,
        (
            "真没想到，\x01",
            "村子的改革竟能\x01",
            "进展得这么快速。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "这多亏了敏涅斯\x01",
            "先生的本领啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D9")

    label("loc_257E")


    #C0128
    ChrTalk(
        0xFE,
        (
            "真没想到，\x01",
            "那个叫敏涅斯的家伙\x01",
            "竟然会放魔兽出来……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "总之，幸好孩子们\x01",
            "都没有受伤。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D9")

    Jump("loc_2909")

    label("loc_25DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_267D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2614")

    #C0130
    ChrTalk(
        0xFE,
        "好了～今天做什么吃的呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2678")

    label("loc_2614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2626")
    Call(0, 22)
    Jump("loc_2678")

    label("loc_2626")


    #C0131
    ChrTalk(
        0xFE,
        (
            "哎呀呀，那个人\x01",
            "真是很不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "对小孩也很温柔，\x01",
            "反正我觉得他不是坏人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2678")

    Jump("loc_2909")

    label("loc_267D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274A")

    #C0133
    ChrTalk(
        0xFE,
        (
            "有时候能在田地采摘到\x01",
            "一些奇形怪状的蔬菜和水果……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "那些蔬菜和水果没法拿出去卖，\x01",
            "村民们就会分着吃掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "虽然外形很难看，\x01",
            "但味道还是一样美味的。\x01",
            "这也补贴了不少家计呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27D6")

    label("loc_274A")


    #C0136
    ChrTalk(
        0xFE,
        (
            "店里不会进购那些\x01",
            "奇形怪状的蔬菜和水果，\x01",
            "所以村民们就会分着吃掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "明明那么好吃，\x01",
            "仅仅因为形状难看就没人买，\x01",
            "真搞不懂那些城里人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D6")

    Jump("loc_2909")

    label("loc_27DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_27E9")
    Jump("loc_2909")

    label("loc_27E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2909")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28AC")

    #C0138
    ChrTalk(
        0xFE,
        (
            "不久前，阿蕾莎女士\x01",
            "正式搬到村里来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "她的儿子肯和我家的小不点\x01",
            "一起玩，真是帮了大忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "那对母子现在好像暂时住在旅馆里，\x01",
            "等有空时，我得去跟她\x01",
            "打声招呼。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2909")

    label("loc_28AC")


    #C0141
    ChrTalk(
        0xFE,
        (
            "史蒂芬时常和\x01",
            "我家的小不点\x01",
            "一起玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "这个村里小孩很少，\x01",
            "他们能交上朋友，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2909")

    TalkEnd(0xFE)
    Return()

    # Function_7_2036 end

    def Function_8_290D(): pass

    label("Function_8_290D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_293A")
    Call(0, 25)
    Return()

    label("loc_293A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_295F")
    Call(0, 19)
    Return()

    label("loc_295F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2ADF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_297D")
    Call(0, 13)
    Jump("loc_2ADA")

    label("loc_297D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A4E")

    #C0143
    ChrTalk(
        0xFE,
        (
            "哈罗德刚刚\x01",
            "回市里去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "他已经和迪利克\x01",
            "商量过日后村子的各种应对措施。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "虽然我很希望哈罗德\x01",
            "多在村里留一段时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "但他想巡回各地，\x01",
            "做些自己力所能及的事。\x01",
            "……这也没办法啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2ADA")

    label("loc_2A4E")


    #C0147
    ChrTalk(
        0xFE,
        (
            "……为了灵活应对日后村子可能发生的情况，\x01",
            "真希望哈罗德\x01",
            "多留一段时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "不过已经有游击士\x01",
            "赶到村里来帮忙了，\x01",
            "我们自己也要努力才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ADA")

    Jump("loc_3847")

    label("loc_2ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2C36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BAF")

    #C0149
    ChrTalk(
        0xFE,
        (
            "独立无效宣言发表之后，\x01",
            "迪利克采取了不少措施。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "在这种状况下……\x01",
            "就连长年担任村长的我\x01",
            "都不知道将会发生什么事。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "总之，大家都要尽量\x01",
            "做好自己力所能及的事，\x01",
            "这是最重要的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C31")

    label("loc_2BAF")


    #C0152
    ChrTalk(
        0xFE,
        (
            "在这种状况下……\x01",
            "就连长年担任村长的我\x01",
            "都不知道将会发生什么事。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "总之，大家都要尽量\x01",
            "做好自己力所能及的事，\x01",
            "这是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C31")

    Jump("loc_3847")

    label("loc_2C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_2D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CE9")

    #C0154
    ChrTalk(
        0xFE,
        (
            "唔，没想到竟然会有\x01",
            "那种人潜伏在古战场……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "虽说是群不可忽视的危险人物，\x01",
            "但他们似乎并不打算\x01",
            "对村子出手。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村暂时还是\x01",
            "静观其变吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2D44")

    label("loc_2CE9")


    #C0157
    ChrTalk(
        0xFE,
        (
            "潜藏在古战场的那些人\x01",
            "似乎并不打算\x01",
            "对村子出手。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村暂时还是\x01",
            "静观其变吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D44")

    Jump("loc_3847")

    label("loc_2D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2E97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E3E")

    #C0159
    ChrTalk(
        0xFE,
        (
            "说实话，我完全跟不上\x01",
            "迪塔总统的想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "但和人口繁多的\x01",
            "克洛斯贝尔市相比，\x01",
            "这个村子的影响力确实是微不足道……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "……不管怎么说，\x01",
            "哈罗德一家也在\x01",
            "尽力协助我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "现在必须全村人齐心协力，\x01",
            "共同渡过这个难关。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E92")

    label("loc_2E3E")


    #C0163
    ChrTalk(
        0xFE,
        (
            "哈罗德一家也在\x01",
            "尽力协助我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "现在必须全村人齐心协力，\x01",
            "共同渡过这个难关。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E92")

    Jump("loc_3847")

    label("loc_2E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3118")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2FBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F63")

    #C0165
    ChrTalk(
        0xFE,
        (
            "呵呵，虽然现在这个时候，大家都很不容易……\x01",
            "但这件事却让人感到温暖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "总之，盖巴尔先生\x01",
            "就交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "我会好好照顾他，\x01",
            "直到他平静下来，重新回到市内的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FB7")

    label("loc_2F63")


    #C0168
    ChrTalk(
        0xFE,
        (
            "盖巴尔先生\x01",
            "就交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "我会好好照顾他，\x01",
            "直到他平静下来，重新回到市内的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB7")

    Jump("loc_3113")

    label("loc_2FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309A")

    #C0170
    ChrTalk(
        0xFE,
        (
            "前几天发生在市内的袭击事件……\x01",
            "让阿尔摩利卡村的居民们\x01",
            "也感到十分不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "有传言说，这是帝国的阴谋，\x01",
            "但既然还没有确凿的证据，\x01",
            "就不能盲目相信……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "……总之，现在\x01",
            "必须得认真做好\x01",
            "村子附近的警戒。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3113")

    label("loc_309A")


    #C0173
    ChrTalk(
        0xFE,
        (
            "包括迪利克在内，村里的年轻人们\x01",
            "在对村子附近进行警戒。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "为了不让村民们\x01",
            "更加担惊受怕……\x01",
            "必须得认真做好这件事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3113")

    Jump("loc_3847")

    label("loc_3118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_31AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3133")
    Call(0, 10)
    Jump("loc_31A6")

    label("loc_3133")


    #C0175
    ChrTalk(
        0xFE,
        (
            "唔，让世人了解\x01",
            "我们村的特色，\x01",
            "这绝不是一件坏事。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "如果他们产生了兴趣，\x01",
            "移居到村里的人说不定也会增多呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31A6")

    Jump("loc_3847")

    label("loc_31AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_32F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31C6")
    Jump("loc_32ED")

    label("loc_31C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D5")
    Jump("loc_32ED")

    label("loc_31D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E7")
    Jump("loc_32ED")

    label("loc_31E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3297")

    #C0177
    ChrTalk(
        0xFE,
        "我和儿子的目的一样……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "我们都希望阿尔摩利卡村越来越好……\x01",
            "但我们的视野都太狭窄了。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "这次的事件也许是女神为了让我们\x01",
            "注意到这一点而给予的试炼吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32ED")

    label("loc_3297")


    #C0180
    ChrTalk(
        0xFE,
        (
            "我和儿子的目的都是\x01",
            "为了阿尔摩利卡村……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "今后我要好好听取\x01",
            "年轻人的想法才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32ED")

    Jump("loc_3847")

    label("loc_32F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34FD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330D")
    Jump("loc_34F8")

    label("loc_330D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331C")
    Jump("loc_34F8")

    label("loc_331C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B7")

    #C0182
    ChrTalk(
        0xFE,
        (
            "和迪利克密谈的外国人……\x01",
            "真是很可疑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "如果他在打什么坏主意，\x01",
            "就得早点采取对策。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        "麻烦你们帮我收集一下情报。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3419")

    label("loc_33B7")


    #C0185
    ChrTalk(
        0xFE,
        (
            "如果和迪利克密谈的外国人\x01",
            "在打什么坏主意，\x01",
            "就得早点采取对策。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "麻烦你们帮我收集一下情报。\x02",
    )

    CloseMessageWindow()

    label("loc_3419")

    Jump("loc_34F8")

    label("loc_341E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34AA")

    #C0187
    ChrTalk(
        0xFE,
        (
            "真是辛苦你们了。\x01",
            "多亏你们，\x01",
            "我大致明白现在的事态了。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "接下来，我会以村长的身份\x01",
            "和迪利克好好谈一下，\x01",
            "试着说服他。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_34F8")

    label("loc_34AA")


    #C0189
    ChrTalk(
        0xFE,
        (
            "作为村长，也作为他的父亲……\x01",
            "我必须得在迪利克犯下大错之前\x01",
            "想办法说服他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F8")

    Jump("loc_3847")

    label("loc_34FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3680")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3518")
    Call(0, 9)
    Jump("loc_367B")

    label("loc_3518")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_360D")

    #C0190
    ChrTalk(
        0xFE,
        (
            "由于年轻人离开村子，导致人手不足。\x01",
            "由于贸易自由化，\x01",
            "导致自治州内的粮食自给率下降……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "村子面临的问题确实很多……\x01",
            "但也不能因此而贸然采纳\x01",
            "迪利克的改革方案。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "保护村子的传统也是村长的职责。\x01",
            "真希望他能明白这一点啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_367B")

    label("loc_360D")


    #C0193
    ChrTalk(
        0xFE,
        (
            "保护村子的传统也是村长的职责。\x01",
            "变化并不完全是件好事。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "我真希望迪利克作为下任村长，\x01",
            "也能明白这一点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367B")

    Jump("loc_3847")

    label("loc_3680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_369B")
    Call(0, 9)
    Jump("loc_37AE")

    label("loc_369B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_374F")

    #C0195
    ChrTalk(
        0xFE,
        (
            "盲目推行改革，\x01",
            "践踏村子的传统，\x01",
            "一定会带来灾难的。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "我明白迪利克\x01",
            "是为村子着想，\x01",
            "才会提出改革方案……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "但为了不让村子\x01",
            "失去本色，\x01",
            "还是要慎重一些才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37AE")

    label("loc_374F")


    #C0198
    ChrTalk(
        0xFE,
        (
            "……我也不认为村子\x01",
            "应该永远维持现状。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "但为了不让村子\x01",
            "失去本色，\x01",
            "还是要慎重一些才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AE")

    Jump("loc_3847")

    label("loc_37B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3847")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37CE")
    Call(0, 9)
    Jump("loc_3847")

    label("loc_37CE")


    #C0200
    ChrTalk(
        0xFE,
        (
            "……这个烦恼是必须由我\x01",
            "自己去解决的。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "如果以后发生了什么事，\x01",
            "我也许会去拜托你们吧……\x01",
            "但是现在还不用替我担心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3847")

    TalkEnd(0xFE)
    Return()

    # Function_8_290D end

    def Function_9_384B(): pass

    label("Function_9_384B")


    #C0202
    ChrTalk(
        0xB,
        "哦哦，你们是特别任务支援科的……\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        "#00000F特鲁塔村长，好久不见了。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xB,
        (
            "哈哈，听说你们已经\x01",
            "重新开始工作了。\x01",
            "一切顺利，真是再好不过。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xB,
        "……唉……\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        (
            "#00105F那个……\x01",
            "您看起来很疲惫呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xB,
        (
            "其实……我最近正在为一些\x01",
            "个人问题而烦恼。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        (
            "不过，还没有严重到需要\x01",
            "你们来帮忙的程度。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x109,
        (
            "#10102F不必客气，您如果有烦恼，\x01",
            "不如和我们商量一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x104,
        (
            "#00300F是啊，一个人烦恼\x01",
            "对健康可不好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，我们特别任务支援科\x01",
            "说不定能帮上什么忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xB,
        (
            "哈哈，\x01",
            "真的不是什么大事。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xB,
        (
            "如果我无论如何都无法解决，\x01",
            "说不定就会去拜托你们了吧，\x01",
            "但现在还不用为我操心。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        (
            "#00003F是吗……\x01",
            "我明白了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AE8")

    #C0215
    ChrTalk(
        0x103,
        (
            "#00200F如果有什么事，\x01",
            "请您随时联系我们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B1A")

    label("loc_3AE8")


    #C0216
    ChrTalk(
        0x102,
        (
            "#00100F要是发生了什么事，\x01",
            "请您随时联系我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B1A")


    #C0217
    ChrTalk(
        0xB,
        (
            "好啊，到时候\x01",
            "就麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 1)
    Return()

    # Function_9_384B end

    def Function_10_3B3F(): pass

    label("Function_10_3B3F")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0218
    ChrTalk(
        0xB,
        (
            "迪利克，关于你提出的\x01",
            "『养蜂业体验活动』\x01",
            "这个企划……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "虽然的确很有吸引力，\x01",
            "但让外行人进入田里，真的好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xD,
        (
            "这的确是个问题……\x01",
            "但蜂蜜是村里的特产，\x01",
            "我觉得也没什么不好。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xD,
        (
            "只要我们事先指导他们\x01",
            "怎么应对那些蜜蜂就行了……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xB,
        "唔，的确值得考虑呢……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3CE8")

    #C0223
    ChrTalk(
        0x101,
        (
            "#00002F（看样子，村长和迪利克先生\x01",
            "  已经和好如初了呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x102,
        (
            "#00104F（这就是所谓的坏事变好事吧？\x01",
            "  呵呵，别打扰他们了，我们走吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D7A")

    label("loc_3CE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3D7A")

    #C0225
    ChrTalk(
        0x101,
        (
            "#00005F（哎？村长和迪利克先生……\x01",
            "  不知何时，他们已经和好如初了啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        (
            "#00104F（也许是在敏涅斯的事件中\x01",
            "  发生了什么事吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D7A")

    SetScenarioFlags(0x16F, 6)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_10_3B3F end

    def Function_11_3D86(): pass

    label("Function_11_3D86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E17")

    #C0227
    ChrTalk(
        0xFE,
        (
            "看着那棵散发着蓝白色光芒的大树，\x01",
            "我就感到非常不安……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "但我丈夫和迪利克\x01",
            "都在努力，\x01",
            "我也要为他们加油才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E90")

    label("loc_3E17")


    #C0229
    ChrTalk(
        0xFE,
        (
            "不仅是我丈夫和迪利克，\x01",
            "还有许多人在现在这种状况下\x01",
            "拼命努力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "虽然我帮不上什么大忙，\x01",
            "但一定要为他们加油才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E90")

    Jump("loc_4865")

    label("loc_3E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3F0E")

    #C0231
    ChrTalk(
        0xFE,
        (
            "独立无效宣言的发表\x01",
            "已经让迪塔总统的\x01",
            "正当性产生了动摇吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市的人们\x01",
            "现在一定非常混乱……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4865")

    label("loc_3F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4058")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE0")

    #C0233
    ChrTalk(
        0xFE,
        (
            "没想到亚里欧斯先生\x01",
            "竟然成为了国防长官……\x01",
            "我到现在还不敢相信。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "这个村庄一直都承蒙\x01",
            "游击士们的关照，\x01",
            "可是独立之后就完全联系不上他们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "真担心啊……\x01",
            "不知道他们怎么样了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4053")

    label("loc_3FE0")


    #C0236
    ChrTalk(
        0xFE,
        (
            "这个村庄一直都承蒙\x01",
            "游击士们的关照，\x01",
            "可是独立之后就完全联系不上他们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "真担心啊……\x01",
            "不知道他们怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4053")

    Jump("loc_4865")

    label("loc_4058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_40D3")

    #C0238
    ChrTalk(
        0xFE,
        (
            "迪利克他们率先开始去\x01",
            "村子附近巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "据说最近有人目击到了\x01",
            "来历不明的怪物……\x01",
            "希望他们多加小心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4865")

    label("loc_40D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4268")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41DC")

    #C0240
    ChrTalk(
        0xFE,
        (
            "从昨晚开始，我丈夫\x01",
            "和迪利克就一直在商量\x01",
            "村庄的新改革方案。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "新方案不只是追求变化，\x01",
            "更着重于传达村庄的传统魅力，\x01",
            "以此来恢复村庄的活力。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "只要他们两人能齐心协力，\x01",
            "阿尔摩利卡村一定能变得越来越好。\x01",
            "呵呵，我也要好好支持他们才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4263")

    label("loc_41DC")


    #C0243
    ChrTalk(
        0xFE,
        (
            "先给我丈夫和迪利克\x01",
            "冲两杯热可可吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "只要他们两人能齐心协力，\x01",
            "阿尔摩利卡村一定能变得越来越好。\x01",
            "呵呵，我也要好好支持他们才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4263")

    Jump("loc_4865")

    label("loc_4268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_43BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4368")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4329")

    #C0245
    ChrTalk(
        0xFE,
        (
            "我丈夫到哈罗德先生\x01",
            "那里商量有关\x01",
            "迪利克的事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "事到如今，\x01",
            "只靠我们已经无能为力了……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "啊啊，女神啊，\x01",
            "请保佑阿尔摩利卡村，\x01",
            "保佑迪利克吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4363")

    label("loc_4329")


    #C0248
    ChrTalk(
        0xFE,
        (
            "啊啊，女神啊，\x01",
            "请保佑阿尔摩利卡村，\x01",
            "保佑迪利克吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4363")

    Jump("loc_43B9")

    label("loc_4368")


    #C0249
    ChrTalk(
        0xFE,
        (
            "我丈夫和迪利克\x01",
            "终于和解，\x01",
            "我也总算放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "各位……\x01",
            "真是太感谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43B9")

    Jump("loc_4865")

    label("loc_43BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_44B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_443A")

    #C0251
    ChrTalk(
        0xFE,
        (
            "迪利克最近\x01",
            "几乎都不回家了……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "唉，真担心啊。\x01",
            "他该不会被卷入到什么\x01",
            "危险的事情中了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44AF")

    label("loc_443A")


    #C0253
    ChrTalk(
        0xFE,
        (
            "没想到迪利克竟然在和一个\x01",
            "叫敏涅斯的人商量改革的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "唉，难道他们父子间的关系\x01",
            "已经到了无可挽回的\x01",
            "地步吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44AF")

    Jump("loc_4865")

    label("loc_44B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_45CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_456E")

    #C0255
    ChrTalk(
        0xFE,
        (
            "我丈夫昨天和迪利克大吵了一架，\x01",
            "那是他们至今为止吵得最厉害的一次。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "他们两人都特别激动，\x01",
            "我都没法劝架……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "唉……到底要怎么做，\x01",
            "才能让他们和解呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_45C7")

    label("loc_456E")


    #C0258
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "到底要怎么做，才能让\x01",
            "我丈夫和迪利克和解呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "我已经不知道\x01",
            "该怎么办了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45C7")

    Jump("loc_4865")

    label("loc_45CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_46F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_468E")

    #C0260
    ChrTalk(
        0xFE,
        (
            "我丈夫和迪利克的争吵\x01",
            "一天比一天激烈。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "我每次都想方设法地打圆场，\x01",
            "可最近已经渐渐开始\x01",
            "感到力不从心了……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "唉，真担心啊。\x01",
            "但愿他们的关系不会\x01",
            "变得更加恶劣。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_46EF")

    label("loc_468E")


    #C0263
    ChrTalk(
        0xFE,
        (
            "我丈夫和迪利克的争吵\x01",
            "一天比一天激烈。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "唉，真担心啊。\x01",
            "但愿他们的关系不会\x01",
            "变得更加恶劣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46EF")

    Jump("loc_4865")

    label("loc_46F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47E9")

    #C0265
    ChrTalk(
        0xFE,
        (
            "最近这段时间，我丈夫和迪利克\x01",
            "每天都在为阿尔摩利卡村的将来\x01",
            "而激烈争论。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "争论本身并不是坏事，\x01",
            "但他们两人全都一步不肯退让，\x01",
            "最后总是发展成争吵……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "再这样下去，父子关系\x01",
            "将会变得越来越差啊。\x01",
            "唉，真是头痛……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4865")

    label("loc_47E9")


    #C0268
    ChrTalk(
        0xFE,
        (
            "我丈夫和儿子为了村子\x01",
            "而争论，\x01",
            "这件事本身并不是坏事……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "可是他们两人都很顽固，\x01",
            "根本没法达成共识。\x01",
            "唉，真是头痛……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4865")

    TalkEnd(0xFE)
    Return()

    # Function_11_3D86 end

    def Function_12_4869(): pass

    label("Function_12_4869")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_49B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4887")
    Call(0, 13)
    Jump("loc_49B1")

    label("loc_4887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493F")

    #C0270
    ChrTalk(
        0xFE,
        (
            "那棵巨大的树出现后，\x01",
            "村民们似乎也感到\x01",
            "相当不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "虽然总统已经被拘捕，\x01",
            "但蓝花和郊外的『幻兽』\x01",
            "等问题都还没有解决……\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "有必要呼吁村民们\x01",
            "继续多加\x01",
            "注意呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_49B1")

    label("loc_493F")


    #C0273
    ChrTalk(
        0xFE,
        (
            "虽然总统已经被拘捕，\x01",
            "但蓝花和郊外的『幻兽』\x01",
            "等问题都还没有解决……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "似乎有必要呼吁\x01",
            "村民们继续多加\x01",
            "注意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49B1")

    Jump("loc_4B9C")

    label("loc_49B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_49C4")
    Jump("loc_4B9C")

    label("loc_49C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_49D2")
    Jump("loc_4B9C")

    label("loc_49D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_49E0")
    Jump("loc_4B9C")

    label("loc_49E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4A4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49FB")
    Call(0, 10)
    Jump("loc_4A45")

    label("loc_49FB")


    #C0275
    ChrTalk(
        0xFE,
        (
            "……唔，老爸说得\x01",
            "也有道理。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "看来应该对这个方案\x01",
            "进一步深入思考。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A45")

    Jump("loc_4B9C")

    label("loc_4A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4B9C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A65")
    Jump("loc_4B9C")

    label("loc_4A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B34")

    #C0277
    ChrTalk(
        0xFE,
        (
            "我当时竟然打算独自\x01",
            "解决村子的问题，\x01",
            "那种想法本身就是个错误。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "通过这次的事件，我终于明白\x01",
            "自己以前的想法有多么肤浅了。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "今后我要和老爸一起……\x01",
            "不，和村民们一起\x01",
            "商讨村子的未来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4B9C")

    label("loc_4B34")


    #C0280
    ChrTalk(
        0xFE,
        (
            "通过这次的事件，我终于明白\x01",
            "自己以前的想法有多么肤浅了。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "今后我要和村民们一起\x01",
            "商讨村子的未来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B9C")

    TalkEnd(0xFE)
    Return()

    # Function_12_4869 end

    def Function_13_4BA0(): pass

    label("Function_13_4BA0")

    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0282
    ChrTalk(
        0xB,
        (
            "恐怕谁都没料到\x01",
            "会出现这种大事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xB,
        (
            "作为贸易中心而高速发展的克洛斯贝尔\x01",
            "以强硬的形式宣布独立，\x01",
            "给整个大陆造成了重大影响……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xB,
        (
            "长久以来一直践踏传统，\x01",
            "持续推行过于激进的改革，\x01",
            "如今终于显现出弊端了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xD,
        (
            "……但是，我们也不能就此\x01",
            "接受这样的现实。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xD,
        (
            "假如这是女神给予我们的试炼，\x01",
            "那女神就一定是在考验\x01",
            "我们能否渡过这个难关……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xB,
        "……唔，说得没错。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xB,
        (
            "哎呀呀，看来我也要\x01",
            "改改我这僵硬的\x01",
            "思考方式啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 4)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_13_4BA0 end

    def Function_14_4D5A(): pass

    label("Function_14_4D5A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D6B")
    Jump("loc_4E39")

    label("loc_4D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4DF8")

    #C0289
    ChrTalk(
        0xFE,
        (
            "我把从敏涅斯先生那里买来的\x01",
            "新型导力车交给警察调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "听他们说用不了几天\x01",
            "就能调查完毕……\x01",
            "唉，真希望能早点还给我啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E39")

    label("loc_4DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4E06")
    Jump("loc_4E39")

    label("loc_4E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E14")
    Jump("loc_4E39")

    label("loc_4E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4E22")
    Jump("loc_4E39")

    label("loc_4E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E30")
    Jump("loc_4E39")

    label("loc_4E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4E39")

    label("loc_4E39")

    TalkEnd(0xFE)
    Return()

    # Function_14_4D5A end

    def Function_15_4E3D(): pass

    label("Function_15_4E3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E62")
    Call(0, 19)
    Return()

    label("loc_4E62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E73")
    Jump("loc_524A")

    label("loc_4E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4F99")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E8E")
    Jump("loc_4F94")

    label("loc_4E8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EA0")
    Jump("loc_4F94")

    label("loc_4EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F36")

    #C0291
    ChrTalk(
        0xF,
        (
            "#03603F这次的事情\x01",
            "真是太感谢你们了。\x02\x03",

            "#03600F多亏你们，\x01",
            "迪利克和村长已经言归于好了。\x02\x03",

            "#03609F呵呵，找各位商量\x01",
            "果然是正确选择。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4F94")

    label("loc_4F36")


    #C0292
    ChrTalk(
        0xF,
        (
            "#03603F多亏你们，\x01",
            "迪利克和村长已经言归于好了。\x02\x03",

            "#03609F呵呵，找各位商量\x01",
            "果然是正确选择。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F94")

    Jump("loc_524A")

    label("loc_4F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_524A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5084")

    #C0293
    ChrTalk(
        0xF,
        (
            "#03603F我和这个村子做生意的时候，\x01",
            "与迪利克见过几次面。\x01",
            "他是个正直又有礼貌的好青年。\x02\x03",

            "#03608F如果他真的被卷入到了什么事件，\x01",
            "我实在是无法坐视不管。\x02\x03",

            "#03601F各位，请你们一定\x01",
            "要找到有用的情报。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_50F2")

    label("loc_5084")


    #C0294
    ChrTalk(
        0xF,
        (
            "#03608F如果他真的被卷入到了什么事件，\x01",
            "我实在是无法坐视不管。\x02\x03",

            "#03601F各位，请你们一定\x01",
            "要找到有用的情报。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50F2")

    Jump("loc_524A")

    label("loc_50F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D0")

    #C0295
    ChrTalk(
        0xF,
        (
            "#03608F虽然现在还不明白\x01",
            "敏涅斯这个人的真实目的……\x02\x03",

            "#03603F但关于这件事，我的看法和村长一样，\x01",
            "认为应该慎重考虑。\x02\x03",

            "#03600F非常感谢各位\x01",
            "陪我们一起商讨。\x02\x03",

            "以后要是出现了其它问题，\x01",
            "还要再麻烦你们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_524A")

    label("loc_51D0")


    #C0296
    ChrTalk(
        0xF,
        (
            "#03603F但关于这件事，我的看法和村长一样，\x01",
            "认为应该慎重考虑。\x02\x03",

            "#03600F各位，以后要是出现了其它问题，\x01",
            "还要再麻烦你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_524A")

    TalkEnd(0xFE)
    Return()

    # Function_15_4E3D end

    def Function_16_524E(): pass

    label("Function_16_524E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52FD")

    #C0297
    ChrTalk(
        0xFE,
        (
            "伊安律师正忙着\x01",
            "撰写宪法草案，\x01",
            "实在是抽不出时间过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "不过，看来事情已经圆满解决了，\x01",
            "这真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "我会把事情的详细经过\x01",
            "转告给伊安律师的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5357")

    label("loc_52FD")


    #C0300
    ChrTalk(
        0xFE,
        (
            "看来事情已经平安解决了，\x01",
            "这真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "我会把事情的详细经过\x01",
            "转告给伊安律师的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5357")

    TalkEnd(0xFE)
    Return()

    # Function_16_524E end

    def Function_17_535B(): pass

    label("Function_17_535B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53D1")

    #C0302
    ChrTalk(
        0xFE,
        (
            "……没想到阿鲁姆那个小家伙\x01",
            "已经变得这么出色了……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)

    #C0303
    ChrTalk(
        0xFE,
        "…………（抽泣）…………\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x12, 0x10)
    SetScenarioFlags(0x1, 1)
    Jump("loc_53EF")

    label("loc_53D1")


    #C0304
    ChrTalk(
        0xFE,
        "…………（抽泣）…………\x02",
    )

    CloseMessageWindow()

    label("loc_53EF")

    TalkEnd(0xFE)
    Return()

    # Function_17_535B end

    def Function_18_53F3(): pass

    label("Function_18_53F3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    LoadChrToIndex("chr/ch03102.itc", 0x20)
    LoadChrToIndex("chr/ch02702.itc", 0x21)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x107, 0x21)
    SetChrSubChip(0x107, 0x0)
    BeginChrThread(0x107, 3, 0, 0)
    SetMapObjFrame(0xFF, "kage03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ha03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika00", 0x0, 0x1)
    SetChrPos(0x101, -38500, 200, -1500, 90)
    SetChrPos(0x103, -38500, 200, -2800, 90)
    SetChrPos(0x105, -34300, 200, -1700, 270)
    SetChrPos(0x107, -38700, 0, 600, 90)
    SetChrPos(0xB, -36300, 200, 100, 180)
    OP_68(-36290, 2500, -2150, 0)
    MoveCamera(327, 15, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Sleep(1000)
    OP_68(-36290, 1500, -2150, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0305
    ChrTalk(
        0xB,
        (
            "#11P原来如此，\x01",
            "是这么一回事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xB,
        (
            "#11P你刚才带着\x01",
            "这位狼阁下来访的时候，\x01",
            "我吓得腿都软了。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        "#00006F#5P真、真抱歉。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x107,
        (
            "#01200F#5P#3C唔，看来是我\x01",
            "考虑得不够周全啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xB,
        (
            "#11P哪里哪里，能亲眼见到\x01",
            "传说中的神狼，\x01",
            "是我无上的光荣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xB,
        (
            "#11P那些所谓的『国防军』\x01",
            "几乎不来这个村子……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xB,
        (
            "#11P你们想留多久\x01",
            "就留多久吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        "#00002F#5P……非常感谢。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        "#00204F#6P真是帮了大忙。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x105,
        (
            "#10406F#12P话说回来，医院那里\x01",
            "有不少人在批评总统……\x02\x03",

            "#10401F这个村子里对迪塔总统的评价\x01",
            "似乎也不太好？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        (
            "#11P唔……因为那个人和我们村子\x01",
            "原本就没什么牵扯。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xB,
        (
            "#11P他说要建立什么『独立国』，\x01",
            "我们也完全搞不懂……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xB,
        (
            "#11P另外，因为那些『幻兽』的出现，\x01",
            "农作物的收成已经陷入低谷。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xB,
        (
            "#11P面对如此状况，国防军竟然也只是\x01",
            "偶尔来巡逻一下而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        "#00006F#5P这样啊……\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x103,
        "#00206F#6P……实在是太不重视了。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x107,
        (
            "#01203F#5P#3C市里人一般都不会\x01",
            "在意周围的村庄……\x02\x03",

            "#01201F不过，这还是\x01",
            "太过分了。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xB,
        (
            "#11P是啊……老实说，\x01",
            "我也觉得跟不上总统的想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xB,
        (
            "#11P但和人口繁多的\x01",
            "克洛斯贝尔市相比，\x01",
            "这个村子的影响力确实是微不足道……\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xB,
        (
            "#11P说实话，我一直在思考\x01",
            "今后到底该怎么办。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x105,
        "#10408F#12P唔，这样啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0326
    ChrTalk(
        0x101,
        (
            "#00003F#5P我们也会留意\x01",
            "『幻兽』的。\x02\x03",

            "#00001F除此之外，最近还遇到\x01",
            "其它困难了吗？\x02\x03",

            "比如说，村里的治安和\x01",
            "气氛有所恶化之类的……\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xB,
        (
            "#11P不，所幸还没到\x01",
            "那个程度。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xB,
        (
            "#11P现在我们正准备\x01",
            "全村人齐心协力，\x01",
            "共同努力渡过这道难关。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xB,
        (
            "#11P哈罗德他们一家\x01",
            "也在尽力协助我们呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0330
    ChrTalk(
        0x101,
        "#00005F#5P哈罗德先生……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 0)), scpexpr(EXPR_END)), "loc_5B43")

    #C0331
    ChrTalk(
        0x103,
        (
            "#00208F#6P说起来……\x01",
            "他的确说过要全家\x01",
            "一起出去玩呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B6C")

    label("loc_5B43")


    #C0332
    ChrTalk(
        0x103,
        (
            "#00205F#6P他们一家现在都\x01",
            "在这里吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B6C")


    #C0333
    ChrTalk(
        0xB,
        (
            "#11P是啊，发生异变时，\x01",
            "他们一家刚好来这里玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xB,
        (
            "#11P随后，上面就突然\x01",
            "颁布了禁行令，\x01",
            "他们只能留在这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        "#00003F#5P这样啊……\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xB,
        (
            "#11P哈罗德他们一家\x01",
            "住在旅馆的二楼。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xB,
        "#11P你们要是有空，可以去看看他们。\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        "#00000F#5P好的，我明白了。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x105,
        "#10400F#12P那我们这就去拜访他们吧。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    EndChrThread(0x107, 0x3)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, -40400, 0, -1800, 270)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A1, 3)
    OP_29(0xAF, 0x1, 0x4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_53F3 end

    def Function_19_5D05(): pass

    label("Function_19_5D05")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-37080, 1500, -1060, 0)
    MoveCamera(329, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -38110, 0, 380, 180)
    SetChrPos(0x102, -37060, 0, 1370, 180)
    SetChrPos(0x103, -39710, 0, -190, 135)
    SetChrPos(0x104, -35620, 0, 1220, 180)
    SetChrPos(0x109, -38610, 0, 2220, 180)
    SetChrPos(0x105, -39730, 0, 1380, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_611E")

    #C0340
    ChrTalk(
        0xB,
        (
            "唔……\x01",
            "迪利克那家伙\x01",
            "到底在做什么啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xF,
        (
            "#03603F真让人担心啊……\x01",
            "难道他……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#00000F特鲁塔村长，您好，\x01",
            "我们是特别任务支援科……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    #C0343
    ChrTalk(
        0x101,
        "#00005F哎……哈罗德先生？\x02",
    )

    CloseMessageWindow()

    def lambda_5E88():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E88)
    Sleep(50)

    def lambda_5E98():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E98)
    Sleep(50)

    def lambda_5EA8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5EA8)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xB, 0x1)

    #C0344
    ChrTalk(
        0xB,
        (
            "哦哦，各位……\x01",
            "我正等着你们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xF,
        (
            "#03600F你们是看到委托后过来的吧？\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#00012F没、没错……\x02\x03",

            "#00005F不过，为什么连哈罗德先生\x01",
            "都在这里？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xB,
        (
            "嗯，其实……\x01",
            "这件事和他\x01",
            "也有关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xF,
        (
            "#03603F我和村长商量到最后，\x01",
            "决定请各位来帮忙。\x02\x03",

            "#03601F因为事情有些严重，\x01",
            "所以我们觉得还是请专业的\x01",
            "调查人员来处理比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Sleep(300)

    #C0349
    ChrTalk(
        0x102,
        (
            "#00101F看来事态\x01",
            "相当严重呢。\x02\x03",

            "#00103F如果没记错，委托好像与\x01",
            "村长的儿子有关……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_608A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_608A)
    Sleep(50)

    def lambda_609A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_609A)
    Sleep(50)

    def lambda_60AA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_60AA)
    Sleep(300)

    #C0350
    ChrTalk(
        0xB,
        "嗯，事情有些复杂。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xB,
        (
            "如果你们愿意接下这个委托，\x01",
            "我会告诉你们详细内容……\x01",
            "你们现在有时间吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_618C")

    label("loc_611E")

    SetChrSubChip(0xB, 0x1)

    #C0352
    ChrTalk(
        0xB,
        "哦，你们现在有空了吗？\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xB,
        (
            "如果你们愿意接下这个委托，\x01",
            "我会告诉你们详细内容……\x01",
            "现在可以接受委托吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_618C")

    Call(0, 20)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -41050, 0, -1950, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_19_5D05 end

    def Function_20_61BB(): pass

    label("Function_20_61BB")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",              # 0
            "【还没做好准备】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6225"),
        (1, "loc_622D"),
        (SWITCH_DEFAULT, "loc_62C8"),
    )


    label("loc_6225")

    Call(0, 21)
    Jump("loc_62C8")

    label("loc_622D")


    #C0354
    ChrTalk(
        0x101,
        (
            "#00006F非常抱歉……\x01",
            "我们现在有些忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xB,
        "唔，这样啊……\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xB,
        (
            "那就等你们有空时\x01",
            "再来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xB,
        (
            "很希望你们能\x01",
            "助我一臂之力啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x173, 7)
    Jump("loc_62C8")

    label("loc_62C8")

    Return()

    # Function_20_61BB end

    def Function_21_62C9(): pass

    label("Function_21_62C9")


    #C0358
    ChrTalk(
        0x101,
        (
            "#00000F嗯，没问题。\x01",
            "请告诉我们详情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xB,
        "好的，实在是感激不尽。\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xB,
        (
            "……其实，最近这段时间，\x01",
            "我儿子迪利克的行为很可疑。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xB,
        (
            "他好像在暗地里策划着\x01",
            "什么不好的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x104,
        "#00305F不好的事是指……？\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xB,
        (
            "我也不知道具体内容……\x01",
            "总之就是搞不懂他在想什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xB,
        (
            "前段时间，他还擅自对哈罗德说了\x01",
            "『请你不要再来村子做生意了』\x01",
            "之类的话。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0365
    ChrTalk(
        0x101,
        (
            "#00005F不要来村子做生意……？\x01",
            "为什么会突然说出那种话？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    #C0366
    ChrTalk(
        0x101,
        (
            "#00003F我记得哈罗德先生\x01",
            "一直和阿尔摩利卡村\x01",
            "保持着友好的关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xF,
        (
            "#03608F是啊，我也觉得\x01",
            "自己和这个村子的关系\x01",
            "一直都很不错……\x02\x03",

            "#03601F所以我当时就想，\x01",
            "或许是自己做错了什么事，\x01",
            "于是就跑来询问村长。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x105,
        (
            "#10303F结果一问之下，\x01",
            "你发现村长也\x01",
            "毫不知情……\x02\x03",

            "#10300F就是这么一回事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xB,
        (
            "没错……\x01",
            "真是太对不起\x01",
            "哈罗德了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0370
    ChrTalk(
        0xB,
        (
            "如果失去他这么好的生意伙伴，\x01",
            "对村子来说，必定是重大损失……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xB,
        (
            "我儿子绝不会\x01",
            "不懂这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        (
            "#00103F的确是难以理解啊……\x02\x03",

            "#00101F令郎是不是\x01",
            "遇到了什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xB,
        (
            "嗯，我也这么认为，\x01",
            "所以就和哈罗德一起\x01",
            "展开了调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xB,
        (
            "结果……\x01",
            "某个来历不明的\x01",
            "人物浮出了水面。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xB,
        (
            "那小子最近似乎\x01",
            "时常与一名\x01",
            "可疑的外国人会面。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x109,
        "#10105F外国人吗……？\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xF,
        (
            "#03603F我们也不了解\x01",
            "具体详情……\x02\x03",

            "#03601F不过，他应该正与\x01",
            "迪利克私下商量着\x01",
            "什么事。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x105,
        (
            "#10303F唔……是密谈吗，\x01",
            "的确非常可疑呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xB,
        (
            "因此我想拜托你们\x01",
            "详细调查一下\x01",
            "那个外国人。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xB,
        (
            "如果他在打什么坏主意，\x01",
            "就得早点采取对策。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x103,
        (
            "#00203F可是……\x01",
            "这件事情并不需要\x01",
            "特地委托我们吧？\x02\x03",

            "#00200F我认为直接向令郎询问\x01",
            "才是最合理的选择……\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        "#00306F喂喂，阿缇……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xB,
        (
            "……嗯，不怕各位笑话，\x01",
            "其实这位小姑娘说的没错。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xB,
        (
            "但我和我儿子对村子的\x01",
            "发展方向有不同观点，\x01",
            "长久以来一直冲突不断……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xB,
        (
            "所以我虽然出言询问过他，\x01",
            "但他却什么都没有告诉我。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xB,
        "身为父亲，可真是丢脸啊。\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        "#00106F哪里的话……\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x101,
        (
            "#00003F……总之，我们已经明白了，\x01",
            "立刻就会展开调查。\x02\x03",

            "#00000F首先，我想向村民们\x01",
            "打听一下消息……\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xB,
        "好，那就拜托你们了。\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xB,
        (
            "不过，迪利克和\x01",
            "一个叫艾尔琴的青年\x01",
            "一起去市里送农作物了。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xB,
        (
            "你们可以稍后再\x01",
            "询问他本人。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xF,
        (
            "#03600F各位，请你们一定要\x01",
            "要找到有用的情报。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    #C0393
    ChrTalk(
        0x101,
        "#00000F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0394
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查可疑人物】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x82, 0x1, 0x0)
    SetScenarioFlags(0x174, 0)
    SetChrSubChip(0xB, 0x0)
    Return()

    # Function_21_62C9 end

    def Function_22_6B79(): pass

    label("Function_22_6B79")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(35510, 1500, -2430, 0)
    MoveCamera(288, 34, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 34950, 0, -2440, 225)
    SetChrPos(0x102, 34150, 0, -1180, 180)
    SetChrPos(0x103, 35670, 0, -3780, 270)
    SetChrPos(0x104, 35390, 0, -1060, 225)
    SetChrPos(0x109, 34780, 0, 40, 180)
    SetChrPos(0x105, 35960, 0, -2370, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0xA, 0x2D, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0395
    ChrTalk(
        0x101,
        (
            "#00003F您好，我有点事情\x01",
            "想向您咨询……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0396
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "询问了最近来访村里的\x01",
            "外国人的情况。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0397
    ChrTalk(
        0xA,
        "哦，你说那个人啊。\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xA,
        (
            "唔……一定要说的话，\x01",
            "他是个很不错的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x103,
        "#00205F很不错的人吗……？\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xA,
        (
            "嗯，有一次，我家的两个小孩\x01",
            "玩耍的时候，他刚好路过，\x01",
            "孩子们不小心弄脏了他的衣服……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xA,
        (
            "但他完全没有放在心上，\x01",
            "还很亲切地送了糕点\x01",
            "给我家的小孩。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xA,
        (
            "我当时的心情真是\x01",
            "又抱歉又感动，\x01",
            "实在是很佩服他的修养。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        (
            "#00003F原来如此……\x01",
            "非常感谢您协助调查。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x174, 3)
    OP_29(0x82, 0x1, 0x3)
    SetChrPos(0x0, 34950, 0, -2440, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_6B79 end

    def Function_23_6E41(): pass

    label("Function_23_6E41")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-37080, 2500, -1060, 0)
    MoveCamera(329, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -38110, 0, 380, 180)
    SetChrPos(0x102, -37060, 0, 1370, 180)
    SetChrPos(0x103, -39710, 0, -190, 135)
    SetChrPos(0x104, -35620, 0, 1220, 180)
    SetChrPos(0x109, -38610, 0, 2220, 180)
    SetChrPos(0x105, -39730, 0, 1380, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x1)
    OP_68(-37080, 1500, -1060, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0404
    ChrTalk(
        0xB,
        (
            "没想到……\x01",
            "那个叫敏涅斯的人\x01",
            "竟然是昆西公司的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xB,
        (
            "还有……\x01",
            "『阿尔摩利卡·甜蜜商社』吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xF,
        (
            "#03605F在私有地建造工厂……\x01",
            "没想到他竟在暗中策划着这么\x01",
            "庞大的计划……\x02\x03",

            "#03608F迪利克\x01",
            "怎么会……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#00005F请问……\x01",
            "迪利克先生现在在哪里？\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x102,
        (
            "#00105F啊……如此说来，\x01",
            "一直没有见到他呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x109,
        (
            "#10100F我们在酒店擦肩而过时，\x01",
            "他说要回村子的。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xB,
        (
            "唔……\x01",
            "其实他这段时间\x01",
            "已经很少回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xB,
        (
            "最近都住在\x01",
            "『白蜡亭』。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xB,
        (
            "那个叫敏涅斯的人\x01",
            "曾到旅馆去找过他，\x01",
            "也许他就是为此才搬过去住的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xB,
        (
            "也正因如此，我才完全没有察觉到\x01",
            "那个在私有地建造工厂的计划。\x01",
            "……唉，说起来，还真是丢脸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x105,
        (
            "#10303F这个嘛……\x02\x03",

            "#10300F也没准是那个商人\x01",
            "劝说他搬过去住的呢。\x02\x03",

            "#10304F目的是为了不让村长获得情报。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0415
    ChrTalk(
        0xB,
        "这、这是什么意思……？\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x105,
        (
            "#10300F接下来，还是交给\x01",
            "我们的队长来说明吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        "#00006F你可真是……\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xF,
        (
            "#03605F罗伊德警官，\x01",
            "你发现了什么\x01",
            "令人在意的情况吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    #C0419
    ChrTalk(
        0x101,
        (
            "#00003F……这仅仅是我们的\x01",
            "直觉而已……\x02\x03",

            "#00001F那个叫敏涅斯的人\x01",
            "存在着几个疑点。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0420
    ChrTalk(
        0xB,
        "你说什么……！？\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x101,
        (
            "#00001F他描述的那项计划\x01",
            "可以让所有参与人员\x01",
            "获得利益。\x02\x03",

            "#00003F阿尔摩利卡村将会得到新的产业，\x01",
            "昆西公司则能得到一个\x01",
            "前途无量的子公司。\x02\x03",

            "#00008F他说的话，听上去\x01",
            "非常具有吸引力……\x02\x03",

            "#00001F但是未免也太过诱人了，\x01",
            "你们不这样认为吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xF,
        (
            "#03605F……！\x01",
            "听、听你这么一说……\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x103,
        (
            "#00203F而且敏涅斯先生\x01",
            "还把新型导力卡车\x01",
            "廉价转让给了村子。\x02\x03",

            "#00200F这可以\x01",
            "看作一种\x01",
            "『事前投资』。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x109,
        (
            "#10108F新型的导力车\x01",
            "现在十分昂贵，\x01",
            "这是毫无疑问的……\x02\x03",

            "#10101F竟然以五万米拉的超低价格出售，\x01",
            "这实在是太不可思议了。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x104,
        (
            "#00303F反过来说，这就意味着……\x02\x03",

            "#00301F他已经『预料』到了，\x01",
            "将来肯定有办法\x01",
            "把这笔钱收回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xF,
        (
            "#03601F这……\x01",
            "的确很可疑啊。\x02\x03",

            "#03603F像昆西公司这样的大公司，\x01",
            "是绝不会推行牺牲自己利益的\x01",
            "计划的。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xB,
        "唔，你说的没错……\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xB,
        (
            "总觉得这件事\x01",
            "越来越可疑了……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0429
    ChrTalk(
        0x101,
        (
            "#00001F敏涅斯还有别的目的……\x01",
            "或者说，他有一定能\x01",
            "赚到钱的办法。\x02\x03",

            "#00003F虽然还没有任何证据……\x01",
            "但小心起见，还是多注意\x01",
            "一下比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xB,
        (
            "唔……\x01",
            "我会多加注意的。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xB,
        (
            "……总之，\x01",
            "真是辛苦你们了，\x01",
            "特别任务支援科的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xB,
        (
            "多亏有你们帮忙，\x01",
            "我对这件事已经有了一定程度的了解。\x01",
            "非常感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x101,
        (
            "#00003F不，这倒没什么……\x02\x03",

            "#00005F不过，这样就够了吗？\x01",
            "我们可以继续调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xB,
        "不……目前来说，这样就够了。\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xB,
        (
            "因为我绝不会允许他们\x01",
            "擅自在村子的私有地\x01",
            "建造工厂。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xB,
        (
            "我会以村长的身份\x01",
            "去和迪利克谈一谈，\x01",
            "想办法说服他。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        "#00103F……嗯，这样最好。\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x101,
        (
            "#00003F那么，我们这就\x01",
            "告辞了。\x02\x03",

            "#00000F如果发生了其它情况，\x01",
            "请随时联系我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xB,
        (
            "好的……\x01",
            "到时候就麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0440
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查可疑人物】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x82, 0x1, 0x7)
    OP_29(0x82, 0x1, 0x8)
    OP_29(0x82, 0x4, 0x10)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0x0, -41050, 0, -1950, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_6E41 end

    def Function_24_797D(): pass

    label("Function_24_797D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    LoadChrToIndex("chr/ch09300.itc", 0x1F)
    OP_68(-46010, 3100, -2510, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xB, -47740, 0, -120, 180)
    SetChrPos(0xF, -48950, 0, -2510, 45)
    SetChrPos(0xD, -46260, 0, 50, 180)
    SetChrPos(0x10, -49140, 0, -3150, 45)
    SetChrPos(0x101, -47540, 0, -1830, 0)
    SetChrPos(0x102, -46230, 0, -1750, 315)
    SetChrPos(0x103, -44810, 0, -1320, 315)
    SetChrPos(0x104, -45630, 0, -3150, 315)
    SetChrPos(0x109, -46960, 0, -3110, 0)
    SetChrPos(0x105, -44330, 0, -2660, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-46010, 1900, -2510, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0441
    ChrTalk(
        0xB,
        "各位，干得漂亮。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xB,
        (
            "多亏你们，\x01",
            "村子才能逃离那个\x01",
            "诈骗犯的魔爪。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x101,
        (
            "#00006F我们最终还是\x01",
            "没能抓到犯人……\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x102,
        (
            "#00103F不过，已经报告给了\x01",
            "警察总部……\x02\x03",

            "#00100F抓住他也只是\x01",
            "时间问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xD,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xF,
        "#03605F迪利克？\x02",
    )

    CloseMessageWindow()

    def lambda_7BC1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7BC1)
    Sleep(50)

    def lambda_7BD1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7BD1)
    Sleep(50)

    #C0447
    ChrTalk(
        0xD,
        (
            "……我真是给各位\x01",
            "添了不少麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xD,
        (
            "都怪我中了\x01",
            "诈骗犯的圈套，\x01",
            "才会闹出这么大的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x109,
        "#10108F这并不是你的错啊……\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xD,
        (
            "不……\x01",
            "全都是我的错。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xD,
        (
            "都怪我一心想要改革，\x01",
            "还和老爸赌气……\x01",
            "最后才搞成这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xD,
        (
            "我根本没资格\x01",
            "当下任村长。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 500)
    Sleep(300)

    #C0453
    ChrTalk(
        0xB,
        "……没有的事。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 500)
    Sleep(300)

    #C0454
    ChrTalk(
        0xD,
        "老爸……？\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xB,
        (
            "我太固执于自己的\x01",
            "保守想法，完全\x01",
            "听不进你的意见。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xB,
        (
            "明知道再这样下去，\x01",
            "村子会渐渐荒废，\x01",
            "但却没有采取任何行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xB,
        (
            "关于这次的事情，\x01",
            "我也应该承担很大的责任。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xF,
        "#03608F村长……\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    #C0459
    ChrTalk(
        0xB,
        (
            "经过这次的事情，\x01",
            "我想了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xB,
        (
            "为了守护这个村子，\x01",
            "我绝不能固执于\x01",
            "自己的想法。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 500)
    Sleep(300)

    #C0461
    ChrTalk(
        0xB,
        (
            "迪利克……\x01",
            "今后一定要把\x01",
            "你的智慧借给我啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xB,
        (
            "我们一起提出方案，\x01",
            "和全村人讨论……\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xB,
        (
            "共同为了阿尔摩利卡村\x01",
            "而努力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xD,
        (
            "……嗯，好的。\x01",
            "抱歉，老爸……\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xD,
        (
            "我今后一定会比以前\x01",
            "更加努力地思考\x01",
            "村子的未来。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x102,
        (
            "#00102F呵呵……\x01",
            "看来他们已经和好了，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        "#00309F哈哈，是啊。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x105,
        (
            "#10304F能得到这种结果，\x01",
            "遭遇诈骗犯似乎\x01",
            "也不是件坏事呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_806D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_806D)
    Sleep(50)

    def lambda_807D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_807D)
    Sleep(50)

    def lambda_808D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_808D)
    Sleep(50)

    def lambda_809D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_809D)
    Sleep(50)

    def lambda_80AD():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_80AD)
    Sleep(50)

    def lambda_80BD():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_80BD)
    Sleep(50)

    def lambda_80CD():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_80CD)
    Sleep(50)

    def lambda_80DD():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_80DD)
    Sleep(50)

    def lambda_80ED():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_80ED)
    Sleep(300)

    #C0469
    ChrTalk(
        0x109,
        "#10106F瓦、瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x103,
        "#00200F唔，凡事都有两面性啊……\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x101,
        (
            "#00006F不、不对不对，\x01",
            "再怎么说，这话说得也太随便了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    #C0472
    ChrTalk(
        0xB,
        "总、总之……\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xB,
        (
            "这次真是多亏\x01",
            "有你们相助。\x01",
            "请让我郑重向你们道谢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_81C7():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81C7)
    Sleep(50)

    def lambda_81D7():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_81D7)
    Sleep(50)

    def lambda_81E7():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_81E7)
    Sleep(50)

    def lambda_81F7():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_81F7)
    Sleep(50)

    def lambda_8207():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8207)
    Sleep(50)

    def lambda_8217():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8217)
    Sleep(50)

    def lambda_8227():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8227)
    Sleep(50)

    def lambda_8237():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8237)
    Sleep(50)

    def lambda_8247():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8247)
    Sleep(300)

    #C0474
    ChrTalk(
        0xB,
        (
            "还有伊安律师那边，\x01",
            "也得专程去向他道谢才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x10,
        (
            "我会向律师转述\x01",
            "事情的详细经过的。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xF,
        (
            "#03604F能为解决这起事件\x01",
            "而发挥作用，我也很高兴。\x02\x03",

            "#03600F今后也要请您\x01",
            "多多关照了，村长。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xB,
        "哈哈，彼此彼此。\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        (
            "#00003F为防万一，大家还是要\x01",
            "对那个诈骗犯多加留意。\x02\x03",

            "#00000F今后如果遇到了其它问题，\x01",
            "请随时联系我们支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xD,
        (
            "好的，拜托你们了。\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0480
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查可疑商人】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x87, 0x1, 0xA)
    OP_29(0x87, 0x1, 0xB)
    OP_29(0x87, 0x4, 0x10)
    SetChrPos(0xB, -38480, 180, -1780, 90)
    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xF, -34200, 180, -1530, 270)
    SetChrChipByIndex(0xF, 0x2)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrPos(0xD, -38050, 0, -140, 180)
    SetChrPos(0x10, -34400, 0, -300, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrPos(0x0, -46650, 0, -1460, 135)
    OP_69(0xFF, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_24_797D end

    def Function_25_84B3(): pass

    label("Function_25_84B3")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xB, 0x0, 0x0)
    OP_68(-37850, 1500, -940, 0)
    MoveCamera(327, 34, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26120, 0)
    SetChrPos(0x101, -38350, 0, -70, 180)
    SetChrPos(0x102, -39580, 0, -40, 135)
    SetChrPos(0x103, -37610, 0, 1040, 180)
    SetChrPos(0x104, -39030, 0, 1050, 180)
    SetChrPos(0x109, -38350, 0, 1950, 180)
    SetChrPos(0x105, -40330, 0, 1370, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0481
    ChrTalk(
        0x101,
        "#00000F您好，特鲁塔村长。\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xB,
        (
            "噢，是特别任务支援科的各位啊。\x01",
            "你们今天有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#00000F其实我们\x01",
            "有件事情\x01",
            "想问问您……\x02\x03",

            "#00003F请问养蜂场的仓库里\x01",
            "有没有住人？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0484
    ChrTalk(
        0xB,
        (
            "唔，现在的确\x01",
            "有人在住呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xB,
        (
            "那是三、四天前的事了。\x01",
            "有人突然拜托我，\x01",
            "让他在那里『暂住几天』。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xB,
        (
            "我记得……\x01",
            "是个叫盖巴尔的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x102,
        (
            "#00105F果然……！\x02\x03",

            "#00106F可是，为什么要住在仓库呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xB,
        (
            "我也这样问过他，\x01",
            "并建议他去住旅馆……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xB,
        (
            "可他却说『想尽量住在不起眼的地方』，\x01",
            "完全不听我劝。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xB,
        (
            "我问他理由，他也什么都不肯说，\x01",
            "我猜他可能是被卷入到\x01",
            "某些重大事件了……\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xB,
        (
            "没想到，他竟然是\x01",
            "你们在找的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xB,
        (
            "难道他是什么案子的\x01",
            "犯人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x103,
        "#00203F不，并不是这样的。\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x109,
        (
            "#10100F罗伊德警官，还是先把\x01",
            "具体情况\x01",
            "告诉村长吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x101,
        "#00003F嗯，好的……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0496
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德把受阿鲁姆和艾娅莉委托，\x01",
            "前来寻找盖巴尔的事情做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0497
    ChrTalk(
        0xB,
        (
            "唔，原来如此……\x01",
            "他原本是个议员啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xB,
        (
            "前段时间因为逃税嫌疑\x01",
            "而装病躲进医院的议员……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xB,
        (
            "听你这么一说，我好像曾在克洛斯贝尔\x01",
            "时代周刊上看到过他的照片呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x105,
        (
            "#10304F不过，这次的事情和逃税\x01",
            "并没有直接关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x101,
        (
            "#00000F特鲁塔村长，我们可以和\x01",
            "仓库里的盖巴尔先生谈谈吗？\x02\x03",

            "#00008F我们也知道他并不想见\x01",
            "阿鲁姆先生，但是……\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xB,
        "……唔，好吧。\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xB,
        (
            "我也和儿子发生过争执，\x01",
            "其中最大的原因就是\x01",
            "我们之间缺少沟通。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xB,
        (
            "我可不能让别人\x01",
            "重蹈覆辙。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        "#00002F村长……\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xB,
        "呵呵，你们跟我来吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_84B3 end

    def Function_26_8AAD(): pass

    label("Function_26_8AAD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(76390, 1500, 1360, 0)
    MoveCamera(315, 32, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    OP_4B(0x12, 0xFF)
    SetChrChipByIndex(0x12, 0xC)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 75800, 0, 2000, 0)
    SetChrChipByIndex(0xB, 0xB)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x101, 75070, 0, -5420, 0)
    SetChrPos(0x102, 75070, 0, -5420, 0)
    SetChrPos(0x103, 75070, 0, -5420, 0)
    SetChrPos(0x104, 75070, 0, -5420, 0)
    SetChrPos(0x109, 75070, 0, -5420, 0)
    SetChrPos(0x105, 75070, 0, -5420, 0)
    SetChrPos(0xB, 75070, 0, -5420, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(76600, 1500, -270, 3000)
    BeginChrThread(0x101, 3, 0, 27)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 28)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 29)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 30)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 31)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 32)
    Sleep(500)
    BeginChrThread(0xB, 3, 0, 33)
    WaitChrThread(0xB, 3)
    OP_6F(0x1)

    #C0507
    ChrTalk(
        0x101,
        (
            "#00000F请问，是盖巴尔先生吧……？\x02\x03",

            "#00006F呼，总算找到您了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    #C0508
    ChrTalk(
        0x12,
        (
            "#4P哼……\x01",
            "你们还真是热爱工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x12,
        (
            "#4P我知道我儿子和\x01",
            "儿媳一直在找我……\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x12,
        (
            "#4P但不管你们说什么，\x01",
            "我都不会去见他们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x109,
        "#10106F您、您为什么要如此固执呢……？\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x12,
        "#4P……这还用问。\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x12,
        (
            "#4P因为我儿子……\x01",
            "阿鲁姆一定\x01",
            "非常恨我。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x103,
        "#00205F恨您……？\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x105,
        (
            "#10301F如果方便，\x01",
            "可以把其中的原委告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x12,
        (
            "#4P……我从见习议员的时代开始，\x01",
            "就染指了各种各样的渎职行为。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x12,
        (
            "#4P我完全是为了地位、名声和钱而工作，\x01",
            "从来都不顾及自己的家人。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x12,
        (
            "#4P我的妻子虽然对我感到不满，\x01",
            "但还是专心养育年幼的阿鲁姆，\x01",
            "想借此来忘记烦恼。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x12,
        (
            "#4P但我却因此而越发肆无忌惮，\x01",
            "有一天……我犯下了为人父母者\x01",
            "绝不能犯的错误。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x12,
        (
            "#4P我趁着妻子出门，把我当时的\x01",
            "情妇带到了自己家里。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0521
    ChrTalk(
        0x109,
        "#10106F这、这实在是……\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x104,
        "#00306F实在是相当过分啊……\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x12,
        (
            "#4P这件事很快就被妻子知道了，\x01",
            "她对我彻底心灰意冷之后，\x01",
            "带着阿鲁姆回到了故乡利贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x12,
        (
            "#4P他们之后的生活情况，我完全不了解……\x01",
            "但离婚这件事肯定让妻子和阿鲁姆\x01",
            "受了不少苦。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x12,
        (
            "#4P可我不但没有反省，反而还觉得\x01",
            "甩掉了包袱，从此轻松自在。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x12,
        (
            "#4P正式办好离婚手续的第二天，\x01",
            "我就把另一名情妇带到了\x01",
            "那个比以往更加宽敞的住所……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x101,
        "#00003F这……\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x104,
        (
            "#00306F你做出了那种事，\x01",
            "就算被人恨也是正常的。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x103,
        (
            "#00211F……兰迪前辈，\x01",
            "你说得太直接了。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x12,
        (
            "#4P哼，那个红毛说得没错，\x01",
            "我确实是个可恨的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x12,
        (
            "#4P而且……说到底，我也只是\x01",
            "哈尔特曼前议长的一个跟班罢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x12,
        (
            "#4P我只不过是犯下了逃税这种小事，\x01",
            "前议长就毫不犹豫地\x01",
            "和我断绝了关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x12,
        (
            "#4P在这种情况下，被捕入狱反倒\x01",
            "能让我乐得轻松，但讽刺的是，\x01",
            "他们竟然只是罢免我的职位。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x12,
        (
            "#4P如果让儿子看见我现在这种\x01",
            "已经失去一切的惨状……\x01",
            "我可受不了。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xB,
        "盖巴尔先生……\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x102,
        "#00103F原来是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0537
    ChrTalk(
        0x101,
        (
            "#00001F……那个，\x01",
            "我可以说一句吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x12,
        (
            "#4P……想说什么？\x01",
            "事到如今，不管你再说什么，我都……\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x101,
        (
            "#00003F……您确实对自己的\x01",
            "儿子和妻子做出了\x01",
            "十分过分的事情。\x02\x03",

            "身为一名堕落的政治家，\x01",
            "您可能还做过很多\x01",
            "见不得人的事。\x02\x03",

            "#00000F可是，从您刚才的话语中，\x01",
            "我能感受到您的悔意。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x102,
        (
            "#00103F……是啊。\x02\x03",

            "#00100F完全可以看出您有反省之意，\x01",
            "而且从社会角度来看，\x01",
            "您也已经受到制裁了。\x02\x03",

            "#00108F因为怀有罪恶感就避而不见，\x01",
            "这似乎有些说不通呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x12,
        "#4P可、可是……！\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        (
            "#00003F而且……\x02\x03",

            "#00002F我完全不觉得阿鲁姆先生\x01",
            "在憎恨您。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x12,
        "#4P……哎……？\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x101,
        (
            "#00004F委托我们寻找您的人\x01",
            "是阿鲁姆先生\x01",
            "和他的夫人艾娅莉女士……\x02\x03",

            "#00002F他们已经建立了一个温暖的家庭，\x01",
            "看上去十分幸福。\x02\x03",

            "在把这个任务委托给我们时，\x01",
            "阿鲁姆先生说他只有一个愿望……\x02\x03",

            "#00004F那就是……\x01",
            "『让父亲看看刚出生不久的孩子，让您知道\x01",
            "  他们已经建立了一个幸福的家庭』。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x12,
        "#4P……！\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x109,
        (
            "#10109F哈哈，的确如此。\x02\x03",

            "#10106F他们恩爱得简直\x01",
            "让人嫉妒呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x104,
        (
            "#00304F不错，哪怕心怀\x01",
            "一丝『恨意』，\x01",
            "都不可能流露出那种表情的。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x105,
        (
            "#10309F呵呵，这可难说。\x02\x03",

            "#10304F说不定他和我一样，\x01",
            "喜怒不形于色呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x105, 500)
    Sleep(300)

    #C0549
    ChrTalk(
        0x103,
        (
            "#00211F……瓦吉先生，\x01",
            "请你不要捣乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x104,
        (
            "#00300F总之，盖巴尔先生，\x01",
            "您的儿子已经茁壮成长为\x01",
            "一名很开朗的人了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    #C0551
    ChrTalk(
        0x101,
        "#00004F……我们能说的也只有这些了。\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x102,
        (
            "#00100F如何……\x01",
            "您要不要和阿鲁姆先生\x01",
            "他们见个面呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x12,
        "#4P…………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0x0, 0x1F4)
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    Sleep(2000)
    OP_64(0x12)

    #C0554
    ChrTalk(
        0x12,
        (
            "#4P……既然你们都这么说了……\x01",
            "我也不是一定不能见他们。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0555
    ChrTalk(
        0x101,
        "#00005F真、真的吗？\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    #C0556
    ChrTalk(
        0x12,
        "#4P哼，我干嘛要骗你们。\x02",
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x12,
        (
            "#4P……好了，在我改变想法之前，\x01",
            "赶紧去叫他们来吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x101,
        (
            "#00011F我、我明白了！\x01",
            "那我现在就去找他们！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 35)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 36)
    Sleep(300)
    OP_68(76460, 1500, -1540, 2000)
    BeginChrThread(0x101, 3, 0, 34)

    def lambda_9A5F():

        label("loc_9A5F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9A5F")

    QueueWorkItem2(0x102, 1, lambda_9A5F)
    Sleep(50)

    def lambda_9A74():

        label("loc_9A74")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9A74")

    QueueWorkItem2(0x103, 1, lambda_9A74)
    Sleep(50)

    def lambda_9A89():

        label("loc_9A89")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9A89")

    QueueWorkItem2(0x104, 1, lambda_9A89)
    Sleep(50)

    def lambda_9A9E():

        label("loc_9A9E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9A9E")

    QueueWorkItem2(0x109, 1, lambda_9A9E)
    Sleep(50)

    def lambda_9AB3():

        label("loc_9AB3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9AB3")

    QueueWorkItem2(0x105, 1, lambda_9AB3)
    Sleep(50)

    def lambda_9AC8():

        label("loc_9AC8")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9AC8")

    QueueWorkItem2(0xB, 1, lambda_9AC8)
    WaitChrThread(0x101, 3)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0xB, 0x1)
    OP_6F(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0559
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，罗伊德\x01",
            "匆忙联络了『龙老饭店』……\x02\x03",

            "把阿鲁姆和艾娅莉\x01",
            "叫到了阿尔摩利卡村。\x02\x03",

            "之后，由于盖巴尔还需要做些心理准备，\x01",
            "一行人便在仓库外面等待。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_8AAD end

    def Function_27_9BA9(): pass

    label("Function_27_9BA9")


    def lambda_9BAE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9BAE)

    def lambda_9BBF():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9BBF)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 75280, 0, 270, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_27_9BA9 end

    def Function_28_9BF4(): pass

    label("Function_28_9BF4")


    def lambda_9BF9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9BF9)

    def lambda_9C0A():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9C0A)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 76460, 0, 280, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_28_9BF4 end

    def Function_29_9C3F(): pass

    label("Function_29_9C3F")


    def lambda_9C44():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9C44)

    def lambda_9C55():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9C55)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 75260, 0, -920, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_29_9C3F end

    def Function_30_9C8A(): pass

    label("Function_30_9C8A")


    def lambda_9C8F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9C8F)

    def lambda_9CA0():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9CA0)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 76470, 0, -920, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_30_9C8A end

    def Function_31_9CD5(): pass

    label("Function_31_9CD5")


    def lambda_9CDA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9CDA)

    def lambda_9CEB():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9CEB)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 75210, 0, -2040, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_31_9CD5 end

    def Function_32_9D20(): pass

    label("Function_32_9D20")


    def lambda_9D25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9D25)

    def lambda_9D36():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9D36)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 76180, 0, -2040, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_32_9D20 end

    def Function_33_9D6B(): pass

    label("Function_33_9D6B")


    def lambda_9D70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_9D70)

    def lambda_9D81():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9D81)
    WaitChrThread(0xB, 1)
    OP_95(0xB, 77380, 0, -2650, 2000, 0x0)
    OP_95(0xB, 77640, 0, -310, 2000, 0x0)
    OP_93(0xB, 0x13B, 0x1F4)
    Return()

    # Function_33_9D6B end

    def Function_34_9DCA(): pass

    label("Function_34_9DCA")


    def lambda_9DCF():
        OP_95(0xFE, 75070, 0, -5420, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DCF)
    Sleep(1000)

    def lambda_9DEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9DEC)
    Return()

    # Function_34_9DCA end

    def Function_35_9DF9(): pass

    label("Function_35_9DF9")

    OP_93(0x103, 0x5A, 0x0)
    OP_9B(0x1, 0x103, 0xB4, 0x1F4, 0x7D0, 0x0)
    Return()

    # Function_35_9DF9 end

    def Function_36_9E10(): pass

    label("Function_36_9E10")

    OP_93(0x109, 0x5A, 0x0)
    OP_9B(0x1, 0x109, 0xB4, 0x2EE, 0x7D0, 0x0)
    Return()

    # Function_36_9E10 end

    def Function_37_9E27(): pass

    label("Function_37_9E27")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(76170, 1500, -1190, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(27560, 0)
    LoadChrToIndex("chr/ch46300.itc", 0x1E)
    LoadChrToIndex("chr/ch46200.itc", 0x1F)
    OP_4B(0x12, 0xFF)
    SetChrChipByIndex(0x12, 0xC)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 75790, 0, 2210, 0)
    SetChrChipByIndex(0x13, 0x1E)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 75070, 0, -5420, 0)
    SetChrChipByIndex(0x14, 0x1F)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 75070, 0, -5420, 0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x13, 3, 0, 38)
    Sleep(500)
    BeginChrThread(0x14, 3, 0, 39)
    OP_68(76070, 1500, 900, 4000)
    SetCameraDistance(24880, 4000)
    OP_6F(0x79)

    #C0560
    ChrTalk(
        0x13,
        "啊……\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x13,
        "是……爸爸吗？\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x13,
        "哈哈，好久不见了啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    #C0563
    ChrTalk(
        0x12,
        "嗯、嗯……\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x12,
        (
            "好、好久不见了啊，阿鲁姆。\x01",
            "有十五年没见了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x12,
        "那位是……\x02",
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x14,
        "您好，初次见面，爸爸。\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x14,
        (
            "我是阿鲁姆的妻子艾娅莉，\x01",
            "请您多多指教。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x12,
        "嗯、嗯……\x02",
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x12,
        (
            "我儿子竟然能娶到一位\x01",
            "这么可爱的姑娘，\x01",
            "我也感到面上有光啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x14,
        "哎呀，您过奖了……\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0571
    ChrTalk(
        0x12,
        "啊…………\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x12,
        (
            "……那、那是……\x01",
            "你手里抱着的是……\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x13,
        "呵呵，是我们的孩子啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    #C0574
    ChrTalk(
        0x13,
        (
            "……阿尔米，\x01",
            "和爷爷打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0575
    NpcTalk(
        0x14,
        "婴儿",
        "哇啊啊。\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x14,
        "哦哦，乖～乖～\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x12,
        "…………哈、哈哈…………\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x12)

    #C0578
    ChrTalk(
        0x12,
        (
            "那、那个……阿鲁姆。\x01",
            "我让你和妈妈\x01",
            "受了不少苦……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0x0, 0x1F4)
    Sleep(300)
    OP_63(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0579
    ChrTalk(
        0x13,
        "哎……？您在说什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    #C0580
    ChrTalk(
        0x13,
        (
            "先别说这个了，您看啊，爸爸，\x01",
            "阿尔米的眼睛多漂亮……\x01",
            "好像苍耀石一样美丽。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x13,
        (
            "艾娅莉……\x01",
            "就像你那宛如天空般\x01",
            "澄澈的瞳眸一样。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(300)

    #C0582
    ChrTalk(
        0x14,
        (
            "嗯，阿鲁姆，你再看他的耳朵……\x01",
            "阿尔米的耳形和你\x01",
            "简直一模一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x14,
        (
            "呵呵呵……\x01",
            "真想一口把它\x01",
            "吃掉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x13,
        (
            "啊～艾娅莉……\x01",
            "我一辈子都不会离开你和这孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x14,
        (
            "阿鲁姆……\x01",
            "我们要幸福一辈子哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x12)
    OP_93(0x12, 0x0, 0x1F4)
    Sleep(300)

    #C0586
    ChrTalk(
        0x12,
        "…………（抽泣）…………\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A392():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A392)
    Sleep(50)

    def lambda_A3A2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A3A2)
    Sleep(300)

    #C0587
    ChrTalk(
        0x13,
        "哎呀，爸爸……您怎么了？\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x14,
        (
            "阿鲁姆，爸爸是不是\x01",
            "身体不舒服？\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x12,
        (
            "……（抽泣）……\x01",
            "………没事……我没事……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4C(0x12, 0xFF)
    SetScenarioFlags(0x22, 3)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_9E27 end

    def Function_38_A44A(): pass

    label("Function_38_A44A")


    def lambda_A44F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_A44F)

    def lambda_A460():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A460)
    WaitChrThread(0x13, 1)
    OP_95(0x13, 74920, 0, 210, 2000, 0x0)
    OP_93(0x13, 0x0, 0x1F4)
    Return()

    # Function_38_A44A end

    def Function_39_A495(): pass

    label("Function_39_A495")


    def lambda_A49A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_A49A)

    def lambda_A4AB():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A4AB)
    WaitChrThread(0x14, 1)
    OP_95(0x14, 76120, 0, 210, 2000, 0x0)
    OP_93(0x14, 0x0, 0x1F4)
    Return()

    # Function_39_A495 end

    SaveToFile()

Try(main)
