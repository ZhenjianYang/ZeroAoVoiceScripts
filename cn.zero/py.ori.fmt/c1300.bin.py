from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1300.bin",                # FileName
        "c1300",                    # MapName
        "c1300",                    # Location
        0x001B,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 27, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1300",                  # 0
        "警备员比尔斯",           # 1
        "警备员汪古",             # 2
        "阿奈斯特秘书",           # 3
        "格蕾丝",                 # 4
        "是假货哦",               # 5
        "中央广场",               # 6
        "西街",                   # 7
        "行政区",                 # 8
        "住宅街",                 # 9
        "欢乐街",                 # 10
        "东街",                   # 11
        "旧城区",                 # 12
        "港湾区",                 # 13
        "ＩＢＣ",                 # 14
        "站前街道",               # 15
        "后巷",                   # 16
        "乌尔斯拉间道",           # 17
        "东克洛斯贝尔街道",       # 18
        "西克洛斯贝尔街道",       # 19
        "玛因兹山道",             # 20
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
    ))

    DeclNpc(3910,    0,       5050,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(1700,    0,       -22129,  180,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(1750,    0,       -1799,   0,    510,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(7000,    0,       2300,    1200,    7000,    1700,    2300,    0x007C, 0,  10, 0x0000)
    DeclActor(1750,    0,       -1800,   1500,    1750,    1500,    -1800,   0x007C, 0,  5,  0x0000)

    PlaceName(-133.72000122070312, 0.0, -187.47999572753906, 0x0000, 0x0000, "中央广场")
    PlaceName(-223.1999969482422, 0.0, -181.35000610351562, 0x0000, 0x0000, "西街")
    PlaceName(-96.97000122070312, 0.0, -66.3499984741211, 0x0000, 0x0000, "行政区")
    PlaceName(-306.2300109863281, 0.0, -79.95999908447266, 0x0000, 0x0000, "住宅街")
    PlaceName(-206.8699951171875, 0.0, -90.8499984741211, 0x0000, 0x0000, "欢乐街")
    PlaceName(-23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0000, "东街")
    PlaceName(25.18000030517578, 0.0, -293.6400146484375, 0x0000, 0x0000, "旧城区")
    PlaceName(14.970000267028809, 0.0, -128.9499969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-20.420000076293945, 0.0, -1.0199999809265137, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-118.41000366210938, 0.0, -281.3900146484375, 0x0000, 0x0000, "站前街道")
    PlaceName(-182.3699951171875, 0.0, -139.83999633789062, 0x0000, 0x0000, "后巷")
    PlaceName(-122.48999786376953, 0.0, -323.5799865722656, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(50.36000061035156, 0.0, -199.72999572753906, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-292.6199951171875, 0.0, -183.38999938964844, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-284.45001220703125, 0.0, -47.290000915527344, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-163.66000366210938, 0.0, -206.52999877929688, 0x0000, 0x0051, "")
    PlaceName(-90.51000213623047, 0.0, -171.14999389648438, 0x0000, 0x0054, "")
    PlaceName(-130.32000732421875, 0.0, -217.4199981689453, 0x0000, 0x0057, "")
    PlaceName(-164.67999267578125, 0.0, -167.05999755859375, 0x0000, 0x0053, "")
    PlaceName(-136.77999877929688, 0.0, -134.39999389648438, 0x0000, 0x0053, "")
    PlaceName(-205.85000610351562, 0.0, -173.8699951171875, 0x0000, 0x0053, "")
    PlaceName(-219.1199951171875, 0.0, -145.2899932861328, 0x0000, 0x0053, "")
    PlaceName(-186.4600067138672, 0.0, -101.7300033569336, 0x0000, 0x0052, "")
    PlaceName(-179.99000549316406, 0.0, -119.43000030517578, 0x0000, 0x0053, "")
    PlaceName(-168.0800018310547, 0.0, -131.0, 0x0000, 0x0053, "")
    PlaceName(-129.3000030517578, 0.0, -34.369998931884766, 0x0000, 0x0051, "")
    PlaceName(23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0052, "")
    PlaceName(0.0, 0.0, -341.95001220703125, 0x0000, 0x0053, "")
    PlaceName(-17.690000534057617, 0.0, -316.7699890136719, 0x0000, 0x0053, "")
    PlaceName(-118.41000366210938, 0.0, -203.80999755859375, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_3F0",          # 00, 0
        "Function_1_4A8",          # 01, 1
        "Function_2_6C0",          # 02, 2
        "Function_3_813",          # 03, 3
        "Function_4_1560",         # 04, 4
        "Function_5_1611",         # 05, 5
        "Function_6_186C",         # 06, 6
        "Function_7_18F7",         # 07, 7
        "Function_8_1DF0",         # 08, 8
        "Function_9_3877",         # 09, 9
        "Function_10_4151",        # 0A, 10
    ))


    def Function_0_3F0(): pass

    label("Function_0_3F0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_430"),
        (1, "loc_43C"),
        (2, "loc_448"),
        (3, "loc_454"),
        (4, "loc_460"),
        (5, "loc_46C"),
        (6, "loc_478"),
        (SWITCH_DEFAULT, "loc_484"),
    )


    label("loc_430")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_43C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_448")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_454")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_460")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_46C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_478")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_484")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_490")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_4A7")

    Return()

    # Function_0_3F0 end

    def Function_1_4A8(): pass

    label("Function_1_4A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_557")
    SetChrPos(0x0, -230, -1450, -33980, 0)
    SetChrPos(0x1, -230, -1450, -33980, 0)
    SetChrPos(0x2, -230, -1450, -33980, 0)
    SetChrPos(0x3, -230, -1450, -33980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52F")
    SetChrPos(0x4, -230, -1450, -33980, 0)
    SetChrPos(0x5, -230, -1450, -33980, 0)
    Jump("loc_54E")

    label("loc_52F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54E")
    SetChrPos(0x4, -230, -1450, -33980, 0)

    label("loc_54E")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_557")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_56F")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 6)

    label("loc_56F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A")
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_5AD")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A0")
    Event(0, 9)
    Jump("loc_5AD")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AD")
    SetScenarioFlags(0x53, 2)

    label("loc_5AD")

    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5DB")
    SetChrPos(0x8, -2040, 0, -21950, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_6A8")

    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5E9")
    Jump("loc_6A8")

    label("loc_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5F7")
    Jump("loc_6A8")

    label("loc_5F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_616")
    SetChrPos(0x8, 2610, 0, 2230, 160)
    Jump("loc_6A8")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_635")
    SetChrPos(0x8, -180, 0, -22030, 180)
    Jump("loc_6A8")

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_643")
    Jump("loc_6A8")

    label("loc_643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_651")
    Jump("loc_6A8")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_65F")
    Jump("loc_6A8")

    label("loc_65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_66D")
    Jump("loc_6A8")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_67B")
    Jump("loc_6A8")

    label("loc_67B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_689")
    Jump("loc_6A8")

    label("loc_689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_697")
    Jump("loc_6A8")

    label("loc_697")

    SetChrPos(0x8, -180, 0, -22030, 180)

    label("loc_6A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BF")
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_6BF")

    Return()

    # Function_1_4A8 end

    def Function_2_6C0(): pass

    label("Function_2_6C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_718")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_779")

    label("loc_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_754")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_779")

    label("loc_754")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_779")

    SetMapObjFlags(0x2, 0x4)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A8")
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_7A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B6")

    label("loc_7B6")

    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D2")
    OP_70(0x1, 0x0)

    label("loc_7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E4")
    OP_70(0x1, 0x0)

    label("loc_7E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7F1")
    OP_70(0x1, 0x0)

    label("loc_7F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80D")
    Jump("loc_812")

    label("loc_80D")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_812")

    Return()

    # Function_2_6C0 end

    def Function_3_813(): pass

    label("Function_3_813")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_87A")

    #C0001
    ChrTalk(
        0xFE,
        (
            "不好意思啊，ＩＢＣ的营业时间\x01",
            "只到四点半哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "衷心期待您的再次光临。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AE")

    label("loc_87A")


    #C0003
    ChrTalk(
        0xFE,
        "门锁ＯＫ。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "门锁没有异常，完毕～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    ClearChrFlags(0x8, 0x10)

    label("loc_8AE")

    Jump("loc_155C")

    label("loc_8B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_946")

    #C0005
    ChrTalk(
        0xFE,
        (
            "我们的保安部门十分优秀哦。\x01",
            "关于市内的事件，我们也接到了报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "但是，出现失踪人员这种事情，\x01",
            "毕竟还是警察的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DF")

    label("loc_946")


    #C0007
    ChrTalk(
        0xFE,
        (
            "从保安部门那里\x01",
            "接到了令人在意的报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "市内好像接连出现了\x01",
            "失踪者呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "嗯，但那些毕竟\x01",
            "都是警察的工作啊。\x01",
            "至少ＩＢＣ这边今天还是很平静。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_9DF")

    Jump("loc_155C")

    label("loc_9E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_AC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A3B")

    #C0010
    ChrTalk(
        0xFE,
        (
            "港湾区那边刚刚\x01",
            "发生过枪击事件，\x01",
            "警备工作也不能松懈大意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABF")

    label("loc_A3B")


    #C0011
    ChrTalk(
        0xFE,
        (
            "之前接到了报告，港湾区\x01",
            "似乎发生了枪击事件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "听说好像是黑手党\x01",
            "之间的争斗……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "今天比平时增加了\x01",
            "更多的警备力量哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_ABF")

    Jump("loc_155C")

    label("loc_AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B3E")

    #C0014
    ChrTalk(
        0xFE,
        "好像聊得莫名地很起劲呢。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "从打扮来看，似乎像是个游手好闲的家伙，\x01",
            "……但却是总裁的熟人吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAB")

    label("loc_B3E")


    #C0016
    ChrTalk(
        0xFE,
        (
            "库罗伊斯总裁回来了呢，\x01",
            "我像往常一样走上前迎接……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "嗯～那个年轻人到底是谁呢？\x01",
            "是总裁的熟人吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_BAB")

    Jump("loc_155C")

    label("loc_BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_CAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C2A")

    #C0018
    ChrTalk(
        0xFE,
        (
            "顺便一说，总裁去国外出差了，\x01",
            "玛丽亚贝尔小姐\x01",
            "也出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "说是在行政区那边\x01",
            "有些事情要处理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA8")

    label("loc_C2A")


    #C0020
    ChrTalk(
        0xFE,
        (
            "哎呀，是客人吗？\x01",
            "不好意思，今天是银行的休业日哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "从原则上说，除了相关人员之外，\x01",
            "都是禁止入内的。\x01",
            "呵，请谅解啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_CA8")

    Jump("loc_155C")

    label("loc_CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_E18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D4D")

    #C0022
    ChrTalk(
        0xFE,
        (
            "听说，好像有人通过导力网络的线路\x01",
            "进行了入侵啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "哎呀呀，那可是我们的警备范围之外啊。\x01",
            "技术部的那些家伙们\x01",
            "必须要再努力些才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E13")

    label("loc_D4D")


    #C0024
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ总部大楼的\x01",
            "警备体制没有任何问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "因为我们保安部门的人\x01",
            "二十四小时都在值班哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "可是……像黑客这种我们不太了解\x01",
            "的东西，可就没法防范了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "哎呀呀，这就在警备范围之外了啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E13")

    Jump("loc_155C")

    label("loc_E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_EEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E71")

    #C0028
    ChrTalk(
        0xFE,
        "有事情要办的话就请去里面。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "大厅的正面有综合接待柜台哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EEA")

    label("loc_E71")

    SetScenarioFlags(0x0, 0)

    #C0030
    ChrTalk(
        0xFE,
        (
            "您好，\x01",
            "今天也是个好天气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "这里与市区有一定距离，\x01",
            "早上的空气非常清新。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "能让人精神十足，努力一整天啊。\x02",
    )

    CloseMessageWindow()

    label("loc_EEA")

    Jump("loc_155C")

    label("loc_EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_FCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F4F")

    #C0033
    ChrTalk(
        0xFE,
        (
            "我们警备员\x01",
            "绝不干涉顾客的私事。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        "……这也是处于保安方面的考虑。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FC6")

    label("loc_F4F")


    #C0035
    ChrTalk(
        0xFE,
        (
            "今天有一位\x01",
            "非常沮丧的客人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "大概是做生意失败了吧。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "……算啦，我毕竟是警备员。\x01",
            "总不能去和他搭话啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_FC6")

    Jump("loc_155C")

    label("loc_FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_10E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_104A")

    #C0038
    ChrTalk(
        0xFE,
        (
            "迎接库罗伊斯总裁\x01",
            "是我的任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "顺便一说，在市内活动的时候，\x01",
            "总裁都会驾驶他那辆红色的豪华轿车。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E1")

    label("loc_104A")


    #C0040
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ集团的首席人物\x01",
            "库罗伊斯总裁是个\x01",
            "非常忙碌的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "平时总是飞往国外，\x01",
            "难得回来一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "当他偶尔回来时，\x01",
            "就必须充满诚意地去迎接呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10E1")

    Jump("loc_155C")

    label("loc_10E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1182")

    #C0043
    ChrTalk(
        0xFE,
        (
            "这里地势很高，视野非常好，\x01",
            "很适合进行警备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "真是个毫无缺陷的工作地点啊，\x01",
            "而在大厦内工作的职员们\x01",
            "也都很中意这个地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1261")

    label("loc_1182")


    #C0045
    ChrTalk(
        0xFE,
        (
            "我经常这么想，\x01",
            "ＩＢＣ的建造地点真不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "可以对市内一览无余的高层建筑，\x01",
            "以及缓缓流淌的河水。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "附近的绿化工作也做得很好，\x01",
            "真是个毫无缺陷的工作地点呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "这里的视野非常不错，\x01",
            "所以保安方面的安全性也很高。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1261")

    Jump("loc_155C")

    label("loc_1266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_138C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12E7")

    #C0049
    ChrTalk(
        0xFE,
        (
            "对了对了，当年正好赶上了\x01",
            "五年一度的市长选举。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "对当时还身为新人的我来说，\x01",
            "真是非常忙碌的一年啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1387")

    label("loc_12E7")


    #C0051
    ChrTalk(
        0xFE,
        (
            "从我被安排到保安部门算起，\x01",
            "到现在都已经十年了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "当时这幢大楼正好刚竣工，\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "那年真是忙得不得了呢。\x01",
            "到任之后，立刻就要开始\x01",
            "向总部大楼转移的工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1387")

    Jump("loc_155C")

    label("loc_138C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_148D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13E4")

    #C0054
    ChrTalk(
        0xFE,
        (
            "欢迎光临ＩＢＣ总部大楼。\x01",
            "有什么要事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "请您随意吩咐。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1488")

    label("loc_13E4")


    #C0056
    ChrTalk(
        0xFE,
        (
            "您好，\x01",
            "欢迎光临ＩＢＣ总部大楼。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "哈哈，吃了一惊吗？\x01",
            "这确实是座气派的大楼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "初次来访的人大多都会很惊讶的。\x01",
            "不过，要是在这里工作，很快就会习惯的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1488")

    Jump("loc_155C")

    label("loc_148D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14EB")

    #C0059
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ今天\x01",
            "暂停营业。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "从原则上说，除了相关人员之外，\x01",
            "都是禁止入内的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155C")

    label("loc_14EB")


    #C0061
    ChrTalk(
        0xFE,
        "您好，今天的天气真不错啊。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ今天\x01",
            "暂停营业。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "如果是来取钱的，那可就不巧啦。\x01",
            "请以后再来吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_155C")

    TalkEnd(0xFE)
    Return()

    # Function_3_813 end

    def Function_4_1560(): pass

    label("Function_4_1560")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_15B4")

    #C0064
    ChrTalk(
        0xFE,
        (
            "我正在检查\x01",
            "大门的门锁呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        "不好意思，能不能不要打扰我呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_160D")

    label("loc_15B4")


    #C0066
    ChrTalk(
        0xFE,
        "哎呀，已经到关门时间了。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "客人也都已经回去了。\x01",
            "如果想取钱，\x01",
            "就请明天再来吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_160D")

    TalkEnd(0xFE)
    Return()

    # Function_4_1560 end

    def Function_5_1611(): pass

    label("Function_5_1611")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_180C")
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)

    #N0068
    NpcTalk(
        0xC,
        "男性的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#N#2S哈哈哈……\x01",
            "你所说的话令人兴趣颇深呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0069
    NpcTalk(
        0xC,
        "男性的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#N#2S呀，正是如此！\x01",
            "真没想到，竟能在克洛斯贝尔\x01",
            "遇到像你这样的人物啊……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("青年的声音")
    SetMessageWindowPos(240, 150, -1, -1)

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S哪里哪里，大叔你也很了不起嘛。\x02",
        )
    )

    CloseMessageWindow()

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S我看你远不止是一个\x01",
            "普通的银行家，\x01",
            "我也必须要向你多多学习呢⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0072
    ChrTalk(
        0x101,
        (
            "#0005F这是……\x01",
            "迪塔总裁的轿车吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#0105F他好像正在说些什么呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_180C")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "查看情况\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185E")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("e0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_186B")

    label("loc_185E")

    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_186B")

    Return()

    # Function_5_1611 end

    def Function_6_186C(): pass

    label("Function_6_186C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1020, 2500, -560, 0)
    MoveCamera(45, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, 1020, 0, -560, 135)
    SetChrPos(0x1, 1020, 0, -560, 135)
    SetChrPos(0x2, 1020, 0, -560, 135)
    SetChrPos(0x3, 1020, 0, -560, 135)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_6_186C end

    def Function_7_18F7(): pass

    label("Function_7_18F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, -970, 0, -25140, 0)
    SetChrPos(0x102, 630, 0, -25140, 0)
    SetChrPos(0x103, 630, 0, -26970, 0)
    SetChrPos(0x104, -970, 0, -26970, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-3130, 2500, -17030, 0)
    MoveCamera(48, 16, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21000, 0)
    FadeToBright(1000, 0)
    OP_68(-140, 4630, 2210, 8000)
    MoveCamera(24, 23, 0, 8000)
    OP_6E(750, 8000)
    SetCameraDistance(39300, 8000)
    PlaceName2(340, 200, "c_plac06", 0x0, 4000)
    OP_6F(0x79)
    Sleep(1000)

    #A0074
    AnonymousTalk(
        0x101,
        (
            "#0000F这里是……那个\x01",
            "ＩＢＣ总部所在的大楼啊。\x02",
        )
    )

    CloseMessageWindow()

    #A0075
    AnonymousTalk(
        0x102,
        (
            "#0104F克洛斯贝尔国际银行\x01",
            "（International Bank of Crossbell）……\x02\x03",

            "拥有数处分行的巨大银行，\x01",
            "开展着广泛事业的一大集团。\x02\x03",

            "#0102F在十年前，其总资产额\x01",
            "就已经达到了大陆第一……\x01",
            "现在已经是克洛斯贝尔的实质性支柱了呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0076
    AnonymousTalk(
        0x103,
        (
            "#0200F嗯，特别是在\x01",
            "金融、建设、不动产业界，\x01",
            "可以算得上是必不可少的存在了。\x02\x03",

            "#0203F目前正在克洛斯贝尔推行\x01",
            "大规模的公共事业计划……\x02\x03",

            "据说，在地下空间，还有导力网络的整备等方面，\x01",
            "ＩＢＣ也都投入了不少资产呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0077
    AnonymousTalk(
        0x104,
        (
            "#0305F呼～……\x01",
            "总觉得，这种地方跟我大概一生无缘啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-1890, 2500, -27740, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(10800, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    TurnDirection(0x103, 0x104, 500)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    #C0078
    ChrTalk(
        0x103,
        (
            "#0200F#11P……那个，兰迪前辈。\x01",
            "我们的薪水也都是通过\x01",
            "ＩＢＣ进行发放的哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0079
    ChrTalk(
        0x104,
        "#0301F#6P什么……还有这种事啊！？\x02",
    )

    CloseMessageWindow()

    def lambda_1D0A():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D0A)
    Sleep(50)
    TurnDirection(0x101, 0x103, 500)

    #C0080
    ChrTalk(
        0x101,
        (
            "#0000F#5P如果是在克洛斯贝尔市内，\x01",
            "还是用那种方式更加便利哦。\x02\x03",

            "#0006F不过……\x01",
            "今天好像是暂停营业呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        (
            "#0104F#11P呵呵，因为周末是银行的休业日啊……\x02\x03",

            "#0100F下次有机会时\x01",
            "再来拜访吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -970, 0, -25140, 0)
    SetScenarioFlags(0x47, 4)
    EventEnd(0x5)
    Return()

    # Function_7_18F7 end

    def Function_8_1DF0(): pass

    label("Function_8_1DF0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02300.itc", 0x1E)
    LoadChrToIndex("chr/ch06000.itc", 0x1F)
    OP_68(0, -1000, -34200, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15000, 0)
    OP_90(0x101, -650, -1700, -37200, 0)
    OP_90(0x102, 650, -1700, -37200, 0)
    OP_90(0x103, -1200, -1900, -38400, 0)
    OP_90(0x104, 1200, -1900, -38400, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 0, -10500, 180)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 0, 0, -12500, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02600.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    ClearMapFlags(0x10000000)

    def lambda_1F20():
        OP_96(0xFE, 0xFFFFFD76, 0x0, 0xFFFF9D90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F20)
    Sleep(200)

    def lambda_1F3D():
        OP_96(0xFE, 0x28A, 0x0, 0xFFFF9D90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F3D)
    Sleep(100)

    def lambda_1F5A():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0xFFFF98E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F5A)
    Sleep(200)

    def lambda_1F77():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFF98E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F77)
    OP_68(0, 4700, -17700, 8000)
    MoveCamera(0, -9, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(13000, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x41)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2089")

    #C0082
    ChrTalk(
        0x104,
        (
            "#0305F这里就是ＩＢＣ大厦吗……\x02\x03",

            "#0302F从近处看来，\x01",
            "还真是个很壮观的建筑呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        (
            "#0204F……是啊。\x02\x03",

            "#0202F设备如此先进的大楼，\x01",
            "在全大陆中或许也不多见呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x53, 2)
    Jump("loc_20C4")

    label("loc_2089")


    #C0084
    ChrTalk(
        0x104,
        (
            "#0302FＩＢＣ大楼吗……\x01",
            "不管看多少次，都感觉很壮观呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C4")


    #C0085
    ChrTalk(
        0x101,
        (
            "#0002F#5P粗略一看的话……\x01",
            "好像最少有十层以上的高度呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        (
            "#0104F#11P这里应该有十六层。\x02\x03",

            "#0100F其中，从五层到十层\x01",
            "好像都是外部的公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#0000F#5P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        (
            "#0204F他们对克洛斯贝尔的税收\x01",
            "应该有相当大的贡献吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1000, -25800, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0089
    ChrTalk(
        0x101,
        (
            "#6P#0001F那么，我们接下来该怎么办？\x02\x03",

            "没有经过预约\x01",
            "就直接来了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    #C0090
    ChrTalk(
        0x102,
        (
            "#11P#0101F也是啊，那就先去\x01",
            "问问里面的接待员吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    #N0091
    NpcTalk(
        0xA,
        "男性的声音",
        "艾莉……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_22E6():
        OP_95(0xFE, 0, 0, -22600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_22E6)
    Sleep(1000)

    def lambda_2303():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2303)

    def lambda_2310():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2310)
    OP_68(0, 1000, -24000, 3000)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)

    #C0092
    ChrTalk(
        0x102,
        "#0105F阿奈斯特先生……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0093
    AnonymousTalk(
        0xA,
        (
            "好巧呢……\x01",
            "竟然会在这里碰面。\x02\x03",

            "各位会一起过来，\x01",
            "看来是为了工作而来的吧？\x02",
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

    #C0094
    ChrTalk(
        0x102,
        (
            "#0104F嗯……\x01",
            "稍微有些事情需要调查。\x02\x03",

            "#0100F阿奈斯特先生是来帮\x01",
            "外公处理什么事情的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "#2604F#5P嗯，关于事务所运营资金\x01",
            "的管理问题，来这里进行了一下商谈。\x02\x03",

            "#2600F从下个月开始就会特别忙了，\x01",
            "到时就真的会分身乏术了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        "#0108F……是吗。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        (
            "#2603F#5P还有，艾莉……\x02\x03",

            "#2601F你之后有没有稍微考虑过一下？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#0103F…………考虑过了。\x02\x03",

            "#0101F我目前果然还是无法\x01",
            "辞去警察的工作。\x02\x03",

            "如今，我还没有抓住任何东西……\x02\x03",

            "在真正把握住自己所追求的东西之前，\x01",
            "我仍然只是半桶水而已。\x02\x03",

            "#0103F像这种状态的我，恐怕\x01",
            "反而只会给外公拖后腿吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "#2605F#5P可是……\x02\x03",

            "#2601F你所追求的东西，\x01",
            "真的在这条道路的前方吗？\x02\x03",

            "说不定，你现在所看到的东西，\x01",
            "仅仅是虚幻的海市蜃楼而已啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#0106F或许真是那样吧。\x02\x03",

            "#0102F可是，在这两个月中……\x01",
            "我觉得自己已经开始看清许多事情。\x02\x03",

            "将众多问题逐个解决，在此\x01",
            "过程中，我确实感到了自己在逐步成长。\x02\x03",

            "#0109F如果当时就那样直接进入事务所，\x01",
            "成为外公的一名秘书，那多半\x01",
            "便得不到这种宝贵的经验了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        "#2605F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#0104F……所以，很抱歉。\x02\x03",

            "#0100F至少，在我能够真正独当一面之前……\x01",
            "还是想在如今的位置上继续努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "#2606F#5P……呼。\x02\x03",

            "#2600F看起来，你的迷惘好像已经打消了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        "#0105F哎……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "#2600F#5P明白了，关于这个问题，我以后再也不会多言了。\x02\x03",

            "#2604F唉，本以为事务所难得\x01",
            "可以增添一名能干的后辈呢。\x02\x03",

            "看起来，期待好像彻底落空了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        "#0102F阿奈斯特先生……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "#2603F#5P只是，对了……\x02\x03",

            "#2600F在下个月的创立纪念庆典时，\x01",
            "希望你一定要来参加仪式。\x02\x03",

            "本来是想让你的母亲\x01",
            "前来出席的，可是……\x02\x03",

            "总之，如果市长的家人中连一个\x01",
            "出席者也没有，那他未免也太寂寞了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#0104F……我明白了。\x02\x03",

            "#0100F阿奈斯特先生。\x01",
            "长期以来，真是承蒙你各方面的关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        (
            "#2604F#5P哈哈，哪里的话，再怎么说，\x01",
            "我曾经也当过你的老师嘛。\x02\x03",

            "#2600F这点小事就不必太放在心上啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0110
    ChrTalk(
        0xA,
        (
            "#2605F#5P啊，不知不觉就在\x01",
            "这种地方耗去了不少时间呢。\x02\x03",

            "#2604F支援科的各位，你们也请努力工作哦。\x02\x03",

            "#2600F还有……\x01",
            "艾莉小姐就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#12P#0002F……好的。\x02",
    )

    CloseMessageWindow()

    def lambda_2B52():

        label("loc_2B52")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_2B52")

    QueueWorkItem2(0x101, 2, lambda_2B52)

    def lambda_2B64():

        label("loc_2B64")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_2B64")

    QueueWorkItem2(0x102, 2, lambda_2B64)

    def lambda_2B76():
        OP_95(0xFE, -1900, 0, -24200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2B76)
    Sleep(500)

    def lambda_2B93():

        label("loc_2B93")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_2B93")

    QueueWorkItem2(0x104, 2, lambda_2B93)

    def lambda_2BA5():

        label("loc_2BA5")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_2BA5")

    QueueWorkItem2(0x103, 2, lambda_2BA5)
    WaitChrThread(0xA, 1)
    OP_68(0, 1000, -27000, 3000)

    def lambda_2BCC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD120, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2BCC)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)
    EndChrThread(0x101, 0x2)

    def lambda_2BF0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2BF0)
    Sleep(50)
    EndChrThread(0x102, 0x2)

    def lambda_2C04():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2C04)
    EndChrThread(0x103, 0x2)

    def lambda_2C15():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2C15)
    Sleep(50)
    EndChrThread(0x104, 0x2)

    def lambda_2C29():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2C29)
    WaitChrThread(0x104, 2)
    ClearChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    #C0112
    ChrTalk(
        0x102,
        "#5P#0108F………………………………\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, -25800, 1000)

    def lambda_2C81():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C81)
    Sleep(150)

    def lambda_2C91():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2C91)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)
    OP_6F(0x1)

    #C0113
    ChrTalk(
        0x101,
        (
            "#6P#0000F真是个处处都为\x01",
            "艾莉考虑的人呢。\x02\x03",

            "他说，以前当过你的老师……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(150)

    #C0114
    ChrTalk(
        0x102,
        (
            "#5P#0102F嗯……在我小时候，\x01",
            "曾经做过我的家庭教师。\x02\x03",

            "#0104F不过，自从我去留学之后，彼此间的关系\x01",
            "就变得稍微有些疏远了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#6P#0200F……他显然还是希望\x01",
            "成为一名政治家吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        (
            "#5P#0100F嗯，在明年的议员竞选中，\x01",
            "他好像会以新人的身份出马呢。\x02\x03",

            "#0108F好像既不打算从属于帝国派，\x01",
            "也不打算从属于共和国派，\x01",
            "我想，那肯定会相当艰辛吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        (
            "#12P#0303F未来的政治家吗？\x02\x03",

            "#0300F不过，就政治家的秘书来说，\x01",
            "他的体格还真是相当结实啊。\x02\x03",

            "好像也学习过武术吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#5P#0105F他好像练习过剑术哦。\x02\x03",

            "#0100F而且听说实力相当不错，\x01",
            "所以以前好像兼任过\x01",
            "外公的护卫工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#6P#0000F原来如此……\x01",
            "这就可以解释他的体格为何相对健壮了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)

    #N0120
    NpcTalk(
        0xB,
        "女性的声音",
        "哎呀哎呀～？\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_2FDD():
        OP_95(0xFE, 0, 0, -22600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2FDD)
    Sleep(1000)
    OP_68(0, 1000, -24000, 3000)

    def lambda_300B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_300B)
    Sleep(50)

    def lambda_301B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_301B)
    Sleep(50)

    def lambda_302B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_302B)
    Sleep(50)

    def lambda_303B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_303B)
    WaitChrThread(0xB, 1)
    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 3)), scpexpr(EXPR_END)), "loc_3153")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0121
    AnonymousTalk(
        0xB,
        "呵呵，又见面了呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0122
    ChrTalk(
        0x101,
        "#12P#0005F格蕾丝小姐……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "#2105F#5P怎么，你们来ＩＢＣ有什么事吗？\x02\x03",

            "#2102F这么多人一起过来，\x01",
            "难道是来进行什么调查的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3426")

    label("loc_3153")

    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0124
    AnonymousTalk(
        0xB,
        (
            "呀～真是好久不见了。\x02\x03",

            "关于上个月那起魔兽骚乱事件的报道，\x01",
            "我已经读过了哦。\x02\x03",

            "嗯嗯，\x01",
            "看来你们很努力呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0125
    ChrTalk(
        0x101,
        "#12P#0005F格蕾丝小姐……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#0100F说起来，那篇报道好像\x01",
            "不是格蕾丝小姐写的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        (
            "#2106F#5P嗯，我当时要外出采访，\x01",
            "所以不在克洛斯贝尔哦。\x02\x03",

            "#2102F如果可以的话，倒是\x01",
            "真希望由我来采访你们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        "#12P#0206F……没采访成也许是幸运呢。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        (
            "#0302F哈，如果总是给我们写那种报道，\x01",
            "实在是让人泄气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "#2104F#5P哎呀呀，我一直都在默默守护你们的成长，\x01",
            "如此深切的感情，你们怎么就不能体会呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0131
    ChrTalk(
        0xB,
        (
            "#2105F#5P话说回来……\x01",
            "你们来ＩＢＣ有什么事吗？\x02\x03",

            "#2102F这么多人一起过来，\x01",
            "难道是来进行什么调查的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3426")


    #C0132
    ChrTalk(
        0x101,
        (
            "#12P#0012F不、不是……\x01",
            "也没有什么大不了的事情啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        (
            "#0100F嗯，只是过来稍微\x01",
            "进行一些询问而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        (
            "#2101F#5P哼～……算啦，就这样吧。\x02\x03",

            "#2104F我现在也很忙，\x01",
            "这次就放过你们吧。\x02\x03",

            "#2110F那么，下次再见啦～！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34FD():

        label("loc_34FD")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_34FD")

    QueueWorkItem2(0x101, 2, lambda_34FD)

    def lambda_350F():

        label("loc_350F")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_350F")

    QueueWorkItem2(0x102, 2, lambda_350F)

    def lambda_3521():
        OP_95(0xFE, 1900, 0, -24200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3521)
    Sleep(500)

    def lambda_353E():

        label("loc_353E")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_353E")

    QueueWorkItem2(0x104, 2, lambda_353E)

    def lambda_3550():

        label("loc_3550")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_3550")

    QueueWorkItem2(0x103, 2, lambda_3550)
    WaitChrThread(0xB, 1)
    OP_68(0, 1000, -27000, 3000)

    def lambda_3577():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD120, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3577)
    WaitChrThread(0xB, 1)
    OP_6F(0x1)
    EndChrThread(0x104, 0x2)

    def lambda_359B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_359B)
    Sleep(50)
    EndChrThread(0x102, 0x2)

    def lambda_35AF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_35AF)
    EndChrThread(0x103, 0x2)

    def lambda_35C0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_35C0)
    Sleep(50)
    EndChrThread(0x101, 0x2)

    def lambda_35D4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35D4)
    WaitChrThread(0x101, 2)
    ClearChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_68(0, 1000, -25800, 1000)
    OP_6F(0x1)

    #C0135
    ChrTalk(
        0x104,
        (
            "#0306F#5P唉，这位姐姐一点都没有变，\x01",
            "还是那么旁若无人、自说自话。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x103,
        (
            "#6P#0200F不过，就格蕾丝小姐一贯的作风来说，\x01",
            "这次还真是放弃得干脆果断呢……\x02\x03",

            "她已经忙到那种程度了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        (
            "#5P#0100F呵呵，临近纪念庆典了，\x01",
            "她大概有很多采访工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#5P#0006F嗯～如果可能的话，真希望\x01",
            "她能放弃我们这边的报道呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(150)

    #C0139
    ChrTalk(
        0x101,
        (
            "#6P#0000F算了……\x01",
            "我们差不多也该进大厦了。\x02\x03",

            "必须去问问接待员，\x01",
            "能否与总裁会面呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_379A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_379A)
    Sleep(50)

    def lambda_37AA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_37AA)
    Sleep(50)

    def lambda_37BA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_37BA)
    Sleep(150)

    #C0140
    ChrTalk(
        0x102,
        "#11P#0102F嗯，我们走吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(0, 2500, -24000, 0)
    MoveCamera(45, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, 0, 0, -24000, 0)
    SetChrPos(0x1, 0, 0, -24000, 0)
    SetChrPos(0x2, 0, 0, -24000, 0)
    SetChrPos(0x3, 0, 0, -24000, 0)
    SetScenarioFlags(0x82, 1)
    OP_29(0x43, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_8_1DF0 end

    def Function_9_3877(): pass

    label("Function_9_3877")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1100, 10800, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29500, 0)
    SetChrPos(0x101, 0, 400, 8500, 180)
    SetChrPos(0x102, 700, 400, 8500, 180)
    SetChrPos(0x103, -700, 400, 8500, 180)
    SetChrPos(0x104, 0, 400, 8500, 180)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_68(0, 1100, 1800, 4000)
    MoveCamera(0, 25, 0, 4000)
    SetCameraDistance(19500, 4000)

    def lambda_397A():
        OP_96(0xFE, 0x0, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_397A)

    def lambda_3994():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3994)
    Sleep(500)

    def lambda_39A8():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_39A8)

    def lambda_39C2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_39C2)
    Sleep(400)

    def lambda_39D6():
        OP_96(0xFE, 0x384, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39D6)

    def lambda_39F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_39F0)
    Sleep(500)

    def lambda_3A04():
        OP_96(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A04)

    def lambda_3A1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A1E)
    Sleep(1500)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x104, 1)

    def lambda_3A51():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A51)
    WaitChrThread(0x103, 1)

    def lambda_3A62():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3A62)
    WaitChrThread(0x102, 1)

    def lambda_3A73():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3A73)
    WaitChrThread(0x101, 1)

    #C0141
    ChrTalk(
        0x101,
        (
            "#5P#0006F唉……\x02\x03",

            "得到了线索，虽然作为结果来说还不错，\x01",
            "但还真是身心俱疲呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        (
            "#6P#0309F哈哈，是啊。\x02\x03",

            "#0302F特别是罗伊德，还被\x01",
            "那位大小姐敌视了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#5P#0001F你还敢说，那都是谁造成的啊……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        (
            "#0202F话说回来，并非专业人士，却又如此\x01",
            "精通导力技术的人，可真是很罕见呢。\x02\x03",

            "玛丽亚贝尔小姐\x01",
            "好像并不是技术人员吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#0104F嗯，她的专业是经营方面。\x02\x03",

            "#0100F听说，她负责数种事业的运营，\x01",
            "可以说是叔叔的\x01",
            "左膀右臂呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(150)

    #C0146
    ChrTalk(
        0x101,
        (
            "#5P#0000F那可真是厉害啊……\x02\x03",

            "#0005F啊，莫非，她很想\x01",
            "把艾莉拉入伙吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        (
            "#0106F嗯、嗯……\x01",
            "我很感谢她的好意，但还是……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x104,
        (
            "#6P#0306F说起来，那位大叔\x01",
            "的气质也相当引人注目啊。\x02\x03",

            "#0301F而且突然就能开始\x01",
            "那么厉害的演说。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x103,
        (
            "#0203F而且……\x01",
            "内容让人非常感兴趣呢。\x02\x03",

            "#0201F人类是追求正义的生物吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#0104F从以前开始，他就经常\x01",
            "对我讲一些很有启迪性的话……\x02\x03",

            "#0100F今天的这番谈话，\x01",
            "似乎尤其值得我们好好思考一番呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#5P#0003F……是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)
    TurnDirection(0x101, 0x104, 500)

    #C0152
    ChrTalk(
        0x101,
        (
            "#0000F#5P──不管怎么说，如此一来，\x01",
            "我们已经掌握到需要的线索了。\x02\x03",

            "现在就去市政厅的接待处，\x01",
            "把地下空间的钥匙借来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x102,
        "#0102F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        "#6P#0302F那么，我们走吧。\x02",
    )

    CloseMessageWindow()

    def lambda_3EC5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3EC5)
    Sleep(100)

    def lambda_3ED5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3ED5)
    Sleep(50)

    def lambda_3EE5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3EE5)
    WaitChrThread(0x104, 2)
    OP_68(0, 1100, -4200, 3000)

    def lambda_3F07():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F07)
    Sleep(150)
    WaitChrThread(0x103, 2)

    def lambda_3F28():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3F28)
    Sleep(150)
    WaitChrThread(0x102, 2)

    def lambda_3F49():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F49)
    Sleep(150)

    def lambda_3F66():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F66)
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_6F(0x1)
    OP_93(0x101, 0x0, 0x12C)
    Fade(500)
    OP_68(0, 1100, -2200, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13000, 0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 2200, -2200, 1500)
    MoveCamera(0, 0, 0, 1500)
    OP_6F(0x41)
    Sleep(500)

    #C0155
    ChrTalk(
        0x101,
        (
            "#0001F#6P#N（……………………………………）\x02\x03",

            "#0003F（……『正义』吗……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x190)

    def lambda_4066():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4066)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x104, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x101, 0x1)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(0, 2500, -10000, 0)
    MoveCamera(45, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, 0, 0, -10000, 180)
    SetChrPos(0x1, 0, 0, -10000, 180)
    SetChrPos(0x2, 0, 0, -10000, 180)
    SetChrPos(0x3, 0, 0, -10000, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetScenarioFlags(0x83, 1)
    Sleep(10)
    PlayBGM("ed7102", 0)
    EventEnd(0x5)
    Return()

    # Function_9_3877 end

    def Function_10_4151(): pass

    label("Function_10_4151")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ｉ．Ｂ．Ｃ\x01",
            "International Bank of Crossbell\x01\x01",
            " 需要与大厦内各公司联系的客人，\x01",
            " 请到一层大厅的服务台，\x01",
            " 咨询接待人员。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_4151 end

    SaveToFile()

Try(main)
