from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c050b.bin",                # FileName
        "c050b",                    # MapName
        "c050b",                    # Location
        0x0026,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 38, 0, 3, 0, 4],
    )

    BuildStringList((
        "c050b",                  # 0
        "揽客员比修",             # 1
        "爱丽斯",                 # 2
        "赛尔盖科长",             # 3
        "蔡特",                   # 4
        "伊梅尔达夫人",           # 5
        "警备队员",               # 6
        "警备队员",               # 7
        "警备队员",               # 8
        "警备队员",               # 9
        "警备队员",               # 10
        "警备队员",               # 11
        "黑手党",                 # 12
        "黑手党",                 # 13
        "事件用ＮＰＣ",           # 14
        "事件用ＮＰＣ",           # 15
        "事件用ＮＰＣ",           # 16
        "SE控制",                 # 17
        "中央广场",               # 18
        "西街",                   # 19
        "行政区",                 # 20
        "住宅街",                 # 21
        "欢乐街",                 # 22
        "东街",                   # 23
        "旧城区",                 # 24
        "港湾区",                 # 25
        "ＩＢＣ",                 # 26
        "站前街道",               # 27
        "后巷",                   # 28
        "乌尔斯拉间道",           # 29
        "东克洛斯贝尔街道",       # 30
        "西克洛斯贝尔街道",       # 31
        "玛因兹山道",             # 32
    ))

    AddCharChip((
        "chr/ch26700.itc",                   # 00
        "chr/ch26900.itc",                   # 01
        "chr/ch31000.itc",                   # 02
        "chr/ch31100.itc",                   # 03
    ))

    DeclNpc(-7590,   0,       2980,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-6170,   0,       1399,    90,   261,  0x0, 0,   1,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-3210,   5800,    22030,   1200,    -3210,   6800,    22030,   0x007C, 0,  5,  0x0000)
    DeclActor(-10590,  5900,    9660,    1200,    -10590,  6900,    9660,    0x007C, 0,  6,  0x0000)
    DeclActor(11410,   0,       7030,    1200,    11410,   1000,    7030,    0x007C, 0,  7,  0x0000)

    PlaceName(79.5, 0.0, -9.0, 0x0000, 0x0000, "中央广场")
    PlaceName(0.0, 0.0, -76.5, 0x0000, 0x0000, "西街")
    PlaceName(11.0, 0.0, 116.0, 0x0000, 0x0000, "行政区")
    PlaceName(-148.0, 0.0, -60.0, 0x0000, 0x0000, "住宅街")
    PlaceName(-57.25, 0.0, 10.0, 0x0000, 0x0000, "欢乐街")
    PlaceName(196.0, 0.0, 56.0, 0x0000, 0x0000, "东街")
    PlaceName(294.0, 0.0, 31.0, 0x0000, 0x0000, "旧城区")
    PlaceName(154.0, 0.0, 158.0, 0x0000, 0x0000, "港湾区")
    PlaceName(20.0, 0.0, 233.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(168.0, 0.0, -73.0, 0x0000, 0x0000, "站前街道")
    PlaceName(1.0, 0.0, -9.0, 0x0000, 0x0000, "后巷")
    PlaceName(200.0, 0.0, -112.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(240.0, 0.0, 130.0, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-52.0, 0.0, -134.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-156.0, 0.0, -17.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(71.0, 0.0, -49.0, 0x0000, 0x0051, "")
    PlaceName(100.5, 0.0, 38.5, 0x0000, 0x0054, "")
    PlaceName(106.0, 0.0, -31.0, 0x0000, 0x0057, "")
    PlaceName(38.0, 0.0, -18.5, 0x0000, 0x0053, "")
    PlaceName(35.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(9.0, 0.0, -57.0, 0x0000, 0x0053, "")
    PlaceName(-23.5, 0.0, -45.0, 0x0000, 0x0053, "")
    PlaceName(-33.0, 0.0, 16.0, 0x0000, 0x0052, "")
    PlaceName(-15.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(6.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(-41.0, 0.0, 118.0, 0x0000, 0x0051, "")
    PlaceName(233.0, 0.0, 91.0, 0x0000, 0x0052, "")
    PlaceName(313.0, 0.0, -26.0, 0x0000, 0x0053, "")
    PlaceName(278.0, 0.0, -19.5, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_588",          # 00, 0
        "Function_1_640",          # 01, 1
        "Function_2_6A7",          # 02, 2
        "Function_3_6C3",          # 03, 3
        "Function_4_879",          # 04, 4
        "Function_5_8D7",          # 05, 5
        "Function_6_A0D",          # 06, 6
        "Function_7_B43",          # 07, 7
        "Function_8_C79",          # 08, 8
        "Function_9_D5D",          # 09, 9
        "Function_10_E1D",         # 0A, 10
        "Function_11_EF4",         # 0B, 11
        "Function_12_10F2",        # 0C, 12
        "Function_13_1AC1",        # 0D, 13
        "Function_14_1C68",        # 0E, 14
        "Function_15_1DA9",        # 0F, 15
        "Function_16_1F58",        # 10, 16
        "Function_17_20C1",        # 11, 17
        "Function_18_216D",        # 12, 18
        "Function_19_21BF",        # 13, 19
        "Function_20_21DE",        # 14, 20
        "Function_21_21F8",        # 15, 21
    ))


    def Function_0_588(): pass

    label("Function_0_588")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5C8"),
        (1, "loc_5D4"),
        (2, "loc_5E0"),
        (3, "loc_5EC"),
        (4, "loc_5F8"),
        (5, "loc_604"),
        (6, "loc_610"),
        (SWITCH_DEFAULT, "loc_61C"),
    )


    label("loc_5C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_604")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_610")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_61C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_628")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_63F")

    Return()

    # Function_0_588 end

    def Function_1_640(): pass

    label("Function_1_640")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A6")
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -240, 0, 15530, 1000, 0x0)
    Sleep(3600)
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -24330, 0, 1400, 1000, 0x0)
    Sleep(1200)
    Jump("Function_1_640")

    label("loc_6A6")

    Return()

    # Function_1_640 end

    def Function_2_6A7(): pass

    label("Function_2_6A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C2")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_2_6A7")

    label("loc_6C2")

    Return()

    # Function_2_6A7 end

    def Function_3_6C3(): pass

    label("Function_3_6C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_838")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A0")
    SetChrPos(0x0, 20160, 0, 650, 270)
    SetChrPos(0x1, 20160, 0, 650, 270)
    SetChrPos(0x2, 20160, 0, 650, 270)
    SetChrPos(0x3, 20160, 0, 650, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77C")
    SetChrPos(0x4, 20160, 0, 650, 270)
    SetChrPos(0x5, 20160, 0, 650, 270)
    Jump("loc_79B")

    label("loc_77C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79B")
    SetChrPos(0x4, 20160, 0, 650, 270)

    label("loc_79B")

    Jump("loc_838")

    label("loc_7A0")

    SetChrPos(0x0, -24900, 0, 220, 90)
    SetChrPos(0x1, -24900, 0, 220, 90)
    SetChrPos(0x2, -24900, 0, 220, 90)
    SetChrPos(0x3, -24900, 0, 220, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_819")
    SetChrPos(0x4, -24900, 0, 220, 90)
    SetChrPos(0x5, -24900, 0, 220, 90)
    Jump("loc_838")

    label("loc_819")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_838")
    SetChrPos(0x4, -24900, 0, 220, 90)

    label("loc_838")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_855")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 10)
    Jump("loc_878")

    label("loc_855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_869")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 11)
    Jump("loc_878")

    label("loc_869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_878")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 12)

    label("loc_878")

    Return()

    # Function_3_6C3 end

    def Function_4_879(): pass

    label("Function_4_879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88C")
    OP_70(0x4, 0x0)
    Jump("loc_890")

    label("loc_88C")

    OP_70(0x4, 0x1E)

    label("loc_890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A3")
    OP_70(0x5, 0x0)
    Jump("loc_8A7")

    label("loc_8A3")

    OP_70(0x5, 0x1E)

    label("loc_8A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BA")
    OP_70(0x6, 0x0)
    Jump("loc_8BE")

    label("loc_8BA")

    OP_70(0x6, 0x1E)

    label("loc_8BE")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D6")
    OP_1B(0x2, 0x0, 0x15)

    label("loc_8D6")

    Return()

    # Function_4_879 end

    def Function_5_8D7(): pass

    label("Function_5_8D7")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C4")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('大回复药', 1)"), scpexpr(EXPR_END)), "loc_956")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_9BF")

    label("loc_956")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_9BF")

    Jump("loc_A01")

    label("loc_9C4")

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

    label("loc_A01")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_8D7 end

    def Function_6_A0D(): pass

    label("Function_6_A0D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFA")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x397, 1)"), scpexpr(EXPR_END)), "loc_A8C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_AF5")

    label("loc_A8C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_AF5")

    Jump("loc_B37")

    label("loc_AFA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_B37")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_A0D end

    def Function_7_B43(): pass

    label("Function_7_B43")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C30")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ２', 1)"), scpexpr(EXPR_END)), "loc_BC2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_C2B")

    label("loc_BC2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C2B")

    Jump("loc_C6D")

    label("loc_C30")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_C6D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_B43 end

    def Function_8_C79(): pass

    label("Function_8_C79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CCF")

    #C0010
    ChrTalk(
        0x8,
        "什么嘛，不来吗？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "真遗憾，比修本来还打算\x01",
            "给客人带来快乐呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D59")

    label("loc_CCF")


    #C0012
    ChrTalk(
        0x8,
        "啊，来了个很帅气的人呢……！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "哎呀～太好了。\x01",
            "有客人来的话，\x01",
            "店里的女孩子们也会很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "快快，这边请。\x01",
            "呀哈哈哈哈……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D59")

    TalkEnd(0xFE)
    Return()

    # Function_8_C79 end

    def Function_9_D5D(): pass

    label("Function_9_D5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DB9")

    #C0015
    ChrTalk(
        0x9,
        "我今天干劲十足呢。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "呵呵，哪怕有一点闲暇时间，\x01",
            "都必须去揽客呢～¤\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E19")

    label("loc_DB9")


    #C0017
    ChrTalk(
        0x9,
        "呵呵，我是爱丽斯～☆\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "啊，这位小哥～\x01",
            "不和我一起玩玩吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        "我今天还有点时间哦～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_E19")

    TalkEnd(0xFE)
    Return()

    # Function_9_D5D end

    def Function_10_E1D(): pass

    label("Function_10_E1D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    OP_68(0, 1950, 42500, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, -2000, 0, 42000, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    SetChrPos(0x14, 2000, 0, 42000, 180)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    OP_68(0, 1950, 45500, 8000)
    MoveCamera(0, 13, 0, 8000)
    SetCameraDistance(21000, 8000)
    FadeToBright(2000, 0)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0597", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_E1D end

    def Function_11_EF4(): pass

    label("Function_11_EF4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch26800.itc", 0x1E)
    SetChrPos(0x101, -3800, 0, 6400, 0)
    SetChrPos(0x102, -3800, 0, 6400, 0)
    SetChrPos(0x103, -3800, 0, 6400, 0)
    SetChrPos(0x104, -3800, 0, 6400, 0)
    OP_68(-10000, 2450, 800, 0)
    MoveCamera(325, 15, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(12500, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x15, 0x0)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 15000, 0, 2000, 270)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x1)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, -15000, 0, 500, 90)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x17, -15400, 0, -500, 90)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)

    def lambda_1009():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1009)
    Sleep(50)

    def lambda_1026():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1026)
    Sleep(50)

    def lambda_1043():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1043)
    OP_68(6000, 2450, 800, 9000)
    SetCameraDistance(14500, 9000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Fade(2000)
    OP_68(0, 1950, 42500, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    OP_68(0, 1950, 45500, 7000)
    MoveCamera(0, 13, 0, 7000)
    SetCameraDistance(21000, 7000)
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0597", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_EF4 end

    def Function_12_10F2(): pass

    label("Function_12_10F2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50506.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("chr/ch02751.itc", 0x21)
    LoadChrToIndex("chr/ch02752.itc", 0x22)
    LoadChrToIndex("chr/ch31252.itc", 0x23)
    LoadChrToIndex("chr/ch31251.itc", 0x24)
    LoadChrToIndex("chr/ch31350.itc", 0x25)
    LoadChrToIndex("chr/ch31351.itc", 0x26)
    LoadChrToIndex("chr/ch09000.itc", 0x29)
    LoadChrToIndex("chr/ch00150.itc", 0x2A)
    LoadChrToIndex("chr/ch00151.itc", 0x2B)
    LoadChrToIndex("chr/ch00250.itc", 0x2C)
    LoadChrToIndex("chr/ch00251.itc", 0x2D)
    LoadChrToIndex("chr/ch00950.itc", 0x2E)
    LoadChrToIndex("chr/ch00951.itc", 0x2F)
    LoadChrToIndex("chr/ch00952.itc", 0x30)
    LoadChrToIndex("apl/ch50509.itc", 0x31)
    LoadChrToIndex("chr/ch00152.itc", 0x32)
    LoadChrToIndex("chr/ch31353.itc", 0x33)
    LoadChrToIndex("chr/ch31352.itc", 0x34)
    LoadChrToIndex("apl/ch50515.itc", 0x35)
    LoadEffect(0x0, "event\\ev606_00.eff")
    LoadEffect(0x1, "battle\\btgun00.eff")
    LoadEffect(0x2, "event\\eva03_00.eff")
    LoadEffect(0x3, "battle\\ms00001.eff")
    OP_68(8500, 900, 700, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    SetChrPos(0x101, 30000, 0, 700, 270)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 33800, 0, 1300, 270)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 32600, 0, 400, 270)
    SetChrPos(0x104, 31600, 0, 1700, 270)
    SetChrChipByIndex(0x10A, 0x2E)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x10A, 38700, 0, 1700, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 39500, 0, 300, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 35400, 0, 300, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x10, 0x26)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x26)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0xD, 33000, 0, 700, 270)
    SetChrPos(0xE, 34100, 0, 1800, 270)
    SetChrPos(0xF, 34200, 0, -200, 270)
    SetChrPos(0x10, 30000, 0, 700, 270)
    SetChrPos(0x11, 31100, 0, 1800, 270)
    SetChrPos(0x12, 31200, 0, -200, 270)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 2300, 0, 2200, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 2600, 0, -1100, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0xC, 0x29)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xC, 5600, 800, 6400, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)

    def lambda_141A():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_141A)
    Sleep(50)

    def lambda_1437():
        OP_96(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1437)
    Sleep(50)

    def lambda_1454():
        OP_96(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1454)
    Sleep(50)

    def lambda_1471():
        OP_96(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1471)
    Sleep(50)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 3, 0, 2)

    def lambda_14B2():
        OP_96(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14B2)
    Sleep(50)

    def lambda_14CF():
        OP_96(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_14CF)
    Sleep(50)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)

    def lambda_14F4():
        OP_96(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14F4)

    def lambda_150E():

        label("loc_150E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_150E")

    QueueWorkItem2(0x8, 2, lambda_150E)

    def lambda_1520():

        label("loc_1520")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1520")

    QueueWorkItem2(0x9, 2, lambda_1520)
    OP_68(2500, 900, 700, 6000)
    MoveCamera(47, 17, -5, 6000)
    SetCameraDistance(14500, 6000)
    FadeToBright(2000, 0)
    BeginChrThread(0x18, 1, 0, 20)
    OP_6F(0x79)
    BeginChrThread(0xC, 3, 0, 18)
    Sleep(1000)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0x18, 0x1)

    #C0020
    ChrTalk(
        0x8,
        "#11P怎么了，是在举行某种庆祝活动吗！？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        "#11P好奇怪的队伍～\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 3)

    #C0022
    ChrTalk(
        0xC,
        (
            "#5P这骚乱是怎么回事啊？\x01",
            "简直吵死人了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_160C():

        label("loc_160C")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_160C")

    QueueWorkItem2(0xC, 2, lambda_160C)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)

    def lambda_165A():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_165A)
    Sleep(50)

    def lambda_1677():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1677)
    Sleep(50)

    def lambda_1694():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1694)
    Sleep(50)

    def lambda_16B1():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_16B1)
    Sleep(50)

    def lambda_16CE():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_16CE)
    Sleep(50)

    def lambda_16EB():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_16EB)
    Sleep(750)

    def lambda_1708():

        label("loc_1708")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_1708")

    QueueWorkItem2(0x8, 2, lambda_1708)
    Sleep(50)

    def lambda_171D():

        label("loc_171D")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_171D")

    QueueWorkItem2(0x9, 2, lambda_171D)
    Sleep(2500)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1768():
        OP_98(0xFE, 0xFFFFFDA8, 0x0, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1768)
    Sleep(50)

    def lambda_1785():
        OP_98(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1785)
    Sleep(150)
    EndChrThread(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x29)
    SetChrSubChip(0xC, 0x0)
    Sound(819, 0, 100, 0)
    Sound(926, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    def lambda_17D5():
        OP_98(0xFE, 0x0, 0x0, 0x258, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_17D5)
    BeginChrThread(0xC, 3, 0, 19)

    #C0023
    ChrTalk(
        0xC,
        "#5P#14A哎……！\x02",
    )
    #Auto

    Sleep(2000)

    #C0024
    ChrTalk(
        0x8,
        "#11P#18A这、这到底是怎么回事！？\x02",
    )
    #Auto

    Sleep(2000)
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0xB, 0x8)
    WaitChrThread(0x10A, 1)
    WaitChrThread(0xA, 1)
    OP_64(0xC)
    OP_64(0x9)
    OP_64(0x8)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Fade(500)
    OP_68(-13500, 900, 700, 0)
    MoveCamera(50, 33, -5, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    OP_EE(0x0, 0x1)
    SetChrChipByIndex(0x10A, 0x30)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x10A, -22000, 0, 1400, 90)
    SetChrChipByIndex(0xA, 0x31)
    SetChrSubChip(0xA, 0x4)
    SetChrPos(0xA, -22300, 0, -200, 90)
    SetChrPos(0xD, 5000, 0, 700, 270)
    SetChrPos(0xE, 6100, 0, 1800, 270)
    SetChrPos(0xF, 6200, 0, -200, 270)
    SetChrPos(0x10, 0, 0, 700, 270)
    SetChrPos(0x11, 1100, 0, 1800, 270)
    SetChrPos(0x12, 1200, 0, -200, 270)

    def lambda_1966():
        OP_98(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1966)
    BeginChrThread(0x10, 3, 0, 17)
    Sleep(50)

    def lambda_1989():
        OP_98(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1989)
    BeginChrThread(0x11, 3, 0, 17)
    Sleep(50)

    def lambda_19AC():
        OP_98(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_19AC)
    BeginChrThread(0x12, 3, 0, 17)
    Sleep(50)

    def lambda_19CF():
        OP_98(0xFE, 0xFFFFB5C8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_19CF)
    BeginChrThread(0xD, 3, 0, 16)
    Sleep(50)

    def lambda_19F2():
        OP_98(0xFE, 0xFFFFB5C8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_19F2)
    BeginChrThread(0xE, 3, 0, 16)
    Sleep(50)

    def lambda_1A15():
        OP_98(0xFE, 0xFFFFB5C8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1A15)
    BeginChrThread(0xF, 3, 0, 16)
    OP_0D()
    Sleep(900)
    OP_68(-18500, 900, 700, 1500)
    MoveCamera(40, 23, -5, 1500)
    SetCameraDistance(14500, 1500)
    OP_6F(0x79)
    StopEffect(0x0, 0x2)
    BeginChrThread(0xA, 3, 0, 15)
    Sleep(50)
    BeginChrThread(0x10A, 3, 0, 14)
    Sleep(500)
    BeginChrThread(0xC, 3, 0, 13)
    Sleep(3500)
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_EE(0x0, 0xA)
    EndChrThread(0x10A, 0x3)
    EndChrThread(0xA, 0x3)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0xB, 0x8)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_10F2 end

    def Function_13_1AC1(): pass

    label("Function_13_1AC1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C67")
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -18900, 0, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -18000, 0, -1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -19100, 0, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -20000, 0, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -19400, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -18200, 0, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -17700, 0, -600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_13_1AC1")

    label("loc_1C67")

    Return()

    # Function_13_1AC1 end

    def Function_14_1C68(): pass

    label("Function_14_1C68")

    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    label("loc_1CB6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DA8")
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    Jump("loc_1CB6")

    label("loc_1DA8")

    Return()

    # Function_14_1C68 end

    def Function_15_1DA9(): pass

    label("Function_15_1DA9")

    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)

    label("loc_1DF7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F57")
    SetChrSubChip(0xA, 0x5)
    Sleep(150)
    SetChrSubChip(0xA, 0x6)
    Sleep(100)
    SetChrSubChip(0xA, 0x7)
    Sound(531, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0xA, 0x4)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(70)
    SetChrSubChip(0xA, 0x2)
    Sleep(70)
    SetChrSubChip(0xA, 0x1)
    Sleep(70)
    SetChrSubChip(0xA, 0x0)
    Sleep(70)
    SetChrSubChip(0xA, 0x1)
    Sleep(70)
    SetChrSubChip(0xA, 0x2)
    Sleep(70)
    SetChrSubChip(0xA, 0x3)
    Sleep(70)
    SetChrSubChip(0xA, 0x4)
    Sleep(600)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0xA, 0x5)
    Sleep(150)
    SetChrSubChip(0xA, 0x6)
    Sleep(100)
    SetChrSubChip(0xA, 0x7)
    Sound(531, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0xA, 0x4)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(70)
    SetChrSubChip(0xA, 0x2)
    Sleep(70)
    SetChrSubChip(0xA, 0x1)
    Sleep(70)
    SetChrSubChip(0xA, 0x0)
    Sleep(70)
    SetChrSubChip(0xA, 0x1)
    Sleep(70)
    SetChrSubChip(0xA, 0x2)
    Sleep(70)
    SetChrSubChip(0xA, 0x3)
    Sleep(70)
    SetChrSubChip(0xA, 0x4)
    Sleep(600)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    Jump("loc_1DF7")

    label("loc_1F57")

    Return()

    # Function_15_1DA9 end

    def Function_16_1F58(): pass

    label("Function_16_1F58")

    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    label("loc_1F64")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20C0")

    def lambda_1F74():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F74)
    SetChrSubChip(0xFE, 0x3)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(356, 0, 100, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(700)
    Jump("loc_1F64")

    label("loc_20C0")

    Return()

    # Function_16_1F58 end

    def Function_17_20C1(): pass

    label("Function_17_20C1")

    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2114():
        OP_9C(0xFE, 0x5DC, 0x0, 0x0, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2114)

    def lambda_2131():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2131)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_17_20C1 end

    def Function_18_216D(): pass

    label("Function_18_216D")

    ClearMapObjFlags(0x0, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)

    def lambda_218D():
        OP_96(0xFE, 0x15E0, 0x0, 0x834, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_218D)

    def lambda_21A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_21A7)
    WaitChrThread(0xC, 1)
    OP_93(0xC, 0xE1, 0x1F4)
    Return()

    # Function_18_216D end

    def Function_19_21BF(): pass

    label("Function_19_21BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21DD")
    OP_A1(0xFE, 0xFA0, 0x8, 0x5, 0x6, 0x7, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_19_21BF")

    label("loc_21DD")

    Return()

    # Function_19_21BF end

    def Function_20_21DE(): pass

    label("Function_20_21DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21F7")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_20_21DE")

    label("loc_21F7")

    Return()

    # Function_20_21DE end

    def Function_21_21F8(): pass

    label("Function_21_21F8")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F8")

    #C0025
    ChrTalk(
        0x104,
        (
            "#0301F鲁巴彻商会……\x01",
            "那件事发生之后，似乎仍然在正常运营啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#0101F虽然因为小琪雅的那件事，\x01",
            "暂时安分了一段时间……\x02\x03",

            "但自从达成和解之后，\x01",
            "他们似乎又重新开始『营业』了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#0003F之前发生了很多事情啊……\x01",
            "还是别去刺激他们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xC9, 2)
    Jump("loc_2351")

    label("loc_22F8")


    #C0028
    ChrTalk(
        0x101,
        (
            "#0001F（这前面就是鲁巴彻商会了。）\x02\x03",

            "（最好不要贸然刺激他们，\x01",
            "  还是别随便靠近了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2351")

    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Return()

    # Function_21_21F8 end

    SaveToFile()

Try(main)
