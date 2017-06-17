from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9012.bin",                # FileName
        "m9012",                    # MapName
        "m9012",                    # Location
        0x00C4,                     # MapIndex
        "ed7353",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 196, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9012",                  # 0
        "伊安律师",               # 1
        "琪雅",                   # 2
        "玛丽亚贝尔",             # 3
        "碧之虚神",               # 4
        "玛丽亚贝尔残影",         # 5
        "伊安被钉模型",           # 6
        "琪雅模型",               # 7
        "SE控制",                 # 8
        "APL表示用",              # 9
        "bm9070",                 # 10
        "bm9099",                 # 11
        "bm9099",                 # 12
    ))

    ATBonus("ATBonus_1C0", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_1D0", 100, 5, 0, 5, 0, 5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_200", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_204", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_20C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_210", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_214", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_218", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_21C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_260", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_264", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_268", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_26C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_270", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_274", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_278", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_280", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_288", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_28C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 0, 0, 180)

    # monster count: 0

    # event battle count: 3

    BattleInfo(
        "BattleInfo_2C0", 0x0052, 255, 6, 45, 3, 1, 30, 0, "bm9070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03700.dat", "ms80500.dat", "ms80500.dat", "ms80500.dat", "ms80500.dat", 0, "ms80500.dat", 0, "MonsterBattlePostion_200", "MonsterBattlePostion_260", "ed7458", "ed7453", "ATBonus_1C0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_304", 0x009A, 255, 6, 45, 3, 1, 30, 0, "bm9099", 0x00000000, 100, 0, 0, 0,
        (
            (0, 0, 0, 0, 0, "ms89000.dat", "ms86400.dat", 0, "MonsterBattlePostion_280", "MonsterBattlePostion_280", "ed7459", "ed7453", "ATBonus_1D0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_348", 0x009A, 255, 6, 45, 3, 1, 30, 0, "bm9099", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89100.dat", 0, 0, 0, 0, 0, "ms86500.dat", 0, "MonsterBattlePostion_2A0", "MonsterBattlePostion_2A0", "ed7459", "ed7453", "ATBonus_1D0"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       3750,    -5849,   0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1300, 0)                                       # 0

    ScpFunction((
        "Function_0_514",          # 00, 0
        "Function_1_55E",          # 01, 1
        "Function_2_5AC",          # 02, 2
        "Function_3_60D",          # 03, 3
        "Function_4_66E",          # 04, 4
        "Function_5_689",          # 05, 5
        "Function_6_695",          # 06, 6
        "Function_7_5731",         # 07, 7
        "Function_8_579B",         # 08, 8
        "Function_9_5805",         # 09, 9
        "Function_10_586F",        # 0A, 10
        "Function_11_58D9",        # 0B, 11
        "Function_12_5943",        # 0C, 12
        "Function_13_59AD",        # 0D, 13
        "Function_14_59C9",        # 0E, 14
        "Function_15_59E8",        # 0F, 15
        "Function_16_5A07",        # 10, 16
        "Function_17_5A26",        # 11, 17
        "Function_18_5A45",        # 12, 18
        "Function_19_5A64",        # 13, 19
        "Function_20_5A76",        # 14, 20
        "Function_21_5A85",        # 15, 21
        "Function_22_5A97",        # 16, 22
        "Function_23_5AA9",        # 17, 23
        "Function_24_5AB5",        # 18, 24
        "Function_25_5B03",        # 19, 25
        "Function_26_5B51",        # 1A, 26
        "Function_27_5B87",        # 1B, 27
        "Function_28_5BC4",        # 1C, 28
        "Function_29_5C16",        # 1D, 29
        "Function_30_5D36",        # 1E, 30
        "Function_31_5E85",        # 1F, 31
        "Function_32_5EFA",        # 20, 32
        "Function_33_5F16",        # 21, 33
        "Function_34_5F2B",        # 22, 34
        "Function_35_5F3A",        # 23, 35
        "Function_36_5FA5",        # 24, 36
        "Function_37_5FBB",        # 25, 37
        "Function_38_5FD1",        # 26, 38
        "Function_39_5FE7",        # 27, 39
        "Function_40_5FFD",        # 28, 40
        "Function_41_6013",        # 29, 41
        "Function_42_6030",        # 2A, 42
        "Function_43_604D",        # 2B, 43
        "Function_44_605C",        # 2C, 44
        "Function_45_606B",        # 2D, 45
        "Function_46_60B8",        # 2E, 46
        "Function_47_7D6C",        # 2F, 47
        "Function_48_7DBB",        # 30, 48
        "Function_49_7DE5",        # 31, 49
        "Function_50_7DEC",        # 32, 50
        "Function_51_7E08",        # 33, 51
        "Function_52_7E86",        # 34, 52
        "Function_53_7EA8",        # 35, 53
        "Function_54_7EB6",        # 36, 54
        "Function_55_7ED0",        # 37, 55
        "Function_56_7EED",        # 38, 56
        "Function_57_7F0C",        # 39, 57
        "Function_58_8DCB",        # 3A, 58
        "Function_59_8DDC",        # 3B, 59
        "Function_60_8E17",        # 3C, 60
        "Function_61_8F3A",        # 3D, 61
        "Function_62_90D4",        # 3E, 62
        "Function_63_9159",        # 3F, 63
        "Function_64_9168",        # 40, 64
        "Function_65_917A",        # 41, 65
        "Function_66_918C",        # 42, 66
        "Function_67_9198",        # 43, 67
        "Function_68_91E6",        # 44, 68
        "Function_69_9234",        # 45, 69
        "Function_70_9251",        # 46, 70
        "Function_71_9296",        # 47, 71
        "Function_72_D050",        # 48, 72
        "Function_73_D097",        # 49, 73
        "Function_74_D0F5",        # 4A, 74
        "Function_75_D120",        # 4B, 75
        "Function_76_D14B",        # 4C, 76
        "Function_77_D16F",        # 4D, 77
        "Function_78_D1C3",        # 4E, 78
        "Function_79_D1E5",        # 4F, 79
        "Function_80_D207",        # 50, 80
        "Function_81_D229",        # 51, 81
        "Function_82_D2A5",        # 52, 82
        "Function_83_D321",        # 53, 83
        "Function_84_D368",        # 54, 84
        "Function_85_D387",        # 55, 85
        "Function_86_D3A6",        # 56, 86
        "Function_87_D3C5",        # 57, 87
        "Function_88_D3E4",        # 58, 88
        "Function_89_D403",        # 59, 89
        "Function_90_D47F",        # 5A, 90
        "Function_91_D4C4",        # 5B, 91
        "Function_92_D54E",        # 5C, 92
        "Function_93_D5C6",        # 5D, 93
        "Function_94_D5EA",        # 5E, 94
        "Function_95_D60E",        # 5F, 95
        "Function_96_D632",        # 60, 96
        "Function_97_D65C",        # 61, 97
    ))


    def Function_0_514(): pass

    label("Function_0_514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 6)), scpexpr(EXPR_END)), "loc_520")
    Event(0, 6)

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_537")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 46)
    Jump("loc_55D")

    label("loc_537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_54E")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 57)
    Jump("loc_55D")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_55D")
    ClearScenarioFlags(0x22, 2)
    Event(0, 71)

    label("loc_55D")

    Return()

    # Function_0_514 end

    def Function_1_55E(): pass

    label("Function_1_55E")

    OP_F0(0x1, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_57C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_591")

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_591")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1CB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)

    label("loc_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5A5")
    OP_24(0x70)
    ClearScenarioFlags(0x0, 2)
    Jump("loc_5AB")

    label("loc_5A5")

    Sound(112, 1, 50, 0)

    label("loc_5AB")

    Return()

    # Function_1_55E end

    def Function_2_5AC(): pass

    label("Function_2_5AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C4")
    LoadChrToIndex("chr/ch03150.itc", 0x26)

    label("loc_5C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DC")
    LoadChrToIndex("chr/ch03250.itc", 0x26)

    label("loc_5DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F4")
    LoadChrToIndex("chr/ch02950.itc", 0x26)

    label("loc_5F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60C")
    LoadChrToIndex("chr/ch00950.itc", 0x26)

    label("loc_60C")

    Return()

    # Function_2_5AC end

    def Function_3_60D(): pass

    label("Function_3_60D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_625")
    LoadChrToIndex("chr/ch03150.itc", 0x27)

    label("loc_625")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63D")
    LoadChrToIndex("chr/ch03250.itc", 0x27)

    label("loc_63D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_655")
    LoadChrToIndex("chr/ch02950.itc", 0x27)

    label("loc_655")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66D")
    LoadChrToIndex("chr/ch00950.itc", 0x27)

    label("loc_66D")

    Return()

    # Function_3_60D end

    def Function_4_66E(): pass

    label("Function_4_66E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_688")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_4_66E")

    label("loc_688")

    Return()

    # Function_4_66E end

    def Function_5_689(): pass

    label("Function_5_689")

    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_5_689 end

    def Function_6_695(): pass

    label("Function_6_695")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51747.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("chr/ch05900.itc", 0x20)
    LoadChrToIndex("apl/ch51745.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    Call(0, 2)
    Call(0, 3)
    LoadChrToIndex("chr/ch03750.itc", 0x28)
    LoadChrToIndex("chr/ch03752.itc", 0x29)
    CreatePortrait(0, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu10800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02201.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    LoadEffect(0x0, "battle/cr037000.eff")
    LoadEffect(0x1, "battle/cr037001.eff")
    LoadEffect(0x2, "battle/cr034001.eff")
    LoadEffect(0x3, "event\\ev202_00.eff")
    LoadEffect(0x4, "event/ev17006.eff")
    LoadEffect(0x5, "event/ev17007.eff")
    LoadEffect(0x6, "event\\ev500_00.eff")
    LoadEffect(0x7, "event/ev17075.eff")
    LoadEffect(0x8, "battle/cr037101.eff")
    SoundLoad(3407)
    SoundLoad(3330)
    SoundLoad(2774)
    SoundLoad(2694)
    SoundLoad(3789)
    SoundLoad(3790)
    SoundLoad(3791)
    SoundLoad(3792)
    SoundLoad(3793)
    SoundLoad(3794)
    SoundLoad(3795)
    SoundLoad(3636)
    SoundLoad(3637)
    SoundLoad(3638)
    SoundLoad(3639)
    SoundLoad(3640)
    SoundLoad(3641)
    SoundLoad(3643)
    SoundLoad(3644)
    SoundLoad(3645)
    SoundLoad(961)
    SoundLoad(474)
    SetChrPos(0x101, 0, 0, -54500, 0)
    SetChrPos(0x102, 0, 0, -54500, 19)
    SetChrPos(0x104, 0, 0, -54500, 342)
    SetChrPos(0x103, 0, 0, -54500, 6)
    SetChrPos(0xF4, 0, 0, -54500, 332)
    SetChrPos(0xF5, 0, 0, -54500, 32)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x1E)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x4)
    Call(0, 43)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 0, 8000, -750, 180)
    PlayEffect(0x6, 0xFF, 0x9, 0x41, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -340, 2990, -5180, 180)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1190, 2990, -4720, 180)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x29)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -2029, 3000, -4860, 180)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-900, 1400, -28370, 0)
    MoveCamera(45, 36, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(70580, 0)
    OP_68(4380, 1400, -16990, 10000)
    MoveCamera(328, 11, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(51750, 10000)
    FadeToBright(1000, 0)
    PlaceName2(340, 40, "c_plac68", 0x0, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, -1100, 2500, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(43160, 0)
    OP_68(0, -1100, -52500, 5500)
    MoveCamera(0, 33, 0, 5500)
    OP_6E(700, 5500)
    SetCameraDistance(24050, 5500)
    OP_0D()
    OP_6F(0x79)
    Sound(920, 0, 100, 0)
    BeginChrThread(0x101, 0, 0, 7)
    Sleep(600)
    OP_6F(0x79)
    OP_68(0, 1200, -32450, 4500)
    MoveCamera(0, 5, 0, 4500)
    OP_6E(700, 4500)
    SetCameraDistance(32409, 4500)
    Sound(920, 0, 50, 0)
    BeginChrThread(0x102, 0, 0, 8)
    Sleep(600)
    Sound(920, 0, 100, 0)
    BeginChrThread(0x104, 0, 0, 9)
    Sleep(600)
    Sound(920, 0, 50, 0)
    BeginChrThread(0x103, 0, 0, 10)
    Sleep(600)
    Sound(920, 0, 100, 0)
    BeginChrThread(0xF4, 0, 0, 11)
    Sleep(600)
    Sound(920, 0, 50, 0)
    BeginChrThread(0xF5, 0, 0, 12)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 13)
    BeginChrThread(0x102, 0, 0, 14)
    BeginChrThread(0x103, 0, 0, 15)
    BeginChrThread(0x104, 0, 0, 16)
    BeginChrThread(0xF4, 0, 0, 17)
    BeginChrThread(0xF5, 0, 0, 18)
    Sleep(200)
    OP_68(0, 3400, -9700, 6800)
    OP_6E(700, 6800)
    SetCameraDistance(18350, 6800)
    Sleep(1000)
    MoveCamera(43, 8, 0, 5800)
    Sleep(3900)
    Sleep(350)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0001
    AnonymousTalk(
        0x8,
        "#40W你们来了啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0002
    AnonymousTalk(
        0xA,
        (
            "#3789V#40W#30A呵呵呵……欢迎。\x02\x03",

            "#3790V#47A欢迎来到世界的尽头，\x01",
            "一切因果律的中心。\x02",
        )
    )
    #Auto

    OP_6F(0x79)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_68(90, 5900, -740, 0)
    MoveCamera(25, 16, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(33110, 0)
    SetCameraDistance(31110, 3000)
    Fade(500)
    OP_0D()
    OP_6F(0x79)
    OP_68(90, 8600, -740, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    Fade(500)
    SetCameraDistance(12000, 10000)
    OP_0D()
    Sleep(500)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(800)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F8A")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E9C")

    #A0003
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#60A罗伊德……艾莉……\x01",
            "……缇欧……兰迪……\x02\x03",

            "#3637V#20A还有诺艾尔和瓦吉……\x07\x00\x02",
        )
    )
    #Auto

    OP_6F(0x79)
    CloseMessageWindow()
    Jump("loc_F85")

    label("loc_E9C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F12")

    #A0004
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#60A罗伊德……艾莉……\x01",
            "……缇欧……兰迪……\x02\x03",

            "#3638V#20A还有诺艾尔和莉夏……\x07\x00\x02",
        )
    )
    #Auto

    OP_6F(0x79)
    CloseMessageWindow()
    Jump("loc_F85")

    label("loc_F12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F85")

    #A0005
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#60A罗伊德……艾莉……\x01",
            "……缇欧……兰迪……\x02\x03",

            "#3639V#20A还有诺艾尔和达德利……\x07\x00\x02",
        )
    )
    #Auto

    OP_6F(0x79)
    CloseMessageWindow()

    label("loc_F85")

    Jump("loc_10E5")

    label("loc_F8A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1084")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_100E")

    #A0006
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#60A罗伊德……艾莉……\x01",
            "……缇欧……兰迪……\x02\x03",

            "#3640V#20A还有瓦吉和莉夏……\x07\x00\x02",
        )
    )
    #Auto

    OP_6F(0x79)
    CloseMessageWindow()
    Jump("loc_107F")

    label("loc_100E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_107F")

    #A0007
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#60A罗伊德……艾莉……\x01",
            "……缇欧……兰迪……\x02\x03",

            "#3641V#20A还有瓦吉和达德利……\x07\x00\x02",
        )
    )
    #Auto

    OP_6F(0x79)
    CloseMessageWindow()

    label("loc_107F")

    Jump("loc_10E5")

    label("loc_1084")


    #A0008
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#60A罗伊德……艾莉……\x01",
            "……缇欧……兰迪……\x02\x03",

            "#3642V#20A还有莉夏和达德利……\x07\x00\x02",
        )
    )
    #Auto

    OP_6F(0x79)
    CloseMessageWindow()

    label("loc_10E5")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    MoveCamera(0, 9, 0, 32000)
    SetMessageWindowPos(-1, 230, -1, -1)

    #C0009
    ChrTalk(
        0x101,
        "#00007F#3330V#5P#N#30W#15A琪雅……！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(30, 230, -1, -1)

    #C0010
    ChrTalk(
        0x103,
        (
            "#00214F#2694V#11P#N#30W#29A太好了……\x01",
            "你没事吧……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(200, 230, -1, -1)

    #C0011
    ChrTalk(
        0x104,
        "#00307F#2774V#5P#N#30W#22A阿琪，你没事吧！？\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(120, 230, -1, -1)

    #C0012
    ChrTalk(
        0x102,
        (
            "#00108F#3407V#11P#N#30W#26A真是的……！\x01",
            "让我们好担心……！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(800)
    Call(0, 44)
    BeginChrThread(0x9, 0, 0, 36)
    WaitChrThread(0x9, 0)

    #C0013
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12303F#3643V#5P#50W#20A………对不起…………\x02\x03",

            "#3644V#50A琪雅…#800W…#50W有许多事……\x01",
            "都没有告诉你们……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(200)
    BeginChrThread(0x9, 0, 0, 37)
    WaitChrThread(0x9, 0)

    #C0014
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#3645V#5P#47A#50W………一直瞒着你们……#800W…\x01",
            "#50W……欺骗你们，对不起……\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0015
    ChrTalk(
        0x101,
        (
            "#00007F#5P#N……不用道歉……！\x01",
            "也没必要感到内疚！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0016
    ChrTalk(
        0x103,
        (
            "#00207F#11P#N只要你平安无事，\x01",
            "我们就非常满足了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0017
    ChrTalk(
        0x104,
        (
            "#00307F#5P#N而且小孩子多少都会\x01",
            "对家长隐瞒一些事情，\x01",
            "这不是理所当然的吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0018
    ChrTalk(
        0x102,
        (
            "#00103F#11P#N利用这种理所当然的事\x01",
            "来蛊惑琪雅的人……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 2900, -9000, 0)
    MoveCamera(114, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14700, 0)
    Call(0, 43)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0019
    ChrTalk(
        0x102,
        (
            "#00107F#11P贝尔、伊安律师！\x01",
            "就是你们两个吧！？\x02",
        )
    )

    Sleep(200)

    def lambda_14B9():
        OP_A6(0xFE, 0x0, 0x19, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_14B9)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    CloseMessageWindow()
    OP_5A()
    Sleep(300)

    #C0020
    ChrTalk(
        0x8,
        "#02203F#5P嗯，正是。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "#10809F#5P呵呵呵……好凶哦。\x02\x03",

            "#10800F#5P但是我们已经\x01",
            "最大限度地尊重了\x01",
            "琪雅的意志哦。\x02\x03",

            "#10811F是这样吧？琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12303F#6P#N#30W……………………（点头）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0023
    ChrTalk(
        0x101,
        "#00010F#11P啧……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1604")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15E4")
    OP_FC(0xB)
    Jump("loc_15E7")

    label("loc_15E4")

    OP_FC(0xB)

    label("loc_15E7")


    #C0024
    ChrTalk(
        0x109,
        "#10101F#13P真会狡辩……\x02",
    )

    CloseMessageWindow()

    label("loc_1604")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1650")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_162E")
    OP_FC(0xB)
    Jump("loc_1631")

    label("loc_162E")

    OP_FC(0xB)

    label("loc_1631")


    #C0025
    ChrTalk(
        0x106,
        "#10701F#13P……太虚伪了。\x02",
    )

    CloseMessageWindow()

    label("loc_1650")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_167A")
    OP_FC(0xB)
    Jump("loc_167D")

    label("loc_167A")

    OP_FC(0xB)

    label("loc_167D")


    #C0026
    ChrTalk(
        0x105,
        (
            "#10406F#13P哎呀呀，\x01",
            "脸皮可真够厚的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16FD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16D1")
    OP_FC(0xB)
    Jump("loc_16D4")

    label("loc_16D1")

    OP_FC(0xB)

    label("loc_16D4")


    #C0027
    ChrTalk(
        0x10A,
        "#00601F#13P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_16FD")


    #C0028
    ChrTalk(
        0x104,
        (
            "#00301F#11P……总之，我们回去\x01",
            "之后再慢慢谈吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        (
            "#00204F#11P是呀，\x01",
            "要开个家庭会议。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0030
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12309F#6P#N#40W嘿嘿……呜……\x01",
            "……谢谢大家……\x02\x03",

            "#12302F可是琪雅……\x01",
            "不能离开这里……\x02\x03",

            "…………所以………………\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        "#00108F#11P琪雅……为什么？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00013F#11P……是不是有什么\x01",
            "关系到『至宝』之力的原因？\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Sleep(300)

    #C0033
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12308F#6P#6P#30W……………这个………………\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xA,
        (
            "#10804F#6P呵呵，琪雅，\x01",
            "不然就把真相告诉他们如何？\x02\x03",

            "#10811F让他们明白，你的所作所为，\x01",
            "全都是为了罗伊德警官他们。\x02",
        )
    )

    CloseMessageWindow()
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    #C0035
    ChrTalk(
        0x103,
        "#00205F#11P#30W哎……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        "#00305F#11P#30W……你说什么……\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    #C0037
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#6P#N#40W…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 3600, -9110, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12870, 0)
    SetCameraDistance(11870, 10000)
    Call(0, 44)
    OP_0D()
    Sleep(500)

    #C0038
    ChrTalk(
        0xA,
        (
            "#10800F#5P和过去的『幻之至宝』不同，\x01",
            "身为『零之至宝』的琪雅\x01",
            "同时具备『时』与『空』的力量。\x02\x03",

            "#10804F当干涉因果与认知的『幻』之力\x01",
            "与干涉时空的力量合而为一之时……\x02\x03",

            "#10811F琪雅就获得了\x01",
            "『编织世界的力量』。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#00011F#6P#N编、编织世界的力量……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B80")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B56")
    OP_FC(0xFFFA)
    Jump("loc_1B59")

    label("loc_1B56")

    OP_FC(0xFFF4)

    label("loc_1B59")


    #C0040
    ChrTalk(
        0x109,
        "#10111F#13P那、那到底是……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1BCB")

    label("loc_1B80")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BCB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BAA")
    OP_FC(0xFFFA)
    Jump("loc_1BAD")

    label("loc_1BAA")

    OP_FC(0xFFF4)

    label("loc_1BAD")


    #C0041
    ChrTalk(
        0x106,
        "#10712F#13P那究竟是……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1BCB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C23")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BF5")
    OP_FC(0xFFFA)
    Jump("loc_1BF8")

    label("loc_1BF5")

    OP_FC(0xFFF4)

    label("loc_1BF8")


    #C0042
    ChrTalk(
        0x105,
        (
            "#10401F#13P又在说些\x01",
            "非同寻常的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1C23")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C70")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C4D")
    OP_FC(0xFFFA)
    Jump("loc_1C50")

    label("loc_1C4D")

    OP_FC(0xFFF4)

    label("loc_1C50")


    #C0043
    ChrTalk(
        0x10A,
        "#00601F#13P怎么回事……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1C70")

    Sleep(300)

    #C0044
    ChrTalk(
        0x8,
        (
            "#02203F#11P这能力正是『碧零计划』的目的，\x01",
            "同时也是它的基础……\x02\x03",

            "#02201F『编织世界』──\x01",
            "亦即操纵因果律，\x01",
            "重塑世界的力量。\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0045
    ChrTalk(
        0x104,
        "#00305F#6P#N#4S啊……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0046
    ChrTalk(
        0x102,
        "#00101F#12P#N重、重塑世界……？\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()

    #C0047
    ChrTalk(
        0x103,
        (
            "#00208F#12P#N#30W……世间万象都具有\x01",
            "『因果系统』，交织成网络……\x02\x03",

            "#00201F难道是能对其过去、现在与未来的任意时刻\x01",
            "进行操作和变更的能力……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0048
    ChrTalk(
        0xA,
        (
            "#10809F#5P呵呵，不愧是缇欧，\x01",
            "这么快就理解了啊。\x02\x03",

            "#10800F没错，这种能力近似于\x01",
            "导力网络的最高级管理员\x01",
            "所拥有的权限。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#02201F#11P改变催生出纷争的现实，\x01",
            "将其替换为安定和平的现实……\x02\x03",

            "#02203F比如说，消除克洛斯贝尔从属于帝国和共和国，\x01",
            "被其玩弄于股掌之中的现实……\x02\x03",

            "#02200F并将其改写为克洛斯贝尔以『宗主国』的\x01",
            "身份凌驾在两国之上的现实。\x01",
            "从原理上来说，连这都是可以实现的。\x02",
        )
    )

    CloseMessageWindow()
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0050
    ChrTalk(
        0x101,
        "#00007F#6P#N………什么…………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_210A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20E7")
    OP_FC(0xFFFA)
    Jump("loc_20EA")

    label("loc_20E7")

    OP_FC(0xFFF4)

    label("loc_20EA")


    #C0051
    ChrTalk(
        0x109,
        "#10101F#13P那、那个……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_210A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2155")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2134")
    OP_FC(0xFFFA)
    Jump("loc_2137")

    label("loc_2134")

    OP_FC(0xFFF4)

    label("loc_2137")


    #C0052
    ChrTalk(
        0x10A,
        "#00610F#13P荒、荒唐……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2155")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_217F")
    OP_FC(0xFFFA)
    Jump("loc_2182")

    label("loc_217F")

    OP_FC(0xFFF4)

    label("loc_2182")


    #C0053
    ChrTalk(
        0x106,
        "#10706F#13P……不可能……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_21A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2204")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21CC")
    OP_FC(0xFFFA)
    Jump("loc_21CF")

    label("loc_21CC")

    OP_FC(0xFFF4)

    label("loc_21CF")


    #C0054
    ChrTalk(
        0x105,
        (
            "#10410F#13P……那恐怕是连女神\x01",
            "都做不到的事……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2204")


    #C0055
    ChrTalk(
        0x104,
        (
            "#00307F#6P#N喂喂，再怎么说，\x01",
            "这也太荒唐无稽了吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0056
    ChrTalk(
        0x102,
        (
            "#00106F#12P#N……这实在是……\x01",
            "令人难以置信。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0057
    ChrTalk(
        0xA,
        (
            "#10809F#5P嘻嘻……\x01",
            "你们这样说就太奇怪了吧？\x02\x03",

            "#10811F毕竟你们也曾被\x01",
            "这种能力救过一次呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)

    #C0058
    ChrTalk(
        0x104,
        "#00305F#6P#N哎……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0059
    ChrTalk(
        0x102,
        "#00105F#12P#N被、被救过……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0060
    ChrTalk(
        0x103,
        (
            "#00201F#12P#N……难道……\x01",
            "………是刚才看见的………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00010F#6P#N几个月前，潜入\x01",
            "教团据点那时的……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis293.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis295.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis333.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(500)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis334.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)
    CreatePortrait(0, 65296, 65408, 240, 128, 240, 136, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis346.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(800)
    VolumeBGM(0x3C, 0x3E8)
    FadeToDark(0, 16777215, -1)
    OP_CB(0x0, 0x1, 0x47E, 0x47E, 0x5DC, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    Sound(3044, 255, 100, 0)    #voice#KeA
    Sleep(1500)
    BeginChrThread(0xF, 1, 0, 45)
    Sleep(2000)
    CreatePortrait(1, 65296, 65408, 240, 128, 240, 136, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis297.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x1, 0x41A, 0x41A, 0x0, 0x0)
    OP_CB(0x1, 0x1, 0x3E8, 0x3E8, 0x5DC, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0x0, 0x0)
    FadeToBright(0, 16777215)
    Sleep(1500)
    StopSound(474, 2000, 90)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    VolumeBGM(0x64, 0x3E8)

    #C0062
    ChrTalk(
        0x101,
        "#00011F#6P#N#50W……………啊………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0063
    ChrTalk(
        0xA,
        (
            "#10800F#5P呵呵，看来罗伊德警官\x01",
            "已经『想起来』了呢。\x02\x03",

            "#10804F虽然规模很小，但现实\x01",
            "已经有过一次改变了。\x02\x03",

            "#10811F那就是你们被失控的\x01",
            "约亚西姆杀死这个现实。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        "#00108F#12P#N#30W……………………………………\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()

    #C0065
    ChrTalk(
        0x104,
        "#00311F#6P#N#30W…………这是……真的吗……？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(0, 8700, 0, 0)
    MoveCamera(354, 2, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(13000, 4500)
    OP_0D()
    Sleep(300)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)
    Sleep(500)
    BeginChrThread(0x9, 0, 0, 38)
    WaitChrThread(0x9, 0)

    #C0066
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#11P#30W一开始……你们和\x01",
            "艾丝蒂尔他们，还有那个叫玲的孩子\x01",
            "并没有那么要好……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    BeginChrThread(0x9, 0, 0, 39)
    Sleep(300)
    WaitChrThread(0x9, 0)

    #C0067
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12308F#11P因此只有你们四个人潜入了那里……\x01",
            "……玲也没有来帮忙，结果……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 0, 0, 40)
    WaitChrThread(0x9, 0)

    #C0068
    ChrTalk(
        0xA,
        (
            "#10800F#5P『得知』此事的琪雅\x01",
            "爆发了『至宝』的力量，\x01",
            "干涉了过去的因果律。\x02\x03",

            "#10804F其结果就是，你们在引导之下，\x01",
            "解决了『歼灭天使』的问题……\x02\x03",

            "经过一番机缘巧合，利贝尔的两位游击士\x01",
            "现身帮助你们……\x02\x03",

            "#10811F最后，在你们本该被杀的场面下，\x01",
            "『歼灭天使』前来助阵了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 3600, -9110, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11870, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B94")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B68")
    OP_FC(0xFFFA)
    Jump("loc_2B6B")

    label("loc_2B68")

    OP_FC(0xFFF4)

    label("loc_2B6B")


    #C0069
    ChrTalk(
        0x109,
        "#10110F#13P竟、竟有这种事……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2C3D")

    label("loc_2B94")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BBE")
    OP_FC(0xFFFA)
    Jump("loc_2BC1")

    label("loc_2BBE")

    OP_FC(0xFFF4)

    label("loc_2BC1")


    #C0070
    ChrTalk(
        0x106,
        "#10708F#13P……竟有这种事……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2C3D")

    label("loc_2BEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C3D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C14")
    OP_FC(0xFFFA)
    Jump("loc_2C17")

    label("loc_2C14")

    OP_FC(0xFFF4)

    label("loc_2C17")


    #C0071
    ChrTalk(
        0x10A,
        "#00610F#13P……竟然有这种事……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2C3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CA2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C67")
    OP_FC(0xFFFA)
    Jump("loc_2C6A")

    label("loc_2C67")

    OP_FC(0xFFF4)

    label("loc_2C6A")


    #C0072
    ChrTalk(
        0x105,
        (
            "#10403F#13P……但是……\x01",
            "似乎并非信口开河。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2D6B")

    label("loc_2CA2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D0B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CCC")
    OP_FC(0xFFFA)
    Jump("loc_2CCF")

    label("loc_2CCC")

    OP_FC(0xFFF4)

    label("loc_2CCF")


    #C0073
    ChrTalk(
        0x10A,
        (
            "#00606F#13P……但是……\x01",
            "似乎并不是信口开河啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2D6B")

    label("loc_2D0B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D6B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D35")
    OP_FC(0xFFFA)
    Jump("loc_2D38")

    label("loc_2D35")

    OP_FC(0xFFF4)

    label("loc_2D38")


    #C0074
    ChrTalk(
        0x106,
        (
            "#10703F#13P……但是……\x01",
            "好像并非信口开河。\x02",
        )
    )

    OP_5A()
    OP_57(0x0)
    OP_5A()

    label("loc_2D6B")

    Sleep(300)

    #C0075
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#5P#N#30W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0076
    ChrTalk(
        0xA,
        (
            "#10804F#5P呵呵……想必给你们\x01",
            "造成了不小的打击吧？\x02\x03",

            "#10800F然而，这还不是『零之至宝』所拥有的\x01",
            "『改变现实之力』的真髓！\x02\x03",

            "回避你们的悲剧这种小事，\x01",
            "仅仅是个序幕而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-1230, 7300, -3350, 0)
    MoveCamera(20, 3, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(43820, 0)
    MoveCamera(340, 4, 0, 45000)
    Call(0, 43)
    OP_0D()
    Sleep(1000)

    #C0077
    ChrTalk(
        0xA,
        (
            "#10804F#5P只要凭借这棵『碧之大树』……\x02\x03",

            "这棵可以使琪雅的力量产生增幅，\x01",
            "通过七耀脉连接\x01",
            "整个世界的神树……\x02\x03",

            "#10811F#5P别说是回避小小的悲剧，\x01",
            "即使想改变律师刚才所说的\x01",
            "那种重大现实，也是可能的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0078
    ChrTalk(
        0x101,
        "#00013F#6P#N……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0079
    ChrTalk(
        0x103,
        "#00201F#12P#N这就是『大树』的力量……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0080
    ChrTalk(
        0x104,
        (
            "#00310F#6P#N……喂喂……\x01",
            "这可不是开玩笑的啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3056")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3012")
    OP_FC(0xFFFA)
    Jump("loc_3015")

    label("loc_3012")

    OP_FC(0xFFF4)

    label("loc_3015")


    #C0081
    ChrTalk(
        0x105,
        (
            "#10408F#13P（……是吗……\x01",
            "  与真正的『始源之地』相同……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3056")


    #C0082
    ChrTalk(
        0xA,
        (
            "#10802F#5P#30W呵呵……很棒吧？\x02\x03",

            "#10809F有了这么棒的东西，\x01",
            "我们就无所畏惧了……！\x02\x03",

            "可以为全世界带来幸福，\x01",
            "不会再有任何悲哀！\x02\x03",

            "人类将从各种不安中解脱，\x01",
            "从此一心追求『良善』！\x02\x03",

            "#10811F这正是炼金术的奥义，\x01",
            "伟大的秘法啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0083
    ChrTalk(
        0x102,
        "#00101F#6P#N贝尔……你……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0084
    ChrTalk(
        0x101,
        "#00008F#6P#N……………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(0, 3600, -9110, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12870, 0)
    Call(0, 44)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0085
    ChrTalk(
        0x101,
        (
            "#00003F#6P#N伊安律师。\x02\x03",

            "#00013F这样真的好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0086
    ChrTalk(
        0x8,
        "#02201F#11P#30W……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 26)
    WaitChrThread(0x8, 0)
    Sleep(500)

    #C0087
    ChrTalk(
        0x8,
        (
            "#02211F#11P……任何事情都需要未雨绸缪。\x02\x03",

            "人类的历史，也正是\x01",
            "对抗各种风险的历史……\x02\x03",

            "而琪雅拥有可以控制\x01",
            "那些风险的神奇力量……\x02\x03",

            "这是无可否认的『事实』。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00006F#6P#N所以呢？即使把琪雅\x01",
            "囚禁在这种地方也在所不惜……？\x02\x03",

            "#00008F听说过去的『幻之至宝』\x01",
            "最终心神崩溃，\x01",
            "并选择了自我消灭。\x02\x03",

            "#00013F你们真的……\x01",
            "打算将这样的重责\x01",
            "推给一个小女孩吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0089
    ChrTalk(
        0x8,
        "#02211F#11P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12300F#5P#N罗伊德，这……\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0091
    ChrTalk(
        0xA,
        (
            "#10800F#5P呵呵呵，正是为了避免那种情况的发生，\x01",
            "才需要我们的存在呀。\x02\x03",

            "#10804F我们不会将改变世界的责任\x01",
            "全部推给琪雅……\x02\x03",

            "而是让律师这样的有识之士\x01",
            "指引方向，提供建议，从而使\x01",
            "世界向『更正确的方向』发展……\x02\x03",

            "#10802F如果是这样，那就另当别论了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        "#00005F#6P#N…………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0093
    ChrTalk(
        0x102,
        (
            "#00107F#12P#N你、你们要完全取消\x01",
            "民主讨论的步骤吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0094
    ChrTalk(
        0x8,
        (
            "#02203F#11P……艾莉，你应该也很清楚\x01",
            "民主制度的弊端。\x02\x03",

            "这种制度往往会造成群愚政治，\x01",
            "在关键时刻也无法\x01",
            "迅速做出决断……\x02\x03",

            "#02201F不仅是克洛斯贝尔，\x01",
            "这不是随处可见的现实吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        "#00108F#12P#N#30W……这……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0096
    ChrTalk(
        0x8,
        (
            "#02200F#11P而且我并不打算仅凭自己的见识\x01",
            "给琪雅指引方向。\x02\x03",

            "#02203F终归还是要请求麦克道尔议长\x01",
            "这样的有识之士来提供协助。\x02\x03",

            "迪塔应该也能\x01",
            "从管理的角度\x01",
            "帮上忙吧。\x02\x03",

            "#02200F另外，希望你们也能对\x01",
            "我们的这次尝试进行协助。\x02",
        )
    )

    CloseMessageWindow()
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0097
    ChrTalk(
        0x8,
        (
            "#02203F#11P要开拓新时代，\x01",
            "你们这些年轻人的意见也是必须的。\x02\x03",

            "#02201F而且……\x02\x03",

            "既然你们能够前进到这里，\x01",
            "对于今后的时代需要什么，\x01",
            "自然有着切身体会。\x02\x03",

            "#02200F这个提议怎么样？\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        "#00208F#12P#N#30W………这、这…………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0099
    ChrTalk(
        0x104,
        (
            "#00310F#6P#N#30W可恶……\x01",
            "好像很有说服力啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0100
    ChrTalk(
        0x101,
        "#00008F#6P#N#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopBGM(0x1388)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_6F(0x79)
    Sleep(500)

    #C0101
    ChrTalk(
        0x101,
        (
            "#00006F#6P#N……伊安律师。\x02\x03",

            "#00003F我刚才的提问，\x01",
            "您直到现在都没有回答。\x02\x03",

            "#00001F#6P#N律师您……\x01",
            "真的觉得这样好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7543", 0)
    SetCameraDistance(11870, 10000)
    Sleep(500)

    #C0102
    ChrTalk(
        0x101,
        (
            "#00003F#6P#N#30W万事万物都有『尊严』。\x02\x03",

            "无论是人类、社会，还是历史。\x02\x03",

            "#00008F虽然我们有时会走上错误的道路，\x01",
            "造成一些悲剧……\x02\x03",

            "#00013F但如果将其抹消，\x01",
            "便会侵犯与其相关的人们的『尊严』。\x02\x03",

            "#00006F比如说，那些从悲剧中重新振作，\x01",
            "并变得更加坚强的人……\x02\x03",

            "#00002F律师……\x01",
            "其实您也明白吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0103
    ChrTalk(
        0x8,
        "#02211F#11P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(150)

    #C0104
    ChrTalk(
        0x102,
        "#00102F#12P#N#30W罗伊德……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BA4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B50")
    OP_FC(0xFFFA)
    Jump("loc_3B53")

    label("loc_3B50")

    OP_FC(0xFFF4)

    label("loc_3B53")


    #C0105
    ChrTalk(
        0x10A,
        (
            "#00606F#13P#30W的确……\x01",
            "任何人都会犯错，不可能\x01",
            "永远都做出正确行动……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3C75")

    label("loc_3BA4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C0C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BCE")
    OP_FC(0xFFFA)
    Jump("loc_3BD1")

    label("loc_3BCE")

    OP_FC(0xFFF4)

    label("loc_3BD1")


    #C0106
    ChrTalk(
        0x109,
        (
            "#10106F#13P#30W的确……\x01",
            "人难免会犯下\x01",
            "一些错误。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3C75")

    label("loc_3C0C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C75")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C36")
    OP_FC(0xFFFA)
    Jump("loc_3C39")

    label("loc_3C36")

    OP_FC(0xFFF4)

    label("loc_3C39")


    #C0107
    ChrTalk(
        0x106,
        (
            "#10708F#13P#30W……的确……\x01",
            "人难免会犯下\x01",
            "各种错误……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3C75")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CEB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C9F")
    OP_FC(0xFFFA)
    Jump("loc_3CA2")

    label("loc_3C9F")

    OP_FC(0xFFF4)

    label("loc_3CA2")


    #C0108
    ChrTalk(
        0x105,
        (
            "#10401F#13P#30W然而，如果将这些\x01",
            "错误抹消，\x01",
            "人也就无法成长……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3DD2")

    label("loc_3CEB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D61")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D15")
    OP_FC(0xFFFA)
    Jump("loc_3D18")

    label("loc_3D15")

    OP_FC(0xFFF4)

    label("loc_3D18")


    #C0109
    ChrTalk(
        0x106,
        (
            "#10701F#13P#30W但是，如果将这些\x01",
            "错误抹消，\x01",
            "人也就无法成长……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3DD2")

    label("loc_3D61")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DD2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D8B")
    OP_FC(0xFFFA)
    Jump("loc_3D8E")

    label("loc_3D8B")

    OP_FC(0xFFF4)

    label("loc_3D8E")


    #C0110
    ChrTalk(
        0x109,
        (
            "#10101F#13P#30W但是，如果将这些\x01",
            "错误抹消，\x01",
            "人永远都无法成长。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3DD2")


    #C0111
    ChrTalk(
        0x103,
        (
            "#00204F#12P#N#30W……共同学习、齐心协力、\x01",
            "勇往直前……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0112
    ChrTalk(
        0x104,
        (
            "#00300F#6P#N#30W这些积极行为的意义，\x01",
            "都将被完全丢弃。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0113
    ChrTalk(
        0x8,
        "#02211F#11P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 5500, -6020, 0)
    MoveCamera(151, 30, 0, 0)
    MoveCamera(139, 30, 0, 20000)
    OP_6E(700, 0)
    SetCameraDistance(17340, 0)
    Call(0, 43)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1000)
    OP_93(0x102, 0x0, 0x0)
    OP_0D()
    Sleep(300)

    #C0114
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12305F#5P#N#30W…………罗伊德………………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00004F#11P琪雅，\x01",
            "和我们一起回去吧。\x02\x03",

            "#00000F你没有必要为了我们\x01",
            "而继续勉强自己。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#5P#N…………………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0117
    ChrTalk(
        0x101,
        (
            "#00008F#11P……在我们\x01",
            "一度死去的那个时候……\x02\x03",

            "你一定感到非常难过、\x01",
            "痛苦和悲伤吧……\x02\x03",

            "#00006F对不起，琪雅，\x01",
            "都怪我们太没用……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12301F#5P#N#30W没、没有那回事……！\x02\x03",

            "#12313F……是琪雅\x01",
            "擅自那么做的……！\x02\x03",

            "所以罗伊德不用道歉！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0119
    ChrTalk(
        0x101,
        (
            "#00003F#11P如果是这样，琪雅……\x02\x03",

            "#00013F你为什么总是\x01",
            "露出那副忧郁的表情？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0120
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12305F#5P#N……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0121
    ChrTalk(
        0x101,
        (
            "#00006F#11P琪雅，你应该也发觉了吧？\x02\x03",

            "#00008F由于你对我们的死亡\x01",
            "感到极度悲伤，\x01",
            "于是便操纵因果律，改变了现实……\x02\x03",

            "#00013F这种行为……\x01",
            "其实根本就是『作弊』。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#5P#N#40W……………啊………………\x02\x03",

            "#12308F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0123
    ChrTalk(
        0x103,
        "#00208F#11P……琪雅………\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#00306F#11P嗯，虽然被人杀死\x01",
            "实在不能算是好结局……\x02\x03",

            "#00300F但再怎么说，复活\x01",
            "终究是『犯规』的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 3500, -9100, 0)
    MoveCamera(125, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12860, 0)
    OP_0D()
    Sleep(300)

    #C0125
    ChrTalk(
        0x102,
        (
            "#00106F#11P伊安律师、贝尔……\x02\x03",

            "关于这一点……\x01",
            "在『政治』中也是一样的。\x02\x03",

            "#00108F有些时候，光走正路是不够的，\x01",
            "确实需要采取一些歪门手段。\x02\x03",

            "#00101F但是，如果以歪门手段为前提，\x01",
            "必然是错误的做法。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        "#02201F#5P………艾莉……………\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        "#10801F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x102,
        (
            "#00103F#11P依靠小琪雅个人的\x01",
            "超自然力量……\x02\x03",

            "这已经不是政治手段，\x01",
            "而是单纯的依靠神明了。\x02\x03",

            "#00108F我认为，只有通过正当的方法\x01",
            "与对话沟通的形式来渡过难关，\x01",
            "并依靠社会全员来解决问题……\x02\x03",

            "#00101F才能算是『真正的政治』。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00006F#11P如果没有琪雅的力量，\x01",
            "克洛斯贝尔很可能会\x01",
            "面临严重的危机。\x02\x03",

            "#00008F席卷整个大陆的混乱，严重经济危机……\x01",
            "而且，帝国的内战一旦结束，\x01",
            "必定会对克洛斯贝尔露出獠牙。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(170, 3500, -8850, 800)
    OP_9B(0x1, 0x101, 0x0, 0xC8, 0x1F4, 0x0)
    Sound(33, 0, 100, 0)
    Sound(48, 0, 50, 0)
    OP_6F(0x79)
    Sleep(300)

    #C0130
    ChrTalk(
        0x101,
        (
            "#00013F#11P但即使如此，\x01",
            "我也不认为将一切都推给琪雅\x01",
            "就是正确的选择。\x02\x03",

            "#00004F如果一味仰赖别人赐予的奇迹，\x01",
            "我们自身就永远无法成长……\x02\x03",

            "#00000F所以，即使要承受各种痛苦……\x01",
            "如今也应该贯彻『常理』。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0131
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12312F#5P#N#30W……………罗伊德………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    #C0132
    ChrTalk(
        0x8,
        "#02203F#5P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x8, 0x21)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrSubChip(0x8, 0x13)
    OP_68(0, 3600, -9110, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11870, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(700)

    #C0133
    ChrTalk(
        0x8,
        "#02211F#11P#40W………到此为止了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 28)
    WaitChrThread(0x8, 0)
    Sleep(500)

    #C0134
    ChrTalk(
        0x8,
        (
            "#02203F#11P#40W我原以为……自己的所作所为\x01",
            "并不是为了私怨……\x02\x03",

            "但终究……\x01",
            "还是自欺欺人啊。\x02\x03",

            "#02200F……感觉就像是\x01",
            "被盖伊说服了一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#00008F#6P#N……律师……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0136
    ChrTalk(
        0x8,
        (
            "#02203F#11P#40W……抱歉，\x01",
            "我没资格对你说这种话。\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-1050, 4800, -5300, 0)
    MoveCamera(41, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17330, 0)
    OP_0D()
    TurnDirection(0x8, 0x9, 500)
    Sleep(300)

    #C0137
    ChrTalk(
        0x8,
        (
            "#02203F#11P#30W……琪雅，对你说了诸多\x01",
            "蛊惑之言，非常抱歉。\x02\x03",

            "#02201F你就通过自己的判断……\x01",
            "来决定接下来该怎么做吧。\x02\x03",

            "#02202F我相信你已经可以做到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12312F#5P#N#30W……律师………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x8, 0xA, 500)
    Sleep(300)

    #C0139
    ChrTalk(
        0x8,
        (
            "#02203F#11P#30W玛丽亚贝尔小姐……\x01",
            "辜负了你的期待，实在抱歉。\x02\x03",

            "#02201F看样子，我也该退场了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)
    Sleep(150)

    #C0140
    ChrTalk(
        0xA,
        (
            "#10804F#6P呵呵呵……没关系。\x02\x03",

            "原本也只是请您\x01",
            "为此项计划做个\x01",
            "综合设计而已。\x02\x03",

            "#10811F一直以来，真是辛苦您了，律师。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    MoveCamera(63, 16, 0, 0)
    SetCameraDistance(13750, 0)
    SetCameraDistance(13000, 1500)
    SetChrPos(0xA, -2000, 3000, -4850, 90)
    SetChrPos(0x8, 0, 3000, -5850, 270)
    OP_0D()
    OP_93(0xC, 0x5A, 0x0)
    Sleep(300)

    def lambda_4AA9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_4AA9)
    BeginChrThread(0xC, 3, 0, 33)
    Sleep(250)

    def lambda_4AC3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4AC3)
    WaitChrThread(0xA, 2)
    OP_6F(0x79)
    Sleep(150)
    BeginChrThread(0xA, 0, 0, 29)
    Sleep(350)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x7D0)
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 30)
    OP_68(5000, 3200, -8150, 1000)
    MoveCamera(100, 12, 0, 1000)
    SetCameraDistance(22300, 1000)
    WaitChrThread(0xA, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(500)

    def lambda_4BEC():

        label("loc_4BEC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4BEC")

    QueueWorkItem2(0x101, 2, lambda_4BEC)

    def lambda_4BFE():

        label("loc_4BFE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4BFE")

    QueueWorkItem2(0x102, 2, lambda_4BFE)

    def lambda_4C10():

        label("loc_4C10")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4C10")

    QueueWorkItem2(0x103, 2, lambda_4C10)

    def lambda_4C22():

        label("loc_4C22")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4C22")

    QueueWorkItem2(0x104, 2, lambda_4C22)

    def lambda_4C34():

        label("loc_4C34")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4C34")

    QueueWorkItem2(0xF4, 2, lambda_4C34)

    def lambda_4C46():

        label("loc_4C46")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4C46")

    QueueWorkItem2(0xF5, 2, lambda_4C46)
    WaitChrThread(0x8, 0)

    #C0141
    ChrTalk(
        0x8,
        "#02212F#11P#10A……呜……\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)

    #C0142
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12313F#N！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0143
    ChrTalk(
        0x101,
        "#00007F#12P#N什么……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0144
    ChrTalk(
        0x102,
        "#00107F#12P#N……贝尔……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7585", 0)
    Fade(500)
    OP_68(4920, 3700, -12390, 0)
    MoveCamera(59, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(7630, 0)
    SetChrPos(0xA, -90, 3000, -5290, 180)
    SetChrPos(0x8, 9400, 700, -9900, 270)
    BeginChrThread(0x8, 0, 0, 31)
    SetCameraDistance(5610, 5000)
    OP_0D()
    Sleep(1000)

    #C0145
    ChrTalk(
        0x8,
        (
            "#02213F#11P#60W……哈哈……\x01",
            "……这也是……因果报应吧……\x02\x03",

            "#70W盖伊……罗伊德……\x01",
            "………对不……起………\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 32)
    WaitChrThread(0x8, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    Sleep(300)

    #C0146
    ChrTalk(
        0x103,
        "#00207F#5P伊安律师……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E31")

    #C0147
    ChrTalk(
        0x10A,
        "#00610F#5P你竟然……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E90")

    label("loc_4E31")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E62")

    #C0148
    ChrTalk(
        0x109,
        "#10110F#5P你居然……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E90")

    label("loc_4E62")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E90")

    #C0149
    ChrTalk(
        0x106,
        "#10707F#5P……你居然……\x02",
    )

    CloseMessageWindow()

    label("loc_4E90")

    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-460, 3700, -1780, 0)
    MoveCamera(353, 8, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16600, 0)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xA, 0x1000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xC, 0x80)

    def lambda_4EFD():
        TurnDirection(0x101, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4EFD)
    Sleep(0)

    def lambda_4F0D():
        TurnDirection(0x102, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4F0D)
    Sleep(0)

    def lambda_4F1D():
        TurnDirection(0x103, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4F1D)
    Sleep(0)

    def lambda_4F2D():
        TurnDirection(0x104, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4F2D)
    Sleep(0)

    def lambda_4F3D():
        TurnDirection(0xF4, 0xA, 0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_4F3D)
    Sleep(0)

    def lambda_4F4D():
        TurnDirection(0xF5, 0xA, 0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_4F4D)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_0D()
    Sleep(300)

    #C0150
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#12P贝尔……为什么要……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xA,
        (
            "#10804F#5P呵呵呵，没用的道具\x01",
            "就要处理掉，仅此而已。\x02\x03",

            "#10811F从这层意义上来说，琪雅……\x01",
            "你也不例外哦！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x29)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 3, 0, 33)
    WaitChrThread(0xA, 3)
    Sound(686, 0, 80, 0)
    PlayEffect(0x8, 0x6, 0xA, 0x1, 250, 2200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Fade(500)
    OP_68(0, 8600, -740, 0)
    MoveCamera(354, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15100, 0)
    SetCameraDistance(16650, 4000)
    Call(0, 44)
    SetChrPos(0x9, 300, 8400, -3000, 180)
    OP_0D()
    PlayEffect(0x7, 0xFF, 0x9, 0x1, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(283, 0, 100, 0)
    Sound(961, 2, 70, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)
    BeginChrThread(0x9, 0, 0, 41)
    WaitChrThread(0x9, 0)

    #C0152
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12311F#3646V#5P#50W#18A……呜啊啊……！！\x02",
        )
    )
    #Auto

    Sleep(500)
    OP_82(0x32, 0x0, 0x7D0, 0x320)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    StopEffect(0x6, 0x2)
    BeginChrThread(0x9, 0, 0, 42)
    WaitChrThread(0x9, 0)

    #C0153
    ChrTalk(
        0x101,
        "#00007F#5P琪雅……！？\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            "#00310F#5P喂……！\x01",
            "你在对我们的孩子做什么！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 0)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)

    #C0155
    ChrTalk(
        0xA,
        (
            "#10804F#5P呵呵，你要是再迷茫下去，\x01",
            "我就只能让你变成没有意志的\x01",
            "可爱人偶了……\x02\x03",

            "#10811F你原本就是依靠库罗伊斯家族的秘术\x01",
            "而获得生命的人造人……\x02\x03",

            "想怎么处置，\x01",
            "全都随我高兴哟～\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        "#00010F#5P开、开什么玩笑……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0157
    ChrTalk(
        0x102,
        (
            "#00107F#11P贝尔……！\x01",
            "你说得太过分了吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0158
    ChrTalk(
        0x103,
        "#00207F#5P……请你撤回前言……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopBGM(0xBB8)
    StopSound(961, 3000, 60)
    Fade(500)
    OP_68(200, 2700, -9200, 0)
    MoveCamera(359, 4, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(15330, 0)
    SetCameraDistance(12330, 42000)
    OP_0D()
    BeginChrThread(0x101, 0, 0, 20)
    BeginChrThread(0x102, 0, 0, 21)
    BeginChrThread(0x103, 0, 0, 22)
    BeginChrThread(0x104, 0, 0, 23)
    BeginChrThread(0xF4, 0, 0, 24)
    BeginChrThread(0xF5, 0, 0, 25)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7458", 0)
    CreatePortrait(0, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu10802.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0159
    AnonymousTalk(
        0xA,
        (
            "#3791V#40W#42A呵呵呵呵……好吧。\x02\x03",

            "#3792V#25A我是玛丽亚贝尔·库罗伊斯。\x02\x03",

            "#3793V#50A追求超越女神的『至宝』，\x01",
            "为此不惜一切代价的一族之后裔。\x02\x03",

            "#3794V#70A这积累千年的执念，\x01",
            "与你们那未满一年的羁绊，\x01",
            "究竟孰强孰弱……\x02\x03",

            "#3795V#35A不如就拼死一战，\x01",
            "比较一下如何？\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0160
    ChrTalk(
        0x101,
        "#00007F#6P#30W#17A……求之不得！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0161
    ChrTalk(
        0x102,
        (
            "#00107F#12P#30W#25A#N贝尔……！\x01",
            "我不会手下留情的！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5622")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55D4")
    OP_FC(0x6)
    Jump("loc_55D7")

    label("loc_55D4")

    OP_FC(0xC)

    label("loc_55D7")


    #C0162
    ChrTalk(
        0x105,
        (
            "#10407F#13P#30W#37A#N认定为最高等级的魔导师……！\x01",
            "开始全力压制！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_5703")

    label("loc_5622")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5696")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_564C")
    OP_FC(0x6)
    Jump("loc_564F")

    label("loc_564C")

    OP_FC(0xC)

    label("loc_564F")


    #C0163
    ChrTalk(
        0x106,
        (
            "#10707F#13P#30W#38A#N感知到了漆黑的法力……！\x01",
            "准备全力降服！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_5703")

    label("loc_5696")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5703")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56C0")
    OP_FC(0x6)
    Jump("loc_56C3")

    label("loc_56C0")

    OP_FC(0xC)

    label("loc_56C3")


    #C0164
    ChrTalk(
        0x109,
        (
            "#10107F#13P#30W#37A#N推定危险度为Ｓ级……！\x01",
            "以全火力迎击！\x02",
        )
    )
    #Auto

    CloseMessageWindow()

    label("loc_5703")

    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 0)
    OP_24(0x1DA)
    OP_24(0x3C1)
    Battle("BattleInfo_2C0", 0x30200011, 0x0, 0x100, 0x41, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 46)
    Return()

    # Function_6_695 end

    def Function_7_5731(): pass

    label("Function_7_5731")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5770():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5770)
    OP_9B(0x0, 0xFE, 0x0, 0x128E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_7_5731 end

    def Function_8_579B(): pass

    label("Function_8_579B")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_57DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_57DA)
    OP_9B(0x0, 0xFE, 0x0, 0x10FE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x155, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_8_579B end

    def Function_9_5805(): pass

    label("Function_9_5805")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5844():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5844)
    OP_9B(0x0, 0xFE, 0x0, 0x1036, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x12, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_9_5805 end

    def Function_10_586F(): pass

    label("Function_10_586F")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_58AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_58AE)
    OP_9B(0x0, 0xFE, 0x0, 0xD48, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x162, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_10_586F end

    def Function_11_58D9(): pass

    label("Function_11_58D9")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5918():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5918)
    OP_9B(0x0, 0xFE, 0x0, 0xB22, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1C, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_11_58D9 end

    def Function_12_5943(): pass

    label("Function_12_5943")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5982():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5982)
    OP_9B(0x0, 0xFE, 0x0, 0xC4E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x148, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_12_5943 end

    def Function_13_59AD(): pass

    label("Function_13_59AD")

    OP_95(0xFE, 0, 1000, -12060, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_59AD end

    def Function_14_59C9(): pass

    label("Function_14_59C9")

    Sleep(50)
    OP_95(0xFE, 1120, 1000, -13300, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_59C9 end

    def Function_15_59E8(): pass

    label("Function_15_59E8")

    Sleep(100)
    OP_95(0xFE, 420, 1000, -14370, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_15_59E8 end

    def Function_16_5A07(): pass

    label("Function_16_5A07")

    Sleep(150)
    OP_95(0xFE, -1270, 1000, -13930, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_5A07 end

    def Function_17_5A26(): pass

    label("Function_17_5A26")

    Sleep(200)
    OP_95(0xFE, -2540, 1990, -13310, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_5A26 end

    def Function_18_5A45(): pass

    label("Function_18_5A45")

    Sleep(250)
    OP_95(0xFE, 2540, 1000, -13510, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_18_5A45 end

    def Function_19_5A64(): pass

    label("Function_19_5A64")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_19_5A64 end

    def Function_20_5A76(): pass

    label("Function_20_5A76")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_5A76 end

    def Function_21_5A85(): pass

    label("Function_21_5A85")

    Sleep(100)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_5A85 end

    def Function_22_5A97(): pass

    label("Function_22_5A97")

    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_5A97 end

    def Function_23_5AA9(): pass

    label("Function_23_5AA9")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_5AA9 end

    def Function_24_5AB5(): pass

    label("Function_24_5AB5")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5AD5")
    Sound(540, 0, 50, 0)
    Jump("loc_5AFA")

    label("loc_5AD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5AFA")
    Sound(531, 0, 100, 0)

    label("loc_5AFA")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_5AB5 end

    def Function_25_5B03(): pass

    label("Function_25_5B03")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B23")
    Sound(540, 0, 50, 0)
    Jump("loc_5B48")

    label("loc_5B23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B48")
    Sound(531, 0, 100, 0)

    label("loc_5B48")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_5B03 end

    def Function_26_5B51(): pass

    label("Function_26_5B51")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x10)
    Sleep(150)
    SetChrSubChip(0xFE, 0x11)
    Sound(318, 0, 60, 0)
    Sleep(350)
    SetChrSubChip(0xFE, 0x12)
    Sleep(150)
    SetChrSubChip(0xFE, 0x13)
    Sleep(150)
    Return()

    # Function_26_5B51 end

    def Function_27_5B87(): pass

    label("Function_27_5B87")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x13)
    Sleep(150)
    SetChrSubChip(0xFE, 0x12)
    Sleep(150)
    SetChrSubChip(0xFE, 0x11)
    Sound(318, 0, 60, 0)
    Sleep(350)
    SetChrSubChip(0xFE, 0x12)
    Sleep(150)
    SetChrSubChip(0xFE, 0x13)
    Sleep(150)
    Return()

    # Function_27_5B87 end

    def Function_28_5BC4(): pass

    label("Function_28_5BC4")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x13)
    Sleep(150)
    SetChrSubChip(0xFE, 0x12)
    Sleep(150)
    Sound(318, 0, 60, 0)
    SetChrSubChip(0xFE, 0x11)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0xFE, 0x10)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_5BC4 end

    def Function_29_5C16(): pass

    label("Function_29_5C16")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x2, 0, 50, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sound(887, 0, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)
    Sleep(600)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Sound(246, 0, 100, 0)
    Sound(255, 0, 100, 0)
    Sound(874, 0, 90, 0)
    OP_82(0x64, 0x64, 0x7D0, 0x12C)
    Sleep(50)
    Sound(251, 0, 100, 0)
    PlayEffect(0x2, 0x0, 0x8, 0x1, 0, 500, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    SetChrSubChip(0xFE, 0x4)
    Sleep(500)
    Return()

    # Function_29_5C16 end

    def Function_30_5D36(): pass

    label("Function_30_5D36")

    StopEffect(0x2, 0x0)
    PlayEffect(0x5, 0x2, 0x8, 0x5, 0, 750, 0, 20536, 0, 0, 670, 670, 670, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x21)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x2968, 0xBB8, 0xFFFFD634, 0x2EE, 0xBB8)
    StopEffect(0x1, 0x0)
    PlayEffect(0x5, 0x2, 0x8, 0x5, -400, 500, 400, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_82(0x32, 0x32, 0x7D0, 0x12C)
    StopEffect(0x0, 0x2)
    Sound(886, 0, 100, 0)
    Sound(815, 0, 100, 0)
    Sound(833, 0, 60, 0)
    OP_9D(0xFE, 0x2774, 0x6A4, 0xFFFFD7C4, 0x96, 0x2BC)
    StopEffect(0x0, 0x2)
    OP_9D(0xFE, 0x2580, 0x2BC, 0xFFFFD954, 0x32, 0x2BC)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 9730, 1100, -10330, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sound(811, 0, 100, 0)
    Sleep(20)
    Sound(862, 0, 40, 0)
    Return()

    # Function_30_5D36 end

    def Function_31_5E85(): pass

    label("Function_31_5E85")

    SetChrChipByIndex(0xFE, 0x21)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)

    label("loc_5EA3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EF9")
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(700)
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(1600)
    Jump("loc_5EA3")

    label("loc_5EF9")

    Return()

    # Function_31_5E85 end

    def Function_32_5EFA(): pass

    label("Function_32_5EFA")

    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x5)
    Sleep(600)
    Return()

    # Function_32_5EFA end

    def Function_33_5F16(): pass

    label("Function_33_5F16")

    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_33_5F16 end

    def Function_34_5F2B(): pass

    label("Function_34_5F2B")

    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_34_5F2B end

    def Function_35_5F3A(): pass

    label("Function_35_5F3A")

    SetChrPos(0x8, 9600, 700, -9900, 305)
    SetChrChipByIndex(0x8, 0x21)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrSubChip(0x8, 0x5)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 9730, 1100, -10330, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_35_5F3A end

    def Function_36_5FA5(): pass

    label("Function_36_5FA5")

    SetChrSubChip(0xFE, 0x0)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0xF)
    Sleep(429)
    Return()

    # Function_36_5FA5 end

    def Function_37_5FBB(): pass

    label("Function_37_5FBB")

    SetChrSubChip(0xFE, 0xF)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0x0)
    Sleep(429)
    Return()

    # Function_37_5FBB end

    def Function_38_5FD1(): pass

    label("Function_38_5FD1")

    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0x11)
    Sleep(167)
    SetChrSubChip(0xFE, 0x12)
    Sleep(500)
    Return()

    # Function_38_5FD1 end

    def Function_39_5FE7(): pass

    label("Function_39_5FE7")

    SetChrSubChip(0xFE, 0x12)
    Sleep(167)
    SetChrSubChip(0xFE, 0x13)
    Sleep(167)
    SetChrSubChip(0xFE, 0x14)
    Sleep(667)
    Return()

    # Function_39_5FE7 end

    def Function_40_5FFD(): pass

    label("Function_40_5FFD")

    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x13)
    Sleep(167)
    SetChrSubChip(0xFE, 0x12)
    Sleep(667)
    Return()

    # Function_40_5FFD end

    def Function_41_6013(): pass

    label("Function_41_6013")

    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    Return()

    # Function_41_6013 end

    def Function_42_6030(): pass

    label("Function_42_6030")

    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(571)
    Return()

    # Function_42_6030 end

    def Function_43_604D(): pass

    label("Function_43_604D")

    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x2)
    Return()

    # Function_43_604D end

    def Function_44_605C(): pass

    label("Function_44_605C")

    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x2)
    Return()

    # Function_44_605C end

    def Function_45_606B(): pass

    label("Function_45_606B")

    Sound(474, 2, 0, 0)
    Sleep(100)
    OP_25(0x1DA, 0xA)
    Sleep(100)
    OP_25(0x1DA, 0x14)
    Sleep(100)
    OP_25(0x1DA, 0x1E)
    Sleep(100)
    OP_25(0x1DA, 0x28)
    Sleep(100)
    OP_25(0x1DA, 0x32)
    Sleep(100)
    OP_25(0x1DA, 0x3C)
    Sleep(100)
    OP_25(0x1DA, 0x46)
    Sleep(100)
    OP_25(0x1DA, 0x50)
    Sleep(100)
    OP_25(0x1DA, 0x5A)
    Sleep(100)
    OP_25(0x1DA, 0x64)
    Return()

    # Function_45_606B end

    def Function_46_60B8(): pass

    label("Function_46_60B8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51747.itc", 0x1E)
    LoadChrToIndex("apl/ch51745.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    Call(0, 2)
    Call(0, 3)
    LoadChrToIndex("chr/ch03750.itc", 0x28)
    LoadChrToIndex("chr/ch03751.itc", 0x29)
    LoadChrToIndex("chr/ch03753.itc", 0x2B)
    LoadChrToIndex("apl/ch51748.itc", 0x2C)
    LoadEffect(0x0, "event/ev500_00.eff")
    LoadEffect(0x1, "event/ev17077.eff")
    LoadEffect(0x2, "battle/cr036301.eff")
    LoadEffect(0x4, "event/ev14001.eff")
    LoadEffect(0x6, "event/ev17076.eff")
    LoadEffect(0x7, "event/ev17075.eff")
    SoundLoad(3408)
    SoundLoad(3331)
    SoundLoad(3332)
    SoundLoad(3333)
    SoundLoad(3334)
    SoundLoad(3335)
    SoundLoad(2775)
    SoundLoad(2695)
    SoundLoad(3796)
    SoundLoad(3797)
    SoundLoad(3798)
    SoundLoad(3646)
    SoundLoad(3647)
    SoundLoad(3648)
    SoundLoad(961)
    SoundLoad(979)
    SoundLoad(1029)
    SoundLoad(960)
    SetChrPos(0x101, 0, 950, -11860, 0)
    SetChrPos(0x102, 1120, 950, -13300, 0)
    SetChrPos(0x103, 420, 950, -14370, 0)
    SetChrPos(0x104, -1270, 950, -13930, 0)
    SetChrPos(0xF4, -2540, 950, -13310, 0)
    SetChrPos(0xF5, 2540, 950, -13510, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x27)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x6)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrPos(0x9, 0, 8000, -750, 180)
    SetChrPos(0x9, 100, 8400, -3000, 180)
    PlayEffect(0x0, 0xFF, 0x9, 0x41, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x7, 0x9, 0x1, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x2C)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 3000, -5850, 180)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 0, 0)
    Call(0, 35)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_78(0x0, 0xB)
    ClearChrFlags(0xB, 0x80)
    OP_68(0, 3500, -6800, 0)
    MoveCamera(340, 1, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19500, 0)
    Sound(961, 2, 50, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17500, 3500)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 3900, -5840, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15300, 0)
    SetCameraDistance(14300, 3000)
    OP_6F(0x79)
    Sound(934, 0, 40, 0)
    Sound(283, 0, 30, 0)
    Fade(500)
    OP_68(0, 8300, 1820, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18900, 0)
    SetCameraDistance(17000, 4000)
    OP_0D()
    StopSound(961, 3000, 40)
    StopEffect(0x7, 0x2)
    PlayEffect(0x6, 0xFF, 0x9, 0x1, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x9, 3, 0, 48)
    WaitChrThread(0x9, 3)
    Sleep(300)
    Sleep(1700)
    OP_6F(0x79)

    #C0165
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#5P#60W……呼……呼……\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 5500, -6020, 0)
    MoveCamera(221, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17340, 0)
    SetChrPos(0x9, 0, 8000, -750, 180)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0166
    ChrTalk(
        0x101,
        "#00007F#5P#4S琪雅，你没事吧！？\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    #C0167
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12314F#11P#N#45W……嗯……\x01",
            "嘿嘿……还好……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0168
    ChrTalk(
        0x103,
        "#00214F#5P太好了……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        "#00306F#5P呼，真不容易啊……\x02",
    )

    CloseMessageWindow()

    def lambda_65CA():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_65CA)
    WaitChrThread(0xA, 2)
    Sleep(500)
    PlayBGM("ed7572", 0)

    #C0170
    ChrTalk(
        0xA,
        (
            "#10803F#11P#30W哼……原来如此。\x02\x03",

            "#10801F不愧是击退了亚里欧斯\x01",
            "先生他们的人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#00106F#5P贝尔……到此为止吧！\x02\x03",

            "#00101F你就算继续和我们战斗，\x01",
            "也是毫无意义的啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "#10804F#11P#30W呵呵呵，我可爱的艾莉。\x02\x03",

            "既然是你的请求，\x01",
            "我也并不是不能退让……\x02\x03",

            "#10811F不过，你应该很了解我吧……？\x01",
            "我的性格就是……\x01",
            "越可爱的孩子就越想欺负。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        "#00105F#5P你、你说什么……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1060, 5500, -5020, 0)
    MoveCamera(223, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10930, 0)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    OP_93(0xA, 0x0, 0x1F4)
    Sleep(300)

    #C0174
    ChrTalk(
        0xA,
        (
            "#10802F#5P#30W对了，琪雅……\x02\x03",

            "罗伊德警官他们\x01",
            "知不知道『那件事』呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12305F#11P#N#30W…………啊………………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0176
    ChrTalk(
        0xA,
        (
            "#10809F#5P呵呵呵，看样子，\x01",
            "你好像还没说吧？\x02\x03",

            "#10811F正好，不如就在这里\x01",
            "告诉他们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#11P#N#30W不、不要……不要说……\x02\x03",

            "#12311F……贝尔……求你……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0178
    ChrTalk(
        0x101,
        "#00013F#5P……怎么回事……？\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x104,
        (
            "#00307F#5P喂！大小姐！\x02\x03",

            "你不要再欺负\x01",
            "我们家的阿琪了！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(150)

    #C0180
    ChrTalk(
        0xA,
        (
            "#10804F#11P呵呵呵，你们是\x01",
            "真心爱着琪雅的吧？\x02\x03",

            "#10800F爱着这个库罗伊斯家族交托给『教团』，\x01",
            "并没有真正灵魂的人造人……\x02\x03",

            "爱着这个汇聚了教团所牺牲的\x01",
            "众多亡者之灵魂的人偶。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0181
    ChrTalk(
        0x101,
        (
            "#00007F#5P事到如今，你说这些又能怎么样！？\x02\x03",

            "#00010F那些事情，我们\x01",
            "早就听蔡特说过了！\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x103,
        (
            "#00203F#5P琪雅就是琪雅，只要以\x01",
            "自己的身份待在我们身边就好……\x02\x03",

            "#00201F没有比这\x01",
            "更加重要的事情！\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        (
            "#10804F#11P呵呵呵，琪雅，\x01",
            "你可真幸福啊。\x02\x03",

            "可以集罗伊德警官他们……\x01",
            "不，是集身边所有人的\x01",
            "好意与疼爱于一身。\x02\x03",

            "#10811F──凭借你的能力。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrSubChip(0x9, 0xA)
    OP_68(0, 9400, 5350, 0)
    MoveCamera(357, -11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(19000, 4000)
    OP_0D()
    SetChrSubChip(0x9, 0x16)
    Sleep(125)
    SetChrSubChip(0x9, 0x17)
    Sleep(300)

    def lambda_6C23():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6C23)
    WaitChrThread(0x9, 2)
    Sleep(800)

    def lambda_6C43():
        OP_A6(0xFE, 0x0, 0x32, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6C43)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 4700, 5350, 0)
    MoveCamera(0, -3, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29500, 0)
    SetCameraDistance(30500, 3500)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0184
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#5P#N#50W………呜呜呜………啊啊…………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0185
    ChrTalk(
        0x101,
        "#00005F#6P#N……哎………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0186
    ChrTalk(
        0x102,
        (
            "#00101F#12P#N……贝尔……\x01",
            "你刚才说什么……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0187
    ChrTalk(
        0xA,
        (
            "#10811F#11P#30W呵呵……难道你们\x01",
            "就不曾觉得不可思议吗？\x02\x03",

            "你们想必是从刚刚遇到琪雅的时候\x01",
            "开始，就发自内心地喜欢上了她，\x01",
            "一心只想保护她吧？\x02\x03",

            "你们觉得这是为什么呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        "#00013F#6P#N……………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0189
    ChrTalk(
        0x103,
        "#00208F#12P#N……难道………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0190
    ChrTalk(
        0x104,
        "#00310F#6P#N喂喂，说什么胡话……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis298.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis299.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(800)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis300.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)

    #C0191
    ChrTalk(
        0xA,
        (
            "#10804F#11P#30W那个约亚西姆自不必说，\x01",
            "就连黑手党成员和魔兽\x01",
            "都不会主动伤害琪雅。\x02\x03",

            "这个女孩和任何人都能马上成为朋友，\x01",
            "被所有人无条件地疼爱喜欢……\x02\x03",

            "#10811F难道就没有一个人对这种\x01",
            "异常情况产生过疑问吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(0, 4200, 5350, 20000)
    MoveCamera(0, 12, 0, 20000)
    OP_6E(700, 20000)
    SetCameraDistance(26810, 20000)
    SetChrSubChip(0x9, 0x16)
    Sleep(125)
    SetChrSubChip(0x9, 0xA)
    Sleep(150)
    OP_C9(0x0, 0x80000000)

    #C0192
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12307F#3647V#5P#N#50W#30A………不……不是这样的………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    #C0193
    ChrTalk(
        0xA,
        "#10803F#11P#30W#23A不——就是这样。\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(1000)

    #C0194
    ChrTalk(
        0xA,
        (
            "#10801F#11P#40W#75A你拥有在无意识中\x01",
            "掌控他人的想法与灵魂的能力。\x02\x03",

            "#10804F#40W#60A那种能力操纵了因果与认知，\x01",
            "让所有人都疼爱你、保护你。\x02\x03",

            "#10811F#40W#86A哼哼……身为虚假的存在，\x01",
            "拥有的也只是虚假的爱呢～\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0xF, 1, 0, 53)
    Sleep(1000)
    BeginChrThread(0x9, 3, 0, 50)
    WaitChrThread(0x9, 3)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(2000)
    OP_68(0, 6900, 5350, 2000)
    MoveCamera(0, 12, 0, 2000)
    SetCameraDistance(20000, 2000)
    FadeToDark(3000, 16777215, -1)
    OP_82(0x0, 0xC8, 0xBB8, 0x3E8)
    BeginChrThread(0xF, 2, 0, 56)
    PlayEffect(0x2, 0xFF, 0x9, 0x1, 0, 750, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 1000)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 140, -1, -1)

    #A0195
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12311F#3648V#11P#N#4S#30A#80W不对————！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_0D()
    OP_C9(0x1, 0x80000000)
    OP_0D()
    Sound(934, 0, 100, 0)
    Sleep(1500)
    Sound(689, 0, 100, 0)
    Sound(694, 0, 80, 0)
    Sound(979, 2, 70, 0)
    Sleep(2000)
    FadeToBright(3000, 16777215)
    OP_68(0, 4400, 5350, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(26910, 0)
    ClearMapObjFlags(0x0, 0x4)
    SetChrPos(0xB, 0, 10000, 0, 0)
    OP_93(0xB, 0xB4, 0x0)
    SetMapObjFrame(0xFF, "egg_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi35", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi25", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi25_", 0x0, 0x1)
    SetChrFlags(0x9, 0x80)
    Fade(1500)
    OP_68(1790, 5450, -470, 0)
    MoveCamera(298, 62, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(47700, 0)
    OP_68(0, 7000, 5350, 9000)
    MoveCamera(0, 19, 0, 9000)
    OP_6E(700, 9000)
    SetCameraDistance(31170, 9000)
    BeginChrThread(0xF, 3, 0, 54)
    OP_71(0x0, 0x7D1, 0x7F8, 0x0, 0x20)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    OP_0D()
    Sleep(1500)
    OP_6F(0x79)
    CancelBlur(0)
    Sound(1030, 0, 100, 0)
    Fade(500)
    Sleep(500)
    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    EndChrThread(0xF, 0x3)
    BeginChrThread(0xB, 3, 0, 51)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    OP_68(0, 11600, 0, 1000)
    MoveCamera(0, 22, 0, 1000)
    OP_6E(700, 1000)
    SetCameraDistance(21500, 1000)
    OP_0D()
    OP_6F(0x79)
    Sleep(2000)
    Sound(1031, 0, 100, 0)
    Sleep(700)
    OP_68(-1150, 11100, -650, 0)
    MoveCamera(10, 4, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27140, 0)
    CancelBlur(1500)
    Fade(500)
    BeginChrThread(0xB, 3, 0, 52)
    OP_68(570, 11200, -130, 0)
    MoveCamera(7, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19270, 0)
    OP_68(570, 10900, -130, 100000)
    MoveCamera(4, -13, 0, 10000)
    SetCameraDistance(23130, 10000)
    Sleep(3000)

    #C0196
    ChrTalk(
        0x102,
        "#00110F#5P#40W#12A…………啊………………\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7631")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_75FE")
    OP_FC(0x5)
    Jump("loc_7601")

    label("loc_75FE")

    OP_FC(0xB)

    label("loc_7601")


    #C0197
    ChrTalk(
        0x105,
        "#10410F#13P#40W#16A……这股神力是……\x02",
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_76EC")

    label("loc_7631")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_768E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_765B")
    OP_FC(0x5)
    Jump("loc_765E")

    label("loc_765B")

    OP_FC(0xB)

    label("loc_765E")


    #C0198
    ChrTalk(
        0x106,
        "#10707F#13P#40W#25A这、这股神力是……\x02",
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_76EC")

    label("loc_768E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76EC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76B8")
    OP_FC(0x5)
    Jump("loc_76BB")

    label("loc_76B8")

    OP_FC(0xB)

    label("loc_76BB")


    #C0199
    ChrTalk(
        0x109,
        "#10110F#13P#40W#27A……这、这道光芒是………\x02",
    )
    #Auto

    CloseMessageWindow()

    label("loc_76EC")

    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_774E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7719")
    OP_FC(0x5)
    Jump("loc_771C")

    label("loc_7719")

    OP_FC(0xB)

    label("loc_771C")


    #C0200
    ChrTalk(
        0x10A,
        "#00610F#13P#40W#36A碧之……『神』……？\x02",
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_7807")

    label("loc_774E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77AD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7778")
    OP_FC(0x5)
    Jump("loc_777B")

    label("loc_7778")

    OP_FC(0xB)

    label("loc_777B")


    #C0201
    ChrTalk(
        0x109,
        "#10110F#13P#40W#26A碧之……『神』……？\x02",
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_7807")

    label("loc_77AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7807")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77D7")
    OP_FC(0x5)
    Jump("loc_77DA")

    label("loc_77D7")

    OP_FC(0xB)

    label("loc_77DA")


    #C0202
    ChrTalk(
        0x106,
        "#10707F#13P#40W#25A碧之……『神』……？\x02",
    )
    #Auto

    CloseMessageWindow()

    label("loc_7807")

    Sleep(300)
    CancelBlur(500)
    Fade(1000)
    OP_68(-180, 7400, -1300, 0)
    MoveCamera(359, -3, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(38490, 0)
    OP_68(-180, 7400, -1300, 20000)
    MoveCamera(359, -3, 0, 20000)
    OP_6E(700, 20000)
    SetCameraDistance(28230, 20000)
    OP_0D()
    Sleep(500)
    StopBGM(0x7D0)
    StopSound(979, 4000, 60)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #C0203
    ChrTalk(
        0x101,
        "#00007F#3331V#6P#N#4S#25A琪雅——！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7459", 0)
    Sleep(300)
    BeginChrThread(0xA, 0, 0, 47)
    WaitChrThread(0xA, 0)
    Sleep(500)
    OP_68(-370, 12190, -1650, 60000)
    MoveCamera(359, -3, 0, 60000)
    OP_6E(700, 60000)
    SetCameraDistance(14000, 60000)

    #C0204
    ChrTalk(
        0xA,
        (
            "#10804F#3796V#6P#N#40W#110A呵呵，这正是『零之至宝』\x01",
            "与『碧之大树』完全一体化之后，\x01",
            "既为终焉，又为始源的形态……\x02\x03",

            "#3797V#80A也就是操纵时空中的一切因果，\x01",
            "打破女神所施加的『枷锁』，\x01",
            "亦真亦伪的地上之神——\x02\x03",

            "#10811F#3798V#30A『碧之虚神』！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #C0205
    ChrTalk(
        0x101,
        (
            "#00010F#3332V#6P#N#30W#30A没空听你胡扯！\x02\x03",

            "#3333V#35A有什么话，都等到夺回琪雅……\x01",
            "夺回那孩子之后再说！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0206
    ChrTalk(
        0x104,
        (
            "#00307F#2775V#6P#N#44W#43A嗯，复杂的事情\x01",
            "稍后再谈也不迟！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0207
    ChrTalk(
        0x103,
        (
            "#00207F#2695V#12P#N#30W#50A已确认巨大灵子体显现！\x01",
            "琪雅就在其中枢的核心部分！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0208
    ChrTalk(
        0x102,
        (
            "#00107F#3408V#12P#N#30W#32A无论如何都要将\x01",
            "琪雅从那里解救出来！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0209
    ChrTalk(
        0x101,
        (
            "#00015F#3334V#6P#N#30A各位，\x01",
            "这是最后的战斗了……！\x02\x03",

            "#00007F#3335V#59A拼尽全力，用我们的一切\x01",
            "去打破那碧色的存在吧！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(800)
    SetMessageWindowPos(-1, 150, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Sound(2153, 255, 90, 0)    #voice#Elie
    Sound(2343, 255, 100, 1)    #voice#Randy
    Sound(2249, 255, 100, 2)    #voice#Tio
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C2E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C25")
    OP_FC(0x4)
    Sound(2478, 255, 100, 4)    #voice#Noel
    Jump("loc_7C2E")

    label("loc_7C25")

    OP_FC(0x3)
    Sound(2478, 255, 100, 3)    #voice#Noel

    label("loc_7C2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C61")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C5B")
    Sound(2417, 255, 100, 4)    #voice#Lazy
    Jump("loc_7C61")

    label("loc_7C5B")

    Sound(2417, 255, 100, 3)    #voice#Lazy

    label("loc_7C61")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C94")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C8E")
    Sound(4115, 255, 100, 4)    #voice#Dudley
    Jump("loc_7C94")

    label("loc_7C8E")

    Sound(4115, 255, 100, 3)    #voice#Dudley

    label("loc_7C94")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7CC7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7CC1")
    Sound(3174, 255, 100, 4)    #voice#Rixia
    Jump("loc_7CC7")

    label("loc_7CC1")

    Sound(3174, 255, 100, 3)    #voice#Rixia

    label("loc_7CC7")

    SetChrName("成员们")

    #A0210
    AnonymousTalk(
        0xFF,
        "#5S#15A嗯！！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EndChrThread(0xF, 0x3)
    SetScenarioFlags(0x0, 0)
    Sound(960, 0, 100, 0)
    OP_50(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFF, 0x0)
    SetMapFlags(0x2000000)
    OP_C9(0x0, 0x8)
    Battle("BattleInfo_304", 0x30200012, 0x0, 0x100, 0x1E, 0xFF)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    OP_C9(0x0, 0x8)
    OP_50(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_348", 0x30200012, 0x0, 0x100, 0x1F, 0xFF)
    FadeToDark(0, 0, -1)
    StopBGM(0x1770)
    WaitBGM()
    ClearMapFlags(0x2000000)
    Call(0, 57)
    Return()

    # Function_46_60B8 end

    def Function_47_7D6C(): pass

    label("Function_47_7D6C")

    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xA, 0x29)
    SetChrSubChip(0xA, 0x0)
    Sound(809, 0, 40, 0)
    OP_9C(0xFE, 0xFFFFF060, 0x0, 0x3E8, 0x15E, 0x3E8)
    Sound(326, 0, 20, 0)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_47_7D6C end

    def Function_48_7DBB(): pass

    label("Function_48_7DBB")

    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(429)
    Return()

    # Function_48_7DBB end

    def Function_49_7DE5(): pass

    label("Function_49_7DE5")

    Sound(898, 0, 100, 0)
    Return()

    # Function_49_7DE5 end

    def Function_50_7DEC(): pass

    label("Function_50_7DEC")

    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0xA)
    Sleep(100)
    SetChrSubChip(0xFE, 0xB)
    Sleep(100)
    SetChrSubChip(0xFE, 0xC)
    Sleep(400)
    Return()

    # Function_50_7DEC end

    def Function_51_7E08(): pass

    label("Function_51_7E08")

    Sound(340, 0, 100, 0)
    Sound(998, 0, 100, 0)
    Sound(889, 0, 60, 0)
    OP_87(0x1, 0x1, 0x0, "891body:Layer2(4)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_74(0x0, 0xA)
    Sound(694, 0, 100, 0)
    OP_71(0x0, 0x803, 0x80C, 0x0, 0x0)
    OP_79(0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    OP_71(0x0, 0x80D, 0x820, 0x0, 0x20)
    Return()

    # Function_51_7E08 end

    def Function_52_7E86(): pass

    label("Function_52_7E86")

    OP_71(0x0, 0x821, 0x82A, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0xF, 3, 0, 55)
    OP_71(0x0, 0x835, 0x85B, 0x0, 0x20)
    Return()

    # Function_52_7E86 end

    def Function_53_7EA8(): pass

    label("Function_53_7EA8")

    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7460", 0)
    Return()

    # Function_53_7EA8 end

    def Function_54_7EB6(): pass

    label("Function_54_7EB6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7ECF")
    Sound(824, 0, 100, 0)
    Sleep(1300)
    Jump("Function_54_7EB6")

    label("loc_7ECF")

    Return()

    # Function_54_7EB6 end

    def Function_55_7ED0(): pass

    label("Function_55_7ED0")

    Sleep(200)

    label("loc_7ED3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EEC")
    Sound(824, 0, 50, 0)
    Sleep(3800)
    Jump("loc_7ED3")

    label("loc_7EEC")

    Return()

    # Function_55_7ED0 end

    def Function_56_7EED(): pass

    label("Function_56_7EED")

    Sound(929, 0, 50, 0)
    Sleep(500)
    Sound(940, 0, 100, 0)
    Sleep(200)
    Sound(936, 0, 100, 0)
    Sound(1029, 0, 100, 0)
    Return()

    # Function_56_7EED end

    def Function_57_7F0C(): pass

    label("Function_57_7F0C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 97)
    LoadChrToIndex("apl/ch51747.itc", 0x1E)
    LoadChrToIndex("chr/ch00001.itc", 0x1F)
    LoadChrToIndex("apl/ch51745.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    Call(0, 2)
    Call(0, 3)
    LoadChrToIndex("chr/ch03750.itc", 0x28)
    LoadEffect(0x0, "battle/bs891090.eff")
    LoadEffect(0x1, "battle/bs891062.eff")
    LoadEffect(0x2, "event/ev17070.eff")
    LoadEffect(0x3, "event/ev17071.eff")
    LoadEffect(0x4, "event/ev14001.eff")
    LoadEffect(0x5, "event\\ev500_00.eff")
    SoundLoad(3409)
    SoundLoad(2925)
    SoundLoad(3531)
    SoundLoad(2776)
    SoundLoad(2696)
    SoundLoad(3264)
    SoundLoad(825)
    SoundLoad(961)
    SoundLoad(832)
    SoundLoad(676)
    SetChrPos(0x101, 0, 950, -11860, 0)
    SetChrPos(0x102, 1120, 950, -13300, 0)
    SetChrPos(0x103, 420, 950, -14370, 0)
    SetChrPos(0x104, -1270, 950, -13930, 0)
    SetChrPos(0xF4, -2540, 950, -13310, 0)
    SetChrPos(0xF5, 2540, 950, -13510, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x27)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x17)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrPos(0x9, 0, 14600, -1150, 180)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x5, 0xFF, 0x9, 0x41, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 0, 14600, -1150, 180)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -3500, 3000, -4150, 45)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 0, 0)
    Call(0, 35)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_78(0x1, 0xB)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 3, 0, 58)
    ClearMapObjFlags(0x1, 0x4)
    SetChrPos(0xB, 0, 10000, 0, 0)
    OP_93(0xB, 0xB4, 0x0)
    SetMapObjFrame(0xFF, "egg_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi35", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi25", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi25_", 0x0, 0x1)
    OP_68(0, 11400, -1880, 0)
    MoveCamera(0, -15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    Sound(825, 2, 100, 0)
    Sleep(300)
    Sound(843, 0, 100, 0)
    Sound(934, 0, 70, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x1, 0, 4000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    FadeToBright(1000, 0)
    SetCameraDistance(27000, 4000)
    OP_0D()
    Sleep(2000)
    BeginChrThread(0xB, 3, 0, 59)
    BeginChrThread(0x9, 0, 0, 60)
    Sleep(2000)
    StopSound(825, 2000, 100)
    CancelBlur(500)
    Fade(500)
    OP_68(30, 14600, -310, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13330, 0)
    Sleep(3500)
    Sound(231, 0, 70, 0)
    StopEffect(0x1, 0x2)
    Sleep(500)
    OP_68(30, 4600, -310, 5500)
    Sleep(5900)
    OP_68(0, 3400, 250, 5000)
    MoveCamera(0, 14, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(17750, 5000)
    Sleep(500)
    StopSound(832, 2000, 100)

    def lambda_834D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_834D)
    OP_75(0x1, 0x1, 0x5DC)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    Sleep(1500)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 2300, -7800, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17140, 0)
    SetCameraDistance(14700, 30000)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x101, 0, 0, 63)
    BeginChrThread(0x102, 0, 0, 64)
    BeginChrThread(0x103, 0, 0, 65)
    BeginChrThread(0x104, 0, 0, 66)
    BeginChrThread(0xF4, 0, 0, 67)
    BeginChrThread(0xF5, 0, 0, 68)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    #C0211
    ChrTalk(
        0x104,
        "#00310F#6P啧……怎么回事！？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x102,
        "#00107F#12P琪雅……！？\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        (
            "#00208F#12P这是悲伤……\x01",
            "……还有绝望……！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_9B(0x1, 0x101, 0x0, 0x190, 0x4B0, 0x0)
    Sound(33, 0, 100, 0)
    Sound(48, 0, 50, 0)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0214
    ChrTalk(
        0x101,
        "#00007F#6P#4S琪雅，振作点！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0215
    ChrTalk(
        0x101,
        "#00007F#6P#4S听到的话就回答我！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0216
    ChrTalk(
        0xA,
        (
            "#10803F#6P#30W呜，怎么会……\x02\x03",

            "#10810F……难道就此……\x01",
            "像过去的幻之至宝一样……\x02",
        )
    )

    CloseMessageWindow()
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8630")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8601")
    OP_FC(0x6)
    Jump("loc_8604")

    label("loc_8601")

    OP_FC(0xC)

    label("loc_8604")


    #C0217
    ChrTalk(
        0x109,
        "#10107F#13P你、你的意思是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_86DD")

    label("loc_8630")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8689")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_865A")
    OP_FC(0x6)
    Jump("loc_865D")

    label("loc_865A")

    OP_FC(0xC)

    label("loc_865D")


    #C0218
    ChrTalk(
        0x106,
        "#10707F#13P你、你的意思是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_86DD")

    label("loc_8689")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86DD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86B3")
    OP_FC(0x6)
    Jump("loc_86B6")

    label("loc_86B3")

    OP_FC(0xC)

    label("loc_86B6")


    #C0219
    ChrTalk(
        0x10A,
        "#00607F#13P你的意思难道是……！？\x02",
    )

    CloseMessageWindow()

    label("loc_86DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_874D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8707")
    OP_FC(0x6)
    Jump("loc_870A")

    label("loc_8707")

    OP_FC(0xC)

    label("loc_870A")


    #C0220
    ChrTalk(
        0x105,
        (
            "#10410F#13P消除自身存在的因果，\x01",
            "使自己从世上消失……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8806")

    label("loc_874D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87A9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8777")
    OP_FC(0x6)
    Jump("loc_877A")

    label("loc_8777")

    OP_FC(0xC)

    label("loc_877A")


    #C0221
    ChrTalk(
        0x10A,
        (
            "#00610F#13P亲手让自己\x01",
            "从世上消失！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8806")

    label("loc_87A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8806")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87D3")
    OP_FC(0x6)
    Jump("loc_87D6")

    label("loc_87D3")

    OP_FC(0xC)

    label("loc_87D6")


    #C0222
    ChrTalk(
        0x106,
        (
            "#10701F#13P亲手令自己\x01",
            "从世上消失吗……！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8806")


    #C0223
    ChrTalk(
        0x101,
        "#00013F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 61)
    OP_68(0, 2800, -6500, 2000)
    MoveCamera(330, 5, 0, 2000)
    OP_6E(700, 2000)
    Sleep(500)

    def lambda_8868():

        label("loc_8868")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8868")

    QueueWorkItem2(0xA, 2, lambda_8868)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)

    #C0224
    ChrTalk(
        0x102,
        "#00105F#6P#N罗伊德……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0225
    ChrTalk(
        0x103,
        "#00207F#6P#N罗伊德前辈……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    EndChrThread(0xA, 0x2)

    #C0226
    ChrTalk(
        0xA,
        "#10805F#6P什、什么……！？\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x104,
        "#00307F#6P#N你想干什么！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 4100, -3910, 0)
    MoveCamera(330, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12810, 0)
    OP_0D()
    OP_68(0, 4300, -2110, 10000)
    MoveCamera(324, 8, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(12810, 10000)
    StopEffect(0x5, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x3, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    #C0228
    ChrTalk(
        0x101,
        (
            "#00010F#5P#50W#55A……没问题的……\x01",
            "你们在那里等我……！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(1000)
    StopEffect(0x3, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x4, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    #C0229
    ChrTalk(
        0x101,
        "#00015F#5P#60W#36A我……一定亲手把那孩子……\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)
    StopEffect(0x4, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x5, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x5, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    #C0230
    ChrTalk(
        0x101,
        "#00007F#5P#80W#28A……把琪雅…………\x02",
    )
    #Auto

    CloseMessageWindow()
    FadeToDark(4000, 16777215, -1)

    def lambda_8BAE():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8BAE)
    OP_68(0, 4300, -160, 4000)
    MoveCamera(324, 8, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(12810, 4000)
    BeginChrThread(0x101, 0, 0, 62)
    Sleep(1000)
    Sound(829, 0, 70, 0)
    StopSound(979, 2500, 70)
    StopSound(112, 2500, 50)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C5D")

    #C0231
    ChrTalk(
        0x102,
        "#00107F#3409V#6P#4S#N#15A#30W罗伊德──！\x02",
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_8DB1")

    label("loc_8C5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CA4")

    #C0232
    ChrTalk(
        0x103,
        "#00207F#2696V#6P#4S#N#15A#30W罗伊德前辈──！\x02",
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_8DB1")

    label("loc_8CA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CE5")

    #C0233
    ChrTalk(
        0x104,
        "#00307F#2776V#6P#4S#N#15A#30W罗伊德！！\x02",
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_8DB1")

    label("loc_8CE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D28")

    #C0234
    ChrTalk(
        0x105,
        "#10407F#2925V#6P#4S#N#15A#30W罗伊德──！\x02",
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_8DB1")

    label("loc_8D28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D6F")

    #C0235
    ChrTalk(
        0x109,
        "#10107F#3531V#6P#4S#N#15A#30W罗伊德警官——！\x02",
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_8DB1")

    label("loc_8D6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DB1")

    #C0236
    ChrTalk(
        0x106,
        "#10707F#3264V#6P#4S#N#15A#30W罗伊德警官──！\x02",
    )
    #Auto

    CloseMessageWindow()

    label("loc_8DB1")

    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_0D()
    Sleep(2000)
    SetScenarioFlags(0x22, 0)
    NewScene("m9013", 0, 20, 0)
    IdleLoop()
    Return()

    # Function_57_7F0C end

    def Function_58_8DCB(): pass

    label("Function_58_8DCB")

    OP_74(0x1, 0xA)
    OP_71(0x1, 0x51, 0x64, 0x0, 0x20)
    Return()

    # Function_58_8DCB end

    def Function_59_8DDC(): pass

    label("Function_59_8DDC")

    ClearMapObjFlags(0x1, 0x20)
    OP_79(0x1)
    Sound(661, 0, 100, 0)
    OP_74(0x1, 0xA)
    OP_71(0x1, 0x30C, 0x35C, 0x0, 0x0)
    Sleep(500)
    StopEffect(0x0, 0x2)
    Sound(676, 0, 80, 0)
    OP_79(0x1)
    OP_71(0x1, 0x367, 0x38E, 0x0, 0x20)
    Return()

    # Function_59_8DDC end

    def Function_60_8E17(): pass

    label("Function_60_8E17")

    Sound(692, 0, 60, 0)
    Sound(930, 0, 100, 0)
    Sleep(1000)
    Sound(682, 0, 100, 0)
    Sound(832, 2, 100, 0)
    OP_87(0x1, 0x1, 0x1, "891core:Layer1(52)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(2500)
    Sleep(600)
    OP_75(0x1, 0x1, 0x2BC)
    Sound(223, 0, 100, 0)
    Sound(920, 0, 100, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    Sleep(800)

    def lambda_8E99():
        OP_96(0xFE, 0x0, 0xFA0, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E99)

    def lambda_8EB3():
        OP_96(0xFE, 0x0, 0xFA0, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8EB3)
    Sleep(2200)
    BeginChrThread(0xF, 1, 0, 70)
    Sleep(300)
    PlayEffect(0x2, 0x2, 0xE, 0x1, 0, 750, 750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sleep(500)
    Sound(898, 0, 50, 0)
    BeginChrThread(0xFE, 0, 0, 69)
    WaitChrThread(0xFE, 0)
    WaitChrThread(0xFE, 1)
    OP_9B(0x1, 0xE, 0x0, 0x3E8, 0x1F4, 0x1)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_60_8E17 end

    def Function_61_8F3A(): pass

    label("Function_61_8F3A")

    Sound(1010, 2, 70, 0)
    OP_95(0xFE, 0, 0, -4750, 5000, 0x1)
    Sound(833, 0, 60, 0)
    StopSound(1010, 500, 60)
    StopSound(961, 1000, 40)
    Sound(979, 2, 80, 0)
    PlayEffect(0x3, 0x3, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    StopEffect(0x3, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x4, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0xB)

    def lambda_9006():
        OP_A6(0xFE, 0x0, 0x32, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9006)
    Sleep(250)
    SetChrSubChip(0xFE, 0x13)
    OP_9B(0x1, 0xFE, 0x0, 0x190, 0x3E8, 0x0)
    StopEffect(0x4, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x5, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1B)

    def lambda_9079():
        OP_A6(0xFE, 0x0, 0x32, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9079)
    Sleep(250)
    SetChrSubChip(0xFE, 0x23)
    OP_9B(0x1, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
    SetChrSubChip(0xFE, 0x3)

    label("loc_90A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90D3")

    def lambda_90B7():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_90B7)
    Sleep(400)
    Jump("loc_90A7")

    label("loc_90D3")

    Return()

    # Function_61_8F3A end

    def Function_62_90D4(): pass

    label("Function_62_90D4")

    PlayEffect(0x3, 0xFF, 0xFF, 0x1, 60, 4100, -2210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0xB)

    def lambda_9114():
        OP_A6(0xFE, 0x0, 0x32, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9114)
    Sleep(250)
    SetChrSubChip(0xFE, 0x13)

    def lambda_9134():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9134)
    Sound(920, 0, 100, 0)
    Sound(1005, 0, 100, 0)
    Sleep(700)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_62_90D4 end

    def Function_63_9159(): pass

    label("Function_63_9159")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_63_9159 end

    def Function_64_9168(): pass

    label("Function_64_9168")

    Sleep(100)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_64_9168 end

    def Function_65_917A(): pass

    label("Function_65_917A")

    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_65_917A end

    def Function_66_918C(): pass

    label("Function_66_918C")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_66_918C end

    def Function_67_9198(): pass

    label("Function_67_9198")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91B8")
    Sound(540, 0, 50, 0)
    Jump("loc_91DD")

    label("loc_91B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_91DD")
    Sound(531, 0, 50, 0)

    label("loc_91DD")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_67_9198 end

    def Function_68_91E6(): pass

    label("Function_68_91E6")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9206")
    Sound(540, 0, 50, 0)
    Jump("loc_922B")

    label("loc_9206")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_922B")
    Sound(531, 0, 50, 0)

    label("loc_922B")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_68_91E6 end

    def Function_69_9234(): pass

    label("Function_69_9234")

    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(571)
    Return()

    # Function_69_9234 end

    def Function_70_9251(): pass

    label("Function_70_9251")

    Sound(961, 2, 0, 0)
    Sleep(150)
    OP_25(0x3C1, 0x5)
    Sleep(150)
    OP_25(0x3C1, 0xA)
    Sleep(150)
    OP_25(0x3C1, 0xF)
    Sleep(150)
    OP_25(0x3C1, 0x14)
    Sleep(150)
    OP_25(0x3C1, 0x19)
    Sleep(150)
    OP_25(0x3C1, 0x1E)
    Sleep(150)
    OP_25(0x3C1, 0x23)
    Sleep(150)
    OP_25(0x3C1, 0x28)
    StopSound(112, 1000, 50)
    Return()

    # Function_70_9251 end

    def Function_71_9296(): pass

    label("Function_71_9296")

    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    Call(0, 97)
    CreatePortrait(0, 112, 76, 368, 204, 70, 90, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x0, "c_vis419.itp")
    CreatePortrait(1, 112, 116, 368, 244, 118, 88, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x0, "c_vis420.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis418.itp")
    LoadChrToIndex("chr/ch05000.itc", 0x1E)
    LoadChrToIndex("chr/ch03750.itc", 0x1F)
    LoadChrToIndex("chr/ch03752.itc", 0x20)
    LoadChrToIndex("apl/ch51745.itc", 0x21)
    LoadChrToIndex("apl/ch51216.itc", 0x22)
    LoadChrToIndex("chr/ch03754.itc", 0x23)
    LoadChrToIndex("apl/ch51757.itc", 0x24)
    LoadChrToIndex("apl/ch51758.itc", 0x25)
    LoadChrToIndex("apl/ch51777.itc", 0x26)
    LoadChrToIndex("apl/ch51776.itc", 0x27)
    LoadEffect(0x0, "battle/mgaria0.eff")
    LoadEffect(0x1, "event/ev17070.eff")
    LoadEffect(0x2, "event/evwarp.eff")
    LoadEffect(0x3, "battle/cr036301.eff")
    LoadEffect(0x4, "event/ev14001.eff")
    SoundLoad(961)
    SoundLoad(832)
    SoundLoad(3410)
    SoundLoad(3337)
    SoundLoad(3338)
    SoundLoad(3339)
    SoundLoad(3340)
    SoundLoad(2777)
    SoundLoad(2697)
    SoundLoad(3799)
    SoundLoad(3800)
    SoundLoad(3655)
    SoundLoad(3656)
    OP_68(0, 2300, -7000, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x101, 0, 1000, -12500, 180)
    SetChrPos(0x102, 2120, 950, -10650, 222)
    SetChrPos(0x103, -3740, 950, -12910, 91)
    SetChrPos(0x104, 3750, 950, -12870, 268)
    SetChrPos(0xF4, 2380, 950, -15570, 317)
    SetChrPos(0xF5, -2360, 950, -15600, 42)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 2000, -12500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1000)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x1)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 1000, -13100, 180)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 2900, -4800, 135)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 0, 0)
    Call(0, 35)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0xB)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x10, 0, 950, -12500, 180)
    SetMapObjFrame(0xFF, "egg_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi35", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi25", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi25_", 0x0, 0x1)
    SetMapObjFrame(0xFF, "line03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "line11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "line11a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pnrm0b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "line02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "line01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "line01a_add", 0x0, 0x1)
    PlayEffect(0x1, 0x0, 0x101, 0x1, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96AD")
    Jump("loc_9757")

    label("loc_96AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96D0")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x103)
    OP_FD(0x103, 0x10)
    Jump("loc_9757")

    label("loc_96D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96F3")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x104)
    OP_FD(0x104, 0x10)
    Jump("loc_9757")

    label("loc_96F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9716")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x105)
    OP_FD(0x105, 0x10)
    Jump("loc_9757")

    label("loc_9716")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9739")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x109)
    OP_FD(0x109, 0x10)
    Jump("loc_9757")

    label("loc_9739")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9757")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x106)
    OP_FD(0x106, 0x10)

    label("loc_9757")

    BeginChrThread(0xF, 1, 0, 70)
    FadeToBright(1000, 16777215)
    OP_68(0, 2100, -13000, 0)
    MoveCamera(290, 26, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(23000, 3500)
    OP_0D()
    Sleep(2500)
    Sound(919, 0, 60, 0)
    PlayEffect(0x3, 0xFF, 0x101, 0x1, 0, 750, 750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Fade(500)
    OP_93(0xA, 0xB4, 0x0)
    OP_68(0, 2100, -13000, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(13450, 4000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 0, 0, 72)
    OP_0D()
    StopEffect(0x0, 0x2)
    StopSound(961, 2000, 40)
    OP_68(0, 2100, -13000, 10000)
    MoveCamera(0, 20, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(11500, 10000)
    Sound(934, 0, 40, 0)
    Sound(935, 0, 80, 0)
    Sound(223, 0, 100, 0)

    def lambda_9883():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9883)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x101, 0)
    BeginChrThread(0x101, 0, 0, 73)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_993C")

    #C0237
    ChrTalk(
        0x103,
        "#00216F#6P#30W#20A……啊………\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0238
    ChrTalk(
        0x104,
        "#00316F#12P#30W#30A罗伊德……阿琪……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0239
    ChrTalk(
        0x102,
        "#00116F#11P#30W#25A你们……回来了……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_9D02")

    label("loc_993C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99D5")

    #C0240
    ChrTalk(
        0x104,
        "#00316F#12P#30W#15A哦哦……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0241
    ChrTalk(
        0x102,
        "#00116F#6P#30W#22A罗伊德……小琪雅……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0242
    ChrTalk(
        0x103,
        "#00216F#11P#30W#30A你们……回来了……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_9D02")

    label("loc_99D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A77")

    #C0243
    ChrTalk(
        0x102,
        "#00116F#12P#30W#15A啊……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0244
    ChrTalk(
        0x103,
        "#00216F#6P#30W#23A罗伊德前辈……琪雅……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0245
    ChrTalk(
        0x104,
        (
            "#00315F#11P#30W#43A哈哈……\x01",
            "终于……回来了吗……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_9D02")

    label("loc_9A77")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B53")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AA0")
    OP_FC(0xC)
    Jump("loc_9AA3")

    label("loc_9AA0")

    OP_FC(0x6)

    label("loc_9AA3")


    #C0246
    ChrTalk(
        0x102,
        "#00116F#13P#30W#15A啊……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0247
    ChrTalk(
        0x103,
        "#00216F#6P#30W#15A……罗伊德前辈……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0248
    ChrTalk(
        0x104,
        "#00316F#12P#30W#15A还有阿琪……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0249
    ChrTalk(
        0x105,
        "#10411F#11P#30W#30A呵呵……回来了吗……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_9D02")

    label("loc_9B53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C2D")

    #C0250
    ChrTalk(
        0x103,
        "#00216F#6P#30W#15A……啊………\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0251
    ChrTalk(
        0x104,
        "#00316F#12P#30W#15A罗伊德……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BCB")
    OP_FC(0xC)
    Jump("loc_9BCE")

    label("loc_9BCB")

    OP_FC(0x6)

    label("loc_9BCE")


    #C0252
    ChrTalk(
        0x102,
        "#00116F#13P#30W#15A还有小琪雅……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0253
    ChrTalk(
        0x109,
        "#10116F#11P#30W#33A你们……回来了……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_9D02")

    label("loc_9C2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D02")

    #C0254
    ChrTalk(
        0x104,
        "#00316F#12P#30W#20A哦哦……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C7C")
    OP_FC(0xC)
    Jump("loc_9C7F")

    label("loc_9C7C")

    OP_FC(0x6)

    label("loc_9C7F")


    #C0255
    ChrTalk(
        0x102,
        "#00116F#13P#30W#15A罗伊德……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0256
    ChrTalk(
        0x103,
        "#00216F#6P#30W#15A……还有琪雅……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0257
    ChrTalk(
        0x106,
        "#10716F#11P#30W#31A你们……回来了……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9D02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D7C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D2C")
    OP_FC(0xC)
    Jump("loc_9D2F")

    label("loc_9D2C")

    OP_FC(0x6)

    label("loc_9D2F")


    #C0258
    ChrTalk(
        0x10A,
        (
            "#00604F#13P#30W#44A真是的……\x01",
            "这股蛮劲，恐怕连你哥哥都要甘拜下风……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9D7C")

    WaitChrThread(0x101, 0)
    OP_6F(0x79)

    #C0259
    ChrTalk(
        0x101,
        (
            "#00006F#11P#40W呼……\x02\x03",

            "#30W#00000F我回来了，各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x9,
        "#05817F#5P#50W……呜呜……呜……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DF7")
    OP_FC(0x5)
    Jump("loc_9E8D")

    label("loc_9DF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E28")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E20")
    OP_FC(0xC)
    Jump("loc_9E23")

    label("loc_9E20")

    OP_FC(0x6)

    label("loc_9E23")

    Jump("loc_9E8D")

    label("loc_9E28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E59")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E51")
    OP_FC(0xC)
    Jump("loc_9E54")

    label("loc_9E51")

    OP_FC(0x6)

    label("loc_9E54")

    Jump("loc_9E8D")

    label("loc_9E59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E8A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E82")
    OP_FC(0xC)
    Jump("loc_9E85")

    label("loc_9E82")

    OP_FC(0x6)

    label("loc_9E85")

    Jump("loc_9E8D")

    label("loc_9E8A")

    OP_FC(0xB)

    label("loc_9E8D")

    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0261
    ChrTalk(
        0x102,
        "#00114F#13P罗伊德……太好了！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(10500, 1000)
    BeginChrThread(0x102, 0, 0, 78)
    BeginChrThread(0x103, 0, 0, 79)
    BeginChrThread(0x104, 0, 0, 80)
    BeginChrThread(0xF4, 0, 0, 81)
    BeginChrThread(0xF5, 0, 0, 82)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F16")
    OP_FC(0xB)
    Jump("loc_9F19")

    label("loc_9F16")

    OP_FC(0x5)

    label("loc_9F19")

    OP_6F(0x79)
    SetCameraDistance(10000, 30000)

    #C0262
    ChrTalk(
        0x103,
        (
            "#00214F#13P还有琪雅……\x01",
            "你没事吧……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x104,
        (
            "#00302F#11P看来已经恢复\x01",
            "原来的样子了……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#00004F#11P嗯，已经没事了。\x02\x03",

            "#00000F……来，琪雅，\x01",
            "有话要对大家说吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x9,
        "#05817F#5P#40W呜……嗯………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(802, 0, 50, 0)
    Sound(898, 0, 30, 0)
    OP_68(0, 2000, -13000, 500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x18)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x1000)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Fade(250)
    OP_0D()
    Sleep(700)
    BeginChrThread(0x9, 1, 0, 74)
    WaitChrThread(0x9, 1)
    BeginChrThread(0x9, 1, 0, 75)
    WaitChrThread(0x9, 1)

    #C0266
    ChrTalk(
        0x9,
        (
            "#05821F#5P#40W对不……起……\x02\x03",

            "……我只会做任性的事……\x01",
            "一直害大家担心……\x02\x03",

            "#05818F还有……\x01",
            "……谢谢你们来找我……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0EC")
    OP_FC(0x5)
    Jump("loc_A182")

    label("loc_A0EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A11D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A115")
    OP_FC(0xC)
    Jump("loc_A118")

    label("loc_A115")

    OP_FC(0x6)

    label("loc_A118")

    Jump("loc_A182")

    label("loc_A11D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A14E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A146")
    OP_FC(0xC)
    Jump("loc_A149")

    label("loc_A146")

    OP_FC(0x6)

    label("loc_A149")

    Jump("loc_A182")

    label("loc_A14E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A17F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A177")
    OP_FC(0xC)
    Jump("loc_A17A")

    label("loc_A177")

    OP_FC(0x6)

    label("loc_A17A")

    Jump("loc_A182")

    label("loc_A17F")

    OP_FC(0xB)

    label("loc_A182")


    #C0267
    ChrTalk(
        0x102,
        "#00116F#13P小琪雅……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1B4")
    OP_FC(0xB)
    Jump("loc_A1B7")

    label("loc_A1B4")

    OP_FC(0x5)

    label("loc_A1B7")


    #C0268
    ChrTalk(
        0x103,
        "#00204F#13P你不需要道谢……\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x104,
        (
            "#00309F#11P哈哈……但回家以后要打一顿屁屁，\x01",
            "这点心理准备可要做好哦～\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 1, 0, 76)
    WaitChrThread(0x9, 1)

    #C0270
    ChrTalk(
        0x9,
        (
            "#05817F#5P#50W……嗯……\x01",
            "呜……呜呜呜……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        (
            "#00012F#11P真是的……\x01",
            "已经不用再哭了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2CD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2B3")
    OP_FC(0xC)
    Jump("loc_A2B6")

    label("loc_A2B3")

    OP_FC(0x6)

    label("loc_A2B6")


    #C0272
    ChrTalk(
        0x10A,
        "#00604F#13P呼……\x02",
    )

    CloseMessageWindow()

    label("loc_A2CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A330")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2F4")
    OP_FC(0xB)
    Jump("loc_A311")

    label("loc_A2F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A30E")
    OP_FC(0xC)
    Jump("loc_A311")

    label("loc_A30E")

    OP_FC(0x6)

    label("loc_A311")


    #C0273
    ChrTalk(
        0x105,
        "#10404F#13P呵呵，真是的。\x02",
    )

    CloseMessageWindow()

    label("loc_A330")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A399")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A357")
    OP_FC(0xB)
    Jump("loc_A374")

    label("loc_A357")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A371")
    OP_FC(0xC)
    Jump("loc_A374")

    label("loc_A371")

    OP_FC(0x6)

    label("loc_A374")


    #C0274
    ChrTalk(
        0x109,
        "#10106F#13P……呼……太好了……\x02",
    )

    CloseMessageWindow()

    label("loc_A399")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A408")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3C0")
    OP_FC(0xB)
    Jump("loc_A3DD")

    label("loc_A3C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3DA")
    OP_FC(0xC)
    Jump("loc_A3DD")

    label("loc_A3DA")

    OP_FC(0x6)

    label("loc_A3DD")


    #C0275
    ChrTalk(
        0x106,
        "#10710F#13P（……这就是……羁绊……）\x02",
    )

    CloseMessageWindow()

    label("loc_A408")

    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0276
    ChrTalk(
        0xA,
        (
            "#10803F#3799V#5P#N#40W#44A真是的，\x01",
            "好无聊的收场啊。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x1, 0x80000000)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x9, 0x1F)
    Sleep(125)
    SetChrSubChip(0x9, 0x1E)
    Sleep(875)
    OP_68(0, 3300, -10520, 1800)
    MoveCamera(0, -1, 0, 1800)
    OP_6E(700, 1800)
    SetCameraDistance(10550, 1800)
    Sleep(200)

    def lambda_A52B():
        OP_93(0xFE, 0xAF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_A52B)
    Sleep(50)

    def lambda_A53B():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A53B)
    Sleep(50)

    def lambda_A54B():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A54B)
    Sleep(50)

    def lambda_A55B():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A55B)
    Sleep(50)

    def lambda_A56B():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A56B)
    Sleep(50)

    def lambda_A57B():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_A57B)
    Sleep(50)

    def lambda_A58B():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_A58B)
    Sleep(300)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x1000)

    def lambda_A5AD():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A5AD)
    WaitChrThread(0xF5, 2)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)

    def lambda_A5C4():
        OP_96(0xFE, 0xFFFFFE8E, 0x3B6, 0xFFFFCCFC, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A5C4)

    #C0277
    ChrTalk(
        0x101,
        "#00001F#6P#N……玛丽亚贝尔小姐。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0278
    ChrTalk(
        0x102,
        (
            "#00101F#12P#N贝尔……\x01",
            "……你还想继续纠缠吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0279
    ChrTalk(
        0xA,
        (
            "#10803F#5P#30W还有什么可纠缠的，\x01",
            "『至宝』的力量已经从琪雅的身上消失了。\x02\x03",

            "连同库罗伊斯家族千年的执念一起……\x02\x03",

            "#10801F真是的……\x01",
            "太让人失望了。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x9,
        "#05816F#6P#N#30W……贝尔……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0281
    ChrTalk(
        0x103,
        (
            "#00206F#6P#N教团的噩梦……\x01",
            "也算是从真正意义上终结了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0282
    ChrTalk(
        0xA,
        (
            "#10803F#5P#30W嗯，但克洛斯贝尔\x01",
            "今后恐怕还要面临\x01",
            "更大的灾难。\x02\x03",

            "特别是埃雷波尼亚……\x01",
            "无论哪一方势力在内战中取得胜利，\x01",
            "侵略克洛斯贝尔的可能性都非常高。\x02\x03",

            "#10801F一旦如此，卡尔瓦德共和国\x01",
            "也必定会派出军队与之对抗。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x102,
        "#00106F#12P#N……嗯………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0284
    ChrTalk(
        0x104,
        "#00301F#12P#N确实如此……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A899")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A867")
    OP_FC(0xFFF4)
    Jump("loc_A86A")

    label("loc_A867")

    OP_FC(0xFFFA)

    label("loc_A86A")


    #C0285
    ChrTalk(
        0x109,
        "#10108F#13P………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_A8F0")

    label("loc_A899")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8F0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8C3")
    OP_FC(0xFFF4)
    Jump("loc_A8C6")

    label("loc_A8C3")

    OP_FC(0xFFFA)

    label("loc_A8C6")


    #C0286
    ChrTalk(
        0x10A,
        "#00608F#13P………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_A8F0")


    #C0287
    ChrTalk(
        0xA,
        (
            "#10804F#5P#30W然而，如今已经失去了『至宝』，\x01",
            "你们再也没有阻挡他们的手段了。\x02\x03",

            "#10800F关于这一点，你们应该明白吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        (
            "#00006F#6P#N嗯，即使如此……\x01",
            "我们还是和琪雅一起选择了这条道路。\x02\x03",

            "#00003F我们会共同跨越今后的灾难，\x01",
            "把握住未来的光明……\x02\x03",

            "#00000F所以……绝不后悔。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0289
    ChrTalk(
        0x103,
        "#00202F#6P#N……是的……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0290
    ChrTalk(
        0x102,
        (
            "#00102F#12P#N呵呵，看来今后\x01",
            "会比以前更忙呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0291
    ChrTalk(
        0x104,
        (
            "#00304F#12P#N话说回来，在走到这一步之前，\x01",
            "我们已经吃过不少苦头了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB06")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAC6")
    OP_FC(0xFFF4)
    Jump("loc_AAC9")

    label("loc_AAC6")

    OP_FC(0xFFFA)

    label("loc_AAC9")


    #C0292
    ChrTalk(
        0x109,
        (
            "#10100F#13P今后只要勇往直前，\x01",
            "大家一起渡过难关就是了！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_AB06")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB7E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB30")
    OP_FC(0xFFF4)
    Jump("loc_AB33")

    label("loc_AB30")

    OP_FC(0xFFFA)

    label("loc_AB33")


    #C0293
    ChrTalk(
        0x10A,
        (
            "#00604F#13P接下来，警察的真正价值恐怕\x01",
            "将会受到比以往更加严格的检验。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_AB7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC22")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABA8")
    OP_FC(0xFFF4)
    Jump("loc_ABAB")

    label("loc_ABA8")

    OP_FC(0xFFFA)

    label("loc_ABAB")


    #C0294
    ChrTalk(
        0x105,
        (
            "#10404F#13P呵呵，以我的立场，\x01",
            "并不能轻率发言……\x02\x03",

            "#10402F不过，典礼省应该不会再出手干涉，\x01",
            "教会大概也能略尽薄力。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_AC22")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC88")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC4C")
    OP_FC(0xFFF4)
    Jump("loc_AC4F")

    label("loc_AC4C")

    OP_FC(0xFFFA)

    label("loc_AC4F")


    #C0295
    ChrTalk(
        0x106,
        (
            "#10704F#13P我……\x01",
            "虽然力量微薄，但也会尽力帮忙的。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_AC88")


    #C0296
    ChrTalk(
        0xA,
        (
            "#10804F#5P#30W呵呵……\x01",
            "真是受不了你们了。\x02\x03",

            "#10802F好吧，既然如此，\x01",
            "你们就尽量加油吧。\x02",
        )
    )

    CloseMessageWindow()
    Sound(805, 0, 70, 0)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    Sleep(700)
    Sound(357, 0, 80, 0)
    Sound(832, 2, 100, 0)
    BeginChrThread(0xA, 3, 0, 4)
    PlayEffect(0x0, 0x0, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0297
    ChrTalk(
        0x102,
        "#00105F#12P#N贝尔……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0298
    ChrTalk(
        0x101,
        "#00011F#6P#N玛丽亚贝尔小姐……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    EndChrThread(0xA, 0x3)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    Sleep(300)

    #C0299
    ChrTalk(
        0xA,
        (
            "#10804F#5P哦，对了，伊安律师\x01",
            "只是陷入假死状态而已。\x02\x03",

            "#10800F只要妥善处理，应该可以保住性命。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        "#00005F#6P#N啊……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(1590, 2400, -10140, 1500)
    MoveCamera(35, 15, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(14390, 1500)

    def lambda_AEEC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AEEC)
    Sleep(50)

    def lambda_AEFC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AEFC)
    Sleep(50)

    def lambda_AF0C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AF0C)
    Sleep(50)

    def lambda_AF1C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AF1C)
    Sleep(50)

    def lambda_AF2C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_AF2C)
    Sleep(50)

    def lambda_AF3C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_AF3C)
    Sleep(50)

    def lambda_AF4C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_AF4C)
    WaitChrThread(0xF5, 2)
    OP_6F(0x79)
    Sleep(700)
    Fade(500)
    OP_68(9510, 1700, -9870, 0)
    MoveCamera(46, 28, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13150, 0)
    OP_0D()
    Sleep(1700)
    Fade(500)
    OP_68(0, 3300, -10520, 0)
    MoveCamera(0, -1, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10550, 0)
    OP_0D()

    def lambda_AFCD():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AFCD)
    Sleep(50)

    def lambda_AFDD():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AFDD)
    Sleep(50)

    def lambda_AFED():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AFED)
    Sleep(50)

    def lambda_AFFD():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AFFD)
    Sleep(50)

    def lambda_B00D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_B00D)
    Sleep(50)

    def lambda_B01D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_B01D)
    Sleep(50)

    def lambda_B02D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B02D)
    WaitChrThread(0xF5, 2)

    #C0301
    ChrTalk(
        0xA,
        (
            "#10804F#5P还有，由于失去了至宝之力，\x01",
            "『大树』在不久之后就会毁灭。\x02\x03",

            "#10800F最多还能撑几小时……\x01",
            "你们还是尽快逃出去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x104,
        "#00301F#12P#N你……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0303
    ChrTalk(
        0x103,
        "#00208F#6P#N……为什么……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0304
    ChrTalk(
        0xA,
        (
            "#10802F#5P呵呵，我早已有所打算，\x01",
            "无论这次的结果如何，都会离开克洛斯贝尔。\x02\x03",

            "#10804F因为『噬身之蛇』的盟主大人\x01",
            "希望我去填补\x01",
            "空缺的使徒位置。\x02",
        )
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0305
    ChrTalk(
        0x101,
        "#00007F#6P#N什么！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0306
    ChrTalk(
        0x103,
        (
            "#00201F#6P#N使徒……\x01",
            "『结社』的最高干部吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0307
    ChrTalk(
        0x102,
        "#00108F#12P#N贝尔……你……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0308
    ChrTalk(
        0xA,
        (
            "#10802F#5P哦呵呵……\x01",
            "艾莉，别摆出那副表情嘛。\x02\x03",

            "#10804F整个大陆的形势如你所见，\x01",
            "我们今后肯定还有再次见面的机会。\x02\x03",

            "#10800F在那之前，我会在遥远之地\x01",
            "继续关注你们的。\x02\x03",

            "看着你们那徒劳无功的挣扎。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x102,
        "#00106F#12P#N………贝尔…………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0310
    ChrTalk(
        0x9,
        "#05808F#6P#N……………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0311
    ChrTalk(
        0xA,
        (
            "#10806F#5P另外，希望你们不要\x01",
            "对我父亲处以极刑。\x02\x03",

            "#10800F在克洛斯贝尔的复兴过程中，\x01",
            "他应该可以派上一些用场。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 3000, 5320, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(21500, 2000)
    Sleep(1000)
    BeginChrThread(0xA, 0, 0, 77)
    WaitChrThread(0xA, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0312
    ChrTalk(
        0xA,
        "#10809F#3800V#5P#40W#30A那么，就请各位多多保重了。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    StopBGM(0x1388)
    SetCameraDistance(20500, 3000)
    StopSound(832, 1000, 90)
    Sound(936, 0, 100, 0)
    StopEffect(0x0, 0x2)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
    Sleep(1500)
    SetChrFlags(0xA, 0x80)
    OP_6F(0x79)
    WaitBGM()
    OP_68(0, 800, 5320, 4500)
    MoveCamera(0, 6, 0, 4500)
    OP_6E(700, 4500)
    SetCameraDistance(30180, 4500)
    Sleep(4000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    Sleep(500)

    #C0313
    ChrTalk(
        0x101,
        "#00008F#5P#30W……………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B615")
    OP_FC(0x5)
    Jump("loc_B618")

    label("loc_B615")

    OP_FC(0xB)

    label("loc_B618")


    #C0314
    ChrTalk(
        0x102,
        (
            "#00106F#13P#30W…………贝尔…………\x01",
            "直到最后……都是这么任性……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7541", 0)
    Fade(500)
    OP_68(1910, 2500, -12300, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13910, 0)
    SetChrPos(0x101, 0, 950, -13000, 0)
    BeginChrThread(0x101, 0, 0, 83)
    Sleep(1200)

    def lambda_B6BB():

        label("loc_B6BB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B6BB")

    QueueWorkItem2(0x9, 2, lambda_B6BB)
    Sleep(300)

    def lambda_B6D0():

        label("loc_B6D0")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B6D0")

    QueueWorkItem2(0x102, 2, lambda_B6D0)
    Sleep(50)

    def lambda_B6E5():

        label("loc_B6E5")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B6E5")

    QueueWorkItem2(0x103, 2, lambda_B6E5)
    Sleep(50)

    def lambda_B6FA():

        label("loc_B6FA")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B6FA")

    QueueWorkItem2(0x104, 2, lambda_B6FA)
    Sleep(50)

    def lambda_B70F():

        label("loc_B70F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B70F")

    QueueWorkItem2(0xF4, 2, lambda_B70F)
    Sleep(50)

    def lambda_B724():

        label("loc_B724")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B724")

    QueueWorkItem2(0xF5, 2, lambda_B724)
    Sleep(50)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    EndChrThread(0x9, 0x2)
    Sound(802, 0, 50, 0)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x1)
    Sleep(500)
    OP_63(0x101, 0x96, 1500, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7B9")
    BeginChrThread(0x102, 0, 0, 84)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_B97D")

    label("loc_B7B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7F1")
    BeginChrThread(0x102, 0, 0, 85)
    BeginChrThread(0x103, 0, 0, 84)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_B97D")

    label("loc_B7F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B829")
    BeginChrThread(0x102, 0, 0, 86)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 84)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_B97D")

    label("loc_B829")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B89C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B873")
    BeginChrThread(0x102, 0, 0, 87)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 84)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_B897")

    label("loc_B873")

    BeginChrThread(0x102, 0, 0, 88)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 84)
    BeginChrThread(0x9, 0, 0, 89)

    label("loc_B897")

    Jump("loc_B97D")

    label("loc_B89C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B90F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B8E6")
    BeginChrThread(0x102, 0, 0, 87)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 84)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_B90A")

    label("loc_B8E6")

    BeginChrThread(0x102, 0, 0, 88)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 84)
    BeginChrThread(0x9, 0, 0, 89)

    label("loc_B90A")

    Jump("loc_B97D")

    label("loc_B90F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B97D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B959")
    BeginChrThread(0x102, 0, 0, 87)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 84)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_B97D")

    label("loc_B959")

    BeginChrThread(0x102, 0, 0, 88)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 84)
    BeginChrThread(0x9, 0, 0, 89)

    label("loc_B97D")

    Sleep(300)
    OP_68(7610, 2000, -10530, 5500)
    MoveCamera(49, 30, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(13000, 3500)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    SetCameraDistance(10000, 120000)

    #C0315
    ChrTalk(
        0x101,
        (
            "#00004F#5P#30W……嗯，\x01",
            "的确不是致命伤。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0xE1, 0x1F4)
    SetChrChipByIndex(0x101, 0x26)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1000)
    SetChrSubChip(0x101, 0x5)
    OP_93(0x9, 0xE1, 0x1F4)
    SetChrChipByIndex(0x9, 0x27)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x1000)
    SetChrSubChip(0x9, 0x0)
    Sleep(150)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAA8")

    def lambda_BA4B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BA4B)

    def lambda_BA58():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BA58)
    Sleep(50)

    def lambda_BA68():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BA68)
    Sleep(50)

    def lambda_BA78():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_BA78)
    Sleep(50)

    def lambda_BA88():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_BA88)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_BE34")

    label("loc_BAA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB19")

    def lambda_BABC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BABC)

    def lambda_BAC9():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BAC9)
    Sleep(50)

    def lambda_BAD9():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BAD9)
    Sleep(50)

    def lambda_BAE9():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_BAE9)
    Sleep(50)

    def lambda_BAF9():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_BAF9)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_BE34")

    label("loc_BB19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB8A")

    def lambda_BB2D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BB2D)

    def lambda_BB3A():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BB3A)
    Sleep(50)

    def lambda_BB4A():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BB4A)
    Sleep(50)

    def lambda_BB5A():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_BB5A)
    Sleep(50)

    def lambda_BB6A():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_BB6A)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_BE34")

    label("loc_BB8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC6F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC0D")

    def lambda_BBB0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_BBB0)

    def lambda_BBBD():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BBBD)
    Sleep(50)

    def lambda_BBCD():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BBCD)
    Sleep(50)

    def lambda_BBDD():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BBDD)
    Sleep(50)

    def lambda_BBED():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_BBED)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_BC6A")

    label("loc_BC0D")


    def lambda_BC12():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_BC12)

    def lambda_BC1F():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BC1F)
    Sleep(50)

    def lambda_BC2F():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BC2F)
    Sleep(50)

    def lambda_BC3F():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BC3F)
    Sleep(50)

    def lambda_BC4F():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_BC4F)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)

    label("loc_BC6A")

    Jump("loc_BE34")

    label("loc_BC6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD54")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCF2")

    def lambda_BC95():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_BC95)

    def lambda_BCA2():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BCA2)
    Sleep(50)

    def lambda_BCB2():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BCB2)
    Sleep(50)

    def lambda_BCC2():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BCC2)
    Sleep(50)

    def lambda_BCD2():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_BCD2)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_BD4F")

    label("loc_BCF2")


    def lambda_BCF7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_BCF7)

    def lambda_BD04():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BD04)
    Sleep(50)

    def lambda_BD14():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BD14)
    Sleep(50)

    def lambda_BD24():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BD24)
    Sleep(50)

    def lambda_BD34():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_BD34)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)

    label("loc_BD4F")

    Jump("loc_BE34")

    label("loc_BD54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE34")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BDD7")

    def lambda_BD7A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_BD7A)

    def lambda_BD87():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BD87)
    Sleep(50)

    def lambda_BD97():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BD97)
    Sleep(50)

    def lambda_BDA7():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BDA7)
    Sleep(50)

    def lambda_BDB7():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_BDB7)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_BE34")

    label("loc_BDD7")


    def lambda_BDDC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_BDDC)

    def lambda_BDE9():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BDE9)
    Sleep(50)

    def lambda_BDF9():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BDF9)
    Sleep(50)

    def lambda_BE09():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BE09)
    Sleep(50)

    def lambda_BE19():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_BE19)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)

    label("loc_BE34")


    #C0316
    ChrTalk(
        0x101,
        (
            "#00000F#11P各位，我们合力\x01",
            "把伊安律师抬回梅尔卡瓦吧。\x02\x03",

            "另外，还要将亚利欧斯先生他们\x01",
            "抬回去救治。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF16")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BEC3")
    OP_FC(0xC)
    Jump("loc_BEC6")

    label("loc_BEC3")

    OP_FC(0x6)

    label("loc_BEC6")


    #C0317
    ChrTalk(
        0x10A,
        (
            "#00604F#13P再过几个小时，\x01",
            "『大树』就要崩塌了，\x01",
            "看来必须抓紧时间了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C03B")

    label("loc_BF16")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BFAA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF3D")
    OP_FC(0x5)
    Jump("loc_BF5A")

    label("loc_BF3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF57")
    OP_FC(0xC)
    Jump("loc_BF5A")

    label("loc_BF57")

    OP_FC(0x6)

    label("loc_BF5A")


    #C0318
    ChrTalk(
        0x106,
        (
            "#10700F#13P再过几个小时，\x01",
            "『大树』就将崩塌，\x01",
            "看来我们必须要抓紧时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C03B")

    label("loc_BFAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C03B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFD1")
    OP_FC(0x5)
    Jump("loc_BFEE")

    label("loc_BFD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BFEB")
    OP_FC(0xC)
    Jump("loc_BFEE")

    label("loc_BFEB")

    OP_FC(0x6)

    label("loc_BFEE")


    #C0319
    ChrTalk(
        0x109,
        (
            "#10100F#13P再过几个小时，\x01",
            "『大树』就会崩塌，\x01",
            "看来我们必须得抓紧时间呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C03B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0B6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C062")
    OP_FC(0x5)
    Jump("loc_C07F")

    label("loc_C062")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C07C")
    OP_FC(0xC)
    Jump("loc_C07F")

    label("loc_C07C")

    OP_FC(0x6)

    label("loc_C07F")


    #C0320
    ChrTalk(
        0x105,
        (
            "#10404F#13P联络阿巴斯和其他人，\x01",
            "分头行动吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1B5")

    label("loc_C0B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C137")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0DD")
    OP_FC(0x5)
    Jump("loc_C0FA")

    label("loc_C0DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0F7")
    OP_FC(0xC)
    Jump("loc_C0FA")

    label("loc_C0F7")

    OP_FC(0x6)

    label("loc_C0FA")


    #C0321
    ChrTalk(
        0x109,
        (
            "#10104F#13P联络梅尔卡瓦上的人，\x01",
            "分头行动比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1B5")

    label("loc_C137")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1B5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C15E")
    OP_FC(0x5)
    Jump("loc_C17B")

    label("loc_C15E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C178")
    OP_FC(0xC)
    Jump("loc_C17B")

    label("loc_C178")

    OP_FC(0x6)

    label("loc_C17B")


    #C0322
    ChrTalk(
        0x106,
        (
            "#10704F#13P联络梅尔卡瓦上的各位，\x01",
            "分头行动比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1B5")

    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1CF")
    OP_FC(0x5)
    Jump("loc_C1D2")

    label("loc_C1CF")

    OP_FC(0x6)

    label("loc_C1D2")


    #C0323
    ChrTalk(
        0x103,
        (
            "#00206F#13P话说回来……\x02\x03",

            "#00202F玛丽亚贝尔小姐直到最后\x01",
            "都保持着本性。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C234")
    OP_FC(0x5)
    Jump("loc_C237")

    label("loc_C234")

    OP_FC(0xC)

    label("loc_C237")


    #C0324
    ChrTalk(
        0x104,
        (
            "#00306F#13P嗯，虽然她做了那么过分的事，\x01",
            "但不知为何，却无法从骨子里憎恨她……\x02\x03",

            "#00302F这也算是个人魅力的一种吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2C3")
    OP_FC(0x6)
    Jump("loc_C370")

    label("loc_C2C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2DA")
    OP_FC(0xC)
    Jump("loc_C370")

    label("loc_C2DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C30B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C303")
    OP_FC(0xC)
    Jump("loc_C306")

    label("loc_C303")

    OP_FC(0x6)

    label("loc_C306")

    Jump("loc_C370")

    label("loc_C30B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C33C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C334")
    OP_FC(0xC)
    Jump("loc_C337")

    label("loc_C334")

    OP_FC(0x6)

    label("loc_C337")

    Jump("loc_C370")

    label("loc_C33C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C36D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C365")
    OP_FC(0xC)
    Jump("loc_C368")

    label("loc_C365")

    OP_FC(0x6)

    label("loc_C368")

    Jump("loc_C370")

    label("loc_C36D")

    OP_FC(0x5)

    label("loc_C370")


    #C0325
    ChrTalk(
        0x102,
        (
            "#00106F#13P贝尔她……\x01",
            "完全忠于自己的想法与欲望。\x02\x03",

            "#00103F一旦下定决心去做，\x01",
            "就会不择手段，不达目的不肯罢休，\x01",
            "绝不会有丝毫踌躇……\x02\x03",

            "#00108F即使孤军奋战，她也毫不在意……\x02\x03",

            "#00101F但是……并非所有人\x01",
            "都像贝尔一样坚强。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#00006F#11P嗯，正因如此……\x01",
            "人才需要亲人和朋友。\x02\x03",

            "#00008F只有与亲人和朋友在一起，我们才能跨越壁障，\x01",
            "抓住未知的明日之光……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4E3")
    OP_FC(0x5)
    Jump("loc_C4E6")

    label("loc_C4E3")

    OP_FC(0xC)

    label("loc_C4E6")


    #C0327
    ChrTalk(
        0x104,
        (
            "#00304F#13P嗯，虽然未来的光明\x01",
            "离我们还很遥远……\x02\x03",

            "#00300F但我总觉得\x01",
            "一定会有办法的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C557")
    OP_FC(0x5)
    Jump("loc_C55A")

    label("loc_C557")

    OP_FC(0x6)

    label("loc_C55A")


    #C0328
    ChrTalk(
        0x103,
        "#00214F#13P……是的……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C768")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5A0")
    OP_FC(0x5)
    Jump("loc_C5BD")

    label("loc_C5A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C5BA")
    OP_FC(0xC)
    Jump("loc_C5BD")

    label("loc_C5BA")

    OP_FC(0x6)

    label("loc_C5BD")


    #C0329
    ChrTalk(
        0x109,
        (
            "#10102F#13P光靠我们在场的几位，\x01",
            "就能完成如此艰巨的任务！\x02\x03",

            "#10109F只要克洛斯贝尔的各位团结一心，\x01",
            "一定能够排除万难！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C6A5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C65C")
    OP_FC(0x5)
    Jump("loc_C679")

    label("loc_C65C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C676")
    OP_FC(0xC)
    Jump("loc_C679")

    label("loc_C676")

    OP_FC(0x6)

    label("loc_C679")


    #C0330
    ChrTalk(
        0x105,
        "#10404F#13P呵呵，或许正如你所说。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C763")

    label("loc_C6A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C713")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6CC")
    OP_FC(0x5)
    Jump("loc_C6E9")

    label("loc_C6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C6E6")
    OP_FC(0xC)
    Jump("loc_C6E9")

    label("loc_C6E6")

    OP_FC(0x6)

    label("loc_C6E9")


    #C0331
    ChrTalk(
        0x106,
        "#10709F#13P呵呵……正是如此啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C763")

    label("loc_C713")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C763")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C73D")
    OP_FC(0xC)
    Jump("loc_C740")

    label("loc_C73D")

    OP_FC(0x6)

    label("loc_C740")


    #C0332
    ChrTalk(
        0x10A,
        "#00604F#13P呵……的确如此啊。\x02",
    )

    CloseMessageWindow()

    label("loc_C763")

    Jump("loc_C9CD")

    label("loc_C768")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8E5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C78F")
    OP_FC(0x5)
    Jump("loc_C7AC")

    label("loc_C78F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C7A9")
    OP_FC(0xC)
    Jump("loc_C7AC")

    label("loc_C7A9")

    OP_FC(0x6)

    label("loc_C7AC")


    #C0333
    ChrTalk(
        0x105,
        (
            "#10404F#13P是啊，光靠我们几人，\x01",
            "就能完成如此壮举。\x02\x03",

            "#10402F如果克洛斯贝尔的所有人齐心协力，\x01",
            "总会有办法的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C890")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C845")
    OP_FC(0x5)
    Jump("loc_C862")

    label("loc_C845")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C85F")
    OP_FC(0xC)
    Jump("loc_C862")

    label("loc_C85F")

    OP_FC(0x6)

    label("loc_C862")


    #C0334
    ChrTalk(
        0x106,
        "#10709F#13P呵呵……或许正是如此啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C8E0")

    label("loc_C890")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8E0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8BA")
    OP_FC(0xC)
    Jump("loc_C8BD")

    label("loc_C8BA")

    OP_FC(0x6)

    label("loc_C8BD")


    #C0335
    ChrTalk(
        0x10A,
        "#00604F#13P呵……的确如此啊。\x02",
    )

    CloseMessageWindow()

    label("loc_C8E0")

    Jump("loc_C9CD")

    label("loc_C8E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8FC")
    OP_FC(0x5)
    Jump("loc_C919")

    label("loc_C8FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C916")
    OP_FC(0xC)
    Jump("loc_C919")

    label("loc_C916")

    OP_FC(0x6)

    label("loc_C919")


    #C0336
    ChrTalk(
        0x106,
        (
            "#10704F#13P……光靠我们在场的诸位，\x01",
            "就能有如此作为。\x02\x03",

            "#10702F如果克洛斯贝尔的各位能够齐心协力，\x01",
            "总会有办法的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C9A7")
    OP_FC(0xC)
    Jump("loc_C9AA")

    label("loc_C9A7")

    OP_FC(0x6)

    label("loc_C9AA")


    #C0337
    ChrTalk(
        0x10A,
        "#00604F#13P呵……的确如此啊。\x02",
    )

    CloseMessageWindow()

    label("loc_C9CD")

    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x9, 1, 0, 90)
    WaitChrThread(0x9, 1)
    OP_C9(0x0, 0x80000000)

    #C0338
    ChrTalk(
        0x9,
        (
            "#05821F#3655V#5P#40W#37A琪雅……\x01",
            "……琪雅也会加油的……！\x02\x03",

            "#05819F#3656V#42A为了和大家一起……\x01",
            "……守护最重要的地方！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA75")
    OP_FC(0x6)
    Jump("loc_CB22")

    label("loc_CA75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA8C")
    OP_FC(0xC)
    Jump("loc_CB22")

    label("loc_CA8C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CABD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAB5")
    OP_FC(0xC)
    Jump("loc_CAB8")

    label("loc_CAB5")

    OP_FC(0x6)

    label("loc_CAB8")

    Jump("loc_CB22")

    label("loc_CABD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAEE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAE6")
    OP_FC(0xC)
    Jump("loc_CAE9")

    label("loc_CAE6")

    OP_FC(0x6)

    label("loc_CAE9")

    Jump("loc_CB22")

    label("loc_CAEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB1F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CB17")
    OP_FC(0xC)
    Jump("loc_CB1A")

    label("loc_CB17")

    OP_FC(0x6)

    label("loc_CB1A")

    Jump("loc_CB22")

    label("loc_CB1F")

    OP_FC(0x5)

    label("loc_CB22")


    #C0339
    ChrTalk(
        0x102,
        "#00102F#3410V#13P#30W#25A琪雅……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB63")
    OP_FC(0x5)
    Jump("loc_CB66")

    label("loc_CB63")

    OP_FC(0x6)

    label("loc_CB66")


    #C0340
    ChrTalk(
        0x103,
        "#00204F#2697V#13P#30W#25A……你可以以一顶千了。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBB5")
    OP_FC(0x5)
    Jump("loc_CBB8")

    label("loc_CBB5")

    OP_FC(0xC)

    label("loc_CBB8")


    #C0341
    ChrTalk(
        0x104,
        "#00309F#2777V#13P#30W#25A哈哈，要的就是这股干劲啊。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 1, 0, 91)
    BeginChrThread(0x9, 1, 0, 92)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x9, 1)

    #C0342
    ChrTalk(
        0x101,
        "#00009F#3337V#11P#25A嗯，一起加油吧。\x02",
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 93)
    BeginChrThread(0x9, 1, 0, 94)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x9, 1)
    Sleep(800)

    #C0343
    ChrTalk(
        0x101,
        (
            "#00004F#3338V#11P#30W#22A特别任务支援科，收队。\x02\x03",

            "#3339V#11P#30W#45A将亚里欧斯先生等人带回之后，\x01",
            "我们就乘坐梅尔卡瓦离开『大树』。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    SetCameraDistance(10000, 1000)
    BeginChrThread(0x101, 1, 0, 96)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0344
    ChrTalk(
        0x101,
        "#00000F#3340V#11P#30W#35A回去吧，回到我们的克洛斯贝尔……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(13820, 4300)
    Sleep(300)
    FadeToDark(4000, 16777215, -1)
    StopBGM(0x1F40)
    Sleep(4000)
    Sleep(1000)
    OP_C9(0x0, 0x10)
    FadeToBright(3000, 16777215)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_ed.pmf", 0x35, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    StopBGM(0x1F4)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    OP_CB(0x2, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(4000)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x640, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x640, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    OP_E0(0x23, 0x0)
    OP_E0(0x1A, 0x0)
    OP_E0(0x1B, 0x0)
    OP_E0(0x80, 0x0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2C, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF69")
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "ＥＸＴＲＡ模式开放。\x02",
        )
    )

    CloseMessageWindow()

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "可以从标题画面\x01",
            "进入ＥＸＴＲＡ模式。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    label("loc_CF69")

    SetMessageWindowPos(14, 280, 60, 3)

    #A0347
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　　　 　　 ～　关于通关存档的保存　～\x01",
            "　　 　　　　建立通关存档后，可以在标题画面中读取，\x01",
            "　　  　　　　 从而继承各项数据，开始二周目游戏。",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveClearMenu()
    OP_57(0x0)
    OP_5A()
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x1, 0x10)
    OP_B9(0x0)
    Return()

    # Function_71_9296 end

    def Function_72_D050(): pass

    label("Function_72_D050")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)), "loc_D096")
    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0x1)
    Sleep(167)
    SetChrSubChip(0xFE, 0x2)
    Sleep(167)
    SetChrSubChip(0xFE, 0x3)
    Sleep(167)
    SetChrSubChip(0xFE, 0x4)
    Sleep(167)
    SetChrSubChip(0xFE, 0x3)
    Sleep(167)
    SetChrSubChip(0xFE, 0x2)
    Sleep(167)
    SetChrSubChip(0xFE, 0x1)
    Sleep(167)
    Jump("Function_72_D050")

    label("loc_D096")

    Return()

    # Function_72_D050 end

    def Function_73_D097(): pass

    label("Function_73_D097")

    OP_96(0xFE, 0x0, 0x3B6, 0xFFFFCF2C, 0x12C, 0x1)
    SetChrSubChip(0xFE, 0x5)
    Sleep(167)
    SetChrSubChip(0xFE, 0x6)
    Sleep(167)
    SetChrSubChip(0xFE, 0x7)
    Sleep(167)
    SetChrSubChip(0xFE, 0x8)
    Sleep(167)
    SetChrSubChip(0xFE, 0x9)
    Sleep(167)
    SetChrSubChip(0xFE, 0xA)
    Sleep(167)
    SetChrSubChip(0xFE, 0xB)
    Sleep(500)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    SetChrFlags(0x10, 0x80)
    Sleep(100)
    Sound(326, 0, 30, 0)
    Return()

    # Function_73_D097 end

    def Function_74_D0F5(): pass

    label("Function_74_D0F5")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x18)
    Sleep(125)
    SetChrSubChip(0xFE, 0x19)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(750)
    Return()

    # Function_74_D0F5 end

    def Function_75_D120(): pass

    label("Function_75_D120")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1C)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(750)
    Return()

    # Function_75_D120 end

    def Function_76_D14B(): pass

    label("Function_76_D14B")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1F)
    Sleep(125)
    SetChrSubChip(0xFE, 0x20)
    Sleep(375)
    Return()

    # Function_76_D14B end

    def Function_77_D16F(): pass

    label("Function_77_D16F")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(898, 0, 60, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(300)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(571)
    Return()

    # Function_77_D16F end

    def Function_78_D1C3(): pass

    label("Function_78_D1C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D1D5")
    Sleep(50)

    label("loc_D1D5")

    OP_9B(0x1, 0xFE, 0x0, 0x640, 0xFA0, 0x0)
    Return()

    # Function_78_D1C3 end

    def Function_79_D1E5(): pass

    label("Function_79_D1E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D1F7")
    Sleep(100)

    label("loc_D1F7")

    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
    Return()

    # Function_79_D1E5 end

    def Function_80_D207(): pass

    label("Function_80_D207")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D219")
    Sleep(150)

    label("loc_D219")

    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
    Return()

    # Function_80_D207 end

    def Function_81_D229(): pass

    label("Function_81_D229")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D24D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D24D")
    Sleep(200)

    label("loc_D24D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D271")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D271")
    Sleep(200)

    label("loc_D271")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D295")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D295")
    Sleep(200)

    label("loc_D295")

    OP_9B(0x1, 0xFE, 0x15E, 0x5DC, 0xFA0, 0x0)
    Return()

    # Function_81_D229 end

    def Function_82_D2A5(): pass

    label("Function_82_D2A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D2C9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D2C9")
    Sleep(250)

    label("loc_D2C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D2ED")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D2ED")
    Sleep(250)

    label("loc_D2ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D311")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D311")
    Sleep(250)

    label("loc_D311")

    OP_9B(0x1, 0xFE, 0xA, 0x5DC, 0xFA0, 0x0)
    Return()

    # Function_82_D2A5 end

    def Function_83_D321(): pass

    label("Function_83_D321")

    TurnDirection(0xFE, 0x8, 500)
    Sleep(450)
    OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x15E, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x1964, 0x7D0, 0x0)
    Return()

    # Function_83_D321 end

    def Function_84_D368(): pass

    label("Function_84_D368")

    Sleep(200)
    OP_96(0xFE, 0x1C5C, 0x3B6, 0xFFFFDD14, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_84_D368 end

    def Function_85_D387(): pass

    label("Function_85_D387")

    Sleep(1100)
    OP_96(0xFE, 0x16A8, 0x406, 0xFFFFDC60, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_85_D387 end

    def Function_86_D3A6(): pass

    label("Function_86_D3A6")

    Sleep(50)
    OP_96(0xFE, 0x1F04, 0x3B6, 0xFFFFD1D4, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_86_D3A6 end

    def Function_87_D3C5(): pass

    label("Function_87_D3C5")

    Sleep(350)
    OP_96(0xFE, 0x19C8, 0x3B6, 0xFFFFD210, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_87_D3C5 end

    def Function_88_D3E4(): pass

    label("Function_88_D3E4")

    Sleep(1450)
    OP_96(0xFE, 0x1608, 0x3B6, 0xFFFFD670, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_88_D3E4 end

    def Function_89_D403(): pass

    label("Function_89_D403")

    Sleep(750)
    OP_9B(0x1, 0xFE, 0x0, 0x4E2, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1C52, 0x1388, 0x1)
    Sound(811, 0, 70, 0)
    Sound(898, 0, 50, 0)

    def lambda_D435():
        OP_A6(0xFE, 0x64, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D435)
    Sleep(50)

    def lambda_D451():
        OP_A6(0xFE, 0x32, 0x0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D451)
    Sleep(450)
    OP_9B(0x1, 0xFE, 0x109, 0x96, 0x3E8, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_89_D403 end

    def Function_90_D47F(): pass

    label("Function_90_D47F")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(625)
    Sound(812, 0, 100, 0)
    Sound(802, 0, 30, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    SetChrSubChip(0xFE, 0x4)
    Sleep(125)
    SetChrSubChip(0xFE, 0x5)
    Sleep(375)
    Return()

    # Function_90_D47F end

    def Function_91_D4C4(): pass

    label("Function_91_D4C4")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(812, 0, 100, 0)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(120)
    SetChrSubChip(0xFE, 0x6)
    Sleep(120)
    SetChrSubChip(0xFE, 0x7)
    Sleep(120)
    SetChrSubChip(0xFE, 0x8)
    Sleep(120)
    SetChrSubChip(0xFE, 0x9)
    Sleep(300)
    Sound(898, 0, 50, 0)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    SetChrSubChip(0xFE, 0xB)
    Sleep(120)
    SetChrSubChip(0xFE, 0xC)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    SetChrSubChip(0xFE, 0xB)
    Sleep(120)
    SetChrSubChip(0xFE, 0xC)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    Return()

    # Function_91_D4C4 end

    def Function_92_D54E(): pass

    label("Function_92_D54E")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x5)
    Sleep(120)
    SetChrSubChip(0xFE, 0x6)
    Sleep(120)
    SetChrSubChip(0xFE, 0x7)
    Sleep(120)
    SetChrSubChip(0xFE, 0x8)
    Sleep(120)
    SetChrSubChip(0xFE, 0x9)
    Sleep(300)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    SetChrSubChip(0xFE, 0xB)
    Sleep(120)
    SetChrSubChip(0xFE, 0xC)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    SetChrSubChip(0xFE, 0xB)
    Sleep(120)
    SetChrSubChip(0xFE, 0xC)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    Return()

    # Function_92_D54E end

    def Function_93_D5C6(): pass

    label("Function_93_D5C6")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xC)
    Sleep(200)
    SetChrSubChip(0xFE, 0xD)
    Sleep(200)
    SetChrSubChip(0xFE, 0xE)
    Sleep(400)
    Return()

    # Function_93_D5C6 end

    def Function_94_D5EA(): pass

    label("Function_94_D5EA")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xC)
    Sleep(200)
    SetChrSubChip(0xFE, 0xD)
    Sleep(200)
    SetChrSubChip(0xFE, 0xE)
    Sleep(400)
    Return()

    # Function_94_D5EA end

    def Function_95_D60E(): pass

    label("Function_95_D60E")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0xF)
    Sleep(143)
    SetChrSubChip(0xFE, 0x10)
    Sleep(429)
    Return()

    # Function_95_D60E end

    def Function_96_D632(): pass

    label("Function_96_D632")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x10)
    Sleep(143)
    SetChrSubChip(0xFE, 0x11)
    Sleep(143)
    SetChrSubChip(0xFE, 0x12)
    Sleep(429)
    Return()

    # Function_96_D632 end

    def Function_97_D65C(): pass

    label("Function_97_D65C")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_D67E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D7E7")

    label("loc_D67E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_D696")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D7E7")

    label("loc_D696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_D6AE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D7E7")

    label("loc_D6AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D6D1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D7E7")

    label("loc_D6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D6F4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D7E7")

    label("loc_D6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D717")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D7E7")

    label("loc_D717")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D735")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D7E7")

    label("loc_D735")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D753")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D7E7")

    label("loc_D753")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D771")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D7E7")

    label("loc_D771")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D79A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D7E7")

    label("loc_D79A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7C3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D7E7")

    label("loc_D7C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7E7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D7E7")

    Return()

    # Function_97_D65C end

    SaveToFile()

Try(main)
