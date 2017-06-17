from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t110b.bin",                # FileName
        "t110b",                    # MapName
        "t110b",                    # Location
        0x0046,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 70, 0, 2, 0, 3],
    )

    BuildStringList((
        "t110b",                  # 0
        "黑衣人",                 # 1
        "黑衣人",                 # 2
        "黑手党",                 # 3
        "黑手党",                 # 4
        "黑手党",                 # 5
        "黑手党",                 # 6
        "黑手党",                 # 7
        "客人",                   # 8
        "客人",                   # 9
        "偃月轮",                 # 10
        "偃月轮",                 # 11
        "偃月轮",                 # 12
        "偃月轮",                 # 13
        "翠雀酒店方向",           # 14
    ))

    AddCharChip((
        "chr/ch36000.itc",                   # 00
        "chr/ch36100.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch26800.itc",                   # 03
        "apl/ch50363.itc",                   # 04
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   2,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   3,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 31,  0.0,                   0.0,                   -1.0,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -0.0,                  0.19999998807907104,   1.0])

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "翠雀酒店方向")

    ScpFunction((
        "Function_0_36C",          # 00, 0
        "Function_1_424",          # 01, 1
        "Function_2_425",          # 02, 2
        "Function_3_446",          # 03, 3
        "Function_4_47A",          # 04, 4
        "Function_5_56D",          # 05, 5
        "Function_6_DAF",          # 06, 6
        "Function_7_1AC0",         # 07, 7
        "Function_8_1AF0",         # 08, 8
        "Function_9_1B20",         # 09, 9
        "Function_10_1B50",        # 0A, 10
        "Function_11_1B80",        # 0B, 11
        "Function_12_1BD5",        # 0C, 12
        "Function_13_1C0C",        # 0D, 13
        "Function_14_2F88",        # 0E, 14
        "Function_15_2FE4",        # 0F, 15
        "Function_16_3045",        # 10, 16
        "Function_17_30A6",        # 11, 17
        "Function_18_311B",        # 12, 18
        "Function_19_3184",        # 13, 19
        "Function_20_31F9",        # 14, 20
        "Function_21_326E",        # 15, 21
        "Function_22_32D7",        # 16, 22
        "Function_23_32F6",        # 17, 23
        "Function_24_331E",        # 18, 24
        "Function_25_3346",        # 19, 25
        "Function_26_338C",        # 1A, 26
        "Function_27_3426",        # 1B, 27
        "Function_28_346C",        # 1C, 28
        "Function_29_351C",        # 1D, 29
        "Function_30_3562",        # 1E, 30
        "Function_31_360B",        # 1F, 31
    ))


    def Function_0_36C(): pass

    label("Function_0_36C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3AC"),
        (1, "loc_3B8"),
        (2, "loc_3C4"),
        (3, "loc_3D0"),
        (4, "loc_3DC"),
        (5, "loc_3E8"),
        (6, "loc_3F4"),
        (SWITCH_DEFAULT, "loc_400"),
    )


    label("loc_3AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_400")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_40C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_423")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_423")

    Return()

    # Function_0_36C end

    def Function_1_424(): pass

    label("Function_1_424")

    Return()

    # Function_1_424 end

    def Function_2_425(): pass

    label("Function_2_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_436")
    Event(0, 5)

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_445")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_445")

    Return()

    # Function_2_425 end

    def Function_3_446(): pass

    label("Function_3_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 3)), scpexpr(EXPR_END)), "loc_452")
    Call(0, 4)

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_45B")

    label("loc_45B")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_473")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_473")

    Sound(126, 1, 80, 0)
    Return()

    # Function_3_446 end

    def Function_4_47A(): pass

    label("Function_4_47A")

    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, 2500, 0, -10500, 315)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x2)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, 1340, 0, -12150, 135)
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xD, -1950, 0, -13510, 315)
    SetChrChipByIndex(0xE, 0x4)
    SetChrSubChip(0xE, 0x2)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x1)
    SetChrPos(0xE, 1910, 0, -15040, 180)
    Return()

    # Function_4_47A end

    def Function_5_56D(): pass

    label("Function_5_56D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08100.itc", 0x1E)
    OP_68(0, 1800, -27300, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(20000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5FF")
    SetChrPos(0x101, -600, 0, -30250, 0)
    SetChrPos(0x102, 600, 0, -31250, 315)
    SetChrPos(0x103, 1250, 0, -33500, 315)
    SetChrPos(0x104, 1990, 0, -32500, 315)
    Jump("loc_69E")

    label("loc_5FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_651")
    SetChrPos(0x101, -600, 0, -30250, 0)
    SetChrPos(0x102, 1250, 0, -33500, 315)
    SetChrPos(0x103, 600, 0, -31250, 315)
    SetChrPos(0x104, 1990, 0, -32500, 315)
    Jump("loc_69E")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_69E")
    SetChrPos(0x101, -600, 0, -30250, 0)
    SetChrPos(0x102, 1990, 0, -32500, 315)
    SetChrPos(0x103, 1250, 0, -33500, 315)
    SetChrPos(0x104, 600, 0, -31250, 315)

    label("loc_69E")

    FadeToBright(1000, 0)
    OP_68(0, 900, -27300, 3000)
    OP_6F(0x1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_709")
    TurnDirection(0x102, 0x101, 300)

    #C0001
    ChrTalk(
        0x102,
        (
            "#5304F#2P我这边准备好了哦。\x02\x03",

            "#5300F差不多该走了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A9")

    label("loc_709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_75E")
    TurnDirection(0x103, 0x101, 300)

    #C0002
    ChrTalk(
        0x103,
        (
            "#5403F#2P……我这边已经\x01",
            "准备好了。\x02\x03",

            "#5401F差不多该走了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A9")

    label("loc_75E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_7A9")
    TurnDirection(0x104, 0x101, 300)

    #C0003
    ChrTalk(
        0x104,
        (
            "#5604F#2P我随时都可以出发哦。\x02\x03",

            "#5600F差不多该走了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A9")

    TurnDirection(0x101, 0xEF, 400)

    #C0004
    ChrTalk(
        0x101,
        "#5003F#5P嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【进入竞拍会场】\x01",      # 0
            "【先不进去】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_81D"),
        (1, "loc_C6E"),
        (SWITCH_DEFAULT, "loc_DAE"),
    )


    label("loc_81D")

    StopBGM(0xBB8)
    Sleep(150)
    Fade(1000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(882, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德戴上了平光眼镜。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0006
    ChrTalk(
        0x101,
        (
            "#5100F#5P──准备ＯＫ了，\x01",
            "进入竞拍会场吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_98F")

    #C0007
    ChrTalk(
        0x102,
        "#5304F#2P嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        (
            "#0201F#12P罗伊德前辈、艾莉前辈，\x01",
            "……请多加小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x1F4)

    #C0009
    ChrTalk(
        0x104,
        (
            "#0301F#12P按照计划，我们\x01",
            "就在这附近待命。\x02\x03",

            "出了什么事的话，\x01",
            "马上用艾尼格玛联络啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#5102F#5P嗯，\x01",
            "你们也要小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x102,
        "#5302F#5P那我们走了哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B82")

    label("loc_98F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_A87")

    #C0012
    ChrTalk(
        0x103,
        "#5404F#2P……明白了。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        (
            "#0101F#12P罗伊德、缇欧，\x01",
            "千万多加小心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x87, 0x1F4)

    #C0014
    ChrTalk(
        0x104,
        (
            "#0301F#12P按照计划，我们\x01",
            "就在这附近待命。\x02\x03",

            "出了什么事的话，\x01",
            "马上用艾尼格玛联络啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#5102F#5P嗯，\x01",
            "你们也要小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#5402F#5P……那我们走了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B82")

    label("loc_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_B82")

    #C0017
    ChrTalk(
        0x104,
        "#5604F#2P好，走吧。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        (
            "#0201F#12P罗伊德前辈、兰迪前辈，\x01",
            "……请多加小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x87, 0x1F4)

    #C0019
    ChrTalk(
        0x102,
        (
            "#0101F#12P按照计划，我们\x01",
            "就在这附近待命哦。\x02\x03",

            "如果出了什么事，\x01",
            "马上用艾尼格玛联络吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#5102F#5P嗯，\x01",
            "你们也要小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#5602F#5P那么，我们走啦。\x02",
    )

    CloseMessageWindow()

    label("loc_B82")

    WaitBGM()
    PlayBGM("ed7125", 0)

    def lambda_B8C():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B8C)

    def lambda_B99():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B99)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_68(0, 2600, -27300, 6000)

    def lambda_BBF():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BBF)

    def lambda_BD4():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_BD4)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_D5(0x1E)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrChipPat(0x0, 0x1, 0x51)
    LoadChrChipPat()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_C43")
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    Jump("loc_C66")

    label("loc_C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_C57")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    Jump("loc_C66")

    label("loc_C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_C66")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)

    label("loc_C66")

    Call(0, 6)
    Jump("loc_DAE")

    label("loc_C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_CD0")

    #C0022
    ChrTalk(
        0x102,
        (
            "#5303F……明白了。\x01",
            "可是，时间不多了。\x02\x03",

            "#5301F尽量混在其他客人\x01",
            "之中进入会场吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D93")

    label("loc_CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_D35")

    #C0023
    ChrTalk(
        0x103,
        (
            "#5403F……明白了。\x02\x03",

            "#5401F只是，我想还是趁着有其他\x01",
            "客人入场时一起混进去会比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D93")

    label("loc_D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_D93")

    #C0024
    ChrTalk(
        0x104,
        (
            "#5605F怎么，还不进去吗？\x02\x03",

            "#5601F趁着有其他客人入场\x01",
            "的时候一起混进去会比较好哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D93")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("t101B", 101, 0, 0)
    IdleLoop()
    Jump("loc_DAE")

    label("loc_DAE")

    Return()

    # Function_5_56D end

    def Function_6_DAF(): pass

    label("Function_6_DAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50354.itc", 0x1E)
    LoadChrToIndex("apl/ch50355.itc", 0x1F)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, 600, 0, 23800, 180)
    SetChrPos(0x9, -600, 0, 23800, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0xF, -340, 200, 1500, 0)
    SetChrPos(0x10, 770, 200, 750, 0)
    SetChrPos(0x101, 600, 0, -19500, 0)
    SetChrPos(0xEF, -600, 0, -21000, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    OP_70(0x0, 0xA)
    ClearMapObjFlags(0x0, 0x10)
    FadeToBright(1000, 0)
    OP_68(0, 500, 1470, 0)
    MoveCamera(36, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44890, 0)
    OP_68(0, 500, 22520, 15000)

    def lambda_EC0():
        OP_95(0xFE, 600, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EC0)

    def lambda_EDA():
        OP_95(0xFE, -600, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_EDA)

    def lambda_EF4():
        OP_95(0xFE, -600, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_EF4)

    def lambda_F0E():
        OP_95(0xFE, 600, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F0E)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    Sleep(1000)
    BeginChrThread(0x8, 3, 0, 7)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 8)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    BeginChrThread(0xF, 3, 0, 11)
    Sleep(1000)
    BeginChrThread(0x10, 3, 0, 11)
    Sleep(2000)
    BeginChrThread(0x8, 3, 0, 9)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 10)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    Sleep(1000)
    OP_0D()
    Fade(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    SetChrPos(0x8, 600, 0, 23800, 180)
    SetChrPos(0x9, -600, 0, 23800, 180)
    SetChrPos(0x101, 600, 0, 13500, 0)
    SetChrPos(0xEF, -600, 0, 12500, 0)
    OP_68(0, 1000, 22320, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21700, 0)
    SetCameraDistance(19200, 3000)

    def lambda_1007():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1007)

    def lambda_101C():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_101C)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1059():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1059)
    Sleep(100)

    def lambda_1071():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1071)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x10)

    #C0025
    ChrTalk(
        0x8,
        "#5P欢迎参加『黑之竞拍会』。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        "#5P请出示您的邀请卡好吗？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        "#5100F#11P嗯，是这个吧。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将印有金色蔷薇的卡片\x01",
            "交给疑似黑手党的黑衣人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0029
    ChrTalk(
        0x8,
        "#5P……的确。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        (
            "#5P保险起见，可以\x01",
            "请教您尊姓大名吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#5105F#11P嗯……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0032
    ChrTalk(
        0x101,
        (
            "#5104F#11P──盖伊·班宁斯。\x01",
            "真实身份就没必要表明了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        "#5P嗯，那当然。\x02",
    )

    CloseMessageWindow()

    def lambda_11F5():

        label("loc_11F5")

        TurnDirection(0xFE, 0xEF, 500)
        Yield()
        Jump("loc_11F5")

    QueueWorkItem2(0x8, 1, lambda_11F5)
    Sleep(300)

    #C0034
    ChrTalk(
        0x8,
        "#5P这位是……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_149B")

    #C0035
    ChrTalk(
        0x102,
        (
            "#5304F#12P呵呵，辛苦了。\x02\x03",

            "#5300F我稍微有些隐情，\x01",
            "不方便表明真实身份……\x02\x03",

            "不过，反正活动的性质也是如此，\x01",
            "应该没关系吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        "#5P是的，当然……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#5P不过，姑且请问一下您与\x01",
            "这位盖伊先生的关系可以吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0x102, 0x2BC, 0x0, 0x1F4, 0x7D0, 0x0)
    Fade(250)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    EndChrThread(0x8, 0x1)
    Sleep(300)

    #C0038
    ChrTalk(
        0x102,
        (
            "#5309F#12P哎呀，看不出我们是恋人吗？\x02\x03",

            "#5302F呵呵……虽说是恋人，\x01",
            "但也只是瞒着双亲\x01",
            "的秘密恋爱关系而已啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#5106F#11P抱歉，都是因为\x01",
            "我的身份配不上你……\x02\x03",

            "#5101F但是，我一定会努力\x01",
            "做出一番事业，然后再去请求\x01",
            "你的父母将女儿托付给我……！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        "#5309F#12P呵呵，我很期待哦。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "#5P咳咳……失礼了。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        "#5P那么，盖伊先生，以及同行的这位小姐。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "#5P请尽情享受\x01",
            "今晚的竞拍会。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A3D")

    label("loc_149B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1770")
    TurnDirection(0x103, 0x101, 400)
    Sleep(300)

    #C0044
    ChrTalk(
        0x103,
        (
            "#5406F#6P……那个，哥哥。\x02\x03",

            "#5408F有必要把我的名字\x01",
            "告诉这两位先生吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#5104F#11P嗯，没有那个必要啦。\x02\x03",

            "#5101F──她是我妹妹。\x01",
            "有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "#5P不，怎么会。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#5P只是……\x01",
            "你们兄妹好像\x01",
            "长得不太像啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x190)

    #C0048
    ChrTalk(
        0x103,
        (
            "#5404F#12P……嗯，这是当然的。\x02\x03",

            "#5402F因为我是母亲再婚时带来的，\x01",
            "和哥哥并没有血缘关系。\x02\x03",

            "#5409F当然也可以结婚哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0049
    ChrTalk(
        0x101,
        (
            "#5106F#11P真是的……\x01",
            "小孩子不要乱说话啦。\x02\x03",

            "#5102F──总之，我们家\x01",
            "也有很多隐情啦。\x02\x03",

            "顺带一提，这孩子的\x01",
            "鉴别眼光相当敏锐。\x02\x03",

            "我带她前来，是想让她帮我\x01",
            "给这场竞拍会的拍卖品估个价。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        (
            "#5402F#12P呵呵……\x01",
            "好期待哦，哥哥。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "#5P哈哈，真是一对亲密的兄妹啊。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        "#5P那么，盖伊先生，以及令妹。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "#5P请尽情享受\x01",
            "今晚的竞拍会。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x1)
    Jump("loc_1A3D")

    label("loc_1770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1A3D")

    #C0054
    ChrTalk(
        0x104,
        (
            "#5600F#12P嗯，我是这位少爷的\x01",
            "幼时玩伴兼损友。\x02\x03",

            "#5609F哈哈～这家伙老是\x01",
            "过于一本正经的。\x02\x03",

            "所以我才劝他来出席\x01",
            "这种成年人的活动，\x01",
            "就当是积累各种经验。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0055
    ChrTalk(
        0x101,
        (
            "#5111F#11P没、没必要把\x01",
            "这种事情也说出来吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        "#5P哈哈，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#5P的确，参加这个活动，\x01",
            "或许真能成为难得的经验呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#5106F#11P真是的，你不要总是\x01",
            "把我当小孩子来看待啦。\x02\x03",

            "#5101F这次来参加活动，也并不\x01",
            "完全是因为你的劝说。\x02\x03",

            "那个，是考虑到自己的将来，\x01",
            "想积累一点社会经验……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#5604F#12P知道啦知道啦，\x01",
            "不要那么认真嘛。\x02\x03",

            "#5602F──据传闻说，在这里展出的都是\x01",
            "相当奢华的拍卖品……\x02\x03",

            "我可以期待一下吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0060
    ChrTalk(
        0x8,
        "#5P嗯，那当然。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        "#5P那么，盖伊先生，以及同行的这位先生。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "#5P请尽情享受\x01",
            "今晚的竞拍会。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x1)

    label("loc_1A3D")

    BeginChrThread(0x8, 3, 0, 7)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 8)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    OP_68(0, 1000, 23820, 3000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1A8F")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    BeginChrThread(0x101, 3, 0, 12)
    BeginChrThread(0x102, 3, 0, 12)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    Jump("loc_1AA6")

    label("loc_1A8F")

    BeginChrThread(0x101, 3, 0, 11)
    Sleep(750)
    BeginChrThread(0xEF, 3, 0, 11)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)

    label("loc_1AA6")

    OP_6F(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_DAF end

    def Function_7_1AC0(): pass

    label("Function_7_1AC0")


    def lambda_1AC5():
        OP_98(0xFE, 0x2BC, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AC5)

    def lambda_1ADF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1ADF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_7_1AC0 end

    def Function_8_1AF0(): pass

    label("Function_8_1AF0")


    def lambda_1AF5():
        OP_98(0xFE, 0xFFFFFD44, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AF5)

    def lambda_1B0F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B0F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_8_1AF0 end

    def Function_9_1B20(): pass

    label("Function_9_1B20")


    def lambda_1B25():
        OP_98(0xFE, 0xFFFFFD44, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B25)

    def lambda_1B3F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B3F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_9_1B20 end

    def Function_10_1B50(): pass

    label("Function_10_1B50")


    def lambda_1B55():
        OP_98(0xFE, 0x2BC, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B55)

    def lambda_1B6F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B6F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_10_1B50 end

    def Function_11_1B80(): pass

    label("Function_11_1B80")


    def lambda_1B85():
        OP_95(0xFE, 0, 0, 24380, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B85)
    WaitChrThread(0xFE, 1)

    def lambda_1BA3():
        OP_95(0xFE, 0, 800, 29450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1BA3)
    Sleep(2000)

    def lambda_1BC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BC0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_11_1B80 end

    def Function_12_1BD5(): pass

    label("Function_12_1BD5")


    def lambda_1BDA():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1BDA)
    Sleep(3500)

    def lambda_1BF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BF7)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_12_1BD5 end

    def Function_13_1C0C(): pass

    label("Function_13_1C0C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31100.itc", 0x22)
    LoadChrToIndex("chr/ch31150.itc", 0x23)
    LoadChrToIndex("chr/ch31151.itc", 0x24)
    LoadChrToIndex("chr/ch31153.itc", 0x25)
    LoadChrToIndex("chr/ch31900.itc", 0x26)
    LoadChrToIndex("chr/ch31952.itc", 0x27)
    LoadChrToIndex("chr/ch31951.itc", 0x28)
    LoadChrToIndex("chr/ch31953.itc", 0x29)
    LoadChrToIndex("apl/ch50372.itc", 0x2A)
    LoadEffect(0x0, "event\\ev310_00.eff")
    LoadEffect(0x1, "battle\\ms00001.eff")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xA, 2500, 0, -16500, 0)
    SetChrPos(0xB, -2500, 0, -16500, 0)
    SetChrPos(0xC, 0, 0, -17500, 0)
    SetChrPos(0xD, 1000, 0, -15500, 0)
    SetChrPos(0xE, -1000, 0, -15500, 0)
    SetChrChipByIndex(0x11, 0x2A)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x2A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x11, 0, 0, 50000, 0)
    SetChrPos(0x12, 0, 0, 50000, 0)
    BeginChrThread(0x11, 0, 0, 22)
    BeginChrThread(0x12, 0, 0, 22)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    OP_A7(0x13, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0x14, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 800, 29650, 180)
    SetChrPos(0xEF, 0, 800, 29650, 180)
    SetChrPos(0x105, 0, 800, 29650, 180)
    SetChrPos(0x133, 0, 800, 29650, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1E51")
    SetChrPos(0x103, 600, 200, -14600, 0)
    SetChrPos(0x104, -600, 200, -14600, 0)
    Jump("loc_1EAC")

    label("loc_1E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1E81")
    SetChrPos(0x102, 600, 200, -14600, 0)
    SetChrPos(0x104, -600, 200, -14600, 0)
    Jump("loc_1EAC")

    label("loc_1E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1EAC")
    SetChrPos(0x103, 600, 200, -14600, 0)
    SetChrPos(0x102, -600, 200, -14600, 0)

    label("loc_1EAC")

    OP_68(0, 1100, 32500, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26840, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(25840, 2500)
    OP_6F(0x79)
    OP_0D()
    Sound(121, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(0, 1100, 21000, 3500)
    MoveCamera(0, 30, 0, 3500)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(300)
    BeginChrThread(0xEF, 3, 0, 15)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 16)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 1100, -2600, 0)
    MoveCamera(325, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25840, 0)
    SetCameraDistance(20320, 4000)
    OP_6F(0x10)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x105, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1100, -3200, 2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2030")

    def lambda_1FFB():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1FFB)
    Sleep(300)

    def lambda_2013():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2013)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_20B1")

    label("loc_2030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2073")

    def lambda_203E():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_203E)
    Sleep(300)

    def lambda_2056():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2056)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_20B1")

    label("loc_2073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_20B1")

    def lambda_2081():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2081)
    Sleep(300)

    def lambda_2099():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2099)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)

    label("loc_20B1")

    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20E4")

    #C0063
    ChrTalk(
        0x103,
        "#0201F#6P罗伊德前辈……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2104")

    label("loc_20E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2104")

    #C0064
    ChrTalk(
        0x104,
        "#0307F#6P罗伊德！\x02",
    )

    CloseMessageWindow()

    label("loc_2104")


    #C0065
    ChrTalk(
        0x101,
        (
            "#0002F#11P太好了……\x01",
            "终于顺利会合了啊！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_21B1")

    #C0066
    ChrTalk(
        0x104,
        (
            "#0306F#6P呼……\x01",
            "真让人捏了一把冷汗啊──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0067
    ChrTalk(
        0x104,
        "#0305F#6P话说，这孩子是怎么回事！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2237")

    label("loc_21B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2237")

    #C0068
    ChrTalk(
        0x102,
        (
            "#0106F#6P呼……\x01",
            "真是让人捏了一把冷汗呢──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0069
    ChrTalk(
        0x102,
        (
            "#0105F#6P话说……\x01",
            "这孩子是怎么回事啊！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_227E")

    #C0070
    ChrTalk(
        0x102,
        (
            "#0106F#11P在通讯时不是说了吗？\x01",
            "我们救出了一个女孩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2307")

    label("loc_227E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_22C3")

    #C0071
    ChrTalk(
        0x103,
        (
            "#0206F#11P就是通讯时说的那个\x01",
            "被我们救出的女孩……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2307")

    label("loc_22C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2307")

    #C0072
    ChrTalk(
        0x104,
        (
            "#0309F#11P在通讯时不是都说了吗？\x01",
            "我们救出了一个女孩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2307")


    #N0073
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#5805F#5P那个那个，罗伊德。\x01",
            "这些人，是同伴吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#0004F#11P嗯，是值得信赖的同伴。\x02\x03",

            "#0000F没时间了，快点从这里──\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)

    #N0075
    NpcTalk(
        0xD,
        "男人的声音",
        "#2P哼，你们休想！\x02",
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
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1200, -7000, 2500)
    MoveCamera(310, 20, 0, 2500)
    OP_6E(560, 2500)
    SetCameraDistance(21000, 2500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_24B7")

    def lambda_249D():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_249D)

    def lambda_24AA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_24AA)
    Jump("loc_2502")

    label("loc_24B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_24DF")

    def lambda_24C5():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24C5)

    def lambda_24D2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_24D2)
    Jump("loc_2502")

    label("loc_24DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2502")

    def lambda_24ED():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_24ED)

    def lambda_24FA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24FA)

    label("loc_2502")


    def lambda_2507():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2507)
    Sleep(50)

    def lambda_251F():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_251F)
    Sleep(50)

    def lambda_2537():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2537)
    Sleep(50)

    def lambda_254F():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_254F)
    Sleep(50)

    def lambda_2567():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2567)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    OP_0D()

    #C0076
    ChrTalk(
        0x101,
        "#0010F#11P呜……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x105,
        (
            "#0406F#2P哎呀呀……\x01",
            "似乎被他们看穿了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xD,
        (
            "#6P哼哼，按照副头目的指示\x01",
            "埋伏在这里，果然没错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xE,
        (
            "#5P原来如此……\x01",
            "是警察局的那些小鬼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xE,
        (
            "#5P哼，你们这次实在是\x01",
            "淘气过头了吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(150)
    Fade(500)
    SetCameraDistance(20500, 500)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x2)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x2)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x2)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x2)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_290D")
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x101,
        "#0007F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#0307F#11P导力式的重机关枪──\x01",
            "你们竟然有这种东西！\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        (
            "#0201F#11P而且好像还是帝国莱恩福尔特公司\x01",
            "制造的最新型号呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xD,
        (
            "#6P哼哼……\x01",
            "你们尽管抵抗吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xE,
        (
            "#5P哈哈，只不过，在这种距离下，\x01",
            "一瞬间就能把你们轰成肉酱吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        "#0110F#11P呜……\x02",
    )

    CloseMessageWindow()

    #N0087
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#5801F#5P那个那个，罗伊德……\x02\x03",

            "莫非这个\x01",
            "就叫『危机』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#0013F#11P嗯……\x01",
            "看来是了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0089
    ChrTalk(
        0x105,
        (
            "#0404F#11P不……\x01",
            "似乎还不算呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#0005F#11P哎──\x02",
    )

    CloseMessageWindow()

    label("loc_290D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2AC8")
    Fade(500)
    OP_68(-11030, 3200, -1010, 0)
    MoveCamera(310, 8, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(23000, 0)
    Sleep(300)
    OP_68(-140, 1200, -10540, 1500)
    MoveCamera(300, 28, 0, 1500)
    SetCameraDistance(17930, 1500)
    BeginChrThread(0x11, 3, 0, 26)
    Sleep(1350)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(500)

    #C0091
    ChrTalk(
        0xE,
        "#4S#5P啊……！？\x05\x02",
    )

    BeginChrThread(0xE, 3, 0, 17)
    Sleep(100)

    #C0092
    ChrTalk(
        0xD,
        "#4S#6P呜咕……！？\x05\x02",
    )

    BeginChrThread(0xD, 3, 0, 18)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x11, 3)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0093
    ChrTalk(
        0xA,
        "#5P什么……\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xB,
        "#5P什么……！？\x02",
    )

    CloseMessageWindow()

    label("loc_2AC8")

    Fade(500)
    OP_68(2450, 800, -11290, 0)
    MoveCamera(224, 35, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(30050, 0)
    OP_68(0, 800, -9180, 3000)
    MoveCamera(305, 25, 0, 3000)
    SetCameraDistance(20000, 3000)
    BeginChrThread(0x11, 3, 0, 28)
    BeginChrThread(0x12, 3, 0, 30)
    Sleep(1650)
    OP_82(0x1F4, 0x0, 0xBB8, 0x96)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(500)

    #C0095
    ChrTalk(
        0xB,
        "#4S#5P呀……！\x05\x02",
    )

    BeginChrThread(0xB, 3, 0, 19)
    Sleep(1600)
    OP_82(0x1F4, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(500)

    #C0096
    ChrTalk(
        0xC,
        "#4S#6P呜哇……！\x05\x02",
    )

    BeginChrThread(0xC, 3, 0, 21)
    Sleep(150)

    #C0097
    ChrTalk(
        0xA,
        "#4S#6P呜哦……！\x05\x02",
    )

    BeginChrThread(0xA, 3, 0, 20)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_68(0, 1100, -3200, 2500)
    MoveCamera(325, 13, 0, 2500)
    OP_6E(500, 2500)
    SetCameraDistance(21000, 2500)
    OP_6F(0x79)

    #N0098
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#5805F#5P哎～……\x02\x03",

            "#5810F黑衣服的人\x01",
            "都被打倒了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        "#0011F#11P刚、刚才的是……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D42")
    OP_93(0x104, 0x0, 0x1F4)

    #C0100
    ChrTalk(
        0x104,
        (
            "#0301F#6P似乎是从\x01",
            "宅邸那边飞过来的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D6F")

    label("loc_2D42")


    #C0101
    ChrTalk(
        0x104,
        (
            "#0301F#11P似乎是从\x01",
            "宅邸那边飞过来的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D6F")


    #C0102
    ChrTalk(
        0x105,
        (
            "#0404F#11P呵呵，看来\x01",
            "还有其他帮手呢。\x02\x03",

            "#0402F稍后再作探究，\x01",
            "先逃为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#0007F#11P嗯……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E1E")
    OP_93(0x102, 0x0, 0x1F4)

    #C0104
    ChrTalk(
        0x102,
        (
            "#0101F#6P现在应该正好\x01",
            "该有水上巴士过来了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E60")

    label("loc_2E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2E60")
    OP_93(0x103, 0x0, 0x1F4)

    #C0105
    ChrTalk(
        0x103,
        (
            "#0201F#6P现在应该刚好\x01",
            "会有水上巴士过来……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E9C")
    OP_93(0x104, 0x0, 0x1F4)

    #C0106
    ChrTalk(
        0x104,
        "#0307F#6P总之，快前往码头吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED6")

    label("loc_2E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2ED6")
    OP_93(0x103, 0x0, 0x1F4)

    #C0107
    ChrTalk(
        0x103,
        (
            "#0201F#6P……总之，\x01",
            "快点前往码头吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED6")

    FadeToDark(1000, 0, -1)
    SetCameraDistance(20000, 2000)
    OP_6F(0x10)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x5A, 3)
    Call(0, 4)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_49()
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    OP_70(0x0, 0x0)
    ClearMapObjFlags(0x0, 0x10)
    SetScenarioFlags(0xA7, 3)
    OP_29(0x47, 0x1, 0x12)
    EventEnd(0x5)
    Return()

    # Function_13_1C0C end

    def Function_14_2F88(): pass

    label("Function_14_2F88")


    def lambda_2F8D():
        OP_9B(0x0, 0xFE, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F8D)

    def lambda_2FA2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FA2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_98(0xFE, 0x0, 0x0, 0x0, 0x0, 0x0)

    def lambda_2FCF():
        OP_9B(0x0, 0xFE, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FCF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_2F88 end

    def Function_15_2FE4(): pass

    label("Function_15_2FE4")


    def lambda_2FE9():
        OP_9B(0x0, 0xFE, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FE9)

    def lambda_2FFE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FFE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_98(0xFE, 0x258, 0x0, 0x0, 0x0, 0x0)

    def lambda_302B():
        OP_95(0xFE, -600, 200, -1700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_302B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_2FE4 end

    def Function_16_3045(): pass

    label("Function_16_3045")


    def lambda_304A():
        OP_9B(0x0, 0xFE, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_304A)

    def lambda_305F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_305F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_98(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x0, 0x0)

    def lambda_308C():
        OP_95(0xFE, 600, 200, -2200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_308C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_3045 end

    def Function_17_30A6(): pass

    label("Function_17_30A6")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1000, 900, -10500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_30F0():
        OP_9D(0xFE, 0xFFFFFC18, 0x0, 0xFFFFCB44, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30F0)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_17_30A6 end

    def Function_18_311B(): pass

    label("Function_18_311B")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 1000, 900, -10500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_315F():
        OP_9D(0xFE, 0x3E8, 0x0, 0xFFFFC950, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_315F)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_18_311B end

    def Function_19_3184(): pass

    label("Function_19_3184")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -2500, 900, -11500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_31CE():
        OP_9D(0xFE, 0xFFFFE4A8, 0xFFFFD8F0, 0xFFFFCD38, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31CE)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Sound(927, 0, 100, 0)
    Return()

    # Function_19_3184 end

    def Function_20_31F9(): pass

    label("Function_20_31F9")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 2500, 900, -11500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_3243():
        OP_9D(0xFE, 0x9C4, 0x0, 0xFFFFCF2C, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3243)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_20_31F9 end

    def Function_21_326E(): pass

    label("Function_21_326E")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 900, -12500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_32B2():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFFCB44, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32B2)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_21_326E end

    def Function_22_32D7(): pass

    label("Function_22_32D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32F5")
    OP_A1(0xFE, 0xFA0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_22_32D7")

    label("loc_32F5")

    Return()

    # Function_22_32D7 end

    def Function_23_32F6(): pass

    label("Function_23_32F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_331D")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_23_32F6")

    label("loc_331D")

    Return()

    # Function_23_32F6 end

    def Function_24_331E(): pass

    label("Function_24_331E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3345")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_24_331E")

    label("loc_3345")

    Return()

    # Function_24_331E end

    def Function_25_3346(): pass

    label("Function_25_3346")

    SetChrPos(0xFE, 0, 0, 14500, 0)
    OP_9E(0xFE, 0x0, 0x7D0, 0xFFFEA070, 0xEA60, 0x0)

    def lambda_3371():
        OP_9E(0xFE, 0x0, 0x7D0, 0xFFFD40E0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3371)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_3346 end

    def Function_26_338C(): pass

    label("Function_26_338C")

    PlayEffect(0x0, 0xFF, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(926, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0x13, 3, 0, 25)
    BeginChrThread(0xFE, 2, 0, 23)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3415")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_33E7")

    label("loc_3415")

    WaitChrThread(0x13, 3)
    EndChrThread(0xFE, 0x2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_26_338C end

    def Function_27_3426(): pass

    label("Function_27_3426")

    SetChrPos(0xFE, -2500, 0, 16000, 0)
    OP_9E(0xFE, 0xFFFFF63C, 0x8CA, 0x13880, 0xEA60, 0x0)

    def lambda_3451():
        OP_9E(0xFE, 0xFFFFF63C, 0x8CA, 0x347D8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3451)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_3426 end

    def Function_28_346C(): pass

    label("Function_28_346C")

    PlayEffect(0x0, 0xFF, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(926, 0, 100, 0)
    SetChrFlags(0xFE, 0x800)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0x13, 3, 0, 27)
    BeginChrThread(0xFE, 2, 0, 23)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_34CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3506")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_NEG), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_34CC")

    label("loc_3506")

    WaitChrThread(0x13, 3)
    EndChrThread(0xFE, 0x2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x800)
    Return()

    # Function_28_346C end

    def Function_29_351C(): pass

    label("Function_29_351C")

    SetChrPos(0xFE, 0, 0, 15000, 0)
    OP_9E(0xFE, 0x0, 0x3E8, 0xFFFDF0A8, 0xEA60, 0x0)

    def lambda_3547():
        OP_9E(0xFE, 0x0, 0x3E8, 0xFFFDF0A8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3547)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_351C end

    def Function_30_3562(): pass

    label("Function_30_3562")

    Sleep(2000)
    PlayEffect(0x0, 0xFF, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(926, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0x14, 3, 0, 29)
    BeginChrThread(0xFE, 2, 0, 24)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_35C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35FA")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_NEG), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_35C0")

    label("loc_35FA")

    WaitChrThread(0x14, 3)
    EndChrThread(0xFE, 0x2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_30_3562 end

    def Function_31_360B(): pass

    label("Function_31_360B")

    EventBegin(0x1)

    #C0108
    ChrTalk(
        0x101,
        (
            "#0001F现在不是回头的时候……\x01",
            "赶快带着这孩子去码头吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 200, -1700, 180)
    EventEnd(0x4)
    Return()

    # Function_31_360B end

    SaveToFile()

Try(main)
