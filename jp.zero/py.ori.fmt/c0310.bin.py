from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0310.bin",                # FileName
        "c0310",                    # MapName
        "c0310",                    # Location
        0x002B,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 43, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0310",                  # 0
        "ヘルマー",               # 1
        "ジョアンナ",             # 2
        "マクダエル市長",         # 3
        "イス",                   # 4
        "彫像",                   # 5
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
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

    DeclNpc(0,       0,       0,       180,  257,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-45349,  59,      3900,    360,  257,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 12,  41.130001068115234,    44.029998779296875,    0.05999999865889549,   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -20.565000534057617,   -14.676666259765625,   -0.012000001035630703, 1.0])

    DeclActor(-40820,  0,       40910,   1500,    -40820,  1500,    40910,   0x007C, 0,  13, 0x0000)

    ScpFunction((
        "Function_0_254",          # 00, 0
        "Function_1_30C",          # 01, 1
        "Function_2_337",          # 02, 2
        "Function_3_362",          # 03, 3
        "Function_4_38D",          # 04, 4
        "Function_5_518",          # 05, 5
        "Function_6_592",          # 06, 6
        "Function_7_20C7",         # 07, 7
        "Function_8_2478",         # 08, 8
        "Function_9_255C",         # 09, 9
        "Function_10_3EF9",        # 0A, 10
        "Function_11_41A5",        # 0B, 11
        "Function_12_4FC2",        # 0C, 12
        "Function_13_5D65",        # 0D, 13
    ))


    def Function_0_254(): pass

    label("Function_0_254")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_294"),
        (1, "loc_2A0"),
        (2, "loc_2AC"),
        (3, "loc_2B8"),
        (4, "loc_2C4"),
        (5, "loc_2D0"),
        (6, "loc_2DC"),
        (SWITCH_DEFAULT, "loc_2E8"),
    )


    label("loc_294")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_30B")

    Return()

    # Function_0_254 end

    def Function_1_30C(): pass

    label("Function_1_30C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_336")
    OP_94(0xFE, 0xFFFFF63C, 0x0, 0x9C4, 0x73A, 0x3E8)
    Sleep(300)
    Jump("Function_1_30C")

    label("loc_336")

    Return()

    # Function_1_30C end

    def Function_2_337(): pass

    label("Function_2_337")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_361")
    OP_94(0xFE, 0xFFFFF8B2, 0x1A36, 0x744, 0x26DE, 0x3E8)
    Sleep(300)
    Jump("Function_2_337")

    label("loc_361")

    Return()

    # Function_2_337 end

    def Function_3_362(): pass

    label("Function_3_362")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38C")
    OP_94(0xFE, 0xA00A, 0xA05A, 0xB31A, 0xB220, 0x3E8)
    Sleep(300)
    Jump("Function_3_362")

    label("loc_38C")

    Return()

    # Function_3_362 end

    def Function_4_38D(): pass

    label("Function_4_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_39C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 11)

    label("loc_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3C7")
    SetChrPos(0x8, 0, 4059, 7760, 180)
    BeginChrThread(0x8, 0, 0, 2)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_3C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3F1")
    SetChrPos(0x8, 0, 4059, 7760, 180)
    BeginChrThread(0x8, 0, 0, 2)
    SetChrFlags(0x9, 0x80)
    Jump("loc_517")

    label("loc_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_41C")
    SetChrPos(0x8, 0, 4059, 7760, 180)
    BeginChrThread(0x8, 0, 0, 2)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_436")
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_461")
    SetChrPos(0x8, 0, 4059, 13210, 360)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_49D")
    SetChrPos(0x8, 2580, 4000, 13150, 45)
    SetChrPos(0x9, -44780, 60, 47510, 270)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_49D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4C8")
    SetChrPos(0x9, 43580, 0, 43630, 180)
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x9, 0, 0, 3)
    Jump("loc_517")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4F3")
    SetChrPos(0x8, 0, 4059, 7760, 180)
    BeginChrThread(0x8, 0, 0, 2)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_50D")
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_50D")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_517")

    Return()

    # Function_4_38D end

    def Function_5_518(): pass

    label("Function_5_518")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_53F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_558")
    OP_10(0x0, 0x0)
    OP_10(0xB, 0x1)
    Jump("loc_55E")

    label("loc_558")

    OP_10(0x0, 0x1)
    OP_10(0xB, 0x0)

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57A")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_591")

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_591")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_591")

    label("loc_591")

    Return()

    # Function_5_518 end

    def Function_6_592(): pass

    label("Function_6_592")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_67A")

    #C0001
    ChrTalk(
        0xFE,
        (
            "旦那様が聞かれるのは\x01",
            "エリィ様のご意見だけでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "申し訳ございませんが\x01",
            "よろしくお願いいたします。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        (
            "#0100Fおじいさまは政治家だもの……\x01",
            "私の話だって聞き入れてくれるかは\x01",
            "分からないけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E3")

    label("loc_67A")


    #C0004
    ChrTalk(
        0xFE,
        (
            "実は先ほど、今日も旦那様は\x01",
            "残業なさるという連絡があったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "はあ、わたくしは心配でございます。\x01",
            "議会が終わったのでしたら\x01",
            "まずはお体を休めて頂きませんと。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        (
            "#0103Fおじいさまもこだわりの人だから……\x01",
            "今は何を言っても聞かないでしょうね。\x02\x03",

            "#0100Fまた時期をみて\x01",
            "私の方からお願いしておくわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "は、申し訳ございませんが\x01",
            "よろしくお願いいたします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_7E3")

    Jump("loc_20C3")

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_946")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_87E")

    #C0008
    ChrTalk(
        0xFE,
        (
            "昨日は港湾区でも\x01",
            "発砲事件があったとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "ボンド様が何か恐ろしい事件に\x01",
            "巻き込まれていないか、\x01",
            "少々心配でございます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_941")

    label("loc_87E")


    #C0010
    ChrTalk(
        0xFE,
        (
            "先ほどクレイユさんが\x01",
            "いらっしゃいまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "旦那様のボンド様を見かけなかったかと。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "はて、どうかなさったのでしょうかね。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "近頃事件が多いと聞きますし……\x01",
            "少々心配になりますな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_941")

    Jump("loc_20C3")

    label("loc_946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_ABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9DA")

    #C0014
    ChrTalk(
        0xFE,
        (
            "わたくしどもはもう４０年も\x01",
            "旦那様に仕えております。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "それだけに\x01",
            "ハルトマン議長の態度には\x01",
            "許しがたい物を覚えますぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB6")

    label("loc_9DA")


    #C0016
    ChrTalk(
        0xFE,
        (
            "ハルトマン議長は\x01",
            "旦那様と並ぶ自治州代表として\x01",
            "議会を纏めるべきお方ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "議会の放漫ぶりを放置し\x01",
            "どっかりと座っているだけのあの態度……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "旦那様を苦しめている\x01",
            "としか思えませぬ。\x01",
            "まったく許せませんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AB6")

    Jump("loc_20C3")

    label("loc_ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 3)), scpexpr(EXPR_END)), "loc_BA2")

    #C0019
    ChrTalk(
        0xFE,
        (
            "予算議会の方が長引き、\x01",
            "旦那様は残業が続いておられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "ふむ、やはり一番の心配は\x01",
            "旦那様のお体ですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "市長選も４ヵ月後に\x01",
            "控えておりますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#0108Fそうですね……\x01",
            "無理しないといいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D96")

    label("loc_BA2")

    TurnDirection(0xFE, 0x102, 500)

    #C0023
    ChrTalk(
        0xFE,
        (
            "おやエリィ様、\x01",
            "本日は顔色が優れぬようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#0105Fえっ…………！？\x01",
            "そ、そんなことないのよ。\x02\x03",

            "#0103Fヘルマーさん、\x01",
            "変なことを言わないで頂戴。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "そうですか……いやしかし\x01",
            "お嬢様のお苦手な物といえば\x01",
            "例のアレかアレくらいしか……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "いやいや確か幼い頃は\x01",
            "オバケの類もダメでしたでしょうか。\x01",
            "ふむぅ……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0309Fお嬢、意外と\x01",
            "ダメなものがあるんだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x109,
        (
            "#0503Fすみません、変な依頼を\x01",
            "持ってきてしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#0112Fダ、ダメじゃありません。\x01",
            "ノエルさんも恐縮しないで下さい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 3)

    label("loc_D96")

    Jump("loc_20C3")

    label("loc_D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1148")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E49")

    #C0030
    ChrTalk(
        0xFE,
        (
            "そうでしたか……\x01",
            "ともかく、当家の方は\x01",
            "至極安全でございますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "もし何かございましたら\x01",
            "ぜひぜひお隠れになってくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F74")

    label("loc_E49")


    #C0032
    ChrTalk(
        0xFE,
        (
            "これはエリィ様、皆様。\x01",
            "旦那様から大体のお話は\x01",
            "伺っております……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "…………………………（キョロキョロ）\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        "#2S（……当家の方は安全でございます。）\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "#2S（もし何かございましたら、\x01",
            "  ぜひお隠れになってくださいませ！）\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#0100Fあ、ありがとう、ヘルマーさん。\x01",
            "でももう大丈夫ですから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F74")

    Jump("loc_1143")

    label("loc_F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_100E")

    #C0037
    ChrTalk(
        0xFE,
        (
            "そうでしたか……\x01",
            "ともかく、当家の方は\x01",
            "至極安全でございますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "もし何かございましたら\x01",
            "ぜひぜひお隠れになってくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1143")

    label("loc_100E")


    #C0039
    ChrTalk(
        0xFE,
        (
            "これは支援課の皆様。\x01",
            "旦那様から大体のお話は\x01",
            "伺っております……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "…………………………（キョロキョロ）\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "……当マクダエル家の方は\x01",
            "安全でございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "もし何かございましたら、\x01",
            "ぜひエリィ様とともに\x01",
            "お隠れになってくださいませ！\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#0000Fあ、ありがとうございます。\x01",
            "……でももう大丈夫ですから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1143")

    Jump("loc_20C3")

    label("loc_1148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1578")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125C")

    #C0044
    ChrTalk(
        0xFE,
        (
            "いやはや、先ほどの件は\x01",
            "驚きましたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "まったくいつの間に\x01",
            "あのような物を……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "旦那様がお帰りになったら\x01",
            "一番にお知らせせねば。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#0100Fそ、そうですね……\x01",
            "おじいさまには一通り\x01",
            "伝えておいて貰えるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "ハイ、喜んで。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12C4")

    label("loc_125C")


    #C0049
    ChrTalk(
        0xFE,
        (
            "しかし怪盗Ｂですか……\x01",
            "まさか当家に現れるとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "わたくしも、もっと\x01",
            "注意しておくべきでしたな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C4")

    Jump("loc_1573")

    label("loc_12C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1352")

    #C0051
    ChrTalk(
        0xFE,
        (
            "近頃、エリィ様のご活躍が\x01",
            "旦那様のもっぱらの\x01",
            "楽しみのようでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "どうかお仕事の方に\x01",
            "励まれてくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1573")

    label("loc_1352")

    TurnDirection(0xFE, 0x102, 500)

    #C0053
    ChrTalk(
        0xFE,
        "これはエリィお嬢様。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "実は、本日は旦那様も\x01",
            "お早めにお帰りになるそうでして。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        (
            "#0105Fそうだったんですか……\x02\x03",

            "#0104Fよかった、おじいさまにも\x01",
            "たまにはゆっくりして頂かないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "ええ、ジョアンナも張り切って\x01",
            "晩餐の支度をしておりますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "……して、エリィお嬢様の方は\x01",
            "ご一緒なさいますでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#0105Fあ……\x01",
            "……今日は大事な仕事が……\x02\x03",

            "#0106Fごめんなさい、\x01",
            "いつ戻れるか分からないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "そうでしたか、失礼致しました。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "ですが準備だけは整えておきましょう。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "どうかお仕事の方に\x01",
            "励まれてくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1573")

    Jump("loc_20C3")

    label("loc_1578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1679")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15EF")

    #C0062
    ChrTalk(
        0xFE,
        "旦那様も責任感の強いお方……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "使用人としては\x01",
            "お体を案じているのですが\x01",
            "難しい所ですな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1674")

    label("loc_15EF")


    #C0064
    ChrTalk(
        0xFE,
        (
            "旦那様は連日の行事や\x01",
            "パーティ出席で疲れておられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "ふむ、たまにはお早めに戻られるよう\x01",
            "お願い申し上げているのですが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1674")

    Jump("loc_20C3")

    label("loc_1679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_18C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16F1")

    #C0066
    ChrTalk(
        0xFE,
        "左様ですか、残念でございます。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "それではまた十何年か後に\x01",
            "開けてみることと致しましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C1")

    label("loc_16F1")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x102, 500)
    Sleep(500)

    #C0068
    ChrTalk(
        0xFE,
        (
            "おお、エリィお嬢様！\x01",
            "これは良い所に……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#0105Fヘルマーさん、何かあったの！？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "掃除をしておりましたら\x01",
            "屋根裏部屋からこんな木箱が……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "おそらくお嬢様が幼かった頃の\x01",
            "宝物入れかと思うのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "いやあ、あの頃のお嬢様は\x01",
            "とてもお可愛らしく、\x01",
            "綺麗な小物などをお集めになって……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "して、いかが致しましょうか。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        (
            "#0113F……元の場所に\x01",
            "戻しておいてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#0000F（エリィ、意外と\x01",
            "  少女趣味だったんだな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18C1")

    Jump("loc_20C3")

    label("loc_18C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1ACA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_194D")

    #C0076
    ChrTalk(
        0xFE,
        (
            "騒がしくしてしまい\x01",
            "申し訳ございません。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "家人がどなたもいらっしゃらないと\x01",
            "つい掃除がしたくなるもので。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC5")

    label("loc_194D")


    #C0078
    ChrTalk(
        0xFE,
        (
            "これはエリィお嬢様、\x01",
            "バタバタと騒がしくしてしまい\x01",
            "申し訳ございません。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#0100Fヘルマーさん、今日は\x01",
            "随分張り切っているようだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        "ハハ、大した事じゃございませんが。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "毎年この時期は\x01",
            "旦那様は各種行事に参加なさって\x01",
            "あまり戻られないのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "使用人だけですから\x01",
            "その間に大掃除を、と思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "エリィ様が留学なされた頃から\x01",
            "毎年行っているのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1AC5")

    Jump("loc_20C3")

    label("loc_1ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B4D")

    #C0084
    ChrTalk(
        0xFE,
        (
            "旦那様のお立場を考えると\x01",
            "強くお止めするわけにも参りません。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "使用人の立場も\x01",
            "辛いものがありますな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C16")

    label("loc_1B4D")


    #C0086
    ChrTalk(
        0xFE,
        (
            "旦那様の体調も\x01",
            "ようやく戻ってきたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "滋養によいお食事を\x01",
            "用意したのが\x01",
            "功を奏したようですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "ですが、あまり無理は\x01",
            "なさらないで頂きたい……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "お立場上難しい事とは思いますが。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C16")

    Jump("loc_20C3")

    label("loc_1C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C36")
    Call(0, 8)
    Jump("loc_1CDA")

    label("loc_1C36")


    #C0090
    ChrTalk(
        0xFE,
        (
            "娘のジョアンナは７つの頃より\x01",
            "お嬢様の世話役を務めております。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "それだけに、エリィお嬢様を\x01",
            "心配しているのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        "どうか大目に見てやって下さいませ。\x02",
    )

    CloseMessageWindow()

    label("loc_1CDA")

    Jump("loc_20C3")

    label("loc_1CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 2)), scpexpr(EXPR_END)), "loc_20C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFA")
    Call(0, 8)
    Jump("loc_20BB")

    label("loc_1CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D63")

    #C0093
    ChrTalk(
        0xFE,
        "大変差し出がましい事を申しました。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "どうかお仕事に励まれてくださいませ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EF7")

    label("loc_1D63")


    #C0095
    ChrTalk(
        0xFE,
        (
            "昨日はアーネスト様に\x01",
            "お会いになったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "……きっとあの方なりに\x01",
            "エリィ様を気遣っての\x01",
            "ご意見なのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "わたくしどもも\x01",
            "気持ちとしては同じでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "お嬢様が迷い苦しんでいる所を\x01",
            "見るのは心苦しゅうございますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#0104F……ありがとう、ヘルマーさん。\x02\x03",

            "#0100Fでももう大丈夫。\x01",
            "迷いが消えたと思うから。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        "そうでしたか。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "ハハ、これは\x01",
            "差し出がましい事を申しましたね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1EF7")

    Jump("loc_20BB")

    label("loc_1EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F70")

    #C0102
    ChrTalk(
        0xFE,
        (
            "皆様、どうかお嬢様を\x01",
            "よろしくお願い致します。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "わたくしどもにとっても\x01",
            "自慢のお嬢様ですので。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BB")

    label("loc_1F70")


    #C0104
    ChrTalk(
        0xFE,
        (
            "……そちらは同僚の方ですな。\x01",
            "お話は聞き及んでおります。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "皆様、どうかお嬢様を\x01",
            "よろしくお願い致します。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "お嬢様は幼い頃から\x01",
            "とても優秀で、\x01",
            "何よりお可愛らしく……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "わたくしどもにとっても\x01",
            "自慢のお嬢様ですので。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#0112F……ヘルマーさんもあまり\x01",
            "余計な事を言わないで下さいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "ハハ、これは失礼いたしました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20BB")

    Jump("loc_20C3")

    label("loc_20C0")

    Call(0, 7)

    label("loc_20C3")

    TalkEnd(0xFE)
    Return()

    # Function_6_592 end

    def Function_7_20C7(): pass

    label("Function_7_20C7")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x102, 500)
    Sleep(500)

    #C0110
    ChrTalk(
        0x8,
        "これは……エリィお嬢様！？\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "お久しゅうございますね。\x01",
            "警察に入られる前に\x01",
            "立ち寄られて以来でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#0103Fへルマーさん、すみません。\x01",
            "長くご無沙汰していて。\x02\x03",

            "#0100Fこちらは変わりないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        "ええ、それはもう。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "わたくしもジョアンナも\x01",
            "病気一つしておりませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "旦那様は相変わらずというか、\x01",
            "お忙しくしておられますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#0100Fふふ、おじいさまにも困ったものね……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        (
            "#0300F（ぼそぼそ……さすがお嬢の実家だな。\x01",
            "  さりげなくミラが掛かってそうだぜ。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230B")

    #C0118
    ChrTalk(
        0x103,
        (
            "#0200F（執事さんとの会話も\x01",
            "  慣れた感じです。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2384")

    label("loc_230B")


    #C0119
    ChrTalk(
        0x103,
        (
            "#0200F（ええ、確か以前にも\x01",
            "  お邪魔しましたが\x01",
            "  お屋敷の中も立派です。）\x02\x03",

            "（執事さんとの会話も\x01",
            "  慣れた感じかと。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2384")


    #C0120
    ChrTalk(
        0x101,
        (
            "#0000F（はは……マクダエル家っていえば\x01",
            "  昔からの名家らしいからね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C0121
    ChrTalk(
        0x102,
        (
            "#0106F……こういう事になるから\x01",
            "家には連れて来たく\x01",
            "なかったのよね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 2)
    Return()

    # Function_7_20C7 end

    def Function_8_2478(): pass

    label("Function_8_2478")


    #C0122
    ChrTalk(
        0xFE,
        "皆様は、小説は読まれますか？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "仕事の合間に読んでいたのですが\x01",
            "私はもう読み終わりましたので\x01",
            "差し上げます。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "どうぞお受け取りください。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0125
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2C9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2C9, 1)
    SetScenarioFlags(0x9C, 3)
    Return()

    # Function_8_2478 end

    def Function_9_255C(): pass

    label("Function_9_255C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_271D")
    TurnDirection(0x9, 0x102, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25F9")

    #C0126
    ChrTalk(
        0xFE,
        (
            "特務支援課のお仕事は\x01",
            "とても立派だと聞いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "どうか皆さんも頑張ってください。\x01",
            "……お帰りをお待ちしています。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2718")

    label("loc_25F9")


    #C0128
    ChrTalk(
        0xFE,
        (
            "旦那様は今日も\x01",
            "帰りが遅いみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        "……お嬢様もお仕事ですか？\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "特務支援課のお仕事は\x01",
            "とても立派だと聞いています。\x01",
            "どうか頑張ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        (
            "#0100Fええ、ありがとうジョアンナ。\x01",
            "おじいさまの方は頼むわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "はい、お任せください。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2718")

    Jump("loc_3EF5")

    label("loc_271D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2763")
    TurnDirection(0x9, 0x102, 0)

    #C0134
    ChrTalk(
        0xFE,
        "……エリィ様、どうかお気をつけて。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2921")

    label("loc_2763")


    #C0135
    ChrTalk(
        0xFE,
        "近頃事件の噂ばかり聞きます。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "警察で働いてらっしゃる\x01",
            "エリィ様の身が心配です。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        (
            "#0100Fあはは……私は\x01",
            "ジョアンナやヘルマーさんの方が\x01",
            "心配なのだけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0000F確かにエリィの実家って\x01",
            "普段は使用人さんしかいないもんな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_28E3")

    #C0140
    ChrTalk(
        0x104,
        (
            "#0300Fま、この辺りは\x01",
            "治安もいいから大丈夫だろ。\x02\x03",

            "#0303F……お隣の件は\x01",
            "ちょいとばかし不可解だが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_291E")

    label("loc_28E3")


    #C0141
    ChrTalk(
        0x104,
        (
            "#0300Fま、この辺りは\x01",
            "治安もいいから大丈夫なはずだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_291E")

    SetScenarioFlags(0x0, 1)

    label("loc_2921")

    Jump("loc_3EF5")

    label("loc_2926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2C09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_29C2")
    TurnDirection(0xFE, 0x102, 500)

    #C0142
    ChrTalk(
        0xFE,
        "エリィ様……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "怖いことがあるなら\x01",
            "無理なさらないで下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x102,
        (
            "#0106F（隠しているのに\x01",
            "  どうして分かるのかしら……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C04")

    label("loc_29C2")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x102, 500)

    #C0145
    ChrTalk(
        0xFE,
        (
            "………………………………？\x01",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        "エリィ様、あの……\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        "#0100Fな、なあにジョアンナ。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "もし怖いことがあるなら\x01",
            "いつでも私を呼びつけてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "昔のように……\x01",
            "添い寝でも夜のお手洗いでも\x01",
            "お付き合いいたしますから。\x02",
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

    #C0150
    ChrTalk(
        0x109,
        (
            "#0500Fすみません、\x01",
            "本当にすみません……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        (
            "#0113Fも、もう……\x01",
            "昔の話だってば……！\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        (
            "#0200F昔はジョアンナさんの\x01",
            "お世話になってたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#0000F（はは……\x01",
            "  意外と可愛い所があるよな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C04")

    Jump("loc_3EF5")

    label("loc_2C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3041")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D0E")
    TurnDirection(0xFE, 0x102, 500)

    #C0154
    ChrTalk(
        0xFE,
        "……今夜はご馳走を作ります。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "ぜひ旦那様と\x01",
            "ご一緒なさってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        (
            "#0104Fそうね、そうしたいかも。\x02\x03",

            "#0100F……それじゃあ\x01",
            "支度の方はお願いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "…………………………（コクコク）\x01",
            "お任せください……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ED6")

    label("loc_2D0E")

    TurnDirection(0xFE, 0x102, 500)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0158
    ChrTalk(
        0xFE,
        "………………………………！\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "エリィ様……\x01",
            "ご無事だったのですね……！\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#0103Fジョアンナ……ごめんなさい。\x01",
            "しばらく顔を出すこともできなくて。\x02\x03",

            "#0100Fジョアンナにも\x01",
            "沢山心配を掛けてしまったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "……………………（フルフル）\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        "お嬢様を信じていました。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x102,
        (
            "#0109Fあはは、そう……\x02\x03",

            "#0100Fありがとう、また今夜にでも\x01",
            "寄らせてもらうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "…………………………（コクコク）\x01",
            "あの、お待ちしています……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2ED6")

    Jump("loc_303C")

    label("loc_2EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F1C")

    #C0165
    ChrTalk(
        0xFE,
        (
            "……お嬢様を\x01",
            "よろしくお願いします。（ペコリ）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_303C")

    label("loc_2F1C")

    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0166
    ChrTalk(
        0xFE,
        "………………………………！\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "あの、エリィ様は……\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#0006Fゴメン、今日は\x01",
            "一緒じゃないんだ。\x02\x03",

            "#0000Fでもみんな元気だから\x01",
            "安心してくれ。\x01",
            "事件も一応解決したしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "………………………………（コクリ）\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "お嬢様をよろしく\x01",
            "お願いします。（ペコリ）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_303C")

    Jump("loc_3EF5")

    label("loc_3041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_339B")
    TurnDirection(0x9, 0x102, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3204")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31BE")

    #C0171
    ChrTalk(
        0xFE,
        (
            "エリィ様……お話は聞きました。\x01",
            "怪盗Ｂと対決なさったとか……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    #C0172
    ChrTalk(
        0xFE,
        (
            "あの、今度からは\x01",
            "ジョアンナのフライパンを\x01",
            "持って行って下さい。\x02",
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

    #C0173
    ChrTalk(
        0x102,
        "#0105Fあ、ありがとう、ジョアンナ。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        "#0000F（防御に使えって事なのかな。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31FF")

    label("loc_31BE")


    #C0175
    ChrTalk(
        0xFE,
        "お嬢様……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "……お仕事をなさる時は\x01",
            "どうかお気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31FF")

    Jump("loc_3396")

    label("loc_3204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3284")

    #C0177
    ChrTalk(
        0xFE,
        (
            "今日は旦那様も\x01",
            "早めにお帰りになるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "エリィ様、お仕事頑張ってください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3396")

    label("loc_3284")


    #C0179
    ChrTalk(
        0xFE,
        (
            "今日は旦那様も\x01",
            "早めにお帰りになるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "……………あの…………\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFE)

    #C0181
    ChrTalk(
        0xFE,
        "……いえ。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "皆さん、お仕事頑張ってください。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x104,
        (
            "#0300F（おい、お嬢に\x01",
            "  何か言いたそうだぞ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        (
            "#0103F（ごめんねジョアンナ、\x01",
            "  今日の仕事は外せないの……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3396")

    Jump("loc_3EF5")

    label("loc_339B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_33F5")

    #C0185
    ChrTalk(
        0xFE,
        "今日はパレードだったのですね。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "子供たちも楽しそうで良かったです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EF5")

    label("loc_33F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_354D")
    TurnDirection(0x9, 0x102, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_345C")

    #C0187
    ChrTalk(
        0xFE,
        (
            "エリィ様のお部屋は\x01",
            "毎日掃除しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        "……どうかご心配なく。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3548")

    label("loc_345C")


    #C0189
    ChrTalk(
        0xFE,
        "エリィ様……\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "毎日ベッドメイクしているので\x01",
            "いつでもお休みになれますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x102,
        "#0105Fあ、ありがとう、ジョアンナ。\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x104,
        (
            "#0300F（過保護っつーか\x01",
            "  過想いなメイドさんだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        (
            "#0100F（ジョアンナは\x01",
            "  私とは同い年なんだけど。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3548")

    Jump("loc_3EF5")

    label("loc_354D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_361C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_35A0")

    #C0194
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "旦那様のお体、少し心配です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3617")

    label("loc_35A0")


    #C0196
    ChrTalk(
        0xFE,
        "旦那様のお部屋を掃除しているのです。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        "ついでにカーテンの調整を……\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        "日差しが強いとお体に障りますから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3617")

    Jump("loc_3EF5")

    label("loc_361C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_38BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3685")
    TurnDirection(0x9, 0x102, 0)

    #C0199
    ChrTalk(
        0xFE,
        (
            "お嬢様、どうか\x01",
            "お仕事頑張ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        "私も応援していますから。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38B5")

    label("loc_3685")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x102, 500)
    Sleep(500)

    #C0201
    ChrTalk(
        0xFE,
        "エリィ様……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "申し訳ありません、私今まで\x01",
            "とんだ勘違いをしていて……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#0105Fジョアンナ……？\x01",
            "（何かあったのかしら……）\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "特務支援課とは\x01",
            "素晴らしい部署なのですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "あの捜査一課以上の権限を持ち\x01",
            "数々の功績を残す\x01",
            "スーパーエリート集団だとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "……どうか、今までの\x01",
            "勘違いをお許しください。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0207
    ChrTalk(
        0x104,
        "#0306F（そいつは過大評価だよなぁ。）\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        (
            "#0108F（困ったわ……\x01",
            "  ジョアンナは少し\x01",
            "  思い込みが激しいのよね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_38B5")

    Jump("loc_3EF5")

    label("loc_38BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3939")

    #C0209
    ChrTalk(
        0xFE,
        (
            "支援課のセルゲイ警部は\x01",
            "昼間からダラダラしている\x01",
            "ダメな方だとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AA4")

    label("loc_3939")


    #C0211
    ChrTalk(
        0xFE,
        (
            "……支援課の責任者は\x01",
            "セルゲイ警部という方だそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "昼間からダラダラしている\x01",
            "ダメな方だとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#0003F（課長が不信感を持たれている……）\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x104,
        (
            "#0306F（ま、当然だろうなぁ。）\x02\x03",

            "#0300F（このままマクダエル家の力で\x01",
            "  潰されなきゃいいんだが。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0216
    ChrTalk(
        0x102,
        "#0103F（……そんな物ありませんから。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3AA4")

    Jump("loc_3EF5")

    label("loc_3AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 3)), scpexpr(EXPR_END)), "loc_3EF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3CE6")
    TurnDirection(0x9, 0x102, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3B3C")

    #C0217
    ChrTalk(
        0xFE,
        (
            "エリィ様の才能でしたら\x01",
            "どんなお仕事にでも就けると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "……いつでも\x01",
            "お戻りになってください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE1")

    label("loc_3B3C")


    #C0219
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x102,
        "#0105Fジョアンナ、どうかしたの？\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        "いえ、その……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "特務支援課というのは\x01",
            "不遇の部署だと聞いたもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0224
    ChrTalk(
        0x103,
        (
            "#0200F（エリィさん、かなり\x01",
            "  心配されていますね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#0103F（ごめんねジョアンナ……\x01",
            "  私はもう少し\x01",
            "  支援課#6Rこ こ#でやってみたいの。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3CE1")

    Jump("loc_3EED")

    label("loc_3CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3D60")

    #C0226
    ChrTalk(
        0xFE,
        (
            "エリィ様の才能でしたら\x01",
            "どんなお仕事にでも就けると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "……いつでも\x01",
            "お戻りになってください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EED")

    label("loc_3D60")


    #C0228
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x102,
        "#0105Fジョアンナ、どうかしたの？\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        "いえ、その……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "特務支援課というのは\x01",
            "不遇の部署だと聞いたもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0233
    ChrTalk(
        0x103,
        (
            "#0200F（エリィさん、かなり\x01",
            "  心配されていますね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x102,
        (
            "#0106F（そ、そうなのよね。\x01",
            "  ジョアンナは心配性だから……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3EED")

    Jump("loc_3EF5")

    label("loc_3EF2")

    Call(0, 10)

    label("loc_3EF5")

    TalkEnd(0xFE)
    Return()

    # Function_9_255C end

    def Function_10_3EF9(): pass

    label("Function_10_3EF9")

    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x102, 500)
    Sleep(500)

    #C0235
    ChrTalk(
        0x9,
        "あ……\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x9,
        "エリィ様……\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        (
            "#0100Fジョアンナ、久し振りね。\x02\x03",

            "ごめんなさい、\x01",
            "突然顔を出してしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x9,
        "……………………（フルフル）\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x9,
        (
            "すぐにお食事をご用意します。\x01",
            "丁度支度中でしたので。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x9,
        (
            "……あの、警察を辞めて\x01",
            "戻られたのでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    #C0241
    ChrTalk(
        0x9,
        "お部屋着は洗濯していつもの所に……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x9,
        (
            "あのあの、お部屋の方も\x01",
            "毎日ベッドメイクをしていますから\x01",
            "すぐにお使いいただけますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x102,
        (
            "#0106Fえっと、ごめんなさい。\x01",
            "ジョアンナの顔を見に来ただけで……\x02\x03",

            "警察を辞めたわけではないの。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    #C0244
    ChrTalk(
        0x9,
        (
            "そ、そうですか。\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x9,
        (
            "失礼しました。\x01",
            "あの、お仕事頑張ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        (
            "#0100F……うん。\x01",
            "ありがとう、ジョアンナ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 3)
    Return()

    # Function_10_3EF9 end

    def Function_11_41A5(): pass

    label("Function_11_41A5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50235.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch50236.itc", 0x20)
    OP_68(45500, 1200, 48400, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 44700, 250, 48500, 90)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, 46100, 550, 48650, 180)
    ClearMapObjFlags(0x5, 0x4)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x5, 0xB)
    OP_49()
    SetChrPos(0xB, 44500, 0, 48600, 0)
    OP_D3(0xB, 0x0, 0x0, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0247
    AnonymousTalk(
        0x102,
        (
            "そ、そんな……\x02\x03",

            "明日から復帰するなんて\x01",
            "そんなの早すぎます……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(20000, 2500)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0248
    ChrTalk(
        0xA,
        (
            "#11P#6503Fなに、たかが\x01",
            "打撲と捻挫くらいだ。\x02\x03",

            "#6500F５日も休んでしまって\x01",
            "むしろ英気が養えたくらいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        (
            "#6P#0106Fじょ、冗談言わないでください！\x02\x03",

            "#0108Fあれほどの事があって\x01",
            "第一秘書がいなくなって……\x02\x03",

            "#0101F今はゆっくりと\x01",
            "お休みになるべきです！\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "#11P#6500F創立記念祭も近い。\x01",
            "仕事は山のようにあるからね。\x02\x03",

            "#6509Fこの程度のことで\x01",
            "市長としての役割を放棄できんさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        "#6P#0106Fこの程度のことって……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    #C0252
    ChrTalk(
        0x102,
        (
            "#6P#0108Fおじいさまは……\x01",
            "辛く……悔しくないんですか？\x02\x03",

            "あれだけ目をかけていた\x01",
            "アーネストさんに裏切られて……\x02\x03",

            "それなのにどうして……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    #C0253
    ChrTalk(
        0xA,
        (
            "#5P#6503F……今回のことがショックで\x01",
            "無かったといえば嘘になる。\x02\x03",

            "聞けば、随分前から事務所の\x01",
            "資金を使い込んでいたようだ。\x02\x03",

            "それで精神的に追い詰められ、\x01",
            "暴走してしまったのかもしれない。\x02\x03",

            "その意味では、気付いてやれなかった\x01",
            "私の責任でもあると思っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        "#6P#0105F……おじいさま……\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xA,
        (
            "#5P#6501F──だが、私は政治家だ。\x02\x03",

            "この身をクロスベル自治州の\x01",
            "現在#4Rい ま#と未来のために奉げると誓った。\x02\x03",

            "如何なることがあろうと、\x01",
            "職務を全うする以外の選択はない。\x02\x03",

            "そう、自分に課しているのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x102,
        "#6P#0108F……………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0257
    ChrTalk(
        0xA,
        (
            "#11P#6503Fすまない、エリィ。\x02\x03",

            "１０年前も私は……\x01",
            "ライアン君を、お前の父さんを\x01",
            "引き止めてやれなかった。\x02\x03",

            "#6503Fそして娘も……お前の母さんも\x01",
            "去るがままにしてしまった。\x02\x03",

            "そして相変わらず……\x01",
            "無力だが必要ではある\x01",
            "クロスベル市長を続けている。\x02\x03",

            "#6501Fさぞ……恨んでいる事だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x102,
        (
            "#6P#0101Fそんな……！\x01",
            "おじいさまは私の誇りです！\x02\x03",

            "#0108Fお父さまや、お母さまとは\x01",
            "たまに連絡はしていますし……\x02\x03",

            "#0106F哀しかったけど……\x01",
            "きちんと乗り越えています。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xA,
        "#11P#6500Fエリィ……\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        (
            "#6P#0103F元々私が警察に入ったのは……\x01",
            "別の形で、おじいさまの\x01",
            "手伝いがしたかったからです。\x02\x03",

            "それが、クロスベルのためにも\x01",
            "なると信じていたから……\x02\x03",

            "#0108F……でも、こんな事になって\x01",
            "アーネストさんが居なくなって……\x02\x03",

            "#0101F私、やっぱり警察を辞めて\x01",
            "おじいさまの手伝いを──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0261
    ChrTalk(
        0xA,
        "#11P#6507F#4S#N馬鹿な事を言っちゃいかん！\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0262
    ChrTalk(
        0x102,
        "#6P#0105Fお、おじいさま……？\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xA,
        (
            "#11P#6501F……もしお前が、\x01",
            "選んだ道を悔やんでいるのなら\x01",
            "すぐにでも戻ってくるべきだ。\x02\x03",

            "だが、そうでは無いのだろう？\x02\x03",

            "なのに道を変えるというのは\x01",
            "多くの者に対して失礼だ。\x02\x03",

            "#6503F同僚にも、私にも\x01",
            "……何よりお前自身にも。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        "#6P#0108Fあ……\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xA,
        (
            "#11P#6500F私の事は心配はいらない。\x02\x03",

            "秘書は一人ではないし、\x01",
            "いざとなればヘルマーだって\x01",
            "助けてくれるだろう。\x02\x03",

            "次の市長選を期に引退することは\x01",
            "少し難しくなってしまったが……\x02\x03",

            "#6509Fなに、もう５年、\x01",
            "楽隠居が遠のくだけのことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x102,
        "#6P#0106F………………………………\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xA,
        (
            "#11P#6503Fだからお前は……\x01",
            "選んだ道を全うしてみなさい。\x02\x03",

            "少なくとも……\x01",
            "お前自身が納得できるまで。\x02\x03",

            "#6500Fそれが私にとっては\x01",
            "何よりの励みになるのだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x102,
        "#6P#0108Fおじいさま……\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xA,
        (
            "#11P#6503Fそもそも、今回の事件も\x01",
            "お前たちの働きが無かったら\x01",
            "私は生きてはいなかったはずだ。\x02\x03",

            "#6500F誇りなさい。\x01",
            "自分たちの働きと成長を。\x02\x03",

            "そして一層輝けるよう、\x01",
            "自分を磨いて行くといいだろう。\x02\x03",

            "#6509Fアルカンシェルの\x01",
            "今回の新作のようにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x102,
        (
            "#6P#0105Fあ……\x02\x03",

            "#0102Fはい、おじいさま……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x102, 0x4)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 44700, 0, 47600, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetCameraDistance(19500, 800)
    Fade(500)
    SetChrSubChip(0x102, 0x1)
    Sound(804, 0, 80, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    OP_0D()
    Sleep(500)

    #C0271
    ChrTalk(
        0x102,
        (
            "#6P#0104Fエリィ・マクダエル──\x02\x03",

            "#0100F明日をもって職場復帰し、\x01",
            "より一層職務に励みます……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 1)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_41A5 end

    def Function_12_4FC2(): pass

    label("Function_12_4FC2")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    EndChrThread(0x8, 0x0)
    OP_68(41010, 1500, 43700, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 41690, 60, 43300, 90)
    SetChrPos(0x102, 41690, 60, 44420, 90)
    SetChrPos(0x103, 40640, 60, 43300, 90)
    SetChrPos(0x104, 40550, 60, 44420, 90)
    SetChrPos(0x8, 37190, 60, 43820, 90)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_78(0x6, 0xC)
    OP_49()
    SetChrPos(0xC, 45500, 0, 43500, 0)
    ClearMapObjFlags(0x3, 0x4)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    OP_0D()

    #C0272
    ChrTalk(
        0x102,
        "#5P#0105Fあっ……！？\x02",
    )

    CloseMessageWindow()
    OP_68(43290, 1500, 44170, 2000)
    MoveCamera(54, 18, 0, 2000)

    def lambda_50E9():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_50E9)

    def lambda_50FE():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_50FE)

    def lambda_5113():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5113)

    def lambda_5128():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5128)
    Sleep(2000)

    #C0273
    ChrTalk(
        0x101,
        "#12P#0011Fな……これは……！？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x104,
        "#6P#0305Fおいおい、まさか……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x103,
        (
            "#12P#0200F間違いないです。\x01",
            "市庁舎から盗まれた彫像\x01",
            "『聖者の祈り』ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x102,
        (
            "#6P#0105Fどうして……\x01",
            "どうやっておじいさまの部屋に！？\x02",
        )
    )

    CloseMessageWindow()

    #N0277
    NpcTalk(
        0x8,
        "男性の声",
        "#2Pお嬢様、どうかなさいましたか。\x02",
    )

    CloseMessageWindow()
    OP_68(42240, 1500, 44090, 1800)
    MoveCamera(55, 26, 0, 1800)

    def lambda_525D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_525D)
    Sleep(12)

    def lambda_526D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_526D)

    def lambda_527A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_527A)
    Sleep(15)

    def lambda_528A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_528A)

    def lambda_5297():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5297)
    OP_95(0x8, 40640, 60, 43910, 1500, 0x0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0278
    ChrTalk(
        0x8,
        (
            "#6Pお、おやこれは……！？\x01",
            "皆様がお運びになったので？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        "#11P#0203Fとんでもないです。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        (
            "#11P#0001F話せば長くなるんですが……\x01",
            "どうも怪盗Ｂという\x01",
            "賊の仕業らしいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        (
            "#6P怪盗Ｂ……\x01",
            "あの有名な……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x102,
        (
            "#5P#0101Fヘルマーさん、今日家の方に\x01",
            "怪しい人が来たりはしなかった？\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x8,
        "#6Pええ、本日はお客様は１人も。\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        (
            "#6P旦那様もお忙しい日ですから\x01",
            "どなたもいらっしゃっていませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x104,
        (
            "#5P#0306F目撃者もなしかよ。\x01",
            "一体どうやって運び込んだんだ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_54A0():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_54A0)
    Sleep(50)

    def lambda_54B0():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_54B0)
    Sleep(50)

    def lambda_54C0():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_54C0)
    Sleep(50)

    def lambda_54D0():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_54D0)
    Sleep(500)

    #C0286
    ChrTalk(
        0x101,
        (
            "#12P#0003Fこればかりは\x01",
            "まったく判らないな……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0287
    ChrTalk(
        0x101,
        (
            "#12P#0005F待ってくれ。\x01",
            "彫像の側面にカードが……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_555D():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_555D)

    def lambda_556A():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_556A)

    def lambda_5577():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5577)
    OP_95(0x101, 44380, 0, 42120, 1000, 0x0)
    OP_93(0x101, 0x2D, 0x190)
    Sleep(800)
    OP_95(0x101, 42890, 60, 43300, 1000, 0x0)

    def lambda_55B6():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55B6)

    def lambda_55C3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_55C3)

    def lambda_55D0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_55D0)

    def lambda_55DD():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_55DD)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特務支援課の諸君、ご苦労だった。\x01",
            "楽しき余興のお陰で\x01",
            "この虚構の街の祝祭も\x01",
            "一層堪能させてもらった。\x01",
            "諸君の勇気と頑張りには敬意を表そう。\x02",
        )
    )

    CloseMessageWindow()

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "残念ながら私にも立場がある。\x01",
            "現時点ではこれ以上\x01",
            "立ち入るつもりはないので安心したまえ。\x02",
        )
    )

    CloseMessageWindow()

    #A0290
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＰＳ．昨日は私の知己たる仔猫が\x01",
            "      世話になったようだ。\x01",
            "      諸君の誠意に感謝しよう。\x01",
            "                ──怪盗Ｂ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #C0291
    ChrTalk(
        0x103,
        (
            "#12P#0200Fどうやら向こうは\x01",
            "楽しんでいたようですね。\x01",
            "……少し悔しいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x102,
        (
            "#5P#0105Fそれにしても、\x01",
            "この“知己たる仔猫”っていうのは……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0293
    ChrTalk(
        0x101,
        "#12P#0001Fもしかして……仔猫#4Rキティ#、か？\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0294
    ChrTalk(
        0x104,
        (
            "#6P#0305F……レンのことだってのか！？\x02\x03",

            "#0301Fいや……結社と怪盗Ｂが\x01",
            "繋がってると仮定すれば\x01",
            "考えられない話じゃねぇが……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#12P#0008F……現時点じゃ確認のしようがない。\x01",
            "とりあえず置いておくとしよう。\x02\x03",

            "#0006Fそれにしても……怪盗Ｂは\x01",
            "他人を引っ掻き回すのが\x01",
            "随分得意なヤツみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        "#12P#0203F重ね重ね、むかつきますね。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x102,
        (
            "#5P#0103Fでもよかった……\x01",
            "向こうも大事#4Rおおごと#にするつもりは\x01",
            "無かったみたいね。\x02\x03",

            "#0100Fこれ以上事件を起こす事は\x01",
            "無いんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x104,
        (
            "#6P#0306F逮捕はできなかったが……\x01",
            "まぁ今回はこれで\x01",
            "良しとするしかねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそうだな……盗まれた品は\x01",
            "無事に見つけ出した訳だし。\x02\x03",

            "#0001Fよし、そうと決まれば……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B87():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5B87)
    Sleep(50)

    def lambda_5B97():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5B97)
    Sleep(50)

    def lambda_5BA7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5BA7)
    Sleep(50)

    def lambda_5BB7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5BB7)
    Sleep(300)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0300
    ChrTalk(
        0x101,
        (
            "#12P#0006F……とりあえず。\x01",
            "市庁舎のクリップさんに連絡して\x01",
            "運送業者を手配してもらおう。\x02\x03",

            "こんな大きな物、\x01",
            "俺たちだけじゃ運べないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x102,
        (
            "#6P#0106Fそうねぇ……\x01",
            "本当にどうやって\x01",
            "運び込んだのかしら。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_4FC2 end

    def Function_13_5D65(): pass

    label("Function_13_5D65")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『猫でもできる！おいしいケーキの作り方』\x01",
            "という本がある。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x11)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E37")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0303
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピが書かれていた。\x02",
        )
    )

    CloseMessageWindow()

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x11)

    label("loc_5E37")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_13_5D65 end

    SaveToFile()

Try(main)
