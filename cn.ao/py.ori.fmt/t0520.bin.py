from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t0520.bin",                # FileName
        "t0520",                    # MapName
        "t0520",                    # Location
        0x003F,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x18,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 63, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0520",                  # 0
        "诺玛",                   # 1
        "琉卡",                   # 2
        "卡洛斯",                 # 3
        "霍夫曼矿山长",           # 4
        "矿工冈兹",               # 5
        "矿工马库斯",             # 6
        "尼尔森",                 # 7
        "矿工玛尔罗",             # 8
        "米蕾优三尉",             # 9
        "艾丝蒂尔",               # 10
        "约修亚",                 # 11
        "约鲁古老人",             # 12
        "玲",                     # 13
        "游击士林",               # 14
        "游击士艾欧莉娅",         # 15
        "游击士斯克特",           # 16
        "格蕾丝",                 # 17
    ))

    AddCharChip((
        "chr/ch23500.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch23602.itc",                   # 02
        "chr/ch26302.itc",                   # 03
        "chr/ch30700.itc",                   # 04
        "chr/ch26202.itc",                   # 05
        "chr/ch45102.itc",                   # 06
        "chr/ch32602.itc",                   # 07
        "chr/ch30702.itc",                   # 08
        "chr/ch00602.itc",                   # 09
        "chr/ch00702.itc",                   # 0A
        "chr/ch06602.itc",                   # 0B
        "apl/ch51771.itc",                   # 0C
        "chr/ch32002.itc",                   # 0D
        "chr/ch32102.itc",                   # 0E
        "chr/ch27202.itc",                   # 0F
    ))

    DeclNpc(3700,    0,       4289,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-4880,   -750,    -860,    270,  261,  0x0, 0,   1,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(-6199,   -600,    4199,    270,  389,  0x0, 0,   2,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-9510,   -600,    -1200,   180,  389,  0x0, 0,   3,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-6389,   -750,    -860,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-8640,   -600,    -4380,   0,    389,  0x0, 0,   5,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(104349,  2150,    1330,    270,  405,  0x0, 0,   6,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-8640,   -600,    -4380,   0,    453,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-7590,   -600,    5769,    180,  453,  0x0, 0,   7,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(94790,   600,     79,      270,  452,  0x0, 0,   9,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(92949,   550,     79,      90,   452,  0x0, 0,   10,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(104349,  2150,    1330,    270,  453,  0x0, 0,   11,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(107339,  2650,    4500,    90,   471,  0x0, 1,   12,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-6199,   -600,    4199,    270,  452,  0x0, 0,   13,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-9289,   -600,    3869,    90,   452,  0x0, 0,   14,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(-9510,   -600,    -1200,   180,  452,  0x0, 0,   15,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(3700,    0,       2920,    1000,    3700,    1500,    4290,    0x007E, 0,  5,  0x0000)
    DeclActor(-3620,   0,       8000,    1200,    -3620,   700,     8000,    0x007C, 0,  4,  0x0000)
    DeclActor(107320,  2000,    3670,    1000,    107240,  3800,    4600,    0x007E, 0,  21, 0x0000)

    ChipFrameInfo(960, 0)                                        # 0

    ScpFunction((
        "Function_0_3C0",          # 00, 0
        "Function_1_470",          # 01, 1
        "Function_2_4F2",          # 02, 2
        "Function_3_799",          # 03, 3
        "Function_4_7F2",          # 04, 4
        "Function_5_8D0",          # 05, 5
        "Function_6_8D4",          # 06, 6
        "Function_7_186A",         # 07, 7
        "Function_8_24EC",         # 08, 8
        "Function_9_25E4",         # 09, 9
        "Function_10_2770",        # 0A, 10
        "Function_11_2855",        # 0B, 11
        "Function_12_296B",        # 0C, 12
        "Function_13_2AEC",        # 0D, 13
        "Function_14_2C01",        # 0E, 14
        "Function_15_2CA8",        # 0F, 15
        "Function_16_33B5",        # 10, 16
        "Function_17_34B6",        # 11, 17
        "Function_18_39E5",        # 12, 18
        "Function_19_3CE6",        # 13, 19
        "Function_20_4108",        # 14, 20
        "Function_21_42B0",        # 15, 21
        "Function_22_42B4",        # 16, 22
        "Function_23_43C0",        # 17, 23
        "Function_24_456D",        # 18, 24
        "Function_25_468B",        # 19, 25
        "Function_26_47BB",        # 1A, 26
        "Function_27_5381",        # 1B, 27
        "Function_28_546D",        # 1C, 28
        "Function_29_5489",        # 1D, 29
        "Function_30_54B9",        # 1E, 30
        "Function_31_54E9",        # 1F, 31
        "Function_32_5505",        # 20, 32
        "Function_33_5549",        # 21, 33
        "Function_34_558D",        # 22, 34
        "Function_35_6701",        # 23, 35
        "Function_36_6F0D",        # 24, 36
        "Function_37_75C9",        # 25, 37
        "Function_38_7C65",        # 26, 38
        "Function_39_7E4A",        # 27, 39
        "Function_40_7F98",        # 28, 40
    ))


    def Function_0_3C0(): pass

    label("Function_0_3C0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3F8"),
        (1, "loc_404"),
        (2, "loc_410"),
        (3, "loc_41C"),
        (4, "loc_428"),
        (5, "loc_434"),
        (6, "loc_440"),
        (SWITCH_DEFAULT, "loc_44C"),
    )


    label("loc_3F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_404")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_410")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_41C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_428")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_434")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_440")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_44C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_458")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_46F")

    Return()

    # Function_0_3C0 end

    def Function_1_470(): pass

    label("Function_1_470")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F1")
    OP_95(0xFE, -6300, -750, 390, 2000, 0x0)
    OP_95(0xFE, -7800, -750, -1400, 2000, 0x0)
    Sleep(1800)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    OP_95(0xFE, -6300, -750, 390, 2000, 0x0)
    OP_95(0xFE, -6300, -750, 3160, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    Jump("Function_1_470")

    label("loc_4F1")

    Return()

    # Function_1_470 end

    def Function_2_4F2(): pass

    label("Function_2_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50A")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_570")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    OP_93(0x14, 0x0, 0x0)
    Jump("loc_789")

    label("loc_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5AB")
    SetChrPos(0x9, 11090, 0, -760, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrChipByIndex(0x10, 0x7)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_789")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_621")
    SetChrPos(0x9, -4840, -750, 1710, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrChipByIndex(0xF, 0x5)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    SetChrChipByIndex(0xC, 0x8)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, -9510, -600, -1200, 180)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61C")
    SetChrFlags(0xC, 0x10)

    label("loc_61C")

    Jump("loc_789")

    label("loc_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_65B")
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0xD)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xE)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_789")

    label("loc_65B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_669")
    Jump("loc_789")

    label("loc_669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_68D")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_789")

    label("loc_68D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_69B")
    Jump("loc_789")

    label("loc_69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6A9")
    Jump("loc_789")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6D6")
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C6")
    SetChrFlags(0xC, 0x10)

    label("loc_6C6")

    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_789")

    label("loc_6D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6E4")
    Jump("loc_789")

    label("loc_6E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6F2")
    Jump("loc_789")

    label("loc_6F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_740")
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73B")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_73B")

    Jump("loc_789")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_764")
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0xF)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    Jump("loc_789")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_772")
    Jump("loc_789")

    label("loc_772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_780")
    Jump("loc_789")

    label("loc_780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_789")

    label("loc_789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_798")
    ClearScenarioFlags(0x22, 0)
    Event(0, 34)

    label("loc_798")

    Return()

    # Function_2_4F2 end

    def Function_3_799(): pass

    label("Function_3_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_7AB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D1")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_7D1")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7F1")
    OP_66(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F1")
    OP_1B(0x3, 0x0, 0x1A)

    label("loc_7F1")

    Return()

    # Function_3_799 end

    def Function_4_7F2(): pass

    label("Function_4_7F2")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "★红砖亭·推荐料理★\x01",
            "　　～经典料理\x01",
            "　　　炸鱼排～\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "张贴着炸鱼排的食谱。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_8CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『炸鱼排』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_8CC")

    TalkEnd(0xFF)
    Return()

    # Function_4_7F2 end

    def Function_5_8D0(): pass

    label("Function_5_8D0")

    Call(0, 6)
    Return()

    # Function_5_8D0 end

    def Function_6_8D4(): pass

    label("Function_6_8D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_902")
    Call(0, 35)
    Return()

    label("loc_902")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92B")
    Call(0, 36)
    Return()

    label("loc_92B")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_938")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1866")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "休息\x01",      # 2
            "放弃\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_997")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_997")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B7")
    OP_AF(0x52)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1861")

    label("loc_9B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D7")
    OP_AF(0x50)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1861")

    label("loc_9D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EB")
    Jump("loc_1861")

    label("loc_9EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A03")
    TalkEnd(0x8)
    Return()

    label("loc_A03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1861")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_A96")

    #C0004
    ChrTalk(
        0x8,
        (
            "呵呵，吃了矿山镇的\x01",
            "特色牛排之后，\x01",
            "马上就会觉得精力十足。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "你们想大吃\x01",
            "一顿的时候，\x01",
            "就再来我们店吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1861")

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6A")

    #C0006
    ChrTalk(
        0x8,
        (
            "城市那边的骚乱结束后，\x01",
            "两位神情疲倦的游击士带着\x01",
            "一个哭红了眼睛的小女孩过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "他们好像也参加了解放\x01",
            "克洛斯贝尔市的作战。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "我们作为反抗军的支持者，\x01",
            "可得好好慰劳\x01",
            "他们一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BF6")

    label("loc_B6A")


    #C0009
    ChrTalk(
        0x8,
        (
            "在楼下休息的那两位\x01",
            "游击士好像参加了\x01",
            "解放克洛斯贝尔市的作战。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "刚才还有其他游击士\x01",
            "来帮我们击退了魔兽……\x01",
            "真是受了协会不少的照顾啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF6")

    Jump("loc_1861")

    label("loc_BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C91")

    #C0011
    ChrTalk(
        0x8,
        (
            "反抗军的领袖米蕾优小姐\x01",
            "来进行补给了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "听说你们最近\x01",
            "有一场大仗要打？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "我们一定会支持你们的，\x01",
            "大家都要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CE1")

    label("loc_C91")


    #C0014
    ChrTalk(
        0x8,
        (
            "听说你们最近\x01",
            "有一场大仗要打？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "我们一定会支持你们的，\x01",
            "大家都要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE1")

    Jump("loc_1861")

    label("loc_CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_EFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC5")
    TurnDirection(0x8, 0x104, 0)

    #C0016
    ChrTalk(
        0x8,
        (
            "兰迪，听说你要\x01",
            "暂时离开反抗军？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#00304F是啊，心爱的女儿\x01",
            "正等着我去救她呢。\x02\x03",

            "#00302F大婶，米蕾优他们\x01",
            "暂时就拜托您和\x01",
            "玛因兹的各位多照顾啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "哈哈，我知道了，\x01",
            "你也要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 7)
    Jump("loc_EF8")

    label("loc_DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAC")

    #C0019
    ChrTalk(
        0x8,
        (
            "我们把山岳地带中适合藏身的地方\x01",
            "告知给反抗军的那些孩子，\x01",
            "并协助他们补给粮食和药品……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "当国防军的那些家伙来搜查时，\x01",
            "我们就装傻充愣到底，\x01",
            "在各个方面支持反抗军。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "虽然帮不上什么大忙，\x01",
            "但还是会尽力而为。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EF8")

    label("loc_EAC")


    #C0022
    ChrTalk(
        0x8,
        (
            "希望反抗军\x01",
            "继续加油。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "虽然我们帮不上什么大忙，\x01",
            "但还是会尽力而为。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF8")

    Jump("loc_1861")

    label("loc_EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_102D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE3")

    #C0024
    ChrTalk(
        0x8,
        (
            "武装集团的那些人\x01",
            "自始至终都没有碰过\x01",
            "镇上的居民和食物。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "虽然我们还是受到了相当严重的惊吓，\x01",
            "但比起损失惨重的警备队，\x01",
            "终归要幸运得多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "……话说回来，他们到底有什么目的呢？\x01",
            "真是莫名其妙啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1028")

    label("loc_FE3")


    #C0027
    ChrTalk(
        0x8,
        (
            "武装集团的那些家伙……\x01",
            "到底有什么目的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "真是莫名其妙啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1028")

    Jump("loc_1861")

    label("loc_102D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1099")

    #C0029
    ChrTalk(
        0x8,
        "唔……这场雨真让人愉快。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "在这样的天气下，\x01",
            "晚上的客人也会比较少，\x01",
            "可以适当放松一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1861")

    label("loc_1099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_12E8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1166")

    #C0031
    ChrTalk(
        0x8,
        (
            "利贝尔制造的玻璃杯\x01",
            "能够平安送到，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "看到送错的包裹中是\x01",
            "手术刀一类的东西时，\x01",
            "我真是吓了一大跳呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "哈哈，总之，\x01",
            "你们辛苦了。\x01",
            "真是谢谢啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11F6")

    label("loc_1166")


    #C0034
    ChrTalk(
        0x8,
        (
            "之前订购的利贝尔\x01",
            "玻璃杯能够平安送到，\x01",
            "真是太好了。\x02\x03",

            "看到那个送错的包裹时，我真是吓了一大跳呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "哈哈，总之，\x01",
            "你们辛苦了。\x01",
            "真是谢谢啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F6")

    Jump("loc_12E3")

    label("loc_11FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1297")

    #C0036
    ChrTalk(
        0x8,
        (
            "玛尔罗先生\x01",
            "终于打起精神了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "在旁人看来，\x01",
            "琉卡的安慰方式\x01",
            "似乎相当冷淡……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "不过，既然他能因此而打起精神，\x01",
            "那就没什么问题了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12E3")

    label("loc_1297")


    #C0039
    ChrTalk(
        0x8,
        (
            "不管怎么说，玛尔罗先生\x01",
            "好像已经打起精神了……\x01",
            "这样也算是告一段落了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E3")

    Jump("loc_1861")

    label("loc_12E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_141A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1398")

    #C0040
    ChrTalk(
        0x8,
        (
            "玛尔罗先生最近\x01",
            "似乎坚信琉卡\x01",
            "很讨厌他呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "他不再来酒馆了，\x01",
            "也无法专心工作，\x01",
            "好像相当烦闷。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "但琉卡对此却毫无察觉，\x01",
            "让事情变得很微妙……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1415")

    label("loc_1398")


    #C0043
    ChrTalk(
        0x8,
        (
            "话说回来，冈兹先生\x01",
            "也有优点呢。\x01",
            "居然会为了朋友，直接跟她谈判。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "但他的对手可是琉卡，\x01",
            "恐怕免不了一场唇枪舌剑的苦战。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1415")

    Jump("loc_1861")

    label("loc_141A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_150E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C0")

    #C0045
    ChrTalk(
        0x8,
        (
            "玛尔罗先生\x01",
            "昨天借着酒劲，\x01",
            "想跟琉卡套近乎……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "结果却被完全无视了，\x01",
            "他似乎受到相当大的打击。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "……呵呵呵，但看起来倒也很有趣。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1509")

    label("loc_14C0")


    #C0048
    ChrTalk(
        0x8,
        "玛尔罗先生真可怜啊。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "呵呵，他下次过来时，\x01",
            "免费送他些下酒菜吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1509")

    Jump("loc_1861")

    label("loc_150E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_15E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157F")

    #C0050
    ChrTalk(
        0x8,
        (
            "矿工们今天都休息，\x01",
            "所以大白天就开始喝酒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "你们要是愿意，\x01",
            "不如也喝一杯吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15DD")

    label("loc_157F")


    #C0052
    ChrTalk(
        0x8,
        (
            "哎呀呀，\x01",
            "即使矿山放假，\x01",
            "我们也没空休息啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "呵呵，但这也正是\x01",
            "做我们这行的\x01",
            "乐趣所在。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15DD")

    Jump("loc_1861")

    label("loc_15E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1732")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C5")

    #C0054
    ChrTalk(
        0x8,
        (
            "琉卡昨天喝醉了，\x01",
            "咯咯地大笑不止。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "那孩子平时很冷淡，\x01",
            "但笑起来的时候其实很可爱。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "玛尔罗先生也注意到了，\x01",
            "好像已经完全迷上她了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "呵呵呵，我最喜欢恋爱故事了。\x01",
            "接下来将会怎么发展呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_172D")

    label("loc_16C5")


    #C0058
    ChrTalk(
        0x8,
        (
            "玛尔罗先生好像在\x01",
            "昨天的宴会上迷上琉卡了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "呵呵呵，我最喜欢恋爱故事了。\x01",
            "接下来将会怎么发展呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_172D")

    Jump("loc_1861")

    label("loc_1732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1861")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FB")

    #C0060
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "你们远道而来，真是不容易呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "因为我们的主要顾客都是矿工，\x01",
            "所以菜式全都分量十足，\x01",
            "保证能让你们填饱肚子。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "想吃什么就随便点吧，\x01",
            "一定给你们装得满满的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1861")

    label("loc_17FB")


    #C0063
    ChrTalk(
        0x8,
        (
            "难得过来一趟，如果想吃\x01",
            "些什么，就随便点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "我们的菜式全都分量十足，\x01",
            "保证能让你们填饱肚子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1861")

    Jump("loc_938")

    label("loc_1866")

    TalkEnd(0x8)
    Return()

    # Function_6_8D4 end

    def Function_7_186A(): pass

    label("Function_7_186A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_19D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1958")

    #C0065
    ChrTalk(
        0x9,
        (
            "冈兹先生和玛尔罗先生\x01",
            "开开心心地跑到矿山去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "他们今晚大概会举行\x01",
            "一场庆祝复工的宴会吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        "……哎呀呀，真麻烦呢。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "话说回来，外面的情况那么糟糕，\x01",
            "若还有些事情能和从前一样，\x01",
            "倒也让人感到安心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19CF")

    label("loc_1958")


    #C0069
    ChrTalk(
        0x9,
        (
            "外面的情况那么糟糕，\x01",
            "若还有些事情能和从前一样，\x01",
            "倒也让人感到安心。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "……算啦，机会难得，\x01",
            "今晚我也玩个痛快吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CF")

    Jump("loc_24E8")

    label("loc_19D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1B3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABE")

    #C0071
    ChrTalk(
        0x9,
        (
            "反抗组织的领袖是个\x01",
            "意志非常坚强的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "竟然能第一个站出来\x01",
            "反对错误的体制。\x01",
            "这种胆量，就连男人都自愧不如啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "同为女性，\x01",
            "她有很多地方值得我学习呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AB6")

    #C0074
    ChrTalk(
        0x109,
        "#10104F嗯……确实如此。\x02",
    )

    CloseMessageWindow()

    label("loc_1AB6")

    SetScenarioFlags(0x0, 1)
    Jump("loc_1B39")

    label("loc_1ABE")


    #C0075
    ChrTalk(
        0x9,
        (
            "竟然能第一个站出来\x01",
            "反对错误的体制。\x01",
            "这种胆量，就连男人都自愧不如啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "同为女性，\x01",
            "那位领袖有很多地方值得我学习呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B39")

    Jump("loc_24E8")

    label("loc_1B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1D50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C35")

    #C0077
    ChrTalk(
        0x9,
        (
            "最近这段时间，\x01",
            "我一直在看连载小说……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "但从目前这种局势来看，\x01",
            "恐怕很难买到后面的书，\x01",
            "暂时就先不看了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        "……如果有兴趣，就送给你们吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0080
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝12卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝12卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 3)
    Jump("loc_1D4B")

    label("loc_1C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC8")

    #C0081
    ChrTalk(
        0x9,
        (
            "最近这段时间，冈兹先生和玛尔罗先生\x01",
            "大白天就会跑到店里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "……不过，矿山已经关闭了，\x01",
            "又不能去市里，\x01",
            "这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D4B")

    label("loc_1CC8")


    #C0083
    ChrTalk(
        0x9,
        (
            "矿山已经关闭了，再加上禁行令的限制，\x01",
            "想去市里都不行，\x01",
            "也难怪他们大白天就开始喝酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "唉……\x01",
            "虽然很麻烦，但还是陪陪他们吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4B")

    Jump("loc_24E8")

    label("loc_1D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E24")

    #C0085
    ChrTalk(
        0x9,
        (
            "镇子被占领的时候……\x01",
            "我只能躲在店内的\x01",
            "角落里不停发抖。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "但玛尔罗先生一直\x01",
            "鼓励我，说不用担心，\x01",
            "肯定会有人来救我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "……我以前一直觉得他很不可靠，\x01",
            "但现在对他有点改观了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E93")

    label("loc_1E24")


    #C0088
    ChrTalk(
        0x9,
        (
            "那个时候……\x01",
            "我实在太害怕了，甚至都不能\x01",
            "像平时那样出言讽刺他了。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "……必须要感谢玛尔罗先生\x01",
            "鼓励了我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E93")

    Jump("loc_24E8")

    label("loc_1E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F06")

    #C0090
    ChrTalk(
        0x9,
        (
            "我不喜欢雨天呢。\x01",
            "地板会湿漉漉的，扫除也很麻烦……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "希望卡洛斯先生快些吃完，\x01",
            "早点回去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E8")

    label("loc_1F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FAD")

    #C0092
    ChrTalk(
        0x9,
        (
            "……昨天到底是\x01",
            "怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "我只是按照冈兹先生的\x01",
            "请求，说了一句\x01",
            "『能不能打起精神来？』而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "算啦，不管了。\x01",
            "赶快做好扫除……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FDB")

    label("loc_1FAD")


    #C0095
    ChrTalk(
        0x9,
        "……呼～好困……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        "赶快把扫除做完吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1FDB")

    Jump("loc_24E8")

    label("loc_1FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2087")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFB")
    Call(0, 8)
    Jump("loc_2082")

    label("loc_1FFB")

    OP_4B(0xC, 0xFF)

    #C0097
    ChrTalk(
        0x9,
        "唔，这样吧……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "要是冈兹先生能把\x01",
            "以前赊的账全部结清，\x01",
            "说一句倒也没关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xC,
        (
            "咦……不，这个……\x01",
            "应该是另一回事吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_2082")

    Jump("loc_24E8")

    label("loc_2087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_21B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2169")

    #C0100
    ChrTalk(
        0x9,
        (
            "玛尔罗先生昨天\x01",
            "很奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "不停找我说话，\x01",
            "还问我要不要\x01",
            "和他一起喝酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "因为很烦，所以我就对他不理不睬，\x01",
            "结果今天他又莫名其妙地消沉了起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "真是的，到底在闹什么啊。\x01",
            "简直是莫名其妙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21B0")

    label("loc_2169")


    #C0104
    ChrTalk(
        0x9,
        (
            "真是的，玛尔罗先生\x01",
            "昨天简直是莫名其妙。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        "所以我最讨厌醉鬼……\x02",
    )

    CloseMessageWindow()

    label("loc_21B0")

    Jump("loc_24E8")

    label("loc_21B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_22A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224C")

    #C0106
    ChrTalk(
        0x9,
        (
            "虽说放了假，\x01",
            "但他们竟然大白天\x01",
            "就有心情喝酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "我只要一喝酒，\x01",
            "马上就会醉倒，而且还会失忆，\x01",
            "真不知道酒有什么好喝的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22A2")

    label("loc_224C")


    #C0108
    ChrTalk(
        0x9,
        (
            "他们竟然大白天\x01",
            "就有心情喝酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "……哎，算了，\x01",
            "不管怎么说，他们好像都很开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A2")

    Jump("loc_24E8")

    label("loc_22A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_23C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236E")

    #C0110
    ChrTalk(
        0x9,
        "啊，头好痛……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "昨天我被矿工们拉着\x01",
            "参加了他们的宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "我本来是不能喝酒的，结果却糊里糊涂地\x01",
            "喝了点，现在什么都不记得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        "……我应该没做什么出格的事情吧？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23C4")

    label("loc_236E")


    #C0114
    ChrTalk(
        0x9,
        (
            "啊，头好痛……\x01",
            "完全想不起昨天的事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "……我应该没有做什么\x01",
            "不该做的事情吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C4")

    Jump("loc_24E8")

    label("loc_23C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_24E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246B")

    #C0116
    ChrTalk(
        0x9,
        (
            "前几天，冈兹先生\x01",
            "又在巴鲁卡输得一败涂地。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "虽然他已经不再像以前一样\x01",
            "抱怨不休，倒是值得肯定……\x01",
            "……但未免也太不懂吸取教训了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24E8")

    label("loc_246B")


    #C0118
    ChrTalk(
        0x9,
        (
            "现在的冈兹先生就算\x01",
            "在巴鲁卡输了钱，\x01",
            "也不会再抱怨不休了。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "……但他把钱输光之后，\x01",
            "总是来这里赊账喝酒，这也很成问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E8")

    TalkEnd(0xFE)
    Return()

    # Function_7_186A end

    def Function_8_24EC(): pass

    label("Function_8_24EC")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0120
    ChrTalk(
        0xC,
        (
            "好不好嘛，琉卡小姐。\x01",
            "事情就是这样，求你了！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "喂，冈兹先生，\x01",
            "我为什么非要去\x01",
            "鼓励玛尔罗先生呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "他最近无精打采，\x01",
            "跟我也没什么关系吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xC,
        (
            "不、不对，硬要说的话，\x01",
            "应该是关系重大呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        "……我不明白你的意思。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_8_24EC end

    def Function_9_25E4(): pass

    label("Function_9_25E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_25F5")
    Jump("loc_276C")

    label("loc_25F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_271D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B2")

    #C0125
    ChrTalk(
        0xA,
        (
            "我今天赶在早上\x01",
            "完成了七耀石的运输工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "雨下大了之后，\x01",
            "地面会很泥泞，\x01",
            "如果轮胎打滑可就麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "选择相对安全的时间段行驶，\x01",
            "也算是驾驶技术的一部分。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2718")

    label("loc_26B2")


    #C0128
    ChrTalk(
        0xA,
        (
            "我今天赶在早上\x01",
            "完成了七耀石的运输工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "选择相对安全的时间段行驶，\x01",
            "也算是驾驶技术的一部分。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2718")

    Jump("loc_276C")

    label("loc_271D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_272B")
    Jump("loc_276C")

    label("loc_272B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2739")
    Jump("loc_276C")

    label("loc_2739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2747")
    Jump("loc_276C")

    label("loc_2747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2755")
    Jump("loc_276C")

    label("loc_2755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2763")
    Jump("loc_276C")

    label("loc_2763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_276C")

    label("loc_276C")

    TalkEnd(0xFE)
    Return()

    # Function_9_25E4 end

    def Function_10_2770(): pass

    label("Function_10_2770")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2781")
    Jump("loc_2851")

    label("loc_2781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_278F")
    Jump("loc_2851")

    label("loc_278F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_279D")
    Jump("loc_2851")

    label("loc_279D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27AB")
    Jump("loc_2851")

    label("loc_27AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27B9")
    Jump("loc_2851")

    label("loc_27B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_283A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D4")
    Call(0, 11)
    Jump("loc_2835")

    label("loc_27D4")


    #C0130
    ChrTalk(
        0xB,
        (
            "在该批评孩子的时候\x01",
            "就得狠狠批评，\x01",
            "这才是真正为孩子着想。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xB,
        (
            "做父母的，\x01",
            "不能一味溺爱孩子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2835")

    Jump("loc_2851")

    label("loc_283A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2848")
    Jump("loc_2851")

    label("loc_2848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2851")

    label("loc_2851")

    TalkEnd(0xFE)
    Return()

    # Function_10_2770 end

    def Function_11_2855(): pass

    label("Function_11_2855")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0132
    ChrTalk(
        0xD,
        (
            "矿山长，您昨天发怒的\x01",
            "样子真是吓了我一跳。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        (
            "您竟然对亚雷库发了那么大的火，\x01",
            "简直就像平时训斥我们时一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        (
            "在该批评孩子的时候\x01",
            "就得狠狠批评，\x01",
            "这才是真正为孩子着想。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xB,
        (
            "等到你们也为人父母的时候，\x01",
            "肯定就会明白\x01",
            "我的心情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xD,
        "这样啊……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 7)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_11_2855 end

    def Function_12_296B(): pass

    label("Function_12_296B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_297C")
    Jump("loc_2AE8")

    label("loc_297C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_298A")
    Jump("loc_2AE8")

    label("loc_298A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_29FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A5")
    Call(0, 13)
    Jump("loc_29F7")

    label("loc_29A5")


    #C0137
    ChrTalk(
        0xC,
        (
            "在这种情况下，\x01",
            "就算大白天喝酒\x01",
            "也提不起兴致啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xC,
        "唉，好想去巴鲁卡啊……\x02",
    )

    CloseMessageWindow()

    label("loc_29F7")

    Jump("loc_2AE8")

    label("loc_29FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A0A")
    Jump("loc_2AE8")

    label("loc_2A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A18")
    Jump("loc_2AE8")

    label("loc_2A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A26")
    Jump("loc_2AE8")

    label("loc_2A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A41")
    Call(0, 8)
    Jump("loc_2AB0")

    label("loc_2A41")


    #C0139
    ChrTalk(
        0xC,
        (
            "（总之，只要让\x01",
            "  琉卡安慰玛尔罗几句，\x01",
            "  他应该就能打起精神了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xC,
        (
            "（一定要想办法\x01",
            "  让她答应啊……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB0")

    Jump("loc_2AE8")

    label("loc_2AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2AC3")
    Jump("loc_2AE8")

    label("loc_2AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2AD1")
    Jump("loc_2AE8")

    label("loc_2AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2ADF")
    Jump("loc_2AE8")

    label("loc_2ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2AE8")

    label("loc_2AE8")

    TalkEnd(0xFE)
    Return()

    # Function_12_296B end

    def Function_13_2AEC(): pass

    label("Function_13_2AEC")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0141
    ChrTalk(
        0xC,
        (
            "唉……在这种情况下，\x01",
            "也不能去市里的巴鲁卡玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xC,
        "这种生活到底要持续到什么时候呢?\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xF,
        (
            "没有娱乐的生活\x01",
            "真是很难熬啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xF,
        (
            "而且矿山还关闭了，\x01",
            "想埋头工作都不行。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)
    OP_64(0xF)

    #C0145
    ChrTalk(
        0xC,
        "唉……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xF,
        "如今也只能叹气了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_13_2AEC end

    def Function_14_2C01(): pass

    label("Function_14_2C01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C12")
    Jump("loc_2CA4")

    label("loc_2C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2C20")
    Jump("loc_2CA4")

    label("loc_2C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2C2E")
    Jump("loc_2CA4")

    label("loc_2C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C3C")
    Jump("loc_2CA4")

    label("loc_2C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2C4A")
    Jump("loc_2CA4")

    label("loc_2C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C65")
    Call(0, 11)
    Jump("loc_2C88")

    label("loc_2C65")


    #C0147
    ChrTalk(
        0xD,
        (
            "唔，为人父母\x01",
            "真是很不容易啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C88")

    Jump("loc_2CA4")

    label("loc_2C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C9B")
    Jump("loc_2CA4")

    label("loc_2C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2CA4")

    label("loc_2CA4")

    TalkEnd(0xFE)
    Return()

    # Function_14_2C01 end

    def Function_15_2CA8(): pass

    label("Function_15_2CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_33B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E4A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E2F")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D5D")
    Jump("loc_2DA7")

    label("loc_2D5D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D7D")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DA7")

    label("loc_2D7D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D9D")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DA7")

    label("loc_2D9D")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DA7")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0148
    ChrTalk(
        0xFE,
        (
            "各位，非常感谢\x01",
            "你们今天配合\x01",
            "我的采访。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "如果今后有机会，\x01",
            "希望还能与各位一叙。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2E45")

    label("loc_2E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 7)), scpexpr(EXPR_END)), "loc_2E41")
    Call(0, 39)
    Return()

    label("loc_2E41")

    Call(0, 37)
    Return()

    label("loc_2E45")

    Jump("loc_33B4")

    label("loc_2E4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3244")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EF2")
    Jump("loc_2F3C")

    label("loc_2EF2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F12")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3C")

    label("loc_2F12")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F32")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3C")

    label("loc_2F32")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F3C")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CB")

    #C0150
    ChrTalk(
        0x101,
        "#00000F尼尔森先生。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0151
    ChrTalk(
        0xFE,
        "唔，这声音是罗伊德警官吧？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "今天怎么来玛因兹了？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#00000F哦，我们在巡逻过程中\x01",
            "顺便来这里看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        (
            "#00100F尼尔森先生，\x01",
            "您是来这里取材的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "嗯，我准备采访一下\x01",
            "这里的镇长先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "关于该镇开采七耀石的历史，\x01",
            "以及近代的各种变化，\x01",
            "我想听听镇长的看法。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "大家如今都在探讨独立的利弊，\x01",
            "我认为在这种时候更应该\x01",
            "将目光聚焦于自治州的历史。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x103,
        "#00200F这……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x109,
        (
            "#10100F该怎么说呢，\x01",
            "着眼点真是与众不同呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "哈哈，所以我总是\x01",
            "事倍功半呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "各位应该\x01",
            "也很忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "今后也许还要面对各种挑战，\x01",
            "请多加努力哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        "#00000F好的，谢谢您。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16B, 5)
    Jump("loc_3238")

    label("loc_31CB")


    #C0164
    ChrTalk(
        0xFE,
        (
            "嗯，采访的时间还没到，\x01",
            "我就在这里悠闲地\x01",
            "消磨一下时间吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "呵呵，这个房间很安静，\x01",
            "可以让人心情平和。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3238")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_33B4")

    label("loc_3244")

    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32D8")
    Jump("loc_3322")

    label("loc_32D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32F8")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3322")

    label("loc_32F8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3318")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3322")

    label("loc_3318")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3322")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0166
    ChrTalk(
        0xFE,
        (
            "呵呵，这个房间很安静，\x01",
            "可以让人心情平和。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "在采访的时间到来之前，\x01",
            "可以悠闲地消磨一下时间了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_33B4")

    Return()

    # Function_15_2CA8 end

    def Function_16_33B5(): pass

    label("Function_16_33B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_33C6")
    Jump("loc_34B2")

    label("loc_33C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_33D4")
    Jump("loc_34B2")

    label("loc_33D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_34B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33EF")
    Call(0, 13)
    Jump("loc_34B2")

    label("loc_33EF")

    SetChrSubChip(0xF, 0x2)

    #C0168
    ChrTalk(
        0xF,
        (
            "（一开始还觉得能见到琉卡，\x01",
            "  所以没什么不好……）\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xF,
        (
            "（但一直泡在酒馆里，\x01",
            "  给人留下的印象不大好吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0xF, 500)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0170
    ChrTalk(
        0x9,
        "（……看我干什么？）\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x10E, 0x0)
    SetChrSubChip(0xF, 0x0)

    label("loc_34B2")

    TalkEnd(0xFE)
    Return()

    # Function_16_33B5 end

    def Function_17_34B6(): pass

    label("Function_17_34B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_34C7")
    Jump("loc_39E1")

    label("loc_34C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_39D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A5")

    #C0171
    ChrTalk(
        0x10,
        (
            "#07901F兰迪，支援科的各位……\x01",
            "事情我已经听说了。\x02\x03",

            "#07903F既然独立宣言现在已经无效，\x01",
            "那么总统应该无法再\x01",
            "自由调动国防军了。\x02\x03",

            "#07901F接下来，只要能将\x01",
            "包围城市的『结界』消除……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x103,
        (
            "#00200F这是解放克洛斯贝尔市的\x01",
            "最好机会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#00000F我们会设法\x01",
            "消除结界的。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#00303F不过，『赤色星座』对这种情况\x01",
            "肯定有所准备。\x02\x03",

            "#00301F在实行作战计划之前，\x01",
            "他们也许就会开始\x01",
            "全力剿灭反抗军了。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        "#00103F看来事不宜迟呢……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x10,
        (
            "#07903F总之，我们会做好充分准备，\x01",
            "以便开始实行作战计划。\x02\x03",

            "这次可以借助神狼们的力量，\x01",
            "我想局势不会再像上次那样狼狈了，\x01",
            "应该可以跟『赤色星座』拼个势均力敌。\x02\x03",

            "#07901F所以，结界的事情\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x104,
        (
            "#00304F好，交给我们吧。\x02\x03",

            "#00301F……多加小心啊，米蕾优。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x104, 0)
    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3810")
    Jump("loc_385A")

    label("loc_3810")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3830")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_385A")

    label("loc_3830")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3850")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_385A")

    label("loc_3850")

    OP_52(0x10, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_385A")

    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x10)

    #C0178
    ChrTalk(
        0x10,
        "#07902F嗯，你也是。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 0)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_39D3")

    label("loc_38A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3979")

    #C0179
    ChrTalk(
        0x10,
        (
            "#07903F总之，我们会做好充分准备，\x01",
            "以便开始实行作战计划。\x02\x03",

            "这次可以借助神狼们的力量，\x01",
            "我想局势不会再像上次那样狼狈了，\x01",
            "应该可以跟『赤色星座』拼个势均力敌。\x02\x03",

            "#07901F结界的事情就\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_39D3")

    label("loc_3979")


    #C0180
    ChrTalk(
        0x10,
        (
            "#07903F我们会做好充分准备，\x01",
            "以便开始实行作战计划。\x02\x03",

            "#07901F结界的事情就\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D3")

    Jump("loc_39E1")

    label("loc_39D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_39E1")

    label("loc_39E1")

    TalkEnd(0xFE)
    Return()

    # Function_17_34B6 end

    def Function_18_39E5(): pass

    label("Function_18_39E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C3B")

    #C0181
    ChrTalk(
        0x11,
        (
            "#00802F#30W……罗伊德，还有各位，\x01",
            "你们要多加小心啊。\x02\x03",

            "#00808F努力自然是好，\x01",
            "但可不要像\x01",
            "『帕蒂尔·玛蒂尔』那样……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        "#00000F嗯……我明白。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x104,
        (
            "#00308F仔细想想，它也是\x01",
            "我们的救命恩人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x103,
        (
            "#00203F……上次造访工房时，\x01",
            "要是和它多聊聊就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x11,
        (
            "#00808F#30W嗯……我也应该\x01",
            "和它多聊聊的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    #C0186
    ChrTalk(
        0x11,
        (
            "#00804F#30W……至于玲，\x01",
            "你们就不用担心了。\x02\x03",

            "#00800F这半年来，她经历了很多事情，\x01",
            "已经在真正意义上坚强了起来……\x02\x03",

            "#00802F而且还有很好的朋友陪伴着她，\x01",
            "我想她一定能从悲痛中走出的。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        "#00004F是吗……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        (
            "#00100F……等她醒来的时候，\x01",
            "请替我们向她问好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3CE2")

    label("loc_3C3B")


    #C0189
    ChrTalk(
        0x11,
        (
            "#00804F#30W你们不用担心玲。\x02\x03",

            "#00800F这半年来，她经历了很多事情，\x01",
            "已经在真正意义上坚强了起来……\x02\x03",

            "#00802F而且还有很好的朋友陪伴着她，\x01",
            "我想她一定能从悲痛中走出的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE2")

    TalkEnd(0xFE)
    Return()

    # Function_18_39E5 end

    def Function_19_3CE6(): pass

    label("Function_19_3CE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_408D")

    #C0190
    ChrTalk(
        0x12,
        (
            "#00903F#30W……诺华提斯博士好像也\x01",
            "离开克洛斯贝尔了。\x02\x03",

            "#00901F如果『结社』不再继续与我们为敌，\x01",
            "自然是再好不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#00001F老实说，真猜不到\x01",
            "他们的目的究竟是什么。\x02\x03",

            "#00003F只知道他们在帝国那边\x01",
            "有什么企图……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x12,
        (
            "#00903F#30W……是『幻焰计划』吧。\x02\x03",

            "#00901F那似乎是一项以克洛斯贝尔事件\x01",
            "为开端的大规模计划……\x02\x03",

            "#00908F……真担心奥利维尔先生他们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x103,
        "#00205F奥利维尔先生是指……\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x104,
        "#00303F奥利维特皇子吗？\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x12,
        (
            "#00903F#30W嗯，自从帝国爆发内战之后，\x01",
            "我们就和他失去了联系。\x02\x03",

            "#00908F虽然有穆拉先生在他身边，\x01",
            "应该不会发生什么事……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        "#00108F但还是很担心吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4088")
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0197
    ChrTalk(
        0x12,
        (
            "#00900F#30W对了，你们……\x01",
            "把这个收下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0198
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('塞姆里亚石碎片', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 3)

    #C0199
    ChrTalk(
        0x101,
        "#00005F这是……？\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x12,
        (
            "#00900F#30W这东西掉落在『帕蒂尔·玛蒂尔』\x01",
            "自爆之处的附近。\x02\x03",

            "#00903F……我想应该是\x01",
            "『神机』零件的一部分，\x01",
            "说不定可以派上什么用场。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#00000F明白了……\x01",
            "那就不客气啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4088")

    Jump("loc_4104")

    label("loc_408D")


    #C0202
    ChrTalk(
        0x12,
        (
            "#00903F#30W那棵『碧之大树』……\x02\x03",

            "从规模而言，恐怕已经超过了\x01",
            "当时出现在利贝尔的浮游都市。\x02\x03",

            "#00900F请各位多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4104")

    TalkEnd(0xFE)
    Return()

    # Function_19_3CE6 end

    def Function_20_4108(): pass

    label("Function_20_4108")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4203")

    #C0203
    ChrTalk(
        0x13,
        (
            "#03900F当初制造『帕蒂尔·玛蒂尔』的\x01",
            "思考模块时，并没有为它设计过\x01",
            "能够做出那种程度的自主行动的指令。\x02\x03",

            "与玲的相遇，使它也\x01",
            "拥有了自己的『心』吗……\x02\x03",

            "#03903F……我当人偶师已经有几十年了，\x01",
            "直到现在，仍然还有很多需要学习的东西啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_42AC")

    label("loc_4203")


    #C0204
    ChrTalk(
        0x13,
        (
            "#03900F……对玲来说，这次的事情\x01",
            "也许反而会起到正面效果。\x02\x03",

            "#03903F因为她这次真正意义上地经历了\x01",
            "过去从没有经历过的『离别』……\x02\x03",

            "#03900F玲的人生体验，现在才刚刚开始。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42AC")

    TalkEnd(0xFE)
    Return()

    # Function_20_4108 end

    def Function_21_42B0(): pass

    label("Function_21_42B0")

    Call(0, 22)
    Return()

    # Function_21_42B0 end

    def Function_22_42B4(): pass

    label("Function_22_42B4")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_436D")

    #C0205
    ChrTalk(
        0x14,
        (
            "#03317F#2S#40W………帕蒂尔·玛蒂尔…………\x02\x03",

            "#2S#40W……为什么………\x01",
            "…………为什么要丢下玲………\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        "#00008F……玲…………\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x102,
        "#00103F……还是不要打扰她了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_43BC")

    label("loc_436D")


    #C0208
    ChrTalk(
        0x14,
        "#03317F#2S#40W………爸爸………妈妈…………\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "玲哭累之后睡着了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_43BC")

    TalkEnd(0x14)
    Return()

    # Function_22_42B4 end

    def Function_23_43C0(): pass

    label("Function_23_43C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44DD")

    #C0210
    ChrTalk(
        0xFE,
        (
            "我和艾欧莉娅一起\x01",
            "负责处理占领事件的\x01",
            "善后事宜。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "出现在周边地带的通缉魔兽\x01",
            "已经都被我们消灭，\x01",
            "暂时可以安心了……\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "但玛因兹的各位遭受的\x01",
            "心灵创伤似乎也相当严重呢。\x01",
            "很多人因为不安而夜不能寐。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "看来还是和米歇尔商量一下，\x01",
            "把滞留在此的时间\x01",
            "延长一些为好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_4569")

    label("loc_44DD")


    #C0214
    ChrTalk(
        0xFE,
        (
            "玛因兹的各位遭受的\x01",
            "心灵创伤似乎相当严重呢，\x01",
            "很多人因为不安而夜不能寐。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "看来还是和米歇尔商量一下，\x01",
            "把滞留在此的时间\x01",
            "延长一些为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4569")

    TalkEnd(0xFE)
    Return()

    # Function_23_43C0 end

    def Function_24_456D(): pass

    label("Function_24_456D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_462F")

    #C0216
    ChrTalk(
        0xFE,
        (
            "由于那起袭击事件，\x01",
            "乌尔斯拉医院好像也一直忙得不可开交。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "所以，我会尽力救治能在\x01",
            "玛因兹就地治疗的伤员。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "虽然很辛苦……但在这种时候\x01",
            "必须要做好自己能完成的工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_4687")

    label("loc_462F")


    #C0219
    ChrTalk(
        0xFE,
        (
            "我会尽力救治能在\x01",
            "玛因兹就地治疗的伤员。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "真庆幸自己拥有医师执照。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4687")

    TalkEnd(0xFE)
    Return()

    # Function_24_456D end

    def Function_25_468B(): pass

    label("Function_25_468B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_473C")

    #C0221
    ChrTalk(
        0xFE,
        (
            "我今天和搭档温蔡尔\x01",
            "分头行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "为了填补艾丝蒂尔他们\x01",
            "留下的空缺，这种特殊\x01",
            "排班也越来越多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "虽然讨伐魔兽的时候很吃力，\x01",
            "但还是要努力坚持下去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_47B7")

    label("loc_473C")


    #C0224
    ChrTalk(
        0xFE,
        (
            "我今天和搭档温蔡尔\x01",
            "分头行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "虽然讨伐魔兽的时候很吃力，\x01",
            "但为了填补因人手不足而出现的空缺，\x01",
            "还是要努力坚持下去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47B7")

    TalkEnd(0xFE)
    Return()

    # Function_25_468B end

    def Function_26_47BB(): pass

    label("Function_26_47BB")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(94170, 1500, 6300, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0xFA0)
    Sound(105, 0, 100, 0)
    OP_74(0x2, 0x1E)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(500)
    OP_68(93680, 1500, 1310, 3000)
    MoveCamera(41, 20, 0, 3000)
    OP_6E(260, 3000)
    SetCameraDistance(34000, 3000)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 1, 0, 27)
    WaitChrThread(0x101, 1)
    Sleep(600)
    BeginChrThread(0x102, 1, 0, 27)
    WaitChrThread(0x102, 1)
    Sleep(600)
    BeginChrThread(0x103, 1, 0, 27)
    WaitChrThread(0x103, 1)
    Sleep(600)
    BeginChrThread(0x104, 1, 0, 27)
    WaitChrThread(0x104, 1)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4903")
    BeginChrThread(0x109, 1, 0, 27)
    WaitChrThread(0x109, 1)
    Sleep(600)

    label("loc_4903")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4920")
    BeginChrThread(0x105, 1, 0, 27)
    WaitChrThread(0x105, 1)
    Sleep(600)

    label("loc_4920")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_493D")
    BeginChrThread(0x106, 1, 0, 27)
    WaitChrThread(0x106, 1)
    Sleep(600)

    label("loc_493D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_495A")
    BeginChrThread(0x10A, 1, 0, 27)
    WaitChrThread(0x10A, 1)
    Sleep(600)

    label("loc_495A")

    OP_6F(0x79)
    Sleep(700)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x11, 0x2)
    SetChrSubChip(0x12, 0x1)

    #C0226
    ChrTalk(
        0x11,
        "#12P#00805F#30W啊，罗伊德，还有大家……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x12,
        "#12P#00902F#30W……你们好………\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        "#5P#00005F艾丝蒂尔、约修亚！？\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x102,
        "#5P#00102F你们来这里了啊……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)

    #C0230
    ChrTalk(
        0x104,
        (
            "#5P#00300F我听说了！你们漂亮地\x01",
            "把那个大家伙干掉了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x103,
        (
            "#5P#00202F真不愧是艾丝蒂尔小姐三人组\x01",
            "和『帕蒂尔·玛蒂尔』。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x11,
        "#12P#00802F#30W啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x12,
        (
            "#12P#00903F#30W……不过，我们能取得胜利，\x01",
            "全部都要归功于『它』的牺牲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        "#5P#00005F咦……\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x102,
        "#5P#00105F说起来……小玲呢？\x02",
    )

    CloseMessageWindow()

    #N0236
    NpcTalk(
        0x13,
        "老人的声音",
        "……玲睡着了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(104580, 3500, 2720, 5000)
    MoveCamera(57, 16, 0, 5000)
    OP_6E(260, 5000)
    SetCameraDistance(34000, 5000)

    def lambda_4CBE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4CBE)
    Sleep(50)

    def lambda_4CCE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4CCE)
    Sleep(50)

    def lambda_4CDE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4CDE)
    Sleep(50)

    def lambda_4CEE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4CEE)
    Sleep(50)

    def lambda_4CFE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_4CFE)
    Sleep(50)

    def lambda_4D0E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_4D0E)
    OP_6F(0x79)

    #C0237
    ChrTalk(
        0x14,
        "#11P#03317F#40W#2S………………………………\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        "#00005F约鲁古大师！\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x103,
        "#00203F……您也在啊。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x13,
        (
            "#11P#03903F嗯……我接到了他们的联络。\x02\x03",

            "#03900F虽然我不关心外面的混乱情况，\x01",
            "但既然『帕蒂尔·玛蒂尔』牺牲了，\x01",
            "我怎么也得过来看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        "#00105F那个智能兵器……牺牲了……？\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#00305F喂喂，难道说……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(93680, 1500, 1310, 0)
    MoveCamera(41, 20, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    OP_93(0x0, 0xB4, 0x0)
    OP_93(0x1, 0xB4, 0x0)
    OP_93(0x2, 0xB4, 0x0)
    OP_93(0x3, 0xB4, 0x0)
    OP_93(0x4, 0xB4, 0x0)
    OP_93(0x5, 0xB4, 0x0)
    OP_70(0x2, 0x0)
    OP_0D()

    #C0243
    ChrTalk(
        0x11,
        (
            "#12P#00808F#30W……嗯……\x01",
            "『帕蒂尔·玛蒂尔』抱着那个巨大的智能兵器，\x01",
            "飞上了天空……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x12,
        (
            "#12P#00908F#30W……大概……\x01",
            "是启动了自爆装置吧。\x02\x03",

            "#00903F这也是出于它自己的判断。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        "#5P#00003F……原来是这样……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x103,
        "#5P#00208F机械竟能做出这种判断……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(107070, 3500, 4380, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(29150, 0)
    OP_0D()

    #C0247
    ChrTalk(
        0x14,
        (
            "#11P#03317F#2S#40W………呜…………\x01",
            "…………帕蒂尔·玛蒂尔…………\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x104,
        "#00305F哭累之后睡着了吗……\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        (
            "#00103F……这也难怪啊……\x01",
            "心灵相通的伙伴已经……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(104580, 3500, 2720, 0)
    MoveCamera(57, 16, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    OP_0D()

    #C0250
    ChrTalk(
        0x13,
        (
            "#11P#03903F……关于『帕蒂尔·玛蒂尔』一事，\x01",
            "只能说是命运。\x02\x03",

            "#03900F我认为，我们应该尊重\x01",
            "『帕蒂尔·玛蒂尔』那颗为了\x01",
            "保护这孩子而舍身一搏的『心』。\x02\x03",

            "它的表现对我这个人偶师来说，也是无上的光荣。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        "#00001F大师……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(93680, 1500, 1310, 0)
    MoveCamera(41, 20, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    OP_0D()

    #C0252
    ChrTalk(
        0x11,
        (
            "#12P#00801F#30W我已经听说了，\x01",
            "好像发生了很严重的情况？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x12,
        (
            "#12P#00900F#30W我们打算恢复过来之后，\x01",
            "就去助你们一臂之力。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#5P#00004F谢谢二位。\x02\x03",

            "#00000F但你们现在应该\x01",
            "好好休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#5P#00303F我们虽然不是小玲的那架智能兵器……\x02\x03",

            "#00300F但为了守护重要之人，\x01",
            "现在同样会拼尽全力。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x11,
        "#12P#00802F#30W是吗……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x12,
        (
            "#12P#00904F#30W……愿女神保佑你们，\x01",
            "请多加小心。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7563", 0)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x0, 94240, 0, 3400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x2, 0x10)
    OP_1B(0x3, 0xFF, 0xFFFF)
    SetScenarioFlags(0x1CE, 2)
    EventEnd(0x5)
    Return()

    # Function_26_47BB end

    def Function_27_5381(): pass

    label("Function_27_5381")

    SetChrPos(0xFE, 94200, 0, 6500, 180)

    def lambda_5397():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5397)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53C7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 28)
    Jump("loc_546C")

    label("loc_53C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53EB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 29)
    Jump("loc_546C")

    label("loc_53EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_540F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 30)
    Jump("loc_546C")

    label("loc_540F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5433")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 31)
    Jump("loc_546C")

    label("loc_5433")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5457")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 32)
    Jump("loc_546C")

    label("loc_5457")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_546C")
    BeginChrThread(0xFE, 2, 0, 33)

    label("loc_546C")

    Return()

    # Function_27_5381 end

    def Function_28_546D(): pass

    label("Function_28_546D")

    OP_95(0xFE, 94200, 0, 3030, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_546D end

    def Function_29_5489(): pass

    label("Function_29_5489")

    OP_95(0xFE, 94200, 0, 4850, 2000, 0x0)
    OP_95(0xFE, 93110, 0, 3070, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_29_5489 end

    def Function_30_54B9(): pass

    label("Function_30_54B9")

    OP_95(0xFE, 94200, 0, 4850, 2000, 0x0)
    OP_95(0xFE, 95280, 0, 3120, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_30_54B9 end

    def Function_31_54E9(): pass

    label("Function_31_54E9")

    OP_95(0xFE, 94210, 0, 4150, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_31_54E9 end

    def Function_32_5505(): pass

    label("Function_32_5505")

    OP_95(0xFE, 94260, 0, 5260, 2000, 0x0)
    OP_95(0xFE, 93580, 0, 4960, 2000, 0x0)
    OP_95(0xFE, 93270, 0, 4310, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_5505 end

    def Function_33_5549(): pass

    label("Function_33_5549")

    OP_95(0xFE, 94260, 0, 5260, 2000, 0x0)
    OP_95(0xFE, 95020, 0, 4960, 2000, 0x0)
    OP_95(0xFE, 95250, 0, 4350, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_5549 end

    def Function_34_558D(): pass

    label("Function_34_558D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32600.itc", 0x1E)
    LoadChrToIndex("chr/ch06000.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetMapObjFlags(0x4, 0x4)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x107, 0x5)
    SetChrPos(0x101, 101200, 2000, 1500, 90)
    SetChrPos(0x107, 100150, 2000, 3100, 135)
    SetChrPos(0x105, 101400, 2000, 600, 90)
    SetChrPos(0x106, 103700, 2000, 3500, 180)
    SetChrPos(0x103, 101790, 2000, 2800, 135)
    SetChrChipByIndex(0x107, 0x20)
    BeginChrThread(0x107, 3, 0, 0)
    SetChrPos(0x104, 104400, 2000, 1300, 270)
    SetChrPos(0x10, 104250, 2000, 100, 270)
    SetChrPos(0x18, 105000, 2000, 2950, 225)
    OP_68(102370, 3400, 1380, 0)
    MoveCamera(59, 15, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33500, 0)
    SetCameraDistance(35500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0258
    ChrTalk(
        0x104,
        (
            "#00306F#11P原来如此，\x01",
            "事情还真是\x01",
            "不得了啊。\x02\x03",

            "#00301F而且，阿琪她……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x18,
        (
            "#02106F#5P唔，实在太脱离现实，\x01",
            "好像都没法写成新闻了……\x02\x03",

            "#02101F不过，你们无论如何\x01",
            "都会把她带回来吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        "#00001F#6P嗯，那当然。\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        "#00203F#6P这还用说。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x104,
        "#00308F#11P…………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x104, 500)
    Sleep(100)

    #C0263
    ChrTalk(
        0x10,
        (
            "#07904F#11P……兰迪，\x01",
            "不用担心我们。\x02\x03",

            "#07902F你原本不就是以帮忙救出\x01",
            "支援科的同伴为条件\x01",
            "而协助我们的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x10, 500)

    #C0264
    ChrTalk(
        0x104,
        "#00305F#5P啊，这个……\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        "#00008F#6P……原来是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x103,
        "#00208F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x105,
        (
            "#10404F#6P嗯……老实说，\x01",
            "我们现在确实\x01",
            "很需要你的助力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x10,
        (
            "#07904F#11P抵抗活动只是我们\x01",
            "这些难以接受国防军的\x01",
            "警备队员在意气用事而已。\x02\x03",

            "#07902F你早已离开了警备队，\x01",
            "自然应该去帮助自己的同伴。\x02\x03",

            "#07909F而且那些狼今后\x01",
            "也会帮助我们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x107,
        (
            "#01203F#6P#3C嗯，我已经郑重交代过了，\x01",
            "让它们协助你们。\x02\x03",

            "#01200F在山岳地带的战斗中，\x01",
            "它们应该能发挥一些作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x104,
        "#00306F#5P……谢谢，真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    def lambda_5A48():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5A48)
    Sleep(50)

    def lambda_5A58():
        OP_93(0x10, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_5A58)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x10, 0)

    #C0271
    ChrTalk(
        0x104,
        (
            "#00300F#11P身为支援科成员，\x01",
            "还有阿琪的监护人！\x02\x03",

            "罗伊德，阿缇，\x01",
            "我也和你们一起行动！\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        "#00002F#6P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x103,
        "#00204F#6P……太好了。\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x106,
        "#10709F#5P呵呵……让人信心倍增呢。\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x18,
        (
            "#02103F#5P唔，既然如此……\x02\x03",

            "#02102F能不能也让我\x01",
            "跟你们一起走呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5C07():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C07)
    Sleep(50)

    def lambda_5C17():
        TurnDirection(0x103, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5C17)
    Sleep(50)

    def lambda_5C27():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5C27)
    Sleep(50)

    def lambda_5C37():
        TurnDirection(0x105, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5C37)
    Sleep(50)

    def lambda_5C47():
        TurnDirection(0x106, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5C47)
    Sleep(50)

    def lambda_5C57():
        TurnDirection(0x10, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_5C57)
    Sleep(50)

    def lambda_5C67():
        TurnDirection(0x107, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_5C67)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)

    #C0276
    ChrTalk(
        0x101,
        "#00011F#6P咦……！？\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x103,
        "#00211F#6P您说什么呢……？\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x18,
        (
            "#02104F#5P看样子，今后的动向\x01",
            "将会以你们为中心。\x02\x03",

            "#02110F身为记者，\x01",
            "自然不应该错过啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        "#00012F#6P这，可是……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x105,
        (
            "#10406F#6P唔，我倒是不介意。\x02\x03",

            "#10400F但如果让媒体界的人士上了飞艇，\x01",
            "阿巴斯肯定会唠叨个没完呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x106,
        (
            "#10706F#6P……如果被写进报道，\x01",
            "我也会很困扰的。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x18,
        (
            "#02105F#5P哦，不用担心。\x02\x03",

            "#02104F虽然我想写进报道的事数不胜数，\x01",
            "但目前的状况并不允许。\x02\x03",

            "#02106F我现在只想知道，\x01",
            "克洛斯贝尔独立国究竟会怎样收场。\x02\x03",

            "#02101F历史又是否会选择这个\x01",
            "充满欺瞒的新体制呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x101,
        "#00005F#6P历史的选择……？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x18,
        (
            "#02103F#5P目前，整个大陆\x01",
            "都处于相当混乱的状态。\x02\x03",

            "不得不说，这很大程度上\x01",
            "是由迪塔总统造成的……\x02\x03",

            "#02101F就算他退出舞台，\x01",
            "我们又能否渡过这场危机呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0285
    ChrTalk(
        0x101,
        "#00011F#6P……这个……\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x10,
        (
            "#07906F#12P说实话……\x01",
            "可能很难呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x18,
        (
            "#02106F#5P实际上，在卡尔瓦德\x01",
            "一百年前的民主化时期，\x01",
            "革命政府也有过不少龌龊行径。\x02\x03",

            "#02103F暗杀行为自不必说，\x01",
            "甚至还有类似于袭击克洛斯贝尔市\x01",
            "事件这样的阴谋。\x02\x03",

            "#02101F但到了现在，当年那些行为\x01",
            "都被一定程度地正当化了。\x02\x03",

            "迪塔总统的所作所为，\x01",
            "最终是否也会如此呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        "#00008F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x106,
        "#10708F#6P（……一百年前的暗杀……）\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x18,
        (
            "#02106F#5P总之，我还是觉得\x01",
            "目前这种状况是不合理的。\x02\x03",

            "#02100F正因如此，我才想确认一下。\x02\x03",

            "克洛斯贝尔今后究竟会\x01",
            "选择怎样的道路。\x02\x03",

            "而它的选择又会\x01",
            "在历史上留下什么样的痕迹。\x02\x03",

            "#02109F我总觉得，只要跟着你们，\x01",
            "就能找到这些答案呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        "#00000F#6P……格蕾丝小姐。\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x104,
        (
            "#00302F#12P该怎么说呢……\x01",
            "没想到你会想得那么深远。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x103,
        (
            "#00202F#6P说得太过严肃，\x01",
            "简直就像变了个人……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x18,
        (
            "#02109F#5P啊哈哈，话说回来，\x01",
            "最大的理由还是因为很有趣。\x02\x03",

            "#02110F而且我在通讯社那边\x01",
            "还有信息渠道呢。\x02\x03",

            "说不定可以为你们\x01",
            "提供市内的情报哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0295
    ChrTalk(
        0x101,
        (
            "#00004F#6P明白了，\x01",
            "我没有异议。\x02\x03",

            "#00000F瓦吉，莉夏，\x01",
            "你们介意吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x106,
        (
            "#10710F#6P我……\x01",
            "只要不被写进新闻就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        (
            "#10404F#6P呵呵，我也不介意。\x02\x03",

            "#10402F不过，要想说服阿巴斯，\x01",
            "大概就得花些时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x18,
        (
            "#02109F#5P谢啦，欠你们一个人情！\x02\x03",

            "#02110F好，大家打起精神来，\x01",
            "向菲利策奖发起冲击吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0299
    ChrTalk(
        0x101,
        (
            "#00012F#6P这……我们并不是\x01",
            "在帮格蕾丝小姐的忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x103,
        "#00211F#6P算啦，格蕾丝小姐一向都是这样。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(37500, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0301
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德一行人前去问候了\x01",
            "一直在暗中协助反抗军的\x01",
            "玛因兹镇长比克森……\x02\x03",

            "商谈过今后的计划之后，\x01",
            "众人就与准备返回山中\x01",
            "据点的米蕾优等人分别了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 5)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_558D end

    def Function_35_6701(): pass

    label("Function_35_6701")

    EventBegin(0x0)
    Fade(500)
    OP_68(2960, 1500, 1030, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(30500, 0)
    SetChrPos(0x101, 3100, 0, 2000, 0)
    SetChrPos(0x102, 4300, 0, 2000, 0)
    SetChrPos(0x103, 3100, 0, 800, 0)
    SetChrPos(0x109, 4300, 0, 800, 0)
    SetChrPos(0x104, 3100, 0, -400, 0)
    SetChrPos(0x105, 4300, 0, -400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0302
    ChrTalk(
        0x8,
        (
            "啊，欢迎，\x01",
            "欢迎光临『红砖亭』。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#00000F打扰了，\x01",
            "我们是特别任务支援科的成员……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将『美食向导』取材一事的\x01",
            "情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0305
    ChrTalk(
        0x8,
        (
            "哦，原来你们是为此而来的啊，\x01",
            "我已经听通讯社的人说过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x8,
        (
            "那么，我就为你们\x01",
            "烹调矿山镇的特色菜\x01",
            "『精力牛排』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x103,
        (
            "#00206F……听起来好像会把\x01",
            "胃撑得满满呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x8,
        (
            "哦，你们要四处取材，\x01",
            "去各种地方\x01",
            "品尝食物吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "既然如此，\x01",
            "我就给你们切成可以\x01",
            "一口吃下的小块吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x102,
        "#00100F呵呵，拜托您了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0311
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人品尝了精力牛排。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0312
    ChrTalk(
        0x104,
        (
            "#00309F（嚼嚼）……\x01",
            "哎呀，虽说只有一口大小，\x01",
            "但还是相当有分量呢。\x02\x03",

            "#00304F牛排果然就\x01",
            "应该这样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x109,
        (
            "#10102F嗯，吃完之后，\x01",
            "确实感到体力充沛呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x8,
        (
            "呵呵，对于矿工们来说，\x01",
            "体力就是生命啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x8,
        (
            "只要有这个和啤酒，\x01",
            "大家就可以像老黄牛\x01",
            "一样拼命工作了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0316
    ChrTalk(
        0x105,
        (
            "#10306F矿工的工作\x01",
            "果然很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，但冈兹先生他们\x01",
            "好像却乐在其中呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "呵呵，他们可是矿山镇的\x01",
            "刚强男子汉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x8,
        (
            "你们想大吃\x01",
            "一顿的时候，\x01",
            "就再来我们店吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x104,
        "#00300F好，我们会的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2, 0)
    SetScenarioFlags(0x173, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_6C4F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_6C6C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_6C7F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_6C92")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_6CAF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_6CC2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_6CDF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_6CF2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_6D0F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_6D22")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_6D3F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D3F")

    OP_29(0x80, 0x1, 0x8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E1A")
    SetChrName("")
    Sound(17, 0, 100, 0)
    Sound(9, 0, 100, 0)

    #A0321
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在六家饮食店完成了取材！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E11")

    #A0322
    AnonymousTalk(
        0x101,
        (
            "#00003F现在就可以去向\x01",
            "格蕾丝小姐报告了……\x02\x03",

            "#00000F不过，还没有把六个人\x01",
            "喜欢的美食全部找到。\x01",
            "不如再努努力吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6E11")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_6E1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6EDD")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "找到了特别任务支援科\x01",
            "全体成员各自喜欢的美食。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0324
    AnonymousTalk(
        0x101,
        (
            "#00000F这样一来，已经找到\x01",
            "所有人喜欢的美食了啊。\x02\x03",

            "取材工作已经足够了，\x01",
            "马上去通讯社报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_6EDD")

    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3700, 0, 2090, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_35_6701 end

    def Function_36_6F0D(): pass

    label("Function_36_6F0D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(3290, 1500, 1670, 0)
    MoveCamera(52, 28, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33630, 0)
    SetChrPos(0x101, 3250, 0, 1590, 0)
    SetChrPos(0x102, 4210, 0, 1500, 0)
    SetChrPos(0x103, 2730, 0, 570, 0)
    SetChrPos(0x109, 2780, 0, -510, 0)
    SetChrPos(0x104, 3820, 0, 430, 0)
    SetChrPos(0x105, 4200, 0, -450, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0325
    ChrTalk(
        0x8,
        (
            "#3P哟，这不是之前来过的\x01",
            "警察小弟吗～\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        (
            "#3P你们今天\x01",
            "是来住宿的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        (
            "#00003F啊，我们是来\x01",
            "咨询点\x01",
            "事情的……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x102,
        (
            "#00100F请问您最近\x01",
            "有没有收到过\x01",
            "奇怪的货物呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        "#3P奇怪的货物……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0330
    ChrTalk(
        0x8,
        (
            "#3P啊！说起来，\x01",
            "确实收到过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x8,
        (
            "#3P那种东西为什么\x01",
            "会送到我们这里啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        (
            "#3P你们是不是\x01",
            "了解什么情况？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x104,
        "#00300F果然有货物错送到这里了啊。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#00003F嗯，其实……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0335
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德向对方说明了\x01",
            "送错货物的情况。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0336
    ChrTalk(
        0x8,
        (
            "#3P哈哈，\x01",
            "原来是这么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x8,
        (
            "#3P也就是说，那些货物\x01",
            "本来是要送到\x01",
            "乌尔斯拉医院的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#3P难怪会是满满一包\x01",
            "手术刀之类的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x103,
        (
            "#00200F突然收到那种东西，\x01",
            "肯定会大吃一惊吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x8,
        "#3P那当然，真是吓了一跳呢。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x8,
        (
            "#3P琉卡觉得很可怕，\x01",
            "还想明天当作\x01",
            "垃圾扔掉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x109,
        "#10106F还、还真是千钧一发啊……\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        (
            "#00000F这才是应该送到\x01",
            "您这里的货物，\x01",
            "请收下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '易碎品的小包裹'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('易碎品的小包裹', 1)

    #C0345
    ChrTalk(
        0x8,
        (
            "#3P哦，谢谢啦。\x01",
            "我看看……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x8,
        (
            "#3P……没错，\x01",
            "这是我之前订购的\x01",
            "利贝尔制造的玻璃杯。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "#3P的确是应该寄到\x01",
            "我们店的货物。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        "#00309F那就好。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x105,
        (
            "#10300F那么，能不能把误发到\x01",
            "您这里的货物交给我们呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x8,
        (
            "#3P当然没问题，\x01",
            "稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    OP_95(0x8, 3700, 0, 6080, 2000, 0x0)
    OP_0D()
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_95(0x8, 3700, 0, 4290, 2000, 0x0)
    OP_0D()

    #C0351
    ChrTalk(
        0x8,
        (
            "#3P之前送来的货物就是这个，\x01",
            "那就交给你们啦。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0352
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沉重货物'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沉重货物', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0353
    ChrTalk(
        0x101,
        "#00004F非常感谢。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0354
    ChrTalk(
        0x101,
        (
            "#00000F……好，接下来，\x01",
            "就去乌尔斯拉医院吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x103,
        (
            "#00200F最好先到接待处\x01",
            "打听一下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x175, 6)
    OP_29(0x85, 0x1, 0x1)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3700, 0, 2090, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_36_6F0D end

    def Function_37_75C9(): pass

    label("Function_37_75C9")

    EventBegin(0x0)
    Fade(500)
    OP_68(103580, 3500, 1840, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    SetChrPos(0x101, 104410, 2000, 2730, 180)
    SetChrPos(0x102, 105590, 2000, 2850, 225)
    SetChrPos(0x103, 103990, 2000, 3850, 180)
    SetChrPos(0x109, 105160, 2000, 3900, 180)
    SetChrPos(0x104, 104700, 2000, 5020, 180)
    SetChrPos(0x105, 103250, 2000, 4800, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0356
    ChrTalk(
        0x101,
        "#00005F尼尔森先生。\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x101, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7738")
    Jump("loc_7782")

    label("loc_7738")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7758")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7782")

    label("loc_7758")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7778")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7782")

    label("loc_7778")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7782")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0357
    ChrTalk(
        0xE,
        "唔，这声音……是罗伊德警官啊。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        "#00000F是的，您还记得我啊，真是荣幸。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xE,
        (
            "呵呵，毕竟是曾经\x01",
            "采访过的人，\x01",
            "我不可能忘记你的声音。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x103,
        "#00205F（难道这个人就是……）\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x104,
        (
            "#00300F（嗯，好像是之前\x01",
            "  采访过罗伊德他们的\x01",
            "  那位著名记者。）\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x109,
        "#10100F（嗯，是尼尔森先生。）\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#00100F您今天怎么\x01",
            "来玛因兹了？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xE,
        (
            "哦，我准备采访一下\x01",
            "这里的镇长先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xE,
        (
            "关于该镇开采七耀石的历史，\x01",
            "以及近代的各种变化，\x01",
            "我想听听镇长的看法。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xE,
        (
            "大家如今都在探讨独立的利弊，\x01",
            "我认为在这种时候更应该\x01",
            "将目光聚焦于自治州的历史。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x105,
        "#10304F呼，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x109,
        (
            "#10100F该怎么说呢，\x01",
            "着眼点真是与众不同呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xE,
        (
            "哈哈，所以我总是\x01",
            "事倍功半呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xE,
        (
            "对了，听说在不久前召开的通商会议中，\x01",
            "各位在抓捕恐怖分子时有很大贡献。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xE,
        (
            "……啊。\x01",
            "如果各位方便的话，\x01",
            "能否再次接受我的采访呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xE,
        (
            "在通商会议的过程中发生恐怖事件，\x01",
            "这到底意味着什么——\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xE,
        (
            "通过与各位探讨，\x01",
            "说不定可以阐明其中的隐情。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x102,
        "#00105F恐怖事件的『隐情』……\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x103,
        "#00208F可是……\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        (
            "#00000F嗯，虽然很失礼，\x01",
            "但这件事关系到\x01",
            "自治州政府和警察局的机密。\x02\x03",

            "我们能说的\x01",
            "内容很有限……\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xE,
        "我当然明白这一点。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xE,
        (
            "但我仍然觉得与你们探讨\x01",
            "一定会很有意义……\x01",
            "各位意下如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        (
            "#00003F这个……\x02\x03",

            "（上次的采访确实\x01",
            "  对我们也很有益处。）\x02\x03",

            "#00008F（如果时间允许，\x01",
            "  还是接受为好……）\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    Return()

    # Function_37_75C9 end

    def Function_38_7C65(): pass

    label("Function_38_7C65")

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
            "接受尼尔森的采访\x01",      # 0
            "放弃\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7CCB"),
        (1, "loc_7D89"),
        (SWITCH_DEFAULT, "loc_7E49"),
    )


    label("loc_7CCB")


    #C0380
    ChrTalk(
        0x101,
        (
            "#00000F明白了，\x01",
            "我们接受您的采访。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xE,
        "非常感谢。\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xE,
        "那我们就马上开始吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0383
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【关于恐怖事件的协助采访】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x89, 0x4, 0x2)
    Call(0, 40)
    Jump("loc_7E49")

    label("loc_7D89")


    #C0384
    ChrTalk(
        0x101,
        (
            "#00006F不好意思，\x01",
            "现在实在是抽不出时间……\x02\x03",

            "可以稍后再谈吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xE,
        "好的，没问题。\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xE,
        (
            "各位方便的时候，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E41")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 104410, 2000, 2730, 180)
    EventEnd(0x5)

    label("loc_7E41")

    SetScenarioFlags(0x177, 7)
    Jump("loc_7E49")

    label("loc_7E49")

    Return()

    # Function_38_7C65 end

    def Function_39_7E4A(): pass

    label("Function_39_7E4A")

    TalkBegin(0xE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7EDE")
    Jump("loc_7F28")

    label("loc_7EDE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7EFE")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F28")

    label("loc_7EFE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F1E")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F28")

    label("loc_7F1E")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F28")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0387
    ChrTalk(
        0xE,
        "……是罗伊德警官啊。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xE,
        (
            "可以接受我关于\x01",
            "恐怖事件的采访吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Call(0, 38)
    TalkEnd(0xE)
    Return()

    # Function_39_7E4A end

    def Function_40_7F98(): pass

    label("Function_40_7F98")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrSubChip(0xE, 0x0)
    OP_68(102190, 3600, 1510, 0)
    MoveCamera(49, 21, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(32220, 0)
    SetChrPos(0x101, 102650, 2150, 3330, 180)
    SetChrPos(0x102, 101250, 2150, 1740, 90)
    SetChrPos(0x103, 102610, 2150, -110, 0)
    SetChrPos(0x109, 103400, 2000, 4800, 180)
    SetChrPos(0x104, 102060, 2000, 4800, 180)
    SetChrPos(0x105, 100750, 2000, 3680, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0389
    ChrTalk(
        0xE,
        (
            "#11P感谢大家\x01",
            "配合我的采访。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xE,
        (
            "#11P这次采访的主题\x01",
            "是发生在通商会议\x01",
            "过程中的恐怖事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xE,
        (
            "#11P首先，作为前提，\x01",
            "我想确认一下\x01",
            "恐怖组织的身份……\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xE,
        "#11P罗伊德警官，你自然了解吧？\x02",
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0393
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K在通商会议的过程中发动袭击的恐怖组织是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "埃雷波尼亚帝国的帝国解放战线\x01",        # 0
            "卡尔瓦德共和国的移民政策反对派\x01",      # 1
            "以上两者\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8239"),
        (1, "loc_82EC"),
        (2, "loc_839F"),
        (SWITCH_DEFAULT, "loc_8470"),
    )


    label("loc_8239")


    #C0394
    ChrTalk(
        0x101,
        (
            "#00001F#5P嗯，是埃雷波尼亚帝国的\x01",
            "『帝国解放战线』。\x02\x03",

            "#00011F（……慢着，\x01",
            "  不只这一个吧？）\x02\x03",

            "#00003F此外还有卡尔瓦德共和国的\x01",
            "移民政策反对派——\x01",
            "『反移民政策主义』组织。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8470")

    label("loc_82EC")


    #C0395
    ChrTalk(
        0x101,
        (
            "#00001F#5P嗯，是卡尔瓦德共和国的\x01",
            "移民政策反对派——\x01",
            "『反移民政策主义』组织。\x02\x03",

            "#00011F（……慢着，\x01",
            "  不只这一个吧？）\x02\x03",

            "#00003F此外还有埃雷波尼亚帝国的\x01",
            "『帝国解放战线』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8470")

    label("loc_839F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0396
    ChrTalk(
        0x101,
        (
            "#00006F#5P嗯，犯罪团伙是分别来自\x01",
            "两大国的两个恐怖组织。\x02\x03",

            "#00008F其中之一是埃雷波尼亚帝国的\x01",
            "『帝国解放战线』。\x02\x03",

            "#00013F另一个则是卡尔瓦德共和国的\x01",
            "移民政策反对派——\x01",
            "『反移民政策主义』组织。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8470")

    label("loc_8470")


    #C0397
    ChrTalk(
        0xE,
        "#11P不错，正是这两个恐怖组织。\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xE,
        (
            "#11P关于他们的背景与主张，\x01",
            "就没必要在这里提及了……\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xE,
        (
            "#11P问题的关键在于，\x01",
            "平时毫无往来的两个组织\x01",
            "是如何结成统一战线的。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xE,
        (
            "#11P有传闻说，过去曾在利贝尔\x01",
            "暗中活动的组织『噬身之蛇』\x01",
            "给他们提供了协助……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0401
    ChrTalk(
        0x101,
        (
            "#00013F#5P结社『噬身之蛇』……\x02\x03",

            "#00008F（说起来，那些恐怖分子\x01",
            "  在通商会议时还\x01",
            "  动用了智能兵器呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x102,
        (
            "#00108F#6P尼尔森先生，\x01",
            "您知道『结社』的事情？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xE,
        (
            "#11P是的，但我只是知道\x01",
            "这个神秘组织确实存在而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xE,
        (
            "#11P各位果然\x01",
            "也知道啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x104,
        "#00306F#5P嗯，但了解的信息非常少。\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x103,
        (
            "#00211F#6P而且，知道的越多，\x01",
            "就越觉得谜团重重……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xE,
        (
            "#11P……不管怎么说，那确实是一个\x01",
            "不可思议的集团，我们甚至连其\x01",
            "行动目的都不清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xE,
        (
            "#11P关于他们的意图，\x01",
            "我们目前还无法推论，\x01",
            "暂且保留意见吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        "#00006F#5P嗯，我也赞成。\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xE,
        "#11P那么，我们继续说下去吧。\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xE,
        (
            "#11P我接下来想要确认的是——\x01",
            "在这次的恐怖事件中，\x01",
            "两大国表现出的意向与立场。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xE,
        (
            "#11P根据我得到的情报，两国事先\x01",
            "就已暗中准备了外部的实战部队。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xE,
        (
            "#11P据说他们在解决恐怖事件的过程中\x01",
            "做出了很大的贡献。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xE,
        (
            "#11P不难发现，两大国早已掌握了\x01",
            "恐怖分子的动向，但却有意放纵他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xE,
        (
            "#11P两位首脑的目的究竟是什么呢？\x01",
            "罗伊德警官，你有何看法？\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)

    label("loc_895C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8C94")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0416
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K在恐怖事件中，奥斯本宰相\x01",
            "和洛克史密斯总统的目的是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "引出恐怖组织\x01",          # 0
            "牵制国内的反对派\x01",      # 1
            "迫使迪塔市长辞职\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8A2D"),
        (1, "loc_8ABB"),
        (2, "loc_8BBB"),
        (SWITCH_DEFAULT, "loc_8C81"),
    )


    label("loc_8A2D")


    #C0417
    ChrTalk(
        0x101,
        (
            "#00005F#5P（他们的目的\x01",
            "  难道是引出恐怖组织……？）\x02\x03",

            "#00006F（……不对，两国原本\x01",
            "  就对恐怖分子的实际情况\x01",
            "  有一定程度的了解。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8C81")

    label("loc_8ABB")


    #C0418
    ChrTalk(
        0x101,
        (
            "#00003F#5P恐怖分子的幕后主使者\x01",
            "是现执政者的反对派。\x02\x03",

            "我想，两位首脑的目的\x01",
            "就是牵制他们。\x02\x03",

            "#00008F奥斯本宰相想牵制\x01",
            "敌对的贵族势力。\x02\x03",

            "#00001F而洛克史密斯总统则想抑制\x01",
            "在国内兴风作浪的危险分子。\x01",
            "这就应该是他们的首要目的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8BB3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BB3")

    SetScenarioFlags(0x1, 1)
    Jump("loc_8C81")

    label("loc_8BBB")


    #C0419
    ChrTalk(
        0x101,
        (
            "#00008F#5P（通过那起恐怖事件，再次证明了\x01",
            "  自治州在安保方面的不足。）\x02\x03",

            "（两大国企图对这个问题穷追不舍，\x01",
            "  迫使迪塔市长下台……）\x02\x03",

            "#00011F（不对不对，那起事件\x01",
            "  并没有严重到那种程度。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_8C81")

    label("loc_8C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8C8F")
    Jump("loc_8C94")

    label("loc_8C8F")

    Jump("loc_895C")

    label("loc_8C94")


    #C0420
    ChrTalk(
        0xE,
        (
            "#11P唔，确实如你所说。\x01",
            "我认为那正是\x01",
            "他们的最大目的。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xE,
        (
            "#11P实际上，自从事件发生之后，\x01",
            "两国内部对那些反对势力的\x01",
            "谴责之声日渐高涨。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x103,
        (
            "#00203F#6P原来如此，在政治斗争中，\x01",
            "那确实是再好不过的攻击材料了。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xE,
        (
            "#11P顺便一说，罗伊德警官，\x01",
            "你刚才说的是『首要目的』……\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xE,
        (
            "#11P如果可以，能否把你想到的\x01",
            "其它目的也说给我听呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x101,
        "#00011F#5P这个……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    #C0426
    ChrTalk(
        0x102,
        "#00108F#6P罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x109,
        "#10108F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(300)

    #C0428
    ChrTalk(
        0x101,
        (
            "#00006F#5P另一个重要目的……\x02\x03",

            "#00013F我认为是为了正式构筑起\x01",
            "进驻克洛斯贝尔的路径。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xE,
        "#11P唔……\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x105,
        (
            "#10303F#6P进驻克洛斯贝尔……\x02\x03",

            "#10301F最显而易见的表现，\x01",
            "就是两大国在通商会议中\x01",
            "提出的军队驻留提案吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x103,
        (
            "#00203F#6P两大国认为，通过那起恐怖事件，\x01",
            "再次证明了克洛斯贝尔在安保方面的不足。\x02\x03",

            "#00201F按照他们的说法，为了解决这一问题，\x01",
            "那项提案是很有必要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x102,
        (
            "#00106F#6P是的，经过那起事件，\x01",
            "签署于利贝尔的《互不侵犯条约》的约束力\x01",
            "已经大幅度降低了……\x02\x03",

            "#00108F再加上独立提案的影响，\x01",
            "两大国的舆论现在都很\x01",
            "关注克洛斯贝尔的动向。\x02\x03",

            "#00101F就结果而言，确实起到了缓解\x01",
            "国内的对立状况、转移不满情绪等作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x103,
        "#00205F#6P竟然算计得如此深远……\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x104,
        (
            "#00306F#5P唉～他们到底想\x01",
            "一举几得啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xE,
        (
            "#11P……唔，各位的见解\x01",
            "果然很深刻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xE,
        (
            "#11P那么，这个话题就到这里，\x01",
            "我们进入最后一个重点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xE,
        (
            "#11P单凭表面状况也不难看出，\x01",
            "在此次事件中，两国之间\x01",
            "明显存在着事先协定……\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xE,
        (
            "#11P这是否意味着，\x01",
            "两国已经结成了同盟关系呢？\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)

    label("loc_91F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9446")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0439
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K通过共同处理恐怖事件这一契机，\x01",
            "帝国和共和国是否已结成了同盟关系？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "暂时结成了同盟关系\x01",      # 0
            "永久结成了同盟关系\x01",      # 1
            "不可能\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_92D1"),
        (1, "loc_9332"),
        (2, "loc_93B3"),
        (SWITCH_DEFAULT, "loc_9433"),
    )


    label("loc_92D1")


    #C0440
    ChrTalk(
        0x101,
        (
            "#00008F#5P（暂时的……\x01",
            "  这样能说得通吗？）\x02\x03",

            "#00003F（不，事情\x01",
            "  并没有那么简单。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_9433")

    label("loc_9332")


    #C0441
    ChrTalk(
        0x101,
        (
            "#00005F#5P（难道说，他们借此机会，\x01",
            "  结成了永久同盟的关系？）\x02\x03",

            "#00006F（——怎么可能！\x01",
            "  那种事情是不可能发生的。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9433")

    label("loc_93B3")


    #C0442
    ChrTalk(
        0x101,
        (
            "#5P#00003F不……\x01",
            "我想这是不可能的。\x02\x03",

            "#00013F因为两大国的最终目的\x01",
            "都是独自支配克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_942B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_942B")

    SetScenarioFlags(0x1, 1)
    Jump("loc_9433")

    label("loc_9433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_9441")
    Jump("loc_9446")

    label("loc_9441")

    Jump("loc_91F4")

    label("loc_9446")


    #C0443
    ChrTalk(
        0xE,
        "#11P不错，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xE,
        (
            "#11P他们仅仅是在此次事件中\x01",
            "步调一致而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xE,
        (
            "#11P克洛斯贝尔是一片\x01",
            "过于繁荣的缓冲地带。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xE,
        (
            "#11P两大国在暗中相互试探，\x01",
            "企图确认这片极其重要的特殊土地\x01",
            "究竟会落入哪一方的手中。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x109,
        "#10113F#5P这……\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x102,
        "#00108F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x103,
        "#00211F#6P……实在太露骨了呢。\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x105,
        (
            "#10306F#6P就是说，这只是真正开战\x01",
            "之前的准备工作而已吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xE,
        (
            "#11P嗯，两国之间的\x01",
            "谍报战，今后想必会\x01",
            "越发激化。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xE,
        (
            "#11P在那种情况下，\x01",
            "犯罪组织和猎兵团\x01",
            "应该也会随之活跃起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xE,
        (
            "#11P一旦如此，过去时而\x01",
            "发生的那种神秘事故，\x01",
            "说不定将会再次出现。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0454
    ChrTalk(
        0x104,
        "#00305F#5P神秘事故……？\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x103,
        "#00205F#6P那是什么……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0456
    ChrTalk(
        0xE,
        (
            "#11P没什么，我好像说了\x01",
            "一些多余的话。\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7121", 0)
    Sleep(1000)

    #C0457
    ChrTalk(
        0xE,
        (
            "#11P这真是一次很有意义的谈话，\x01",
            "让我把很多事情都梳理清楚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xE,
        "#11P非常感谢各位的帮助。\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        "#00003F#5P……不，我们才应该道谢。\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x102,
        (
            "#00100F#6P通过和您的交流，\x01",
            "我们似乎也大致理清了情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x109,
        "#10106F#5P……真是受教了。\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xE,
        "#11P听各位这样说，我非常高兴。\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xE,
        (
            "#11P如果今后有机会，\x01",
            "请大家再陪我谈谈吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        "#00000F#5P好的，一定。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0465
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【关于恐怖事件的协助采访】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 104500, 2000, 3740, 180)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_996F")
    OP_2C(0x89, 0x2)
    Jump("loc_9983")

    label("loc_996F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9983")
    OP_2C(0x89, 0x1)

    label("loc_9983")

    OP_29(0x89, 0x1, 0x0)
    OP_29(0x89, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_40_7F98 end

    SaveToFile()

Try(main)
