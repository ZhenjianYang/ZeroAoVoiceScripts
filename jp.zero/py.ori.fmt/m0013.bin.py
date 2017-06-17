from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0013.bin",                # FileName
        "m0013",                    # MapName
        "m0013",                    # Location
        0x0067,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 103, 0, 3, 0, 4],
    )

    BuildStringList((
        "m0013",                  # 0
        "ボス",                   # 1
        "ヨナの声",               # 2
        "ヨナの声",               # 3
        "bm0012",                 # 4
        "bm0012",                 # 5
    ))

    ATBonus("ATBonus_324", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_404", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 6, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 10, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 8, 14, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_468", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm0012", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_3C4", "ed7401", "ed7403", "ATBonus_324"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_424", 0x0012, 22, 6, 0, 0, 1, 0, 0, "bm0012", 0x00000000, 100, 0, 0, 0,
        (
            ("ms77600.dat", 0, 0, 0, 0, 0, "ms67001.dat", 0, "MonsterBattlePostion_3E4", "MonsterBattlePostion_3C4", "ed7402", "ed7403", "ATBonus_324"),
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
        "monster/ch66150.itc",               # 10
        "monster/ch66150.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(0,       0,       750,     0x18500B4,    "BattleInfo_468", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 6,   0.0,                   -7.5,                  -1.0,                  56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  2.5,                   0.20000000298023224,   1.0])
    DeclEvent(0x0040, 0, 5,   0.0,                   0.0,                   -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -0.0,                  0.25,                  1.0])
    DeclEvent(0x0000, 0, 15,  0.0,                   9.5,                   -1.0,                  64.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -4.75,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 16,  0.0,                   -10.5,                 -1.5,                  64.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  5.25,                  0.30000001192092896,   1.0])

    DeclActor(102770,  200,     -60,     1200,    102770,  1700,    -60,     0x007C, 0,  17, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 1

    ScpFunction((
        "Function_0_50C",          # 00, 0
        "Function_1_528",          # 01, 1
        "Function_2_547",          # 02, 2
        "Function_3_566",          # 03, 3
        "Function_4_590",          # 04, 4
        "Function_5_6A6",          # 05, 5
        "Function_6_8E2",          # 06, 6
        "Function_7_DBA",          # 07, 7
        "Function_8_E69",          # 08, 8
        "Function_9_124A",         # 09, 9
        "Function_10_58F9",        # 0A, 10
        "Function_11_5926",        # 0B, 11
        "Function_12_5951",        # 0C, 12
        "Function_13_59B0",        # 0D, 13
        "Function_14_5A0F",        # 0E, 14
        "Function_15_5AB9",        # 0F, 15
        "Function_16_5BC9",        # 10, 16
        "Function_17_5CE9",        # 11, 17
    ))


    def Function_0_50C(): pass

    label("Function_0_50C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_527")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_50C")

    label("loc_527")

    Return()

    # Function_0_50C end

    def Function_1_528(): pass

    label("Function_1_528")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_546")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_528")

    label("loc_546")

    Return()

    # Function_1_528 end

    def Function_2_547(): pass

    label("Function_2_547")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_565")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_547")

    label("loc_565")

    Return()

    # Function_2_547 end

    def Function_3_566(): pass

    label("Function_3_566")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_580")
    Event(0, 9)

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_58F")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 8)

    label("loc_58F")

    Return()

    # Function_3_566 end

    def Function_4_590(): pass

    label("Function_4_590")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5CA")
    SetChrFlags(0xB, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_5DE")

    label("loc_5CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DE")
    ClearChrFlags(0xB, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_5DE")

    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0xB, 0x100)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66F")
    SetMapFlags(0x2000)
    SetMapFlags(0x8000000)
    OP_E0(0x2)
    Jump("loc_679")

    label("loc_66F")

    ClearMapFlags(0x2000)
    ClearMapFlags(0x8000000)

    label("loc_679")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68D")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_68D")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A5")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_6A5")

    Return()

    # Function_4_590 end

    def Function_5_6A6(): pass

    label("Function_5_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 0)), scpexpr(EXPR_END)), "loc_6B0")
    Return()

    label("loc_6B0")

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

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型の魔獣が徘徊#4Rはいかい#している。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【退治する】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_792"),
        (SWITCH_DEFAULT, "loc_7A9"),
    )


    label("loc_792")

    Sleep(500)
    OP_90(0x0, 200, 0, -8530, 0)
    EventEnd(0x5)
    Return()

    label("loc_7A9")

    Battle("BattleInfo_468", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(200, 1000, -8530, 0)
    OP_90(0x0, 200, 0, -8530, 0)
    OP_90(0x1, 200, 0, -8530, 0)
    OP_90(0x2, 200, 0, -8530, 0)
    OP_90(0x3, 200, 0, -8530, 0)
    OP_90(0x4, 200, 0, -8530, 0)
    OP_90(0x5, 200, 0, -8530, 0)
    OP_90(0x6, 200, 0, -8530, 0)
    OP_90(0x7, 200, 0, -8530, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_86B"),
        (1, "loc_86E"),
        (SWITCH_DEFAULT, "loc_871"),
    )


    label("loc_86B")

    EventEnd(0x5)
    Return()

    label("loc_86E")

    OP_B7(0x0)
    Return()

    label("loc_871")

    EventBegin(0x1)
    SetChrFlags(0xB, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_0D()
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手配魔獣を退治した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x79, 0)
    OP_29(0x25, 0x4, 0x10)
    OP_29(0x25, 0x4, 0x2)
    OP_29(0x25, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_5_6A6 end

    def Function_6_8E2(): pass

    label("Function_6_8E2")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00251.itc", 0x21)
    LoadChrToIndex("monster/ch77650.itc", 0x22)
    LoadChrToIndex("chr/ch00056.itc", 0x23)
    LoadChrToIndex("chr/ch00256.itc", 0x24)
    LoadEffect(0x0, "event\\eva04_00.eff")
    OP_68(0, 700, -1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -700, 0, -7300, 0)
    SetChrPos(0x103, 700, 0, -7000, 0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 6000, 0, 180)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x8, 0xFF)

    def lambda_A07():
        OP_96(0xFE, 0x2BC, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A07)
    Sleep(50)

    def lambda_A24():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFF704, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A24)
    SetCameraDistance(20000, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)
    OP_6F(0x10)

    #C0003
    ChrTalk(
        0x101,
        "#12P#0000Fここは……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x103,
        (
            "#0204F#12P……どうやら終点のようですね。\x02\x03",

            "#0202F多分この近くに、\x01",
            "第３制御端末のある部屋が──\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AD8():
        OP_96(0xFE, 0x2BC, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AD8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x103, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 80, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    #C0005
    ChrTalk(
        0x101,
        "#12P#4S#0007Fティオ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x7D0)
    Fade(250)
    OP_68(0, 1700, -1000, 0)
    MoveCamera(50, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13500, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x1)

    def lambda_B9A():
        OP_9D(0xFE, 0x12C, 0x0, 0xFFFFFDA8, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B9A)
    Sound(814, 0, 100, 0)
    Sound(1011, 255, 100, 0)    #voice#Lloyd
    WaitChrThread(0x101, 1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    BeginChrThread(0x8, 3, 0, 7)
    OP_68(0, 1500, -3000, 500)
    MoveCamera(40, 13, 0, 500)
    SetCameraDistance(14500, 500)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x2)

    def lambda_C04():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFFEE08, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C04)
    Sound(854, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x2)

    def lambda_C2F():
        OP_9D(0xFE, 0x2BC, 0x0, 0xFFFFEC78, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C2F)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(42, 0, 100, 0)
    Sound(31, 0, 100, 0)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x8, 3)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    Sleep(500)

    #C0006
    ChrTalk(
        0x103,
        "#0207F#12Pこれは……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#0013F#6Pくそっ……\x01",
            "下層のヌシってところか！\x02\x03",

            "#0007Fティオ、何とかいけそうか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        "#0205F#12Pあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 900, 0, -5000, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0009
    ChrTalk(
        0x103,
        "#0201F#12Pはい……問題ありません！\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_D69():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D69)
    Sleep(50)

    def lambda_D81():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D81)
    Sleep(500)
    Battle("BattleInfo_424", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    Call(0, 8)
    Return()

    # Function_6_8E2 end

    def Function_7_DBA(): pass

    label("Function_7_DBA")

    SetChrChip(0x0, 0x8, 0x1E, 0x12C)

    def lambda_DC7():
        OP_9D(0xFE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DC7)
    Sound(812, 0, 100, 0)
    WaitChrThread(0x8, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0x0, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_4C(0x8, 0xFF)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x1F4, 0xBB8, 0x3E8)
    Sound(813, 0, 100, 0)
    Sleep(1000)
    CancelBlur(0)
    Return()

    # Function_7_DBA end

    def Function_8_E69(): pass

    label("Function_8_E69")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00251.itc", 0x21)
    LoadChrToIndex("monster/ch77650.itc", 0x22)
    LoadChrToIndex("chr/ch00056.itc", 0x23)
    LoadChrToIndex("chr/ch00256.itc", 0x24)
    OP_68(0, 1000, -4000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x101, -800, 0, -4000, 0)
    SetChrPos(0x103, 700, 0, -4200, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetCameraDistance(16000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0010
    ChrTalk(
        0x101,
        "#12P#0006Fふう、何とか撃退できたか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x101, 0x103, 500)

    #C0011
    ChrTalk(
        0x101,
        (
            "#6P#0001Fティオ、大丈夫か？\x01",
            "ずいぶん苦戦しちゃったけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0012
    ChrTalk(
        0x103,
        (
            "#0204F#11Pいえ……問題ないです。\x02\x03",

            "#0202Fロイドさんの方は大丈夫ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#6P#0004Fはは、ランディ曰く\x01",
            "防御のテクニックだけは\x01",
            "ちょっとしたモンらしいからさ。\x02\x03",

            "#0001Fしかし、ランディとエリィがいたら\x01",
            "もっと効率的に戦えたんだろうな。\x02\x03",

            "#0006F日頃から、どれだけあの２人に\x01",
            "助けられていたか身に沁みたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        "#0202F#11P……ふふ………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0015
    ChrTalk(
        0x101,
        "#6P#0011Fな、なんか変なことを言ったか？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        (
            "#0204F#11P……いえ。\x01",
            "こちらの事ですから。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(300)

    #C0017
    ChrTalk(
        0x103,
        (
            "#0202F#5P《第３制御端末》は\x01",
            "右にある扉の中だと思います。\x02\x03",

            "早速、起動させてから\x01",
            "ヨナに通信で連絡しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#6P#0000Fああ……そうするか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_37()
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 0, 0, -4000, 0)
    SetScenarioFlags(0xA1, 2)
    OP_E0(0x2)
    EventEnd(0x5)
    Return()

    # Function_8_E69 end

    def Function_9_124A(): pass

    label("Function_9_124A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00202.itc", 0x1E)
    LoadChrToIndex("apl/ch50092.itc", 0x1F)
    LoadChrToIndex("apl/ch50011.itc", 0x20)
    LoadChrToIndex("apl/ch50324.itc", 0x21)
    LoadChrToIndex("apl/ch50326.itc", 0x22)
    LoadChrToIndex("apl/ch50218.itc", 0x23)
    LoadEffect(0x0, "event\\eva06_00.eff")
    SoundLoad(806)
    SoundLoad(840)
    SoundLoad(905)
    OP_68(101500, 1000, 0, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 92000, 150, -300, 90)
    SetChrPos(0x103, 92000, 150, 300, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x13)
    SetChrFlags(0x9, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis041.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis042.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis020.itp")
    OP_68(97500, 1000, 0, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    def lambda_13DE():
        OP_96(0xFE, 0x1750C, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13DE)

    def lambda_13F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13F8)
    Sleep(400)

    def lambda_140C():
        OP_96(0xFE, 0x1750C, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_140C)

    def lambda_1426():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1426)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)

    #C0019
    ChrTalk(
        0x101,
        "#0005F#6Pこの端末が……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#0202F《第３制御端末》ですね。\x02\x03",

            "ここと、ヨナが勝手に利用している\x01",
            "《第８制御端末》の２箇所から\x01",
            "ハッキングを仕掛ける段取りです。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0021
    ChrTalk(
        0x101,
        (
            "#12P#0004Fなるほど。\x02\x03",

            "#0000Fそれじゃあ、ヨナに連絡するか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0022
    ChrTalk(
        0x103,
        (
            "#0203Fはい、お願いします。\x02\x03",

            "#0200Fエリィさんたちからも\x01",
            "連絡があるかもしれませんから\x01",
            "わたしのエニグマを使ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#12P#0000Fああ、分かった。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはティオのエニグマを受け取った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_68(103000, 1000, 0, 3000)
    MoveCamera(55, 15, 0, 3000)
    SetCameraDistance(21000, 3000)
    OP_93(0x103, 0x5A, 0x1F4)

    def lambda_1640():
        OP_95(0xFE, 102000, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1640)
    Sleep(200)
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_1664():
        OP_95(0xFE, 101200, 0, -1700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1664)
    WaitChrThread(0x103, 1)
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 102300, 250, 0, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)
    SetMapObjFrame(0x3, "m00gim02", 0x2, "open")
    Sound(72, 0, 100, 0)
    OP_6F(0x79)
    Sleep(800)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(902, 0, 100, 0)
    Sleep(2800)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0025
    AnonymousTalk(
        0x101,
        (
            "#0000Fヨナ？\x01",
            "こちらロイドだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アンタか。\x01",
            "もう着いたのかよ？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0027
    AnonymousTalk(
        0x101,
        (
            "#0000Fああ、ちょうど今、\x01",
            "ティオが端末を起動している。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オッケーオッケー。\x01",
            "そんじゃあこっちも始めるぜ。\x02\x03",

            "そうだアンタ。\x01",
            "エニグマの通信モードの\x01",
            "スピーカーをＯＮにしなよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0029
    AnonymousTalk(
        0x101,
        "#0005FスピーカーをＯＮ……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x103, 0x2)
    Sleep(300)
    SetMessageWindowPos(120, 30, -1, -1)

    #A0030
    AnonymousTalk(
        0x103,
        (
            "#0200Fエニグマの裏側にある\x01",
            "赤いスイッチを押してください。\x02\x03",

            "そうすると通話相手の声が\x01",
            "他の人にも聞こえますから。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0031
    AnonymousTalk(
        0x101,
        "#0000Fこうか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは言われた通りに操作し、\x01",
            "エニグマを端末の横に置いた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x9, 102600, 700, -1500, 0)
    SetChrPos(0xA, 102600, -500, -1500, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Sound(31, 0, 100, 0)
    Sound(42, 0, 100, 0)
    Sleep(800)

    #C0033
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P──ハッ。\x01",
            "聞こえるようになっただろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#6P#0000Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#0203F#5P消費ＥＰが多めなので\x01",
            "あまり推奨はされていませんが\x01",
            "何とか保つでしょう。\x02\x03",

            "#0200F──ヨナ。\x01",
            "こちらの準備は完了です。\x02\x03",

            "あとの段取りは？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2Pああ、こっちはとっくに\x01",
            "囮になるべく動き回ってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P《仔猫#4Rキティ#》が現れたら\x01",
            "連絡するから対応してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0200F#5P了解しました。\x01",
            "それまで待機します。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2Pよろしく頼んだぜ！\x02",
        )
    )

    CloseMessageWindow()
    Sound(825, 0, 80, 0)
    StopBGM(0x1F40)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x103)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0040
    ChrTalk(
        0x101,
        (
            "#12P#0005F──えっと。\x01",
            "これで準備は終わりなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#0204F#5Pええ、後はひたすら待機です。\x02\x03",

            "ハッキングを始めた後も\x01",
            "わたし一人で十分ですし……\x02\x03",

            "#0211F……わたしが一人で行くと\x01",
            "言った理由が分かりましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#12P#0006Fな、なるほど。\x02\x03",

            "#0000Fでも実際、ここに来るまでに\x01",
            "結構大変だったわけだし……\x02\x03",

            "結果オーライで良かったじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#0203F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#12P#0012Fその、はは……\x01",
            "（困ったな、話題がないぞ。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x190)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)

    #C0045
    ChrTalk(
        0x101,
        (
            "#6P#0005Fそういえば……\x01",
            "《みっしぃ》だっけか？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)

    #A0046
    AnonymousTalk(
        0x101,
        (
            "#0002F随分、気に入ったんだな。\x01",
            "そんなストラップまで付けて。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0047
    AnonymousTalk(
        0x103,
        (
            "#0204Fええ……\x01",
            "そうかもしれませんね。\x02\x03",

            "わたしはあまり物には\x01",
            "執着しない性質ですけど……\x02\x03",

            "#0202F不思議とこれだけは\x01",
            "ずっと持ち続けていますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x101, 0x103, 500)

    #C0048
    ChrTalk(
        0x101,
        (
            "#12P#0005Fこれ、ここに来てから\x01",
            "買ったものじゃないのか？\x02\x03",

            "たしかクロスベルの\x01",
            "ご当地キャラクターだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        (
            "#0204F#5Pこれは貰ったものです。\x02\x03",

            "５年くらい前に、ガイさんから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0050
    ChrTalk(
        0x101,
        "#12P#0011F#4S───え。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x103,
        (
            "#0203F#5Pガイ・バニングス……\x02\x03",

            "#0202Fロイドさんのお兄さんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#12P#0008Fえ、ああ、いや……\x01",
            "……もちろんそうだけど……\x02\x03",

            "#0011Fティオって──\x01",
            "兄貴と面識あったのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        "#0204F#5Pはい。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#12P#0006Fし、知らなかった……\x02\x03",

            "#0002F何だよ、だったらもっと\x01",
            "早く言ってくれればいいのに！\x02\x03",

            "#0005Fでも、ティオは確か\x01",
            "レマン自治州から来たんだろ？\x02\x03",

            "どうして兄貴と──\x02",
        )
    )

    CloseMessageWindow()
    OP_C7(0x0, 0x800)
    FadeToDark(800, 0, -1)
    OP_C9(0x3, 0x3, 0xAAFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(300)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("")

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "しばらく旅に出るって……\x01",
            "そんないきなり。\x02\x03",

            "一体どこに行くつもりなのさ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "レミフェリア公国だ。\x02\x03",

            "なァに、しばらくと言っても\x01",
            "２ヶ月くらいで済むだろう。\x02\x03",

            "実はな……\x01",
            "とびっきり可愛い女の子を\x01",
            "エスコートしながらの旅なんだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_END)), "loc_2402")
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_C9(0x2, 0x3, 0xAAFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(300)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("")

    #A0057
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "ティオ……\x01",
            "前にこの病院に？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, 130, -1, -1)
    SetChrName("")

    #A0058
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "……ええ。\x02\x03",

            "６年ほど前のことです。\x02\x03",

            "黙っているつもりでは\x01",
            "なかったんですけど……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Jump("loc_241E")

    label("loc_2402")

    FadeToBright(1000, 0)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x3, 0x3)

    label("loc_241E")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0059
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあれは……\x01",
            "ティオの事だったのか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        (
            "#0203F#5P多分、そうです。\x02\x03",

            "#0202Fわたしが９歳の時……\x02\x03",

            "レミフェリアにある実家まで\x01",
            "ガイさんに送ってもらった時ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#12P#0002Fレミフェリア……\x02\x03",

            "ティオの出身はそこなのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        (
            "#0202F#5Pはい。\x02\x03",

            "#0204Fといっても、あまり思い入れが\x01",
            "ある故郷ではありませんが……\x02\x03",

            "もうほとんど\x01",
            "捨ててしまった場所ですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#12P#0005Fえ……\x02\x03",

            "#0001Fその、ティオのご両親は？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        (
            "#0206F#5P元気だと思いますよ……？\x02\x03",

            "３年前に家を出てから\x01",
            "ほとんど連絡を取ってませんけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#12P#0001F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#0203F#5P──ある事情で\x01",
            "わたしは５歳くらいの時から\x01",
            "行方不明の身の上でした。\x02\x03",

            "ガイさんに保護され……\x01",
            "衰弱していたわたしはウルスラ病院に\x01",
            "半年ほど入院していました。\x02\x03",

            "#0202Fそして何とか回復した後……\x01",
            "実家まで送ってもらったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそう、だったのか……\x02\x03",

            "#0008Fでも……\x01",
            "どうしてまた家を出たんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        "#0204F#5Pふふっ……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x103, 0x20)

    def lambda_27CB():
        OP_96(0xFE, 0x18ED4, 0xFA, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27CB)

    def lambda_27E5():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_27E5)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    SetChrSubChip(0x103, 0x2)
    ClearChrFlags(0x103, 0x20)
    Sleep(500)

    #C0069
    ChrTalk(
        0x103,
        (
            "#0204F#5P──ロイドさん。\x02\x03",

            "#0202Fわたしが普通の人間と\x01",
            "少し違うのは分かりますよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0070
    ChrTalk(
        0x101,
        "#12P#0007F違うなんて……！\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        (
            "#0202F#5P事実ですから。\x02\x03",

            "#0203F外界の事象に関して……\x01",
            "わたしは普通の人間の\x01",
            "数倍の感応力を持っています。\x02\x03",

            "普通の人には聞き取れない微かな音。\x02\x03",

            "普通の人には見えない導力波の流れ。\x02\x03",

            "普通の人には感じられない属性の気配。\x02\x03",

            "#0208F#40Wそして……人の感情や心のゆらぎまで。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        "#12P#0005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#0208F#5P日曜学校に通っていても……\x01",
            "わたしは一人ぼっちでした。\x02\x03",

            "周りの子たちとは違ったものを見て\x01",
            "違ったものを感じて……\x02\x03",

            "そして見えない悪意や好奇心も\x01",
            "はっきりと感じ取れてしまう……\x02\x03",

            "#0206F両親はわたしを愛してくれましたが\x01",
            "……やはり限界があったんでしょう。\x02\x03",

            "次第に家の空気が張り詰めて……\x01",
            "わたしは気付いてしまいました。\x02\x03",

            "#0202Fああ──\x01",
            "帰って来なければ良かったって。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#12P#0013Fっ……！\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#0204F#5Pそして気付いたら……\x01",
            "わたしは列車に乗っていました。\x02\x03",

            "共和国を経由して\x01",
            "クロスベルに向かう列車に。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#12P#0006Fそうか……\x02\x03",

            "#0008Fティオは……\x01",
            "兄貴に会いに来たんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        (
            "#0208F#5P……そうかもしれません。\x02\x03",

            "#0206Fそのマスコットを\x01",
            "プレゼントしてくれた時に\x01",
            "ガイさんが言ったんです。\x02\x03",

            "#0202F『──安心しろ。\x01",
            "  きっとお前は幸せになれる。』\x02\x03",

            "『もし、そうならなかったら\x01",
            "  いつでも俺を呼んでくれ。』\x02\x03",

            "#0204F『お前を不幸にする原因を\x01",
            "  一緒にぶっ飛ばしてやるからよ！』\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#12P#0012Fはは、いかにも\x01",
            "兄貴が言いそうな言葉だけど……\x02\x03",

            "#0008F……でも……\x01",
            "ちょうどその頃に兄貴は……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        "#0203F#5P……………………（コクン）\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x103, 0x20)

    def lambda_2DB9():
        OP_96(0xFE, 0x18F9C, 0xFA, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2DB9)

    def lambda_2DD3():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2DD3)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x20)
    Sleep(500)

    #C0080
    ChrTalk(
        0x103,
        (
            "#0208F#5P──途方に暮れていたわたしは\x01",
            "エプスタイン財団の人と知り合って……\x02\x03",

            "その感応力を見込まれて、\x01",
            "当時発足したばかりの魔導杖の\x01",
            "開発チームにスカウトされました。\x02\x03",

            "#0204Fそしてレマン自治州に渡り、\x01",
            "財団の研究所で３年間過ごして……\x02\x03",

            "#0202Fそして３ヶ月前、\x01",
            "再びクロスベルに戻ってきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        "#12P#0001F………ティオ……………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Fade(500)
    OP_68(202400, 1000, 0, 0)
    MoveCamera(310, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 202200, 0, -1700, 0)
    SetChrPos(0x103, 202400, 250, 0, 90)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x9, 203100, 750, -1300, 0)
    SetCameraDistance(19000, 1500)
    SetChrFlags(0x101, 0x4)

    def lambda_2FDC():
        OP_95(0xFE, 202200, 100, -400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FDC)
    Sleep(800)
    SetChrSubChip(0x103, 0x6)
    Sleep(150)
    SetChrSubChip(0x103, 0x7)
    WaitChrThread(0x101, 1)
    OP_6F(0x10)
    Fade(250)
    SetChrFlags(0x101, 0x8)
    SetChrSubChip(0x103, 0xA)
    OP_0D()
    SetChrSubChip(0x103, 0xB)
    Sleep(100)
    SetChrSubChip(0x103, 0xC)
    Sleep(100)
    SetChrSubChip(0x103, 0xD)
    Sleep(100)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x103, 0xE)
    Sleep(100)
    SetChrSubChip(0x103, 0xD)
    Sleep(100)
    SetChrSubChip(0x103, 0xC)
    Sleep(500)

    #C0082
    ChrTalk(
        0x103,
        "#0205F#5P#40W……あ………\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#6P#0006F……ゴメンな。\x01",
            "突然いなくなっちまうような\x01",
            "バカ兄貴で……\x02\x03",

            "#0008F女の子との約束を守らないなんて\x01",
            "ホント、兄貴らしくもない……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        "#0208F#5P#40W………ロイドさん……………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(806, 2, 100, 0)
    Sleep(500)
    StopBGM(0x7D0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0x101, 0x8)
    SetChrSubChip(0x103, 0x6)
    OP_0D()

    def lambda_3175():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3175)
    Sleep(150)
    SetChrSubChip(0x103, 0x7)
    Sleep(300)

    #C0085
    ChrTalk(
        0x101,
        "#0005F#5Pあ……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#0200F#5P……ヨナみたいですね。\x02",
    )

    CloseMessageWindow()
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7524", 0)
    Sleep(300)

    #C0087
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6P《仔猫》が現れた……！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6P今、ちょうどこっちが用意した\x01",
            "エサを発見したところだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6P追い込んでいくから\x01",
            "サポートを始めてくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x103,
        "#0203F#5P分かりました。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#0003F#5P……俺は高見の見物か……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0092
    ChrTalk(
        0x101,
        (
            "#6P#0001F──ティオ。\x01",
            "無茶だけはするなよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        "#0202F#11Pはい……心配ご無用です。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x6)
    Sleep(100)
    SetChrSubChip(0x103, 0x5)
    Sleep(100)
    SetChrSubChip(0x103, 0x4)
    Sleep(100)
    SetChrSubChip(0x103, 0x3)
    Sleep(1000)
    SetChrSubChip(0x103, 0x4)
    Sleep(100)
    SetChrSubChip(0x103, 0x5)
    Sound(1278, 255, 100, 0)    #voice#Tio
    Sleep(1000)
    Sound(1280, 255, 100, 0)    #voice#Tio
    Sleep(1500)
    SetCameraDistance(18500, 3000)
    PlayEffect(0x0, 0x0, 0x103, 0x140, 0, 1250, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(840, 2, 100, 0)
    BeginChrThread(0x103, 3, 0, 10)
    Sound(850, 0, 100, 0)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x348)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis122.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis043.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis044.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis045.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_68(302400, 1000, 0, 0)
    MoveCamera(310, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(0, 0)
    EndChrThread(0x103, 0x3)
    SetChrSubChip(0x103, 0x0)
    Sleep(500)

    #A0094
    AnonymousTalk(
        0x103,
        (
            "#0203Fネットワーク上のリソースの\x01",
            "第二境界領域に潜伏開始。\x02\x03",

            "#0200F《仔猫》が来るのを待ちます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("ヨナの声")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アイアイ・マム。\x02\x03",

            "って──おいおい、マジデスカ！？\x02\x03",

            "《仔猫》のヤツ……\x01",
            "もうプロテクトを解除しやがった！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(905, 2, 100, 0)
    Sound(903, 0, 100, 0)
    OP_C9(0x1, 0x0, 0xFFFC0860, 0xFFFF8AD0, 0x0)
    OP_C9(0x1, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x1, 0x2, 0x0, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x1, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    SetChrName("ヨナの声")

    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "うわああ、せっかく用意した\x01",
            "美味しい情報#4Rエ サ#が一瞬で……！\x02\x03",

            "し、信じられねえ……！\x01",
            "どうやって仕掛けてるんだよ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0097
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0201F落ち着いて、ヨナ。\x02\x03",

            "恐らく圧倒的な処理能力で\x01",
            "力任せに進んでいるだけでしょう。\x02\x03",

            "#0203F焦らず、２歩先を読んで\x01",
            "こちらへと誘導してください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("ヨナの声")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クソ、無茶言いやがる！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(904, 0, 100, 0)
    OP_C9(0x2, 0x0, 0xFFF97050, 0xFFFEEE90, 0x0)
    OP_C9(0x2, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x2, 0x2, 0x0, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x2, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("ヨナの声")

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第４ターミナル、第１７ターミナル、\x01",
            "市庁舎のメインターミナルを通過……\x02",
        )
    )

    CloseMessageWindow()

    #A0100
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第２５ターミナルに追い込んだ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(906, 0, 100, 0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis046.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis047.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis047.itp")
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("ヨナの声")

    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そっちの領域に行ったぞ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0102
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0202F──確認しました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(904, 0, 100, 0)
    OP_C9(0x0, 0x0, 0xFFFE0430, 0xFFFE2B40, 0x0)
    OP_C9(0x0, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x0, 0x2, 0x0, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x0, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    Sleep(500)
    SetMessageWindowPos(300, 140, -1, -1)

    #A0103
    AnonymousTalk(
        0x103,
        (
            "#0205Fこれが《仔猫》……\x02\x03",

            "確かに速い……速すぎる……！\x02\x03",

            "#0201F《エイオンシステム》解放！\x01",
            "複数同時並列処理に入ります……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1203, 255, 100, 0)    #voice#Tio
    Sleep(800)
    CreatePortrait(3, 0, 0, 480, 16, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C9(0x1, 0x0, 0xFFF97050, 0xFFFC5680, 0x0)
    OP_C9(0x1, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x1, 0x2, 0x0, 0x0, 0x0)
    OP_C9(0x2, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x2, 0x2, 0x0, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    Sound(907, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    CreatePortrait(0, 0, 256, 480, 272, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C9(0x2, 0x0, 0xFFF8FB20, 0xFFFF7748, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_C9(0x1, 0x4, 0x0, 0x0, 0x0)
    OP_C9(0x1, 0x0, 0xFFFF15A0, 0xFFFD67F0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x1, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis117.itp")
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x0, 0x0)
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis048.itp")
    Sleep(500)
    SetChrName("ヨナの声")

    #A0104
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こちらも確認──\x01",
            "おおっ、いい流れじゃん！\x02\x03",

            "このまま行けば、そっちだけで\x01",
            "《仔猫》を捕まえられるんじゃね！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 150, -1, -1)

    #A0105
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0206Fいえ……あなたや《仔猫》と違って\x01",
            "わたしは純粋なハッカーではありません。\x02\x03",

            "《エイオン》がダウンしたら\x01",
            "さすがに追いつけないでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("ヨナの声")

    #A0106
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クソッ、だったらどうすんだよ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 150, -1, -1)

    #A0107
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0203F──ダウン覚悟で限界まで処理を高めて\x01",
            "《仔猫》の退路を塞ぎます。\x02\x03",

            "#0201F恐らく、《仔猫》はもう一度、\x01",
            "そちらの領域に跳躍#4Rシフト#するはずです。\x02\x03",

            "タイミングを見計らって\x01",
            "コンマ１秒以内で捕まえてください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("ヨナの声")

    #A0108
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああもう……\x01",
            "わかった、やればいいんだろ！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 90, -1, -1)

    #A0109
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0204Fそれでは……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1281, 255, 100, 0)    #voice#Tio
    Sound(831, 0, 100, 0)
    Sound(506, 0, 100, 0)
    Sleep(2000)
    Sound(908, 0, 100, 0)
    FadeToDark(0, 16777215, -1)
    OP_0D()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x4, 0x0, 0x0, 0x0)
    CreatePortrait(1, 0, 0, 480, 16, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    Sleep(1000)
    OP_C9(0x2, 0x0, 0xFFFC5680, 0xFFFF9E58, 0x0)
    OP_C9(0x2, 0x1, 0x5DC, 0x5DC, 0x0)
    OP_C9(0x3, 0x0, 0xFFFC5680, 0xFFFF9E58, 0x0)
    OP_C9(0x3, 0x1, 0x5DC, 0x5DC, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_C9(0x2, 0x0, 0xFFFEA070, 0xFFFE5250, 0x5DC)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x3, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    Sleep(1000)
    FadeToBright(0, 16777215)
    OP_0D()
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis049.itp")
    Sound(903, 0, 100, 0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    SetMessageWindowPos(200, 170, -1, -1)

    #A0110
    AnonymousTalk(
        0x103,
        "#0201F#4S──今です！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(907, 0, 100, 0)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis118.itp")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis116.itp")
    OP_C9(0x1, 0x0, 0xFFF8AD00, 0xFFFD19D0, 0x0)
    OP_C9(0x1, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    CreatePortrait(2, 0, 0, 480, 16, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    CreatePortrait(3, 0, 256, 480, 272, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetMessageWindowPos(250, 150, -1, -1)
    SetChrName("ヨナの声")

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x18),
            "#4S#1Kそこだあああっ！！\x02",
        )
    )

    Sleep(1600)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(906, 0, 100, 0)
    Sound(813, 0, 100, 0)
    OP_24(0x389)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFD19D0, 0x0)
    OP_C9(0x0, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_C9(0x0, 0x1, 0x3E8, 0x3E8, 0x3E8)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x3E8)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFDCD8, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x2328, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFE0C0, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x1F40, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFE4A8, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x1B58, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFEC78, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x1388, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x0, 0x0)
    SetMessageWindowPos(250, 10, -1, -1)
    SetChrName("ヨナの声")

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "よっしゃあああ！\x01",
            "捕まえたぜええええっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(202400, 1000, 0, 0)
    MoveCamera(310, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 202200, 0, -1700, 45)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sound(840, 2, 100, 0)
    StopBGM(0x1770)

    #C0113
    ChrTalk(
        0x101,
        "#6P#0005Fや、やったのか……？\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        (
            "#0204F#5P#30Wええ……そうみたいですね。\x02\x03",

            "#0208F#40Wあ──\x02",
        )
    )

    CloseMessageWindow()
    StopEffect(0x0, 0x2)
    Sound(820, 0, 100, 0)
    OP_24(0x348)
    SetChrSubChip(0x103, 0x11)
    Sleep(150)
    SetChrSubChip(0x103, 0x12)
    Sleep(150)
    SetChrSubChip(0x103, 0x13)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_445F():
        OP_95(0xFE, 202200, 100, -400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_445F)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrFlags(0x101, 0x8)
    SetChrSubChip(0x103, 0x14)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(100)
    SetChrSubChip(0x103, 0x15)

    #C0115
    ChrTalk(
        0x101,
        "#6P#0007Fだ、大丈夫か！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1272, 255, 70, 0)    #voice#Tio
    Sleep(1000)

    #C0116
    ChrTalk(
        0x103,
        (
            "#5P#0206F#40Wは、はい……\x02\x03",

            "ちょっと処理を上げすぎたせいで\x01",
            "目を回してしまいました……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#6P#0006Fまったく……\x01",
            "無茶するなって言ったのに。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    SetChrSubChip(0x103, 0x16)
    Sleep(130)
    SetChrSubChip(0x103, 0x17)
    Sleep(130)
    SetChrSubChip(0x103, 0x18)
    Sleep(130)
    SetChrSubChip(0x103, 0x19)
    Sleep(130)
    SetChrSubChip(0x103, 0x18)
    Sleep(130)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x103, 0x17)
    Sleep(130)
    SetChrSubChip(0x103, 0x18)
    Sleep(130)
    SetChrSubChip(0x103, 0x19)
    Sleep(130)
    SetChrSubChip(0x103, 0x18)
    Sleep(130)
    SetChrSubChip(0x103, 0x17)
    Sleep(300)
    SetChrSubChip(0x103, 0x1D)
    Sleep(100)
    SetChrSubChip(0x103, 0x1E)
    Sleep(300)

    #C0118
    ChrTalk(
        0x103,
        "#5P#0205F#30Wあ……\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#6P#0003F──あのさ、ティオ。\x02\x03",

            "#0000F兄貴がした約束……\x01",
            "俺に引き継がせてくれないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x103,
        "#5P#0200F#30Wえ──\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#6P#0008F『もし幸せになれなかったら\x01",
            "  いつでも呼んでくれ……』\x02\x03",

            "『お前を不幸にする原因を\x01",
            "  一緒にぶっ飛ばしてやる……』\x02\x03",

            "#0006F……悔しいけど、兄貴は凄かった。\x02\x03",

            "パワーにしても行動力にしても\x01",
            "まだまだ足元にも及んじゃいない。\x02\x03",

            "#0000F──でも俺、頑張るから。\x02\x03",

            "その約束を守れるくらいは\x01",
            "デカイ男になってみせるからさ。\x02\x03",

            "だから……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1E)
    Sleep(100)
    SetChrSubChip(0x103, 0x1D)
    Sleep(100)
    SetChrSubChip(0x103, 0x1C)
    Sleep(500)

    #C0122
    ChrTalk(
        0x103,
        (
            "#5P#0204F#30W……………………………………\x02\x03",

            "ふふっ……不思議ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        (
            "#5P#0204Fロイドさんとガイさんって\x01",
            "あんまり似ていないのに……\x02\x03",

            "それでもどこか\x01",
            "似たようなものを感じます。\x02\x03",

            "魂の在り様というか……\x01",
            "見ている方向が同じというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#6P#0005F俺と、兄貴が……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1C)
    Sleep(100)
    SetChrSubChip(0x103, 0x1D)
    Sleep(100)
    SetChrSubChip(0x103, 0x1E)
    Sleep(300)

    #C0126
    ChrTalk(
        0x103,
        (
            "#5P#0202Fはい。\x02\x03",

            "#0204Fでも──やっぱり違います。\x02\x03",

            "ロイドさんはロイドさんであって\x01",
            "ガイさんと同じじゃありません。\x02\x03",

            "#0201Fそれはロイドさんが一番、\x01",
            "分かっているんじゃないですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#6P#0008F……それは………\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        (
            "#5P#0204F──ですから。\x02\x03",

            "どうせ約束してくれるのなら\x01",
            "別の内容がいいです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0129
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_4A5A():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A5A)
    Fade(250)
    SetChrSubChip(0x103, 0xA)
    OP_0D()
    Sleep(500)

    #C0130
    ChrTalk(
        0x103,
        (
            "#11P#0202F別に……\x01",
            "今すぐじゃなくていいです。\x02\x03",

            "ロイドさんの言葉で\x01",
            "わたしにしてくれる約束……\x02\x03",

            "#0204F思いついたらで結構ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        "#6P#0002Fティオ……\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x103,
        (
            "#11P#0206Fそれに……\x01",
            "わたしも子供じゃありません。\x02\x03",

            "一方的に守られるのも\x01",
            "何かをしてもらうのもイヤです。\x02\x03",

            "#0201Fわたしだって……\x01",
            "同じ支援課のメンバーでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#6P#0002F……そうだな。\x02\x03",

            "#0014Fははっ、確かにその通りだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x103,
        "#11P#0209F……ふふっ………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0135
    ChrTalk(
        0x101,
        "#6P#0005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x103,
        (
            "#11P#0205F？？？\x02\x03",

            "どうしたんですか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#6P#0011Fいや、その……\x02\x03",

            "#0012Fちゃんと笑ってる顔、\x01",
            "初めて見たかもって思ってさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x103, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x103)

    #C0138
    ChrTalk(
        0x103,
        (
            "#11P#0206Fべ、別に笑っていません……！\x02\x03",

            "#0208Fこれはその……\x01",
            "気が抜けてしまっただけで……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#6P#0004Fはは、照れるなって。\x02\x03",

            "#0002Fうーん、でも勿体ないな。\x02\x03",

            "ティオ、元がすごく可愛いんだから\x01",
            "普通に笑えばモテモテだろうに。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x103,
        (
            "#11P#0205Fす、すごく可愛いって……\x02\x03",

            "#0211F……～～～っ～～～……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0141
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6Pえー、コホンコホン。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x101, 0x8)
    SetChrSubChip(0x103, 0x6)

    def lambda_4E7F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E7F)
    SetChrSubChip(0x103, 0x7)
    Sleep(300)

    #C0142
    ChrTalk(
        0x101,
        "#0005F#5Pおっと……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        (
            "#11P#0205Fヨ、ヨナ！？\x02\x03",

            "#0201Fい、い、いつから\x01",
            "聞いていたんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6Pいや、笑ってる顔は初めて～、\x01",
            "とかのあたりだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6Pハハッ、なんか珍しいモンを\x01",
            "聞かせてもらっちまったなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6Pまさかアンタが\x01",
            "そんな風に慌てるなんてねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#11P#0211F……それ以上無駄口を叩いたら\x01",
            "《ポムっと！》で４０連鎖します。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6Pそれは仕様的に無理だから！\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6Pって、アンタなら\x01",
            "本当にやりかねないけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 11)
    WaitChrThread(0x101, 3)
    Fade(500)
    OP_68(103000, 1000, 0, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 101200, 0, -1700, 90)
    SetChrPos(0x103, 102300, 250, 0, 90)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x2)
    SetChrPos(0x9, 102600, 700, -1500, 0)
    OP_0D()

    #C0150
    ChrTalk(
        0x101,
        (
            "#6P#0001Fそれで、ヨナ。\x02\x03",

            "《仔猫#4Rキティ#》の正体は\x01",
            "ちゃんと掴めたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2Pハッ、ボクを誰だと\x01",
            "思ってるんだっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P無事、アドレスは掴んだから\x01",
            "そっちにも情報を送るぜ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(824, 0, 100, 0)
    Sleep(500)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x103, 0x0)

    def lambda_51C2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_51C2)
    Sleep(500)

    #C0153
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P#0205F#6P……？\x02\x03",

            "妙な添付ファイルが\x01",
            "付いてるみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P添付ファイル～？\x01",
            "──って、なんだこりゃ！\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2Pアドレスを割り出したログに\x01",
            "どうしてこんなものが……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P#0201F開いてみましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Sound(850, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 10)
    Sleep(1200)
    EndChrThread(0x103, 0x3)
    SetChrSubChip(0x103, 0x0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0157
    ChrTalk(
        0x103,
        "#6P#0205Fえ……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        "#6P#0013Fこれは……！？\x02",
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis123.itp")
    CreatePortrait(1, 112, 64, 368, 192, 0, 0, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x1, "c_vis050.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    SetChrName("ヨナの声")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "な、な、なんじゃこりゃ～！？\x02\x03",

            "ちょ、ちょっと待て！\x02\x03",

            "これって、ひょっとして……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0160
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0206F居場所を突き止められた仕返しに\x01",
            "ハッキングを受けたみたいですね。\x02\x03",

            "#0208Fいえ……\x01",
            "最初から掌の上だったのかも。\x02\x03",

            "#0201Fそうなると、ダミー情報を\x01",
            "掴まされた可能性もありますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("ヨナの声")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "きゅうっ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x103, 3, 0, 14)
    Sound(819, 0, 90, 0)
    Sound(514, 0, 70, 0)
    Sleep(1000)
    SetChrSubChip(0x103, 0x2)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x1F4)

    #C0162
    ChrTalk(
        0x101,
        "#6P#0011Fおーい、大丈夫か？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#2Sくっ……\x01",
            "あの状況でアドレスを偽装する\x01",
            "余裕は流石になかったはずだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#2Sだったらアドレスを解析すれば\x01",
            "何とかアクセスポイントも……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#2S……いやでも……ブツブツ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0166
    ChrTalk(
        0x101,
        "#6P#0012Fおーい……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetMapObjFrame(0x3, "m00gim02", 0x2, "close")
    Sound(73, 0, 100, 0)
    Sleep(800)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrPos(0x103, 101800, 0, 800, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    TurnDirection(0x103, 0x101, 400)

    #C0167
    ChrTalk(
        0x103,
        (
            "#0206F#5Pまあ、放っておいて\x01",
            "いったんヨナの所に戻りましょう。\x02\x03",

            "#0202F報酬の記録結晶#8Rメモリークオーツ#も\x01",
            "受け取る必要がありますし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0168
    ChrTalk(
        0x101,
        (
            "#12P#0000Fあ……そんな話もあったか。\x02\x03",

            "なんか色々ありすぎて\x01",
            "すっかり忘れていたな……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        (
            "#0204F#5Pふふっ……\x02\x03",

            "#0202Fこの近くに、出口付近に出る\x01",
            "非常エレベーターがあるはずです。\x02\x03",

            "それを起動させて帰りましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        "#12P#0002Fああ、そうするか。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_68(100000, 2000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 100000, 0, 0, 270)
    SetChrPos(0x1, 100000, 0, 0, 270)
    SetScenarioFlags(0xA1, 3)
    OP_29(0x45, 0x1, 0x4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7300", 0)
    OP_24(0x326)
    OP_24(0x348)
    OP_24(0x389)
    EventEnd(0x5)
    Return()

    # Function_9_124A end

    def Function_10_58F9(): pass

    label("Function_10_58F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5925")
    SetChrSubChip(0x103, 0x0)
    Sleep(70)
    SetChrSubChip(0x103, 0x1)
    Sleep(70)
    SetChrSubChip(0x103, 0x2)
    Sleep(70)
    SetChrSubChip(0x103, 0x1)
    Sleep(70)
    Jump("Function_10_58F9")

    label("loc_5925")

    Return()

    # Function_10_58F9 end

    def Function_11_5926(): pass

    label("Function_11_5926")


    def lambda_592B():
        OP_95(0xFE, 202200, 0, -1700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_592B)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x190)
    ClearChrFlags(0x101, 0x4)
    Return()

    # Function_11_5926 end

    def Function_12_5951(): pass

    label("Function_12_5951")

    Sleep(1000)
    OP_C9(0x3, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0x640, 0xFFFFFB50, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1)
    OP_CA(0x0, 0xFF, 0x0)
    Return()

    # Function_12_5951 end

    def Function_13_59B0(): pass

    label("Function_13_59B0")

    Sleep(300)
    OP_C9(0x2, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    Sleep(1)
    OP_C9(0x2, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x2, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1)
    Sleep(1)
    OP_C9(0x2, 0x0, 0x640, 0xFFFFFB50, 0x1)
    Sleep(1)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1)
    OP_CA(0x0, 0xFF, 0x0)
    Return()

    # Function_13_59B0 end

    def Function_14_5A0F(): pass

    label("Function_14_5A0F")

    Sleep(300)
    OP_C9(0x0, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    OP_C9(0x1, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    Sleep(1)
    OP_C9(0x0, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    OP_C9(0x1, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x0, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    OP_C9(0x1, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x0, 0x0, 0x640, 0xFFFFFB50, 0x1)
    OP_C9(0x1, 0x0, 0x640, 0xFFFFFB50, 0x1)
    Sleep(1)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1)
    OP_CA(0x0, 0xFF, 0x0)
    Return()

    # Function_14_5A0F end

    def Function_15_5AB9(): pass

    label("Function_15_5AB9")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B50")

    #C0171
    ChrTalk(
        0x103,
        (
            "#0200Fロイドさん、\x01",
            "《第３制御端末》は右の扉です。\x02\x03",

            "早速起動させて\x01",
            "スタンバイしておきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#0005Fおっと、そうだな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BB2")

    label("loc_5B50")


    #C0173
    ChrTalk(
        0x103,
        (
            "#0203F……《第３制御端末》は\x01",
            "右の扉ですね。\x02\x03",

            "#0200F早速起動させて\x01",
            "スタンバイしておかないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BB2")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 6540, 180)
    EventEnd(0x4)
    Return()

    # Function_15_5AB9 end

    def Function_16_5BC9(): pass

    label("Function_16_5BC9")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C3F")

    #C0174
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……確か近くに\x01",
            "非常エレベーターがあるんだったな。\x02\x03",

            "#0000Fそっちを使ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CA4")

    label("loc_5C3F")


    #C0175
    ChrTalk(
        0x103,
        (
            "#0203F……近くに出口付近に出る\x01",
            "非常エレベーターがあったはず。\x02\x03",

            "#0200Fそっちを使ってみましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA4")

    Sleep(50)
    OP_68(0, 0, -8290, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    SetChrPos(0x0, 0, 0, -8290, 0)
    EventEnd(0x4)
    Return()

    # Function_16_5BC9 end

    def Function_17_5CE9(): pass

    label("Function_17_5CE9")

    TalkBegin(0xFF)
    SetChrName("")

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "端末の導力は落ちている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_17_5CE9 end

    SaveToFile()

Try(main)
