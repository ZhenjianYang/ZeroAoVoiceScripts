from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4100.bin",                # FileName
        "e4100",                    # MapName
        "e4100",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, -74000, 0, -2500, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4100",                  # 0
        "神狼ツァイト",           # 1
        "守護騎士ワジ",           # 2
        "守護騎士ケビン",         # 3
        "従騎士リース",           # 4
        "正騎士アッバス",         # 5
        "神狼ツァイト",           # 6
        "メルカバ",               # 7
        "メルカバ",               # 8
        "メルカバ光学迷彩",       # 9
        "メルカバ光学迷彩",       # 10
        "SE制御",                 # 11
    ))

    DeclNpc(0,       0,       0,       0,    229,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(568, 0)                                        # 0

    ScpFunction((
        "Function_0_238",          # 00, 0
        "Function_1_248",          # 01, 1
        "Function_2_25E",          # 02, 2
        "Function_3_3945",         # 03, 3
        "Function_4_39B1",         # 04, 4
        "Function_5_3A2E",         # 05, 5
        "Function_6_3A53",         # 06, 6
        "Function_7_3A78",         # 07, 7
        "Function_8_3AA5",         # 08, 8
        "Function_9_3AF4",         # 09, 9
        "Function_10_3B6D",        # 0A, 10
        "Function_11_3BE6",        # 0B, 11
        "Function_12_3C1A",        # 0C, 12
        "Function_13_3C36",        # 0D, 13
        "Function_14_3C8E",        # 0E, 14
        "Function_15_3CF9",        # 0F, 15
        "Function_16_3D88",        # 10, 16
        "Function_17_3DE0",        # 11, 17
        "Function_18_3E4B",        # 12, 18
        "Function_19_3EDA",        # 13, 19
        "Function_20_3EF2",        # 14, 20
        "Function_21_3F31",        # 15, 21
        "Function_22_3F7C",        # 16, 22
        "Function_23_3FF7",        # 17, 23
        "Function_24_4021",        # 18, 24
        "Function_25_4061",        # 19, 25
        "Function_26_408A",        # 1A, 26
        "Function_27_40A2",        # 1B, 27
    ))


    def Function_0_238(): pass

    label("Function_0_238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_247")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_247")

    Return()

    # Function_0_238 end

    def Function_1_248(): pass

    label("Function_1_248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_25D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_25D")

    Return()

    # Function_1_248 end

    def Function_2_25E(): pass

    label("Function_2_25E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xFE, 0x0)
    LoadChrToIndex("chr/ch03100.itc", 0x1E)
    LoadChrToIndex("chr/ch06710.itc", 0x1F)
    LoadChrToIndex("chr/ch11400.itc", 0x20)
    LoadChrToIndex("chr/ch11500.itc", 0x21)
    LoadChrToIndex("apl/ch51620.itc", 0x22)
    LoadChrToIndex("apl/ch51614.itc", 0x23)
    LoadChrToIndex("apl/ch51615.itc", 0x24)
    LoadChrToIndex("chr/ch00056.itc", 0x25)
    LoadChrToIndex("apl/ch51619.itc", 0x26)
    SoundLoad(2917)
    SoundLoad(2918)
    SoundLoad(2919)
    SoundLoad(2920)
    SoundLoad(962)
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(496)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis413.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10401.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12100.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13800.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04300.itp")
    SetChrPos(0x101, -129880, 4000, -26390, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x1)
    SetChrFlags(0x101, 0x2000)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1000)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x2, 0x8)
    OP_49()
    SetChrPos(0x8, -127870, 4000, -35110, 0)
    OP_93(0x8, 0x5A, 0x0)
    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0xA, 0x32, 0x1, 0x20)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x8000)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1C84), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x2, 0x97, 0xAA, 0x1, 0x20)
    OP_D3(0x101, 0x2, "Null_senaka(42)")
    SetMapObjFrame(0x2, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x2, "879mabuta:Layer2(44)", 0x0, 0x1)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_78(0x0, 0xE)
    OP_78(0x1, 0xF)
    OP_78(0x4, 0x10)
    OP_78(0x5, 0x11)
    SetChrPos(0xE, -136010, -1150, -71530, 0)
    SetChrPos(0x10, -136010, -1150, -71530, 0)
    SetChrPos(0xF, -123270, -1350, -76920, 0)
    SetChrPos(0x11, -123270, -1350, -76920, 0)
    OP_93(0xE, 0x0, 0x15E)
    OP_93(0x10, 0x0, 0x15E)
    OP_93(0xF, 0x0, 0x15E)
    OP_93(0x11, 0x0, 0x15E)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x7, 0x1000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1000, 0, 0, 0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 2000, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 3000, 0, 0, 0)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 4000, 0, 0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    OP_70(0x3, 0x0)
    Sound(132, 2, 100, 0)
    BeginChrThread(0x12, 1, 0, 20)
    Sleep(2000)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_68(-207000, 1650, -16820, 0)
    MoveCamera(333, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(74640, 0)
    SetChrPos(0x8, -225000, 0, -24000, 0)
    BeginChrThread(0x8, 0, 0, 3)
    OP_68(-165050, 1650, -5550, 6000)
    MoveCamera(312, 34, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(56890, 6000)
    PlaceName2(340, 200, "c_plac65", 0x0, 0)
    Sleep(4500)
    StopSound(962, 2000, 40)
    Sleep(1000)
    FadeToDark(500, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x0)
    SetChrPos(0x8, -132000, 4000, -31000, 0)
    OP_93(0x8, 0x46, 0x0)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    SetChrFlags(0x8, 0x1)
    OP_93(0x101, 0x0, 0x0)
    SetChrSubChip(0x101, 0x3)
    OP_68(-129830, 6900, -28710, 0)
    MoveCamera(262, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    Sleep(1000)
    BeginChrThread(0x12, 1, 0, 21)
    FadeToBright(500, 0)
    SetCameraDistance(15390, 6000)
    Sleep(500)
    BeginChrThread(0x101, 0, 0, 4)
    Sleep(1000)
    OP_68(-129750, 7300, -28810, 4500)
    MoveCamera(263, 11, 0, 4500)
    OP_6E(600, 4500)
    OP_0D()
    Sleep(1000)
    SetChrPos(0xD, -128370, 7200, -29090, 0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x101, 0)
    Sleep(500)
    Sleep(500)
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x101,
        (
            "#00008F#5Pここは……\x01",
            "共和国方面の国境か。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 5)
    Sleep(1500)

    #C0002
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5Pここならば国防軍とやらも\x01",
            "手を延ばしては来ないだろう。\x02",
        )
    )

    WaitChrThread(0x8, 0)
    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5Pまずは一息付くがいい。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)
    Sleep(150)

    #C0004
    ChrTalk(
        0x101,
        (
            "#00006F#12P#Nありがとう、ツァイト。\x01",
            "……本当に助かったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0005
    ChrTalk(
        0x101,
        "#00011F#5Pえ───\x02",
    )

    CloseMessageWindow()
    OP_68(-146110, 10500, -23540, 3000)
    MoveCamera(260, 9, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15390, 3000)
    OP_6F(0x79)

    #C0006
    ChrTalk(
        0x101,
        "#00007F#6P#Nあれは……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0007
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#6P#Nクロスベル市を包み込むように\x01",
            "出現した《結界》のようなものだ。\x02\x03",

            "“許された存在”については\x01",
            "自由に出入りできるようだが……\x02\x03",

            "そうでない存在は\x01",
            "決して通すことがないらしい。\x02\x03",

            "人にしても、乗り物にしても。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0008
    ChrTalk(
        0x101,
        "#00013F#6P#N……そんなものが……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-129830, 6900, -28710, 0)
    MoveCamera(262, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    Fade(500)
    OP_0D()
    OP_68(-129830, 6900, -28710, 80000)
    MoveCamera(235, 19, 0, 80000)
    OP_6E(600, 80000)
    SetCameraDistance(20000, 80000)
    Sleep(500)

    #C0009
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P既に《プレロマ草》も\x01",
            "クロスベル全土に咲き乱れている。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P今やクロスベルそのものが\x01",
            "《至宝》と一体化してしまったと\x01",
            "言っても過言ではないだろう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    #C0011
    ChrTalk(
        0x101,
        (
            "#00008F#12P《プレロマ草》というのは\x01",
            "結局なんなんだ？\x02\x03",

            "地下に流れる七耀脈に\x01",
            "関係するとは聞いたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5Pかつての《幻の至宝》が\x01",
            "人と地上を識#2Rし#るために咲かせた\x01",
            "眼にして依代とでも言うべきか。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P《至宝》と霊的に結びつくことで\x01",
            "周囲の空間を歪ませたりもする。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P本来、この次元には現れない\x01",
            "《幻獣》などが出現しているのも\x01",
            "そのあたりが原因だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00006F#12Pなるほど……\x02\x03",

            "#00008F……かつて《Ｄ∴Ｇ教団》が\x01",
            "やってきた非道な儀式の数々……\x02\x03",

            "#00013Fあれにプレロマ草を原料とした\x01",
            "《グノーシス》が使われた事にも\x01",
            "理由があったんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5Pうむ、恐らく犠牲となった\x01",
            "数多#4Rあま た #の被験者の知識や人格……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5Pそれらの膨大な情報が\x01",
            "《太陽の砦》に眠る“彼女”に\x01",
            "送り届けられていたのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5Pそれらの情報は自己組織化され、\x01",
            "より高位の人格を生み出すための\x01",
            "苗床となり……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5Pそして５００年の時を経て、\x01",
            "《至宝》の“核”は目覚めた。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00006F#12P#40W………………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0021
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P──私がおぬしに\x01",
            "伝えられるのはこのくらいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P“彼ら”は周到に計画を練り上げ、\x01",
            "この状況を作り出した。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5Pその意味で、おぬしの取れる\x01",
            "選択肢は余りにも少ないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5Pこのままほとぼりが冷めるまで\x01",
            "異国に逃れていたらどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00004F#12Pはは、そうだな……\x02\x03",

            "#00008F……カルバードだったら\x01",
            "叔父さんの家もあるし、\x01",
            "悪くないかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-130699, 6500, -28440, 0)
    MoveCamera(264, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17590, 0)
    Fade(500)
    OP_0D()
    Sleep(300)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    #C0026
    ChrTalk(
        0x101,
        (
            "#00006F#6P──でも、止めておくよ。\x02\x03",

            "#00000F一番知りたい真実を\x01",
            "まだ確かめていないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5Pなに……？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00003F#6Pそれを確かめるためにも……\x01",
            "俺にはみんなの力が必要だ。\x02\x03",

            "エリィ、ティオ、ランディ。\x01",
            "それ以外にも大勢の力が……\x02\x03",

            "#00008Fそのためにも俺は……\x01",
            "“あちら側”に戻るよ。\x02\x03",

            "#00000Fせっかくここまで\x01",
            "送ってくれて悪いんだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P確かめたい真実とは、何だ？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#00004F#6P──決まっている。\x02",
    )

    CloseMessageWindow()
    OP_68(-129470, 6300, -28970, 0)
    MoveCamera(263, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12800, 0)
    Fade(500)
    OP_0D()
    TurnDirection(0x101, 0xD, 500)
    Sleep(300)

    #C0032
    ChrTalk(
        0x101,
        (
            "#00008F#12P力や生い立ちに関係なく……\x02\x03",

            "#00000Fあの子が──キーアが\x01",
            "本当はどうしたいのか#20R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲#って事さ。\x02\x03",

            "多分、あの子を取り戻さない限り、\x01",
            "本心は教えてくれないだろうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#N…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0034
    ChrTalk(
        0x101,
        (
            "#00006F#12Pそれに、かつての《至宝》が\x01",
            "耐えられなかったほどの重圧に\x01",
            "晒されてるかもしれないなんて……\x02\x03",

            "そんな環境に、うちのキーアを\x01",
            "置いておけるわけがないだろう？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0035
    ChrTalk(
        0x101,
        (
            "#00010F#12P#4S大統領やアリオスさんを\x01",
            "殴り飛ばしても絶対に連れ戻す！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#Nフフ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    StopBGM(0xFA0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x2000)
    SetChrFlags(0xC, 0x2000)
    SetChrFlags(0xA, 0x2000)
    SetChrFlags(0xB, 0x2000)
    BeginChrThread(0x9, 0, 0, 7)
    BeginChrThread(0xC, 0, 0, 8)
    BeginChrThread(0xA, 0, 0, 9)
    BeginChrThread(0xB, 0, 0, 10)
    Sleep(100)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xD, -133920, 8200, -35070, 0)
    OP_C9(0x0, 0x80000000)

    #N0037
    NpcTalk(
        0x9,
        "少年の声",
        "#11P#2917V#30W#38A#Nアハハ、ホント親バカだなぁ。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x101,
        "#00011F#12Pえ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)
    OP_68(-137840, 4800, -46130, 0)
    MoveCamera(235, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18330, 0)
    Fade(500)
    OP_68(-133770, 4600, -39110, 4000)
    MoveCamera(227, 20, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(19660, 4000)
    BeginChrThread(0x8, 0, 0, 11)
    BeginChrThread(0x101, 0, 0, 12)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_6F(0x79)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)

    #C0039
    ChrTalk(
        0x101,
        (
            "#00005F#6P#Nワジ、どうして……\x02\x03",

            "#00011Fそれにアッバスに……\x01",
            "リースさんに、あなたは！？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("アッバス")

    #A0040
    AnonymousTalk(
        0xFF,
        "──久しいな、バニングス。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("シスター・リース")

    #A0041
    AnonymousTalk(
        0xFF,
        "ご無沙汰しています。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("ケビン神父")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            "やー、オレとは\x01",
            "４ヶ月ぶりくらいかな？\x02\x03",

            "覚えとってくれて嬉しいわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)

    #C0043
    ChrTalk(
        0x101,
        (
            "#00006F#6P#N確かあなたとリースさんは\x01",
            "教会の『星杯騎士団』……\x02\x03",

            "#00007Fワジ、もしかしてお前──！？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)
    #Sound(2430, 255, 100, 0)    #voice#Lazy

    #N0044
    NpcTalk(
        0x9,
        "ワジ",
        "#10404F#5Pフフ……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7356", 0)
    OP_68(-133770, 4600, -39110, 100000)
    MoveCamera(227, 19, 0, 100000)
    OP_6E(600, 100000)
    SetCameraDistance(16860, 100000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0045
    AnonymousTalk(
        0x9,
        (
            "#2918V#30W七耀教会、星杯騎士団所属。\x02\x03",

            "#2919V守護騎士#8Rド ミ ニ オ ン#第九位──\x01",
            "《蒼の聖典》ワジ・ヘミスフィアさ。\x02\x03",

            "#2920V改めてよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB68)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_C9(0x1, 0x80000000)

    #C0046
    ChrTalk(
        0x101,
        "#00011F#6P………………………（パクパク）\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xC,
        (
            "#12102F#5P……ちなみに自分は\x01",
            "騎士団の正騎士の立場にある。\x02\x03",

            "ワジの補佐が主な任務だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#00015F#6P……ああもう！\x01",
            "いきなりすぎて何が何だか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0049
    ChrTalk(
        0x101,
        (
            "#00011F#6Pそ、それじゃあ。\x02\x03",

            "リースさんと最初に会った時、\x01",
            "お互い何も言わなかったのは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xB,
        (
            "#13806F#11P……すみません。\x01",
            "知らないフリをしていました。\x02\x03",

            "#13802Fヘミスフィア卿の潜入調査は\x01",
            "極秘とされていましたので。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "#10404F#5Pで、彼女が来てくれたおかげで\x01",
            "エラルダ大司教の注意が\x01",
            "完全に逸れてくれたってワケさ。\x02\x03",

            "#10402Fいや、ホント助かっちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xB,
        "#13804F#11Pお役に立てて幸いです。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xA,
        (
            "#04306F#11Pま、リースの場合、\x01",
            "どう考えても普通のシスターには\x01",
            "見えへんやろうからなぁ。\x02\x03",

            "#04302F大司教もさぞ面食らったやろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        (
            "#13803F#11P……大きなお世話。\x02\x03",

            "#13811Fというかケビンは\x01",
            "人のことは言えないと思う。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0055
    ChrTalk(
        0x101,
        (
            "#00012F#6P（なんか誰一人として普通の\x01",
            "  聖職者には見えないんだが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "#10404F#5P──まあ、改めての\x01",
            "自己紹介はこのくらいにして。\x02\x03",

            "#10400F僕たちがこの場に現れたのは\x01",
            "そちらの彼に呼ばれたからでね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x104, 0x1F4)

    #C0057
    ChrTalk(
        0x101,
        "#00011F#6Pツァイトに……？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 5)
    WaitChrThread(0x8, 0)
    SetChrPos(0xD, -132240, 7300, -35100, 0)

    #C0058
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#Nうむ、そうさせてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#Nおぬしの決意が固いのであれば\x01",
            "協力者は必要かと思ってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#00005F#6Pあ……\x02",
    )

    CloseMessageWindow()

    def lambda_1F41():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F41)
    BeginChrThread(0x8, 0, 0, 6)
    SetChrPos(0xD, -133920, 8200, -35070, 0)
    Sleep(500)

    #C0061
    ChrTalk(
        0x9,
        (
            "#10406F#5P僕が潜入していた事からも\x01",
            "分かると思うけど……\x02\x03",

            "#10401F騎士団はある程度、\x01",
            "今回の事態を予測していてね。\x02\x03",

            "ただ、クロイス家の陰謀や\x01",
            "キーアの正体については\x01",
            "判らないことも多かったんだ。\x02\x03",

            "先日、彼と再会した折に、\x01",
            "一通り教えてもらったけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xC,
        (
            "#12100F#5Pしかし《幻の至宝》は消滅しており、\x01",
            "それに代わる新たな至宝が\x01",
            "人の手で生み出されたとなると……\x02\x03",

            "事態は『古代遺物#8Rアーティファクト#』を回収する\x01",
            "騎士団の役割から外れて来てな。\x02\x03",

            "このままでは介入する口実が\x01",
            "無くなってしまう所だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        (
            "#04303F#11Pかといって《結社》が\x01",
            "この事態に絡んでいるとなると\x01",
            "オレらも放ってはおけん……\x02\x03",

            "#04300Fそこで“君”という口実に\x01",
            "頼らせてもらおうと思ったんや。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00001F#6P……！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "#10404F#5Pそういうこと──\x02\x03",

            "#10402F君に協力させてもらう形で\x01",
            "僕たちは今回の事件に\x01",
            "介入させてもらおうと思う。\x02\x03",

            "どうだい、ロイド？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#00008F#6P#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0067
    ChrTalk(
        0x101,
        (
            "#00006F#6P──１つ確認させてくれ。\x02\x03",

            "#00013Fあんたたちは……\x01",
            "キーアをどうするつもりだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0068
    ChrTalk(
        0x9,
        "#10408F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        "#04306F#11P……難しい質問やねぇ。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        (
            "#13808F#11Pでも、誤魔化しても\x01",
            "始まらないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "#12100F#5Pうむ、正直なところを\x01",
            "まずは伝えるべきだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "#10403F#5P……そうだね。\x02\x03",

            "#10401F《零#2Rゼロ#の至宝》だけど──\x01",
            "正直、《空の至宝#8Rオ ー リ オ ー ル#》より\x01",
            "遥かに危険で厄介な存在だ。\x02\x03",

            "現時点で、力の全貌が\x01",
            "見えていないにも関わらず、\x01",
            "ここまでの状況を作り上げた。\x02\x03",

            "#10406F──君、いま大陸諸国が\x01",
            "どうなっているか知ってるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#00005F#6Pいや……\x02\x03",

            "#00001F……帝国の方で内戦が\x01",
            "始まったのは噂で聞いたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "#04306F#11Pぶっちゃけ、直接のきっかけは\x01",
            "クロスベル方面に投入された\x01",
            "帝国軍師団が壊滅したことでな。\x02\x03",

            "#04308F帝国軍もプライドがあるから\x01",
            "次々と師団を送り込んだんやけど\x01",
            "あの人形どもに全部返り討ちされて……\x02\x03",

            "#04301Fそれで帝国軍が混乱しとる隙に\x01",
            "貴族勢力の連合軍が\x01",
            "帝都を電撃占領したんや。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0075
    ChrTalk(
        0xC,
        (
            "#12100F#5P結果、鉄血宰相は凶弾に倒れ、\x01",
            "行方知れず……\x02\x03",

            "帝国全土を巻き込んだ内戦が\x01",
            "長期化し始めている状況だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xB,
        (
            "#13803F#11P一方、共和国の方でも\x01",
            "クロスベルに端を発する\x01",
            "経済恐慌が発生し……\x02\x03",

            "#13801Fテロが活発化した事によって\x01",
            "非常事態宣言が出されています。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#00006F#6P……そうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#10403F#5P勿論、それ以外の国だって\x01",
            "恐慌や混乱とは無縁じゃない。\x02\x03",

            "特に今まで帝国と共和国に\x01",
            "押さえつけられていた地域では\x01",
            "キナ臭い動きも出始めている。\x02\x03",

            "#10408F──そんな中、ディーター大統領は\x01",
            "各地に働きかけているらしいんだ。\x02\x03",

            "#10401Fクロスベルを盟主とする\x01",
            "新たな秩序に参加するようにとね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x101,
        (
            "#00013F#6P…………………………………\x02\x03",

            "#00003F……当然、その背景には\x01",
            "《至宝》の力があるわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "#10404F#5Pもちろん。\x02\x03",

            "大陸最強と言われる帝国軍を\x01",
            "あっさり撃退できるだけの力だ。\x02\x03",

            "#10408Fしかも、今は《結社》が用意した\x01",
            "３体の人形兵器しかないけど……\x02\x03",

            "#10402Fそれが増産されて、\x01",
            "全てが《至宝》の力を受けて\x01",
            "大陸全土に飛ばされたりしたら？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#00010F#6Pくっ……\x02\x03",

            "#00007F……キーアは……\x01",
            "あの子はそんなことはしない！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xC,
        (
            "#12100F#5P──ちなみにあの人形兵器は\x01",
            "至宝が操っているわけではない。\x02\x03",

            "至宝の力を受け、自律的に行動する\x01",
            "《守護者》のような存在だろう。\x02\x03",

            "あのレンという娘が使っていた\x01",
            "《パテル＝マテル》という機体同様。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        "#00011F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "#04306F#11P……その意味では、\x01",
            "その子の意志とは関係なく\x01",
            "勝手に動いとるってことやね。\x02\x03",

            "#04301Fそれどころか、関係ない連中に\x01",
            "利用される可能性だってある。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xB,
        (
            "#13806F#11Pキーアちゃんの意志とは別に……\x02\x03",

            "#13808Fそれだけの“力”が持つ危険性は\x01",
            "無視できないという事でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#00008F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_68(-132290, 5000, -37670, 0)
    MoveCamera(1, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    Fade(500)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0087
    ChrTalk(
        0x101,
        (
            "#00003F#11P──あなた達の意見は判った。\x02\x03",

            "#00001Fそれでも構わないから……\x01",
            "今は協力を頼みたいと思う。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0088
    ChrTalk(
        0x9,
        (
            "#10405F#6Pへえ……？\x02\x03",

            "#10402Fてっきり申し出を\x01",
            "突っぱねるかと思ったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00006F#11P俺だけで何とかなる事態じゃ\x01",
            "ないのは確かだからな……\x02\x03",

            "#00008F解決が長引けば長引くほど\x01",
            "あの子も苦しむかもしれない……\x02\x03",

            "#00010F───だが！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(812, 0, 100, 0)
    SetCameraDistance(14300, 500)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x6)
    OP_0D()
    Sleep(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13000, 250)
    Sound(802, 0, 70, 0)
    SetChrSubChip(0x101, 0x7)
    OP_6F(0x79)
    CancelBlur(0)
    OP_82(0x96, 0x0, 0xBB8, 0x1F4)

    #C0090
    ChrTalk(
        0x101,
        (
            "#00007F#11Pもし、あんた達が勝手に\x01",
            "キーアの処遇を決めようとしたら！\x02\x03",

            "全力をもって阻止するとだけは\x01",
            "今、この場で言っておく！\x02\x03",

            "#00003F俺だけじゃない！\x01",
            "エリィやティオ、ランディだって\x01",
            "きっと同じことを言うはずだ！\x02\x03",

            "#00013F理屈も道理も関係なく──\x01",
            "ただあの子の“保護者”として！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xB,
        "#13805F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        "#12102F#6P………ふむ……………\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "#04304F#6Pハハ、秀才君っぽいのに\x01",
            "メチャメチャ熱い兄さんやな。\x02\x03",

            "#04302Fワジ、お前が気に入るのも\x01",
            "判る気がするで。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "#10409F#6Pフフ、愛してるといっても\x01",
            "過言じゃないけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#00010F#11Pワジ、俺は本気で──！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_68(-133770, 4600, -39110, 0)
    MoveCamera(227, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16860, 0)
    Fade(500)
    OP_68(-133450, 4400, -39970, 2000)
    MoveCamera(227, 22, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14450, 2000)
    OP_0D()
    BeginChrThread(0x9, 0, 0, 25)
    WaitChrThread(0x9, 0)
    Sleep(800)

    #C0096
    ChrTalk(
        0x9,
        (
            "#10403F#5P──星杯の騎士として\x01",
            "女神#4Rエイドス#の名に賭けて誓おう。\x02\x03",

            "あの子の処遇に関しては\x01",
            "君たちの意見を\x01",
            "必ず聞くことを約束する。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-133770, 4600, -39110, 1500)
    MoveCamera(227, 19, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(16860, 1500)
    Sleep(500)
    SetChrSubChip(0x9, 0x0)
    Sleep(130)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x1000)
    OP_6F(0x79)

    #C0097
    ChrTalk(
        0x9,
        (
            "#10406F#5P……僕らの立場としては\x01",
            "このあたりが限界なんだけど。\x02\x03",

            "#10402Fどうかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00006F#6Pああ……十分だ。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xC,
        "#12102F#5P──決まりだな。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        (
            "#04304F#11Pよし、そんなら早速、\x01",
            "動き始めるとしようか。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    BeginChrThread(0xA, 2, 0, 26)
    Sound(812, 0, 100, 0)
    BeginChrThread(0x12, 1, 0, 22)
    StopSound(132, 1000, 30)
    OP_68(-134270, 4400, -39100, 2500)
    MoveCamera(227, 19, 0, 2500)
    OP_6E(600, 2500)
    SetCameraDistance(16860, 2500)
    OP_6F(0x79)

    #C0101
    ChrTalk(
        0x101,
        "#00005F#6Pな、なんだ……？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12Pフム……\x01",
            "随分と懐かしい響きだ。\x02\x03",

            "教会の《天の車》か。\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    OP_75(0x6, 0x1, 0x0)
    OP_75(0x7, 0x1, 0x0)
    SetChrPos(0xE, -136010, 41150, -71530, 0)
    SetChrPos(0x10, -136010, 41150, -71530, 0)
    SetChrPos(0xF, -123270, 46350, -76920, 0)
    SetChrPos(0x11, -123270, 46350, -76920, 0)
    BeginChrThread(0xE, 0, 0, 13)
    BeginChrThread(0xF, 0, 0, 16)
    BeginChrThread(0x101, 1, 0, 19)
    BeginChrThread(0x12, 1, 0, 23)
    BeginChrThread(0xA, 2, 0, 27)
    OP_68(-126850, 7200, -36760, 3000)
    MoveCamera(185, -18, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(9560, 3000)
    Sleep(1500)
    WaitChrThread(0xA, 2)

    def lambda_3530():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3530)
    Sleep(30)

    def lambda_3540():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3540)
    Sleep(30)

    def lambda_3550():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3550)
    Sleep(30)

    def lambda_3560():
        OP_93(0xC, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_3560)
    Sleep(30)

    def lambda_3570():
        OP_93(0xB, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_3570)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xB, 0)
    OP_6F(0x79)
    OP_68(-126020, 9000, -47760, 9000)
    MoveCamera(188, 23, 0, 9000)
    OP_6E(600, 9000)
    SetCameraDistance(24000, 9000)
    BeginChrThread(0x8, 0, 0, 5)
    Sleep(4000)
    Sound(942, 0, 100, 0)
    Sleep(2000)
    Sound(942, 0, 100, 0)
    Sleep(2000)
    Sleep(500)

    #C0103
    ChrTalk(
        0x101,
        "#00011F#12P#Nひ、飛行艇……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_6F(0x79)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    BeginChrThread(0x12, 1, 0, 24)
    Fade(500)
    OP_68(-132090, 5900, -41380, 0)
    MoveCamera(359, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Sleep(300)

    #C0104
    ChrTalk(
        0xB,
        (
            "#13804F#5P星杯騎士団で使っている\x01",
            "《メルカバ》という作戦艇です。\x02\x03",

            "#13802Fステルス機能に加えて、\x01",
            "光学迷彩機能を備えています。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "#10403F#5Pこれを使って極秘裏に\x01",
            "クロスベル領空に潜入する……\x02\x03",

            "#10400F心の準備はいいかい、ロイド？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0106
    ChrTalk(
        0x101,
        "#00007F#11P#4Sああ──もちろんだ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-167100, 6900, -14880, 0)
    MoveCamera(262, 6, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(52800, 0)
    Fade(500)
    SetCameraDistance(48800, 20000)
    OP_0D()
    StopSound(496, 1000, 30)
    StopSound(497, 1000, 30)
    Sleep(800)
    SetMessageWindowPos(0, 170, -1, -1)

    #A0107
    AnonymousTalk(
        0x101,
        (
            "#00003F#6P#N#30W（キーア……\x01",
            "  ……それにみんな……）\x02\x03",

            "#00013F#30W（どうか待っていてくれ……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(48800, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_24(0x3C2)
    OP_24(0x84)
    OP_24(0x1F1)
    OP_24(0x1F0)
    OP_29(0xAE, 0x1, 0x2)
    OP_29(0xAE, 0x4, 0x10)
    SubItemNumber(0x333, 1)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x22, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_25E end

    def Function_3_3945(): pass

    label("Function_3_3945")

    SetChrPos(0xFE, -250000, 0, -28000, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -225000, 0, -24000)
    OP_9F(0x1, -210000, 0, -20750)
    OP_9F(0x1, -193000, 0, -15500)
    OP_9F(0x1, -173000, 0, -10500)
    OP_9F(0x1, -130000, 0, -5220)
    OP_9F(0x2, 0xFE, 20000, 0x6)
    Return()

    # Function_3_3945 end

    def Function_4_39B1(): pass

    label("Function_4_39B1")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    OP_D3(0x101, 0xFF, "")
    Sound(809, 0, 40, 0)
    OP_9D(0xFE, 0xFFFDFF4E, 0xFA0, 0xFFFF92A0, 0xFA, 0x3E8)
    Sound(326, 0, 40, 0)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_4_39B1 end

    def Function_5_3A2E(): pass

    label("Function_5_3A2E")

    ClearMapObjFlags(0x2, 0x20)
    OP_79(0x2)
    OP_71(0x2, 0x1A4, 0x1AE, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0x1AE, 0x1D6, 0x0, 0x20)
    Return()

    # Function_5_3A2E end

    def Function_6_3A53(): pass

    label("Function_6_3A53")

    ClearMapObjFlags(0x2, 0x20)
    OP_79(0x2)
    OP_71(0x2, 0x1D6, 0x1E0, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    Return()

    # Function_6_3A53 end

    def Function_7_3A78(): pass

    label("Function_7_3A78")

    SetChrPos(0xFE, -137500, 4019, -45600, 30)
    OP_95(0xFE, -133390, 4000, -39760, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_7_3A78 end

    def Function_8_3AA5(): pass

    label("Function_8_3AA5")

    SetChrPos(0xFE, -138450, 3480, -47600, 90)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -137500, 4019, -45600)
    OP_9F(0x2, 0xFE, 2000, 0x2)
    OP_95(0xFE, -132640, 4000, -40680, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_8_3AA5 end

    def Function_9_3AF4(): pass

    label("Function_9_3AF4")

    SetChrPos(0xFE, -144000, -40, -56500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x0, 0x0)
    OP_9F(0x1, -144000, 600, -54730)
    OP_9F(0x1, -141500, 2350, -50000)
    OP_9F(0x1, -139000, 3300, -48000)
    OP_9F(0x1, -137500, 4019, -45600)
    OP_9F(0x2, 0xFE, 3000, 0x2)
    OP_95(0xFE, -134290, 4000, -38890, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_9_3AF4 end

    def Function_10_3B6D(): pass

    label("Function_10_3B6D")

    SetChrPos(0xFE, -144000, 600, -54730, 30)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -144000, 600, -54730)
    OP_9F(0x1, -141500, 2350, -50000)
    OP_9F(0x1, -139000, 3300, -48000)
    OP_9F(0x1, -137500, 4019, -45600)
    OP_9F(0x2, 0xFE, 3000, 0x2)
    OP_95(0xFE, -135320, 4000, -38530, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_10_3B6D end

    def Function_11_3BE6(): pass

    label("Function_11_3BE6")

    OP_71(0x2, 0x1D6, 0x1E0, 0x0, 0x0)
    SetChrPos(0x8, -131250, 4000, -31250, 215)
    OP_93(0x8, 0xD7, 0x1F4)
    OP_79(0x2)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    Return()

    # Function_11_3BE6 end

    def Function_12_3C1A(): pass

    label("Function_12_3C1A")

    OP_95(0xFE, -130300, 4000, -36350, 2000, 0x0)
    OP_93(0xFE, 0xD7, 0x1F4)
    Return()

    # Function_12_3C1A end

    def Function_13_3C36(): pass

    label("Function_13_3C36")

    Sleep(1000)
    OP_71(0x4, 0x65, 0xA0, 0x1, 0x20)
    BeginChrThread(0xE, 1, 0, 14)
    BeginChrThread(0x10, 1, 0, 14)
    Sleep(4000)
    Sound(202, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x4)
    OP_75(0x0, 0x1, 0x0)
    OP_75(0x0, 0x2, 0x1F4)
    Sleep(500)
    Sound(920, 0, 100, 0)
    OP_75(0x4, 0x1, 0x3E8)
    OP_75(0x6, 0x2, 0x1F4)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x10, 1)
    Return()

    # Function_13_3C36 end

    def Function_14_3C8E(): pass

    label("Function_14_3C8E")

    OP_96(0xFE, 0xFFFDECB6, 0x3E8, 0xFFFEE896, 0x1770, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0x1F4, 0xFFFEE896, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0x0, 0xFFFEE896, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFE0C, 0xFFFEE896, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFC18, 0xFFFEE896, 0x3E8, 0x1)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_14_3C8E end

    def Function_15_3CF9(): pass

    label("Function_15_3CF9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D87")
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFB50, 0xFFFEE896, 0x190, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFAEC, 0xFFFEE896, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFB50, 0xFFFEE896, 0xC8, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFCE0, 0xFFFEE896, 0x190, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFD44, 0xFFFEE896, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFCE0, 0xFFFEE896, 0xC8, 0x1)
    Jump("Function_15_3CF9")

    label("loc_3D87")

    Return()

    # Function_15_3CF9 end

    def Function_16_3D88(): pass

    label("Function_16_3D88")

    Sleep(2000)
    OP_71(0x5, 0x65, 0xA0, 0x1, 0x20)
    BeginChrThread(0xF, 1, 0, 17)
    BeginChrThread(0x11, 1, 0, 17)
    Sleep(4000)
    Sound(202, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x4)
    OP_75(0x1, 0x1, 0x0)
    OP_75(0x1, 0x2, 0x1F4)
    Sleep(500)
    Sound(920, 0, 100, 0)
    OP_75(0x5, 0x1, 0x3E8)
    OP_75(0x7, 0x2, 0x1F4)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x11, 1)
    Return()

    # Function_16_3D88 end

    def Function_17_3DE0(): pass

    label("Function_17_3DE0")

    OP_96(0xFE, 0xFFFE1E7A, 0x3E8, 0xFFFED388, 0x1770, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0x1F4, 0xFFFED388, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0x0, 0xFFFED388, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFE0C, 0xFFFED388, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFC18, 0xFFFED388, 0x3E8, 0x1)
    BeginChrThread(0xFE, 3, 0, 18)
    Return()

    # Function_17_3DE0 end

    def Function_18_3E4B(): pass

    label("Function_18_3E4B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3ED9")
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFB50, 0xFFFED388, 0x190, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFAEC, 0xFFFED388, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFB50, 0xFFFED388, 0xC8, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFCE0, 0xFFFED388, 0x190, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFD44, 0xFFFED388, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFCE0, 0xFFFED388, 0xC8, 0x1)
    Jump("Function_18_3E4B")

    label("loc_3ED9")

    Return()

    # Function_18_3E4B end

    def Function_19_3EDA(): pass

    label("Function_19_3EDA")

    Sleep(1000)
    OP_95(0xFE, -130310, 4100, -40610, 2000, 0x0)
    Return()

    # Function_19_3EDA end

    def Function_20_3EF2(): pass

    label("Function_20_3EF2")

    Sound(962, 2, 10, 0)
    Sleep(400)
    OP_25(0x3C2, 0xF)
    Sleep(400)
    OP_25(0x3C2, 0x14)
    Sleep(400)
    OP_25(0x3C2, 0x19)
    Sleep(400)
    OP_25(0x3C2, 0x1E)
    Sleep(400)
    OP_25(0x3C2, 0x23)
    Sleep(400)
    OP_25(0x3C2, 0x28)
    Sleep(400)
    OP_25(0x3C2, 0x2D)
    Sleep(400)
    OP_25(0x3C2, 0x32)
    Return()

    # Function_20_3EF2 end

    def Function_21_3F31(): pass

    label("Function_21_3F31")

    OP_25(0x84, 0x5F)
    Sleep(200)
    OP_25(0x84, 0x5A)
    Sleep(200)
    OP_25(0x84, 0x55)
    Sleep(200)
    OP_25(0x84, 0x50)
    Sleep(200)
    OP_25(0x84, 0x4B)
    Sleep(200)
    OP_25(0x84, 0x46)
    Sleep(200)
    OP_25(0x84, 0x41)
    Sleep(200)
    OP_25(0x84, 0x3C)
    Sleep(200)
    OP_25(0x84, 0x32)
    Sleep(200)
    OP_25(0x84, 0x28)
    Sleep(200)
    OP_25(0x84, 0x1E)
    Return()

    # Function_21_3F31 end

    def Function_22_3F7C(): pass

    label("Function_22_3F7C")

    Sound(497, 2, 0, 0)
    Sound(496, 2, 0, 0)
    Sleep(300)
    OP_25(0x1F1, 0x5)
    OP_25(0x1F0, 0x5)
    Sleep(300)
    OP_25(0x1F1, 0xA)
    OP_25(0x1F0, 0xA)
    Sleep(300)
    OP_25(0x1F1, 0xF)
    OP_25(0x1F0, 0xF)
    Sleep(300)
    OP_25(0x1F1, 0x14)
    OP_25(0x1F0, 0x14)
    Sleep(300)
    OP_25(0x1F1, 0x19)
    OP_25(0x1F0, 0x19)
    Sleep(300)
    OP_25(0x1F1, 0x1E)
    OP_25(0x1F0, 0x1E)
    Sleep(300)
    OP_25(0x1F1, 0x23)
    OP_25(0x1F0, 0x23)
    Sleep(300)
    OP_25(0x1F1, 0x28)
    OP_25(0x1F0, 0x28)
    Sleep(300)
    OP_25(0x1F1, 0x2D)
    OP_25(0x1F0, 0x2D)
    Sleep(300)
    OP_25(0x1F1, 0x32)
    OP_25(0x1F0, 0x32)
    Return()

    # Function_22_3F7C end

    def Function_23_3FF7(): pass

    label("Function_23_3FF7")

    OP_25(0x1F1, 0x37)
    OP_25(0x1F0, 0x37)
    Sleep(200)
    OP_25(0x1F1, 0x3C)
    OP_25(0x1F0, 0x3C)
    Sleep(200)
    OP_25(0x1F1, 0x41)
    OP_25(0x1F0, 0x41)
    Sleep(200)
    OP_25(0x1F1, 0x46)
    OP_25(0x1F0, 0x46)
    Return()

    # Function_23_3FF7 end

    def Function_24_4021(): pass

    label("Function_24_4021")

    OP_25(0x1F1, 0x41)
    OP_25(0x1F0, 0x41)
    Sleep(200)
    OP_25(0x1F1, 0x3C)
    OP_25(0x1F0, 0x3C)
    Sleep(200)
    OP_25(0x1F1, 0x37)
    OP_25(0x1F0, 0x37)
    Sleep(200)
    OP_25(0x1F1, 0x32)
    OP_25(0x1F0, 0x32)
    Sleep(200)
    OP_25(0x1F1, 0x2D)
    OP_25(0x1F0, 0x2D)
    Sleep(200)
    OP_25(0x1F1, 0x28)
    OP_25(0x1F0, 0x28)
    Return()

    # Function_24_4021 end

    def Function_25_4061(): pass

    label("Function_25_4061")

    Sleep(500)
    SetChrChipByIndex(0x9, 0x23)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x1000)
    Sleep(120)
    SetChrSubChip(0x9, 0x0)
    Sleep(120)
    SetChrSubChip(0x9, 0x1)
    Sound(802, 0, 100, 0)
    Sleep(300)
    Return()

    # Function_25_4061 end

    def Function_26_408A(): pass

    label("Function_26_408A")

    SetChrChipByIndex(0xA, 0x24)
    Fade(250)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_26_408A end

    def Function_27_40A2(): pass

    label("Function_27_40A2")

    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    Return()

    # Function_27_40A2 end

    SaveToFile()

Try(main)
