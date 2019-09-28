from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c050c.bin",                # FileName
        "c050c",                    # MapName
        "c050c",                    # Location
        0x0026,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 38, 0, 2, 0, 3],
    )

    BuildStringList((
        "c050c",                  # 0
        "黑手党",                 # 1
        "黑手党",                 # 2
        "揽客员比修",             # 3
        "爱丽斯",                 # 4
        "游客",                   # 5
        "游客",                   # 6
        "游客",                   # 7
        "游客",                   # 8
        "游客",                   # 9
        "游客",                   # 10
        "中央广场",               # 11
        "西街",                   # 12
        "行政区",                 # 13
        "住宅街",                 # 14
        "欢乐街",                 # 15
        "东街",                   # 16
        "旧城区",                 # 17
        "港湾区",                 # 18
        "ＩＢＣ",                 # 19
        "站前街道",               # 20
        "后巷",                   # 21
        "乌尔斯拉间道",           # 22
        "东克洛斯贝尔街道",       # 23
        "西克洛斯贝尔街道",       # 24
        "玛因兹山道",             # 25
    ))

    AddCharChip((
        "chr/ch20200.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch23500.itc",                   # 02
        "chr/ch23600.itc",                   # 03
        "chr/ch24200.itc",                   # 04
        "chr/ch24400.itc",                   # 05
        "chr/ch26700.itc",                   # 06
        "chr/ch26900.itc",                   # 07
        "chr/ch31000.itc",                   # 08
        "chr/ch31100.itc",                   # 09
    ))

    DeclNpc(-2000,   0,       41700,   180,  261,  0x0, 0,   8,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(2000,    0,       41700,   180,  261,  0x0, 0,   9,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-16590,  0,       2980,    90,   277,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-6170,   0,       1399,    90,   261,  0x0, 0,   7,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(-14979,  0,       2980,    270,  405,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-14979,  0,       2980,    270,  405,  0x0, 0,   1,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-14100,  0,       2549,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-14979,  0,       2980,    270,  405,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-14979,  0,       2980,    270,  405,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-14100,  0,       2549,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   20,  255,  0)

    DeclEvent(0x0000, 0, 24,  -0.10000000149011612,  43.849998474121094,    -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.05000000074505806,   -21.924999237060547,   0.10000000149011612,   1.0])

    DeclActor(-3210,   5800,    22030,   1200,    -3210,   6800,    22030,   0x007C, 0,  4,  0x0000)
    DeclActor(-10590,  5900,    9660,    1200,    -10590,  6900,    9660,    0x007C, 0,  5,  0x0000)
    DeclActor(11410,   0,       7030,    1200,    11410,   1000,    7030,    0x007C, 0,  6,  0x0000)

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
        "Function_0_54C",          # 00, 0
        "Function_1_604",          # 01, 1
        "Function_2_66B",          # 02, 2
        "Function_3_8A4",          # 03, 3
        "Function_4_9B0",          # 04, 4
        "Function_5_AE6",          # 05, 5
        "Function_6_C1C",          # 06, 6
        "Function_7_D52",          # 07, 7
        "Function_8_F7A",          # 08, 8
        "Function_9_11A6",         # 09, 9
        "Function_10_1582",        # 0A, 10
        "Function_11_1622",        # 0B, 11
        "Function_12_16D2",        # 0C, 12
        "Function_13_176C",        # 0D, 13
        "Function_14_1822",        # 0E, 14
        "Function_15_1E74",        # 0F, 15
        "Function_16_1EB7",        # 10, 16
        "Function_17_1F1D",        # 11, 17
        "Function_18_1F43",        # 12, 18
        "Function_19_1F9D",        # 13, 19
        "Function_20_1FF7",        # 14, 20
        "Function_21_203C",        # 15, 21
        "Function_22_20C2",        # 16, 22
        "Function_23_23A8",        # 17, 23
        "Function_24_3134",        # 18, 24
        "Function_25_31C8",        # 19, 25
    ))


    def Function_0_54C(): pass

    label("Function_0_54C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_58C"),
        (1, "loc_598"),
        (2, "loc_5A4"),
        (3, "loc_5B0"),
        (4, "loc_5BC"),
        (5, "loc_5C8"),
        (6, "loc_5D4"),
        (SWITCH_DEFAULT, "loc_5E0"),
    )


    label("loc_58C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_598")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_603")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_603")

    Return()

    # Function_0_54C end

    def Function_1_604(): pass

    label("Function_1_604")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66A")
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -240, 0, 15530, 1000, 0x0)
    Sleep(3600)
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -24330, 0, 1400, 1000, 0x0)
    Sleep(1200)
    Jump("Function_1_604")

    label("loc_66A")

    Return()

    # Function_1_604 end

    def Function_2_66B(): pass

    label("Function_2_66B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FB")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_75A")
    SetChrPos(0x0, 20160, 0, 650, 270)
    SetChrPos(0x1, 20160, 0, 650, 270)
    SetChrPos(0x2, 20160, 0, 650, 270)
    SetChrPos(0x3, 20160, 0, 650, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72D")
    SetChrPos(0x4, 20160, 0, 650, 270)
    SetChrPos(0x5, 20160, 0, 650, 270)
    Jump("loc_74C")

    label("loc_72D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74C")
    SetChrPos(0x4, 20160, 0, 650, 270)

    label("loc_74C")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7FB")

    label("loc_75A")

    SetChrPos(0x0, -24900, 0, 220, 90)
    SetChrPos(0x1, -24900, 0, 220, 90)
    SetChrPos(0x2, -24900, 0, 220, 90)
    SetChrPos(0x3, -24900, 0, 220, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D3")
    SetChrPos(0x4, -24900, 0, 220, 90)
    SetChrPos(0x5, -24900, 0, 220, 90)
    Jump("loc_7F2")

    label("loc_7D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F2")
    SetChrPos(0x4, -24900, 0, 220, 90)

    label("loc_7F2")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7FB")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81A")
    SetMapFlags(0x10000000)
    Event(0, 22)

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_841")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83C")
    SetChrFlags(0x9, 0x10)

    label("loc_83C")

    Jump("loc_88B")

    label("loc_841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_85B")
    OP_93(0xA, 0xB4, 0x0)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_88B")

    label("loc_85B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_86E")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_88B")

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_886")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_88B")

    label("loc_886")

    ClearChrFlags(0xC, 0x80)

    label("loc_88B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A3")
    OP_C7(0x1, 0x1000)

    label("loc_8A3")

    Return()

    # Function_2_66B end

    def Function_3_8A4(): pass

    label("Function_3_8A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B7")
    OP_70(0x4, 0x0)
    Jump("loc_8BB")

    label("loc_8B7")

    OP_70(0x4, 0x1E)

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CE")
    OP_70(0x5, 0x0)
    Jump("loc_8D2")

    label("loc_8CE")

    OP_70(0x5, 0x1E)

    label("loc_8D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E5")
    OP_70(0x6, 0x0)
    Jump("loc_8E9")

    label("loc_8E5")

    OP_70(0x6, 0x1E)

    label("loc_8E9")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_901")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_901")

    OP_1B(0x1, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_919")
    OP_1B(0x1, 0x0, 0x19)

    label("loc_919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92C")
    OP_1B(0x1, 0x0, 0x17)

    label("loc_92C")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 13000, -4000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -13000, -4000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_3_8A4 end

    def Function_4_9B0(): pass

    label("Function_4_9B0")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9D")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('大回复药', 1)"), scpexpr(EXPR_END)), "loc_A2F")
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
    Jump("loc_A98")

    label("loc_A2F")

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

    label("loc_A98")

    Jump("loc_ADA")

    label("loc_A9D")

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

    label("loc_ADA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_9B0 end

    def Function_5_AE6(): pass

    label("Function_5_AE6")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD3")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x397, 1)"), scpexpr(EXPR_END)), "loc_B65")
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
    Jump("loc_BCE")

    label("loc_B65")

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

    label("loc_BCE")

    Jump("loc_C10")

    label("loc_BD3")

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

    label("loc_C10")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_AE6 end

    def Function_6_C1C(): pass

    label("Function_6_C1C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D09")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ２', 1)"), scpexpr(EXPR_END)), "loc_C9B")
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
    Jump("loc_D04")

    label("loc_C9B")

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

    label("loc_D04")

    Jump("loc_D46")

    label("loc_D09")

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

    label("loc_D46")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_C1C end

    def Function_7_D52(): pass

    label("Function_7_D52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DCC")

    #C0010
    ChrTalk(
        0x8,
        (
            "今天有很重要的活动啊，\x01",
            "可不能触了霉头。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "再在这里转来转去的，\x01",
            "小心我把你打到水沟里去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1C")

    label("loc_DCC")


    #C0012
    ChrTalk(
        0x8,
        "啊？干什么啊，小鬼。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "再在这里转来转去的，\x01",
            "小心我把你打到水沟里去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E1C")

    Jump("loc_F76")

    label("loc_E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_F0E")

    #C0014
    ChrTalk(
        0x8,
        "呵呵，庆典这么华丽热闹，真好啊。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "要是没有偶尔迷路\x01",
            "闯进来的白痴游客，\x01",
            "放哨也就能轻松很多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0006F（再怎么说，应该也不会\x01",
            "  来这里吧……\x01",
            "  ……还好，似乎没有来。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_F09")

    #C0017
    ChrTalk(
        0x160,
        "#3308F（…………………………）\x02",
    )

    CloseMessageWindow()

    label("loc_F09")

    Jump("loc_F76")

    label("loc_F0E")


    #C0018
    ChrTalk(
        0x8,
        "哼哼，庆典这么华丽热闹，真好啊。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "要是没有偶尔迷路\x01",
            "闯进来的白痴游客，\x01",
            "放哨工作就能轻松很多了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F76")

    TalkEnd(0xFE)
    Return()

    # Function_7_D52 end

    def Function_8_F7A(): pass

    label("Function_8_F7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_105D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FD5")

    #C0020
    ChrTalk(
        0x9,
        "警察既无能，又像苍蝇一样烦人。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "快滚吧！\x01",
            "我们也很忙的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1058")

    label("loc_FD5")


    #C0022
    ChrTalk(
        0x9,
        "嘁，偏偏要在今天留守。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        "真倒霉啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x0, 750)
    Sleep(750)

    #C0024
    ChrTalk(
        0x9,
        "……你是………\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "快滚吧！\x01",
            "我们也很忙的。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)

    label("loc_1058")

    Jump("loc_11A2")

    label("loc_105D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1132")

    #C0026
    ChrTalk(
        0x9,
        (
            "喂喂，干什么啊？\x01",
            "没事的话就快滚吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "副头目也没空\x01",
            "招呼你们这些小鬼。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0006F（再怎么说，应该也\x01",
            "  不会来这里吧……\x01",
            "  ……还好，似乎没有来。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_112D")

    #C0029
    ChrTalk(
        0x160,
        "#3308F（…………………………）\x02",
    )

    CloseMessageWindow()

    label("loc_112D")

    Jump("loc_11A2")

    label("loc_1132")


    #C0030
    ChrTalk(
        0x9,
        (
            "……又是你们啊。\x01",
            "真是不吸取教训，怎么又来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        "没事的话就快滚吧。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "副头目也没空\x01",
            "招呼你们这些小鬼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A2")

    TalkEnd(0xFE)
    Return()

    # Function_8_F7A end

    def Function_9_11A6(): pass

    label("Function_9_11A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_11BA")
    Call(0, 10)
    Jump("loc_157E")

    label("loc_11BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_END)), "loc_1253")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1204")

    #C0033
    ChrTalk(
        0xA,
        (
            "好，今天也要\x01",
            "努力招揽客人～！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xA,
        "哦哈哈哈！\x02",
    )

    CloseMessageWindow()
    Jump("loc_124E")

    label("loc_1204")


    #C0035
    ChrTalk(
        0xA,
        (
            "呼……工作之后\x01",
            "抽一支烟，感觉真是太棒了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        "人生真充实啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_124E")

    Jump("loc_157E")

    label("loc_1253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_13B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 4)), scpexpr(EXPR_END)), "loc_12DB")

    #C0037
    ChrTalk(
        0xA,
        (
            "呼，游行那么吵吵嚷嚷的，\x01",
            "说不定会有\x01",
            "一两个小鬼经过吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "比修我可不知道啊，\x01",
            "这种赚不来钱的事才不关心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B4")

    label("loc_12DB")


    #C0039
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0041
    ChrTalk(
        0xA,
        "哦哈哈哈……！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xA,
        (
            "…………不知道呢，\x01",
            "没见过。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#0008F是吗……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 21)

    label("loc_13B4")

    Jump("loc_157E")

    label("loc_13B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1456")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1407")

    #C0044
    ChrTalk(
        0xA,
        (
            "好，今天也要\x01",
            "努力招揽客人～！\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xA,
        "哦哈哈哈……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1451")

    label("loc_1407")


    #C0046
    ChrTalk(
        0xA,
        (
            "呼……工作之后\x01",
            "抽一支烟，感觉真是太棒了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xA,
        "人生真充实啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1451")

    Jump("loc_157E")

    label("loc_1456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_14CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_14C6")
    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0048
    ChrTalk(
        0xA,
        (
            "既然来到了克洛斯贝尔，\x01",
            "就要玩个痛快才行呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xA,
        "来来，我来带路吧。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Jump("loc_14C9")

    label("loc_14C6")

    Call(0, 11)

    label("loc_14C9")

    Jump("loc_157E")

    label("loc_14CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1528")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1520")
    OP_4B(0xA, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0050
    ChrTalk(
        0xA,
        (
            "不要客气哦～\x01",
            "热烈欢迎两位哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_1523")

    label("loc_1520")

    Call(0, 12)

    label("loc_1523")

    Jump("loc_157E")

    label("loc_1528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_157B")
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0051
    ChrTalk(
        0xA,
        (
            "来来，大叔走这边。\x01",
            "一定会是很有趣的旅行见闻哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Jump("loc_157E")

    label("loc_157B")

    Call(0, 13)

    label("loc_157E")

    TalkEnd(0xFE)
    Return()

    # Function_9_11A6 end

    def Function_10_1582(): pass

    label("Function_10_1582")

    OP_4B(0xA, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0052
    ChrTalk(
        0xA,
        (
            "讨厌啦～我可不是为了这个\x01",
            "才跟你搭话的啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xA,
        (
            "小哥你一定能当大明星的，\x01",
            "我的眼光可是不会错的哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x10,
        "我、我可没有那种想法哦！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_10_1582 end

    def Function_11_1622(): pass

    label("Function_11_1622")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0055
    ChrTalk(
        0xA,
        (
            "如何如何，小哥。\x01",
            "最近都没怎么出来玩吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        (
            "这可不行啊～既然来到了克洛斯贝尔，\x01",
            "就要玩个痛快才行呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xA,
        "这可是礼节嘛～！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xF,
        "是、是这样的吗……！？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_11_1622 end

    def Function_12_16D2(): pass

    label("Function_12_16D2")

    OP_4B(0xA, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0059
    ChrTalk(
        0xA,
        (
            "热烈欢迎，热烈欢迎。\x01",
            "我保证让你们两位\x01",
            "都玩得尽兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        (
            "只要交给我\x01",
            "比修，就一切搞定啦～\x01",
            "哈哈哈！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xD,
        "不、不了，我们……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_12_16D2 end

    def Function_13_176C(): pass

    label("Function_13_176C")

    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0062
    ChrTalk(
        0xA,
        (
            "呜哇～大叔，你来我们店里的话，\x01",
            "一定会大受欢迎的啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        (
            "来来，进来看看吧。\x01",
            "一定会是很有趣的旅行见闻哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        "哈哈，是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xC,
        "可是，我还有家人在……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_176C end

    def Function_14_1822(): pass

    label("Function_14_1822")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_18F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1880")

    #C0066
    ChrTalk(
        0xB,
        "纪念庆典在今天就要结束了呢～\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xB,
        "要加把劲，最后大赚一笔才行。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18EE")

    label("loc_1880")


    #C0068
    ChrTalk(
        0xB,
        "创立纪念庆典万岁～！\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        (
            "……我是听客人说的，\x01",
            "今天好像是自治州诞生的日子。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        "我可是完全不知道呢～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_18EE")

    Jump("loc_1E70")

    label("loc_18F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_END)), "loc_1986")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1937")

    #C0071
    ChrTalk(
        0xB,
        (
            "哟……\x01",
            "糟糕糟糕。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xB,
        "要认真工作才是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1981")

    label("loc_1937")

    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0073
    ChrTalk(
        0xB,
        "游行好棒哦！\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "我也跟着\x01",
            "一起挥手了～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1981")

    Jump("loc_1E70")

    label("loc_1986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1BA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_19FE")

    #C0075
    ChrTalk(
        0xB,
        (
            "我也去看\x01",
            "游行了～\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xB,
        (
            "嗯，有个小孩子还追着\x01",
            "游行的车子一起跑～\x01",
            "因为很可爱，所以我有点印象。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA0")

    label("loc_19FE")


    #C0077
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0079
    ChrTalk(
        0xFE,
        "嗯，呃……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "……这么一说的话，\x01",
            "好像是见过两三个小孩子～\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0000F真的吗……？\x02\x03",

            "其中有没有这张照片上的孩子呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "嗯～很难说啊～……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "我这个人，\x01",
            "脑子可是很差的～\x01",
            "不管是什么事情，都会马上忘掉啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "印象很模糊了，\x01",
            "已经想不起来啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#0006F是、是吗……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 21)

    label("loc_1BA0")

    Jump("loc_1E70")

    label("loc_1BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1C38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1BE9")

    #C0086
    ChrTalk(
        0xB,
        (
            "哟……\x01",
            "糟糕糟糕。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xB,
        "要认真工作才是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C33")

    label("loc_1BE9")

    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0088
    ChrTalk(
        0xB,
        "游行好棒哦！\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        (
            "我也跟着\x01",
            "一起挥手了～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1C33")

    Jump("loc_1E70")

    label("loc_1C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1D18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C9E")

    #C0090
    ChrTalk(
        0xB,
        "呵呵，欢迎光临⊥\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xB,
        "小哥，去玩吧☆\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xB,
        (
            "呜哇……感觉\x01",
            "好像已经很累了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D13")

    label("loc_1C9E")


    #C0093
    ChrTalk(
        0xB,
        "呵呵，欢迎光临⊥\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xB,
        "小哥，去玩吧☆\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xB,
        (
            "……怎样？\x01",
            "稍微改变了点形象。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xB,
        (
            "游客似乎\x01",
            "都比较喜欢这种风格呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1D13")

    Jump("loc_1E70")

    label("loc_1D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1DCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1D5C")

    #C0097
    ChrTalk(
        0xB,
        (
            "真不愧是大型庆典啊。\x01",
            "要趁机大捞一笔～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC9")

    label("loc_1D5C")


    #C0098
    ChrTalk(
        0xB,
        (
            "呵呵，昨天的\x01",
            "营业额比我的对手\x01",
            "多那么一点点呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0099
    ChrTalk(
        0xB,
        "不愧是纪念庆典，真棒～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1DC9")

    Jump("loc_1E70")

    label("loc_1DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1E20")

    #C0100
    ChrTalk(
        0xB,
        (
            "我和对手\x01",
            "在竞争营业额呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xB,
        (
            "必须要趁庆典期间\x01",
            "跟她拉开差距。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E70")

    label("loc_1E20")


    #C0102
    ChrTalk(
        0xB,
        "哇～纪念庆典万岁！\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        "好多客人哦！\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xB,
        (
            "今天也要努力\x01",
            "提高营业额哦～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1E70")

    TalkEnd(0xFE)
    Return()

    # Function_14_1822 end

    def Function_15_1E74(): pass

    label("Function_15_1E74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1EB0")
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0105
    ChrTalk(
        0xC,
        (
            "可是，\x01",
            "我还有家人……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Jump("loc_1EB3")

    label("loc_1EB0")

    Call(0, 13)

    label("loc_1EB3")

    TalkEnd(0xFE)
    Return()

    # Function_15_1E74 end

    def Function_16_1EB7(): pass

    label("Function_16_1EB7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1F16")
    OP_4B(0xA, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0106
    ChrTalk(
        0xD,
        "不、不了，我们……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xD,
        "接下来还要去其它地方……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_1F19")

    label("loc_1F16")

    Call(0, 12)

    label("loc_1F19")

    TalkEnd(0xFE)
    Return()

    # Function_16_1EB7 end

    def Function_17_1F1D(): pass

    label("Function_17_1F1D")

    TalkBegin(0xFE)

    #C0108
    ChrTalk(
        0xE,
        (
            "哇～被奇怪的人\x01",
            "缠住了啦！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1F1D end

    def Function_18_1F43(): pass

    label("Function_18_1F43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1F96")
    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0109
    ChrTalk(
        0xF,
        "我只是来看游行的……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xF,
        "是、是这样吗……？\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Jump("loc_1F99")

    label("loc_1F96")

    Call(0, 11)

    label("loc_1F99")

    TalkEnd(0xFE)
    Return()

    # Function_18_1F43 end

    def Function_19_1F9D(): pass

    label("Function_19_1F9D")

    TalkBegin(0xFE)
    OP_4B(0xA, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0111
    ChrTalk(
        0x10,
        "在、在我太太面前说什么呢。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x10,
        (
            "不像话！\x01",
            "真是不像话！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_19_1F9D end

    def Function_20_1FF7(): pass

    label("Function_20_1FF7")

    TalkBegin(0xFE)

    #C0113
    ChrTalk(
        0x11,
        (
            "以前就听说过克洛斯贝尔的后巷\x01",
            "很可怕……\x01",
            "好像是真的呢……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_1FF7 end

    def Function_21_203C(): pass

    label("Function_21_203C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C1")
    OP_29(0x46, 0x1, 0x4)

    #C0114
    ChrTalk(
        0x101,
        (
            "#0003F（好，后巷的探听\x01",
            "  到这里就足够了吧。）\x02\x03",

            "#0001F（接下来就去中央广场\x01",
            "  探听一下吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 4)
    OP_1B(0x1, 0x0, 0x17)

    label("loc_20C1")

    Return()

    # Function_21_203C end

    def Function_22_20C2(): pass

    label("Function_22_20C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-23300, 2300, 1000, 0)
    MoveCamera(330, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -28300, 0, 1000, 90)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(-23300, 1300, 1000, 2500)

    def lambda_2166():
        OP_96(0xFE, 0xFFFFA4FC, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2166)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(1084, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0115
    AnonymousTalk(
        0x101,
        "#0001F我是罗伊德。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1364, 255, 100, 0)    #voice#Randy
    Sleep(500)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("兰迪的声音")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我是兰迪，\x01",
            "东街基本调查了一圈。\x02\x03",

            "也问过协会的接待员了，\x01",
            "似乎没什么有价值的线索啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0117
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0008F明白了，\x01",
            "我在欢乐街也没找到。\x02\x03",

            "#0001F继续进行搜索吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("兰迪的声音")

    #A0118
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是，队长。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    Sleep(300)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -23900, 0, 1000, 90)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA2, 0)
    OP_29(0x46, 0x1, 0x3)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_22_20C2 end

    def Function_23_23A8(): pass

    label("Function_23_23A8")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    AddParty(0x5F, 0xFF, 0xFF)
    OP_68(18000, 1100, 1000, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 15000, 0, 1000, 90)
    SetChrPos(0x160, 8000, 0, 1000, 90)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis056.itp")

    def lambda_2465():
        OP_96(0xFE, 0x4650, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2465)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    #N0119
    NpcTalk(
        0x160,
        "少女的声音",
        (
            "#2P呵呵……\x01",
            "大哥哥，好久不见了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x101,
        "#0005F#5P哎……\x02",
    )

    CloseMessageWindow()

    def lambda_24F0():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24F0)
    Fade(500)
    SetChrPos(0x160, 13000, 0, 1000, 90)
    OP_68(17160, 1300, 1300, 0)
    MoveCamera(27, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(13500, 1600)

    def lambda_254A():
        OP_96(0xFE, 0x3EE4, 0x0, 0x3E8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_254A)
    WaitChrThread(0x160, 1)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 0)), scpexpr(EXPR_END)), "loc_26AB")

    #C0121
    ChrTalk(
        0x101,
        "#11P#0002F啊，是小玲啊。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0122
    AnonymousTalk(
        0x160,
        (
            "贵安，大哥哥。\x02\x03",

            "呵呵，有一个月没见了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0123
    ChrTalk(
        0x101,
        (
            "#11P#0004F嗯，差不多吧。\x02\x03",

            "#0002F你又一个人\x01",
            "来古董店\x01",
            "玩吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x160,
        (
            "#3309F#5P嗯，顺便来看看庆典。\x02\x03",

            "#3302F刚才有游行，\x01",
            "大哥哥也看了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A63")

    label("loc_26AB")


    #C0125
    ChrTalk(
        0x101,
        "#11P#0005F你是……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("穿连衣裙的少女")

    #A0126
    AnonymousTalk(
        0xFF,
        (
            "贵安，大哥哥。\x02\x03",

            "呵呵，有两个月没见了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0127
    ChrTalk(
        0x101,
        (
            "#11P#0005F啊……你是人偶工房的那个……\x02\x03",

            "#0002F好久不见了。\x01",
            "没记错的话，你好像是叫小玲吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x160,
        (
            "#3306F#5P真是的，怎么可以这么不确定地\x01",
            "再次询问淑女的名字呢。\x02\x03",

            "#3301F牢记清楚，再会的时候\x01",
            "优雅地问候，才能算是合格的绅士吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#11P#0012F哈哈……抱歉，是我不好。\x02\x03",

            "#0000F你在这种地方做什么呢？\x02\x03",

            "#0005F好像只有你一个人……\x01",
            "莫非是迷路了？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x160,
        (
            "#3304F#5P玲可不是迷路了哦。\x02\x03",

            "只是偶尔会一个人来这家\x01",
            "古董店玩玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#11P#0005F是、是这样吗？\x02\x03",

            "#0001F不过，小孩子孤身一人\x01",
            "在这附近走动，多少也有点……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x160,
        (
            "#3309F#5P嘻嘻，\x01",
            "不会有什么危险啦。\x02\x03",

            "#3302F揽客的大哥哥\x01",
            "和陪酒的大姐姐都很和善……\x02\x03",

            "小巷里面戴着墨镜的叔叔们\x01",
            "也都是很有趣的人呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0133
    ChrTalk(
        0x101,
        "#11P#0011F是、是这样吗……？\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x160,
        (
            "#3304F#5P而且我今天\x01",
            "是来看庆典的。\x02\x03",

            "#3302F刚才的游行，\x01",
            "大哥哥也看了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A63")


    #C0135
    ChrTalk(
        0x101,
        (
            "#11P#0006F不，当时正在处理工作，\x01",
            "就错过了呢。\x02\x03",

            "#0008F（不过，这可伤脑筋了……）\x02\x03",

            "（把她一个人放在这里不管好像也不太好，\x01",
            "  要是没有工作的话，就可以\x01",
            "  送她回人偶工房了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x160,
        (
            "#3305F#5P？？？\x02\x03",

            "#3300F话说回来，大哥哥你\x01",
            "一个人在干什么呢？\x02\x03",

            "又在和谁\x01",
            "玩捉迷藏吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#11P#0006F不……\x01",
            "其实我正在寻找一个走失的孩子。\x02\x03",

            "#0000F好像是在今天游行的时候\x01",
            "跟家人走散的，\x01",
            "到现在还没找到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x160,
        (
            "#3300F#5P哦，是这样啊。\x02\x03",

            "你有照片什么的吗？\x01",
            "说不定玲知道哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#11P#0002F也是……\x01",
            "那就给你看一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德给玲看了柯林的照片。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(18, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)

    #A0141
    AnonymousTalk(
        0x160,
        (
            "#3300F……………………………………………\x02\x03",

            "#3305F#30W………………哎…………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0142
    ChrTalk(
        0x101,
        (
            "#11P#0005F怎么了？\x02\x03",

            "#0000F莫非你\x01",
            "见过这孩子吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x160, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x160)
    Sleep(300)

    #C0143
    ChrTalk(
        0x160,
        (
            "#5P#60W───没有。\x02\x01",

            "玲#500W……#60W才没有见过#500W……#60W这样的孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        "#11P#0006F是吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x160, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x160)

    #C0145
    ChrTalk(
        0x160,
        (
            "#3303F#5P不过……是个可爱的男孩呢。\x02\x03",

            "#3300F大哥哥……\x01",
            "你就是在找这孩子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#11P#0000F嗯，正在和同伴分头寻找他。\x02\x03",

            "#0008F真希望能早点找到他，\x01",
            "把他送回到父母身边……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x160,
        (
            "#3304F#5P呵呵……\x02\x03",

            "#3302F这样的话，玲也来\x01",
            "帮忙找这个孩子吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0148
    ChrTalk(
        0x101,
        "#11P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x160,
        (
            "#3302F#5P之前不是说过吗？\x01",
            "玲最擅长捉迷藏了。\x02\x03",

            "玲应该能找到\x01",
            "这孩子躲在哪里的。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#11P#0011F不，可是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x101,
        (
            "#11P#0004F（放着她一个人不管也不太好，\x01",
            "  姑且就让她跟着吧……）\x02\x03",

            "（万一不行的话，还可以让她\x01",
            "  到支援科去等……）\x02\x03",

            "#0000F──好吧，\x01",
            "那就麻烦你了哦。\x02\x03",

            "暂时跟大哥哥\x01",
            "一起行动好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x160,
        (
            "#3304F#5P呵呵，好啊。\x02\x03",

            "#3302F请多关照哦，罗伊德大哥哥。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        "#11P#0002F嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(13750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(18000, 1950, 1000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x0, 18000, 0, 1000, 270)
    SetChrPos(0x1, 18000, 0, 1000, 270)
    OP_1B(0x1, 0xFF, 0xFFFF)
    SetScenarioFlags(0xA2, 1)
    OP_29(0x46, 0x1, 0x5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_23_23A8 end

    def Function_24_3134(): pass

    label("Function_24_3134")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    def lambda_3143():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3143)
    Sleep(50)

    def lambda_3153():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3153)
    WaitChrThread(0x8, 1)

    #C0154
    ChrTalk(
        0x8,
        (
            "喂，别在那里\x01",
            "瞎转悠……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        "再不快滚的话，就要你们好看！\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    SetChrPos(0x0, -100, 0, 41020, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_24_3134 end

    def Function_25_31C8(): pass

    label("Function_25_31C8")

    EventBegin(0x1)

    #C0156
    ChrTalk(
        0x101,
        (
            "#0001F不，情报还没\x01",
            "探听够呢……\x02\x03",

            "在这一带再多\x01",
            "收集一下情报吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 20170, 0, 940, 274)
    EventEnd(0x4)
    Return()

    # Function_25_31C8 end

    SaveToFile()

Try(main)
