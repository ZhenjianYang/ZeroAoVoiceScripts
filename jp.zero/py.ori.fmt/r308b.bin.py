from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r308b.bin",                # FileName
        "r308b",                    # MapName
        "r308b",                    # Location
        0x0065,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -74000, 0, -2000, 0, 0, 1, 101, 0, 1, 0, 2],
    )

    BuildStringList((
        "r308b",                  # 0
        "セルゲイ課長",           # 1
        "ツァイト",               # 2
        "車１",                   # 3
        "アルモリカ古道方面",     # 4
        "太陽の砦",               # 5
    ))

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-94.0, 0.0, -5.0, 0x0000, 0x0000, "アルモリカ古道方面")
    PlaceName(68.0, 0.0, -1.0, 0x0000, 0x0000, "太陽の砦")

    ScpFunction((
        "Function_0_290",          # 00, 0
        "Function_1_2AD",          # 01, 1
        "Function_2_2BD",          # 02, 2
        "Function_3_2CD",          # 03, 3
        "Function_4_1772",         # 04, 4
        "Function_5_17F3",         # 05, 5
    ))


    def Function_0_290(): pass

    label("Function_0_290")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2AC")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x2, 0x1)
    Jump("Function_0_290")

    label("loc_2AC")

    Return()

    # Function_0_290 end

    def Function_1_2AD(): pass

    label("Function_1_2AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_2BC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 3)

    label("loc_2BC")

    Return()

    # Function_1_2AD end

    def Function_2_2BD(): pass

    label("Function_2_2BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC")
    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_2CC")

    Return()

    # Function_2_2BD end

    def Function_3_2CD(): pass

    label("Function_3_2CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02700.itc", 0x1E)
    LoadChrToIndex("chr/ch02702.itc", 0x1F)
    LoadChrToIndex("apl/ch50520.itc", 0x20)
    LoadChrToIndex("apl/ch50521.itc", 0x21)
    AddParty(0x6, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    OP_32(0x6, 0x0, 0x26)
    RemoveCraft(0x6, 0xFFFF)
    OP_38(0x6, 0x80, 0x2)
    OP_38(0x6, 0x81, 0x2)
    OP_38(0x6, 0x82, 0x2)
    OP_38(0x6, 0x83, 0x2)
    OP_38(0x6, 0x84, 0x2)
    OP_38(0x6, 0x85, 0x2)
    OP_38(0x6, 0x86, 0x2)
    OP_42(0x6, 0x442, 0xFF)
    OP_42(0x6, 0x5EC, 0xFF)
    OP_42(0x6, 0x650, 0xFF)
    AddCraft(0x6, 0xD2)
    AddCraft(0x6, 0xD3)
    AddCraft(0x6, 0xD4)
    AddCraft(0x6, 0xD5)
    AddCraft(0x6, 0xD6)
    AddCraft(0x6, 0x118)
    SetChrChipPat(0x6, 0x6, 0x118)
    AddCraft(0x6, 0x13E)
    AddCraft(0x6, 0x150)
    OP_42(0x6, 0x87, 0x0)
    OP_42(0x6, 0x6C, 0x1)
    OP_42(0x6, 0x8D, 0x2)
    OP_42(0x6, 0x7E, 0x3)
    OP_42(0x6, 0x66, 0x4)
    OP_42(0x6, 0x6F, 0x5)
    OP_42(0x6, 0x81, 0x6)
    OP_32(0x7, 0x0, 0x26)
    RemoveCraft(0x7, 0xFFFF)
    OP_38(0x7, 0x80, 0x2)
    OP_38(0x7, 0x81, 0x2)
    OP_38(0x7, 0x82, 0x2)
    OP_38(0x7, 0x83, 0x2)
    OP_38(0x7, 0x84, 0x2)
    OP_38(0x7, 0x85, 0x2)
    OP_38(0x7, 0x86, 0x2)
    OP_42(0x7, 0x447, 0xFF)
    OP_42(0x7, 0x5EC, 0xFF)
    OP_42(0x7, 0x650, 0xFF)
    AddCraft(0x7, 0xDC)
    AddCraft(0x7, 0xDD)
    AddCraft(0x7, 0xDE)
    AddCraft(0x7, 0xDF)
    AddCraft(0x7, 0xE0)
    AddCraft(0x7, 0x11D)
    SetChrChipPat(0x7, 0x6, 0x11D)
    AddCraft(0x7, 0x141)
    AddCraft(0x7, 0x150)
    OP_42(0x7, 0x81, 0x0)
    OP_42(0x7, 0x6C, 0x1)
    OP_42(0x7, 0x99, 0x2)
    OP_42(0x7, 0xA3, 0x3)
    OP_42(0x7, 0x7E, 0x4)
    OP_42(0x7, 0x8B, 0x5)
    OP_42(0x7, 0x7B, 0x6)
    OP_68(-70000, 900, 1000, 0)
    MoveCamera(67, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(29000, 0)
    SetChrPos(0x101, -51300, 0, -2500, 90)
    SetChrPos(0x102, -51800, 0, -1500, 90)
    SetChrPos(0x103, -52800, 0, -3300, 90)
    SetChrPos(0x104, -53300, 0, -2300, 90)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrPos(0x107, -29000, 0, -3100, 270)
    SetChrPos(0x108, -28700, 0, -1900, 270)
    SetChrFlags(0x107, 0x80)
    SetChrBattleFlags(0x107, 0x8000)
    SetChrFlags(0x108, 0x80)
    SetChrBattleFlags(0x108, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x9, -55000, 0, -2900, 90)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, -54000, 250, 1400, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x5, 0xA)
    OP_49()
    SetChrPos(0xA, -84000, 100, 1000, 0)
    OP_D3(0xA, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB5, 0xF0, 0x0, 0x20)
    SetMapObjFlags(0x4, 0x4)
    Sound(485, 0, 100, 0)
    Sleep(300)
    OP_68(-59000, 900, 1000, 5000)
    MoveCamera(67, 17, 0, 5000)
    SetCameraDistance(21000, 5000)

    def lambda_5A7():
        OP_96(0xFE, 0xFFFF2D10, 0x64, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5A7)
    FadeToBright(2000, 0)
    WaitChrThread(0xA, 1)
    ClearMapObjFlags(0x5, 0x20)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x5)
    Sleep(500)
    OP_71(0x5, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_79(0x5)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_68(-52000, 1000, -2300, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0xA, -54000, 100, 1500, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    #C0001
    ChrTalk(
        0x101,
        (
            "#0013F#5P古戦場……\x01",
            "……まさかここが……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        (
            "#0101F#5P《教団》の残党が潜む\x01",
            "拠点#4Rロッジ#だったなんて……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x107, 0x80)
    ClearChrBattleFlags(0x107, 0x8000)
    Sleep(300)
    #Sound(1708, 255, 100, 0)    #voice#Estelle
    Sleep(150)

    #N0003
    NpcTalk(
        0x107,
        "娘の声",
        "#8A来たわね……！\x02",
    )
    #Auto

    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_68(-50200, 900, -2300, 3500)
    MoveCamera(40, 23, 0, 3500)
    SetCameraDistance(17000, 3500)
    ClearChrFlags(0x108, 0x80)
    ClearChrBattleFlags(0x108, 0x8000)

    def lambda_7B2():
        OP_96(0xFE, 0xFFFF3FD0, 0x0, 0xFFFFF3E4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7B2)
    Sleep(200)

    def lambda_7CF():
        OP_96(0xFE, 0xFFFF40FC, 0x0, 0xFFFFF894, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_7CF)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x108, 1)
    OP_6F(0x79)

    #C0004
    ChrTalk(
        0x101,
        "#6P#0002Fエステル、ヨシュア！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#6P#0300Fよう……！\x01",
            "お疲れさんだったな！\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x108,
        (
            "#0903F#11Pそちらこそ……\x01",
            "大変だったみたいですね。\x02\x03",

            "#0900F詳しい話は先ほど通信で\x01",
            "アリオスさんから聞きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x107,
        (
            "#11P#0800Fあたしたちも、さっきやっと\x01",
            "そこの入口を開いたばかりよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        "#6P#0205Fあ……\x02",
    )

    CloseMessageWindow()
    OP_68(-24000, 3000, -2000, 3000)
    MoveCamera(75, 5, 0, 3000)
    SetCameraDistance(26500, 3000)

    def lambda_937():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_937)
    Sleep(100)

    def lambda_947():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_947)
    OP_6F(0x79)

    #C0009
    ChrTalk(
        0x103,
        "#0201F閉じていた扉が……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0010
    ChrTalk(
        0x107,
        (
            "#0806F変な仕掛けがあって\x01",
            "開くのに手間取っちゃった。\x02\x03",

            "#0800Fでもこれで、連中の拠点に\x01",
            "潜入することが出来るわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-50200, 900, -2300, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    Sleep(300)

    #C0011
    ChrTalk(
        0x101,
        (
            "#6P#0004F……本当に助かったよ。\x02\x03",

            "#0001F俺たちはこのまま、\x01",
            "首謀者を逮捕しに行くけれど……\x02\x03",

            "君たちの方はどうする？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A97():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A97)
    Sleep(50)

    def lambda_AA7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_AA7)
    Sleep(300)

    #C0012
    ChrTalk(
        0x107,
        (
            "#11P#0809Fモチ、手伝わせてもらうわ！\x02\x03",

            "#0800Fそのためにここで待ってたんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x108,
        (
            "#0900F#11P失踪者も救出する必要があるし、\x01",
            "助太刀させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#6P#0004F……ありがとう。\x01",
            "君たちがいたら百人力だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    StopBGM(0xFA0)

    #C0015
    ChrTalk(
        0x101,
        (
            "#6P#0001F──そうだ。\x01",
            "君たちに伝言があったんだ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "病院の研究棟でレンから聞いた伝言を伝えた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(500)
    PlayBGM("ed7001", 0)

    #C0017
    ChrTalk(
        0x108,
        "#0908F#11Pそうか……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x107,
        "#11P#0808F……やっぱり……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#0103F#6Pレンちゃんを捕まえる\x01",
            "最後のチャンスをあげる……\x02\x03",

            "#0101F一体、どういう意味なのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x107,
        (
            "#11P#0804Fうん……\x02\x03",

            "#0800F──多分レンは、あたしたちが\x01",
            "あの子の全てを受け止められるか\x01",
            "試しているんだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x108,
        (
            "#0903F#11Pそのためには\x01",
            "かつてあの子を襲った悲劇の\x01",
            "一端を担っていた人物……\x02\x03",

            "#0901F“彼”から全ての真実を\x01",
            "聞き出す必要がありそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#6P#0001Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#6P#0206F……わたしも改めて\x01",
            "あの人を問い詰めたいです。\x02\x03",

            "#0208Fなぜ、あんな実験をしたのか……\x02\x03",

            "どうしてこの地に落ち延びて\x01",
            "《グノーシス》を完成させたのか……\x02\x03",

            "#0201Fそしてキーアの正体と、\x01",
            "彼女に何をするつもりなのか……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EF0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EF0)
    Sleep(100)

    def lambda_F00():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F00)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    #C0024
    ChrTalk(
        0x102,
        "#0101F#5Pそうね……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#5P#0303F締め上げることは\x01",
            "どのみち確定みてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#11P#0003Fああ……確実に逮捕しよう。\x02\x03",

            "#0013F操られた警備隊を解放して、\x01",
            "キーアの安全を確保するためにも。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    #N0027
    NpcTalk(
        0x8,
        "男の声",
        "#40W……行くのか。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x108, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_106D():

        label("loc_106D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_106D")

    QueueWorkItem2(0x101, 2, lambda_106D)
    Sleep(50)

    def lambda_1082():

        label("loc_1082")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1082")

    QueueWorkItem2(0x102, 2, lambda_1082)
    Sleep(50)

    def lambda_1097():

        label("loc_1097")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1097")

    QueueWorkItem2(0x103, 2, lambda_1097)
    Sleep(50)

    def lambda_10AC():

        label("loc_10AC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_10AC")

    QueueWorkItem2(0x104, 2, lambda_10AC)

    def lambda_10BE():

        label("loc_10BE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_10BE")

    QueueWorkItem2(0x9, 2, lambda_10BE)
    OP_68(-52700, 1000, -1000, 2500)
    MoveCamera(47, 25, 0, 2500)
    SetCameraDistance(16500, 2500)
    BeginChrThread(0x8, 3, 0, 4)
    WaitChrThread(0x8, 3)
    OP_6F(0x79)

    #C0028
    ChrTalk(
        0x101,
        "#0005F#11P課長……！\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#11P#0101F止血したばかりなんですから\x01",
            "あまり動かないでください……！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#5P#1002F#30Wクク、さすがにこの足で\x01",
            "付いていくつもりはねえさ……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 5)
    WaitChrThread(0x8, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x9, 0x2)

    #C0031
    ChrTalk(
        0x8,
        (
            "#1004F#5P#30W……だがせめて、\x01",
            "ここで見送るくらいはさせろ。\x02\x03",

            "一人前になりかけの部下どもを\x01",
            "見送るくらいはな……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#0008F#11P課長……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#12P#0306Fったく……\x01",
            "カッコ付けすぎだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "#1002F#5P#30Wクク……それが\x01",
            "オヤジの特権ってヤツだ。\x02\x03",

            "#1003F──ロイド、エリィ、\x01",
            "ティオ、ランディ……\x02\x03",

            "着任して４ヶ月あまり……\x01",
            "お前らもそれなりに成長した。\x02\x03",

            "無事、この件にケリを付けたら\x01",
            "晴れて一人前として認めてやる。\x02\x03",

            "#1001Fだから……\x01",
            "絶対に無事に戻ってこい！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#0001F#11Pはい……！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        "#11P#0100F分かりました！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        "#12P#0202F……了解です……！\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#12P#0309Fイエス・サー！\x02",
    )

    CloseMessageWindow()
    OP_E5()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    OP_6F(0x10)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7305", 0)
    ReplaceBGM("ed7510", "ed7305")
    Sleep(1600)
    OP_68(-29000, 1000, -2000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20000, 0)
    OP_90(0x101, -40000, 0, -2000, 90)
    OP_90(0x102, -41300, 0, -2900, 90)
    OP_90(0x103, -41700, 0, -1500, 90)
    OP_90(0x104, -40600, 0, -900, 90)
    OP_90(0x107, -43500, 0, -2500, 90)
    OP_90(0x108, -44000, 0, -1500, 90)
    OP_90(0x9, -53400, 0, -2300, 90)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x8, 0x1)

    def lambda_14EF():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14EF)
    Sleep(50)

    def lambda_1507():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1507)
    Sleep(50)

    def lambda_151F():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_151F)
    Sleep(50)

    def lambda_1537():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1537)
    Sleep(50)

    def lambda_154F():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_154F)
    Sleep(50)

    def lambda_1567():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1567)
    SetCameraDistance(17000, 4000)
    FadeToBright(2000, 0)
    OP_6F(0x10)
    OP_4B(0x101, 0xFF)
    OP_4B(0x102, 0xFF)
    OP_4B(0x103, 0xFF)
    OP_4B(0x104, 0xFF)
    OP_4B(0x107, 0xFF)
    OP_4B(0x108, 0xFF)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x107, 0x80)
    SetChrBattleFlags(0x107, 0x8000)
    SetChrFlags(0x108, 0x80)
    SetChrBattleFlags(0x108, 0x8000)
    Fade(500)
    OP_68(-53500, 2000, -1800, 0)
    MoveCamera(63, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12000, 0)
    OP_68(-53500, 1300, -1800, 5000)
    OP_6F(0x1)
    OP_4C(0x101, 0xFF)
    OP_4C(0x102, 0xFF)
    OP_4C(0x103, 0xFF)
    OP_4C(0x104, 0xFF)
    OP_4C(0x107, 0xFF)
    OP_4C(0x108, 0xFF)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    ClearChrFlags(0x107, 0x80)
    ClearChrBattleFlags(0x107, 0x8000)
    ClearChrFlags(0x108, 0x80)
    ClearChrBattleFlags(0x108, 0x8000)
    PlaceName2(340, 200, "c_plac30", 0x0, 2500)
    Fade(500)
    OP_68(-7500, 6200, -2000, 0)
    MoveCamera(50, 40, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_68(12500, 17200, -2000, 6000)
    MoveCamera(60, 15, 0, 6000)
    SetCameraDistance(25000, 6000)
    OP_6F(0x79)
    Sleep(2000)
    Fade(500)
    OP_68(38500, 21000, -2000, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(30000, 0)
    OP_68(51500, 21000, -2000, 4000)
    MoveCamera(60, 27, 0, 4000)
    SetCameraDistance(17000, 4000)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x107, 0xFF)
    EndChrThread(0x108, 0xFF)
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("m3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2CD end

    def Function_4_1772(): pass

    label("Function_4_1772")

    BeginChrThread(0x8, 0, 0, 0)

    def lambda_177D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_177D)

    def lambda_178E():
        OP_96(0xFE, 0xFFFF2D10, 0xFA, 0x0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_178E)
    WaitChrThread(0x8, 1)

    def lambda_17AC():
        OP_96(0xFE, 0xFFFF2D10, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17AC)
    WaitChrThread(0x8, 1)

    def lambda_17CA():
        OP_96(0xFE, 0xFFFF2D10, 0x0, 0xFFFFFCE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17CA)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x8, 0x101, 500)
    Return()

    # Function_4_1772 end

    def Function_5_17F3(): pass

    label("Function_5_17F3")

    OP_92(0x8, 0xFFFF3224, 0xFFFFFCE0, 0x1F4)
    BeginChrThread(0x8, 0, 0, 0)

    def lambda_180B():
        OP_96(0xFE, 0xFFFF3224, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_180B)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    OP_93(0x8, 0xB4, 0x1F4)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    Return()

    # Function_5_17F3 end

    SaveToFile()

Try(main)
