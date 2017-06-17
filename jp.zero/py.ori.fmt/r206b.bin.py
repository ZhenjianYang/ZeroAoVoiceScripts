from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r206b.bin",                # FileName
        "r206b",                    # MapName
        "r206b",                    # Location
        0x0062,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 0, 0, 1],
    )

    BuildStringList((
        "r206b",                  # 0
        "軍用犬",                 # 1
        "軍用犬",                 # 2
        "軍用犬",                 # 3
        "軍用犬",                 # 4
        "軍用犬",                 # 5
        "軍用犬",                 # 6
        "軍用犬",                 # 7
        "軍用犬",                 # 8
        "軍用犬",                 # 9
        "軍用犬",                 # 10
        "マフィア",               # 11
        "マフィア",               # 12
        "ツァイト",               # 13
        "白い狼",                 # 14
        "白い狼",                 # 15
        "白い狼",                 # 16
        "白い狼",                 # 17
        "白い狼",                 # 18
        "白い狼",                 # 19
        "レン",                   # 20
        "アリオス",               # 21
        "車",                     # 22
        "SE制御",                 # 23
        "BR206b",                 # 24
        "クロスベル市方面",       # 25
        "鉱山町マインツ方面",     # 26
    ))

    ATBonus("ATBonus_40C", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_4CC", 9, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D0", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D4", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D8", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 6, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4C4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C8", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_4EC", 0x0002, 16, 6, 0, 0, 0, 0, 0, "BR206b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31001.dat", "ms31101.dat", "ms75600.dat", "ms75600.dat", "ms75600.dat", 0, 0, 0, "MonsterBattlePostion_4CC", "MonsterBattlePostion_4AC", "ed7402", "ed7403", "ATBonus_40C"),
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(18120,   10000,   151900,  1200,    18120,   11000,   151900,  0x007C, 0,  2,  0x0000)

    PlaceName(-3.0, 0.0, -15.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(87.0, 6.0, 122.0, 0x0000, 0x0000, "鉱山町マインツ方面")

    ScpFunction((
        "Function_0_598",          # 00, 0
        "Function_1_5BC",          # 01, 1
        "Function_2_5D4",          # 02, 2
        "Function_3_721",          # 03, 3
        "Function_4_17EC",         # 04, 4
        "Function_5_1813",         # 05, 5
        "Function_6_183D",         # 06, 6
        "Function_7_4758",         # 07, 7
        "Function_8_4789",         # 08, 8
        "Function_9_47B3",         # 09, 9
        "Function_10_47DD",        # 0A, 10
        "Function_11_4804",        # 0B, 11
        "Function_12_4821",        # 0C, 12
        "Function_13_484B",        # 0D, 13
        "Function_14_4872",        # 0E, 14
        "Function_15_4890",        # 0F, 15
        "Function_16_491C",        # 10, 16
        "Function_17_49AF",        # 11, 17
        "Function_18_49F0",        # 12, 18
        "Function_19_4A31",        # 13, 19
        "Function_20_4A72",        # 14, 20
        "Function_21_4AB3",        # 15, 21
        "Function_22_4AF4",        # 16, 22
        "Function_23_4B35",        # 17, 23
        "Function_24_4B4D",        # 18, 24
        "Function_25_4B67",        # 19, 25
    ))


    def Function_0_598(): pass

    label("Function_0_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_5AC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 3)
    Jump("loc_5BB")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_5BB")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 6)

    label("loc_5BB")

    Return()

    # Function_0_598 end

    def Function_1_5BC(): pass

    label("Function_1_5BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CF")
    OP_70(0x1, 0x0)
    Jump("loc_5D3")

    label("loc_5CF")

    OP_70(0x1, 0x1E)

    label("loc_5D3")

    Return()

    # Function_1_5BC end

    def Function_2_5D4(): pass

    label("Function_2_5D4")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D0")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_659")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_6CB")

    label("loc_659")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_6CB")

    Jump("loc_715")

    label("loc_6D0")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_715")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_5D4 end

    def Function_3_721(): pass

    label("Function_3_721")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31000.itc", 0x26)
    LoadChrToIndex("chr/ch31050.itc", 0x27)
    LoadChrToIndex("chr/ch31051.itc", 0x28)
    LoadChrToIndex("chr/ch31100.itc", 0x29)
    LoadChrToIndex("chr/ch31150.itc", 0x2A)
    LoadChrToIndex("chr/ch31151.itc", 0x2B)
    LoadChrToIndex("monster/ch75650.itc", 0x2C)
    LoadChrToIndex("monster/ch75651.itc", 0x2D)
    LoadChrToIndex("apl/ch50121.itc", 0x2E)
    LoadChrToIndex("chr/ch31054.itc", 0x2F)
    LoadEffect(0x0, "battle\\mg128_00.eff")
    LoadEffect(0x1, "event\\ev101_00.eff")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2D)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x29)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x12, 11530, 0, 138630, 180)
    SetChrPos(0x13, 12930, 0, 137890, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    OP_78(0x0, 0x1D)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1D, 18850, 0, 138470, 0)
    OP_D3(0x1D, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(85720, 600, 134260, 0)
    MoveCamera(36, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40000, 0)
    OP_68(60560, -2600, 129789, 8000)
    SetCameraDistance(47000, 8000)
    SetChrPos(0x8, 88960, 6000, 118390, 270)
    SetChrPos(0x9, 87080, 6000, 116180, 270)
    SetChrPos(0xA, 91990, 6000, 116720, 270)
    BeginChrThread(0x8, 0, 0, 4)
    BeginChrThread(0x9, 0, 0, 4)
    BeginChrThread(0xA, 0, 0, 4)
    BeginChrThread(0x1E, 1, 0, 24)

    def lambda_9B6():
        OP_9B(0x0, 0xFE, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9B6)

    def lambda_9CB():
        OP_9B(0x0, 0xFE, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9CB)

    def lambda_9E0():
        OP_9B(0x0, 0xFE, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9E0)
    Sleep(1500)
    OP_63(0x9, 0xFFFFFD44, 1600, 0x28, 0x2B, 0x64, 0x0)
    Sleep(100)
    OP_63(0x8, 0xFFFFFD44, 1600, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    OP_63(0xA, 0xFFFFFD44, 1600, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0x1E, 0x1)
    OP_0D()
    OP_6F(0x11)
    Fade(1000)
    OP_68(14370, 3400, 137860, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_68(14370, 900, 137860, 6000)
    OP_0D()
    OP_64(0x8)
    OP_64(0x9)
    OP_64(0xA)
    OP_63(0x9, 0xFFFFFC7C, 1800, 0x28, 0x2B, 0x64, 0x0)
    Sleep(100)
    OP_63(0x8, 0xFFFFFC7C, 1800, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    OP_63(0xA, 0xFFFFFC7C, 1800, 0x28, 0x2B, 0x64, 0x0)
    OP_6F(0x1)
    Sleep(500)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(13820, 900, 136010, 2500)
    BeginChrThread(0x8, 0, 0, 4)
    BeginChrThread(0x9, 0, 0, 4)
    BeginChrThread(0xA, 0, 0, 4)
    BeginChrThread(0x1E, 1, 0, 25)
    SetChrPos(0x8, 18050, 0, 125300, 270)
    SetChrPos(0x9, 19860, 0, 123430, 270)
    SetChrPos(0xA, 18390, 0, 121930, 270)

    def lambda_B74():
        OP_95(0xFE, 11210, 0, 134270, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B74)

    def lambda_B8E():
        OP_95(0xFE, 13320, 0, 132200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B8E)

    def lambda_BA8():
        OP_95(0xFE, 10820, 0, 130550, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BA8)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 5)
    OP_93(0x8, 0x0, 0x1F4)
    OP_64(0x8)
    OP_63(0x8, 0xFFFFFD44, 2100, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0x9, 1)
    EndChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 0, 0, 5)
    OP_93(0x9, 0x0, 0x1F4)
    OP_64(0x9)
    OP_63(0x9, 0xFFFFFD44, 2100, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0xA, 1)
    EndChrThread(0xA, 0x0)
    SetChrChipByIndex(0xA, 0x2C)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 0, 0, 5)
    OP_93(0xA, 0x0, 0x1F4)
    OP_64(0xA)
    OP_63(0xA, 0xFFFFFD44, 2100, 0x28, 0x2B, 0x64, 0x0)
    EndChrThread(0x1E, 0x1)
    OP_6F(0x1)

    #C0004
    ChrTalk(
        0x8,
        "#11Pグルルル！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        "#11Pバウバウ！\x02",
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_64(0x9)
    OP_64(0xA)
    EndChrThread(0x8, 0x0)

    def lambda_C93():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C93)
    Sleep(250)
    Sound(514, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0x8, 0x2E)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    WaitChrThread(0x8, 2)
    Sleep(500)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)

    def lambda_CDD():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_CDD)

    def lambda_CF6():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_CF6)
    Sleep(250)
    Sound(514, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x2E)
    SetChrSubChip(0xA, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)

    #C0006
    ChrTalk(
        0x12,
        "#5Pな、なんだ……？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x12,
        (
            "#5Pおい、なんで\x01",
            "こんな早く戻ってくるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x13,
        (
            "#5P町の人間を襲うように\x01",
            "指示を出していたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x13,
        (
            "#5Pどうしたお前ら、\x01",
            "早すぎるんじゃないのか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 20720, 0, 128080, 270)
    SetChrPos(0x102, 20490, 0, 126430, 270)
    SetChrPos(0x103, 22480, 0, 127490, 270)
    SetChrPos(0x104, 22610, 0, 125580, 270)
    Sleep(300)
    #Sound(1090, 255, 100, 0)    #voice#Lloyd

    #N0010
    NpcTalk(
        0x101,
        "ロイドの声",
        "#1P──そこまでだ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x12, 0x101, 500)
    Sleep(50)
    TurnDirection(0x13, 0x101, 500)
    Fade(500)
    OP_68(12890, 0, 137590, 0)
    MoveCamera(330, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(28010, 0)
    SetCameraDistance(26010, 2000)

    def lambda_EF3():
        OP_95(0xFE, 17030, 0, 132160, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EF3)

    def lambda_F0D():
        OP_95(0xFE, 16490, 0, 130310, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F0D)

    def lambda_F27():
        OP_95(0xFE, 19410, 0, 131940, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F27)

    def lambda_F41():
        OP_95(0xFE, 18620, 0, 129940, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F41)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x13B, 0x1F4)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x13B, 0x1F4)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x13B, 0x1F4)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x13B, 0x1F4)
    OP_6F(0x79)
    OP_0D()

    #C0011
    ChrTalk(
        0x12,
        "#5Pな、なんだ！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x13,
        "#11Pお前たちは……！？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#0013F#6Pクロスベル警察、特務支援課の者だ。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        (
            "#0101F#6P《ルバーチェ商会》の方々ですね。\x02\x03",

            "器物損壊、および傷害の容疑で\x01",
            "あなた方を拘束させてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x12,
        "#5Pけ、警察……！？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x13,
        "#11Pなんでこんな町に……\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0017
    ChrTalk(
        0x12,
        (
            "#5P《特務支援課》……\x01",
            "ファビオたちが下手打ったあの……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x13,
        (
            "#11P旧市街での仕込みを\x01",
            "邪魔したとかいうガキどもか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#0302F#12Pハハ、どうやら名前を\x01",
            "覚えられちまったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#0204F#12Pここは光栄に思っておけば\x01",
            "いいんでしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x12,
        "#5Pチッ……まあいい。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x12,
        (
            "#5P警察の跳ねっ返りなんぞ、\x01",
            "ここで痛めつければ済むことだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2A)
    SetChrSubChip(0x13, 0x0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0023
    ChrTalk(
        0x13,
        (
            "#11P前に仲間が\x01",
            "世話になったようだなァ？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x13,
        (
            "#11Pおまけにウチの犬どもを\x01",
            "可愛がってくれたようだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x12,
        (
            "#5P丁度いい……\x01",
            "ここで礼をさせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#0013F#6P……抵抗するのか。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x13,
        (
            "#11Pクハハ！\x01",
            "それはこっちの台詞だぜ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x8, 500)

    #C0028
    ChrTalk(
        0x12,
        "#5P──攻撃準備#8Rゲット・レディ#！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x12, 0x2F)
    SetChrSubChip(0x12, 0x0)
    OP_A1(0x12, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    PlayEffect(0x1, 0xFF, 0x12, 0x40, 0, 1000, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(590, 0, 100, 0)
    OP_68(12020, 0, 137490, 1000)
    OP_A1(0x12, 0x3E8, 0x2, 0x3, 0x4)
    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    Sleep(1000)
    PlayEffect(0x0, 0xFF, 0x8, 0x140, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x9, 0x140, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xA, 0x140, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    TurnDirection(0x12, 0x102, 500)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)

    def lambda_14D2():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_14D2)

    def lambda_14EB():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14EB)

    def lambda_1504():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1504)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x2C)
    SetChrSubChip(0xA, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 5)
    BeginChrThread(0x9, 0, 0, 5)
    BeginChrThread(0xA, 0, 0, 5)
    OP_0D()
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)

    def lambda_157D():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_157D)

    def lambda_158A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_158A)
    Sleep(100)

    def lambda_159A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_159A)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)

    def lambda_15B3():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15B3)

    def lambda_15C0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15C0)
    Sleep(100)

    def lambda_15D0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15D0)

    def lambda_15DD():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15DD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0029
    ChrTalk(
        0x101,
        "#0010F#11Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0310F#12Pチッ……\x01",
            "薬で回復させやがったか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x13,
        (
            "#11Pククク……\x01",
            "これでもプロなんでねぇ。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x708)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0032
    ChrTalk(
        0x12,
        "#5P──行け、仕留めろ#14Rゴー・アンド・アタック#！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x12,
        (
            "#5Pこいつらの喉を\x01",
            "喰い千切るつもりで行け！\x02",
        )
    )

    CloseMessageWindow()
    Sound(836, 0, 100, 0)

    #C0034
    ChrTalk(
        0x8,
        "#5Pグルルル……！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        "#5Pガウッ！！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        "#0101F#6P来る……！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        "#0007F#2Pこちらも手加減無用だ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    SetCameraDistance(24010, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    Battle("BattleInfo_4EC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    Call(0, 6)
    Return()

    # Function_3_721 end

    def Function_4_17EC(): pass

    label("Function_4_17EC")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1812")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_17F7")

    label("loc_1812")

    Return()

    # Function_4_17EC end

    def Function_5_1813(): pass

    label("Function_5_1813")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_181E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_183C")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_181E")

    label("loc_183C")

    Return()

    # Function_5_1813 end

    def Function_6_183D(): pass

    label("Function_6_183D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31000.itc", 0x26)
    LoadChrToIndex("chr/ch31050.itc", 0x27)
    LoadChrToIndex("chr/ch31051.itc", 0x28)
    LoadChrToIndex("chr/ch31053.itc", 0x29)
    LoadChrToIndex("chr/ch31100.itc", 0x2A)
    LoadChrToIndex("chr/ch31150.itc", 0x2B)
    LoadChrToIndex("chr/ch31153.itc", 0x2C)
    LoadChrToIndex("chr/ch09500.itc", 0x2D)
    LoadChrToIndex("chr/ch02400.itc", 0x2E)
    LoadChrToIndex("chr/ch02600.itc", 0x2F)
    LoadChrToIndex("monster/ch75650.itc", 0x30)
    LoadChrToIndex("monster/ch75651.itc", 0x31)
    LoadChrToIndex("chr/ch02650.itc", 0x33)
    LoadChrToIndex("chr/ch02651.itc", 0x34)
    LoadChrToIndex("apl/ch50112.itc", 0x35)
    LoadChrToIndex("apl/ch50118.itc", 0x36)
    LoadChrToIndex("chr/ch02656.itc", 0x37)
    LoadChrToIndex("apl/ch50113.itc", 0x38)
    LoadChrToIndex("apl/ch50115.itc", 0x39)
    LoadChrToIndex("apl/ch50121.itc", 0x3A)
    LoadChrToIndex("chr/ch02602.itc", 0x3B)
    LoadChrToIndex("apl/ch50125.itc", 0x3C)
    OP_68(10560, 800, 129789, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17770, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 11220, 0, 132770, 0)
    SetChrPos(0x102, 10050, 0, 131260, 0)
    SetChrPos(0x103, 12170, 0, 131370, 0)
    SetChrPos(0x104, 10840, 0, 130060, 0)
    SetChrChipByIndex(0x8, 0x3A)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x3A)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x3A)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x30)
    SetChrSubChip(0xC, 0x1)
    SetChrChipByIndex(0xD, 0x30)
    SetChrSubChip(0xD, 0x1)
    SetChrChipByIndex(0xE, 0x30)
    SetChrSubChip(0xE, 0x1)
    SetChrChipByIndex(0xF, 0x30)
    SetChrSubChip(0xF, 0x1)
    SetChrChipByIndex(0x10, 0x30)
    SetChrSubChip(0x10, 0x1)
    SetChrChipByIndex(0x11, 0x30)
    SetChrSubChip(0x11, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 4250, 0, 130520, 90)
    SetChrPos(0x9, 5870, 0, 127000, 45)
    SetChrPos(0xA, 8119, 0, 123880, 0)
    SetChrPos(0xB, 13090, 0, 125630, 315)
    SetChrPos(0xC, 10600, 0, 142410, 180)
    SetChrPos(0xD, 9510, 0, 137200, 180)
    SetChrPos(0xE, 5740, 0, 137380, 180)
    SetChrPos(0xF, 17670, 0, 134980, 225)
    SetChrPos(0x10, 18840, 0, 132120, 270)
    SetChrPos(0x11, 18070, 0, 129470, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x2C)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 9840, 0, 136620, 180)
    SetChrPos(0x12, 11740, 0, 135960, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    OP_78(0x0, 0x1D)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1D, 18850, 0, 138470, 0)
    OP_D3(0x1D, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x35)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x35)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x35)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x35)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x35)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x17, 0x20)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x19, 0x20)
    SetChrFlags(0x1A, 0x20)
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x2D)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, -53820, 16000, 120750, 90)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -60750, 16000, 122310, 0)
    SetChrChipByIndex(0x1C, 0x2E)
    SetChrSubChip(0x1C, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01200.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_68(11640, 800, 134270, 3000)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33DF")

    #C0038
    ChrTalk(
        0x101,
        "#0010F#2Pはあはあ……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#0106F#12Pさ、さすがに\x01",
            "厳しかったわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x103,
        (
            "#0208F#2Pまさかあんな風に\x01",
            "犬を操るなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        (
            "#0301F#4Pフン……\x01",
            "なかなかの練度じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x12,
        "#5Pば、馬鹿な……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x13,
        (
            "#1Pくっ……\x01",
            "こんなガキどもに……！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(100)
    SetCameraDistance(16000, 1500)
    OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_6F(0x79)

    #C0044
    ChrTalk(
        0x101,
        (
            "#0003F#12P──これ以上の抵抗は無駄だ。\x02\x03",

            "#0001Fあんたたちの身柄は\x01",
            "明日の朝、警備隊に引き渡す。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        (
            "#0304F#4Pま、今夜のところは\x01",
            "倉庫にでも泊まっていけよ。\x02\x03",

            "#0300F俺たちが責任をもって\x01",
            "見張っといてやるからよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x12,
        "#5Pククク……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x13,
        "#1Pハハハ……！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2B)
    SetChrSubChip(0x13, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(100)
    OP_68(13470, 300, 138160, 1500)
    MoveCamera(45, 16, 0, 1500)
    SetCameraDistance(20970, 1500)
    OP_93(0x12, 0xE1, 0x0)

    def lambda_232C():
        OP_9D(0xFE, 0x3692, 0x0, 0x21CDC, 0x258, 0x9C4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_232C)
    Sleep(200)
    Sound(814, 0, 100, 0)
    OP_93(0x13, 0xE1, 0x0)

    def lambda_2359():
        OP_9D(0xFE, 0x303E, 0x0, 0x22132, 0x320, 0x9C4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2359)
    Sound(820, 0, 100, 0)
    WaitChrThread(0x12, 1)
    OP_93(0x12, 0xB4, 0x0)
    WaitChrThread(0x13, 1)
    OP_93(0x13, 0xB4, 0x0)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0048
    ChrTalk(
        0x101,
        "#0007F#6P待て……！\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        "#0307Fハッ、行かせるかよ！\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x12,
        "#5Pクク、勘違いするな……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x13,
        (
            "#1Pこうなったら手段は\x01",
            "選ばねぇってだけだ！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_68(15600, 600, 138500, 1500)
    SetCameraDistance(19000, 1500)
    OP_93(0x12, 0x5A, 0x1F4)
    OP_71(0x0, 0xF1, 0x10E, 0x0, 0x0)
    Sound(454, 0, 100, 0)
    OP_6F(0x79)
    OP_79(0x0)
    Sound(836, 0, 100, 0)
    OP_93(0x12, 0xB4, 0x0)

    def lambda_247D():
        OP_9D(0xFE, 0x3638, 0x0, 0x220E2, 0x258, 0xDAC)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_247D)
    WaitChrThread(0x12, 1)
    Sound(42, 0, 100, 0)
    OP_93(0x12, 0xB4, 0x1F4)
    OP_68(14860, 600, 136990, 6000)
    MoveCamera(55, 16, 0, 6000)
    SetCameraDistance(24270, 6000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    BeginChrThread(0xE, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0xC, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0xF, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0xD, 3, 0, 18)
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
    Sleep(350)
    BeginChrThread(0x10, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 22)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    OP_6F(0x79)

    #C0052
    ChrTalk(
        0x103,
        "#0205F#11Pっ！？\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        "#0105F#11Pま、まだいたの！？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        "#0301F#11Pチッ……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)

    def lambda_2648():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2648)
    Sleep(50)

    def lambda_2660():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2660)
    Sleep(100)

    def lambda_2678():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2678)
    Sleep(50)

    def lambda_2690():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2690)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)

    def lambda_26B1():
        OP_93(0xFE, 0xB4, 0x2EE)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26B1)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)

    def lambda_26CA():
        OP_93(0xFE, 0xB4, 0x2EE)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_26CA)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)

    def lambda_26E3():
        OP_93(0xFE, 0xB4, 0x2EE)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_26E3)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    def lambda_26FC():
        OP_93(0xFE, 0xB4, 0x2EE)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26FC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_68(11630, 600, 132400, 1000)
    SetCameraDistance(23060, 1000)
    OP_6F(0x79)

    def lambda_2741():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2741)

    def lambda_275A():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_275A)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x9, 0x30)
    SetChrSubChip(0x9, 0x1)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 0, 0, 5)
    SetChrChipByIndex(0xB, 0x30)
    SetChrSubChip(0xB, 0x1)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 0, 0, 5)
    OP_0D()
    WaitChrThread(0x9, 2)
    WaitChrThread(0xB, 2)

    def lambda_27B6():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_27B6)

    def lambda_27CF():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_27CF)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 5)
    SetChrChipByIndex(0xA, 0x30)
    SetChrSubChip(0xA, 0x1)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 5)
    OP_0D()
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)

    #C0055
    ChrTalk(
        0x101,
        "#0013F#5Pしまった……！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#0310F#5P１０匹か……\x01",
            "さすがに数が多すぎるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x12,
        (
            "#5Pククク……\x01",
            "形勢逆転だなぁ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x13,
        (
            "#1P俺たちを\x01",
            "コケにしてくれた礼だ……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x13,
        (
            "#1Pせいぜい時間をかけて\x01",
            "なぶり殺しにしてやるよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#0010F#5Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#0108F#5P……このままじゃ……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        "#0206F#5P……ピンチ、ですね。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0063
    ChrTalk(
        0x104,
        "#0308F#5P#30W（チッ、こうなったら……）\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x13,
        (
            "#1Pクク……女神への\x01",
            "祈りの時間は終わったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x12,
        (
            "#5Pそれじゃあ楽しい\x01",
            "処刑タイムの始まりと──\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(842, 0, 100, 0)
    Sleep(1500)
    CancelBlur(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0066
    ChrTalk(
        0x101,
        "#0005F#5Pなっ……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x12,
        "#5Pな、なんだ！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x15, -6820, 4000, 146610, 180)
    SetChrPos(0x16, -2980, 4000, 147620, 180)
    SetChrPos(0x17, 6510, 6000, 145910, 180)
    SetChrPos(0x18, 13520, 6000, 144820, 180)
    SetChrPos(0x19, 17340, 6000, 141120, 225)
    SetChrPos(0x1A, 20260, 6000, 137750, 225)
    SetChrPos(0x14, 12860, 10000, 152980, 180)
    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x15, 0, 0, 8)
    BeginChrThread(0x16, 0, 0, 8)
    BeginChrThread(0x17, 0, 0, 8)
    BeginChrThread(0x18, 0, 0, 8)
    BeginChrThread(0x19, 0, 0, 8)
    BeginChrThread(0x1A, 0, 0, 8)
    BeginChrThread(0x14, 0, 0, 9)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    Fade(1000)
    OP_68(250, 5000, 151050, 0)
    MoveCamera(25, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21730, 0)
    OP_68(20200, 5000, 141800, 10000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(20800, 7900, 150250, 0)
    MoveCamera(65, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31530, 0)
    OP_68(22960, 7900, 157520, 2500)
    SetCameraDistance(29530, 2500)
    OP_6F(0x79)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    #Sound(2047, 255, 100, 0)    #voice#Zeit
    SetChrName("白い狼")

    #A0068
    AnonymousTalk(
        0xFF,
        "#1Pグルルルルル……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetCameraDistance(27530, 1000)
    OP_6F(0x10)
    EndChrThread(0x14, 0x0)
    BeginChrThread(0x14, 0, 0, 11)
    Sound(846, 0, 100, 0)
    Sound(842, 0, 100, 0)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x1A, 0x0)
    BeginChrThread(0x15, 0, 0, 14)
    BeginChrThread(0x16, 0, 0, 14)
    BeginChrThread(0x17, 0, 0, 14)
    BeginChrThread(0x18, 0, 0, 14)
    BeginChrThread(0x19, 0, 0, 14)
    BeginChrThread(0x1A, 0, 0, 14)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_68(1790, 7900, 135730, 750)
    SetCameraDistance(40740, 750)
    OP_6F(0x79)
    Sleep(1000)
    CancelBlur(500)
    Sleep(2000)
    Fade(1000)
    OP_68(11630, 600, 132400, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18690, 0)
    OP_93(0x101, 0x0, 0x0)
    OP_93(0x102, 0x0, 0x0)
    SetChrPos(0x103, 11900, 0, 131330, 0)
    OP_93(0x104, 0x0, 0x0)
    SetCameraDistance(23060, 3000)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xF, 0x0)
    EndChrThread(0x10, 0x0)
    EndChrThread(0x11, 0x0)
    Sleep(1000)
    SetCameraDistance(23060, 1000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    BeginChrThread(0x8, 3, 0, 7)
    BeginChrThread(0x9, 3, 0, 7)
    BeginChrThread(0xA, 3, 0, 7)
    BeginChrThread(0xB, 3, 0, 7)
    BeginChrThread(0xC, 3, 0, 7)
    BeginChrThread(0xD, 3, 0, 7)
    BeginChrThread(0xE, 3, 0, 7)
    BeginChrThread(0xF, 3, 0, 7)
    BeginChrThread(0x10, 3, 0, 7)
    BeginChrThread(0x11, 3, 0, 7)
    Sound(847, 0, 100, 0)
    Sound(514, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(1500)

    #C0069
    ChrTalk(
        0x103,
        "#0205F#12Pあ、あれは……！\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        "#0105F#6Pあの時の白い狼……！\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0309F#12Pはは……\x01",
            "仲間を連れて見参ってわけか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0072
    ChrTalk(
        0x13,
        (
            "#1Pお、お前ら……！\x01",
            "何を怯えてやがる！？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x12,
        (
            "#5P数じゃこちらも\x01",
            "負けてねえだろうが！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x12,
        "#5P尻尾を丸めてんじゃねえ！\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#0004F#6Pまあ、本物と偽物の\x01",
            "格の差ってやつだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#0302F#12P確かに……\x01",
            "犬が狼に勝てるハズがねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        (
            "#0204F#12Pなんか、名誉を傷つけられて\x01",
            "怒っているみたいですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x102,
        (
            "#0102F#6P落とし前を付けに来た……\x01",
            "といったところかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(14080, 600, 137980, 2000)
    SetCameraDistance(18740, 2000)

    def lambda_3292():
        OP_96(0xFE, 0x3372, 0x0, 0x21250, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3292)
    Sleep(50)

    def lambda_32AF():
        OP_95(0xFE, 11270, 0, 135430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32AF)
    Sleep(100)

    def lambda_32CC():
        OP_95(0xFE, 13600, 0, 133690, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_32CC)
    Sleep(50)

    def lambda_32E9():
        OP_95(0xFE, 11770, 0, 132800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_32E9)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_6F(0x79)

    #C0079
    ChrTalk(
        0x12,
        "#5Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#0003F#12P……今度こそ終わりだ。\x02\x03",

            "#0001F器物損壊と傷害容疑、\x01",
            "および公務執行妨害で\x01",
            "あんたたちを逮捕する──\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_33DF")

    SetChrPos(0x101, 16970, 0, 135400, 180)
    SetChrPos(0x102, 19260, 0, 134710, 225)
    SetChrPos(0x12, 16800, 0, 133770, 180)
    SetChrPos(0x13, 18090, 0, 133340, 180)
    SetChrPos(0x104, 14260, 0, 140550, 180)
    SetChrPos(0x103, 10960, 0, 134320, 45)
    SetChrPos(0x8, 12970, 0, 138000, 90)
    SetChrPos(0x9, 10320, 0, 137530, 90)
    SetChrPos(0xA, 7500, 0, 135860, 45)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x30)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x30)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x10E, 0x10E, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0x101, 0, 0, 23)
    BeginChrThread(0x102, 0, 0, 23)
    BeginChrThread(0x103, 0, 0, 23)
    BeginChrThread(0x104, 0, 0, 23)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x2)
    SetChrChipByIndex(0x13, 0x2C)
    SetChrSubChip(0x13, 0x2)
    SetChrChipByIndex(0x14, 0x3B)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 12)
    SetChrChipByIndex(0x15, 0x3C)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x3C)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x3C)
    SetChrSubChip(0x17, 0x0)
    Sleep(100)
    BeginChrThread(0x15, 0, 0, 12)
    Sleep(100)
    BeginChrThread(0x16, 0, 0, 12)
    Sleep(100)
    BeginChrThread(0x17, 0, 0, 12)
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x14, 13600, 10000, 151880, 180)
    SetChrPos(0x15, 12200, 10000, 154210, 180)
    SetChrPos(0x16, 15510, 10000, 154290, 180)
    SetChrPos(0x17, 13670, 10000, 156770, 180)
    FadeToBright(1000, 0)
    OP_68(-700, 8100, 125760, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12620, 0)
    OP_68(12620, 11400, 151020, 12000)
    SetCameraDistance(14540, 12000)
    OP_6F(0x11)
    OP_0D()
    Sleep(500)
    EndChrThread(0x14, 0x0)
    ClearChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x14, 0x2F)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x14, 0x0, 0x1F4)
    Sleep(500)
    Sound(2053, 255, 90, 0)    #voice#Zeit
    BeginChrThread(0x14, 3, 0, 11)
    WaitChrThread(0x14, 3)
    SetChrChipByIndex(0x14, 0x2F)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x1E, 1, 0, 24)
    SetChrChipByIndex(0x15, 0x36)
    SetChrSubChip(0x15, 0x0)
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x15, 0x10E, 0x1F4)
    BeginChrThread(0x15, 0, 0, 13)

    def lambda_3757():
        OP_95(0xFE, -1110, 9450, 159020, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3757)
    Sleep(300)
    SetChrChipByIndex(0x16, 0x36)
    SetChrSubChip(0x16, 0x0)
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x16, 0x10E, 0x1F4)
    BeginChrThread(0x16, 0, 0, 13)

    def lambda_3794():
        OP_95(0xFE, 1170, 10000, 158500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3794)
    Sleep(200)
    SetChrChipByIndex(0x17, 0x36)
    SetChrSubChip(0x17, 0x0)
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x17, 0x10E, 0x1F4)
    BeginChrThread(0x17, 0, 0, 13)

    def lambda_37D1():
        OP_95(0xFE, 320, 10000, 160370, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_37D1)

    def lambda_37EB():

        label("loc_37EB")

        TurnDirection(0xFE, 0x15, 100)
        Yield()
        Jump("loc_37EB")

    QueueWorkItem2(0x14, 3, lambda_37EB)
    WaitChrThread(0x15, 1)
    EndChrThread(0x15, 0x0)
    SetChrChipByIndex(0x15, 0x35)
    SetChrSubChip(0x15, 0x0)
    WaitChrThread(0x16, 1)
    EndChrThread(0x16, 0x0)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x1E, 0x1)
    WaitChrThread(0x17, 1)
    EndChrThread(0x17, 0x0)
    SetChrChipByIndex(0x17, 0x35)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x14, 0x3)
    OP_68(10390, 11400, 152400, 4000)
    MoveCamera(45, 13, 0, 4000)

    def lambda_3851():
        OP_95(0xFE, 11000, 10000, 153000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3851)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x14, 1)
    OP_6F(0x79)
    Sleep(500)
    OP_93(0x14, 0x10E, 0x1F4)
    SetChrChipByIndex(0x14, 0x3B)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 12)
    Sleep(1000)

    #N0081
    NpcTalk(
        0x14,
        "白い狼",
        "#5412F#11P……………………………………\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x14, 0x0)
    SetChrChipByIndex(0x14, 0x2F)
    SetChrSubChip(0x14, 0x0)
    OP_93(0x14, 0x13B, 0x12C)
    Sleep(300)
    SetChrChipByIndex(0x14, 0x34)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(19880, 2000)
    BeginChrThread(0x1E, 1, 0, 24)
    BeginChrThread(0x14, 0, 0, 10)
    OP_95(0x14, 1170, 10000, 158500, 7000, 0x0)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x1E, 0x1)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    OP_6F(0x10)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Fade(1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    OP_68(-43190, 16000, 121730, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22050, 0)
    OP_68(-49650, 16000, 122160, 5000)
    OP_6F(0x1)
    OP_0D()

    #N0082
    NpcTalk(
        0x1B,
        "ドレスの少女",
        (
            "#5Pうふふ……\x01",
            "やっぱり気付かれてたか。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0083
    AnonymousTalk(
        0x1B,
        (
            "#1Pあの狼さん、何者かしら？\x01",
            "タダ者じゃないみたいだけど……\x02\x03",

            "うふふ……でも、\x01",
            "お兄さんたちも詰めが甘いわね。\x02\x03",

            "狼さん達が助けてくれなかったら\x01",
            "どうするつもりだったのかしら？\x02\x03",

            "クスクス……先が思いやられるわね。\x02",
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

    #N0084
    NpcTalk(
        0x1C,
        "男の声",
        "#2P……まあ、これからだろう。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0085
    ChrTalk(
        0x1B,
        "#3305F#5Pあら……\x02",
    )

    CloseMessageWindow()
    OP_68(-51770, 16000, 123370, 4000)

    def lambda_3BD6():
        OP_95(0xFE, -54170, 16000, 122860, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3BD6)
    WaitChrThread(0x1C, 1)
    OP_6F(0x1)
    SetCameraDistance(21050, 80000)
    Sleep(300)

    #C0086
    ChrTalk(
        0x1B,
        (
            "#3304F#6Pうふふ、貴方も来ていたのね。\x02\x03",

            "さしずめ、彼らの手に余ったら\x01",
            "手助けするつもりだったのかしら？\x02\x03",

            "#3302F《風の剣聖》……\x01",
            "アリオス・マクレイン。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1C,
        (
            "#1403F#5P……君こそな。\x02\x03",

            "#1401F結社《身食らう蛇#10Rウ ロ ボ ロ ス#》の執行者。\x01",
            "Ｎｏ．──\x02\x03",      #line#50

            "ⅩⅤ──《殲滅天使》レン。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x1B,
        (
            "#3309F#6Pクスクス……\x01",
            "自己紹介するまでもなかったか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1C, 400)
    Sleep(300)

    #C0089
    ChrTalk(
        0x1B,
        (
            "#3302F#12PさすがＳ級への昇格要請を\x01",
            "辞退しているだけはあるみたいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x1C,
        (
            "#1403F#5P正直、過ぎた位階#4Rランク#だからな。\x02\x03",

            "カシウス・ブライトの代わりを\x01",
            "期待されても荷が重いだけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x1B,
        (
            "#3302F#12Pふふ……どうかしら？\x02\x03",

            "#3304Fレン、カシウス・ブライトと\x01",
            "一度会ったことがあるけど……\x02\x03",

            "貴方、剣の腕だったら\x01",
            "彼を凌#2Rしの#いでるんじゃないかしら？\x02\x03",

            "#3300Fそうね、レンが知っている\x01",
            "一番強い人に匹敵する感じがするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x1C,
        (
            "#1404F#5Pフフ……\x01",
            "それは光栄と言うべきか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 400)
    Sleep(500)

    #C0093
    ChrTalk(
        0x1C,
        (
            "#1401F#5P──この数ヶ月。\x01",
            "君がクロスベル自治州に\x01",
            "滞在していることは掴んでいる。\x02\x03",

            "最初は『お茶会』とやらを\x01",
            "開くつもりかと思ったんだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x5A, 0x190)
    Sleep(300)

    #C0094
    ChrTalk(
        0x1B,
        (
            "#3304F#6Pうふふ、判っていないわね。\x02\x03",

            "レンがお茶会を開かなくても\x01",
            "クロスベルは十分刺激的でしょう？\x02\x03",

            "#3302Fこの上、余計な催し物をするのは\x01",
            "無粋というものだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x1C,
        (
            "#1403F#5Pそれを聞いて安心した。\x02\x03",

            "どうやら個人的な事情で\x01",
            "滞在しているだけのようだが……\x02\x03",

            "#1400F──いつまで\x01",
            "“彼ら”から逃げるつもりだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0096
    ChrTalk(
        0x1B,
        "#3308F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x1C,
        (
            "#1403F#5P君たちの因縁に\x01",
            "とやかく口を出すつもりはない。\x02\x03",

            "彼らがクロスベルに来てくれた事は\x01",
            "個人的には大助かりだからな。\x02\x03",

            "#1400Fだが……目の前にある答えから\x01",
            "いつまでも逃げられはしないぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x1B,
        (
            "#3306F#6P……放っておいて。\x02\x03",

            "#3300Fそれに、レンがここにいるのは\x01",
            "エステルたちの事だけじゃないわ。\x02\x03",

            "《彼》の修理もあるし……\x01",
            "確かめなくちゃいけない事があるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x1C,
        "#1405F#5P確かめなくてはならない事……？\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x1B,
        (
            "#3304F#6Pうふふ、貴方には関係ないことよ。\x02\x03",

            "#3302F大人しくするって約束するから\x01",
            "レンのことは放っておいてちょうだい。\x02\x03",

            "もちろん……エステルたちにも\x01",
            "余計なことは喋らないでね？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x1C,
        (
            "#1404F#5P……承知した。\x02\x03",

            "#1402F君がこの地に仇#2Rあだ#なさぬ限り、\x01",
            "余計な干渉はしないことを誓おう。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x1B,
        "#3309F#6Pうふふ、ありがとう。\x02",
    )

    CloseMessageWindow()
    OP_93(0x1B, 0xB4, 0x190)
    Sleep(300)

    #C0103
    ChrTalk(
        0x1B,
        (
            "#3304F#5Pじゃあ、レンはもう行くわね。\x02\x03",

            "#3302Fご機嫌よう……《風の剣聖》さん。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x1B, 0x2)
    SetChrFlags(0x1B, 0x10)
    SetChrChipByIndex(0x1B, 0x39)
    SetChrSubChip(0x1B, 0x0)
    Sound(820, 0, 100, 0)
    OP_A1(0x1B, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    OP_A1(0x1B, 0x3E8, 0x4, 0x3, 0x2, 0x1, 0x0)
    SetChrChipByIndex(0x1B, 0x2D)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x2)
    ClearChrFlags(0x1B, 0x10)
    Sleep(200)

    def lambda_449F():

        label("loc_449F")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_449F")

    QueueWorkItem2(0x1C, 1, lambda_449F)
    OP_68(-51970, 16000, 121990, 5000)
    MoveCamera(68, 25, 0, 5000)
    SetCameraDistance(22500, 5000)

    def lambda_44D6():
        OP_96(0xFE, 0xFFFF1AA0, 0x3E80, 0x1B5B2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_44D6)
    WaitChrThread(0x1B, 1)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    EndChrThread(0x1C, 0x1)
    OP_6F(0x10)
    OP_63(0x1C, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1C)

    #C0104
    ChrTalk(
        0x1C,
        (
            "#1403F#5P迷子の子猫、か……\x02\x03",

            "しかしこのままでは\x01",
            "彼女も、彼らも迷い続けるだけだ。\x02\x03",

            "#1401F何か良いきっかけをもたらす\x01",
            "第三者でもいれば、あるいは……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x1C, 0x87, 0x190)
    Sleep(300)
    OP_63(0x1C, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1C)

    #C0105
    ChrTalk(
        0x1C,
        "#1404F#5Pフッ……まさかな。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(22500, 2000)
    OP_6F(0x10)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(6000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)
    OP_D5(0x30)
    OP_D5(0x31)
    OP_D5(0x33)
    OP_D5(0x34)
    OP_D5(0x35)
    OP_D5(0x36)
    OP_D5(0x37)
    OP_D5(0x38)
    OP_D5(0x39)
    ClearMapObjFlags(0x1, 0x4)
    SetScenarioFlags(0x5C, 1)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_183D end

    def Function_7_4758(): pass

    label("Function_7_4758")

    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4770():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4770)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_7_4758 end

    def Function_8_4789(): pass

    label("Function_8_4789")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4794")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47B2")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_4794")

    label("loc_47B2")

    Return()

    # Function_8_4789 end

    def Function_9_47B3(): pass

    label("Function_9_47B3")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_47BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47DC")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_47BE")

    label("loc_47DC")

    Return()

    # Function_9_47B3 end

    def Function_10_47DD(): pass

    label("Function_10_47DD")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_47E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4803")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_47E8")

    label("loc_4803")

    Return()

    # Function_10_47DD end

    def Function_11_4804(): pass

    label("Function_11_4804")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_11_4804 end

    def Function_12_4821(): pass

    label("Function_12_4821")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_482C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_484A")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_482C")

    label("loc_484A")

    Return()

    # Function_12_4821 end

    def Function_13_484B(): pass

    label("Function_13_484B")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4856")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4871")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_4856")

    label("loc_4871")

    Return()

    # Function_13_484B end

    def Function_14_4872(): pass

    label("Function_14_4872")

    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x3)
    Return()

    # Function_14_4872 end

    def Function_15_4890(): pass

    label("Function_15_4890")

    SetChrPos(0xFE, 17000, 450, 138450, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_48B4():
        OP_95(0xFE, 15400, 450, 138450, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48B4)

    def lambda_48CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48CE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_48F4():
        OP_9D(0xFE, 0x2F08, 0x0, 0x219BC, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48F4)
    WaitChrThread(0xFE, 1)
    Sound(39, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    Return()

    # Function_15_4890 end

    def Function_16_491C(): pass

    label("Function_16_491C")

    SetChrPos(0xFE, 17000, 450, 138450, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_4940():
        OP_95(0xFE, 15400, 450, 138450, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4940)

    def lambda_495A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_495A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_93(0xFE, 0xE1, 0x0)

    def lambda_4987():
        OP_9D(0xFE, 0x35AC, 0x0, 0x218AE, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4987)
    WaitChrThread(0xFE, 1)
    Sound(39, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    Return()

    # Function_16_491C end

    def Function_17_49AF(): pass

    label("Function_17_49AF")

    Call(0, 15)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_49BD():
        OP_95(0xFE, 8530, 0, 139830, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49BD)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_17_49AF end

    def Function_18_49F0(): pass

    label("Function_18_49F0")

    Call(0, 15)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_49FE():
        OP_95(0xFE, 8400, 0, 136320, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49FE)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_18_49F0 end

    def Function_19_4A31(): pass

    label("Function_19_4A31")

    Call(0, 15)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_4A3F():
        OP_95(0xFE, 5740, 0, 137380, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A3F)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_19_4A31 end

    def Function_20_4A72(): pass

    label("Function_20_4A72")

    Call(0, 16)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_4A80():
        OP_95(0xFE, 18070, 0, 129470, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A80)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_20_4A72 end

    def Function_21_4AB3(): pass

    label("Function_21_4AB3")

    Call(0, 16)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_4AC1():
        OP_95(0xFE, 18840, 0, 132120, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4AC1)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_4AB3 end

    def Function_22_4AF4(): pass

    label("Function_22_4AF4")

    Call(0, 16)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_4B02():
        OP_95(0xFE, 17670, 0, 134980, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B02)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_22_4AF4 end

    def Function_23_4B35(): pass

    label("Function_23_4B35")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B4C")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("Function_23_4B35")

    label("loc_4B4C")

    Return()

    # Function_23_4B35 end

    def Function_24_4B4D(): pass

    label("Function_24_4B4D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B66")
    Sound(832, 0, 100, 0)
    Sleep(500)
    Jump("Function_24_4B4D")

    label("loc_4B66")

    Return()

    # Function_24_4B4D end

    def Function_25_4B67(): pass

    label("Function_25_4B67")

    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Return()

    # Function_25_4B67 end

    SaveToFile()

Try(main)
