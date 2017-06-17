from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r000b.bin",                # FileName
        "r000b",                    # MapName
        "r000b",                    # Location
        0x005E,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 5700, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 2, 0, 3],
    )

    BuildStringList((
        "r000b",                  # 0
        "ツァイト",               # 1
        "マフィア",               # 2
        "マフィア",               # 3
        "マフィア",               # 4
        "マフィア",               # 5
        "マフィア",               # 6
        "マフィア",               # 7
        "マフィア",               # 8
        "マフィア",               # 9
        "マフィア",               # 10
        "マフィア",               # 11
        "マフィア",               # 12
        "マフィア",               # 13
        "マフィア",               # 14
        "マフィア",               # 15
        "ドーベンカイザー",       # 16
        "ドーベンカイザー",       # 17
        "警備隊員",               # 18
        "警備隊員",               # 19
        "警備隊員",               # 20
        "警備隊員",               # 21
        "警備隊員",               # 22
        "警備隊員",               # 23
        "車１",                   # 24
        "車２",                   # 25
        "車３",                   # 26
        "ディーター総裁",         # 27
        "マリアベル",             # 28
        "SE制御",                 # 29
        "br000b",                 # 30
        "クロスベル市方面",       # 31
        "アルモリカ村・タングラム門方面",# 32
    ))

    ATBonus("ATBonus_490", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_550", 6, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_554", 10, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_558", 4, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_55C", 12, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_560", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_564", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_568", 9, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_56C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_530", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_534", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_538", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_53C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_540", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_544", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_548", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_54C", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_570", 0x000A, 34, 6, 0, 0, 0, 0, 0, "br000b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31003.dat", "ms67101.dat", "ms67101.dat", "ms31103.dat", "ms31901.dat", "ms31901.dat", 0, "MonsterBattlePostion_550", "MonsterBattlePostion_530", "ed7405", "ed7000", "ATBonus_490"),
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-17.0, 0.0, -7.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(203.0, 0.0, 27.5, 0x0000, 0x0000, "アルモリカ村・タングラム門方面")

    ScpFunction((
        "Function_0_6B8",          # 00, 0
        "Function_1_6D4",          # 01, 1
        "Function_2_6F0",          # 02, 2
        "Function_3_728",          # 03, 3
        "Function_4_729",          # 04, 4
        "Function_5_15E8",         # 05, 5
        "Function_6_160E",         # 06, 6
        "Function_7_1652",         # 07, 7
        "Function_8_1681",         # 08, 8
        "Function_9_16B0",         # 09, 9
        "Function_10_16DF",        # 0A, 10
        "Function_11_1732",        # 0B, 11
        "Function_12_3044",        # 0C, 12
        "Function_13_3164",        # 0D, 13
        "Function_14_32C6",        # 0E, 14
        "Function_15_3314",        # 0F, 15
        "Function_16_3374",        # 10, 16
        "Function_17_33D4",        # 11, 17
        "Function_18_3623",        # 12, 18
        "Function_19_3781",        # 13, 19
        "Function_20_3954",        # 14, 20
        "Function_21_39F9",        # 15, 21
        "Function_22_3A6A",        # 16, 22
        "Function_23_3ADB",        # 17, 23
        "Function_24_3B46",        # 18, 24
        "Function_25_3B7D",        # 19, 25
        "Function_26_3BB4",        # 1A, 26
        "Function_27_3C05",        # 1B, 27
        "Function_28_3C50",        # 1C, 28
        "Function_29_3CA1",        # 1D, 29
        "Function_30_3CFE",        # 1E, 30
        "Function_31_3D25",        # 1F, 31
        "Function_32_3D4C",        # 20, 32
        "Function_33_3D73",        # 21, 33
        "Function_34_3D9A",        # 22, 34
        "Function_35_3DC1",        # 23, 35
        "Function_36_3DE8",        # 24, 36
        "Function_37_3E0F",        # 25, 37
        "Function_38_3E36",        # 26, 38
        "Function_39_3E8C",        # 27, 39
        "Function_40_3EE2",        # 28, 40
        "Function_41_3EFC",        # 29, 41
        "Function_42_3F16",        # 2A, 42
        "Function_43_3F33",        # 2B, 43
        "Function_44_47EF",        # 2C, 44
        "Function_45_4876",        # 2D, 45
        "Function_46_4A44",        # 2E, 46
        "Function_47_4CC3",        # 2F, 47
        "Function_48_4D44",        # 30, 48
        "Function_49_4F12",        # 31, 49
        "Function_50_5191",        # 32, 50
        "Function_51_5200",        # 33, 51
        "Function_52_5269",        # 34, 52
        "Function_53_52EB",        # 35, 53
        "Function_54_5342",        # 36, 54
        "Function_55_538D",        # 37, 55
        "Function_56_5415",        # 38, 56
        "Function_57_5452",        # 39, 57
        "Function_58_55D6",        # 3A, 58
        "Function_59_5B0D",        # 3B, 59
        "Function_60_5C2D",        # 3C, 60
        "Function_61_5D4D",        # 3D, 61
        "Function_62_5D6B",        # 3E, 62
        "Function_63_5D83",        # 3F, 63
        "Function_64_5D9D",        # 40, 64
    ))


    def Function_0_6B8(): pass

    label("Function_0_6B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D3")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_6B8")

    label("loc_6D3")

    Return()

    # Function_0_6B8 end

    def Function_1_6D4(): pass

    label("Function_1_6D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EF")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_6D4")

    label("loc_6EF")

    Return()

    # Function_1_6D4 end

    def Function_2_6F0(): pass

    label("Function_2_6F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_704")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_727")

    label("loc_704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_718")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 11)
    Jump("loc_727")

    label("loc_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_727")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 43)

    label("loc_727")

    Return()

    # Function_2_6F0 end

    def Function_3_728(): pass

    label("Function_3_728")

    Return()

    # Function_3_728 end

    def Function_4_729(): pass

    label("Function_4_729")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x9F, 0xFF, 0xFF)
    AddParty(0x57, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch02750.itc", 0x1E)
    LoadChrToIndex("chr/ch02751.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00051.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00151.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00251.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch00351.itc", 0x27)
    LoadChrToIndex("chr/ch31050.itc", 0x28)
    LoadChrToIndex("chr/ch31051.itc", 0x29)
    LoadChrToIndex("chr/ch31150.itc", 0x2A)
    LoadChrToIndex("chr/ch31151.itc", 0x2B)
    LoadChrToIndex("chr/ch31950.itc", 0x2C)
    LoadChrToIndex("chr/ch31951.itc", 0x2D)
    LoadChrToIndex("monster/ch67150.itc", 0x2E)
    LoadChrToIndex("monster/ch67151.itc", 0x2F)
    LoadChrToIndex("apl/ch50111.itc", 0x30)
    LoadChrToIndex("chr/ch02752.itc", 0x31)
    LoadChrToIndex("chr/ch02702.itc", 0x32)
    SoundLoad(891)
    OP_68(24300, 1000, 0, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 15600, 0, 0, 90)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 14500, 0, 1000, 90)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 13100, 0, 0, 90)
    SetChrPos(0x104, 13900, 0, -1000, 90)
    SetChrPos(0x1A0, 45600, 0, -1000, 90)
    SetChrPos(0x158, 43900, 0, -2000, 90)
    SetChrFlags(0x1A0, 0x80)
    SetChrBattleFlags(0x1A0, 0x8000)
    SetChrFlags(0x158, 0x80)
    SetChrBattleFlags(0x158, 0x8000)
    SetChrChipByIndex(0x8, 0x32)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, 13300, 0, 2600, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x2A)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x2C)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    OP_52(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x18, 0x2E)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    OP_52(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 77000, 0, -1400, 270)
    SetChrPos(0xA, 77000, 0, 1400, 270)
    SetChrPos(0xB, 79000, 0, 0, 270)
    SetChrPos(0xD, 80500, 0, -900, 270)
    SetChrPos(0xE, 80500, 0, 900, 270)
    SetChrPos(0x17, 78400, 0, -3400, 270)
    SetChrPos(0x18, 78400, 0, 3400, 270)

    def lambda_9BC():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9BC)
    Sleep(50)

    def lambda_9D9():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9D9)
    Sleep(50)

    def lambda_9F6():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9F6)
    Sleep(50)

    def lambda_A13():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A13)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x24, 1, 0, 41)

    def lambda_A5A():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A5A)
    SetCameraDistance(21000, 4000)
    FadeToBright(2000, 0)
    OP_6F(0x10)
    StopBGM(0x1F40)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(44500, 1000, 0, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(19500, 1500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x24, 0x1)
    SetChrChipByIndex(0x8, 0x32)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x87, 0x1F4)
    OP_6F(0x10)

    #C0001
    ChrTalk(
        0x101,
        "#0006F#5Pはあはあ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0002
    ChrTalk(
        0x101,
        (
            "#0000F#11P……さすがにここまで\x01",
            "追ってくる気配はないな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B5E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B5E)
    Sleep(100)

    def lambda_B6E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B6E)
    Sleep(50)

    def lambda_B7E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B7E)
    WaitChrThread(0x104, 2)

    #C0003
    ChrTalk(
        0x102,
        (
            "#0106F#11Pええ……\x01",
            "課長たちのおかげでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x103,
        "#11P#0208F……無事だといいんですけど。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        "#11P#0303F今は女神に祈るしかねぇな……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#0006F#11Pああ……\x02\x03",

            "#0001F……キーア、シズクちゃん。\x01",
            "大丈夫か？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C61():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C61)
    Sleep(50)

    def lambda_C71():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C71)
    Sleep(50)

    def lambda_C81():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C81)
    WaitChrThread(0x103, 2)

    #N0007
    NpcTalk(
        0x104,
        "シズク",
        "#5P#6000Fは、はい……\x02",
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x101,
        "キーア",
        (
            "#5P#1110Fキーアもへいきだよー。\x02\x03",

            "#1109Fえへへ、みんなとはじめて\x01",
            "会った時みたいだねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#0012F#11Pはは……そうだな。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x104,
        (
            "#6P#0306Fあの競売会から\x01",
            "まだ一月ちょっとかよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        "#6P#0202Fちょっと信じられませんね……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#0104F#5Pふふっ……\x02\x03",

            "#0100F──さてと、\x01",
            "このまま街道に出るとして。\x02\x03",

            "先にタングラム門に連絡する？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0013
    ChrTalk(
        0x101,
        (
            "#0000F#11Pああ、頼む。\x02\x03",

            "繋がりにくかったら\x01",
            "ノエル曹長の方でもいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#0100F#5Pええ、分かったわ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x30)
    SetChrSubChip(0x102, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    def lambda_E9A():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E9A)
    Sleep(50)

    def lambda_EAA():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_EAA)
    Sound(807, 0, 100, 0)
    Sleep(800)
    Sound(891, 2, 100, 0)
    Sleep(3000)

    #C0015
    ChrTalk(
        0x102,
        "#0108F#5P……話し中みたい……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#12P#0300F無理もねぇ……\x01",
            "相当、混乱してんだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#6P#0206Fしばらく通信は\x01",
            "繋がりにくいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_24(0x37B)
    Sound(807, 0, 100, 0)
    Sleep(500)

    #C0018
    ChrTalk(
        0x102,
        (
            "#0100F#5P仕方ないわ。\x01",
            "直接ノエルさんの方に──\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x2BC)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(45550, 1000, 160, 1000)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x24, 1, 0, 40)

    def lambda_FE2():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FE2)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x24, 0x1)
    SetChrChipByIndex(0x8, 0x31)
    SetChrSubChip(0x8, 0x3)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    #Sound(2058, 255, 100, 0)    #voice#Zeit

    #C0019
    ChrTalk(
        0x8,
        "#6P#1201Fグルルル……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_10B3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10B3)
    Sleep(50)

    def lambda_10C3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10C3)
    Sleep(50)

    def lambda_10D3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10D3)
    Sleep(50)

    def lambda_10E3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10E3)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x102, 2)

    #C0020
    ChrTalk(
        0x101,
        "#0005F#6Pなんだ……！？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#6P#0301Fおい、まさか……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    BeginChrThread(0x9, 3, 0, 7)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 7)
    Sleep(50)
    BeginChrThread(0x17, 3, 0, 10)
    BeginChrThread(0x18, 3, 0, 10)
    BeginChrThread(0x24, 1, 0, 40)
    BeginChrThread(0xB, 3, 0, 8)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 9)
    OP_68(57000, 1000, 0, 2000)
    MoveCamera(35, 20, 0, 2000)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x18, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_6F(0x41)

    #C0022
    ChrTalk(
        0x101,
        "#0007Fルバーチェ……！？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0201F病院を襲撃したのとは\x01",
            "別働隊みたいですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#0310F３００人近い大所帯だ。\x01",
            "他にもいるとは思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#0103Fここは突破するしか\x01",
            "道はなさそうね……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(47500, 1000, 0, 0)
    MoveCamera(90, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x9, 54000, 0, -1400, 270)
    SetChrPos(0xA, 54000, 0, 1400, 270)
    SetChrPos(0xB, 56000, 0, 0, 270)
    SetChrPos(0xD, 57500, 0, -900, 270)
    SetChrPos(0xE, 57500, 0, 900, 270)
    SetChrPos(0x17, 55400, 0, -3400, 270)
    SetChrPos(0x18, 55400, 0, 3400, 270)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x1A0, 0x80)
    ClearChrBattleFlags(0x1A0, 0x8000)
    ClearChrFlags(0x158, 0x80)
    ClearChrBattleFlags(0x158, 0x8000)
    OP_0D()

    #C0026
    ChrTalk(
        0x101,
        (
            "#0013Fキーア、シズクちゃん。\x01",
            "出来るだけ下がっててくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x1A0,
        "#1101F#6P……うんっ……！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x158,
        "#6001F#12P#Nは、はいっ……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x158, 3, 0, 5)
    Sleep(100)
    BeginChrThread(0x1A0, 3, 0, 6)
    WaitChrThread(0x158, 3)
    WaitChrThread(0x1A0, 3)

    #C0029
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#30W………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#35W………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(19500, 500)
    SetChrChipByIndex(0x9, 0x29)
    SetChrSubChip(0x9, 0x0)

    def lambda_14BB():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_14BB)
    SetChrChipByIndex(0xA, 0x29)
    SetChrSubChip(0xA, 0x0)

    def lambda_14DD():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14DD)
    SetChrChipByIndex(0xB, 0x2B)
    SetChrSubChip(0xB, 0x0)

    def lambda_14FF():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14FF)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)

    def lambda_1521():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1521)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x0)

    def lambda_1543():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1543)
    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 0, 0, 1)

    def lambda_156B():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_156B)
    SetChrChipByIndex(0x18, 0x2F)
    SetChrSubChip(0x18, 0x0)
    BeginChrThread(0x18, 0, 0, 1)

    def lambda_1593():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1593)
    Sleep(500)
    OP_24(0x37B)
    Battle("BattleInfo_570", 0x30200011, 0x0, 0x0, 0x17, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0xE, 0xFF)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0x18, 0xFF)
    Call(0, 11)
    Return()

    # Function_4_729 end

    def Function_5_15E8(): pass

    label("Function_5_15E8")

    OP_93(0x158, 0x10E, 0x1F4)

    def lambda_15F4():
        OP_95(0xFE, 38900, 0, -2000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x158, 1, lambda_15F4)
    WaitChrThread(0x158, 1)
    Return()

    # Function_5_15E8 end

    def Function_6_160E(): pass

    label("Function_6_160E")

    OP_93(0x1A0, 0xE1, 0x1F4)

    def lambda_161A():
        OP_95(0xFE, 43900, 0, -2000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A0, 1, lambda_161A)
    WaitChrThread(0x1A0, 1)

    def lambda_1638():
        OP_95(0xFE, 38900, 0, -2000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A0, 1, lambda_1638)
    WaitChrThread(0x1A0, 1)
    Return()

    # Function_6_160E end

    def Function_7_1652(): pass

    label("Function_7_1652")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    def lambda_165F():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_165F)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_7_1652 end

    def Function_8_1681(): pass

    label("Function_8_1681")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    def lambda_168E():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_168E)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_1681 end

    def Function_9_16B0(): pass

    label("Function_9_16B0")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)

    def lambda_16BD():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16BD)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_9_16B0 end

    def Function_10_16DF(): pass

    label("Function_10_16DF")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_16F2():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16F2)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x24, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_16DF end

    def Function_11_1732(): pass

    label("Function_11_1732")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    RemoveParty(0x9F, 0x0)
    AddParty(0x52, 0xFF, 0xFF)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_32(0x0, 0x5, 0xC8)
    OP_32(0x1, 0x5, 0xC8)
    OP_32(0x2, 0x5, 0xC8)
    OP_32(0x3, 0x5, 0xC8)
    LoadChrToIndex("chr/ch02750.itc", 0x14)
    LoadChrToIndex("chr/ch02751.itc", 0x15)
    LoadChrToIndex("chr/ch00050.itc", 0x16)
    LoadChrToIndex("chr/ch00051.itc", 0x17)
    LoadChrToIndex("chr/ch00150.itc", 0x18)
    LoadChrToIndex("chr/ch00151.itc", 0x19)
    LoadChrToIndex("chr/ch00250.itc", 0x1A)
    LoadChrToIndex("chr/ch00251.itc", 0x1B)
    LoadChrToIndex("chr/ch00350.itc", 0x1C)
    LoadChrToIndex("chr/ch00351.itc", 0x1D)
    LoadChrToIndex("chr/ch31050.itc", 0x1E)
    LoadChrToIndex("chr/ch31051.itc", 0x1F)
    LoadChrToIndex("chr/ch31053.itc", 0x20)
    LoadChrToIndex("chr/ch31150.itc", 0x21)
    LoadChrToIndex("chr/ch31151.itc", 0x22)
    LoadChrToIndex("chr/ch31153.itc", 0x23)
    LoadChrToIndex("chr/ch31950.itc", 0x24)
    LoadChrToIndex("chr/ch31951.itc", 0x25)
    LoadChrToIndex("chr/ch31953.itc", 0x26)
    LoadChrToIndex("chr/ch31250.itc", 0x27)
    LoadChrToIndex("chr/ch31251.itc", 0x28)
    LoadChrToIndex("chr/ch31350.itc", 0x29)
    LoadChrToIndex("chr/ch31351.itc", 0x2A)
    LoadChrToIndex("chr/ch02752.itc", 0x2B)
    LoadChrToIndex("chr/ch31052.itc", 0x2C)
    LoadChrToIndex("chr/ch31952.itc", 0x2D)
    LoadChrToIndex("chr/ch31252.itc", 0x2E)
    LoadChrToIndex("apl/ch50363.itc", 0x2F)
    LoadChrToIndex("chr/ch02702.itc", 0x30)
    LoadChrToIndex("chr/ch05500.itc", 0x31)
    LoadChrToIndex("chr/ch00000.itc", 0x32)
    LoadChrToIndex("chr/ch00300.itc", 0x33)
    LoadChrToIndex("chr/ch00152.itc", 0x34)
    LoadChrToIndex("chr/ch00254.itc", 0x35)
    LoadChrToIndex("chr/ch31353.itc", 0x36)
    SoundLoad(460)
    SoundLoad(468)
    OP_68(44500, 900, 0, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrChipByIndex(0x101, 0x16)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 43600, 0, 0, 90)
    SetChrChipByIndex(0x102, 0x18)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 42500, 0, 1000, 90)
    SetChrChipByIndex(0x103, 0x1A)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 41100, 0, 0, 90)
    SetChrChipByIndex(0x104, 0x1C)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 41900, 0, -1000, 90)
    SetChrPos(0x153, 39200, 0, 100, 90)
    SetChrPos(0x158, 39200, 0, -900, 90)
    SetChrChipByIndex(0x8, 0x14)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, 43300, 0, 2600, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x23, 0x31)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x23, 37000, 150, -100, 315)
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x2F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x2F)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x2F)
    SetChrSubChip(0xD, 0x2)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x2F)
    SetChrSubChip(0xE, 0x2)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0x9, 46500, 0, -1900, 270)
    SetChrPos(0xA, 47200, 0, 1000, 315)
    SetChrPos(0xB, 48800, 0, -300, 180)
    SetChrPos(0xD, 50700, 0, -1700, 180)
    SetChrPos(0xE, 50500, 0, 1300, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 0x28)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x28)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x2A)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x2A)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x2A)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x19, 1300, 0, 0, 90)
    SetChrPos(0x1A, 0, 0, 1200, 90)
    SetChrPos(0x1B, 0, 0, -1200, 90)
    SetChrPos(0x1C, 5300, 0, 0, 90)
    SetChrPos(0x1D, 4000, 0, 1200, 90)
    SetChrPos(0x1E, 4000, 0, -1200, 90)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x13, 111100, 500, -2400, 180)
    SetChrPos(0x14, 111100, 500, -2400, 180)
    SetChrPos(0x15, 111100, 500, -2400, 180)
    SetChrPos(0x16, 111100, 500, -2400, 180)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xF, 113100, 500, 2400, 180)
    SetChrPos(0x10, 113100, 500, 2400, 180)
    SetChrPos(0x11, 113100, 500, 2400, 180)
    SetChrPos(0x12, 113100, 500, 2400, 180)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_78(0x5, 0x1F)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x5, 0x4)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1F, 0x4)
    OP_49()
    SetChrPos(0x1F, 141500, 0, -2400, 0)
    OP_D3(0x1F, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB5, 0xF0, 0x0, 0x20)
    OP_78(0x6, 0x20)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFlags(0x6, 0x4)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x20, 0x4)
    OP_49()
    SetChrPos(0x20, 143500, 0, 2400, 0)
    OP_D3(0x20, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0xB5, 0xF0, 0x0, 0x20)
    OP_78(0x7, 0x21)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFlags(0x7, 0x4)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x21, 0x4)
    OP_49()
    SetChrPos(0x21, 153000, 0, 0, 0)
    OP_D3(0x21, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0xB5, 0xF0, 0x0, 0x20)
    SetMapObjFrame(0x7, "bul00", 0x0, 0x1)
    SetMapObjFrame(0x7, "bul01", 0x0, 0x1)
    LoadEffect(0x0, "battle\\ms00001.eff")
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "battle\\mg040_00.eff")
    LoadEffect(0x4, "battle\\btgun00.eff")
    LoadEffect(0x5, "event\\eva03_01.eff")
    LoadEffect(0x6, "event\\eva04_00.eff")
    SetCameraDistance(20500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0031
    ChrTalk(
        0x104,
        (
            "#6P#0302Fよっしゃ……\x01",
            "何とか切り抜けたか！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#0000F#5Pみんな、このまま街道に──\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(485, 0, 100, 0)
    Fade(500)
    OP_68(127500, 1000, 0, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_EE(0x0, 0x1)
    OP_68(112500, 1000, 0, 4000)
    MoveCamera(55, 20, 0, 4000)
    SetCameraDistance(20000, 4000)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)

    def lambda_1F80():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1F80)
    Sleep(50)

    def lambda_1F9D():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1F9D)
    WaitChrThread(0x1F, 1)
    Sound(495, 0, 100, 0)
    SetMapObjFlags(0x5, 0x20)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x20, 1)
    OP_24(0x1E5)
    SetMapObjFlags(0x6, 0x20)
    OP_71(0x6, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x6)
    OP_71(0x6, 0x1, 0x1E, 0x0, 0x0)
    OP_79(0x5)
    OP_79(0x6)
    OP_6F(0x79)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    BeginChrThread(0xF, 3, 0, 38)
    BeginChrThread(0x13, 3, 0, 39)
    Sleep(400)
    BeginChrThread(0x10, 3, 0, 38)
    BeginChrThread(0x14, 3, 0, 39)
    Sleep(400)
    BeginChrThread(0x11, 3, 0, 38)
    BeginChrThread(0x15, 3, 0, 39)
    Sleep(400)
    BeginChrThread(0x12, 3, 0, 38)
    BeginChrThread(0x16, 3, 0, 39)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x13, 3)
    Fade(500)
    OP_68(44500, 900, 0, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_EE(0x0, 0xA)
    OP_0D()

    #C0033
    ChrTalk(
        0x101,
        "#0007F#6P……な………\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        (
            "#6P#0310Fチッ……\x01",
            "さすがにアレは無理だな。\x02\x03",

            "#0307F仕方ねぇ、一度街に戻って\x01",
            "旧市街あたりにでも……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x10E, 0x1F4)

    #C0035
    ChrTalk(
        0x103,
        "#0201F#11Pあ……\x02",
    )

    CloseMessageWindow()

    def lambda_219B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_219B)
    Sleep(50)

    def lambda_21AB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_21AB)
    Sleep(50)

    def lambda_21BB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_21BB)
    Sleep(50)

    def lambda_21CB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_21CB)

    def lambda_21D8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x158, 2, lambda_21D8)
    WaitChrThread(0x153, 2)
    OP_68(14500, 900, 0, 3000)
    MoveCamera(45, 20, 0, 3000)
    SetCameraDistance(18500, 3000)
    OP_6F(0x79)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)

    def lambda_224C():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_224C)

    def lambda_2266():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2266)

    def lambda_2280():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_2280)

    def lambda_229A():
        OP_98(0xFE, 0x88B8, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_229A)

    def lambda_22B4():
        OP_98(0xFE, 0x88B8, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_22B4)

    def lambda_22CE():
        OP_98(0xFE, 0x88B8, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_22CE)
    Sleep(1500)

    #C0036
    ChrTalk(
        0x101,
        "#0010Fくっ……！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#0108Fそ、そんな……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#0310F絶体絶命ってやつか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(31300, 900, 3200, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 32800, 0, 2400, 135)
    SetChrPos(0x102, 34500, 0, 4700, 90)
    SetChrPos(0x103, 29100, 0, 4700, 270)
    SetChrPos(0x104, 29800, 0, 2400, 225)
    SetChrPos(0x153, 32299, 0, 4800, 180)
    SetChrPos(0x158, 31300, 0, 4800, 180)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x3)
    SetChrPos(0x8, 31800, 1000, 6000, 270)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x1B, 0x1)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x19, 20500, 0, 4600, 90)
    SetChrPos(0x1A, 19900, 0, 2000, 90)
    SetChrPos(0x1C, 23200, 0, -3600, 45)
    SetChrPos(0x1D, 29100, 0, -5400, 0)
    BeginChrThread(0x19, 3, 0, 34)
    BeginChrThread(0x1A, 3, 0, 35)
    BeginChrThread(0x1C, 3, 0, 36)
    BeginChrThread(0x1D, 3, 0, 37)
    SetChrPos(0xF, 43100, 0, 4600, 270)
    SetChrPos(0x10, 43700, 0, 2000, 270)
    SetChrPos(0x13, 40400, 0, -3600, 315)
    SetChrPos(0x14, 34500, 0, -5400, 0)
    BeginChrThread(0xF, 3, 0, 30)
    BeginChrThread(0x10, 3, 0, 31)
    BeginChrThread(0x13, 3, 0, 32)
    BeginChrThread(0x14, 3, 0, 33)
    MoveCamera(45, 19, 0, 2000)
    SetCameraDistance(20500, 2000)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x19, 3)
    WaitChrThread(0x1A, 3)
    WaitChrThread(0x1C, 3)
    WaitChrThread(0x1D, 3)
    OP_6F(0x79)

    #C0039
    ChrTalk(
        0x153,
        "#5P#1101Fむむっ……！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x158,
        "#5P#6008F……お、お父さん……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0008F#5P（くっ……\x01",
            "  何とかこの子たちだけでも……！）\x02",
        )
    )

    CloseMessageWindow()
    Sound(490, 0, 80, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x158, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(460, 2, 100, 0)
    Sound(468, 2, 100, 0)

    def lambda_2610():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2610)
    Sleep(50)

    def lambda_2620():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2620)
    Sleep(50)

    def lambda_2630():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2630)
    Sleep(50)

    def lambda_2640():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_2640)

    def lambda_264D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x158, 2, lambda_264D)
    WaitChrThread(0x153, 2)

    #C0042
    ChrTalk(
        0x101,
        "#0005F#6Pあれは……！？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#0205F#6P車がもう一台……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(491, 0, 100, 0)
    Fade(500)
    OP_68(143000, 900, 10, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13000, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    ClearMapObjFlags(0x7, 0x4)
    SetChrPos(0x1F, 105500, 0, -2900, 0)
    SetChrPos(0x20, 113500, 0, 2900, 0)
    OP_68(133000, 900, 0, 2000)
    MoveCamera(45, 20, 0, 2000)
    SetCameraDistance(17000, 2000)
    BeginChrThread(0x101, 3, 0, 29)
    PlayEffect(0x5, 0x0, 0x21, 0x40, 0, 0, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x21, 0x40, 0, 0, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x2, 0x21, 0x40, 0, 0, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_282C():
        OP_96(0xFE, 0x20788, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_282C)
    WaitChrThread(0x21, 1)
    OP_9F(0x0, 0x21)
    Sound(494, 0, 100, 0)
    OP_9F(0x1, 123900, 0, 0)
    OP_9F(0x1, 114300, 0, -1000)
    OP_9F(0x1, 105900, 0, 1000)
    OP_9F(0x2, 0x21, 11000, 0x6)
    OP_9F(0x0, 0x21)
    OP_9F(0x1, 91600, 0, 3500)
    OP_9F(0x1, 80300, 0, 0)
    OP_9F(0x2, 0x21, 11000, 0x6)
    Sound(493, 0, 100, 0)
    OP_24(0x1CC)
    OP_24(0x1D4)
    Fade(500)
    OP_68(47000, 900, -500, 0)
    MoveCamera(70, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 32500, 0, 2400, 135)
    SetChrPos(0x102, 33900, 0, 4700, 180)
    SetChrPos(0x103, 29700, 0, 4700, 135)
    SetChrPos(0x104, 30100, 0, 2400, 135)
    SetChrPos(0x153, 32299, 0, 4800, 135)
    SetChrPos(0x158, 31300, 0, 4800, 135)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 31800, 1000, 6000, 135)

    def lambda_296E():

        label("loc_296E")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_296E")

    QueueWorkItem2(0xF, 2, lambda_296E)

    def lambda_2980():

        label("loc_2980")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_2980")

    QueueWorkItem2(0x10, 2, lambda_2980)

    def lambda_2992():

        label("loc_2992")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_2992")

    QueueWorkItem2(0x13, 2, lambda_2992)

    def lambda_29A4():

        label("loc_29A4")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_29A4")

    QueueWorkItem2(0x14, 2, lambda_29A4)
    BeginChrThread(0x10, 3, 0, 26)
    BeginChrThread(0x13, 3, 0, 28)
    BeginChrThread(0x14, 3, 0, 27)
    OP_68(38000, 900, -500, 3000)
    SetCameraDistance(18000, 3000)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    SetChrPos(0x21, 61000, 0, 500, 0)
    OP_D3(0x21, 0x0, 0x41EB0, 0x0, 0x0)
    PlayEffect(0x5, 0x0, 0x21, 0x40, 0, 0, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x21, 0x40, 0, 0, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x2, 0x21, 0x40, 0, 0, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2AB4():
        OP_96(0xFE, 0xA028, 0x0, 0x1F4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2AB4)
    WaitChrThread(0x21, 1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    Sound(495, 0, 100, 0)
    OP_82(0x12C, 0x0, 0xBB8, 0x258)

    def lambda_2AF2():
        OP_9E(0xFE, 0xA028, 0xFFFFE69C, 0xFFFF8AD0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2AF2)

    def lambda_2B0D():
        OP_D3(0xFE, 0x0, 0x35B60, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_2B0D)
    BeginChrThread(0x21, 3, 0, 12)
    Sleep(300)
    SetMapObjFlags(0x7, 0x20)
    OP_71(0x7, 0x5B, 0x78, 0x0, 0x0)
    OP_24(0x1ED)
    WaitChrThread(0x21, 1)
    OP_79(0x7)
    OP_6F(0x79)
    EndChrThread(0xF, 0x2)
    EndChrThread(0x10, 0x2)
    EndChrThread(0x14, 0x2)

    def lambda_2B59():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_2B59)

    def lambda_2B66():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2B66)

    def lambda_2B73():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_2B73)

    def lambda_2B80():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_2B80)
    OP_68(35000, 900, 2000, 1500)
    SetCameraDistance(19000, 1500)
    OP_6F(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x3)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2BF0")

    #C0044
    ChrTalk(
        0x101,
        (
            "#0005F#6Pこのリムジンは……\x01",
            "ディーター総裁の！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C1B")

    label("loc_2BF0")


    #C0045
    ChrTalk(
        0x102,
        "#0105F#5Pこ、この赤いリムジンは……！\x02",
    )

    CloseMessageWindow()

    label("loc_2C1B")

    OP_71(0x7, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0x7)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)

    def lambda_2C3F():
        OP_96(0xFE, 0x8F5C, 0x96, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_2C3F)

    def lambda_2C59():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_2C59)
    WaitChrThread(0x23, 1)

    #C0046
    ChrTalk(
        0x23,
        (
            "#2901F#11Pさあ！\x01",
            "早くお乗りなさい！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#0102F#5Pベル……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#6P#0011Fマリアベルさん！？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x22, 35900, 0, -1200, 315)
    SetChrFlags(0x22, 0x8)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    #C0049
    ChrTalk(
        0x22,
        (
            "#2801F話は後だ！\x01",
            "とにかく乗りたまえ！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#6P#0002Fは、はい！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x32)
    SetChrSubChip(0x101, 0x0)
    TurnDirection(0x101, 0x153, 500)

    #C0051
    ChrTalk(
        0x101,
        "#11P#0000Fキーア、乗り込むぞ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)

    #C0052
    ChrTalk(
        0x153,
        "#1102F#5Pうんっ！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 24)
    SetChrChipByIndex(0x104, 0x33)
    SetChrSubChip(0x104, 0x0)
    TurnDirection(0x104, 0x158, 500)

    #C0053
    ChrTalk(
        0x104,
        "#11P#0300Fシズクちゃん、掴まれ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x158, 0x104, 500)

    #C0054
    ChrTalk(
        0x158,
        "#6000F#5Pは、はいっ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x158, 3, 0, 25)
    OP_68(29000, 900, 500, 6000)
    MoveCamera(55, 17, 0, 6000)
    SetCameraDistance(21000, 6000)
    BeginChrThread(0x102, 3, 0, 18)
    BeginChrThread(0x103, 3, 0, 19)
    BeginChrThread(0x8, 3, 0, 17)

    def lambda_2E20():
        OP_96(0xFE, 0x9088, 0x96, 0xFFFFFF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_2E20)

    def lambda_2E3A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_2E3A)
    WaitChrThread(0x153, 3)
    BeginChrThread(0x101, 3, 0, 15)
    WaitChrThread(0x158, 3)
    BeginChrThread(0x104, 3, 0, 16)
    WaitChrThread(0x101, 3)
    Sound(470, 0, 100, 0)
    OP_71(0x7, 0x169, 0x186, 0x0, 0x0)
    WaitChrThread(0x104, 3)
    OP_93(0x21, 0xDC, 0x0)
    OP_71(0x7, 0x1E0, 0x1A5, 0x0, 0x20)

    def lambda_2E8C():
        OP_9B(0x1, 0xFE, 0xB4, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2E8C)
    WaitChrThread(0x21, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sleep(300)

    def lambda_2EB9():

        label("loc_2EB9")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_2EB9")

    QueueWorkItem2(0x1C, 2, lambda_2EB9)
    Sound(490, 0, 100, 0)
    Sound(495, 0, 100, 0)
    OP_71(0x7, 0x1E1, 0x21C, 0x0, 0x20)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    def lambda_2EF4():
        OP_9E(0xFE, 0x7C38, 0x206C, 0xC350, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2EF4)
    Sleep(800)
    BeginChrThread(0x1C, 3, 0, 14)
    WaitChrThread(0x21, 1)

    def lambda_2F1C():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2F1C)
    OP_6F(0x79)
    Fade(250)
    OP_68(15000, 900, 0, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    EndChrThread(0x19, 0x2)

    def lambda_2F6F():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2F6F)
    BeginChrThread(0x19, 3, 0, 13)
    BeginChrThread(0x24, 2, 0, 42)
    EndChrThread(0x1A, 0x2)

    def lambda_2F8C():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2F8C)
    BeginChrThread(0x1A, 3, 0, 13)
    OP_68(5000, 900, 0, 4000)
    SetCameraDistance(21000, 4000)
    Sleep(1000)
    SetChrChipByIndex(0x1C, 0x2A)
    SetChrSubChip(0x1C, 0x0)

    def lambda_2FC4():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2FC4)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x21, 0xFF)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x1A, 0xFF)
    EndChrThread(0x1C, 0xFF)
    EndChrThread(0x24, 0x2)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    SetChrChipPat(0x0, 0x1, 0x0)
    SetChrChipPat(0x3, 0x1, 0x3)
    LoadChrChipPat()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1CC)
    OP_24(0x1D4)
    SetScenarioFlags(0x5C, 0)
    NewScene("e0111", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1732 end

    def Function_12_3044(): pass

    label("Function_12_3044")

    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 43300, 0, 500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 42000, 0, 1000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 40500, 0, 1500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 39000, 0, 2000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 37500, 0, 2300, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_12_3044 end

    def Function_13_3164(): pass

    label("Function_13_3164")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)

    label("loc_316F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32C5")

    def lambda_317F():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_317F)
    SetChrSubChip(0xFE, 0x3)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(700)
    Jump("loc_316F")

    label("loc_32C5")

    Return()

    # Function_13_3164 end

    def Function_14_32C6(): pass

    label("Function_14_32C6")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1C, 0x2A)
    SetChrSubChip(0x1C, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_32E4():
        OP_9D(0xFE, 0x61A8, 0x0, 0x320, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_32E4)
    WaitChrThread(0x1C, 1)
    SetChrChipByIndex(0x1C, 0x29)
    SetChrSubChip(0x1C, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_32C6 end

    def Function_15_3314(): pass

    label("Function_15_3314")

    OP_92(0x101, 0x8B10, 0x320, 0x1F4)

    def lambda_3326():
        OP_95(0xFE, 35600, 0, 800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3326)
    WaitChrThread(0x101, 1)
    SetChrFlags(0x101, 0x4)

    def lambda_3349():
        OP_95(0xFE, 37000, 150, -100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3349)

    def lambda_3363():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3363)
    WaitChrThread(0x101, 1)
    Return()

    # Function_15_3314 end

    def Function_16_3374(): pass

    label("Function_16_3374")

    OP_92(0x104, 0x8B10, 0x320, 0x1F4)

    def lambda_3386():
        OP_95(0xFE, 35600, 0, 800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3386)
    WaitChrThread(0x104, 1)
    SetChrFlags(0x104, 0x4)

    def lambda_33A9():
        OP_95(0xFE, 37000, 150, -100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_33A9)

    def lambda_33C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_33C3)
    WaitChrThread(0x104, 1)
    Return()

    # Function_16_3374 end

    def Function_17_33D4(): pass

    label("Function_17_33D4")

    Sleep(1000)
    SetChrChipByIndex(0x8, 0x15)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_33FA():
        OP_92(0xFE, 0x6BD0, 0x1A2C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_33FA)
    SetChrChip(0x0, 0x8, 0x1E, 0xC8)
    Sound(854, 0, 100, 0)

    def lambda_341B():
        OP_9D(0xFE, 0x6BD0, 0x3E8, 0x1A2C, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_341B)
    Sleep(350)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    WaitChrThread(0x8, 1)
    PlayEffect(0x6, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3481():
        OP_92(0xFE, 0x55F0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3481)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x0)

    def lambda_349C():

        label("loc_349C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_349C")

    QueueWorkItem2(0x19, 2, lambda_349C)

    def lambda_34AE():

        label("loc_34AE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_34AE")

    QueueWorkItem2(0x1A, 2, lambda_34AE)
    Sleep(3500)
    SetChrChipByIndex(0x8, 0x15)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_34D8():
        OP_9D(0xFE, 0x55F0, 0x0, 0x708, 0x6A4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_34D8)
    Sleep(550)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    WaitChrThread(0x8, 1)
    PlayEffect(0x6, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_353E():
        OP_92(0xFE, 0x4268, 0xFFFFF704, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_353E)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_3562():
        OP_9D(0xFE, 0x4268, 0x76C, 0xFFFFF704, 0xA28, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3562)
    Sleep(400)
    WaitChrThread(0x8, 1)
    Sound(925, 0, 100, 0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0x8, 0x0, 0x0)

    def lambda_35AA():
        OP_98(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_35AA)
    SetChrChipByIndex(0x8, 0x14)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_35F8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_35F8)
    WaitChrThread(0x8, 2)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x3)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_33D4 end

    def Function_18_3623(): pass

    label("Function_18_3623")

    OP_93(0x102, 0x6E, 0x1F4)
    SetChrChipByIndex(0x102, 0x34)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(600)
    BeginChrThread(0xF, 3, 0, 20)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1100, 1000, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(600)
    BeginChrThread(0x10, 3, 0, 20)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1100, 1000, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x18)
    SetChrSubChip(0x102, 0x0)
    Sleep(400)

    def lambda_3733():
        OP_95(0xFE, 37800, 0, 3200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3733)
    WaitChrThread(0x102, 1)
    SetChrFlags(0x102, 0x4)

    def lambda_3756():
        OP_95(0xFE, 39000, 150, 2200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3756)

    def lambda_3770():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3770)
    WaitChrThread(0x102, 1)
    Return()

    # Function_18_3623 end

    def Function_19_3781(): pass

    label("Function_19_3781")

    OP_93(0x103, 0xB4, 0x1F4)
    SetChrChipByIndex(0x103, 0x35)
    SetChrSubChip(0x103, 0x0)
    PlayEffect(0x1, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(831, 0, 100, 0)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    PlayEffect(0x2, 0x1, 0x103, 0x140, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(280, 0, 80, 0)
    SetChrSubChip(0x103, 0x3)
    PlayEffect(0x3, 0xFF, 0xFF, 0x140, 39600, 0, -4200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x13, 3, 0, 21)
    PlayEffect(0x3, 0xFF, 0xFF, 0x140, 31400, 0, -4700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x14, 3, 0, 22)
    PlayEffect(0x3, 0xFF, 0xFF, 0x140, 29100, 0, -2400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x1D, 3, 0, 23)
    SetChrSubChip(0x103, 0x4)
    Sleep(1200)
    SetChrChipByIndex(0x103, 0x1A)
    SetChrSubChip(0x103, 0x0)

    def lambda_3906():
        OP_95(0xFE, 32200, 0, 400, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3906)
    WaitChrThread(0x103, 1)
    SetChrFlags(0x103, 0x4)

    def lambda_3929():
        OP_95(0xFE, 31200, 150, -1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3929)

    def lambda_3943():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3943)
    WaitChrThread(0x103, 1)
    Return()

    # Function_19_3781 end

    def Function_20_3954(): pass

    label("Function_20_3954")

    OP_93(0xFE, 0x10E, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_39AA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39AA)

    def lambda_39C3():
        OP_9C(0xFE, 0xFA0, 0x0, 0x190, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39C3)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_20_3954 end

    def Function_21_39F9(): pass

    label("Function_21_39F9")

    Sleep(1100)
    OP_93(0xFE, 0x13B, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3A1B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A1B)

    def lambda_3A34():
        OP_9D(0xFE, 0xA0F0, 0x0, 0xFFFFEA20, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A34)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_21_39F9 end

    def Function_22_3A6A(): pass

    label("Function_22_3A6A")

    Sleep(1100)
    OP_93(0xFE, 0x0, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3A8C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A8C)

    def lambda_3AA5():
        OP_9D(0xFE, 0x7AA8, 0x0, 0xFFFFEB4C, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AA5)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_22_3A6A end

    def Function_23_3ADB(): pass

    label("Function_23_3ADB")

    Sleep(1100)
    OP_93(0xFE, 0x2D, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3AFD():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3AFD)

    def lambda_3B16():
        OP_9D(0xFE, 0x6C34, 0x0, 0xFFFFEE08, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B16)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_23_3ADB end

    def Function_24_3B46(): pass

    label("Function_24_3B46")


    def lambda_3B4B():
        OP_99(0xFE, 0x101, 0x320, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3B4B)
    WaitChrThread(0x153, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x153, 0x80)
    SetChrBattleFlags(0x153, 0x8000)
    OP_0D()
    Return()

    # Function_24_3B46 end

    def Function_25_3B7D(): pass

    label("Function_25_3B7D")


    def lambda_3B82():
        OP_99(0xFE, 0x104, 0x320, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x158, 1, lambda_3B82)
    WaitChrThread(0x158, 1)
    Fade(250)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x158, 0x80)
    SetChrBattleFlags(0x158, 0x8000)
    OP_0D()
    Return()

    # Function_25_3B7D end

    def Function_26_3BB4(): pass

    label("Function_26_3BB4")

    Sleep(1300)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_3BD5():
        OP_9D(0xFE, 0xA5A0, 0x0, 0xFA0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3BD5)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_26_3BB4 end

    def Function_27_3C05(): pass

    label("Function_27_3C05")

    Sleep(1800)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x1)

    def lambda_3C20():
        OP_9D(0xFE, 0x7AA8, 0x0, 0xFFFFEDA4, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3C20)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_27_3C05 end

    def Function_28_3C50(): pass

    label("Function_28_3C50")

    Sleep(1600)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_3C71():
        OP_9D(0xFE, 0x9AB0, 0x0, 0xFFFFEF98, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3C71)
    WaitChrThread(0x13, 1)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_28_3C50 end

    def Function_29_3CA1(): pass

    label("Function_29_3CA1")

    OP_6F(0x79)
    Fade(250)
    OP_68(117700, 900, 0, 0)
    MoveCamera(65, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_68(102000, 900, -400, 4000)
    MoveCamera(35, 27, 0, 4000)
    SetCameraDistance(18000, 4000)
    OP_6F(0x79)
    Return()

    # Function_29_3CA1 end

    def Function_30_3CFE(): pass

    label("Function_30_3CFE")


    def lambda_3D03():
        OP_95(0xFE, 39100, 0, 4600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D03)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    Return()

    # Function_30_3CFE end

    def Function_31_3D25(): pass

    label("Function_31_3D25")


    def lambda_3D2A():
        OP_95(0xFE, 39700, 0, 2000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D2A)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_31_3D25 end

    def Function_32_3D4C(): pass

    label("Function_32_3D4C")


    def lambda_3D51():
        OP_95(0xFE, 37900, 0, -1100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D51)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    Return()

    # Function_32_3D4C end

    def Function_33_3D73(): pass

    label("Function_33_3D73")


    def lambda_3D78():
        OP_95(0xFE, 34500, 0, -2400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D78)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    Return()

    # Function_33_3D73 end

    def Function_34_3D9A(): pass

    label("Function_34_3D9A")


    def lambda_3D9F():
        OP_95(0xFE, 24500, 0, 4600, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D9F)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x19, 0x27)
    SetChrSubChip(0x19, 0x0)
    Return()

    # Function_34_3D9A end

    def Function_35_3DC1(): pass

    label("Function_35_3DC1")


    def lambda_3DC6():
        OP_95(0xFE, 23900, 0, 2000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DC6)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x1A, 0x27)
    SetChrSubChip(0x1A, 0x0)
    Return()

    # Function_35_3DC1 end

    def Function_36_3DE8(): pass

    label("Function_36_3DE8")


    def lambda_3DED():
        OP_95(0xFE, 25700, 0, -1100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DED)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x1C, 0x29)
    SetChrSubChip(0x1C, 0x0)
    Return()

    # Function_36_3DE8 end

    def Function_37_3E0F(): pass

    label("Function_37_3E0F")


    def lambda_3E14():
        OP_95(0xFE, 29100, 0, -2400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E14)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x1D, 0x29)
    SetChrSubChip(0x1D, 0x0)
    Return()

    # Function_37_3E0F end

    def Function_38_3E36(): pass

    label("Function_38_3E36")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3E43():
        OP_95(0xFE, 113100, 0, 400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E43)

    def lambda_3E5D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E5D)
    WaitChrThread(0xFE, 1)

    def lambda_3E72():
        OP_95(0xFE, 100100, 0, 400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E72)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_3E36 end

    def Function_39_3E8C(): pass

    label("Function_39_3E8C")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3E99():
        OP_95(0xFE, 111100, 0, -4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E99)

    def lambda_3EB3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3EB3)
    WaitChrThread(0xFE, 1)

    def lambda_3EC8():
        OP_95(0xFE, 100100, 0, -4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EC8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_39_3E8C end

    def Function_40_3EE2(): pass

    label("Function_40_3EE2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EFB")
    Sound(832, 0, 100, 0)
    Sleep(500)
    Jump("Function_40_3EE2")

    label("loc_3EFB")

    Return()

    # Function_40_3EE2 end

    def Function_41_3EFC(): pass

    label("Function_41_3EFC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F15")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_41_3EFC")

    label("loc_3F15")

    Return()

    # Function_41_3EFC end

    def Function_42_3F16(): pass

    label("Function_42_3F16")

    Sleep(500)

    label("loc_3F19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F32")
    Sound(957, 0, 100, 0)
    Sleep(1200)
    Jump("loc_3F19")

    label("loc_3F32")

    Return()

    # Function_42_3F16 end

    def Function_43_3F33(): pass

    label("Function_43_3F33")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31050.itc", 0x1E)
    LoadChrToIndex("chr/ch31051.itc", 0x1F)
    LoadChrToIndex("chr/ch31053.itc", 0x20)
    LoadChrToIndex("chr/ch31150.itc", 0x21)
    LoadChrToIndex("chr/ch31151.itc", 0x22)
    LoadChrToIndex("chr/ch31153.itc", 0x23)
    LoadChrToIndex("chr/ch31950.itc", 0x24)
    LoadChrToIndex("chr/ch31951.itc", 0x25)
    LoadChrToIndex("chr/ch31953.itc", 0x26)
    LoadChrToIndex("chr/ch31152.itc", 0x27)
    LoadChrToIndex("chr/ch31952.itc", 0x28)
    LoadEffect(0x0, "battle\\btgun00.eff")
    LoadEffect(0x1, "event\\eva03_01.eff")
    LoadEffect(0x2, "event\\eva04_00.eff")
    LoadEffect(0x3, "event\\ev606_00.eff")
    LoadEffect(0x4, "event\\eva01_00.eff")
    OP_68(71000, 500, 0, 0)
    MoveCamera(55, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(27500, 0)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0xC, 53500, 0, 2900, 180)
    SetChrPos(0x16, 53500, 0, 1300, 0)
    SetChrPos(0xF, 66500, 0, -900, 90)
    SetChrPos(0x10, 66500, 0, -2100, 90)
    SetChrPos(0x11, 65400, 0, -900, 90)
    SetChrPos(0x12, 65400, 0, -2100, 90)
    SetChrPos(0x13, 68600, 0, -1500, 270)
    SetChrPos(0xD, 78000, 0, 900, 90)
    SetChrPos(0xE, 78000, 0, -900, 90)
    SetChrPos(0x14, 58000, 0, 3000, 180)
    SetChrPos(0x15, 58000, 0, 4500, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    OP_78(0x5, 0x1F)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1F, 0x4)
    OP_49()
    SetChrPos(0x1F, 56000, 0, 2400, 0)
    OP_D3(0x1F, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x0)
    OP_78(0x6, 0x20)
    SetMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x6, 0x4)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x20, 0x4)
    OP_49()
    SetChrPos(0x20, 71000, 0, -2400, 0)
    OP_D3(0x20, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x6, 0x1E)
    OP_70(0x6, 0x0)
    OP_78(0x7, 0x21)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x7, "bul00", 0x0, 0x1)
    SetMapObjFrame(0x7, "bul01", 0x0, 0x1)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x21, 0x4)
    OP_49()
    SetChrPos(0x21, -10000, 0, 0, 0)
    OP_D3(0x21, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0xB5, 0xF0, 0x0, 0x20)
    OP_E5()
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K同日、２３：３０──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7527", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(59000, 500, 0, 7000)
    SetCameraDistance(30500, 7000)
    FadeToBright(2000, 0)
    Sleep(4000)
    BeginChrThread(0x14, 3, 0, 56)
    BeginChrThread(0x15, 3, 0, 56)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x14, 20000, 0, 900, 270)
    SetChrPos(0x15, 20000, 0, -900, 270)
    Sound(490, 0, 100, 0)
    Sleep(3500)
    OP_68(9500, 500, 0, 0)
    MoveCamera(63, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    PlayEffect(0x1, 0x0, 0x21, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x21, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x21, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x21, 3, 0, 57)
    BeginChrThread(0x101, 3, 0, 58)
    OP_68(17500, 500, 0, 3500)
    SetCameraDistance(21000, 3500)
    Sound(493, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    CancelBlur(2000)
    BeginChrThread(0x14, 3, 0, 44)
    BeginChrThread(0x15, 3, 0, 47)
    BeginChrThread(0x24, 1, 0, 61)
    OP_6F(0x79)
    Fade(250)
    OP_68(48500, 500, 0, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    EndChrThread(0x14, 0xFF)
    EndChrThread(0x15, 0xFF)

    def lambda_4530():

        label("loc_4530")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_4530")

    QueueWorkItem2(0xC, 2, lambda_4530)

    def lambda_4542():

        label("loc_4542")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_4542")

    QueueWorkItem2(0x16, 2, lambda_4542)
    BeginChrThread(0xC, 0, 0, 55)
    BeginChrThread(0x16, 0, 0, 53)
    OP_68(63500, 500, 0, 2500)
    MoveCamera(47, 15, 0, 2500)
    SetCameraDistance(21000, 2500)
    Sound(491, 0, 100, 0)

    def lambda_458B():

        label("loc_458B")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_458B")

    QueueWorkItem2(0x13, 2, lambda_458B)
    BeginChrThread(0x13, 0, 0, 53)
    BeginChrThread(0x11, 3, 0, 52)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 52)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 52)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 52)
    Sound(494, 0, 100, 0)
    OP_6F(0x79)
    Sleep(150)
    Fade(250)
    OP_68(65500, 0, 0, 0)
    MoveCamera(290, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0x16, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x24, 0x1)
    BeginChrThread(0xD, 3, 0, 50)
    BeginChrThread(0xE, 3, 0, 51)
    BeginChrThread(0x24, 0, 0, 62)
    Sound(495, 0, 100, 0)
    Sound(491, 0, 100, 0)
    MoveCamera(305, 20, 0, 4000)
    SetCameraDistance(27000, 4000)
    OP_68(73500, 0, 2000, 1000)
    OP_6F(0x1)
    OP_68(88500, 0, 0, 3000)
    OP_6F(0x79)
    EndChrThread(0x21, 0x1)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    Sound(490, 0, 100, 0)
    Fade(500)
    OP_68(90500, 500, 0, 0)
    MoveCamera(90, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x21, 70000, 0, 0, 0)
    OP_D3(0x21, 0x0, 0x15F90, 0x0, 0x0)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0xE, 0xFF)
    PlayEffect(0x1, 0x0, 0x21, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x21, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x21, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(2500)

    def lambda_4798():
        OP_98(0xFE, 0x13880, 0x0, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4798)
    MoveCamera(90, 17, 0, 5000)
    SetCameraDistance(24000, 5000)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    EndChrThread(0x24, 0x0)
    Sleep(1500)
    OP_E6()
    SetScenarioFlags(0x5C, 1)
    NewScene("e0111", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_3F33 end

    def Function_44_47EF(): pass

    label("Function_44_47EF")

    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_480C():

        label("loc_480C")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_480C")

    QueueWorkItem2(0x14, 2, lambda_480C)
    Sleep(1000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_483A():
        OP_9D(0xFE, 0x5014, 0x32, 0xB54, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_483A)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 53)
    BeginChrThread(0xFE, 1, 0, 45)
    Return()

    # Function_44_47EF end

    def Function_45_4876(): pass

    label("Function_45_4876")

    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 18900, 0, -1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 19200, 0, -1900, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 19700, 0, -1500, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 20600, 0, -800, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 21900, 0, -1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 23800, 0, -2900, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 26100, 0, -1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 29000, 0, -2200, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_45_4876 end

    def Function_46_4A44(): pass

    label("Function_46_4A44")

    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 77900, 0, -1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 78200, 0, -2400, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 79400, 0, -1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 81000, 0, -500, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 79400, 0, -1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 81000, 0, -500, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 83700, 0, -1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 86000, 0, -3100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 88300, 0, -2400, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 90800, 0, -1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 95000, 0, -2900, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_46_4A44 end

    def Function_47_4CC3(): pass

    label("Function_47_4CC3")

    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_4CE0():

        label("loc_4CE0")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_4CE0")

    QueueWorkItem2(0x15, 2, lambda_4CE0)
    Sleep(900)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x1)

    def lambda_4D08():
        OP_9D(0xFE, 0x5014, 0x32, 0xFFFFF0C4, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D08)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 53)
    BeginChrThread(0xFE, 1, 0, 48)
    Return()

    # Function_47_4CC3 end

    def Function_48_4D44(): pass

    label("Function_48_4D44")

    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 18900, 0, 1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 19200, 0, 1900, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 19700, 0, 1500, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 20600, 0, 800, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 21900, 0, 1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 23800, 0, 2900, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 26100, 0, 1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 29000, 0, 2200, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_48_4D44 end

    def Function_49_4F12(): pass

    label("Function_49_4F12")

    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 77900, 0, 1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 78200, 0, 2400, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 79400, 0, 1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 81000, 0, 500, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 79400, 0, 1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 81000, 0, 500, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 83700, 0, 1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 86000, 0, 3100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 88300, 0, 2400, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 90800, 0, 1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 95000, 0, 2900, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_49_4F12 end

    def Function_50_5191(): pass

    label("Function_50_5191")


    def lambda_5196():

        label("loc_5196")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_5196")

    QueueWorkItem2(0xD, 2, lambda_5196)
    Sleep(1000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_51C4():
        OP_9D(0xFE, 0x13498, 0x32, 0xB54, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_51C4)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 1, 0, 49)
    BeginChrThread(0xFE, 3, 0, 53)
    Return()

    # Function_50_5191 end

    def Function_51_5200(): pass

    label("Function_51_5200")


    def lambda_5205():

        label("loc_5205")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_5205")

    QueueWorkItem2(0xE, 2, lambda_5205)
    Sleep(1100)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x1)

    def lambda_522D():
        OP_9D(0xFE, 0x132A4, 0x32, 0xFFFFF4AC, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_522D)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 1, 0, 46)
    BeginChrThread(0xFE, 3, 0, 53)
    Return()

    # Function_51_5200 end

    def Function_52_5269(): pass

    label("Function_52_5269")

    OP_93(0xFE, 0x10E, 0x0)
    BeginChrThread(0xFE, 0, 0, 55)
    Sleep(2250)
    EndChrThread(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xFE, 0x10E, 0x2BC)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_529C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_529C)
    Sound(814, 0, 100, 0)

    def lambda_52BB():
        OP_9C(0xFE, 0x1F4, 0x0, 0xFFFFF63C, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_52BB)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_52_5269 end

    def Function_53_52EB(): pass

    label("Function_53_52EB")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    BeginChrThread(0xFE, 0, 0, 54)

    label("loc_530A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5341")

    def lambda_531A():
        OP_A6(0xFE, 0x0, 0x1E, 0x3C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_531A)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    Jump("loc_530A")

    label("loc_5341")

    Return()

    # Function_53_52EB end

    def Function_54_5342(): pass

    label("Function_54_5342")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_538C")
    PlayEffect(0x0, 0xFF, 0xFE, 0x140, 0, 900, 900, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Jump("Function_54_5342")

    label("loc_538C")

    Return()

    # Function_54_5342 end

    def Function_55_538D(): pass

    label("Function_55_538D")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)

    label("loc_539F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5414")
    PlayEffect(0x0, 0xFF, 0xFE, 0x140, 0, 900, 900, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_53E6():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53E6)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    Jump("loc_539F")

    label("loc_5414")

    Return()

    # Function_55_538D end

    def Function_56_5415(): pass

    label("Function_56_5415")


    def lambda_541A():
        OP_95(0xFE, 58000, 0, -600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_541A)
    WaitChrThread(0xFE, 1)

    def lambda_5438():
        OP_95(0xFE, 48000, 0, -600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5438)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_5415 end

    def Function_57_5452(): pass

    label("Function_57_5452")


    def lambda_5457():
        OP_95(0xFE, 56000, 0, -3000, 13000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_5457)
    WaitChrThread(0x21, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    BeginChrThread(0x1F, 3, 0, 59)

    def lambda_548D():
        OP_9E(0xFE, 0xE290, 0x1B58, 0xFFFF5038, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_548D)

    def lambda_54A8():
        OP_D3(0xFE, 0x0, 0xAFC8, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_54A8)
    WaitChrThread(0x21, 2)
    OP_82(0x12C, 0x0, 0xBB8, 0xFA)

    def lambda_54D6():
        OP_D3(0xFE, 0x0, 0xEA60, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_54D6)
    WaitChrThread(0x21, 1)
    CancelBlur(1000)
    OP_93(0x21, 0x3C, 0x0)

    def lambda_54FF():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_54FF)
    WaitChrThread(0x21, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    BeginChrThread(0x20, 3, 0, 60)

    def lambda_5530():
        OP_9E(0xFE, 0x11B34, 0xFFFFF060, 0xC350, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_5530)

    def lambda_554B():
        OP_D3(0xFE, 0x0, 0x1E848, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_554B)
    Sleep(400)
    OP_82(0x12C, 0x0, 0xBB8, 0xFA)
    WaitChrThread(0x21, 1)
    CancelBlur(1000)
    OP_93(0x21, 0x7D, 0x0)

    def lambda_5588():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_5588)
    WaitChrThread(0x21, 1)

    def lambda_55A1():
        OP_9E(0xFE, 0x13C68, 0x30D4, 0xFFFF6F78, 0x2710, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_55A1)
    WaitChrThread(0x21, 1)

    def lambda_55C0():
        OP_96(0xFE, 0x27100, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_55C0)
    Return()

    # Function_57_5452 end

    def Function_58_55D6(): pass

    label("Function_58_55D6")

    Sleep(2200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -1500, 1100, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -1500, 1700, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3000, 1500, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3000, 1600, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1500, -900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1200, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1700, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1000, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1500, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 2000, 1500, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 1000, 1000, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 3500, 1100, -900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 0, 1700, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 3500, 1500, -700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -1000, 1000, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 3500, 1100, -1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 0, 1100, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -500, 1700, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -1000, 1500, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -1500, 1400, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -2500, 1100, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1500, -1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_58_55D6 end

    def Function_59_5B0D(): pass

    label("Function_59_5B0D")

    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 54200, 0, -3700, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 55900, 0, -4700, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 57600, 0, -5400, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 59500, 0, -4700, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 62100, 0, -3800, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_59_5B0D end

    def Function_60_5C2D(): pass

    label("Function_60_5C2D")

    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 63200, 0, 2600, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 64800, 0, 3600, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 66600, 0, 4500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 68300, 0, 5300, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 70400, 0, 5600, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_60_5C2D end

    def Function_61_5D4D(): pass

    label("Function_61_5D4D")

    Sleep(1600)
    BeginChrThread(0x24, 2, 0, 63)
    BeginChrThread(0x24, 3, 0, 64)
    Sleep(3500)
    EndChrThread(0x24, 0x3)
    Sleep(500)
    EndChrThread(0x24, 0x2)
    Return()

    # Function_61_5D4D end

    def Function_62_5D6B(): pass

    label("Function_62_5D6B")

    BeginChrThread(0x24, 2, 0, 63)
    BeginChrThread(0x24, 3, 0, 64)
    Sleep(4000)
    EndChrThread(0x24, 0x3)
    EndChrThread(0x24, 0x2)
    Return()

    # Function_62_5D6B end

    def Function_63_5D83(): pass

    label("Function_63_5D83")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D9C")
    Sound(355, 0, 90, 0)
    Sleep(600)
    Jump("Function_63_5D83")

    label("loc_5D9C")

    Return()

    # Function_63_5D83 end

    def Function_64_5D9D(): pass

    label("Function_64_5D9D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5DBC")
    Sound(956, 0, 90, 0)
    Sound(957, 0, 90, 0)
    Sleep(1100)
    Jump("Function_64_5D9D")

    label("loc_5DBC")

    Return()

    # Function_64_5D9D end

    SaveToFile()

Try(main)
