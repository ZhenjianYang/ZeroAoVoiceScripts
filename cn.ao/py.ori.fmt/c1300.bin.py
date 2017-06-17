from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1300.bin",                # FileName
        "c1300",                    # MapName
        "c1300",                    # Location
        0x001B,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c1300", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 27, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1300",                  # 0
        "警备员比尔斯",           # 1
        "警备员",                 # 2
        "警官",                   # 3
        "警备员",                 # 4
        "警官",                   # 5
        "银",                     # 6
        "曹",                     # 7
        "刘",                     # 8
        "高级轿车",               # 9
        "中央广场",               # 10
        "西街",                   # 11
        "行政区",                 # 12
        "住宅街",                 # 13
        "欢乐街",                 # 14
        "东街",                   # 15
        "旧城区",                 # 16
        "港湾区",                 # 17
        "ＩＢＣ",                 # 18
        "站前街道",               # 19
        "后巷",                   # 20
        "乌尔斯拉间道",           # 21
        "东克洛斯贝尔街道",       # 22
        "西克洛斯贝尔街道",       # 23
        "玛因兹山道",             # 24
        "兰花塔",                 # 25
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch30000.itc",                   # 01
    ))

    DeclNpc(3910,    0,       5050,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(1500,    0,       500,     270,  389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(1500,    0,       3000,    270,  389,  0x1, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-3500,   0,       500,     90,   389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-3500,   0,       3000,    90,   389,  0x1, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 7,   0.0,                   7.300000190734863,     0.0,                   14.0625,               [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.6666666865348816,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -0.0,                  -4.866666793823242,    -0.0,                  1.0])

    DeclActor(7000,    0,       2300,    1200,    7000,    1700,    2300,    0x007C, 0,  8,  0x0000)

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
    PlaceName(-107.0, 0.0, 114.0, 0x0000, 0x0000, "兰花塔")
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

    ChipFrameInfo(1176, 0)                                       # 0

    ScpFunction((
        "Function_0_498",          # 00, 0
        "Function_1_548",          # 01, 1
        "Function_2_743",          # 02, 2
        "Function_3_8B5",          # 03, 3
        "Function_4_13DA",         # 04, 4
        "Function_5_1A3E",         # 05, 5
        "Function_6_2399",         # 06, 6
        "Function_7_23BF",         # 07, 7
        "Function_8_2434",         # 08, 8
    ))


    def Function_0_498(): pass

    label("Function_0_498")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4D0"),
        (1, "loc_4DC"),
        (2, "loc_4E8"),
        (3, "loc_4F4"),
        (4, "loc_500"),
        (5, "loc_50C"),
        (6, "loc_518"),
        (SWITCH_DEFAULT, "loc_524"),
    )


    label("loc_4D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_4DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_4E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_4F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_500")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_50C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_518")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_524")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_530")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_547")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_547")

    Return()

    # Function_0_498 end

    def Function_1_548(): pass

    label("Function_1_548")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F7")
    SetChrPos(0x0, -230, -1450, -33980, 0)
    SetChrPos(0x1, -230, -1450, -33980, 0)
    SetChrPos(0x2, -230, -1450, -33980, 0)
    SetChrPos(0x3, -230, -1450, -33980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CF")
    SetChrPos(0x4, -230, -1450, -33980, 0)
    SetChrPos(0x5, -230, -1450, -33980, 0)
    Jump("loc_5EE")

    label("loc_5CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EE")
    SetChrPos(0x4, -230, -1450, -33980, 0)

    label("loc_5EE")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F7")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_613")
    SetChrFlags(0x8, 0x80)
    Jump("loc_6D2")

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_626")
    SetChrFlags(0x8, 0x80)
    Jump("loc_6D2")

    label("loc_626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_634")
    Jump("loc_6D2")

    label("loc_634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_642")
    Jump("loc_6D2")

    label("loc_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_650")
    Jump("loc_6D2")

    label("loc_650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_65E")
    Jump("loc_6D2")

    label("loc_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_66C")
    Jump("loc_6D2")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_67A")
    Jump("loc_6D2")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6AD")
    SetChrPos(0x8, 1600, 0, -21430, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_6D2")

    label("loc_6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6BB")
    Jump("loc_6D2")

    label("loc_6BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6C9")
    Jump("loc_6D2")

    label("loc_6C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6D2")

    label("loc_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6E1")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)

    label("loc_6E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_717")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_742")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_742")

    Return()

    # Function_1_548 end

    def Function_2_743(): pass

    label("Function_2_743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7F8")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x95, 0xA0, 0xB5, 0xD, 0x19F, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_7F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_856")
    OP_78(0x2, 0x10)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -4990, 0, 2500, 180)
    OP_D5(0x10, 0x0, 0x2BF20, 0x0, 0x0)

    label("loc_856")

    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x14)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88A")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_88A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B4")
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)

    label("loc_8B4")

    Return()

    # Function_2_743 end

    def Function_3_8B5(): pass

    label("Function_3_8B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8C6")
    Jump("loc_13D6")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8D4")
    Jump("loc_13D6")

    label("loc_8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_947")

    #C0001
    ChrTalk(
        0xFE,
        (
            "占领玛因兹的那起事件……\x01",
            "果然是帝国在暗中策划的吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "……不管怎么说，必须要保持警戒啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13D6")

    label("loc_947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F8")

    #C0003
    ChrTalk(
        0xFE,
        (
            "早上好啊，特别任务支援科的各位。\x01",
            "虽然我们都得冒雨工作，\x01",
            "但今天一定要继续加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "听兰菲小姐说，\x01",
            "雨到下午就会停了。\x01",
            "在那之前，就忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A6D")

    label("loc_9F8")


    #C0005
    ChrTalk(
        0xFE,
        (
            "虽然我们都得冒雨工作，\x01",
            "但今天一定要继续加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "听兰菲小姐说，\x01",
            "雨到下午就会停了。\x01",
            "在那之前，就忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6D")

    Jump("loc_13D6")

    label("loc_A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEA")

    #C0007
    ChrTalk(
        0xFE,
        (
            "唔，那么小的孩子\x01",
            "竟然一个人来我们这里，\x01",
            "真是很少见呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "大概是来找大楼内的\x01",
            "家人吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B4C")

    label("loc_AEA")


    #C0009
    ChrTalk(
        0xFE,
        (
            "哦哦，真是不应该。\x01",
            "我竟然会随便\x01",
            "谈论客人的私事。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "身为保安部门的人员，必须要慎言才行啊。\x02",
    )

    CloseMessageWindow()

    label("loc_B4C")

    Jump("loc_13D6")

    label("loc_B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BD2")

    #C0011
    ChrTalk(
        0xFE,
        (
            "早上好，今天早上的天气\x01",
            "真不错啊，让人心情愉快。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "这个地方的视野\x01",
            "总是这么好，\x01",
            "空气也非常清新，真是太棒了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D6")

    label("loc_BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C74")

    #C0013
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔是否应该\x01",
            "独立为自主国家……\x01",
            "这真是个相当深刻的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "这个问题必定也会关系到\x01",
            "ＩＢＣ的发展……\x01",
            "但我实在是考虑不到太细致的方面。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D6")

    label("loc_C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E74")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D84")

    #C0015
    ChrTalk(
        0xFE,
        (
            "我昨天在近距离\x01",
            "观望到了来ＩＢＣ\x01",
            "访问的洛克史密斯总统……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "身为管理着那种\x01",
            "超级大国的领袖，\x01",
            "他的气场果然非同寻常呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "从外表来看，也许与普通人没什么不同，\x01",
            "但该怎么说才好呢……从他的身上可以\x01",
            "清晰地感觉到一股很强的威严感。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DED")

    label("loc_D84")


    #C0018
    ChrTalk(
        0xFE,
        (
            "说起来，听说今天早上\x01",
            "有可疑人员入侵ＩＢＣ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "但我当时并没有\x01",
            "察觉到任何异常……\x01",
            "真是很受打击呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DED")

    Jump("loc_E6F")

    label("loc_DF2")


    #C0020
    ChrTalk(
        0xFE,
        (
            "传闻果然没错，那个怪盗Ｂ\x01",
            "的确是个相当古怪的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "竟然把盗走的东西\x01",
            "分别放置在自治州各地……\x01",
            "他到底有什么企图呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6F")

    Jump("loc_13D6")

    label("loc_E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1046")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF1")

    #C0022
    ChrTalk(
        0xFE,
        (
            "哦，是你们啊。\x01",
            "真不好意思，\x01",
            "ＩＢＣ今天停业休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "其实主要还是因为\x01",
            "洛克史密斯总统\x01",
            "正在里面考察。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "如果你们有什么事情，\x01",
            "不妨明天再来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 7)), scpexpr(EXPR_END)), "loc_F69")

    #C0025
    ChrTalk(
        0x101,
        (
            "#00005F总统来视察吗……\x02\x03",

            "#00003F兰菲小姐昨天\x01",
            "好像也说过呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F86")

    label("loc_F69")


    #C0026
    ChrTalk(
        0x101,
        "#00005F总统来视察吗……\x02",
    )

    CloseMessageWindow()

    label("loc_F86")


    #C0027
    ChrTalk(
        0x104,
        (
            "#00300F呼，警戒工作\x01",
            "真是相当严格。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#00100F是啊，\x01",
            "我们就别在这里碍事了，\x01",
            "还是尽快离开吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1041")

    label("loc_FF1")


    #C0029
    ChrTalk(
        0xFE,
        (
            "真不好意思，\x01",
            "ＩＢＣ今天停业休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "如果你们有什么事情，\x01",
            "不妨明天再来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1041")

    Jump("loc_13D6")

    label("loc_1046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10B7")

    #C0031
    ChrTalk(
        0xFE,
        "通商会议终于要在明天正式召开了。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "市内已经提高了警备力度，\x01",
            "我们保安部门自然也要拿出干劲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D6")

    label("loc_10B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_12D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D9")

    #C0033
    ChrTalk(
        0xFE,
        (
            "我刚刚看到了\x01",
            "库罗伊斯总裁……\x01",
            "不，库罗伊斯市长。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "市长平时基本都在新市政厅大楼，\x01",
            "但偶尔也会\x01",
            "到这里露个面。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……话说回来，库罗伊斯市长身兼两项\x01",
            "如此重要的职务，真是令人难以想象。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "而且他还能将这\x01",
            "两项事务都完美处理好，\x01",
            "真是让人佩服不已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_127D")

    label("loc_11D9")


    #C0037
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市长和ＩＢＣ总裁……\x01",
            "仔细想想，库罗伊斯市长身兼两项\x01",
            "如此重要的职务，真是令人难以想象。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "而且他还能将这\x01",
            "两项事务都完美处理好，\x01",
            "真是让人佩服不已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_127D")

    Jump("loc_12D3")

    label("loc_1282")


    #C0039
    ChrTalk(
        0xFE,
        (
            "库罗伊斯市长已经\x01",
            "匆匆赶回新市政厅大楼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "他做事还是和以往一样迅速呢。\x02",
    )

    CloseMessageWindow()

    label("loc_12D3")

    Jump("loc_13D6")

    label("loc_12D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_13D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1377")

    #C0041
    ChrTalk(
        0xFE,
        (
            "您好，欢迎光临\x01",
            "ＩＢＣ总部大楼。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        "如果有什么事情，请去接待处咨询。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ引以为傲的接待小姐一定会\x01",
            "耐心诚挚地为您服务。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13D6")

    label("loc_1377")


    #C0044
    ChrTalk(
        0xFE,
        "如果有什么事情，请去接待处咨询。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ引以为傲的接待小姐一定会\x01",
            "耐心诚挚地为您服务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D6")

    TalkEnd(0xFE)
    Return()

    # Function_3_8B5 end

    def Function_4_13DA(): pass

    label("Function_4_13DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00500.itc", 0x1E)
    LoadChrToIndex("chr/ch06300.itc", 0x1F)
    LoadChrToIndex("chr/ch31400.itc", 0x20)
    LoadChrToIndex("apl/ch50237.itc", 0x21)
    LoadEffect(0x0, "event\\ev202_00.eff")
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 8000, -7000, -74600, 310)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 8000, -7000, -72500, 310)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 9300, -7000, -73300, 310)
    VolumeBGM(0x5A, 0x3E8)
    OP_68(8000, -5900, -73200, 0)
    MoveCamera(57, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_68(8000, -5900, -73200, 5000)
    MoveCamera(81, 15, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(25000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(8000, -5900, -73200, 0)
    MoveCamera(64, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14730, 0)
    OP_0D()
    Sleep(500)

    #C0046
    ChrTalk(
        0xF,
        "#11P……真了不起啊。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xE,
        (
            "#03209F#11P呵呵，好漂亮。\x02\x03",

            "#03210F单是能欣赏到如此盛况，\x01",
            "都不枉特意来\x01",
            "克洛斯贝尔走一遭。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(100)
    Sound(2628, 255, 100, 0)    #voice#Yin
    Sleep(800)

    #C0048
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#00702F……装模作样的家伙。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0xC8, 0x1F4)
    Sleep(200)

    #C0049
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00700F好了，我要走了。\x02\x03",

            "似乎有奇怪的老鼠\x01",
            "混了进来。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_164C():
        TurnDirection(0xE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_164C)
    Sleep(50)

    def lambda_165C():
        TurnDirection(0xF, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_165C)
    Sleep(50)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    #C0050
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#03204F#5P嗯，那就拜托您了。\x02\x03",

            "#03200F另外，在明天的行动中，\x01",
            "请务必助我们一臂之力哦。\x02\x03",

            "您只要肯赏光前来，\x01",
            "我们便会面上有光呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702F哼，知道了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2614, 255, 100, 0)    #voice#Yin
    Sleep(1200)
    Sound(341, 0, 100, 0)
    OP_68(8119, -5900, -73810, 1000)
    PlayEffect(0x0, 0xFF, 0xD, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0xD, 0x1E, 0x12C)

    def lambda_1779():
        OP_93(0xFE, 0xD2, 0xC8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1779)

    def lambda_1786():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1786)

    def lambda_17A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_17A0)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xD, 2)
    SetChrChip(0x1, 0xD, 0x0, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    Sleep(1000)

    #C0052
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P呼……\x01",
            "还是和以前一样神出鬼没啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xF,
        (
            "#5P要是能改掉这种反复无常\x01",
            "的怪脾气就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xE,
        (
            "#03204F#5P呵呵，不对，恐怕并不是\x01",
            "什么反复无常，情绪善变呢。\x02\x03",

            "#03200F他协助我们的时间\x01",
            "似乎存在着一个特定规律……\x02\x03",

            "只要遵循那个规律来提出要求，\x01",
            "就基本不会遭到拒绝。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(100)

    #C0055
    ChrTalk(
        0xF,
        "#11P真、真的吗？\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xF,
        "#11P那规律究竟是……？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xE,
        "#03209F#5P呵呵，暂且保密。\x02",
    )

    CloseMessageWindow()
    OP_68(7440, -5600, -71690, 1500)
    MoveCamera(71, 11, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(14250, 1500)
    OP_93(0xE, 0x136, 0x190)
    OP_6F(0x79)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    Sleep(130)
    SetChrSubChip(0xE, 0x1)
    Sleep(130)
    SetChrSubChip(0xE, 0x2)
    Sleep(130)
    Sound(318, 0, 100, 0)
    SetChrSubChip(0xE, 0x3)
    Sleep(500)

    #C0058
    ChrTalk(
        0xE,
        (
            "#03204F#11P至今为止，事态一直都在按照我的计划发展。\x02\x03",

            "#03202F为了确保明日的行动顺利成功，\x01",
            "我们还要再加把劲。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)
    OP_82(0x1E, 0x0, 0x7D0, 0xC8)

    #C0059
    ChrTalk(
        0xF,
        "#11P是！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14750, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 1)
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_13DA end

    def Function_5_1A3E(): pass

    label("Function_5_1A3E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-10630, 5300, -20350, 0)
    MoveCamera(24, -8, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(15210, 0)
    OP_68(-8590, 7900, -25570, 10000)
    MoveCamera(23, -1, 0, 10000)
    OP_6E(750, 10000)
    SetCameraDistance(27170, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1B73")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x104, 950, -1090, -32509, 0)

    def lambda_1B05():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1B05)

    def lambda_1B1F():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B1F)
    Sleep(100)

    def lambda_1B3C():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B3C)
    Sleep(50)

    def lambda_1B59():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B59)
    Jump("loc_1CEE")

    label("loc_1B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1C33")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x109, 950, -1090, -32509, 0)

    def lambda_1BC5():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1BC5)

    def lambda_1BDF():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BDF)
    Sleep(100)

    def lambda_1BFC():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BFC)
    Sleep(50)

    def lambda_1C19():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1C19)
    Jump("loc_1CEE")

    label("loc_1C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1CEE")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x105, 950, -1090, -32509, 0)

    def lambda_1C85():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1C85)

    def lambda_1C9F():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C9F)
    Sleep(100)

    def lambda_1CBC():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CBC)
    Sleep(50)

    def lambda_1CD9():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1CD9)

    label("loc_1CEE")

    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-1300, 1910, -24540, 0)
    MoveCamera(48, 25, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(10770, 0)
    OP_0D()

    #C0060
    ChrTalk(
        0x1A2,
        (
            "#5PＩＢＣ……\x01",
            "嗯，还是和以前一样雄伟呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0061
    ChrTalk(
        0x102,
        "#11P#00105F秦，你不是第一次来这里吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0062
    ChrTalk(
        0x1A2,
        (
            "#6P嗯，我们黑月自然\x01",
            "也在ＩＢＣ开办了帐户。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x1A2,
        (
            "#6P顺便一说，我最近还\x01",
            "开办了自己的个人帐户，\x01",
            "开始炒股了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x1A2,
        "#6P等拿到这次的分红之后，如果可以……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0065
    ChrTalk(
        0x101,
        (
            "#12P#00000F对了，艾莉在学生时代\x01",
            "炒过股吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0066
    ChrTalk(
        0x102,
        (
            "#5P#00100F嗯，为了了解这方面的知识，\x01",
            "稍微尝试过一点点。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0067
    ChrTalk(
        0x1A2,
        (
            "#6P艾莉姐竟然也\x01",
            "炒过股啊——！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0068
    ChrTalk(
        0x1A2,
        (
            "#6P对了，我最近发现了\x01",
            "一支很不错的股票。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x1A2,
        (
            "#6P它的涨幅相当稳定，而且很有潜力，\x01",
            "最重要的是，关注它的人还不是很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x1A2,
        (
            "#6P哦，除此之外，\x01",
            "还有几支股票值得推荐……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x1A2, 0, 0, 6)
    Sleep(800)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0071
    ChrTalk(
        0x102,
        "#11P#00105F那、那个……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_206E")
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0072
    ChrTalk(
        0x101,
        "#12P#00012F（我、我好像说了些多余的话吧……？）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0073
    ChrTalk(
        0x104,
        "#12P#00306F（……没错。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2159")

    label("loc_206E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_20E8")
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0074
    ChrTalk(
        0x101,
        "#12P#00012F（我、我好像说了些多余的话吧……？）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0075
    ChrTalk(
        0x109,
        "#12P#10106F（……我想是的。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2159")

    label("loc_20E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2159")
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0076
    ChrTalk(
        0x101,
        "#12P#00012F（我、我好像说了些多余的话吧……？）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0077
    ChrTalk(
        0x105,
        "#12P#10306F（……是的。）\x02",
    )

    CloseMessageWindow()

    label("loc_2159")

    EndChrThread(0x1A2, 0x0)
    OP_64(0x1A2)
    Sleep(500)
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0078
    ChrTalk(
        0x1A2,
        "#6P——啊！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x1A2,
        "#6P抱歉哦，艾莉姐。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x1A2,
        (
            "#6P因为找到了共同话题，太过激动了，\x01",
            "一时兴起就说个没完……\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1A2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2228")

    def lambda_2208():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2208)
    Sleep(50)

    def lambda_2218():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2218)
    Sleep(300)
    Jump("loc_227F")

    label("loc_2228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_2256")

    def lambda_2236():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2236)
    Sleep(50)

    def lambda_2246():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2246)
    Sleep(300)
    Jump("loc_227F")

    label("loc_2256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_227F")

    def lambda_2264():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2264)
    Sleep(50)

    def lambda_2274():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2274)
    Sleep(300)

    label("loc_227F")


    #C0081
    ChrTalk(
        0x102,
        (
            "#11P#00109F呵呵，不必介意哦，\x01",
            "我只是有点吃惊而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x1A2,
        (
            "#6P啊，艾莉姐……\x01",
            "你果然像女神一样温柔。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0083
    ChrTalk(
        0x1A2,
        (
            "#5P话说回来，只要我有需要，\x01",
            "随时都可以来这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x1A2,
        "#5P还是赶快带我去下一个地方吧。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#12P#00012F啊，好的……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C5, 2)
    OP_29(0x73, 0x1, 0x4)
    OP_1B(0x1, 0x0, 0x7)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -210, 0, -24590, 180)
    EventEnd(0x5)
    Return()

    # Function_5_1A3E end

    def Function_6_2399(): pass

    label("Function_6_2399")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23BE")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_6_2399")

    label("loc_23BE")

    Return()

    # Function_6_2399 end

    def Function_7_23BF(): pass

    label("Function_7_23BF")

    EventBegin(0x1)
    TurnDirection(0x1A2, 0x101, 0)

    #C0086
    ChrTalk(
        0x1A2,
        (
            "都说过啦！没必要带我\x01",
            "来ＩＢＣ！\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1A2,
        "赶快去下一个地方吧！\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00000F啊，好的……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -160, 400, 5710, 180)
    EventEnd(0x4)
    Return()

    # Function_7_23BF end

    def Function_8_2434(): pass

    label("Function_8_2434")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ｉ．Ｂ．Ｃ\x01",
            "International Bank of Crossbell\x01\x01",
            " 需要与大楼内各公司联系的客人，\x01",
            " 请到一层大厅的服务台\x01",
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

    # Function_8_2434 end

    SaveToFile()

Try(main)
