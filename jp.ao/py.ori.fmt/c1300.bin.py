from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "警備員ビルス",           # 1
        "警備員",                 # 2
        "警官",                   # 3
        "警備員",                 # 4
        "警官",                   # 5
        "銀",                     # 6
        "ツァオ",                 # 7
        "ラウ",                   # 8
        "リムジン",               # 9
        "中央広場",               # 10
        "西通り",                 # 11
        "行政区",                 # 12
        "住宅街",                 # 13
        "歓楽街",                 # 14
        "東通り",                 # 15
        "旧市街",                 # 16
        "港湾区",                 # 17
        "ＩＢＣ",                 # 18
        "駅前通り",               # 19
        "裏通り",                 # 20
        "ウルスラ間道",           # 21
        "東クロスベル街道",       # 22
        "西クロスベル街道",       # 23
        "マインツ山道",           # 24
        "オルキスタワー",         # 25
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

    PlaceName(-133.72000122070312, 0.0, -187.47999572753906, 0x0000, 0x0000, "中央広場")
    PlaceName(-223.1999969482422, 0.0, -181.35000610351562, 0x0000, 0x0000, "西通り")
    PlaceName(-96.97000122070312, 0.0, -66.3499984741211, 0x0000, 0x0000, "行政区")
    PlaceName(-306.2300109863281, 0.0, -79.95999908447266, 0x0000, 0x0000, "住宅街")
    PlaceName(-206.8699951171875, 0.0, -90.8499984741211, 0x0000, 0x0000, "歓楽街")
    PlaceName(-23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0000, "東通り")
    PlaceName(25.18000030517578, 0.0, -293.6400146484375, 0x0000, 0x0000, "旧市街")
    PlaceName(14.970000267028809, 0.0, -128.9499969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-20.420000076293945, 0.0, -1.0199999809265137, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-118.41000366210938, 0.0, -281.3900146484375, 0x0000, 0x0000, "駅前通り")
    PlaceName(-182.3699951171875, 0.0, -139.83999633789062, 0x0000, 0x0000, "裏通り")
    PlaceName(-122.48999786376953, 0.0, -323.5799865722656, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(50.36000061035156, 0.0, -199.72999572753906, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-292.6199951171875, 0.0, -183.38999938964844, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-284.45001220703125, 0.0, -47.290000915527344, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-107.0, 0.0, 114.0, 0x0000, 0x0000, "オルキスタワー")
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
        "Function_4_15A0",         # 04, 4
        "Function_5_1CAE",         # 05, 5
        "Function_6_269F",         # 06, 6
        "Function_7_26C5",         # 07, 7
        "Function_8_2758",         # 08, 8
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
    Jump("loc_159C")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8D4")
    Jump("loc_159C")

    label("loc_8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_945")

    #C0001
    ChrTalk(
        0xFE,
        (
            "マインツで占拠事件とは……\x01",
            "やはり背後には帝国がいるのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "……とにかく、要警戒だな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_159C")

    label("loc_945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0E")

    #C0003
    ChrTalk(
        0xFE,
        (
            "おはよう、特務支援課の諸君。\x01",
            "お互い雨に晒されるけど、\x01",
            "今日も張り切って行こうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "何でもランフィさんの話だと\x01",
            "午後には雨も上がるらしいし、\x01",
            "それまでの辛抱ってわけだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A9F")

    label("loc_A0E")


    #C0005
    ChrTalk(
        0xFE,
        (
            "お互い雨に晒されるけど、\x01",
            "今日も張り切って行こうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "何でもランフィさんの話だと\x01",
            "午後には雨も上がるらしいし、\x01",
            "それまでの辛抱ってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9F")

    Jump("loc_159C")

    label("loc_AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3A")

    #C0007
    ChrTalk(
        0xFE,
        (
            "ふむ、あんな小さな子が\x01",
            "たった１人でウチを\x01",
            "訪れるというのも珍しいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "ビルにいる家族にでも\x01",
            "会いに来たのだろうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BB4")

    label("loc_B3A")


    #C0009
    ChrTalk(
        0xFE,
        (
            "おっと、いかんいかん。\x01",
            "俺としたことが、ついお客さんを\x01",
            "詮索するような真似を。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "保安部たるもの、口は慎まないとな。\x02",
    )

    CloseMessageWindow()

    label("loc_BB4")

    Jump("loc_159C")

    label("loc_BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C3A")

    #C0011
    ChrTalk(
        0xFE,
        (
            "おはよう。\x01",
            "今朝も気持ちのいい天気だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "この場所は相変わらず\x01",
            "見晴らしがよくて、\x01",
            "空気もうまくて最高だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159C")

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CF6")

    #C0013
    ChrTalk(
        0xFE,
        (
            "クロスベルが国家として\x01",
            "独立すべきか否か……\x01",
            "深く考えさせられる話だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "何気にＩＢＣのあり方にも\x01",
            "関わってくる話だと思うけど……\x01",
            "流石に細かい所までは想像できないな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159C")

    label("loc_CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F4A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E20")

    #C0015
    ChrTalk(
        0xFE,
        (
            "昨日、ＩＢＣに訪れていた\x01",
            "ロックスミス大統領を\x01",
            "間近で見る事が出来たんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "やはり、あれだけの大国を\x01",
            "まとめ上げるトップともなると、\x01",
            "流石に存在感が普通じゃないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "外見がどうとかじゃなく、\x01",
            "何と言うか、オーラみたいなものを\x01",
            "ひしひし感じたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EB3")

    label("loc_E20")


    #C0018
    ChrTalk(
        0xFE,
        (
            "それはそうと、今朝不審人物が\x01",
            "このＩＢＣに侵入したらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "特に変わった事は\x01",
            "なかったと思うんだが……\x01",
            "気付けなかった事がショックだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB3")

    Jump("loc_F45")

    label("loc_EB8")


    #C0020
    ChrTalk(
        0xFE,
        (
            "怪盗Ｂって噂に聞いた通り、\x01",
            "随分と変わり者なんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "盗んだものを自治州各地に\x01",
            "放置して回るなんて……\x01",
            "ヤツは一体何がしたかったんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F45")

    Jump("loc_159C")

    label("loc_F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_11B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1143")

    #C0022
    ChrTalk(
        0xFE,
        (
            "ああ、君たち。\x01",
            "申し訳ないんだけど、\x01",
            "本日ＩＢＣは休行日なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "というのも、実は今まさに\x01",
            "あのロックスミス大統領が\x01",
            "視察に訪れている最中でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "用事があるなら、\x01",
            "また明日改めて来てくれるかな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 7)), scpexpr(EXPR_END)), "loc_108B")

    #C0025
    ChrTalk(
        0x101,
        (
            "#00005F大統領の視察か……\x02\x03",

            "#00003F確かに、昨日ランフィさんも\x01",
            "そう言っていたな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AA")

    label("loc_108B")


    #C0026
    ChrTalk(
        0x101,
        "#00005F大統領の視察か……\x02",
    )

    CloseMessageWindow()

    label("loc_10AA")


    #C0027
    ChrTalk(
        0x104,
        (
            "#00300Fなんつうか、流石にハンパな\x01",
            "警戒態勢じゃなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#00100Fそうね、とりあえず\x01",
            "お邪魔にならない内に\x01",
            "大人しく退散しましょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11AD")

    label("loc_1143")


    #C0029
    ChrTalk(
        0xFE,
        (
            "申し訳ないんだけど、\x01",
            "本日ＩＢＣは休行日なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "用事があるなら、\x01",
            "また明日改めて来てくれるかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11AD")

    Jump("loc_159C")

    label("loc_11B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1235")

    #C0031
    ChrTalk(
        0xFE,
        "明日から、いよいよ通商会議だな。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "街の警戒レベルも既に高まっているし、\x01",
            "俺たち保安部も自然と気合いが入るよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159C")

    label("loc_1235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1492")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1381")

    #C0033
    ChrTalk(
        0xFE,
        (
            "クロイス総裁、\x01",
            "いや、クロイス市長が\x01",
            "さっきお見えになられたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "市長は基本的に新市庁ビルに\x01",
            "詰めているんだが、時々こうして\x01",
            "こちらにやって来るんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……それにしても、\x01",
            "この２足のわらじは凄まじいよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "しかも実際、それを見事に\x01",
            "履きこなしておられるんだから\x01",
            "本当に感服するよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1427")

    label("loc_1381")


    #C0037
    ChrTalk(
        0xFE,
        (
            "クロスベル市長とＩＢＣ総裁……\x01",
            "よくよく考えると、\x01",
            "この２足のわらじは凄まじいよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "しかも実際、それを見事に\x01",
            "履きこなしておられるんだから\x01",
            "本当に感服するよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1427")

    Jump("loc_148D")

    label("loc_142C")


    #C0039
    ChrTalk(
        0xFE,
        (
            "クロイス市長なら早々に\x01",
            "新市庁の方へ戻っていったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "相変わらずフットワークが軽いよな。\x02",
    )

    CloseMessageWindow()

    label("loc_148D")

    Jump("loc_159C")

    label("loc_1492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_159C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153B")

    #C0041
    ChrTalk(
        0xFE,
        (
            "こんにちは。\x01",
            "ＩＢＣ本社ビルへようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        "何か用事なら受付に行くといいよ。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "我らが自慢の受付嬢が\x01",
            "懇切丁寧に案内してくれるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_159C")

    label("loc_153B")


    #C0044
    ChrTalk(
        0xFE,
        "何か用事なら受付に行くといいよ。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "我らが自慢の受付嬢が\x01",
            "懇切丁寧に案内してくれるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_159C")

    TalkEnd(0xFE)
    Return()

    # Function_3_8B5 end

    def Function_4_15A0(): pass

    label("Function_4_15A0")

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
        "#11P……大したものですね。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xE,
        (
            "#03209F#11Pフフ、素晴らしい。\x02\x03",

            "#03210Fこの光景を見ただけでも\x01",
            "クロスベルに来た甲斐が\x01",
            "あったというものです。\x02",
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
            "#11P#00702F……殊勝なことを。\x02",
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
            "#5P#00700F──まあいい、私は行くぞ。\x02\x03",

            "どうも奇妙なネズミどもが\x01",
            "入り込んでいるようだからな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_184C():
        TurnDirection(0xE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_184C)
    Sleep(50)

    def lambda_185C():
        TurnDirection(0xF, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_185C)
    Sleep(50)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    #C0050
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#03204F#5Pええ、そちらはお任せします。\x02\x03",

            "#03200Fそれと、明日のイベントには\x01",
            "是非とも協力をお願いしますよ？\x02\x03",

            "貴方が来てくださるだけで\x01",
            "相当な箔#2Rハク#が付きますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702Fフン、まあいいだろう。\x02",
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

    def lambda_19AB():
        OP_93(0xFE, 0xD2, 0xC8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_19AB)

    def lambda_19B8():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_19B8)

    def lambda_19D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_19D2)
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
            "#5Pふう……\x01",
            "相変わらず神出鬼没ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xF,
        (
            "#5Pあの気まぐれさえなければ\x01",
            "こちらも助かるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xE,
        (
            "#03204F#5Pフフ、どうやら気まぐれと\x01",
            "いうわけではなさそうです。\x02\x03",

            "#03200F“彼”がこちらに協力してくれる\x01",
            "タイミングにはルールがある……\x02\x03",

            "それを見極めておけば\x01",
            "滅多に断られたりしませんから。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(100)

    #C0055
    ChrTalk(
        0xF,
        "#11Pそ、そうなのですか？\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xF,
        "#11Pしかし、そのルールとは一体……？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xE,
        "#03209F#5Pフフ、まだヒミツです。\x02",
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
            "#03204F#11P──ここまでは段取り通り。\x02\x03",

            "#03202F明日のイベントの成功のため、\x01",
            "もうひと頑張りしておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)
    OP_82(0x1E, 0x0, 0x7D0, 0xC8)

    #C0059
    ChrTalk(
        0xF,
        "#11Pは！\x02",
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

    # Function_4_15A0 end

    def Function_5_1CAE(): pass

    label("Function_5_1CAE")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1DE3")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x104, 950, -1090, -32509, 0)

    def lambda_1D75():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1D75)

    def lambda_1D8F():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D8F)
    Sleep(100)

    def lambda_1DAC():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DAC)
    Sleep(50)

    def lambda_1DC9():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DC9)
    Jump("loc_1F5E")

    label("loc_1DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1EA3")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x109, 950, -1090, -32509, 0)

    def lambda_1E35():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1E35)

    def lambda_1E4F():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E4F)
    Sleep(100)

    def lambda_1E6C():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E6C)
    Sleep(50)

    def lambda_1E89():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E89)
    Jump("loc_1F5E")

    label("loc_1EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1F5E")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x105, 950, -1090, -32509, 0)

    def lambda_1EF5():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1EF5)

    def lambda_1F0F():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F0F)
    Sleep(100)

    def lambda_1F2C():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F2C)
    Sleep(50)

    def lambda_1F49():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1F49)

    label("loc_1F5E")

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
            "#5PＩＢＣか……\x01",
            "ふむ、あいかわらず立派なビルだな。\x02",
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
        "#11P#00105Fシン君は初めてじゃないの？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0062
    ChrTalk(
        0x1A2,
        (
            "#6Pええ、ＩＢＣには当然\x01",
            "黒月の口座もありますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x1A2,
        (
            "#6Pちなみに最近、\x01",
            "ボクも自分の口座を開設して\x01",
            "カブをはじめたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x1A2,
        "#6Pこんど配当金が入るのでよければ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0065
    ChrTalk(
        0x101,
        (
            "#12P#00000Fそういえば、エリィも\x01",
            "学生時代に株をやってたんだよな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0066
    ChrTalk(
        0x102,
        (
            "#5P#00100Fええまあ、後学のために\x01",
            "少しかじった程度だけどね。\x02",
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
            "#6Pまさかエリィお姉さんも\x01",
            "カブをやっていたなんて――\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0068
    ChrTalk(
        0x1A2,
        (
            "#6Pそうだ、ボクこの前\x01",
            "いい銘柄を見つけたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x1A2,
        (
            "#6P堅実ながらも将来性があって\x01",
            "まだそれほど注目されてなくて――\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x1A2,
        (
            "#6Pあ、それ以外にも\x01",
            "オススメの銘柄は他にもあって――\x02",
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
        "#11P#00105Fえ、えっと……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2336")
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0072
    ChrTalk(
        0x101,
        "#12P#00012F（よ、余計なこと言ったかな……？）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0073
    ChrTalk(
        0x104,
        "#12P#00306F（……だな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_2336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_23B2")
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0074
    ChrTalk(
        0x101,
        "#12P#00012F（よ、余計なこと言ったかな……？）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0075
    ChrTalk(
        0x109,
        "#12P#10106F（……だと思います。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_23B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2421")
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0076
    ChrTalk(
        0x101,
        "#12P#00012F（よ、余計なこと言ったかな……？）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0077
    ChrTalk(
        0x105,
        "#12P#10306F（……だね。）\x02",
    )

    CloseMessageWindow()

    label("loc_2421")

    EndChrThread(0x1A2, 0x0)
    OP_64(0x1A2)
    Sleep(500)
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0078
    ChrTalk(
        0x1A2,
        "#6P――ハッ！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x1A2,
        "#6Pすみません、お姉さん。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x1A2,
        (
            "#6P共通のわだいが見つかったと思って\x01",
            "ついうれしくなって一方的に……\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1A2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2500")

    def lambda_24E0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24E0)
    Sleep(50)

    def lambda_24F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_24F0)
    Sleep(300)
    Jump("loc_2557")

    label("loc_2500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_252E")

    def lambda_250E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_250E)
    Sleep(50)

    def lambda_251E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_251E)
    Sleep(300)
    Jump("loc_2557")

    label("loc_252E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2557")

    def lambda_253C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_253C)
    Sleep(50)

    def lambda_254C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_254C)
    Sleep(300)

    label("loc_2557")


    #C0081
    ChrTalk(
        0x102,
        (
            "#11P#00109Fふふ、別に構わないわよ？\x01",
            "ちょっと驚いたけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x1A2,
        (
            "#6Pああ、お姉さん……\x01",
            "やはりあなたは女神のようだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0083
    ChrTalk(
        0x1A2,
        (
            "#5Pとりあえず、ここはその気になれば\x01",
            "いつでも来れるから案内は必要ないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x1A2,
        "#5Pはやく次の場所に向かってくれ。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#12P#00012Fあ、ああ……\x02",
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

    # Function_5_1CAE end

    def Function_6_269F(): pass

    label("Function_6_269F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26C4")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_6_269F")

    label("loc_26C4")

    Return()

    # Function_6_269F end

    def Function_7_26C5(): pass

    label("Function_7_26C5")

    EventBegin(0x1)
    TurnDirection(0x1A2, 0x101, 0)

    #C0086
    ChrTalk(
        0x1A2,
        (
            "だからー、別にＩＢＣを\x01",
            "案内してもらう必要はないんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1A2,
        "はやく次の場所に行くぞ！\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00000Fあ、ああ……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -160, 400, 5710, 180)
    EventEnd(0x4)
    Return()

    # Function_7_26C5 end

    def Function_8_2758(): pass

    label("Function_8_2758")

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
            " 入居各社にお問い合わせの方は\x01",
            " １階ロビーカウンターにて\x01",
            " 声をおかけ下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_2758 end

    SaveToFile()

Try(main)
