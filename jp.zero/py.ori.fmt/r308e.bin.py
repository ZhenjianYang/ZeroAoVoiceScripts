from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r308e.bin",                # FileName
        "r308e",                    # MapName
        "r308e",                    # Location
        0x0065,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -74000, 0, -2000, 0, 0, 1, 101, 0, 2, 0, 3],
    )

    BuildStringList((
        "r308e",                  # 0
        "キーア",                 # 1
        "セルゲイ課長",           # 2
        "ツァイト",               # 3
        "ダドリー捜査官",         # 4
        "アリオス",               # 5
        "ノエル曹長",             # 6
        "ソーニャ副司令",         # 7
        "レン",                   # 8
        "グレイス",               # 9
        "レインズ",               # 10
        "車１",                   # 11
        "車２",                   # 12
        "車３",                   # 13
        "車４",                   # 14
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_2D8",          # 00, 0
        "Function_1_2FA",          # 01, 1
        "Function_2_317",          # 02, 2
        "Function_3_33B",          # 03, 3
        "Function_4_33C",          # 04, 4
        "Function_5_1C5F",         # 05, 5
        "Function_6_1C7E",         # 06, 6
        "Function_7_1CA4",         # 07, 7
        "Function_8_1CCA",         # 08, 8
        "Function_9_1CF0",         # 09, 9
        "Function_10_1D38",        # 0A, 10
        "Function_11_1D8E",        # 0B, 11
        "Function_12_1DAD",        # 0C, 12
        "Function_13_1DDA",        # 0D, 13
        "Function_14_1E00",        # 0E, 14
        "Function_15_1E26",        # 0F, 15
        "Function_16_1E4C",        # 10, 16
    ))


    def Function_0_2D8(): pass

    label("Function_0_2D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F9")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(832, 0, 100, 0)
    Jump("Function_0_2D8")

    label("loc_2F9")

    Return()

    # Function_0_2D8 end

    def Function_1_2FA(): pass

    label("Function_1_2FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_316")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x2, 0x1)
    Jump("Function_1_2FA")

    label("loc_316")

    Return()

    # Function_1_2FA end

    def Function_2_317(): pass

    label("Function_2_317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_32B")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_33A")

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_33A")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 16)

    label("loc_33A")

    Return()

    # Function_2_317 end

    def Function_3_33B(): pass

    label("Function_3_33B")

    Return()

    # Function_3_33B end

    def Function_4_33C(): pass

    label("Function_4_33C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("apl/ch50520.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    LoadChrToIndex("chr/ch00900.itc", 0x21)
    LoadChrToIndex("chr/ch02400.itc", 0x22)
    LoadChrToIndex("chr/ch00800.itc", 0x23)
    LoadChrToIndex("chr/ch05700.itc", 0x24)
    LoadChrToIndex("chr/ch09500.itc", 0x25)
    LoadChrToIndex("chr/ch06000.itc", 0x26)
    LoadChrToIndex("apl/ch50378.itc", 0x27)
    LoadChrToIndex("chr/ch08201.itc", 0x28)
    LoadChrToIndex("apl/ch50380.itc", 0x29)
    LoadChrToIndex("chr/ch02751.itc", 0x2A)
    LoadChrToIndex("apl/ch50314.itc", 0x2B)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis105.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01102.itp")
    OP_68(48100, 22100, -2000, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 56000, 20000, -2000, 270)
    SetChrPos(0x103, 57100, 20000, -2900, 270)
    SetChrPos(0x102, 57100, 20000, -1100, 270)
    SetChrPos(0x104, 58200, 20000, -2000, 270)
    SetChrPos(0x107, 32400, 20000, -1600, 270)
    SetChrPos(0x108, 32400, 20000, -3400, 270)
    SetChrFlags(0x107, 0x8)
    SetChrFlags(0x108, 0x8)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 32400, 20000, -2500, 270)
    SetChrFlags(0xF, 0x8)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    OP_90(0x8, 6300, 11700, -2000, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x8000)
    OP_90(0x9, 6600, 11800, -1400, 90)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x8000)
    OP_90(0xA, 5900, 11450, 400, 90)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    OP_90(0xB, 6200, 11650, -2200, 90)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    OP_90(0xC, 4100, 10600, -300, 90)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    OP_90(0xD, 5400, 11250, -4200, 90)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    OP_90(0xE, 5400, 11250, -3400, 90)
    SetChrChipByIndex(0x10, 0x26)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x8000)
    OP_90(0x10, 8100, 12540, -2000, 90)
    SetChrChipByIndex(0x11, 0x27)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    OP_90(0x11, 7600, 12320, -1100, 90)

    def lambda_621():
        OP_96(0xFE, 0xB798, 0x4E20, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_621)
    Sleep(50)

    def lambda_63E():
        OP_96(0xFE, 0xBBE4, 0x4E20, 0xFFFFFBB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63E)
    Sleep(50)

    def lambda_65B():
        OP_96(0xFE, 0xBBE4, 0x4E20, 0xFFFFF4AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_65B)
    Sleep(50)

    def lambda_678():
        OP_96(0xFE, 0xC030, 0x4E20, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_678)
    Sound(829, 0, 100, 0)
    OP_68(48100, 21100, -2000, 4500)
    MoveCamera(30, 17, 0, 4500)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x41)

    #C0001
    ChrTalk(
        0x101,
        "#11P#0002Fあ……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        "#0102F#11P……朝陽が……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        "#0202F#11P……キレイです……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x104,
        (
            "#0304F#11Pああ……\x01",
            "それに暖かいな……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 36150, 21000, -2410, 100)
    #Sound(2042, 255, 90, 0)    #voice#KeA

    #N0005
    NpcTalk(
        0x8,
        "少女の声",
        "#2P#24Aロイド────っ！\x02",
    )
    #Auto

    Sleep(1800)
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
    Sleep(1000)
    ClearChrFlags(0x8, 0x4)

    #C0006
    ChrTalk(
        0x101,
        "#0005F#11Pこの声……！？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x103,
        "#0205F#11Pまさか……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(11300, 15100, -2000, 0)
    MoveCamera(35, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 32000, 20000, -2000, 270)
    SetChrPos(0x102, 32400, 20000, -3100, 270)
    SetChrPos(0x103, 32200, 20000, -400, 270)
    SetChrPos(0x104, 33600, 20000, -600, 270)
    OP_90(0x8, 6300, 11700, -2000, 90)
    BeginChrThread(0x8, 3, 0, 9)
    BeginChrThread(0x101, 3, 0, 5)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 6)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 7)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 8)
    Sleep(900)
    OP_68(19330, 17100, -2040, 1500)
    MoveCamera(58, 20, 0, 1500)
    SetCameraDistance(18000, 1500)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    BeginChrThread(0xA, 3, 0, 10)
    Sleep(50)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    BeginChrThread(0x9, 3, 0, 12)
    Sleep(50)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    BeginChrThread(0xB, 3, 0, 11)
    Sleep(400)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    BeginChrThread(0xE, 3, 0, 14)
    Sleep(50)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    BeginChrThread(0xD, 3, 0, 15)
    Sleep(400)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    BeginChrThread(0xC, 3, 0, 13)
    Sleep(500)
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x108, 0x8)
    ClearChrFlags(0xF, 0x8)

    def lambda_9A9():
        OP_96(0xFE, 0x5780, 0x3E80, 0xFFFFF9C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9A9)
    Sleep(100)

    def lambda_9C6():
        OP_96(0xFE, 0x5780, 0x3E80, 0xFFFFF2B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_9C6)
    Sleep(300)

    def lambda_9E3():
        OP_96(0xFE, 0x5780, 0x3E80, 0xFFFFF63C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9E3)
    WaitChrThread(0x8, 3)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 70, 0)
    OP_6F(0x79)
    SetCameraDistance(17000, 80000)

    #C0008
    ChrTalk(
        0x101,
        "#11P#0011Fキーア……！\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        "#6P#1114F……～～～っ～～～～！！！\x02",
    )

    CloseMessageWindow()
    Sound(910, 0, 100, 0)

    def lambda_A63():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A63)

    def lambda_A7C():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A7C)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x8, 2)
    Sound(804, 0, 70, 0)
    Sleep(300)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0010
    AnonymousTalk(
        0x8,
        (
            "よ、よかったぁ……！\x02\x03",

            "ロイドも、エリィも……\x01",
            "ティオもランディも無事で……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    WaitChrThread(0xA, 3)

    #C0011
    ChrTalk(
        0xA,
        "#1200Fグルル……ウォン！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#0102F#11Pどうしてキーアちゃんが……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#5P#0309Fはは……\x01",
            "しかもえらい大所帯じゃねえか。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 3)

    #C0014
    ChrTalk(
        0xC,
        (
            "#6P#1404F先ほど、市街に展開していた\x01",
            "警備隊員たちが全員気絶した。\x02\x03",

            "#1402Fそれで取り急ぎ、彼女を連れて\x01",
            "こちらに出向いたというわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xB,
        (
            "#6P#0606Fまったく、連れて行けと\x01",
            "ダダをこねられて困ったぞ。\x02\x03",

            "#0601Fフン、これだから支援課は……\x01",
            "躾くらいきちんとしておけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "#6P#1004Fクク、そう言いながら\x01",
            "わざわざ連れて来てやるあたりが\x01",
            "お前らしいがな……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 500)
    Sleep(300)

    #C0017
    ChrTalk(
        0xB,
        "#12P#0605Fセ、セルゲイさん……！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#11P#0009Fはは……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    OP_96(0x8, 0x4B64, 0x3E80, 0xFFFFF830, 0x3E8, 0x0)
    Sleep(300)
    TurnDirection(0x101, 0xE, 500)
    Sleep(150)

    #C0019
    ChrTalk(
        0x101,
        "#5P#0002F副司令に、ノエル曹長も……\x02",
    )

    CloseMessageWindow()

    def lambda_DE1():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DE1)
    Sleep(50)

    def lambda_DF1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_DF1)
    Sleep(300)

    #C0020
    ChrTalk(
        0xD,
        "#12P#0502F皆さん、お疲れさまです！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "#6P#2004Fこちらの部隊もようやく\x01",
            "身動きが取れるようになったわ。\x02\x03",

            "#2002Fそれで様子を見に来たんだけど……\x01",
            "とりあえず、危機は去ったのね？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#5P#0004Fはい……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0204F#5P不気味な魔獣たちも全て\x01",
            "姿を消してしまいましたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#5P#0300Fおかげで全員、\x01",
            "連れて帰って来られたぜ。\x02\x03",

            "#0306Fま、マフィアたちは拘束して、\x01",
            "地下に置いたままだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#0108F#11P……むしろこれからの方が\x01",
            "大変かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xE,
        (
            "#6P#2006Fそうね……市民への説明と\x01",
            "諸外国への対応……\x02\x03",

            "#2001F操られた警備隊員たちへの\x01",
            "ケアもきちんとしないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xD,
        (
            "#12P#0501Fマフィアたちも一通り、\x01",
            "拘束する必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xB,
        (
            "#6P#0603Fそして今回の事件に関する、\x01",
            "一連の証拠集め……\x02\x03",

            "#0601F一ヶ月は大忙しだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        (
            "#6P#1402Fフフ……\x01",
            "ギルドも協力させてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        "#6P#0604F……感謝する。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        "#0202F#5P……ふふっ……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#5P#0304F確かに死ぬほど\x01",
            "忙しくなりそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#0109F#11Pでも……何だか全てが\x01",
            "良い方向に行きそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#5P#0002F……ああ………\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        "#6P#1109Fうんっ！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        "#1200Fウォン……！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#6P#1002Fクク……\x02\x03",

            "#1003F──ロイド、エリィ、\x01",
            "ティオ、ランディ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_128F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_128F)
    Sleep(50)

    def lambda_129F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_129F)
    Sleep(50)

    def lambda_12AF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12AF)
    Sleep(50)

    def lambda_12BF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12BF)
    Sleep(300)

    #C0038
    ChrTalk(
        0x9,
        (
            "#6P#1003F詳しい報告はゆっくりと\x01",
            "聞かせてもらうとして……\x02\x03",

            "#1002Fとりあえず──\x01",
            "ケリは付けてきたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#11P#0005Fあ……\x02",
    )

    CloseMessageWindow()

    def lambda_134E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_134E)
    Sleep(100)

    def lambda_135E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_135E)
    Sleep(1300)

    def lambda_136E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_136E)
    Sleep(100)

    def lambda_137E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_137E)
    Sleep(50)

    def lambda_138E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_138E)
    Sleep(1500)

    def lambda_139E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_139E)
    Sleep(50)

    def lambda_13AE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_13AE)
    Sleep(50)

    def lambda_13BE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_13BE)
    Sleep(50)

    def lambda_13CE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_13CE)
    WaitChrThread(0x101, 2)
    Sleep(300)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロイドたち")
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #A0040
    AnonymousTalk(
        0xFF,
        "#5Sはい……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0041
    ChrTalk(
        0x9,
        (
            "#6P#1004Fクク……上出来だ。\x02\x03",

            "これでどうやら……\x01",
            "お前たちを一人前として\x01",
            "認めてやる事が出来そうだ。\x02\x03",

            "#1002F……ガイのやつも喜んでるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#11P#0005F課長……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xC,
        "#3P#1402F………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)

    #N0044
    NpcTalk(
        0x10,
        "女性の声",
        (
            "はいは～い！\x01",
            "ちょっとどいてどいて～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetCameraDistance(18000, 2000)
    OP_68(17710, 17100, -1790, 2000)
    MoveCamera(50, 20, 0, 2000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)

    def lambda_15B9():
        OP_96(0xFE, 0x37DC, 0x3D2C, 0xFFFFF830, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_15B9)
    Sleep(100)

    def lambda_15D6():
        OP_96(0xFE, 0x35E8, 0x3C46, 0xFFFFFBB4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_15D6)

    def lambda_15F0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_15F0)
    Sleep(50)

    def lambda_1600():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1600)
    Sleep(50)

    def lambda_1610():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1610)
    Sleep(50)

    def lambda_1620():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1620)
    Sleep(50)

    def lambda_1630():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1630)
    Sleep(50)

    def lambda_1640():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1640)
    Sleep(50)

    def lambda_1650():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1650)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    OP_6F(0x41)

    #C0045
    ChrTalk(
        0x101,
        "#0011F#11Pグレイスさん！？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0105F#11Pこ、こんな所まで……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x10,
        (
            "#2109F#6P#Nこんな美味しいネタを\x01",
            "見逃すわけにいきますかって！\x02\x03",

            "#2102F何はともあれ、まずは一枚\x01",
            "パシャリと行かせてもらうわよ～！\x02\x03",

            "ほら、全員入った入った。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0048
    ChrTalk(
        0x9,
        "#1006F#11Pやれやれ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0049
    ChrTalk(
        0x8,
        "#5P#1110F写真、とってもらうの～？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0002F#11Pああ……\x01",
            "ニッコリ笑うんだぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "#5P#1109Fうんっ！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#11P#0202F#Nツァイト、入りましょう。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0xA, 0x103, 500)
    Sleep(150)

    #C0053
    ChrTalk(
        0xA,
        "#5P#1200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0054
    ChrTalk(
        0x107,
        "#0802F#11P#Nえっと、あたしたちは……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0055
    ChrTalk(
        0x108,
        (
            "#0904F#11P#Nさすがに遠慮した方が\x01",
            "よさそうだね……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x104, 0x107, 500)

    #C0056
    ChrTalk(
        0x104,
        (
            "#6P#0301Fおらおら。\x01",
            "遠慮すんなっつーの。\x02\x03",

            "#0309F嬢ちゃんも入ってけよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xF,
        (
            "#3300F#11P#Nふふっ……\x01",
            "それじゃあ遠慮なく。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0058
    ChrTalk(
        0xB,
        "#11P#0606Fまったく……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xC,
        (
            "#1404F#5Pフフ、たまには\x01",
            "こういうのも悪くなかろう？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(300)

    #C0060
    ChrTalk(
        0xD,
        (
            "#12P#0509Fほら、副司令も\x01",
            "課長さんの横あたりに！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xE,
        (
            "#11P#2002Fはいはい……でもこれ、\x01",
            "どんな絵面になるのかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(24300, 17100, -2000, 0)
    MoveCamera(90, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_90(0x8, 23400, 16000, -2000, 270)
    OP_90(0x101, 24300, 16140, -2100, 270)
    OP_90(0x102, 24000, 16000, -2700, 270)
    OP_90(0x103, 23800, 16000, -1300, 270)
    OP_90(0x104, 24450, 16219, -1150, 270)
    OP_90(0x9, 23750, 16000, -3550, 270)
    OP_90(0xA, 23400, 16000, -300, 225)
    OP_90(0x107, 25200, 16600, -2300, 270)
    OP_90(0x108, 25200, 16600, -3500, 270)
    OP_90(0xF, 25300, 16650, -2900, 270)
    OP_90(0xB, 24900, 16450, -450, 270)
    OP_90(0xC, 24900, 16450, 550, 270)
    OP_90(0xD, 24500, 16260, -4950, 270)
    OP_90(0xE, 24500, 16260, -4250, 270)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x11, 19200, 16000, -2000, 90)
    SetChrPos(0x10, 18800, 16000, -3000, 90)
    FadeToBright(1000, 0)
    OP_68(22300, 17100, -2000, 4000)
    SetCameraDistance(18500, 4000)
    OP_0D()
    OP_6F(0x11)

    #C0062
    ChrTalk(
        0x10,
        (
            "#2102F#6P#Nさあ、行きますよー。\x02\x03",

            "#2109F──はい、チーズ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(817, 0, 100, 0)
    FadeToDark(0, -1, 0)
    FadeToDark(100, 16777215, -1)
    OP_0D()
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    Sleep(1000)
    FadeToBright(2000, 16777215)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(3000)
    OP_C9(0x0, 0x3, 0xFFCCAA77, 0x7D0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x0, 0x3, 0xCCAA77, 0xBB8, 0x0)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    FadeToBright(0, -1)
    OP_C7(0x1, 0x10)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CA(0x1, 0xFF, 0x0)
    OP_29(0x4F, 0x4, 0x10)
    OP_29(0x4F, 0x4, 0x20)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    OP_DE(0x80, 0x0)
    Call(0, 16)
    Return()

    # Function_4_33C end

    def Function_5_1C5F(): pass

    label("Function_5_1C5F")


    def lambda_1C64():
        OP_96(0xFE, 0x4E20, 0x3E80, 0xFFFFF830, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C64)
    WaitChrThread(0x101, 1)
    Return()

    # Function_5_1C5F end

    def Function_6_1C7E(): pass

    label("Function_6_1C7E")


    def lambda_1C83():
        OP_96(0xFE, 0x4FB0, 0x3E80, 0xFFFFF3E4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C83)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x13B, 0x1F4)
    Return()

    # Function_6_1C7E end

    def Function_7_1CA4(): pass

    label("Function_7_1CA4")


    def lambda_1CA9():
        OP_96(0xFE, 0x4EE8, 0x3E80, 0xFFFFFE70, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CA9)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0xE1, 0x1F4)
    Return()

    # Function_7_1CA4 end

    def Function_8_1CCA(): pass

    label("Function_8_1CCA")


    def lambda_1CCF():
        OP_96(0xFE, 0x5460, 0x3E80, 0xFFFFFDA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CCF)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0xE1, 0x1F4)
    Return()

    # Function_8_1CCA end

    def Function_9_1CF0(): pass

    label("Function_9_1CF0")

    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)

    def lambda_1CFD():
        OP_96(0xFE, 0x4C90, 0x3E80, 0xFFFFF830, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1CFD)
    WaitChrThread(0x8, 1)

    def lambda_1D1B():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D1B)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_9_1CF0 end

    def Function_10_1D38(): pass

    label("Function_10_1D38")

    SetChrChipByIndex(0xA, 0x2A)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 0)

    def lambda_1D61():
        OP_96(0xFE, 0x4844, 0x3E80, 0x2BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D61)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    OP_93(0xA, 0x87, 0x1F4)
    Return()

    # Function_10_1D38 end

    def Function_11_1D8E(): pass

    label("Function_11_1D8E")


    def lambda_1D93():
        OP_96(0xFE, 0x4330, 0x3E80, 0xFFFFF768, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1D93)
    WaitChrThread(0xB, 1)
    Return()

    # Function_11_1D8E end

    def Function_12_1DAD(): pass

    label("Function_12_1DAD")

    BeginChrThread(0x9, 0, 0, 1)

    def lambda_1DB8():
        OP_96(0xFE, 0x44C0, 0x3E80, 0xFFFFFA88, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1DB8)
    WaitChrThread(0x9, 1)
    EndChrThread(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_12_1DAD end

    def Function_13_1DDA(): pass

    label("Function_13_1DDA")


    def lambda_1DDF():
        OP_96(0xFE, 0x40D8, 0x3E80, 0xFFFFFED4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1DDF)
    WaitChrThread(0xC, 1)
    OP_93(0xC, 0x87, 0x1F4)
    Return()

    # Function_13_1DDA end

    def Function_14_1E00(): pass

    label("Function_14_1E00")


    def lambda_1E05():
        OP_96(0xFE, 0x43F8, 0x3E80, 0xFFFFF2B8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E05)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x2D, 0x1F4)
    Return()

    # Function_14_1E00 end

    def Function_15_1E26(): pass

    label("Function_15_1E26")


    def lambda_1E2B():
        OP_96(0xFE, 0x43F8, 0x3E80, 0xFFFFEF98, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1E2B)
    WaitChrThread(0xD, 1)
    OP_93(0xD, 0x2D, 0x1F4)
    Return()

    # Function_15_1E26 end

    def Function_16_1E4C(): pass

    label("Function_16_1E4C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_1E4C end

    SaveToFile()

Try(main)
