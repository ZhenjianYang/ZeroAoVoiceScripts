from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1030.bin",                # FileName
        "t1030",                    # MapName
        "t1030",                    # Location
        0x0041,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1030",                  # 0
        "係員",                   # 1
        "係員",                   # 2
        "みっしぃ",               # 3
        "女性",                   # 4
        "女の子",                 # 5
        "男の子",                 # 6
        "男性",                   # 7
        "観光客",                 # 8
        "ボンド",                 # 9
        "クレイユ",               # 10
        "サニータ",               # 11
        "マリー",                 # 12
        "SE制御",                 # 13
        "ホテル・デルフィニア方面",# 14
        "テーマパーク方面",       # 15
    ))

    AddCharChip((
        "chr/ch28300.itc",                   # 00
        "chr/ch23500.itc",                   # 01
        "chr/ch23900.itc",                   # 02
        "chr/ch24600.itc",                   # 03
        "chr/ch24200.itc",                   # 04
        "chr/ch32200.itc",                   # 05
        "chr/ch10200.itc",                   # 06
        "chr/ch27600.itc",                   # 07
        "chr/ch33300.itc",                   # 08
        "chr/ch34400.itc",                   # 09
        "chr/ch39000.itc",                   # 0A
    ))

    DeclNpc(4750,    4400,    0,       180,  257,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-4000,   4400,    0,       180,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(360,     4159,    -15840,  180,  385,  0x0, 0,   6,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-9810,   4000,    -5130,   45,   385,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-8970,   4000,    -4289,   225,  385,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-3690,   4000,    -19149,  180,  385,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-3690,   1639,    -23280,  0,    385,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-7409,   4000,    -6219,   180,  385,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(7699,    4000,    -1519,   135,  389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(9159,    4000,    -1759,   270,  389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(7889,    4000,    -3069,   360,  405,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(6949,    4000,    -3160,   45,   389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 16,  0.0,                   -48.0,                 -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  16.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 15,  0.0,                   4.150000095367432,     3.0,                   81.0,                  [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.6666666865348816,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -2.766666889190674,    -0.6000000238418579,   1.0])

    DeclActor(-14170,  4000,    -6040,   1200,    -14170,  5500,    -6040,   0x007C, 0,  18, 0x0000)
    DeclActor(-6650,   4000,    1550,    1200,    -6650,   5500,    1550,    0x007C, 0,  19, 0x0000)
    DeclActor(4180,    4250,    -9540,   1200,    4180,    4250,    -9540,   0x007C, 0,  17, 0x0000)

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "ホテル・デルフィニア方面")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "テーマパーク方面")

    ScpFunction((
        "Function_0_3D0",          # 00, 0
        "Function_1_488",          # 01, 1
        "Function_2_526",          # 02, 2
        "Function_3_647",          # 03, 3
        "Function_4_917",          # 04, 4
        "Function_5_CF2",          # 05, 5
        "Function_6_E28",          # 06, 6
        "Function_7_E91",          # 07, 7
        "Function_8_EC5",          # 08, 8
        "Function_9_EF1",          # 09, 9
        "Function_10_1005",        # 0A, 10
        "Function_11_1043",        # 0B, 11
        "Function_12_1116",        # 0C, 12
        "Function_13_1173",        # 0D, 13
        "Function_14_11F7",        # 0E, 14
        "Function_15_1212",        # 0F, 15
        "Function_16_1478",        # 10, 16
        "Function_17_1C4D",        # 11, 17
        "Function_18_1DE8",        # 12, 18
        "Function_19_1E65",        # 13, 19
    ))


    def Function_0_3D0(): pass

    label("Function_0_3D0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_410"),
        (1, "loc_41C"),
        (2, "loc_428"),
        (3, "loc_434"),
        (4, "loc_440"),
        (5, "loc_44C"),
        (6, "loc_458"),
        (SWITCH_DEFAULT, "loc_464"),
    )


    label("loc_410")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_41C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_428")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_434")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_440")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_44C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_458")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_464")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_470")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_487")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_487")

    Return()

    # Function_0_3D0 end

    def Function_1_488(): pass

    label("Function_1_488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_496")
    Jump("loc_525")

    label("loc_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_525")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_4B2")
    Jump("loc_525")

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4C0")
    Jump("loc_525")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_4CE")
    Jump("loc_525")

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4EB")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_525")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_51C")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_525")

    label("loc_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_525")

    label("loc_525")

    Return()

    # Function_1_488 end

    def Function_2_526(): pass

    label("Function_2_526")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_543")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_583")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "t1030_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1030_sky_y", 0x1, 0x1)
    Jump("loc_5A7")

    label("loc_583")

    SetMapObjFrame(0xFF, "t1030_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1030_sky_y", 0x0, 0x1)

    label("loc_5A7")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_610")
    LoadEffect(0x1, "event\\eva00_00.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0x0, 4180, 4250, -9540, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_610")

    SoundDistance(0x375, 0x92E0, 0xFA0, 0x44D4, 0x15F90, 0xEA60, 0x64, 0x0)
    OP_E1(0xFFFFF646, 0xFA0, 0x2800)
    OP_E1(0xFFFED040, 0xFA0, 0x466E)
    Return()

    # Function_2_526 end

    def Function_3_647(): pass

    label("Function_3_647")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_658")
    Jump("loc_913")

    label("loc_658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_666")
    Jump("loc_913")

    label("loc_666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_674")
    Jump("loc_913")

    label("loc_674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_682")
    Jump("loc_913")

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_690")
    Jump("loc_913")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_723")

    #C0001
    ChrTalk(
        0xFE,
        (
            "テーマパーク夜の部のために\x01",
            "この時間から入場する方も\x01",
            "多々おられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "雰囲気たっぷりの夜の部は\x01",
            "カップルに大人気なのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_913")

    label("loc_723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_90A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_838")

    #C0003
    ChrTalk(
        0xFE,
        (
            "ミシュラムの誇る\x01",
            "テーマパークへようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "入場券はお持ちでしょうか？\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0000Fいや……今回は用があってね。\x01",
            "悪いけど遠慮させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "おお、そうですか……\x01",
            "それは残念です。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "またお越しいただいた際の\x01",
            "ご利用をお待ちしております。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_905")

    label("loc_838")


    #C0008
    ChrTalk(
        0xFE,
        (
            "今回はテーマパークを\x01",
            "ご利用なさらないということで……\x01",
            "残念です。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "まぁ、このミシュラムには\x01",
            "他にも数々の見所があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "夜には園の外からでも\x01",
            "花火が見られると思いますので\x01",
            "どうかお見逃しなく。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_905")

    Jump("loc_913")

    label("loc_90A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_913")

    label("loc_913")

    TalkEnd(0xFE)
    Return()

    # Function_3_647 end

    def Function_4_917(): pass

    label("Function_4_917")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_928")
    Jump("loc_CEE")

    label("loc_928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_936")
    Jump("loc_CEE")

    label("loc_936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_944")
    Jump("loc_CEE")

    label("loc_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_952")
    Jump("loc_CEE")

    label("loc_952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_960")
    Jump("loc_CEE")

    label("loc_960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_AD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A39")

    #C0011
    ChrTalk(
        0xFE,
        (
            "園内には各種乗り物のほかに、\x01",
            "みっしぃグッズなどの販売も\x01",
            "行っていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "中でもおすすめは\x01",
            "『みっしぃの耳バンド』！\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "園内ならではのハイテンションに\x01",
            "身を任せてはいかがでしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_AD3")

    label("loc_A39")


    #C0014
    ChrTalk(
        0xFE,
        (
            "園内には各種乗り物のほかに、\x01",
            "みっしぃグッズなどの販売も\x01",
            "行っていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "『みっしぃの耳バンド』の他にも\x01",
            "ストラップなども\x01",
            "取り揃えておりますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD3")

    Jump("loc_CEE")

    label("loc_AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_CE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEE")

    #C0016
    ChrTalk(
        0xFE,
        (
            "さっき入って行った旅行者の方……\x01",
            "なかなか面白い方でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "『テーマパークの中に\x01",
            "  もう一人みっしぃがいないか\x01",
            "  確かめてやる！』\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "……などと意気込んでいまして。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#0006F（レクターさんだな……）\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        "#0106F（一体何をやってるんだか……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CE0")

    label("loc_BEE")


    #C0021
    ChrTalk(
        0xFE,
        (
            "ふふ、心配はございません。\x01",
            "みっしぃが２人以上存在するなど\x01",
            "有り得ないことですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#0003F（ふーむ、抜かりないシフトが\x01",
            "  組まれてるんだろうな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0211F（……夢の無いことを\x01",
            "  言わないで下さい。）\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0011F（す、すみません。）\x02",
    )

    CloseMessageWindow()

    label("loc_CE0")

    Jump("loc_CEE")

    label("loc_CE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_CEE")

    label("loc_CEE")

    TalkEnd(0xFE)
    Return()

    # Function_4_917 end

    def Function_5_CF2(): pass

    label("Function_5_CF2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC9")

    #C0025
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "こんにちは！\x01",
            "ワンダーランドにようこそっ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、楽しんでいってネ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        "#0201F……生みっしぃ……！！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0005Fティ、ティオ？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        (
            "#0203F……コホン。\x01",
            "なんでもないです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_E24")

    label("loc_DC9")


    #C0030
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "こんにちは！\x01",
            "ワンダーランドにようこそっ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、楽しんでいってネ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E24")

    TalkEnd(0xFE)
    Return()

    # Function_5_CF2 end

    def Function_6_E28(): pass

    label("Function_6_E28")

    TalkBegin(0xFE)

    #C0032
    ChrTalk(
        0xFE,
        (
            "はァ～……\x01",
            "これがテーマパークかぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "……さすがにでっかいねぇ。\x01",
            "遊びきれるといいけど……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_E28 end

    def Function_7_E91(): pass

    label("Function_7_E91")

    TalkBegin(0xFE)

    #C0034
    ChrTalk(
        0xFE,
        (
            "わァい！\x01",
            "前からここ、来たかったんだぁ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_E91 end

    def Function_8_EC5(): pass

    label("Function_8_EC5")

    TalkBegin(0xFE)
    OP_93(0xFE, 0xB4, 0x0)

    #C0035
    ChrTalk(
        0xFE,
        "おとーさん、早く入ろ～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_EC5 end

    def Function_9_EF1(): pass

    label("Function_9_EF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F70")
    OP_93(0xFE, 0x0, 0x0)

    #C0036
    ChrTalk(
        0xD,
        (
            "おとーさん！\x01",
            "何してんのー？\x01",
            "早く入ろうよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "はいはい、わかったわかった。\x01",
            "少し待ちなさい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1001")

    label("loc_F70")


    #C0038
    ChrTalk(
        0xFE,
        (
            "しかし、子供は本当に\x01",
            "こういう場所が好きだよなぁ。\x01",
            "もう夕方だと言うのにあんなに元気とは。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "放っといたら体力の限界まで\x01",
            "遊んでそうだよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1001")

    TalkEnd(0xFE)
    Return()

    # Function_9_EF1 end

    def Function_10_1005(): pass

    label("Function_10_1005")

    TalkBegin(0xFE)

    #C0040
    ChrTalk(
        0xFE,
        (
            "まだ夕方だけど、混みあう前に\x01",
            "ホテルに戻ろうかな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_1005 end

    def Function_11_1043(): pass

    label("Function_11_1043")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10AB")

    #C0041
    ChrTalk(
        0x10,
        "実はまだ仕事も残ってるんだ。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x10,
        (
            "そんなには遊べないんだが……\x01",
            "ま、まあいいか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1112")

    label("loc_10AB")


    #C0043
    ChrTalk(
        0x10,
        (
            "たまには家族サービス\x01",
            "……と思ったんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x10,
        (
            "２人ともはしゃぎすぎだな……\x01",
            "ま、まあいいか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_1112")

    TalkEnd(0xFE)
    Return()

    # Function_11_1043 end

    def Function_12_1116(): pass

    label("Function_12_1116")

    TalkBegin(0xFE)

    #C0045
    ChrTalk(
        0x11,
        (
            "今日は主人が\x01",
            "連れて来てくれたんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x11,
        (
            "うふふ、テーマパーク\x01",
            "楽しみですの。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1116 end

    def Function_13_1173(): pass

    label("Function_13_1173")

    TalkBegin(0xFE)

    #C0047
    ChrTalk(
        0x12,
        (
            "お父さま、サニータは\x01",
            "かんらんしゃにのりたいですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x12,
        (
            "マリーといっしょに\x01",
            "いちばんたかいところまで\x01",
            "のぼりたいですの。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1173 end

    def Function_14_11F7(): pass

    label("Function_14_11F7")

    TalkBegin(0xFE)

    #C0049
    ChrTalk(
        0x13,
        "ニャーオ……♪\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_11F7 end

    def Function_15_1212(): pass

    label("Function_15_1212")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_1222")
    Jump("loc_1464")

    label("loc_1222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_1230")
    Jump("loc_1464")

    label("loc_1230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_123E")
    Jump("loc_1464")

    label("loc_123E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_124C")
    Jump("loc_1464")

    label("loc_124C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_125A")
    Jump("loc_1464")

    label("loc_125A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_13A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135B")

    #C0050
    ChrTalk(
        0x151,
        (
            "#5705F……今からテーマパークで\x01",
            "遊ぶのかい？\x02\x03",

            "#5702Fみっしぃの着ぐるみを手に入れて\x01",
            "競売会に参加するのも\x01",
            "なかなか面白いかもしれないけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#0006Fそんなの怪しすぎるだろ……\x02\x03",

            "#0000Fと、とにかく。\x01",
            "今はブティックに向かおう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_13A2")

    label("loc_135B")


    #C0052
    ChrTalk(
        0x101,
        (
            "#0000F今はテーマパークに用はないな。\x01",
            "ブティックで正装してこよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A2")

    Jump("loc_1464")

    label("loc_13A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_145B")

    #C0053
    ChrTalk(
        0x101,
        (
            "#0003F今回の目的は《黒の競売会》だ。\x01",
            "テーマパークは諦めるしかないか……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1456")

    #C0054
    ChrTalk(
        0x103,
        "#0208F…………………………\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#0011F（や、やっぱ残念そう……かな？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1456")

    Jump("loc_1464")

    label("loc_145B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1464")

    label("loc_1464")

    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x5)
    Return()

    # Function_15_1212 end

    def Function_16_1478(): pass

    label("Function_16_1478")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadEffect(0x0, "event\\ev309_00.eff")
    FadeToBright(1000, 0)
    OP_68(0, 2200, -47400, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22940, 0)
    SetCameraDistance(21940, 2500)
    SetChrPos(0x101, 600, 0, -49200, 0)
    SetChrPos(0x102, -600, 0, -49200, 0)
    SetChrPos(0x103, 1200, 0, -50700, 0)
    SetChrPos(0x104, -1200, 0, -50700, 0)

    def lambda_1525():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1525)

    def lambda_153A():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_153A)

    def lambda_154F():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_154F)

    def lambda_1564():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1564)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0056
    ChrTalk(
        0x103,
        "#0205F#11Pあ……！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#0005F#5Pあれがテーマパークか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 4500, -47400, 3000)
    MoveCamera(0, 0, 0, 3000)
    OP_6E(600, 0)
    SetCameraDistance(10020, 3000)
    OP_6F(0x79)
    Fade(1000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 4250, -9800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-20, 9500, -8210, 0)
    MoveCamera(337, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27300, 0)
    OP_68(-20, 5300, -8210, 8000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    StopEffect(0x0, 0x0)
    OP_68(-2830, 2200, -34120, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27290, 0)
    SetCameraDistance(25290, 3000)
    OP_90(0x101, -3930, 4000, -37980, 0)
    OP_90(0x102, -4800, 4000, -38790, 0)
    OP_90(0x103, -2750, 4000, -39310, 0)
    OP_90(0x104, -3800, 4000, -40070, 0)

    def lambda_176E():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_176E)
    Sleep(50)

    def lambda_1786():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1786)
    Sleep(50)

    def lambda_179E():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_179E)
    Sleep(50)

    def lambda_17B6():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17B6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)
    OP_0D()
    Sleep(500)

    #C0058
    ChrTalk(
        0x103,
        "#0205F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#0012F#5P何というか……\x01",
            "確かに楽しそうな場所だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#0302F#6Pま、実際大したモンだぜ。\x02\x03",

            "#0304F観覧車にジェットコースター。\x02\x03",

            "ホラーハウスに\x01",
            "メリーゴーラウンド。\x02\x03",

            "#0300Fおとぎ話に出てくるような\x01",
            "中世の城まで建ってやがるしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#0011Fな、なんか凄そうだな。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#0104F#5Pふふ、ＩＢＣが観光の目玉として\x01",
            "オープンさせた施設だから\x01",
            "気合いが入っているのは確かね。\x02\x03",

            "#0102F私もベルに誘われて\x01",
            "一度入ったことがあるけど\x01",
            "とても回りきれなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        "#0205F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 500)

    def lambda_1A09():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1A09)

    def lambda_1A16():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1A16)

    #C0064
    ChrTalk(
        0x101,
        (
            "#0012F#5Pえっと……\x02\x03",

            "#0000F……あまり時間は取れないけど\x01",
            "ちょっと中を覗いてみるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#0208F#6P…………いえ………………\x02\x03",

            "#0206F遊びに来た訳ではないので\x01",
            "わざわざ入る必要は無いかと。\x02\x03",

            "入場料も結構するみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#0303F#6Pまあ、確かに安くはねぇな。\x02\x03",

            "#0300F今から入ったんじゃ\x01",
            "とても元は取れないだろうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#0109F#5P今度、お休みを貰ったら\x01",
            "みんなで遊びに来ましょう。\x02\x03",

            "#0102Fそれこそ午前中から\x01",
            "一日中遊び尽くせるくらいに。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0068
    ChrTalk(
        0x103,
        "#0202F#12P……はい。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -3890, 0, -32460, 0)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xA4, 2)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_16_1478 end

    def Function_17_1C4D(): pass

    label("Function_17_1C4D")

    EventBegin(0x0)
    Fade(500)
    OP_68(8380, 7250, -13860, 0)
    MoveCamera(313, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20350, 0)
    SetChrPos(0x101, 4970, 4250, -11650, 0)
    SetChrPos(0x102, 4400, 4250, -13060, 0)
    SetChrPos(0x103, 6270, 4000, -12400, 315)
    SetChrPos(0x104, 7200, 4000, -11960, 315)
    StopEffect(0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1CE3")
    SetChrPos(0x151, 5580, 4000, -13450, 0)

    label("loc_1CE3")

    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34D, 1)

    #C0070
    ChrTalk(
        0x101,
        "#5P#0005Fん、この指輪は……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#12P#0300Fトマって奴が言ってた\x01",
            "婚約指輪かもしれねぇなぁ。\x02\x03",

            "#0306Fしゃあねぇ、\x01",
            "あとでホテルの部屋に\x01",
            "見せにいくか。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x3)
    OP_65(0x2, 0x1)
    SetChrPos(0x0, 4970, 4250, -11650, 0)
    EventEnd(0x5)
    Return()

    # Function_17_1C4D end

    def Function_18_1DE8(): pass

    label("Function_18_1DE8")

    TalkBegin(0xFF)
    SetChrName("")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "テーマパークの\x01",
            "見取り図が描かれている。\x02\x03",

            "広大な敷地に\x01",
            "さまざまなアミューズメント施設が\x01",
            "並んでいるようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_18_1DE8 end

    def Function_19_1E65(): pass

    label("Function_19_1E65")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   ～こ来園のみなさまへ～\x01\x01",
            "当テーマパーク内での\x01",
            "暴走行為や危険物の持ち込みは\x01",
            "固くお断り申し上げます。\x01\x01",
            "また、お子様には必ず\x01",
            "保護者の方が同伴なさるよう\x01",
            "お願い申し上げます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_1E65 end

    SaveToFile()

Try(main)
