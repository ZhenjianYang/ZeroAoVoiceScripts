from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1000.bin",                # FileName
        "t1000",                    # MapName
        "t1000",                    # Location
        0x0041,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1000",                  # 0
        "萨尔莎乘务员",           # 1
        "詹姆斯",                 # 2
        "尼基塔",                 # 3
        "男孩",                   # 4
        "男性",                   # 5
        "女性",                   # 6
        "游客",                   # 7
        "本德",                   # 8
        "库雷优",                 # 9
        "萨妮塔",                 # 10
        "玛丽",                   # 11
        "彼德",                   # 12
        "特级钓师罗伊德",         # 13
        "雾香",                   # 14
        "雷克特",                 # 15
        "水上巴士",               # 16
        "乘客",                   # 17
        "乘客",                   # 18
        "乘客",                   # 19
        "乘客",                   # 20
        "乘客",                   # 21
        "乘客",                   # 22
        "乘客",                   # 23
        "乘客",                   # 24
        "SE控制",                 # 25
        "主题公园方向",           # 26
        "宅邸方向",               # 27
    ))

    AddCharChip((
        "chr/ch28400.itc",                   # 00
        "chr/ch20600.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch27800.itc",                   # 04
        "chr/ch26800.itc",                   # 05
        "chr/ch24400.itc",                   # 06
        "chr/ch27600.itc",                   # 07
        "chr/ch33300.itc",                   # 08
        "chr/ch34400.itc",                   # 09
        "chr/ch39000.itc",                   # 0A
        "apl/ch50165.itc",                   # 0B
        "apl/ch50169.itc",                   # 0C
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

    DeclNpc(-3740,   -4000,   -47180,  180,  385,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(15460,   -2000,   -24889,  180,  385,  0x0, 0,   4,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(15479,   -2000,   -25989,  0,    385,  0x0, 0,   5,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(9600,    -4000,   -47930,  268,  385,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(8069,    -4000,   -48130,  86,   385,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(8699,    -4000,   -49430,  45,   385,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-7000,   -2000,   -26329,  270,  385,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-6340,   -4000,   -47330,  135,  389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-6869,   -4000,   -48279,  45,   389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-4769,   -4000,   -47900,  270,  389,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-3809,   -4000,   -47520,  270,  389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(20559,   -5000,   -56500,  180,  277,  0x0, 0,   11,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(18040,   -5000,   -56500,  180,  277,  0x0, 0,   12,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-24500,  -4000,   -45660,  1200,    -24490,  -6000,   -38830,  0x007C, 0,  17, 0x0000)
    DeclActor(10350,   -3990,   -46410,  1200,    10350,   -2500,   -46410,  0x007C, 0,  27, 0x0000)
    DeclActor(-30180,  -4000,   -47980,  1200,    -30180,  -4000,   -47980,  0x007C, 0,  26, 0x0000)

    PlaceName(-5.0, 0.0, 95.0, 0x0000, 0x0000, "主题公园方向")
    PlaceName(-95.0, 0.0, 20.0, 0x0000, 0x0000, "宅邸方向")
    PlaceName(1.0, 0.0, 17.5, 0x0000, 0x0052, "")

    ScpFunction((
        "Function_0_4E0",          # 00, 0
        "Function_1_598",          # 01, 1
        "Function_2_64A",          # 02, 2
        "Function_3_7AD",          # 03, 3
        "Function_4_878",          # 04, 4
        "Function_5_8CE",          # 05, 5
        "Function_6_93E",          # 06, 6
        "Function_7_9EB",          # 07, 7
        "Function_8_A85",          # 08, 8
        "Function_9_AD6",          # 09, 9
        "Function_10_B3B",         # 0A, 10
        "Function_11_C4F",         # 0B, 11
        "Function_12_CAE",         # 0C, 12
        "Function_13_CD6",         # 0D, 13
        "Function_14_D78",         # 0E, 14
        "Function_15_D8D",         # 0F, 15
        "Function_16_10CB",        # 10, 16
        "Function_17_11A5",        # 11, 17
        "Function_18_126D",        # 12, 18
        "Function_19_1E07",        # 13, 19
        "Function_20_1E5C",        # 14, 20
        "Function_21_1E88",        # 15, 21
        "Function_22_1EE4",        # 16, 22
        "Function_23_1F40",        # 17, 23
        "Function_24_1F9C",        # 18, 24
        "Function_25_1FF8",        # 19, 25
        "Function_26_201D",        # 1A, 26
        "Function_27_219A",        # 1B, 27
    ))


    def Function_0_4E0(): pass

    label("Function_0_4E0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_520"),
        (1, "loc_52C"),
        (2, "loc_538"),
        (3, "loc_544"),
        (4, "loc_550"),
        (5, "loc_55C"),
        (6, "loc_568"),
        (SWITCH_DEFAULT, "loc_574"),
    )


    label("loc_520")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_52C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_538")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_544")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_550")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_55C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_568")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_574")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_580")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_597")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_597")

    Return()

    # Function_0_4E0 end

    def Function_1_598(): pass

    label("Function_1_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_5A7")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 18)

    label("loc_5A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_5B5")
    Jump("loc_649")

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_5C3")
    Jump("loc_649")

    label("loc_5C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_5D1")
    Jump("loc_649")

    label("loc_5D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_5DF")
    Jump("loc_649")

    label("loc_5DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_5ED")
    Jump("loc_649")

    label("loc_5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_61E")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_649")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_640")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_649")

    label("loc_640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_649")

    label("loc_649")

    Return()

    # Function_1_598 end

    def Function_2_64A(): pass

    label("Function_2_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_690")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "t1000_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1000_sky_y", 0x1, 0x1)
    SetMapObjFlags(0x0, 0x4)
    Jump("loc_6B4")

    label("loc_690")

    SetMapObjFrame(0xFF, "t1000_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1000_sky_y", 0x0, 0x1)

    label("loc_6B4")

    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -24490, -6000, -38830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73D")
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)

    label("loc_73D")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A6")
    LoadEffect(0x0, "event\\eva00_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -30180, -4000, -47980, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_7A6")

    Sound(126, 1, 80, 0)
    Return()

    # Function_2_64A end

    def Function_3_7AD(): pass

    label("Function_3_7AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_826")

    #C0001
    ChrTalk(
        0xFE,
        (
            "前往往克洛斯贝尔市的水上巴士\x01",
            "刚刚已经出发。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "下一班很快就将到达，\x01",
            "需要乘坐的客人，请稍候片刻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_874")

    label("loc_826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_874")

    #C0003
    ChrTalk(
        0xFE,
        "水上巴士之旅让大家辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "请在米修拉姆\x01",
            "度过梦幻般的时刻。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_874")

    TalkEnd(0xFE)
    Return()

    # Function_3_7AD end

    def Function_4_878(): pass

    label("Function_4_878")

    TalkBegin(0xFE)
    TurnDirection(0x9, 0xA, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_894")
    Call(0, 6)
    Jump("loc_8CA")

    label("loc_894")


    #C0005
    ChrTalk(
        0xFE,
        (
            "哈哈哈……\x01",
            "我跟我太太说我出差去了，\x01",
            "不必担心啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CA")

    TalkEnd(0xFE)
    Return()

    # Function_4_878 end

    def Function_5_8CE(): pass

    label("Function_5_8CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EA")
    TurnDirection(0xA, 0x9, 0)
    Call(0, 6)
    Jump("loc_93A")

    label("loc_8EA")


    #C0006
    ChrTalk(
        0xFE,
        (
            "那个竞拍会，\x01",
            "我以前就很有兴趣了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "呵呵……能有人带我来，\x01",
            "真是幸运啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93A")

    TalkEnd(0xFE)
    Return()

    # Function_5_8CE end

    def Function_6_93E(): pass

    label("Function_6_93E")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0008
    ChrTalk(
        0x9,
        "今晚要在议长宅邸举行宴会。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "就让我为你拍个\x01",
            "美丽的饰品吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        (
            "呵呵……真是个坏人。\x01",
            "明明都有妻子了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "哈哈哈……\x01",
            "不是说好今晚不提这个的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_6_93E end

    def Function_7_9EB(): pass

    label("Function_7_9EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A58")

    #C0012
    ChrTalk(
        0xFE,
        (
            "刚才下船的那个大哥哥\x01",
            "以超快的速度跑掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "他那么期待啊～\x01",
            "我也要好好玩个痛快！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A81")

    label("loc_A58")


    #C0014
    ChrTalk(
        0xFE,
        (
            "今天爸爸也在……\x01",
            "我要好好玩个痛快！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A81")

    TalkEnd(0xFE)
    Return()

    # Function_7_9EB end

    def Function_8_A85(): pass

    label("Function_8_A85")

    TalkBegin(0xFE)

    #C0015
    ChrTalk(
        0xFE,
        (
            "好～快点前往\x01",
            "主题公园吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "任何游乐设施，爸爸今天\x01",
            "都会陪你玩哦！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_A85 end

    def Function_9_AD6(): pass

    label("Function_9_AD6")

    TalkBegin(0xFE)

    #C0017
    ChrTalk(
        0xFE,
        (
            "哎呀呀，老公你真是的，\x01",
            "这么爱逞强。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "呵呵，那我就不客气地\x01",
            "去坐惊险刺激的游乐设施啦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_AD6 end

    def Function_10_B3B(): pass

    label("Function_10_B3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BED")

    #C0019
    ChrTalk(
        0xFE,
        (
            "我打算逛完纪念庆典之后\x01",
            "再来这里，\x01",
            "结果就拖到傍晚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "没办法，\x01",
            "去精品店那边随便看看，\x01",
            "然后就早点回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "要是被卷入回程大潮，\x01",
            "可就太糟糕了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C4B")

    label("loc_BED")


    #C0022
    ChrTalk(
        0xFE,
        (
            "我来得太迟了呢，\x01",
            "大概玩不到什么东西了……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "去精品店那边随便看看，\x01",
            "然后就早点回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4B")

    TalkEnd(0xFE)
    Return()

    # Function_10_B3B end

    def Function_11_C4F(): pass

    label("Function_11_C4F")

    TalkBegin(0xFE)

    #C0024
    ChrTalk(
        0xF,
        (
            "哈哈，真愉快，\x01",
            "今天全家人一起玩了个痛快呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xF,
        (
            "偶尔这样放松一下，\x01",
            "感觉也不错啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_C4F end

    def Function_12_CAE(): pass

    label("Function_12_CAE")

    TalkBegin(0xFE)

    #C0026
    ChrTalk(
        0x10,
        (
            "酒店都住满了……\x01",
            "好遗憾……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_CAE end

    def Function_13_CD6(): pass

    label("Function_13_CD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D14")

    #C0027
    ChrTalk(
        0x11,
        (
            "爸爸和妈妈……\x01",
            "以后会不会再带我来呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D74")

    label("loc_D14")


    #C0028
    ChrTalk(
        0x11,
        (
            "因为爸爸还有工作，\x01",
            "所以今天必须回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x11,
        (
            "……而且\x01",
            "玛丽也累了，\x01",
            "萨妮塔今天就先回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_D74")

    TalkEnd(0xFE)
    Return()

    # Function_13_CD6 end

    def Function_14_D78(): pass

    label("Function_14_D78")

    TalkBegin(0xFE)

    #C0030
    ChrTalk(
        0x12,
        "呼啊……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_D78 end

    def Function_15_D8D(): pass

    label("Function_15_D8D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB7")

    #C0031
    ChrTalk(
        0xFE,
        (
            "哎呀，罗伊德团员\x01",
            "也来钓鱼吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "呵呵，你果然也还没从\x01",
            "钓鱼大赛的热情中冷却下来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "对了，你带着鱼饵吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0034
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '熬炼丸子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "共５个获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('熬炼丸子', 5)

    #C0035
    ChrTalk(
        0xFE,
        "分给你一点好了，虽然不多。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "呵呵，罗伊德团员\x01",
            "也请加油哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD9, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_EB2")
    SetScenarioFlags(0xD9, 1)

    label("loc_EB2")

    Jump("loc_10C7")

    label("loc_EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('熬炼丸子', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FAD")

    #C0037
    ChrTalk(
        0xFE,
        (
            "哎呀，罗伊德团员。\x01",
            "莫非是\x01",
            "鱼饵不够了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0038
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '熬炼丸子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "共２个获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('熬炼丸子', 2)

    #C0039
    ChrTalk(
        0xFE,
        "分给你一点好了，虽然不多。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "呵呵，罗伊德团员也很有热情呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD9, 1)
    Jump("loc_10C7")

    label("loc_FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1003")

    #C0041
    ChrTalk(
        0xFE,
        (
            "哎呀，水流的情况似乎\x01",
            "改变了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "很遗憾，今天\x01",
            "就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C7")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_10C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109A")

    #C0043
    ChrTalk(
        0xFE,
        (
            "这位罗伊德大师\x01",
            "说也想到对岸来\x01",
            "钓鱼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "呵呵，不愧是特级钓师，\x01",
            "判断力就是不同呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "今天的钓鱼成果\x01",
            "真是太棒了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_10C7")

    label("loc_109A")


    #C0046
    ChrTalk(
        0xFE,
        (
            "不愧是特级钓师，\x01",
            "判断力真是太出色了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C7")

    TalkEnd(0xFE)
    Return()

    # Function_15_D8D end

    def Function_16_10CB(): pass

    label("Function_16_10CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1129")

    #C0047
    ChrTalk(
        0xFE,
        "唔，今天也就这样了吧……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "钓到了大口鲈鱼这样的大鱼，\x01",
            "就算不错了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A1")

    label("loc_1129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_11A1")

    #C0049
    ChrTalk(
        0xFE,
        (
            "纪念庆典结束以后，\x01",
            "我就打算回利贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔能够\x01",
            "体验到的钓鱼方式，\x01",
            "可要全部尝试一次才行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A1")

    TalkEnd(0xFE)
    Return()

    # Function_16_10CB end

    def Function_17_11A5(): pass

    label("Function_17_11A5")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0051
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
    )

    CloseMessageWindow()
    OP_68(-23140, -2400, -43580, 1500)
    MoveCamera(315, 36, 0, 1500)
    OP_6E(200, 1500)
    SetCameraDistance(50000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要钓鱼吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1268")
    OP_E0(0x2)
    MiniGame(0x6, 0x3, 0xFFFFA04C, 0xFFFFF060, 0xFFFF4912, 0x0, 0xFFFFA056, 0xFFFFE890, 0xFFFF6852)

    label("loc_1268")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_17_11A5 end

    def Function_18_126D(): pass

    label("Function_18_126D")

    EventBegin(0x0)
    OP_E5()
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x1E)
    LoadChrToIndex("chr/ch07300.itc", 0x1F)
    LoadChrToIndex("chr/ch20600.itc", 0x20)
    LoadChrToIndex("chr/ch20200.itc", 0x21)
    LoadChrToIndex("chr/ch20300.itc", 0x22)
    LoadChrToIndex("chr/ch21600.itc", 0x23)
    LoadChrToIndex("chr/ch21300.itc", 0x24)
    LoadChrToIndex("chr/ch21200.itc", 0x25)
    LoadChrToIndex("chr/ch27700.itc", 0x26)
    LoadChrToIndex("chr/ch23600.itc", 0x27)
    SetChrPos(0x101, -7250, -4000, -40000, 180)
    SetChrPos(0x102, -7250, -4000, -40000, 180)
    SetChrPos(0x103, -7250, -4000, -40000, 180)
    SetChrPos(0x104, -7250, -4000, -40000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0x16, -7250, -4000, -40000, 180)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrPos(0x15, -7250, -4000, -40000, 180)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x0, 0x17)
    OP_49()
    SetChrPos(0x17, -45000, -5500, -38200, 0)
    OP_D3(0x17, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetChrChipByIndex(0x18, 0x20)
    SetChrChipByIndex(0x19, 0x21)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrChipByIndex(0x1B, 0x23)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrChipByIndex(0x1E, 0x26)
    SetChrChipByIndex(0x1F, 0x27)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x18, -7250, -4000, -40000, 180)
    SetChrPos(0x19, -7250, -4000, -40000, 180)
    SetChrPos(0x1A, -7250, -4000, -40000, 180)
    SetChrPos(0x1B, -7250, -4000, -40000, 180)
    SetChrPos(0x1C, -7250, -4000, -40000, 180)
    SetChrPos(0x1D, -7250, -4000, -40000, 180)
    SetChrPos(0x1E, -7250, -4000, -40000, 180)
    SetChrPos(0x1F, -7250, -4000, -40000, 180)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    PlaceName2(340, 200, "c_plac20", 0x0, 3000)
    FadeToBright(2000, 0)
    OP_68(20240, -2400, -36530, 0)
    MoveCamera(334, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(64730, 0)
    OP_68(-1240, -2400, -36530, 15000)
    BeginChrThread(0x20, 1, 0, 25)

    def lambda_15EB():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_15EB)
    WaitChrThread(0x17, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    Sound(478, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0x12D, 0x168, 0x0, 0x20)
    OP_6F(0x1)
    EndChrThread(0x20, 0x1)
    OP_0D()
    Fade(1000)
    OP_68(-5240, -1300, -48610, 0)
    MoveCamera(327, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(31570, 0)
    OP_0D()
    OP_71(0x0, 0x1, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0xF1, 0x12C, 0x0, 0x20)
    BeginChrThread(0x18, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x19, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x1A, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x1B, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x16, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x1C, 3, 0, 19)
    Sleep(1000)
    OP_63(0x16, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    BeginChrThread(0x1D, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x1E, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x15, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x1F, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 22)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 23)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 24)
    Fade(1000)
    OP_68(-530, -1300, -54200, 0)
    MoveCamera(326, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13040, 0)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_0D()
    Sleep(500)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x19, 0x3)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x1B, 0x3)
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x1D, 0x3)
    EndChrThread(0x1E, 0x3)
    EndChrThread(0x1F, 0x3)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x15, 0x3)
    OP_E6()

    #C0053
    ChrTalk(
        0x101,
        (
            "#0008F#5P──这里就是米修拉姆啊。\x02\x03",

            "#0006F该怎么说呢，真是比想象中\x01",
            "更加奢华的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x103,
        (
            "#0203F#5P这里原本是个高级疗养地，\x01",
            "由ＩＢＣ着手开发为度假村……\x02\x03",

            "#0200F酒店和主题公园好像\x01",
            "也是在两年前才刚建成的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        (
            "#0104F#5P嗯，从那以后，这里就成为了\x01",
            "与彩虹剧团齐名的观光胜地。\x02\x03",

            "#0100F正面是酒店，\x01",
            "一楼是商店街。\x02\x03",

            "其中有餐厅、精品店、\x01",
            "珠宝店等等。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#0306F#5P但价格全都高得离谱，\x01",
            "平民很难承受就是了～\x02\x03",

            "#0300F我以前约会的时候，\x01",
            "也只去过主题公园\x01",
            "和餐厅……\x02\x03",

            "那么，接下来该怎么办？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1970():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1970)

    def lambda_197D():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_197D)
    Sleep(100)

    def lambda_198D():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_198D)

    def lambda_199A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_199A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0057
    ChrTalk(
        0x101,
        (
            "#0003F#12P这个嘛……\x02\x03",

            "#0001F先确认一下\x01",
            "拍卖会场周边的情况吧。\x02\x03",

            "会场就在哈尔特曼议长宅邸，没错吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#0100F#6P嗯……\x01",
            "从左边穿过商店街，可以看到一片\x01",
            "别墅林立的疗养地区域。\x02\x03",

            "议长宅邸应该就在最里面。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#0004F#12P明白了。\x02\x03",

            "#0000F除此之外……\x01",
            "能去的地方也都去看看吧。\x02\x03",

            "说不定还会遇到\x01",
            "像雷克特那样的\x01",
            "『竞拍会』宾客呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        "#0202F#5P……是啊。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        (
            "#0106F#6P说起来，那个人……\x02\x03",

            "#0101F言行举止相当奇怪，\x01",
            "真的是帝国贵族吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        (
            "#0303F#5P……谁知道。\x02\x03",

            "#0301F说不定和他之前自称为铁血宰相的代理人一样，\x01",
            "只是在信口开河而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#0006F#12P只是，似乎连这种奇怪的人\x01",
            "也都被邀请为来宾了。\x02\x03",

            "#0013F『黑之竞拍会』──\x01",
            "果然不能以常理度之啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetCameraDistance(13290, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x0)
    SetChrChipByIndex(0x1F, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x0, -2000, -4000, -50200, 90)
    SetScenarioFlags(0xA4, 0)
    OP_29(0x47, 0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D47")
    OP_29(0x18, 0x4, 0x40)
    Jump("loc_1D59")

    label("loc_1D47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D59")
    OP_29(0x18, 0x4, 0x40)

    label("loc_1D59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D6B")
    OP_29(0x1A, 0x4, 0x40)

    label("loc_1D6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D89")
    OP_29(0x1C, 0x4, 0x40)
    Jump("loc_1D9B")

    label("loc_1D89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9B")
    OP_29(0x1C, 0x4, 0x40)

    label("loc_1D9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DAD")
    OP_29(0x1E, 0x4, 0x40)

    label("loc_1DAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x21, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DBF")
    OP_29(0x21, 0x4, 0x40)

    label("loc_1DBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DDD")
    OP_29(0x22, 0x4, 0x40)
    Jump("loc_1DEF")

    label("loc_1DDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEF")
    OP_29(0x22, 0x4, 0x40)

    label("loc_1DEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E01")
    OP_29(0x23, 0x4, 0x40)

    label("loc_1E01")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_126D end

    def Function_19_1E07(): pass

    label("Function_19_1E07")


    def lambda_1E0C():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E0C)
    Sleep(500)

    def lambda_1E29():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E29)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1E42():
        OP_95(0xFE, 7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E42)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_1E07 end

    def Function_20_1E5C(): pass

    label("Function_20_1E5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E87")
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(3000)
    Jump("Function_20_1E5C")

    label("loc_1E87")

    Return()

    # Function_20_1E5C end

    def Function_21_1E88(): pass

    label("Function_21_1E88")


    def lambda_1E8D():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E8D)
    Sleep(500)

    def lambda_1EAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1EAA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1EC3():
        OP_95(0xFE, -2940, -4000, -50580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1EC3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_21_1E88 end

    def Function_22_1EE4(): pass

    label("Function_22_1EE4")


    def lambda_1EE9():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1EE9)
    Sleep(500)

    def lambda_1F06():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F06)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1F1F():
        OP_95(0xFE, -4019, -4000, -51400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F1F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_22_1EE4 end

    def Function_23_1F40(): pass

    label("Function_23_1F40")


    def lambda_1F45():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F45)
    Sleep(500)

    def lambda_1F62():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F62)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1F7B():
        OP_95(0xFE, -4680, -4000, -49050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F7B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_23_1F40 end

    def Function_24_1F9C(): pass

    label("Function_24_1F9C")


    def lambda_1FA1():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1FA1)
    Sleep(500)

    def lambda_1FBE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1FBE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1FD7():
        OP_95(0xFE, -5640, -4000, -50180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1FD7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_24_1F9C end

    def Function_25_1FF8(): pass

    label("Function_25_1FF8")

    Sleep(1000)
    Sound(475, 0, 100, 0)
    Sleep(1500)
    Sound(477, 0, 100, 0)
    Sleep(4000)
    Sound(476, 0, 100, 0)
    Sleep(1000)
    Sound(477, 0, 100, 0)
    Return()

    # Function_25_1FF8 end

    def Function_26_201D(): pass

    label("Function_26_201D")

    EventBegin(0x0)
    Fade(500)
    OP_68(-28230, -2400, -50050, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(34310, 0)
    SetChrPos(0x101, -28000, -4000, -48730, 270)
    SetChrPos(0x102, -28000, -4000, -47510, 225)
    SetChrPos(0x103, -26240, -4000, -49940, 270)
    SetChrPos(0x104, -26310, -4000, -48550, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_20B0")
    SetChrPos(0x151, -25030, -4000, -49530, 270)

    label("loc_20B0")

    StopEffect(0x0, 0x2)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0064
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '影丸储蓄罐'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('影丸储蓄罐', 1)

    #C0065
    ChrTalk(
        0x101,
        "#12P#0005F咦，这个戒指……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#11P#0105F说不定正是托马先生\x01",
            "之前说的订婚戒指呢。\x02\x03",

            "#0100F稍后拿到酒店的房间里\x01",
            "给他看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x1)
    OP_65(0x2, 0x1)
    SetChrPos(0x0, -28000, -4000, -48730, 270)
    EventEnd(0x5)
    Return()

    # Function_26_201D end

    def Function_27_219A(): pass

    label("Function_27_219A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "前往『克洛斯贝尔市』的水上巴士·时刻表\x01\x01",
            "   ※期待着您的\x01",
            "　       下次光临！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_219A end

    SaveToFile()

Try(main)
