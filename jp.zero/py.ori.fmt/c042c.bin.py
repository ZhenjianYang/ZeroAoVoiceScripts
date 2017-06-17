from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c042c.bin",                # FileName
        "c042c",                    # MapName
        "c042c",                    # Location
        0x0023,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 2, 0, 3],
    )

    BuildStringList((
        "c042c",                  # 0
        "アバン劇団長",           # 1
        "イリア",                 # 2
        "リーシャ",               # 3
        "ニコル",                 # 4
        "ハインツ",               # 5
        "シュリ",                 # 6
    ))

    AddCharChip((
        "chr/ch05100.itc",                   # 00
        "chr/ch05200.itc",                   # 01
        "chr/ch27500.itc",                   # 02
        "chr/ch24200.itc",                   # 03
        "chr/ch36800.itc",                   # 04
        "chr/ch10100.itc",                   # 05
    ))

    DeclNpc(-1480,   0,       15689,   45,   261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-209,    0,       15550,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1330,    0,       15699,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-68150,  0,       2150,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-66489,  0,       7329,    0,    261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(64569,   0,       4590,    315,  389,  0x0, 0,   5,   0,   0,   1,   0,   9,   255,  0)

    ScpFunction((
        "Function_0_18C",          # 00, 0
        "Function_1_244",          # 01, 1
        "Function_2_26F",          # 02, 2
        "Function_3_330",          # 03, 3
        "Function_4_331",          # 04, 4
        "Function_5_7E9",          # 05, 5
        "Function_6_A2D",          # 06, 6
        "Function_7_B26",          # 07, 7
        "Function_8_BFF",          # 08, 8
        "Function_9_D1F",          # 09, 9
        "Function_10_FB9",         # 0A, 10
        "Function_11_10C5",        # 0B, 11
        "Function_12_2BE0",        # 0C, 12
        "Function_13_3303",        # 0D, 13
    ))


    def Function_0_18C(): pass

    label("Function_0_18C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1CC"),
        (1, "loc_1D8"),
        (2, "loc_1E4"),
        (3, "loc_1F0"),
        (4, "loc_1FC"),
        (5, "loc_208"),
        (6, "loc_214"),
        (SWITCH_DEFAULT, "loc_220"),
    )


    label("loc_1CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_1D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_1E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_1F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_1FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_208")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_214")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_220")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_22C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_243")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_243")

    Return()

    # Function_0_18C end

    def Function_1_244(): pass

    label("Function_1_244")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26E")
    OP_94(0xFE, 0xF4D8, 0x532, 0x1054A, 0x15AE, 0x3E8)
    Sleep(300)
    Jump("Function_1_244")

    label("loc_26E")

    Return()

    # Function_1_244 end

    def Function_2_26F(): pass

    label("Function_2_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2B3")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, -66690, 0, 4990, 0)
    SetChrPos(0xC, -66690, 0, 6530, 180)
    Jump("loc_32F")

    label("loc_2B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D3")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_32F")

    label("loc_2D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_30E")
    SetChrPos(0x8, -1880, 10, 15240, 135)
    SetChrPos(0xA, -210, 0, 13820, 0)
    OP_93(0x9, 0xB4, 0x0)
    Jump("loc_32F")

    label("loc_30E")

    BeginChrThread(0x9, 2, 0, 13)
    BeginChrThread(0xA, 2, 0, 13)
    BeginChrThread(0x8, 2, 0, 13)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_32F")

    Return()

    # Function_2_26F end

    def Function_3_330(): pass

    label("Function_3_330")

    Return()

    # Function_3_330 end

    def Function_4_331(): pass

    label("Function_4_331")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35A")
    Call(0, 11)
    Return()

    label("loc_35A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_469")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3CF")

    #C0001
    ChrTalk(
        0x8,
        (
            "今日の人出では\x01",
            "迷子になるのも無理はないだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "早く見つかる事を祈っているよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_464")

    label("loc_3CF")


    #C0003
    ChrTalk(
        0x8,
        (
            "ああ、ロイド君か。\x01",
            "男の子が迷子になったそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "ふむ、外は記念祭の人出だし\x01",
            "今日はパレードもあった……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "早く見つかるといいんだが。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_464")

    Jump("loc_7E5")

    label("loc_469")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_47A")
    Jump("loc_7E5")

    label("loc_47A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_70D")

    #C0006
    ChrTalk(
        0x8,
        (
            "明日からはまた\x01",
            "イリア君の公演がある……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "この大事な時期に\x01",
            "ストーカーが出るなんて\x01",
            "居ても立ってもいられないよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "どうか、早急に\x01",
            "捕まえてはくれないだろうか！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【断る】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_649")
    TalkEnd(0xFE)
    EventBegin(0x0)
    StopBGM(0x5DC)
    Fade(500)
    OP_68(-250, 1670, 13660, 0)
    MoveCamera(32, 29, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14970, 0)
    SetChrPos(0x101, 260, 120, 13350, 346)
    SetChrPos(0x102, -850, 450, 12100, 346)
    SetChrPos(0x103, -840, 0, 13680, 346)
    SetChrPos(0x104, 300, 450, 12100, 346)
    SetChrPos(0x8, -1480, 0, 15690, 180)
    SetChrPos(0xA, 1330, 0, 15700, 225)
    OP_93(0x9, 0xB4, 0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    OP_0D()
    OP_29(0x1D, 0x1, 0x1)
    Call(0, 12)
    Return()

    label("loc_649")


    #C0009
    ChrTalk(
        0x101,
        (
            "#0006Fすみません……まだ\x01",
            "他の仕事が残っていまして。\x01",
            "今は手が離せないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "そうか……\x01",
            "それなら仕方ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "手が空いたら頼めないだろうか。\x01",
            "何としても\x01",
            "早急に解決して欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E5")

    label("loc_70D")


    #C0012
    ChrTalk(
        0xFE,
        (
            "ふむ、試してみる\x01",
            "価値はありそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "しかしリーシャ君も大したものだ。\x01",
            "このイリア君の無茶なオーダーに\x01",
            "応えられるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "#1700Fあはは、だってリーシャだもの。\x02\x03",

            "#1709F見込んだあたしの目に\x01",
            "狂いはなーい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E5")

    TalkEnd(0xFE)
    Return()

    # Function_4_331 end

    def Function_5_7E9(): pass

    label("Function_5_7E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_812")
    Call(0, 11)
    Return()

    label("loc_812")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_948")

    #C0015
    ChrTalk(
        0x9,
        (
            "#1704Fさて、今の内に\x01",
            "稽古の続きでもやりますか。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0xA, 0x9, 500)
    TurnDirection(0x8, 0x9, 500)

    #C0016
    ChrTalk(
        0xA,
        (
            "#1801Fいえ、待ってください\x01",
            "イリアさん！！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "そうだよ、今はお預けだ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    #C0018
    ChrTalk(
        0x9,
        (
            "#1706Fちぇー、いいじゃない。\x01",
            "暇なんだしー。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#0006F（引き受けるなら\x01",
            "  早くした方が良さそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x1F4)
    OP_93(0x8, 0x87, 0x1F4)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    Jump("loc_A29")

    label("loc_948")


    #C0020
    ChrTalk(
        0x9,
        (
            "#1700F次の登場シーンなんだけどね、\x01",
            "もちっとタイミングを……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "#1800Fそうですね、私もその方が\x01",
            "合わせやすいですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0000F（稽古の相談中みたいだな。）\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#0100F（今日は休館日らしいけど、\x01",
            "  ３人とも熱心よね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A29")

    TalkEnd(0xFE)
    Return()

    # Function_5_7E9 end

    def Function_6_A2D(): pass

    label("Function_6_A2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A56")
    Call(0, 11)
    Return()

    label("loc_A56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_B1F")

    #C0024
    ChrTalk(
        0xA,
        (
            "#1803Fすみません、イリアさんは\x01",
            "こういう事に疎くて。\x02\x03",

            "#1808F私も日中は\x01",
            "対処できないし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0025
    ChrTalk(
        0xA,
        (
            "#1801Fあ、あのともかく皆さん、\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B22")

    label("loc_B1F")

    Call(0, 5)

    label("loc_B22")

    TalkEnd(0xFE)
    Return()

    # Function_6_A2D end

    def Function_7_B26(): pass

    label("Function_7_B26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BA5")

    #C0026
    ChrTalk(
        0xB,
        (
            "ごめんよ、上演中は\x01",
            "客席まで見てないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        (
            "イリアさんかプリエさんに聞くのが\x01",
            "いいんじゃないかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFB")

    label("loc_BA5")


    #C0028
    ChrTalk(
        0xB,
        "……えっ、男の子？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xB,
        (
            "そんな……上演中は必死だし\x01",
            "客のことまで見てないよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_BFB")

    TalkEnd(0xFE)
    Return()

    # Function_7_B26 end

    def Function_8_BFF(): pass

    label("Function_8_BFF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_CA9")

    #C0030
    ChrTalk(
        0xC,
        (
            "子供ならこの辺りには\x01",
            "来ていないと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xC,
        (
            "舞台装置の操作は\x01",
            "極めて繊細で、神経を使うのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xC,
        (
            "当然上演中は\x01",
            "周囲にも注意していますから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1B")

    label("loc_CA9")


    #C0033
    ChrTalk(
        0xC,
        (
            "本日は休演日ですので、\x01",
            "舞台装置の総点検をしているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xC,
        (
            "こんな時でないと\x01",
            "チェックできませんからねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1B")

    TalkEnd(0xFE)
    Return()

    # Function_8_BFF end

    def Function_9_D1F(): pass

    label("Function_9_D1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE6")

    #C0035
    ChrTalk(
        0xFE,
        "あ、お前は……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#0000Fやあ、元気にしてるか？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "う、う、うるさい。\x01",
            "あっちへ行け。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "オレは今忙しいんだよ！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#0000Fハハ、まだまだ頑なだなぁ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EC0")

    label("loc_DE6")


    #C0040
    ChrTalk(
        0xFE,
        "あ、お前は……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        "#0300Fよう、元気してるかよ？\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "う、う、うるさい。\x01",
            "あっちへ行け。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        "オレは今忙しいんだよ！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0000Fまだまだ頑なだなぁ。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#0204Fロイドさんは\x01",
            "嫌われてますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#0006Fうっ……\x02",
    )

    CloseMessageWindow()

    label("loc_EC0")

    SetScenarioFlags(0x0, 2)
    Jump("loc_F32")

    label("loc_EC8")


    #C0047
    ChrTalk(
        0xFE,
        (
            "まだ仕事を覚えてるとこだし、\x01",
            "分からねえ事ばっかだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "まだまだこれからなんだ。\x01",
            "邪魔すんなよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F32")

    Jump("loc_FB5")

    label("loc_F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F49")
    Call(0, 10)
    Jump("loc_FB5")

    label("loc_F49")


    #C0049
    ChrTalk(
        0xFE,
        (
            "……これから調整があって、\x01",
            "その後また夕方の部だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "こっちは忙しいんだから\x01",
            "図々しく入ってくんなよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB5")

    TalkEnd(0xFE)
    Return()

    # Function_9_D1F end

    def Function_10_FB9(): pass

    label("Function_10_FB9")


    #C0051
    ChrTalk(
        0x101,
        (
            "#0005Fあれ……？\x01",
            "劇団にこんな子、いたっけな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_102C")

    #C0052
    ChrTalk(
        0xFE,
        (
            "……何だお前、\x01",
            "イリアさんの知り合いか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_105B")

    label("loc_102C")


    #C0053
    ChrTalk(
        0xFE,
        (
            "……何だお前ら、\x01",
            "イリアさんの知り合いか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_105B")


    #C0054
    ChrTalk(
        0xFE,
        (
            "フン……\x01",
            "劇団は一般人立ち入り禁止だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "いくら知り合いだからって\x01",
            "図々しく上がってくんなよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 0)
    Return()

    # Function_10_FB9 end

    def Function_11_10C5(): pass

    label("Function_11_10C5")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-250, 1670, 13660, 0)
    MoveCamera(32, 29, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14970, 0)
    SetChrPos(0x101, 260, 120, 13350, 346)
    SetChrPos(0x102, -850, 450, 12100, 346)
    SetChrPos(0x103, -840, 0, 13680, 346)
    SetChrPos(0x104, 300, 450, 12100, 346)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0x8, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_11A4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11A4)
    Sleep(10)

    def lambda_11B4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11B4)
    Sleep(12)

    def lambda_11C4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11C4)
    Sleep(300)

    #C0056
    ChrTalk(
        0x9,
        (
            "#5P#1705Fあれ、弟君たちじゃない。\x01",
            "おヒサ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xA,
        (
            "#11P#1809F皆さんお久し振りです。\x01",
            "……すみません、私たちだけで\x01",
            "話しこんでたみたいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        "#5Pはは、すまない。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#5P稽古の話になると\x01",
            "ついつい熱中してしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#12P#0102F皆さんご無沙汰しています。\x01",
            "新作も大好評みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "#5P#1704Fフフン。\x01",
            "ま、当然だけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        (
            "#11P#1802Fロイドさんは初日に\x01",
            "見にきてくれたんですよね。\x02\x03",

            "#1809Fふふっ、ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#12P#0012Fいやあ……\x01",
            "セシル姉のオマケだから。\x02\x03",

            "#0002Fでも、ステージは本当に凄かった！\x02\x03",

            "イリアさんはもちろんだけど\x01",
            "リーシャも改めて大ファンになったよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        "#11P#1810Fそ、そんな……恥ずかしいです。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(200)

    #C0065
    ChrTalk(
        0x9,
        "#5P#1705Fあらら、お安くないわねぇ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(200)

    #C0066
    ChrTalk(
        0x9,
        (
            "#5P#1709F弟君がナンパしてたって\x01",
            "セシルに言いつけてやろうかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#12P#0011Fいっ……\x01",
            "ナンパじゃないですってば！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    #C0068
    ChrTalk(
        0xA,
        "#11P#1801Fも、もう、イリアさんったら。\x02",
    )

    CloseMessageWindow()

    def lambda_1538():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1538)

    def lambda_1545():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1545)

    def lambda_1552():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1552)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)
    OP_64(0x103)
    OP_64(0x102)

    #C0069
    ChrTalk(
        0x103,
        (
            "#6P#0211Fロイドさんはいいですね。\x02\x03",

            "わたしたちが頂いたチケットは\x01",
            "来週の物なので、\x01",
            "もうしばらくはお預けです。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#12P#0310Fそしてセシルさんと\x01",
            "アルカンシェルデートだと！？\x02\x03",

            "暗い劇場、盛り上がるステージ……\x01",
            "２人でそんな雰囲気を堪能したなんて\x01",
            "羨ましすぎるぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        (
            "#12P#0104F……まあまあ、２人とも。\x02\x03",

            "#0111F確かにセシルさんに続いて\x01",
            "リーシャさんもというのは\x01",
            "節操がないとは思うけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)

    #C0072
    ChrTalk(
        0x101,
        (
            "#11P#0012Fいや何の話だよ！？\x02\x03",

            "#0001F確かに１人だけ舞台を観たのは\x01",
            "抜け駆けだったかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#12P#0111Fじー……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x103,
        "#6P#0211Fじー……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x104,
        "#12P#0301F……弟ブルジョアジーめ！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#11P#0006F（ううっ、やめて欲しい……）\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "#5P#1702Fあはは、弟君も大変ね。\x02\x03",

            "#1709Fそこにあたしも名乗りを上げたら\x01",
            "もっと凄いことになりそうだけど！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)

    #C0078
    ChrTalk(
        0x101,
        "#12P#0006F人の人生で遊ぶのはやめて下さい。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x1F4)
    Sleep(200)

    #C0079
    ChrTalk(
        0xA,
        "#11P#1809Fあ、あははは……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "#5Pまあまあ、\x01",
            "それくらいにしておき給え。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "#5Pイリア君、あまり若者を\x01",
            "からかう物ではないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "#5P#1704Fはいはい分かってますって。\x02\x03",

            "#1700Fで……なに、\x01",
            "今日はあたしたちに会いに来たの？\x02\x03",

            "#1709Fちょうど休演日だし、\x01",
            "一緒にお茶でも飲む？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A0C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A0C)

    def lambda_1A19():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1A19)

    def lambda_1A26():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1A26)

    def lambda_1A33():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1A33)
    Sleep(300)

    #C0083
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあ、いや……\x01",
            "実は仕事で伺ったんですが。\x02\x03",

            "#0001Fほら、例の支援要請の件で。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1200)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(10)

    def lambda_1B0C():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x258, 0x2EE0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1B0C)

    def lambda_1B29():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x258, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B29)
    Sleep(800)

    #C0084
    ChrTalk(
        0x8,
        (
            "#5Pそ、そうだった……\x01",
            "すっかり忘れていたよ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "#11P#1805Fす、すみません。\x01",
            "最初はその話を\x01",
            "３人でしていたんですけど……\x02\x03",

            "#1806Fい、いつの間にか稽古の\x01",
            "打ち合わせになってしまって……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0x9, 0x5A, 0x1F4)

    #C0086
    ChrTalk(
        0x9,
        "#5P#1705Fえ？　え？　何の話？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_1C5E():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1C5E)

    def lambda_1C6B():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C6B)
    Sleep(300)

    #C0087
    ChrTalk(
        0x8,
        (
            "#5Pイリア君～、\x01",
            "しっかりしてくれたまえ！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        (
            "#11P#1801Fほら、昨晩言っていた\x01",
            "例のストーカーの件ですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "#5P#1705Fあー……その話か。\x01",
            "やっぱり相談しちゃったの？\x02\x03",

            "#1706F別に実害はないんだし\x01",
            "放っときゃいいのにー。\x02",
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
    Sleep(1200)

    #C0090
    ChrTalk(
        0x104,
        (
            "#12P#0305Fさ、さすがイリアさんだぜ。\x01",
            "今度はストーカーに\x01",
            "狙われてるってのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        (
            "#12P#0106Fまったく気にしてないんですね……\x01",
            "（女性としては、ちょっと\x01",
            "  信じられないけど……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E70():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E70)

    def lambda_1E7D():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1E7D)

    def lambda_1E8A():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E8A)
    Sleep(300)

    #C0092
    ChrTalk(
        0x8,
        (
            "#5Pす、すまなかった。\x01",
            "ストーカーと言っても\x01",
            "プチ・ストーカーだとかで……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "#11P#1806Fその、私たちも昨晩\x01",
            "イリアさんから聞いたばかりで……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#12P#0003F（２人とも混乱してるみたいだな。）\x02\x03",

            "#0001Fええと……お２人とも\x01",
            "とにかく落ち着いてください。\x02\x03",

            "まずはストーカーの被害状況から\x01",
            "聞いてもいいでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "#11P#1805Fは、はい。\x01",
            "私の方から説明します！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 400)
    Sleep(200)

    #C0096
    ChrTalk(
        0xA,
        "#11P#1801Fいいですよね、イリアさん！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 400)
    Sleep(200)

    #C0097
    ChrTalk(
        0x9,
        (
            "#5P#1703Fま、しゃーないわね。\x01",
            "いいわよリーシャ、話しちゃって。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x9C4)

    #C0098
    ChrTalk(
        0xA,
        "#11P#1801Fはい！\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x190)
    OP_93(0x9, 0xB4, 0x190)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    #C0099
    ChrTalk(
        0xA,
        (
            "#11P#1801Fイリアさんの話では\x01",
            "ここ１～２週間の事らしいんです。\x02\x03",

            "#1803Fイリアさんの自宅の方に\x01",
            "不審な人物──ストーカーが\x01",
            "現れるらしくて。\x02\x03",

            "#1801Fアパートの周りをうろついたり、\x01",
            "ここ数日はアパートの中でも\x01",
            "目撃されているとか！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#12P#0001F自宅の方につきまとい、ですか……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "#5P#1700Fただし、あたしもリーシャも\x01",
            "姿を見た事はないのよね。\x02\x03",

            "#1703Fときどき視線っていうの？\x01",
            "変な気配を感じたりする程度なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        (
            "#6P#0205Fご本人に見つからないとは、\x01",
            "相当勘が鋭い人物のようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x102,
        (
            "#12P#0101Fでも……イリアさんの\x01",
            "ご自宅は非公開ですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "#5Pああ、もちろんだ。\x01",
            "団員の住所は追っかけ対策に\x01",
            "一切公表していない。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#5Pだが……どこからか\x01",
            "突き止めてしまったようでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#12P#0301F目撃情報があるってことは\x01",
            "犯人の人相も判ってるんスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "#11P#1803F見た人の話では、\x01",
            "１４、５歳くらいの\x01",
            "小柄な少年だったとか……\x02\x03",

            "#1801F帽子で顔を隠していて\x01",
            "人相までは判らないそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#12P#0303Fふむ、年若い\x01",
            "ファンってとこかねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#12P#0001Fいや、ファンにしては\x01",
            "明らかに行き過ぎているよ。\x02\x03",

            "それにストーキングは\x01",
            "エスカレートする可能性もあるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "#5Pそうなんだ。\x01",
            "私もその点を心配していてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "#5P君たちを見込んで\x01",
            "早期に何とかしてもらおうと……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0112
    ChrTalk(
        0x9,
        (
            "#5P#1705Fああ、そういえば……\x01",
            "今思い出したんだけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(200)

    #C0113
    ChrTalk(
        0x9,
        (
            "#5P#1705Fリーシャ、昨日\x01",
            "あたしの部屋に入った？\x02\x03",

            "#1700Fなーんか物の位置が\x01",
            "変わってる気がしたんだけど……\x01",
            "リーシャしか鍵持ってないわよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(200)
    TurnDirection(0xA, 0x9, 500)
    TurnDirection(0x8, 0x9, 500)
    Sleep(800)

    #C0114
    ChrTalk(
        0xA,
        "#11P#1805Fイリアさん、それって！！\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "#5Pそ、それは\x01",
            "まずいよイリア君！\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        (
            "#12P#0005Fま、まさか自宅の中まで\x01",
            "侵入してるんですか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        (
            "#12P#0101Fそれが本当なら\x01",
            "予想以上に深刻ね……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_27CA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27CA)
    Sleep(10)

    def lambda_27DA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_27DA)

    def lambda_27E7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_27E7)
    Sleep(200)

    #C0118
    ChrTalk(
        0x8,
        (
            "#5Pこ、こうしてはいられない。\x01",
            "支援課の諸君、\x01",
            "一刻も早く何とかしてくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "#5P#1706F劇団長はいつも大げさよねー。\x01",
            "見られて困る物なんて無いわよ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_288E():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_288E)

    def lambda_289B():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_289B)
    Sleep(300)

    #C0120
    ChrTalk(
        0xA,
        (
            "#11P#1801Fそういう問題じゃないです！\x01",
            "イリアさん……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        "#5Pそうだよイリア君……！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(800)
    OP_93(0x8, 0xB4, 0x190)
    OP_93(0xA, 0xE1, 0x190)
    Sleep(300)

    #C0122
    ChrTalk(
        0x8,
        (
            "#5Pああ……ただし\x01",
            "《銀》の事件の時と同じく\x01",
            "表沙汰にはしたくないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "#5P犯人が熱狂的なファンかも\x01",
            "しれないとなると、なおさらね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "#5Pできれば内々に\x01",
            "ストーキングを諦めさせるか、\x01",
            "……無理な場合は逮捕してもらいたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        "#5Pどうか、頼めないだろうか。\x02",
    )

    CloseMessageWindow()
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【断る】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA5")
    OP_29(0x1D, 0x1, 0x2)
    Call(0, 12)
    Jump("loc_2BDF")

    label("loc_2AA5")


    #C0126
    ChrTalk(
        0x101,
        (
            "#12P#0006Fすみません……まだ\x01",
            "他の仕事が残っていまして。\x01",
            "今は手が離せないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "#5Pそうか……\x01",
            "それなら仕方ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "#5P手が空いたら頼めないだろうか。\x01",
            "何としても\x01",
            "早急に解決して欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    SetChrPos(0x0, -400, 450, 11590, 0)
    SetChrPos(0x8, -1880, 10, 15240, 135)
    SetChrPos(0xA, -210, 0, 13820, 0)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_29(0x1D, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)

    label("loc_2BDF")

    Return()

    # Function_11_10C5 end

    def Function_12_2BE0(): pass

    label("Function_12_2BE0")


    #C0129
    ChrTalk(
        0x101,
        (
            "#12P#0000F判りました、\x01",
            "お引き受けしましょう。\x02\x03",

            "#0003Fこのまま野放しにしておくと\x01",
            "危険かもしれませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "#5Pおお、ありがとう！\x01",
            "どうかよろしく頼むよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#12P#0301Fまあ犯人の行動範囲は\x01",
            "判っているみてえだし……\x02\x03",

            "現場付近に張り込みゃ\x01",
            "何とかなりそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "#5P#1705Fあ、そういう事なら\x01",
            "鍵持って行く？\x02\x03",

            "#1700Fあたしの部屋が使えた方が\x01",
            "何かと都合がいいでしょ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0133
    ChrTalk(
        0x101,
        "#12P#0005Fいいんですか……？\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "#5P#1700F全然オッケーよ。\x01",
            "ちょうど予備の鍵も持ってるし。\x02\x03",

            "ちなみに場所は\x01",
            "西通りにある《ヴィラ・レザン》\x01",
            "ってトコだから。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ED0")

    #C0135
    ChrTalk(
        0x101,
        (
            "#12P#0000Fああ、あの……\x01",
            "西通りじゃ一番の\x01",
            "高級アパルトメントですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "#5P#1702Fそそ、そこの最上階だから。\x02\x03",

            "はい、これ鍵ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F56")

    label("loc_2ED0")


    #C0137
    ChrTalk(
        0x101,
        (
            "#12P#0000Fああ、あの\x01",
            "高級アパルトメントの……\x02\x03",

            "確か最上階でしたっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "#5P#1702Fそそ、よく知ってるわねー。\x02\x03",

            "はい、これ鍵ね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F56")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x347),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x347, 1)

    #C0140
    ChrTalk(
        0x101,
        "#12P#0000Fお預かりします。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "#11P#1803Fすみません、本当は\x01",
            "お手伝いしたい所なんですけど……\x02\x03",

            "#1801F私も顔を覚えられてるみたいで、\x01",
            "ちょっと近づけないんです。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_304D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_304D)
    Sleep(8)

    def lambda_305D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_305D)

    def lambda_306A():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_306A)
    Sleep(5)

    def lambda_307A():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_307A)
    Sleep(300)

    #C0142
    ChrTalk(
        0x101,
        (
            "#12P#0000Fああ、大丈夫だ。\x01",
            "俺たちで捜査してみるからさ。\x02\x03",

            "リーシャはイリアさんと\x01",
            "劇団で待っていてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "#11P#1801Fそれでは、無事捕まえたら\x01",
            "連絡を下さい。\x01",
            "イリアさんと駆けつけますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#12P#0002Fはは、了解。\x01",
            "（リーシャはイリアさんの事になると\x01",
            "  一生懸命だな。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_31A1():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31A1)

    def lambda_31AE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31AE)

    def lambda_31BB():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_31BB)

    def lambda_31C8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_31C8)
    Sleep(400)

    #C0145
    ChrTalk(
        0x101,
        (
            "#5P#0001Fそれじゃあみんな、\x01",
            "早速行ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        "#12P#0101Fええ。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x103,
        "#6P#0200Fはい。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x104,
        (
            "#12P#0304F行き過ぎたファンってやつに\x01",
            "お灸を据えてやるかね！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0149
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【ストーカーの捜査依頼！！】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_29(0x1D, 0x1, 0x1)
    SetScenarioFlags(0x5C, 1)
    NewScene("c020C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2BE0 end

    def Function_13_3303(): pass

    label("Function_13_3303")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_335D")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3331")
    Sleep(400)
    Jump("loc_3343")

    label("loc_3331")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3343")
    Sleep(750)

    label("loc_3343")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("Function_13_3303")

    label("loc_335D")

    Return()

    # Function_13_3303 end

    SaveToFile()

Try(main)
