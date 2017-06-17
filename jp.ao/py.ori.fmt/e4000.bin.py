from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4000.bin",                # FileName
        "e4000",                    # MapName
        "e4000",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 2000, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4000",                  # 0
        "ガレリア要塞司令",       # 1
        "帝国軍兵士",             # 2
        "帝国軍兵士",             # 3
        "帝国軍兵士",             # 4
        "帝国軍兵士",             # 5
        "帝国軍兵士",             # 6
        "帝国軍兵士",             # 7
        "帝国軍兵士",             # 8
        "帝国軍兵士",             # 9
        "帝国軍兵士",             # 10
        "帝国軍兵士",             # 11
        "帝国軍兵士",             # 12
        "帝国軍兵士",             # 13
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(524, 0)                                        # 0

    ScpFunction((
        "Function_0_20C",          # 00, 0
        "Function_1_21C",          # 01, 1
        "Function_2_21D",          # 02, 2
    ))


    def Function_0_20C(): pass

    label("Function_0_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_21B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_21B")

    Return()

    # Function_0_20C end

    def Function_1_21C(): pass

    label("Function_1_21C")

    Return()

    # Function_1_21C end

    def Function_2_21D(): pass

    label("Function_2_21D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41002.itc", 0x1E)
    LoadChrToIndex("chr/ch41102.itc", 0x1F)
    SoundLoad(498)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x8, 0, 2150, -2700, 180)
    SetChrPos(0x9, -1800, 150, -6700, 90)
    SetChrPos(0xA, -1800, 150, -9100, 90)
    SetChrPos(0xB, -1800, 150, -11450, 90)
    SetChrPos(0xC, 1800, 150, -6700, 270)
    SetChrPos(0xD, 1800, 150, -9000, 270)
    SetChrPos(0xE, 1800, 150, -11400, 270)
    SetChrPos(0xF, -6300, 150, -9900, 270)
    SetChrPos(0x10, -6300, 150, -13850, 270)
    SetChrPos(0x11, -2200, 150, -16300, 180)
    SetChrPos(0x12, 1600, 150, -16300, 180)
    SetChrPos(0x13, 6300, 150, -10050, 90)
    SetChrPos(0x14, 6300, 150, -14000, 90)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x103, 0x8)
    OP_68(0, 1700, -11000, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(24000, 0)
    Sound(498, 2, 80, 0)
    FadeToBright(1000, 0)
    OP_68(1000, 1700, -3000, 5000)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(1000, 3000, -2700, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0001
    ChrTalk(
        0x8,
        "#5P#4Sば、馬鹿な……！？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "#5P第５機甲師団が\x01",
            "壊滅しただと！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0xD, 0x2)
    Fade(500)
    OP_68(0, 3500, -8000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    #C0003
    ChrTalk(
        0xD,
        "#11Pし、信じ難いことですが……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xD,
        (
            "#11P巨大な人型が現れて\x01",
            "全てを薙ぎ払ったと……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "#5Pな、何を馬鹿な……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#5P……まあいい。\x01",
            "そっちがその気ならば\x01",
            "こちらも容赦はせん。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrSubChip(0xD, 0x0)
    OP_68(-60, 3900, -13100, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(10500, 1000)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0007
    ChrTalk(
        0x8,
        (
            "#5P#4S列車砲起動！\x01",
            "目標、クロスベル市！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "#5P#4Sせめてもの情けだ！\x01",
            "民間人の密集地は避けてやれ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(330, 140, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetChrName("兵士たち")

    #A0009
    AnonymousTalk(
        0xFF,
        "#5S了解#4Rヤ ー#！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(12170, 2000)
    StopSound(498, 2000, 70)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C9(0x0, 0x10)
    FadeToBright(300, 16777215)
    OP_0D()
    PlayMovie(0x0, "ed72_04b.pmf", 0x22A, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x22A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x103, 0x8)
    SetScenarioFlags(0x22, 4)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_21D end

    SaveToFile()

Try(main)
