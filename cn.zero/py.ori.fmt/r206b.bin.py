from ZeroScenarioHelper import *

def main():
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
        "军犬",                   # 1
        "军犬",                   # 2
        "军犬",                   # 3
        "军犬",                   # 4
        "军犬",                   # 5
        "军犬",                   # 6
        "军犬",                   # 7
        "军犬",                   # 8
        "军犬",                   # 9
        "军犬",                   # 10
        "黑手党",                 # 11
        "黑手党",                 # 12
        "黑手党",                 # 13
        "白狼",                   # 14
        "白狼",                   # 15
        "白狼",                   # 16
        "白狼",                   # 17
        "白狼",                   # 18
        "白狼",                   # 19
        "玲",                     # 20
        "亚里欧斯",               # 21
        "车",                     # 22
        "SE控制",                 # 23
        "BR206b",                 # 24
        "克洛斯贝尔市方向",       # 25
        "矿山镇玛因兹方向",       # 26
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

    PlaceName(-3.0, 0.0, -15.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(87.0, 6.0, 122.0, 0x0000, 0x0000, "矿山镇玛因兹方向")

    ScpFunction((
        "Function_0_598",          # 00, 0
        "Function_1_5BC",          # 01, 1
        "Function_2_5D4",          # 02, 2
        "Function_3_70A",          # 03, 3
        "Function_4_1718",         # 04, 4
        "Function_5_173F",         # 05, 5
        "Function_6_1769",         # 06, 6
        "Function_7_4413",         # 07, 7
        "Function_8_4444",         # 08, 8
        "Function_9_446E",         # 09, 9
        "Function_10_4498",        # 0A, 10
        "Function_11_44BF",        # 0B, 11
        "Function_12_44DC",        # 0C, 12
        "Function_13_4506",        # 0D, 13
        "Function_14_452D",        # 0E, 14
        "Function_15_454B",        # 0F, 15
        "Function_16_45D7",        # 10, 16
        "Function_17_466A",        # 11, 17
        "Function_18_46AB",        # 12, 18
        "Function_19_46EC",        # 13, 19
        "Function_20_472D",        # 14, 20
        "Function_21_476E",        # 15, 21
        "Function_22_47AF",        # 16, 22
        "Function_23_47F0",        # 17, 23
        "Function_24_4808",        # 18, 24
        "Function_25_4822",        # 19, 25
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C1")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('复苏药', 1)"), scpexpr(EXPR_END)), "loc_653")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_6BC")

    label("loc_653")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_6BC")

    Jump("loc_6FE")

    label("loc_6C1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_6FE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_5D4 end

    def Function_3_70A(): pass

    label("Function_3_70A")

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

    def lambda_99F():
        OP_9B(0x0, 0xFE, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_99F)

    def lambda_9B4():
        OP_9B(0x0, 0xFE, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9B4)

    def lambda_9C9():
        OP_9B(0x0, 0xFE, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9C9)
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

    def lambda_B5D():
        OP_95(0xFE, 11210, 0, 134270, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B5D)

    def lambda_B77():
        OP_95(0xFE, 13320, 0, 132200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B77)

    def lambda_B91():
        OP_95(0xFE, 10820, 0, 130550, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B91)
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
        "#11P呜噜噜噜！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        "#11P汪汪！\x02",
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_64(0x9)
    OP_64(0xA)
    EndChrThread(0x8, 0x0)

    def lambda_C78():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C78)
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

    def lambda_CC2():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_CC2)

    def lambda_CDB():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_CDB)
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
        "#5P什、什么……？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x12,
        (
            "#5P喂，为什么\x01",
            "这么快就回来了？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x13,
        (
            "#5P我们的指示可是\x01",
            "袭击镇里的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x13,
        (
            "#5P你们怎么回事，\x01",
            "回来得也太快了吧？\x02",
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
        "罗伊德的声音",
        "#1P──到此为止。\x02",
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

    def lambda_EB2():
        OP_95(0xFE, 17030, 0, 132160, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EB2)

    def lambda_ECC():
        OP_95(0xFE, 16490, 0, 130310, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ECC)

    def lambda_EE6():
        OP_95(0xFE, 19410, 0, 131940, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EE6)

    def lambda_F00():
        OP_95(0xFE, 18620, 0, 129940, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F00)
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
        "#5P什、什么！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x13,
        "#11P你们是……！？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#0013F#6P克洛斯贝尔警察局·特别任务支援科的人。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        (
            "#0101F#6P各位是『鲁巴彻商会』的成员吧？\x02\x03",

            "在此以损坏公物以及人身伤害的嫌疑\x01",
            "逮捕你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x12,
        "#5P警、警察……！？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x13,
        "#11P怎么会来这种镇子……\x02",
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
            "#5P『特别任务支援科』……\x01",
            "是让法比奥他们搞砸了计划的那个……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x13,
        (
            "#11P原来是阻挠了旧城区计划的\x01",
            "那些小鬼吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#0302F#12P哈哈，看起来，我们的名字\x01",
            "好像已经被他们记住了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#0204F#12P现在是否应该\x01",
            "感到荣幸呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x12,
        "#5P嘁……也罢。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x12,
        (
            "#5P不过就是几个来捣乱的警察而已，\x01",
            "只要在此让他们吃点苦头就好了。\x02",
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
            "#11P我们的同伴之前\x01",
            "似乎承蒙你们关照了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x13,
        (
            "#11P你们好像也挺疼爱\x01",
            "我们的狗……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x12,
        (
            "#5P正好……\x01",
            "在此给你们回个礼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#0013F#6P……你们是打算反抗吗？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x13,
        (
            "#11P呼哈哈！\x01",
            "那正是我们要说的话啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x8, 500)

    #C0028
    ChrTalk(
        0x12,
        "#5P──准备攻击！\x02",
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

    def lambda_1437():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1437)

    def lambda_1450():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1450)

    def lambda_1469():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1469)
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

    def lambda_14E2():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14E2)

    def lambda_14EF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_14EF)
    Sleep(100)

    def lambda_14FF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14FF)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)

    def lambda_1518():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1518)

    def lambda_1525():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1525)
    Sleep(100)

    def lambda_1535():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1535)

    def lambda_1542():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1542)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0029
    ChrTalk(
        0x101,
        "#0010F#11P呜……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0310F#12P嘁……\x01",
            "竟然用药回复了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x13,
        (
            "#11P哼哼哼……\x01",
            "我们毕竟也是职业人士嘛。\x02",
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
        "#5P──上，干掉他们！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x12,
        (
            "#5P把这些家伙的喉咙\x01",
            "都给我撕裂！\x02",
        )
    )

    CloseMessageWindow()
    Sound(836, 0, 100, 0)

    #C0034
    ChrTalk(
        0x8,
        "#5P呜噜噜噜……！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        "#5P嗷呜！！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        "#0101F#6P来了……！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        "#0007F#2P我们也不会手软的！\x02",
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

    # Function_3_70A end

    def Function_4_1718(): pass

    label("Function_4_1718")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1723")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_173E")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_1723")

    label("loc_173E")

    Return()

    # Function_4_1718 end

    def Function_5_173F(): pass

    label("Function_5_173F")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_174A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1768")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_174A")

    label("loc_1768")

    Return()

    # Function_5_173F end

    def Function_6_1769(): pass

    label("Function_6_1769")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3217")

    #C0038
    ChrTalk(
        0x101,
        "#0010F#2P呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#0106F#12P真、真是\x01",
            "有点棘手呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x103,
        (
            "#0208F#2P没想到竟然\x01",
            "可以使用那种方法操纵狗……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        (
            "#0301F#4P哼……\x01",
            "还挺熟练的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x12,
        "#5P不、不可能……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x13,
        (
            "#1P呜……\x01",
            "竟被这些小鬼……！\x02",
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
            "#0003F#12P──继续抵抗也是徒劳。\x02\x03",

            "#0001F明早，我们就会\x01",
            "将你们交给警备队。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        (
            "#0304F#4P嗯，你们今晚\x01",
            "就住在仓库吧。\x02\x03",

            "#0300F我们会负起责任，\x01",
            "看住你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x12,
        "#5P哼哼哼……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x13,
        "#1P哈哈哈……！\x02",
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

    def lambda_2206():
        OP_9D(0xFE, 0x3692, 0x0, 0x21CDC, 0x258, 0x9C4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2206)
    Sleep(200)
    Sound(814, 0, 100, 0)
    OP_93(0x13, 0xE1, 0x0)

    def lambda_2233():
        OP_9D(0xFE, 0x303E, 0x0, 0x22132, 0x320, 0x9C4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2233)
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
        "#0007F#6P站住……！\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        "#0307F哈，怎么会让你们跑掉！\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x12,
        "#5P哼哼，不要误会……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x13,
        (
            "#1P既然如此，\x01",
            "我们也只有不择手段了！\x02",
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

    def lambda_234F():
        OP_9D(0xFE, 0x3638, 0x0, 0x220E2, 0x258, 0xDAC)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_234F)
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
        "#0205F#11P！？\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        "#0105F#11P还、还有吗！？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        "#0301F#11P嘁……！\x02",
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

    def lambda_2512():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2512)
    Sleep(50)

    def lambda_252A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_252A)
    Sleep(100)

    def lambda_2542():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2542)
    Sleep(50)

    def lambda_255A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_255A)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)

    def lambda_257B():
        OP_93(0xFE, 0xB4, 0x2EE)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_257B)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)

    def lambda_2594():
        OP_93(0xFE, 0xB4, 0x2EE)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2594)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)

    def lambda_25AD():
        OP_93(0xFE, 0xB4, 0x2EE)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_25AD)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    def lambda_25C6():
        OP_93(0xFE, 0xB4, 0x2EE)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_25C6)
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

    def lambda_260B():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_260B)

    def lambda_2624():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2624)
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

    def lambda_2680():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2680)

    def lambda_2699():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2699)
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
        "#0013F#5P糟了……！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#0310F#5P十只吗……\x01",
            "这可真是太多了点啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x12,
        (
            "#5P哼哼哼……\x01",
            "形势逆转了吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x13,
        (
            "#1P这是小看我们的\x01",
            "回礼……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x13,
        (
            "#1P我们会花足时间，\x01",
            "慢慢虐杀你们的……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#0010F#5P呜……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#0108F#5P……这样下去……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        "#0206F#5P……陷入危机了呢。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0063
    ChrTalk(
        0x104,
        "#0308F#5P#30W（嘁，既然如此，只能……）\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x13,
        (
            "#1P哼哼……已经向女神\x01",
            "祈祷完毕了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x12,
        (
            "#5P那么，就开始\x01",
            "快乐的处刑时间──\x02",
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
        "#0005F#5P什么……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x12,
        "#5P什、什么！？\x02",
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
    SetChrName("白狼")

    #A0068
    AnonymousTalk(
        0xFF,
        "#1P呜噜噜噜噜噜……\x02",
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
        "#0205F#12P那、那是……！\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        "#0105F#6P那个时候的白狼……！\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0309F#12P哈哈……\x01",
            "带着伙伴前来参战了吗？\x02",
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
            "#1P你、你们……！\x01",
            "有什么可害怕的！？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x12,
        (
            "#5P从数量上来看，\x01",
            "我们也没输啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x12,
        "#5P不准夹着尾巴蜷成一团！\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#0004F#6P嗯，这就是\x01",
            "正牌和假货的实力差距了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#0302F#12P的确……\x01",
            "狗是赢不了狼的。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        (
            "#0204F#12P它们好像因为名誉被损害\x01",
            "而生气了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x102,
        (
            "#0102F#6P来算总账了……\x01",
            "是这样吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(14080, 600, 137980, 2000)
    SetCameraDistance(18740, 2000)

    def lambda_30D0():
        OP_96(0xFE, 0x3372, 0x0, 0x21250, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30D0)
    Sleep(50)

    def lambda_30ED():
        OP_95(0xFE, 11270, 0, 135430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30ED)
    Sleep(100)

    def lambda_310A():
        OP_95(0xFE, 13600, 0, 133690, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_310A)
    Sleep(50)

    def lambda_3127():
        OP_95(0xFE, 11770, 0, 132800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3127)
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
        "#5P呜……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#0003F#12P……这次彻底结束了。\x02\x03",

            "#0001F以损坏公物、人身伤害、\x01",
            "以及妨碍执行公务的嫌疑，\x01",
            "在此逮捕你们──\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_3217")

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

    def lambda_358F():
        OP_95(0xFE, -1110, 9450, 159020, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_358F)
    Sleep(300)
    SetChrChipByIndex(0x16, 0x36)
    SetChrSubChip(0x16, 0x0)
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x16, 0x10E, 0x1F4)
    BeginChrThread(0x16, 0, 0, 13)

    def lambda_35CC():
        OP_95(0xFE, 1170, 10000, 158500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_35CC)
    Sleep(200)
    SetChrChipByIndex(0x17, 0x36)
    SetChrSubChip(0x17, 0x0)
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x17, 0x10E, 0x1F4)
    BeginChrThread(0x17, 0, 0, 13)

    def lambda_3609():
        OP_95(0xFE, 320, 10000, 160370, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3609)

    def lambda_3623():

        label("loc_3623")

        TurnDirection(0xFE, 0x15, 100)
        Yield()
        Jump("loc_3623")

    QueueWorkItem2(0x14, 3, lambda_3623)
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

    def lambda_3689():
        OP_95(0xFE, 11000, 10000, 153000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3689)
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
        "白狼",
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
        "穿连衣裙的少女",
        (
            "#5P呵呵……\x01",
            "果然察觉到了啊。\x02",
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
            "#1P那位狼先生究竟是何方神圣？\x01",
            "似乎并不是等闲之辈……\x02\x03",

            "呵呵……不过，\x01",
            "大哥哥们也真是掉以轻心呢。\x02\x03",

            "要是那些狼先生没来相助的话，\x01",
            "可要怎么办呢？\x02\x03",

            "嘻嘻……真是不堪设想啊。\x02",
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
        "男人的声音",
        "#2P……嗯，应该说是后果难料吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0085
    ChrTalk(
        0x1B,
        "#3305F#5P哎呀……\x02",
    )

    CloseMessageWindow()
    OP_68(-51770, 16000, 123370, 4000)

    def lambda_39E2():
        OP_95(0xFE, -54170, 16000, 122860, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_39E2)
    WaitChrThread(0x1C, 1)
    OP_6F(0x1)
    SetCameraDistance(21050, 80000)
    Sleep(300)

    #C0086
    ChrTalk(
        0x1B,
        (
            "#3304F#6P呵呵，你也来了啊。\x02\x03",

            "大概是打算在他们无力应对时\x01",
            "出手相助吧？\x02\x03",

            "#3302F『风之剑圣』……\x01",
            "亚里欧斯·马克莱因。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1C,
        (
            "#1403F#5P……你也是吧。\x02\x03",

            "#1401F结社『噬身之蛇』的执行者。\x01",
            "Ｎｏ．──\x02\x03",      #line#50

            "ⅩⅤ──『歼灭天使』玲。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x1B,
        (
            "#3309F#6P嘻嘻……\x01",
            "都不用自我介绍了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1C, 400)
    Sleep(300)

    #C0089
    ChrTalk(
        0x1B,
        (
            "#3302F#12P听说你收到了晋升Ｓ级的邀请，\x01",
            "但又谢绝掉了，实力果然名不虚传呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x1C,
        (
            "#1403F#5P老实说，那个级别我实在受之有愧。\x02\x03",

            "被期待为接替卡西乌斯·布莱特的人选，\x01",
            "这份担子未免也太过沉重了。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x1B,
        (
            "#3302F#12P呵呵……这可难说吧？\x02\x03",

            "#3304F玲以前也曾与卡西乌斯·布莱特\x01",
            "有过一面之缘……\x02\x03",

            "如果只论剑术，\x01",
            "你恐怕还在他之上吧？\x02\x03",

            "#3300F没错，玲感觉得到。你应该可以\x01",
            "与玲所认识的那个最强之人相匹敌呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x1C,
        (
            "#1404F#5P呵呵……\x01",
            "该说不胜荣幸吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 400)
    Sleep(500)

    #C0093
    ChrTalk(
        0x1C,
        (
            "#1401F#5P──我早就察觉到了。\x01",
            "这几个月来，你一直滞留在\x01",
            "克洛斯贝尔自治州。\x02\x03",

            "一开始，还以为\x01",
            "你要开办什么『茶会』……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x5A, 0x190)
    Sleep(300)

    #C0094
    ChrTalk(
        0x1B,
        (
            "#3304F#6P呵呵，你根本不明白呢。\x02\x03",

            "就算玲不开茶会，\x01",
            "克洛斯贝尔也已经足够刺激了吧？\x02\x03",

            "#3302F在这种情势下再举办多余的活动，\x01",
            "那可就太不识趣了。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x1C,
        (
            "#1403F#5P听你这么说，我就放心了。\x02\x03",

            "看来，你只是出于个人原因\x01",
            "而暂时留在此地……\x02\x03",

            "#1400F──可是，你打算\x01",
            "逃避『他们』到几时？\x02",
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
            "#1403F#5P我无意对你们之间的是非\x01",
            "妄加评论。\x02\x03",

            "他们能来克洛斯贝尔，\x01",
            "对我个人而言，也算是帮了大忙。\x02\x03",

            "#1400F只是……面对着近在眼前的答案，\x01",
            "你总不能永远逃避下去吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x1B,
        (
            "#3306F#6P……请别管这件事。\x02\x03",

            "#3300F而且，玲会留在这里，\x01",
            "也不仅是因为艾丝蒂尔他们哦。\x02\x03",

            "既要修理『他』……\x01",
            "还必须要确认一些事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x1C,
        "#1405F#5P必须要确认一些事情……？\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x1B,
        (
            "#3304F#6P呵呵，和你没关系啦。\x02\x03",

            "#3302F我保证会安分守己的，\x01",
            "你就不要管玲了。\x02\x03",

            "当然……也不许对\x01",
            "艾丝蒂尔他们说些多余的话哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x1C,
        (
            "#1404F#5P……明白了。\x02\x03",

            "#1402F只要你不危害这片土地，\x01",
            "我便发誓绝不会多加干涉。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x1B,
        "#3309F#6P呵呵，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_93(0x1B, 0xB4, 0x190)
    Sleep(300)

    #C0103
    ChrTalk(
        0x1B,
        (
            "#3304F#5P那，玲先走了哦。\x02\x03",

            "#3302F贵安……『风之剑圣』先生。\x02",
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

    def lambda_4170():

        label("loc_4170")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_4170")

    QueueWorkItem2(0x1C, 1, lambda_4170)
    OP_68(-51970, 16000, 121990, 5000)
    MoveCamera(68, 25, 0, 5000)
    SetCameraDistance(22500, 5000)

    def lambda_41A7():
        OP_96(0xFE, 0xFFFF1AA0, 0x3E80, 0x1B5B2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_41A7)
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
            "#1403F#5P迷途的小猫吗……\x02\x03",

            "可是，这样下去的话，\x01",
            "她与他们都只会继续迷惘。\x02\x03",

            "#1401F如果能有第三方带来好的契机，\x01",
            "或许……\x02",
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
        "#1404F#5P呵……应该是我想多了吧。\x02",
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

    # Function_6_1769 end

    def Function_7_4413(): pass

    label("Function_7_4413")

    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_442B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_442B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_7_4413 end

    def Function_8_4444(): pass

    label("Function_8_4444")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_444F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_446D")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_444F")

    label("loc_446D")

    Return()

    # Function_8_4444 end

    def Function_9_446E(): pass

    label("Function_9_446E")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4479")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4497")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_4479")

    label("loc_4497")

    Return()

    # Function_9_446E end

    def Function_10_4498(): pass

    label("Function_10_4498")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44BE")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_44A3")

    label("loc_44BE")

    Return()

    # Function_10_4498 end

    def Function_11_44BF(): pass

    label("Function_11_44BF")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_11_44BF end

    def Function_12_44DC(): pass

    label("Function_12_44DC")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4505")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_44E7")

    label("loc_4505")

    Return()

    # Function_12_44DC end

    def Function_13_4506(): pass

    label("Function_13_4506")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4511")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_452C")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_4511")

    label("loc_452C")

    Return()

    # Function_13_4506 end

    def Function_14_452D(): pass

    label("Function_14_452D")

    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x3)
    Return()

    # Function_14_452D end

    def Function_15_454B(): pass

    label("Function_15_454B")

    SetChrPos(0xFE, 17000, 450, 138450, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_456F():
        OP_95(0xFE, 15400, 450, 138450, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_456F)

    def lambda_4589():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4589)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_45AF():
        OP_9D(0xFE, 0x2F08, 0x0, 0x219BC, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45AF)
    WaitChrThread(0xFE, 1)
    Sound(39, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    Return()

    # Function_15_454B end

    def Function_16_45D7(): pass

    label("Function_16_45D7")

    SetChrPos(0xFE, 17000, 450, 138450, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_45FB():
        OP_95(0xFE, 15400, 450, 138450, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45FB)

    def lambda_4615():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4615)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_93(0xFE, 0xE1, 0x0)

    def lambda_4642():
        OP_9D(0xFE, 0x35AC, 0x0, 0x218AE, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4642)
    WaitChrThread(0xFE, 1)
    Sound(39, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    Return()

    # Function_16_45D7 end

    def Function_17_466A(): pass

    label("Function_17_466A")

    Call(0, 15)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_4678():
        OP_95(0xFE, 8530, 0, 139830, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4678)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_17_466A end

    def Function_18_46AB(): pass

    label("Function_18_46AB")

    Call(0, 15)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_46B9():
        OP_95(0xFE, 8400, 0, 136320, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46B9)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_18_46AB end

    def Function_19_46EC(): pass

    label("Function_19_46EC")

    Call(0, 15)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_46FA():
        OP_95(0xFE, 5740, 0, 137380, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46FA)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_19_46EC end

    def Function_20_472D(): pass

    label("Function_20_472D")

    Call(0, 16)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_473B():
        OP_95(0xFE, 18070, 0, 129470, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_473B)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_20_472D end

    def Function_21_476E(): pass

    label("Function_21_476E")

    Call(0, 16)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_477C():
        OP_95(0xFE, 18840, 0, 132120, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_477C)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_476E end

    def Function_22_47AF(): pass

    label("Function_22_47AF")

    Call(0, 16)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_47BD():
        OP_95(0xFE, 17670, 0, 134980, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_47BD)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_22_47AF end

    def Function_23_47F0(): pass

    label("Function_23_47F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4807")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("Function_23_47F0")

    label("loc_4807")

    Return()

    # Function_23_47F0 end

    def Function_24_4808(): pass

    label("Function_24_4808")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4821")
    Sound(832, 0, 100, 0)
    Sleep(500)
    Jump("Function_24_4808")

    label("loc_4821")

    Return()

    # Function_24_4808 end

    def Function_25_4822(): pass

    label("Function_25_4822")

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

    # Function_25_4822 end

    SaveToFile()

Try(main)
