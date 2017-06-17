from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0310.bin",                # FileName
        "e0310",                    # MapName
        "e0310",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e0310",                  # 0
        "ハロルド",               # 1
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_C0",           # 00, 0
        "Function_1_D0",           # 01, 1
        "Function_2_D1",           # 02, 2
        "Function_3_8A1",          # 03, 3
    ))


    def Function_0_C0(): pass

    label("Function_0_C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_CF")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)

    label("loc_CF")

    Return()

    # Function_0_C0 end

    def Function_1_D0(): pass

    label("Function_1_D0")

    Return()

    # Function_1_D0 end

    def Function_2_D1(): pass

    label("Function_2_D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50101.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch00202.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SoundLoad(460)
    OP_68(210, 1100, -880, 0)
    MoveCamera(320, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11750, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 850, 100, -2000, 180)
    SetChrPos(0x102, 950, 100, 550, 180)
    SetChrPos(0x103, 50, 100, 550, 180)
    SetChrPos(0x104, -850, 100, 550, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -650, 100, -1850, 180)
    Sound(460, 2, 100, 0)
    BeginChrThread(0x101, 3, 0, 3)
    FadeToBright(1000, 0)
    SetCameraDistance(10750, 2000)
    OP_6F(0x10)
    OP_0D()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    #C0001
    ChrTalk(
        0x101,
        (
            "#0000F#12P……すみません。\x01",
            "わざわざ送っていただいて。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "#3609F#5Pはは、いいんですよ。\x01",
            "ついでに送るだけですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x104,
        (
            "#0302F#11Pしかし自分の車を持ってるって\x01",
            "相当スゴイよなぁ。\x02\x03",

            "まだまだバカ高いんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x103,
        (
            "#0203F#11Pこのクラスの自家用車なら\x01",
            "たしか８０万ミラくらいかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        "#0005F#12P８０万ミラ……そりゃ凄いな。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#3604F#5P一応、貿易商としての\x01",
            "仕事の道具でもありますから。\x02\x03",

            "#3600Fバスを使ってもいいんですけど\x01",
            "どうしても時間の融通が\x01",
            "利かないことが多くて……\x02\x03",

            "去年、思い切って\x01",
            "購入してしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        (
            "#0104F#11Pふふ、それ以外にも\x01",
            "理由がありそうですね？\x02\x03",

            "#0102F待っている奥様と息子さんに\x01",
            "一刻でも早く会いたいとか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0008
    ChrTalk(
        0x8,
        "#3609F#5Pはは……参ったな。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#0302F#11Pなるほど、お土産も\x01",
            "マメに用意してるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#0202F#11P……所謂#4Rいわゆる#マイホームパパと\x01",
            "いうわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#3604F#5Pいやあ……とんでもない。\x02\x03",

            "#3600Fどうしても出張が多くて\x01",
            "妻と息子には寂しい想いを\x01",
            "させてしまうことが多くて……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#0000F#12P息子さんはお幾つなんですか？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#3609F#5P今年で５歳になります。\x02\x03",

            "まだ日曜学校に入る前ですけど\x01",
            "もう好奇心旺盛で……\x02\x03",

            "#3600F色んなものに興味を示しては\x01",
            "妻の手を焼かせていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#0002F#12Pへえ……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        "#0102F#11Pふふ、お幸せそうですね。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#3609F#5Pはは……それはもう。\x02\x03",

            "#3608F#30Wそれに私は──私たちは\x01",
            "幸せでなくてはなりませんから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1500)

    #C0017
    ChrTalk(
        0x101,
        "#0005F#12Pえ……？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#3605F#5Pあ、いや……\x01",
            "すみません、こちらの事です。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0019
    ChrTalk(
        0x8,
        (
            "#3600F#5Pおっと……古道を抜けますね。\x02\x03",

            "右に曲がりますから、\x01",
            "皆さん、どうかお気をつけて。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    OP_25(0x1CC, 0x5A)
    Sleep(80)
    OP_25(0x1CC, 0x50)
    Sleep(80)
    OP_25(0x1CC, 0x46)
    Sleep(80)
    OP_25(0x1CC, 0x3C)
    Sleep(80)
    OP_25(0x1CC, 0x32)
    Sleep(80)
    OP_25(0x1CC, 0x28)
    Sleep(80)
    OP_25(0x1CC, 0x1E)
    Sleep(80)
    OP_25(0x1CC, 0x14)
    Sleep(80)
    OP_25(0x1CC, 0xA)
    Sleep(80)
    OP_25(0x1CC, 0x0)
    OP_24(0x1CC)
    SetScenarioFlags(0x5C, 0)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_D1 end

    def Function_3_8A1(): pass

    label("Function_3_8A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8C5")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_3_8A1")

    label("loc_8C5")

    Return()

    # Function_3_8A1 end

    SaveToFile()

Try(main)
