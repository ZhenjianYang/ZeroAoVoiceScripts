from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c030c.bin",                # FileName
        "c030c",                    # MapName
        "c030c",                    # Location
        0x002A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 42, 0, 2, 0, 3],
    )

    BuildStringList((
        "c030c",                  # 0
        "雷兹老人",               # 1
        "本特斯",                 # 2
        "库雷优",                 # 3
        "萨妮塔",                 # 4
        "菲伊",                   # 5
        "潘莎",                   # 6
        "达德利搜查官",           # 7
        "中央广场",               # 8
        "西街",                   # 9
        "行政区",                 # 10
        "住宅街",                 # 11
        "欢乐街",                 # 12
        "东街",                   # 13
        "旧城区",                 # 14
        "港湾区",                 # 15
        "ＩＢＣ",                 # 16
        "站前街道",               # 17
        "后巷",                   # 18
        "乌尔斯拉间道",           # 19
        "东克洛斯贝尔街道",       # 20
        "西克洛斯贝尔街道",       # 21
        "玛因兹山道",             # 22
    ))

    AddCharChip((
        "chr/ch21602.itc",                   # 00
        "chr/ch33000.itc",                   # 01
        "chr/ch33300.itc",                   # 02
        "chr/ch34400.itc",                   # 03
        "chr/ch32700.itc",                   # 04
        "chr/ch00902.itc",                   # 05
        "chr/ch22300.itc",                   # 06
    ))

    DeclNpc(-12850,  -5900,   -31489,  315,  341,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(32279,   0,       -4369,   270,  257,  0x0, 0,   1,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(-10039,  -6000,   -24590,  225,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-11039,  -6000,   -25709,  45,   277,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-5420,   0,       -3670,   90,   405,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-3980,   0,       -3670,   270,  405,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-12850,  -5849,   -31329,  315,  469,  0x0, 0,   5,   0,   255, 255, 0,   11,  255,  0)

    DeclActor(-2700,   -6500,   -38000,  2000,    -2700,   -5500,   -38000,  0x007C, 0,  12, 0x0000)
    DeclActor(17650,   0,       -800,    2000,    17650,   1500,    -800,    0x007C, 0,  13, 0x0000)
    DeclActor(0,       0,       -770,    2000,    0,       1500,    -770,    0x007C, 0,  14, 0x0000)

    PlaceName(167.6699981689453, 0.0, -124.73999786376953, 0x0000, 0x0000, "中央广场")
    PlaceName(61.15999984741211, 0.0, -117.44999694824219, 0x0000, 0x0000, "西街")
    PlaceName(211.41000366210938, 0.0, 19.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-37.66999816894531, 0.0, 3.240000009536743, 0x0000, 0x0000, "住宅街")
    PlaceName(80.5999984741211, 0.0, -9.720000267028809, 0x0000, 0x0000, "欢乐街")
    PlaceName(299.29998779296875, 0.0, -162.0, 0x0000, 0x0000, "东街")
    PlaceName(356.80999755859375, 0.0, -251.10000610351562, 0x0000, 0x0000, "旧城区")
    PlaceName(344.6600036621094, 0.0, -55.08000183105469, 0x0000, 0x0000, "港湾区")
    PlaceName(302.5400085449219, 0.0, 97.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(185.89999389648438, 0.0, -236.52000427246094, 0x0000, 0x0000, "站前街道")
    PlaceName(109.76000213623047, 0.0, -68.04000091552734, 0x0000, 0x0000, "后巷")
    PlaceName(181.0399932861328, 0.0, -286.739990234375, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(386.7799987792969, 0.0, -139.32000732421875, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-21.469999313354492, 0.0, -119.87999725341797, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-11.75, 0.0, 42.119998931884766, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(132.02999877929688, 0.0, -147.4199981689453, 0x0000, 0x0051, "")
    PlaceName(219.11000061035156, 0.0, -105.30000305175781, 0x0000, 0x0054, "")
    PlaceName(171.72000122070312, 0.0, -160.3800048828125, 0x0000, 0x0057, "")
    PlaceName(130.82000732421875, 0.0, -100.44000244140625, 0x0000, 0x0053, "")
    PlaceName(164.02999877929688, 0.0, -61.560001373291016, 0x0000, 0x0053, "")
    PlaceName(81.80999755859375, 0.0, -108.54000091552734, 0x0000, 0x0053, "")
    PlaceName(66.0199966430664, 0.0, -74.5199966430664, 0x0000, 0x0053, "")
    PlaceName(104.9000015258789, 0.0, -22.68000030517578, 0x0000, 0x0052, "")
    PlaceName(112.58999633789062, 0.0, -43.7400016784668, 0x0000, 0x0053, "")
    PlaceName(126.7699966430664, 0.0, -57.5099983215332, 0x0000, 0x0053, "")
    PlaceName(172.94000244140625, 0.0, 57.5099983215332, 0x0000, 0x0051, "")
    PlaceName(354.3800048828125, 0.0, -162.0, 0x0000, 0x0052, "")
    PlaceName(326.8399963378906, 0.0, -308.6099853515625, 0x0000, 0x0053, "")
    PlaceName(305.7799987792969, 0.0, -278.6400146484375, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_460",          # 00, 0
        "Function_1_518",          # 01, 1
        "Function_2_579",          # 02, 2
        "Function_3_7A9",          # 03, 3
        "Function_4_8C3",          # 04, 4
        "Function_5_CA2",          # 05, 5
        "Function_6_EFB",          # 06, 6
        "Function_7_10DF",         # 07, 7
        "Function_8_128E",         # 08, 8
        "Function_9_12E9",         # 09, 9
        "Function_10_131F",        # 0A, 10
        "Function_11_13FF",        # 0B, 11
        "Function_12_18D0",        # 0C, 12
        "Function_13_18D1",        # 0D, 13
        "Function_14_18F5",        # 0E, 14
    ))


    def Function_0_460(): pass

    label("Function_0_460")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4A0"),
        (1, "loc_4AC"),
        (2, "loc_4B8"),
        (3, "loc_4C4"),
        (4, "loc_4D0"),
        (5, "loc_4DC"),
        (6, "loc_4E8"),
        (SWITCH_DEFAULT, "loc_4F4"),
    )


    label("loc_4A0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4AC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4B8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4C4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4D0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4DC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_500")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_517")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_517")

    Return()

    # Function_0_460 end

    def Function_1_518(): pass

    label("Function_1_518")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_578")
    OP_95(0xFE, 2630, 0, -4370, 1000, 0x0)
    OP_95(0xFE, 240, 0, -7350, 1000, 0x0)
    OP_95(0xFE, 240, -750, -48720, 1000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 35280, 0, -4370, 45)
    Jump("Function_1_518")

    label("loc_578")

    Return()

    # Function_1_518 end

    def Function_2_579(): pass

    label("Function_2_579")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70A")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63B")
    SetChrPos(0x0, 230, -750, -38720, 0)
    SetChrPos(0x1, 230, -750, -38720, 0)
    SetChrPos(0x2, 230, -750, -38720, 0)
    SetChrPos(0x3, 230, -750, -38720, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60E")
    SetChrPos(0x4, 230, -750, -38720, 0)
    SetChrPos(0x5, 230, -750, -38720, 0)
    Jump("loc_62D")

    label("loc_60E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62D")
    SetChrPos(0x4, 230, -750, -38720, 0)

    label("loc_62D")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70A")

    label("loc_63B")

    SetChrPos(0x0, 24330, 0, -4050, 270)
    SetChrPos(0x1, 24330, 0, -4050, 270)
    SetChrPos(0x2, 24330, 0, -4050, 270)
    SetChrPos(0x3, 24330, 0, -4050, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B4")
    SetChrPos(0x4, 24330, 0, -4050, 270)
    SetChrPos(0x5, 24330, 0, -4050, 270)
    Jump("loc_6D3")

    label("loc_6B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D3")
    SetChrPos(0x4, 24330, 0, -4050, 270)

    label("loc_6D3")

    OP_68(24330, 2000, -4050, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70A")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_735")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_790")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_765")
    SetChrPos(0xA, -2820, 0, -6370, 90)
    SetChrPos(0xB, -3310, 0, -5590, 135)
    Jump("loc_790")

    label("loc_765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_773")
    Jump("loc_790")

    label("loc_773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_790")
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_790")

    label("loc_790")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A8")
    OP_C7(0x1, 0x1000)

    label("loc_7A8")

    Return()

    # Function_2_579 end

    def Function_3_7A9(): pass

    label("Function_3_7A9")

    OP_65(0x0, 0x1)
    SetMapObjFrame(0xF, "light", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0xD, 0x10)
    OP_70(0x0, 0xA)
    OP_70(0x1, 0xA)
    OP_70(0x3, 0xA)
    OP_70(0x4, 0xA)
    OP_70(0x5, 0x0)
    OP_70(0x6, 0xA)
    OP_70(0xD, 0x1E)
    OP_70(0x0, 0x0)
    OP_66(0x2, 0x1)
    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, -4000, -5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, -4000, -30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -15000, -9000, -30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_3_7A9 end

    def Function_4_8C3(): pass

    label("Function_4_8C3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_957")
    Jump("loc_9A1")

    label("loc_957")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_977")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A1")

    label("loc_977")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_997")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A1")

    label("loc_997")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_AD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A2A")

    #C0001
    ChrTalk(
        0x8,
        (
            "听说那些游击士在纪念庆典期间\x01",
            "也连日表现活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "呵呵，果然厉害呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD1")

    label("loc_A2A")


    #C0003
    ChrTalk(
        0x8,
        (
            "听说那些游击士在纪念庆典期间\x01",
            "也表现活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "呵呵，真不愧是\x01",
            "『支援护臂甲』——游击士协会呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "无论何时\x01",
            "都是市民的伙伴……\x01",
            "再没有比他们更可靠的人了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AD1")

    Jump("loc_C9A")

    label("loc_AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B3B")

    #C0006
    ChrTalk(
        0x8,
        (
            "唔……送比萨的人\x01",
            "刚才路过了这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "竟然有人在纪念庆典时\x01",
            "还待在家里\x01",
            "吃比萨吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9A")

    label("loc_B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BB1")

    #C0008
    ChrTalk(
        0x8,
        (
            "朋友邀请我\x01",
            "去参加宴会，\x01",
            "差不多该走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "哎呀呀，虽然是\x01",
            "每年的例行公事，但还真麻烦呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2D")

    label("loc_BB1")


    #C0010
    ChrTalk(
        0x8,
        "好，走吧。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "今年也有人\x01",
            "邀请我参加宴会。\x01",
            "差不多该走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "唉，真是的……\x01",
            "虽然是每年的例行公事，但还真麻烦呀。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C2D")

    Jump("loc_C9A")

    label("loc_C32")


    #C0013
    ChrTalk(
        0x8,
        "纪念庆典，很好很好。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "市长似乎也平安无事，\x01",
            "没有比这更值得庆贺的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "稍后我也去\x01",
            "逛一圈吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_8C3 end

    def Function_5_CA2(): pass

    label("Function_5_CA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_CFC")

    #C0016
    ChrTalk(
        0x9,
        "庆典到今天也该收场了。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "今天想到的事请\x01",
            "就必须要在今天全部做完。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF7")

    label("loc_CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_D61")

    #C0018
    ChrTalk(
        0x9,
        (
            "糟了，忘记\x01",
            "带相机了……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "算了，反正\x01",
            "明天的克洛斯贝尔时代周刊\x01",
            "也会登照片的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF7")

    label("loc_D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_E10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D97")

    #C0020
    ChrTalk(
        0x9,
        (
            "唔，我也去\x01",
            "找个好地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0B")

    label("loc_D97")


    #C0021
    ChrTalk(
        0x9,
        (
            "游行是从警察局总部的\x01",
            "旁边开始的。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            "唔，大概还要过一阵\x01",
            "才能走到这边吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "……我也先去\x01",
            "找个好地方吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_E0B")

    Jump("loc_EF7")

    label("loc_E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E75")

    #C0024
    ChrTalk(
        0x9,
        (
            "听说有扒手\x01",
            "混在人群里\x01",
            "为非作歹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "警官刚才提醒大家小心了，\x01",
            "你们也当心点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF7")

    label("loc_E75")


    #C0026
    ChrTalk(
        0x9,
        "……纪念庆典真是华丽壮观。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        "……愿克洛斯贝尔辉煌永存。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "唔，庆典真不错啊。\x01",
            "只要是克洛斯贝尔人，\x01",
            "都会觉得激动不已的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF7")

    TalkEnd(0xFE)
    Return()

    # Function_5_CA2 end

    def Function_6_EFB(): pass

    label("Function_6_EFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_F54")
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    #C0029
    ChrTalk(
        0xA,
        "游行好精彩啊～！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        (
            "来看游行\x01",
            "真是来对了～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DB")

    label("loc_F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_F9D")

    #C0031
    ChrTalk(
        0xA,
        (
            "今天的游行\x01",
            "好像要通过住宅街呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        "呵呵，好期待哦～\x02",
    )

    CloseMessageWindow()
    Jump("loc_10DB")

    label("loc_F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_FF8")

    #C0033
    ChrTalk(
        0xA,
        (
            "今天打算\x01",
            "去欢乐街那边。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xA,
        (
            "我先生让我们\x01",
            "出去玩玩，\x01",
            "一定要玩个痛快呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DB")

    label("loc_FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1054")

    #C0035
    ChrTalk(
        0xA,
        (
            "我先生时不时\x01",
            "就会说些令人开心的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            "呵呵，他怎么知道\x01",
            "我在想什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DB")

    label("loc_1054")


    #C0037
    ChrTalk(
        0xA,
        (
            "我先生让我带女儿\x01",
            "出去逛一圈。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "他那个人呀……\x01",
            "时不时就会说些\x01",
            "体贴人的话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "呵呵，机会难得嘛，\x01",
            "我就恭敬不如从命了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_10DB")

    TalkEnd(0xFE)
    Return()

    # Function_6_EFB end

    def Function_7_10DF(): pass

    label("Function_7_10DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1124")
    OP_4B(0xA, 0xFF)

    #C0040
    ChrTalk(
        0xB,
        (
            "咳咳，妈妈，\x01",
            "您别太兴奋了，\x01",
            "很丢人啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_128A")

    label("loc_1124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_117F")
    OP_4B(0xA, 0xFF)
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0041
    ChrTalk(
        0xB,
        (
            "妈妈，再不快一点的话，\x01",
            "游行就要开始了！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)
    OP_4C(0xA, 0xFF)
    Jump("loc_128A")

    label("loc_117F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_123F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_11CC")

    #C0042
    ChrTalk(
        0xB,
        (
            "玛丽还小，\x01",
            "父亲又有工作嘛。\x01",
            "……萨妮塔会忍耐的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123A")

    label("loc_11CC")


    #C0043
    ChrTalk(
        0xB,
        (
            "既然要出去逛，\x01",
            "要是玛丽和爸爸\x01",
            "也一起去就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xB,
        (
            "当、当然了，萨妮塔\x01",
            "是不会提出这么任性的要求的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_123A")

    Jump("loc_128A")

    label("loc_123F")

    OP_4B(0xA, 0xFF)

    #C0045
    ChrTalk(
        0xB,
        (
            "妈妈，萨妮塔\x01",
            "想吃手制冰激凌呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        "今天请给我一些零用钱吧。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_128A")

    TalkEnd(0xFE)
    Return()

    # Function_7_10DF end

    def Function_8_128E(): pass

    label("Function_8_128E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A3")
    Call(0, 10)
    Jump("loc_12E5")

    label("loc_12A3")


    #C0047
    ChrTalk(
        0xFE,
        (
            "看呀，\x01",
            "多么气派的住宅街。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "嗯嗯，那栋大宅\x01",
            "很值得欣赏吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E5")

    TalkEnd(0xFE)
    Return()

    # Function_8_128E end

    def Function_9_12E9(): pass

    label("Function_9_12E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FE")
    Call(0, 10)
    Jump("loc_131B")

    label("loc_12FE")


    #C0049
    ChrTalk(
        0xFE,
        (
            "哇～我想去看\x01",
            "庆典呀～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131B")

    TalkEnd(0xFE)
    Return()

    # Function_9_12E9 end

    def Function_10_131F(): pass

    label("Function_10_131F")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0050
    ChrTalk(
        0xD,
        "爸爸是大笨蛋～！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xD,
        (
            "身为铁道工程师，\x01",
            "竟然是个路痴～！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xC,
        "潘莎，那是当然的啦。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xC,
        (
            "因为列车只会往\x01",
            "固定的方向跑啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    OP_63(0xD, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0xC)

    #C0054
    ChrTalk(
        0xD,
        "爸爸是个大笨蛋～！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_10_131F end

    def Function_11_13FF(): pass

    label("Function_11_13FF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1493")
    Jump("loc_14DD")

    label("loc_1493")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14B3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14DD")

    label("loc_14B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14D3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14DD")

    label("loc_14D3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14DD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1786")
    SetChrSubChip(0xFE, 0x0)

    #C0055
    ChrTalk(
        0xFE,
        "#0600F呼……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0056
    ChrTalk(
        0x101,
        "#0005F达、达德利搜查官！？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#0105F您怎么会在这里……\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1657")
    Jump("loc_16A1")

    label("loc_1657")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1677")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16A1")

    label("loc_1677")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1697")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16A1")

    label("loc_1697")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16A1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0058
    ChrTalk(
        0xFE,
        (
            "#0601F是支援科啊……\x02\x03",

            "#0603F……只是稍微休息一下而已，\x01",
            "不必管我。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        "#0000F是、是……\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        "#0203F（似乎相当疲倦呢。）\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#0300F（虽然他爱摆架子，\x01",
            "  不过也确实在努力工作呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 7)
    Jump("loc_18C8")

    label("loc_1786")

    SetChrSubChip(0xFE, 0x0)

    #C0062
    ChrTalk(
        0xFE,
        (
            "#0603F话说回来，\x01",
            "今天好像有那个吧……\x02\x03",

            "还是和历年一样，\x01",
            "只有形式上的监视吗……\x02\x03",

            "#0601F哼……\x01",
            "……等着瞧吧……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C8")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0063
    ChrTalk(
        0x103,
        "#0200F（似乎很不爽呢。）\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#0100F（他看上去好像挺疲倦的，\x01",
            "  还是不要打扰他了吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_18C8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_13FF end

    def Function_12_18D0(): pass

    label("Function_12_18D0")

    Return()

    # Function_12_18D0 end

    def Function_13_18D1(): pass

    label("Function_13_18D1")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_13_18D1 end

    def Function_14_18F5(): pass

    label("Function_14_18F5")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F5")

    #C0066
    ChrTalk(
        0x102,
        (
            "#0105F这里是……\x01",
            "坎贝尔议员的宅邸呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        "#0005F坎贝尔议员？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#0103F是共和国派的领头议员。\x01",
            "在政界也有相当的权威。\x02\x03",

            "#0100F如果没什么事的话，\x01",
            "还是不要去打扰\x01",
            "人家比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#0000F说得也是……也没什么要事，\x01",
            "还是不要去了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x46, 3)
    Jump("loc_1A3D")

    label("loc_19F5")

    SetChrName("")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里是共和国派·坎贝尔议员的宅邸。\x01",
            "没什么需要去拜访的要事。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1A3D")

    TalkEnd(0xFF)
    Return()

    # Function_14_18F5 end

    SaveToFile()

Try(main)
