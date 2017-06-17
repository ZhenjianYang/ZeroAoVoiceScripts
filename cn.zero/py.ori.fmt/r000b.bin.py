from ZeroScenarioHelper import *

def main():
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
        "蔡特",                   # 1
        "黑手党",                 # 2
        "黑手党",                 # 3
        "黑手党",                 # 4
        "黑手党",                 # 5
        "黑手党",                 # 6
        "黑手党",                 # 7
        "黑手党",                 # 8
        "黑手党",                 # 9
        "黑手党",                 # 10
        "黑手党",                 # 11
        "黑手党",                 # 12
        "黑手党",                 # 13
        "黑手党",                 # 14
        "黑手党",                 # 15
        "猎犬帝王",               # 16
        "猎犬帝王",               # 17
        "警备队员",               # 18
        "警备队员",               # 19
        "警备队员",               # 20
        "警备队员",               # 21
        "警备队员",               # 22
        "警备队员",               # 23
        "车１",                   # 24
        "车２",                   # 25
        "车３",                   # 26
        "迪塔总裁",               # 27
        "玛丽亚贝尔",             # 28
        "SE控制",                 # 29
        "br000b",                 # 30
        "克洛斯贝尔市方向",       # 31
        "阿尔摩利卡村·唐古拉姆门方向",# 32
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

    PlaceName(-17.0, 0.0, -7.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(203.0, 0.0, 27.5, 0x0000, 0x0000, "阿尔摩利卡村·唐古拉姆门方向")

    ScpFunction((
        "Function_0_6B8",          # 00, 0
        "Function_1_6D4",          # 01, 1
        "Function_2_6F0",          # 02, 2
        "Function_3_728",          # 03, 3
        "Function_4_729",          # 04, 4
        "Function_5_1586",         # 05, 5
        "Function_6_15AC",         # 06, 6
        "Function_7_15F0",         # 07, 7
        "Function_8_161F",         # 08, 8
        "Function_9_164E",         # 09, 9
        "Function_10_167D",        # 0A, 10
        "Function_11_16D0",        # 0B, 11
        "Function_12_2F92",        # 0C, 12
        "Function_13_30B2",        # 0D, 13
        "Function_14_3214",        # 0E, 14
        "Function_15_3262",        # 0F, 15
        "Function_16_32C2",        # 10, 16
        "Function_17_3322",        # 11, 17
        "Function_18_3571",        # 12, 18
        "Function_19_36CF",        # 13, 19
        "Function_20_38A2",        # 14, 20
        "Function_21_3947",        # 15, 21
        "Function_22_39B8",        # 16, 22
        "Function_23_3A29",        # 17, 23
        "Function_24_3A94",        # 18, 24
        "Function_25_3ACB",        # 19, 25
        "Function_26_3B02",        # 1A, 26
        "Function_27_3B53",        # 1B, 27
        "Function_28_3B9E",        # 1C, 28
        "Function_29_3BEF",        # 1D, 29
        "Function_30_3C4C",        # 1E, 30
        "Function_31_3C73",        # 1F, 31
        "Function_32_3C9A",        # 20, 32
        "Function_33_3CC1",        # 21, 33
        "Function_34_3CE8",        # 22, 34
        "Function_35_3D0F",        # 23, 35
        "Function_36_3D36",        # 24, 36
        "Function_37_3D5D",        # 25, 37
        "Function_38_3D84",        # 26, 38
        "Function_39_3DDA",        # 27, 39
        "Function_40_3E30",        # 28, 40
        "Function_41_3E4A",        # 29, 41
        "Function_42_3E64",        # 2A, 42
        "Function_43_3E81",        # 2B, 43
        "Function_44_473D",        # 2C, 44
        "Function_45_47C4",        # 2D, 45
        "Function_46_4992",        # 2E, 46
        "Function_47_4C11",        # 2F, 47
        "Function_48_4C92",        # 30, 48
        "Function_49_4E60",        # 31, 49
        "Function_50_50DF",        # 32, 50
        "Function_51_514E",        # 33, 51
        "Function_52_51B7",        # 34, 52
        "Function_53_5239",        # 35, 53
        "Function_54_5290",        # 36, 54
        "Function_55_52DB",        # 37, 55
        "Function_56_5363",        # 38, 56
        "Function_57_53A0",        # 39, 57
        "Function_58_5524",        # 3A, 58
        "Function_59_5A5B",        # 3B, 59
        "Function_60_5B7B",        # 3C, 60
        "Function_61_5C9B",        # 3D, 61
        "Function_62_5CB9",        # 3E, 62
        "Function_63_5CD1",        # 3F, 63
        "Function_64_5CEB",        # 40, 64
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
        "#0006F#5P呼……呼……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0002
    ChrTalk(
        0x101,
        (
            "#0000F#11P……再怎么说，\x01",
            "他们也无法追到这里了吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B58():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B58)
    Sleep(100)

    def lambda_B68():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B68)
    Sleep(50)

    def lambda_B78():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B78)
    WaitChrThread(0x104, 2)

    #C0003
    ChrTalk(
        0x102,
        (
            "#0106F#11P是啊……\x01",
            "这全都多亏了科长他们的掩护。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x103,
        "#11P#0208F……希望他们能平安无事。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        "#11P#0303F如今我们能做的就只有向女神祈祷了……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#0006F#11P是啊……\x02\x03",

            "#0001F……琪雅、小滴，\x01",
            "你们没事吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C57():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C57)
    Sleep(50)

    def lambda_C67():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C67)
    Sleep(50)

    def lambda_C77():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C77)
    WaitChrThread(0x103, 2)

    #N0007
    NpcTalk(
        0x104,
        "滴",
        "#5P#6000F没、没事……\x02",
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#5P#1110F琪雅也不要紧哦～\x02\x03",

            "#1109F嘿嘿，现在就和第一次\x01",
            "遇见大家时一样呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#0012F#11P哈哈……确实呢。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x104,
        (
            "#6P#0306F自那场竞拍会之后，\x01",
            "才过了一个月多一点啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        "#6P#0202F稍微有些难以置信呢……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#0104F#5P呵呵……\x02\x03",

            "#0100F──那么，\x01",
            "既然决定了就这样前往郊外。\x02\x03",

            "我就先跟唐古拉姆门联络一下吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0013
    ChrTalk(
        0x101,
        (
            "#0000F#11P嗯，拜托了。\x02\x03",

            "如果联系不上的话，\x01",
            "联络诺艾尔上士也可以。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#0100F#5P嗯，知道了。\x02",
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

    def lambda_E68():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E68)
    Sleep(50)

    def lambda_E78():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E78)
    Sound(807, 0, 100, 0)
    Sleep(800)
    Sound(891, 2, 100, 0)
    Sleep(3000)

    #C0015
    ChrTalk(
        0x102,
        "#0108F#5P……好像正在通话……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#12P#0300F并不奇怪……\x01",
            "那边的情况应该也相当混乱吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#6P#0206F似乎暂时\x01",
            "无法取得联络呢。\x02",
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
            "#0100F#5P没办法了，\x01",
            "还是直接去诺艾尔小姐那──\x02",
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

    def lambda_FA0():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FA0)
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
        "#6P#1201F呜噜噜噜……\x02",
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

    def lambda_1071():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1071)
    Sleep(50)

    def lambda_1081():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1081)
    Sleep(50)

    def lambda_1091():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1091)
    Sleep(50)

    def lambda_10A1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10A1)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x102, 2)

    #C0020
    ChrTalk(
        0x101,
        "#0005F#6P怎么了……！？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#6P#0301F喂！该不会是……\x02",
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
        "#0007F鲁巴彻……！？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0201F袭击医院的似乎只是\x01",
            "他们的突击队……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#0310F毕竟是个人数多达三百人的组织，\x01",
            "虽然早就料到其它地方也会有埋伏了……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#0103F眼下似乎也只有\x01",
            "强行突破了呢……\x02",
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
            "#0013F琪雅、小滴，\x01",
            "尽量靠后站。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x1A0,
        "#1101F#6P……嗯……！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x158,
        "#6001F#12P#N是、是……！\x02",
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

    def lambda_1459():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1459)
    SetChrChipByIndex(0xA, 0x29)
    SetChrSubChip(0xA, 0x0)

    def lambda_147B():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_147B)
    SetChrChipByIndex(0xB, 0x2B)
    SetChrSubChip(0xB, 0x0)

    def lambda_149D():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_149D)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)

    def lambda_14BF():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_14BF)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x0)

    def lambda_14E1():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_14E1)
    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 0, 0, 1)

    def lambda_1509():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1509)
    SetChrChipByIndex(0x18, 0x2F)
    SetChrSubChip(0x18, 0x0)
    BeginChrThread(0x18, 0, 0, 1)

    def lambda_1531():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1531)
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

    def Function_5_1586(): pass

    label("Function_5_1586")

    OP_93(0x158, 0x10E, 0x1F4)

    def lambda_1592():
        OP_95(0xFE, 38900, 0, -2000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x158, 1, lambda_1592)
    WaitChrThread(0x158, 1)
    Return()

    # Function_5_1586 end

    def Function_6_15AC(): pass

    label("Function_6_15AC")

    OP_93(0x1A0, 0xE1, 0x1F4)

    def lambda_15B8():
        OP_95(0xFE, 43900, 0, -2000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A0, 1, lambda_15B8)
    WaitChrThread(0x1A0, 1)

    def lambda_15D6():
        OP_95(0xFE, 38900, 0, -2000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A0, 1, lambda_15D6)
    WaitChrThread(0x1A0, 1)
    Return()

    # Function_6_15AC end

    def Function_7_15F0(): pass

    label("Function_7_15F0")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    def lambda_15FD():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_15FD)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_7_15F0 end

    def Function_8_161F(): pass

    label("Function_8_161F")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    def lambda_162C():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_162C)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_161F end

    def Function_9_164E(): pass

    label("Function_9_164E")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)

    def lambda_165B():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_165B)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_9_164E end

    def Function_10_167D(): pass

    label("Function_10_167D")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1690():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1690)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x24, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_167D end

    def Function_11_16D0(): pass

    label("Function_11_16D0")

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
            "#6P#0302F好……\x01",
            "总算是摆平了！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#0000F#5P各位，就这样向郊外前──\x02",
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

    def lambda_1F10():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1F10)
    Sleep(50)

    def lambda_1F2D():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1F2D)
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
        "#0007F#6P……什么………\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        (
            "#6P#0310F嘁……\x01",
            "这下实在是闯不过去了啊。\x02\x03",

            "#0307F没办法，暂且先回市里吧，\x01",
            "可以去旧城区那边……\x02",
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
        "#0201F#11P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_2129():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2129)
    Sleep(50)

    def lambda_2139():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2139)
    Sleep(50)

    def lambda_2149():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2149)
    Sleep(50)

    def lambda_2159():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_2159)

    def lambda_2166():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x158, 2, lambda_2166)
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

    def lambda_21DA():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_21DA)

    def lambda_21F4():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_21F4)

    def lambda_220E():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_220E)

    def lambda_2228():
        OP_98(0xFE, 0x88B8, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2228)

    def lambda_2242():
        OP_98(0xFE, 0x88B8, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2242)

    def lambda_225C():
        OP_98(0xFE, 0x88B8, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_225C)
    Sleep(1500)

    #C0036
    ChrTalk(
        0x101,
        "#0010F唔……！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#0108F怎、怎么会……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#0310F穷途末路了吗……\x02",
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
        "#5P#1101F呀……！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x158,
        "#5P#6008F……爸、爸爸……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0008F#5P（唔……\x01",
            "  至少也要让这两个孩子……！）\x02",
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

    def lambda_2588():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2588)
    Sleep(50)

    def lambda_2598():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2598)
    Sleep(50)

    def lambda_25A8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_25A8)
    Sleep(50)

    def lambda_25B8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_25B8)

    def lambda_25C5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x158, 2, lambda_25C5)
    WaitChrThread(0x153, 2)

    #C0042
    ChrTalk(
        0x101,
        "#0005F#6P那是……！？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#0205F#6P又来了一辆车……！？\x02",
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

    def lambda_27A2():
        OP_96(0xFE, 0x20788, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_27A2)
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

    def lambda_28E4():

        label("loc_28E4")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_28E4")

    QueueWorkItem2(0xF, 2, lambda_28E4)

    def lambda_28F6():

        label("loc_28F6")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_28F6")

    QueueWorkItem2(0x10, 2, lambda_28F6)

    def lambda_2908():

        label("loc_2908")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_2908")

    QueueWorkItem2(0x13, 2, lambda_2908)

    def lambda_291A():

        label("loc_291A")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_291A")

    QueueWorkItem2(0x14, 2, lambda_291A)
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

    def lambda_2A2A():
        OP_96(0xFE, 0xA028, 0x0, 0x1F4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2A2A)
    WaitChrThread(0x21, 1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    Sound(495, 0, 100, 0)
    OP_82(0x12C, 0x0, 0xBB8, 0x258)

    def lambda_2A68():
        OP_9E(0xFE, 0xA028, 0xFFFFE69C, 0xFFFF8AD0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2A68)

    def lambda_2A83():
        OP_D3(0xFE, 0x0, 0x35B60, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_2A83)
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

    def lambda_2ACF():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_2ACF)

    def lambda_2ADC():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2ADC)

    def lambda_2AE9():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_2AE9)

    def lambda_2AF6():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_2AF6)
    OP_68(35000, 900, 2000, 1500)
    SetCameraDistance(19000, 1500)
    OP_6F(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x3)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B60")

    #C0044
    ChrTalk(
        0x101,
        (
            "#0005F#6P这辆豪华轿车是……\x01",
            "迪塔总裁的！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B8D")

    label("loc_2B60")


    #C0045
    ChrTalk(
        0x102,
        "#0105F#5P这、这辆红色的豪华轿车是……！\x02",
    )

    CloseMessageWindow()

    label("loc_2B8D")

    OP_71(0x7, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0x7)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)

    def lambda_2BB1():
        OP_96(0xFE, 0x8F5C, 0x96, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_2BB1)

    def lambda_2BCB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_2BCB)
    WaitChrThread(0x23, 1)

    #C0046
    ChrTalk(
        0x23,
        (
            "#2901F#11P来！\x01",
            "快上来！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#0102F#5P贝尔……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#6P#0011F玛丽亚贝尔小姐！？\x02",
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
            "#2801F有话稍后再说！\x01",
            "总之先上车！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#6P#0002F是、是！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x32)
    SetChrSubChip(0x101, 0x0)
    TurnDirection(0x101, 0x153, 500)

    #C0051
    ChrTalk(
        0x101,
        "#11P#0000F琪雅，要上车了哦！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)

    #C0052
    ChrTalk(
        0x153,
        "#1102F#5P嗯！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 24)
    SetChrChipByIndex(0x104, 0x33)
    SetChrSubChip(0x104, 0x0)
    TurnDirection(0x104, 0x158, 500)

    #C0053
    ChrTalk(
        0x104,
        "#11P#0300F小滴，抓紧我！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x158, 0x104, 500)

    #C0054
    ChrTalk(
        0x158,
        "#6000F#5P是、是。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x158, 3, 0, 25)
    OP_68(29000, 900, 500, 6000)
    MoveCamera(55, 17, 0, 6000)
    SetCameraDistance(21000, 6000)
    BeginChrThread(0x102, 3, 0, 18)
    BeginChrThread(0x103, 3, 0, 19)
    BeginChrThread(0x8, 3, 0, 17)

    def lambda_2D6E():
        OP_96(0xFE, 0x9088, 0x96, 0xFFFFFF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_2D6E)

    def lambda_2D88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_2D88)
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

    def lambda_2DDA():
        OP_9B(0x1, 0xFE, 0xB4, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2DDA)
    WaitChrThread(0x21, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sleep(300)

    def lambda_2E07():

        label("loc_2E07")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_2E07")

    QueueWorkItem2(0x1C, 2, lambda_2E07)
    Sound(490, 0, 100, 0)
    Sound(495, 0, 100, 0)
    OP_71(0x7, 0x1E1, 0x21C, 0x0, 0x20)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    def lambda_2E42():
        OP_9E(0xFE, 0x7C38, 0x206C, 0xC350, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2E42)
    Sleep(800)
    BeginChrThread(0x1C, 3, 0, 14)
    WaitChrThread(0x21, 1)

    def lambda_2E6A():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2E6A)
    OP_6F(0x79)
    Fade(250)
    OP_68(15000, 900, 0, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    EndChrThread(0x19, 0x2)

    def lambda_2EBD():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2EBD)
    BeginChrThread(0x19, 3, 0, 13)
    BeginChrThread(0x24, 2, 0, 42)
    EndChrThread(0x1A, 0x2)

    def lambda_2EDA():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2EDA)
    BeginChrThread(0x1A, 3, 0, 13)
    OP_68(5000, 900, 0, 4000)
    SetCameraDistance(21000, 4000)
    Sleep(1000)
    SetChrChipByIndex(0x1C, 0x2A)
    SetChrSubChip(0x1C, 0x0)

    def lambda_2F12():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2F12)
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

    # Function_11_16D0 end

    def Function_12_2F92(): pass

    label("Function_12_2F92")

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

    # Function_12_2F92 end

    def Function_13_30B2(): pass

    label("Function_13_30B2")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)

    label("loc_30BD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3213")

    def lambda_30CD():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30CD)
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
    Jump("loc_30BD")

    label("loc_3213")

    Return()

    # Function_13_30B2 end

    def Function_14_3214(): pass

    label("Function_14_3214")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1C, 0x2A)
    SetChrSubChip(0x1C, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_3232():
        OP_9D(0xFE, 0x61A8, 0x0, 0x320, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3232)
    WaitChrThread(0x1C, 1)
    SetChrChipByIndex(0x1C, 0x29)
    SetChrSubChip(0x1C, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_3214 end

    def Function_15_3262(): pass

    label("Function_15_3262")

    OP_92(0x101, 0x8B10, 0x320, 0x1F4)

    def lambda_3274():
        OP_95(0xFE, 35600, 0, 800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3274)
    WaitChrThread(0x101, 1)
    SetChrFlags(0x101, 0x4)

    def lambda_3297():
        OP_95(0xFE, 37000, 150, -100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3297)

    def lambda_32B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_32B1)
    WaitChrThread(0x101, 1)
    Return()

    # Function_15_3262 end

    def Function_16_32C2(): pass

    label("Function_16_32C2")

    OP_92(0x104, 0x8B10, 0x320, 0x1F4)

    def lambda_32D4():
        OP_95(0xFE, 35600, 0, 800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_32D4)
    WaitChrThread(0x104, 1)
    SetChrFlags(0x104, 0x4)

    def lambda_32F7():
        OP_95(0xFE, 37000, 150, -100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_32F7)

    def lambda_3311():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3311)
    WaitChrThread(0x104, 1)
    Return()

    # Function_16_32C2 end

    def Function_17_3322(): pass

    label("Function_17_3322")

    Sleep(1000)
    SetChrChipByIndex(0x8, 0x15)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3348():
        OP_92(0xFE, 0x6BD0, 0x1A2C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3348)
    SetChrChip(0x0, 0x8, 0x1E, 0xC8)
    Sound(854, 0, 100, 0)

    def lambda_3369():
        OP_9D(0xFE, 0x6BD0, 0x3E8, 0x1A2C, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3369)
    Sleep(350)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    WaitChrThread(0x8, 1)
    PlayEffect(0x6, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_33CF():
        OP_92(0xFE, 0x55F0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_33CF)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x0)

    def lambda_33EA():

        label("loc_33EA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_33EA")

    QueueWorkItem2(0x19, 2, lambda_33EA)

    def lambda_33FC():

        label("loc_33FC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_33FC")

    QueueWorkItem2(0x1A, 2, lambda_33FC)
    Sleep(3500)
    SetChrChipByIndex(0x8, 0x15)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_3426():
        OP_9D(0xFE, 0x55F0, 0x0, 0x708, 0x6A4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3426)
    Sleep(550)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    WaitChrThread(0x8, 1)
    PlayEffect(0x6, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_348C():
        OP_92(0xFE, 0x4268, 0xFFFFF704, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_348C)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_34B0():
        OP_9D(0xFE, 0x4268, 0x76C, 0xFFFFF704, 0xA28, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_34B0)
    Sleep(400)
    WaitChrThread(0x8, 1)
    Sound(925, 0, 100, 0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0x8, 0x0, 0x0)

    def lambda_34F8():
        OP_98(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_34F8)
    SetChrChipByIndex(0x8, 0x14)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3546():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3546)
    WaitChrThread(0x8, 2)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x3)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_3322 end

    def Function_18_3571(): pass

    label("Function_18_3571")

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

    def lambda_3681():
        OP_95(0xFE, 37800, 0, 3200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3681)
    WaitChrThread(0x102, 1)
    SetChrFlags(0x102, 0x4)

    def lambda_36A4():
        OP_95(0xFE, 39000, 150, 2200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36A4)

    def lambda_36BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_36BE)
    WaitChrThread(0x102, 1)
    Return()

    # Function_18_3571 end

    def Function_19_36CF(): pass

    label("Function_19_36CF")

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

    def lambda_3854():
        OP_95(0xFE, 32200, 0, 400, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3854)
    WaitChrThread(0x103, 1)
    SetChrFlags(0x103, 0x4)

    def lambda_3877():
        OP_95(0xFE, 31200, 150, -1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3877)

    def lambda_3891():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3891)
    WaitChrThread(0x103, 1)
    Return()

    # Function_19_36CF end

    def Function_20_38A2(): pass

    label("Function_20_38A2")

    OP_93(0xFE, 0x10E, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_38F8():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38F8)

    def lambda_3911():
        OP_9C(0xFE, 0xFA0, 0x0, 0x190, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3911)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_20_38A2 end

    def Function_21_3947(): pass

    label("Function_21_3947")

    Sleep(1100)
    OP_93(0xFE, 0x13B, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3969():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3969)

    def lambda_3982():
        OP_9D(0xFE, 0xA0F0, 0x0, 0xFFFFEA20, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3982)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_21_3947 end

    def Function_22_39B8(): pass

    label("Function_22_39B8")

    Sleep(1100)
    OP_93(0xFE, 0x0, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_39DA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39DA)

    def lambda_39F3():
        OP_9D(0xFE, 0x7AA8, 0x0, 0xFFFFEB4C, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39F3)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_22_39B8 end

    def Function_23_3A29(): pass

    label("Function_23_3A29")

    Sleep(1100)
    OP_93(0xFE, 0x2D, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3A4B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A4B)

    def lambda_3A64():
        OP_9D(0xFE, 0x6C34, 0x0, 0xFFFFEE08, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A64)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_23_3A29 end

    def Function_24_3A94(): pass

    label("Function_24_3A94")


    def lambda_3A99():
        OP_99(0xFE, 0x101, 0x320, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3A99)
    WaitChrThread(0x153, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x153, 0x80)
    SetChrBattleFlags(0x153, 0x8000)
    OP_0D()
    Return()

    # Function_24_3A94 end

    def Function_25_3ACB(): pass

    label("Function_25_3ACB")


    def lambda_3AD0():
        OP_99(0xFE, 0x104, 0x320, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x158, 1, lambda_3AD0)
    WaitChrThread(0x158, 1)
    Fade(250)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x158, 0x80)
    SetChrBattleFlags(0x158, 0x8000)
    OP_0D()
    Return()

    # Function_25_3ACB end

    def Function_26_3B02(): pass

    label("Function_26_3B02")

    Sleep(1300)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_3B23():
        OP_9D(0xFE, 0xA5A0, 0x0, 0xFA0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3B23)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_26_3B02 end

    def Function_27_3B53(): pass

    label("Function_27_3B53")

    Sleep(1800)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x1)

    def lambda_3B6E():
        OP_9D(0xFE, 0x7AA8, 0x0, 0xFFFFEDA4, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3B6E)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_27_3B53 end

    def Function_28_3B9E(): pass

    label("Function_28_3B9E")

    Sleep(1600)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_3BBF():
        OP_9D(0xFE, 0x9AB0, 0x0, 0xFFFFEF98, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3BBF)
    WaitChrThread(0x13, 1)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_28_3B9E end

    def Function_29_3BEF(): pass

    label("Function_29_3BEF")

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

    # Function_29_3BEF end

    def Function_30_3C4C(): pass

    label("Function_30_3C4C")


    def lambda_3C51():
        OP_95(0xFE, 39100, 0, 4600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C51)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    Return()

    # Function_30_3C4C end

    def Function_31_3C73(): pass

    label("Function_31_3C73")


    def lambda_3C78():
        OP_95(0xFE, 39700, 0, 2000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C78)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_31_3C73 end

    def Function_32_3C9A(): pass

    label("Function_32_3C9A")


    def lambda_3C9F():
        OP_95(0xFE, 37900, 0, -1100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C9F)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    Return()

    # Function_32_3C9A end

    def Function_33_3CC1(): pass

    label("Function_33_3CC1")


    def lambda_3CC6():
        OP_95(0xFE, 34500, 0, -2400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CC6)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    Return()

    # Function_33_3CC1 end

    def Function_34_3CE8(): pass

    label("Function_34_3CE8")


    def lambda_3CED():
        OP_95(0xFE, 24500, 0, 4600, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CED)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x19, 0x27)
    SetChrSubChip(0x19, 0x0)
    Return()

    # Function_34_3CE8 end

    def Function_35_3D0F(): pass

    label("Function_35_3D0F")


    def lambda_3D14():
        OP_95(0xFE, 23900, 0, 2000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D14)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x1A, 0x27)
    SetChrSubChip(0x1A, 0x0)
    Return()

    # Function_35_3D0F end

    def Function_36_3D36(): pass

    label("Function_36_3D36")


    def lambda_3D3B():
        OP_95(0xFE, 25700, 0, -1100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D3B)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x1C, 0x29)
    SetChrSubChip(0x1C, 0x0)
    Return()

    # Function_36_3D36 end

    def Function_37_3D5D(): pass

    label("Function_37_3D5D")


    def lambda_3D62():
        OP_95(0xFE, 29100, 0, -2400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D62)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x1D, 0x29)
    SetChrSubChip(0x1D, 0x0)
    Return()

    # Function_37_3D5D end

    def Function_38_3D84(): pass

    label("Function_38_3D84")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3D91():
        OP_95(0xFE, 113100, 0, 400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D91)

    def lambda_3DAB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3DAB)
    WaitChrThread(0xFE, 1)

    def lambda_3DC0():
        OP_95(0xFE, 100100, 0, 400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DC0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_3D84 end

    def Function_39_3DDA(): pass

    label("Function_39_3DDA")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3DE7():
        OP_95(0xFE, 111100, 0, -4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DE7)

    def lambda_3E01():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E01)
    WaitChrThread(0xFE, 1)

    def lambda_3E16():
        OP_95(0xFE, 100100, 0, -4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E16)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_39_3DDA end

    def Function_40_3E30(): pass

    label("Function_40_3E30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E49")
    Sound(832, 0, 100, 0)
    Sleep(500)
    Jump("Function_40_3E30")

    label("loc_3E49")

    Return()

    # Function_40_3E30 end

    def Function_41_3E4A(): pass

    label("Function_41_3E4A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E63")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_41_3E4A")

    label("loc_3E63")

    Return()

    # Function_41_3E4A end

    def Function_42_3E64(): pass

    label("Function_42_3E64")

    Sleep(500)

    label("loc_3E67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E80")
    Sound(957, 0, 100, 0)
    Sleep(1200)
    Jump("loc_3E67")

    label("loc_3E80")

    Return()

    # Function_42_3E64 end

    def Function_43_3E81(): pass

    label("Function_43_3E81")

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
            "#1K同日，２３：３０──\x02",
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

    def lambda_447E():

        label("loc_447E")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_447E")

    QueueWorkItem2(0xC, 2, lambda_447E)

    def lambda_4490():

        label("loc_4490")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_4490")

    QueueWorkItem2(0x16, 2, lambda_4490)
    BeginChrThread(0xC, 0, 0, 55)
    BeginChrThread(0x16, 0, 0, 53)
    OP_68(63500, 500, 0, 2500)
    MoveCamera(47, 15, 0, 2500)
    SetCameraDistance(21000, 2500)
    Sound(491, 0, 100, 0)

    def lambda_44D9():

        label("loc_44D9")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_44D9")

    QueueWorkItem2(0x13, 2, lambda_44D9)
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

    def lambda_46E6():
        OP_98(0xFE, 0x13880, 0x0, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_46E6)
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

    # Function_43_3E81 end

    def Function_44_473D(): pass

    label("Function_44_473D")

    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_475A():

        label("loc_475A")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_475A")

    QueueWorkItem2(0x14, 2, lambda_475A)
    Sleep(1000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_4788():
        OP_9D(0xFE, 0x5014, 0x32, 0xB54, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4788)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 53)
    BeginChrThread(0xFE, 1, 0, 45)
    Return()

    # Function_44_473D end

    def Function_45_47C4(): pass

    label("Function_45_47C4")

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

    # Function_45_47C4 end

    def Function_46_4992(): pass

    label("Function_46_4992")

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

    # Function_46_4992 end

    def Function_47_4C11(): pass

    label("Function_47_4C11")

    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_4C2E():

        label("loc_4C2E")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_4C2E")

    QueueWorkItem2(0x15, 2, lambda_4C2E)
    Sleep(900)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x1)

    def lambda_4C56():
        OP_9D(0xFE, 0x5014, 0x32, 0xFFFFF0C4, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C56)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 53)
    BeginChrThread(0xFE, 1, 0, 48)
    Return()

    # Function_47_4C11 end

    def Function_48_4C92(): pass

    label("Function_48_4C92")

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

    # Function_48_4C92 end

    def Function_49_4E60(): pass

    label("Function_49_4E60")

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

    # Function_49_4E60 end

    def Function_50_50DF(): pass

    label("Function_50_50DF")


    def lambda_50E4():

        label("loc_50E4")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_50E4")

    QueueWorkItem2(0xD, 2, lambda_50E4)
    Sleep(1000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_5112():
        OP_9D(0xFE, 0x13498, 0x32, 0xB54, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5112)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 1, 0, 49)
    BeginChrThread(0xFE, 3, 0, 53)
    Return()

    # Function_50_50DF end

    def Function_51_514E(): pass

    label("Function_51_514E")


    def lambda_5153():

        label("loc_5153")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_5153")

    QueueWorkItem2(0xE, 2, lambda_5153)
    Sleep(1100)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x1)

    def lambda_517B():
        OP_9D(0xFE, 0x132A4, 0x32, 0xFFFFF4AC, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_517B)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 1, 0, 46)
    BeginChrThread(0xFE, 3, 0, 53)
    Return()

    # Function_51_514E end

    def Function_52_51B7(): pass

    label("Function_52_51B7")

    OP_93(0xFE, 0x10E, 0x0)
    BeginChrThread(0xFE, 0, 0, 55)
    Sleep(2250)
    EndChrThread(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xFE, 0x10E, 0x2BC)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_51EA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_51EA)
    Sound(814, 0, 100, 0)

    def lambda_5209():
        OP_9C(0xFE, 0x1F4, 0x0, 0xFFFFF63C, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5209)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_52_51B7 end

    def Function_53_5239(): pass

    label("Function_53_5239")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    BeginChrThread(0xFE, 0, 0, 54)

    label("loc_5258")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_528F")

    def lambda_5268():
        OP_A6(0xFE, 0x0, 0x1E, 0x3C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5268)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    Jump("loc_5258")

    label("loc_528F")

    Return()

    # Function_53_5239 end

    def Function_54_5290(): pass

    label("Function_54_5290")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52DA")
    PlayEffect(0x0, 0xFF, 0xFE, 0x140, 0, 900, 900, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Jump("Function_54_5290")

    label("loc_52DA")

    Return()

    # Function_54_5290 end

    def Function_55_52DB(): pass

    label("Function_55_52DB")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)

    label("loc_52ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5362")
    PlayEffect(0x0, 0xFF, 0xFE, 0x140, 0, 900, 900, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_5334():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5334)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    Jump("loc_52ED")

    label("loc_5362")

    Return()

    # Function_55_52DB end

    def Function_56_5363(): pass

    label("Function_56_5363")


    def lambda_5368():
        OP_95(0xFE, 58000, 0, -600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5368)
    WaitChrThread(0xFE, 1)

    def lambda_5386():
        OP_95(0xFE, 48000, 0, -600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5386)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_5363 end

    def Function_57_53A0(): pass

    label("Function_57_53A0")


    def lambda_53A5():
        OP_95(0xFE, 56000, 0, -3000, 13000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_53A5)
    WaitChrThread(0x21, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    BeginChrThread(0x1F, 3, 0, 59)

    def lambda_53DB():
        OP_9E(0xFE, 0xE290, 0x1B58, 0xFFFF5038, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_53DB)

    def lambda_53F6():
        OP_D3(0xFE, 0x0, 0xAFC8, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_53F6)
    WaitChrThread(0x21, 2)
    OP_82(0x12C, 0x0, 0xBB8, 0xFA)

    def lambda_5424():
        OP_D3(0xFE, 0x0, 0xEA60, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_5424)
    WaitChrThread(0x21, 1)
    CancelBlur(1000)
    OP_93(0x21, 0x3C, 0x0)

    def lambda_544D():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_544D)
    WaitChrThread(0x21, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    BeginChrThread(0x20, 3, 0, 60)

    def lambda_547E():
        OP_9E(0xFE, 0x11B34, 0xFFFFF060, 0xC350, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_547E)

    def lambda_5499():
        OP_D3(0xFE, 0x0, 0x1E848, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_5499)
    Sleep(400)
    OP_82(0x12C, 0x0, 0xBB8, 0xFA)
    WaitChrThread(0x21, 1)
    CancelBlur(1000)
    OP_93(0x21, 0x7D, 0x0)

    def lambda_54D6():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_54D6)
    WaitChrThread(0x21, 1)

    def lambda_54EF():
        OP_9E(0xFE, 0x13C68, 0x30D4, 0xFFFF6F78, 0x2710, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_54EF)
    WaitChrThread(0x21, 1)

    def lambda_550E():
        OP_96(0xFE, 0x27100, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_550E)
    Return()

    # Function_57_53A0 end

    def Function_58_5524(): pass

    label("Function_58_5524")

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

    # Function_58_5524 end

    def Function_59_5A5B(): pass

    label("Function_59_5A5B")

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

    # Function_59_5A5B end

    def Function_60_5B7B(): pass

    label("Function_60_5B7B")

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

    # Function_60_5B7B end

    def Function_61_5C9B(): pass

    label("Function_61_5C9B")

    Sleep(1600)
    BeginChrThread(0x24, 2, 0, 63)
    BeginChrThread(0x24, 3, 0, 64)
    Sleep(3500)
    EndChrThread(0x24, 0x3)
    Sleep(500)
    EndChrThread(0x24, 0x2)
    Return()

    # Function_61_5C9B end

    def Function_62_5CB9(): pass

    label("Function_62_5CB9")

    BeginChrThread(0x24, 2, 0, 63)
    BeginChrThread(0x24, 3, 0, 64)
    Sleep(4000)
    EndChrThread(0x24, 0x3)
    EndChrThread(0x24, 0x2)
    Return()

    # Function_62_5CB9 end

    def Function_63_5CD1(): pass

    label("Function_63_5CD1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CEA")
    Sound(355, 0, 90, 0)
    Sleep(600)
    Jump("Function_63_5CD1")

    label("loc_5CEA")

    Return()

    # Function_63_5CD1 end

    def Function_64_5CEB(): pass

    label("Function_64_5CEB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D0A")
    Sound(956, 0, 90, 0)
    Sound(957, 0, 90, 0)
    Sleep(1100)
    Jump("Function_64_5CEB")

    label("loc_5D0A")

    Return()

    # Function_64_5CEB end

    SaveToFile()

Try(main)
