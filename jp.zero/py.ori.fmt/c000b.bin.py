from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c000b.bin",                # FileName
        "c000b",                    # MapName
        "c000b",                    # Location
        0x0002,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 2, 0, 2, 0, 3],
    )

    BuildStringList((
        "c000b",                  # 0
        "ワジ",                   # 1
        "ヴァルド",               # 2
        "列車",                   # 3
        "SE制御",                 # 4
        "中央広場",               # 5
        "西通り",                 # 6
        "行政区",                 # 7
        "住宅街",                 # 8
        "歓楽街",                 # 9
        "東通り",                 # 10
        "旧市街",                 # 11
        "港湾区",                 # 12
        "ＩＢＣ",                 # 13
        "駅前通り",               # 14
        "裏通り",                 # 15
        "ウルスラ間道",           # 16
        "東クロスベル街道",       # 17
        "西クロスベル街道",       # 18
        "マインツ山道",           # 19
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-9.25, 0.0, 67.0, 0x0000, 0x0000, "中央広場")
    PlaceName(-75.0, 0.0, 71.5, 0x0000, 0x0000, "西通り")
    PlaceName(17.75, 0.0, 156.0, 0x0000, 0x0000, "行政区")
    PlaceName(-136.0, 0.0, 146.0, 0x0000, 0x0000, "住宅街")
    PlaceName(-63.0, 0.0, 138.0, 0x0000, 0x0000, "歓楽街")
    PlaceName(72.0, 0.0, 44.0, 0x0000, 0x0000, "東通り")
    PlaceName(107.5, 0.0, -11.0, 0x0000, 0x0000, "旧市街")
    PlaceName(100.0, 0.0, 110.0, 0x0000, 0x0000, "港湾区")
    PlaceName(74.0, 0.0, 204.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(2.0, 0.0, -2.0, 0x0000, 0x0000, "駅前通り")
    PlaceName(-45.0, 0.0, 102.0, 0x0000, 0x0000, "裏通り")
    PlaceName(-1.0, 0.0, -33.0, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(126.0, 0.0, 58.0, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-126.0, 0.0, 70.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-120.0, 0.0, 170.0, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-31.25, 0.0, 53.0, 0x0000, 0x0051, "")
    PlaceName(22.5, 0.0, 79.0, 0x0000, 0x0054, "")
    PlaceName(-6.75, 0.0, 45.0, 0x0000, 0x0057, "")
    PlaceName(-32.0, 0.0, 82.0, 0x0000, 0x0053, "")
    PlaceName(-11.5, 0.0, 106.0, 0x0000, 0x0053, "")
    PlaceName(-62.25, 0.0, 77.0, 0x0000, 0x0053, "")
    PlaceName(-72.0, 0.0, 98.0, 0x0000, 0x0053, "")
    PlaceName(-48.0, 0.0, 130.0, 0x0000, 0x0052, "")
    PlaceName(-43.25, 0.0, 117.0, 0x0000, 0x0053, "")
    PlaceName(-34.5, 0.0, 108.5, 0x0000, 0x0053, "")
    PlaceName(-6.0, 0.0, 179.5, 0x0000, 0x0051, "")
    PlaceName(106.0, 0.0, 44.0, 0x0000, 0x0052, "")
    PlaceName(89.0, 0.0, -46.5, 0x0000, 0x0053, "")
    PlaceName(76.0, 0.0, -28.0, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_3EC",          # 00, 0
        "Function_1_4A4",          # 01, 1
        "Function_2_4DD",          # 02, 2
        "Function_3_4ED",          # 03, 3
        "Function_4_4FA",          # 04, 4
        "Function_5_20DB",         # 05, 5
        "Function_6_210B",         # 06, 6
        "Function_7_2148",         # 07, 7
        "Function_8_2185",         # 08, 8
        "Function_9_21C2",         # 09, 9
        "Function_10_21FF",        # 0A, 10
    ))


    def Function_0_3EC(): pass

    label("Function_0_3EC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_42C"),
        (1, "loc_438"),
        (2, "loc_444"),
        (3, "loc_450"),
        (4, "loc_45C"),
        (5, "loc_468"),
        (6, "loc_474"),
        (SWITCH_DEFAULT, "loc_480"),
    )


    label("loc_42C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_438")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_444")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_450")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_45C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_468")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_474")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_480")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_48C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_4A3")

    Return()

    # Function_0_3EC end

    def Function_1_4A4(): pass

    label("Function_1_4A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DC")
    OP_95(0xFE, -1830, 0, -23430, 2000, 0x0)
    Sleep(800)
    SetChrPos(0xFE, -1830, 0, 25870, 180)
    Jump("Function_1_4A4")

    label("loc_4DC")

    Return()

    # Function_1_4A4 end

    def Function_2_4DD(): pass

    label("Function_2_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_4EC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)

    label("loc_4EC")

    Return()

    # Function_2_4DD end

    def Function_3_4ED(): pass

    label("Function_3_4ED")

    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    Return()

    # Function_3_4ED end

    def Function_4_4FA(): pass

    label("Function_4_4FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00400.itc", 0x1E)
    LoadChrToIndex("chr/ch02100.itc", 0x1F)
    LoadChrToIndex("chr/ch02150.itc", 0x20)
    OP_68(-500, 1300, 16500, 0)
    MoveCamera(36, 12, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(18500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -500, 0, 23500, 180)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -20800, -5000, 17000, 90)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8)
    OP_90(0x101, -11600, -4800, 17000, 270)
    OP_90(0x102, -10200, -3800, 17000, 270)
    OP_90(0x103, -8800, -2800, 17000, 270)
    OP_90(0x104, -7400, -1800, 17000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_78(0xB, 0xA)
    OP_49()
    SetChrPos(0xA, -50000, -11500, 7500, 0)
    OP_D3(0xA, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0xB, 0x1000)
    OP_7D(0xB4, 0xC8, 0xDC, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01600.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00400.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00000.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetCameraDistance(15500, 3500)

    def lambda_6FE():
        OP_95(0xFE, -500, 0, 16500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6FE)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x9, 1)
    OP_6F(0x10)
    Sleep(300)
    OP_93(0x9, 0x10E, 0x1F4)
    Sound(1805, 255, 90, 0)    #voice#Wald
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0001
    AnonymousTalk(
        0x9,
        (
            "駅前通りの外れにある\x01",
            "資材置き場だったか……\x02\x03",

            "しかし、通信で呼び出したかと思えば\x01",
            "こんな夜中に一人で来いとはな……\x02\x03",

            "警察のガキどもが……\x01",
            "いったい何様のつもりだ……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_68(-14500, -4200, 16500, 7000)
    MoveCamera(45, 16, 0, 7000)

    def lambda_863():
        OP_95(0xFE, -14500, -5000, 16500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_863)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_6F(0x41)
    Fade(500)
    OP_68(-39500, -8000, 6500, 0)
    MoveCamera(65, 24, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(23000, 0)
    OP_11(0x34, 0x21, 0x49, 0x28, 0xFA, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    BeginChrThread(0xA, 3, 0, 5)
    BeginChrThread(0xB, 1, 0, 10)
    OP_68(-21500, -8000, 6500, 5000)
    MoveCamera(45, 4, 0, 5000)
    SetCameraDistance(20000, 5000)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    Fade(500)
    OP_68(-14500, -4200, 16500, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15500, 0)
    OP_11(0x34, 0x21, 0x49, 0x28, 0x78, 0x0)
    SetMapObjFlags(0xB, 0x4)
    OP_0D()

    #C0002
    ChrTalk(
        0x9,
        "#1605F今のは……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    #N0003
    NpcTalk(
        0x8,
        "少年の声",
        (
            "#2P多分、共和国方面の\x01",
            "最終列車ってところじゃない？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x8, 500)
    Fade(1000)
    SetChrPos(0x9, -16000, -5000, 17000, 270)
    SetChrPos(0x8, -24400, -5000, 17000, 90)
    ClearChrFlags(0x8, 0x8)
    OP_68(-18040, -4000, 17740, 0)
    MoveCamera(325, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    Sleep(1)
    OP_68(-21120, -4000, 17740, 1600)
    OP_6F(0x1)

    #C0004
    ChrTalk(
        0x9,
        "#11P#1601Fワジ……！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1435, 255, 90, 0)    #voice#Lazy
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0005
    AnonymousTalk(
        0x8,
        (
            "こんばんは、ヴァルド。\x02\x03",

            "なかなか良い夜だね。\x01",
            "月が濡れたように輝いているよ。\x02",
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

    #C0006
    ChrTalk(
        0x9,
        (
            "#11P#1601Fてめえ……\x02\x03",

            "#1604F……クク、そうか。\x01",
            "そういう事だったのか……\x02\x03",

            "#1602F警察のガキどもを騙#2Rかた#って\x01",
            "俺を嵌めたってことかよ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-22590, -4000, 17740, 2000)

    def lambda_BE2():
        OP_95(0xFE, -20400, -5000, 17000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BE2)
    WaitChrThread(0x9, 1)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    Sound(808, 0, 100, 0)
    SetCameraDistance(18500, 0)
    OP_0D()
    Sleep(500)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    #C0007
    ChrTalk(
        0x9,
        (
            "#1607F#4Sそういう事なら話は早え！\x02\x03",

            "#3Sタイマンなら望むところだ！\x01",
            "ここでケリを付けてやらあ！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "#0404Fフフ、僕としては\x01",
            "それでも異存はないけれど……\x02\x03",

            "#0400Fあいにく僕も、君と同じく\x01",
            "この場に招待されたゲストでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        "#1601Fなに……？\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "#0402Fほら、来たみたいだよ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-16500, -4000, 17000, 0)
    MoveCamera(33, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x9, -22000, -5000, 17500, 270)
    SetChrPos(0x8, -25000, -5000, 17000, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(-20500, -4000, 17000, 5500)
    BeginChrThread(0x101, 3, 0, 6)
    BeginChrThread(0x102, 3, 0, 7)
    BeginChrThread(0x103, 3, 0, 8)
    BeginChrThread(0x104, 3, 0, 9)
    OP_0D()
    Sleep(500)
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(1000)

    def lambda_E00():
        OP_95(0xFE, -23900, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E00)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    #C0011
    ChrTalk(
        0x9,
        "#1600Fてめえら……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0012
    AnonymousTalk(
        0x101,
        (
            "済まない、２人とも。\x01",
            "待たせてしまったみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    #C0013
    ChrTalk(
        0x8,
        (
            "#3P#0404Fお招きにあずかり光栄至極──\x02\x03",

            "#0402F約束通り、さぞ面白い話を\x01",
            "聞かせてくれるんだろうね？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#0004F#11P面白いかどうかはともかく、\x01",
            "興味深い話ではあると思う。\x02\x03",

            "#0000Fさっそく聞いてくれるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0015
    ChrTalk(
        0x9,
        (
            "#1607Fちょ、ちょっと待ちやがれ。\x02\x03",

            "面白い話だぁ……！？\x01",
            "いったい何を言ってやがる！？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        "#3P#0406F馬鹿だなぁ、君は。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 600)

    #C0017
    ChrTalk(
        0x9,
        "#11P#1605Fなっ……！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#3P#0404F５日前の夜、旧市街で起こった\x01",
            "２件の傷害事件……\x02\x03",

            "#0402Fその真犯人の目星が付いたって\x01",
            "話に決まってるじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
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

    #C0019
    ChrTalk(
        0x9,
        "#11P#1605Fな、なにぃ……！？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        "#11P#0105F驚いた……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        (
            "#11P#0200F……あなたの方も\x01",
            "疑っていたようですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "#3P#0403Fまあ、僕も最初は\x01",
            "メンバーの勝手な暴走かと\x01",
            "思ってたんだけど……\x02\x03",

            "#0401Fよくよく状況を整理してみると　\x01",
            "どう考えても不自然じゃないか。\x02\x03",

            "バイパー側にしてもそれは同じ……\x02\x03",

            "#0406Fまあ、僕の推理は\x01",
            "そこで止まっちゃってるけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0003F#11Pそうか……\x01",
            "だったら話は早そうだ。\x02\x03",

            "#0001F──ヴァルド・ヴァレス。\x02\x03",

            "色々と不審なことは\x01",
            "あるかもしれないけど……\x02\x03",

            "まずは一旦、こちらの話を\x01",
            "最後まで聞いてくれないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        "#11P#1603F……チッ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    #C0025
    ChrTalk(
        0x9,
        (
            "#1601F──手短に話せ。\x02\x03",

            "もし、下らねぇ話だったら\x01",
            "その頭をカチ割ってやるからな。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(-20500, -4000, 17000, 0)
    MoveCamera(33, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    Sleep(1000)
    SetChrPos(0x9, -22000, -5000, 18000, 90)
    SetChrPos(0x8, -22200, -5000, 16500, 90)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetCameraDistance(17500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_64(0x8)
    OP_64(0x9)
    OP_6F(0x10)

    #C0026
    ChrTalk(
        0x101,
        (
            "#0003F#11P──これが現時点での情報を\x01",
            "組み立ててみた推理だ。\x02\x03",

            "#0001F率直な感想を聞かせて欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        "#1605F#3P………………………………\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#6P#0406F……やれやれ、参ったね。\x02\x03",

            "まさかマフィアなんかに\x01",
            "そこまでコケにされてたとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#0000F#11Pそれじゃあ……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#11P#0101F今の話……\x01",
            "納得してくれたのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#6P#0402Fフフ、納得もなにも……\x02\x03",

            "前にルバーチェの遣いが\x01",
            "僕たちの所に来てるからね。\x02\x03",

            "良い目を見させてやるから\x01",
            "ウチの下で働かないかッてね。\x02\x03",

            "#0404Fもちろん鼻で笑って\x01",
            "追い返してやったけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#0001F#11Pそうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        "#11P#0303F……決まりだな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    Sleep(300)

    #C0034
    ChrTalk(
        0x8,
        (
            "#12P#0400Fヴァルド。\x01",
            "君のところはどうだい？\x02\x03",

            "やっぱりマフィアの\x01",
            "勧誘があったんじゃないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "#1603F……ああ、一月くらい前にな……\x02\x03",

            "あまりに舐めた話だったから\x01",
            "脅しつけて叩き出してやったが……\x02\x03",

            "#1602F……まさかここまで\x01",
            "舐めた真似をしてくれるとはなァ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(1808, 255, 90, 0)    #voice#Wald
    Sleep(800)
    Fade(250)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    #C0036
    ChrTalk(
        0x9,
        (
            "#1607F#5Pワジ！\x01",
            "てめえとの決着は延期だ！\x02\x03",

            "マフィアだろうと関係ねえ！\x01",
            "まとめて叩き潰してやらあッ！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x102,
        "#11P#0101Fちょ、ちょっと！？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        "#11P#0203F沸点低すぎです……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0013F#11Pお、落ち着いてくれ！\x01",
            "下手にそんな事をしたら──\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        "#12P#0406F本当、馬鹿だなぁ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0041
    ChrTalk(
        0x9,
        "#1601F#5Pなにぃ……！？\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#12P#0400Fマフィア相手に喧嘩して\x01",
            "勝ち目があるわけないだろう？\x02\x03",

            "下手に乗り込んだところで\x01",
            "蜂の巣にされるのがオチだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "#1607Fるせえ！\x01",
            "やってみなきゃ判らねえだろうが！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "#12P#0406Fあのね……君はいいとしても。\x02\x03",

            "#0401F君の可愛い舎弟たちまで\x01",
            "それに巻き込むつもりかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0045
    ChrTalk(
        0x9,
        (
            "#1601F#5P…………ぐ………………\x02\x03",

            "#1607Fなら、てめえはどうなんだ！？\x02\x03",

            "ここまでコケにされて……\x01",
            "仲間をやられたままで\x01",
            "おめおめと引き下がれんのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#12P#0409Fフッ……\x01",
            "そんなワケないだろ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0047
    ChrTalk(
        0x8,
        (
            "#12P#0404F今回の件、関わってるのは\x01",
            "マフィアでもごく一部のはずだ。\x02\x03",

            "なら、そいつらにのみ\x01",
            "落とし前を付けさせればいい。\x02\x03",

            "#0402F報復もできないくらい、\x01",
            "きっちりとスジを通した上でね。\x02\x03",

            "#0409F──ヴァルド。\x01",
            "君にも協力してもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        "#1605F#5P……お前………\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#0011F#11Pちょ、ちょっと待ってくれ。\x02\x03",

            "#0013F何をするつもりだ？\x01",
            "あんまり不穏なことは──\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0050
    ChrTalk(
        0x8,
        (
            "#6P#0409Fああ、心配しなくても\x01",
            "君たちにも手伝ってもらうから。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#0005F#11Pなっ……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1430, 255, 90, 0)    #voice#Lazy
    Sleep(300)
    OP_68(-19110, -4000, 16930, 1800)

    def lambda_1E3F():

        label("loc_1E3F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1E3F")

    QueueWorkItem2(0x9, 2, lambda_1E3F)

    def lambda_1E51():

        label("loc_1E51")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1E51")

    QueueWorkItem2(0x102, 2, lambda_1E51)

    def lambda_1E63():

        label("loc_1E63")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1E63")

    QueueWorkItem2(0x104, 2, lambda_1E63)

    def lambda_1E75():
        OP_95(0xFE, -19700, -5000, 16500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E75)
    WaitChrThread(0x8, 1)
    Sleep(500)

    #C0052
    ChrTalk(
        0x8,
        (
            "#6P#0404F#30W──君たちの任務は\x01",
            "旧市街での事件を解決すること。\x02\x03",

            "だったらマフィアが今後、\x01",
            "僕たちに余計な手出しをしないよう\x01",
            "『言い含めてやる』必要がある……\x02\x03",

            "#20W#0402Fどう──違うかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#0011F#11Pそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        "#5P#0105F（どういう事……？）\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#11P#0202F（……よく判りませんが……）\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#11P#0309F（なんかロイドのやつ、\x01",
            "  取って喰われそうだな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#6P#0402Fフフ、あんな面白い推理を\x01",
            "わざわざ披露してくれたんだ。\x02\x03",

            "#0409F責任をとって……\x01",
            "最後まで付き合ってもらうよ？\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x9, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(2000)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c140B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_4FA end

    def Function_5_20DB(): pass

    label("Function_5_20DB")

    OP_82(0x64, 0x0, 0xBB8, 0x1B58)

    def lambda_20F1():
        OP_96(0xFE, 0xEA60, 0xFFFFD314, 0x1D4C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_20F1)
    WaitChrThread(0xA, 1)
    Return()

    # Function_5_20DB end

    def Function_6_210B(): pass

    label("Function_6_210B")


    def lambda_2110():
        OP_95(0xFE, -13500, -5000, 17000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2110)
    WaitChrThread(0xFE, 1)

    def lambda_212E():
        OP_96(0xFE, 0xFFFFB5C8, 0xFFFFEC78, 0x413C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_212E)
    WaitChrThread(0x101, 1)
    Return()

    # Function_6_210B end

    def Function_7_2148(): pass

    label("Function_7_2148")


    def lambda_214D():
        OP_95(0xFE, -13500, -5000, 17000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_214D)
    WaitChrThread(0xFE, 1)

    def lambda_216B():
        OP_96(0xFE, 0xFFFFB5C8, 0xFFFFEC78, 0x4588, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_216B)
    WaitChrThread(0x102, 1)
    Return()

    # Function_7_2148 end

    def Function_8_2185(): pass

    label("Function_8_2185")


    def lambda_218A():
        OP_95(0xFE, -13500, -5000, 17000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_218A)
    WaitChrThread(0xFE, 1)

    def lambda_21A8():
        OP_96(0xFE, 0xFFFFBB40, 0xFFFFEC78, 0x4010, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21A8)
    WaitChrThread(0x103, 1)
    Return()

    # Function_8_2185 end

    def Function_9_21C2(): pass

    label("Function_9_21C2")


    def lambda_21C7():
        OP_95(0xFE, -13500, -5000, 17000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21C7)
    WaitChrThread(0xFE, 1)

    def lambda_21E5():
        OP_96(0xFE, 0xFFFFBB40, 0xFFFFEC78, 0x445C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_21E5)
    WaitChrThread(0x104, 1)
    Return()

    # Function_9_21C2 end

    def Function_10_21FF(): pass

    label("Function_10_21FF")

    Sound(455, 0, 100, 0)
    Return()

    # Function_10_21FF end

    SaveToFile()

Try(main)
