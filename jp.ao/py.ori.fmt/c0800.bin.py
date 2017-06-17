from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "列車",                   # 1
        "列車",                   # 2
        "キーア",                 # 3
        "フラン",                 # 4
        "セルゲイ課長",           # 5
        "オズボーン宰相",         # 6
        "レクター",               # 7
        "オリヴァルト皇子",       # 8
        "ミュラー少佐",           # 9
        "乗客",                   # 10
        "乗客",                   # 11
        "乗客",                   # 12
        "乗客",                   # 13
        "乗客",                   # 14
        "乗客",                   # 15
        "乗客",                   # 16
        "乗客",                   # 17
        "駅員",                   # 18
        "帝国軍仕官",             # 19
        "帝国軍仕官",             # 20
        "帝国軍仕官",             # 21
        "帝国軍仕官",             # 22
        "帝国軍仕官",             # 23
        "帝国軍仕官",             # 24
        "臨検官マーロウ",         # 25
        "レイモンド捜査官",       # 26
        "偽ブランド商",           # 27
        "帝国商人",               # 28
        "列車",                   # 29
        "SE制御",                 # 30
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
        "Function_3_3143",         # 03, 3
        "Function_4_3187",         # 04, 4
        "Function_5_31DD",         # 05, 5
        "Function_6_3233",         # 06, 6
        "Function_7_328E",         # 07, 7
        "Function_8_32E1",         # 08, 8
        "Function_9_332D",         # 09, 9
        "Function_10_3381",        # 0A, 10
        "Function_11_33B1",        # 0B, 11
        "Function_12_3B1C",        # 0C, 12
        "Function_13_3B68",        # 0D, 13
        "Function_14_3BA4",        # 0E, 14
        "Function_15_3BBB",        # 0F, 15
        "Function_16_3BF7",        # 10, 16
        "Function_17_3C0E",        # 11, 17
        "Function_18_3C4A",        # 12, 18
        "Function_19_3C61",        # 13, 19
        "Function_20_3CAE",        # 14, 20
        "Function_21_3CBE",        # 15, 21
        "Function_22_3CFA",        # 16, 22
        "Function_23_3D0A",        # 17, 23
        "Function_24_3D21",        # 18, 24
        "Function_25_3D5D",        # 19, 25
        "Function_26_3D74",        # 1A, 26
        "Function_27_3DB0",        # 1B, 27
        "Function_28_3DC7",        # 1C, 28
        "Function_29_3E03",        # 1D, 29
        "Function_30_3E1A",        # 1E, 30
        "Function_31_3E67",        # 1F, 31
        "Function_32_3E77",        # 20, 32
        "Function_33_3EB3",        # 21, 33
        "Function_34_3EC3",        # 22, 34
        "Function_35_3EDF",        # 23, 35
        "Function_36_3EF6",        # 24, 36
        "Function_37_3F3D",        # 25, 37
        "Function_38_3F84",        # 26, 38
        "Function_39_6650",        # 27, 39
        "Function_40_6681",        # 28, 40
        "Function_41_6B81",        # 29, 41
        "Function_42_7BEE",        # 2A, 42
        "Function_43_849F",        # 2B, 43
        "Function_44_86EA",        # 2C, 44
        "Function_45_8727",        # 2D, 45
        "Function_46_AF4A",        # 2E, 46
        "Function_47_AF73",        # 2F, 47
        "Function_48_AF9F",        # 30, 48
        "Function_49_AFCB",        # 31, 49
        "Function_50_AFFB",        # 32, 50
        "Function_51_B059",        # 33, 51
        "Function_52_B0B7",        # 34, 52
        "Function_53_B113",        # 35, 53
        "Function_54_B185",        # 36, 54
        "Function_55_B1B1",        # 37, 55
        "Function_56_B2AF",        # 38, 56
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
        "少女の声",
        "#4S#3595V#21A#30Wロイド────っ！！\x02",
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
        "#11P#00005F#3315V#30Wあ……\x02",
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

    def lambda_F9E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F9E)

    def lambda_FAF():
        OP_95(0xFE, 3250, 0, -15450, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FAF)
    Sleep(2000)

    def lambda_FCC():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFC3D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FCC)
    Sleep(50)
    Sound(3037, 255, 100, 0)    #voice#KeA
    BeginChrThread(0x109, 3, 0, 10)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x0)

    def lambda_1001():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1001)
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0003
    ChrTalk(
        0x101,
        (
            "#12P#00002F#3316V#30Wキーア……！\x01",
            "迎えに来てくれたのか。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCF4)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)

    def lambda_1072():
        OP_96(0xFE, 0xB54, 0x0, 0xFFFFC3D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1072)
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
            "#3596V#30Wうんっ！\x01",
            "今日帰ってくるって聞いたから！\x02\x03",

            "#3597Vだいじょうぶ！？\x01",
            "どこもケガをしてない！？\x02",
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
            "#12P#00004Fああ、平気だよ。\x02\x03",

            "#00002Fただいま、キーア。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xA,
        "#01109F#5Pおかえりっ、ロイド！\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x87, 0x1F4)
    Sleep(300)

    #C0007
    ChrTalk(
        0xA,
        (
            "#01121F#5Pえへへ……\x01",
            "ノエルもおかえりなさい！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            "#12P#10109Fあはは……\x01",
            "ただいま、キーアちゃん。\x02",
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
        "娘の声",
        "#2708V#18A#30Wおねえちゃ～～ん！！\x02",
    )
    #Auto
    Sleep(300)

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0xB, 0x8)

    def lambda_12DE():
        OP_95(0xFE, 4350, 0, -16650, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12DE)
    Sleep(300)

    def lambda_12FB():

        label("loc_12FB")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_12FB")

    QueueWorkItem2(0xA, 2, lambda_12FB)

    def lambda_130D():

        label("loc_130D")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_130D")

    QueueWorkItem2(0x101, 2, lambda_130D)
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

    def lambda_1359():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1359)
    Sound(811, 0, 100, 0)
    Sleep(500)

    #C0010
    ChrTalk(
        0x109,
        "#12P#10111F#3513V#30Wわわっ、フラン！？\x02",
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
            "#2709V#30Wふええん……！\x01",
            "お姉ちゃんが無事でよかった！\x02\x03",

            "#2710Vおかえりなさいっ！\x01",
            "ケガとかしてないよね～！？\x02",
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
            "#12P#10102Fうん、見ての通り大丈夫。\x02\x03",

            "#10106Fていうか、たった数日なのに\x01",
            "そんな大げさにしなくても……\x02",
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

    def lambda_1532():
        OP_96(0xFE, 0xFA0, 0x0, 0xFFFFBEC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1532)
    WaitChrThread(0xB, 1)
    Sleep(150)

    #C0013
    ChrTalk(
        0xB,
        (
            "#01903F#5Pお姉ちゃんは分かってません！\x01",
            "時間なんて関係ないんだよ～。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)
    Sleep(150)

    #C0014
    ChrTalk(
        0xB,
        "#6P#01909Fねー、キーアちゃん？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xA,
        "#5P#01101Fそーそー、その通り！\x02",
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
        "#00012Fはは……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x109,
        (
            "#12P#10112F何だか戻ってきたって\x01",
            "実感がありますね……\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_16FE")

    #N0018
    NpcTalk(
        0x102,
        "娘の声",
        "#3385Vロイド#30W……おかえりなさい。\x02",
    )

    CloseMessageWindow()
    OP_24(0xD39)
    OP_C9(0x1, 0x80000000)
    Jump("loc_1743")

    label("loc_16FE")


    #N0019
    NpcTalk(
        0x102,
        "娘の声",
        (
            "#3386V#30Wふふっ……\x01",
            "２人ともお疲れさまでした。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD3A)
    OP_C9(0x1, 0x80000000)

    label("loc_1743")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1778():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1778)
    Sleep(50)

    def lambda_1788():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1788)
    Sleep(50)

    def lambda_1798():
        OP_93(0xA, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1798)
    Sleep(50)

    def lambda_17A8():
        OP_93(0xB, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_17A8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)

    #C0020
    ChrTalk(
        0x101,
        "#12P#00002Fあ……\x02",
    )

    CloseMessageWindow()
    OP_68(-6900, 1400, -16000, 3000)
    MoveCamera(321, 21, 0, 3000)
    SetCameraDistance(14500, 3000)
    Sleep(1300)

    def lambda_1807():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1807)

    def lambda_1818():
        OP_96(0xFE, 0xFFFFE124, 0x258, 0xFFFFC374, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1818)
    Sleep(100)

    def lambda_1835():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1835)

    def lambda_1846():
        OP_96(0xFE, 0xFFFFDE68, 0x258, 0xFFFFBF8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1846)
    WaitChrThread(0x102, 1)
    WaitChrThread(0xC, 1)
    OP_6F(0x79)
    Sleep(300)

    def lambda_186D():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFC374, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_186D)
    Sleep(100)

    def lambda_188A():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFFBF8C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_188A)
    Sleep(2500)
    Fade(500)
    OP_68(2600, 900, -15600, 0)
    MoveCamera(325, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(14000, 1500)

    def lambda_18E3():
        OP_96(0xFE, 0x1004, 0x0, 0xFFFFC5CC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_18E3)
    Sleep(50)

    def lambda_1900():
        OP_96(0xFE, 0x1130, 0x0, 0xFFFFBBA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1900)
    WaitChrThread(0xA, 1)

    def lambda_191E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_191E)
    WaitChrThread(0x102, 1)

    #C0021
    ChrTalk(
        0x101,
        (
            "#12P#00002Fエリィ！\x01",
            "もう戻ってきたのか！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_1EB1")
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
            "#3387V#30Wう、うん、つい昨日にね。\x02\x03",

            "#3389Vおじいさまの手伝いも終わったし、\x01",
            "私も今日から復帰できるわ。\x02",
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
            "#12P#00002F#30Wそっか……\x01",
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
            "#01105F#11Pねーねー。\x02\x03",

            "ロイドとエリィ、\x01",
            "見つめ合ってどうしたのー？\x02",
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

    def lambda_1B58():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1B58)

    def lambda_1B65():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1B65)
    TurnDirection(0x101, 0xA, 700)

    #C0025
    ChrTalk(
        0x101,
        (
            "#6P#00011Fい、いや！\x01",
            "別に何でもないって！\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#00109F#5Pそ、そうそう。\x01",
            "久しぶりだったから\x01",
            "つい懐かしいなぁっていうか！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        "#01100F#11Pんー？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xB,
        (
            "#6P#01902F（うーん……\x01",
            "  なんかラブラブだなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x109,
        (
            "#12P#10114F（ねえ、やっぱりこの２人って\x01",
            "  そういう関係なの……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        (
            "#6P#01900F（わたしの見立てだと\x01",
            "  決定的な関係じゃないみたい。）\x02\x03",

            "#01909F（えへへ、気になるなら\x01",
            "  まだチャンスはあるかもよ～？）\x02",
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
        "#11P#10111F（あ、あたしはそんな……！）\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0032
    ChrTalk(
        0x102,
        (
            "#00109F#5Pあ、ノエルさんもお疲れさま。\x02\x03",

            "#00102F危険なことはなかった？\x01",
            "ロイド、たまに無茶なことを\x01",
            "しでかすことがあるから……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)
    Sleep(150)

    #C0033
    ChrTalk(
        0x109,
        (
            "#12P#10112Fい、いえいえ。\x01",
            "エリィさんこそお疲れさまです。\x02\x03",

            "#10100Fたしかマクダエル議長の付き合いで\x01",
            "各国を回ってたんですよね？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E94():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E94)
    Sleep(50)

    def lambda_1EA4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1EA4)
    Jump("loc_2027")

    label("loc_1EB1")

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
            "#3388V#30Wええ、つい昨日にね。\x02\x03",

            "#3389Vおじいさまの手伝いも終わったし、\x01",
            "私も今日から復帰できるわ。\x02",
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
        "#12P#00002Fそっか……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x109,
        (
            "#12P#10109Fお疲れさまです、エリィさん。\x02\x03",

            "#10100Fたしかマクダエル議長の付き合いで\x01",
            "各国を回ってたんですよね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2027")


    #C0037
    ChrTalk(
        0x102,
        (
            "#00104F#5Pええ、大した手伝いが\x01",
            "出来たわけじゃないけど。\x02\x03",

            "#00100Fでも、色々と面白い情報を\x01",
            "仕入れてくることが出来たわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#12P#00000Fそっか……\x01",
            "後で改めて聞かせてもらうよ。\x02\x03",

            "#00006Fしかし、これで\x01",
            "ティオとランディが戻ってたら\x01",
            "言うことないんだけどな……\x02",
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
            "ま、今月中には\x01",
            "２人とも戻ってくるだろう。\x02\x03",

            "それより、ロイド。\x01",
            "ちゃんとケリは付けてきたのか？\x02",
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
            "#12P#00003F……はい。\x01",
            "無事、両名とも逮捕しました。\x02\x03",

            "#00001Fダドリーさんとアリオスさんが\x01",
            "拘置所の方に護送しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xC,
        (
            "#01003F#5Pそうか……\x02\x03",

            "#01002Fま、これで教団絡みの事件は\x01",
            "一段落したと見ていいだろう。\x02\x03",

            "分かってると思うが……\x01",
            "ボチボチ頭を切り替えてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#12P#00000Fはい、そのつもりです。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xC,
        (
            "#01002F#5Pノエルの方は\x01",
            "あらためてよろしく頼む。\x02\x03",

            "今日からでいいんだったな？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2389():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2389)
    Sleep(100)

    def lambda_2399():
        TurnDirection(0xB, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2399)
    Sleep(100)

    def lambda_23A9():
        TurnDirection(0xA, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_23A9)
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
            "#12P#10103Fノエル・シーカー！\x02\x03",

            "#10101F本日より特務支援課へ\x01",
            "出向させていただきます！\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xA,
        "#11P#01105Fほえ～……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "#6P#01909Fえへへ……\x01",
            "これでお姉ちゃんもお仲間だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xC,
        (
            "#01006F#5Pあー、そんなに\x01",
            "畏#2Rかしこ#まらなくてもいい。\x02\x03",

            "#01000Fソーニャからも聞いてるだろうが\x01",
            "ウチにはウチのペースがある。\x02\x03",

            "軍隊式の上意下達#8Rじょういかたつ#は\x01",
            "とりあえず捨ててもらうぞ。\x02",
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
        "#12P#10105Fど、努力します。\x02",
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
        "少年の声",
        (
            "#2904V#30Wふふ……\x01",
            "揃っているみたいだね。\x02",
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

    def lambda_2631():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2631)
    Sleep(50)

    def lambda_2641():
        TurnDirection(0xA, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2641)
    Sleep(50)

    def lambda_2651():
        TurnDirection(0xB, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2651)
    Sleep(50)

    def lambda_2661():
        TurnDirection(0xC, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_2661)
    Sleep(50)

    def lambda_2671():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2671)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x102, 0)

    def lambda_2695():

        label("loc_2695")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_2695")

    QueueWorkItem2(0x102, 2, lambda_2695)

    def lambda_26A7():

        label("loc_26A7")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_26A7")

    QueueWorkItem2(0xC, 2, lambda_26A7)

    def lambda_26B9():

        label("loc_26B9")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_26B9")

    QueueWorkItem2(0xB, 2, lambda_26B9)
    Sleep(500)

    def lambda_26CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_26CE)

    def lambda_26DF():
        OP_95(0xFE, -3000, 0, -16000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_26DF)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0050
    ChrTalk(
        0x109,
        "#10100Fあ……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#00000Fワジ……！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xA,
        "#01110Fあ、ワジだー！\x02",
    )

    CloseMessageWindow()

    def lambda_2744():
        OP_95(0xFE, 1700, 0, -15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2744)
    Sleep(800)
    Fade(500)
    OP_68(2600, 900, -15600, 0)
    MoveCamera(325, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    Sleep(500)

    def lambda_2797():
        OP_96(0xFE, 0x802, 0x0, 0xFFFFC856, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2797)
    WaitChrThread(0x105, 1)

    def lambda_27B5():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_27B5)
    WaitChrThread(0x102, 1)
    OP_C9(0x0, 0x80000000)

    #C0053
    ChrTalk(
        0x105,
        (
            "#10304F#2905V#5P#30Wフフ、お勤めご苦労さま。\x02\x03",

            "#10300F#2906Vその調子だと\x01",
            "上手く行ったみたいだね？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xB5A)

    #C0054
    ChrTalk(
        0x101,
        (
            "#12P#00000Fああ、ワジの情報があったから\x01",
            "アルタイル市の情報屋にも\x01",
            "何とか接触できたけど……\x02\x03",

            "#00006F……いったいどこで\x01",
            "あんな情報を仕入れてきたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x105,
        "#10309F#5Pフフ……蛇の道は蛇ってね。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(3150, 900, -15230, 1500)

    def lambda_2912():
        OP_95(0xFE, 3150, 0, -15400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2912)
    WaitChrThread(0x105, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0xC, 0x2)

    def lambda_2938():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2938)
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
            "#2901V#30W──他ならぬ君のためだ。\x01",
            "役に立ったのなら嬉しいよ。\x02",
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
        "#6P#01905Fわわっ……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0059
    ChrTalk(
        0x101,
        (
            "#12P#00011Fちょ、近いって！\x02\x03",

            "なんでにじり寄るんだよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x105,
        (
            "#5P#10309Fあはは、愚問だなぁ。\x02\x03",

            "君の反応が面白いからに\x01",
            "決まってるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#12P#00013Fあ、あのな……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        "#5P#00111Fワジ君、あなたねぇ……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x109,
        (
            "#12P#10112Fあはは……\x01",
            "（やっぱり謎な子だなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        (
            "#01109F#11Pえへへ。\x01",
            "なんか楽しそーだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xB,
        (
            "#6P#01906Fいいなぁ、特務支援課……\x02\x03",

            "お姉ちゃんもキーアちゃんもいるし、\x01",
            "困ってるロイドさんも見られるし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    #C0066
    ChrTalk(
        0x101,
        (
            "#00012F#11Pいや！\x01",
            "羨ましがられても困るから！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xC,
        (
            "#01006F#5Pやれやれ……\x01",
            "ジャレるのはそのくらいにしとけ。\x02",
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

    def lambda_2D26():
        TurnDirection(0x101, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D26)
    Sleep(0)

    def lambda_2D36():
        TurnDirection(0x109, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D36)
    Sleep(0)

    def lambda_2D46():
        TurnDirection(0x102, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D46)
    Sleep(0)

    def lambda_2D56():
        TurnDirection(0xB, 0xC, 0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2D56)
    Sleep(0)

    def lambda_2D66():
        TurnDirection(0xA, 0xC, 0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2D66)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)

    def lambda_2D8A():
        OP_96(0xFE, 0x9C4, 0x0, 0xFFFFC504, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2D8A)
    WaitChrThread(0x105, 1)
    TurnDirection(0x105, 0xC, 500)
    OP_0D()

    #C0068
    ChrTalk(
        0xC,
        (
            "#6P#01003F──ともかく。\x01",
            "これが新生・特務支援課の\x01",
            "スターティングメンバーだ。\x02\x03",

            "#01000Fリーダーとして、\x01",
            "ロイド・バニングス。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0069
    ChrTalk(
        0x101,
        "#00000F#3317V#30W……はい！\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xC,
        (
            "#6P#01000Fリーダー補佐、\x01",
            "エリィ・マクダエル。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0071
    ChrTalk(
        0x102,
        "#00102F#3390V#5P#30Wはい。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xC,
        (
            "#6P#01003F警備隊からの出向、\x01",
            "ノエル・シーカー。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0073
    ChrTalk(
        0x109,
        "#10102F#3514V#11P#30Wはいっ！\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        (
            "#6P#01000F臨時の準メンバーとして\x01",
            "ワジ・ヘミスフィア。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0075
    ChrTalk(
        0x105,
        "#10304F#2907V#5P#30Wｊａ#4Rヤ ー#。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xC,
        (
            "#6P#01004F本日、１８：３０をもって\x01",
            "特務支援課の再始動を宣言する。\x02\x03",

            "#01002F前以上に楽しいお仕事が\x01",
            "舞い込んでくるはずだから\x01",
            "楽しみにしておくといい──\x02",
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

    def Function_3_3143(): pass

    label("Function_3_3143")

    Sound(452, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x168, 0x0, 0x0)
    Sleep(2000)

    def lambda_3161():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3161)
    OP_79(0x1)
    Sound(143, 0, 100, 0)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Return()

    # Function_3_3143 end

    def Function_4_3187(): pass

    label("Function_4_3187")

    SetChrPos(0xFE, 22700, 0, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_31A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31A8)
    OP_95(0xFE, 22700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 7300, 0, -12800, 2000, 0x0)
    Return()

    # Function_4_3187 end

    def Function_5_31DD(): pass

    label("Function_5_31DD")

    SetChrPos(0xFE, 22700, 0, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_31FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31FE)
    OP_95(0xFE, 22700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 8500, 0, -12800, 2000, 0x0)
    Return()

    # Function_5_31DD end

    def Function_6_3233(): pass

    label("Function_6_3233")

    SetChrPos(0xFE, 19700, 100, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3254():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3254)
    OP_95(0xFE, 19700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 0, 0, -12800, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_6_3233 end

    def Function_7_328E(): pass

    label("Function_7_328E")

    ClearScenarioFlags(0x0, 0)

    def lambda_3296():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3296)
    OP_95(0xFE, 22700, 0, -13700, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 0, 0, -13700, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_7_328E end

    def Function_8_32E1(): pass

    label("Function_8_32E1")


    def lambda_32E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32E6)
    OP_95(0xFE, 22700, 0, -12700, 2000, 0x0)
    Sleep(500)
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 0, 0, -12700, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_8_32E1 end

    def Function_9_332D(): pass

    label("Function_9_332D")


    def lambda_3332():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3332)
    OP_95(0xFE, 32500, 0, -12700, 4000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, 0, 0, -12700, 4000, 0x0)
    OP_64(0xFE)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_9_332D end

    def Function_10_3381(): pass

    label("Function_10_3381")

    OP_95(0xFE, 7500, 0, -13700, 2000, 0x0)
    OP_95(0xFE, 4800, 0, -16700, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_3381 end

    def Function_11_33B1(): pass

    label("Function_11_33B1")

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

    # Function_11_33B1 end

    def Function_12_3B1C(): pass

    label("Function_12_3B1C")

    Sound(963, 0, 100, 0)
    Sound(825, 2, 50, 0)
    OP_71(0x3, 0x5A, 0x168, 0x0, 0x8)
    Sleep(2000)

    def lambda_3B3C():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3B3C)
    OP_79(0x3)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sound(143, 0, 100, 0)
    StopSound(825, 500, 50)
    Sleep(500)
    Return()

    # Function_12_3B1C end

    def Function_13_3B68(): pass

    label("Function_13_3B68")


    def lambda_3B6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3B6D)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 40000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_13_3B68 end

    def Function_14_3BA4(): pass

    label("Function_14_3BA4")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_14_3BA4 end

    def Function_15_3BBB(): pass

    label("Function_15_3BBB")


    def lambda_3BC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3BC0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 39000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_15_3BBB end

    def Function_16_3BF7(): pass

    label("Function_16_3BF7")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_16_3BF7 end

    def Function_17_3C0E(): pass

    label("Function_17_3C0E")


    def lambda_3C13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3C13)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 38000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_17_3C0E end

    def Function_18_3C4A(): pass

    label("Function_18_3C4A")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_18_3C4A end

    def Function_19_3C61(): pass

    label("Function_19_3C61")


    def lambda_3C66():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3C66)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_68(35000, 700, 3300, 2000)
    OP_95(0xFE, 35000, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_19_3C61 end

    def Function_20_3CAE(): pass

    label("Function_20_3CAE")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_20_3CAE end

    def Function_21_3CBE(): pass

    label("Function_21_3CBE")


    def lambda_3CC3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3CC3)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 35750, 0, 2500, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_3CBE end

    def Function_22_3CFA(): pass

    label("Function_22_3CFA")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_22_3CFA end

    def Function_23_3D0A(): pass

    label("Function_23_3D0A")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_23_3D0A end

    def Function_24_3D21(): pass

    label("Function_24_3D21")


    def lambda_3D26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3D26)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 27000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_24_3D21 end

    def Function_25_3D5D(): pass

    label("Function_25_3D5D")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_25_3D5D end

    def Function_26_3D74(): pass

    label("Function_26_3D74")


    def lambda_3D79():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3D79)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 26000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_26_3D74 end

    def Function_27_3DB0(): pass

    label("Function_27_3DB0")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_27_3DB0 end

    def Function_28_3DC7(): pass

    label("Function_28_3DC7")


    def lambda_3DCC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3DCC)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 25000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_3DC7 end

    def Function_29_3E03(): pass

    label("Function_29_3E03")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_29_3E03 end

    def Function_30_3E1A(): pass

    label("Function_30_3E1A")


    def lambda_3E1F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3E1F)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_68(22000, 700, 3300, 2000)
    OP_95(0xFE, 22000, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_30_3E1A end

    def Function_31_3E67(): pass

    label("Function_31_3E67")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_31_3E67 end

    def Function_32_3E77(): pass

    label("Function_32_3E77")


    def lambda_3E7C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3E7C)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 22750, 0, 2500, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_32_3E77 end

    def Function_33_3EB3(): pass

    label("Function_33_3EB3")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_33_3EB3 end

    def Function_34_3EC3(): pass

    label("Function_34_3EC3")

    OP_95(0xFE, 20500, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_34_3EC3 end

    def Function_35_3EDF(): pass

    label("Function_35_3EDF")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_35_3EDF end

    def Function_36_3EF6(): pass

    label("Function_36_3EF6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F3C")
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x11)
    Sleep(500)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xD)
    Sleep(500)
    Jump("Function_36_3EF6")

    label("loc_3F3C")

    Return()

    # Function_36_3EF6 end

    def Function_37_3F3D(): pass

    label("Function_37_3F3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F83")
    OP_63(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x12)
    Sleep(500)
    OP_63(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xF)
    Sleep(500)
    Jump("Function_37_3F3D")

    label("loc_3F83")

    Return()

    # Function_37_3F3D end

    def Function_38_3F84(): pass

    label("Function_38_3F84")

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

    def lambda_405D():
        OP_95(0x20, 1000, 600, 40, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_405D)
    Sleep(800)

    def lambda_407A():
        OP_95(0x101, 200, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_407A)
    Sleep(200)

    def lambda_4097():
        OP_95(0x102, 300, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4097)
    Sleep(300)

    def lambda_40B4():
        OP_95(0x103, -1000, 0, -950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_40B4)
    Sleep(100)

    def lambda_40D1():
        OP_95(0x104, -1100, 0, 1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_40D1)
    Sleep(200)

    def lambda_40EE():
        OP_95(0x109, -2500, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_40EE)
    Sleep(50)

    def lambda_410B():
        OP_95(0x105, -2400, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_410B)
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

    def lambda_4200():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4200)
    Sleep(50)

    def lambda_4210():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4210)
    Sleep(50)

    def lambda_4220():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4220)
    Sleep(10)

    def lambda_4230():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4230)
    Sleep(30)

    def lambda_4240():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4240)
    Sleep(10)

    def lambda_4250():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4250)
    Sleep(10)

    def lambda_4260():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_4260)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x20, 2)

    #C0077
    ChrTalk(
        0x101,
        "#00005Fこれは……\x02",
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
            "#00100F帝国政府の専用列車、\x01",
            "《アイゼングラーフ号》ね。\x02\x03",

            "#00103Fこの豪奢な外観……\x01",
            "まるで帝国を象徴しているみたい。\x02",
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
            "#10103F確かに……\x01",
            "まさに威風堂々という感じですね。\x02",
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
            "#00300Fあの《鉄血宰相》はコイツで\x01",
            "クロスベル入りしたんだよな。\x02\x03",

            "#00306F確かにインパクト十分だが、\x01",
            "どんだけ目立ちゃあ\x01",
            "気が済むんだよっつう話だぜ。\x02",
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
            "#10300Fああ、それにミラのかかり方も\x01",
            "半端じゃなさそうだ。\x02",
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
            "#00203F……凄いのは\x01",
            "見た目だけではないようです。\x02\x03",

            "#00200F何でもこの列車、\x01",
            "今ある導力列車の中でも\x01",
            "最高速度を誇るんだそうです。\x02\x03",

            "はっきりした情報が\x01",
            "公開されているわけではないので\x01",
            "確かなことは言えませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        "#00005Fそ、そうなのか……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x102,
        (
            "#00103Fさすがは本国全土に\x01",
            "鉄道網を敷くエレボニア帝国……\x02\x03",

            "#00101Fこと鉄道の分野に関しては\x01",
            "他の追随を許さないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#00003Fああ、改めて思い知らされるな。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x20,
        "――ゴホン。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x20,
        (
            "では仕事の話をしたいんだが\x01",
            "準備はよかったかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4706():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4706)
    Sleep(50)

    def lambda_4716():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4716)
    Sleep(30)

    def lambda_4726():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4726)
    Sleep(20)

    def lambda_4736():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4736)
    Sleep(40)

    def lambda_4746():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4746)
    Sleep(20)

    def lambda_4756():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4756)
    WaitChrThread(0x105, 2)

    #C0088
    ChrTalk(
        0x101,
        (
            "#00005Fす、すみません。\x01",
            "あまりの威容に驚いてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        "#00100Fええ、もちろん大丈夫です。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x20,
        "うむ、結構。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x20,
        (
            "さて、さっきも言った通り\x01",
            "君たちに頼みたいのは\x01",
            "列車の臨検業務の手伝いだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x20,
        (
            "具体的には、乗客全員の\x01",
            "入国申請書と手荷物のチェック。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x20,
        (
            "それから、列車そのものの\x01",
            "安全チェックを分担して行う。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#00005Fえっと、列車の\x01",
            "安全チェックというのは？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x20,
        (
            "ああ、これは私の手伝いだ。\x01",
            "とにかく指示に従って\x01",
            "各種点検作業を行ってもらいたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x20,
        (
            "ふむ、君たちは\x01",
            "全員で６名いるんだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x20,
        (
            "となると、２人１組で全３組――\x01",
            "客室車両の臨検を２組で分担し、\x01",
            "私の手伝いに１組欲しい所だな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B06")

    #C0098
    ChrTalk(
        0x101,
        (
            "#00005F２人１組で臨検、ですか。\x01",
            "確か以前は１人で回ったような……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#00100Fええ、少なくとも前に\x01",
            "手伝った時はそうだったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x20,
        "ああ、君たちは経験者だったな。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x20,
        (
            "確かにいつもは\x01",
            "１人で行なう業務なんだが、\x01",
            "今は警戒レベルが上がっているからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x20,
        (
            "より厳密なチェックのため、\x01",
            "今回はこの態勢でお願いする次第だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BDD")

    label("loc_4B06")


    #C0103
    ChrTalk(
        0x101,
        (
            "#00005F２人１組で臨検……\x01",
            "いつもそのような態勢なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x20,
        (
            "いや、いつもは\x01",
            "１人で行なう業務なんだが、\x01",
            "今は警戒レベルが上がっているからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x20,
        (
            "より厳密なチェックのため、\x01",
            "今回はこの態勢でお願いする次第だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BDD")


    #C0106
    ChrTalk(
        0x101,
        "#00000Fなるほど、事情は判りました。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x20,
        (
            "それでは、さっそく\x01",
            "３つの組に分かれてくれるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x20,
        "何ならジャンケンで決めてもいいが。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0109
    ChrTalk(
        0x101,
        "#00005Fジャ、ジャンケンですか？\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x20,
        (
            "まあ正直な話、それほど個々の\x01",
            "適性を問う作業でもないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x20,
        (
            "こちらとしては\x01",
            "早く仕事に取りかかりたいし、\x01",
            "君たちも手っ取り早くていいだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00000Fええまあ、そういうことなら\x01",
            "それでも構いませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、なら決まりだね。\x01",
            "楽しそうでいいじゃない♪\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        (
            "#00205Fでも、具体的には\x01",
            "どうやって決めるんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x20,
        (
            "ああ、では\x01",
            "こういうルールはどうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x20,
        (
            "ジャンケンの要領で一斉に手を出し、\x01",
            "２人だけが同じ手だったら\x01",
            "その者たちが“組み”となり抜ける。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x20,
        "後は決まるまで、それの繰り返しだ。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x109,
        (
            "#10106Fえっと……\x01",
            "なんていうか、慣れていませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x20,
        "はは、まあね。\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x20,
        (
            "実は我々共和国臨検官の間では\x01",
            "息抜きを兼ねて、たまにこうして\x01",
            "分担などを決めるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x20,
        (
            "堅物揃いの帝国臨検官にはない\x01",
            "柔軟な発想ってヤツだな。\x02",
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
            "#00106Fそれが柔軟な発想なのかどうかは\x01",
            "分かりませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#00200Fとりあえず、\x01",
            "これもお国柄の違いでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#00300Fはは、かもな。\x02\x03",

            "ま、とにかく\x01",
            "さっさと試してみようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#00000Fああ、そうするか。\x02",
    )

    CloseMessageWindow()

    def lambda_50F5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50F5)
    Sleep(10)

    def lambda_5105():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5105)
    Sleep(10)

    def lambda_5115():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5115)
    Sleep(10)

    def lambda_5125():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5125)
    Sleep(30)

    def lambda_5135():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5135)
    Sleep(10)

    def lambda_5145():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5145)
    WaitChrThread(0x105, 2)
    Sleep(500)

    #C0126
    ChrTalk(
        0x101,
        (
            "#00003Fじゃあ、みんな。\x01",
            "“いっせいの～せ”で行くぞ。\x02",
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
            "グーを出す\x01",        # 0
            "チョキを出す\x01",      # 1
            "パーを出す\x01",        # 2
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
    SetChrName("一同")

    #A0127
    AnonymousTalk(
        0xFF,
        "#4S#11Aいっせいの～……\x02",
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

    def lambda_525D():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_525D)

    def lambda_5272():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5272)

    def lambda_5287():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5287)

    def lambda_529C():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_529C)

    def lambda_52B1():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_52B1)

    def lambda_52C6():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_52C6)
    Sound(802, 0, 100, 0)
    SetChrName("一同")

    #A0128
    AnonymousTalk(
        0xFF,
        "#4S#11Aせ！\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B6")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_533F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_533F)

    def lambda_5354():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5354)

    def lambda_5369():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5369)

    def lambda_537E():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_537E)

    def lambda_5393():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5393)

    def lambda_53A8():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_53A8)
    WaitChrThread(0x101, 1)

    def lambda_53C1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_53C1)
    Sleep(50)

    def lambda_53D1():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_53D1)
    Sleep(300)

    #C0129
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、私とティオちゃんだけが\x01",
            "チョキね。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x103,
        (
            "#00200Fということは、\x01",
            "わたしはエリィさんと組ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        "#00300Fで、残りはグー３人に、パー１人か。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x109,
        (
            "#10100Fとなると、\x01",
            "残った４人でやり直しですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#00000Fああ、それじゃ続けて行こう。\x02",
    )

    CloseMessageWindow()

    def lambda_54DB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54DB)
    Sleep(50)

    def lambda_54EB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_54EB)
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
            "グーを出す\x01",        # 0
            "チョキを出す\x01",      # 1
            "パーを出す\x01",        # 2
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
    SetChrName("一同")

    #A0134
    AnonymousTalk(
        0xFF,
        "#4S#11Aいっせいの～\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)

    def lambda_55AD():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55AD)

    def lambda_55C2():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_55C2)

    def lambda_55D7():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_55D7)

    def lambda_55EC():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_55EC)
    Sound(802, 0, 100, 0)
    SetChrName("一同")

    #A0135
    AnonymousTalk(
        0xFF,
        "#4S#11Aせ！\x02",
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

    def lambda_567A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_567A)

    def lambda_568F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_568F)

    def lambda_56A4():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_56A4)

    def lambda_56B9():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_56B9)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57CC")

    def lambda_56E1():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56E1)
    Sleep(50)

    def lambda_56F1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_56F1)
    Sleep(300)

    #C0136
    ChrTalk(
        0x101,
        "#00005F俺とノエルがグーか。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x109,
        (
            "#10100Fふふ、ロイドさん。\x01",
            "よろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_575A():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_575A)
    Sleep(50)

    def lambda_576A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_576A)
    Sleep(300)

    #C0138
    ChrTalk(
        0x104,
        (
            "#00300Fとなると、\x01",
            "残った俺とワジが組だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x105,
        "#10300Fフフ、よろしくね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 4)
    Jump("loc_59B1")

    label("loc_57CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58C0")

    def lambda_57E0():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57E0)
    Sleep(50)

    def lambda_57F0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_57F0)
    Sleep(300)

    #C0140
    ChrTalk(
        0x101,
        "#00005F俺とワジがチョキか。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x105,
        "#10300Fフフ、よろしくね。\x02",
    )

    CloseMessageWindow()

    def lambda_5840():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5840)
    Sleep(50)

    def lambda_5850():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5850)
    Sleep(300)

    #C0142
    ChrTalk(
        0x104,
        (
            "#00300Fとなると、\x01",
            "残った俺とノエルが組だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x109,
        "#10100Fですね、よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)
    Jump("loc_59B1")

    label("loc_58C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B1")

    def lambda_58D4():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58D4)
    Sleep(50)

    def lambda_58E4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_58E4)
    Sleep(300)

    #C0144
    ChrTalk(
        0x101,
        "#00005F俺とランディがパーか。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        "#00300Fああ、よろしく頼むぜ。\x02",
    )

    CloseMessageWindow()

    def lambda_593A():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_593A)
    Sleep(50)

    def lambda_594A():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_594A)
    Sleep(300)

    #C0146
    ChrTalk(
        0x109,
        (
            "#10100Fということは、\x01",
            "残ったあたしとワジ君が組ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x105,
        "#10300Fだね、ヨロシク。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 3)

    label("loc_59B1")

    Jump("loc_61F1")

    label("loc_59B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6060")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_59F1():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59F1)

    def lambda_5A06():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A06)

    def lambda_5A1B():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A1B)

    def lambda_5A30():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A30)

    def lambda_5A45():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A45)

    def lambda_5A5A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A5A)
    WaitChrThread(0x101, 1)

    def lambda_5A73():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A73)
    Sleep(50)

    def lambda_5A83():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A83)
    Sleep(300)

    #C0148
    ChrTalk(
        0x104,
        "#00305Fふむ、俺とノエルだけがグーか。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x109,
        (
            "#10100Fということは、\x01",
            "あたしはランディ先輩と組ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x105,
        "#10300Fで、残りはチョキ３人に、パー１人と。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        (
            "#00100Fということは、\x01",
            "残った４人でやり直しね。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#00000Fああ、それじゃ続けて行こう。\x02",
    )

    CloseMessageWindow()

    def lambda_5B88():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B88)
    Sleep(50)

    def lambda_5B98():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B98)
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
            "グーを出す\x01",        # 0
            "チョキを出す\x01",      # 1
            "パーを出す\x01",        # 2
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
    SetChrName("一同")

    #A0153
    AnonymousTalk(
        0xFF,
        "#4S#11Aいっせいの～\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x105, 0x3)

    def lambda_5C5A():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C5A)

    def lambda_5C6F():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C6F)

    def lambda_5C84():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C84)

    def lambda_5C99():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5C99)
    Sound(802, 0, 100, 0)
    SetChrName("一同")

    #A0154
    AnonymousTalk(
        0xFF,
        "#4S#11Aせ！\x02",
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

    def lambda_5D27():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D27)

    def lambda_5D3C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D3C)

    def lambda_5D51():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D51)

    def lambda_5D66():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D66)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E73")

    def lambda_5D8E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D8E)
    Sleep(50)

    def lambda_5D9E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D9E)
    Sleep(300)

    #C0155
    ChrTalk(
        0x101,
        "#00005F俺とティオがグーか。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        (
            "#00200Fロイドさん。\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5DFF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DFF)
    Sleep(50)

    def lambda_5E0F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E0F)
    Sleep(300)

    #C0157
    ChrTalk(
        0x102,
        (
            "#00100Fということは、\x01",
            "残った私とワジ君が組ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x105,
        "#10300Fだね、ヨロシク。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 2)
    Jump("loc_605B")

    label("loc_5E73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F6E")

    def lambda_5E87():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E87)
    Sleep(50)

    def lambda_5E97():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E97)
    Sleep(300)

    #C0159
    ChrTalk(
        0x101,
        "#00005F俺とワジがチョキか。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x105,
        "#10300Fフフ、よろしくね。\x02",
    )

    CloseMessageWindow()

    def lambda_5EE7():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5EE7)
    Sleep(50)

    def lambda_5EF7():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5EF7)
    Sleep(300)

    #C0161
    ChrTalk(
        0x102,
        (
            "#00100Fということは、\x01",
            "私とティオちゃんが組ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x103,
        (
            "#00200Fエリィさん。\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)
    Jump("loc_605B")

    label("loc_5F6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_605B")

    def lambda_5F82():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F82)
    Sleep(50)

    def lambda_5F92():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F92)
    Sleep(300)

    #C0163
    ChrTalk(
        0x101,
        "#00005F俺とエリィがパーか。\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x102,
        "#00100Fふふ、よろしくね。\x02",
    )

    CloseMessageWindow()

    def lambda_5FE2():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5FE2)
    Sleep(50)

    def lambda_5FF2():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FF2)
    Sleep(300)

    #C0165
    ChrTalk(
        0x103,
        (
            "#00200Fということは、残ったわたしと\x01",
            "ワジさんが組ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x105,
        "#10300Fだね、ヨロシク。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 1)

    label("loc_605B")

    Jump("loc_61F1")

    label("loc_6060")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61F1")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_60E9():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60E9)

    def lambda_60FE():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_60FE)

    def lambda_6113():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6113)

    def lambda_6128():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6128)

    def lambda_613D():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_613D)

    def lambda_6152():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6152)
    WaitChrThread(0x101, 1)

    #C0167
    ChrTalk(
        0x101,
        (
            "#00005Fお、また見事に分かれたな。\x02\x03",

            "#00000Fワジと俺、エリィとティオ、\x01",
            "それにランディとノエルが組か。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x105,
        "#10300Fフフ、よろしくね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)

    label("loc_61F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_6208")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_625F")

    label("loc_6208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_621F")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_625F")

    label("loc_621F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_6236")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_625F")

    label("loc_6236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_624D")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_625F")

    label("loc_624D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_625F")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_625F")


    #C0169
    ChrTalk(
        0x20,
        "ふむ、どうやら決まったみたいだな。\x02",
    )

    CloseMessageWindow()

    def lambda_628C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_628C)
    Sleep(10)

    def lambda_629C():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_629C)
    Sleep(10)

    def lambda_62AC():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_62AC)
    Sleep(10)

    def lambda_62BC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_62BC)
    Sleep(30)

    def lambda_62CC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_62CC)
    Sleep(10)

    def lambda_62DC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_62DC)
    WaitChrThread(0x105, 2)
    Sleep(500)

    #C0170
    ChrTalk(
        0x101,
        "#00000F分担の方はどうしましょう？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_6413")

    #C0171
    ChrTalk(
        0x20,
        "そうだな……\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x20,
        (
            "何かと動いてもらうつもりだから\x01",
            "ここは男手が欲しいところだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        "#00300Fつうことは、俺とワジをご指名か。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x105,
        (
            "#10306Fやれやれ、いかにも\x01",
            "こき使われそうな物言いだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x20,
        (
            "はは、せっかくだから\x01",
            "目一杯活用させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64E4")

    label("loc_6413")


    #C0176
    ChrTalk(
        0x109,
        (
            "#10105Fあ、なんでしたら\x01",
            "あたしがお手伝いしましょうか？\x02\x03",

            "#10100F車両の点検なら\x01",
            "警備隊で経験があるので\x01",
            "お役に立てると思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0177
    ChrTalk(
        0x20,
        (
            "なるほど、そうなのか。\x01",
            "ふむ、ならお願いできるかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64E4")


    #C0178
    ChrTalk(
        0x20,
        (
            "よし、では\x01",
            "さっそく業務を開始しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x20,
        (
            "客室車両のチェックは\x01",
            "君たちに任せたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x20,
        (
            "既にアナウンスもしてあるし、\x01",
            "『臨検官補佐』を名乗れば\x01",
            "滞りなく業務を行えるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        "#00000Fええ、了解です。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_65F7")
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_6643")

    label("loc_65F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_6609")
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_6643")

    label("loc_6609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_661B")
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_6643")

    label("loc_661B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_662D")
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_6643")

    label("loc_662D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_663F")
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_6643")

    label("loc_663F")

    AddParty(0x1, 0xFF, 0xFF)

    label("loc_6643")

    SetScenarioFlags(0x22, 3)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_3F84 end

    def Function_39_6650(): pass

    label("Function_39_6650")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6680")

    def lambda_6660():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6660)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_39_6650")

    label("loc_6680")

    Return()

    # Function_39_6650 end

    def Function_40_6681(): pass

    label("Function_40_6681")

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
        "ふむ、みんなお疲れ様だったね。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x20,
        (
            "特にチケットの\x01",
            "盗難騒動の方は大変だったろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#00000Fいえ、そんなに大したことも\x01",
            "出来なかったので。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        (
            "#00100Fちなみに、窃盗犯は\x01",
            "特定できそうなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x20,
        "ああ、それは可能だ。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x20,
        (
            "こういう時のためにも\x01",
            "チケットの購入者情報を\x01",
            "控えているからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x20,
        (
            "調査によって盗難が発覚すれば、\x01",
            "先の駅で捕まえることになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        "#00200Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        (
            "#00300Fしかし、被害者のじいさんは\x01",
            "どうなったんスかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x20,
        (
            "ああ、老人は急ぐというので\x01",
            "チケットの方を一旦\x01",
            "買い直してもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x20,
        (
            "無事、窃盗犯が捕まったら\x01",
            "犯人に弁償させる形になるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x105,
        "#10300Fフフ、ご老人も災難だね。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x109,
        (
            "#10100Fまあでも、すぐに\x01",
            "解決できそうで何よりだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x20,
        (
            "ああ、とにかく君たちは\x01",
            "やることを尽くしてくれた。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x20,
        "おかげで助かったよ、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#00000Fいえ、こちらこそ\x01",
            "そう言ってもらえて\x01",
            "良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x102,
        (
            "#00100Fまた何かありましたら、\x01",
            "気軽にご連絡くださいね。\x02",
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
            "クエスト【共和国臨検官の作業補助】\x07\x00",
            "を達成した！\x02",
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

    # Function_40_6681 end

    def Function_41_6B81(): pass

    label("Function_41_6B81")

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
        "話は全て聞かせてもらったよ。\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x20,
        (
            "盗難騒動の方は\x01",
            "本当にお疲れ様だったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        (
            "#00003Fいえ、そんなに\x01",
            "大したことはしていないので。\x02\x03",

            "#00000Fそれで結局、窃盗を犯した\x01",
            "青年はどうなるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x20,
        (
            "ああ、それが\x01",
            "罪は一切不問になったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x102,
        "#00100Fえっと、それはどういう……？\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x20,
        (
            "ああ、それが当の\x01",
            "被害者であるはずの老人が\x01",
            "窃盗などなかったと言い出してね。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x20,
        (
            "青年はあくまで入場券で\x01",
            "ホームに入った後、後から\x01",
            "チケットを買い忘れただけ――\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x20,
        (
            "そういう話になって、\x01",
            "それ以上はこちらも追求の\x01",
            "しようがなくなったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x104,
        "#00306Fハ、そいつはまた……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#00003Fう～ん、これも\x01",
            "シンが言い含めたのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x105,
        "#10300Fフフ、そうなんじゃない？\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x109,
        (
            "#10105Fちなみに、商人さんの方は\x01",
            "どうなったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x20,
        (
            "ああ、実はこっちの方が\x01",
            "大捕り物でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x20,
        (
            "ヤツの正体は偽造チケットの\x01",
            "ブローカーだったんだ。\x02",
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
        "#00005Fそ、そうなんですか？\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        "#00100Fですが、どういう理由で列車に？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x20,
        (
            "ああ、どうやら\x01",
            "自らの商品を実際に使って\x01",
            "試していたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x20,
        "まったく大胆なヤツだよ。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x103,
        "#00203Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x20,
        (
            "いや、しかし君たちの活躍は\x01",
            "素晴らしかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x20,
        "おかげで助かったよ、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#00000Fいえ、こちらこそ\x01",
            "そう言ってもらえて\x01",
            "良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        (
            "#00100Fまた何かありましたら、\x01",
            "気軽にご連絡くださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x20,
        "ああ、ではまたね。\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0x2D, 0x1F4)
    OP_95(0x20, 5760, 0, 2550, 2000, 0x0)

    def lambda_71D9():
        OP_95(0x20, 24940, 0, 2810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_71D9)
    Sleep(500)
    OP_68(-1190, 1500, -230, 2000)
    MoveCamera(45, 34, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(15430, 2000)
    Sleep(1500)

    def lambda_7227():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7227)
    Sleep(10)

    def lambda_7237():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7237)
    Sleep(10)

    def lambda_7247():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7247)
    Sleep(10)

    def lambda_7257():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7257)
    Sleep(30)

    def lambda_7267():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7267)
    Sleep(10)

    def lambda_7277():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7277)
    WaitChrThread(0x105, 2)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_7455")

    #C0224
    ChrTalk(
        0x109,
        (
            "#10100Fそれにしても、シン君は\x01",
            "大活躍だったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#00109Fふふ、まさかこんな所で\x01",
            "会うとは思わなかったけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#00003Fああ、それに改めて\x01",
            "大器の片鱗を思い知らされたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x104,
        (
            "#00306Fったく、つくづく\x01",
            "末恐ろしいガキだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x103,
        "#00200Fふむ、一目見たかったです。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、見た目は\x01",
            "可愛らしい坊やなんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        (
            "#00002Fはは、確かにな。\x02\x03",

            "#00003Fともあれ、これで一件落着だ。\x02\x03",

            "#00000F一息入れたら、\x01",
            "次の仕事に向かうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B63")

    label("loc_7455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_760E")

    #C0231
    ChrTalk(
        0x102,
        (
            "#00100Fそれにしても、シン君は\x01",
            "大活躍だったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x103,
        (
            "#00200Fええ、まだまだ幼いのに\x01",
            "色々と驚かされました。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#00000Fああ、改めて大器の片鱗を\x01",
            "思い知らされた感じだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        (
            "#00306Fったく、つくづく\x01",
            "末恐ろしいガキだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x109,
        "#10100Fええ、本当に。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、見た目は\x01",
            "可愛らしい坊やなんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        (
            "#00002Fはは、確かにな。\x02\x03",

            "#00003Fともあれ、これで一件落着だ。\x02\x03",

            "#00000F一息入れたら、\x01",
            "次の仕事に向かうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B63")

    label("loc_760E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_77C6")

    #C0238
    ChrTalk(
        0x102,
        (
            "#00100Fそれにしても、シン君は\x01",
            "大活躍だったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x104,
        "#00300Fああ、相変わらずって感じでな。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#00000Fだな、改めて大器の片鱗を\x01",
            "思い知らされた感じだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x109,
        (
            "#10106Fなんていうか、\x01",
            "本当に末恐ろしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        "#00200Fふむ、一目見たかったです。\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、見た目は\x01",
            "可愛らしい坊やなんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#00002Fはは、確かにな。\x02\x03",

            "#00003Fともあれ、これで一件落着だ。\x02\x03",

            "#00000F一息入れたら、\x01",
            "次の仕事に向かうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B63")

    label("loc_77C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_7993")

    #C0245
    ChrTalk(
        0x102,
        (
            "#00100Fそれにしても、シン君は\x01",
            "大活躍だったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x109,
        (
            "#10100Fええ、まさかこんな所で\x01",
            "会うとは思いませんでしたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#00000Fああ、それに改めて\x01",
            "大器の片鱗を思い知らされたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x104,
        (
            "#00306Fったく、つくづく\x01",
            "末恐ろしいガキだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x103,
        "#00200Fふむ、一目見たかったです。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、見た目は\x01",
            "可愛らしい坊やなんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#00002Fはは、確かにな。\x02\x03",

            "#00003Fともあれ、これで一件落着だ。\x02\x03",

            "#00000F一息入れたら、\x01",
            "次の仕事に向かうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B63")

    label("loc_7993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_7B63")

    #C0252
    ChrTalk(
        0x102,
        (
            "#00100Fそれにしても、シン君は\x01",
            "大活躍だったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、まさかこんな所で\x01",
            "再会すると思わなかったけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00000Fああ、それに改めて\x01",
            "大器の片鱗を思い知らされたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#00306Fったく、つくづく\x01",
            "末恐ろしいガキだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x103,
        "#00200Fふむ、一目見たかったです。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x109,
        (
            "#10100Fふふ、見た目は可愛らしい\x01",
            "お坊ちゃんなんですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        (
            "#00002Fはは、確かにな。\x02\x03",

            "#00003Fともあれ、これで一件落着だ。\x02\x03",

            "#00000F一息入れたら、\x01",
            "次の仕事に向かうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B63")

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
            "クエスト【共和国臨検官の作業補助】\x07\x00",
            "を達成した！\x02",
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

    # Function_41_6B81 end

    def Function_42_7BEE(): pass

    label("Function_42_7BEE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C87")
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
    Jump("loc_7D01")

    label("loc_7C87")

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

    label("loc_7D01")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DB6")
    OP_68(-1150, 1000, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(16500, 4000)
    Jump("loc_7DED")

    label("loc_7DB6")

    OP_68(-1150, 1000, -16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(16500, 4000)

    label("loc_7DED")


    def lambda_7DF2():
        OP_97(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7DF2)
    Sleep(50)

    def lambda_7E0F():
        OP_97(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7E0F)
    Sleep(50)

    def lambda_7E2C():
        OP_97(0x103, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7E2C)
    Sleep(50)

    def lambda_7E49():
        OP_97(0x104, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7E49)
    Sleep(50)

    def lambda_7E66():
        OP_97(0xF4, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_7E66)
    Sleep(50)

    def lambda_7E83():
        OP_97(0xF5, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_7E83)
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
            "#00306F#5Pしかし、人がいないホームってのは\x01",
            "何とも物悲しいもんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        (
            "#6P#00206F……横断鉄道の列車も\x01",
            "ずっと停車したままみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x102,
        "#5P#00108Fそうね……\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Sleep(150)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FB6")

    #C0263
    ChrTalk(
        0x102,
        (
            "#5P#00101F……３番ホームの列車というと\x01",
            "あちらかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FF1")

    label("loc_7FB6")


    #C0264
    ChrTalk(
        0x102,
        (
            "#5P#00101F……３番ホームの列車というと\x01",
            "そちらかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FF1")

    OP_68(-1150, 1000, -24100, 3000)
    MoveCamera(63, 27, 0, 3000)
    SetCameraDistance(25500, 3000)

    def lambda_801B():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_801B)
    Sleep(50)

    def lambda_802B():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_802B)
    Sleep(50)

    def lambda_803B():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_803B)
    Sleep(50)

    def lambda_804B():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_804B)
    Sleep(50)

    def lambda_805B():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_805B)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_811B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80DC")

    #C0265
    ChrTalk(
        0x10A,
        (
            "#00601Fフン、あの列車の\x01",
            "前から２番目の車輌だったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8116")

    label("loc_80DC")


    #C0266
    ChrTalk(
        0x10A,
        (
            "#00601Fフン、その列車の\x01",
            "前から２番目の車輌だったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8116")

    Jump("loc_824E")

    label("loc_811B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81B7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8178")

    #C0267
    ChrTalk(
        0x109,
        (
            "#10101Fええ、あの列車の\x01",
            "前から２番目の車輌でしたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81B2")

    label("loc_8178")


    #C0268
    ChrTalk(
        0x109,
        (
            "#10101Fええ、その列車の\x01",
            "前から２番目の車輌でしたね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81B2")

    Jump("loc_824E")

    label("loc_81B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_824E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8214")

    #C0269
    ChrTalk(
        0x105,
        (
            "#10400Fああ、あの列車の\x01",
            "前から２番目の車輌だったね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_824E")

    label("loc_8214")


    #C0270
    ChrTalk(
        0x105,
        (
            "#10400Fああ、その列車の\x01",
            "前から２番目の車輌だったね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_824E")

    OP_57(0x0)
    OP_5A()
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8297")
    OP_68(-1150, 1000, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Jump("loc_82C5")

    label("loc_8297")

    OP_68(-1150, 1000, -16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)

    label("loc_82C5")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8317")
    OP_93(0x106, 0x5A, 0x1F4)

    #C0271
    ChrTalk(
        0x106,
        (
            "#6P#10701F向こうにある連絡橋から\x01",
            "渡れそうです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83B2")

    label("loc_8317")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8368")
    OP_93(0x105, 0x5A, 0x1F4)

    #C0272
    ChrTalk(
        0x105,
        (
            "#6P#10400F向こうにある連絡橋から\x01",
            "渡れそうだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83B2")

    label("loc_8368")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_83B2")
    OP_93(0x109, 0x5A, 0x1F4)

    #C0273
    ChrTalk(
        0x109,
        (
            "#6P#10101F向こうにある連絡橋から\x01",
            "渡れますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83B2")


    def lambda_83B7():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_83B7)
    Sleep(50)

    def lambda_83C7():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_83C7)
    Sleep(50)

    def lambda_83D7():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_83D7)
    Sleep(50)

    def lambda_83E7():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_83E7)
    Sleep(50)

    def lambda_83F7():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_83F7)
    Sleep(50)

    def lambda_8407():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_8407)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0274
    ChrTalk(
        0x101,
        "#5P#00001Fよし……行ってみよう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8474")
    SetChrPos(0x0, -2500, 0, 0, 90)
    Jump("loc_8485")

    label("loc_8474")

    SetChrPos(0x0, -2500, 0, -16000, 90)

    label("loc_8485")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1A5, 7)
    EventEnd(0x5)
    Return()

    # Function_42_7BEE end

    def Function_43_849F(): pass

    label("Function_43_849F")

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
            "#11P#00008F（３番ホーム、２番車輌……\x01",
            "  しかも鍵が掛かっていない。）\x02\x03",

            "#00013F（……どうする？）\x02",
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
            "ドアを開けて中に入る\x01",      # 0
            "その場を離れる\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8612"),
        (1, "loc_86B9"),
        (SWITCH_DEFAULT, "loc_86E9"),
    )


    label("loc_8612")

    Sound(454, 0, 100, 0)
    OP_71(0x0, 0x295, 0x2B2, 0x0, 0x0)
    OP_79(0x0)
    OP_68(10190, 1200, -25980, 4000)

    def lambda_863D():
        OP_95(0xFE, 10000, 0, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_863D)
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
    Jump("loc_86E9")

    label("loc_86B9")

    SetChrPos(0x0, 8710, 0, -29420, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_86E9")

    label("loc_86E9")

    Return()

    # Function_43_849F end

    def Function_44_86EA(): pass

    label("Function_44_86EA")


    def lambda_86EF():
        OP_95(0xFE, 10000, 0, -28000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86EF)
    WaitChrThread(0xFE, 1)

    def lambda_870D():
        OP_95(0xFE, 10000, 0, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_870D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_86EA end

    def Function_45_8727(): pass

    label("Function_45_8727")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30200.itc", 0x1E)
    LoadChrToIndex("chr/ch24100.itc", 0x1F)
    LoadChrToIndex("chr/ch21800.itc", 0x20)
    LoadChrToIndex("apl/ch51216.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8766")
    LoadChrToIndex("apl/ch51217.itc", 0x22)
    Jump("loc_87CD")

    label("loc_8766")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8781")
    LoadChrToIndex("apl/ch51218.itc", 0x22)
    Jump("loc_87CD")

    label("loc_8781")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_879C")
    LoadChrToIndex("apl/ch51219.itc", 0x22)
    Jump("loc_87CD")

    label("loc_879C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87B7")
    LoadChrToIndex("apl/ch51220.itc", 0x22)
    Jump("loc_87CD")

    label("loc_87B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87CD")
    LoadChrToIndex("apl/ch51221.itc", 0x22)

    label("loc_87CD")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8847")
    SetChrPos(0x102, -14410, 590, -16430, 90)
    Jump("loc_88DA")

    label("loc_8847")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_886D")
    SetChrPos(0x103, -14410, 590, -16430, 90)
    Jump("loc_88DA")

    label("loc_886D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8893")
    SetChrPos(0x104, -14410, 590, -16430, 90)
    Jump("loc_88DA")

    label("loc_8893")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88B9")
    SetChrPos(0x109, -14410, 590, -16430, 90)
    Jump("loc_88DA")

    label("loc_88B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88DA")
    SetChrPos(0x105, -14410, 590, -16430, 90)

    label("loc_88DA")

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

    def lambda_893C():
        OP_95(0xFE, -1500, 10, -16020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_893C)

    def lambda_8956():
        OP_95(0xFE, -3000, 10, -15160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8956)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_899A")

    def lambda_8980():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8980)
    Jump("loc_8A51")

    label("loc_899A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89C9")

    def lambda_89AF():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_89AF)
    Jump("loc_8A51")

    label("loc_89C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89F8")

    def lambda_89DE():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_89DE)
    Jump("loc_8A51")

    label("loc_89F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A27")

    def lambda_8A0D():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8A0D)
    Jump("loc_8A51")

    label("loc_8A27")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A51")

    def lambda_8A3C():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8A3C)

    label("loc_8A51")

    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x21, 1)
    WaitChrThread(0x101, 1)
    Sound(801, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("アナウンス")

    #A0276
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "間もなく、共和国行き列車の\x01",
            "臨検が終了いたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今しばらく、列車内には\x01",
            "立ち入らないようお願いします。\x02",
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
            "#00005F共和国行きは\x01",
            "そろそろ発車か……\x02\x03",

            "#00003Fさて……\x01",
            "偽ブランド商はどこかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x21,
        (
            "さっき覗いたときは、\x01",
            "たしかあのあたりに……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BD0")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0280
    ChrTalk(
        0x102,
        "#00101F……いたわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CFD")

    label("loc_8BD0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C15")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0281
    ChrTalk(
        0x103,
        "#00201F……いました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CFD")

    label("loc_8C15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C5C")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0282
    ChrTalk(
        0x104,
        "#00301F……いやがった。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CFD")

    label("loc_8C5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CB1")
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x109,
        "#10105F……もしかして、あれですかね？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CFD")

    label("loc_8CB1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CFD")
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0284
    ChrTalk(
        0x105,
        "#10305F……もしかして、あれかな？\x02",
    )

    CloseMessageWindow()

    label("loc_8CFD")

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
            "──ほほう、\x01",
            "同業者の方でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x23,
        (
            "それで、クロスベルでの\x01",
            "商売のほうはどうでした？\x02",
        )
    )

    CloseMessageWindow()

    #N0287
    NpcTalk(
        0x22,
        "老婆",
        "#11Pふふ、それが残念ながら……\x02",
    )

    CloseMessageWindow()

    #N0288
    NpcTalk(
        0x22,
        "老婆",
        (
            "#11Pちょっと商売敵からの\x01",
            "営業妨害なんかがあってねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x23,
        (
            "むむ……\x01",
            "それは災難でしたなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x23,
        (
            "まったく、そういう輩は\x01",
            "商人の風上にも置けませんな。\x02",
        )
    )

    CloseMessageWindow()

    #N0291
    NpcTalk(
        0x22,
        "老婆",
        (
            "#11Pいいえ、私の力不足も\x01",
            "あったんだと思うの。\x02",
        )
    )

    CloseMessageWindow()

    #N0292
    NpcTalk(
        0x22,
        "老婆",
        (
            "#11Pだから今度は心機一転して、\x01",
            "帝国の方に行ってみようと思って。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x23,
        (
            "はっはっは、\x01",
            "見上げた商売根性ですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x23,
        (
            "ふむ、こうして会えたのも\x01",
            "何かの縁でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x23,
        (
            "よければ帝国方面の\x01",
            "いいツテを紹介させて\x01",
            "いただきますよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0296
    NpcTalk(
        0x22,
        "老婆",
        "#11Pあら、本当に？\x02",
    )

    CloseMessageWindow()

    #N0297
    NpcTalk(
        0x22,
        "老婆",
        (
            "#11Pおほほ…\x01",
            "なんだか悪いけど、\x01",
            "お言葉に甘えちゃおうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        "#00003F……そうはいきません。\x02",
    )

    CloseMessageWindow()
    OP_63(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0299
    NpcTalk(
        0x22,
        "老婆",
        "#11Pえ……\x02",
    )

    CloseMessageWindow()
    OP_68(7590, 1700, -13830, 3000)
    MoveCamera(45, 12, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14960, 3000)
    SetChrPos(0x101, 1130, 0, -14460, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9086")
    SetChrPos(0x102, -1220, 0, -14540, 90)
    Jump("loc_9119")

    label("loc_9086")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90AC")
    SetChrPos(0x103, -1220, 0, -14540, 90)
    Jump("loc_9119")

    label("loc_90AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90D2")
    SetChrPos(0x104, -1220, 0, -14540, 90)
    Jump("loc_9119")

    label("loc_90D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90F8")
    SetChrPos(0x109, -1220, 0, -14540, 90)
    Jump("loc_9119")

    label("loc_90F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9119")
    SetChrPos(0x105, -1220, 0, -14540, 90)

    label("loc_9119")

    SetChrPos(0x21, -140, 0, -16200, 90)

    def lambda_912F():
        OP_95(0xFE, 6590, 0, -12750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_912F)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9173")

    def lambda_9159():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9159)
    Jump("loc_922A")

    label("loc_9173")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91A2")

    def lambda_9188():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9188)
    Jump("loc_922A")

    label("loc_91A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91D1")

    def lambda_91B7():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_91B7)
    Jump("loc_922A")

    label("loc_91D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9200")

    def lambda_91E6():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_91E6)
    Jump("loc_922A")

    label("loc_9200")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_922A")

    def lambda_9215():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9215)

    label("loc_922A")


    def lambda_922F():
        OP_95(0xFE, 5280, 0, -14060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_922F)
    Sleep(1000)

    def lambda_924C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_924C)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_927F")
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x0)
    Jump("loc_92FA")

    label("loc_927F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_929F")
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x0)
    Jump("loc_92FA")

    label("loc_929F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92BF")
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x0)
    Jump("loc_92FA")

    label("loc_92BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92DF")
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0x5A, 0x0)
    Jump("loc_92FA")

    label("loc_92DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92FA")
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x5A, 0x0)

    label("loc_92FA")

    WaitChrThread(0x21, 1)
    OP_93(0x21, 0x5A, 0x0)
    OP_6F(0x79)

    #C0300
    ChrTalk(
        0x101,
        (
            "#00003Fクロスベル警察、\x01",
            "特務支援課のものです。\x02\x03",

            "#00000Fお婆さん、お久しぶりですね。\x02",
        )
    )

    CloseMessageWindow()

    #N0301
    NpcTalk(
        0x22,
        "老婆",
        "#11Pあ、あなたたちは……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93DF")

    #C0302
    ChrTalk(
        0x102,
        (
            "#00100Fふふ……\x01",
            "覚えていたみたいですね、\x01",
            "偽ブランド商のお婆さん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9529")

    label("loc_93DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_942E")

    #C0303
    ChrTalk(
        0x103,
        (
            "#00200F覚えていましたか……\x01",
            "偽ブランド商のお婆さん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9529")

    label("loc_942E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9496")

    #C0304
    ChrTalk(
        0x104,
        (
            "#00300Fへへっ、どうやら\x01",
            "ちゃんと覚えてたらしいな、\x01",
            "偽ブランド商のバーさんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9529")

    label("loc_9496")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94E1")

    #C0305
    ChrTalk(
        0x109,
        (
            "#10101Fこの人が、話に聞く\x01",
            "偽ブランド商ですか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9529")

    label("loc_94E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9529")

    #C0306
    ChrTalk(
        0x105,
        (
            "#10304Fなるほど、このマダムが\x01",
            "噂の偽ブランド商か。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9529")


    #C0307
    ChrTalk(
        0x21,
        (
            "どうやら僕たちを\x01",
            "完全に撒いたと\x01",
            "おもっていたようだね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x21,
        "ふふ、今度は逃がさないよ～！\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x23,
        (
            "は、はて……\x01",
            "一体なにがどうなって\x01",
            "いるんです？\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x23,
        (
            "偽ブランドがどうとか……\x01",
            "なんの話なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #N0311
    NpcTalk(
        0x22,
        "老婆",
        "#11P……う……うう……\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#00003F自治州法改正項目に基づき、\x01",
            "違法取引の疑いで\x01",
            "あなたを連行させて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x21,
        (
            "駅の包囲も済んでる。\x01",
            "もう逃げ場はないよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x21,
        (
            "これ以上逃げようなんて\x01",
            "考えない方が\x01",
            "いいんじゃないかな～？\x02",
        )
    )

    CloseMessageWindow()

    #N0315
    NpcTalk(
        0x22,
        "老婆",
        (
            "#11P………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    #N0316
    NpcTalk(
        0x22,
        "老婆",
        (
            "#11P………………………………\x01",
            "………じょう………いよ……\x02",
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
            "#11P#5S冗談じゃないよ、\x01",
            "このクソガキどもがぁぁぁぁぁ！！#3S\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x22, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97F1")

    #C0319
    ChrTalk(
        0x102,
        "#00105Fきゃあっ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_98A4")

    label("loc_97F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_981F")

    #C0320
    ChrTalk(
        0x103,
        "#00210F……っ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_98A4")

    label("loc_981F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9849")

    #C0321
    ChrTalk(
        0x104,
        "#00305Fどわっ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_98A4")

    label("loc_9849")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_987B")

    #C0322
    ChrTalk(
        0x109,
        "#10105Fええええええ！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_98A4")

    label("loc_987B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98A4")

    #C0323
    ChrTalk(
        0x105,
        "#10305F……ヒュウ♪\x02",
    )

    CloseMessageWindow()

    label("loc_98A4")


    #C0324
    ChrTalk(
        0x21,
        "ひぃっ！\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x23,
        "な、なななな……！？\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0326
    ChrTalk(
        0x22,
        (
            "#11P#5Sこんな場所に追い込んで、\x01",
            "逃げられなくして……#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0327
    ChrTalk(
        0x22,
        (
            "#11P#5S一度ならず二度までも、\x01",
            "よくもこのアタシを\x01",
            "ハメてくれたもんだねぇ！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0328
    ChrTalk(
        0x22,
        (
            "#11P#5Sズル賢いマネばかりしくさって！\x01",
            "だから警察は嫌いなんだよ！#3S\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#00006Fい、いや、ズル賢いって……\x01",
            "駅に逃げ込んだのは\x01",
            "あなたのミスでは……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0330
    ChrTalk(
        0x22,
        "#11P#5Sおだまり！#3S\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x22,
        (
            "#11P……フン、まあいいわ。\x01",
            "包囲だかなんだか\x01",
            "知らないけれど……\x02",
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
            "#11P#5S#15A#N捕まえられるものなら\x01",
            "捕まえてみなああああああ！！#3S\x02",
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
            "#00006Fな、何度見ても\x01",
            "すごい迫力だ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BFB")

    #C0334
    ChrTalk(
        0x102,
        (
            "#00107Fって、ロイド！\x01",
            "呆けてる場合じゃ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D1B")

    label("loc_9BFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C42")

    #C0335
    ChrTalk(
        0x103,
        (
            "#00205F……ロイドさん！\x01",
            "呆けてる場合では……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D1B")

    label("loc_9C42")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C89")

    #C0336
    ChrTalk(
        0x104,
        (
            "#00307Fおいロイド！\x01",
            "呆けてる場合じゃねえぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D1B")

    label("loc_9C89")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CD9")

    #C0337
    ChrTalk(
        0x109,
        (
            "#10105Fはっ……\x01",
            "ロ、ロイドさん！\x01",
            "呆けてる場合じゃ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D1B")

    label("loc_9CD9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D1B")

    #C0338
    ChrTalk(
        0x105,
        (
            "#10301F……呆けてる場合じゃ\x01",
            "ないんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D1B")


    #C0339
    ChrTalk(
        0x21,
        "そ、そうだね！\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#00011Fあ、ああ、追いかけよう！\x02\x03",

            "#00000F出入り口はみんなが\x01",
            "固めてくれてる……\x01",
            "あとは捕まえるだけだ！！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 46)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DBC")
    BeginChrThread(0x102, 1, 0, 47)
    Jump("loc_9E23")

    label("loc_9DBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DD7")
    BeginChrThread(0x103, 1, 0, 47)
    Jump("loc_9E23")

    label("loc_9DD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DF2")
    BeginChrThread(0x104, 1, 0, 47)
    Jump("loc_9E23")

    label("loc_9DF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E0D")
    BeginChrThread(0x109, 1, 0, 47)
    Jump("loc_9E23")

    label("loc_9E0D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E23")
    BeginChrThread(0x105, 1, 0, 47)

    label("loc_9E23")

    BeginChrThread(0x21, 1, 0, 48)
    Sleep(3500)
    OP_63(0x23, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x23)

    #C0341
    ChrTalk(
        0x23,
        "ポカーン……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E7E")
    EndChrThread(0x102, 0x1)
    Jump("loc_9EDD")

    label("loc_9E7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E97")
    EndChrThread(0x103, 0x1)
    Jump("loc_9EDD")

    label("loc_9E97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EB0")
    EndChrThread(0x104, 0x1)
    Jump("loc_9EDD")

    label("loc_9EB0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EC9")
    EndChrThread(0x109, 0x1)
    Jump("loc_9EDD")

    label("loc_9EC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EDD")
    EndChrThread(0x105, 0x1)

    label("loc_9EDD")

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
        "チィッ、あのクソガキどもめ……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x22, 1)

    #C0343
    ChrTalk(
        0x22,
        (
            "駅構内に待ち伏せされてるなら、\x01",
            "別のルートを見つけないと……\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x1F4)
    Sound(801, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("アナウンス")

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──お待たせしました。\x01",
            "共和国行き列車、\x01",
            "間もなく発車いたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "危険ですので、駆け込み乗車は\x01",
            "ご容赦くださいませ。\x02",
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
        "……これだよ！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A127")
    SetChrPos(0x102, 54450, 0, -16550, 90)
    Jump("loc_A1BA")

    label("loc_A127")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A14D")
    SetChrPos(0x103, 54450, 0, -16550, 90)
    Jump("loc_A1BA")

    label("loc_A14D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A173")
    SetChrPos(0x104, 54450, 0, -16550, 90)
    Jump("loc_A1BA")

    label("loc_A173")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A199")
    SetChrPos(0x109, 54450, 0, -16550, 90)
    Jump("loc_A1BA")

    label("loc_A199")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1BA")
    SetChrPos(0x105, 54450, 0, -16550, 90)

    label("loc_A1BA")

    SetChrPos(0x21, 53420, 0, -15670, 90)

    def lambda_A1D0():
        OP_95(0xFE, 66750, 6000, -15280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A1D0)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A217")

    def lambda_A1FD():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A1FD)
    Jump("loc_A2CE")

    label("loc_A217")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A246")

    def lambda_A22C():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A22C)
    Jump("loc_A2CE")

    label("loc_A246")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A275")

    def lambda_A25B():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A25B)
    Jump("loc_A2CE")

    label("loc_A275")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2A4")

    def lambda_A28A():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A28A)
    Jump("loc_A2CE")

    label("loc_A2A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2CE")

    def lambda_A2B9():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A2B9)

    label("loc_A2CE")

    Sleep(100)

    def lambda_A2D6():
        OP_95(0xFE, 65090, 6000, -15890, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A2D6)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_A2F5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A2F5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A323")
    WaitChrThread(0x102, 1)

    def lambda_A316():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A316)
    Jump("loc_A3B6")

    label("loc_A323")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A349")
    WaitChrThread(0x103, 1)

    def lambda_A33C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A33C)
    Jump("loc_A3B6")

    label("loc_A349")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A36F")
    WaitChrThread(0x104, 1)

    def lambda_A362():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A362)
    Jump("loc_A3B6")

    label("loc_A36F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A395")
    WaitChrThread(0x109, 1)

    def lambda_A388():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A388)
    Jump("loc_A3B6")

    label("loc_A395")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3B6")
    WaitChrThread(0x105, 1)

    def lambda_A3AE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A3AE)

    label("loc_A3B6")

    WaitChrThread(0x21, 1)

    def lambda_A3BF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A3BF)
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
        "#00005F#5Sあ、あれは……！#3S\x02",
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

    def lambda_A53B():
        OP_96(0xFE, 0x33450, 0xFFFFF9F2, 0x1FA4, 0x251C, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_A53B)
    Sleep(2000)

    #C0348
    ChrTalk(
        0x21,
        "#5S#6Aええええええええええ！！#3S\x02",
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
        "#00011Fま、まさか……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A61B")

    #C0350
    ChrTalk(
        0x102,
        "#00105Fう、うそでしょ……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6EE")

    label("loc_A61B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A64D")

    #C0351
    ChrTalk(
        0x103,
        "#00205Fそ、そんな……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6EE")

    label("loc_A64D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A685")

    #C0352
    ChrTalk(
        0x104,
        "#00305Fおいおい、マジかよ！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6EE")

    label("loc_A685")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6BD")

    #C0353
    ChrTalk(
        0x109,
        "#10101Fくっ……なんて手段を！\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6EE")

    label("loc_A6BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6EE")

    #C0354
    ChrTalk(
        0x105,
        "#10305F……なかなかやるね。\x02",
    )

    CloseMessageWindow()

    label("loc_A6EE")


    #C0355
    ChrTalk(
        0x21,
        "さ、最後の最後で……！\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x21,
        (
            "ああ、ドノバン警部に\x01",
            "なんて言えばいいんだ……？\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A7C5")

    #C0358
    ChrTalk(
        0x101,
        "#00001F……行こう、エリィ！\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x102,
        (
            "#00105F……！\x01",
            "そ、そうね、分かったわ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A92A")

    label("loc_A7C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A819")

    #C0360
    ChrTalk(
        0x101,
        "#00001F……行こう、ティオ！\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x103,
        (
            "#00201F……！\x01",
            "了解です！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A92A")

    label("loc_A819")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A875")

    #C0362
    ChrTalk(
        0x101,
        "#00001F……行こう、ランディ！\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x104,
        (
            "#00302F……！\x01",
            "おうよ、任せろ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A92A")

    label("loc_A875")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8CD")

    #C0364
    ChrTalk(
        0x101,
        "#00001F……行こう、ノエル！\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x109,
        (
            "#10107F……！\x01",
            "イエス・サー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A92A")

    label("loc_A8CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A92A")

    #C0366
    ChrTalk(
        0x101,
        "#00001F……行こう、ワジ！\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x105,
        (
            "#10304Fフフ……\x01",
            "君も負けてないじゃない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A92A")

    OP_93(0x21, 0x5A, 0x1F4)
    OP_63(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0368
    ChrTalk(
        0x21,
        "……え……もしかして……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0369
    ChrTalk(
        0x21,
        "#5S……ええっ！？#3S\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x21,
        (
            "う、うそだろ……？\x01",
            "アレを追いかけるってのかい！？\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#00007F彼女を捕まえるには\x01",
            "追うしかありません！\x02\x03",

            "#00003F時間がない……\x01",
            "お先に失礼します！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_AA36():
        OP_95(0xFE, 66750, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA36)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA7D")

    def lambda_AA63():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA63)
    Jump("loc_AB34")

    label("loc_AA7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAAC")

    def lambda_AA92():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AA92)
    Jump("loc_AB34")

    label("loc_AAAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AADB")

    def lambda_AAC1():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AAC1)
    Jump("loc_AB34")

    label("loc_AADB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB0A")

    def lambda_AAF0():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AAF0)
    Jump("loc_AB34")

    label("loc_AB0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB34")

    def lambda_AB1F():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AB1F)

    label("loc_AB34")

    OP_63(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(2000)
    OP_64(0x21)

    #C0372
    ChrTalk(
        0x21,
        (
            "ど、どうしよう……\x01",
            "支援課だけにまかせるわけには……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x21)

    #C0373
    ChrTalk(
        0x21,
        "#5S……う、うわあああああ！#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0x21, 65890, 6000, -15300, 4000, 0x0)

    def lambda_ABEC():
        OP_95(0xFE, 66750, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_ABEC)
    Sleep(1000)
    Fade(500)
    EndChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC26")
    EndChrThread(0x102, 0x1)
    Jump("loc_AC85")

    label("loc_AC26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC3F")
    EndChrThread(0x103, 0x1)
    Jump("loc_AC85")

    label("loc_AC3F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC58")
    EndChrThread(0x104, 0x1)
    Jump("loc_AC85")

    label("loc_AC58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC71")
    EndChrThread(0x109, 0x1)
    Jump("loc_AC85")

    label("loc_AC71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC85")
    EndChrThread(0x105, 0x1)

    label("loc_AC85")

    EndChrThread(0x21, 0x1)
    OP_68(69980, 1500, 7190, 0)
    MoveCamera(43, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30010, 0)
    SetChrPos(0x101, 66310, 6000, -9500, 0)
    SetChrFlags(0x101, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACF8")
    SetChrPos(0x102, 66090, 6000, -10500, 0)
    SetChrFlags(0x102, 0x40)
    Jump("loc_AD9F")

    label("loc_ACF8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD23")
    SetChrPos(0x103, 66090, 6000, -10500, 0)
    SetChrFlags(0x103, 0x40)
    Jump("loc_AD9F")

    label("loc_AD23")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD4E")
    SetChrPos(0x104, 66090, 6000, -10500, 0)
    SetChrFlags(0x104, 0x40)
    Jump("loc_AD9F")

    label("loc_AD4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD79")
    SetChrPos(0x109, 66090, 6000, -10500, 0)
    SetChrFlags(0x109, 0x40)
    Jump("loc_AD9F")

    label("loc_AD79")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD9F")
    SetChrPos(0x105, 66090, 6000, -10500, 0)
    SetChrFlags(0x105, 0x40)

    label("loc_AD9F")

    SetChrPos(0x21, 66310, 6000, -11500, 0)
    SetChrFlags(0x21, 0x40)
    Sound(456, 0, 100, 0)
    StopSound(835, 1000, 100)
    BeginChrThread(0x8, 1, 0, 54)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 50)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADEC")
    BeginChrThread(0x102, 1, 0, 51)
    Jump("loc_AE53")

    label("loc_ADEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE07")
    BeginChrThread(0x103, 1, 0, 51)
    Jump("loc_AE53")

    label("loc_AE07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE22")
    BeginChrThread(0x104, 1, 0, 51)
    Jump("loc_AE53")

    label("loc_AE22")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE3D")
    BeginChrThread(0x109, 1, 0, 51)
    Jump("loc_AE53")

    label("loc_AE3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE53")
    BeginChrThread(0x105, 1, 0, 51)

    label("loc_AE53")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEAC")
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x1000)
    Jump("loc_AF37")

    label("loc_AEAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AED0")
    ClearChrFlags(0x103, 0x40)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x1000)
    Jump("loc_AF37")

    label("loc_AED0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEF4")
    ClearChrFlags(0x104, 0x40)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x1000)
    Jump("loc_AF37")

    label("loc_AEF4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF18")
    ClearChrFlags(0x109, 0x40)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x1000)
    Jump("loc_AF37")

    label("loc_AF18")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF37")
    ClearChrFlags(0x105, 0x40)
    ClearChrFlags(0x105, 0x20)
    ClearChrFlags(0x105, 0x1000)

    label("loc_AF37")

    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("e4800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_8727 end

    def Function_46_AF4A(): pass

    label("Function_46_AF4A")

    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_46_AF4A end

    def Function_47_AF73(): pass

    label("Function_47_AF73")

    Sleep(200)
    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_47_AF73 end

    def Function_48_AF9F(): pass

    label("Function_48_AF9F")

    Sleep(800)
    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_48_AF9F end

    def Function_49_AFCB(): pass

    label("Function_49_AFCB")

    OP_95(0xFE, 66190, 6000, -15970, 4000, 0x0)
    OP_95(0xFE, 66190, 6000, -5060, 4000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_49_AFCB end

    def Function_50_AFFB(): pass

    label("Function_50_AFFB")

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

    # Function_50_AFFB end

    def Function_51_B059(): pass

    label("Function_51_B059")

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

    # Function_51_B059 end

    def Function_52_B0B7(): pass

    label("Function_52_B0B7")

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

    # Function_52_B0B7 end

    def Function_53_B113(): pass

    label("Function_53_B113")


    def lambda_B118():
        OP_95(0xFE, 210000, -1550, 8100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B118)
    Sleep(500)

    def lambda_B135():
        OP_95(0xFE, 210000, -1550, 8100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B135)
    Sleep(700)

    def lambda_B152():
        OP_95(0xFE, 210000, -1550, 8100, 8500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B152)
    Sleep(800)

    def lambda_B16F():
        OP_95(0xFE, 210000, -1550, 8100, 9500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B16F)
    Return()

    # Function_53_B113 end

    def Function_54_B185(): pass

    label("Function_54_B185")

    SetChrPos(0x8, 70000, -1550, 8100, 0)

    def lambda_B19B():
        OP_95(0xFE, 210000, -1550, 8100, 9500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B19B)
    Return()

    # Function_54_B185 end

    def Function_55_B1B1(): pass

    label("Function_55_B1B1")

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

    # Function_55_B1B1 end

    def Function_56_B2AF(): pass

    label("Function_56_B2AF")

    Sleep(11000)
    Sound(143, 0, 50, 0)
    Return()

    # Function_56_B2AF end

    SaveToFile()

Try(main)
