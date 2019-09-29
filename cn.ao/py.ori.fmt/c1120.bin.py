from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1120.bin",                # FileName
        "c1120",                    # MapName
        "c1120",                    # Location
        0x0017,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 23, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1120",                  # 0
        "格蕾丝",                 # 1
        "雷因兹",                 # 2
        "芬",                     # 3
        "奥斯卡",                 # 4
        "接待小姐辛茜亚",         # 5
        "爱丽斯",                 # 6
        "凯特巡警",               # 7
        "钢琴演奏者",             # 8
        "向导",                   # 9
        "女仆",                   # 10
        "市民",                   # 11
        "市民",                   # 12
        "市民",                   # 13
        "男孩",                   # 14
        "市民",                   # 15
        "莉丝修女",               # 16
        "桑桑",                   # 17
        "乔安娜",                 # 18
        "摩尔斯老人",             # 19
        "洛依",                   # 20
        "温蒂",                   # 21
        "市民",                   # 22
        "市民",                   # 23
        "市民",                   # 24
        "市民",                   # 25
        "市民",                   # 26
        "市民",                   # 27
        "市民",                   # 28
        "坎贝尔议员",             # 29
        "帝国派议员",             # 30
        "独立派议员",             # 31
        "独立派议员",             # 32
        "司仪",                   # 33
    ))

    AddCharChip((
        "chr/ch06000.itc",                   # 00
        "chr/ch28100.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch07000.itc",                   # 03
        "chr/ch34600.itc",                   # 04
        "chr/ch26900.itc",                   # 05
        "chr/ch30600.itc",                   # 06
        "chr/ch33302.itc",                   # 07
        "chr/ch25900.itc",                   # 08
        "chr/ch25600.itc",                   # 09
        "chr/ch21600.itc",                   # 0A
        "chr/ch21000.itc",                   # 0B
        "chr/ch20300.itc",                   # 0C
        "chr/ch23000.itc",                   # 0D
        "chr/ch21702.itc",                   # 0E
        "chr/ch14000.itc",                   # 0F
        "chr/ch26902.itc",                   # 10
        "chr/ch32500.itc",                   # 11
        "chr/ch25700.itc",                   # 12
    ))

    DeclNpc(-4659,   0,       9239,    0,    261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-5949,   0,       9800,    45,   261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-10529,  0,       1179,    90,   261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-10189,  0,       7269,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-6579,   0,       -2069,   109,  261,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(5000,    0,       2289,    270,  261,  0x0, 0,   16,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-4070,   0,       6420,    135,  261,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-3309,   1049,    13500,   135,  261,  0x0, 0,   7,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-1019,   0,       -9300,   270,  261,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-790,    0,       7590,    348,  261,  0x0, 0,   9,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(-2180,   0,       3890,    315,  261,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-90,     0,       4420,    45,   261,  0x0, 0,   11,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-730,    0,       -2769,   135,  261,  0x0, 0,   12,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-29,     0,       -3329,   315,  261,  0x0, 0,   13,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5000,    0,       -2769,   270,  261,  0x0, 0,   14,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   15,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   0,   0,   0,   10,  255,  0)
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

    DeclActor(7750,    4000,    12300,   1200,    7750,    5450,    12300,   0x007C, 0,  5,  0x0000)
    DeclActor(-2170,   880,     11540,   1000,    -3310,   2550,    13500,   0x007E, 0,  17, 0x0000)

    ChipFrameInfo(1392, 0)                                       # 0

    ScpFunction((
        "Function_0_570",          # 00, 0
        "Function_1_620",          # 01, 1
        "Function_2_76E",          # 02, 2
        "Function_3_85B",          # 03, 3
        "Function_4_990",          # 04, 4
        "Function_5_A5A",          # 05, 5
        "Function_6_B66",          # 06, 6
        "Function_7_E8B",          # 07, 7
        "Function_8_F40",          # 08, 8
        "Function_9_1151",         # 09, 9
        "Function_10_128B",        # 0A, 10
        "Function_11_1361",        # 0B, 11
        "Function_12_1640",        # 0C, 12
        "Function_13_182F",        # 0D, 13
        "Function_14_1A0A",        # 0E, 14
        "Function_15_1AC1",        # 0F, 15
        "Function_16_1BBC",        # 10, 16
        "Function_17_1CB5",        # 11, 17
        "Function_18_1D47",        # 12, 18
        "Function_19_1E37",        # 13, 19
        "Function_20_1EE1",        # 14, 20
        "Function_21_1F84",        # 15, 21
        "Function_22_1FEA",        # 16, 22
        "Function_23_20BF",        # 17, 23
        "Function_24_23D3",        # 18, 24
        "Function_25_438C",        # 19, 25
        "Function_26_43F6",        # 1A, 26
        "Function_27_4437",        # 1B, 27
        "Function_28_4522",        # 1C, 28
        "Function_29_6D87",        # 1D, 29
        "Function_30_6DC5",        # 1E, 30
        "Function_31_6DE4",        # 1F, 31
        "Function_32_6E15",        # 20, 32
        "Function_33_6E49",        # 21, 33
        "Function_34_6E7D",        # 22, 34
        "Function_35_6E99",        # 23, 35
        "Function_36_6ECA",        # 24, 36
        "Function_37_6EE6",        # 25, 37
        "Function_38_6F02",        # 26, 38
        "Function_39_6F4D",        # 27, 39
        "Function_40_6F87",        # 28, 40
        "Function_41_6FE9",        # 29, 41
        "Function_42_711E",        # 2A, 42
    ))


    def Function_0_570(): pass

    label("Function_0_570")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5A8"),
        (1, "loc_5B4"),
        (2, "loc_5C0"),
        (3, "loc_5CC"),
        (4, "loc_5D8"),
        (5, "loc_5E4"),
        (6, "loc_5F0"),
        (SWITCH_DEFAULT, "loc_5FC"),
    )


    label("loc_5A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_608")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_61F")

    Return()

    # Function_0_570 end

    def Function_1_620(): pass

    label("Function_1_620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76D")
    SetChrPos(0xFE, 3130, 0, 9060, 270)
    OP_95(0xFE, -160, 0, 7500, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, -1340, 0, 3750, 1000, 0x0)
    OP_95(0xFE, -80, 0, -190, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(2000)
    OP_95(0xFE, -1120, 0, 1760, 1000, 0x0)
    OP_95(0xFE, -3830, 0, 1460, 1000, 0x0)
    OP_95(0xFE, -4390, 0, 2430, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(2000)
    OP_95(0xFE, -4330, 0, -270, 1000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2360, 0, 1350, 1000, 0x0)
    OP_95(0xFE, 1010, 0, 2510, 1000, 0x0)
    OP_95(0xFE, 1630, 0, 3540, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(2000)
    OP_95(0xFE, 3710, 0, 4130, 1000, 0x0)
    OP_95(0xFE, 4290, 0, 7130, 1000, 0x0)
    OP_95(0xFE, 3130, 0, 9060, 1000, 0x0)
    Jump("Function_1_620")

    label("loc_76D")

    Return()

    # Function_1_620 end

    def Function_2_76E(): pass

    label("Function_2_76E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_85A")
    OP_95(0x17, -7300, 0, -2510, 2000, 0x0)
    OP_95(0x17, -7330, 0, 1430, 2000, 0x0)
    OP_93(0x17, 0x10E, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -5910, 0, 4260, 2000, 0x0)
    OP_93(0x17, 0x5A, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -6960, 0, 7410, 2000, 0x0)
    OP_93(0x17, 0x10E, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -5910, 0, 4260, 2000, 0x0)
    OP_93(0x17, 0x5A, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -7330, 0, 1430, 2000, 0x0)
    OP_93(0x17, 0x10E, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -7300, 0, -2510, 2000, 0x0)
    OP_95(0x17, -5820, 0, -3790, 2000, 0x0)
    OP_93(0x17, 0x2D, 0x1F4)
    Sleep(2000)
    Jump("Function_2_76E")

    label("loc_85A")

    Return()

    # Function_2_76E end

    def Function_3_85B(): pass

    label("Function_3_85B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_872")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 3)
    Event(0, 24)
    Jump("loc_881")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_881")
    ClearScenarioFlags(0x22, 2)
    Event(0, 41)

    label("loc_881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89C")
    Event(0, 42)

    label("loc_89C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98F")
    SetScenarioFlags(0x1, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_96A")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -4500, 0, -7300, 270)
    SetChrPos(0x8, -5560, 0, -7300, 90)
    SetChrPos(0x9, -5160, 0, -6000, 135)
    SetChrPos(0x18, -8590, 0, 2730, 225)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0x19, 3340, 0, 10090, 90)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x17, -5820, 0, -3790, 45)
    BeginChrThread(0x17, 0, 0, 2)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0x16, 0xE)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_97E")

    label("loc_96A")

    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x15, 0x10)

    label("loc_97E")

    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)

    label("loc_98F")

    Return()

    # Function_3_85B end

    def Function_4_990(): pass

    label("Function_4_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B3")
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetScenarioFlags(0x1, 3)

    label("loc_9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F2")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light04", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A27")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light04", 0x0, 0x1)

    label("loc_A27")

    OP_65(0x0, 0x1)
    SetMapObjFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A44")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0xE, 0x4)

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_A59")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 3)

    label("loc_A59")

    Return()

    # Function_4_990 end

    def Function_5_A5A(): pass

    label("Function_5_A5A")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "★特制香甜巧克力蛋糕的制作方法★\x01",
            "　～　大家也在自己家中\x01",
            "　　　试着做做看吧　　～\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "记录着香甜巧克力蛋糕的食谱。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_B62")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x11)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B62")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『香甜巧克力蛋糕』\x07\x00",
            "的食谱已经记下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_B62")

    TalkEnd(0xFF)
    Return()

    # Function_5_A5A end

    def Function_6_B66(): pass

    label("Function_6_B66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7B")
    TurnDirection(0x8, 0x0, 500)

    #C0004
    ChrTalk(
        0x8,
        (
            "#02102F啊，你们也辛苦了！\x02\x03",

            "我正在采访职业女性\x01",
            "选秀活动的参加者呢。\x02\x03",

            "#02109F呵呵，稍后你们也要\x01",
            "接受我的采访哦～¤\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#00006F（唔、唔～如果接受，\x01",
            "  恐怕会占用不少时间呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x105,
        (
            "#10302F（呵呵，看来还是偷偷\x01",
            "  逃走为好啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    SetScenarioFlags(0x0, 4)
    Jump("loc_CD1")

    label("loc_C7B")


    #C0007
    ChrTalk(
        0x8,
        (
            "#02105F呀，是吗？\x02\x03",

            "#02100F嗯，毕竟发生了那样的事件，\x01",
            "确实应该回去\x01",
            "和家人见个面。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD1")

    Jump("loc_E87")

    label("loc_CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E25")

    #C0008
    ChrTalk(
        0x8,
        "#02109F呀，罗伊德和各位！\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00000F格蕾丝小姐……\x01",
            "您正在慈善宴会取材吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "#02100F呵呵，没错☆\x02\x03",

            "这里真是相当热闹，\x01",
            "看来可以写出一篇能让克洛斯贝尔\x01",
            "市民重振精神的报道了。\x02\x03",

            "#02103F那起袭击事件所造成\x01",
            "的伤害还没有消退……\x02\x03",

            "#02102F我们这些媒体界人士也必须\x01",
            "要做好自己力所能及的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        "#00309F哈哈，请加油啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 6)
    Jump("loc_E87")

    label("loc_E25")


    #C0012
    ChrTalk(
        0x8,
        (
            "#02102F听说在慈善宴会中\x01",
            "还会举办一个\x01",
            "很有趣的活动……\x02\x03",

            "#02109F呵呵，一定要第一时间做个快报！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E87")

    TalkEnd(0xFE)
    Return()

    # Function_6_B66 end

    def Function_7_E8B(): pass

    label("Function_7_E8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EF3")

    #C0013
    ChrTalk(
        0xFE,
        (
            "职业女性选秀活动\x01",
            "很有观赏价值啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "我拍了很多不错的照片，\x01",
            "得赶快回去整理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F3C")

    label("loc_EF3")


    #C0015
    ChrTalk(
        0xFE,
        (
            "被邀请至慈善宴会的\x01",
            "美女钢琴演奏家……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "看来能拍出很好的照片呢。\x02",
    )

    CloseMessageWindow()

    label("loc_F3C")

    TalkEnd(0xFE)
    Return()

    # Function_7_E8B end

    def Function_8_F40(): pass

    label("Function_8_F40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1023")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD7")

    #C0017
    ChrTalk(
        0xFE,
        (
            "哎呀～真没想到\x01",
            "桑桑会参加\x01",
            "职业女性选秀活动啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "多亏如此，她似乎已经\x01",
            "稍微恢复了一些精神，\x01",
            "这种结果真是不错。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_101E")

    label("loc_FD7")


    #C0019
    ChrTalk(
        0xFE,
        (
            "不过，桑桑来参加\x01",
            "职业女性选秀活动……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "……但愿老板不要发怒。\x02",
    )

    CloseMessageWindow()

    label("loc_101E")

    Jump("loc_114D")

    label("loc_1023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10EA")

    #C0021
    ChrTalk(
        0xFE,
        (
            "我把『龙老饭店』的料理\x01",
            "送到了这个\x01",
            "慈善宴会的会场。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "至于店里，就由帕库和鲁斯\x01",
            "来填补我不在所造成的空缺。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "虽然有点担心，\x01",
            "但他们两个也已经有所成长了，\x01",
            "应该不会有问题吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_114D")

    label("loc_10EA")


    #C0024
    ChrTalk(
        0xFE,
        (
            "不过……桑桑最近\x01",
            "一直都很没精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "而且还拒绝参与\x01",
            "选秀活动……\x01",
            "真希望她能早日恢复精神。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114D")

    TalkEnd(0xFE)
    Return()

    # Function_8_F40 end

    def Function_9_1151(): pass

    label("Function_9_1151")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1287")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1218")

    #C0026
    ChrTalk(
        0xFE,
        (
            "呵呵，如果这样\x01",
            "能使店里的客人增加，\x01",
            "爸爸也会很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "……虽然很担心莉夏，\x01",
            "但她一定会回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "为了到时候能面带笑容地迎接她，\x01",
            "我必须要打起精神来等待。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_1282")

    label("loc_1218")


    #C0029
    ChrTalk(
        0xFE,
        (
            "……虽然很担心莉夏，\x01",
            "但她一定会回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "为了到时候能面带笑容地迎接她，\x01",
            "我必须要打起精神来等待。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1282")

    Jump("loc_1287")

    label("loc_1287")

    TalkEnd(0xFE)
    Return()

    # Function_9_1151 end

    def Function_10_128B(): pass

    label("Function_10_128B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_135D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1321")

    #C0031
    ChrTalk(
        0xFE,
        (
            "呼……竟然让我这种身份的人\x01",
            "站到台上……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00109F呵呵……乔安娜，\x01",
            "别担心，你很可爱啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "呜呜，好丢人……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_1358")

    label("loc_1321")


    #C0034
    ChrTalk(
        0xFE,
        (
            "竟然让我这种身份的人站到台上……\x01",
            "呜呜，好丢人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1358")

    Jump("loc_135D")

    label("loc_135D")

    TalkEnd(0xFE)
    Return()

    # Function_10_128B end

    def Function_11_1361(): pass

    label("Function_11_1361")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_14B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1479")

    #C0035
    ChrTalk(
        0xFE,
        (
            "哟，罗伊德和支援科的各位！\x01",
            "你们的代表太帅气啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "哈哈，虽然在登台出场的时候\x01",
            "显得有点紧张，\x01",
            "但在我个人眼里，她才是真正的冠军。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_1428")

    #C0037
    ChrTalk(
        0x102,
        "#00109F呵呵，谢谢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1471")

    label("loc_1428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_144F")

    #C0038
    ChrTalk(
        0x103,
        "#00202F呵呵，谢谢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1471")

    label("loc_144F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_1471")

    #C0039
    ChrTalk(
        0x109,
        "#10109F呵呵，谢谢！\x02",
    )

    CloseMessageWindow()

    label("loc_1471")

    SetScenarioFlags(0x0, 6)
    Jump("loc_14B3")

    label("loc_1479")


    #C0040
    ChrTalk(
        0xFE,
        (
            "好啦，你们就继续\x01",
            "享受宴会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "料理还\x01",
            "有的是呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B3")

    Jump("loc_163C")

    label("loc_14B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D1")

    #C0042
    ChrTalk(
        0xFE,
        "哦哦！这不是罗伊德吗！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#00005F奥斯卡……？\x01",
            "你来宴会现场帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "嗯，店里有贝奈特和老板在看着，\x01",
            "我就到这边来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "餐台上摆放着我们的长面包，\x01",
            "另外我还做了一些\x01",
            "适合与面包一起吃的料理。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#00102F嗯，真了不起呢。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "哈哈，你们也要\x01",
            "尽情享受哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 7)
    Jump("loc_163C")

    label("loc_15D1")


    #C0048
    ChrTalk(
        0xFE,
        (
            "餐台上摆放着我们的长面包，\x01",
            "另外我还做了一些\x01",
            "适合与面包一起吃的料理。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "哈哈，你们也要\x01",
            "尽情享受哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163C")

    TalkEnd(0xFE)
    Return()

    # Function_11_1361 end

    def Function_12_1640(): pass

    label("Function_12_1640")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1654")
    Jump("loc_182B")

    label("loc_1654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_END)), "loc_16C6")

    #C0050
    ChrTalk(
        0xFE,
        (
            "罗伊德，你们好像正在寻找\x01",
            "选秀活动的参加人员啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "呵呵，请加油吧。\x01",
            "我会在这里为你们鼓劲的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_182B")

    label("loc_16C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DA")

    #C0052
    ChrTalk(
        0xFE,
        "啊，这不是罗伊德和各位吗！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00003F哎，凯特前辈？\x01",
            "您在这种地方做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "嗯，算是来宴会现场\x01",
            "帮忙吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "不过，再过一段时间\x01",
            "才轮到我出场，\x01",
            "所以要先把肚子填饱。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        "#00105F出场……？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "哦，这个嘛，\x01",
            "暂时保密。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "呵呵，请尽管\x01",
            "期待吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 0)
    Jump("loc_182B")

    label("loc_17DA")


    #C0059
    ChrTalk(
        0xFE,
        (
            "再过一段时间\x01",
            "才轮到我出场，\x01",
            "所以要先把肚子填饱。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "呵呵，请尽管\x01",
            "期待吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182B")

    TalkEnd(0xFE)
    Return()

    # Function_12_1640 end

    def Function_13_182F(): pass

    label("Function_13_182F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1998")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1931")

    #C0061
    ChrTalk(
        0x8,
        (
            "#02100F嗯嗯，也就是说，\x01",
            "是职场的同事劝说你来参加活动的？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "呵呵，站在选秀活动的台上，\x01",
            "真是很紧张。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "不过，当听到大家的掌声时，\x01",
            "实在是非常开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        "呵呵，这次果然来对了。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "#02104F嗯嗯……（记录）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1993")

    label("loc_1931")


    #C0067
    ChrTalk(
        0xFE,
        (
            "我准备在近期返回故乡雷米菲利亚，\x01",
            "不过很快就会回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "可以给父母讲讲\x01",
            "这次的有趣经历呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1993")

    Jump("loc_1A06")

    label("loc_1998")


    #C0069
    ChrTalk(
        0xFE,
        (
            "在稍后的活动中，\x01",
            "必须要上台\x01",
            "展示自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "因为工作缘故，\x01",
            "我早就习惯站在人前了，\x01",
            "但终究还是有些紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A06")

    TalkEnd(0xFE)
    Return()

    # Function_13_182F end

    def Function_14_1A0A(): pass

    label("Function_14_1A0A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1A78")

    #C0071
    ChrTalk(
        0xFE,
        (
            "啊～被别人赞赏\x01",
            "的感觉真是最棒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "这次非常开心，\x01",
            "以后要是有机会，还想再参加啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABD")

    label("loc_1A78")


    #C0073
    ChrTalk(
        0xFE,
        (
            "（擦粉底）……\x01",
            "嗯，妆容很完美。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "既然参加，就一定要得冠军～\x02",
    )

    CloseMessageWindow()

    label("loc_1ABD")

    TalkEnd(0xFE)
    Return()

    # Function_14_1A0A end

    def Function_15_1AC1(): pass

    label("Function_15_1AC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B55")

    #C0075
    ChrTalk(
        0xFE,
        (
            "多亏职业女性选秀活动的影响力，\x01",
            "克洛斯贝尔市筹集到了\x01",
            "大量的复兴援助款。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "非常感谢诸位市民，\x01",
            "还有特别任务支援科\x01",
            "的各位。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB8")

    label("loc_1B55")


    #C0077
    ChrTalk(
        0xFE,
        (
            "今天的立餐宴会所收取的\x01",
            "餐饮费用将全部捐赠\x01",
            "为克洛斯贝尔市的复兴基金。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "请各位\x01",
            "尽情享受吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB8")

    TalkEnd(0xFE)
    Return()

    # Function_15_1AC1 end

    def Function_16_1BBC(): pass

    label("Function_16_1BBC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C1E")

    #C0079
    ChrTalk(
        0xFE,
        (
            "参加活动的各位选手\x01",
            "都很出色呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "我要是担当女仆一职\x01",
            "的候选人就好了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB1")

    label("loc_1C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_END)), "loc_1C8A")

    #C0081
    ChrTalk(
        0xFE,
        (
            "我还得在立餐宴会中帮忙，\x01",
            "没办法参加职业女性选秀活动啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "不好意思，\x01",
            "请你们找别人吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB1")

    label("loc_1C8A")


    #C0083
    ChrTalk(
        0xFE,
        (
            "如果需要食物或饮料，\x01",
            "请尽管开口～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB1")

    TalkEnd(0xFE)
    Return()

    # Function_16_1BBC end

    def Function_17_1CB5(): pass

    label("Function_17_1CB5")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D25")

    #C0084
    ChrTalk(
        0xF,
        (
            "我本来觉得职业女性选秀\x01",
            "这种活动太庸俗了……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xF,
        (
            "呵呵，但真是很开心呢。\x01",
            "你们也辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D43")

    label("loc_1D25")


    #C0086
    ChrTalk(
        0xF,
        "接下来要弹什么曲子呢……\x02",
    )

    CloseMessageWindow()

    label("loc_1D43")

    TalkEnd(0xF)
    Return()

    # Function_17_1CB5 end

    def Function_18_1D47(): pass

    label("Function_18_1D47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1DB1")

    #C0087
    ChrTalk(
        0xFE,
        (
            "……唔、唔唔唔……\x01",
            "吃得实在太多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "不过，为了克洛斯贝尔……\x01",
            "我一定拼命吃！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E33")

    label("loc_1DB1")


    #C0089
    ChrTalk(
        0xFE,
        (
            "（大吃大嚼）……\x01",
            "克洛斯贝尔的各种美食\x01",
            "好像都汇集到这个会场了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "吃得越多，\x01",
            "对市里的贡献就越大，\x01",
            "所以一定要拼命多吃啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E33")

    TalkEnd(0xFE)
    Return()

    # Function_18_1D47 end

    def Function_19_1E37(): pass

    label("Function_19_1E37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E85")

    #C0091
    ChrTalk(
        0xFE,
        "哈～真是养眼啊。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        "漂亮姑娘果然是最好的下酒菜啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EDD")

    label("loc_1E85")


    #C0093
    ChrTalk(
        0xFE,
        (
            "嗯～会场内好像\x01",
            "有很多漂亮姑娘呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "莫非和稍后举办的那个\x01",
            "重头活动有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDD")

    TalkEnd(0xFE)
    Return()

    # Function_19_1E37 end

    def Function_20_1EE1(): pass

    label("Function_20_1EE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F59")

    #C0095
    ChrTalk(
        0xFE,
        (
            "呵呵，身为同性，\x01",
            "也觉得那些参选者都很有魅力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "这孩子好像也很憧憬\x01",
            "那些劳动中的大姐姐呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F80")

    label("loc_1F59")


    #C0097
    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，怎么吃了\x01",
            "一嘴番茄酱啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F80")

    TalkEnd(0xFE)
    Return()

    # Function_20_1EE1 end

    def Function_21_1F84(): pass

    label("Function_21_1F84")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1FC1")

    #C0098
    ChrTalk(
        0xFE,
        "我觉得……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "还是警察\x01",
            "最帅气了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FE6")

    label("loc_1FC1")


    #C0100
    ChrTalk(
        0xFE,
        (
            "（嚼嚼）……\x01",
            "嘿嘿嘿，真好吃～¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE6")

    TalkEnd(0xFE)
    Return()

    # Function_21_1F84 end

    def Function_22_1FEA(): pass

    label("Function_22_1FEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2059")

    #C0101
    ChrTalk(
        0xFE,
        "职业女性选秀活动真有意思啊。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "呵呵，要是我能年轻三十岁，\x01",
            "倒也很想去当个候选人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BB")

    label("loc_2059")


    #C0103
    ChrTalk(
        0xFE,
        (
            "刚才演奏的那首钢琴曲\x01",
            "真是音色优美啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "受袭击事件的影响而消沉\x01",
            "的心情似乎已经平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BB")

    TalkEnd(0xFE)
    Return()

    # Function_22_1FEA end

    def Function_23_20BF(): pass

    label("Function_23_20BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_23CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2269")

    #C0105
    ChrTalk(
        0x17,
        (
            "#04402F多谢大家\x01",
            "邀请我过来。\x02\x03",

            "这真是一次在教会中\x01",
            "无法经历的有趣体验。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        "#00109F呵呵，辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        (
            "#00302F难得的机会，\x01",
            "我本来还很想投票\x01",
            "给莉丝小姐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x17,
        (
            "#04406F我毕竟不是市民，\x01",
            "如果和其他参选者竞争，\x01",
            "未免有些不妥……\x02\x03",

            "#04409F不过，谢谢了。\x01",
            "就算只是客套话，我也很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#00005F（嗯……如果她参加票选，\x01",
            "  我想一定会得到相当多的票数。）\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        "#00202F（她完全没有这方面的意识呢。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 1)
    Jump("loc_23CF")

    label("loc_2269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2360")

    #C0111
    ChrTalk(
        0x17,
        (
            "#04402F我虽然谢绝了\x01",
            "参加票选，\x01",
            "但这确实是一次很有趣的体验。\x02\x03",

            "#04404F（大吃大嚼）……\x01",
            "而且还可以这样尽情\x01",
            "享用立餐宴会的美味……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00011F（手中的盘子上\x01",
            "  放着堆积如山的料理……）\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x102,
        "#00109F（呵呵，真不愧是莉丝小姐啊。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_23CF")

    label("loc_2360")


    #C0114
    ChrTalk(
        0x17,
        (
            "#04404F（大吃大嚼）……\x01",
            "我再过一会\x01",
            "就回大圣堂了。\x02\x03",

            "#04402F……在那之前，我打算\x01",
            "继续享用立餐宴会上的料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23CF")

    TalkEnd(0xFE)
    Return()

    # Function_23_20BF end

    def Function_24_23D3(): pass

    label("Function_24_23D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev15001.eff")
    LoadEffect(0x1, "event\\ev290_03.eff")
    LoadChrToIndex("chr/ch20800.itc", 0x1F)
    LoadChrToIndex("chr/ch21200.itc", 0x20)
    LoadChrToIndex("apl/ch51257.itc", 0x21)
    LoadChrToIndex("chr/ch26100.itc", 0x22)
    LoadChrToIndex("apl/ch51547.itc", 0x24)
    LoadChrToIndex("chr/ch20200.itc", 0x25)
    LoadChrToIndex("chr/ch20700.itc", 0x26)
    LoadChrToIndex("chr/ch21100.itc", 0x27)
    LoadChrToIndex("chr/ch28000.itc", 0x28)
    LoadChrToIndex("chr/ch20000.itc", 0x29)
    LoadChrToIndex("chr/ch20100.itc", 0x2A)
    LoadChrToIndex("chr/ch20400.itc", 0x2B)
    SoundLoad(803)
    SoundLoad(821)
    SoundLoad(877)
    SoundLoad(818)
    SoundLoad(819)
    SoundLoad(820)
    SoundLoad(420)
    SoundLoad(421)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    OP_68(-5060, 1500, 1290, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(28100, 0)
    SetChrPos(0x10, -10190, 0, 7270, 90)
    SetChrPos(0x11, -10530, 0, 1180, 90)
    SetChrPos(0x12, -3480, 0, 2530, 340)
    SetChrPos(0x13, -2870, 0, -3210, 290)
    SetChrPos(0x14, -5740, 0, 3660, 70)
    SetChrPos(0x15, -4630, 0, 2520, 25)
    SetChrPos(0x16, 5000, 0, 2290, 270)
    SetChrPos(0x8, 3180, 0, 9920, 308)
    SetChrPos(0x9, 1230, 0, 9680, 0)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 680, 0, 3780, 25)
    SetChrChipByIndex(0x1E, 0x26)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 820, 0, 7140, 160)
    SetChrChipByIndex(0x1F, 0x27)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -200, 0, 4660, 70)
    SetChrChipByIndex(0x20, 0x28)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -6170, 0, -3230, 70)
    SetChrChipByIndex(0x21, 0x29)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, -3630, 0, -4340, 335)
    SetChrChipByIndex(0x22, 0x2A)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -5180, 0, -4080, 25)
    SetChrChipByIndex(0x23, 0x2B)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, -6160, 0, -1580, 115)
    BeginChrThread(0x1D, 0, 0, 0)
    BeginChrThread(0x1E, 0, 0, 0)
    BeginChrThread(0x1F, 0, 0, 0)
    BeginChrThread(0x20, 0, 0, 0)
    BeginChrThread(0x21, 0, 0, 0)
    BeginChrThread(0x22, 0, 0, 0)
    BeginChrThread(0x23, 0, 0, 0)
    BeginChrThread(0x1A, 0, 0, 0)
    BeginChrThread(0x1B, 0, 0, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1460, 880, 10670, 180)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -3880, 0, 8840, 180)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -4600, 0, -520, 180)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3140, 0, 6130, 245)
    SetChrChipByIndex(0xD, 0x5)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -2290, 0, 4950, 245)
    BeginChrThread(0x18, 0, 0, 0)
    BeginChrThread(0x1C, 0, 0, 0)
    BeginChrThread(0x19, 0, 0, 0)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -4880, 0, 5930, 155)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -230, 0, 6070, 110)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -2790, 0, -1720, 245)
    OP_4B(0xE, 0xFF)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2900, 0, -2250, 290)
    SetChrPos(0x101, 3000, 0, -1000, 245)
    SetChrPos(0x102, 2000, 0, -3250, 335)
    SetChrPos(0x103, 550, 0, -3270, 20)
    SetChrPos(0x104, -400, 0, -2400, 65)
    SetChrPos(0x109, -550, 0, -970, 110)
    SetChrPos(0x105, 600, 0, 100, 155)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x1A, -5310, 0, 8840, 180)
    PlayBGM("ed7162", 0)
    Sound(821, 2, 60, 0)
    Sound(877, 2, 60, 0)
    FadeToBright(2000, 0)
    OP_68(-1240, 2250, 12460, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(29120, 0)
    Sleep(2000)
    OP_68(-1980, 1500, 6460, 10000)
    MoveCamera(62, 23, 0, 10000)
    OP_6E(380, 10000)
    Sleep(10000)
    Fade(500)
    OP_68(-5990, 1500, 630, 0)
    MoveCamera(47, 23, 0, 0)
    OP_6E(280, 0)
    SetCameraDistance(29120, 0)
    OP_63(0x17, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(2000)
    OP_95(0x17, -6030, 0, 980, 3000, 0x0)
    OP_95(0x17, -7300, 0, 1270, 3000, 0x0)
    Sleep(1000)
    OP_63(0x17, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(2000)

    def lambda_2927():
        OP_95(0xFE, -8350, 0, 6120, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2927)
    Sleep(1000)
    Fade(500)
    OP_68(1040, 1700, -1990, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21120, 0)
    OP_0D()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00003F唔……莉丝小姐\x01",
            "一直在边吃边走呢。\x02\x03",

            "#00012F她穿着修女服，\x01",
            "似乎显得异常显眼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        (
            "#00109F呵呵……是啊。\x02\x03",

            "#00102F不过，这里的料理\x01",
            "确实很美味呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        (
            "#00302F听说市内各家饮食店\x01",
            "都为这个活动提供了料理。\x02\x03",

            "#00309F那边还有『龙老饭店』\x01",
            "的超辣麻婆豆腐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x109,
        (
            "#10109F哦哦！那可一定\x01",
            "要去吃啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xE,
        (
            "呵呵……\x01",
            "你们的关系真亲密啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2AC6():

        label("loc_2AC6")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_2AC6")

    QueueWorkItem2(0x109, 0, lambda_2AC6)

    def lambda_2AD8():

        label("loc_2AD8")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_2AD8")

    QueueWorkItem2(0x102, 0, lambda_2AD8)

    def lambda_2AEA():

        label("loc_2AEA")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_2AEA")

    QueueWorkItem2(0x104, 0, lambda_2AEA)

    def lambda_2AFC():

        label("loc_2AFC")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_2AFC")

    QueueWorkItem2(0x101, 0, lambda_2AFC)

    def lambda_2B0E():

        label("loc_2B0E")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_2B0E")

    QueueWorkItem2(0x105, 0, lambda_2B0E)

    def lambda_2B20():

        label("loc_2B20")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_2B20")

    QueueWorkItem2(0x103, 0, lambda_2B20)

    #C0120
    ChrTalk(
        0xE,
        (
            "料理如此美味，\x01",
            "活动肯定也会大获成功吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x105,
        (
            "#10304F呵呵……\x01",
            "但愿别出现什么意外。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#00006F喂喂……\x01",
            "这可是难得的慈善宴会，\x01",
            "不要说那种不吉利的话啊。\x02\x03",

            "#00000F话说回来，\x01",
            "前辈竟然也会来参加\x01",
            "职业女性选秀活动啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#00200F警察总部刚刚遭受过袭击，\x01",
            "应该非常忙吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xE,
        (
            "唔，这个嘛……\x01",
            "在刚刚接到邀请的时候，\x01",
            "我也很拿不定主意。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xE,
        (
            "但乔里基科长\x01",
            "劝说我一定要\x01",
            "参加。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#00102F呵呵，是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xE,
        (
            "在这种时期，\x01",
            "我们也想以这种贴近市民\x01",
            "的形式来做些什么呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xE,
        (
            "呵呵，从某种意义上说，\x01",
            "似乎是在模仿你们支援科了。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，哪里的话，\x01",
            "我们可没有那么了不起……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(803, 2, 100, 0)
    Sleep(500)

    #C0130
    ChrTalk(
        0xE,
        (
            "啊……是我的。\x01",
            "不好意思啊，我接一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0xE, 4600, 0, -1680, 2000, 0x0)
    OP_93(0xE, 0xB4, 0x1F4)
    OP_0D()
    Fade(250)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0xE, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0131
    ChrTalk(
        0xE,
        (
            "您好，我是凯特巡警……\x01",
            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xE,
        (
            "……好的、好的……\x01",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xE,
        (
            "……是吗，我明白了。\x01",
            "马上就会过去。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0xE, 0x20)
    ClearChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(150)
    OP_95(0xE, 2900, 0, -2250, 2000, 0x0)

    #C0134
    ChrTalk(
        0x101,
        "#00005F凯特前辈，刚才那是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)

    #C0135
    ChrTalk(
        0xE,
        (
            "嗯……\x01",
            "很抱歉，我突然接到了\x01",
            "一件紧急工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xE,
        (
            "虽然很不好意思，\x01",
            "但我不能参加\x01",
            "职业女性选秀活动了……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        (
            "#00306F呜哇……不是开玩笑吧！\x02\x03",

            "#00301F不过……既然有工作，那也没办法了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x104, 500)

    #C0138
    ChrTalk(
        0xE,
        (
            "抱歉啊，\x01",
            "我必须要立刻过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xE,
        (
            "请各位代我向\x01",
            "洛依先生道个歉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#00000F嗯，知道了。\x01",
            "您辛苦了，前辈。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xE,
        "辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_68(760, 1700, -3000, 3000)
    BeginChrThread(0xE, 3, 0, 25)
    Sleep(4000)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x103, 0x0)
    OP_4B(0x1B, 0xFF)
    BeginChrThread(0x1B, 3, 0, 26)

    #C0142
    ChrTalk(
        0x102,
        (
            "#00106F唉，本想和她\x01",
            "再聊几句呢，\x01",
            "真是遗憾啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#00003F是啊……\x02",
    )

    CloseMessageWindow()
    OP_68(1040, 1700, -1990, 2000)
    MoveCamera(38, 23, 0, 2000)
    WaitChrThread(0x1B, 3)
    OP_6F(0x79)

    #C0144
    ChrTalk(
        0x1B,
        (
            "嘿，各位，\x01",
            "玩得还开心吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30D3():

        label("loc_30D3")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_30D3")

    QueueWorkItem2(0x109, 0, lambda_30D3)

    def lambda_30E5():

        label("loc_30E5")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_30E5")

    QueueWorkItem2(0x102, 0, lambda_30E5)

    def lambda_30F7():

        label("loc_30F7")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_30F7")

    QueueWorkItem2(0x104, 0, lambda_30F7)

    def lambda_3109():

        label("loc_3109")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_3109")

    QueueWorkItem2(0x101, 0, lambda_3109)

    def lambda_311B():

        label("loc_311B")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_311B")

    QueueWorkItem2(0x105, 0, lambda_311B)

    def lambda_312D():

        label("loc_312D")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_312D")

    QueueWorkItem2(0x103, 0, lambda_312D)

    #C0145
    ChrTalk(
        0x1B,
        (
            "职业女性选秀活动马上就要开始了，\x01",
            "能帮我和各位参加者打个招呼，\x01",
            "让她们现在到后台去吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x1B,
        (
            "……嗯？哎？\x01",
            "那位女警怎么不见了？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        "#00005F那个，是这样的……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将凯特突然接到紧急工作\x01",
            "而离开的情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x103, 0x0)

    #C0149
    ChrTalk(
        0x1B,
        "什、什么～！？\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x1B,
        (
            "唔～这可伤脑筋了。\x01",
            "该怎么办才好呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1B)
    OP_63(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x1B,
        "……对了！\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x1B,
        (
            "你们能不能派出一个人，\x01",
            "代替她担当『女警』的人选？\x02",
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0153
    ChrTalk(
        0x101,
        "#00011F哎哎……！\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x103,
        "#00205F要我们去……？\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，这不是很有趣嘛。\x02\x03",

            "机会难得，\x01",
            "试试看也无妨啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x109,
        "#10106F前、前辈，你不要这么一副事不关己的口气……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x1B,
        "拜、拜托了！\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x1B,
        (
            "这场慈善宴会的目的不仅是\x01",
            "为了支援复兴重建工作，\x01",
            "还包含让大家振奋精神的用意在内。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x1B,
        (
            "就算是为了克洛斯贝尔的广大市民……\x01",
            "请各位一定要帮帮忙！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x109)

    #C0160
    ChrTalk(
        0x102,
        (
            "#00106F……呼，说的也是啊。\x02\x03",

            "#00100F各位，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x103,
        "#00203F……没有异议。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x109,
        (
            "#10100F我的本职其实是警备队成员，\x01",
            "如果可以的话……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x1B,
        "谢、谢谢！\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x1B,
        (
            "那么……\x01",
            "要由谁来参加呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0165
    ChrTalk(
        0x104,
        (
            "#00309F好，罗伊德，\x01",
            "赶快选吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3618():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3618)

    def lambda_3625():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3625)

    def lambda_3632():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3632)

    def lambda_363F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_363F)
    TurnDirection(0x101, 0x104, 500)

    #C0166
    ChrTalk(
        0x101,
        "#00011F让、让我选吗！？\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，身为支援科的队长，\x01",
            "这自然是你的义务。\x02\x03",

            "#10302F好啦，赶快做出合理决定吧，\x01",
            "时间已经不多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#00006F说、说的对啊……\x02\x03",

            "#00003F嗯，那么……\x01",
            "职业女性选秀活动就由……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FFB")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "由谁来参加职业女性选秀活动？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "罗伊德")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_378D")
    MenuCmd(3, 0, 0x0)

    label("loc_378D")

    MenuCmd(1, 0, "艾莉")
    MenuCmd(1, 0, "缇欧")
    MenuCmd(1, 0, "兰迪")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_37B2")
    MenuCmd(3, 0, 0x3)

    label("loc_37B2")

    MenuCmd(1, 0, "诺艾尔")
    MenuCmd(1, 0, "瓦吉")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_37D1")
    MenuCmd(3, 0, 0x5)

    label("loc_37D1")

    MenuCmd(2, 0, -1, 80, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_381A"),
        (3, "loc_3980"),
        (5, "loc_3B14"),
        (1, "loc_3D19"),
        (2, "loc_3E07"),
        (4, "loc_3EF5"),
        (SWITCH_DEFAULT, "loc_3FF6"),
    )


    label("loc_381A")

    TurnDirection(0x101, 0x104, 500)

    #C0170
    ChrTalk(
        0x101,
        (
            "#00001F……明白了，\x01",
            "既然如此，那就由我去吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3858():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3858)

    def lambda_3865():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3865)

    def lambda_3872():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3872)

    def lambda_387F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_387F)

    def lambda_388C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_388C)

    #C0171
    ChrTalk(
        0x102,
        "#00105F哎……罗伊德！？\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x103,
        "#00205F……你打算换上女装吗？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        "#00309F哎呀呀，说不定会很合适呢。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x105,
        (
            "#10306F唔，感觉很微妙啊。\x02\x03",

            "#10300F你的肩比较宽，如果想扮女装，\x01",
            "恐怕还要稍微花些工夫……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x109,
        "#10114F（心跳加快……）\x02",
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 0)
    Jump("loc_3FF6")

    label("loc_3980")

    TurnDirection(0x101, 0x104, 500)

    #C0176
    ChrTalk(
        0x101,
        (
            "#00001F……兰迪，\x01",
            "你去参加如何？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_39B2():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_39B2)

    def lambda_39BF():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_39BF)

    def lambda_39CC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_39CC)

    def lambda_39D9():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_39D9)

    def lambda_39E6():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_39E6)

    #C0177
    ChrTalk(
        0x104,
        "#00305F……你、你是认真的吗？\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        "#00101F兰、兰迪……？\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#00211F……脑中浮现出了\x01",
            "很糟糕的画面。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x105,
        (
            "#10306F唔，依靠化妆与服饰，\x01",
            "说不定也可以打扮成\x01",
            "男装丽人的形象呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x109,
        (
            "#10106F那终究还是太乱来了吧……\x01",
            "毕竟前辈的体格那么魁梧。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x104,
        (
            "#00306F唉……\x01",
            "说了半天，我还是不行啊。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FF6")

    label("loc_3B14")

    TurnDirection(0x101, 0x105, 500)

    #C0183
    ChrTalk(
        0x101,
        (
            "#00001F……瓦吉，\x01",
            "你去参加如何？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B46():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3B46)

    def lambda_3B53():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3B53)

    def lambda_3B60():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3B60)

    def lambda_3B6D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3B6D)

    def lambda_3B7A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3B7A)

    #C0184
    ChrTalk(
        0x105,
        (
            "#10302F呵呵……\x01",
            "我倒是不介意哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        (
            "#00105F等、等一下，瓦吉，\x01",
            "你为什么不拒绝啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x105,
        (
            "#10309F因为听起来\x01",
            "好像很有趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x109,
        (
            "#10101F罗伊德警官，你这是什么意思！\x02\x03",

            "难、难得你觉得\x01",
            "我们的魅力全都\x01",
            "比不上瓦吉吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        "#00011F并、并不是那个意思……\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，但从某种意义上说，\x01",
            "这似乎也没说错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        (
            "#00203F……兰迪前辈，\x01",
            "你是想主动沉默，\x01",
            "还是想让我帮你沉默？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        "#00306F……对不起。\x02",
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 2)
    Jump("loc_3FF6")

    label("loc_3D19")

    TurnDirection(0x101, 0x102, 500)

    #C0192
    ChrTalk(
        0x101,
        (
            "#00000F……艾莉，\x01",
            "你去参加如何？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D4B():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3D4B)

    def lambda_3D58():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3D58)

    def lambda_3D65():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3D65)

    def lambda_3D72():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D72)

    def lambda_3D7F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3D7F)

    #C0193
    ChrTalk(
        0x102,
        (
            "#00112F我、我吗！？\x02\x03",

            "#00113F嗯……\x01",
            "好、好吧，我知道了。\x02\x03",

            "#00100F虽然有点不好意思……\x01",
            "但我会努力的。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x6)
    SetScenarioFlags(0x19A, 1)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3FF6")

    label("loc_3E07")

    TurnDirection(0x101, 0x103, 500)

    #C0194
    ChrTalk(
        0x101,
        (
            "#00000F……缇欧，\x01",
            "你去参加如何？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E39():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E39)

    def lambda_3E46():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3E46)

    def lambda_3E53():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3E53)

    def lambda_3E60():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E60)

    def lambda_3E6D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3E6D)

    #C0195
    ChrTalk(
        0x103,
        (
            "#00205F我、我吗……\x02\x03",

            "#00204F………………\x01",
            "知、知道了。\x02\x03",

            "#00201F虽然多少有些不好意思，\x01",
            "但我会尽力的。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x7)
    SetScenarioFlags(0x19A, 2)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3FF6")

    label("loc_3EF5")

    TurnDirection(0x101, 0x109, 500)

    #C0196
    ChrTalk(
        0x101,
        (
            "#00000F……诺艾尔，\x01",
            "你去参加如何？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F29():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F29)

    def lambda_3F36():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3F36)

    def lambda_3F43():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3F43)

    def lambda_3F50():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3F50)

    def lambda_3F5D():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3F5D)

    #C0197
    ChrTalk(
        0x109,
        (
            "#10114F要、要我去吗！？\x01",
            "唔……\x02\x03",

            "#10103F……明、明白了！\x02\x03",

            "#10102F虽然很不习惯\x01",
            "参加这样的活动……\x01",
            "但我一定会尽力而为！\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x8)
    SetScenarioFlags(0x19A, 3)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3FF6")

    label("loc_3FF6")

    Jump("loc_3722")

    label("loc_3FFB")


    #C0198
    ChrTalk(
        0x104,
        (
            "#00302F哈哈，站到台上之后，\x01",
            "说不定就会找到感觉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x105,
        (
            "#10304F不过，这和战斗、搜查时的紧张感\x01",
            "还是有本质差别的。\x02\x03",

            "#10302F另外，由于没有穿着制服，\x01",
            "在选秀时恐怕会处于不利地位。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x1B,
        (
            "算啦，作为『便衣警察』的话，\x01",
            "也还算可以吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x1B,
        "不过，没能看到制服女警形象……真遗憾啊。\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#00012F（他对这种奇怪的问题相当执著啊……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_41E0")

    #C0203
    ChrTalk(
        0x109,
        (
            "#10102F总之，现在还是专心考虑\x01",
            "如何才能使活动顺利成功吧！\x02\x03",

            "#10109F加油啊，艾莉小姐！\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x103,
        "#00202F呵呵，加油。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x102,
        "#00102F嗯，我一定尽力而为。\x02",
    )

    CloseMessageWindow()
    Jump("loc_432B")

    label("loc_41E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_4289")

    #C0206
    ChrTalk(
        0x102,
        (
            "#00102F总之，现在还是先考虑\x01",
            "如何才能使活动顺利成功吧。\x02\x03",

            "#00109F加油啊，缇欧。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x109,
        "#10109F呵呵，我也会为你加油的！\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x103,
        "#00201F嗯，我一定会尽力而为。\x02",
    )

    CloseMessageWindow()
    Jump("loc_432B")

    label("loc_4289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_432B")

    #C0209
    ChrTalk(
        0x103,
        (
            "#00204F总之，现在就专心考虑\x01",
            "如何才能使活动顺利成功吧。\x02\x03",

            "#00202F诺艾尔小姐，请加油。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x102,
        "#00109F呵呵，我也会给你助威的。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x109,
        "#10101F嗯，一定努力！\x02",
    )

    CloseMessageWindow()

    label("loc_432B")


    #C0212
    ChrTalk(
        0x1B,
        (
            "好了，时间已经所剩不多啦，\x01",
            "请到后台听取活动流程！\x02",
        )
    )

    CloseMessageWindow()
    StopSound(821, 2000, 50)
    StopSound(877, 2000, 50)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    OP_24(0x323)
    OP_24(0x335)
    OP_24(0x36D)
    Call(0, 28)
    Return()

    # Function_24_23D3 end

    def Function_25_438C(): pass

    label("Function_25_438C")

    OP_95(0xFE, 3050, 0, -3910, 3000, 0x0)
    OP_95(0xFE, 1400, 0, -4710, 3000, 0x0)
    OP_95(0xFE, -1250, 0, -5460, 3000, 0x0)
    OP_95(0xFE, -940, 130, -7420, 3000, 0x0)
    OP_95(0xFE, 3690, 3560, -7710, 3000, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_438C end

    def Function_26_43F6(): pass

    label("Function_26_43F6")

    SetChrPos(0xFE, -3350, 0, 1340, 0)
    OP_95(0xFE, 1650, 0, 1870, 2000, 0x0)
    OP_95(0xFE, 3130, 0, 520, 2000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_26_43F6 end

    def Function_27_4437(): pass

    label("Function_27_4437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4472")

    #C0213
    ChrTalk(
        0x1B,
        (
            "喂喂！你们为何要\x01",
            "认真讨论这种事情！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4488")

    label("loc_4472")


    #C0214
    ChrTalk(
        0x1B,
        "都～说～过～了！\x02",
    )

    CloseMessageWindow()

    label("loc_4488")


    #C0215
    ChrTalk(
        0x1B,
        (
            "这是职业女性选秀活动！\x01",
            "男人是不能出场的！！\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x1B,
        (
            "就是这样，赶快选\x01",
            "其他人吧！！\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#00011F明、明白了。\x02\x03",

            "#00008F嗯，那么，\x01",
            "职业女性选秀活动就由……\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_27_4437 end

    def Function_28_4522(): pass

    label("Function_28_4522")

    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0x18, 0xFF)
    EndChrThread(0x1C, 0xFF)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0x1A, 0xFF)
    SetChrPos(0xC, -4460, 750, 16000, 180)
    SetChrPos(0xD, -3460, 750, 16000, 180)
    SetChrPos(0x18, -2460, 750, 16000, 180)
    SetChrPos(0x1C, -1460, 750, 16000, 180)
    SetChrPos(0x19, -460, 750, 16000, 180)
    SetChrPos(0x17, 540, 750, 16000, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_45DD")
    LoadChrToIndex("chr/ch00155.itc", 0x1E)
    SetChrPos(0x102, 1540, 750, 16000, 180)
    Jump("loc_4622")

    label("loc_45DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_4602")
    LoadChrToIndex("chr/ch00255.itc", 0x1E)
    SetChrPos(0x103, 1540, 750, 16000, 180)
    Jump("loc_4622")

    label("loc_4602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_4622")
    LoadChrToIndex("chr/ch02955.itc", 0x1E)
    SetChrPos(0x109, 1540, 750, 16000, 180)

    label("loc_4622")

    SetChrFlags(0xF, 0x80)
    SetMapObjFlags(0x1, 0x4)
    OP_68(-1310, 7400, 11320, 0)
    MoveCamera(0, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19820, 0)
    OP_68(-1310, 2500, 11320, 5000)
    MoveCamera(0, 11, 0, 5000)
    SetCameraDistance(20760, 5000)
    FadeToBright(2000, 0)
    SetChrPos(0x1B, -5720, 750, 13840, 180)
    OP_95(0x1B, -1530, 750, 12520, 2000, 0x0)
    OP_93(0x1B, 0xB4, 0x12C)
    OP_95(0x1B, -1520, 880, 10600, 1000, 0x0)
    OP_6F(0x79)

    #C0218
    ChrTalk(
        0x1B,
        "女士们！先生们！\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x1B,
        (
            "让大家久等了。\x01",
            "今天的重头戏──\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x1B,
        (
            "『克洛斯贝尔职业女性选秀活动\x01",
            "  　～劳动中的女性最美丽～　』\x01",
            "——即将开始！！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    Sleep(1500)

    #C0221
    ChrTalk(
        0x1B,
        (
            "那么，首先由我来说明\x01",
            "本次选秀的流程。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x1B,
        (
            "接下来，各位参选者\x01",
            "将会逐一上前，\x01",
            "讲出富有魅力的代表性台词。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x1B,
        (
            "代表性台词可以是\x01",
            "在工作中所使用的寒暄语，\x01",
            "或是做生意时的招呼语等等。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x1B,
        (
            "请各位观众以此为参考，\x01",
            "将你们心中最富魅力的女性\x01",
            "的姓名书写在手边的投票纸上。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x1B,
        (
            "得票数最多的女性\x01",
            "将会获得『克洛斯贝尔小姐』\x01",
            "这一称号！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    #C0226
    ChrTalk(
        0x1B,
        (
            "好，\x01",
            "那我们就赶快开始吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x1B,
        (
            "展示时间……\x01",
            "正式～～开始！\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    Fade(500)
    OP_68(-1450, 2250, 14880, 0)
    MoveCamera(1, 11, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18000, 0)
    OP_95(0x1B, -2180, 750, 13210, 3000, 0x0)
    OP_95(0x1B, -5730, 750, 13620, 3000, 0x0)
    OP_93(0x1B, 0x5A, 0x1F4)
    Sleep(500)

    #C0228
    ChrTalk(
        0x1B,
        "首先是一号参赛选手！\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x1B,
        (
            "『时代』百货店的招牌店员，\x01",
            "清纯可爱的百货店导购──\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x1B,
        "辛茜亚小姐！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 0, 0, 29)
    WaitChrThread(0xC, 0)

    #C0231
    ChrTalk(
        0xC,
        "欢迎光临『时代』百货店。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xC,
        (
            "如果您遇到了什么问题，\x01",
            "请不必客气，尽管向我咨询。\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0xC, 0, 0, 31)
    Sleep(1000)

    #C0233
    ChrTalk(
        0x1B,
        "太棒了！\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x1B,
        (
            "恐怕已经有很多人\x01",
            "被她那清纯的气质\x01",
            "彻底征服了吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x1B,
        (
            "顺便一说，她现在好像还是单身！\x01",
            "究竟哪位幸运儿可以获得\x01",
            "辛茜亚小姐的垂青呢！？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0)

    #C0236
    ChrTalk(
        0x1B,
        (
            "好，让我们继续吧！\x01",
            "接下来是二号参赛选手！\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x1B,
        (
            "在后巷翩翩起舞的夜之蝶，\x01",
            "绽放着妖艳魅力的蔷薇──\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x1B,
        "爱丽斯小姐！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 0, 0, 29)
    WaitChrThread(0xD, 0)

    #C0239
    ChrTalk(
        0xD,
        (
            "多谢指名～！\x01",
            "我是只属于您的爱丽斯～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xD,
        (
            "今天也要多喝几杯哟！\x01",
            "──啾⊥\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0xD, 0, 0, 32)
    Sleep(1000)

    #C0241
    ChrTalk(
        0x1B,
        (
            "噢噢噢！\x01",
            "竟然向大家投来飞吻！\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x1B,
        (
            "可以与爱丽斯小姐一起饮酒的店\x01",
            "好像是在后巷！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x1B,
        (
            "不过，只有成年之后才可以喝酒哦！\x01",
            "请牢记这一点！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 0)

    #C0244
    ChrTalk(
        0x1B,
        (
            "那么，继续有请\x01",
            "三号参赛选手登场！\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x1B,
        (
            "东街知名老店『龙老饭店』的店员，\x01",
            "由东方飘然而至的天使──\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x1B,
        "桑桑小姐！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x18, 0, 0, 29)
    WaitChrThread(0x18, 0)

    #C0247
    ChrTalk(
        0x18,
        (
            "客人您好～！\x01",
            "欢迎光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x18,
        (
            "爸爸做的料理是天下一流的哦～\x01",
            "请多点一些吧～⊥\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x18, 0, 0, 33)
    Sleep(1000)

    #C0249
    ChrTalk(
        0x1B,
        (
            "出现了！\x01",
            "看啊！这纯真自然的笑容！\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x1B,
        (
            "招牌店员桑桑小姐\x01",
            "在东街可是个名人！\x01",
            "连我都是她的倾慕者！\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x1B,
        (
            "不过呢，如果对桑桑小姐有非分之想，\x01",
            "她的父亲强霍先生可是绝不会饶恕的！\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x1B,
        (
            "如果能拿出舍弃性命的觉悟，\x01",
            "就去挑战一下吧！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 0)

    #C0253
    ChrTalk(
        0x1B,
        (
            "好，出场选手即将过半，\x01",
            "接下来有请四号参赛选手登场！\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x1B,
        (
            "来自导力商店『原点』的导力器专家，\x01",
            "美丽的女性技师──\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x1B,
        "温蒂小姐！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1C, 0, 0, 29)
    WaitChrThread(0x1C, 0)

    #C0256
    ChrTalk(
        0x1C,
        (
            "……唔，咳咳。\x01",
            "我不擅长说什么\x01",
            "漂亮话……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x1C,
        (
            "不过，如果您的导力器坏了，\x01",
            "随时都可以来找我修哦！\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x1C, 0, 0, 34)
    Sleep(1000)

    #C0258
    ChrTalk(
        0x1B,
        (
            "太可靠了！\x01",
            "这也可以算是她的\x01",
            "个性与独有魅力吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x1B,
        (
            "请各位不要为了创造\x01",
            "与她见面的机会，\x01",
            "故意将导力器损坏哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x1B,
        (
            "如果那样做，一定会被她\x01",
            "用扳手狠狠修理一顿的！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1C, 0)

    #C0261
    ChrTalk(
        0x1B,
        (
            "好了好了，不知不觉间，\x01",
            "就要轮到第五位参赛选手登场了！\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x1B,
        (
            "在克洛斯贝尔自治州议会首领\x01",
            "亨利·麦克道尔议长的官邸\x01",
            "任职的优秀女仆──\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x1B,
        "乔安娜小姐！\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x19, 0, 0, 30)
    WaitChrThread(0x19, 0)
    OP_64(0x19)

    #C0264
    ChrTalk(
        0x19,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x19,
        (
            "………………那、那个…………\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x19)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0266
    ChrTalk(
        0x19,
        (
            "欢、欢迎您回来，主人。\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x19,
        "…………………失、失礼了。\x02",
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x19, 0, 0, 35)
    Sleep(1000)

    #C0268
    ChrTalk(
        0x1B,
        "噢、噢噢噢噢噢……！\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x1B,
        (
            "不知为何，心情瞬间变得无比爽快！\x01",
            "这样的女仆小姐真是很棒啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x1B,
        (
            "在座的诸位之中，\x01",
            "恐怕已经有人开始\x01",
            "嫉恨麦克道尔议长了吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_524A")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_524A")

    Sleep(1000)
    WaitChrThread(0x19, 0)

    #C0271
    ChrTalk(
        0x1B,
        (
            "好了，终于要临近尾声了！\x01",
            "六号参赛选手！\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x1B,
        (
            "气质清圣，忠于空之女神的\x01",
            "大圣堂新到修女──\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x1B,
        "莉丝小姐！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x17, 0, 0, 30)
    WaitChrThread(0x17, 0)
    Fade(250)
    Sound(802, 0, 90, 0)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    OP_A1(0x17, 0x5DC, 0x4, 0x3, 0x2, 0x1, 0x0)
    Sleep(500)

    #A0274
    AnonymousTalk(
        0x17,
        (
            "七耀的教诲\x01",
            "常存于大家的心中。\x02\x03",

            "愿各位获得女神的保佑与引导……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x17, 0xF)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    Sleep(500)
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x17, 0, 0, 36)
    Sleep(1000)

    #C0275
    ChrTalk(
        0x1B,
        (
            "哦哦、哦哦哦哦……！\x01",
            "这是何等圣洁的姿态！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x1B,
        (
            "和之前在立餐宴会上\x01",
            "到处游荡的样子相比，\x01",
            "简直就是判若两人啊！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 0)

    #C0277
    ChrTalk(
        0x1B,
        (
            "接下来，终于要轮到最后一位了！\x01",
            "七号参赛选手！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_5463")

    #C0278
    ChrTalk(
        0x1B,
        (
            "隶属于警察局·特别任务支援科，\x01",
            "名门出身的美丽大小姐──\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x1B,
        "艾莉·麦克道尔小姐！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5524")

    label("loc_5463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_54C0")

    #C0280
    ChrTalk(
        0x1B,
        (
            "隶属于警察局·特别任务支援科，\x01",
            "气质沉静的少女──\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x1B,
        "缇欧·普拉托小姐！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5524")

    label("loc_54C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_5524")

    #C0282
    ChrTalk(
        0x1B,
        (
            "暂时调任至警察局·特别任务支援科，\x01",
            "规矩有礼的女性警备队员──\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x1B,
        "诺艾尔·希卡小姐！\x02",
    )

    CloseMessageWindow()

    label("loc_5524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_553C")
    BeginChrThread(0x102, 0, 0, 30)
    WaitChrThread(0x102, 0)
    Jump("loc_5567")

    label("loc_553C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_5554")
    BeginChrThread(0x103, 0, 0, 30)
    WaitChrThread(0x103, 0)
    Jump("loc_5567")

    label("loc_5554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_5567")
    BeginChrThread(0x109, 0, 0, 30)
    WaitChrThread(0x109, 0)

    label("loc_5567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_5718")

    #C0284
    ChrTalk(
        0x102,
        (
            "#00105F（那个……\x01",
            "  好像必须要说几句\x01",
            "  代表性台词呢。）\x02\x03",

            "#00103F（该说什么好呢？）\x02",
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
            "逮捕宣言\x01",          # 0
            "射击后的自白\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x102, 0x2)
    OP_A1(0x102, 0x640, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 100, 0)
    OP_A1(0x102, 0x640, 0x6, 0x0, 0x0, 0x3, 0x4, 0x5, 0x6)
    OP_A1(0x102, 0x640, 0x8, 0x7, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5670"),
        (1, "loc_56BE"),
        (SWITCH_DEFAULT, "loc_5713"),
    )


    label("loc_5670")

    SetScenarioFlags(0x19A, 4)

    #C0285
    ChrTalk(
        0x102,
        (
            "#00107F举起手来！\x02\x03",

            "根据自治州法，你涉嫌\x01",
            "多项罪名，在此将你逮捕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5713")

    label("loc_56BE")


    #C0286
    ChrTalk(
        0x102,
        (
            "#00104F呼……百发百中啊。\x02\x03",

            "#00101F如果你认为自己能逃掉，那可就大错特错了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5713")

    label("loc_5713")

    Jump("loc_5ACF")

    label("loc_5718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_590A")

    #C0287
    ChrTalk(
        0x103,
        (
            "#00200F（那么……\x01",
            "  好像是要说几句\x01",
            "  代表性台词吧。）\x02\x03",

            "#00203F（该说什么呢？）\x02",
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
            "逮捕宣言\x01",                  # 0
            "启动永世系统时的自白\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x103, 0x2)
    OP_A1(0x103, 0x640, 0x3, 0x0, 0x1, 0x2)
    Sound(533, 0, 80, 0)
    OP_A1(0x103, 0x640, 0x5, 0x3, 0x4, 0x5, 0x6, 0x7)
    OP_A1(0x103, 0x640, 0x3, 0x8, 0x9, 0xA)
    Sound(337, 0, 70, 0)
    OP_A1(0x103, 0x640, 0x5, 0xB, 0xC, 0xD, 0xE, 0xF)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5836"),
        (1, "loc_589E"),
        (SWITCH_DEFAULT, "loc_5905"),
    )


    label("loc_5836")

    SetScenarioFlags(0x19A, 4)

    #C0288
    ChrTalk(
        0x103,
        (
            "#00203F信息收集完毕。\x01",
            "犯人……就是你。\x02\x03",

            "#00201F你已经无处可逃了，\x01",
            "老老实实地跟我一起走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5905")

    label("loc_589E")


    #C0289
    ChrTalk(
        0x103,
        (
            "#00203F『永世系统』启动……\x01",
            "高速展开导力力场。\x02\x03",

            "#00201F就让你好好尝尝\x01",
            "这把魔导杖的性能吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5905")

    label("loc_5905")

    Jump("loc_5ACF")

    label("loc_590A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_5ACF")

    #C0290
    ChrTalk(
        0x109,
        (
            "#10105F（那个……\x01",
            "  好像是必须要说几句\x01",
            "  代表性台词吧。）\x02\x03",

            "#10103F（要说什么呢？）\x02",
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
            "逮捕宣言\x01",          # 0
            "警备队的号令\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x109, 0x2)
    OP_A1(0x109, 0x640, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 100, 0)
    OP_A1(0x109, 0x640, 0x5, 0x3, 0x3, 0x4, 0x5, 0x6)
    OP_A1(0x109, 0x640, 0x5, 0x7, 0x7, 0x8, 0x9, 0xA)
    Sound(590, 0, 100, 0)
    OP_A1(0x109, 0x640, 0x5, 0xB, 0xC, 0xD, 0xC, 0xB)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5A20"),
        (1, "loc_5A75"),
        (SWITCH_DEFAULT, "loc_5ACF"),
    )


    label("loc_5A20")

    SetScenarioFlags(0x19A, 4)

    #C0291
    ChrTalk(
        0x109,
        (
            "#10101F你已经被彻底包围了……\x01",
            "没有任何可逃之处！\x02\x03",

            "#10107F请赶快投降吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ACF")

    label("loc_5A75")


    #C0292
    ChrTalk(
        0x109,
        (
            "#10101F目标：迎击敌人的机甲部队，\x01",
            "营救陷入孤立的补给部队！\x02\x03",

            "#10107F战斗开始！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ACF")

    label("loc_5ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_5B2D")
    Sound(819, 0, 100, 0)
    Sound(820, 0, 100, 0)

    #C0293
    ChrTalk(
        0x1B,
        (
            "哦哦……\x01",
            "噢噢！！\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x1B,
        (
            "太棒了，让我们充分\x01",
            "见识到了女警的风采！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B7B")

    label("loc_5B2D")

    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)

    #C0295
    ChrTalk(
        0x1B,
        (
            "哦哦……\x01",
            "噢噢！！\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x1B,
        (
            "那个……让我们\x01",
            "见识到了很棒的一面呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_5BD8")

    #C0297
    ChrTalk(
        0x102,
        (
            "#00106F（唔、唔……\x01",
            "  似乎应该说些\x01",
            "  更有警察风格的台词啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C68")

    label("loc_5BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_5C20")

    #C0298
    ChrTalk(
        0x103,
        (
            "#00206F（……看来应该说些\x01",
            "  更有警察风格的台词呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C68")

    label("loc_5C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_5C68")

    #C0299
    ChrTalk(
        0x109,
        (
            "#10106F（糟糕……\x01",
            "  本应说些\x01",
            "  更有警察风格的台词啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_5C93")
    Fade(250)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    BeginChrThread(0x102, 0, 0, 37)
    WaitChrThread(0x102, 0)
    Jump("loc_5CE4")

    label("loc_5C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_5CBE")
    Fade(250)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    BeginChrThread(0x103, 0, 0, 37)
    WaitChrThread(0x103, 0)
    Jump("loc_5CE4")

    label("loc_5CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_5CE4")
    Fade(250)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    BeginChrThread(0x109, 0, 0, 37)
    WaitChrThread(0x109, 0)

    label("loc_5CE4")


    #C0300
    ChrTalk(
        0x1B,
        (
            "好，七名参赛选手\x01",
            "已经全部亮相完毕！\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x1B,
        (
            "请再次向她们献上\x01",
            "热烈的掌声！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    Sound(821, 2, 60, 0)
    Sound(877, 2, 60, 0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，在场观众们参加了\x01",
            "职业女性选秀活动的投票。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0303
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在投票开始之前，莉丝修女\x01",
            "以自己不是克洛斯贝尔市民为由\x01",
            "谢绝了参加票选……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "优胜者将从莉丝修女\x01",
            "之外的参选者之中选出。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0305
    AnonymousTalk(
        0x101,
        (
            "#00000F（嗯，我的手中\x01",
            "  也有选票……\x01",
            "  不过，投给自己的同伴总有些不妥。）\x02\x03",

            "#00003F（……既然如此，要投给谁呢？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "投票给辛茜亚\x01",      # 0
            "投票给爱丽斯\x01",      # 1
            "投票给桑桑\x01",        # 2
            "投票给温蒂\x01",        # 3
            "投票给乔安娜\x01",      # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5F2D"),
        (1, "loc_5F63"),
        (2, "loc_5F99"),
        (3, "loc_5FCD"),
        (4, "loc_6001"),
        (SWITCH_DEFAULT, "loc_6037"),
    )


    label("loc_5F2D")


    #A0306
    AnonymousTalk(
        0x101,
        "#00002F（好……那就投票给辛茜亚吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x9)
    Jump("loc_6037")

    label("loc_5F63")


    #A0307
    AnonymousTalk(
        0x101,
        "#00002F（好……那就投票给爱丽斯吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xA)
    Jump("loc_6037")

    label("loc_5F99")


    #A0308
    AnonymousTalk(
        0x101,
        "#00002F（好……那就投票给桑桑吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xB)
    Jump("loc_6037")

    label("loc_5FCD")


    #A0309
    AnonymousTalk(
        0x101,
        "#00002F（好……那就投票给温蒂吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xC)
    Jump("loc_6037")

    label("loc_6001")


    #A0310
    AnonymousTalk(
        0x101,
        "#00002F（好……那就投票给乔安娜吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xD)
    Jump("loc_6037")

    label("loc_6037")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0311
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "随后……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-1450, 2250, 14880, 0)
    StopSound(821, 2000, 50)
    StopSound(877, 2000, 50)
    StopBGM(0x7D0)
    WaitBGM()
    MoveCamera(1, 11, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18000, 0)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0xF, 0x17, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1450, 880, 10860, 180)
    SetChrPos(0x1B, -190, 750, 13500, 180)
    FadeToBright(2000, 0)
    OP_0D()

    #C0312
    ChrTalk(
        0x1A,
        (
            "下面将为大家公布职业女性\x01",
            "选秀活动的投票结果，\x01",
            "相信在场的各位早已迫不及待了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x0, 0x1F4)
    OP_95(0x1A, -1450, 750, 12450, 2000, 0x0)
    OP_95(0x1A, 1620, 750, 12450, 2000, 0x0)
    OP_93(0x1A, 0xE0, 0x1F4)
    OP_95(0x1B, -1450, 750, 13500, 2000, 0x0)
    OP_93(0x1B, 0xB4, 0x12C)
    OP_95(0x1B, -1450, 880, 11370, 2000, 0x0)
    Sleep(1000)

    #C0313
    ChrTalk(
        0x1B,
        "在第一届克洛斯贝尔职业女性选秀活动中……\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x1B,
        "荣获优胜的是——\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(420, 1, 80, 0)
    SetChrFlags(0x101, 0x48)
    SetChrFlags(0x105, 0x48)
    BeginChrThread(0x101, 1, 0, 38)
    BeginChrThread(0x105, 1, 0, 38)
    SetChrPos(0x101, 1540, 750, 16000, 180)
    SetChrPos(0x105, -4460, 750, 16000, 180)

    def lambda_6253():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6253)

    def lambda_626D():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_626D)

    def lambda_6287():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6287)
    OP_96(0x1B, 0xFFFFFE0C, 0x370, 0x2C6A, 0x3E8, 0x0)
    WaitChrThread(0x101, 0)

    def lambda_62AC():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_62AC)

    def lambda_62C6():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_62C6)
    WaitChrThread(0x101, 0)

    def lambda_62E4():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_62E4)

    def lambda_62FE():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_62FE)
    WaitChrThread(0x101, 0)
    Fade(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x105, 0x1)
    StopEffect(0x1, 0x0)
    Sleep(1000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x105, 0, 0, 0, 0)
    OP_11(0x0, 0x0, 0x0, 0x10, 0x1E, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6384"),
        (1, "loc_6469"),
        (2, "loc_6550"),
        (3, "loc_6635"),
        (4, "loc_672D"),
        (SWITCH_DEFAULT, "loc_681E"),
    )


    label("loc_6384")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0xC, 1, 0, 38)

    def lambda_6398():

        label("loc_6398")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_6398")

    QueueWorkItem2(0x1B, 1, lambda_6398)

    #C0315
    ChrTalk(
        0x1B,
        (
            "#4S一号参赛选手！\x01",
            "辛茜亚小姐！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    BeginChrThread(0xC, 0, 0, 39)
    WaitChrThread(0xC, 0)
    EndChrThread(0xC, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    #C0316
    ChrTalk(
        0x1B,
        (
            "在此授予优胜者纪念盾。\x01",
            "……请收下！\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        "呵呵，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0xC, 0xB4, 0x1F4)
    Jump("loc_681E")

    label("loc_6469")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0xD, 1, 0, 38)

    def lambda_647D():

        label("loc_647D")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_647D")

    QueueWorkItem2(0x1B, 1, lambda_647D)

    #C0318
    ChrTalk(
        0x1B,
        (
            "#4S二号参赛选手！\x01",
            "爱丽斯小姐！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    BeginChrThread(0xD, 0, 0, 39)
    WaitChrThread(0xD, 0)
    EndChrThread(0xD, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    #C0319
    ChrTalk(
        0x1B,
        (
            "在此授予优胜者纪念盾。\x01",
            "……请收下！\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xD,
        "呵呵呵，谢谢⊥\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0xD, 0xB4, 0x1F4)
    Jump("loc_681E")

    label("loc_6550")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x18, 1, 0, 38)

    def lambda_6564():

        label("loc_6564")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_6564")

    QueueWorkItem2(0x1B, 1, lambda_6564)

    #C0321
    ChrTalk(
        0x1B,
        (
            "#4S三号参赛选手！\x01",
            "桑桑小姐！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x18, 0, 0, 39)
    WaitChrThread(0x18, 0)
    EndChrThread(0x18, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    #C0322
    ChrTalk(
        0x1B,
        (
            "在此授予优胜者纪念盾。\x01",
            "……请收下！\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x18,
        "嘿嘿嘿，谢谢～\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x18, 0xB4, 0x1F4)
    Jump("loc_681E")

    label("loc_6635")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x1C, 1, 0, 38)

    def lambda_6649():

        label("loc_6649")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6649")

    QueueWorkItem2(0x1B, 1, lambda_6649)

    #C0324
    ChrTalk(
        0x1C,
        (
            "#4S四号参赛选手！\x01",
            "温蒂小姐！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    OP_24(0x1A4)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x1C, 0, 0, 39)
    WaitChrThread(0x1C, 0)
    EndChrThread(0x1C, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    #C0325
    ChrTalk(
        0x1B,
        (
            "在此授予优胜者纪念盾。\x01",
            "……请收下！\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x1C,
        "啊哈哈，真的可以收下吗？谢啦～\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x1C, 0xB4, 0x1F4)
    Jump("loc_681E")

    label("loc_672D")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x19, 1, 0, 38)

    def lambda_6741():

        label("loc_6741")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_6741")

    QueueWorkItem2(0x1B, 1, lambda_6741)

    #C0327
    ChrTalk(
        0x1B,
        (
            "#4S五号参赛选手！\x01",
            "乔安娜小姐！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x19, 0, 0, 39)
    WaitChrThread(0x19, 0)
    EndChrThread(0x19, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    #C0328
    ChrTalk(
        0x1B,
        (
            "在此授予优胜者纪念盾。\x01",
            "……请收下！\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x19,
        "那、那个……谢、谢谢……\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x19, 0xB4, 0x1F4)
    Jump("loc_681E")

    label("loc_681E")

    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_6C4D")
    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)

    #C0330
    ChrTalk(
        0x1B,
        (
            "另外，作为本届活动的特别奖项，\x01",
            "我们还准备了评委会特别奖！\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_68A7"),
        (1, "loc_68C7"),
        (2, "loc_68E7"),
        (3, "loc_6907"),
        (4, "loc_6927"),
        (SWITCH_DEFAULT, "loc_6947"),
    )


    label("loc_68A7")

    OP_96(0xC, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0xC, 0x87, 0x1F4)
    Jump("loc_6947")

    label("loc_68C7")

    OP_96(0xD, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0xD, 0x87, 0x1F4)
    Jump("loc_6947")

    label("loc_68E7")

    OP_96(0x18, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x18, 0x87, 0x1F4)
    Jump("loc_6947")

    label("loc_6907")

    OP_96(0x1C, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x1C, 0x87, 0x1F4)
    Jump("loc_6947")

    label("loc_6927")

    OP_96(0x19, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x19, 0x87, 0x1F4)
    Jump("loc_6947")

    label("loc_6947")

    OP_2C(0x8F, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_699C")
    BeginChrThread(0x102, 1, 0, 38)

    def lambda_6960():

        label("loc_6960")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_6960")

    QueueWorkItem2(0x1B, 0, lambda_6960)

    #C0331
    ChrTalk(
        0x1B,
        (
            "#4S获得者是七号参赛选手！\x01",
            "艾莉小姐！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A39")

    label("loc_699C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_69EC")
    BeginChrThread(0x103, 1, 0, 38)

    def lambda_69B0():

        label("loc_69B0")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_69B0")

    QueueWorkItem2(0x1B, 0, lambda_69B0)

    #C0332
    ChrTalk(
        0x1B,
        (
            "#4S获得者是七号参赛选手！\x01",
            "缇欧小姐！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A39")

    label("loc_69EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_6A39")
    BeginChrThread(0x109, 1, 0, 38)

    def lambda_6A00():

        label("loc_6A00")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_6A00")

    QueueWorkItem2(0x1B, 0, lambda_6A00)

    #C0333
    ChrTalk(
        0x1B,
        (
            "#4S获得者是七号参赛选手！\x01",
            "诺艾尔小姐！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A39")

    OP_96(0x1B, 0xFFFFFE0C, 0x370, 0x2C6A, 0x3E8, 0x0)
    Sound(818, 0, 80, 0)
    Sound(820, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_6A78")
    BeginChrThread(0x102, 0, 0, 40)
    WaitChrThread(0x102, 0)
    EndChrThread(0x102, 0x1)
    Jump("loc_6AAB")

    label("loc_6A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_6A94")
    BeginChrThread(0x103, 0, 0, 40)
    WaitChrThread(0x103, 0)
    EndChrThread(0x103, 0x1)
    Jump("loc_6AAB")

    label("loc_6A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_6AAB")
    BeginChrThread(0x109, 0, 0, 40)
    WaitChrThread(0x109, 0)
    EndChrThread(0x109, 0x1)

    label("loc_6AAB")

    StopEffect(0x1, 0x0)

    #C0334
    ChrTalk(
        0x1B,
        (
            "特别奖的获得者\x01",
            "也将得到纪念盾。\x01",
            "……请收下！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_6B55")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0335
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x341),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x341, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0336
    ChrTalk(
        0x102,
        "#00109F呵呵，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Jump("loc_6C42")

    label("loc_6B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_6BCC")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0337
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x342),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x342, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0338
    ChrTalk(
        0x103,
        "#00205F……谢、谢谢。\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)
    Jump("loc_6C42")

    label("loc_6BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_6C42")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0339
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x343),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x343, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0340
    ChrTalk(
        0x109,
        "#10109F呵呵，真是不敢当。\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0xB4, 0x1F4)

    label("loc_6C42")

    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)

    label("loc_6C4D")

    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_93(0x18, 0xB4, 0x0)
    OP_93(0x1C, 0xB4, 0x0)
    OP_93(0x19, 0xB4, 0x0)
    OP_93(0x17, 0xB4, 0x0)
    Fade(500)
    Fade(500)
    OP_11(0x0, 0x0, 0x0, 0x10, 0x1E, 0x0)
    StopEffect(0x0, 0x0)
    ClearMapFlags(0x10)
    OP_0D()
    Sleep(500)

    #C0341
    ChrTalk(
        0x1B,
        (
            "那么，我宣布，\x01",
            "克洛斯贝尔职业女性选秀活动\x01",
            "到此结束！\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x1B,
        (
            "接下来，立餐宴会\x01",
            "将会再次开始，\x01",
            "请各位继续享用吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_6E(580, 3000)
    Sound(819, 0, 100, 0)
    Sound(820, 0, 100, 0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0343
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，慈善宴会的\x01",
            "职业女性选秀活动落下了帷幕。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    WaitBGM()
    OP_0D()
    OP_24(0x335)
    OP_24(0x36D)
    SetScenarioFlags(0x22, 1)
    NewScene("c1110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_4522 end

    def Function_29_6D87(): pass

    label("Function_29_6D87")

    OP_95(0xFE, -1460, 750, 12650, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x3E8)
    OP_93(0xFE, 0x0, 0x3E8)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_93(0xFE, 0xB4, 0x3E8)
    Sleep(1000)
    Return()

    # Function_29_6D87 end

    def Function_30_6DC5(): pass

    label("Function_30_6DC5")

    OP_95(0xFE, -1460, 750, 12650, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    Return()

    # Function_30_6DC5 end

    def Function_31_6DE4(): pass

    label("Function_31_6DE4")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -4460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_64(0xFE)
    Return()

    # Function_31_6DE4 end

    def Function_32_6E15(): pass

    label("Function_32_6E15")

    OP_63(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_95(0xFE, -3460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_6E15 end

    def Function_33_6E49(): pass

    label("Function_33_6E49")

    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_95(0xFE, -2460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_6E49 end

    def Function_34_6E7D(): pass

    label("Function_34_6E7D")

    OP_95(0xFE, -1460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_34_6E7D end

    def Function_35_6E99(): pass

    label("Function_35_6E99")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_64(0xFE)
    Return()

    # Function_35_6E99 end

    def Function_36_6ECA(): pass

    label("Function_36_6ECA")

    OP_95(0xFE, 540, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_36_6ECA end

    def Function_37_6EE6(): pass

    label("Function_37_6EE6")

    OP_95(0xFE, 1540, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_37_6EE6 end

    def Function_38_6F02(): pass

    label("Function_38_6F02")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F4C")
    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3200)
    Jump("Function_38_6F02")

    label("loc_6F4C")

    Return()

    # Function_38_6F02 end

    def Function_39_6F4D(): pass

    label("Function_39_6F4D")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -1910, 880, 11420, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_39_6F4D end

    def Function_40_6F87(): pass

    label("Function_40_6F87")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, 800, 750, 14930, 3000, 0x0)
    OP_95(0xFE, -1500, 750, 13910, 2000, 0x0)
    OP_95(0xFE, -1500, 880, 11420, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_40_6F87 end

    def Function_41_6FE9(): pass

    label("Function_41_6FE9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -1500, 900, 14300, 180)
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xC, 0x1000)
    OP_68(-1500, 2500, 14000, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_41_6FE9 end

    def Function_42_711E(): pass

    label("Function_42_711E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    LoadChrToIndex("chr/ch27702.itc", 0x1E)
    LoadChrToIndex("chr/ch27500.itc", 0x1F)
    LoadChrToIndex("chr/ch27802.itc", 0x20)
    LoadChrToIndex("chr/ch27600.itc", 0x21)
    LoadChrToIndex("chr/ch25900.itc", 0x22)
    LoadChrToIndex("chr/ch27502.itc", 0x23)
    LoadChrToIndex("chr/ch27602.itc", 0x24)
    LoadChrToIndex("chr/ch44202.itc", 0x25)
    LoadChrToIndex("chr/ch21002.itc", 0x26)
    LoadChrToIndex("chr/ch20302.itc", 0x27)
    SoundLoad(851)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x24, 2230, 900, 12630, 252)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    EndChrThread(0x24, 0x0)
    SetChrBattleFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x25, 2280, 750, 14110, 252)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x26, -5210, 900, 12820, 107)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    EndChrThread(0x26, 0x0)
    SetChrBattleFlags(0x26, 0x4)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x27, -3140, 750, 13930, 110)
    SetChrChipByIndex(0x27, 0x21)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x28, -340, 750, 14570, 180)
    SetChrChipByIndex(0x28, 0x22)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x1E, -5800, 150, 7350, 0)
    SetChrChipByIndex(0x1E, 0x26)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1F, -4000, 150, 7350, 0)
    SetChrChipByIndex(0x1F, 0x27)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x20, -2250, 150, 7350, 0)
    SetChrChipByIndex(0x20, 0x23)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x21, -450, 150, 7350, 0)
    SetChrChipByIndex(0x21, 0x25)
    SetChrSubChip(0x21, 0x0)
    EndChrThread(0x21, 0x0)
    SetChrBattleFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x22, 1250, 150, 7350, 0)
    SetChrChipByIndex(0x22, 0xE)
    SetChrSubChip(0x22, 0x0)
    EndChrThread(0x22, 0x0)
    SetChrBattleFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x23, 2930, 150, 7350, 0)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    EndChrThread(0x23, 0x0)
    SetChrBattleFlags(0x23, 0x4)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x15, 6880, 4000, 7260, 315)
    SetChrChipByIndex(0x15, 0xA)
    SetChrFlags(0x15, 0x8000)
    EndChrThread(0x15, 0x0)
    SetChrPos(0x16, 6880, 4000, -610, 315)
    SetChrChipByIndex(0x16, 0xC)
    SetChrFlags(0x16, 0x8000)
    OP_68(2390, 1500, -520, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(32530, 0)
    Sound(851, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_68(-1450, 2250, 12090, 5000)
    MoveCamera(40, 23, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(30820, 5000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-1450, 2250, 12090, 0)
    MoveCamera(28, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22540, 0)
    OP_0D()
    Sleep(500)

    #C0344
    ChrTalk(
        0x26,
        (
            "如今的法律毫无平等可言，对外国人，\x01",
            "特别是帝国人和共和国人过于优待！\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x26,
        (
            "而且竟然要将饱含市民血汗的税收\x01",
            "的１０％缴纳给两大国！\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x26,
        (
            "这无论怎么想也都很奇怪，\x01",
            "你难道不这么觉得吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x27,
        (
            "我们现在如果不站起来，\x01",
            "这种糟糕的状况恐怕将会\x01",
            "永远持续下去吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x27,
        "这样真的没问题吗！？\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x25,
        "……哼，真是愚蠢。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x25,
        (
            "现实问题是不能逃避的，如果没有足够的力量，\x01",
            "所谓的独立也只是不切实际的空谈罢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x25,
        (
            "假如别国大军真的发动侵攻，\x01",
            "连战车都没有配备的警备队又能如何抵御？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x26,
        (
            "你所说的别国，无论怎么想\x01",
            "也都是指埃雷波尼亚帝国吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x26,
        (
            "他们在西边的卡雷利亚要塞中配备了名为『列车炮』\x01",
            "的重型破坏兵器，随时瞄准着克洛斯贝尔市，\x01",
            "这可是众所周知的事实！\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x27,
        (
            "战车也好，军用飞艇也好，\x01",
            "凭克洛斯贝尔雄厚的财政实力，\x01",
            "完全可以配备得十分充足！\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x27,
        (
            "最重要的还是我们的决断，\x01",
            "难道不对吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x25,
        (
            "真是不明事理的家伙……\x01",
            "我都说过了，要看清现实！\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x25,
        (
            "首先，克洛斯贝尔之所以会如此繁荣，\x01",
            "很重要的一个原因就是帝国和共和国\x01",
            "的米拉大量流入这里！\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x25,
        (
            "如果真的独立，并与他们断绝往来，\x01",
            "克洛斯贝尔的财富说不定也会随之消失！\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x24,
        "好了好了，大家都冷静些。\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x24,
        (
            "……不管怎么说，最关键的问题还是\x01",
            "这种态度强硬的独立提案\x01",
            "是否能在国际社会中得到认同。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x24,
        "在之前的议论中，是否忽视了这一点呢？\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x26,
        "这和国际社会无关！\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x26,
        (
            "克洛斯贝尔独立才是\x01",
            "实现『正义』的唯一道路！\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x27,
        (
            "我看你终究也只是个\x01",
            "替卡尔瓦德说好话的代言人！\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x24,
        (
            "我、我的确被人\x01",
            "称为共和国派成员……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x24,
        (
            "但我相信自己对克洛斯贝尔\x01",
            "的热爱之心不会输给任何人！\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x24,
        "请你收回刚才那句话！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(6040, 5500, -5410, 0)
    MoveCamera(29, 31, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21420, 0)
    SetChrPos(0x101, 6940, 4000, -3750, 315)
    SetChrPos(0x103, 6910, 4000, -4960, 315)
    SetChrPos(0x102, 8010, 4000, -4600, 315)
    SetChrPos(0x109, 7960, 4000, -5740, 315)
    SetChrPos(0x104, 4750, 4120, -6880, 0)
    SetChrPos(0x105, 5580, 4120, -8020, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0368
    ChrTalk(
        0x104,
        (
            "#00300F虽然外面下着雨，\x01",
            "但这里却讨论得热火朝天啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        (
            "#00000F嗯，参加座谈会的市民\x01",
            "也比想象中更多……\x02\x03",

            "#00003F话说回来，帝国派、共和国派的重要议员\x01",
            "与最近迅速起势的独立派年轻议员们\x01",
            "展开辩论吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，这种辩论阵容似乎也\x01",
            "反映出了克洛斯贝尔如今的政治状况呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x103,
        (
            "#00200F听起来，双方的观点\x01",
            "似乎都很有道理……\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        (
            "#00103F……这个问题恐怕无法\x01",
            "如此简单地得出结论呢。\x02\x03",

            "就算再过几十年，\x01",
            "同样的辩论也只会不断重复。\x02\x03",

            "#00101F不过，或许真的已经到了\x01",
            "必须要下定最终结论的时候了……\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x109,
        (
            "#10101F………是啊。\x02\x03",

            "#10108F（应该选择前途多难的独立，\x01",
            "  还是背弃正义的从属地位呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(821, 500, 90)
    SetScenarioFlags(0x17B, 6)
    SetScenarioFlags(0x22, 2)
    NewScene("c1110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_711E end

    SaveToFile()

Try(main)
