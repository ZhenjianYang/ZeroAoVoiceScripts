from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0800.bin",                # FileName
        "c0800",                    # MapName
        "c0800",                    # Location
        0x0003,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 1],
    )

    BuildStringList((
        "c0800",                  # 0
        "列车",                   # 1
        "列车",                   # 2
        "琪雅",                   # 3
        "芙兰",                   # 4
        "赛尔盖科长",             # 5
        "奥斯本宰相",             # 6
        "雷克特",                 # 7
        "奥利维特皇子",           # 8
        "穆拉少校",               # 9
        "乘客",                   # 10
        "乘客",                   # 11
        "乘客",                   # 12
        "乘客",                   # 13
        "乘客",                   # 14
        "乘客",                   # 15
        "乘客",                   # 16
        "乘客",                   # 17
        "站员",                   # 18
        "帝国军士官",             # 19
        "帝国军士官",             # 20
        "帝国军士官",             # 21
        "帝国军士官",             # 22
        "帝国军士官",             # 23
        "帝国军士官",             # 24
        "马洛安检官",             # 25
        "雷蒙德搜查官",           # 26
        "假货商",                 # 27
        "帝国商人",               # 28
        "列车",                   # 29
        "SE控制",                 # 30
    ))

    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(10000,   0,       -27000,  2000,    10000,   1200,    -26300,  0x007C, 0,  43, 0x0000)

    ChipFrameInfo(1252, 0)                                       # 0

    ScpFunction((
        "Function_0_4E4",          # 00, 0
        "Function_1_58C",          # 01, 1
        "Function_2_772",          # 02, 2
        "Function_3_2EB4",         # 03, 3
        "Function_4_2EF8",         # 04, 4
        "Function_5_2F4E",         # 05, 5
        "Function_6_2FA4",         # 06, 6
        "Function_7_2FFF",         # 07, 7
        "Function_8_3052",         # 08, 8
        "Function_9_309E",         # 09, 9
        "Function_10_30F2",        # 0A, 10
        "Function_11_3122",        # 0B, 11
        "Function_12_388D",        # 0C, 12
        "Function_13_38D9",        # 0D, 13
        "Function_14_3915",        # 0E, 14
        "Function_15_392C",        # 0F, 15
        "Function_16_3968",        # 10, 16
        "Function_17_397F",        # 11, 17
        "Function_18_39BB",        # 12, 18
        "Function_19_39D2",        # 13, 19
        "Function_20_3A1F",        # 14, 20
        "Function_21_3A2F",        # 15, 21
        "Function_22_3A6B",        # 16, 22
        "Function_23_3A7B",        # 17, 23
        "Function_24_3A92",        # 18, 24
        "Function_25_3ACE",        # 19, 25
        "Function_26_3AE5",        # 1A, 26
        "Function_27_3B21",        # 1B, 27
        "Function_28_3B38",        # 1C, 28
        "Function_29_3B74",        # 1D, 29
        "Function_30_3B8B",        # 1E, 30
        "Function_31_3BD8",        # 1F, 31
        "Function_32_3BE8",        # 20, 32
        "Function_33_3C24",        # 21, 33
        "Function_34_3C34",        # 22, 34
        "Function_35_3C50",        # 23, 35
        "Function_36_3C67",        # 24, 36
        "Function_37_3CAE",        # 25, 37
        "Function_38_3CF5",        # 26, 38
        "Function_39_6055",        # 27, 39
        "Function_40_6086",        # 28, 40
        "Function_41_64C2",        # 29, 41
        "Function_42_7387",        # 2A, 42
        "Function_43_7B8C",        # 2B, 43
        "Function_44_7DB7",        # 2C, 44
        "Function_45_7DF4",        # 2D, 45
        "Function_46_A3A9",        # 2E, 46
        "Function_47_A3D2",        # 2F, 47
        "Function_48_A3FE",        # 30, 48
        "Function_49_A42A",        # 31, 49
        "Function_50_A45A",        # 32, 50
        "Function_51_A4B8",        # 33, 51
        "Function_52_A516",        # 34, 52
        "Function_53_A572",        # 35, 53
        "Function_54_A5E4",        # 36, 54
        "Function_55_A610",        # 37, 55
        "Function_56_A70E",        # 38, 56
    ))


    def Function_0_4E4(): pass

    label("Function_0_4E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4FB")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 2)
    Jump("loc_57A")

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_50F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 11)
    Jump("loc_57A")

    label("loc_50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_526")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 3)
    Event(0, 38)
    Jump("loc_57A")

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_53D")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 4)
    Event(0, 40)
    Jump("loc_57A")

    label("loc_53D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_554")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x0, 4)
    Event(0, 41)
    Jump("loc_57A")

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_56B")
    ClearScenarioFlags(0x22, 5)
    SetScenarioFlags(0x0, 5)
    Event(0, 45)
    Jump("loc_57A")

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_57A")
    ClearScenarioFlags(0x22, 6)
    Event(0, 55)

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58B")
    Event(0, 42)

    label("loc_58B")

    Return()

    # Function_0_4E4 end

    def Function_1_58C(): pass

    label("Function_1_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5A6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    Jump("loc_5BE")

    label("loc_5A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_5BE")
    SetScenarioFlags(0x0, 2)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_5BE")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D4")
    OP_66(0x0, 0x1)

    label("loc_5D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5E8")
    OP_24(0x343)
    ClearScenarioFlags(0x0, 2)
    Jump("loc_604")

    label("loc_5E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FE")
    OP_24(0x343)
    Jump("loc_604")

    label("loc_5FE")

    Sound(835, 1, 100, 0)

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62F")
    OP_7D(0xD2, 0xD2, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_664")
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_664")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x3, 0x1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 6)), scpexpr(EXPR_END)), "loc_702")
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    SetChrPos(0x8, 2000, -1550, -24100, 0)
    OP_D5(0x8, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x1, 0x9)
    SetChrPos(0x9, 54000, -1550, 8100, 0)
    OP_D5(0x9, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    Jump("loc_771")

    label("loc_702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_71C")
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    Jump("loc_771")

    label("loc_71C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_730")
    ClearMapObjFlags(0x3, 0x4)
    Jump("loc_771")

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_771")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_78(0x0, 0x8)
    SetChrPos(0x8, 38000, -1550, 8100, 0)
    OP_D5(0x8, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)

    label("loc_771")

    Return()

    # Function_1_58C end

    def Function_2_772(): pass

    label("Function_2_772")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    OP_32(0x1, 0x0, 0x32)
    OP_32(0x1, 0x5, 0x64)
    OP_42(0x1, 0x3FD, 0xFF)
    OP_42(0x1, 0x5DD, 0xFF)
    OP_42(0x1, 0x641, 0xFF)
    RemoveCraft(0x1, 0xFFFF)
    OP_38(0x1, 0x80, 0x2)
    OP_38(0x1, 0x83, 0x1)
    OP_38(0x1, 0x84, 0x1)
    OP_42(0x1, 0x80, 0x4)
    AddCraft(0x1, 0xA0)
    AddCraft(0x1, 0xA1)
    AddCraft(0x1, 0xA7)
    AddCraft(0x1, 0xA3)
    AddCraft(0x1, 0xA4)
    AddCraft(0x1, 0x11D)
    AddCraft(0x1, 0x11E)
    SetChrChipPat(0x1, 0x6, 0x11D)
    SetChrChipPat(0x1, 0x6, 0x11E)
    SetChrChipPat(0x1, 0x6, 0x120)
    SetChrChipPat(0x1, 0x6, 0x121)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_806")
    AddCraft(0x1, 0x1AE)
    AddCraft(0x0, 0x1AE)
    Jump("loc_824")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_81C")
    AddCraft(0x1, 0x19A)
    AddCraft(0x0, 0x19A)
    Jump("loc_824")

    label("loc_81C")

    AddCraft(0x1, 0x186)
    AddCraft(0x0, 0x186)

    label("loc_824")

    OP_32(0x4, 0x0, 0x32)
    OP_32(0x4, 0x5, 0x64)
    OP_42(0x4, 0x439, 0xFF)
    OP_42(0x4, 0x5DD, 0xFF)
    OP_42(0x4, 0x641, 0xFF)
    RemoveCraft(0x4, 0xFFFF)
    OP_38(0x4, 0x80, 0x2)
    OP_38(0x4, 0x82, 0x1)
    OP_38(0x4, 0x83, 0x1)
    OP_42(0x4, 0x7C, 0x3)
    AddCraft(0x4, 0xBE)
    AddCraft(0x4, 0xBF)
    AddCraft(0x4, 0xC0)
    AddCraft(0x4, 0x12C)
    SetChrChipPat(0x4, 0x6, 0x12C)
    SetChrChipPat(0x4, 0x6, 0x12F)
    OP_32(0xFF, 0xFE, 0x0)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08201.itc", 0x1F)
    LoadChrToIndex("chr/ch06900.itc", 0x20)
    LoadChrToIndex("chr/ch02500.itc", 0x21)
    LoadChrToIndex("apl/ch50380.itc", 0x22)
    LoadChrToIndex("chr/ch28300.itc", 0x23)
    LoadChrToIndex("chr/ch20102.itc", 0x24)
    LoadChrToIndex("chr/ch22002.itc", 0x25)
    LoadChrToIndex("chr/ch33002.itc", 0x26)
    LoadChrToIndex("chr/ch20000.itc", 0x27)
    LoadChrToIndex("chr/ch44000.itc", 0x28)
    LoadChrToIndex("chr/ch24400.itc", 0x29)
    LoadChrToIndex("chr/ch24500.itc", 0x2A)
    LoadChrToIndex("chr/ch27600.itc", 0x2B)
    LoadChrToIndex("apl/ch51020.itc", 0x2C)
    LoadChrToIndex("apl/ch51027.itc", 0x2D)
    LoadChrToIndex("apl/ch51712.itc", 0x2E)
    SoundLoad(452)
    SoundLoad(453)
    SoundLoad(3315)
    SoundLoad(3316)
    SoundLoad(3317)
    SoundLoad(3385)
    SoundLoad(3386)
    SoundLoad(3387)
    SoundLoad(3388)
    SoundLoad(3389)
    SoundLoad(3390)
    SoundLoad(2904)
    SoundLoad(2905)
    SoundLoad(2906)
    SoundLoad(2907)
    SoundLoad(2901)
    SoundLoad(3513)
    SoundLoad(3514)
    SoundLoad(3595)
    SoundLoad(3596)
    SoundLoad(3597)
    SoundLoad(2708)
    SoundLoad(2709)
    SoundLoad(2710)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis401.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01103.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00100.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10301.itp")
    CreatePortrait(5, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01000.itp")
    CreatePortrait(6, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01902.itp")
    SetChrPos(0x101, -10000, 0, 15000, 0)
    SetChrPos(0x109, -10000, 0, 15000, 0)
    SetChrPos(0x102, -10000, 0, 15000, 0)
    SetChrPos(0x105, -10000, 0, 15000, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 33100, 100, -14700, 0)
    SetChrChipByIndex(0x12, 0x25)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 20500, 100, -17200, 180)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 37300, 100, -14700, 0)
    SetChrChipByIndex(0x14, 0x27)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x14, 19700, 100, -9700, 180)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, 19700, 100, -9700, 180)
    SetChrChipByIndex(0x16, 0x29)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, 22700, 0, -9700, 180)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x17, 22700, 0, -9700, 180)
    SetChrChipByIndex(0x18, 0x2B)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x18, 32500, 0, -9700, 180)
    SetChrChipByIndex(0x19, 0x23)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 52500, 0, -13300, 45)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x1, 0x8)
    OP_49()
    SetChrPos(0x8, 7000, -1550, -8100, 0)
    OP_D5(0x8, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    SetChrPos(0x9, 54000, -1550, 8100, 0)
    OP_D5(0x9, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(65000, 10000, -11000, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(30000, 0)
    OP_F0(0x0, 0x1)
    OP_68(25000, 1500, -11000, 15000)
    MoveCamera(47, 17, 0, 15000)
    SetCameraDistance(50000, 15000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    Sound(801, 0, 100, 0)
    Sleep(2500)
    PlaceName2(340, 200, "c_plac00", 0x0, 0)
    Sleep(2500)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x169, 0x294, 0x0, 0x0)
    Sound(453, 0, 100, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(57000, 1500, -8500, 0)
    MoveCamera(53, 2, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(21000, 0)
    OP_68(10000, 500, -8500, 10000)
    MoveCamera(57, 12, 0, 10000)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x8, 3, 0, 3)
    WaitChrThread(0x8, 3)
    Sleep(300)
    Fade(500)
    OP_68(20500, 1300, -12800, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x8, 2000, -1550, -8100, 0)
    OP_0D()
    SetCameraDistance(19000, 6000)
    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)
    BeginChrThread(0x14, 3, 0, 6)
    Sleep(1000)
    BeginChrThread(0x16, 3, 0, 7)
    Sleep(500)
    BeginChrThread(0x15, 3, 0, 6)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 8)
    Sleep(2000)
    BeginChrThread(0x18, 3, 0, 9)
    Sleep(4000)
    BeginChrThread(0x101, 3, 0, 4)
    Sleep(800)
    BeginChrThread(0x109, 3, 0, 5)
    Sleep(1000)
    OP_68(7900, 1300, -12800, 8000)
    MoveCamera(39, 17, 0, 8000)
    SetCameraDistance(18000, 8000)
    WaitChrThread(0x101, 3)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -11000, 600, -16000, 270)
    OP_C9(0x0, 0x80000000)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #N0001
    NpcTalk(
        0xA,
        "少女的声音",
        "#4S#3595V#21A#30W罗伊德！！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0002
    ChrTalk(
        0x101,
        "#11P#00005F#3315V#30W啊……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xCF3)
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-8000, 1500, -16000, 0)
    MoveCamera(317, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    OP_68(3400, 900, -15400, 3000)
    MoveCamera(327, 27, 0, 3000)
    SetCameraDistance(14000, 3000)
    ClearChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_F96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F96)

    def lambda_FA7():
        OP_95(0xFE, 3250, 0, -15450, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FA7)
    Sleep(2000)

    def lambda_FC4():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFC3D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FC4)
    Sleep(50)
    Sound(3037, 255, 100, 0)    #voice#KeA
    BeginChrThread(0x109, 3, 0, 10)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x0)

    def lambda_FF9():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FF9)
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0003
    ChrTalk(
        0x101,
        (
            "#12P#00002F#3316V#30W琪雅……！\x01",
            "你是来接我的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCF4)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)

    def lambda_1062():
        OP_96(0xFE, 0xB54, 0x0, 0xFFFFC3D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1062)
    WaitChrThread(0xA, 1)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_82(0x32, 0x0, 0x7D0, 0x12C)

    #A0004
    AnonymousTalk(
        0xA,
        (
            "#3596V#30W嗯！\x01",
            "我听说你今天回来！\x02\x03",

            "#3597V没事吧！？\x01",
            "没有受伤吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xE0D)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0005
    ChrTalk(
        0x101,
        (
            "#12P#00004F嗯，没有啦。\x02\x03",

            "#00002F我回来了，琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xA,
        "#01109F#5P欢迎回来，罗伊德！\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x87, 0x1F4)
    Sleep(300)

    #C0007
    ChrTalk(
        0xA,
        (
            "#01121F#5P嘿嘿嘿……\x01",
            "诺艾尔，也欢迎你回来！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            "#12P#10109F啊哈哈……\x01",
            "我回来了，小琪雅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0xB, -8200, 600, -16400, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8)
    OP_C9(0x0, 0x80000000)

    #N0009
    NpcTalk(
        0xB,
        "年轻女孩的声音",
        "#2708V#18A#30W姐姐～～！！\x02",
    )
    #Auto
    Sleep(300)

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0xB, 0x8)

    def lambda_129E():
        OP_95(0xFE, 4350, 0, -16650, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_129E)
    Sleep(300)

    def lambda_12BB():

        label("loc_12BB")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_12BB")

    QueueWorkItem2(0xA, 2, lambda_12BB)

    def lambda_12CD():

        label("loc_12CD")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_12CD")

    QueueWorkItem2(0x101, 2, lambda_12CD)
    WaitChrThread(0xB, 1)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0x109, 0x10)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x20)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x0)
    EndChrThread(0xA, 0x2)
    EndChrThread(0x101, 0x2)

    def lambda_1319():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1319)
    Sound(811, 0, 100, 0)
    Sleep(500)

    #C0010
    ChrTalk(
        0x109,
        "#12P#10111F#3513V#30W哇哇，芙兰！？\x02",
    )

    CloseMessageWindow()
    OP_24(0xDB9)
    OP_CB(0x6, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x6, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x6, 0x3)
    OP_CC(0x0, 0x6, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(150)

    #A0011
    AnonymousTalk(
        0xB,
        (
            "#2709V#30W呜呜呜……！\x01",
            "姐姐你没事就好！\x02\x03",

            "#2710V欢迎回来！\x01",
            "没有受伤吧～！？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xA96)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x6, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x6, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x6, 0x3)
    OP_CC(0x0, 0x6, 0x0)

    #C0012
    ChrTalk(
        0x109,
        (
            "#12P#10102F嗯，你看啊，完全没有。\x02\x03",

            "#10106F话说回来，才几天不见而已，\x01",
            "不用那么夸张吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xB, 0x2)
    ClearChrFlags(0xB, 0x20)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x109, 0x10)
    ClearChrFlags(0x109, 0x2)
    ClearChrFlags(0x109, 0x20)

    def lambda_14C2():
        OP_96(0xFE, 0xFA0, 0x0, 0xFFFFBEC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14C2)
    WaitChrThread(0xB, 1)
    Sleep(150)

    #C0013
    ChrTalk(
        0xB,
        (
            "#01903F#5P姐姐你什么都不懂！\x01",
            "这不是时间的问题～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)
    Sleep(150)

    #C0014
    ChrTalk(
        0xB,
        "#6P#01909F对吧，小琪雅？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xA,
        "#5P#01101F对啊对啊，没错！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0016
    ChrTalk(
        0x101,
        "#00012F哈哈……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x109,
        (
            "#12P#10112F真有种回到家的\x01",
            "感觉呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x102, -9000, 600, -15600, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xC, -9700, 600, -16800, 90)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_1662")

    #N0018
    NpcTalk(
        0x102,
        "年轻女孩的声音",
        "#3385V罗伊德#30W……欢迎回来。\x02",
    )

    CloseMessageWindow()
    OP_24(0xD39)
    OP_C9(0x1, 0x80000000)
    Jump("loc_16A5")

    label("loc_1662")


    #N0019
    NpcTalk(
        0x102,
        "年轻女孩的声音",
        (
            "#3386V#30W呵呵……\x01",
            "你们两位都辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD3A)
    OP_C9(0x1, 0x80000000)

    label("loc_16A5")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_16DA():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_16DA)
    Sleep(50)

    def lambda_16EA():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16EA)
    Sleep(50)

    def lambda_16FA():
        OP_93(0xA, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_16FA)
    Sleep(50)

    def lambda_170A():
        OP_93(0xB, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_170A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)

    #C0020
    ChrTalk(
        0x101,
        "#12P#00002F啊……\x02",
    )

    CloseMessageWindow()
    OP_68(-6900, 1400, -16000, 3000)
    MoveCamera(321, 21, 0, 3000)
    SetCameraDistance(14500, 3000)
    Sleep(1300)

    def lambda_1769():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1769)

    def lambda_177A():
        OP_96(0xFE, 0xFFFFE124, 0x258, 0xFFFFC374, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_177A)
    Sleep(100)

    def lambda_1797():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1797)

    def lambda_17A8():
        OP_96(0xFE, 0xFFFFDE68, 0x258, 0xFFFFBF8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_17A8)
    WaitChrThread(0x102, 1)
    WaitChrThread(0xC, 1)
    OP_6F(0x79)
    Sleep(300)

    def lambda_17CF():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFC374, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17CF)
    Sleep(100)

    def lambda_17EC():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFFBF8C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_17EC)
    Sleep(2500)
    Fade(500)
    OP_68(2600, 900, -15600, 0)
    MoveCamera(325, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(14000, 1500)

    def lambda_1845():
        OP_96(0xFE, 0x1004, 0x0, 0xFFFFC5CC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1845)
    Sleep(50)

    def lambda_1862():
        OP_96(0xFE, 0x1130, 0x0, 0xFFFFBBA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1862)
    WaitChrThread(0xA, 1)

    def lambda_1880():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1880)
    WaitChrThread(0x102, 1)

    #C0021
    ChrTalk(
        0x101,
        (
            "#12P#00002F艾莉！\x01",
            "你已经回来了啊！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_1D9D")
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0022
    AnonymousTalk(
        0x102,
        (
            "#3387V#30W嗯，昨天刚回来。\x02\x03",

            "#3389V协助外公的工作已经处理完了，\x01",
            "从今天开始，我就可以重回工作岗位啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xD3D)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    #C0023
    ChrTalk(
        0x101,
        (
            "#12P#00002F#30W是吗……\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xA, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0024
    ChrTalk(
        0xA,
        (
            "#01105F#11P罗伊德。\x02\x03",

            "你和艾莉为什么要\x01",
            "目不转睛地凝视对方？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_64(0x102)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1AA6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1AA6)

    def lambda_1AB3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1AB3)
    TurnDirection(0x101, 0xA, 700)

    #C0025
    ChrTalk(
        0x101,
        (
            "#6P#00011F没、没有！\x01",
            "才没有那种事！\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#00109F#5P是、是啊，\x01",
            "那个……只是好久没见了，\x01",
            "感觉有点怀念而已啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        "#01100F#11P嗯？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xB,
        (
            "#6P#01902F（唔……\x01",
            "  看起来好像很恩爱呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x109,
        (
            "#12P#10114F（喂，难道他们两个\x01",
            "  真的是那种关系吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        (
            "#6P#01900F（据我观察，好像还没有\x01",
            "  发展到决定性的关系。）\x02\x03",

            "#01909F（呵呵呵，姐姐要是有心，\x01",
            "  说不定还有机会哦～）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x109, 0xB, 700)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0031
    ChrTalk(
        0x109,
        "#11P#10111F（我、我才没有那种想法……！）\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0032
    ChrTalk(
        0x102,
        (
            "#00109F#5P啊，诺艾尔小姐，你也辛苦了。\x02\x03",

            "#00102F没遇到什么险情吧？\x01",
            "罗伊德有时候\x01",
            "很鲁莽……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)
    Sleep(150)

    #C0033
    ChrTalk(
        0x109,
        (
            "#12P#10112F没、没有没有，\x01",
            "艾莉小姐，你也辛苦了。\x02\x03",

            "#10100F你这段时间一直在陪着\x01",
            "麦克道尔议长巡访各国吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D80():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D80)
    Sleep(50)

    def lambda_1D90():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1D90)
    Jump("loc_1EFD")

    label("loc_1D9D")

    OP_C9(0x0, 0x80000000)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0034
    AnonymousTalk(
        0x102,
        (
            "#3388V#30W是啊，昨天刚回来。\x02\x03",

            "#3389V协助外公的工作已经处理完了，\x01",
            "从今天开始，我就可以重回工作岗位啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD3D)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0035
    ChrTalk(
        0x101,
        "#12P#00002F是吗……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x109,
        (
            "#12P#10109F辛苦了，艾莉小姐。\x02\x03",

            "#10100F你这段时间一直在陪着\x01",
            "麦克道尔议长巡访各国吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFD")


    #C0037
    ChrTalk(
        0x102,
        (
            "#00104F#5P嗯，也帮不上\x01",
            "什么大忙就是了。\x02\x03",

            "#00100F不过，我得到了很多\x01",
            "有意思的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#12P#00000F是吗……\x01",
            "找个时间好好讲给我听吧。\x02\x03",

            "#00006F艾莉已经归队，等缇欧和\x01",
            "兰迪回来以后，\x01",
            "我们的阵容就算完美了……\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x5, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x5, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CC(0x0, 0x5, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0039
    AnonymousTalk(
        0xC,
        (
            "嗯，反正他们两个\x01",
            "都会在这个月之内回来。\x02\x03",

            "对了，罗伊德，\x01",
            "事情都处理完了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x5, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x5, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CC(0x0, 0x5, 0x0)

    #C0040
    ChrTalk(
        0x101,
        (
            "#12P#00003F……是的，\x01",
            "我们顺利逮捕了两名犯罪嫌疑人。\x02\x03",

            "#00001F达德利警官和亚里欧斯先生\x01",
            "押送他们去拘留所了。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xC,
        (
            "#01003F#5P是吗……\x02\x03",

            "#01002F由教团引发的一系列事件，\x01",
            "至此总算是彻底结束了。\x02\x03",

            "我想你应该也明白……\x01",
            "一定要尽快把心态调整过来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#12P#00000F是的，一定。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xC,
        (
            "#01002F#5P诺艾尔，今后就要\x01",
            "靠你多帮忙了。\x02\x03",

            "你可以从今天开始工作吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21EF():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21EF)
    Sleep(100)

    def lambda_21FF():
        TurnDirection(0xB, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_21FF)
    Sleep(100)

    def lambda_220F():
        TurnDirection(0xA, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_220F)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrSubChip(0x109, 0x1)
    OP_0D()
    Sleep(100)
    Sound(2491, 255, 100, 0)    #voice#Noel
    Sleep(500)

    #C0044
    ChrTalk(
        0x109,
        (
            "#12P#10103F诺艾尔·希卡！\x02\x03",

            "#10101F从今天开始，正式外派至\x01",
            "特别任务支援科工作！\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xA,
        "#11P#01105F哇……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "#6P#01909F嘿嘿……\x01",
            "姐姐现在也是同事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xC,
        (
            "#01006F#5P哦，不用\x01",
            "那么诚惶诚恐的。\x02\x03",

            "#01000F索妮亚应该跟你说过吧，\x01",
            "我们这里的氛围比较随便。\x02\x03",

            "所以在这里就不要\x01",
            "再像警备队时那么严肃啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()

    #C0048
    ChrTalk(
        0x109,
        "#12P#10105F我、我会努力的。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x105, -9000, 600, -16000, 90)
    OP_C9(0x0, 0x80000000)

    #N0049
    NpcTalk(
        0x105,
        "年轻男性的声音",
        (
            "#2904V#30W呵呵……\x01",
            "好像都到齐了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xB58)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-2000, 900, -15600, 3000)
    SetCameraDistance(13500, 3000)

    def lambda_244D():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_244D)
    Sleep(50)

    def lambda_245D():
        TurnDirection(0xA, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_245D)
    Sleep(50)

    def lambda_246D():
        TurnDirection(0xB, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_246D)
    Sleep(50)

    def lambda_247D():
        TurnDirection(0xC, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_247D)
    Sleep(50)

    def lambda_248D():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_248D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x102, 0)

    def lambda_24B1():

        label("loc_24B1")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_24B1")

    QueueWorkItem2(0x102, 2, lambda_24B1)

    def lambda_24C3():

        label("loc_24C3")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_24C3")

    QueueWorkItem2(0xC, 2, lambda_24C3)

    def lambda_24D5():

        label("loc_24D5")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_24D5")

    QueueWorkItem2(0xB, 2, lambda_24D5)
    Sleep(500)

    def lambda_24EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_24EA)

    def lambda_24FB():
        OP_95(0xFE, -3000, 0, -16000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_24FB)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0050
    ChrTalk(
        0x109,
        "#10100F啊……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#00000F瓦吉……！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xA,
        "#01110F啊，是瓦吉！\x02",
    )

    CloseMessageWindow()

    def lambda_255E():
        OP_95(0xFE, 1700, 0, -15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_255E)
    Sleep(800)
    Fade(500)
    OP_68(2600, 900, -15600, 0)
    MoveCamera(325, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    Sleep(500)

    def lambda_25B1():
        OP_96(0xFE, 0x802, 0x0, 0xFFFFC856, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_25B1)
    WaitChrThread(0x105, 1)

    def lambda_25CF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_25CF)
    WaitChrThread(0x102, 1)
    OP_C9(0x0, 0x80000000)

    #C0053
    ChrTalk(
        0x105,
        (
            "#10304F#2905V#5P#30W呵呵，工作辛苦了。\x02\x03",

            "#10300F#2906V看样子，你们已经\x01",
            "顺利完成任务了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xB5A)

    #C0054
    ChrTalk(
        0x101,
        (
            "#12P#00000F是啊，多亏有你的情报，\x01",
            "我们和阿尔泰尔市的\x01",
            "情报商顺利取得了联系……\x02\x03",

            "#00006F……话说回来，你到底\x01",
            "是从哪里得到那种情报的？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x105,
        "#10309F#5P呵呵……所谓蛇行蛇道嘛。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(3150, 900, -15230, 1500)

    def lambda_2712():
        OP_95(0xFE, 3150, 0, -15400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2712)
    WaitChrThread(0x105, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0xC, 0x2)

    def lambda_2738():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2738)
    EndChrThread(0xB, 0x2)
    OP_6F(0x79)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(150)
    OP_C9(0x0, 0x80000000)

    #A0056
    AnonymousTalk(
        0x105,
        (
            "#2901V#30W正是为了你，我才会如此用心。\x01",
            "如果帮上了忙，我就再开心不过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xB55)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)

    #C0057
    ChrTalk(
        0x102,
        "#5P#00105F！？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xB,
        "#6P#01905F哇哇……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0059
    ChrTalk(
        0x101,
        (
            "#12P#00011F喂，太近了！\x02\x03",

            "为什么越靠越近啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x105,
        (
            "#5P#10309F啊哈哈，真是个蠢问题。\x02\x03",

            "当然是因为\x01",
            "你的反应很有趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#12P#00013F你、你可真是……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        "#5P#00111F瓦吉，你也太……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x109,
        (
            "#12P#10112F啊哈哈……\x01",
            "（果然是个神秘的人啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        (
            "#01109F#11P嘿嘿嘿，\x01",
            "大家好像很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xB,
        (
            "#6P#01906F特别任务支援科真好啊……\x02\x03",

            "姐姐和小琪雅都在，而且还能\x01",
            "看到罗伊德警官窘困的样子。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    #C0066
    ChrTalk(
        0x101,
        (
            "#00012F#11P不不！不管你再\x01",
            "怎么羡慕，我也不希望这样！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xC,
        (
            "#01006F#5P哎呀呀……\x01",
            "说笑就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(2400, 1100, -16300, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetChrPos(0xC, 1100, 0, -17200, 0)
    SetChrPos(0xA, 4000, 0, -14700, 0)
    SetChrPos(0x101, 3700, 0, -15400, 0)
    SetChrPos(0x109, 3900, 0, -16900, 0)
    SetChrPos(0xB, 4400, 0, -17500, 0)
    SetChrPos(0x102, 2000, 0, -14100, 0)
    SetChrPos(0x105, 3150, 0, -15400, 90)
    TurnDirection(0xC, 0x101, 0)

    def lambda_2AF6():
        TurnDirection(0x101, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AF6)
    Sleep(0)

    def lambda_2B06():
        TurnDirection(0x109, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2B06)
    Sleep(0)

    def lambda_2B16():
        TurnDirection(0x102, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2B16)
    Sleep(0)

    def lambda_2B26():
        TurnDirection(0xB, 0xC, 0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2B26)
    Sleep(0)

    def lambda_2B36():
        TurnDirection(0xA, 0xC, 0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2B36)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)

    def lambda_2B5A():
        OP_96(0xFE, 0x9C4, 0x0, 0xFFFFC504, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B5A)
    WaitChrThread(0x105, 1)
    TurnDirection(0x105, 0xC, 500)
    OP_0D()

    #C0068
    ChrTalk(
        0xC,
        (
            "#6P#01003F总之，\x01",
            "这就是新生特别任务支援科的\x01",
            "初始阵容了。\x02\x03",

            "#01000F队长，\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0069
    ChrTalk(
        0x101,
        "#00000F#3317V#30W……是！\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xC,
        (
            "#6P#01000F队长助手，\x01",
            "艾莉·麦克道尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0071
    ChrTalk(
        0x102,
        "#00102F#3390V#5P#30W是。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xC,
        (
            "#6P#01003F来自警备队的借调人员，\x01",
            "诺艾尔·希卡。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0073
    ChrTalk(
        0x109,
        "#10102F#3514V#11P#30W是！\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        (
            "#6P#01000F临时准成员，\x01",
            "瓦吉·赫米斯菲亚。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0075
    ChrTalk(
        0x105,
        "#10304F#2907V#5P#30W在。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xC,
        (
            "#6P#01004F我宣布，自今天１８：３０开始，\x01",
            "特别任务支援科重新启动。\x02\x03",

            "#01002F今后的工作应该\x01",
            "会比以前更加有趣，\x01",
            "你们不妨期待一下。\x02",
        )
    )

    CloseMessageWindow()
    StopSound(835, 2000, 100)
    SetCameraDistance(14500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_F0(0x0, 0xA)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_op.pmf", 0x34, 0x0)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    StopBGM(0x1F4)
    WaitBGM()
    OP_29(0xA0, 0x1, 0x3)
    OP_29(0xA0, 0x4, 0x10)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x1C, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_772 end

    def Function_3_2EB4(): pass

    label("Function_3_2EB4")

    Sound(452, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x168, 0x0, 0x0)
    Sleep(2000)

    def lambda_2ED2():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_2ED2)
    OP_79(0x1)
    Sound(143, 0, 100, 0)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Return()

    # Function_3_2EB4 end

    def Function_4_2EF8(): pass

    label("Function_4_2EF8")

    SetChrPos(0xFE, 22700, 0, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2F19():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F19)
    OP_95(0xFE, 22700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 7300, 0, -12800, 2000, 0x0)
    Return()

    # Function_4_2EF8 end

    def Function_5_2F4E(): pass

    label("Function_5_2F4E")

    SetChrPos(0xFE, 22700, 0, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2F6F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F6F)
    OP_95(0xFE, 22700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 8500, 0, -12800, 2000, 0x0)
    Return()

    # Function_5_2F4E end

    def Function_6_2FA4(): pass

    label("Function_6_2FA4")

    SetChrPos(0xFE, 19700, 100, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2FC5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FC5)
    OP_95(0xFE, 19700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 0, 0, -12800, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_6_2FA4 end

    def Function_7_2FFF(): pass

    label("Function_7_2FFF")

    ClearScenarioFlags(0x0, 0)

    def lambda_3007():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3007)
    OP_95(0xFE, 22700, 0, -13700, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 0, 0, -13700, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_7_2FFF end

    def Function_8_3052(): pass

    label("Function_8_3052")


    def lambda_3057():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3057)
    OP_95(0xFE, 22700, 0, -12700, 2000, 0x0)
    Sleep(500)
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 0, 0, -12700, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_8_3052 end

    def Function_9_309E(): pass

    label("Function_9_309E")


    def lambda_30A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30A3)
    OP_95(0xFE, 32500, 0, -12700, 4000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, 0, 0, -12700, 4000, 0x0)
    OP_64(0xFE)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_9_309E end

    def Function_10_30F2(): pass

    label("Function_10_30F2")

    OP_95(0xFE, 7500, 0, -13700, 2000, 0x0)
    OP_95(0xFE, 4800, 0, -16700, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_30F2 end

    def Function_11_3122(): pass

    label("Function_11_3122")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10900.itc", 0x1E)
    LoadChrToIndex("chr/ch12400.itc", 0x1F)
    LoadChrToIndex("chr/ch11100.itc", 0x20)
    LoadChrToIndex("chr/ch11300.itc", 0x21)
    LoadChrToIndex("chr/ch41000.itc", 0x22)
    LoadChrToIndex("chr/ch41100.itc", 0x23)
    LoadChrToIndex("apl/ch51231.itc", 0x24)
    LoadChrToIndex("chr/ch27600.itc", 0x25)
    LoadChrToIndex("chr/ch27800.itc", 0x26)
    LoadChrToIndex("chr/ch28400.itc", 0x27)
    SoundLoad(963)
    SoundLoad(825)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07400.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07200.itp")
    CreatePortrait(2, 16, 200, 528, 264, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis514.itp")
    CreatePortrait(3, 16, 200, 528, 264, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis515.itp")
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x11, 0x25)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x27)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x1A, 0x23)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1B, 0x23)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x24, 0x80)
    OP_78(0x3, 0x24)
    OP_49()
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    OP_70(0x3, 0x5A)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x1, 0x1000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x11, 33000, 0, 3300, 0)
    SetChrPos(0x12, 20500, 0, 3300, 0)
    SetChrPos(0x13, -2900, 0, 3450, 315)
    SetChrPos(0x14, 40000, 0, 1500, 315)
    SetChrPos(0x15, 40750, 0, 2250, 315)
    SetChrPos(0x16, 22500, 0, 1000, 0)
    SetChrPos(0x17, 23500, 0, 1000, 0)
    SetChrPos(0x24, 38000, -1500, 8000, 90)
    OP_D5(0x24, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(-7250, 1500, 8000, 0)
    MoveCamera(315, 5, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24000, 0)
    OP_F0(0x0, 0x1)
    OP_68(41000, 1500, 8000, 8500)
    MoveCamera(310, 5, 0, 8500)
    SetCameraDistance(20000, 8500)
    BeginChrThread(0x24, 1, 0, 12)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x24, 1)
    Fade(500)
    SetChrPos(0xD, 37000, 0, 6800, 180)
    SetChrPos(0xE, 37000, 0, 6800, 180)
    SetChrPos(0x1A, 37000, 0, 6800, 180)
    SetChrPos(0x1B, 37000, 0, 6800, 180)
    SetChrPos(0x1C, 37000, 0, 6800, 180)
    SetChrPos(0xF, 24000, 0, 6800, 180)
    SetChrPos(0x10, 24000, 0, 6800, 180)
    SetChrPos(0x1D, 24000, 0, 6800, 180)
    SetChrPos(0x11, 33000, 0, 3300, 90)
    SetChrPos(0x12, 20500, 0, 2000, 0)
    SetChrPos(0x24, 45000, -1500, 8000, 90)
    OP_D5(0x24, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(37000, 700, 3800, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    MoveCamera(40, 13, 0, 5000)
    SetCameraDistance(16000, 5000)
    OP_0D()
    Sound(454, 0, 100, 0)
    OP_71(0x3, 0x1, 0x1E, 0x0, 0x8)
    OP_79(0x3)
    BeginChrThread(0x1A, 1, 0, 13)
    Sleep(750)
    BeginChrThread(0x1B, 1, 0, 15)
    Sleep(750)
    BeginChrThread(0x1C, 1, 0, 17)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1C, 1)
    OP_6F(0x79)
    BeginChrThread(0xD, 1, 0, 19)
    Sleep(750)
    BeginChrThread(0xE, 1, 0, 21)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    BeginChrThread(0x11, 1, 0, 36)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(3500)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    EndChrThread(0x11, 0x1)
    OP_64(0x11)
    OP_64(0xD)
    BeginChrThread(0x11, 1, 0, 23)
    Sleep(750)
    BeginChrThread(0xD, 1, 0, 20)
    Sleep(100)
    BeginChrThread(0xE, 1, 0, 22)
    Sleep(100)
    BeginChrThread(0x1C, 1, 0, 18)
    Sleep(100)
    BeginChrThread(0x1B, 1, 0, 16)
    Sleep(100)
    BeginChrThread(0x1A, 1, 0, 14)
    OP_68(24000, 700, 3800, 10000)
    MoveCamera(45, 33, 0, 10000)
    Sleep(8000)
    Sleep(1500)
    BeginChrThread(0x1D, 1, 0, 28)
    Sleep(100)
    BeginChrThread(0x12, 1, 0, 34)
    WaitChrThread(0x1D, 1)
    WaitChrThread(0x12, 1)
    OP_6F(0x79)
    BeginChrThread(0xF, 1, 0, 30)
    Sleep(750)
    BeginChrThread(0x10, 1, 0, 32)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)
    BeginChrThread(0x12, 1, 0, 37)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(3500)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    EndChrThread(0x12, 0x1)
    OP_64(0x12)
    OP_64(0xF)
    OP_68(15000, 700, 3800, 10000)
    BeginChrThread(0x12, 1, 0, 35)
    Sleep(750)
    BeginChrThread(0xF, 1, 0, 31)
    Sleep(100)
    BeginChrThread(0x10, 1, 0, 33)
    Sleep(100)
    BeginChrThread(0x1D, 1, 0, 25)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 2)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_3122 end

    def Function_12_388D(): pass

    label("Function_12_388D")

    Sound(963, 0, 100, 0)
    Sound(825, 2, 50, 0)
    OP_71(0x3, 0x5A, 0x168, 0x0, 0x8)
    Sleep(2000)

    def lambda_38AD():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_38AD)
    OP_79(0x3)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sound(143, 0, 100, 0)
    StopSound(825, 500, 50)
    Sleep(500)
    Return()

    # Function_12_388D end

    def Function_13_38D9(): pass

    label("Function_13_38D9")


    def lambda_38DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_38DE)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 40000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_13_38D9 end

    def Function_14_3915(): pass

    label("Function_14_3915")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_14_3915 end

    def Function_15_392C(): pass

    label("Function_15_392C")


    def lambda_3931():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3931)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 39000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_15_392C end

    def Function_16_3968(): pass

    label("Function_16_3968")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_16_3968 end

    def Function_17_397F(): pass

    label("Function_17_397F")


    def lambda_3984():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3984)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 38000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_17_397F end

    def Function_18_39BB(): pass

    label("Function_18_39BB")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_18_39BB end

    def Function_19_39D2(): pass

    label("Function_19_39D2")


    def lambda_39D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_39D7)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_68(35000, 700, 3300, 2000)
    OP_95(0xFE, 35000, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_19_39D2 end

    def Function_20_3A1F(): pass

    label("Function_20_3A1F")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_20_3A1F end

    def Function_21_3A2F(): pass

    label("Function_21_3A2F")


    def lambda_3A34():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3A34)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 35750, 0, 2500, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_3A2F end

    def Function_22_3A6B(): pass

    label("Function_22_3A6B")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_22_3A6B end

    def Function_23_3A7B(): pass

    label("Function_23_3A7B")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_23_3A7B end

    def Function_24_3A92(): pass

    label("Function_24_3A92")


    def lambda_3A97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3A97)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 27000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_24_3A92 end

    def Function_25_3ACE(): pass

    label("Function_25_3ACE")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_25_3ACE end

    def Function_26_3AE5(): pass

    label("Function_26_3AE5")


    def lambda_3AEA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3AEA)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 26000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_26_3AE5 end

    def Function_27_3B21(): pass

    label("Function_27_3B21")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_27_3B21 end

    def Function_28_3B38(): pass

    label("Function_28_3B38")


    def lambda_3B3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3B3D)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 25000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_3B38 end

    def Function_29_3B74(): pass

    label("Function_29_3B74")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_29_3B74 end

    def Function_30_3B8B(): pass

    label("Function_30_3B8B")


    def lambda_3B90():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3B90)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_68(22000, 700, 3300, 2000)
    OP_95(0xFE, 22000, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_30_3B8B end

    def Function_31_3BD8(): pass

    label("Function_31_3BD8")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_31_3BD8 end

    def Function_32_3BE8(): pass

    label("Function_32_3BE8")


    def lambda_3BED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3BED)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 22750, 0, 2500, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_32_3BE8 end

    def Function_33_3C24(): pass

    label("Function_33_3C24")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_33_3C24 end

    def Function_34_3C34(): pass

    label("Function_34_3C34")

    OP_95(0xFE, 20500, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_34_3C34 end

    def Function_35_3C50(): pass

    label("Function_35_3C50")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_35_3C50 end

    def Function_36_3C67(): pass

    label("Function_36_3C67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CAD")
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x11)
    Sleep(500)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xD)
    Sleep(500)
    Jump("Function_36_3C67")

    label("loc_3CAD")

    Return()

    # Function_36_3C67 end

    def Function_37_3CAE(): pass

    label("Function_37_3CAE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CF4")
    OP_63(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x12)
    Sleep(500)
    OP_63(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xF)
    Sleep(500)
    Jump("Function_37_3CAE")

    label("loc_3CF4")

    Return()

    # Function_37_3CAE end

    def Function_38_3CF5(): pass

    label("Function_38_3CF5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46400.itc", 0x1E)
    OP_68(-1390, 2700, -10, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -10000, 600, 700, 90)
    SetChrPos(0x102, -10000, 600, -600, 90)
    SetChrPos(0x103, -11500, 600, -700, 90)
    SetChrPos(0x104, -11500, 600, 650, 90)
    SetChrPos(0x109, -13000, 600, -600, 90)
    SetChrPos(0x105, -13000, 600, 700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x20, 0x1E)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -9500, 600, 40, 90)

    def lambda_3DCE():
        OP_95(0x20, 1000, 600, 40, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3DCE)
    Sleep(800)

    def lambda_3DEB():
        OP_95(0x101, 200, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DEB)
    Sleep(200)

    def lambda_3E08():
        OP_95(0x102, 300, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E08)
    Sleep(300)

    def lambda_3E25():
        OP_95(0x103, -1000, 0, -950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E25)
    Sleep(100)

    def lambda_3E42():
        OP_95(0x104, -1100, 0, 1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3E42)
    Sleep(200)

    def lambda_3E5F():
        OP_95(0x109, -2500, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3E5F)
    Sleep(50)

    def lambda_3E7C():
        OP_95(0x105, -2400, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3E7C)
    OP_68(-1390, 1500, -10, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x20, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3F71():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F71)
    Sleep(50)

    def lambda_3F81():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3F81)
    Sleep(50)

    def lambda_3F91():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3F91)
    Sleep(10)

    def lambda_3FA1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3FA1)
    Sleep(30)

    def lambda_3FB1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3FB1)
    Sleep(10)

    def lambda_3FC1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3FC1)
    Sleep(10)

    def lambda_3FD1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_3FD1)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x20, 2)

    #C0077
    ChrTalk(
        0x101,
        "#00005F这是……\x02",
    )

    CloseMessageWindow()
    OP_68(-1120, 1500, -24350, 5000)
    MoveCamera(45, 30, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(24120, 5000)
    OP_6F(0x79)
    OP_68(6950, 1500, -25730, 5000)
    MoveCamera(11, 16, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(19540, 5000)
    OP_6F(0x79)
    SetMessageWindowPos(50, 50, -1, -1)

    #A0078
    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00100F帝国政府的专用列车，\x01",
            "『艾森古拉夫号』吧。\x02\x03",

            "#00103F这豪华的外观……\x01",
            "似乎也象征着帝国的强大。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 50, -1, -1)

    #A0079
    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10103F的确……\x01",
            "正是那种威风凛凛的感觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 50, -1, -1)

    #A0080
    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00300F『铁血宰相』就是乘坐这个\x01",
            "抵达克洛斯贝尔的吧？\x02\x03",

            "#00306F冲击力自然是足够了，\x01",
            "但他到底要张扬到\x01",
            "什么程度才满意啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 50, -1, -1)

    #A0081
    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10300F是啊，金钱方面的花销\x01",
            "肯定非同一般。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-160, 1500, 410, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16250, 0)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_93(0x109, 0xB4, 0x0)
    OP_93(0x105, 0xB4, 0x0)
    OP_93(0x20, 0x10E, 0x0)
    OP_0D()

    #C0082
    ChrTalk(
        0x103,
        (
            "#00203F……惊人的\x01",
            "不只是外表。\x02\x03",

            "#00200F据说这辆列车\x01",
            "是如今速度最快的\x01",
            "导力列车。\x02\x03",

            "但由于具体情报\x01",
            "并没有公开，\x01",
            "所以还无法断言。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        "#00005F是、是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x102,
        (
            "#00103F真不愧是铁路网覆盖国土全域的\x01",
            "埃雷波尼亚帝国……\x02\x03",

            "#00101F在铁路领域，\x01",
            "没有任何地方可以赶超他们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#00003F是啊，如今真是有了深刻感受。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x20,
        "咳咳……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x20,
        (
            "我准备说说工作的事情了，\x01",
            "你们准备好了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_43CB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_43CB)
    Sleep(50)

    def lambda_43DB():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_43DB)
    Sleep(30)

    def lambda_43EB():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_43EB)
    Sleep(20)

    def lambda_43FB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_43FB)
    Sleep(40)

    def lambda_440B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_440B)
    Sleep(20)

    def lambda_441B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_441B)
    WaitChrThread(0x105, 2)

    #C0088
    ChrTalk(
        0x101,
        (
            "#00005F不、不好意思，那辆列车太壮观了，\x01",
            "让我们一时分了心。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        "#00100F是的，当然准备好了。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x20,
        "嗯，很好。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x20,
        (
            "那么，正如我刚才所说，\x01",
            "希望你们帮忙完成\x01",
            "列车安检工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x20,
        (
            "具体内容就是检查所有乘客的\x01",
            "入境申请书和随身行李。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x20,
        (
            "另外，还要帮我做\x01",
            "列车的安全检查工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#00005F请问，在列车的安全检查中\x01",
            "要做些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x20,
        (
            "哦，主要是协助我。\x01",
            "总之，就是在我的指示下，\x01",
            "展开各种检查工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x20,
        (
            "嗯，你们一共\x01",
            "有六个人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x20,
        (
            "既然如此，那就两人一组，分成三组吧。\x01",
            "其中两组负责检查乘客所在的车厢，\x01",
            "另外一组来协助我。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_474B")

    #C0098
    ChrTalk(
        0x101,
        (
            "#00005F两人一组吗？\x01",
            "上次好像是一个人负责一节车厢呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#00100F是啊，上次帮忙时\x01",
            "都是单独行动的。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x20,
        "哦，对了，你们有这方面的工作经验。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x20,
        (
            "在平时，这确实是\x01",
            "由单人完成的工作，\x01",
            "但现在的警戒力度提高了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x20,
        (
            "为了让检查工作更加严密，\x01",
            "这次才会以这种形式委托你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F6")

    label("loc_474B")


    #C0103
    ChrTalk(
        0x101,
        (
            "#00005F两人一组……\x01",
            "平时也是这种形式吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x20,
        (
            "不，在平时，\x01",
            "这是由单人完成的工作。\x01",
            "但现在的警戒力度提高了。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x20,
        (
            "为了让检查工作更加严密，\x01",
            "这次才会以这种形式委托你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47F6")


    #C0106
    ChrTalk(
        0x101,
        "#00000F原来如此，我明白了。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x20,
        (
            "那么，能否请你们\x01",
            "立刻分成三组？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x20,
        "如果不好分，不妨用猜拳来决定。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0109
    ChrTalk(
        0x101,
        "#00005F用、用猜拳来决定？\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x20,
        (
            "嗯，老实说，这项工作\x01",
            "对个人能力并没有什么要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x20,
        (
            "而且我希望你们\x01",
            "能尽快开始工作。\x01",
            "对你们而言，这样也比较简单吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00000F嗯，说的也是，\x01",
            "那我们就猜拳好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，就这么定了吧。\x01",
            "听起来似乎很有趣，没什么不好¤\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        (
            "#00205F不过，具体要\x01",
            "怎么决定呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x20,
        (
            "嗯，就按照这种规则\x01",
            "来分配好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x20,
        (
            "首先，大家遵照猜拳的规矩，一起出手。\x01",
            "如果只有两个人出了一样的手势，\x01",
            "就直接结为一组，不用再继续猜拳了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x20,
        "之后就一直重复，直到所有人都定下来。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x109,
        (
            "#10106F那个……\x01",
            "您好像很熟悉这种规则啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x20,
        "哈哈，算是吧。\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x20,
        (
            "其实，我们共和国安检官\x01",
            "有时候就会用这种方式来\x01",
            "决定分工，这也算是一种放松吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x20,
        (
            "那些死板的帝国安检官\x01",
            "就不会有这种灵活的想法。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0122
    ChrTalk(
        0x102,
        (
            "#00106F算不算灵活的想法，\x01",
            "还有待商榷……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#00200F总之，\x01",
            "这也算是国家间的差异吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#00300F哈哈，也许呢。\x02\x03",

            "好啦，\x01",
            "我们赶快开始吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#00000F嗯，好的。\x02",
    )

    CloseMessageWindow()

    def lambda_4C68():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C68)
    Sleep(10)

    def lambda_4C78():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4C78)
    Sleep(10)

    def lambda_4C88():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4C88)
    Sleep(10)

    def lambda_4C98():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4C98)
    Sleep(30)

    def lambda_4CA8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4CA8)
    Sleep(10)

    def lambda_4CB8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4CB8)
    WaitChrThread(0x105, 2)
    Sleep(500)

    #C0126
    ChrTalk(
        0x101,
        (
            "#00003F那么，各位，\x01",
            "我们喊完『一二三』之后一起出手。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "出石头\x01",      # 0
            "出剪刀\x01",      # 1
            "出布\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 39)
    BeginChrThread(0x102, 3, 0, 39)
    BeginChrThread(0x103, 3, 0, 39)
    BeginChrThread(0x104, 3, 0, 39)
    BeginChrThread(0x109, 3, 0, 39)
    BeginChrThread(0x105, 3, 0, 39)
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("众人")

    #A0127
    AnonymousTalk(
        0xFF,
        "#4S#11A一、二……\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)

    def lambda_4DBA():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DBA)

    def lambda_4DCF():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4DCF)

    def lambda_4DE4():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4DE4)

    def lambda_4DF9():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4DF9)

    def lambda_4E0E():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4E0E)

    def lambda_4E23():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4E23)
    Sound(802, 0, 100, 0)
    SetChrName("众人")

    #A0128
    AnonymousTalk(
        0xFF,
        "#4S#11A三！\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_549B")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4E9C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E9C)

    def lambda_4EB1():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4EB1)

    def lambda_4EC6():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4EC6)

    def lambda_4EDB():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4EDB)

    def lambda_4EF0():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4EF0)

    def lambda_4F05():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F05)
    WaitChrThread(0x101, 1)

    def lambda_4F1E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F1E)
    Sleep(50)

    def lambda_4F2E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F2E)
    Sleep(300)

    #C0129
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，只有我和缇欧\x01",
            "是剪刀呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x103,
        (
            "#00200F也就是说，\x01",
            "我和艾莉前辈一组。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        "#00300F剩下的人……三个出石头，一个出布啊。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x109,
        (
            "#10100F这样的话，\x01",
            "剩下的四人就要再来一次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#00000F嗯，我们继续吧。\x02",
    )

    CloseMessageWindow()

    def lambda_5012():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5012)
    Sleep(50)

    def lambda_5022():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5022)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "出石头\x01",      # 0
            "出剪刀\x01",      # 1
            "出布\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 39)
    BeginChrThread(0x104, 3, 0, 39)
    BeginChrThread(0x109, 3, 0, 39)
    BeginChrThread(0x105, 3, 0, 39)
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("众人")

    #A0134
    AnonymousTalk(
        0xFF,
        "#4S#11A一、二……\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)

    def lambda_50D2():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50D2)

    def lambda_50E7():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50E7)

    def lambda_50FC():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_50FC)

    def lambda_5111():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5111)
    Sound(802, 0, 100, 0)
    SetChrName("众人")

    #A0135
    AnonymousTalk(
        0xFF,
        "#4S#11A三！\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_519F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_519F)

    def lambda_51B4():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_51B4)

    def lambda_51C9():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_51C9)

    def lambda_51DE():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_51DE)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52DF")

    def lambda_5206():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5206)
    Sleep(50)

    def lambda_5216():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5216)
    Sleep(300)

    #C0136
    ChrTalk(
        0x101,
        "#00005F我和诺艾尔是石头。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x109,
        (
            "#10100F呵呵，罗伊德警官，\x01",
            "一起加油吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5271():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5271)
    Sleep(50)

    def lambda_5281():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5281)
    Sleep(300)

    #C0138
    ChrTalk(
        0x104,
        (
            "#00300F嗯，剩下的我和瓦吉\x01",
            "就是一组了。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x105,
        "#10300F呵呵，一起加油吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 4)
    Jump("loc_5496")

    label("loc_52DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53BF")

    def lambda_52F3():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52F3)
    Sleep(50)

    def lambda_5303():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5303)
    Sleep(300)

    #C0140
    ChrTalk(
        0x101,
        "#00005F我和瓦吉是剪刀。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x105,
        "#10300F呵呵，一起加油吧。\x02",
    )

    CloseMessageWindow()

    def lambda_534F():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_534F)
    Sleep(50)

    def lambda_535F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_535F)
    Sleep(300)

    #C0142
    ChrTalk(
        0x104,
        (
            "#00300F嗯，剩下的我和诺艾尔\x01",
            "就是一组了。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x109,
        "#10100F是啊，一起加油吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)
    Jump("loc_5496")

    label("loc_53BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5496")

    def lambda_53D3():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53D3)
    Sleep(50)

    def lambda_53E3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_53E3)
    Sleep(300)

    #C0144
    ChrTalk(
        0x101,
        "#00005F我和兰迪是布。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        "#00300F嗯，一起加油吧。\x02",
    )

    CloseMessageWindow()

    def lambda_542B():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_542B)
    Sleep(50)

    def lambda_543B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_543B)
    Sleep(300)

    #C0146
    ChrTalk(
        0x109,
        (
            "#10100F也就是说，\x01",
            "剩下的我和瓦吉是一组了。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x105,
        "#10300F嗯，一起加油吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 3)

    label("loc_5496")

    Jump("loc_5C5C")

    label("loc_549B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD9")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_54D6():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54D6)

    def lambda_54EB():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54EB)

    def lambda_5500():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5500)

    def lambda_5515():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5515)

    def lambda_552A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_552A)

    def lambda_553F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_553F)
    WaitChrThread(0x101, 1)

    def lambda_5558():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5558)
    Sleep(50)

    def lambda_5568():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5568)
    Sleep(300)

    #C0148
    ChrTalk(
        0x104,
        "#00305F嗯，只有我和诺艾尔是石头啊。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x109,
        (
            "#10100F也就是说，\x01",
            "我和兰迪前辈是一组呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x105,
        "#10300F剩下的人……三个出剪刀，一个出布啊。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        (
            "#00100F这样的话，\x01",
            "剩下的四人就要再来一次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#00000F嗯，我们继续吧。\x02",
    )

    CloseMessageWindow()

    def lambda_564F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_564F)
    Sleep(50)

    def lambda_565F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_565F)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "出石头\x01",      # 0
            "出剪刀\x01",      # 1
            "出布\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 39)
    BeginChrThread(0x102, 3, 0, 39)
    BeginChrThread(0x103, 3, 0, 39)
    BeginChrThread(0x105, 3, 0, 39)
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("众人")

    #A0153
    AnonymousTalk(
        0xFF,
        "#4S#11A一、二……\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x105, 0x3)

    def lambda_570F():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_570F)

    def lambda_5724():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5724)

    def lambda_5739():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5739)

    def lambda_574E():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_574E)
    Sound(802, 0, 100, 0)
    SetChrName("众人")

    #A0154
    AnonymousTalk(
        0xFF,
        "#4S#11A三！\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_57DC():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57DC)

    def lambda_57F1():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57F1)

    def lambda_5806():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5806)

    def lambda_581B():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_581B)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5916")

    def lambda_5843():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5843)
    Sleep(50)

    def lambda_5853():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5853)
    Sleep(300)

    #C0155
    ChrTalk(
        0x101,
        "#00005F我和缇欧是石头。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        (
            "#00200F罗伊德前辈，\x01",
            "一起努力吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_58A6():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58A6)
    Sleep(50)

    def lambda_58B6():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_58B6)
    Sleep(300)

    #C0157
    ChrTalk(
        0x102,
        (
            "#00100F也就是说，\x01",
            "剩下的我和瓦吉是一组了。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x105,
        "#10300F嗯，一起加油吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 2)
    Jump("loc_5AD4")

    label("loc_5916")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59F7")

    def lambda_592A():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_592A)
    Sleep(50)

    def lambda_593A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_593A)
    Sleep(300)

    #C0159
    ChrTalk(
        0x101,
        "#00005F我和瓦吉是剪刀。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x105,
        "#10300F呵呵，一起加油吧。\x02",
    )

    CloseMessageWindow()

    def lambda_5986():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5986)
    Sleep(50)

    def lambda_5996():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5996)
    Sleep(300)

    #C0161
    ChrTalk(
        0x102,
        (
            "#00100F也就是说，\x01",
            "我和缇欧是一组呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x103,
        (
            "#00200F艾莉前辈，\x01",
            "一起努力吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)
    Jump("loc_5AD4")

    label("loc_59F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD4")

    def lambda_5A0B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A0B)
    Sleep(50)

    def lambda_5A1B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A1B)
    Sleep(300)

    #C0163
    ChrTalk(
        0x101,
        "#00005F我和艾莉是布。\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x102,
        "#00100F呵呵，一起加油吧。\x02",
    )

    CloseMessageWindow()

    def lambda_5A65():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A65)
    Sleep(50)

    def lambda_5A75():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A75)
    Sleep(300)

    #C0165
    ChrTalk(
        0x103,
        (
            "#00200F也就是说，剩下的我\x01",
            "和瓦吉先生是一组呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x105,
        "#10300F嗯，一起加油吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 1)

    label("loc_5AD4")

    Jump("loc_5C5C")

    label("loc_5AD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C5C")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5B62():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B62)

    def lambda_5B77():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B77)

    def lambda_5B8C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B8C)

    def lambda_5BA1():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BA1)

    def lambda_5BB6():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5BB6)

    def lambda_5BCB():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5BCB)
    WaitChrThread(0x101, 1)

    #C0167
    ChrTalk(
        0x101,
        (
            "#00005F哦，一下就分好了呢。\x02\x03",

            "#00000F瓦吉和我，艾莉和缇欧，\x01",
            "还有兰迪和诺艾尔各是一组。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x105,
        "#10300F呵呵，一起加油吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)

    label("loc_5C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_5C73")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5CCA")

    label("loc_5C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_5C8A")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5CCA")

    label("loc_5C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_5CA1")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5CCA")

    label("loc_5CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_5CB8")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5CCA")

    label("loc_5CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_5CCA")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5CCA")


    #C0169
    ChrTalk(
        0x20,
        "唔，看样子，你们已经决定好了啊。\x02",
    )

    CloseMessageWindow()

    def lambda_5CF5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5CF5)
    Sleep(10)

    def lambda_5D05():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5D05)
    Sleep(10)

    def lambda_5D15():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5D15)
    Sleep(10)

    def lambda_5D25():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5D25)
    Sleep(30)

    def lambda_5D35():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5D35)
    Sleep(10)

    def lambda_5D45():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5D45)
    WaitChrThread(0x105, 2)
    Sleep(500)

    #C0170
    ChrTalk(
        0x101,
        "#00000F要如何分工呢？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_5E4E")

    #C0171
    ChrTalk(
        0x20,
        "这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x20,
        (
            "我这边的工作量比较大，\x01",
            "比较需要男性帮手。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        "#00300F也就是说，我和瓦吉被点名了啊。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x105,
        (
            "#10306F哎呀呀，听起来，\x01",
            "似乎会被使唤得很累呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x20,
        (
            "哈哈，难得有人帮忙，\x01",
            "我一定会充分利用你们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EFF")

    label("loc_5E4E")


    #C0176
    ChrTalk(
        0x109,
        (
            "#10105F啊，不然就由我们去\x01",
            "协助安检官先生吧？\x02\x03",

            "#10100F我在警备队有过\x01",
            "检查车辆的经验，\x01",
            "应该可以帮上一些忙。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0177
    ChrTalk(
        0x20,
        (
            "原来如此，是这样啊。\x01",
            "嗯，那就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EFF")


    #C0178
    ChrTalk(
        0x20,
        (
            "好，我们马上\x01",
            "开始工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x20,
        (
            "乘客所在的车厢\x01",
            "就交给你们检查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x20,
        (
            "之前已经通过广播通知乘客了，\x01",
            "你们只要说自己是『代理安检官』，\x01",
            "大家应该就会配合的。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        "#00000F好的，我明白了。\x02",
    )

    CloseMessageWindow()
    StopSound(835, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x20, 0x0)
    SetChrFlags(0x20, 0x80)
    OP_D7(0x1E)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_5FFC")
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_6048")

    label("loc_5FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_600E")
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_6048")

    label("loc_600E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_6020")
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_6048")

    label("loc_6020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_6032")
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_6048")

    label("loc_6032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_6044")
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_6048")

    label("loc_6044")

    AddParty(0x1, 0xFF, 0xFF)

    label("loc_6048")

    SetScenarioFlags(0x22, 3)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_3CF5 end

    def Function_39_6055(): pass

    label("Function_39_6055")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6085")

    def lambda_6065():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6065)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_39_6055")

    label("loc_6085")

    Return()

    # Function_39_6055 end

    def Function_40_6086(): pass

    label("Function_40_6086")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch46400.itc", 0x1E)
    OP_68(520, 1500, 270, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x101, 200, 0, 700, 90)
    SetChrPos(0x102, 300, 0, -600, 90)
    SetChrPos(0x103, -1000, 0, -950, 90)
    SetChrPos(0x104, -1100, 0, 1100, 90)
    SetChrPos(0x109, -2500, 0, -600, 90)
    SetChrPos(0x105, -2400, 0, 700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x20, 0x1E)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 2200, 600, 40, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0182
    ChrTalk(
        0x20,
        "嗯，各位都辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x20,
        (
            "尤其是车票盗窃案引起的骚乱，\x01",
            "真是麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#00000F不，我们也没\x01",
            "帮什么大忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        (
            "#00100F顺便一问，有没有确认\x01",
            "盗窃犯身份的方法？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x20,
        "嗯，有的。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x20,
        (
            "为了防止这种情况，\x01",
            "我们都会预留\x01",
            "购票者的信息。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x20,
        (
            "如果在调查中发现盗窃案，\x01",
            "在下一站就能将犯人逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        "#00200F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        (
            "#00300F那位遭窃的老爷爷\x01",
            "怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x20,
        (
            "哦，那位老人\x01",
            "还要赶时间，\x01",
            "所以又买了一张票。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x20,
        (
            "将盗窃犯逮捕之后，\x01",
            "让他赔偿就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x105,
        "#10300F呵呵，那位老人真倒霉啊。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x109,
        (
            "#10100F不过，能及时解决，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x20,
        (
            "嗯，你们已经在力所能及的\x01",
            "范围内做到最好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x20,
        "真是帮了大忙，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#00000F哪里，\x01",
            "您能这样说，\x01",
            "我感到很荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x102,
        (
            "#00100F如果以后还有什么事，\x01",
            "请不必客气，尽管和我们联系。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0199
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【协助共和国的安检官】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x79, 0x1, 0xE)
    OP_29(0x79, 0x4, 0x10)
    StopSound(835, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0010", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_40_6086 end

    def Function_41_64C2(): pass

    label("Function_41_64C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch46400.itc", 0x1E)
    OP_68(520, 1500, 270, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x101, 200, 0, 700, 90)
    SetChrPos(0x102, 300, 0, -600, 90)
    SetChrPos(0x103, -1000, 0, -950, 90)
    SetChrPos(0x104, -1100, 0, 1100, 90)
    SetChrPos(0x109, -2500, 0, -600, 90)
    SetChrPos(0x105, -2400, 0, 700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x20, 0x1E)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 2200, 600, 40, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0200
    ChrTalk(
        0x20,
        "我都听说了……\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x20,
        (
            "竟然发生了盗窃案，\x01",
            "真是辛苦你们啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        (
            "#00003F哪里，我们也没\x01",
            "帮什么大忙。\x02\x03",

            "#00000F那名盗窃他人车票的青年\x01",
            "最后怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x20,
        (
            "哦，被盗者决定\x01",
            "不追究他的责任了。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x102,
        "#00100F哎，这是怎么回事……？\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x20,
        (
            "那位遭窃的老人\x01",
            "突然改了口，\x01",
            "声称并没有发生盗窃事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x20,
        (
            "那名青年则说只是在\x01",
            "买了站台票并进入月台之后，\x01",
            "忘了再买车票而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x20,
        (
            "既然事情变成这样，\x01",
            "我们也就无法\x01",
            "继续追究了。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x104,
        "#00306F呼，这还真是……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#00003F唔～这大概也是\x01",
            "由于秦的劝说。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x105,
        "#10300F呵呵，也许吧。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x109,
        (
            "#10105F顺便一问，那位商人\x01",
            "怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x20,
        (
            "哦，他才是这次\x01",
            "捕到的大鱼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x20,
        (
            "那家伙其实是个\x01",
            "伪造车票的票贩。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0214
    ChrTalk(
        0x101,
        "#00005F是、是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        "#00100F那他是出于什么理由而登上列车的？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x20,
        (
            "哦，他似乎是想\x01",
            "通过实际使用的方式\x01",
            "来检验自己的商品。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x20,
        "真是个胆大包天的家伙啊。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x103,
        "#00203F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x20,
        (
            "哎呀，话说回来，你们的\x01",
            "活跃表现实在是太棒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x20,
        "真是帮了大忙啊，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#00000F哪里，\x01",
            "您能这样说，\x01",
            "我感到很荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        (
            "#00100F如果以后还有什么事，\x01",
            "请不必客气，尽管和我们联系。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x20,
        "嗯，再见了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0x2D, 0x1F4)
    OP_95(0x20, 5760, 0, 2550, 2000, 0x0)

    def lambda_6A38():
        OP_95(0x20, 24940, 0, 2810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6A38)
    Sleep(500)
    OP_68(-1190, 1500, -230, 2000)
    MoveCamera(45, 34, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(15430, 2000)
    Sleep(1500)

    def lambda_6A86():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A86)
    Sleep(10)

    def lambda_6A96():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6A96)
    Sleep(10)

    def lambda_6AA6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6AA6)
    Sleep(10)

    def lambda_6AB6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6AB6)
    Sleep(30)

    def lambda_6AC6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6AC6)
    Sleep(10)

    def lambda_6AD6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6AD6)
    WaitChrThread(0x105, 2)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_6C8A")

    #C0224
    ChrTalk(
        0x109,
        (
            "#10100F话说回来，秦的表现\x01",
            "真是相当活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#00109F呵呵，没想到会在\x01",
            "这种地方遇到他。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#00003F是啊，更加确信他\x01",
            "将来必成大器了。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x104,
        (
            "#00306F真是的，越来越不敢想象\x01",
            "这小鬼将来会有多可怕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x103,
        "#00200F唔，很想见识一下呢。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，单看外表，\x01",
            "倒是个很可爱的小朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，确实。\x02\x03",

            "#00003F不管怎么说，任务已经告一段落了。\x02\x03",

            "#00000F我们稍微休息一下，\x01",
            "然后就去处理下一项工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_730A")

    label("loc_6C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_6E39")

    #C0231
    ChrTalk(
        0x102,
        (
            "#00100F话说回来，秦的表现\x01",
            "真是相当活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x103,
        (
            "#00200F是啊，明明年纪还那么小，\x01",
            "但出色的表现真让人大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#00000F是啊，更加确信他\x01",
            "将来必成大器了。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        (
            "#00306F真是的，越来越不敢想象\x01",
            "那小鬼将来会有多可怕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x109,
        "#10100F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，单看外表，\x01",
            "倒是个很可爱的小朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，确实。\x02\x03",

            "#00003F不管怎么说，任务已经告一段落了。\x02\x03",

            "#00000F我们稍微休息一下，\x01",
            "然后就去处理下一项工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_730A")

    label("loc_6E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_6FC7")

    #C0238
    ChrTalk(
        0x102,
        (
            "#00100F话说回来，秦的表现\x01",
            "真是相当活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x104,
        "#00300F嗯，他还是老样子。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#00000F是啊，更加确信他\x01",
            "将来必成大器了。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x109,
        (
            "#10106F该怎么说呢……\x01",
            "他的前途真是无可限量啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        "#00200F唔，很想见识一下呢。\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，单看外表，\x01",
            "倒是个很可爱的小朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，确实。\x02\x03",

            "#00003F不管怎么说，任务已经告一段落了。\x02\x03",

            "#00000F我们稍微休息一下，\x01",
            "然后就去处理下一项工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_730A")

    label("loc_6FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_716A")

    #C0245
    ChrTalk(
        0x102,
        (
            "#00100F话说回来，秦的表现\x01",
            "真是相当活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x109,
        (
            "#10100F是啊，没想到\x01",
            "会在这种地方遇到他。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#00000F嗯，更加确信他\x01",
            "将来必成大器了。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x104,
        (
            "#00306F真是的，越来越不敢想象\x01",
            "这小鬼将来会有多可怕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x103,
        "#00200F唔，很想见识一下呢。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，单看外表，\x01",
            "倒是个很可爱的小朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，确实。\x02\x03",

            "#00003F不管怎么说，任务已经告一段落了。\x02\x03",

            "#00000F我们稍微休息一下，\x01",
            "然后就去处理下一项工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_730A")

    label("loc_716A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_730A")

    #C0252
    ChrTalk(
        0x102,
        (
            "#00100F话说回来，秦的表现\x01",
            "真是相当活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，没想到\x01",
            "会在这种地方与他重逢。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00000F嗯，更加确信他\x01",
            "将来必成大器了。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#00306F真是的，越来越不敢想象\x01",
            "这小鬼将来会有多可怕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x103,
        "#00200F唔，很想见识一下呢。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x109,
        (
            "#10100F呵呵，单看外表，\x01",
            "倒是个很可爱的小朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，确实。\x02\x03",

            "#00003F不管怎么说，任务已经告一段落了。\x02\x03",

            "#00000F我们稍微休息一下，\x01",
            "然后就去处理下一项工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_730A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0259
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【协助共和国的安检官】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x79, 0x1, 0xF)
    OP_29(0x79, 0x4, 0x10)
    StopSound(835, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0010", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_41_64C2 end

    def Function_42_7387(): pass

    label("Function_42_7387")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7420")
    SetChrPos(0x101, -8000, 600, -850, 90)
    SetChrPos(0x102, -8000, 600, 500, 90)
    SetChrPos(0x103, -9150, 600, -1350, 90)
    SetChrPos(0x104, -9150, 600, 1000, 90)
    SetChrPos(0xF4, -10300, 600, -850, 90)
    SetChrPos(0xF5, -10300, 600, 500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_749A")

    label("loc_7420")

    SetChrPos(0x101, -8000, 600, -16850, 90)
    SetChrPos(0x102, -8000, 600, -15500, 90)
    SetChrPos(0x103, -9150, 600, -17350, 90)
    SetChrPos(0x104, -9150, 600, -15000, 90)
    SetChrPos(0xF4, -10300, 600, -16850, 90)
    SetChrPos(0xF5, -10300, 600, -15500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_749A")

    OP_68(27000, 1500, 1000, 0)
    MoveCamera(54, 5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(28000, 0)
    OP_F0(0x0, 0x1)
    MoveCamera(60, 5, 0, 8000)
    SetCameraDistance(38000, 8000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    PlaceName2(340, 200, "c_plac00", 0x0, 0)
    OP_6F(0x79)
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_754F")
    OP_68(-1150, 1000, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(16500, 4000)
    Jump("loc_7586")

    label("loc_754F")

    OP_68(-1150, 1000, -16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(16500, 4000)

    label("loc_7586")


    def lambda_758B():
        OP_97(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_758B)
    Sleep(50)

    def lambda_75A8():
        OP_97(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_75A8)
    Sleep(50)

    def lambda_75C5():
        OP_97(0x103, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_75C5)
    Sleep(50)

    def lambda_75E2():
        OP_97(0x104, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_75E2)
    Sleep(50)

    def lambda_75FF():
        OP_97(0xF4, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_75FF)
    Sleep(50)

    def lambda_761C():
        OP_97(0xF5, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_761C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0260
    ChrTalk(
        0x104,
        (
            "#00306F#5P唔，空无一人的月台\x01",
            "还真是荒凉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        (
            "#6P#00206F……列车似乎一直都\x01",
            "停在站台。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x102,
        "#5P#00108F是啊……\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Sleep(150)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7711")

    #C0263
    ChrTalk(
        0x102,
        (
            "#5P#00101F……三号月台的列车\x01",
            "是在那边吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7740")

    label("loc_7711")


    #C0264
    ChrTalk(
        0x102,
        (
            "#5P#00101F……三号月台的列车\x01",
            "是在那边吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7740")

    OP_68(-1150, 1000, -24100, 3000)
    MoveCamera(63, 27, 0, 3000)
    SetCameraDistance(25500, 3000)

    def lambda_776A():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_776A)
    Sleep(50)

    def lambda_777A():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_777A)
    Sleep(50)

    def lambda_778A():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_778A)
    Sleep(50)

    def lambda_779A():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_779A)
    Sleep(50)

    def lambda_77AA():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_77AA)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7852")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_781F")

    #C0265
    ChrTalk(
        0x10A,
        (
            "#00601F嗯，是那辆列车的\x01",
            "前数第二节车厢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_784D")

    label("loc_781F")


    #C0266
    ChrTalk(
        0x10A,
        (
            "#00601F嗯，是那辆列车的\x01",
            "前数第二节车厢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_784D")

    Jump("loc_7955")

    label("loc_7852")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78D6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78A3")

    #C0267
    ChrTalk(
        0x109,
        (
            "#10101F嗯，是那辆列车的\x01",
            "前数第二节车厢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78D1")

    label("loc_78A3")


    #C0268
    ChrTalk(
        0x109,
        (
            "#10101F嗯，是那辆列车的\x01",
            "前数第二节车厢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78D1")

    Jump("loc_7955")

    label("loc_78D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7955")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7927")

    #C0269
    ChrTalk(
        0x105,
        (
            "#10400F嗯，是那辆列车的\x01",
            "前数第二节车厢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7955")

    label("loc_7927")


    #C0270
    ChrTalk(
        0x105,
        (
            "#10400F嗯，是那辆列车的\x01",
            "前数第二节车厢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7955")

    OP_57(0x0)
    OP_5A()
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_799E")
    OP_68(-1150, 1000, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Jump("loc_79CC")

    label("loc_799E")

    OP_68(-1150, 1000, -16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)

    label("loc_79CC")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A16")
    OP_93(0x106, 0x5A, 0x1F4)

    #C0271
    ChrTalk(
        0x106,
        (
            "#6P#10701F我们可以从前面的\x01",
            "连通桥过去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA3")

    label("loc_7A16")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A5F")
    OP_93(0x105, 0x5A, 0x1F4)

    #C0272
    ChrTalk(
        0x105,
        (
            "#6P#10400F我们可以从前面的\x01",
            "连通桥过去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA3")

    label("loc_7A5F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AA3")
    OP_93(0x109, 0x5A, 0x1F4)

    #C0273
    ChrTalk(
        0x109,
        (
            "#6P#10101F我们可以从前面的\x01",
            "连通桥过去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AA3")


    def lambda_7AA8():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7AA8)
    Sleep(50)

    def lambda_7AB8():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7AB8)
    Sleep(50)

    def lambda_7AC8():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7AC8)
    Sleep(50)

    def lambda_7AD8():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7AD8)
    Sleep(50)

    def lambda_7AE8():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_7AE8)
    Sleep(50)

    def lambda_7AF8():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_7AF8)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0274
    ChrTalk(
        0x101,
        "#5P#00001F好……过去看看吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B61")
    SetChrPos(0x0, -2500, 0, 0, 90)
    Jump("loc_7B72")

    label("loc_7B61")

    SetChrPos(0x0, -2500, 0, -16000, 90)

    label("loc_7B72")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1A5, 7)
    EventEnd(0x5)
    Return()

    # Function_42_7387 end

    def Function_43_7B8C(): pass

    label("Function_43_7B8C")

    EventBegin(0x0)
    Fade(500)
    OP_68(10000, 1200, -27200, 0)
    MoveCamera(30, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17530, 0)
    SetChrPos(0x101, 10000, 0, -28000, 0)
    SetChrPos(0x102, 9000, 0, -29500, 0)
    SetChrPos(0x103, 10200, 0, -29500, 0)
    SetChrPos(0x104, 10900, 0, -30100, 0)
    SetChrPos(0xF4, 8500, 0, -30600, 0)
    SetChrPos(0xF5, 9700, 0, -30600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0275
    ChrTalk(
        0x101,
        (
            "#11P#00008F（三号月台，第二节车厢……\x01",
            "  而且门没有锁。）\x02\x03",

            "#00013F（……怎么办？）\x02",
        )
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
            "开门进去\x01",      # 0
            "离开此处\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7CDF"),
        (1, "loc_7D86"),
        (SWITCH_DEFAULT, "loc_7DB6"),
    )


    label("loc_7CDF")

    Sound(454, 0, 100, 0)
    OP_71(0x0, 0x295, 0x2B2, 0x0, 0x0)
    OP_79(0x0)
    OP_68(10190, 1200, -25980, 4000)

    def lambda_7D0A():
        OP_95(0xFE, 10000, 0, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D0A)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 44)
    Sleep(900)
    BeginChrThread(0x103, 3, 0, 44)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 44)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    BeginChrThread(0xF4, 3, 0, 44)
    Sleep(900)
    BeginChrThread(0xF5, 3, 0, 44)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0xF4, 0xFF)
    EndChrThread(0xF5, 0xFF)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 4)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_7DB6")

    label("loc_7D86")

    SetChrPos(0x0, 8710, 0, -29420, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_7DB6")

    label("loc_7DB6")

    Return()

    # Function_43_7B8C end

    def Function_44_7DB7(): pass

    label("Function_44_7DB7")


    def lambda_7DBC():
        OP_95(0xFE, 10000, 0, -28000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7DBC)
    WaitChrThread(0xFE, 1)

    def lambda_7DDA():
        OP_95(0xFE, 10000, 0, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7DDA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_7DB7 end

    def Function_45_7DF4(): pass

    label("Function_45_7DF4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30200.itc", 0x1E)
    LoadChrToIndex("chr/ch24100.itc", 0x1F)
    LoadChrToIndex("chr/ch21800.itc", 0x20)
    LoadChrToIndex("apl/ch51216.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E33")
    LoadChrToIndex("apl/ch51217.itc", 0x22)
    Jump("loc_7E9A")

    label("loc_7E33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E4E")
    LoadChrToIndex("apl/ch51218.itc", 0x22)
    Jump("loc_7E9A")

    label("loc_7E4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E69")
    LoadChrToIndex("apl/ch51219.itc", 0x22)
    Jump("loc_7E9A")

    label("loc_7E69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E84")
    LoadChrToIndex("apl/ch51220.itc", 0x22)
    Jump("loc_7E9A")

    label("loc_7E84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E9A")
    LoadChrToIndex("apl/ch51221.itc", 0x22)

    label("loc_7E9A")

    LoadChrToIndex("chr/ch24153.itc", 0x23)
    LoadChrToIndex("chr/ch30253.itc", 0x24)
    SoundLoad(453)
    SoundLoad(451)
    SoundLoad(825)
    OP_68(-2990, 1510, -16460, 0)
    MoveCamera(43, 38, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17100, 0)
    SetChrPos(0x101, -13640, 590, -15080, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F14")
    SetChrPos(0x102, -14410, 590, -16430, 90)
    Jump("loc_7FA7")

    label("loc_7F14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F3A")
    SetChrPos(0x103, -14410, 590, -16430, 90)
    Jump("loc_7FA7")

    label("loc_7F3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F60")
    SetChrPos(0x104, -14410, 590, -16430, 90)
    Jump("loc_7FA7")

    label("loc_7F60")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F86")
    SetChrPos(0x109, -14410, 590, -16430, 90)
    Jump("loc_7FA7")

    label("loc_7F86")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FA7")
    SetChrPos(0x105, -14410, 590, -16430, 90)

    label("loc_7FA7")

    SetChrChipByIndex(0x21, 0x1E)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -12200, 590, -15670, 90)
    SetChrChipByIndex(0x22, 0x1F)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12210, 0, -13360, 270)
    SetChrChipByIndex(0x23, 0x20)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 10060, 0, -13390, 90)

    def lambda_8009():
        OP_95(0xFE, -1500, 10, -16020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8009)

    def lambda_8023():
        OP_95(0xFE, -3000, 10, -15160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8023)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8067")

    def lambda_804D():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_804D)
    Jump("loc_811E")

    label("loc_8067")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8096")

    def lambda_807C():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_807C)
    Jump("loc_811E")

    label("loc_8096")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80C5")

    def lambda_80AB():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_80AB)
    Jump("loc_811E")

    label("loc_80C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80F4")

    def lambda_80DA():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_80DA)
    Jump("loc_811E")

    label("loc_80F4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_811E")

    def lambda_8109():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8109)

    label("loc_811E")

    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x21, 1)
    WaitChrThread(0x101, 1)
    Sound(801, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("广播")

    #A0276
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开往共和国列车的\x01",
            "安检工作即将结束。\x02",
        )
    )

    CloseMessageWindow()

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请暂时不要\x01",
            "进入列车内。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0278
    ChrTalk(
        0x101,
        (
            "#00005F去往共和国的列车\x01",
            "马上就要发车了……\x02\x03",

            "#00003F嗯……\x01",
            "假货商在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x21,
        (
            "刚才看到的时候，\x01",
            "明明就在那附近……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_825D")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0280
    ChrTalk(
        0x102,
        "#00101F……找到了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8374")

    label("loc_825D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82A0")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0281
    ChrTalk(
        0x103,
        "#00201F……找到了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8374")

    label("loc_82A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82E3")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0282
    ChrTalk(
        0x104,
        "#00301F……找到了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8374")

    label("loc_82E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_832E")
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x109,
        "#10105F……莫非是那个人吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8374")

    label("loc_832E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8374")
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0284
    ChrTalk(
        0x105,
        "#10305F……莫非是那个人吗？\x02",
    )

    CloseMessageWindow()

    label("loc_8374")

    Fade(500)
    OP_68(11100, 1200, -13380, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14210, 0)
    OP_0D()

    #C0285
    ChrTalk(
        0x23,
        (
            "哦哦，\x01",
            "原来您是同行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x23,
        (
            "在克洛斯贝尔的\x01",
            "生意做得怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #N0287
    NpcTalk(
        0x22,
        "老婆婆",
        "#11P呵呵，很遗憾……\x02",
    )

    CloseMessageWindow()

    #N0288
    NpcTalk(
        0x22,
        "老婆婆",
        (
            "#11P竞争对手暗中使坏，\x01",
            "妨害我正常经营。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x23,
        (
            "唔……\x01",
            "那还真是不幸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x23,
        (
            "真是的，那种人\x01",
            "就是商人中的败类。\x02",
        )
    )

    CloseMessageWindow()

    #N0291
    NpcTalk(
        0x22,
        "老婆婆",
        (
            "#11P不，这也要怪我自己\x01",
            "能力不足。\x02",
        )
    )

    CloseMessageWindow()

    #N0292
    NpcTalk(
        0x22,
        "老婆婆",
        (
            "#11P所以我这次转换了想法，\x01",
            "打算去帝国那边看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x23,
        (
            "哈哈哈，您真是个百折不挠的\x01",
            "商人啊，佩服佩服。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x23,
        (
            "唔，我们在此相遇，\x01",
            "也是一种缘分。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x23,
        (
            "如果您愿意，\x01",
            "我可以把帝国那边的\x01",
            "好渠道介绍给您。\x02",
        )
    )

    CloseMessageWindow()

    #N0296
    NpcTalk(
        0x22,
        "老婆婆",
        "#11P哎呀，真的吗？\x02",
    )

    CloseMessageWindow()

    #N0297
    NpcTalk(
        0x22,
        "老婆婆",
        (
            "#11P呵呵……\x01",
            "虽然有点不好意思，\x01",
            "但我就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        "#00003F……那可不行。\x02",
    )

    CloseMessageWindow()
    OP_63(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0299
    NpcTalk(
        0x22,
        "老婆婆",
        "#11P哎……\x02",
    )

    CloseMessageWindow()
    OP_68(7590, 1700, -13830, 3000)
    MoveCamera(45, 12, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14960, 3000)
    SetChrPos(0x101, 1130, 0, -14460, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8685")
    SetChrPos(0x102, -1220, 0, -14540, 90)
    Jump("loc_8718")

    label("loc_8685")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86AB")
    SetChrPos(0x103, -1220, 0, -14540, 90)
    Jump("loc_8718")

    label("loc_86AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86D1")
    SetChrPos(0x104, -1220, 0, -14540, 90)
    Jump("loc_8718")

    label("loc_86D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86F7")
    SetChrPos(0x109, -1220, 0, -14540, 90)
    Jump("loc_8718")

    label("loc_86F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8718")
    SetChrPos(0x105, -1220, 0, -14540, 90)

    label("loc_8718")

    SetChrPos(0x21, -140, 0, -16200, 90)

    def lambda_872E():
        OP_95(0xFE, 6590, 0, -12750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_872E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8772")

    def lambda_8758():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8758)
    Jump("loc_8829")

    label("loc_8772")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87A1")

    def lambda_8787():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8787)
    Jump("loc_8829")

    label("loc_87A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87D0")

    def lambda_87B6():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_87B6)
    Jump("loc_8829")

    label("loc_87D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87FF")

    def lambda_87E5():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_87E5)
    Jump("loc_8829")

    label("loc_87FF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8829")

    def lambda_8814():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8814)

    label("loc_8829")


    def lambda_882E():
        OP_95(0xFE, 5280, 0, -14060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_882E)
    Sleep(1000)

    def lambda_884B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_884B)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_887E")
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x0)
    Jump("loc_88F9")

    label("loc_887E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_889E")
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x0)
    Jump("loc_88F9")

    label("loc_889E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88BE")
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x0)
    Jump("loc_88F9")

    label("loc_88BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88DE")
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0x5A, 0x0)
    Jump("loc_88F9")

    label("loc_88DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88F9")
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x5A, 0x0)

    label("loc_88F9")

    WaitChrThread(0x21, 1)
    OP_93(0x21, 0x5A, 0x0)
    OP_6F(0x79)

    #C0300
    ChrTalk(
        0x101,
        (
            "#00003F我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的成员。\x02\x03",

            "#00000F老婆婆，好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0301
    NpcTalk(
        0x22,
        "老婆婆",
        "#11P你、你们是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89CA")

    #C0302
    ChrTalk(
        0x102,
        (
            "#00100F呵呵……\x01",
            "您好像还记得我们啊，\x01",
            "假货商婆婆。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AF2")

    label("loc_89CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A0B")

    #C0303
    ChrTalk(
        0x103,
        (
            "#00200F您还记得我们吧……\x01",
            "假货商婆婆。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AF2")

    label("loc_8A0B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A5F")

    #C0304
    ChrTalk(
        0x104,
        (
            "#00300F嘿嘿，看样子，\x01",
            "你好像还记得我们啊，\x01",
            "假货商老婆婆。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AF2")

    label("loc_8A5F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AA6")

    #C0305
    ChrTalk(
        0x109,
        (
            "#10101F这个人就是你们\x01",
            "说过的那名假货商吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AF2")

    label("loc_8AA6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AF2")

    #C0306
    ChrTalk(
        0x105,
        (
            "#10304F原来如此，这位女士就是\x01",
            "你们说过的那名假货商啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AF2")


    #C0307
    ChrTalk(
        0x21,
        (
            "她好像以为\x01",
            "完全甩掉\x01",
            "我们了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x21,
        "呵呵，这次可不会再让你跑掉啦～！\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x23,
        (
            "哎、哎呀……\x01",
            "这到底是\x01",
            "怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x23,
        (
            "假货商……？\x01",
            "你们在说什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #N0311
    NpcTalk(
        0x22,
        "老婆婆",
        "#11P……唔……唔唔……\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#00003F根据自治州法的修正条例，\x01",
            "您有从事违法交易的嫌疑，\x01",
            "请跟我们走一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x21,
        (
            "车站已经被包围，\x01",
            "您已经无处可逃了～\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x21,
        (
            "最好放弃\x01",
            "继续逃跑的\x01",
            "想法哦～\x02",
        )
    )

    CloseMessageWindow()

    #N0315
    NpcTalk(
        0x22,
        "老婆婆",
        (
            "#11P………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    #N0316
    NpcTalk(
        0x22,
        "老婆婆",
        (
            "#11P………………………………\x01",
            "………开………啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        "#00005F……！\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0318
    ChrTalk(
        0x22,
        (
            "#11P#5S开什么玩笑啊！\x01",
            "你们这帮臭小鬼！！！！！#3S\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x22, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D4C")

    #C0319
    ChrTalk(
        0x102,
        "#00105F呀！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DF5")

    label("loc_8D4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D78")

    #C0320
    ChrTalk(
        0x103,
        "#00210F…………！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DF5")

    label("loc_8D78")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DA0")

    #C0321
    ChrTalk(
        0x104,
        "#00305F哇哇！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DF5")

    label("loc_8DA0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DD0")

    #C0322
    ChrTalk(
        0x109,
        "#10105F咦咦咦咦咦！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DF5")

    label("loc_8DD0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DF5")

    #C0323
    ChrTalk(
        0x105,
        "#10305F……喔¤\x02",
    )

    CloseMessageWindow()

    label("loc_8DF5")


    #C0324
    ChrTalk(
        0x21,
        "哇呀呀！\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x23,
        "怎、怎怎怎……怎么回事……！？\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0326
    ChrTalk(
        0x22,
        (
            "#11P#5S竟然追到这种地方，\x01",
            "不肯让我轻易逃走……#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0327
    ChrTalk(
        0x22,
        (
            "#11P#5S你们一而再，\x01",
            "再而三地\x01",
            "算计我！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0328
    ChrTalk(
        0x22,
        (
            "#11P#5S就会耍些奸诈的小花招！\x01",
            "所以我才讨厌警察！#3S\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#00006F这、这个，也不能说是奸诈吧……\x01",
            "逃进车站难道不是\x01",
            "您自己的失误……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0330
    ChrTalk(
        0x22,
        "#11P#5S给我闭嘴！#3S\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x22,
        (
            "#11P……哼，无所谓。\x01",
            "被包围了\x01",
            "又如何……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_96(0x22, 0x3458, 0x0, 0xFFFFCBD0, 0x3E8, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0332
    ChrTalk(
        0x22,
        (
            "#11P#5S#15A#N你们要是抓得到我，\x01",
            "就来试试看吧！！！！！#3S\x02",
        )
    )
    #Auto

    OP_93(0x22, 0x5A, 0x1F4)
    Sound(250, 0, 100, 0)
    OP_95(0x22, 25000, 0, -13360, 5000, 0x0)
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0x22, 0x80)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x21, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0333
    ChrTalk(
        0x101,
        (
            "#00006F再、再次看到这一幕，\x01",
            "仍然觉得冲击力十足……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9108")

    #C0334
    ChrTalk(
        0x102,
        (
            "#00107F喂，罗伊德！\x01",
            "现在不是发呆的时候……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9220")

    label("loc_9108")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9151")

    #C0335
    ChrTalk(
        0x103,
        (
            "#00205F……罗伊德前辈！\x01",
            "现在不是发呆的时候……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9220")

    label("loc_9151")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9198")

    #C0336
    ChrTalk(
        0x104,
        (
            "#00307F喂，罗伊德！\x01",
            "现在可不是发呆的时候啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9220")

    label("loc_9198")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91E8")

    #C0337
    ChrTalk(
        0x109,
        (
            "#10105F啊……\x01",
            "罗、罗伊德警官！\x01",
            "现在不是发呆的时候……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9220")

    label("loc_91E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9220")

    #C0338
    ChrTalk(
        0x105,
        (
            "#10301F……现在不是\x01",
            "发呆的时候吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9220")


    #C0339
    ChrTalk(
        0x21,
        "是、是啊！\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#00011F是、是的，我们快追！\x02\x03",

            "#00000F大家已经\x01",
            "把出入口守住了……\x01",
            "接下来就只剩抓住她了！！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 46)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92AF")
    BeginChrThread(0x102, 1, 0, 47)
    Jump("loc_9316")

    label("loc_92AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92CA")
    BeginChrThread(0x103, 1, 0, 47)
    Jump("loc_9316")

    label("loc_92CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92E5")
    BeginChrThread(0x104, 1, 0, 47)
    Jump("loc_9316")

    label("loc_92E5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9300")
    BeginChrThread(0x109, 1, 0, 47)
    Jump("loc_9316")

    label("loc_9300")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9316")
    BeginChrThread(0x105, 1, 0, 47)

    label("loc_9316")

    BeginChrThread(0x21, 1, 0, 48)
    Sleep(3500)
    OP_63(0x23, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x23)

    #C0341
    ChrTalk(
        0x23,
        "（目瞪口呆）……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9375")
    EndChrThread(0x102, 0x1)
    Jump("loc_93D4")

    label("loc_9375")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_938E")
    EndChrThread(0x103, 0x1)
    Jump("loc_93D4")

    label("loc_938E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93A7")
    EndChrThread(0x104, 0x1)
    Jump("loc_93D4")

    label("loc_93A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93C0")
    EndChrThread(0x109, 0x1)
    Jump("loc_93D4")

    label("loc_93C0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93D4")
    EndChrThread(0x105, 0x1)

    label("loc_93D4")

    EndChrThread(0x101, 0x1)
    OP_68(36050, 1500, -13190, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrPos(0x22, 54750, 0, -15970, 90)
    OP_6B(0x22)
    Sleep(100)
    BeginChrThread(0x22, 1, 0, 49)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)

    #C0342
    ChrTalk(
        0x22,
        "啧，那帮可恶的臭小鬼……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x22, 1)

    #C0343
    ChrTalk(
        0x22,
        (
            "既然他们已经在车站内设了埋伏，\x01",
            "我就只能另辟蹊径了……\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x1F4)
    Sound(801, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("广播")

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "让各位久等了，\x01",
            "去往共和国的列车\x01",
            "即将发车。\x02",
        )
    )

    CloseMessageWindow()

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "为了避免危险，\x01",
            "请勿追赶列车。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0x3E8)
    OP_63(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0346
    ChrTalk(
        0x22,
        "……有了！\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6B(0xFF)
    OP_68(65349, 7430, -15360, 0)
    MoveCamera(63, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14220, 0)
    SetChrPos(0x101, 55180, 0, -15400, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95DE")
    SetChrPos(0x102, 54450, 0, -16550, 90)
    Jump("loc_9671")

    label("loc_95DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9604")
    SetChrPos(0x103, 54450, 0, -16550, 90)
    Jump("loc_9671")

    label("loc_9604")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_962A")
    SetChrPos(0x104, 54450, 0, -16550, 90)
    Jump("loc_9671")

    label("loc_962A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9650")
    SetChrPos(0x109, 54450, 0, -16550, 90)
    Jump("loc_9671")

    label("loc_9650")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9671")
    SetChrPos(0x105, 54450, 0, -16550, 90)

    label("loc_9671")

    SetChrPos(0x21, 53420, 0, -15670, 90)

    def lambda_9687():
        OP_95(0xFE, 66750, 6000, -15280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9687)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96CE")

    def lambda_96B4():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_96B4)
    Jump("loc_9785")

    label("loc_96CE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96FD")

    def lambda_96E3():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_96E3)
    Jump("loc_9785")

    label("loc_96FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_972C")

    def lambda_9712():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9712)
    Jump("loc_9785")

    label("loc_972C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_975B")

    def lambda_9741():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9741)
    Jump("loc_9785")

    label("loc_975B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9785")

    def lambda_9770():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9770)

    label("loc_9785")

    Sleep(100)

    def lambda_978D():
        OP_95(0xFE, 65090, 6000, -15890, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_978D)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_97AC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97AC)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97DA")
    WaitChrThread(0x102, 1)

    def lambda_97CD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_97CD)
    Jump("loc_986D")

    label("loc_97DA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9800")
    WaitChrThread(0x103, 1)

    def lambda_97F3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_97F3)
    Jump("loc_986D")

    label("loc_9800")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9826")
    WaitChrThread(0x104, 1)

    def lambda_9819():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9819)
    Jump("loc_986D")

    label("loc_9826")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_984C")
    WaitChrThread(0x109, 1)

    def lambda_983F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_983F)
    Jump("loc_986D")

    label("loc_984C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_986D")
    WaitChrThread(0x105, 1)

    def lambda_9865():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9865)

    label("loc_986D")

    WaitChrThread(0x21, 1)

    def lambda_9876():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_9876)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0347
    ChrTalk(
        0x101,
        "#00005F#5S那、那是……！#3S\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(34280, 1500, 9060, 0)
    MoveCamera(43, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30010, 0)
    ClearChrFlags(0x22, 0x80)
    OP_0D()
    Sound(490, 0, 100, 0)
    Sleep(500)
    Sound(453, 0, 100, 0)
    Sound(825, 2, 50, 0)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    BeginChrThread(0x8, 1, 0, 53)
    OP_68(69980, 1500, 7190, 5000)
    MoveCamera(43, 28, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(30010, 5000)
    SetChrPos(0x22, 66310, 6000, -6920, 0)
    SetChrFlags(0x22, 0x40)
    Sleep(2200)
    OP_95(0x22, 66280, 6000, 140, 4000, 0x0)
    Sound(844, 0, 80, 0)
    OP_9D(0x22, 0x10306, 0x1770, 0x1E96, 0x5DC, 0xBB8)
    Sound(326, 0, 70, 0)
    SetChrChipByIndex(0x22, 0x23)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x20)

    def lambda_99F0():
        OP_96(0xFE, 0x33450, 0xFFFFF9F2, 0x1FA4, 0x251C, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_99F0)
    Sleep(2000)

    #C0348
    ChrTalk(
        0x21,
        "#5S#6A咦咦咦咦咦咦咦咦咦咦！！#3S\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    Sound(451, 2, 50, 0)
    Fade(500)
    OP_68(65349, 7430, -15360, 0)
    MoveCamera(63, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14220, 0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x22, 0x1)
    SetChrFlags(0x22, 0x80)
    OP_0D()

    #C0349
    ChrTalk(
        0x101,
        "#00011F她、她竟然……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9ACC")

    #C0350
    ChrTalk(
        0x102,
        "#00105F不、不会吧……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B93")

    label("loc_9ACC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AFE")

    #C0351
    ChrTalk(
        0x103,
        "#00205F怎、怎么会……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B93")

    label("loc_9AFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B32")

    #C0352
    ChrTalk(
        0x104,
        "#00305F喂喂，真的假的！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B93")

    label("loc_9B32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B68")

    #C0353
    ChrTalk(
        0x109,
        "#10101F唔……真是不择手段！\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B93")

    label("loc_9B68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B93")

    #C0354
    ChrTalk(
        0x105,
        "#10305F……真厉害啊。\x02",
    )

    CloseMessageWindow()

    label("loc_9B93")


    #C0355
    ChrTalk(
        0x21,
        "竟、竟然在最后的最后让她跑掉了……！\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x21,
        (
            "啊啊，我该如何向\x01",
            "多诺邦警督交待啊……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x101,
        "#00003F……………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C6C")

    #C0358
    ChrTalk(
        0x101,
        "#00001F……我们上，艾莉！\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x102,
        (
            "#00105F……！\x01",
            "好、好的，我明白了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DBB")

    label("loc_9C6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CBA")

    #C0360
    ChrTalk(
        0x101,
        "#00001F……我们上，缇欧！\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x103,
        (
            "#00201F……！\x01",
            "明白！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DBB")

    label("loc_9CBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D0E")

    #C0362
    ChrTalk(
        0x101,
        "#00001F……我们上，兰迪！\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x104,
        (
            "#00302F……！\x01",
            "嗯，没问题！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DBB")

    label("loc_9D0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D5E")

    #C0364
    ChrTalk(
        0x101,
        "#00001F……我们上，诺艾尔！\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x109,
        (
            "#10107F……！\x01",
            "遵命！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DBB")

    label("loc_9D5E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DBB")

    #C0366
    ChrTalk(
        0x101,
        "#00001F……我们上，瓦吉！\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x105,
        (
            "#10304F呵呵……\x01",
            "你的疯狂程度不输于她呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DBB")

    OP_93(0x21, 0x5A, 0x1F4)
    OP_63(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0368
    ChrTalk(
        0x21,
        "……咦……难道说……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0369
    ChrTalk(
        0x21,
        "#5S……咦咦！？#3S\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x21,
        (
            "不、不会吧……？\x01",
            "你们要追上去！？\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#00007F要想抓住她，\x01",
            "就只能追上去了！\x02\x03",

            "#00003F没时间了……\x01",
            "我们先告辞了！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_9EA1():
        OP_95(0xFE, 66750, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9EA1)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EE8")

    def lambda_9ECE():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9ECE)
    Jump("loc_9F9F")

    label("loc_9EE8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F17")

    def lambda_9EFD():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9EFD)
    Jump("loc_9F9F")

    label("loc_9F17")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F46")

    def lambda_9F2C():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9F2C)
    Jump("loc_9F9F")

    label("loc_9F46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F75")

    def lambda_9F5B():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9F5B)
    Jump("loc_9F9F")

    label("loc_9F75")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F9F")

    def lambda_9F8A():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9F8A)

    label("loc_9F9F")

    OP_63(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(2000)
    OP_64(0x21)

    #C0372
    ChrTalk(
        0x21,
        (
            "怎、怎么办……\x01",
            "总不能全部交给支援科……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x21)

    #C0373
    ChrTalk(
        0x21,
        "#5S……呜、呜啊啊啊啊啊啊！#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0x21, 65890, 6000, -15300, 4000, 0x0)

    def lambda_A04B():
        OP_95(0xFE, 66750, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A04B)
    Sleep(1000)
    Fade(500)
    EndChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A085")
    EndChrThread(0x102, 0x1)
    Jump("loc_A0E4")

    label("loc_A085")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A09E")
    EndChrThread(0x103, 0x1)
    Jump("loc_A0E4")

    label("loc_A09E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A0B7")
    EndChrThread(0x104, 0x1)
    Jump("loc_A0E4")

    label("loc_A0B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A0D0")
    EndChrThread(0x109, 0x1)
    Jump("loc_A0E4")

    label("loc_A0D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A0E4")
    EndChrThread(0x105, 0x1)

    label("loc_A0E4")

    EndChrThread(0x21, 0x1)
    OP_68(69980, 1500, 7190, 0)
    MoveCamera(43, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30010, 0)
    SetChrPos(0x101, 66310, 6000, -9500, 0)
    SetChrFlags(0x101, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A157")
    SetChrPos(0x102, 66090, 6000, -10500, 0)
    SetChrFlags(0x102, 0x40)
    Jump("loc_A1FE")

    label("loc_A157")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A182")
    SetChrPos(0x103, 66090, 6000, -10500, 0)
    SetChrFlags(0x103, 0x40)
    Jump("loc_A1FE")

    label("loc_A182")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1AD")
    SetChrPos(0x104, 66090, 6000, -10500, 0)
    SetChrFlags(0x104, 0x40)
    Jump("loc_A1FE")

    label("loc_A1AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1D8")
    SetChrPos(0x109, 66090, 6000, -10500, 0)
    SetChrFlags(0x109, 0x40)
    Jump("loc_A1FE")

    label("loc_A1D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1FE")
    SetChrPos(0x105, 66090, 6000, -10500, 0)
    SetChrFlags(0x105, 0x40)

    label("loc_A1FE")

    SetChrPos(0x21, 66310, 6000, -11500, 0)
    SetChrFlags(0x21, 0x40)
    Sound(456, 0, 100, 0)
    StopSound(835, 1000, 100)
    BeginChrThread(0x8, 1, 0, 54)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 50)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A24B")
    BeginChrThread(0x102, 1, 0, 51)
    Jump("loc_A2B2")

    label("loc_A24B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A266")
    BeginChrThread(0x103, 1, 0, 51)
    Jump("loc_A2B2")

    label("loc_A266")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A281")
    BeginChrThread(0x104, 1, 0, 51)
    Jump("loc_A2B2")

    label("loc_A281")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A29C")
    BeginChrThread(0x109, 1, 0, 51)
    Jump("loc_A2B2")

    label("loc_A29C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2B2")
    BeginChrThread(0x105, 1, 0, 51)

    label("loc_A2B2")

    Sleep(500)
    BeginChrThread(0x21, 1, 0, 52)
    Sleep(2000)
    Sleep(4000)
    StopSound(451, 1000, 50)
    StopSound(825, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A30B")
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x1000)
    Jump("loc_A396")

    label("loc_A30B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A32F")
    ClearChrFlags(0x103, 0x40)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x1000)
    Jump("loc_A396")

    label("loc_A32F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A353")
    ClearChrFlags(0x104, 0x40)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x1000)
    Jump("loc_A396")

    label("loc_A353")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A377")
    ClearChrFlags(0x109, 0x40)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x1000)
    Jump("loc_A396")

    label("loc_A377")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A396")
    ClearChrFlags(0x105, 0x40)
    ClearChrFlags(0x105, 0x20)
    ClearChrFlags(0x105, 0x1000)

    label("loc_A396")

    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("e4800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_7DF4 end

    def Function_46_A3A9(): pass

    label("Function_46_A3A9")

    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_46_A3A9 end

    def Function_47_A3D2(): pass

    label("Function_47_A3D2")

    Sleep(200)
    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_47_A3D2 end

    def Function_48_A3FE(): pass

    label("Function_48_A3FE")

    Sleep(800)
    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_48_A3FE end

    def Function_49_A42A(): pass

    label("Function_49_A42A")

    OP_95(0xFE, 66190, 6000, -15970, 4000, 0x0)
    OP_95(0xFE, 66190, 6000, -5060, 4000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_49_A42A end

    def Function_50_A45A(): pass

    label("Function_50_A45A")

    OP_95(0xFE, 66280, 6000, 140, 4000, 0x0)
    Sound(844, 0, 80, 0)
    OP_9D(0xFE, 0x102E8, 0x1770, 0x1E96, 0x5DC, 0xBB8)
    Sound(326, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_96(0xFE, 0x33450, 0xFFFFF9F2, 0x1FA4, 0x251C, 0x0)
    Return()

    # Function_50_A45A end

    def Function_51_A4B8(): pass

    label("Function_51_A4B8")

    OP_95(0xFE, 66090, 6000, 140, 4000, 0x0)
    Sound(844, 0, 80, 0)
    OP_9D(0xFE, 0x1022A, 0x1770, 0x1E96, 0x5DC, 0xBB8)
    Sound(326, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_96(0xFE, 0x33450, 0xFFFFF9F2, 0x1FA4, 0x251C, 0x0)
    Return()

    # Function_51_A4B8 end

    def Function_52_A516(): pass

    label("Function_52_A516")

    OP_95(0xFE, 66280, 6000, 140, 4000, 0x0)
    Sound(844, 0, 80, 0)
    OP_9D(0xFE, 0x102E8, 0x1770, 0x1E96, 0x5DC, 0xBB8)
    Sound(326, 0, 70, 0)
    OP_64(0xFE)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    OP_96(0xFE, 0x33450, 0xFFFFF9F2, 0x1FA4, 0x251C, 0x0)
    Return()

    # Function_52_A516 end

    def Function_53_A572(): pass

    label("Function_53_A572")


    def lambda_A577():
        OP_95(0xFE, 210000, -1550, 8100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A577)
    Sleep(500)

    def lambda_A594():
        OP_95(0xFE, 210000, -1550, 8100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A594)
    Sleep(700)

    def lambda_A5B1():
        OP_95(0xFE, 210000, -1550, 8100, 8500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A5B1)
    Sleep(800)

    def lambda_A5CE():
        OP_95(0xFE, 210000, -1550, 8100, 9500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A5CE)
    Return()

    # Function_53_A572 end

    def Function_54_A5E4(): pass

    label("Function_54_A5E4")

    SetChrPos(0x8, 70000, -1550, 8100, 0)

    def lambda_A5FA():
        OP_95(0xFE, 210000, -1550, 8100, 9500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A5FA)
    Return()

    # Function_54_A5E4 end

    def Function_55_A610(): pass

    label("Function_55_A610")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x1, 0x8)
    OP_49()
    SetChrPos(0x8, 7000, -1550, -8100, 0)
    OP_D5(0x8, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_68(65000, 10000, -11000, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(30000, 0)
    OP_F0(0x0, 0x1)
    OP_71(0x1, 0x3D, 0x3D, 0x0, 0x0)
    SoundLoad(452)
    OP_68(25000, 1500, -11000, 15000)
    MoveCamera(47, 17, 0, 15000)
    SetCameraDistance(50000, 15000)
    Sound(801, 0, 100, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    Sound(452, 0, 100, 0)
    BeginChrThread(0x25, 1, 0, 56)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x168, 0x0, 0x0)
    OP_6F(0x79)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x17B, 5)
    SetScenarioFlags(0x22, 1)
    NewScene("c0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_A610 end

    def Function_56_A70E(): pass

    label("Function_56_A70E")

    Sleep(11000)
    Sound(143, 0, 50, 0)
    Return()

    # Function_56_A70E end

    SaveToFile()

Try(main)
