from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0304.bin",                # FileName
        "m0304",                    # MapName
        "m0304",                    # Location
        0x0000,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "m0304",                  # 0
        "レインズ",               # 1
        "SE制御",                 # 2
    ))

    AddCharChip((
        "chr/ch28100.itc",                   # 00
    ))

    DeclNpc(0,       0,       1629,    0,    261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(232, 0)                                        # 0

    ScpFunction((
        "Function_0_E8",           # 00, 0
        "Function_1_198",          # 01, 1
        "Function_2_1A8",          # 02, 2
        "Function_3_1A9",          # 03, 3
        "Function_4_241",          # 04, 4
        "Function_5_1EE0",         # 05, 5
    ))


    def Function_0_E8(): pass

    label("Function_0_E8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_120"),
        (1, "loc_12C"),
        (2, "loc_138"),
        (3, "loc_144"),
        (4, "loc_150"),
        (5, "loc_15C"),
        (6, "loc_168"),
        (SWITCH_DEFAULT, "loc_174"),
    )


    label("loc_120")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_12C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_138")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_144")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_150")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_15C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_168")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_174")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_180")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_197")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_197")

    Return()

    # Function_0_E8 end

    def Function_1_198(): pass

    label("Function_1_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1A7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)

    label("loc_1A7")

    Return()

    # Function_1_198 end

    def Function_2_1A8(): pass

    label("Function_2_1A8")

    Return()

    # Function_2_1A8 end

    def Function_3_1A9(): pass

    label("Function_3_1A9")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "またいずれ、皆さんとは\x01",
            "Ｒ＆Ａリサーチの人間として\x01",
            "会う機会もあるかと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "まあ、まずはとにかく、\x01",
            "突入作戦の成功を祈っていますよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_1A9 end

    def Function_4_241(): pass

    label("Function_4_241")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    BeginChrThread(0x9, 1, 0, 5)
    OP_68(1090, 0, -8490, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19760, 0)
    SetChrPos(0x101, 0, 0, -10650, 0)
    SetChrPos(0x102, 1100, 0, -10650, 0)
    SetChrPos(0x103, -1100, 0, -10650, 0)
    SetChrPos(0x104, 0, 0, -10650, 0)
    SetChrPos(0xF4, -1100, 0, -10650, 0)
    SetChrPos(0xF5, 1100, 0, -10650, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)

    #A0003
    AnonymousTalk(
        0x101,
        (
            "#00001Fやはり、ジオフロントに\x01",
            "通じていたんだな……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0004
    AnonymousTalk(
        0x102,
        (
            "#00103Fどうやら、Ｄ区画の一角には\x01",
            "間違いないみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0005
    AnonymousTalk(
        0x103,
        (
            "#00205F……気配が強くなって来ました。\x02\x03",

            "#00203F数は１つですが……\x01",
            "誰かがいるのは確実みたいです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_462")

    #A0006
    AnonymousTalk(
        0x10A,
        "#00601F（この扉の奥か……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DB")

    label("loc_462")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A3")

    #A0007
    AnonymousTalk(
        0x109,
        "#10101F（この扉の向こうですね……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DB")

    label("loc_4A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DB")

    #A0008
    AnonymousTalk(
        0x106,
        "#10701F（この扉の奥ですね……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4DB")


    #A0009
    AnonymousTalk(
        0x103,
        "#00201F（ええ、間違いありません。）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56B")

    #A0010
    AnonymousTalk(
        0x105,
        (
            "#10400F（ここは、倉庫か何かかな？\x01",
            "  扉に窓が付いているみたいだけど。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_636")

    label("loc_56B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D3")

    #A0011
    AnonymousTalk(
        0x106,
        (
            "#10705F（ここは、倉庫か何かでしょうか？\x01",
            "  扉に窓が付いているようですが。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_636")

    label("loc_5D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_636")

    #A0012
    AnonymousTalk(
        0x109,
        (
            "#10105F（ここは、倉庫か何かですかね？\x01",
            "  扉に窓が付いているようですけど。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_636")


    #A0013
    AnonymousTalk(
        0x101,
        (
            "#00003F（分からないけど……\x01",
            "  とりあえず好都合だな。）\x02\x03",

            "#00000F（ここから少し、\x01",
            "  中の様子を窺ってみよう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x9, 0x1)
    OP_68(950, 0, 3180, 0)
    MoveCamera(42, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16090, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(10)
    PlayBGM("ed7302", 0)

    #N0014
    NpcTalk(
        0x8,
        "？？？",
        (
            "そうです、大佐……\x01",
            "はい、はい……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0015
    NpcTalk(
        0x8,
        "？？？",
        (
            "え、そう言いましたっけ？\x01",
            "あはは……すみません、所長。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#00005F#N（あの後ろ姿は……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0017
    ChrTalk(
        0x102,
        (
            "#00105F#N（もしかして……\x01",
            "  クロスベルタイムズの\x01",
            "  レインズさん？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0018
    ChrTalk(
        0x103,
        "#00205F#N（こんな所で一体何を……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x8, 0x0, 500)
    Sleep(300)

    #C0019
    ChrTalk(
        0x8,
        (
            "#5Pあの……そこにいるのは\x01",
            "支援課の皆さんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#5Pもしよければ、\x01",
            "軽くお話をして行きませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        (
            "#00306F#Nやれやれ……\x01",
            "既に気付いてたってわけか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00001F#N油断はできないけど、\x01",
            "とりあえず言う通りにするか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(980, 900, -2510, 4500)
    MoveCamera(39, 16, 0, 4500)
    OP_6E(600, 4500)
    SetCameraDistance(18630, 4500)
    Sleep(2000)

    def lambda_939():
        OP_97(0xFE, 0x0, 0x0, 0x10CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_939)

    def lambda_953():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_953)
    Sleep(100)

    def lambda_967():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_967)

    def lambda_981():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_981)
    Sleep(100)

    def lambda_995():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_995)

    def lambda_9AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9AF)
    Sleep(500)

    def lambda_9C3():
        OP_97(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9C3)

    def lambda_9DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9DD)
    Sleep(100)

    def lambda_9F1():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_9F1)

    def lambda_A0B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_A0B)
    Sleep(100)

    def lambda_A1F():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A1F)

    def lambda_A39():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_A39)
    WaitChrThread(0xF5, 1)

    #C0023
    ChrTalk(
        0x8,
        "#5Pはは、やっぱり皆さんだ。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#5Pでもまさか、\x01",
            "こんな所でお会いするとは\x01",
            "思いもよりませんでした。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(590, 400, 910, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16820, 3000)

    def lambda_AE4():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE4)
    Sleep(50)

    def lambda_B01():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B01)
    Sleep(50)

    def lambda_B1E():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B1E)
    Sleep(50)

    def lambda_B3B():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B3B)
    Sleep(50)

    def lambda_B58():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B58)
    Sleep(50)

    def lambda_B75():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B75)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)

    #C0025
    ChrTalk(
        0x101,
        "#12P#00001Fええ、それは俺たちもです。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#12P#00103Fクロスベルタイムズの\x01",
            "新人記者で、カメラマンで、\x01",
            "グレイスさんのパートナー……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#12P#00303Fま、こんな所で会う以上、\x01",
            "それだけじゃねえのは確かだな。\x02\x03",

            "#00301Fとりあえず、猫被ってないで\x01",
            "さっさと正体を吐いたらどうだ？\x02\x03",

            "俺たちに気付いていながら\x01",
            "隠れなかったってことは、\x01",
            "アンタもそのつもりだったんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#5Pええ、といっても性格は\x01",
            "これが素なんですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#5P実は僕は――\x01",
            "民間の調査会社の人間なんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0030
    ChrTalk(
        0x101,
        "#12P#00005F民間の調査会社……？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#5Pええ、リベールにある\x01",
            "『Ｒ＆Ａリサーチ』という\x01",
            "名前の会社でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#12P#00105F『Ｒ＆Ａリサーチ』……\x01",
            "聞いたことがあるような気は\x01",
            "しますけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E7B")

    #C0033
    ChrTalk(
        0x10A,
        "#12P#00603Fふむ、名前くらいは把握しているが……\x02",
    )

    CloseMessageWindow()

    label("loc_E7B")


    #C0034
    ChrTalk(
        0x8,
        (
            "#5Pまあ、最近出来たばかりの\x01",
            "小さい会社ですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#5Pリシャール所長はそれなりに\x01",
            "有名だとは思いますけど。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1070")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0036
    ChrTalk(
        0x102,
        (
            "#12P#00105Fそれってもしかして……\x01",
            "王国軍に所属されていた、\x01",
            "リシャール元大佐のことですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x10A,
        "#12P#00600Fなるほど……確かに合点は行くか。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#5P#00005Fエリィにダドリーさん……\x01",
            "ご存知なんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x10A,
        (
            "#12P#00603Fああ、アラン・リシャール――\x02\x03",

            "#00600F……２年前、リベールで\x01",
            "クーデター事件を引き起こした\x01",
            "元・情報将校だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1186")

    label("loc_1070")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0040
    ChrTalk(
        0x102,
        (
            "#12P#00105Fそれってもしかして……\x01",
            "王国軍に所属されていた、\x01",
            "リシャール元大佐のことですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#5P#00005Fエリィ、知っているのか？\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#12P#00103Fええ、アラン・リシャール――\x02\x03",

            "#00101F……２年前、リベールで\x01",
            "クーデター事件を引き起こした\x01",
            "元・情報将校よ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1186")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x101,
        "#5P#00005Fあのクーデター事件を……？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#12P#00103Fそう、だけど\x01",
            "リベールの異変時には\x01",
            "国難を救う大活躍を見せて……\x02\x03",

            "#00100Fその後、女王陛下から正式に\x01",
            "恩赦をもらったという話なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#5P#00005F恩赦を……\x02\x03",

            "#00003Fなるほど、それで\x01",
            "自身の経歴を活かしつつ\x01",
            "調査会社を立ち上げたわけか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_130C")

    #C0046
    ChrTalk(
        0x106,
        (
            "#12P#10703Fなんというか……\x01",
            "相当な切れ者のようですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AB")

    label("loc_130C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_135D")

    #C0047
    ChrTalk(
        0x105,
        (
            "#12P#10402Fフフ、どうやら\x01",
            "かなり優秀な人物みたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AB")

    label("loc_135D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13AB")

    #C0048
    ChrTalk(
        0x109,
        (
            "#12P#10106Fなんていうか……\x01",
            "相当、優秀な人みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AB")


    #C0049
    ChrTalk(
        0x8,
        (
            "#5Pふむ、流石は支援課の皆さん。\x01",
            "こういった話題にもお詳しいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "#5P――そういうことで僕の立場を\x01",
            "少しは分かって頂けたでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#12P#00003Fええ、大体のところは。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        (
            "#12P#00101Fですが、どうしてまた\x01",
            "私たちに身分を明かす気に？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#5Pええ、いずれ皆さんとも\x01",
            "お仕事をさせて頂く機会が\x01",
            "あるかと思いましたので。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#5Pそうなれば、今明かすのも\x01",
            "後で明かすのも同じですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#5Pちなみに通信社のみんなには\x01",
            "グレイスさんを始め、\x01",
            "誰にも話していないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "#5P図々しいお願いですが、\x01",
            "内密にしておいて頂けますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#12P#00000Fええ、話を聞く限り\x01",
            "あなたたちはあくまで\x01",
            "第三者でしょうし。\x02\x03",

            "敢えて秘密を洩らしたりする\x01",
            "つもりはありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#5Pありがとうございます。\x01",
            "そう言って頂けると思いました。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        (
            "#12P#00203Fそういえば、モヤの影響で\x01",
            "導力通信がつながりにくいと\x01",
            "聞いていたのですが……\x02\x03",

            "#00205Fそちらの通信器は、\x01",
            "問題なく使えるんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        "#5Pああ、これのことですか。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "#5Pモヤの影響は勿論ありますが、\x01",
            "この通信器は単純に強力な\x01",
            "導力波を出すことが可能なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#5Pただそれでも、範囲はギリギリ\x01",
            "クロスベルを越える程度でしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#5Pちなみに今は所長自らが\x01",
            "アルタイル市に出張って来ていて\x01",
            "通信を中継してもらっているんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1883")

    #C0064
    ChrTalk(
        0x10A,
        (
            "#12P#00603Fなるほど……\x01",
            "この状況下で大した連携だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_1883")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18D2")

    #C0065
    ChrTalk(
        0x105,
        (
            "#12P#10404Fなるほど……\x01",
            "この状況下で大した連携だね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_18D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_191E")

    #C0066
    ChrTalk(
        0x109,
        (
            "#12P#10105Fなるほど……\x01",
            "この状況下で見事な連携ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_191E")


    #C0067
    ChrTalk(
        0x104,
        (
            "#12P#00303Fその通信器……\x01",
            "見た所、暗号化通信まで\x01",
            "使えるタイプのようだな。\x02\x03",

            "#00302Fなかなかどうして、\x01",
            "軍も顔負けなんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "#5Pはは、軍も顔負けというのは\x01",
            "流石に過大評価ですが……\x01",
            "よくご存知ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "#5Pまあとりあえず、国防軍に通信を\x01",
            "解析されるわけにもいきませんからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "#5Pそうそう、ちなみにこの通信器は\x01",
            "高性能なだけあって、その分\x01",
            "ミラも相当かかっていましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "#5P副所長からどんなことがあっても\x01",
            "壊すなと釘を刺されているので、\x01",
            "持ち運びには相当気を遣うんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "#5Pなので僕がここにいることは\x01",
            "他の方にはくれぐれも\x01",
            "秘密にしておいて下さいね。\x02",
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
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C34")

    #C0073
    ChrTalk(
        0x106,
        "#12P#10703F……いかにも民間らしい発言ですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_1C34")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C85")

    #C0074
    ChrTalk(
        0x109,
        (
            "#12P#10103F何ていうか……\x01",
            "すごく民間らしい発言ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_1C85")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CC8")

    #C0075
    ChrTalk(
        0x105,
        "#12P#10404Fフフ、いかにも民間らしい発言だね。\x02",
    )

    CloseMessageWindow()

    label("loc_1CC8")


    #C0076
    ChrTalk(
        0x8,
        (
            "#5Pはは、そうなんです。\x01",
            "ほんと苦労も絶えませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "#5P……それはともかく、\x01",
            "随分と話し込んでしまいましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "#5P僕は引き続き、\x01",
            "この場所で外の人間と\x01",
            "連絡を取る予定ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "#5P皆さんもオルキスタワーに\x01",
            "突入される際は、\x01",
            "くれぐれも気を付けて下さいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#12P#00006Fええ――ってその話は\x01",
            "していなかったと思いますが。\x02\x03",

            "#00000Fまあとにかく、時間もないので\x01",
            "俺たちはこの辺で失礼します。\x02\x03",

            "#00001Fレインズさんもここでの活動には\x01",
            "十分気を付けてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        "#5Pええ、もちろんですよ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x23, 1)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_241 end

    def Function_5_1EE0(): pass

    label("Function_5_1EE0")

    Sound(32, 0, 30, 0)
    Sleep(700)
    Sound(33, 0, 20, 0)
    Sleep(700)
    Sound(32, 0, 40, 0)
    Sleep(700)
    Sound(33, 0, 30, 0)
    Sleep(700)

    label("loc_1F04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F26")
    Sound(32, 0, 50, 0)
    Sleep(700)
    Sound(33, 0, 40, 0)
    Sleep(700)
    Jump("loc_1F04")

    label("loc_1F26")

    Return()

    # Function_5_1EE0 end

    SaveToFile()

Try(main)
