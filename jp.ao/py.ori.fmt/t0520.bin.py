from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ノーマ",                 # 1
        "リュッカ",               # 2
        "カルロス",               # 3
        "鉱山長ホフマン",         # 4
        "鉱員ガンツ",             # 5
        "鉱員マックス",           # 6
        "ニールセン",             # 7
        "鉱員マルロ",             # 8
        "ミレイユ三尉",           # 9
        "エステル",               # 10
        "ヨシュア",               # 11
        "ヨルグ老人",             # 12
        "レン",                   # 13
        "遊撃士リン",             # 14
        "遊撃士エオリア",         # 15
        "遊撃士スコット",         # 16
        "グレイス",               # 17
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
        "Function_5_90C",          # 05, 5
        "Function_6_910",          # 06, 6
        "Function_7_1BE6",         # 07, 7
        "Function_8_2A3C",         # 08, 8
        "Function_9_2B6C",         # 09, 9
        "Function_10_2D22",        # 0A, 10
        "Function_11_2E1B",        # 0B, 11
        "Function_12_2F4B",        # 0C, 12
        "Function_13_30FE",        # 0D, 13
        "Function_14_3254",        # 0E, 14
        "Function_15_3309",        # 0F, 15
        "Function_16_3B02",        # 10, 16
        "Function_17_3C2F",        # 11, 17
        "Function_18_41EE",        # 12, 18
        "Function_19_454D",        # 13, 19
        "Function_20_4A35",        # 14, 20
        "Function_21_4BF1",        # 15, 21
        "Function_22_4BF5",        # 16, 22
        "Function_23_4D1D",        # 17, 23
        "Function_24_4F10",        # 18, 24
        "Function_25_507A",        # 19, 25
        "Function_26_51FA",        # 1A, 26
        "Function_27_5E84",        # 1B, 27
        "Function_28_5F70",        # 1C, 28
        "Function_29_5F8C",        # 1D, 29
        "Function_30_5FBC",        # 1E, 30
        "Function_31_5FEC",        # 1F, 31
        "Function_32_6008",        # 20, 32
        "Function_33_604C",        # 21, 33
        "Function_34_6090",        # 22, 34
        "Function_35_74D7",        # 23, 35
        "Function_36_7E0D",        # 24, 36
        "Function_37_861F",        # 25, 37
        "Function_38_8DEB",        # 26, 38
        "Function_39_9038",        # 27, 39
        "Function_40_9194",        # 28, 40
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
            "★赤レンガ亭・イチオシのレシピ★\x01",
            "　　～定番だけど\x01",
            "　　　フライドフィッシュ～\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フライドフィッシュのレシピが書かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_908")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_908")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『フライドフィッシュ』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_908")

    TalkEnd(0xFF)
    Return()

    # Function_4_7F2 end

    def Function_5_90C(): pass

    label("Function_5_90C")

    Call(0, 6)
    Return()

    # Function_5_90C end

    def Function_6_910(): pass

    label("Function_6_910")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_93E")
    Call(0, 35)
    Return()

    label("loc_93E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_967")
    Call(0, 36)
    Return()

    label("loc_967")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_974")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE2")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "休憩をする\x01",        # 2
            "やめる\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_9E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A07")
    OP_AF(0x52)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BDD")

    label("loc_A07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A27")
    OP_AF(0x50)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BDD")

    label("loc_A27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3B")
    Jump("loc_1BDD")

    label("loc_A3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A53")
    TalkEnd(0x8)
    Return()

    label("loc_A53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BDD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_B02")

    #C0004
    ChrTalk(
        0x8,
        (
            "フフ、鉱山町名物の\x01",
            "ステーキを食べれば、\x01",
            "たちまち力が湧いてくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "あんたたちも、\x01",
            "ガッツリ食べたい時は\x01",
            "またウチに来るんだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDD")

    label("loc_B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C06")

    #C0006
    ChrTalk(
        0x8,
        (
            "街での騒ぎのあと、\x01",
            "疲れ果てた様子の遊撃士たちと、\x01",
            "泣きはらした顔の女の子が来てね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "彼らもクロスベル市での\x01",
            "解放作戦に参加したらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "レジスタンスに協力してた\x01",
            "あたしたちとしては、是非とも\x01",
            "労ってあげたいところだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CB2")

    label("loc_C06")


    #C0009
    ChrTalk(
        0x8,
        (
            "下で休んでる遊撃士たちは、\x01",
            "クロスベル市での\x01",
            "解放作戦に参加したらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "さっき別の遊撃士さんも来て\x01",
            "魔獣退治を手伝ってくれたし……\x01",
            "本当に彼らには世話になるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB2")

    Jump("loc_1BDD")

    label("loc_CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_DE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D79")

    #C0011
    ChrTalk(
        0x8,
        (
            "今、レジスタンスのリーダー\x01",
            "ミレイユさんが補給に来てるとこだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "あんたたち、近々\x01",
            "大きな作戦をやるんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "あたし達も応援してるよ。\x01",
            "気張っていくんだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DDD")

    label("loc_D79")


    #C0014
    ChrTalk(
        0x8,
        (
            "あんたたち、近々\x01",
            "大きな作戦をやるんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "あたし達も応援してるよ。\x01",
            "気張っていくんだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDD")

    Jump("loc_1BDD")

    label("loc_DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFB")
    TurnDirection(0x8, 0x104, 0)

    #C0016
    ChrTalk(
        0x8,
        (
            "ランディ、レジスタンスから\x01",
            "一度離れたんだってね？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#00304Fああ、助けてやらなきゃならん\x01",
            "愛娘が待ってるんでな。\x02\x03",

            "#00302Fオバちゃん、しばらくの間\x01",
            "マインツの奴らと一緒に\x01",
            "ミレイユたちを頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "はは、了解だ。\x01",
            "あんたも気をつけるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 7)
    Jump("loc_107E")

    label("loc_EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100A")

    #C0019
    ChrTalk(
        0x8,
        (
            "レジスタンスの子達には、\x01",
            "山岳地帯のいい隠れ場所を教えたり、\x01",
            "食糧や薬の補給を手伝ったり……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "国防軍の連中が捜索に来ても\x01",
            "徹底的にしらんぷりしてやったり、\x01",
            "とまあ色々手伝ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "大したことじゃないけど、\x01",
            "出来る限りの事はしてあげないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_107E")

    label("loc_100A")


    #C0022
    ChrTalk(
        0x8,
        (
            "レジスタンスには\x01",
            "頑張って欲しいものだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "大した手伝いはできないけど、\x01",
            "出来る限りの事はしてあげないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107E")

    Jump("loc_1BDD")

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119D")

    #C0024
    ChrTalk(
        0x8,
        (
            "あの武装集団の連中は、\x01",
            "結局町の人間や食料なんかには\x01",
            "一切手をつけなかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "恐ろしい目にあったことには\x01",
            "変わりないけど、大きな被害が出た\x01",
            "警備隊に比べたらマシかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "……しかし、何が目的だったのかねえ。\x01",
            "本当にワケが分からないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11EE")

    label("loc_119D")


    #C0027
    ChrTalk(
        0x8,
        (
            "武装集団の連中……\x01",
            "何が目的だったのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "本当にワケが分からないよ。\x02",
    )

    CloseMessageWindow()

    label("loc_11EE")

    Jump("loc_1BDD")

    label("loc_11F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1265")

    #C0029
    ChrTalk(
        0x8,
        "うーん、心地いい雨だねえ。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "こんな日は\x01",
            "夜のお客も少なくなるし、\x01",
            "ノンビリしてるとするかね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDD")

    label("loc_1265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_152C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1362")

    #C0031
    ChrTalk(
        0x8,
        (
            "リベール製のグラス、\x01",
            "ちゃんと届いてよかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "間違えて届いた荷物に\x01",
            "メスやら何やらが入ってたときは\x01",
            "本当にギョッとしたもんさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "ハハ、とにかくあんたたちも\x01",
            "ご苦労だったね。\x01",
            "礼を言わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1410")

    label("loc_1362")


    #C0034
    ChrTalk(
        0x8,
        (
            "ちょっと前に注文した\x01",
            "リベール製のグラス、\x01",
            "ちゃんと届いてよかったよ。\x02\x03",

            "本当にギョッとしたもんさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "ハハ、とにかくあんたたちも\x01",
            "ご苦労だったね。\x01",
            "礼を言わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1410")

    Jump("loc_1527")

    label("loc_1415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D9")

    #C0036
    ChrTalk(
        0x8,
        (
            "マルロさん、\x01",
            "ようやく元気になったらしいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "リュッカの慰め方は、\x01",
            "ハタから見ても物凄く\x01",
            "素っ気無かったもんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "まあ、本人がそれで\x01",
            "元気がでたならいいってことさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1527")

    label("loc_14D9")


    #C0039
    ChrTalk(
        0x8,
        (
            "ま、これでマルロさんも\x01",
            "元気になったみたいだし……\x01",
            "ひとまず一件落着かね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1527")

    Jump("loc_1BDD")

    label("loc_152C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161A")

    #C0040
    ChrTalk(
        0x8,
        (
            "最近、マルロさんは\x01",
            "リュッカに嫌われたと\x01",
            "思いこんでるらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "酒場にも顔を出さないし、\x01",
            "仕事にも身が入らなくて\x01",
            "困ってるらしいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "リュッカ本人に自覚がないから\x01",
            "微妙な話になってるのよねえ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16A9")

    label("loc_161A")


    #C0043
    ChrTalk(
        0x8,
        (
            "でも、ガンツさんも\x01",
            "いいところあるじゃないか。\x01",
            "友達のために直談判なんてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "まー、相手があのリュッカだから\x01",
            "苦戦してるみたいだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A9")

    Jump("loc_1BDD")

    label("loc_16AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_17DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1784")

    #C0045
    ChrTalk(
        0x8,
        (
            "マルロさん、昨日はリュッカに\x01",
            "酔いに任せてアプローチを\x01",
            "かけてたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "完膚なきまでに無視されて、\x01",
            "すっかり撃沈しちゃったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "……くふふ、みてて面白かったけど。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17D9")

    label("loc_1784")


    #C0048
    ChrTalk(
        0x8,
        "マルロさんもかわいそうにね。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "どれ、今度おつまみでも\x01",
            "サービスしてやるかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D9")

    Jump("loc_1BDD")

    label("loc_17DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_18F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1867")

    #C0050
    ChrTalk(
        0x8,
        (
            "今日は鉱員連中が休みでね。\x01",
            "昼間っから飲みに来てるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "よかったら、あんたらも\x01",
            "飲んでったらどうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18EB")

    label("loc_1867")


    #C0052
    ChrTalk(
        0x8,
        (
            "やれやれ、\x01",
            "鉱山が休みっつっても\x01",
            "ほんと休む暇がないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "ふふ、まあそれが楽しくて\x01",
            "この商売やってるような\x01",
            "もんなんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18EB")

    Jump("loc_1BDD")

    label("loc_18F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A15")

    #C0054
    ChrTalk(
        0x8,
        (
            "昨日、リュッカが酔っ払って\x01",
            "けらけらと笑い上戸を披露してたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "あの子は普段ブアイソだけど、\x01",
            "実は笑うととっても可愛くてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "どうもマルロさんがそれに気づいて、\x01",
            "すっかりホレちまったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "くふふ、色恋沙汰は大好物さ。\x01",
            "これからどうなるのかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A95")

    label("loc_1A15")


    #C0058
    ChrTalk(
        0x8,
        (
            "マルロさんは、昨日の宴会で\x01",
            "リュッカにホレちまったみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "くふふ、色恋沙汰は大好物さ。\x01",
            "これからどうなるのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A95")

    Jump("loc_1BDD")

    label("loc_1A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1BDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B77")

    #C0060
    ChrTalk(
        0x8,
        (
            "あいよ、いらっしゃい。\x01",
            "遠いところからよく来たね。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "ウチは鉱員たち御用達でね、\x01",
            "腹いっぱい食べてもらえる\x01",
            "メニューが目白押しさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "大盛りにしてあげるから、\x01",
            "よかったら何か食べておいき。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BDD")

    label("loc_1B77")


    #C0063
    ChrTalk(
        0x8,
        (
            "せっかく来たんだ、\x01",
            "よかったら何か食べておいき。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "腹いっぱいになれるメニューが\x01",
            "目白押しだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDD")

    Jump("loc_974")

    label("loc_1BE2")

    TalkEnd(0x8)
    Return()

    # Function_6_910 end

    def Function_7_1BE6(): pass

    label("Function_7_1BE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D02")

    #C0065
    ChrTalk(
        0x9,
        (
            "ガンツさんもマルロさんも、\x01",
            "嬉々として鉱山に出かけていったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "どうせ今夜は再開記念の宴会でも\x01",
            "やるつもりなんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        "……やれやれ、面倒くさいわね。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "でも、外があんな状況だし\x01",
            "以前と変わらないものがあるのは\x01",
            "なんだか安心するわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D8B")

    label("loc_1D02")


    #C0069
    ChrTalk(
        0x9,
        (
            "外があんな状況だし、\x01",
            "以前と変わらないものがあるのは\x01",
            "なんだか安心するわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "……ま、今夜はせっかくだから\x01",
            "私も楽しむとしますか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8B")

    Jump("loc_2A38")

    label("loc_1D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9A")

    #C0071
    ChrTalk(
        0x9,
        (
            "あのリーダーさんって、\x01",
            "すごく芯が強い人よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "間違った体制に\x01",
            "真っ先に異を唱えるなんて、\x01",
            "男でも出来ることじゃないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "あの姿勢には、女として\x01",
            "見習うべき所が多そうだわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E92")

    #C0074
    ChrTalk(
        0x109,
        "#10104Fええ……本当にそう思います。\x02",
    )

    CloseMessageWindow()

    label("loc_1E92")

    SetScenarioFlags(0x0, 1)
    Jump("loc_1F2B")

    label("loc_1E9A")


    #C0075
    ChrTalk(
        0x9,
        (
            "間違った体制に\x01",
            "真っ先に異を唱えるなんて、\x01",
            "男でも出来ることじゃないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "あのリーダーさんの姿勢には、\x01",
            "女として見習うべき所が多そうだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F2B")

    Jump("loc_2A38")

    label("loc_1F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2180")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2047")

    #C0077
    ChrTalk(
        0x9,
        (
            "あたし、こないだから\x01",
            "続きものの小説を読んでるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "こんな状況だから\x01",
            "続刊が入荷されてこないし、\x01",
            "しばらく読むのはやめようかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        "……よかったら、あげるわ。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F9, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 3)
    Jump("loc_217B")

    label("loc_2047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F6")

    #C0081
    ChrTalk(
        0x9,
        (
            "ガンツさんもマルロさんも、\x01",
            "ここ最近は昼間から通ってるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "……まー、鉱山が閉鎖された上\x01",
            "街にも出れない今の状況じゃ、\x01",
            "仕方ないのかもしれないけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_217B")

    label("loc_20F6")


    #C0083
    ChrTalk(
        0x9,
        (
            "鉱山が閉鎖された上、\x01",
            "移動制限で街にも行けないんじゃ\x01",
            "昼間から飲みたくもなるわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "はあ……\x01",
            "面倒だけど、付き合ってあげよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_217B")

    Jump("loc_2A38")

    label("loc_2180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2276")

    #C0085
    ChrTalk(
        0x9,
        (
            "町が占領されたとき……\x01",
            "私は店の隅で震えてることしか\x01",
            "出来なかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "でも、マルロさんがずっと\x01",
            "大丈夫だ、きっと助かるって\x01",
            "励ましてくれてて……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "……頼りない人だと思ってたけど、\x01",
            "ちょっとだけ見直しちゃった。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2301")

    label("loc_2276")


    #C0088
    ChrTalk(
        0x9,
        (
            "あの時は……\x01",
            "いつもみたいに悪態をつく事すら\x01",
            "できないほど怖かったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "……励ましてくれたマルロさんには\x01",
            "感謝しないといけないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2301")

    Jump("loc_2A38")

    label("loc_2306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_238C")

    #C0090
    ChrTalk(
        0x9,
        (
            "雨の日ってニガテなのよね。\x01",
            "床が濡れて掃除も面倒だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "カルロスさんもさっさと食べて、\x01",
            "帰ってくれないかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A38")

    label("loc_238C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2498")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2453")

    #C0092
    ChrTalk(
        0x9,
        (
            "……結局昨日のは\x01",
            "なんだったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "ガンツさんに頼まれた通り、\x01",
            "『元気だせば？』って\x01",
            "言っただけだったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "まー、どうでもいっか。\x01",
            "さっさと掃除掃除……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2493")

    label("loc_2453")


    #C0095
    ChrTalk(
        0x9,
        "……ふあ～、だるぅ……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        "さっさと掃除すませちゃおっと。\x02",
    )

    CloseMessageWindow()

    label("loc_2493")

    Jump("loc_2A38")

    label("loc_2498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B3")
    Call(0, 8)
    Jump("loc_2542")

    label("loc_24B3")

    OP_4B(0xC, 0xFF)

    #C0097
    ChrTalk(
        0x9,
        "まあ、そうね……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "ガンツさんが\x01",
            "溜まったツケを払うなら\x01",
            "やったげてもいいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xC,
        (
            "え゛……いやそれはその、\x01",
            "別の話というか……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_2542")

    Jump("loc_2A38")

    label("loc_2547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_26B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2659")

    #C0100
    ChrTalk(
        0x9,
        (
            "マルロさん、なんだか\x01",
            "昨日は変だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "やたらと私に話しかけてきて、\x01",
            "『一緒に飲まない？』とか\x01",
            "誘ってくるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "鬱陶しいから完全にスルーしたら、\x01",
            "今日は妙に落ち込んでるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "ったく、どうしろっていうのよ。\x01",
            "ほんと面倒くさいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26B0")

    label("loc_2659")


    #C0104
    ChrTalk(
        0x9,
        (
            "ったく、昨日のマルロさんは\x01",
            "ほんと面倒くさかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        "これだから酔っ払いは……\x02",
    )

    CloseMessageWindow()

    label("loc_26B0")

    Jump("loc_2A38")

    label("loc_26B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_27C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2764")

    #C0106
    ChrTalk(
        0x9,
        (
            "休みだからって\x01",
            "よくもまあ昼間っから\x01",
            "お酒を飲む気になるわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "私は飲んだらすぐ酔って\x01",
            "記憶失くしちゃうから、\x01",
            "いまいち良さが分かんないわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27C4")

    label("loc_2764")


    #C0108
    ChrTalk(
        0x9,
        (
            "よくもまあ昼間っから\x01",
            "お酒を飲む気になるわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "……ま、いっか。\x01",
            "みんな楽しそうだし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C4")

    Jump("loc_2A38")

    label("loc_27C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_28F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2896")

    #C0110
    ChrTalk(
        0x9,
        "あー頭いたい……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "昨日は、鉱員たちの宴会に\x01",
            "付き合わされちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "ついうっかり飲めないお酒を\x01",
            "飲んじゃって、記憶が全然ないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        "……私、何かしなかったかしら。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28F4")

    label("loc_2896")


    #C0114
    ChrTalk(
        0x9,
        (
            "あー、頭いたい……\x01",
            "昨日の記憶も全然ないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "……私、余計な事を\x01",
            "してないでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F4")

    Jump("loc_2A38")

    label("loc_28F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2A38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29AB")

    #C0116
    ChrTalk(
        0x9,
        (
            "この間、またガンツさんが\x01",
            "ギャンブルにボロ負けしてきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "前みたいにグチグチと\x01",
            "愚痴らなくなったのはいいけど……\x01",
            "……あの人も懲りないわよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A38")

    label("loc_29AB")


    #C0118
    ChrTalk(
        0x9,
        (
            "ガンツさん、最近は\x01",
            "ギャンブルで負けてきても\x01",
            "グチグチと愚痴らなくなったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "……負けたら負けたで、\x01",
            "ツケで飲むのはどうかと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A38")

    TalkEnd(0xFE)
    Return()

    # Function_7_1BE6 end

    def Function_8_2A3C(): pass

    label("Function_8_2A3C")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0120
    ChrTalk(
        0xC,
        (
            "なっリュッカちゃん。\x01",
            "頼むよ、このとーり！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "あのね、ガンツさん。\x01",
            "なんで私がわざわざマルロさんを\x01",
            "励まさないといけないわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "彼が最近元気ないのは、\x01",
            "私には関係ない話でしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xC,
        (
            "い、いや、どちらかというと\x01",
            "大アリっつーかなんつーか……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        "……意味分かんないんだけど。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_8_2A3C end

    def Function_9_2B6C(): pass

    label("Function_9_2B6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B7D")
    Jump("loc_2D1E")

    label("loc_2B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C56")

    #C0125
    ChrTalk(
        0xA,
        (
            "今日は七耀石の運搬を\x01",
            "朝のうちに済ませておいたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "雨がひどくなって\x01",
            "地面がぬかるんだら、\x01",
            "タイヤが取られて大変だからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "危険の少ない時間を選ぶのも\x01",
            "運転技術のうちってわけさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CCA")

    label("loc_2C56")


    #C0128
    ChrTalk(
        0xA,
        (
            "今日は七耀石の運搬を\x01",
            "朝のうちに済ませておいたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "危険の少ない時間を選ぶのも\x01",
            "運転技術のうちってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CCA")

    Jump("loc_2D1E")

    label("loc_2CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2CDD")
    Jump("loc_2D1E")

    label("loc_2CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CEB")
    Jump("loc_2D1E")

    label("loc_2CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2CF9")
    Jump("loc_2D1E")

    label("loc_2CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D07")
    Jump("loc_2D1E")

    label("loc_2D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D15")
    Jump("loc_2D1E")

    label("loc_2D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2D1E")

    label("loc_2D1E")

    TalkEnd(0xFE)
    Return()

    # Function_9_2B6C end

    def Function_10_2D22(): pass

    label("Function_10_2D22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D33")
    Jump("loc_2E17")

    label("loc_2D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D41")
    Jump("loc_2E17")

    label("loc_2D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D4F")
    Jump("loc_2E17")

    label("loc_2D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D5D")
    Jump("loc_2E17")

    label("loc_2D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D6B")
    Jump("loc_2E17")

    label("loc_2D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D86")
    Call(0, 11)
    Jump("loc_2DFB")

    label("loc_2D86")


    #C0130
    ChrTalk(
        0xB,
        (
            "叱るときはキチっと\x01",
            "叱ってやらねえと、\x01",
            "子供のタメにならねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xB,
        (
            "甘やかすばかりが\x01",
            "親の仕事じゃねえってこった。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DFB")

    Jump("loc_2E17")

    label("loc_2E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E0E")
    Jump("loc_2E17")

    label("loc_2E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2E17")

    label("loc_2E17")

    TalkEnd(0xFE)
    Return()

    # Function_10_2D22 end

    def Function_11_2E1B(): pass

    label("Function_11_2E1B")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0132
    ChrTalk(
        0xD,
        (
            "しかし、昨日の鉱山長の\x01",
            "剣幕にはビックリしたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        (
            "俺らに怒るのと同じ調子で\x01",
            "アレクを怒っちまうんだもんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        (
            "叱るときはキチっと\x01",
            "叱ってやらねえと、\x01",
            "子供のためになんねえからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xB,
        (
            "おめえも親になれば\x01",
            "俺の気持ちが\x01",
            "きっと分かるだろうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xD,
        "そういうもんかねえ……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 7)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_11_2E1B end

    def Function_12_2F4B(): pass

    label("Function_12_2F4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F5C")
    Jump("loc_30FA")

    label("loc_2F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2F6A")
    Jump("loc_30FA")

    label("loc_2F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2FF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F85")
    Call(0, 13)
    Jump("loc_2FED")

    label("loc_2F85")


    #C0137
    ChrTalk(
        0xC,
        (
            "こんな状況だから\x01",
            "昼間から酒ってのも\x01",
            "気分が乗らねえんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xC,
        "あー、カジノに行きてえよぉ……\x02",
    )

    CloseMessageWindow()

    label("loc_2FED")

    Jump("loc_30FA")

    label("loc_2FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3000")
    Jump("loc_30FA")

    label("loc_3000")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_300E")
    Jump("loc_30FA")

    label("loc_300E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_301C")
    Jump("loc_30FA")

    label("loc_301C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3037")
    Call(0, 8)
    Jump("loc_30C2")

    label("loc_3037")


    #C0139
    ChrTalk(
        0xC,
        (
            "（とりあえずリュッカちゃんが\x01",
            "  慰めてくれりゃ、マルロも\x01",
            "  元気が出るはずなんだ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xC,
        (
            "（なんとしてもＯＫを\x01",
            "  もらわねえとな……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C2")

    Jump("loc_30FA")

    label("loc_30C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_30D5")
    Jump("loc_30FA")

    label("loc_30D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_30E3")
    Jump("loc_30FA")

    label("loc_30E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_30F1")
    Jump("loc_30FA")

    label("loc_30F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_30FA")

    label("loc_30FA")

    TalkEnd(0xFE)
    Return()

    # Function_12_2F4B end

    def Function_13_30FE(): pass

    label("Function_13_30FE")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0141
    ChrTalk(
        0xC,
        (
            "あーあ……こんな状況じゃ\x01",
            "街のカジノにも遊びに行けねえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xC,
        "いつまでこんな生活が続くのかねえ。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xF,
        (
            "娯楽がないってのは\x01",
            "やっぱり辛いものがあるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xF,
        (
            "かといって、鉱山は閉まってて\x01",
            "仕事に打ち込むこともできないし。\x02",
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
        "はあー……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xF,
        "ため息しか出ないよな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_13_30FE end

    def Function_14_3254(): pass

    label("Function_14_3254")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3265")
    Jump("loc_3305")

    label("loc_3265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3273")
    Jump("loc_3305")

    label("loc_3273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3281")
    Jump("loc_3305")

    label("loc_3281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_328F")
    Jump("loc_3305")

    label("loc_328F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_329D")
    Jump("loc_3305")

    label("loc_329D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B8")
    Call(0, 11)
    Jump("loc_32E9")

    label("loc_32B8")


    #C0147
    ChrTalk(
        0xD,
        (
            "うーん、親ってのも\x01",
            "なかなか難しいんだなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32E9")

    Jump("loc_3305")

    label("loc_32EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32FC")
    Jump("loc_3305")

    label("loc_32FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3305")

    label("loc_3305")

    TalkEnd(0xFE)
    Return()

    # Function_14_3254 end

    def Function_15_3309(): pass

    label("Function_15_3309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B01")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_34D1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_34B6")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33BE")
    Jump("loc_3408")

    label("loc_33BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33DE")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3408")

    label("loc_33DE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33FE")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3408")

    label("loc_33FE")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3408")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0148
    ChrTalk(
        0xFE,
        (
            "皆さん、本日も私の取材に\x01",
            "付き合っていただいて\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "また機会があれば、\x01",
            "お話できればと思います。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_34CC")

    label("loc_34B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 7)), scpexpr(EXPR_END)), "loc_34C8")
    Call(0, 39)
    Return()

    label("loc_34C8")

    Call(0, 37)
    Return()

    label("loc_34CC")

    Jump("loc_3B01")

    label("loc_34D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3999")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3579")
    Jump("loc_35C3")

    label("loc_3579")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3599")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35C3")

    label("loc_3599")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35B9")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35C3")

    label("loc_35B9")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_35C3")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3904")

    #C0150
    ChrTalk(
        0x101,
        "#00000Fニールセンさん――\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0151
    ChrTalk(
        0xFE,
        "ふむ、その声はロイドさんですね。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "今日はどうしてマインツの方に？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#00000Fええ、巡回のついでに\x01",
            "立ち寄ったって所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        (
            "#00100Fニールセンさんの方は、\x01",
            "取材でいらしたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "ええ、実はここの町長さんに\x01",
            "取材をさせて頂く予定でしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "この町の七耀石採掘の歴史と\x01",
            "近代における推移について、\x01",
            "お話を伺うつもりなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "独立の是非が問われている\x01",
            "今だからこそ、改めて自治州の歴史に\x01",
            "焦点を当てておこうと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x103,
        "#00200Fへえ、それは……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x109,
        (
            "#10100Fなんというか、\x01",
            "目の付け所が違いますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "はは、おかげでいつも\x01",
            "遠回りばかりしていますけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "しかし、皆さんも\x01",
            "相変わらずお忙しそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "今後も色々大変だと思いますが、\x01",
            "どうか頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        "#00000Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16B, 5)
    Jump("loc_398D")

    label("loc_3904")


    #C0164
    ChrTalk(
        0xFE,
        (
            "さてと、取材の時間までは\x01",
            "まだ余裕があるので私はここで\x01",
            "のんびりさせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "ふふ、ここは静かで\x01",
            "落ち着けるいい部屋ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_398D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_3B01")

    label("loc_3999")

    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A2D")
    Jump("loc_3A77")

    label("loc_3A2D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A4D")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A77")

    label("loc_3A4D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A6D")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A77")

    label("loc_3A6D")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A77")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0166
    ChrTalk(
        0xFE,
        (
            "ふふ、ここは静かで\x01",
            "落ち着けるいい部屋ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "取材の時間まで\x01",
            "のんびりできそうです。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_3B01")

    Return()

    # Function_15_3309 end

    def Function_16_3B02(): pass

    label("Function_16_3B02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B13")
    Jump("loc_3C2B")

    label("loc_3B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3B21")
    Jump("loc_3C2B")

    label("loc_3B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3C2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B3C")
    Call(0, 13)
    Jump("loc_3C2B")

    label("loc_3B3C")

    SetChrSubChip(0xF, 0x2)

    #C0168
    ChrTalk(
        0xF,
        (
            "（最初はリュッカちゃんに会えるから\x01",
            "  そこまで悪くないかとも思ったけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xF,
        (
            "（酒場に入り浸ってるのって\x01",
            "  あんまり印象はよくないよな……）\x02",
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
        "（……なに見てんのかしら。）\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x10E, 0x0)
    SetChrSubChip(0xF, 0x0)

    label("loc_3C2B")

    TalkEnd(0xFE)
    Return()

    # Function_16_3B02 end

    def Function_17_3C2F(): pass

    label("Function_17_3C2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C40")
    Jump("loc_41EA")

    label("loc_3C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_41E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4092")

    #C0171
    ChrTalk(
        0x10,
        (
            "#07901Fランディ、支援課の皆さん……\x01",
            "話は聞かせてもらったわ。\x02\x03",

            "#07903F独立宣言が無効となった今、\x01",
            "少なくとも大統領が国防軍を\x01",
            "自由に動かす事はできないはず。\x02\x03",

            "#07901Fあとは街を包み込む\x01",
            "《結界》さえ消えれば……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x103,
        (
            "#00200Fクロスベル市を解放する\x01",
            "最大のチャンス、ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#00000F結界の方は、俺たちで\x01",
            "何とか消してみせます。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#00303Fだが、当然《赤い星座》も\x01",
            "その事態には備えてるはずだ。\x02\x03",

            "#00301F下手すりゃ作戦を決行する前に\x01",
            "本格的なレジスタンス狩りが\x01",
            "始まるかもしれねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        "#00103F急いだほうがよさそうね……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x10,
        (
            "#07903Fとにかく、今は作戦開始に向けて\x01",
            "万全の準備を整えておくわ。\x02\x03",

            "神狼たちの助けも借りられるし、\x01",
            "前よりは《赤い星座》とも\x01",
            "いい勝負が出来ると思う。\x02\x03",

            "#07901Fだから、結界の方は\x01",
            "どうかよろしく頼むわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x104,
        (
            "#00304Fああ、任せとけ。\x02\x03",

            "#00301F……気をつけろよ、ミレイユ。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FF7")
    Jump("loc_4041")

    label("loc_3FF7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4017")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4041")

    label("loc_4017")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4037")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4041")

    label("loc_4037")

    OP_52(0x10, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4041")

    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x10)

    #C0178
    ChrTalk(
        0x10,
        "#07902Fええ、そっちもね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 0)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_41DC")

    label("loc_4092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_416E")

    #C0179
    ChrTalk(
        0x10,
        (
            "#07903Fとにかく、今は作戦開始に向けて\x01",
            "万全の準備を整えておくわ。\x02\x03",

            "神狼たちの助けも借りられるし、\x01",
            "前よりは《赤い星座》とも\x01",
            "いい勝負が出来ると思う。\x02\x03",

            "#07901Fあなたたちは結界の方を\x01",
            "よろしく頼むわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_41DC")

    label("loc_416E")


    #C0180
    ChrTalk(
        0x10,
        (
            "#07903F今は作戦開始に向けて\x01",
            "万全の準備を整えておくわ。\x02\x03",

            "#07901Fあなたたちは結界の方を\x01",
            "よろしく頼むわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41DC")

    Jump("loc_41EA")

    label("loc_41E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_41EA")

    label("loc_41EA")

    TalkEnd(0xFE)
    Return()

    # Function_17_3C2F end

    def Function_18_41EE(): pass

    label("Function_18_41EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_449C")

    #C0181
    ChrTalk(
        0x11,
        (
            "#00802F#30W……ロイド君たち。\x01",
            "くれぐれも気を付けてね。\x02\x03",

            "#00808F頑張るのはいいけど、\x01",
            "《パテル＝マテル》みたいに\x01",
            "なっちゃダメだからね？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        "#00000Fああ……分かってる。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x104,
        (
            "#00308F考えてみりゃ、俺らにとっても\x01",
            "命の恩人だったんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x103,
        (
            "#00203F……前に工房を訪ねた時に\x01",
            "もっと話しておけば良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x11,
        (
            "#00808F#30Wうん……あたしも\x01",
            "もっと話しておけばよかった。\x02",
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
            "#00804F#30W……レンのことは\x01",
            "どうか心配しないで。\x02\x03",

            "#00800Fここ半年、色々な経験をして\x01",
            "本当の意味で強くなってきてるし……\x02\x03",

            "#00802F大切な友だちもいるから\x01",
            "きっと乗り越えられると思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        "#00004Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        (
            "#00100F……目を覚ましたら\x01",
            "よろしく言っておいてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_4549")

    label("loc_449C")


    #C0189
    ChrTalk(
        0x11,
        (
            "#00804F#30Wレンのことは心配しないで。\x02\x03",

            "#00800Fここ半年、色々な経験をして\x01",
            "本当の意味で強くなってきてるし……\x02\x03",

            "#00802F大切な友だちもいるから\x01",
            "きっと乗り越えられると思う。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4549")

    TalkEnd(0xFE)
    Return()

    # Function_18_41EE end

    def Function_19_454D(): pass

    label("Function_19_454D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4990")

    #C0190
    ChrTalk(
        0x12,
        (
            "#00903F#30W……既にノバルティス博士も\x01",
            "この地を去ったみたいだね。\x02\x03",

            "#00901F今回は《結社》がこれ以上、\x01",
            "敵に回らないのは助かるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#00001F正直、何を狙っているのか\x01",
            "こちらでは判らなかったんだ。\x02\x03",

            "#00003F帝国方面で何かを\x01",
            "企んでいるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x12,
        (
            "#00903F#30W……『幻焔計画』だね。\x02\x03",

            "#00901Fクロスベルの事件を発端にした\x01",
            "大規模な計画みたいだけど……\x02\x03",

            "#00908F……オリビエさんたちが心配だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x103,
        "#00205Fオリビエさんというと……\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x104,
        "#00303Fあのオリヴァルト皇子の事か。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x12,
        (
            "#00903F#30Wええ、帝国で内戦が始まって以来、\x01",
            "連絡が取れなくなってしまって。\x02\x03",

            "#00908Fミュラーさんが付いている限り、\x01",
            "滅多な事はないと思うんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        "#00108Fそれでも心配ですね……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_498B")
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0197
    ChrTalk(
        0x12,
        (
            "#00900F#30Wそうだ、君たち……\x01",
            "これを受け取ってくれないか？\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x394, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 3)

    #C0199
    ChrTalk(
        0x101,
        "#00005Fこれは……？\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x12,
        (
            "#00900F#30W《パテル＝マテル》の最期を\x01",
            "看取った場所に落ちていたんだ。\x02\x03",

            "#00903F……多分、『神機』の\x01",
            "部品の一部だと思う。\x01",
            "何かの役に立つかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#00000F分かった……\x01",
            "ありがたくもらっておくよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_498B")

    Jump("loc_4A31")

    label("loc_4990")


    #C0202
    ChrTalk(
        0x12,
        (
            "#00903F#30Wあの《碧の大樹》……\x02\x03",

            "リベールに出現した浮遊都市#8Rリベル＝アーク#よりも\x01",
            "規模としては上回っていると思う。\x02\x03",

            "#00900Fどうか、くれぐれも気を付けて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A31")

    TalkEnd(0xFE)
    Return()

    # Function_19_454D end

    def Function_20_4A35(): pass

    label("Function_20_4A35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B3C")

    #C0203
    ChrTalk(
        0x13,
        (
            "#03900F《パテル＝マテル》の思考ユニットは\x01",
            "本来、あれほどの自律行動を\x01",
            "取れるようには設計されていなかった。\x02\x03",

            "レンと出会ったことで彼もまた\x01",
            "“心”を手に入れたということか……\x02\x03",

            "#03903F……人形師となって数十年。\x01",
            "いまだ学ばされることが多いな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_4BED")

    label("loc_4B3C")


    #C0204
    ChrTalk(
        0x13,
        (
            "#03900F……今回の件、レンにとっては\x01",
            "逆に良い方向に働くかもしれん。\x02\x03",

            "#03903F過去に経験できなかった“別れ”を\x01",
            "本当の意味で経験したのだから……\x02\x03",

            "#03900F全てはこれからだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BED")

    TalkEnd(0xFE)
    Return()

    # Function_20_4A35 end

    def Function_21_4BF1(): pass

    label("Function_21_4BF1")

    Call(0, 22)
    Return()

    # Function_21_4BF1 end

    def Function_22_4BF5(): pass

    label("Function_22_4BF5")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB8")

    #C0205
    ChrTalk(
        0x14,
        (
            "#03317F#2S#40W………パテル＝マテル…………\x02\x03",

            "#2S#40W……どうして………\x01",
            "…………どうしてレンを………\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        "#00008F……レン…………\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x102,
        "#00103F……そっとしておきましょう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_4D19")

    label("loc_4CB8")


    #C0208
    ChrTalk(
        0x14,
        "#03317F#2S#40W………パパ………ママ…………\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レンは泣き疲れて眠ってしまっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_4D19")

    TalkEnd(0x14)
    Return()

    # Function_22_4BF5 end

    def Function_23_4D1D(): pass

    label("Function_23_4D1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E6C")

    #C0210
    ChrTalk(
        0xFE,
        (
            "エオリアと一緒に、\x01",
            "占領事件のアフターケアに\x01",
            "当たっていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "周辺に出ていた手配魔獣も\x01",
            "退治できたし、とりあえずは\x01",
            "安心……と言いたい所だけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "マインツの人々が受けた\x01",
            "心の傷は相当なものみたいでね。\x01",
            "不安で夜も眠れない人も多い。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "ミシェルに相談して、\x01",
            "もう少し滞在期間を\x01",
            "延ばした方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_4F0C")

    label("loc_4E6C")


    #C0214
    ChrTalk(
        0xFE,
        (
            "マインツの人々が受けた\x01",
            "心の傷は相当なものみたいでね。\x01",
            "不安で夜も眠れない人も多い。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "ミシェルに相談して、\x01",
            "もう少し滞在期間を\x01",
            "延ばした方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F0C")

    TalkEnd(0xFE)
    Return()

    # Function_23_4D1D end

    def Function_24_4F10(): pass

    label("Function_24_4F10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF2")

    #C0216
    ChrTalk(
        0xFE,
        (
            "あの襲撃事件のせいで、\x01",
            "ウルスラ病院もずっと手一杯みたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "だから、マインツで治療できる患者は\x01",
            "出来るだけ私が請け負っているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "相当大変だけど……こういう時は\x01",
            "ちゃんと役割分担をしなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_5076")

    label("loc_4FF2")


    #C0219
    ChrTalk(
        0xFE,
        (
            "マインツで治療できる患者は\x01",
            "出来るだけ私が請け負っているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "こういう時は、医師免許をとっていて\x01",
            "本当に良かったって思うわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5076")

    TalkEnd(0xFE)
    Return()

    # Function_24_4F10 end

    def Function_25_507A(): pass

    label("Function_25_507A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5161")

    #C0221
    ChrTalk(
        0xFE,
        (
            "今日は相棒のヴェンツェルと\x01",
            "別行動をとっていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "エステルたちが抜けた穴を\x01",
            "カバーするために、こういう\x01",
            "変則的なシフトも増えているのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "魔獣退治の時とかは苦労するけど、\x01",
            "なんとかやってかないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_51F6")

    label("loc_5161")


    #C0224
    ChrTalk(
        0xFE,
        (
            "今日は相棒のヴェンツェルと\x01",
            "別行動をとっていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "魔獣退治の時とかは苦労するけど、\x01",
            "人手不足をカバーするためにも\x01",
            "なんとかやってかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F6")

    TalkEnd(0xFE)
    Return()

    # Function_25_507A end

    def Function_26_51FA(): pass

    label("Function_26_51FA")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5342")
    BeginChrThread(0x109, 1, 0, 27)
    WaitChrThread(0x109, 1)
    Sleep(600)

    label("loc_5342")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_535F")
    BeginChrThread(0x105, 1, 0, 27)
    WaitChrThread(0x105, 1)
    Sleep(600)

    label("loc_535F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_537C")
    BeginChrThread(0x106, 1, 0, 27)
    WaitChrThread(0x106, 1)
    Sleep(600)

    label("loc_537C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5399")
    BeginChrThread(0x10A, 1, 0, 27)
    WaitChrThread(0x10A, 1)
    Sleep(600)

    label("loc_5399")

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
        "#12P#00805F#30Wあ、ロイド君たち……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x12,
        "#12P#00902F#30W……やあ………\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        "#5P#00005Fエステル、ヨシュア！？\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x102,
        "#5P#00102Fこちらに来てたんですか……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)

    #C0230
    ChrTalk(
        0x104,
        (
            "#5P#00300F聞いたぜ、あのデカブツ人形を\x01",
            "見事ブッ飛ばしたそうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x103,
        (
            "#5P#00202Fさすがはエステルさんたちと\x01",
            "《パテル＝マテル》ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x11,
        "#12P#00802F#30Wあはは……\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x12,
        (
            "#12P#00903F#30W……まあ、勝てたのは全部、\x01",
            "“彼”の犠牲のおかげだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        "#5P#00005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x102,
        "#5P#00105Fそういえば……レンちゃんは？\x02",
    )

    CloseMessageWindow()

    #N0236
    NpcTalk(
        0x13,
        "老人の声",
        "……レンなら眠っておる。\x02",
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

    def lambda_5729():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5729)
    Sleep(50)

    def lambda_5739():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5739)
    Sleep(50)

    def lambda_5749():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5749)
    Sleep(50)

    def lambda_5759():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5759)
    Sleep(50)

    def lambda_5769():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_5769)
    Sleep(50)

    def lambda_5779():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_5779)
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
        "#00005Fヨルグ・マイスター！\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x103,
        "#00203F……いらしてたんですか。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x13,
        (
            "#11P#03903Fうむ……彼らの連絡を受けてな。\x02\x03",

            "#03900F大変な事が起きているようだが\x01",
            "《パテル＝マテル》が逝ったとあらば\x01",
            "顔を出さないわけにもいくまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        "#00105Fあの人形が、逝った……？\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#00305Fオイオイ、ひょっとして……\x02",
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
            "#12P#00808F#30W……うん……\x01",
            "あのデッカイ人形を持ち上げて\x01",
            "そのまま空に運んで……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x12,
        (
            "#12P#00908F#30W……多分……\x01",
            "自爆装置を起動させたんだろう。\x02\x03",

            "#00903Fそれも自分自身の判断で。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        "#5P#00003F……そうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x103,
        "#5P#00208F機械がそんな判断を……\x02",
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
            "#11P#03317F#2S#40W………グス…………\x01",
            "…………パテル＝マテル…………\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x104,
        "#00305F泣き疲れて眠っちまったのか……\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        (
            "#00103F……無理もないわ……\x01",
            "あんなに心が通じ合っていたし……\x02",
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
            "#11P#03903F……《パテル＝マテル》については\x01",
            "運命と諦めるしかあるまい。\x02\x03",

            "#03900Fわしとしては、この子を守るため\x01",
            "身を投げ打った彼の“心”を\x01",
            "尊重してやりたいと思う。\x02\x03",

            "人形師冥利に尽きるというものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        "#00001Fマイスター……\x02",
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
            "#12P#00801F#30W──話は聞いたわ。\x01",
            "大変な事になってるんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x12,
        (
            "#12P#00900F#30W僕たちも回復しだい、\x01",
            "助太刀させてもらうつもりだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#5P#00004Fありがとう、２人とも。\x02\x03",

            "#00000Fでも、今は身体を休めることを\x01",
            "最優先にしてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#5P#00303F嬢ちゃんの人形じゃねえが……\x02\x03",

            "#00300F今は俺たちがキー坊のために\x01",
            "全力を尽くすべき時だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x11,
        "#12P#00802F#30Wそっか……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x12,
        (
            "#12P#00904F#30W……女神の加護を。\x01",
            "くれぐれも気を付けて。\x02",
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

    # Function_26_51FA end

    def Function_27_5E84(): pass

    label("Function_27_5E84")

    SetChrPos(0xFE, 94200, 0, 6500, 180)

    def lambda_5E9A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5E9A)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ECA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 28)
    Jump("loc_5F6F")

    label("loc_5ECA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EEE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 29)
    Jump("loc_5F6F")

    label("loc_5EEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F12")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 30)
    Jump("loc_5F6F")

    label("loc_5F12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F36")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 31)
    Jump("loc_5F6F")

    label("loc_5F36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F5A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 32)
    Jump("loc_5F6F")

    label("loc_5F5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F6F")
    BeginChrThread(0xFE, 2, 0, 33)

    label("loc_5F6F")

    Return()

    # Function_27_5E84 end

    def Function_28_5F70(): pass

    label("Function_28_5F70")

    OP_95(0xFE, 94200, 0, 3030, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_5F70 end

    def Function_29_5F8C(): pass

    label("Function_29_5F8C")

    OP_95(0xFE, 94200, 0, 4850, 2000, 0x0)
    OP_95(0xFE, 93110, 0, 3070, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_29_5F8C end

    def Function_30_5FBC(): pass

    label("Function_30_5FBC")

    OP_95(0xFE, 94200, 0, 4850, 2000, 0x0)
    OP_95(0xFE, 95280, 0, 3120, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_30_5FBC end

    def Function_31_5FEC(): pass

    label("Function_31_5FEC")

    OP_95(0xFE, 94210, 0, 4150, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_31_5FEC end

    def Function_32_6008(): pass

    label("Function_32_6008")

    OP_95(0xFE, 94260, 0, 5260, 2000, 0x0)
    OP_95(0xFE, 93580, 0, 4960, 2000, 0x0)
    OP_95(0xFE, 93270, 0, 4310, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_6008 end

    def Function_33_604C(): pass

    label("Function_33_604C")

    OP_95(0xFE, 94260, 0, 5260, 2000, 0x0)
    OP_95(0xFE, 95020, 0, 4960, 2000, 0x0)
    OP_95(0xFE, 95250, 0, 4350, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_604C end

    def Function_34_6090(): pass

    label("Function_34_6090")

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
            "#00306F#11P──なるほど。\x01",
            "そりゃまたとんでもない\x01",
            "話になってるみたいだな。\x02\x03",

            "#00301Fそれも、あのキー坊が……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x18,
        (
            "#02106F#5Pうーん、突拍子が無さすぎて\x01",
            "記事にも書けない感じだけど……\x02\x03",

            "#02101Fロイド君たちは何としても\x01",
            "彼女を取り戻すつもりなのね？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        "#00001F#6Pええ、勿論です。\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        "#00203F#6P言うまでもないかと。\x02",
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
            "#07904F#11P……ランディ。\x01",
            "私たち#6Rレジスタンス#の方は大丈夫よ。\x02\x03",

            "#07902F元々、支援課の仲間たちを\x01",
            "助け出すという条件で\x01",
            "力を貸してくれたんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x10, 500)

    #C0264
    ChrTalk(
        0x104,
        "#00305F#5Pいや、それは……\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        "#00008F#6P……そうだったのか。\x02",
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
            "#10404F#6Pま、こちらとしては\x01",
            "君に合流してもらえると\x01",
            "助かるのは確かだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x10,
        (
            "#07904F#11P元々、私たちの抵抗活動は\x01",
            "国防軍に納得しきれなかった\x01",
            "警備隊員としての意地よ。\x02\x03",

            "#07902F警備隊から離れた貴方は\x01",
            "仲間たちの力になるべきだわ。\x02\x03",

            "#07909F今後は、あの狼さんたちも\x01",
            "力になってくれそうだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x107,
        (
            "#01203F#6P#3Cうむ、おぬしらに協力するよう\x01",
            "改めて伝えておいた。\x02\x03",

            "#01200F山岳地での戦いならば\x01",
            "力になってくれるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x104,
        "#00306F#5P……悪い、助かる。\x02",
    )

    CloseMessageWindow()

    def lambda_6609():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6609)
    Sleep(50)

    def lambda_6619():
        OP_93(0x10, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6619)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x10, 0)

    #C0271
    ChrTalk(
        0x104,
        (
            "#00300F#11Pロイド、ティオすけ。\x01",
            "俺も付き合わせてもらうぜ！\x02\x03",

            "支援課のメンバーとして、\x01",
            "キー坊の保護者としてな！\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        "#00002F#6Pああ……！\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x103,
        "#00204F#6P……良かった。\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x106,
        "#10709F#5Pふふ……心強いです。\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x18,
        (
            "#02103F#5Pうーん、そうなると。\x02\x03",

            "#02102Fあたしもあなた達に\x01",
            "同行させてもらおっかな？\x02",
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

    def lambda_67F4():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67F4)
    Sleep(50)

    def lambda_6804():
        TurnDirection(0x103, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6804)
    Sleep(50)

    def lambda_6814():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6814)
    Sleep(50)

    def lambda_6824():
        TurnDirection(0x105, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6824)
    Sleep(50)

    def lambda_6834():
        TurnDirection(0x106, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6834)
    Sleep(50)

    def lambda_6844():
        TurnDirection(0x10, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6844)
    Sleep(50)

    def lambda_6854():
        TurnDirection(0x107, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_6854)
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
        "#00011F#6Pへ……！？\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x103,
        "#00211F#6Pいきなり何を……？\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x18,
        (
            "#02104F#5Pだって今後の動きの中心は\x01",
            "あなた達になりそうだし。\x02\x03",

            "#02110Fジャーナリストとしては\x01",
            "ちょっと見過ごせないわね！\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        "#00012F#6Pいや、でも……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x105,
        (
            "#10406F#6Pうーん、僕は別に構わないけど。\x02\x03",

            "#10400Fマスコミの人間を乗せたら\x01",
            "アッバスがうるさいだろうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x106,
        (
            "#10706F#6P……私も記事にされたら\x01",
            "ちょっと困ります。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x18,
        (
            "#02105F#5Pあー、心配しないで。\x02\x03",

            "#02104F記事にしたいのは山々だけど\x01",
            "今はそんな状況じゃないしね。\x02\x03",

            "#02106F今のあたしは、クロスベル独立国が\x01",
            "どうなるかだけが知りたいの。\x02\x03",

            "#02101Fこの欺瞞に満ちた新体制が\x01",
            "果たして歴史に選ばれるのか#18R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲#をね。\x02",
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
        "#00005F#6P歴史に選ばれる……？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x18,
        (
            "#02103F#5Pこう言っちゃなんだけど、\x01",
            "大陸全土の混乱はかなりのものよ。\x02\x03",

            "その一因が、ディーター大統領に\x01",
            "あることは否定できないけど……\x02\x03",

            "#02101F彼が退#2Rしりぞ#いたからといって、\x01",
            "この危機が乗り越えられるかしら？\x02",
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
        "#00011F#6P……それは……\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x10,
        (
            "#07906F#12P正直……\x01",
            "難しいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x18,
        (
            "#02106F#5P実際、１００年前にカルバードが\x01",
            "民主化した時も、革命政府によって\x01",
            "相当エゲつないことが行われたそうよ。\x02\x03",

            "#02103F暗殺なんかは当たり前。\x01",
            "更にはクロスベル市襲撃に\x01",
            "近いような陰謀劇もあったみたい。\x02\x03",

            "#02101Fでもそれは現在、\x01",
            "ある程度正当化されてしまっている。\x02\x03",

            "ディーター大統領のした事だって\x01",
            "同じことが言えるんじゃないかしら？\x02",
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
        "#10708F#6P（……百年前の暗殺劇……）\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x18,
        (
            "#02106F#5Pそうは言っても、この状況が\x01",
            "正しいとはあたしも思えない。\x02\x03",

            "#02100F──だからね、確かめたいの。\x02\x03",

            "今後、クロスベルが\x01",
            "どんな道を選んでいくのか。\x02\x03",

            "そしてその選択が、\x01",
            "歴史にどう伝えられるのか。\x02\x03",

            "#02109Fあなた達に付いて行ったら\x01",
            "それが見られる気がするのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        "#00000F#6P……グレイスさん。\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x104,
        (
            "#00302F#12Pなんつーか……\x01",
            "そこまで考えてたとはねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x103,
        (
            "#00202F#6P何だかシリアスすぎて\x01",
            "別人みたいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x18,
        (
            "#02109F#5Pあはは、まあ一番の理由は\x01",
            "面白そうだからなんだけど。\x02\x03",

            "#02110Fそれに通信社の方に\x01",
            "パイプは残してあるからね。\x02\x03",

            "ひょっとしたら市内の情報なんかも\x01",
            "提供できるかもしれないわよ？\x02",
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
            "#00004F#6P──分かりました。\x01",
            "俺たちは異存ありません。\x02\x03",

            "#00000Fワジ、リーシャ。\x01",
            "そちらは構わないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x106,
        (
            "#10710F#6P私は……\x01",
            "記事にしないで頂けるのなら。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        (
            "#10404F#6Pフフ、僕も構わないよ。\x02\x03",

            "#10402Fまあアッバスを説得するのは\x01",
            "一苦労かもしれないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x18,
        (
            "#02109F#5Pサンクス、恩に着るわ！\x02\x03",

            "#02110Fよーし、みんなで気合いを入れて\x01",
            "フューリッツァ賞を狙いましょ！\x02",
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
            "#00012F#6Pいや、別にグレイスさんの\x01",
            "手伝いをするわけじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x103,
        "#00211F#6Pまあ、グレイスさんですから。\x02",
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
            "その後、ロイドたちは\x01",
            "レジスタンスに密かに協力している\x01",
            "マインツのビクセン町長に挨拶した後……\x02\x03",

            "今後の段取りを話し合ってから\x01",
            "山間部の拠点#4Rベース#に戻るミレイユたちに\x01",
            "別れを告げるのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 5)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_6090 end

    def Function_35_74D7(): pass

    label("Function_35_74D7")

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
            "おや、いらっしゃい。\x01",
            "《赤レンガ亭》によく来たね。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#00000Fすみません、\x01",
            "特務支援課の者なんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『一押しグルメ』の取材で\x01",
            "来たことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0305
    ChrTalk(
        0x8,
        (
            "ああ、あんたたちだったかい。\x01",
            "通信社の人から話は聞いてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x8,
        (
            "それじゃあ、鉱山町の名物料理\x01",
            "《スタミナステーキ》を\x01",
            "焼いてあげるとするかねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x103,
        (
            "#00206F……胃にドスンと\x01",
            "溜まりそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x8,
        (
            "ああ、あんたらは色々と\x01",
            "食べて回らなきゃ\x01",
            "いけないんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "それじゃあ\x01",
            "一口サイズに切り分けて\x01",
            "持ってくるとするかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x102,
        "#00100Fふふ、よろしくお願いします。\x02",
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
            "ロイドたちはスタミナステーキを食べた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0312
    ChrTalk(
        0x104,
        (
            "#00309Fもぐもぐ……\x01",
            "いやー、一口サイズっつっても\x01",
            "なかなか食べ応えがあるねえ。\x02\x03",

            "#00304Fやっぱステーキっつったら\x01",
            "こうじゃねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x109,
        (
            "#10102Fええ、いかにもパワーが\x01",
            "湧いてきそうですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x8,
        (
            "フフ、鉱山の連中は\x01",
            "体力が命だからねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x8,
        (
            "こいつとビールがありゃ、\x01",
            "そりゃもう馬車馬のように\x01",
            "働いてけるって寸法さ。\x02",
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
            "#10306F鉱員っていうのはやっぱり\x01",
            "キツい仕事みたいだねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        (
            "#00009Fはは、ガンツさんたちは\x01",
            "楽しんでやってるみたいだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "フフ、鉱山町の\x01",
            "屈強な男たちだからこそさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x8,
        (
            "あんたたちも、\x01",
            "ガッツリ食べたい時は\x01",
            "またウチに来るんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x104,
        "#00300Fああ、そうさせてもらうぜ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2, 0)
    SetScenarioFlags(0x173, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_7B13")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_7B30")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_7B43")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_7B56")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_7B73")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_7B86")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_7BA3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_7BB6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_7BD3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_7BE6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_7C03")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7C03")

    OP_29(0x80, 0x1, 0x8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D0C")
    SetChrName("")
    Sound(17, 0, 100, 0)
    Sound(9, 0, 100, 0)

    #A0321
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "飲食店６ヶ所の取材を終えた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7D03")

    #A0322
    AnonymousTalk(
        0x101,
        (
            "#00003Fすぐにでもグレイスさんに\x01",
            "報告に行く事はできそうだけど……\x02\x03",

            "#00000Fまだ６人全員のお気に入りが\x01",
            "見つかったわけじゃない。\x01",
            "もう少し頑張ってみるかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7D03")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_7D0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DDD")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特務支援課メンバー全員の\x01",
            "お気に入りを見つけた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0324
    AnonymousTalk(
        0x101,
        (
            "#00000Fこれで６人全員の\x01",
            "お気に入りが見つかった。\x02\x03",

            "取材はこれで十分だな。\x01",
            "さっそく通信社に報告へ行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_7DDD")

    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3700, 0, 2090, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_35_74D7 end

    def Function_36_7E0D(): pass

    label("Function_36_7E0D")

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
            "#3Pやあ、いつぞやの\x01",
            "警察の坊やたちじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        (
            "#3P今日は泊まりに\x01",
            "来てくれたのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        (
            "#00003Fええと、ちょっと\x01",
            "お尋ねしたいことが\x01",
            "あって来たんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x102,
        (
            "#00100F最近、こちらに\x01",
            "覚えのない荷物が\x01",
            "届きませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        "#3P覚えのない荷物……？\x02",
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
            "#3Pあーあー、そういえば\x01",
            "確かに届いたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x8,
        (
            "#3Pなんでまたあんなモンが\x01",
            "うちに届いたやら……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        (
            "#3Pあんたたち、\x01",
            "なにか知っているのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x104,
        "#00300F当たりみたいだな。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#00003Fえっと、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0335
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは荷物の誤配が\x01",
            "あったことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0336
    ChrTalk(
        0x8,
        (
            "#3Pハハーン、\x01",
            "そういうことだったのかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x8,
        (
            "#3Pってことは、あの荷物は\x01",
            "ウルスラ病院宛ての\x01",
            "荷物だったわけだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#3P道理でメスやらなにやらが\x01",
            "ごちゃっと入っているワケだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x103,
        (
            "#00200Fそんなものが突然届いたら\x01",
            "結構不気味ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x8,
        "#3Pそりゃあギョッとしたもんさ。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x8,
        (
            "#3Pリュッカなんか気味悪がって、\x01",
            "明日にでもゴミに出そうと\x01",
            "してたくらいだったしねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x109,
        "#10106Fそ、それは間一髪でしたね……\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        (
            "#00000F本来こちらに届けられる\x01",
            "はずだった荷物も預かってます。\x01",
            "お受け取りください。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x331),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x331, 1)

    #C0345
    ChrTalk(
        0x8,
        (
            "#3Pおお、ありがとね。\x01",
            "どれどれ……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x8,
        (
            "#3P……ああ、\x01",
            "ちょっと前に注文した\x01",
            "リベール製のグラスだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "#3Pたしかにウチ宛ての荷物\x01",
            "みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        "#00309Fそいつぁよかったぜ。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x105,
        (
            "#10300Fそれじゃ、そちらの荷物は\x01",
            "引き取らせてもらっていいかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x8,
        (
            "#3Pほいきた。\x01",
            "ちょいと待ってちょうだい。\x02",
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
            "#3P届いてた荷物はこれさ。\x01",
            "後はよろしく頼むよ。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x330),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x330, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0353
    ChrTalk(
        0x101,
        "#00004Fありがとうございました。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0354
    ChrTalk(
        0x101,
        (
            "#00000F……よし、次は\x01",
            "ウルスラ病院に向かうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x103,
        (
            "#00200F受付で事情を聞いてみると\x01",
            "いいかもしれませんね。\x02",
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

    # Function_36_7E0D end

    def Function_37_861F(): pass

    label("Function_37_861F")

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
        "#00005Fニールセンさん――\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8794")
    Jump("loc_87DE")

    label("loc_8794")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_87B4")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87DE")

    label("loc_87B4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87D4")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87DE")

    label("loc_87D4")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_87DE")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0357
    ChrTalk(
        0xE,
        "ふむ、その声はロイドさんですね。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        "#00000Fええ、覚えていて頂けて光栄です。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xE,
        (
            "ふふ、一度取材をさせて\x01",
            "頂いた方の声ですから。\x01",
            "忘れるはずがありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x103,
        "#00205F（もしかして、この人が……）\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x104,
        (
            "#00300F（ああ、前にロイドたちが\x01",
            "  取材を受けたっつう、\x01",
            "  著名なジャーナリストか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x109,
        "#10100F（はい、ニールセンさんです。）\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#00100Fあの、今日はどうしてまた\x01",
            "マインツの方へ？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xE,
        (
            "ええ、実はここの町長さんに\x01",
            "取材をさせて頂く予定でしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xE,
        (
            "この町の七耀石採掘の歴史と\x01",
            "近代における推移について、\x01",
            "お話を伺うつもりなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xE,
        (
            "独立の是非が問われている\x01",
            "今だからこそ、改めて自治州の歴史に\x01",
            "焦点を当てておこうと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x105,
        "#10304Fふぅん、なるほどね。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x109,
        (
            "#10100Fなんというか、\x01",
            "目の付け所が違いますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xE,
        (
            "はは、おかげでいつも\x01",
            "遠回りばかりしていますけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xE,
        (
            "ところで皆さんは先の通商会議で\x01",
            "テロリストの拿捕に貢献されたとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xE,
        (
            "……ふむ、そうだ。\x01",
            "よければまた、私の取材に\x01",
            "付き合って頂けないでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xE,
        (
            "通商会議におけるテロ事件に\x01",
            "一体どんな意味があったのか――\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xE,
        (
            "皆さんとお話をさせて頂くことで、\x01",
            "見えてくるものがあると思うのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x102,
        "#00105Fテロ事件の“意味”……\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x103,
        "#00208Fですがそれは……\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        (
            "#00000Fええ、失礼ですが\x01",
            "本件は自治州政府と警察の\x01",
            "機密に関わります。\x02\x03",

            "俺たちに話せることは\x01",
            "限られると思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xE,
        "勿論、それは弁えています。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xE,
        (
            "それでも、お話する意義は\x01",
            "きっとあると思うのですが……\x01",
            "いかがでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        (
            "#00003Fそうですね……\x02\x03",

            "（確かに、前回の取材は\x01",
            "  俺たちにとっても有益だった。）\x02\x03",

            "#00008F（時間があるなら、受けて\x01",
            "  おいた方が良さそうだけど……）\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    Return()

    # Function_37_861F end

    def Function_38_8DEB(): pass

    label("Function_38_8DEB")

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
            "ニールセンの取材に協力する\x01",      # 0
            "やめておく\x01",                      # 1
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
        (0, "loc_8E61"),
        (1, "loc_8F4B"),
        (SWITCH_DEFAULT, "loc_9037"),
    )


    label("loc_8E61")


    #C0380
    ChrTalk(
        0x101,
        (
            "#00000F分かりました。\x01",
            "取材の話、お受けします。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xE,
        "ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xE,
        "では早速、話を始めましょう。\x02",
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
            "クエスト【テロ事件に関する取材協力】\x07\x00",
            "を開始した！\x02",
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
    Jump("loc_9037")

    label("loc_8F4B")


    #C0384
    ChrTalk(
        0x101,
        (
            "#00006Fすみません。\x01",
            "今はちょっと時間が取れなくて……\x02\x03",

            "あとで改めて伺っても結構ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xE,
        "ええ、構いませんよ。\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xE,
        (
            "では都合が付いたら、\x01",
            "いつでも声を掛けて下さい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_902F")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 104410, 2000, 2730, 180)
    EventEnd(0x5)

    label("loc_902F")

    SetScenarioFlags(0x177, 7)
    Jump("loc_9037")

    label("loc_9037")

    Return()

    # Function_38_8DEB end

    def Function_39_9038(): pass

    label("Function_39_9038")

    TalkBegin(0xE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90CC")
    Jump("loc_9116")

    label("loc_90CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_90EC")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9116")

    label("loc_90EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_910C")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9116")

    label("loc_910C")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9116")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0387
    ChrTalk(
        0xE,
        "……ロイドさんですね。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xE,
        (
            "テロ事件に関する取材、\x01",
            "付き合って頂けますか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Call(0, 38)
    TalkEnd(0xE)
    Return()

    # Function_39_9038 end

    def Function_40_9194(): pass

    label("Function_40_9194")

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
            "#11P取材に付き合って頂き、\x01",
            "どうもありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xE,
        (
            "#11P今回の取材テーマは、\x01",
            "先の通商会議中に発生した\x01",
            "テロ事件についてです。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xE,
        (
            "#11Pまずは前提として、\x01",
            "犯人であるテロ集団について\x01",
            "確認しておきたいのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xE,
        "#11Pロイドさん、当然ご存知ですね？\x02",
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
            "#1K通商会議を狙ったテロリスト集団とは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "エレボニア帝国の帝国解放戦線\x01",          # 0
            "カルバード共和国の移民政策反対派\x01",      # 1
            "その両方\x01",                              # 2
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
        (0, "loc_947F"),
        (1, "loc_9548"),
        (2, "loc_9611"),
        (SWITCH_DEFAULT, "loc_96EE"),
    )


    label("loc_947F")


    #C0394
    ChrTalk(
        0x101,
        (
            "#00001F#5Pええ、エレボニア帝国の\x01",
            "『帝国解放戦線』ですね。\x02\x03",

            "#00011F（――って、\x01",
            "  それだけじゃないだろ。）\x02\x03",

            "#00003Fさらに、カルバード共和国の\x01",
            "移民政策反対派――\x01",
            "『反移民政策主義』の一派です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96EE")

    label("loc_9548")


    #C0395
    ChrTalk(
        0x101,
        (
            "#00001F#5Pええ、カルバード共和国の\x01",
            "移民政策反対派――\x01",
            "『反移民政策主義』の一派ですね。\x02\x03",

            "#00011F（――って、\x01",
            "  それだけじゃないだろ。）\x02\x03",

            "#00003Fさらに、エレボニア帝国の\x01",
            "『帝国解放戦線』です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96EE")

    label("loc_9611")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0396
    ChrTalk(
        0x101,
        (
            "#00006F#5Pええ、犯人は２大国に\x01",
            "それぞれ存在するテロ集団――\x02\x03",

            "#00008F一方はエレボニア帝国の\x01",
            "『帝国解放戦線』――\x02\x03",

            "#00013Fもう一方は、カルバード共和国の\x01",
            "移民政策反対派――\x01",
            "『反移民政策主義』の一派です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96EE")

    label("loc_96EE")


    #C0397
    ChrTalk(
        0xE,
        "#11Pええ、まさしくその２者です。\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xE,
        (
            "#11P彼らの背景や主義主張に関しては、\x01",
            "あえてこの場では言及しませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xE,
        (
            "#11Pここでポイントとなるのは、\x01",
            "通常接点のない両者が共同戦線を\x01",
            "張ったということですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xE,
        (
            "#11P噂では、かつてリベールで暗躍した\x01",
            "《身喰らう蛇》という組織が\x01",
            "協力していたとも言われていますが……\x02",
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
            "#00013F#5P結社《身喰らう蛇》……\x02\x03",

            "#00008F（そういえば、通商会議で\x01",
            "  テロリストたちは人形兵器を\x01",
            "  使っていたんだよな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x102,
        (
            "#00108F#6Pニールセンさんは、\x01",
            "《結社》をご存知なんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xE,
        (
            "#11Pええ、そういう謎めいた組織が\x01",
            "確かに存在しているという程度には。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xE,
        (
            "#11Pしかし、やはり皆さんも\x01",
            "ご存知だったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x104,
        "#00306F#5Pま、ほんの少しッスけどね。\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x103,
        (
            "#00211F#6P知れば知るほど\x01",
            "胡散臭さが増すばかりですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xE,
        (
            "#11P……いずれにしても\x01",
            "何が目的で動いているのかも一切不明な\x01",
            "不可思議な集団であるのは確かなようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xE,
        (
            "#11Pその意図については\x01",
            "現時点では推論しようもないので\x01",
            "一旦保留にした方が無難でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        "#00006F#5P確かに、それが良さそうですね。\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xE,
        "#11Pでは、話を先に進めましょう。\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xE,
        (
            "#11P次に確認したいのは――\x01",
            "今回のテロ事件における、\x01",
            "２大国の意向と立場です。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xE,
        (
            "#11P情報筋によると、両国は前もって\x01",
            "外部の実動部隊を密かに用意。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xE,
        (
            "#11Pその存在が、テロ事件の収拾に\x01",
            "大きく貢献したという話ですが――\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xE,
        (
            "#11Pテロの動きを掴んでおきながら、\x01",
            "あえて泳がせたとも言えるこの行動。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xE,
        (
            "#11P両首脳の狙いは一体何だったのか――\x01",
            "ロイドさんはどうお考えになりますか？\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)

    label("loc_9CDC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A08C")
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
            "#1Kテロ事件における、オズボーン宰相と\x01",
            "ロックスミス大統領の狙いとは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "テロ集団の炙り出し\x01",        # 0
            "国内の反対派への牽制\x01",      # 1
            "ディーター市長の退陣\x01",      # 2
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
        (0, "loc_9DC9"),
        (1, "loc_9E75"),
        (2, "loc_9FAF"),
        (SWITCH_DEFAULT, "loc_A079"),
    )


    label("loc_9DC9")


    #C0417
    ChrTalk(
        0x101,
        (
            "#00005F#5P（もしや、テロ集団を\x01",
            "  炙り出すという狙いが……？）\x02\x03",

            "#00006F（……いや違う、そもそも\x01",
            "  両国ともテロリストの実態は\x01",
            "  それなりに把握しているはずだ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A079")

    label("loc_9E75")


    #C0418
    ChrTalk(
        0x101,
        (
            "#00003F#5Pテロリストを放った側である\x01",
            "現政権への反対派――\x02\x03",

            "彼らに対する牽制が\x01",
            "両首脳の狙いだと思います。\x02\x03",

            "#00008Fオズボーン宰相にとっては、\x01",
            "敵対する貴族勢力に対しての牽制。\x02\x03",

            "#00001Fロックスミス大統領にとっては、\x01",
            "国内を騒がす不穏分子への抑制が\x01",
            "第一目的なのではないでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9FA7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9FA7")

    SetScenarioFlags(0x1, 1)
    Jump("loc_A079")

    label("loc_9FAF")


    #C0419
    ChrTalk(
        0x101,
        (
            "#00008F#5P（テロ事件で改めて証明された\x01",
            "  自治州の安全保障の不足。）\x02\x03",

            "（それを追求することで\x01",
            "  ディーター市長への退陣要求に……）\x02\x03",

            "#00011F（いやいや、これは\x01",
            "  そんなスケールの話じゃない。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_A079")

    label("loc_A079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A087")
    Jump("loc_A08C")

    label("loc_A087")

    Jump("loc_9CDC")

    label("loc_A08C")


    #C0420
    ChrTalk(
        0xE,
        (
            "#11Pふむ、仰る通りです。\x01",
            "確かにそのことが\x01",
            "最大の狙いと考えられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xE,
        (
            "#11P実際、両国では事件以降、\x01",
            "それらの勢力に対する糾弾の声も\x01",
            "高まっているそうですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x103,
        (
            "#00203F#6Pなるほど、政争における格好の\x01",
            "攻撃材料というわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xE,
        (
            "#11Pちなみにロイドさんは\x01",
            "第一目的と仰いましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xE,
        (
            "#11Pよければ、その他の狙いについても\x01",
            "お聞かせ願えますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x101,
        "#00011F#5Pそれは……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    #C0426
    ChrTalk(
        0x102,
        "#00108F#6Pロイド……\x02",
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
            "#00006F#5Pもう１つの大きな狙い――\x02\x03",

            "#00013Fそれは、クロスベル進出の足がかりを\x01",
            "本格的に構築するためだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xE,
        "#11Pふむ……\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x105,
        (
            "#10303F#6Pクロスベル進出――\x02\x03",

            "#10301F一番分かりやすいのは、\x01",
            "通商会議で両国から提案された\x01",
            "軍の駐留案ってヤツだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x103,
        (
            "#00203F#6Pテロ事件で改めて証明された\x01",
            "クロスベルの安全保障の不足――\x02\x03",

            "#00201Fそれを解決するために\x01",
            "必要な提案ということでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x102,
        (
            "#00106F#6Pええ、それによって\x01",
            "リベールで締結された『不戦条約』は\x01",
            "大幅に抑止力を失ってしまった……\x02\x03",

            "#00108Fさらに独立提唱も含めて\x01",
            "２大国の世論は現在、クロスベルに\x01",
            "大きな関心を持っているわ。\x02\x03",

            "#00101Fそれが結果的に、国内の対立や不満を\x01",
            "逸らすことにも繋がったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x103,
        "#00205F#6Pそんな所にまで狙いが……\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x104,
        (
            "#00306F#5Pはぁ～、いったい\x01",
            "一石何鳥だって話だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xE,
        (
            "#11P……ふむ、やはり皆さんは\x01",
            "なかなか深く考察されているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xE,
        (
            "#11P――では、このあたりで\x01",
            "最後のポイントに移りましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xE,
        (
            "#11P今回の件は、状況からしても\x01",
            "両国の間で申し合わせが\x01",
            "あったことは明白と言えますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xE,
        (
            "#11Pこれは、両国の同盟関係を\x01",
            "意味するものなのでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)

    label("loc_A684")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8FE")
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
            "#1Kテロ事件の対処を通して、\x01",
            "帝国と共和国は同盟関係を結んだのか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "一時的に結んだ\x01",      # 0
            "永続的に結んだ\x01",      # 1
            "あり得ない\x01",          # 2
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
        (0, "loc_A759"),
        (1, "loc_A7CC"),
        (2, "loc_A84F"),
        (SWITCH_DEFAULT, "loc_A8EB"),
    )


    label("loc_A759")


    #C0440
    ChrTalk(
        0x101,
        (
            "#00008F#5P（一時的に……\x01",
            "  なら考えられるか？）\x02\x03",

            "#00003F（いや、そんな\x01",
            "  単純な話であるはずがない。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A8EB")

    label("loc_A7CC")


    #C0441
    ChrTalk(
        0x101,
        (
            "#00005F#5P（まさか、これを機に\x01",
            "  永続的な同盟関係を――）\x02\x03",

            "#00006F（――ってバカな。\x01",
            "  そんなことがあるはずがない。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_A8EB")

    label("loc_A84F")


    #C0442
    ChrTalk(
        0x101,
        (
            "#5P#00003Fいえ……\x01",
            "それはあり得ないと思います。\x02\x03",

            "#00013F──どちらも最終的な目的は\x01",
            "クロスベルの単独支配でしょうから。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8E3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A8E3")

    SetScenarioFlags(0x1, 1)
    Jump("loc_A8EB")

    label("loc_A8EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A8F9")
    Jump("loc_A8FE")

    label("loc_A8F9")

    Jump("loc_A684")

    label("loc_A8FE")


    #C0443
    ChrTalk(
        0xE,
        "#11Pええ――その通りです。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xE,
        (
            "#11P今回の件はあくまで一時的に\x01",
            "足並みを揃えただけでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xE,
        (
            "#11Pクロスベルという\x01",
            "力を持ちすぎた緩衝地帯――\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xE,
        (
            "#11Pそんな特異で重要な地を\x01",
            "一体どちらが手中に収めるか、\x01",
            "そんな意志確認を暗に含めて。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x109,
        "#10113F#5Pそれは……\x02",
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
        "#00211F#6P……露骨すぎですね。\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x105,
        (
            "#10306F#6Pあくまでガチでやり合う前の\x01",
            "下準備ってわけだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xE,
        (
            "#11Pええ──今後は\x01",
            "ますます両国による諜報戦が\x01",
            "激化していくことも考えられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xE,
        (
            "#11Pそうした状況になれば\x01",
            "犯罪組織や猟兵団などの動きが\x01",
            "活発化することにも繋がるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xE,
        (
            "#11Pそうすれば、過去に度々\x01",
            "起きていた不可解な事故も再び\x01",
            "その姿を現し出すかもしれない──\x02",
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
        "#00305F#5P不可解な事故……？\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x103,
        "#00205F#6Pそれはどういう……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0456
    ChrTalk(
        0xE,
        (
            "#11Pいえ──詮ないことを\x01",
            "言ってしまったようですね。\x02",
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
            "#11P色々と整理できましたし、\x01",
            "有意義なお話も伺えました。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xE,
        "#11Pご協力、本当に感謝します。\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        "#00003F#5P……いえ、こちらこそ。\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x102,
        (
            "#00100F#6P私たちの方も大分、\x01",
            "状況整理が出来た気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x109,
        "#10106F#5P……とても勉強になりました。\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xE,
        "#11Pそう言って頂けると。\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xE,
        (
            "#11Pまた機会があれば、\x01",
            "こうしてお話を聞かせてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        "#00000F#5Pええ、その時は是非。\x02",
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
            "クエスト【テロ事件に関する取材協力】\x07\x00",
            "を達成した！\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEE5")
    OP_2C(0x89, 0x2)
    Jump("loc_AEF9")

    label("loc_AEE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEF9")
    OP_2C(0x89, 0x1)

    label("loc_AEF9")

    OP_29(0x89, 0x1, 0x0)
    OP_29(0x89, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_40_9194 end

    SaveToFile()

Try(main)
