from ZeroScenarioHelper import *

def main():
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
        "琪雅",                   # 1
        "赛尔盖科长",             # 2
        "蔡特",                   # 3
        "达德利搜查官",           # 4
        "亚里欧斯",               # 5
        "诺艾尔上士",             # 6
        "索妮亚副司令",           # 7
        "玲",                     # 8
        "格蕾丝",                 # 9
        "雷因兹",                 # 10
        "车１",                   # 11
        "车２",                   # 12
        "车３",                   # 13
        "车４",                   # 14
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
        "Function_5_1AEB",         # 05, 5
        "Function_6_1B0A",         # 06, 6
        "Function_7_1B30",         # 07, 7
        "Function_8_1B56",         # 08, 8
        "Function_9_1B7C",         # 09, 9
        "Function_10_1BC4",        # 0A, 10
        "Function_11_1C1A",        # 0B, 11
        "Function_12_1C39",        # 0C, 12
        "Function_13_1C66",        # 0D, 13
        "Function_14_1C8C",        # 0E, 14
        "Function_15_1CB2",        # 0F, 15
        "Function_16_1CD8",        # 10, 16
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
        "#11P#0002F啊……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        "#0102F#11P……朝阳升起了……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        "#0202F#11P……真漂亮……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x104,
        (
            "#0304F#11P是啊……\x01",
            "而且好温暖啊……\x02",
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
        "少女的声音",
        "#2P#24A罗伊德────！\x02",
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
        "#0005F#11P这个声音……！？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x103,
        "#0205F#11P难道是……！\x02",
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
        "#11P#0011F琪雅……！\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        "#6P#1114F……～～～唔～～～～！！！\x02",
    )

    CloseMessageWindow()
    Sound(910, 0, 100, 0)

    def lambda_A61():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A61)

    def lambda_A7A():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A7A)
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
            "太、太好了……！\x02\x03",

            "罗伊德、艾莉……\x01",
            "还有缇欧和兰迪，你们都没事……！\x02",
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
        "#1200F呜噜噜噜……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#0102F#11P为什么小琪雅会……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#5P#0309F哈哈……\x01",
            "而且还带了这么多人来。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 3)

    #C0014
    ChrTalk(
        0xC,
        (
            "#6P#1404F之前在市内发起袭击的\x01",
            "警备队员们已经全部失去意识了。\x02\x03",

            "#1402F然后我们就急忙带着她\x01",
            "赶来这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xB,
        (
            "#6P#0606F真是的，她一直在求我们\x01",
            "带上她，真让人头疼。\x02\x03",

            "#0601F哼，所以我才受不了你们支援科的人……\x01",
            "至少也该好好教会她什么叫做涵养吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "#6P#1004F呵呵，嘴上这么说，\x01",
            "但特意带她来的\x01",
            "好像就是你啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 500)
    Sleep(300)

    #C0017
    ChrTalk(
        0xB,
        "#12P#0605F赛、赛尔盖长官……！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#11P#0009F哈哈……\x02",
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
        "#5P#0002F副司令，还有诺艾尔上士也……\x02",
    )

    CloseMessageWindow()

    def lambda_D9B():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D9B)
    Sleep(50)

    def lambda_DAB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_DAB)
    Sleep(300)

    #C0020
    ChrTalk(
        0xD,
        "#12P#0502F各位，辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "#6P#2004F我们这边的部队也终于\x01",
            "能抽出身来了。\x02\x03",

            "#2002F然后就来看看情况如何了……\x01",
            "总之，危机已经过去了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#5P#0004F是的……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0204F#5P那些诡异的魔兽也\x01",
            "全部都消失了……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#5P#0300F多亏它们消失了，\x01",
            "我们才能把全体失踪者顺利带出来。\x02\x03",

            "#0306F不过，那些黑手党\x01",
            "还被绑着丢在地下呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#0108F#11P……不如说，今后的措施\x01",
            "才比较麻烦吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xE,
        (
            "#6P#2006F是啊……面向市民的解释，\x01",
            "以及对周边诸国的应对……\x02\x03",

            "#2001F还必须要努力安抚\x01",
            "那些曾被操纵的警备队员……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xD,
        (
            "#12P#0501F而且，似乎也有必要对\x01",
            "那些黑手党实施拘禁呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xB,
        (
            "#6P#0603F以及收集关于此次事件的\x01",
            "一系列证据……\x02\x03",

            "#0601F看来要忙上一个月吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        (
            "#6P#1402F呵呵……\x01",
            "游击士协会也会帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        "#6P#0604F……十分感谢。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        "#0202F#5P……呵呵……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#5P#0304F看来确实会\x01",
            "忙到死吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#0109F#11P但是……总觉得一切\x01",
            "都会朝好的方向发展呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#5P#0002F……是啊………\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        "#6P#1109F嗯！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        "#1200F嗷……！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#6P#1002F呵呵……\x02\x03",

            "#1003F──罗伊德、艾莉、\x01",
            "缇欧、兰迪。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_11C1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11C1)
    Sleep(50)

    def lambda_11D1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11D1)
    Sleep(50)

    def lambda_11E1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_11E1)
    Sleep(50)

    def lambda_11F1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11F1)
    Sleep(300)

    #C0038
    ChrTalk(
        0x9,
        (
            "#6P#1003F详细的报告\x01",
            "就以后再听……\x02\x03",

            "#1002F总之──\x01",
            "事件已经解决了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#11P#0005F啊……\x02",
    )

    CloseMessageWindow()

    def lambda_1262():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1262)
    Sleep(100)

    def lambda_1272():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1272)
    Sleep(1300)

    def lambda_1282():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1282)
    Sleep(100)

    def lambda_1292():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1292)
    Sleep(50)

    def lambda_12A2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12A2)
    Sleep(1500)

    def lambda_12B2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12B2)
    Sleep(50)

    def lambda_12C2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12C2)
    Sleep(50)

    def lambda_12D2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12D2)
    Sleep(50)

    def lambda_12E2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12E2)
    WaitChrThread(0x101, 2)
    Sleep(300)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伊德一行")
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #A0040
    AnonymousTalk(
        0xFF,
        "#5S是的……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0041
    ChrTalk(
        0x9,
        (
            "#6P#1004F呵呵……干得漂亮。\x02\x03",

            "这样一来，我应该……\x01",
            "就能承认你们已经\x01",
            "变得独当一面了呢。\x02\x03",

            "#1002F……盖伊那小子也会高兴的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#11P#0005F科长……\x02",
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
        "女性的声音",
        (
            "不好意～思！\x01",
            "麻烦让一下让一下～！\x02",
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

    def lambda_14BB():
        OP_96(0xFE, 0x37DC, 0x3D2C, 0xFFFFF830, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_14BB)
    Sleep(100)

    def lambda_14D8():
        OP_96(0xFE, 0x35E8, 0x3C46, 0xFFFFFBB4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_14D8)

    def lambda_14F2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14F2)
    Sleep(50)

    def lambda_1502():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1502)
    Sleep(50)

    def lambda_1512():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1512)
    Sleep(50)

    def lambda_1522():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1522)
    Sleep(50)

    def lambda_1532():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1532)
    Sleep(50)

    def lambda_1542():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1542)
    Sleep(50)

    def lambda_1552():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1552)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    OP_6F(0x41)

    #C0045
    ChrTalk(
        0x101,
        "#0011F#11P格蕾丝小姐！？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0105F#11P居、居然跟到这种地方来了……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x10,
        (
            "#2109F#6P#N我怎么会错过\x01",
            "这么精彩的新闻呢！\x02\x03",

            "#2102F不管怎么说，先让我\x01",
            "咔嚓拍一张啦～！\x02\x03",

            "快点，全员集合集合。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0048
    ChrTalk(
        0x9,
        "#1006F#11P哎呀哎呀……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0049
    ChrTalk(
        0x8,
        "#5P#1110F要拍照吗～？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0002F#11P是啊……\x01",
            "要记着微笑哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "#5P#1109F嗯！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#11P#0202F#N蔡特，我们也过去照相吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0xA, 0x103, 500)
    Sleep(150)

    #C0053
    ChrTalk(
        0xA,
        "#5P#1200F呜噜噜……嗷。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0054
    ChrTalk(
        0x107,
        "#0802F#11P#N那个，我们就……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0055
    ChrTalk(
        0x108,
        (
            "#0904F#11P#N还是回避一下\x01",
            "比较好呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x104, 0x107, 500)

    #C0056
    ChrTalk(
        0x104,
        (
            "#6P#0301F喂喂，\x01",
            "别客气啦。\x02\x03",

            "#0309F这位小姑娘也过来拍吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xF,
        (
            "#3300F#11P#N呵呵……\x01",
            "那么我就不客气了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0058
    ChrTalk(
        0xB,
        "#11P#0606F真是的……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xC,
        (
            "#1404F#5P呵呵，像这种事，\x01",
            "偶尔来一次也不坏吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(300)

    #C0060
    ChrTalk(
        0xD,
        (
            "#12P#0509F我说，副司令\x01",
            "也去站到科长先生的旁边吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xE,
        (
            "#11P#2002F好的好的……不过，\x01",
            "这照片会拍成什么样呢？\x02",
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
            "#2102F#6P#N好，我要拍了哦～\x02\x03",

            "#2109F──各位，说茄子！\x02",
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

    def Function_5_1AEB(): pass

    label("Function_5_1AEB")


    def lambda_1AF0():
        OP_96(0xFE, 0x4E20, 0x3E80, 0xFFFFF830, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AF0)
    WaitChrThread(0x101, 1)
    Return()

    # Function_5_1AEB end

    def Function_6_1B0A(): pass

    label("Function_6_1B0A")


    def lambda_1B0F():
        OP_96(0xFE, 0x4FB0, 0x3E80, 0xFFFFF3E4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B0F)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x13B, 0x1F4)
    Return()

    # Function_6_1B0A end

    def Function_7_1B30(): pass

    label("Function_7_1B30")


    def lambda_1B35():
        OP_96(0xFE, 0x4EE8, 0x3E80, 0xFFFFFE70, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B35)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0xE1, 0x1F4)
    Return()

    # Function_7_1B30 end

    def Function_8_1B56(): pass

    label("Function_8_1B56")


    def lambda_1B5B():
        OP_96(0xFE, 0x5460, 0x3E80, 0xFFFFFDA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B5B)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0xE1, 0x1F4)
    Return()

    # Function_8_1B56 end

    def Function_9_1B7C(): pass

    label("Function_9_1B7C")

    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)

    def lambda_1B89():
        OP_96(0xFE, 0x4C90, 0x3E80, 0xFFFFF830, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B89)
    WaitChrThread(0x8, 1)

    def lambda_1BA7():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BA7)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_9_1B7C end

    def Function_10_1BC4(): pass

    label("Function_10_1BC4")

    SetChrChipByIndex(0xA, 0x2A)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 0)

    def lambda_1BED():
        OP_96(0xFE, 0x4844, 0x3E80, 0x2BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BED)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    OP_93(0xA, 0x87, 0x1F4)
    Return()

    # Function_10_1BC4 end

    def Function_11_1C1A(): pass

    label("Function_11_1C1A")


    def lambda_1C1F():
        OP_96(0xFE, 0x4330, 0x3E80, 0xFFFFF768, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C1F)
    WaitChrThread(0xB, 1)
    Return()

    # Function_11_1C1A end

    def Function_12_1C39(): pass

    label("Function_12_1C39")

    BeginChrThread(0x9, 0, 0, 1)

    def lambda_1C44():
        OP_96(0xFE, 0x44C0, 0x3E80, 0xFFFFFA88, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C44)
    WaitChrThread(0x9, 1)
    EndChrThread(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_12_1C39 end

    def Function_13_1C66(): pass

    label("Function_13_1C66")


    def lambda_1C6B():
        OP_96(0xFE, 0x40D8, 0x3E80, 0xFFFFFED4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1C6B)
    WaitChrThread(0xC, 1)
    OP_93(0xC, 0x87, 0x1F4)
    Return()

    # Function_13_1C66 end

    def Function_14_1C8C(): pass

    label("Function_14_1C8C")


    def lambda_1C91():
        OP_96(0xFE, 0x43F8, 0x3E80, 0xFFFFF2B8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C91)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x2D, 0x1F4)
    Return()

    # Function_14_1C8C end

    def Function_15_1CB2(): pass

    label("Function_15_1CB2")


    def lambda_1CB7():
        OP_96(0xFE, 0x43F8, 0x3E80, 0xFFFFEF98, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1CB7)
    WaitChrThread(0xD, 1)
    OP_93(0xD, 0x2D, 0x1F4)
    Return()

    # Function_15_1CB2 end

    def Function_16_1CD8(): pass

    label("Function_16_1CD8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_1CD8 end

    SaveToFile()

Try(main)
