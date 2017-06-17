from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "レイズ老人",             # 1
        "ペントス",               # 2
        "クレイユ",               # 3
        "サニータ",               # 4
        "フェイ",                 # 5
        "パンセ",                 # 6
        "ダドリー捜査官",         # 7
        "中央広場",               # 8
        "西通り",                 # 9
        "行政区",                 # 10
        "住宅街",                 # 11
        "歓楽街",                 # 12
        "東通り",                 # 13
        "旧市街",                 # 14
        "港湾区",                 # 15
        "ＩＢＣ",                 # 16
        "駅前通り",               # 17
        "裏通り",                 # 18
        "ウルスラ間道",           # 19
        "東クロスベル街道",       # 20
        "西クロスベル街道",       # 21
        "マインツ山道",           # 22
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

    PlaceName(167.6699981689453, 0.0, -124.73999786376953, 0x0000, 0x0000, "中央広場")
    PlaceName(61.15999984741211, 0.0, -117.44999694824219, 0x0000, 0x0000, "西通り")
    PlaceName(211.41000366210938, 0.0, 19.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-37.66999816894531, 0.0, 3.240000009536743, 0x0000, 0x0000, "住宅街")
    PlaceName(80.5999984741211, 0.0, -9.720000267028809, 0x0000, 0x0000, "歓楽街")
    PlaceName(299.29998779296875, 0.0, -162.0, 0x0000, 0x0000, "東通り")
    PlaceName(356.80999755859375, 0.0, -251.10000610351562, 0x0000, 0x0000, "旧市街")
    PlaceName(344.6600036621094, 0.0, -55.08000183105469, 0x0000, 0x0000, "港湾区")
    PlaceName(302.5400085449219, 0.0, 97.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(185.89999389648438, 0.0, -236.52000427246094, 0x0000, 0x0000, "駅前通り")
    PlaceName(109.76000213623047, 0.0, -68.04000091552734, 0x0000, 0x0000, "裏通り")
    PlaceName(181.0399932861328, 0.0, -286.739990234375, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(386.7799987792969, 0.0, -139.32000732421875, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-21.469999313354492, 0.0, -119.87999725341797, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-11.75, 0.0, 42.119998931884766, 0x0000, 0x0000, "マインツ山道")
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
        "Function_5_D3E",          # 05, 5
        "Function_6_103D",         # 06, 6
        "Function_7_12C5",         # 07, 7
        "Function_8_14F6",         # 08, 8
        "Function_9_1579",         # 09, 9
        "Function_10_15BF",        # 0A, 10
        "Function_11_16BB",        # 0B, 11
        "Function_12_1BDC",        # 0C, 12
        "Function_13_1BDD",        # 0D, 13
        "Function_14_1C0F",        # 0E, 14
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_AF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A36")

    #C0001
    ChrTalk(
        0x8,
        (
            "記念祭の間も遊撃士たちは\x01",
            "連日活躍しておるそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "ふぉふぉ、さすがじゃな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AEB")

    label("loc_A36")


    #C0003
    ChrTalk(
        0x8,
        (
            "記念祭の間も遊撃士たちは\x01",
            "活躍しておるそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "ふぉふぉ、さすがは\x01",
            "《支える篭手》じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "どんなときも\x01",
            "市民の味方になってくれる……\x01",
            "これほど心強い存在はないわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AEB")

    Jump("loc_D36")

    label("loc_AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B73")

    #C0006
    ChrTalk(
        0x8,
        (
            "む……またピザの配達人が\x01",
            "通っていったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "記念祭だというのに\x01",
            "自宅でピザを食べておる\x01",
            "輩でもおるのかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D36")

    label("loc_B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C07")

    #C0008
    ChrTalk(
        0x8,
        (
            "知り合いのパーティに\x01",
            "呼ばれておってな、\x01",
            "そろそろ出かけねばならんのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "やれやれ、毎年の\x01",
            "ことながら億劫じゃわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA9")

    label("loc_C07")


    #C0010
    ChrTalk(
        0x8,
        "どれ、よっこらしょっと。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "わしも今日は\x01",
            "パーティに呼ばれておってのう。\x01",
            "出かけねばならんのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "ああ、やれやれ……\x01",
            "毎年のことながら億劫じゃわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_CA9")

    Jump("loc_D36")

    label("loc_CAE")


    #C0013
    ChrTalk(
        0x8,
        "記念祭、結構結構。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "市長もご無事だったことじゃし\x01",
            "めでたいことこの上ないわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "わしも後でぶらりと\x01",
            "一回りしてみようかのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D36")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_8C3 end

    def Function_5_D3E(): pass

    label("Function_5_D3E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_DB0")

    #C0016
    ChrTalk(
        0x9,
        "祭りも今日で遊び収めというわけだ。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "今日のうちに思いつく事は\x01",
            "全てやっておかなければな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1039")

    label("loc_DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_E35")

    #C0018
    ChrTalk(
        0x9,
        (
            "しまった、カメラを\x01",
            "持ってくるのを忘れたな……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "まあよいか、写真なら\x01",
            "明日のクロスベルタイムズにも\x01",
            "載るだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1039")

    label("loc_E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E77")

    #C0020
    ChrTalk(
        0x9,
        (
            "ふむ、私もいい場所を\x01",
            "探しておこうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_E77")


    #C0021
    ChrTalk(
        0x9,
        (
            "パレードは警察本部の\x01",
            "脇からスタートするのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            "ふむこの辺りに差し掛かるのは\x01",
            "もう少し先になるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "……私もいい場所を\x01",
            "探しておこうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_F13")

    Jump("loc_1039")

    label("loc_F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_FAB")

    #C0024
    ChrTalk(
        0x9,
        (
            "このどさくさに紛れて\x01",
            "スリや引ったくりが\x01",
            "横行しているらしいぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "先ほど警官が注意を呼びかけていた。\x01",
            "君たちも気を付けたまえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1039")

    label("loc_FAB")


    #C0026
    ChrTalk(
        0x9,
        "……記念祭、華やかなるかな。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        "……クロスベル、永遠なるかな。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "うむ、祭りは良いものだ。\x01",
            "クロスベル人なら\x01",
            "血が騒ぐというものだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1039")

    TalkEnd(0xFE)
    Return()

    # Function_5_D3E end

    def Function_6_103D(): pass

    label("Function_6_103D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_10AC")
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    #C0029
    ChrTalk(
        0xA,
        "見事なパレードでしたのー！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        (
            "やっぱり見にきて\x01",
            "良かったですわー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C1")

    label("loc_10AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_110D")

    #C0031
    ChrTalk(
        0xA,
        (
            "今日のパレードは\x01",
            "住宅街の中も通るらしいんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        "ふふ、楽しみですわ～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12C1")

    label("loc_110D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1198")

    #C0033
    ChrTalk(
        0xA,
        (
            "今日は歓楽街の方へ\x01",
            "行ってみるつもりですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xA,
        (
            "主人も遊んでくればいいと\x01",
            "言ってくれましたし、\x01",
            "目一杯楽しんできますの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C1")

    label("loc_1198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_120C")

    #C0035
    ChrTalk(
        0xA,
        (
            "主人は時々\x01",
            "嬉しい事を言ってくれますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            "ふふ、どうして私の\x01",
            "考えている事が判ったのでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C1")

    label("loc_120C")


    #C0037
    ChrTalk(
        0xA,
        (
            "主人が、娘と一回り\x01",
            "してきたらどうだと言うんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "あの人ったら……\x01",
            "時々優しい事を\x01",
            "言ってくれるんですのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "ふふ、せっかくですもの。\x01",
            "好意に甘えてしまおうかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_12C1")

    TalkEnd(0xFE)
    Return()

    # Function_6_103D end

    def Function_7_12C5(): pass

    label("Function_7_12C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1320")
    OP_4B(0xA, 0xFF)

    #C0040
    ChrTalk(
        0xB,
        (
            "コホン、お母さま。\x01",
            "あまりはしゃぐと\x01",
            "みっともありませんわよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_14F2")

    label("loc_1320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_138D")
    OP_4B(0xA, 0xFF)
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0041
    ChrTalk(
        0xB,
        (
            "お母さま、いそがないと\x01",
            "パレードがはじまってしまいますわ！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)
    OP_4C(0xA, 0xFF)
    Jump("loc_14F2")

    label("loc_138D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_148B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1400")

    #C0042
    ChrTalk(
        0xB,
        (
            "マリーはちいさいし\x01",
            "お父さまはおしごとがあるんですもの。\x01",
            "……サニータはがまんしますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1486")

    label("loc_1400")


    #C0043
    ChrTalk(
        0xB,
        (
            "おそとをあるくのだったら\x01",
            "マリーやお父さまも\x01",
            "いっしょがよかったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xB,
        (
            "も、もちろんサニータは\x01",
            "わがままはいわないけれど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1486")

    Jump("loc_14F2")

    label("loc_148B")

    OP_4B(0xA, 0xFF)

    #C0045
    ChrTalk(
        0xB,
        (
            "お母さま、サニータは\x01",
            "ジェラートがたべたいですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        "きょうはおこづかいをくださいませ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_14F2")

    TalkEnd(0xFE)
    Return()

    # Function_7_12C5 end

    def Function_8_14F6(): pass

    label("Function_8_14F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150B")
    Call(0, 10)
    Jump("loc_1575")

    label("loc_150B")


    #C0047
    ChrTalk(
        0xFE,
        (
            "でもごらんよ。\x01",
            "立派な住宅街じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "ふむふむ、あのお屋敷なんて\x01",
            "鑑賞に値するんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1575")

    TalkEnd(0xFE)
    Return()

    # Function_8_14F6 end

    def Function_9_1579(): pass

    label("Function_9_1579")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_158E")
    Call(0, 10)
    Jump("loc_15BB")

    label("loc_158E")


    #C0049
    ChrTalk(
        0xFE,
        (
            "わーん、あたしは\x01",
            "お祭りが見たいのに～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BB")

    TalkEnd(0xFE)
    Return()

    # Function_9_1579 end

    def Function_10_15BF(): pass

    label("Function_10_15BF")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0050
    ChrTalk(
        0xD,
        "おとーさんのバカー！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xD,
        (
            "鉄道技師のくせに\x01",
            "方向音痴なんだから～！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xC,
        "パンセ、それは当然だよ。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xC,
        (
            "鉄道は決まった\x01",
            "方向にしか走らないからね！\x02",
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
        "おとーさんのバカーっ！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_10_15BF end

    def Function_11_16BB(): pass

    label("Function_11_16BB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_174F")
    Jump("loc_1799")

    label("loc_174F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_176F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1799")

    label("loc_176F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_178F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1799")

    label("loc_178F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1799")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A68")
    SetChrSubChip(0xFE, 0x0)

    #C0055
    ChrTalk(
        0xFE,
        "#0600Fふう……\x02",
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
        "#0005Fダ、ダドリー捜査官！？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#0105Fどうしてこんな所に……\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_191B")
    Jump("loc_1965")

    label("loc_191B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_193B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1965")

    label("loc_193B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_195B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1965")

    label("loc_195B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1965")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0058
    ChrTalk(
        0xFE,
        (
            "#0601F支援課、お前たちか……\x02\x03",

            "#0603F……少々休憩しているだけだ。\x01",
            "いいから放っておけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        "#0000Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        "#0203F（相当お疲れのようですね。）\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#0300F（偉そうにしてる分は\x01",
            "  働いているみてぇだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 7)
    Jump("loc_1BD4")

    label("loc_1A68")

    SetChrSubChip(0xFE, 0x0)

    #C0062
    ChrTalk(
        0xFE,
        (
            "#0603Fそういえば今日は\x01",
            "アレがあるんだったな……\x02\x03",

            "また例年通りお座なりな\x01",
            "監視だけというわけか……\x02\x03",

            "#0601Fフン……\x01",
            "……今に見ているがいい……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BD4")
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
        "#0200F（何だかやさぐれてますね。）\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#0100F（疲れているみたいだし\x01",
            "  そっとしておきましょう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_1BD4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_16BB end

    def Function_12_1BDC(): pass

    label("Function_12_1BDC")

    Return()

    # Function_12_1BDC end

    def Function_13_1BDD(): pass

    label("Function_13_1BDD")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_13_1BDD end

    def Function_14_1C0F(): pass

    label("Function_14_1C0F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D21")

    #C0066
    ChrTalk(
        0x102,
        (
            "#0105Fここは……\x01",
            "キャンベル議員のお宅ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        "#0005Fキャンベル議員？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#0103F共和国派の筆頭議員よ。\x01",
            "政界でもかなりの実力者ね。\x02\x03",

            "#0100F用事が無いなら\x01",
            "お邪魔しない方が\x01",
            "いいんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#0000Fそうだな……特に用もないし\x01",
            "止めておこうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x46, 3)
    Jump("loc_1D67")

    label("loc_1D21")

    SetChrName("")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "共和国派・キャンベル議員の邸宅だ。\x01",
            "特に訪ねる用事はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1D67")

    TalkEnd(0xFF)
    Return()

    # Function_14_1C0F end

    SaveToFile()

Try(main)
