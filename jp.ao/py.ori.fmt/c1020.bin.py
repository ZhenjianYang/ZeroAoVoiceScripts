from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1020.bin",                # FileName
        "c1020",                    # MapName
        "c1020",                    # Location
        0x0014,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 20, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1020",                  # 0
        "レイクロードⅢ世",       # 1
        "受付嬢セイラーム",       # 2
        "銀鯱トリトン",           # 3
        "竜宮カグヤ",             # 4
        "水狂ナルセス",           # 5
        "海刃シャークマン",       # 6
        "ペーター",               # 7
        "コパン",                 # 8
        "セルダン支部長",         # 9
        "フィッシャー団長",       # 10
    ))

    AddCharChip((
        "chr/ch45600.itc",                   # 00
        "chr/ch22100.itc",                   # 01
        "chr/ch45700.itc",                   # 02
        "chr/ch45800.itc",                   # 03
        "chr/ch45900.itc",                   # 04
        "chr/ch46000.itc",                   # 05
        "chr/ch24200.itc",                   # 06
        "chr/ch23600.itc",                   # 07
        "chr/ch32200.itc",                   # 08
        "chr/ch46100.itc",                   # 09
    ))

    DeclNpc(-4000,   0,       48369,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(7230,    0,       9069,    180,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(50,      0,       43369,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-4769,   0,       47610,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4599,    0,       -330,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-200,    0,       7579,    315,  389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4260,    0,       6059,    90,   389,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-3549,   0,       51630,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(5639,    0,       6059,    270,  389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4260,    0,       6059,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(6580,    0,       7980,    1500,    7230,    1500,    9070,    0x007E, 0,  4,  0x0000)

    ChipFrameInfo(592, 0)                                        # 0

    ScpFunction((
        "Function_0_250",          # 00, 0
        "Function_1_308",          # 01, 1
        "Function_2_4C5",          # 02, 2
        "Function_3_53E",          # 03, 3
        "Function_4_1021",         # 04, 4
        "Function_5_1025",         # 05, 5
        "Function_6_30C6",         # 06, 6
        "Function_7_31C7",         # 07, 7
        "Function_8_32D3",         # 08, 8
        "Function_9_3409",         # 09, 9
        "Function_10_34F4",        # 0A, 10
        "Function_11_37B4",        # 0B, 11
        "Function_12_3AE6",        # 0C, 12
        "Function_13_3D80",        # 0D, 13
        "Function_14_3E24",        # 0E, 14
        "Function_15_4BC4",        # 0F, 15
        "Function_16_4BFF",        # 10, 16
        "Function_17_60D2",        # 11, 17
        "Function_18_650E",        # 12, 18
        "Function_19_69CB",        # 13, 19
        "Function_20_69E7",        # 14, 20
        "Function_21_6A03",        # 15, 21
    ))


    def Function_0_250(): pass

    label("Function_0_250")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_290"),
        (1, "loc_29C"),
        (2, "loc_2A8"),
        (3, "loc_2B4"),
        (4, "loc_2C0"),
        (5, "loc_2CC"),
        (6, "loc_2D8"),
        (SWITCH_DEFAULT, "loc_2E4"),
    )


    label("loc_290")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_29C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2A8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2B4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2C0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2CC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_307")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_307")

    Return()

    # Function_0_250 end

    def Function_1_308(): pass

    label("Function_1_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_31B")
    SetChrFlags(0x8, 0x80)
    Jump("loc_470")

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_35F")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 4850, 0, 6960, 45)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8390, 0, 6850, 0)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_470")

    label("loc_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A1")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C")
    SetChrPos(0xE, 50, 0, 43370, 90)
    ClearChrFlags(0x11, 0x80)

    label("loc_39C")

    Jump("loc_470")

    label("loc_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BD")
    SetChrFlags(0x8, 0x80)

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_3DF")
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_3DF")

    Jump("loc_470")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3F7")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_470")

    label("loc_3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_405")
    Jump("loc_470")

    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_413")
    Jump("loc_470")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_421")
    Jump("loc_470")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_42F")
    Jump("loc_470")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_43D")
    Jump("loc_470")

    label("loc_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_44B")
    Jump("loc_470")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_459")
    Jump("loc_470")

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_467")
    Jump("loc_470")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_470")

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_484")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A9")
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_4C4")

    label("loc_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C4")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_4C4")

    Return()

    # Function_1_308 end

    def Function_2_4C5(): pass

    label("Function_2_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F6")
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51D")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)

    label("loc_51D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_534")
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53D")

    label("loc_534")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53D")

    Return()

    # Function_2_4C5 end

    def Function_3_53E(): pass

    label("Function_3_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_565")
    Call(0, 17)
    Return()

    label("loc_565")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_576")
    Jump("loc_101D")

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62D")

    #C0001
    ChrTalk(
        0x8,
        (
            "奴ら、まさか\x01",
            "ハーバードを呼ぶとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "……フフ、だが願ったり叶ったりだ。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "何せ、俺はそのために\x01",
            "クロスベルに来たようなものだからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_670")

    label("loc_62D")


    #C0004
    ChrTalk(
        0x8,
        (
            "さあ早く来い、ハ－バード……\x01",
            "この俺が直々に引導を渡してやる！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_670")

    Jump("loc_6D8")

    label("loc_675")


    #C0005
    ChrTalk(
        0x8,
        "ボート小屋を使って構わんだと……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "確かに、あの雰囲気は\x01",
            "修行には打ってつけかもしれんが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D8")

    Jump("loc_101D")

    label("loc_6DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A4")

    #C0007
    ChrTalk(
        0x8,
        (
            "我が釣皇倶楽部と釣公師団には\x01",
            "少なからぬ因縁があってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "貴様は何も知らんと思うが……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0009
    ChrTalk(
        0x8,
        (
            "……フン、くだらぬ事を言った。\x01",
            "今の話は忘れろ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7D9")

    label("loc_7A4")


    #C0010
    ChrTalk(
        0x8,
        (
            "……フン、くだらぬ事を言った。\x01",
            "今の話は忘れろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D9")

    Jump("loc_101D")

    label("loc_7DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_94F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C1")

    #C0011
    ChrTalk(
        0x8,
        (
            "どうやら、セルダンたちは\x01",
            "負けを認めつつあるようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "フフ、だがこの時点でまだ\x01",
            "この俺に辿り着きもしないとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "貴様らの釣りに対する情熱は\x01",
            "どうやら見せかけだったようだな。\x01",
            "フハハハハッ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_94A")

    label("loc_8C1")


    #C0014
    ChrTalk(
        0x8,
        (
            "フフ、この時点でまだ\x01",
            "この俺に辿り着きもしないとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "貴様らの釣りに対する情熱は\x01",
            "どうやら見せかけだったようだな。\x01",
            "フハハハハッ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94A")

    Jump("loc_101D")

    label("loc_94F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_AB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2C")

    #C0016
    ChrTalk(
        0x8,
        (
            "我が父レイクロードⅡ世は\x01",
            "偉大なる至高の釣師だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "我がレイクロード社では、\x01",
            "その名を冠する釣具を\x01",
            "いくつも開発しているのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "それらは全て、我が父が\x01",
            "自らの手で設計したものなのだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AB3")

    label("loc_A2C")


    #C0019
    ChrTalk(
        0x8,
        (
            "我が父レイクロードⅡ世は\x01",
            "偉大なる至高の釣師だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "その飽くなき探究心は\x01",
            "いつも我々の想像を超える……\x01",
            "まさに究極の趣味人なのだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB3")

    Jump("loc_101D")

    label("loc_AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB6")

    #C0021
    ChrTalk(
        0x8,
        (
            "我が釣皇倶楽部のメンバーは、\x01",
            "全員がプロのエリート釣師だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "そして、その釣果は全て\x01",
            "レイクロード社の新製品開発に\x01",
            "フィードバックされている。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "釣公師団などという\x01",
            "遊び半分のお茶らけた連中とは\x01",
            "根本から違うというわけだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C41")

    label("loc_BB6")


    #C0024
    ChrTalk(
        0x8,
        (
            "我が釣皇倶楽部の会員は、\x01",
            "全員がプロのエリート釣師だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "釣公師団などという\x01",
            "遊び半分のお茶らけた連中とは\x01",
            "根本から違うというわけだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C41")

    Jump("loc_101D")

    label("loc_C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CF2")

    #C0026
    ChrTalk(
        0x8,
        (
            "ふむ、独立の提唱などと\x01",
            "何やらクロスベル人が勝手を\x01",
            "ほざいているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "この地の安寧は、我が祖国\x01",
            "エレボニアあってこそというのが\x01",
            "何故分からんのだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D81")

    #C0028
    ChrTalk(
        0x8,
        (
            "ふむ、クロスベルには\x01",
            "存外良い釣り場が多いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "海がないのは残念だが、\x01",
            "なかなかに魚種も豊富で\x01",
            "楽しませてもらっているぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_ECB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E41")

    #C0030
    ChrTalk(
        0x8,
        "貴様ら、爆釣勝負は順調か？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "フフ、辛くば無理をせず\x01",
            "降参しても良いのだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "何、その時はクロスベルで\x01",
            "自由に釣りができなくなるだけだ。\x01",
            "フハハハハッ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EC6")

    label("loc_E41")


    #C0033
    ChrTalk(
        0x8,
        (
            "フフ、辛くば無理をせず\x01",
            "降参しても良いのだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "何、その時はクロスベルで\x01",
            "自由に釣りができなくなるだけだ。\x01",
            "フハハハハッ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC6")

    Jump("loc_101D")

    label("loc_ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F60")

    #C0035
    ChrTalk(
        0x8,
        (
            "フフ、貴様らがどこまでやれるか\x01",
            "せいぜい楽しみにさせてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "もっとも、結果は\x01",
            "火を見るよりも明らかだがな。\x01",
            "フハハハハッ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1014")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD2")

    #C0037
    ChrTalk(
        0x8,
        "ん……まだいたのか？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "貴様と話すことはもう何もない。\x01",
            "さっさと立ち去るんだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_100F")

    label("loc_FD2")


    #C0039
    ChrTalk(
        0x8,
        (
            "貴様と話すことはもう何もない。\x01",
            "さっさと立ち去るんだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100F")

    Jump("loc_101D")

    label("loc_1014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_101D")

    label("loc_101D")

    TalkEnd(0xFE)
    Return()

    # Function_3_53E end

    def Function_4_1021(): pass

    label("Function_4_1021")

    Call(0, 5)
    Return()

    # Function_4_1021 end

    def Function_5_1025(): pass

    label("Function_5_1025")

    TalkBegin(0x9)
    ClearScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1047")
    SetScenarioFlags(0x0, 2)

    label("loc_1047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_1053")
    SetScenarioFlags(0x0, 2)

    label("loc_1053")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_105D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B9")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                  # 0
            "爆釣勝負の説明を聞く\x01",      # 1
            "やめる\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_1117")

    label("loc_10B9")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_110D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_1117")

    label("loc_110D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1117")

    Jump("loc_1126")

    label("loc_111C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1126")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1157")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1146")
    OP_AF(0x36)
    Jump("loc_1148")

    label("loc_1146")

    OP_AF(0x37)

    label("loc_1148")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30BD")

    label("loc_1157")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1170")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE3")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "勝負の取り決めについて\x01",          # 0
            "挑戦に必要な資格について\x01",        # 1
            "釣傑四天王の居場所について\x01",      # 2
            "やめる\x01",                          # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1392")

    #C0040
    ChrTalk(
        0x9,
        (
            "全ての爆釣勝負に勝利すれば……\x01",
            "この事務所を取り返す事ができ、\x01",
            "何でも１つだけ命令ができる約束よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "勝負の相手は全部で５人。\x01",
            "釣傑四天王とレイクロード様が\x01",
            "そのお相手よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            "ちなみに釣傑四天王に勝利すると、\x01",
            "現在それぞれが管理している\x01",
            "釣り場が開放されるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "それから、各人に挑戦するには\x01",
            "それぞれ資格が必要になるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "資格は一度手にしちゃえば、\x01",
            "以後、何度でも挑戦することが可能よ。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CDE")

    label("loc_1392")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC5")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "レイクロードⅢ世\x01",      # 0
            "銀鯱トリトン\x01",          # 1
            "竜宮カグヤ\x01",            # 2
            "水狂ナルセス\x01",          # 3
            "海刃シャークマン\x01",      # 4
            "やめる\x01",                # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A2")

    #C0045
    ChrTalk(
        0x9,
        (
            "名実ともに倶楽部の頂点に\x01",
            "君臨するレイクロード様に\x01",
            "挑戦するための資格――\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "それはズバリ、\x01",
            "『釣傑四天王を４人全員倒す』\x01",
            "ことで得られるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "果てしなく厳しい\x01",
            "困難だとは思うけど……\x01",
            "気合いと根性で乗り越えてね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1593")

    #C0048
    ChrTalk(
        0x9,
        (
            "――ってもう、４人全員倒したのよね。\x01",
            "ふふ、すごいじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "あとはレイクロード様を\x01",
            "残すのみ……武運を祈ってるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1593")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC0")

    label("loc_15A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F8")

    #C0050
    ChrTalk(
        0x9,
        (
            "四天王最強と謳われる、\x01",
            "《銀鯱》トリトンさんに\x01",
            "挑戦するための資格――\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "それはズバリ、\x01",
            "『２９種類の獲物を釣る』\x01",
            "ことで得られるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "道はかなり険しいと思うけど……\x01",
            "最後まで諦めずに頑張ってね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_END)), "loc_16E9")

    #C0053
    ChrTalk(
        0x9,
        (
            "――ってもう、\x01",
            "トリトンさんに勝ったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "ふふ、だったらもう\x01",
            "こんな情報必要なかったわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC0")

    label("loc_16F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1855")

    #C0055
    ChrTalk(
        0x9,
        (
            "釣りの神々に愛された、\x01",
            "《竜宮》カグヤさんに\x01",
            "挑戦するための資格――\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "それはズバリ、\x01",
            "『１３０リジュ以上の大物を釣る』\x01",
            "ことで得られるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "技術以上に、\x01",
            "運も重要になると思うけど……\x01",
            "挫けずに頑張ってね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_END)), "loc_1846")

    #C0058
    ChrTalk(
        0x9,
        (
            "――ってもう、\x01",
            "カグヤさんに勝ったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "ふふ、だったらもう\x01",
            "こんな情報必要なかったわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1846")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC0")

    label("loc_1855")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CE")

    #C0060
    ChrTalk(
        0x9,
        (
            "綺麗な魚と自分が大好きな\x01",
            "《水狂》ナルセスさんに\x01",
            "挑戦するための資格――\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "それはズバリ、\x01",
            "『クロスベルで最も美しい魚を釣る』\x01",
            "ことで得られるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "基準はあいまいだけど……\x01",
            "これだっていうものを釣り上げて\x01",
            "ナルセスさんを唸らせてね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_END)), "loc_19BF")

    #C0063
    ChrTalk(
        0x9,
        (
            "――ってもう、\x01",
            "ナルセスさんに勝ったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "ふふ、だったらもう\x01",
            "こんな情報必要なかったわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC0")

    label("loc_19CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BBB")

    #C0065
    ChrTalk(
        0x9,
        (
            "見た目に反して技巧派で知られる\x01",
            "《海刃》シャークマンさんに\x01",
            "挑戦するための資格――\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "それはズバリ、\x01",
            "『ゲームフィッシュを６種類釣る』\x01",
            "ことで得られるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "詳しい魚種は、グラトンバスに\x01",
            "ロック、アルモリカブナ――\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "さらにピラーニャにアローナ、\x01",
            "そして、パルルクね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "全てを釣り上げるのは\x01",
            "けっこう大変だと思うけど……\x01",
            "なんとか頑張ってね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_END)), "loc_1BAC")

    #C0070
    ChrTalk(
        0x9,
        (
            "――ってもう、\x01",
            "シャークマンさんに勝ったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "ふふ、だったらもう\x01",
            "こんな情報必要なかったわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC0")

    label("loc_1BBB")

    Jump("loc_1BC5")

    label("loc_1BC0")

    Jump("loc_13AB")

    label("loc_1BC5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CDE")

    label("loc_1BD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CCF")

    #C0072
    ChrTalk(
        0x9,
        (
            "シャークマンさんは\x01",
            "『ウルスラ間道の池』。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "ナルセスさんは\x01",
            "『マインツ山道の渓流』。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "カグヤさんは\x01",
            "『アルモリカ古道の休憩所』。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "そして、トリトンさんは\x01",
            "『西クロスベル街道の池』に\x01",
            "それぞれいらっしゃるわよ。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CDE")

    label("loc_1CCF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CE3")

    label("loc_1CE3")

    Jump("loc_30BD")

    label("loc_1CDE")

    Jump("loc_1170")

    label("loc_1CE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DAE")

    #C0076
    ChrTalk(
        0x9,
        (
            "さっき、アルモリカ村の\x01",
            "家族や友達たちと\x01",
            "何とか連絡が取れたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "これからのことは\x01",
            "色々と不安だけど……\x01",
            "とりあえず一安心したわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E31")

    label("loc_1DAE")


    #C0078
    ChrTalk(
        0x9,
        (
            "それにしても……\x01",
            "みんな筋金入りの釣りバカよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "支部長もペーターさんも\x01",
            "コパンさんも、さっそく釣りに\x01",
            "出かけて行ったわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E31")

    Jump("loc_30BD")

    label("loc_1E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1EA6")

    #C0080
    ChrTalk(
        0x9,
        (
            "……う～ん、\x01",
            "それにしても不穏な状況ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "アルモリカ村のみんなも\x01",
            "無事だといいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BD")

    label("loc_1EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_207D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_1F31")

    #C0082
    ChrTalk(
        0x9,
        (
            "釣公師団の活動も\x01",
            "いよいよ再開って時に、\x01",
            "トンデモないことになったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        "一度、アルモリカ村に戻ろうかしら？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2078")

    label("loc_1F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF8")

    #C0084
    ChrTalk(
        0x9,
        (
            "私、レイクロード様のおかげで\x01",
            "釣公師団に入ることが出来たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "レイクロード様って本当は\x01",
            "とても優しくて良い方なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "どうして、釣公師団と\x01",
            "仲良くできないんだろうな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2078")

    label("loc_1FF8")


    #C0087
    ChrTalk(
        0x9,
        (
            "それにしても釣公師団の活動も\x01",
            "いよいよ再開って時に、\x01",
            "トンデモないことになったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        "一度、アルモリカ村に戻ろうかしら？\x02",
    )

    CloseMessageWindow()

    label("loc_2078")

    Jump("loc_30BD")

    label("loc_207D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_24AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2122")

    #C0089
    ChrTalk(
        0x9,
        (
            "釣公師団の最終兵器というのは、\x01",
            "とある人物のことだったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "一体どんな人、\x01",
            "いや釣師なのかしら……\x01",
            "なんか異様にドキドキするわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A9")

    label("loc_2122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224B")

    #C0091
    ChrTalk(
        0x9,
        (
            "聞いたわ、いよいよ\x01",
            "レイクロード様に挑むのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "決戦の場はウルスラ間道の浅瀬……\x01",
            "数ある釣り場の中でもレイクロード様が\x01",
            "最も気に入られている場所よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "苦しい戦いになると思うけど、\x01",
            "どうか頑張ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "そして、できれば釣皇倶楽部と\x01",
            "釣公師団の仲を取り持って。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22E8")

    label("loc_224B")


    #C0095
    ChrTalk(
        0x9,
        (
            "決戦の場はウルスラ間道の浅瀬……\x01",
            "数ある釣り場の中でもレイクロード様が\x01",
            "最も気に入られている場所よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "苦しい戦いになると思うけど、\x01",
            "どうか頑張ってね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E8")

    Jump("loc_24A9")

    label("loc_22ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2418")

    #C0097
    ChrTalk(
        0x9,
        (
            "おめでとう、ロイドさん。\x01",
            "みごと勝負に勝ったんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "それと、レイクロード様のおかげで\x01",
            "私が釣公師団に入れたことも聞いたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "なんていうか、\x01",
            "レイクロード様って本当は\x01",
            "とても優しくて良い方なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "どうすれば、釣公師団との\x01",
            "わだかまりを解消できるのかしらね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24A9")

    label("loc_2418")


    #C0101
    ChrTalk(
        0x9,
        (
            "なんていうか、\x01",
            "レイクロード様って本当は\x01",
            "とても優しくて良い方なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "どうすれば、釣公師団との\x01",
            "わだかまりを解消できるのかしらね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A9")

    Jump("loc_30BD")

    label("loc_24AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_25F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257B")

    #C0103
    ChrTalk(
        0x9,
        (
            "レイクロード様、\x01",
            "前にアマチュア釣師が\x01",
            "嫌いって言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "どうやら、それ以前に\x01",
            "釣公師団に対して何か個人的な\x01",
            "思いがあるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        "一体、何があったのかしらね？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25F3")

    label("loc_257B")


    #C0106
    ChrTalk(
        0x9,
        (
            "レイクロード様、どうやら\x01",
            "釣公師団に対して何か個人的な\x01",
            "思いがあるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        "一体、何があったのかしらね？\x02",
    )

    CloseMessageWindow()

    label("loc_25F3")

    Jump("loc_30BD")

    label("loc_25F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_26EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A6")

    #C0108
    ChrTalk(
        0x9,
        (
            "なんか最近、セルダンさんが\x01",
            "最終兵器を投入するとかなんとか\x01",
            "呟いていたらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "それって一体何なのかしら？\x01",
            "う～ん、もの凄く気になるわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26E9")

    label("loc_26A6")


    #C0110
    ChrTalk(
        0x9,
        (
            "最終兵器って一体何なのかしら？\x01",
            "う～ん、もの凄く気になるわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E9")

    Jump("loc_30BD")

    label("loc_26EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2772")

    #C0111
    ChrTalk(
        0x9,
        (
            "レイクロード様が\x01",
            "お父上の話をされる時は、\x01",
            "いつも目がキラキラ輝いて見えるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        "ふふ、そういうのって素敵よね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30BD")

    label("loc_2772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2842")

    #C0113
    ChrTalk(
        0x9,
        (
            "この間、レイクロード様に\x01",
            "お前には想像力があるって\x01",
            "褒められたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "この釣り場にはどんな魚がいて\x01",
            "どんな風に生活しているか……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "そうやって想像する力が\x01",
            "釣りには重要なことなんだってね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BD")

    label("loc_2842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28D7")

    #C0116
    ChrTalk(
        0x9,
        (
            "私も何だかんだ、\x01",
            "街に出てきて随分になるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "定期的に顔は出してるけど……\x01",
            "アルモリカ村ののんびりとした\x01",
            "空気が懐かしいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BD")

    label("loc_28D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_298F")

    #C0118
    ChrTalk(
        0x9,
        (
            "四天王の皆さんって、\x01",
            "ただ遊んでいるように見えて\x01",
            "実は色んな仕事をされているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "釣具のテストはもちろん、\x01",
            "水質や生態の分布調査まで……\x01",
            "本当に頭が下がるわよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BD")

    label("loc_298F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE5")

    #C0120
    ChrTalk(
        0x9,
        (
            "レイクロード様の家系は代々\x01",
            "帝国の子爵位を継いでおられるそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "帝国ではお国柄、事業家をされている\x01",
            "貴族の人って多いみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "レイクロード様の場合、おまけに\x01",
            "プロの釣師というのが凄いわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "何でも、子供の頃から釣りの\x01",
            "英才教育を受けていらっしゃったそうよ。\x01",
            "……どんな教育かは知らないけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B7C")

    label("loc_2AE5")


    #C0124
    ChrTalk(
        0x9,
        (
            "自分で言い出してなんだけど……\x01",
            "よく考えると釣りの英才教育って\x01",
            "どんなのか想像も付かないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            "……今度、レイクロード様に\x01",
            "聞いてみようかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7C")

    Jump("loc_30BD")

    label("loc_2B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C0B")

    #C0126
    ChrTalk(
        0x9,
        (
            "えっと、レイクロード様から\x01",
            "詳しいお話は聞いているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "勝負について分からないことが\x01",
            "あったら、何でも私に聞いてね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BD")

    label("loc_2C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_30B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3024")
    TurnDirection(0x9, 0x101, 0)

    #C0128
    ChrTalk(
        0x9,
        (
            "えっと……\x01",
            "あなた釣公師団の人よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "私、本当は釣公師団に\x01",
            "入るつもりだったんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0130
    ChrTalk(
        0x101,
        "#00005F釣公師団に……そうだったんだ？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        "うん、ずっと迷ってたんだけどね。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "ある日、入団を\x01",
            "決意してここへ来たら\x01",
            "レイクロード様がいて……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "あれよあれよと言っている間に\x01",
            "気付いたら受付になっていて……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0134
    ChrTalk(
        0x102,
        "#00106Fそう、色々大変だったのね。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x9,
        (
            "でも、そうも言い切れないから\x01",
            "何だか申し訳なくって……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "というのも、レイクロード様は\x01",
            "私にすごく良くしてくれるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x9,
        (
            "レイクロード社製の最新型の\x01",
            "釣竿をプレゼントしてくれたり……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "時間がある時は個人的に\x01",
            "釣りの指導までしてくれるし、\x01",
            "釣りエサは無償で使い放題だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        "#00006Fそれは凄い待遇だな……\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        "何ていうか、だから私複雑で……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        (
            "とりあえず、レイクロード様は\x01",
            "釣公師団のことを凄く嫌っている\x01",
            "みたいなんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x9,
        (
            "私としては、両者に何とかして\x01",
            "仲良くしてもらいたいのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x9,
        (
            "何か私にも出来ることが\x01",
            "あればいいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 6)
    Jump("loc_30AF")

    label("loc_3024")


    #C0144
    ChrTalk(
        0x9,
        (
            "釣公師団と釣皇倶楽部……\x01",
            "私としては、両者に何とかして\x01",
            "仲良くしてもらいたいのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        (
            "何か私にも出来ることが\x01",
            "あればいいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30AF")

    Jump("loc_30BD")

    label("loc_30B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_30BD")

    label("loc_30BD")

    Jump("loc_105D")

    label("loc_30C2")

    TalkEnd(0x9)
    Return()

    # Function_5_1025 end

    def Function_6_30C6(): pass

    label("Function_6_30C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_30D7")
    Jump("loc_31C3")

    label("loc_30D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_313C")

    #C0146
    ChrTalk(
        0xA,
        (
            "いや～、まさか\x01",
            "みんな負けちゃうなんてな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        "楽しかったけど、やっぱ悔しいね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_31C3")

    label("loc_313C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_314A")
    Jump("loc_31C3")

    label("loc_314A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3158")
    Jump("loc_31C3")

    label("loc_3158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3166")
    Jump("loc_31C3")

    label("loc_3166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3174")
    Jump("loc_31C3")

    label("loc_3174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3182")
    Jump("loc_31C3")

    label("loc_3182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3190")
    Jump("loc_31C3")

    label("loc_3190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_319E")
    Jump("loc_31C3")

    label("loc_319E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_31AC")
    Jump("loc_31C3")

    label("loc_31AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_31BA")
    Jump("loc_31C3")

    label("loc_31BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_31C3")

    label("loc_31C3")

    TalkEnd(0xFE)
    Return()

    # Function_6_30C6 end

    def Function_7_31C7(): pass

    label("Function_7_31C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_31D8")
    Jump("loc_32CF")

    label("loc_31D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3248")

    #C0148
    ChrTalk(
        0xB,
        (
            "まさか、あのギガルークを\x01",
            "釣ってしまうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "フンッ、ただの\x01",
            "まぐれに決まってますわ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32CF")

    label("loc_3248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3256")
    Jump("loc_32CF")

    label("loc_3256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3264")
    Jump("loc_32CF")

    label("loc_3264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3272")
    Jump("loc_32CF")

    label("loc_3272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3280")
    Jump("loc_32CF")

    label("loc_3280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_328E")
    Jump("loc_32CF")

    label("loc_328E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_329C")
    Jump("loc_32CF")

    label("loc_329C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32AA")
    Jump("loc_32CF")

    label("loc_32AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32B8")
    Jump("loc_32CF")

    label("loc_32B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_32C6")
    Jump("loc_32CF")

    label("loc_32C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_32CF")

    label("loc_32CF")

    TalkEnd(0xFE)
    Return()

    # Function_7_31C7 end

    def Function_8_32D3(): pass

    label("Function_8_32D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32E4")
    Jump("loc_3405")

    label("loc_32E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_333D")

    #C0150
    ChrTalk(
        0xC,
        (
            "ボクたちにウィンした釣公師団……\x01",
            "ン～～、ビュリホーーーーーーーーッ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3405")

    label("loc_333D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_338C")

    #C0151
    ChrTalk(
        0xC,
        (
            "ミステリアスな武装集団……\x01",
            "ン～～、ナット・ビュリホーーッ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3405")

    label("loc_338C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_339A")
    Jump("loc_3405")

    label("loc_339A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33A8")
    Jump("loc_3405")

    label("loc_33A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_33B6")
    Jump("loc_3405")

    label("loc_33B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_33C4")
    Jump("loc_3405")

    label("loc_33C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33D2")
    Jump("loc_3405")

    label("loc_33D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_33E0")
    Jump("loc_3405")

    label("loc_33E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_33EE")
    Jump("loc_3405")

    label("loc_33EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_33FC")
    Jump("loc_3405")

    label("loc_33FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3405")

    label("loc_3405")

    TalkEnd(0xFE)
    Return()

    # Function_8_32D3 end

    def Function_9_3409(): pass

    label("Function_9_3409")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_341A")
    Jump("loc_34F0")

    label("loc_341A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3469")

    #C0152
    ChrTalk(
        0xD,
        (
            "この大漁旗……イカスなぁ。\x01",
            "がはは、帝国に持って帰りてえぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F0")

    label("loc_3469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3477")
    Jump("loc_34F0")

    label("loc_3477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3485")
    Jump("loc_34F0")

    label("loc_3485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3493")
    Jump("loc_34F0")

    label("loc_3493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34A1")
    Jump("loc_34F0")

    label("loc_34A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34AF")
    Jump("loc_34F0")

    label("loc_34AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34BD")
    Jump("loc_34F0")

    label("loc_34BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34CB")
    Jump("loc_34F0")

    label("loc_34CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_34D9")
    Jump("loc_34F0")

    label("loc_34D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_34E7")
    Jump("loc_34F0")

    label("loc_34E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34F0")

    label("loc_34F0")

    TalkEnd(0xFE)
    Return()

    # Function_9_3409 end

    def Function_10_34F4(): pass

    label("Function_10_34F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3505")
    Jump("loc_37B0")

    label("loc_3505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_356B")

    #C0153
    ChrTalk(
        0xE,
        (
            "う～む……とりあえずは\x01",
            "釣具の手入れでもして時間を\x01",
            "潰しているしかなさそうですねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B0")

    label("loc_356B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_371B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_3611")

    #C0154
    ChrTalk(
        0xE,
        (
            "いやはや、\x01",
            "ディーター大統領も大胆ですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xE,
        (
            "主張は分かりますが……\x01",
            "この先クロスベルがやっていけるのか\x01",
            "えも言われぬ不安を感じますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3716")

    label("loc_3611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3689")

    #C0156
    ChrTalk(
        0xE,
        (
            "いやはや、\x01",
            "我らがフィッシャー団長は\x01",
            "本当に凄まじいお方です。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xE,
        "フィッシャー団長、バンザ～イ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3716")

    label("loc_3689")


    #C0158
    ChrTalk(
        0xE,
        (
            "ですが、ディーター大統領も\x01",
            "大胆ですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xE,
        (
            "主張は分かりますが……\x01",
            "この先クロスベルがやっていけるのか\x01",
            "ただならない不安を感じますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3716")

    Jump("loc_37B0")

    label("loc_371B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3729")
    Jump("loc_37B0")

    label("loc_3729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3737")
    Jump("loc_37B0")

    label("loc_3737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3745")
    Jump("loc_37B0")

    label("loc_3745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3753")
    Jump("loc_37B0")

    label("loc_3753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3761")
    Jump("loc_37B0")

    label("loc_3761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_376F")
    Jump("loc_37B0")

    label("loc_376F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_377D")
    Jump("loc_37B0")

    label("loc_377D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_378B")
    Jump("loc_37B0")

    label("loc_378B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3799")
    Jump("loc_37B0")

    label("loc_3799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_37A7")
    Jump("loc_37B0")

    label("loc_37A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_37B0")

    label("loc_37B0")

    TalkEnd(0xFE)
    Return()

    # Function_10_34F4 end

    def Function_11_37B4(): pass

    label("Function_11_37B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_37C5")
    Jump("loc_3AE2")

    label("loc_37C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_383C")

    #C0160
    ChrTalk(
        0xF,
        "この支部には保存食が沢山あるんスよ。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xF,
        (
            "……だから間違っても\x01",
            "水槽の魚には手を付けないッスからね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AE2")

    label("loc_383C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_3960")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38EE")

    #C0162
    ChrTalk(
        0xF,
        (
            "あ～、やっぱり\x01",
            "この建物は落ち着くッスね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xF,
        (
            "しかし、この独立の展開は\x01",
            "ちっとも読めなかったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xF,
        "……この先、どうなるんスかね？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_395B")

    label("loc_38EE")


    #C0165
    ChrTalk(
        0xF,
        (
            "ようやく戻って来たはいいものの、\x01",
            "この独立の展開は読めなかったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xF,
        "……この先、どうなるんスかね？\x02",
    )

    CloseMessageWindow()

    label("loc_395B")

    Jump("loc_3A48")

    label("loc_3960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39DD")

    #C0167
    ChrTalk(
        0xF,
        "フィッシャー団長、恐るべしッスね！\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xF,
        (
            "くう～、オレもあんな超大物を\x01",
            "一度は釣り上げてみたいものッス！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3A48")

    label("loc_39DD")


    #C0169
    ChrTalk(
        0xF,
        (
            "それはそれにしても、とりあえず\x01",
            "この独立の展開は読めなかったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xF,
        "……この先、どうなるんスかね？\x02",
    )

    CloseMessageWindow()

    label("loc_3A48")

    Jump("loc_3AE2")

    label("loc_3A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3A5B")
    Jump("loc_3AE2")

    label("loc_3A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3A69")
    Jump("loc_3AE2")

    label("loc_3A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A77")
    Jump("loc_3AE2")

    label("loc_3A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A85")
    Jump("loc_3AE2")

    label("loc_3A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A93")
    Jump("loc_3AE2")

    label("loc_3A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3AA1")
    Jump("loc_3AE2")

    label("loc_3AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3AAF")
    Jump("loc_3AE2")

    label("loc_3AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3ABD")
    Jump("loc_3AE2")

    label("loc_3ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3ACB")
    Jump("loc_3AE2")

    label("loc_3ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3AD9")
    Jump("loc_3AE2")

    label("loc_3AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3AE2")

    label("loc_3AE2")

    TalkEnd(0xFE)
    Return()

    # Function_11_37B4 end

    def Function_12_3AE6(): pass

    label("Function_12_3AE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3AF7")
    Jump("loc_3D7C")

    label("loc_3AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3B7A")

    #C0171
    ChrTalk(
        0x10,
        (
            "市外に出れない状況が続いたと思ったら\x01",
            "今度は支部から出れないなんてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x10,
        "はぁ、釣りがしたくてたまらんなァ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D7C")

    label("loc_3B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3CE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_3BE6")

    #C0173
    ChrTalk(
        0x10,
        "クロスベル独立国か……\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x10,
        (
            "釣皇倶楽部然り、帝国とは\x01",
            "仲良く出来ない運命なのか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE2")

    label("loc_3BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C85")

    #C0175
    ChrTalk(
        0x10,
        (
            "しかし、釣皇倶楽部の連中は\x01",
            "本当に手強い連中だったなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x10,
        (
            "ヤツらの釣りに対する愛は\x01",
            "紛れもなく本物……\x01",
            "おかげで勉強させてもらったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3CE2")

    label("loc_3C85")


    #C0177
    ChrTalk(
        0x10,
        "しかし、クロスベル独立国か……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x10,
        (
            "釣皇倶楽部然り、帝国とは\x01",
            "仲良く出来ない運命なのか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE2")

    Jump("loc_3D7C")

    label("loc_3CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CF5")
    Jump("loc_3D7C")

    label("loc_3CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D03")
    Jump("loc_3D7C")

    label("loc_3D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D11")
    Jump("loc_3D7C")

    label("loc_3D11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D1F")
    Jump("loc_3D7C")

    label("loc_3D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D2D")
    Jump("loc_3D7C")

    label("loc_3D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D3B")
    Jump("loc_3D7C")

    label("loc_3D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3D49")
    Jump("loc_3D7C")

    label("loc_3D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D57")
    Jump("loc_3D7C")

    label("loc_3D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D65")
    Jump("loc_3D7C")

    label("loc_3D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D73")
    Jump("loc_3D7C")

    label("loc_3D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3D7C")

    label("loc_3D7C")

    TalkEnd(0xFE)
    Return()

    # Function_12_3AE6 end

    def Function_13_3D80(): pass

    label("Function_13_3D80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3E17")

    #C0179
    ChrTalk(
        0x11,
        (
            "ふむ、とにかく\x01",
            "クロスベル支部の危機を救えて\x01",
            "良かったのである。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x11,
        (
            "これで我輩、\x01",
            "胸を張ってリベールに\x01",
            "帰ることができるのである。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E20")

    label("loc_3E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3E20")

    label("loc_3E20")

    TalkEnd(0xFE)
    Return()

    # Function_13_3D80 end

    def Function_14_3E24(): pass

    label("Function_14_3E24")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch24200.itc", 0x1F)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 7530, 0, 6780, 225)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 7230, 0, 9070, 225)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrPos(0xF, 5820, 0, 4630, 45)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrPos(0xE, 5020, 0, 5530, 45)
    OP_4B(0xE, 0xFF)
    OP_68(2300, 1400, 1800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 2300, 0, 1600, 45)
    SetChrPos(0x102, 1300, 0, 2100, 45)
    SetChrPos(0x109, 1600, 0, 300, 45)
    SetChrPos(0x105, 100, 0, 1600, 45)

    def lambda_3F23():
        OP_9B(0x1, 0x101, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F23)
    Sleep(300)

    def lambda_3F3B():
        OP_9B(0x1, 0x102, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F3B)
    Sleep(300)

    def lambda_3F53():
        OP_9B(0x1, 0x109, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3F53)
    Sleep(300)

    def lambda_3F6B():
        OP_9B(0x1, 0x105, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3F6B)
    OP_68(4590, 1400, 3920, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0181
    ChrTalk(
        0x101,
        "#12P#00000F――失礼します。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0182
    ChrTalk(
        0x9,
        "#5Pあら……\x02",
    )

    CloseMessageWindow()

    #N0183
    NpcTalk(
        0x8,
        "身なりのいい男",
        "#11Pふむ、何奴だ？\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xE,
        "#6Pな、何ですか……？\x02",
    )

    CloseMessageWindow()

    def lambda_4040():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4040)
    Sleep(50)

    def lambda_4050():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4050)
    WaitChrThread(0xE, 1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    #C0185
    ChrTalk(
        0xF,
        "#11Pロ、ロイド団員じゃないッスか！？\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xE,
        (
            "#5Pああ、ちょうど良かった。\x01",
            "ロイド君もこちらの人に\x01",
            "言ってやってくれませんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xE,
        (
            "#5Pここは釣公師団・クロスベル支部――\x01",
            "平和と共存を愛する釣り人たちの\x01",
            "憩いの場所だということを。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0188
    ChrTalk(
        0x101,
        "#12P#00012Fな、なんの話でしょうか？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(5070, 1400, 5070, 0)
    MoveCamera(75, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21850, 0)
    SetChrPos(0x101, 4500, 0, 3800, 45)
    SetChrPos(0x102, 3400, 0, 4300, 45)
    SetChrPos(0x109, 4200, 0, 2500, 45)
    SetChrPos(0x105, 3200, 0, 3000, 45)
    SetChrPos(0xF, 5300, 0, 3000, 45)
    SetChrPos(0xE, 6200, 0, 2250, 0)
    OP_0D()

    #N0189
    NpcTalk(
        0x8,
        "身なりのいい男",
        (
            "#5Pフン、貴様も釣公師団に縁ある者か。\x01",
            "仲良く抗議にでも来たか？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            "#12P#00005Fえっと、確かに\x01",
            "団員ではあるんですが……\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    SetChrName("")

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは男に捜査手帳を見せ、\x01",
            "今行っている調査の説明をした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0192
    NpcTalk(
        0x8,
        "身なりのいい男",
        "#5P不審住戸の調査、だと……？\x02",
    )

    CloseMessageWindow()

    #N0193
    NpcTalk(
        0x8,
        "身なりのいい男",
        (
            "#5Pフン、確かに法人登録はまだだったが、\x01",
            "ならば、改めて自己紹介しよう――\x01",
            "俺の名前はレイクロードⅢ世。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x8,
        (
            "#5Pエレボニア帝国に本拠を構える\x01",
            "大陸有数の釣具メーカー、\x01",
            "《レイクロード社》を継ぐ者だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "#5Pそして《釣皇#4Rちょうおう#倶楽部》とは、\x01",
            "この俺が代表を務める\x01",
            "プロの釣り組織に他ならない。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        "#12P#00005Fレイクロード社……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x102,
        "#6P#00105Fロイド、知っているの？\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        (
            "#12P#00003Fああ、釣りをやっている\x01",
            "人間なら必ずと言っていいほど\x01",
            "耳にする名前だからね。\x02\x03",

            "#00000F何しろ大陸の釣具シェアで\x01",
            "常にトップを走り続ける\x01",
            "不動のＮｏ．１メーカーなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        "#6P#00105Fな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x109,
        (
            "#12P#10101Fでも、どうしてそんな人が\x01",
            "このクロスベルに？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "#5Pフッ、それは無論\x01",
            "我が釣皇倶楽部の更なる発展と\x01",
            "規模拡大のためだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "#5Pそして、ここを新たな\x01",
            "事務所としたのはその足がかり。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x8,
        (
            "#5Pちなみに契約の正当性は\x01",
            "この書類が示す通りだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        "#12P#00001F……確認させてもらいます。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9B(0x1, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
    Sleep(800)

    #C0205
    ChrTalk(
        0x101,
        (
            "#12P#00005Fこれは……\x01",
            "この物件の賃貸契約書ですね。\x02\x03",

            "#00003F確かにあなたの言う通り、\x01",
            "現契約者は釣皇倶楽部とあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x8,
        "#5Pフフ、理解したか？\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0xB4, 0x7D0, 0x7D0, 0x0)
    Sleep(50)

    #C0207
    ChrTalk(
        0xF,
        (
            "#11Pロイド団員……\x01",
            "こんな横暴、認めちゃ駄目ッスよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)

    #C0208
    ChrTalk(
        0x101,
        "#6P#00005F横暴、というと……？\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xE,
        (
            "#11Pええ、実はこの男は\x01",
            "セルダン支部長に何の断りなく、\x01",
            "強引に契約を奪い取ったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xE,
        (
            "#11Pミラの力に飽かして、\x01",
            "不動産会社を言い含めることでね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    #C0211
    ChrTalk(
        0x8,
        (
            "#5Pフン、多少やり方が強引だろうと、\x01",
            "正式な手続きには違いない。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "#5Pそれに、ここはそもそも\x01",
            "貴様らには勿体ない物件なのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x8,
        (
            "#5P釣りをただの道楽や\x01",
            "馴れ合いの道具と考えている、\x01",
            "貴様ら《釣公師団》にはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#12P#00001Fあ、あなたは……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x8,
        "#5Pとにかく、話はこれで終わりだ。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "#5P理解したら早々に立ち去り、\x01",
            "セルダンとやらにも伝えるんだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0217
    ChrTalk(
        0x8,
        "#11P――セイラーム、後は任せたぞ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 300)

    #C0218
    ChrTalk(
        0x9,
        "#5Pは、はい、かしこまりました。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 15)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_4AB7():
        OP_93(0xF, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4AB7)
    Sleep(50)

    def lambda_4AC7():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4AC7)
    Sleep(50)

    def lambda_4AD7():
        TurnDirection(0x102, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4AD7)
    Sleep(50)

    def lambda_4AE7():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4AE7)
    Sleep(50)

    def lambda_4AF7():
        TurnDirection(0x105, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4AF7)
    Sleep(50)

    def lambda_4B07():
        TurnDirection(0xE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B07)

    #C0219
    ChrTalk(
        0xF,
        "#12Pあ、逃げるなんて卑怯ッス。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xE,
        (
            "#12Pそうですよ、こちらにも\x01",
            "まだ言いたいことが……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)

    #C0221
    ChrTalk(
        0x105,
        "#6P#10302Fフフ、行ってしまったね。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    StopSound(128, 2000, 40)
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 5)
    NewScene("c1000", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3E24 end

    def Function_15_4BC4(): pass

    label("Function_15_4BC4")

    OP_95(0x8, 8680, 0, 4760, 2000, 0x0)
    OP_95(0x8, 11520, 0, 4740, 2000, 0x0)
    OP_9B(0x0, 0x8, 0x10E, 0x7D0, 0x7D0, 0x0)
    Sleep(200)
    Return()

    # Function_15_4BC4 end

    def Function_16_4BFF(): pass

    label("Function_16_4BFF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x8, 7530, 0, 6780, 225)
    SetChrPos(0x10, 5820, 0, 4630, 45)
    SetChrPos(0xE, 5020, 0, 5530, 45)
    SetChrPos(0xF, 6570, 0, 3900, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xE1, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_68(2300, 1400, 1800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 2300, 0, 1600, 45)
    SetChrPos(0x102, 1300, 0, 2100, 45)
    SetChrPos(0x109, 1600, 0, 300, 45)
    SetChrPos(0x104, 100, 0, 1600, 45)
    SetChrPos(0x105, 410, 0, 410, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0222
    ChrTalk(
        0x10,
        "ふ、ふざけるなっ！\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x10,
        (
            "一体、どこまで俺たちを\x01",
            "バカにすれば気が済むんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x104,
        "#00305F（なんだ、揉め事か？）\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        "#00001F（また何かあったのかな……？）\x02",
    )

    CloseMessageWindow()

    def lambda_4DB2():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DB2)
    Sleep(300)

    def lambda_4DCA():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4DCA)
    Sleep(300)

    def lambda_4DE2():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4DE2)
    Sleep(300)

    def lambda_4DFA():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4DFA)
    Sleep(300)

    def lambda_4E12():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4E12)
    OP_68(4190, 1400, 3520, 2500)
    OP_6F(0x1)

    #C0226
    ChrTalk(
        0x101,
        (
            "#00005F皆さん……\x01",
            "どうかしたんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x101, 500)

    #C0227
    ChrTalk(
        0xE,
        (
            "ああ、ロイド君……\x01",
            "ちょうどよかった。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4EAD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4EAD)
    Sleep(50)
    TurnDirection(0xF, 0x101, 500)

    #C0228
    ChrTalk(
        0x10,
        "ロイド団員、聞いてくれ。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x10,
        (
            "実はこいつらの仲間が何人か、\x01",
            "市外各所の釣り場に現れてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x10,
        (
            "急にそれらの場所を独占するって\x01",
            "言い出しやがったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        "#00005Fつ、釣り場を独占……？\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xF,
        (
            "ええ、釣皇倶楽部以外の\x01",
            "人間はその場所で釣りをしちゃ\x01",
            "ダメだなんて言って……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xF,
        (
            "俺は無視して強行したんスけど、\x01",
            "そしたら糸をプツッと切られて\x01",
            "妨害されたんスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x102,
        "#00106Fそれはひどい話ですね。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x109,
        (
            "#10101Fあの……どうして\x01",
            "仲良くできないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "フン、それは釣公師団が\x01",
            "ふざけたアマチュア集団だからだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "至高のプロ集団である\x01",
            "我々の前をウロチョロされると、\x01",
            "それだけで目障りなのでな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0238
    ChrTalk(
        0xE,
        (
            "ア、アマチュアで\x01",
            "いったい何が悪いんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xE,
        (
            "釣りを楽しむのに、\x01",
            "プロもアマも関係ないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5194():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5194)
    Sleep(50)
    TurnDirection(0xF, 0x8, 500)

    #C0240
    ChrTalk(
        0x10,
        (
            "ああ、それにアンタらが\x01",
            "色んな大会で結果を出しているのを\x01",
            "知ってはいるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x10,
        (
            "ウチにも相応の実力者はいるんだ。\x01",
            "俺たちを舐めないで欲しいものだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0242
    ChrTalk(
        0x8,
        "ほう……？\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xF,
        "支部長の言う通りッス！\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xF,
        (
            "今は返上しちゃってるッスけど、\x01",
            "『特級釣師』を舐めんなッス！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    #C0245
    ChrTalk(
        0x8,
        "#4Sフフ、フハハハハッ！#3S\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x8,
        (
            "……面白い。\x01",
            "貴様たちからそんな言葉が\x01",
            "聞けるとは意外だったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x8,
        (
            "そこまで言うのなら……\x01",
            "特別に《爆釣#4Rばくちょう#勝負》を\x01",
            "受けてやらんこともないが？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0248
    ChrTalk(
        0x10,
        "ば、爆釣勝負だと……？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xF,
        "アンタ、正気ッスか？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#00005Fえ、えっと、\x01",
            "《爆釣勝負》って……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_544C():
        TurnDirection(0x10, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_544C)
    Sleep(50)

    def lambda_545C():
        TurnDirection(0xE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_545C)
    Sleep(50)

    def lambda_546C():
        TurnDirection(0xF, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_546C)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    #C0251
    ChrTalk(
        0xE,
        (
            "はい、その名の通り釣りによる\x01",
            "対決のことを示すのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xE,
        (
            "『爆釣』の名を冠する勝負は\x01",
            "釣師にとって絶対的な意味を持つんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x10,
        (
            "ああ、釣師の誇りと名誉……\x01",
            "そして有形無形のあらゆる物を\x01",
            "賭けて行われる真剣勝負なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xF,
        (
            "オレは実際にやったことは\x01",
            "ないッスけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xF,
        (
            "爆釣勝負に負けて全財産を失った\x01",
            "釣師の話を聞いたことがあるッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xF,
        (
            "つまり何が何でも負けられない……\x01",
            "そんな戦いなんスよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0257
    ChrTalk(
        0x101,
        "#00006Fそ、そうなんですか。\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x104,
        "#00306F何だかとんでもねえな……\x02",
    )

    CloseMessageWindow()

    def lambda_56DA():
        TurnDirection(0x10, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_56DA)
    Sleep(50)

    def lambda_56EA():
        TurnDirection(0xE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_56EA)
    Sleep(50)

    def lambda_56FA():
        TurnDirection(0xF, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_56FA)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    #C0259
    ChrTalk(
        0x10,
        "それで……勝負のルールは？\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "そうだな、今クロスベルに\x01",
            "来ている仲間たち４人とこの俺――\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "この５人全員に勝負を挑み、\x01",
            "誰か１人でも５人抜きができたら、\x01",
            "貴様らの勝利というのはどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        (
            "何度挑もうが自由だが……\x01",
            "代わりに、それを果たせない限り\x01",
            "俺たちの我侭を通させてもらう。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x8,
        (
            "といっても無論、内容は\x01",
            "釣りに関することに限ってだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x10,
        (
            "………………………………\x01",
            "……我々が勝った場合は？\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        (
            "ふむ、万が一にもない奇跡だが、\x01",
            "貴様らも夢は見たいだろうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x8,
        (
            "まあ、それぞれに勝利するごとに\x01",
            "順次釣り場を開放するのはもちろん……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x8,
        (
            "５人全員に勝つことができれば、\x01",
            "俺たちはクロスベルから完全に撤退……\x01",
            "この事務所も当然引き渡す。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x8,
        (
            "さらに――\x01",
            "何でも１つだけ命令を聞いてやろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0269
    ChrTalk(
        0x101,
        "#00005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xF,
        "マ、マジッスか！？\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、でも本当に\x01",
            "信用しちゃっていいのかい？\x02\x03",

            "#10300Fこっちが勝っても約束を守る\x01",
            "保証なんてなさそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x10,
        (
            "いや、さっきペーターの言った通り\x01",
            "爆釣勝負の結果は釣師にとって絶対だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x10,
        (
            "そして、俺たちへの態度がどうだろうと\x01",
            "こいつらが釣師としての誇りを\x01",
            "人一倍持っていることは間違いない。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x10,
        (
            "約束を破ることは\x01",
            "ありえないと言っていいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#00006Fな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x102,
        "#00100Fそういうものなんですね。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x8,
        (
            "フフ、セルダン……\x01",
            "貴様も存外、話が分かるではないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x8,
        (
            "それでどうする。\x01",
            "俺たちに勝負を挑んでみるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x10,
        "……………………………\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x10,
        "……分かった、挑戦させてもらおう。\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        "フフ、よかろう。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 500)

    #C0282
    ChrTalk(
        0xE,
        "いいんですか、セルダン支部長。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xE,
        (
            "勝てなかったら、ずっと\x01",
            "向こうの我侭に従うって話ですよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xF,
        (
            "へへっ、けどその代わりに\x01",
            "何度挑戦してもいいんスよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xF,
        (
            "こう言っちゃなんスけど、\x01",
            "正直、楽勝なんじゃないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xF,
        (
            "いくら実力があっても\x01",
            "釣りで勝ち続けられる人間なんて\x01",
            "いないッスからね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#00006F確かに……\x01",
            "そういう気はするけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x8,
        (
            "フフッ、お前たちは\x01",
            "まだまだ釣りというものが\x01",
            "よく解っていないようだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)

    #C0289
    ChrTalk(
        0x8,
        (
            "まあいい、ちなみに\x01",
            "この俺に挑むことが許されるのは\x01",
            "４人の仲間を倒した者だけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "加えて彼らに挑む際にも、\x01",
            "相応の資格を示してもらう。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x8,
        (
            "流石に一定以上の実力がない者の\x01",
            "相手をしている暇もないのでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        "その点は了承してもらうぞ。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x10,
        "ああ……分かった。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 500)

    #C0294
    ChrTalk(
        0xE,
        "セルダン支部長……\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x8,
        (
            "まあ、何か他にも\x01",
            "分からないことがあったら\x01",
            "後で受付のセイラームに聞くがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x8,
        (
            "我が釣皇倶楽部が誇る\x01",
            "『釣傑#4Rちょうけつ#四天王』……\x01",
            "果たして貴様らに相手が務まるかな？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 7)
    NewScene("c1000", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_16_4BFF end

    def Function_17_60D2(): pass

    label("Function_17_60D2")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4540, 1400, 48400, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -4070, 0, 49840, 180)
    SetChrPos(0x102, -2990, 0, 50250, 180)
    SetChrPos(0x103, -4110, 0, 50870, 180)
    SetChrPos(0x104, -5080, 0, 51200, 180)
    SetChrPos(0x109, -2730, 0, 51480, 180)
    SetChrPos(0x105, -1420, 0, 51120, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0297
    ChrTalk(
        0x8,
        "ん……何だ貴様？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0298
    ChrTalk(
        0x8,
        (
            "まさか、釣傑四天王を\x01",
            "全員倒したとか言うんじゃ\x01",
            "ないだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        "#00005Fえっと、そのまさかですが……\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x8,
        (
            "ふむ……ならば、\x01",
            "メダルを見せてもらおうか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0301
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣傑四天王から受け取った\x01",
            "４枚のメダルを\x01",
            "レイクロードⅢ世に見せた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0302
    ChrTalk(
        0x8,
        (
            "確かに、これらは\x01",
            "紛れもなく四天王のメダル……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x8,
        (
            "……フフ、まさか\x01",
            "この《釣皇》に挑む者が\x01",
            "現れようとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        "#00011Fちょ、《釣皇》……？\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x8,
        (
            "――然り。\x01",
            "俺は《釣皇》レイクロードⅢ世。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x8,
        (
            "釣皇倶楽部の名そのものを冠し、\x01",
            "また、その頂点に君臨する者だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x8,
        (
            "とにかく……\x01",
            "一足先に決戦の場で待っているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x8,
        "場所は――ウルスラ間道の浅瀬だ。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)

    def lambda_6422():

        label("loc_6422")

        TurnDirection(0x101, 0x8, 500)
        Yield()
        Jump("loc_6422")

    QueueWorkItem2(0x101, 2, lambda_6422)

    def lambda_6434():

        label("loc_6434")

        TurnDirection(0x102, 0x8, 500)
        Yield()
        Jump("loc_6434")

    QueueWorkItem2(0x102, 2, lambda_6434)

    def lambda_6446():

        label("loc_6446")

        TurnDirection(0x109, 0x8, 500)
        Yield()
        Jump("loc_6446")

    QueueWorkItem2(0x109, 2, lambda_6446)

    def lambda_6458():

        label("loc_6458")

        TurnDirection(0x105, 0x8, 500)
        Yield()
        Jump("loc_6458")

    QueueWorkItem2(0x105, 2, lambda_6458)

    def lambda_646A():

        label("loc_646A")

        TurnDirection(0x104, 0x8, 500)
        Yield()
        Jump("loc_646A")

    QueueWorkItem2(0x104, 2, lambda_646A)

    def lambda_647C():

        label("loc_647C")

        TurnDirection(0x103, 0x8, 500)
        Yield()
        Jump("loc_647C")

    QueueWorkItem2(0x103, 2, lambda_647C)

    def lambda_648E():
        OP_95(0xFE, -210, 0, 50780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_648E)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_64B3():
        OP_9B(0x1, 0xFE, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_64B3)
    WaitChrThread(0x8, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x103, 0x2)
    SetScenarioFlags(0x190, 7)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -4070, 0, 49840, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_17_60D2 end

    def Function_18_650E(): pass

    label("Function_18_650E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xE1, 0x0)
    OP_68(410, 1400, 410, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -1580, 0, -580, 45)
    SetChrPos(0x102, -580, 0, -1580, 45)
    SetChrPos(0x104, -1580, 0, -2580, 45)
    SetChrPos(0x103, -2580, 0, -1580, 45)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(3850, 1400, 4450, 4000)
    SetCameraDistance(22000, 4000)

    def lambda_65EC():
        OP_95(0xFE, 3330, 0, 4330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65EC)

    def lambda_6606():
        OP_95(0xFE, 2310, 0, 3310, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6606)
    BeginChrThread(0x102, 3, 0, 19)
    BeginChrThread(0x104, 3, 0, 20)

    def lambda_662C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_662C)

    def lambda_663D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_663D)

    def lambda_664E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_664E)

    def lambda_665F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_665F)
    Sleep(1000)
    BeginChrThread(0x10, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 21)
    OP_6F(0x1)

    #C0309
    ChrTalk(
        0x10,
        "#11Pおお、ロイド団員じゃないか。\x02",
    )

    CloseMessageWindow()

    #N0310
    NpcTalk(
        0x11,
        "フィッシャー",
        (
            "ふむ、君が噂の特務支援課の\x01",
            "ロイド・バニングス君であるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#6P#00005Fええ、そうですけど……\x01",
            "釣皇倶楽部の人たちは一体？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0312
    ChrTalk(
        0x101,
        (
            "#6P#00000Fそうか、全ての爆釣勝負に\x01",
            "勝つことができたんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x10,
        "#11Pああ、そういうことだ。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x10,
        (
            "#11Pそれもこれも――\x01",
            "全てはここにおられる我らが\x01",
            "フィッシャー団長のおかげさ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0315
    ChrTalk(
        0x101,
        "#6P#00005Fあ、あなたが釣公師団の団長……\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x10,
        (
            "#11Pいやぁ、それにしても\x01",
            "あの大ヌシを見事\x01",
            "釣り上げてしまうとは……！\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x10,
        (
            "#11P久しぶりに\x01",
            "大興奮させていただきましたよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x11,
        (
            "いやはや、それもこれも\x01",
            "君たちが開発した虹玉ＥＸが\x01",
            "あったればこそだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x11,
        (
            "何はともあれ、\x01",
            "事務所を取り戻すことが出来て\x01",
            "良かったのである。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#6P#00004Fな、なるほど……\x01",
            "どうもありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x191, 2)
    TurnDirection(0x11, 0x10, 0)
    TurnDirection(0x10, 0x11, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_4C(0x9, 0xFF)
    ClearMapFlags(0x10000000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3330, 0, 4330, 45)
    EventEnd(0x5)
    Return()

    # Function_18_650E end

    def Function_19_69CB(): pass

    label("Function_19_69CB")

    OP_95(0xFE, 4310, 0, 3130, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_19_69CB end

    def Function_20_69E7(): pass

    label("Function_20_69E7")

    OP_95(0xFE, 3310, 0, 2130, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_20_69E7 end

    def Function_21_6A03(): pass

    label("Function_21_6A03")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 500)
    OP_4B(0xFE, 0xFF)
    Return()

    # Function_21_6A03 end

    SaveToFile()

Try(main)
