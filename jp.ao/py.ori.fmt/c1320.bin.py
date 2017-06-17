from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1320.bin",                # FileName
        "c1320",                    # MapName
        "c1320",                    # Location
        0x001F,                     # MapIndex
        "ed7522",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 31, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1320",                  # 0
        "研究員クレイ",           # 1
        "研究員ダビッド",         # 2
        "人形",                   # 3
    ))

    AddCharChip((
        "chr/ch32800.itc",                   # 00
        "chr/ch29402.itc",                   # 01
    ))

    DeclNpc(-3099,   -479,    22659,   315,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-4699,   -379,    22700,   315,  325,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       -280,    16660,   1100,    0,       -130,    16660,   0x007C, 0,  7,  0x0000)

    ChipFrameInfo(324, 0)                                        # 0

    ScpFunction((
        "Function_0_144",          # 00, 0
        "Function_1_1F4",          # 01, 1
        "Function_2_236",          # 02, 2
        "Function_3_23D",          # 03, 3
        "Function_4_2BA",          # 04, 4
        "Function_5_448",          # 05, 5
        "Function_6_5D0",          # 06, 6
        "Function_7_955",          # 07, 7
        "Function_8_1DDF",         # 08, 8
        "Function_9_1E2A",         # 09, 9
        "Function_10_1EA0",        # 0A, 10
        "Function_11_1EEB",        # 0B, 11
    ))


    def Function_0_144(): pass

    label("Function_0_144")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_17C"),
        (1, "loc_188"),
        (2, "loc_194"),
        (3, "loc_1A0"),
        (4, "loc_1AC"),
        (5, "loc_1B8"),
        (6, "loc_1C4"),
        (SWITCH_DEFAULT, "loc_1D0"),
    )


    label("loc_17C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_188")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_194")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1F3")

    Return()

    # Function_0_144 end

    def Function_1_1F4(): pass

    label("Function_1_1F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_215")
    ClearScenarioFlags(0x25, 1)
    Call(0, 2)

    label("loc_215")

    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_235")
    SetChrFlags(0x8, 0x10)

    label("loc_235")

    Return()

    # Function_1_1F4 end

    def Function_2_236(): pass

    label("Function_2_236")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_236 end

    def Function_3_23D(): pass

    label("Function_3_23D")

    SetMapObjFrame(0xFF, "monita2_add", 0x2, "nomal")
    SetMapObjFrame(0xFF, "monita3_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita4_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita5_add", 0x0, 0x1)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B9")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x5, 0x4)

    label("loc_2B9")

    Return()

    # Function_3_23D end

    def Function_4_2BA(): pass

    label("Function_4_2BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF")
    Call(0, 6)
    Jump("loc_444")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C4")

    #C0001
    ChrTalk(
        0xFE,
        (
            "ちなみにロバーツ主任は今、\x01",
            "エプスタイン財団のフロアで\x01",
            "忙しくしているみたいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "なんでも、オルキスタワーの\x01",
            "図面を盗んだっていうハッカーを\x01",
            "探ってるらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "どうしてハッカーはそんなものを\x01",
            "盗んだんだろうね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_444")

    label("loc_3C4")


    #C0004
    ChrTalk(
        0xFE,
        (
            "ロバーツ主任がタワーの図面を盗んだ\x01",
            "ハッカーを探ってるらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "どうしてハッカーはそんなものを\x01",
            "盗んだんだろうね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_444")

    TalkEnd(0xFE)
    Return()

    # Function_4_2BA end

    def Function_5_448(): pass

    label("Function_5_448")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45D")
    Call(0, 6)
    Jump("loc_5CC")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55F")

    #C0006
    ChrTalk(
        0xFE,
        (
            "マリアベルお嬢様は\x01",
            "人使いが荒いけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "システムの管理っていう\x01",
            "責任のある部分を任されてんだ。\x01",
            "気合入れて頑張んないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "あんたたちは、\x01",
            "盗まれたお嬢様の人形を\x01",
            "探しに来てくれたんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "そっちもなんとか\x01",
            "頑張ってくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5CC")

    label("loc_55F")


    #C0010
    ChrTalk(
        0xFE,
        (
            "あんたたちは、\x01",
            "盗まれたお嬢様の人形を\x01",
            "探しに来てくれたんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "そっちもなんとか\x01",
            "頑張ってくれよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CC")

    TalkEnd(0xFE)
    Return()

    # Function_5_448 end

    def Function_6_5D0(): pass

    label("Function_6_5D0")

    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 500)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66C")
    Jump("loc_6B6")

    label("loc_66C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68C")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B6")

    label("loc_68C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AC")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B6")

    label("loc_6AC")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B6")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    #C0012
    ChrTalk(
        0x8,
        "あれ、君達は……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "あんたら、\x01",
            "確か特務支援課だったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "ハハ、久しぶりだな。\x01",
            "俺たちのこと覚えてるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        (
            "#00200FＩＢＣ技術部のクレイさんと\x01",
            "ダビッドさんでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00000Fお久しぶりです。\x01",
            "……なんだか忙しそうですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "ああ、導力ネットが\x01",
            "普及してきたからシステムの管理も\x01",
            "以前より大変になってきてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "まあ、しっかりやらせてもらうさ。\x01",
            "お嬢様にも言い含められているしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#00109Fふふ、ベルの下で働くのは\x01",
            "相変わらず大変でしょうけど……\x01",
            "頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        "ああ、ありがとさん。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "そっちも、盗まれたお嬢様の人形を\x01",
            "探しに来てくれたんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        "なんとか頑張ってくれよな。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x13B, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x1C6, 2)
    Return()

    # Function_6_5D0 end

    def Function_7_955(): pass

    label("Function_7_955")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-820, 900, 14940, 0)
    MoveCamera(32, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13870, 0)
    SetChrPos(0x101, 40, -510, 15350, 0)
    SetChrPos(0x102, -1100, -590, 14550, 0)
    SetChrPos(0x103, -70, -590, 13800, 0)
    SetChrPos(0x104, 1090, -590, 14550, 0)
    SetChrPos(0x109, -1030, -590, 13110, 0)
    SetChrPos(0x105, 970, -590, 13140, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("apl/ch51099.itc", 0x1E)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0xB)
    SetChrPos(0xA, 0, -130, 16660, 0)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    LoadChrToIndex("chr/ch29400.itc", 0x1F)
    FadeToBright(500, 0)
    OP_0D()

    #C0023
    ChrTalk(
        0x101,
        "#12P#00000Fあった……最後のトランク！\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        (
            "#12P#00203F『高くそびえし摩天楼、\x01",
            "　１６層の頂より２１層を下りて\x01",
            "　異界を覗く数多の窓を探せ』……\x02\x03",

            "#00200F地上１６階のＩＢＣビル、\x01",
            "その最上階から２１階層降りた地下５階。\x01",
            "……この場所の事だったようです。\x02\x03",

            "#00200Fそして『異界を覗く数多の窓』は、\x01",
            "導力ネットを覗けるこれらの端末の\x01",
            "モニタを指していたわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#12P#00300F言われてみりゃ、この場所以外は\x01",
            "考えられなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#12P#00000Fよし、さっそく確認してみよう。\x02",
    )

    CloseMessageWindow()
    Sound(1024, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x1, 0x14, 0x1, 0x8)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_79(0x5)
    Sleep(1000)

    #C0027
    ChrTalk(
        0x102,
        (
            "#6P#00100F確か、この人形は『アリス』……\x01",
            "ベルのコレクションでも\x01",
            "一番のお気に入りだったはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#12P#00005F怪盗Ｂのカードは……最後だし、\x01",
            "貼り付けられてはないみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x105,
        "#12P#10300Fフフ、これにて依頼達成って所かな？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        "#6P#10106Fはあ、長かったですねえ……\x02",
    )

    CloseMessageWindow()
    Sound(1026, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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

    #C0031
    ChrTalk(
        0x101,
        "#12P#00005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        "#12P#00301Fな、なんだあ？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 8)
    BeginChrThread(0x9, 1, 0, 9)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)

    #C0033
    ChrTalk(
        0x8,
        "#6P君たち、何かあったのかい？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        (
            "#6P導力メールが届いたアラートが\x01",
            "聞こえてきたみたいだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "#6Pって、そこにあるのは\x01",
            "マリアベルお嬢様の人形か！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F27():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F27)
    Sleep(50)

    def lambda_F37():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F37)
    Sleep(50)

    def lambda_F47():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F47)
    Sleep(50)

    def lambda_F57():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F57)
    Sleep(50)

    def lambda_F67():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F67)
    Sleep(50)

    def lambda_F77():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F77)
    Sleep(100)

    #C0036
    ChrTalk(
        0x101,
        (
            "#11P#00005Fえっと、さっきからここに\x01",
            "あったみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#12P#00203Fふむ……それよりも、\x01",
            "このタイミングでメールだなんて\x01",
            "なんだか気になりますね。\x02\x03",

            "#00200Fちょっと確認してみてもいいですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 500)

    #C0038
    ChrTalk(
        0x8,
        (
            "#6Pあ、ああ……\x01",
            "なんだか不気味だしよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(50, 720, 17660, 0)
    MoveCamera(33, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13720, 0)
    SetChrPos(0x101, -1060, -280, 17870, 0)
    SetChrPos(0x102, 1060, -280, 17990, 0)
    SetChrPos(0x104, -540, -280, 16850, 0)
    SetChrPos(0x109, 630, -280, 17010, 0)
    SetChrPos(0x105, -50, -280, 16120, 0)
    SetChrPos(0x8, -920, -600, 14160, 0)
    SetChrPos(0x9, 750, -600, 14180, 0)
    SetChrFlags(0xA, 0x80)
    SetMapObjFlags(0x5, 0x4)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x103, 0x0)
    SetChrBattleFlags(0x103, 0x4)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, -40, -130, 18520, 0)
    Sleep(1500)
    FadeToBright(500, 0)
    OP_0D()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    Sound(836, 0, 100, 0)

    #C0039
    ChrTalk(
        0x103,
        (
            "#11P#00203F（カタカタカタカタ……）\x02\x03",

            "#00205F……えっ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#6P#00005Fどうした、ティオ？\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#11P#00201F……差出人の欄に、\x01",
            "『怪盗Ｂ』の名前が……\x02",
        )
    )

    CloseMessageWindow()
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
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0042
    ChrTalk(
        0x102,
        "#00105Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        "怪盗Ｂって……あの！？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        "い、一体どこから……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#6P#00001F……ティオ。\x01",
            "開いてみてくれるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        "#11P#00201F……了解しました。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, 100)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "差出人：怪盗Ｂ\x01",
            "件　名：無題　\x02",
        )
    )

    CloseMessageWindow()

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "親愛なる特務支援課の諸君へ──\x01\x01",
            "まずは此度の私の余興に\x01",
            "心ゆくまで付き合ってもらったことに\x01",
            "感謝の意を表明させていただこう。\x02",
        )
    )

    CloseMessageWindow()

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "人形の所持者であるマリアベル女史、\x01",
            "及び製作者のヨルグ・マイスターには\x01",
            "大変な失礼を働いたことをお詫びする。\x01\x01",
            "ただ、この至高の芸術品に傷がつかないよう\x01",
            "最大の配慮はさせてもらったので、\x01",
            "その点については安心してくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "さて、私は間もなく\x01",
            "この地を去らせていただく。\x01",
            "さらばだ、特務支援課の諸君。\x02",
        )
    )

    CloseMessageWindow()

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《身喰らう蛇》執行者Ｎｏ．Ⅹ、\x01",
            "『怪盗紳士』ブルブラン──\x01",
            "　\x01",
            "諸君の更なる成長を大いに期待し、\x01",
            "女神に健闘を祈らせてもらう事にしよう。\x02",
        )
    )

    CloseMessageWindow()

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ｐ．Ｓ．\x01",
            "この導力メールは自動的に削除される。\x01",
            "保存なども不可能なので諦めるように。\x01",
            "  　　　　　　　　　　　　　──怪盗Ｂ\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(500, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x8)
    OP_64(0x9)

    #C0053
    ChrTalk(
        0x101,
        "#6P#00005F……な……な………………\x02",
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0054
    ChrTalk(
        0x101,
        "#6P#00011F#4S……なんだ、このメールはっ！？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、まさか突然こんな\x01",
            "カミングアウトがあるなんてね。\x02\x03",

            "#10304F《身喰らう蛇》の執行者、\x01",
            "『怪盗紳士』か……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_18DD")

    #C0056
    ChrTalk(
        0x102,
        (
            "#00106Fた、確かに前の時も、\x01",
            "レンちゃんとの関係を\x01",
            "匂わせてはいたけど……\x02\x03",

            "#00107Fそ、そうよ、ティオちゃん！\x01",
            "このメールを出力できないの？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1978")

    label("loc_18DD")


    #C0057
    ChrTalk(
        0x102,
        (
            "#00106Fた、確かにそういう話なら\x01",
            "怪盗Ｂの盗みの技術にも\x01",
            "説明がつくかもしれないけど……\x02\x03",

            "#00107Fそ、そうよ、ティオちゃん！\x01",
            "このメールを出力できないの？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1978")


    #C0058
    ChrTalk(
        0x101,
        (
            "#6P#00005Fそ、そうだ！\x01",
            "もしかすると重要な手がかりに……！\x02",
        )
    )

    CloseMessageWindow()
    Sound(836, 0, 100, 0)

    #C0059
    ChrTalk(
        0x103,
        (
            "#11P#00203F（カタカタカタカタ……）\x01",
            "すでにやっていますが……だめです。\x02\x03",

            "#00200Fメールの開封と同時に、\x01",
            "徐々にデータの自己破壊が\x01",
            "開始していたようですね。\x02\x03",

            "#00206F他の端末には影響はありませんが、\x01",
            "修復はほぼ不可能かと。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#6P#00306Fやれやれ、用意周到なこった。\x02\x03",

            "#00301F昨日ジオフロントで\x01",
            "仕掛けてきた野郎のことも\x01",
            "何も分からずじまいだしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x109,
        (
            "#12P#10103Fそうですね……\x02\x03",

            "#10101Fあのハッキングといい、\x01",
            "とんでもない技術を持っているのは\x01",
            "間違いないと思いますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        "ぼ、僕たちには何がなんだか……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "……っと、クレイ！\x01",
            "一応データに影響がねえか\x01",
            "確認しておかねえと！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "そ、そうだな。\x01",
            "ウイルスでも入ってたら事だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "そう言うわけだから、\x01",
            "僕たちはこれで失礼するよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x8, 1, 0, 10)
    BeginChrThread(0x9, 1, 0, 11)
    Sleep(1200)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0066
    ChrTalk(
        0x101,
        (
            "#6P#00003Fと、とにかく……\x01",
            "ローゼンベルク人形は\x01",
            "これで全部回収できたんだ。\x02\x03",

            "#00000Fこのままマリアベルさんのところに\x01",
            "渡しにいくとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)

    def lambda_1D30():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D30)
    Sleep(50)

    def lambda_1D40():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D40)
    Sleep(50)

    def lambda_1D50():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D50)
    Sleep(50)

    def lambda_1D60():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D60)
    Sleep(100)

    #C0067
    ChrTalk(
        0x102,
        "#00100Fええ……そうしましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ClearChrBattleFlags(0x103, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetChrFlags(0x103, 0x8000)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    OP_64(0x8)
    OP_64(0x9)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_955 end

    def Function_8_1DDF(): pass

    label("Function_8_1DDF")

    OP_93(0xFE, 0xBE, 0x1F4)
    OP_95(0xFE, -3750, -600, 19550, 2000, 0x0)
    OP_95(0xFE, -3600, -600, 15950, 2000, 0x0)
    OP_95(0xFE, -2560, -600, 14690, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_8_1DDF end

    def Function_9_1E2A(): pass

    label("Function_9_1E2A")

    Sleep(1000)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0xFE, -4560, -480, 21280, 135)
    OP_0D()
    OP_95(0xFE, -3750, -600, 19550, 2000, 0x0)
    OP_95(0xFE, -3600, -600, 15950, 2000, 0x0)
    OP_95(0xFE, -3430, -600, 15650, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_9_1E2A end

    def Function_10_1EA0(): pass

    label("Function_10_1EA0")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, -3720, -600, 15980, 2000, 0x0)
    OP_95(0xFE, -3470, -600, 20320, 2000, 0x0)
    OP_95(0xFE, -5210, -480, 21950, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_1EA0 end

    def Function_11_1EEB(): pass

    label("Function_11_1EEB")

    OP_93(0xFE, 0x2D, 0x1F4)
    OP_95(0xFE, 3720, -600, 15950, 2000, 0x0)
    OP_95(0xFE, 3610, -600, 20460, 2000, 0x0)
    OP_95(0xFE, 5110, -480, 21860, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_11_1EEB end

    SaveToFile()

Try(main)
