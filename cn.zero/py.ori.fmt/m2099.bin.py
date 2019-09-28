from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m2099.bin",                # FileName
        "M2099",                    # MapName
        "M2099",                    # Location
        0x0074,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 116, 0, 1, 0, 2],
    )

    BuildStringList((
        "m2099",                  # 0
        "ＢＯＳＳ１",             # 1
        "bm2099",                 # 2
        "bm2099",                 # 3
    ))

    ATBonus("ATBonus_1BC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_1DC", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_29C", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_280", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_284", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_288", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_28C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_290", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_294", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_21C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_220", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_224", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_228", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_22C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_230", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_234", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_238", 8, 14, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_300", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm2099", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72201.dat", "ms72201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_29C", "MonsterBattlePostion_27C", "ed7401", "ed7403", "ATBonus_1BC"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_2BC", 0x0052, 30, 6, 45, 0, 1, 0, 0, "bm2099", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75100.dat", "ms74100.dat", "ms74100.dat", 0, 0, 0, "ms74100.dat", 0, "MonsterBattlePostion_21C", "MonsterBattlePostion_27C", "ed7405", "ed7403", "ATBonus_1DC"),
            (),
            (),
            (),
        )
    )

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
        "monster/ch75150.itc",               # 10
        "monster/ch75150.itc",               # 11
        "monster/ch74150.itc",               # 12
        "monster/ch74150.itc",               # 13
        "monster/ch72250.itc",               # 14
        "monster/ch72250.itc",               # 15
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(49520,   -10,     1100,    0x185010E,    "BattleInfo_300", 0,   20,  0xFFFF, 4,  5)

    DeclEvent(0x0040, 0, 9,   49.52000045776367,     -0.009999999776482582, 0.25,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -6.190000057220459,    0.0012499999720603228, -0.0625,               1.0])

    DeclActor(-83500,  0,       -5000,   1200,    -83500,  1500,    -5000,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 2, 1])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5

    ScpFunction((
        "Function_0_3B4",          # 00, 0
        "Function_1_3D3",          # 01, 1
        "Function_2_3FD",          # 02, 2
        "Function_3_4F7",          # 03, 3
        "Function_4_5EA",          # 04, 4
        "Function_5_10EF",         # 05, 5
        "Function_6_1114",         # 06, 6
        "Function_7_1131",         # 07, 7
        "Function_8_116A",         # 08, 8
        "Function_9_14FC",         # 09, 9
    ))


    def Function_0_3B4(): pass

    label("Function_0_3B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D2")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_3B4")

    label("loc_3D2")

    Return()

    # Function_0_3B4 end

    def Function_1_3D3(): pass

    label("Function_1_3D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3ED")
    Event(0, 4)

    label("loc_3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_3FC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 8)

    label("loc_3FC")

    Return()

    # Function_1_3D3 end

    def Function_2_3FD(): pass

    label("Function_2_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_40F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_41E")
    StopEffect(0x80, 0x0)
    StopEffect(0x81, 0x0)

    label("loc_41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_47F")
    SetMapObjFrame(0xFF, "object02_smoke", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_particle", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_fire", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model04_glow", 0x0, 0x1)

    label("loc_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_49E")
    SetMapObjFrame(0xFF, "model05_mark_2", 0x0, 0x1)

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B7")
    SetChrFlags(0x9, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_4CB")

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB")
    ClearChrFlags(0x9, 0x80)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4CB")

    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x9, 0x100)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F6")
    Sound(129, 1, 100, 0)

    label("loc_4F6")

    Return()

    # Function_2_3FD end

    def Function_3_4F7(): pass

    label("Function_3_4F7")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CC")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x0, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x0, 0x0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x0, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_5CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E8")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_5E8")

    Return()

    # Function_3_4F7 end

    def Function_4_5EA(): pass

    label("Function_4_5EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    LoadChrToIndex("monster/ch75150.itc", 0x23)
    LoadChrToIndex("monster/ch75150.itc", 0x24)
    LoadEffect(0x0, "event\\ev501_00.eff")
    SetChrPos(0x101, 13330, 0, 10, 90)
    SetChrPos(0x109, 12590, 0, 1200, 90)
    SetChrPos(0x103, 11580, 0, -830, 90)
    SetChrPos(0x104, 9960, 250, -1360, 90)
    SetChrPos(0x102, 10920, 0, 560, 90)

    def lambda_691():
        OP_95(0xFE, 43330, 0, 10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_691)
    Sleep(50)

    def lambda_6AE():
        OP_95(0xFE, 42590, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6AE)
    Sleep(50)

    def lambda_6CB():
        OP_95(0xFE, 41580, 0, -830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6CB)
    Sleep(50)

    def lambda_6E8():
        OP_95(0xFE, 39960, 250, -1360, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E8)
    Sleep(50)

    def lambda_705():
        OP_95(0xFE, 40920, 0, 560, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_705)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 50000, -2500, 0, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    BeginChrThread(0x8, 0, 0, 6)
    FadeToBright(1000, 0)
    OP_68(16390, 1850, 0, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17140, 0)
    OP_68(42880, 1850, 0, 12000)
    SetCameraDistance(25140, 12000)
    Sleep(9000)
    OP_0D()
    Fade(1000)
    OP_68(49940, 200, 0, 0)
    MoveCamera(90, 45, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(29320, 0)
    OP_68(49940, -450, 0, 7000)
    MoveCamera(90, 16, 0, 7000)
    SetCameraDistance(26460, 7000)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0002
    ChrTalk(
        0x109,
        "#0501F#6P这、这是……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x104,
        (
            "#0306F#12P该怎么说呢……\x01",
            "好诡异的地方啊。\x02\x03",

            "#0301F为什么礼拜堂的后面\x01",
            "会有这种地方啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0008F#6P是啊……\x02\x03",

            "作为七耀教会的遗迹来说，\x01",
            "感觉未免也太阴森了……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#0101F#6P那、那个地板上画的图案\x01",
            "到底是什么意思……？\x02\x03",

            "形状好像……眼睛一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        "#0201F#12P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9D8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9D8)
    Sleep(50)

    def lambda_9E8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E8)
    Sleep(50)

    def lambda_9F8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9F8)
    Sleep(50)

    def lambda_A08():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A08)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0007
    ChrTalk(
        0x101,
        "#0005F#5P怎么了，缇欧？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        "#0501F#5P想、想到什么了吗？\x02",
    )

    CloseMessageWindow()
    OP_64(0x103)
    Sleep(800)

    #C0009
    ChrTalk(
        0x103,
        (
            "#0208F#12P……看起来，这个地方\x01",
            "以前很有可能是某种\x01",
            "『仪式堂』。\x02\x03",

            "用来举行某种活祭之类仪式的\x01",
            "不祥之地……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        "#0107F#6P活、活祭……！？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        (
            "#0206F#12P嗯……地上那些暗红色的痕迹\x01",
            "大概就是残留的血迹。\x02\x03",

            "#0201F不过，不分析其成分的话，\x01",
            "也不能妄下定论……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        "#0301F#12P真是让人毛骨悚然的话题啊……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#0013F#5P但是，为什么……\x01",
            "教会的遗迹中会有这种地方……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(100)
    Sound(935, 0, 100, 0)
    Sleep(500)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_C67():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C67)
    Sleep(50)

    def lambda_C77():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C77)
    Sleep(50)

    def lambda_C87():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C87)
    Sleep(50)

    def lambda_C97():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C97)
    Sleep(50)

    def lambda_CA7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CA7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0014
    ChrTalk(
        0x109,
        "#0507F#6P又、又来了吗……！？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        "#0007F#6P可恶……这次是什么！？\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(1500)
    OP_68(49940, 1150, 0, 1500)
    SetCameraDistance(16020, 1500)
    OP_6F(0x11)
    Fade(1000)
    SetCameraDistance(15520, 0)
    Sound(934, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 50000, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    BeginChrThread(0x101, 3, 0, 5)
    OP_68(49940, 1550, 0, 2500)
    SetCameraDistance(12520, 2500)
    Sleep(1500)
    BeginChrThread(0x8, 3, 0, 7)
    OP_6F(0x79)
    Fade(2000)
    Sound(868, 0, 100, 0)
    WaitChrThread(0x8, 3)
    OP_0D()
    Sleep(1000)
    OP_68(49940, 550, 0, 1000)
    MoveCamera(90, 12, 0, 1000)
    SetCameraDistance(19480, 1000)
    OP_6F(0x79)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(47940, 550, 0, 1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_EEE():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EEE)
    Sleep(50)

    def lambda_F06():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F06)
    Sleep(50)

    def lambda_F1E():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F1E)
    Sleep(50)

    def lambda_F36():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F36)
    Sleep(50)

    def lambda_F4E():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F4E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0016
    ChrTalk(
        0x101,
        "#0007F#6P这家伙是……！？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        "#0110F#6P#N恶、恶魔……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0018
    ChrTalk(
        0x103,
        (
            "#0207F#12P#N请务必小心……！\x01",
            "能感到很强的『灵压』……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0019
    ChrTalk(
        0x104,
        (
            "#0310F#12P#N喂喂，我们可不是\x01",
            "教会的驱魔师啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0020
    ChrTalk(
        0x109,
        "#0507F#6P要来了……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15980, 500)
    OP_68(50940, 1050, 0, 500)
    OP_82(0x0, 0x64, 0x1388, 0x1F4)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(500)
    EndChrThread(0x101, 0x3)
    Battle("BattleInfo_2BC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 8)
    Return()

    # Function_4_5EA end

    def Function_5_10EF(): pass

    label("Function_5_10EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1113")
    OP_82(0x64, 0x64, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_5_10EF")

    label("loc_1113")

    Return()

    # Function_5_10EF end

    def Function_6_1114(): pass

    label("Function_6_1114")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1130")
    OP_A1(0xFE, 0x4E2, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_6_1114")

    label("loc_1130")

    Return()

    # Function_6_1114 end

    def Function_7_1131(): pass

    label("Function_7_1131")

    ClearChrFlags(0xFE, 0x1)

    def lambda_113B():
        OP_98(0xFE, 0x0, 0xAF0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_113B)

    def lambda_1155():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1155)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_7_1131 end

    def Function_8_116A(): pass

    label("Function_8_116A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    OP_68(53090, 850, 0, 0)
    MoveCamera(90, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21650, 0)
    SetMapObjFrame(0xFF, "model05_mark_2", 0x0, 0x1)
    SetChrPos(0x101, 46890, 0, -70, 90)
    SetChrPos(0x109, 45620, 0, 1750, 90)
    SetChrPos(0x103, 45140, 0, -1890, 90)
    SetChrPos(0x102, 43000, 0, 620, 90)
    SetChrPos(0x104, 44170, 0, -680, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    OP_68(53090, -450, 0, 3000)
    OP_6F(0x1)
    OP_0D()
    OP_6F(0x10)

    #C0021
    ChrTalk(
        0x101,
        "#0006F#6P呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x109,
        "#0506F#6P总、总算是击退了……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0023
    ChrTalk(
        0x102,
        (
            "#0106F#6P#N刚、刚才那个东西……究竟是什么？\x02\x03",

            "#0101F好像是教会圣典中\x01",
            "所记载的『恶魔』……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        (
            "#0206F#12P先不说是不是真的……\x01",
            "总之，它的灵压可真是相当恐怖……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#0303F#12P亡灵、骸骨、怪物，\x01",
            "最后竟然连恶魔都出现了……\x02\x03",

            "#0301F这个遗迹到底是怎么回事啊……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(61640, 1250, -50, 2000)
    MoveCamera(90, 16, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(26460, 2000)
    Sleep(2500)

    #C0026
    ChrTalk(
        0x101,
        (
            "#0001F#5P……从位置上来看，\x01",
            "那上面应该就是钟楼了。\x02\x03",

            "总之，去调查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x109,
        "#0501F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_37()
    SetChrPos(0x0, 43000, 250, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC0, 5)
    OP_29(0x49, 0x1, 0x3)
    Sleep(500)
    OP_E0(0x2)
    EventEnd(0x5)
    Return()

    # Function_8_116A end

    def Function_9_14FC(): pass

    label("Function_9_14FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 1)), scpexpr(EXPR_END)), "loc_1506")
    Return()

    label("loc_1506")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【消灭】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_15D2"),
        (SWITCH_DEFAULT, "loc_15E9"),
    )


    label("loc_15D2")

    Sleep(500)
    OP_90(0x0, 44860, 250, -10, 270)
    EventEnd(0x5)
    Return()

    label("loc_15E9")

    Battle("BattleInfo_300", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(44860, 1250, -10, 0)
    OP_90(0x0, 44860, 250, -10, 270)
    OP_90(0x1, 44860, 250, -10, 270)
    OP_90(0x2, 44860, 250, -10, 270)
    OP_90(0x3, 44860, 250, -10, 270)
    OP_90(0x4, 44860, 250, -10, 270)
    OP_90(0x5, 44860, 250, -10, 270)
    OP_90(0x6, 44860, 250, -10, 270)
    OP_90(0x7, 44860, 250, -10, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_16AB"),
        (1, "loc_16AE"),
        (SWITCH_DEFAULT, "loc_16B1"),
    )


    label("loc_16AB")

    EventEnd(0x5)
    Return()

    label("loc_16AE")

    OP_B7(0x0)
    Return()

    label("loc_16B1")

    FadeToDark(0, 0, -1)
    OP_68(49680, 1550, -270, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "消灭了通缉魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0030
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber('战术书·十', 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17F4")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 49520, 250, 1990, 180)
    SetChrPos(0x102, 51420, 250, 610, 252)
    SetChrPos(0x103, 50700, 250, -1620, 324)
    SetChrPos(0x104, 48340, 250, -1620, 36)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17DE")
    SetChrPos(0x10A, 47620, 250, 610, 108)
    Jump("loc_17EF")

    label("loc_17DE")

    SetChrPos(0x109, 47620, 250, 610, 108)

    label("loc_17EF")

    Jump("loc_1838")

    label("loc_17F4")

    SetChrPos(0x101, 49520, 250, 2009, 180)
    SetChrPos(0x102, 51520, 250, -10, 270)
    SetChrPos(0x103, 49520, 250, -2009, 0)
    SetChrPos(0x104, 47520, 250, -10, 90)

    label("loc_1838")

    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1886")

    #C0031
    ChrTalk(
        0x101,
        (
            "#5P#0005F战术书……\x01",
            "好像是本很古老的书籍啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BE")

    label("loc_1886")


    #C0032
    ChrTalk(
        0x101,
        (
            "#5P#0000F战术书……\x01",
            "这好像也是一本很古老的书籍啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BE")


    #C0033
    ChrTalk(
        0x104,
        (
            "#6P#0303F似乎记载了关于组合战技\x01",
            "的使用方法呢。\x02\x03",

            "#0300F大小姐和阿缇使用的战技\x01",
            "和这里写的\x01",
            "不是很接近吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x102,
        (
            "#11P#0105F哦，好像的确如此呢。\x02\x03",

            "#0100F缇欧，要不要试试呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        "#12P#0202F好的，试试看吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19E4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_19E4")

    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x1, 0x14D)
    AddCraft(0x2, 0x14D)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧和艾莉习得了组合战技\x01\x07\x02",

            "『冷酷冰狱』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人各自消耗１００点ＣＰ，\x01",
            "便可以施展威力强大的组合技攻击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x79, 1)
    SetScenarioFlags(0xD8, 7)
    OP_29(0x2B, 0x4, 0x10)
    OP_29(0x2B, 0x4, 0x2)
    OP_29(0x2B, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_DE(0x21, 0x0)
    EventEnd(0x5)
    Return()

    # Function_9_14FC end

    SaveToFile()

Try(main)
