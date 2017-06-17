from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c047c.bin",                # FileName
        "c047c",                    # MapName
        "c047c",                    # Location
        0x0025,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 37, 0, 1, 0, 2],
    )

    BuildStringList((
        "c047c",                  # 0
        "ドレイク・オーナー",     # 1
        "チェリー",               # 2
        "ガレッティ",             # 3
        "エリンデ",               # 4
        "レイタロッサ",           # 5
        "リッケ爺さん",           # 6
        "鉱員ガンツ",             # 7
        "鉱員マルロ",             # 8
        "観光客",                 # 9
        "観光客",                 # 10
        "観光客",                 # 11
        "観光客",                 # 12
        "帝国貴族",               # 13
        "観光客",                 # 14
        "フィリア",               # 15
        "ラン",                   # 16
        "エイダ",                 # 17
    ))

    AddCharChip((
        "chr/ch20002.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch20402.itc",                   # 02
        "chr/ch34300.itc",                   # 03
        "chr/ch23600.itc",                   # 04
        "chr/ch25800.itc",                   # 05
        "chr/ch25900.itc",                   # 06
        "chr/ch26902.itc",                   # 07
        "chr/ch27000.itc",                   # 08
        "chr/ch27100.itc",                   # 09
        "chr/ch33100.itc",                   # 0A
        "chr/ch33302.itc",                   # 0B
        "chr/ch30702.itc",                   # 0C
        "chr/ch26200.itc",                   # 0D
    ))

    DeclNpc(-899,    4000,    21299,   180,  261,  0x0, 0,   5,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(6199,    -1000,   8000,    270,  261,  0x0, 0,   9,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       -1000,   13649,   180,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-6500,   -1000,   6000,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(1350,    -949,    11500,   0,    261,  0x0, 0,   11,  0,   255, 255, 0,   13,  255,  0)
    DeclNpc(6699,    4269,    15750,   90,   261,  0x0, 0,   0,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(6699,    4250,    17979,   90,   277,  0x0, 0,   12,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(6510,    4000,    18979,   135,  261,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       -1000,   4219,    360,  405,  0x0, 0,   1,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-3019,   -1000,   3390,    315,  277,  0x0, 0,   3,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-4519,   -1000,   9789,    225,  261,  0x0, 0,   4,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(50,      4000,    18950,   0,    261,  0x0, 0,   7,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-4570,   -1000,   13279,   0,    405,  0x0, 0,   10,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-3400,   -949,    4409,    270,  261,  0x0, 0,   2,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-900,    4000,    20000,   2000,    -900,    5500,    21300,   0x007E, 0,  3,  0x0000)
    DeclActor(5240,    -1000,   8000,    1200,    6200,    500,     8000,    0x007E, 0,  7,  0x0000)
    DeclActor(-920,    -1000,   12050,   1700,    0,       500,     13650,   0x007E, 0,  9,  0x0000)
    DeclActor(-4500,   -1000,   6000,    1500,    -6500,   500,     6000,    0x007E, 0,  11, 0x0000)
    DeclActor(7530,    4000,    17960,   1800,    7530,    5500,    17960,   0x007C, 0,  26, 0x0000)
    DeclActor(7530,    4000,    15750,   1800,    7530,    5500,    15750,   0x007C, 0,  26, 0x0000)
    DeclActor(7530,    4000,    13410,   1800,    7530,    5500,    13410,   0x007C, 0,  26, 0x0000)
    DeclActor(7530,    4000,    10460,   1800,    7530,    5500,    10460,   0x007C, 0,  26, 0x0000)
    DeclActor(7530,    4000,    8300,    1800,    7530,    5500,    8300,    0x007C, 0,  26, 0x0000)

    ScpFunction((
        "Function_0_460",          # 00, 0
        "Function_1_518",          # 01, 1
        "Function_2_5AF",          # 02, 2
        "Function_3_5EE",          # 03, 3
        "Function_4_5F2",          # 04, 4
        "Function_5_CB1",          # 05, 5
        "Function_6_DE0",          # 06, 6
        "Function_7_E90",          # 07, 7
        "Function_8_E94",          # 08, 8
        "Function_9_1403",         # 09, 9
        "Function_10_1407",        # 0A, 10
        "Function_11_195C",        # 0B, 11
        "Function_12_1960",        # 0C, 12
        "Function_13_1CF4",        # 0D, 13
        "Function_14_2219",        # 0E, 14
        "Function_15_26EF",        # 0F, 15
        "Function_16_2C10",        # 10, 16
        "Function_17_2EF3",        # 11, 17
        "Function_18_3129",        # 12, 18
        "Function_19_3133",        # 13, 19
        "Function_20_31B3",        # 14, 20
        "Function_21_33EB",        # 15, 21
        "Function_22_34F9",        # 16, 22
        "Function_23_37B1",        # 17, 23
        "Function_24_3AEE",        # 18, 24
        "Function_25_3B94",        # 19, 25
        "Function_26_3C31",        # 1A, 26
        "Function_27_3CC3",        # 1B, 27
        "Function_28_3D56",        # 1C, 28
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_527")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 28)

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_550")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x8, -4570, -1000, 14750, 180)
    SetChrFlags(0x8, 0x10)
    Jump("loc_5AE")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_55E")
    Jump("loc_5AE")

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_571")
    SetChrFlags(0x8, 0x10)
    Jump("loc_5AE")

    label("loc_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_58E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_589")
    SetChrFlags(0x8, 0x10)

    label("loc_589")

    Jump("loc_5AE")

    label("loc_58E")

    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x11, 1000, -1000, 3500, 315)

    label("loc_5AE")

    Return()

    # Function_1_518 end

    def Function_2_5AF(): pass

    label("Function_2_5AF")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -6000, -1000, 16000, 5000, 5000, 0)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5ED")
    OP_65(0x0, 0x1)

    label("loc_5ED")

    Return()

    # Function_2_5AF end

    def Function_3_5EE(): pass

    label("Function_3_5EE")

    Call(0, 4)
    Return()

    # Function_3_5EE end

    def Function_4_5F2(): pass

    label("Function_4_5F2")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_665")
    OP_4B(0x14, 0xFF)

    #C0001
    ChrTalk(
        0x8,
        (
            "これは伯爵、\x01",
            "ご無沙汰しておりますな。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "どうぞ、奥の特別席へ\x01",
            "お越しくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_CAD")

    label("loc_665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_6D6")

    #C0003
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "カジノハウス《バルカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "本日もお楽しみ頂けると幸いですな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CAD")

    label("loc_6D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_923")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 1)), scpexpr(EXPR_END)), "loc_7C2")

    #C0005
    ChrTalk(
        0x8,
        (
            "外は混雑したそうですから\x01",
            "迷子など出ないかと\x01",
            "心配していたのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "ふむ……歓楽街にいないとすれば\x01",
            "パレードを追って中央広場の方へ、\x01",
            "という可能性でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "大したお力にもなれず\x01",
            "申し訳ありませんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91E")

    label("loc_7C2")


    #C0008
    ChrTalk(
        0x8,
        (
            "外は随分と\x01",
            "混雑したそうですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "迷子などが出ないか\x01",
            "心配でございますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#0000Fはは、実は……\x01",
            "今迷子の子を捜索中でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "おっとそうでしたか。\x01",
            "これは失礼。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "ふむ、２階では\x01",
            "子供は見ておりませんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "１階のことでしたら\x01",
            "チェリーに聞くのがよろしいかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "チェリーが見ていないようでしたら\x01",
            "当店には来ていないでしょうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 1)

    label("loc_91E")

    Jump("loc_CAD")

    label("loc_923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_98C")

    #C0015
    ChrTalk(
        0x8,
        (
            "外は随分と\x01",
            "混雑したそうですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "迷子などが出ないか\x01",
            "心配でございますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F2")

    label("loc_98C")


    #C0017
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "カジノハウス《バルカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "本日もお楽しみ頂けると幸いですな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_9F2")

    Jump("loc_CAD")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A5E")

    #C0019
    ChrTalk(
        0x8,
        (
            "……お嬢さん、\x01",
            "そろそろおウチに帰んな。\x01",
            "アンタまだ二十#4Rハタチ#前だろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A61")

    label("loc_A5E")

    Call(0, 5)

    label("loc_A61")

    Jump("loc_CAD")

    label("loc_A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B04")

    #C0020
    ChrTalk(
        0x8,
        (
            "……やれやれ。\x01",
            "ランディ、代わってくれねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#0303Fやだね、自分で責任持てっつーの。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "……なに拗ねてやがるんだ、テメー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B07")

    label("loc_B04")

    Call(0, 6)

    label("loc_B07")

    Jump("loc_CAD")

    label("loc_B0C")

    TurnDirection(0x8, 0x104, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B89")

    #C0023
    ChrTalk(
        0x8,
        (
            "確かに客は多いが\x01",
            "別にトラブっちゃいねえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "ランディ、そう心配すんな。\x01",
            "何かありゃあ連絡する。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAD")

    label("loc_B89")


    #C0025
    ChrTalk(
        0x8,
        "……ランディか。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "昨日は散々楽しんだくせに\x01",
            "また来やがったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0300Fんや、今日は仕事だ。\x02\x03",

            "カジノの方は\x01",
            "相変わらず盛況みてえだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "ああ、特にトラブってねえよ。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "何かありゃあ\x01",
            "お前んとこに連絡する。\x01",
            "そう心配すんなや。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0300Fははっ、了解。\x01",
            "また様子を見に来るぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_CAD")

    TalkEnd(0x8)
    Return()

    # Function_4_5F2 end

    def Function_5_CB1(): pass

    label("Function_5_CB1")

    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x13, 0x0)

    #C0031
    ChrTalk(
        0x8,
        (
            "……お嬢さん、そろそろ\x01",
            "おウチに帰ったらどうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "俺は何かと忙しいんだよ。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x13,
        "えー、やだー！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x13,
        (
            "今日はいいの、\x01",
            "お祭りなんだもの～。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D97")

    #C0035
    ChrTalk(
        0x104,
        (
            "#0303F（オーナー、珍しく\x01",
            "  てこずってやがんな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD8")

    label("loc_D97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DD8")

    #C0036
    ChrTalk(
        0x101,
        (
            "#0003F（オーナーさん、\x01",
            "  もててるなぁ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD8")

    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_5_CB1 end

    def Function_6_DE0(): pass

    label("Function_6_DE0")

    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x13, 0x0)

    #C0037
    ChrTalk(
        0x13,
        "ねえねえ、オーナーって幾つなの？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x13,
        "元ヤクザだったってホント～？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "お客さん、酔ってますな。\x01",
            "そのくらいでお控えになっては？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x13,
        "……い～やン㈱㈱\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_6_DE0 end

    def Function_7_E90(): pass

    label("Function_7_E90")

    Call(0, 8)
    Return()

    # Function_7_E90 end

    def Function_8_E94(): pass

    label("Function_8_E94")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13FF")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "交換をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EFD")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_EFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1D")
    OP_AF(0x40)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13FA")

    label("loc_F1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F31")
    Jump("loc_13FA")

    label("loc_F31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13FA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_FA7")

    #C0041
    ChrTalk(
        0x9,
        (
            "記念祭中の大放出は\x01",
            "今日で最後よ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        "みんな頑張って遊んで行ってね～☆\x02",
    )

    CloseMessageWindow()
    Jump("loc_13FA")

    label("loc_FA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_101F")

    #C0043
    ChrTalk(
        0x9,
        (
            "パレードが終わって\x01",
            "みんな戻ってきたみたいね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "みんな～、がんばって\x01",
            "ミラを落として行ってね～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FA")

    label("loc_101F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_11E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 3)), scpexpr(EXPR_END)), "loc_1098")

    #C0045
    ChrTalk(
        0x9,
        (
            "可愛い男のコね～。\x01",
            "でもカジノには来てないかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "あたしお客さんなら\x01",
            "みんな見てるも～ん☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DB")

    label("loc_1098")


    #C0047
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0049
    ChrTalk(
        0x9,
        "え～、迷子のコなの～？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        "カジノには来てないと思うけど～。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "ウチみたいなお店じゃ\x01",
            "子供は目立つしね☆\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#0000Fはは、そうですね……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)

    label("loc_11DB")

    Jump("loc_13FA")

    label("loc_11E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1258")

    #C0053
    ChrTalk(
        0x9,
        (
            "パレードが終わって\x01",
            "みんな戻ってきたみたいね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "みんな～、がんばって\x01",
            "ミラを落として行ってね～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FA")

    label("loc_1258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_12F4")

    #C0055
    ChrTalk(
        0x9,
        (
            "オーナーって\x01",
            "ああ見えてすっごくもてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        "ふう、しょうがないかも～。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "ちょっとキケンな匂いのする所が\x01",
            "くすぐられちゃうのよね～㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FA")

    label("loc_12F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_138D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_133E")

    #C0058
    ChrTalk(
        0x9,
        (
            "ガンツさ～ん、また\x01",
            "ミラを落として行ってね～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1388")

    label("loc_133E")


    #C0059
    ChrTalk(
        0x9,
        "あ、ガンツさんだー。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "うふふ、また\x01",
            "負けに来ちゃったのかしら☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1388")

    Jump("loc_13FA")

    label("loc_138D")


    #C0061
    ChrTalk(
        0x9,
        "ようこそ《バルカ》へ～！\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "記念祭に合わせて\x01",
            "豪華景品も揃えちゃったわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        "ぜひ挑戦してみてね～☆\x02",
    )

    CloseMessageWindow()

    label("loc_13FA")

    Jump("loc_EA1")

    label("loc_13FF")

    TalkEnd(0x9)
    Return()

    # Function_8_E94 end

    def Function_9_1403(): pass

    label("Function_9_1403")

    Call(0, 10)
    Return()

    # Function_9_1403 end

    def Function_10_1407(): pass

    label("Function_10_1407")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1414")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1958")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                    # 0
            "ポーカーで遊ぶ\x01",              # 1
            "ブラックジャックで遊ぶ\x01",      # 2
            "やめる\x01",                      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_148B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_148B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DB")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_14DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152B")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_152B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153F")
    Jump("loc_1953")

    label("loc_153F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1953")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_15D1")

    #C0064
    ChrTalk(
        0xA,
        (
            "伯爵のお相手は\x01",
            "オーナーが自らなさるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "フフ、大金で遊ばれる\x01",
            "大切なお客様ですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164C")

    label("loc_15D1")


    #C0066
    ChrTalk(
        0xA,
        (
            "伯爵は毎年この時期に\x01",
            "よく立ち寄ってくださるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        (
            "特別室常連客のお一人……\x01",
            "大金で遊ばれる太っ腹な方ですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_164C")

    Jump("loc_1953")

    label("loc_1651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_16F7")

    #C0068
    ChrTalk(
        0xA,
        (
            "人にはそれぞれ\x01",
            "器というものがございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        "フフ、皆様もお気をつけ下さいませ。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "己の器を越えて賭けをなされば、\x01",
            "結果は見えてございましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1953")

    label("loc_16F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_185E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_178D")

    #C0071
    ChrTalk(
        0xA,
        (
            "賭け事はついつい\x01",
            "熱くなってしまうものでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "記念祭だからといって\x01",
            "羽目を外しすぎるのは\x01",
            "よろしくありませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1859")

    label("loc_178D")


    #C0073
    ChrTalk(
        0xA,
        (
            "賭け事はマナーを守って、が\x01",
            "原則でございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "いくら祭りだからといって\x01",
            "羽目を外しすぎるのは\x01",
            "よろしくありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        (
            "普段より少しだけ\x01",
            "チップを上乗せして……\x01",
            "そんな加減が宜しいかと思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1859")

    Jump("loc_1953")

    label("loc_185E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_18EB")

    #C0076
    ChrTalk(
        0xA,
        (
            "観光に来られた方が\x01",
            "ほぼ必ず立ち寄られる場所……\x01",
            "それがこの歓楽街でございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "ふう……\x01",
            "本日も大盛況でございますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1953")

    label("loc_18EB")


    #C0078
    ChrTalk(
        0xA,
        (
            "いらっしゃいませ。\x01",
            "こちらはカード台でございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "記念祭の思い出に\x01",
            "皆様も一勝負いかがですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1953")

    Jump("loc_1414")

    label("loc_1958")

    TalkEnd(0xA)
    Return()

    # Function_10_1407 end

    def Function_11_195C(): pass

    label("Function_11_195C")

    Call(0, 12)
    Return()

    # Function_11_195C end

    def Function_12_1960(): pass

    label("Function_12_1960")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_196D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF0")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",              # 0
            "ルーレットで遊ぶ\x01",      # 1
            "やめる\x01",                # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19CF")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_19CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1F")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_1A1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A33")
    Jump("loc_1CEB")

    label("loc_1A33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CEB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1B59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1AE3")

    #C0080
    ChrTalk(
        0xB,
        (
            "記念祭も最終日ですし、\x01",
            "何かいいことがあるかもしれませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xB,
        (
            "……うふふ、根拠はないですけど。\x01",
            "一勝負お試しになっては？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B54")

    label("loc_1AE3")


    #C0082
    ChrTalk(
        0xB,
        (
            "いらっしゃいませ。\x01",
            "ルーレットはいかが？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "記念祭も最終日ですし、\x01",
            "何かいいことがあるかもしれませんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1B54")

    Jump("loc_1CEB")

    label("loc_1B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1B8F")

    #C0084
    ChrTalk(
        0xB,
        "うふふ、楽しんで頂けましたかしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CEB")

    label("loc_1B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1C0B")

    #C0085
    ChrTalk(
        0xB,
        (
            "いらっしゃいませ。\x01",
            "カジノハウス《バルカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xB,
        (
            "丁度台が空きましたわ。\x01",
            "お客様もいかがかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEB")

    label("loc_1C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C7F")

    #C0087
    ChrTalk(
        0xB,
        (
            "うふふ……皆様も勝負では\x01",
            "手を抜かれないことですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xB,
        (
            "情けは無用。\x01",
            "それが賭け事の掟ですもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEB")

    label("loc_1C7F")


    #C0089
    ChrTalk(
        0xB,
        (
            "記念祭の間は\x01",
            "賭け事も盛り上がりますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xB,
        (
            "ふふ、どうぞおかけになって。\x01",
            "まだ席が空いておりますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CEB")

    Jump("loc_196D")

    label("loc_1CF0")

    TalkEnd(0xB)
    Return()

    # Function_12_1960 end

    def Function_13_1CF4(): pass

    label("Function_13_1CF4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D88")
    Jump("loc_1DD2")

    label("loc_1D88")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DA8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DD2")

    label("loc_1DA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DC8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DD2")

    label("loc_1DC8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DD2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1E8B")

    #C0091
    ChrTalk(
        0xC,
        (
            "あら……あれって帝国の\x01",
            "カーライル伯爵じゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        "帝国東部の有力貴族よ。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xC,
        (
            "毎年記念祭に来てるって噂は\x01",
            "本当だったみたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2211")

    label("loc_1E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1F1E")

    #C0094
    ChrTalk(
        0xC,
        (
            "アルカンシェルの公演、\x01",
            "今日も盛況みたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xC,
        (
            "私ももう一度\x01",
            "観に行きたいものだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xC,
        (
            "うふふ、どこかで\x01",
            "手に入らないかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2211")

    label("loc_1F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_204A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1F82")

    #C0097
    ChrTalk(
        0xC,
        (
            "もしかして事務仕事も\x01",
            "自分でやっているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xC,
        "市長さんも大変ね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2045")

    label("loc_1F82")


    #C0099
    ChrTalk(
        0xC,
        (
            "マクダエル市長は連日\x01",
            "会談や祝賀会に呼ばれているそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xC,
        (
            "市長の立場なら\x01",
            "無理ないことだと思うけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xC,
        (
            "確か市長の秘書って\x01",
            "逮捕されているのよね。\x01",
            "事務仕事はどうしているのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2045")

    Jump("loc_2211")

    label("loc_204A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_20D5")

    #C0102
    ChrTalk(
        0xC,
        (
            "クロスベルには今の時期\x01",
            "『偽ブランド業者』が出没するそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xC,
        (
            "うふふ、庶民の欲望に\x01",
            "付け込んだ商売って訳ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A2")

    label("loc_20D5")


    #C0104
    ChrTalk(
        0xC,
        (
            "そういえば……\x01",
            "アナタたち知ってる？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xC,
        (
            "クロスベルには今の時期\x01",
            "『偽ブランド業者』が出没するのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xC,
        (
            "一度はあの百貨店に\x01",
            "偽ブランドを卸そうとしたとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xC,
        (
            "うふふ、油断ならない\x01",
            "連中みたいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_21A2")

    Jump("loc_2211")

    label("loc_21A7")


    #C0108
    ChrTalk(
        0xC,
        (
            "イリア・プラティエか……\x01",
            "確かに噂以上に衝撃だったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xC,
        (
            "うふふ、チケットが\x01",
            "高価なのも頷けるわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2211")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_1CF4 end

    def Function_14_2219(): pass

    label("Function_14_2219")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22AD")
    Jump("loc_22F7")

    label("loc_22AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22F7")

    label("loc_22CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22ED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22F7")

    label("loc_22ED")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22F7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_23C0")

    #C0110
    ChrTalk(
        0xD,
        (
            "祭りが終われば\x01",
            "ツキが消えてしまう気がしてな。\x01",
            "毎年最終日はしんみりしてしまうワイ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xD,
        (
            "いかんいかん、今日は\x01",
            "打ちまくってやらんとのう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2454")

    label("loc_23C0")


    #C0112
    ChrTalk(
        0xD,
        "今日も出します、出させます！\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xD,
        "……今のうちに稼いでおかんとのう。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xD,
        (
            "なんとなく、記念祭が終われば\x01",
            "ツキが消えてしまう気がするんじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_2454")

    Jump("loc_26E7")

    label("loc_2459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2573")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_24D4")

    #C0115
    ChrTalk(
        0xD,
        (
            "祭りといっても\x01",
            "記者や警察なんかは\x01",
            "普段以上に忙しくなるんじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xD,
        "ほっほ、働け若者どもよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_256E")

    label("loc_24D4")


    #C0117
    ChrTalk(
        0xD,
        (
            "表はパレードで\x01",
            "大した賑わいじゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xD,
        (
            "雑誌の記者じゃろうか、\x01",
            "カメラを持って追いかけておる\x01",
            "青年もおったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xD,
        "ほっほ、ご苦労な事じゃの。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_256E")

    Jump("loc_26E7")

    label("loc_2573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_25CA")

    #C0120
    ChrTalk(
        0xD,
        "スロットの調子も良さそうじゃ。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xD,
        "むほほ、稼がんとのー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2643")

    label("loc_25CA")


    #C0122
    ChrTalk(
        0xD,
        (
            "婆さんめ、今日もワシの\x01",
            "カジノ通いを妨害しようとしたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xD,
        (
            "フン、まだまだ！\x01",
            "ワシはこの程度で負けるものか！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_2643")

    Jump("loc_26E7")

    label("loc_2648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2692")

    #C0124
    ChrTalk(
        0xD,
        "おー、出よる出よる！\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xD,
        "むほほ、笑いが止まらんのう！\x02",
    )

    CloseMessageWindow()
    Jump("loc_26E7")

    label("loc_2692")


    #C0126
    ChrTalk(
        0xD,
        "おっほっほ、出よる出よる！\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "さすがは記念祭じゃ、\x01",
            "スロットも景気がいいのう！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_2219 end

    def Function_15_26EF(): pass

    label("Function_15_26EF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2783")
    Jump("loc_27CD")

    label("loc_2783")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_27A3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27CD")

    label("loc_27A3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27C3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27CD")

    label("loc_27C3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27CD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2927")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C1")

    #C0128
    ChrTalk(
        0xFE,
        (
            "うぐぅ……\x01",
            "また負けちまった……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "昨日は大当たりがあたったから\x01",
            "ツキは来てるハズなんだけどな……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        "くそ、今夜こそ勝負だぜ！\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        "#0203F……典型的なハマりパターンですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2922")

    label("loc_28C1")


    #C0132
    ChrTalk(
        0xFE,
        (
            "昨日は大当たりがあたったから\x01",
            "ツキは来てるハズなんだけどな……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "くそ、今夜こそ勝負だぜ！\x02",
    )

    CloseMessageWindow()

    label("loc_2922")

    Jump("loc_2C08")

    label("loc_2927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_29DC")

    #C0134
    ChrTalk(
        0xFE,
        "おい、聞いてくれよ。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "昨日このスロットで\x01",
            "なんと大当たりを当てちまったんだ！\x01",
            "大フィーバーだぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "……ま、今まで負けた分に比べりゃ\x01",
            "全然足りないんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C08")

    label("loc_29DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2B7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEC")

    #C0137
    ChrTalk(
        0xFE,
        (
            "昨日、ルーレットで\x01",
            "負けちまったんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "ああぁ……あの玉が\x01",
            "あとほんの１リジュだけ\x01",
            "右側に逸れてくれてたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#0303Fその気持ち、分かる……！\x02\x03",

            "#0309F女神ももうちょい\x01",
            "サービスしてくれても\x01",
            "いいのになぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        "#0006F……同調するなよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2B78")

    label("loc_2AEC")


    #C0141
    ChrTalk(
        0xFE,
        (
            "あのルーレットの玉が\x01",
            "あとほんの１リジュだけ\x01",
            "右側にそれてくれてたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "……ちくしょーっ！\x01",
            "この負けはスロットで\x01",
            "取り返してやるよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B78")

    Jump("loc_2C08")

    label("loc_2B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2C08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B98")
    Call(0, 17)
    Jump("loc_2C08")

    label("loc_2B98")


    #C0143
    ChrTalk(
        0xFE,
        (
            "う～……まだ頭がいてぇ。\x01",
            "完全に二日酔いだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "チッ、完全に潰れてるロージーが\x01",
            "うらやましいくらいだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C08")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_26EF end

    def Function_16_2C10(): pass

    label("Function_16_2C10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2CA9")

    #C0145
    ChrTalk(
        0xFE,
        (
            "昨日大勝ちしてたんだけど、\x01",
            "今日の負けで完全にパーに\x01",
            "なっちゃったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "結局カジノって、\x01",
            "店側が儲かるように\x01",
            "出来てるんだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EEF")

    label("loc_2CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D17")

    #C0147
    ChrTalk(
        0xFE,
        (
            "ガンツが勝つなんて\x01",
            "めずらしいなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "この辺りでやめといた方が\x01",
            "いいと思うんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EEF")

    label("loc_2D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE0")

    #C0149
    ChrTalk(
        0xFE,
        (
            "ガンツのやつと\x01",
            "毎日カジノに来てるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "大穴狙いばっかしてるから\x01",
            "ちっとも勝てないらしくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "一発で今までの負けを\x01",
            "取り戻そうなんて\x01",
            "夢見すぎだとは思わないか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2E6B")

    label("loc_2DE0")


    #C0152
    ChrTalk(
        0xFE,
        (
            "ガンツがカジノでスッちまうのは、\x01",
            "大穴狙いばっかりしてるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "一発で今までの負けを\x01",
            "取り戻そうなんて\x01",
            "夢見すぎだとは思わないか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E6B")

    Jump("loc_2EEF")

    label("loc_2E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2EEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E8B")
    Call(0, 17)
    Jump("loc_2EEF")

    label("loc_2E8B")


    #C0154
    ChrTalk(
        0xFE,
        (
            "ガンツに付き合って\x01",
            "クロスベルに遊びに来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "記念祭中はずっと\x01",
            "こっちにいるつもりだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EEF")

    TalkEnd(0xFE)
    Return()

    # Function_16_2C10 end

    def Function_17_2EF3(): pass

    label("Function_17_2EF3")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0xF, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F8F")
    Jump("loc_2FD9")

    label("loc_2F8F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2FAF")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FD9")

    label("loc_2FAF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FCF")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FD9")

    label("loc_2FCF")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FD9")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    TurnDirection(0xF, 0xE, 0)

    #C0156
    ChrTalk(
        0xE,
        (
            "う～……\x01",
            "頭がまだガンガンするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xF,
        "どう考えても飲みすぎだな。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xF,
        (
            "……でも町長もいい人だよな。\x01",
            "記念祭だからって鉱員全員に\x01",
            "酒を振舞うなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xE,
        (
            "お陰でロージーのヤツは\x01",
            "いまだに赤レンガ亭で\x01",
            "寝てやがるけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xE,
        (
            "……ま、昨日は楽しかったし\x01",
            "よしとするか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    OP_93(0xF, 0x87, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_17_2EF3 end

    def Function_18_3129(): pass

    label("Function_18_3129")

    TalkBegin(0xFE)
    Call(0, 19)
    TalkEnd(0xFE)
    Return()

    # Function_18_3129 end

    def Function_19_3133(): pass

    label("Function_19_3133")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0161
    ChrTalk(
        0x11,
        "あんた、がんばってよ！\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x11,
        (
            "１０倍くらいにして\x01",
            "ミシュラムで遊ぶんだからねっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x10,
        "ははは、まっかしとけ！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_19_3133 end

    def Function_20_31B3(): pass

    label("Function_20_31B3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3247")
    Jump("loc_3291")

    label("loc_3247")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3267")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3291")

    label("loc_3267")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3287")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3291")

    label("loc_3287")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3291")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_32F3")
    SetChrSubChip(0x15, 0x0)

    #C0164
    ChrTalk(
        0x15,
        (
            "今度こそ、今度こそは……\x01",
            "……畜生！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E3")

    label("loc_32F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3396")

    #C0165
    ChrTalk(
        0x15,
        (
            "うおお……\x01",
            "一晩勝ちまくったのに～……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x15,
        (
            "さ、最後の一勝負で\x01",
            "全部持っていかれちまったぁ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x15,
        (
            "お、俺のミラが……\x01",
            "……チップの山がっ………！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E3")

    label("loc_3396")


    #C0168
    ChrTalk(
        0x15,
        "おっ、君らも勝負するのかい？\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x15,
        (
            "ははは、あんま\x01",
            "やり込まねえようにな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_31B3 end

    def Function_21_33EB(): pass

    label("Function_21_33EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_342D")

    #C0170
    ChrTalk(
        0x11,
        (
            "あ、あんた～……\x01",
            "あんま熱くなんないでよ～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F5")

    label("loc_342D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_34AB")

    #C0171
    ChrTalk(
        0x11,
        (
            "あああ～～～っ……\x01",
            "最後の勝負だったのにぃ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x11,
        (
            "ディーラーの人、イカサマ\x01",
            "したんじゃないでしょうね！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F5")

    label("loc_34AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_34F2")

    #C0173
    ChrTalk(
        0x11,
        (
            "きゃっ、すっごーい！\x01",
            "また勝った！\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x11,
        "さっすがね！\x02",
    )

    CloseMessageWindow()
    Jump("loc_34F5")

    label("loc_34F2")

    Call(0, 19)

    label("loc_34F5")

    TalkEnd(0xFE)
    Return()

    # Function_21_33EB end

    def Function_22_34F9(): pass

    label("Function_22_34F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_35C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3569")

    #C0175
    ChrTalk(
        0x12,
        (
            "やはり儲けられると\x01",
            "気持ちがいいものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x12,
        (
            "来年もこのカジノに\x01",
            "来るとしよう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C4")

    label("loc_3569")


    #C0177
    ChrTalk(
        0x12,
        (
            "今年はかなり\x01",
            "儲けさせてもらった……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x12,
        (
            "来年の記念祭も\x01",
            "このカジノに来るとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_35C4")

    Jump("loc_37AD")

    label("loc_35C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_36B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3642")

    #C0179
    ChrTalk(
        0x12,
        (
            "調子がいい日はどんどん\x01",
            "勝負を重ねるべきだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x12,
        (
            "……もちろん、止め時は\x01",
            "冷静に見極めねばな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B2")

    label("loc_3642")


    #C0181
    ChrTalk(
        0x12,
        "……今日は調子がいい……\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x12,
        (
            "そんな日はどんどん\x01",
            "勝負を重ねるべきだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x12,
        "俺も今日は調子がいい。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_36B2")

    Jump("loc_37AD")

    label("loc_36B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3743")

    #C0184
    ChrTalk(
        0x12,
        (
            "……損をすることと\x01",
            "負ける事は全く違う……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x12,
        (
            "１つ損をしても\x01",
            "最後に大勝ちする事もあるわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x12,
        "賭け事は奥が深い……\x02",
    )

    CloseMessageWindow()
    Jump("loc_37AD")

    label("loc_3743")


    #C0187
    ChrTalk(
        0x12,
        (
            "……ルーレットは\x01",
            "流れの勝負だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x12,
        (
            "熱くなって大きく出ると\x01",
            "損をする……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x12,
        "自制心が大切なんだ。\x02",
    )

    CloseMessageWindow()

    label("loc_37AD")

    TalkEnd(0xFE)
    Return()

    # Function_22_34F9 end

    def Function_23_37B1(): pass

    label("Function_23_37B1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3845")
    Jump("loc_388F")

    label("loc_3845")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3865")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_388F")

    label("loc_3865")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3885")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_388F")

    label("loc_3885")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_388F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3994")
    SetChrSubChip(0x13, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_391C")

    #C0190
    ChrTalk(
        0x13,
        "ぐびぐび……ぷはぁ～。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x13,
        (
            "オーナーのバカ。\x01",
            "あたしとお喋りしようよぅ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_398F")

    label("loc_391C")


    #C0192
    ChrTalk(
        0x13,
        (
            "ぐびぐび……\x01",
            "オーナーったらあたしを捨てて……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x13,
        (
            "オトコの相手するなんて何事よう！\x01",
            "ぐびぐび、ぐびぐび……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_398F")

    Jump("loc_3AE6")

    label("loc_3994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3A16")

    #C0194
    ChrTalk(
        0x13,
        (
            "オーナーったら\x01",
            "ちっとも相手してくれないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x13,
        (
            "んもう、ホントにいけずぅ！\x01",
            "でもムキになる所がカ・ワ・イ・イ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AE6")

    label("loc_3A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3A8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3A84")
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x13, 0x0)

    #C0196
    ChrTalk(
        0x13,
        (
            "オーナーのイジワルぅ、\x01",
            "いけずぅ～～……！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x13,
        "でもそこが好きかも㈱㈱\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_3A87")

    label("loc_3A84")

    Call(0, 5)

    label("loc_3A87")

    Jump("loc_3AE6")

    label("loc_3A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3AE3")

    #C0198
    ChrTalk(
        0x13,
        "んふ、あたし好みかも㈱\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x13,
        (
            "今日は帰んないで\x01",
            "泊まっちゃうも～ん㈱㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AE6")

    label("loc_3AE3")

    Call(0, 6)

    label("loc_3AE6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_37B1 end

    def Function_24_3AEE(): pass

    label("Function_24_3AEE")

    TalkBegin(0xFE)
    OP_4B(0x8, 0xFF)

    #C0200
    ChrTalk(
        0x14,
        (
            "フ……それでは今年も\x01",
            "楽しませてもらうとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x14,
        (
            "ドレイク君、部屋の準備は\x01",
            "できているのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "ご案内いたしましょう。\x01",
            "どうぞ、奥の方へ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_24_3AEE end

    def Function_25_3B94(): pass

    label("Function_25_3B94")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C30")
    OP_29(0x46, 0x1, 0x2)

    #C0203
    ChrTalk(
        0x101,
        (
            "#0003F（よし、歓楽街の聞き込みは\x01",
            "  これで十分だな。）\x02\x03",

            "#0001F（次は裏通りだ……\x01",
            "  同じように聞き込みを進めていこう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 3)

    label("loc_3C30")

    Return()

    # Function_25_3B94 end

    def Function_26_3C31(): pass

    label("Function_26_3C31")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "スロットで遊ぶ\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CBF")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_3CBF")

    TalkEnd(0xFF)
    Return()

    # Function_26_3C31 end

    def Function_27_3CC3(): pass

    label("Function_27_3CC3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D55")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CF1")
    Sleep(500)
    Jump("loc_3D39")

    label("loc_3CF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D08")
    Sleep(150)
    Jump("loc_3D39")

    label("loc_3D08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D1F")
    Sleep(200)
    Jump("loc_3D39")

    label("loc_3D1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D36")
    Sleep(300)
    Jump("loc_3D39")

    label("loc_3D36")

    Sleep(400)

    label("loc_3D39")

    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    Jump("Function_27_3CC3")

    label("loc_3D55")

    Return()

    # Function_27_3CC3 end

    def Function_28_3D56(): pass

    label("Function_28_3D56")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch36300.itc", 0x1E)
    LoadChrToIndex("chr/ch36400.itc", 0x1F)
    LoadChrToIndex("chr/ch36500.itc", 0x20)
    LoadEffect(0x0, "event\\ev300_00.eff")
    LoadEffect(0x1, "event\\ev399_00.eff")
    ClearMapObjFlags(0x7, 0x4)
    OP_68(-4120, 4270, 6410, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(20500, 0)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x104, -3700, -1200, 6430, 315)
    SetChrPos(0x16, -3370, -1000, 7440, 315)
    SetChrPos(0x18, -2450, -1000, 5890, 315)
    SetChrPos(0x17, -3450, -1000, 5410, 315)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrChipByIndex(0x18, 0x20)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    OP_68(-6000, 0, 8000, 0)
    MoveCamera(43, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -5950, -70, 8050, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    MoveCamera(33, 33, 0, 4000)
    SetCameraDistance(17500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_68(-4120, 0, 6410, 2000)
    MoveCamera(80, 23, 0, 2000)
    SetCameraDistance(19000, 2000)
    Sleep(3000)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 136000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1332, 255, 100, 0)    #voice#Randy
    Sound(506, 0, 100, 0)
    Sound(565, 0, 100, 0)
    Sleep(5000)
    Sound(85, 0, 100, 0)
    Sleep(500)
    Sound(1290, 255, 100, 0)    #voice#Randy

    def lambda_3F61():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_3F61)

    def lambda_3F6E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3F6E)

    def lambda_3F7B():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3F7B)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    BeginChrThread(0x16, 1, 0, 27)
    BeginChrThread(0x18, 1, 0, 27)
    BeginChrThread(0x17, 1, 0, 27)
    Sleep(2000)
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 7)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_3D56 end

    SaveToFile()

Try(main)
