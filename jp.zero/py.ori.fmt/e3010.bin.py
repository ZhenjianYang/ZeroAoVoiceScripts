from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3010.bin",                # FileName
        "e3010",                    # MapName
        "e3010",                    # Location
        0x0000,                     # MapIndex
        "ed7515",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3010",                  # 0
        "セルゲイ課長",           # 1
        "ツァイト",               # 2
        "ボート",                 # 3
        "SE制御",                 # 4
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_128",          # 00, 0
        "Function_1_138",          # 01, 1
        "Function_2_14E",          # 02, 2
        "Function_3_DDE",          # 03, 3
        "Function_4_E08",          # 04, 4
        "Function_5_E39",          # 05, 5
        "Function_6_E53",          # 06, 6
        "Function_7_E9F",          # 07, 7
        "Function_8_EDE",          # 08, 8
    ))


    def Function_0_128(): pass

    label("Function_0_128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_137")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)

    label("loc_137")

    Return()

    # Function_0_128 end

    def Function_1_138(): pass

    label("Function_1_138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 0)), scpexpr(EXPR_END)), "loc_14D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x5F, 0)

    label("loc_14D")

    Return()

    # Function_1_138 end

    def Function_2_14E(): pass

    label("Function_2_14E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    LoadChrToIndex("apl/ch50542.itc", 0x1F)
    SoundLoad(483)
    SoundLoad(126)
    SetChrChipPat(0x0, 0x1, 0x0)
    LoadChrChipPat()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis157.itp")
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 3, 0, 3)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 0, 300, -1500, 180)
    SetChrPos(0x133, 0, 900, 3300, 0)
    SetChrPos(0x9, -750, 900, 3300, 0)
    SetChrPos(0x101, 0, 900, 300, 0)
    SetChrPos(0x102, -900, 900, 1000, 90)
    SetChrPos(0x103, 900, 900, 1000, 270)
    SetChrPos(0x104, -900, 900, 2100, 90)
    SetChrPos(0x105, 900, 900, 2100, 270)
    BeginChrThread(0xB, 0, 0, 7)
    FadeToBright(1000, 0)
    BeginChrThread(0xB, 1, 0, 4)
    OP_68(690, 9850, 800, 0)
    MoveCamera(250, 6, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(46340, 0)
    OP_68(690, 3850, 800, 5000)
    OP_6F(0x1)
    Sleep(1000)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xB, 0x1)
    OP_0D()
    Fade(1000)
    BeginChrThread(0xB, 1, 0, 5)
    OP_68(160, 1750, 1530, 0)
    MoveCamera(219, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15070, 0)
    OP_0D()
    Sleep(500)
    EndChrThread(0xB, 0x1)

    #C0001
    ChrTalk(
        0x8,
        (
            "#1003F#5P……なるほどな。\x02\x03",

            "#1001Fま、俺の忠告を\x01",
            "完璧に無視しやがったことは\x01",
            "いったん置いておくとして……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0002
    ChrTalk(
        0x101,
        "#0008F#11Pす、済みません……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#1000F#5P問題はその子だな。\x02\x03",

            "#1003F事と次第によっては\x01",
            "とんでもない事になるかもしれん。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_411():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_411)

    def lambda_41E():
        TurnDirection(0xFE, 0x133, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_41E)
    Sleep(100)

    def lambda_42E():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_42E)

    def lambda_43B():
        TurnDirection(0xFE, 0x133, 300)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43B)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)

    #C0004
    ChrTalk(
        0x104,
        (
            "#0303F#11Pだな……\x02\x03",

            "#0301Fオークションで人形の代わりに\x01",
            "出品される所だった子供……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x105,
        (
            "#0406F#5Pま、よくない想像ばかり\x01",
            "働いてしまいそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        "#0208F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        (
            "#0106F#5P……まさかマフィアも\x01",
            "そこまで愚かなことを\x01",
            "しないとは思うけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x133, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x133, 0xB4, 0x1F4)

    #C0008
    ChrTalk(
        0x133,
        (
            "#5805F#12Pん～？\x02\x03",

            "#5810Fキーア、とんでもない\x01",
            "ことになっちゃうのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#0004F#5P大丈夫……\x01",
            "そんな事にはさせないから。\x02\x03",

            "#0001Fそれより、キーア。\x02\x03",

            "名前以外について\x01",
            "何か思い出せた事はあるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x133,
        (
            "#5811F#12Pん～……\x02\x03",

            "#5809F……えへへ。\x01",
            "ぜんぜん思い出せないや。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#0006F#5Pそっか……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#0108F#5P困ったわね……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        "#0308F#11P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x101,
        "#0001F#5Pそういえば、ランディ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)
    Sleep(300)

    #C0015
    ChrTalk(
        0x104,
        (
            "#0304F#11P──ま、俺の話は\x01",
            "おいおいさせてもらうさ。\x02\x03",

            "#0300F……まだ俺が支援課に\x01",
            "居てもいいってんならな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_7ED():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7ED)
    Sleep(50)

    def lambda_7FD():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7FD)
    Sleep(50)

    def lambda_80D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_80D)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)

    #C0016
    ChrTalk(
        0x101,
        "#0013F#5P……怒るぞ、ランディ。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#0201F#6Pランディさん、\x01",
            "たまに空気読めなさすぎです。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        (
            "#0101F#5Pええ、あんまり馬鹿な事を\x01",
            "言わないでちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        "#0302F#11P………悪い。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x133,
        "#5801F#12Pん～……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x133, 0x9, 500)
    Sleep(300)

    #C0021
    ChrTalk(
        0x133,
        (
            "#5810F#6Pねえ、ワンちゃん。\x01",
            "ロイドたちどうしたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        "#1203F#11Pグルルル……\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x190)

    #C0023
    ChrTalk(
        0x105,
        (
            "#0409F#5Pフフ、これも一種の\x01",
            "青春ってやつじゃない？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x133, 0xB4, 0x1F4)

    #C0024
    ChrTalk(
        0x133,
        "#5805F#12Pせいしゅん～？\x02",
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

    def lambda_A1E():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A1E)
    Sleep(50)

    def lambda_A2E():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A2E)
    Sleep(50)

    def lambda_A3E():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A3E)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0025
    ChrTalk(
        0x104,
        (
            "#0309F#11Pハハ……\x01",
            "緊張感の欠片もねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#0012F#5Pそういや俺たち、\x01",
            "さっきまでマフィアに追われて\x01",
            "ピンチだったんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#0102F#5Pなんだか実感がないわね……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#0202F#5P……残念ながら\x01",
            "夢ではなさそうですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#1004F#5Pクク……\x02\x03",

            "#1002Fま、とにかく全ては\x01",
            "支援課に戻ってからだ。\x02\x03",

            "明日からしばらくの間……\x01",
            "厳戒態勢になると思っておけ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BB9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BB9)
    Sleep(50)

    def lambda_BC9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BC9)
    Sleep(50)

    def lambda_BD9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BD9)
    Sleep(50)

    def lambda_BE9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BE9)
    Sleep(50)

    def lambda_BF9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BF9)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)

    #C0030
    ChrTalk(
        0x101,
        "#0001F#12P……はい……！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x133,
        "#5809F#12Pはーい！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(0, 6850, -23170, 0)
    MoveCamera(180, 1, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(35770, 0)
    OP_68(0, 6850, 20170, 6000)
    BeginChrThread(0xB, 1, 0, 6)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    WaitChrThread(0xB, 0)
    WaitChrThread(0xB, 1)
    SetScenarioFlags(0x5A, 2)
    ClearScenarioFlags(0x5A, 3)
    OP_BA(0x4)
    RemoveParty(0x4, 0x0)
    RemoveParty(0x32, 0x0)
    OP_29(0x44, 0x4, 0x10)
    OP_29(0x47, 0x4, 0x10)
    OP_29(0x45, 0x4, 0x20)
    SubItemNumber(0x329, 1)
    SubItemNumber(0x32A, 1)
    SubItemNumber(0x330, 1)
    SubItemNumber(0x2DB, 1)
    SubItemNumber(0x348, 1)
    SubItemNumber(0x347, 1)
    SubItemNumber(0x33B, 1)
    SubItemNumber(0x34C, 1)
    SubItemNumber(0x34F, 1)
    SubItemNumber(0x34D, 1)
    SubItemNumber(0x34E, 1)
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DE(0x27, 0x0)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5F, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1E3)
    OP_24(0x7E)
    SetScenarioFlags(0x5D, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_14E end

    def Function_3_DDE(): pass

    label("Function_3_DDE")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DE9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E07")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_DE9")

    label("loc_E07")

    Return()

    # Function_3_DDE end

    def Function_4_E08(): pass

    label("Function_4_E08")

    Sound(483, 2, 0, 0)
    Sleep(200)
    OP_25(0x1E3, 0xA)
    Sleep(200)
    OP_25(0x1E3, 0x14)
    Sleep(200)
    OP_25(0x1E3, 0x1E)
    Sleep(200)
    OP_25(0x1E3, 0x28)
    Sleep(200)
    OP_25(0x1E3, 0x32)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Return()

    # Function_4_E08 end

    def Function_5_E39(): pass

    label("Function_5_E39")

    OP_25(0x1E3, 0x46)
    Sleep(100)
    OP_25(0x1E3, 0x50)
    Sleep(100)
    OP_25(0x1E3, 0x5A)
    Sleep(100)
    OP_25(0x1E3, 0x64)
    Return()

    # Function_5_E39 end

    def Function_6_E53(): pass

    label("Function_6_E53")

    Sleep(2500)
    OP_25(0x1E3, 0x5A)
    Sleep(400)
    OP_25(0x1E3, 0x50)
    Sleep(400)
    OP_25(0x1E3, 0x46)
    Sleep(400)
    OP_25(0x1E3, 0x3C)
    Sleep(400)
    OP_25(0x1E3, 0x32)
    Sleep(400)
    OP_25(0x1E3, 0x28)
    Sleep(400)
    OP_25(0x1E3, 0x1E)
    Sleep(400)
    BeginChrThread(0xB, 0, 0, 8)
    OP_25(0x1E3, 0x14)
    Sleep(400)
    OP_25(0x1E3, 0xA)
    Sleep(400)
    OP_24(0x1E3)
    Return()

    # Function_6_E53 end

    def Function_7_E9F(): pass

    label("Function_7_E9F")

    Sound(126, 2, 0, 0)
    Sleep(100)
    OP_25(0x7E, 0xA)
    Sleep(100)
    OP_25(0x7E, 0x14)
    Sleep(100)
    OP_25(0x7E, 0x1E)
    Sleep(100)
    OP_25(0x7E, 0x28)
    Sleep(100)
    OP_25(0x7E, 0x32)
    Sleep(100)
    OP_25(0x7E, 0x3C)
    Sleep(100)
    OP_25(0x7E, 0x46)
    Sleep(100)
    OP_25(0x7E, 0x50)
    Return()

    # Function_7_E9F end

    def Function_8_EDE(): pass

    label("Function_8_EDE")

    OP_25(0x7E, 0x3C)
    Sleep(200)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x7E, 0x28)
    Sleep(200)
    OP_25(0x7E, 0x1E)
    Sleep(200)
    OP_25(0x7E, 0x14)
    Sleep(200)
    OP_25(0x7E, 0xA)
    Sleep(200)
    OP_24(0x7E)
    Return()

    # Function_8_EDE end

    SaveToFile()

Try(main)
