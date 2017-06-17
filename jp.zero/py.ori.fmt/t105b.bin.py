from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t105b.bin",                # FileName
        "t105b",                    # MapName
        "t105b",                    # Location
        0x0043,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 67, 0, 4, 0, 5],
    )

    BuildStringList((
        "t105b",                  # 0
        "ハガー支配人",           # 1
        "ロッチー",               # 2
        "シトラス",               # 3
        "観光客",                 # 4
        "観光客",                 # 5
        "観光客",                 # 6
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25600.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch32300.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch20202.itc",                   # 06
        "chr/ch20302.itc",                   # 07
    ))

    DeclNpc(-479,    0,       10050,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-93959,  0,       8260,    270,  257,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(94190,   0,       11579,   90,   257,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-99480,  0,       -80559,  90,   257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(97559,   150,     -84309,  90,   341,  0x0, 0,   6,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(100540,  150,     -84309,  270,  341,  0x0, 0,   7,   0,   255, 255, 0,   13,  255,  0)

    DeclActor(-20,     0,       8270,    1500,    -480,    1500,    10050,   0x007E, 0,  7,  0x0000)
    DeclActor(5500,    0,       13500,   1200,    5500,    1500,    13500,   0x007C, 0,  15, 0x0000)
    DeclActor(-96600,  0,       120560,  1500,    -96600,  1000,    120560,  0x007C, 0,  6,  0x0000)

    ScpFunction((
        "Function_0_208",          # 00, 0
        "Function_1_2C0",          # 01, 1
        "Function_2_321",          # 02, 2
        "Function_3_382",          # 03, 3
        "Function_4_3AD",          # 04, 4
        "Function_5_3CF",          # 05, 5
        "Function_6_3D0",          # 06, 6
        "Function_7_475",          # 07, 7
        "Function_8_479",          # 08, 8
        "Function_9_513",          # 09, 9
        "Function_10_57C",         # 0A, 10
        "Function_11_5F0",         # 0B, 11
        "Function_12_65E",         # 0C, 12
        "Function_13_67F",         # 0D, 13
        "Function_14_69A",         # 0E, 14
        "Function_15_1362",        # 0F, 15
    ))


    def Function_0_208(): pass

    label("Function_0_208")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_248"),
        (1, "loc_254"),
        (2, "loc_260"),
        (3, "loc_26C"),
        (4, "loc_278"),
        (5, "loc_284"),
        (6, "loc_290"),
        (SWITCH_DEFAULT, "loc_29C"),
    )


    label("loc_248")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_254")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_260")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_26C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_278")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_284")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_290")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_29C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_2A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_2BF")

    Return()

    # Function_0_208 end

    def Function_1_2C0(): pass

    label("Function_1_2C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_320")
    OP_95(0xFE, -106030, 0, 8260, 2000, 0x0)
    OP_95(0xFE, -106030, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 8260, 2000, 0x0)
    Jump("Function_1_2C0")

    label("loc_320")

    Return()

    # Function_1_2C0 end

    def Function_2_321(): pass

    label("Function_2_321")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_381")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_2_321")

    label("loc_381")

    Return()

    # Function_2_321 end

    def Function_3_382(): pass

    label("Function_3_382")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AC")
    OP_94(0xFE, 0xFFFE730C, 0xFFFEC082, 0xFFFE8086, 0xFFFECBC2, 0x3E8)
    Sleep(400)
    Jump("Function_3_382")

    label("loc_3AC")

    Return()

    # Function_3_382 end

    def Function_4_3AD(): pass

    label("Function_4_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_3BC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 14)

    label("loc_3BC")

    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 3)
    Return()

    # Function_4_3AD end

    def Function_5_3CF(): pass

    label("Function_5_3CF")

    Return()

    # Function_5_3CF end

    def Function_6_3D0(): pass

    label("Function_6_3D0")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_457")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_457")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_473")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_473")

    Return()

    # Function_6_3D0 end

    def Function_7_475(): pass

    label("Function_7_475")

    Call(0, 8)
    Return()

    # Function_7_475 end

    def Function_8_479(): pass

    label("Function_8_479")

    TalkBegin(0x8)

    #C0001
    ChrTalk(
        0x8,
        (
            "ワジ様のお連れの皆様……\x01",
            "お出かけでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "ディナーでしたら、アーケード内にある\x01",
            "レストラン《フォルトゥナ》が\x01",
            "おすすめでございますよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_8_479 end

    def Function_9_513(): pass

    label("Function_9_513")

    TalkBegin(0xFE)

    #C0003
    ChrTalk(
        0xFE,
        (
            "あ～ん、ワジ様がどこかへ\x01",
            "出かけちゃった……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "もっとあの綺麗なお顔を\x01",
            "拝見したかったのに㈱\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_513 end

    def Function_10_57C(): pass

    label("Function_10_57C")

    TalkBegin(0xFE)

    #C0005
    ChrTalk(
        0xFE,
        (
            "ルームサービスの\x01",
            "お申し付けでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "少々お待ちいただければ\x01",
            "ワインや軽食などを\x01",
            "お持ちしますわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_57C end

    def Function_11_5F0(): pass

    label("Function_11_5F0")

    TalkBegin(0xFE)

    #C0007
    ChrTalk(
        0xFE,
        (
            "ふぅ～……\x01",
            "部屋が取れてよかったぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "いやぁ、辛抱強く\x01",
            "キャンセル待ちしてた\x01",
            "甲斐があったよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_5F0 end

    def Function_12_65E(): pass

    label("Function_12_65E")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        "記念祭の夜に、乾杯。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_65E end

    def Function_13_67F(): pass

    label("Function_13_67F")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        "うふふ、乾杯。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_67F end

    def Function_14_69A(): pass

    label("Function_14_69A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_709")
    SetChrPos(0x101, -97500, 0, 124700, 0)
    SetChrPos(0x102, -96400, 0, 124700, 0)
    SetChrPos(0x103, -96400, 0, 123500, 0)
    SetChrPos(0x104, -97500, 0, 123500, 0)
    SetChrPos(0x151, -98000, 0, 121100, 0)
    Jump("loc_7CA")

    label("loc_709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_76C")
    SetChrPos(0x101, -97500, 0, 124700, 0)
    SetChrPos(0x102, -96400, 0, 123500, 0)
    SetChrPos(0x103, -96400, 0, 124700, 0)
    SetChrPos(0x104, -97500, 0, 123500, 0)
    SetChrPos(0x151, -98000, 0, 121100, 0)
    Jump("loc_7CA")

    label("loc_76C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_7CA")
    SetChrPos(0x101, -97500, 0, 124700, 0)
    SetChrPos(0x102, -97500, 0, 123500, 0)
    SetChrPos(0x103, -96400, 0, 123500, 0)
    SetChrPos(0x104, -96400, 0, 124700, 0)
    SetChrPos(0x151, -98000, 0, 121100, 0)

    label("loc_7CA")

    OP_68(-97030, 900, 124240, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19350, 0)
    FadeToBright(2000, 0)
    SetCameraDistance(18350, 3000)
    OP_6F(0x10)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_913")

    #C0011
    ChrTalk(
        0x103,
        "#0202F#6P……綺麗ですね……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#5302F#6Pふふ、そうね……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#5006F#6Pしかし夜には\x01",
            "花火まで上げるなんてなぁ。\x02\x03",

            "#5000F記念祭だけの演出なのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        (
            "#0300F#6Pいや、毎日ある演出らしいぜ？\x02\x03",

            "テーマパークの夜の部も\x01",
            "これからが本番ってところだろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1A")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_A19")

    #C0015
    ChrTalk(
        0x103,
        "#5402F#6P……綺麗ですね……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        "#0102F#6Pふふ、そうね……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#5006F#6Pしかし夜には\x01",
            "花火まで上げるなんてなぁ。\x02\x03",

            "#5000F記念祭だけの演出なのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        (
            "#0300F#6Pいや、毎日ある演出らしいぜ？\x02\x03",

            "テーマパークの夜の部も\x01",
            "これからが本番ってところだろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1A")

    label("loc_A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_B1A")

    #C0019
    ChrTalk(
        0x103,
        "#0202F#6P……綺麗ですね……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        "#0102F#6Pふふ、そうね……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#5006F#6Pしかし夜には\x01",
            "花火まで上げるなんてなぁ。\x02\x03",

            "#5000F記念祭だけの演出なのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#5600F#6Pいや、毎日ある演出らしいぜ？\x02\x03",

            "テーマパークの夜の部も\x01",
            "これからが本番ってところだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1A")


    #C0023
    ChrTalk(
        0x151,
        (
            "#5704F#6Pナイトパレードに\x01",
            "ライトアップされた観覧車……\x02\x03",

            "フフ、女の子を口説くには\x01",
            "絶好のシチュエーションだろうね。\x02\x03",

            "#5700F──さてと。\x01",
            "僕は一足先に行こうかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-97750, 900, 123480, 2000)

    def lambda_C28():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C28)
    Sleep(50)

    def lambda_C38():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C38)
    Sleep(50)

    def lambda_C48():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C48)
    Sleep(50)

    def lambda_C58():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C58)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0024
    ChrTalk(
        0x101,
        (
            "#5000F#11Pそうか……どこかのご婦人と\x01",
            "待ち合わせしてるんだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x151,
        "#5702F#6Pフフ、まあね。\x02",
    )

    CloseMessageWindow()
    OP_93(0x151, 0xB4, 0x190)
    Sleep(300)

    #C0026
    ChrTalk(
        0x151,
        (
            "#5704F#11Pそれでは女神#4Rエイドス#の幸運を。\x02\x03",

            "#5702F君たちがヘマをしなければ\x01",
            "オークション会場で会おう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(1424, 255, 90, 0)    #voice#Lazy
    Sleep(500)
    OP_68(-99750, 900, 120550, 3500)
    OP_95(0x151, -100000, 0, 116800, 2000, 0x1)

    def lambda_D83():
        OP_95(0xFE, -100000, 0, 114300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_D83)
    Sleep(300)

    def lambda_DA0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_DA0)
    Sound(121, 0, 100, 0)
    WaitChrThread(0x151, 1)
    WaitChrThread(0x151, 2)
    Sound(890, 0, 100, 0)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-97040, 900, 124460, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17300, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_F03")

    #C0027
    ChrTalk(
        0x104,
        (
            "#0306F#11Pやれやれ……\x01",
            "人を喰ったヤツだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#0206F#12P不良集団のヘッドにして\x01",
            "上流階級ご用達のホスト……\x02\x03",

            "#0211F色々と妖しい人ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#5304F#11Pでも正直、競売会の情報を\x01",
            "教えてくれたのは助かったわ。\x02\x03",

            "#5300F借りを作ってしまったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_110C")

    label("loc_F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_100A")

    #C0030
    ChrTalk(
        0x104,
        (
            "#0306F#11Pやれやれ……\x01",
            "人を喰ったヤツだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        (
            "#5406F#11P不良集団のヘッドにして\x01",
            "上流階級ご用達のホスト……\x02\x03",

            "#5411F色々と妖しい人ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#0104F#12Pでも正直、競売会の情報を\x01",
            "教えてくれたのは助かったわ。\x02\x03",

            "#0100F借りを作ってしまったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_110C")

    label("loc_100A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_110C")

    #C0033
    ChrTalk(
        0x104,
        (
            "#5606F#11Pやれやれ……\x01",
            "人を喰ったヤツだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#0206F#12P不良集団のヘッドにして\x01",
            "上流階級ご用達のホスト……\x02\x03",

            "#0211F色々と妖しい人ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#0104F#11Pでも正直、競売会の情報を\x01",
            "教えてくれたのは助かったわ。\x02\x03",

            "#0100F借りを作ってしまったわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_110C")


    #C0036
    ChrTalk(
        0x101,
        "#5000F#11Pああ……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_93(0x101, 0x87, 0x190)
    Sleep(300)

    #C0037
    ChrTalk(
        0x101,
        (
            "#5003F#5P──俺たちもそろそろ\x01",
            "オークション会場に向かおう。\x02\x03",

            "#5001F何とか入口のチェックを抜けて\x01",
            "会場の中に入り込まないとな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11C4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11C4)
    Sleep(50)

    def lambda_11D4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11D4)
    Sleep(50)

    def lambda_11E4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11E4)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_121D")

    #C0038
    ChrTalk(
        0x102,
        "#5301F#12Pええ……そうね！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1266")

    label("loc_121D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1245")

    #C0039
    ChrTalk(
        0x103,
        "#5401F#12Pはい……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1266")

    label("loc_1245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1266")

    #C0040
    ChrTalk(
        0x104,
        "#5601F#12Pおうよ！\x02",
    )

    CloseMessageWindow()

    label("loc_1266")

    SetCameraDistance(17600, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_12BB")
    AddParty(0x1, 0xEF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_12EA")

    label("loc_12BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_12D5")
    AddParty(0x2, 0xEF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_12EA")

    label("loc_12D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_12EA")
    AddParty(0x3, 0xEF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_12EA")

    SetChrPos(0x0, -99730, 0, 120850, 180)
    SetScenarioFlags(0xA4, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_131C")
    OP_29(0x24, 0x4, 0x40)
    Jump("loc_132E")

    label("loc_131C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132E")
    OP_29(0x24, 0x4, 0x40)

    label("loc_132E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_133F")
    OP_DE(0x2A, 0x0)
    Jump("loc_135C")

    label("loc_133F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1350")
    OP_DE(0x2B, 0x0)
    Jump("loc_135C")

    label("loc_1350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_135C")
    OP_DE(0x2C, 0x0)

    label("loc_135C")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_69A end

    def Function_15_1362(): pass

    label("Function_15_1362")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "        ～階段室～\x01",
            "現在、３階のＶＩＰフロアは\x01",
            "貸し切りとなっております。\x01",
            "立ち入りはご遠慮下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_1362 end

    SaveToFile()

Try(main)
