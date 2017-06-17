from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "乗組員サルサ",           # 1
        "ジェイムズ",             # 2
        "ニキータ",               # 3
        "男の子",                 # 4
        "男性",                   # 5
        "女性",                   # 6
        "観光客",                 # 7
        "ボンド",                 # 8
        "クレイユ",               # 9
        "サニータ",               # 10
        "マリー",                 # 11
        "ペーター",               # 12
        "特級釣師ロイド",         # 13
        "キリカ",                 # 14
        "レクター",               # 15
        "水上バス",               # 16
        "乗客",                   # 17
        "乗客",                   # 18
        "乗客",                   # 19
        "乗客",                   # 20
        "乗客",                   # 21
        "乗客",                   # 22
        "乗客",                   # 23
        "乗客",                   # 24
        "SE制御",                 # 25
        "テーマパーク方面",       # 26
        "邸宅方面",               # 27
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

    PlaceName(-5.0, 0.0, 95.0, 0x0000, 0x0000, "テーマパーク方面")
    PlaceName(-95.0, 0.0, 20.0, 0x0000, 0x0000, "邸宅方面")
    PlaceName(1.0, 0.0, 17.5, 0x0000, 0x0052, "")

    ScpFunction((
        "Function_0_4E0",          # 00, 0
        "Function_1_598",          # 01, 1
        "Function_2_64A",          # 02, 2
        "Function_3_7AD",          # 03, 3
        "Function_4_89E",          # 04, 4
        "Function_5_8FE",          # 05, 5
        "Function_6_98A",          # 06, 6
        "Function_7_A59",          # 07, 7
        "Function_8_B25",          # 08, 8
        "Function_9_B96",          # 09, 9
        "Function_10_C01",         # 0A, 10
        "Function_11_D4B",         # 0B, 11
        "Function_12_DB8",         # 0C, 12
        "Function_13_DEC",         # 0D, 13
        "Function_14_ED4",         # 0E, 14
        "Function_15_EEF",         # 0F, 15
        "Function_16_12DB",        # 10, 16
        "Function_17_13C9",        # 11, 17
        "Function_18_149D",        # 12, 18
        "Function_19_211B",        # 13, 19
        "Function_20_2170",        # 14, 20
        "Function_21_219C",        # 15, 21
        "Function_22_21F8",        # 16, 22
        "Function_23_2254",        # 17, 23
        "Function_24_22B0",        # 18, 24
        "Function_25_230C",        # 19, 25
        "Function_26_2331",        # 1A, 26
        "Function_27_24D4",        # 1B, 27
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_838")

    #C0001
    ChrTalk(
        0xFE,
        (
            "クロスベル市への便が\x01",
            "先程出発いたしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "次の便も間もなく到着しますので\x01",
            "ご利用の方はしばらくお待ちください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89A")

    label("loc_838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_89A")

    #C0003
    ChrTalk(
        0xFE,
        "水上バスの旅、お疲れ様でした。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "ミシュラムでの夢の一時を\x01",
            "お楽しみくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89A")

    TalkEnd(0xFE)
    Return()

    # Function_3_7AD end

    def Function_4_89E(): pass

    label("Function_4_89E")

    TalkBegin(0xFE)
    TurnDirection(0x9, 0xA, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BA")
    Call(0, 6)
    Jump("loc_8FA")

    label("loc_8BA")


    #C0005
    ChrTalk(
        0xFE,
        (
            "はっはっは……\x01",
            "妻には出張と言ってある。\x01",
            "心配はいらないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FA")

    TalkEnd(0xFE)
    Return()

    # Function_4_89E end

    def Function_5_8FE(): pass

    label("Function_5_8FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91A")
    TurnDirection(0xA, 0x9, 0)
    Call(0, 6)
    Jump("loc_986")

    label("loc_91A")


    #C0006
    ChrTalk(
        0xFE,
        (
            "あのオークションには\x01",
            "前々から興味があったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "ウフフ……連れてきてもらえて\x01",
            "ラッキーだったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_986")

    TalkEnd(0xFE)
    Return()

    # Function_5_8FE end

    def Function_6_98A(): pass

    label("Function_6_98A")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0008
    ChrTalk(
        0x9,
        "今夜は議長邸でパーティだ。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "君の為に美しい装飾品を\x01",
            "落札してあげようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        (
            "ウフフ……悪い人。\x01",
            "奥さんがいるくせに。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "はっはっは……\x01",
            "今夜はそれは言わない約束だろう？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_6_98A end

    def Function_7_A59(): pass

    label("Function_7_A59")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEA")

    #C0012
    ChrTalk(
        0xFE,
        (
            "さきに降りたお兄ちゃんが\x01",
            "スゴい速さで走っていったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "そんなに楽しみだったんだね～。\x01",
            "僕もたっぷり楽しもうっと！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B21")

    label("loc_AEA")


    #C0014
    ChrTalk(
        0xFE,
        (
            "今日はお父さんもいるし……\x01",
            "たっぷり楽しもうっと！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B21")

    TalkEnd(0xFE)
    Return()

    # Function_7_A59 end

    def Function_8_B25(): pass

    label("Function_8_B25")

    TalkBegin(0xFE)

    #C0015
    ChrTalk(
        0xFE,
        (
            "よーし、早速テーマパークに\x01",
            "向かうとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "今日はお父さん、\x01",
            "どんな乗り物でも付き合うからな！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_B25 end

    def Function_9_B96(): pass

    label("Function_9_B96")

    TalkBegin(0xFE)

    #C0017
    ChrTalk(
        0xFE,
        (
            "あらあら、あなたったら\x01",
            "強がっちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "ふふ、それなら遠慮なく\x01",
            "怖いのに乗っちゃいましょ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_B96 end

    def Function_10_C01(): pass

    label("Function_10_C01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD3")

    #C0019
    ChrTalk(
        0xFE,
        (
            "記念祭を楽しんでから\x01",
            "来ようと思ってたら\x01",
            "結局夕方になっちゃったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "仕方ない、\x01",
            "ブティックあたりを冷やかしたら\x01",
            "とっとと帰るとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "帰りの混雑に巻き込まれたら\x01",
            "最悪だしね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D47")

    label("loc_CD3")


    #C0022
    ChrTalk(
        0xFE,
        (
            "来るのが遅くなっちゃったよ。\x01",
            "あんまり遊べないだろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "ブティックだけ冷やかして\x01",
            "とっとと帰るとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D47")

    TalkEnd(0xFE)
    Return()

    # Function_10_C01 end

    def Function_11_D4B(): pass

    label("Function_11_D4B")

    TalkBegin(0xFE)

    #C0024
    ChrTalk(
        0xF,
        (
            "はは、愉快愉快。\x01",
            "今日は家族で遊んでしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xF,
        (
            "たまにはこんな息抜きも\x01",
            "悪くない気がするよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_D4B end

    def Function_12_DB8(): pass

    label("Function_12_DB8")

    TalkBegin(0xFE)

    #C0026
    ChrTalk(
        0x10,
        (
            "ホテルは満室でしたの……\x01",
            "残念ですわ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_DB8 end

    def Function_13_DEC(): pass

    label("Function_13_DEC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E3A")

    #C0027
    ChrTalk(
        0x11,
        (
            "お父さまとお母さま……\x01",
            "またつれてきてくれないかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED0")

    label("loc_E3A")


    #C0028
    ChrTalk(
        0x11,
        (
            "お父さまのおしごとがあるから、\x01",
            "きょうはかえらなくてはいけないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x11,
        (
            "……それに\x01",
            "マリーもつかれていますし。\x01",
            "サニータ、きょうはかえりますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_ED0")

    TalkEnd(0xFE)
    Return()

    # Function_13_DEC end

    def Function_14_ED4(): pass

    label("Function_14_ED4")

    TalkBegin(0xFE)

    #C0030
    ChrTalk(
        0x12,
        "フニャアァ……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_ED4 end

    def Function_15_EEF(): pass

    label("Function_15_EEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1051")

    #C0031
    ChrTalk(
        0xFE,
        (
            "おや、ロイド団員も\x01",
            "釣りに来られたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "うふふ、やはり貴方も\x01",
            "釣り大会の熱が冷め止まないんですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "そうだ、釣りエサはお持ちですか？\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "５個を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x187, 5)

    #C0035
    ChrTalk(
        0xFE,
        "少しですが、おすそ分けです。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "うふふ、ロイド団員も\x01",
            "頑張ってくださいねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD9, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_104C")
    SetScenarioFlags(0xD9, 1)

    label("loc_104C")

    Jump("loc_12D7")

    label("loc_1051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x187, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_116B")

    #C0037
    ChrTalk(
        0xFE,
        (
            "おや、ロイド団員。\x01",
            "もしや釣りエサが\x01",
            "足りなくなってしまったのでは？\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "２個を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x187, 2)

    #C0039
    ChrTalk(
        0xFE,
        "少しですが、おすそ分けです。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "うふふ、ロイド団員も熱心ですねえ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD9, 1)
    Jump("loc_12D7")

    label("loc_116B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_11DB")

    #C0041
    ChrTalk(
        0xFE,
        (
            "おや、流れが\x01",
            "変わってきましたねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "残念です、今日は\x01",
            "この辺りでお開きでしょうかねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D7")

    label("loc_11DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_12D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129C")

    #C0043
    ChrTalk(
        0xFE,
        (
            "こちらのロイド師が\x01",
            "対岸の方でも釣ってみたいと\x01",
            "仰いましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "ふふっ、さすが特級釣師の方は\x01",
            "読みが違いますねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "今日は魚の食い入れが\x01",
            "素晴らしいですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_12D7")

    label("loc_129C")


    #C0046
    ChrTalk(
        0xFE,
        (
            "さすが特級釣師の方は\x01",
            "素晴らしい読みをなさいますねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D7")

    TalkEnd(0xFE)
    Return()

    # Function_15_EEF end

    def Function_16_12DB(): pass

    label("Function_16_12DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1349")

    #C0047
    ChrTalk(
        0xFE,
        "ふむ、今日はこんな所か……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "グラトンバスの大物が釣れたから\x01",
            "良しとしようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13C5")

    label("loc_1349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_13C5")

    #C0049
    ChrTalk(
        0xFE,
        (
            "記念祭が終わったら\x01",
            "リベールに帰る予定なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "クロスベルでできる\x01",
            "釣りスタイルは\x01",
            "全て試しておかないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C5")

    TalkEnd(0xFE)
    Return()

    # Function_16_12DB end

    def Function_17_13C9(): pass

    label("Function_17_13C9")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0051
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1498")
    OP_E0(0x2)
    MiniGame(0x6, 0x3, 0xFFFFA04C, 0xFFFFF060, 0xFFFF4912, 0x0, 0xFFFFA056, 0xFFFFE890, 0xFFFF6852)

    label("loc_1498")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_17_13C9 end

    def Function_18_149D(): pass

    label("Function_18_149D")

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

    def lambda_181B():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_181B)
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
            "#0008F#5P──ここがミシュラムか。\x02\x03",

            "#0006F何ていうか、想像以上に\x01",
            "ゴージャスそうな場所だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x103,
        (
            "#0203F#5P元々、高級保養地だった所に\x01",
            "ＩＢＣがリゾート開発を着手……\x02\x03",

            "#0200Fホテルとテーマパークが出来たのが\x01",
            "２年ほど前らしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        (
            "#0104F#5Pええ、以来アルカンシェルと並んで\x01",
            "観光地としての目玉になっているわね。\x02\x03",

            "#0100F正面にあるのはホテルで\x01",
            "１階がアーケードになっているわ。\x02\x03",

            "レストラン、ブティック、\x01",
            "宝飾店なんかが入っているわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#0306F#5Pどこもバカ高で\x01",
            "庶民には入りにくいけどな～。\x02\x03",

            "#0300F俺も前にデートで\x01",
            "テーマパークとレストランを\x01",
            "利用したくらいなんだが……\x02\x03",

            "それで、これからどうすんだ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C1A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C1A)

    def lambda_1C27():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C27)
    Sleep(100)

    def lambda_1C37():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C37)

    def lambda_1C44():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C44)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0057
    ChrTalk(
        0x101,
        (
            "#0003F#12Pそうだな……\x02\x03",

            "#0001Fまずはオークション会場の\x01",
            "周辺の様子を確かめてみよう。\x02\x03",

            "ハルトマン議長邸、だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#0100F#6Pええ……\x01",
            "アーケードを左に抜けた先に\x01",
            "別荘が並ぶリゾート区画があるの。\x02\x03",

            "議長邸はその奥だったはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#0004F#12P分かった。\x02\x03",

            "#0000Fそれ以外にも……\x01",
            "行ける場所には行ってみよう。\x02\x03",

            "あのレクターって人みたいに\x01",
            "《競売会》の招待客にも\x01",
            "出くわすかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        "#0202F#5P……ですね。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        (
            "#0106F#6Pそういえば、あの人……\x02\x03",

            "#0101Fずいぶん怪しい言動だったけど\x01",
            "本当に帝国貴族なのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        (
            "#0303F#5P……さてな。\x02\x03",

            "#0301F鉄血宰相の代理って話と同じく、\x01",
            "単なるフカシかもしれねぇが……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#0006F#12Pただ、ああいう怪しい人間も\x01",
            "招待客として呼ばれているらしい。\x02\x03",

            "#0013F《黒の競売会》──\x01",
            "やはり一筋縄じゃ行かなさそうだ。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_205B")
    OP_29(0x18, 0x4, 0x40)
    Jump("loc_206D")

    label("loc_205B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_206D")
    OP_29(0x18, 0x4, 0x40)

    label("loc_206D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207F")
    OP_29(0x1A, 0x4, 0x40)

    label("loc_207F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_209D")
    OP_29(0x1C, 0x4, 0x40)
    Jump("loc_20AF")

    label("loc_209D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20AF")
    OP_29(0x1C, 0x4, 0x40)

    label("loc_20AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C1")
    OP_29(0x1E, 0x4, 0x40)

    label("loc_20C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x21, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D3")
    OP_29(0x21, 0x4, 0x40)

    label("loc_20D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20F1")
    OP_29(0x22, 0x4, 0x40)
    Jump("loc_2103")

    label("loc_20F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2103")
    OP_29(0x22, 0x4, 0x40)

    label("loc_2103")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2115")
    OP_29(0x23, 0x4, 0x40)

    label("loc_2115")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_149D end

    def Function_19_211B(): pass

    label("Function_19_211B")


    def lambda_2120():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2120)
    Sleep(500)

    def lambda_213D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_213D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2156():
        OP_95(0xFE, 7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2156)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_211B end

    def Function_20_2170(): pass

    label("Function_20_2170")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_219B")
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(3000)
    Jump("Function_20_2170")

    label("loc_219B")

    Return()

    # Function_20_2170 end

    def Function_21_219C(): pass

    label("Function_21_219C")


    def lambda_21A1():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21A1)
    Sleep(500)

    def lambda_21BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_21BE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_21D7():
        OP_95(0xFE, -2940, -4000, -50580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21D7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_21_219C end

    def Function_22_21F8(): pass

    label("Function_22_21F8")


    def lambda_21FD():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21FD)
    Sleep(500)

    def lambda_221A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_221A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2233():
        OP_95(0xFE, -4019, -4000, -51400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2233)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_22_21F8 end

    def Function_23_2254(): pass

    label("Function_23_2254")


    def lambda_2259():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2259)
    Sleep(500)

    def lambda_2276():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2276)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_228F():
        OP_95(0xFE, -4680, -4000, -49050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_228F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_23_2254 end

    def Function_24_22B0(): pass

    label("Function_24_22B0")


    def lambda_22B5():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22B5)
    Sleep(500)

    def lambda_22D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22D2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_22EB():
        OP_95(0xFE, -5640, -4000, -50180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22EB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_24_22B0 end

    def Function_25_230C(): pass

    label("Function_25_230C")

    Sleep(1000)
    Sound(475, 0, 100, 0)
    Sleep(1500)
    Sound(477, 0, 100, 0)
    Sleep(4000)
    Sound(476, 0, 100, 0)
    Sleep(1000)
    Sound(477, 0, 100, 0)
    Return()

    # Function_25_230C end

    def Function_26_2331(): pass

    label("Function_26_2331")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_23C4")
    SetChrPos(0x151, -25030, -4000, -49530, 270)

    label("loc_23C4")

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
            scpstr(SCPSTR_CODE_ITEM, 0x34C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34C, 1)

    #C0065
    ChrTalk(
        0x101,
        "#12P#0005Fあれ、この指輪って……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#11P#0105Fさっき、トマさんの言ってた\x01",
            "婚約指輪かもしれないわね。\x02\x03",

            "#0100Fあとでホテルの部屋に\x01",
            "持って行って見ましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x1)
    OP_65(0x2, 0x1)
    SetChrPos(0x0, -28000, -4000, -48730, 270)
    EventEnd(0x5)
    Return()

    # Function_26_2331 end

    def Function_27_24D4(): pass

    label("Function_27_24D4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《クロスベル市》行き水上バス・時刻表\x01\x01",
            "   ※またのお越しを\x01",
            "　       お待ちしております！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_24D4 end

    SaveToFile()

Try(main)
