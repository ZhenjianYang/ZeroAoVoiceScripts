from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t0010.bin",                # FileName
        "t0010",                    # MapName
        "t0010",                    # Location
        0x0038,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 56, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0010",                  # 0
        "特鲁塔村长",             # 1
        "艾娜夫人",               # 2
        "米莉亚",                 # 3
        "多纳尔德",               # 4
        "安洁",                   # 5
        "哈罗德",                 # 6
    ))

    AddCharChip((
        "chr/ch23702.itc",                   # 00
        "chr/ch24002.itc",                   # 01
        "chr/ch24100.itc",                   # 02
        "chr/ch24202.itc",                   # 03
        "chr/ch24300.itc",                   # 04
        "chr/ch24302.itc",                   # 05
        "chr/ch24102.itc",                   # 06
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

    DeclNpc(-38479,  250,     -1799,   90,   341,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(-88830,  0,       -1460,   270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(519,     180,     -1850,   180,  469,  0x0, 0,   0,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(38409,   180,     540,     180,  469,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(33700,   0,       -2619,   204,  389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(73630,   0,       670,     1200,    73630,   1000,    670,     0x007C, 0,  4,  0x0000)
    DeclActor(75750,   0,       3060,    1200,    75750,   1000,    3060,    0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_240",          # 00, 0
        "Function_1_2F8",          # 01, 1
        "Function_2_4CA",          # 02, 2
        "Function_3_520",          # 03, 3
        "Function_4_540",          # 04, 4
        "Function_5_676",          # 05, 5
        "Function_6_1685",         # 06, 6
        "Function_7_1F97",         # 07, 7
        "Function_8_27E0",         # 08, 8
        "Function_9_3734",         # 09, 9
        "Function_10_3735",        # 0A, 10
        "Function_11_3D92",        # 0B, 11
        "Function_12_3E70",        # 0C, 12
        "Function_13_45E3",        # 0D, 13
        "Function_14_4A27",        # 0E, 14
        "Function_15_6B96",        # 0F, 15
        "Function_16_71C8",        # 10, 16
    ))


    def Function_0_240(): pass

    label("Function_0_240")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_280"),
        (1, "loc_28C"),
        (2, "loc_298"),
        (3, "loc_2A4"),
        (4, "loc_2B0"),
        (5, "loc_2BC"),
        (6, "loc_2C8"),
        (SWITCH_DEFAULT, "loc_2D4"),
    )


    label("loc_280")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_28C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_298")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2A4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2B0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2BC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2F7")

    Return()

    # Function_0_240 end

    def Function_1_2F8(): pass

    label("Function_1_2F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_310")
    Event(0, 13)

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_363")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, 38320, 180, -2250, 0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x4)
    Jump("loc_4AA")

    label("loc_363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_37B")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4AA")

    label("loc_37B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3BF")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x9, -38500, 150, -3230, 90)
    Jump("loc_4AA")

    label("loc_3BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3D7")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4AA")

    label("loc_3D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3EF")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4AA")

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_402")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4AA")

    label("loc_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_41A")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4AA")

    label("loc_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_437")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4AA")

    label("loc_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_454")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4AA")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_46C")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4AA")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_484")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4AA")

    label("loc_484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_49C")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4AA")

    label("loc_49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4AA")
    ClearChrFlags(0xA, 0x80)

    label("loc_4AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C9")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_4C9")

    Return()

    # Function_1_2F8 end

    def Function_2_4CA(): pass

    label("Function_2_4CA")

    SetMapObjFrame(0xFF, "kage03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FA")
    OP_70(0x0, 0x0)
    Jump("loc_4FE")

    label("loc_4FA")

    OP_70(0x0, 0x1E)

    label("loc_4FE")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51C")
    OP_66(0x1, 0x1)

    label("loc_51C")

    Call(0, 3)
    Return()

    # Function_2_4CA end

    def Function_3_520(): pass

    label("Function_3_520")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_539")
    SetMapObjFlags(0x0, 0x4)
    Jump("loc_53F")

    label("loc_539")

    ClearMapObjFlags(0x0, 0x4)

    label("loc_53F")

    Return()

    # Function_3_520 end

    def Function_4_540(): pass

    label("Function_4_540")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62D")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('移动２', 1)"), scpexpr(EXPR_END)), "loc_5BF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '移动２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x103, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_628")

    label("loc_5BF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '移动２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '移动２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_628")

    Jump("loc_66A")

    label("loc_62D")

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

    label("loc_66A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_540 end

    def Function_5_676(): pass

    label("Function_5_676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_698")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_698")
    Call(0, 12)
    Return()

    label("loc_698")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_72C")
    Jump("loc_776")

    label("loc_72C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_74C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_776")

    label("loc_74C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_776")

    label("loc_76C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_776")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_855")

    #C0004
    ChrTalk(
        0xFE,
        (
            "……如今的生活\x01",
            "是女神赐予阿尔摩利卡村\x01",
            "的自然姿态。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "胡乱追求发展的话，\x01",
            "必然会再次导致\x01",
            "之前的魔兽骚动那种事。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "……虽然也不是不明白\x01",
            "那家伙的想法。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8BE")

    label("loc_855")


    #C0007
    ChrTalk(
        0xFE,
        (
            "迪利克想让村民们过上\x01",
            "富裕生活的想法也不是不能理解……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "但作为现任村长，只有这一点是不能妥协的。\x02",
    )

    CloseMessageWindow()

    label("loc_8BE")

    Jump("loc_167D")

    label("loc_8C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_97F")

    #C0009
    ChrTalk(
        0xFE,
        (
            "我认为像迪利克那样，\x01",
            "拿村子和克洛斯贝尔市来比较，\x01",
            "是毫无意义的……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市是克洛斯贝尔市，\x01",
            "阿尔摩利卡村是阿尔摩利卡村……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "两者各行其道才是\x01",
            "顺应自然法则。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167D")

    label("loc_97F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_AB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5D")

    #C0012
    ChrTalk(
        0xFE,
        (
            "我前几天跟迪利克\x01",
            "讨论了村子的将来……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "他还是坚持\x01",
            "应该发展村子，\x01",
            "不肯听我的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "纪念庆典中，因为他太过贪心，\x01",
            "招来了过多的游客，\x01",
            "已经产生很多问题了……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "迪利克也真让人伤脑筋啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AB1")

    label("loc_A5D")


    #C0016
    ChrTalk(
        0xFE,
        (
            "迪利克那家伙，\x01",
            "不支持我希望村子\x01",
            "维持现状的想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "……到底该怎么办才好呢。\x02",
    )

    CloseMessageWindow()

    label("loc_AB1")

    Jump("loc_167D")

    label("loc_AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_C20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAC")

    #C0018
    ChrTalk(
        0xFE,
        (
            "唔……游客也差不多\x01",
            "都回克洛斯贝尔市了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "这次为了吸引游客而开设露天店……\x01",
            "到底对不对呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "虽然村子的确有盈利……\x01",
            "但是也发生了游客\x01",
            "误入古战场这样的麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "……等迪利克回来以后，\x01",
            "要好好跟他谈一次才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C1B")

    label("loc_BAC")


    #C0022
    ChrTalk(
        0xFE,
        (
            "虽然游客增加，\x01",
            "村子有所盈利，\x01",
            "但是也发生了一些麻烦……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "……等迪利克回来以后，\x01",
            "要好好跟他谈一次才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1B")

    Jump("loc_167D")

    label("loc_C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAE")

    #C0024
    ChrTalk(
        0xFE,
        (
            "……今年的纪念庆典\x01",
            "果然来了很多游客啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "迪利克的目的\x01",
            "达到了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "这会对村子的发展\x01",
            "有所帮助吗……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D0A")

    label("loc_CAE")


    #C0027
    ChrTalk(
        0xFE,
        (
            "来观光的游客数量，\x01",
            "今天应该会达到顶峰吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "这究竟能否对村子的发展\x01",
            "有所帮助呢……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0A")

    Jump("loc_167D")

    label("loc_D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0B")

    #C0029
    ChrTalk(
        0xFE,
        (
            "嗯……参观纪念庆典的游客被吸引而来，\x01",
            "让村子变得热闹，倒也不错……\x01",
            "但不知会持续到何时呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "他们毕竟只是游客嘛。\x01",
            "到纪念庆典快结束的时候，\x01",
            "也会渐渐散去的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "听说他们还妨碍了农务……\x01",
            "果然凡事并非都只有好的一面啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E6D")

    label("loc_E0B")


    #C0032
    ChrTalk(
        0xFE,
        (
            "我感觉村子的热闹\x01",
            "也只是一时的。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "听说他们还妨碍了农务……\x01",
            "果然凡事并非都只有好的一面啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6D")

    Jump("loc_167D")

    label("loc_E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_F72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF6")

    #C0034
    ChrTalk(
        0xFE,
        (
            "看露天店的情况，\x01",
            "似乎广受好评。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "作为长年生产蜂蜜的\x01",
            "阿尔摩利卡村村长，\x01",
            "没有比这更值得骄傲的了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F6D")

    label("loc_EF6")


    #C0036
    ChrTalk(
        0xFE,
        (
            "露天店似乎广受好评……\x01",
            "将这件事交给迪利克，\x01",
            "看来是正确的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "身为阿尔摩利卡村村长，\x01",
            "没有比这更值得骄傲的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6D")

    Jump("loc_167D")

    label("loc_F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100C")

    #C0038
    ChrTalk(
        0xFE,
        (
            "迪利克提出的开办露天店的建议……\x01",
            "似乎进展得很顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "唔，村民们\x01",
            "似乎也很开心……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "允许他这么做，\x01",
            "或许是正确的吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1072")

    label("loc_100C")


    #C0041
    ChrTalk(
        0xFE,
        (
            "接下来就是创立纪念庆典\x01",
            "正式开始之后的事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "希望游客不要来得太多，\x01",
            "进而引发什么不好的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1072")

    Jump("loc_167D")

    label("loc_1077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1355")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1109")

    #C0043
    ChrTalk(
        0xFE,
        "特别任务支援科吗……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "一开始见面的时候，\x01",
            "还真没想到\x01",
            "警察会这么可靠呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        "以后再有什么事的话，就麻烦你们了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1350")

    label("loc_1109")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_1197")

    #C0046
    ChrTalk(
        0xFE,
        (
            "魔兽侵占的私有地\x01",
            "就在村子的东南方向，\x01",
            "沿着那个方向前进就是了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "私有地里的东西，\x01",
            "你们可以随便使用。\x01",
            "一切就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1350")

    label("loc_1197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1281")

    #C0048
    ChrTalk(
        0xFE,
        (
            "我儿子迪利克\x01",
            "提议要振兴村子。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "虽然我认为如果\x01",
            "做得太过火，忘却了\x01",
            "谦恭的生活态度也不好……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "不过，在创立纪念庆典开设露天店这种事，\x01",
            "我以前也曾经参加过，\x01",
            "所以就推荐他试试。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "好吧，\x01",
            "看看会有什么结果……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1350")

    label("loc_1281")


    #C0052
    ChrTalk(
        0xFE,
        (
            "看到克洛斯贝尔市的样子，\x01",
            "我就会觉得\x01",
            "一味发展也未必是好事。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "我觉得这个村子\x01",
            "一直像往昔一样朴素就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "但我儿子迪利克\x01",
            "似乎不同意我的看法……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "好吧，在纪念庆典开办的露天店，\x01",
            "会有什么结果呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1350")

    Jump("loc_167D")

    label("loc_1355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D2")

    #C0056
    ChrTalk(
        0xFE,
        (
            "昨天听你们说过之后，\x01",
            "我就提醒过村民了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "魔兽还没被找到吧？\x01",
            "我们村子也尚不能安心度日啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1414")

    label("loc_13D2")


    #C0058
    ChrTalk(
        0xFE,
        (
            "魔兽还没被找到吧？\x01",
            "村民们当然都得注意，\x01",
            "你们也要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1414")

    Jump("loc_167D")

    label("loc_1419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_1534")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D7")

    #C0059
    ChrTalk(
        0xFE,
        "唔，果然什么也没查到吗……\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "那已经是三个星期前的事了。\x01",
            "从某种程度上说，也是没办法的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "既然我们村子之外的地方也受了灾，\x01",
            "或许应该去\x01",
            "那些地方问问吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_152F")

    label("loc_14D7")


    #C0062
    ChrTalk(
        0xFE,
        (
            "还有『神狼』的事……\x01",
            "那纯粹只是个传说。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "虽然我告诉了你们，\x01",
            "但也不用太在意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152F")

    Jump("loc_167D")

    label("loc_1534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_167D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15FB")

    #C0064
    ChrTalk(
        0xFE,
        (
            "话说，探听情报啊……\x01",
            "警察的工作\x01",
            "也不比游击士轻松啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "毕竟事情发生的时候\x01",
            "都已经是深夜了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "虽然不知道能不能得到什么有用的情报……\x01",
            "不过还是先问问村里的人吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_167D")

    label("loc_15FB")


    #C0067
    ChrTalk(
        0xFE,
        (
            "现在这时间的话，\x01",
            "出去干农活的人\x01",
            "应该也都回来了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "也有很多人在\x01",
            "河边的酒馆『白蜡亭』吃午饭。\x01",
            "愿意的话，去那里看看如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_676 end

    def Function_6_1685(): pass

    label("Function_6_1685")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_170C")

    #C0069
    ChrTalk(
        0xFE,
        (
            "我丈夫昨天又和迪利克\x01",
            "吵了一架。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "毕竟是父子，\x01",
            "真希望他们能互相理解……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "但是看情况，一时半会还是很难啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F93")

    label("loc_170C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_176E")

    #C0072
    ChrTalk(
        0xFE,
        (
            "我丈夫和迪利克\x01",
            "都有坚定的思想，\x01",
            "对立是在所难免的。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "……事情总会有波折呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F93")

    label("loc_176E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_17D6")
    SetChrSubChip(0xFE, 0x1)

    #C0074
    ChrTalk(
        0xFE,
        (
            "村长和村长之子有矛盾，\x01",
            "会给村民们带来不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "你就尽量\x01",
            "支持一下迪利克吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_1F93")

    label("loc_17D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_18EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1877")

    #C0076
    ChrTalk(
        0xFE,
        (
            "我丈夫和迪利克\x01",
            "虽然做法不同，\x01",
            "但出发点都是为了村子好。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "虽说思想对立这点\x01",
            "在某种程度上也是没办法的事，\x01",
            "但我的心情还真复杂……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18EA")

    label("loc_1877")


    #C0078
    ChrTalk(
        0xFE,
        (
            "毕竟是父子，\x01",
            "我希望他们不要闹矛盾，\x01",
            "齐心协力地发展村子……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "但既然想法不同，\x01",
            "有矛盾或许也是在所难免的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18EA")

    Jump("loc_1F93")

    label("loc_18EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_19FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B2")

    #C0080
    ChrTalk(
        0xFE,
        (
            "我丈夫从昨天开始就很苦恼，\x01",
            "他好像一直在思索，自己之前同意在\x01",
            "纪念庆典期间开露天店这种决定是否正确。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "本以为这次应该会顺利的，\x01",
            "但看来又要和\x01",
            "迪利克意见相左了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19F8")

    label("loc_19B2")


    #C0082
    ChrTalk(
        0xFE,
        (
            "作为妻子和母亲……\x01",
            "看到丈夫和迪利克之间矛盾重重，\x01",
            "心情真是复杂。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F8")

    Jump("loc_1F93")

    label("loc_19FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1AFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A83")

    #C0083
    ChrTalk(
        0xFE,
        (
            "虽然明白丈夫\x01",
            "在担心游客带来的问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "但是，首先应该\x01",
            "表扬为了振兴村子\x01",
            "而做了许多努力的迪利克吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AF6")

    label("loc_1A83")


    #C0085
    ChrTalk(
        0xFE,
        (
            "无论结果如何，\x01",
            "至少说明迪利克作为\x01",
            "下任村长，具有充分的素质……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "光是知道这点，对我来说\x01",
            "就是很大的收获了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF6")

    Jump("loc_1F93")

    label("loc_1AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B6F")

    #C0087
    ChrTalk(
        0xFE,
        (
            "算上今天，纪念庆典\x01",
            "还有四天，\x01",
            "游客还会继续增加吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "我得去拜托\x01",
            "酒馆的格方先生\x01",
            "好好招待他们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F93")

    label("loc_1B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE8")

    #C0089
    ChrTalk(
        0xFE,
        (
            "好久没看到\x01",
            "迪利克那么\x01",
            "充满干劲的样子了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "那孩子也有了\x01",
            "身为下任村长的\x01",
            "具体想法了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C4E")

    label("loc_1BE8")


    #C0091
    ChrTalk(
        0xFE,
        (
            "看到迪利克积极\x01",
            "安排各种活动的样子，\x01",
            "我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "那孩子也有了\x01",
            "身为下任村长的\x01",
            "具体想法了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4E")

    Jump("loc_1F93")

    label("loc_1C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1D97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3E")

    #C0093
    ChrTalk(
        0xFE,
        (
            "迪利克和我丈夫\x01",
            "的关系并不太好。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "丈夫身为村长，\x01",
            "想要维持村子的传统……\x01",
            "他很看重这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "但儿子作为下任村长，\x01",
            "希望能推动村子发展，\x01",
            "让村民们能过上更轻松的好日子。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "两边都没有错，\x01",
            "真是个难题。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D92")

    label("loc_1D3E")


    #C0097
    ChrTalk(
        0xFE,
        (
            "意见相左的丈夫和儿子\x01",
            "总是相处不好……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "唉，没有什么办法\x01",
            "可以让他们和好吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D92")

    Jump("loc_1F93")

    label("loc_1D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1E60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1B")

    #C0099
    ChrTalk(
        0xFE,
        (
            "狼形魔兽竟然在那么大的\x01",
            "范围内出没……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "即使有一天再来村里\x01",
            "也不足为奇吧。\x01",
            "啊，好可怕，好可怕……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E5B")

    label("loc_1E1B")


    #C0101
    ChrTalk(
        0xFE,
        (
            "总而言之，下次\x01",
            "说不定还会有人遭到袭击。\x01",
            "必须要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E5B")

    Jump("loc_1F93")

    label("loc_1E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_1EAE")

    #C0102
    ChrTalk(
        0xFE,
        (
            "那件事可是\x01",
            "闹得满村风雨的。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "因为那种事\x01",
            "是很少见的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F93")

    label("loc_1EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1F93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3D")

    #C0104
    ChrTalk(
        0xFE,
        (
            "我和老伴一样，\x01",
            "出事那天晚上也睡得很熟……\x01",
            "大概帮不上你们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "……对了，\x01",
            "去问问离受害地点\x01",
            "更近的人怎么样？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F93")

    label("loc_1F3D")


    #C0106
    ChrTalk(
        0xFE,
        (
            "魔兽袭击的是养蜂场、\x01",
            "家畜和田里的农作物……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "去问问管理这些的人\x01",
            "会比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F93")

    TalkEnd(0xFE)
    Return()

    # Function_6_1685 end

    def Function_7_1F97(): pass

    label("Function_7_1F97")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_202B")
    Jump("loc_2075")

    label("loc_202B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_204B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2075")

    label("loc_204B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_206B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2075")

    label("loc_206B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2075")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_214F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2117")

    #C0108
    ChrTalk(
        0xFE,
        (
            "昨天我多收了一些蔬菜，\x01",
            "所以要和艾尔琴一起去卖掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "平时坐车的机会很少，\x01",
            "还真有点期待呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_214A")

    label("loc_2117")


    #C0110
    ChrTalk(
        0xFE,
        (
            "不过，艾尔琴那家伙，\x01",
            "检查车子到底要多久啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_214A")

    Jump("loc_27D8")

    label("loc_214F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_21B7")

    #C0111
    ChrTalk(
        0xFE,
        (
            "今天开始工作之前，\x01",
            "要不要先做个便当呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "每天都去『白蜡亭』吃饭，\x01",
            "也会吃腻的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D8")

    label("loc_21B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_22CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2273")

    #C0113
    ChrTalk(
        0xFE,
        (
            "我弟弟艾尔琴只要一兴奋，\x01",
            "说话就会带口音。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "那是阿尔摩利卡的方言，\x01",
            "以前村民们说话都是那种口音……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "但现在还有口音的也只有\x01",
            "多纳尔德大叔和艾尔琴了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_22C9")

    label("loc_2273")


    #C0116
    ChrTalk(
        0xFE,
        (
            "多纳尔德大叔以前经常\x01",
            "带艾尔琴一起玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "所以艾尔琴不知不觉就\x01",
            "传染了他的口音。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C9")

    Jump("loc_27D8")

    label("loc_22CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_22DC")
    Jump("loc_27D8")

    label("loc_22DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_22EA")
    Jump("loc_27D8")

    label("loc_22EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_22F8")
    Jump("loc_27D8")

    label("loc_22F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2306")
    Jump("loc_27D8")

    label("loc_2306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_237C")

    #C0118
    ChrTalk(
        0xFE,
        (
            "村里似乎也要正式\x01",
            "举办面向纪念庆典的活动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "……我也不能置身事外啊。\x01",
            "嗯～有什么能帮上忙的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D8")

    label("loc_237C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2416")

    #C0120
    ChrTalk(
        0xFE,
        (
            "我弟弟艾尔琴\x01",
            "特别喜欢导力车。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "村民们凑钱\x01",
            "买的导力卡车，\x01",
            "都快被他据为己有了。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "……算啦，反正大家也都没什么意见，\x01",
            "就随他去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D8")

    label("loc_2416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2504")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24CB")

    #C0123
    ChrTalk(
        0xFE,
        (
            "村里的养蜂场\x01",
            "摆列着一些木箱，看到了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "那叫养蜂箱，\x01",
            "里面有蜂巢，\x01",
            "可以产出很～甜的蜂蜜哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "注意不要随便乱碰哦。\x01",
            "被蜇到的话，我可就不管了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24FF")

    label("loc_24CB")


    #C0126
    ChrTalk(
        0xFE,
        (
            "养蜂场的养蜂箱里\x01",
            "有蜂巢。\x01",
            "注意不要随便乱碰哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24FF")

    Jump("loc_27D8")

    label("loc_2504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_25F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B5")

    #C0127
    ChrTalk(
        0xFE,
        (
            "在养蜂场工作的迪利克……\x01",
            "虽然是个好人，\x01",
            "但是也太一本正经了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "大概因为是村长的儿子，\x01",
            "所以责任感特别强烈吧……\x01",
            "但其实完全可以活得轻松点啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_25F2")

    label("loc_25B5")


    #C0129
    ChrTalk(
        0xFE,
        (
            "毕竟是住在这么悠闲的村子里嘛，\x01",
            "得过得悠闲自在点才对呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F2")

    Jump("loc_27D8")

    label("loc_25F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_26F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2692")

    #C0130
    ChrTalk(
        0xFE,
        (
            "干农活必须要多花时间，\x01",
            "怀着爱心来做才行。\x01",
            "农作物就像是自己的孩子一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "要是被糟蹋了……\x01",
            "你们能明白我们\x01",
            "有多伤心了吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26EE")

    label("loc_2692")


    #C0132
    ChrTalk(
        0xFE,
        (
            "呕心沥血栽培的\x01",
            "农作物要是被糟蹋了……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "对我们来说，\x01",
            "就等于是自己的孩子受了伤一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26EE")

    Jump("loc_27D8")

    label("loc_26F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_27D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2773")

    #C0134
    ChrTalk(
        0xFE,
        (
            "这个村子的优美风景\x01",
            "就是最棒的飨宴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "啊～好像有点困了。\x01",
            "要不要躲进村子的仓库\x01",
            "小睡一会呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27D8")

    label("loc_2773")


    #C0136
    ChrTalk(
        0xFE,
        (
            "要不要躲进村子的仓库\x01",
            "小睡一会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "……要是被迪利克发现的话，\x01",
            "一定会被说教的，\x01",
            "还是算了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_1F97 end

    def Function_8_27E0(): pass

    label("Function_8_27E0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2874")
    Jump("loc_28BE")

    label("loc_2874")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2894")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28BE")

    label("loc_2894")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28B4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28BE")

    label("loc_28B4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28BE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2969")

    #C0138
    ChrTalk(
        0xFE,
        "哦，找到书了啊。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "嗯～竟然弄丢了\x01",
            "别人的东西，\x01",
            "俺也真是太不小心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "今后会小心一点的。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_2969")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A18")

    #C0141
    ChrTalk(
        0xFE,
        (
            "俺丢书的地方\x01",
            "是村长家前面的\x01",
            "养蜂场小屋。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "俺在里面看书，\x01",
            "结果不知几时就找不到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "哎呀，真是抱歉哇。\x01",
            "不好意思，你们去找找吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_2A18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A39")
    Call(0, 15)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_2A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADB")
    SetChrSubChip(0xB, 0x0)

    #C0144
    ChrTalk(
        0xB,
        "总是麻烦你啊，安洁。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "谢谢你帮我\x01",
            "照顾孩子们。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xC,
        "啊哈，说什么呢，真见外。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xC,
        (
            "这种小事就别提了，\x01",
            "今后也要\x01",
            "努力工作哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B1D")

    label("loc_2ADB")


    #C0148
    ChrTalk(
        0xFE,
        (
            "安洁帮我把孩子们\x01",
            "照顾得很好，\x01",
            "所以我才能毫无牵挂地专心干活。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B1D")

    Jump("loc_372C")

    label("loc_2B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2C48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BDC")

    #C0149
    ChrTalk(
        0xFE,
        (
            "村长的儿子迪利克\x01",
            "一直努力想要\x01",
            "让村子发展起来……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "但俺觉得村子\x01",
            "像现在这样就最好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村要是\x01",
            "变得和克洛斯贝尔市一样，\x01",
            "那该多让人失落哇。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C43")

    label("loc_2BDC")


    #C0152
    ChrTalk(
        0xFE,
        (
            "俺觉得村子\x01",
            "像现在这样就最好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村要是\x01",
            "变得和克洛斯贝尔市一样，\x01",
            "那该多让人失落哇。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C43")

    Jump("loc_372C")

    label("loc_2C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2CB6")

    #C0154
    ChrTalk(
        0xFE,
        "今年可是个丰收年哇。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "前一阵子，有人抓住了\x01",
            "冒充成『神狼』的狗，\x01",
            "这一定是当时的奖赏哇。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372C")

    label("loc_2CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2D38")

    #C0156
    ChrTalk(
        0xFE,
        (
            "纪念庆典……\x01",
            "今年也是从头到尾\x01",
            "干活干个没完啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "不过，农家的日常生活\x01",
            "就是这样了，\x01",
            "事到如今，也早就习惯了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372C")

    label("loc_2D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2DA9")

    #C0158
    ChrTalk(
        0xFE,
        (
            "今天的活也干完了……\x01",
            "待会去『白蜡亭』\x01",
            "喝两杯吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "难得的纪念庆典，\x01",
            "这点享受应该没关系吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372C")

    label("loc_2DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2ECB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E65")

    #C0160
    ChrTalk(
        0xFE,
        (
            "游客增加了，\x01",
            "热闹一点倒是好事……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "不过，或许还是提醒他们一下，\x01",
            "让他们不要去太危险的地方比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "特别是阿尔摩利卡古道途中的\x01",
            "古战场，很危险的哇。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2EC6")

    label("loc_2E65")


    #C0163
    ChrTalk(
        0xFE,
        (
            "得提醒游客\x01",
            "不要进入\x01",
            "危险的地方才行哇。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "特别是阿尔摩利卡古道途中的\x01",
            "古战场，很危险的哇。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC6")

    Jump("loc_372C")

    label("loc_2ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA8")
    OP_4B(0xC, 0xFF)

    #C0165
    ChrTalk(
        0xFE,
        (
            "我听人家说，\x01",
            "『彩虹剧团』今年的表演\x01",
            "好像精彩绝伦哇。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "要是俺也有票的话，\x01",
            "哪怕丢下田里的农活，\x01",
            "也要跑去看哇。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    #C0167
    ChrTalk(
        0xC,
        "……你刚才说什么？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    #C0168
    ChrTalk(
        0xFE,
        "……开个玩笑啦。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    OP_93(0xC, 0xCC, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_301D")

    label("loc_2FA8")


    #C0169
    ChrTalk(
        0xFE,
        (
            "不、不过，虽说丢下农活\x01",
            "只是在开玩笑……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "但只要是居住在克洛斯贝尔的人，\x01",
            "谁都会想去看\x01",
            "『彩虹剧团』的表演啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_301D")

    Jump("loc_372C")

    label("loc_3022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_312E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D1")

    #C0171
    ChrTalk(
        0xFE,
        (
            "创立纪念庆典开始以后，\x01",
            "就会零零星星地有游客过来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "不，考虑到今年还要开设露天店，\x01",
            "说不定来的人会多过预期呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        "嗯～有点紧张起来了啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3129")

    label("loc_30D1")


    #C0174
    ChrTalk(
        0xFE,
        (
            "虽然偶尔也会有游客或者商人过来，\x01",
            "但来的也就是一两个人吧。\x01",
            "这次可要有心理准备哇……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3129")

    Jump("loc_372C")

    label("loc_312E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_32A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31EC")

    #C0175
    ChrTalk(
        0xFE,
        (
            "对了，在阿尔摩利卡古道的途中，\x01",
            "不是有座无法通行的桥吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "那前面啊，\x01",
            "有个很有年头的古战场呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "虽然是个很有气氛的地方，\x01",
            "但是有很多魔兽，要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_329B")

    label("loc_31EC")


    #C0178
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡古道途中的古战场\x01",
            "是个很有气氛的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "虽然有魔兽徘徊，比较危险……\x01",
            "但你们去大概没问题吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "……哈，虽然现在过不去，\x01",
            "但以后要是有机会了，可以去看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_329B")

    Jump("loc_372C")

    label("loc_32A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B8")

    #C0181
    ChrTalk(
        0xFE,
        (
            "村里的导力卡车\x01",
            "是大家一起凑钱买的。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "虽然价格很贵，\x01",
            "但要把农作物送到克洛斯贝尔市的话，\x01",
            "买车也是必须的，没办法呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "嗯，那种方便的东西，\x01",
            "随着逐渐普及，\x01",
            "自然会慢慢便宜起来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "等到我家孩子有了自己的车时，\x01",
            "价格应该就会变得\x01",
            "比较合理了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_343C")

    label("loc_33B8")


    #C0185
    ChrTalk(
        0xFE,
        (
            "导力车这种方便的东西，\x01",
            "随着逐渐普及，\x01",
            "自然会慢慢便宜起来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "等到我家孩子有了自己的车时，\x01",
            "价格应该就会变得\x01",
            "比较合理了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_343C")

    Jump("loc_372C")

    label("loc_3441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_35C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3535")

    #C0187
    ChrTalk(
        0xFE,
        (
            "贸易商给人一种\x01",
            "经常游历于各国的印象……\x01",
            "但那个哈罗德先生却不一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "他似乎只在自治州内经商，\x01",
            "脚踏实地地展开事业，\x01",
            "是个很勤奋努力的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "如今这世道，那么稳重踏实的贸易商已经很少见了。\x01",
            "总之，他是个好人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_35C2")

    label("loc_3535")


    #C0190
    ChrTalk(
        0xFE,
        (
            "我和哈罗德先生的关系很好，\x01",
            "经常和他商量生意上的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "脚踏实地，一点点\x01",
            "加深本地人的信赖……\x01",
            "如今这世道，那样的贸易商已经很少见了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35C2")

    Jump("loc_372C")

    label("loc_35C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_3723")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36B4")

    #C0192
    ChrTalk(
        0xFE,
        (
            "前一阵子，农场被魔兽糟蹋了。\x01",
            "重要的农作物和家畜都遭了灾。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "虽然现场留有狼形魔兽的足迹，\x01",
            "但看上去好像并不是附近会有的种类。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "说不定真像村长说的一样，\x01",
            "是『神狼』干的好事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36AC")
    SetScenarioFlags(0x68, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36AC")

    SetScenarioFlags(0x0, 3)
    Jump("loc_371E")

    label("loc_36B4")


    #C0195
    ChrTalk(
        0xFE,
        (
            "糟蹋农场的狼形魔兽，\x01",
            "好像是这附近没有的种类呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "说不定真像村长说的一样，\x01",
            "是『神狼』干的好事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_371E")

    Jump("loc_372C")

    label("loc_3723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_372C")

    label("loc_372C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_27E0 end

    def Function_9_3734(): pass

    label("Function_9_3734")

    Return()

    # Function_9_3734 end

    def Function_10_3735(): pass

    label("Function_10_3735")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3814")
    TurnDirection(0xC, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C0")

    #C0197
    ChrTalk(
        0xFE,
        (
            "史蒂芬今天一大早\x01",
            "就来和卡米尤他们玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "那孩子今天也会在我们家吃饭吧，\x01",
            "午饭得多做些才行呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_380F")

    label("loc_37C0")


    #C0199
    ChrTalk(
        0xFE,
        (
            "史蒂芬经常陪我家\x01",
            "那两个淘气的孩子玩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        "下次也要跟他妈妈道个谢才是。\x02",
    )

    CloseMessageWindow()

    label("loc_380F")

    Jump("loc_3D8E")

    label("loc_3814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3822")
    Jump("loc_3D8E")

    label("loc_3822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3897")

    #C0201
    ChrTalk(
        0xFE,
        (
            "在『白蜡亭』住宿的\x01",
            "阿蕾莎太太和她的儿子\x01",
            "最近常来玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "希望我家的孩子可别\x01",
            "把人家的小孩弄伤啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D8E")

    label("loc_3897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3908")

    #C0203
    ChrTalk(
        0xFE,
        (
            "虽然很想带孩子们\x01",
            "去看纪念庆典……\x01",
            "但真是没办法呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "比起没事可做，\x01",
            "还是忙忙碌碌要好多了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D8E")

    label("loc_3908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_39BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_398A")

    #C0205
    ChrTalk(
        0xFE,
        (
            "可以的话，真想带孩子们\x01",
            "去看纪念庆典呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "算啦，努力干活，\x01",
            "希望明年的这个时候\x01",
            "可以休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_39B9")

    label("loc_398A")


    #C0207
    ChrTalk(
        0xFE,
        (
            "明年可一定要带孩子们\x01",
            "去看纪念庆典才行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39B9")

    Jump("loc_3D8E")

    label("loc_39BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_39CC")
    Jump("loc_3D8E")

    label("loc_39CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3AB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A57")

    #C0208
    ChrTalk(
        0xFE,
        (
            "田里的活很忙呢。\x01",
            "虽然遗憾，但今年纪念庆典是去不成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "阿蕾莎太太和史蒂芬\x01",
            "好像去了，也算是回家探亲吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3AAF")

    label("loc_3A57")


    #C0210
    ChrTalk(
        0xFE,
        (
            "阿蕾莎太太和史蒂芬\x01",
            "好像去看纪念庆典了，顺便也算是回家探亲。\x01",
            "啊哈哈，真羡慕他们呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AAF")

    Jump("loc_3D8E")

    label("loc_3AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3BE9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD0")
    Call(0, 11)
    Jump("loc_3BE4")

    label("loc_3AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B6F")

    #C0211
    ChrTalk(
        0xFE,
        (
            "我让克洛斯贝尔市的\x01",
            "朋友帮忙确认了一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的公演似乎\x01",
            "连两个月之后的座位都预约满了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "唉～市里人的\x01",
            "热情就是不一样呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3BE4")

    label("loc_3B6F")


    #C0214
    ChrTalk(
        0xFE,
        (
            "两个月以后的预约啊……\x01",
            "还真是有耐心。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "对克洛斯贝尔市的人来说，\x01",
            "『彩虹剧团』就是有\x01",
            "等待这么长时间的价值吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BE4")

    Jump("loc_3D8E")

    label("loc_3BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3D5B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C05")
    Call(0, 11)
    Jump("loc_3D56")

    label("loc_3C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD6")

    #C0216
    ChrTalk(
        0xFE,
        (
            "之前频繁发生的魔兽灾害也平息了，\x01",
            "可以放心让孩子出去玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "不过，农家是很忙碌的。\x01",
            "很少有机会\x01",
            "带他们出村子去。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "虽然他们央求我\x01",
            "带他们去参加创立纪念庆典……\x01",
            "不过实在抽不出时间啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3D56")

    label("loc_3CD6")


    #C0219
    ChrTalk(
        0xFE,
        (
            "农家是很忙碌的呢。\x01",
            "所以很少有机会\x01",
            "带他们出村子去。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "虽然他们央求我\x01",
            "带他们去参加创立纪念庆典……\x01",
            "不过实在抽不出时间啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D56")

    Jump("loc_3D8E")

    label("loc_3D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3D69")
    Jump("loc_3D8E")

    label("loc_3D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_3D77")
    Jump("loc_3D8E")

    label("loc_3D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_3D85")
    Jump("loc_3D8E")

    label("loc_3D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3D8E")

    label("loc_3D8E")

    TalkEnd(0xFE)
    Return()

    # Function_10_3735 end

    def Function_11_3D92(): pass

    label("Function_11_3D92")


    #C0221
    ChrTalk(
        0xFE,
        (
            "我正在做奶酪沙司薏面。\x01",
            "我们家里人都喜欢吃这个。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "愿意的话，你们就学学吧。\x01",
            "自己亲手做的话，会格外好吃哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0223
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '香草面'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0224
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '香草面'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xA)
    Return()

    # Function_11_3D92 end

    def Function_12_3E70(): pass

    label("Function_12_3E70")

    EventBegin(0x0)
    Fade(500)
    OP_68(-39840, 1950, -2730, 0)
    MoveCamera(325, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23700, 0)
    SetChrPos(0x101, -41000, 0, -1800, 90)
    SetChrPos(0x102, -41500, 0, -2800, 90)
    SetChrPos(0x103, -42500, 0, -800, 90)
    SetChrPos(0x104, -43250, 0, -1800, 90)
    SetChrPos(0x8, -39300, 180, -1800, 270)
    OP_0D()

    #C0225
    ChrTalk(
        0x101,
        "#5P#0000F好久不见了，特鲁塔村长。\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        (
            "#12P是特别任务支援科的……！\x01",
            "你们来得正好。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "#12P之前那起狼形魔兽事件顺利解决的消息，\x01",
            "也已经传到村里来啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x8,
        (
            "#12P警察也不是\x01",
            "完全没有希望啊。\x01",
            "大家都这么说呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x104,
        (
            "#5P#0309F不，您过奖了。\x02\x03",

            "#0301F……话说，现在可不是\x01",
            "闲聊的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        (
            "#5P#0100F方便的话，\x01",
            "能不能把委托的详情\x01",
            "告诉我们？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x8,
        (
            "#12P哦哦，说得对。\x01",
            "还要再次感谢你们\x01",
            "能再来这一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x8,
        (
            "#12P唔……那么，\x01",
            "我这就给大家\x01",
            "说明一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        (
            "#5P#0200F委托内容上说……\x01",
            "魔兽侵入了村子的私有地里，\x01",
            "是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        "#12P唔，正是。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x8,
        (
            "#12P你们在来村子的路上\x01",
            "可能也见过……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "#12P阿尔摩利卡古道中，\x01",
            "有块用来放置资材的\x01",
            "私有地。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "#12P有一群魔兽\x01",
            "闯进里面去了，\x01",
            "我们正伤脑筋呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        (
            "#5P#0103F一群魔兽……\x01",
            "那的确……很危险呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        "#5P#0005F村民中有人受伤吗？\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        "#12P现在还没有。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        (
            "#12P只是，那里也放着\x01",
            "干农活的工具，\x01",
            "所以不能置之不理啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x8,
        (
            "#12P因为看好你们解决之前那起事件时的本领，\x01",
            "所以就没有拜托游击士，\x01",
            "而是向各位发出了支援请求。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x104,
        (
            "#5P#0309F嘿嘿……看来我们的行情\x01",
            "也略微上涨了一点嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)

    #C0244
    ChrTalk(
        0x103,
        (
            "#5P#0203F……这虽然值得高兴，\x01",
            "但现在可不是得意的时候。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x104,
        (
            "#5P#0304F知～道啦。\x01",
            "……那么，就赶紧去\x01",
            "把魔兽都赶跑吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0246
    ChrTalk(
        0x101,
        (
            "#5P#0001F嗯……\x01",
            "看来事不宜迟啊。\x02\x03",

            "这样下去的话，\x01",
            "大家都没法干活了吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_43BB():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43BB)
    Sleep(50)

    def lambda_43CB():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43CB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    #C0247
    ChrTalk(
        0x8,
        (
            "#12P哦哦，你们愿意接受吗……\x01",
            "太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x8,
        (
            "#12P那么……你们\x01",
            "收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0249
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '小箱子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了 。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('小箱子', 1)

    #C0250
    ChrTalk(
        0x8,
        (
            "#12P有了这把钥匙，\x01",
            "就能进入私有地了。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "#12P私有地就在古道的东南方向，\x01",
            "沿路走下去就是了。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x8,
        (
            "#12P不过，也许还是坐巴士\x01",
            "到途中的停靠站更好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "#12P私有地里的东西，\x01",
            "你们可以随便使用。\x01",
            "一切就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        "#5P#0001F明白了……就交给我们吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0255
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【讨伐古道私有地的魔兽】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -41000, 0, -1800, 90)
    OP_29(0xD, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_3E70 end

    def Function_13_45E3(): pass

    label("Function_13_45E3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-39840, 1950, -2730, 0)
    MoveCamera(325, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24700, 0)
    SetChrPos(0x101, -41000, 0, -1800, 90)
    SetChrPos(0x102, -41500, 0, -2800, 90)
    SetChrPos(0x103, -42500, 0, -800, 90)
    SetChrPos(0x104, -43250, 0, -1800, 90)
    SetChrPos(0x8, -39300, 180, -1800, 270)
    SetCameraDistance(23700, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0256
    ChrTalk(
        0x8,
        "#12P……是吗，把魔兽都消灭了啊？\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        (
            "#12P嗯……这样一来，应该就能\x01",
            "放心去干农活了。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "#12P太感谢你们了，\x01",
            "特别任务支援科的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x104,
        "#5P#0309F哪里哪里，这只是我们的分内之事啦。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        "#5P#0106F真是的，又开始得意忘形了。\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        (
            "#5P#0001F只是……\x01",
            "既然郊外地区还有私有地，\x01",
            "今后似乎也需要注意警惕魔兽呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        (
            "#12P唔，这个嘛……\x01",
            "也只有靠村里的人\x01",
            "来想想办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x8,
        (
            "#12P话说回来，真没想到这次的事情\x01",
            "是由之前那起魔兽事件引起的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x8,
        (
            "#12P自那以后，明明都过去\x01",
            "将近一个月了……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#5P#0203F虽然只是推测，\x01",
            "但可能性应该很高。\x02\x03",

            "#0200F不过，把这批消灭了以后，\x01",
            "应该就不会再有那么多魔兽\x01",
            "接近私有地了。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x8,
        (
            "#12P是吗……\x01",
            "听你这样说，我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x8,
        (
            "#12P总而言之，这次真是帮大忙了。\x01",
            "以后再有什么事的话，还要麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x101,
        (
            "#5P#0000F请您放心，\x01",
            "我们到时一定会尽快赶过来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x102,
        "#5P#0100F那么，我们就先失陪了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【讨伐古道私有地的魔兽】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -41000, 0, -1800, 90)
    OP_29(0xD, 0x1, 0x3)
    OP_29(0xD, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_13_45E3 end

    def Function_14_4A27(): pass

    label("Function_14_4A27")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09300.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch00202.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("apl/ch50014.itc", 0x24)
    OP_68(-44120, 1200, -2790, 0)
    MoveCamera(318, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrPos(0xD, -40600, 0, -2700, 0)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -40600, 0, -1200, 180)
    SetChrPos(0x101, -46400, 0, -1800, 90)
    SetChrPos(0x102, -46400, 0, -3000, 90)
    SetChrPos(0x103, -47800, 0, -3000, 90)
    SetChrPos(0x104, -47800, 0, -1800, 90)
    FadeToBright(1000, 0)
    OP_68(-42120, 1200, -2790, 3000)
    OP_6F(0x1)
    OP_0D()

    #N0271
    NpcTalk(
        0xD,
        "面容温和的男性",
        (
            "#3609F#6P……托您的福，\x01",
            "这笔生意很成功。\x02\x03",

            "#3600F今后也请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    #N0272
    NpcTalk(
        0x8,
        "老人",
        "#11P嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()

    #N0273
    NpcTalk(
        0x8,
        "老人",
        (
            "#11P话虽如此……\x01",
            "但这个价格真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0274
    NpcTalk(
        0x8,
        "老人",
        "#11P比其他商人给的价格高了两成吧？\x02",
    )

    CloseMessageWindow()

    #N0275
    NpcTalk(
        0xD,
        "面容温和的男性",
        (
            "#3604F#6P这只是因为村里的特产\x01",
            "很受好评，值得上这个价格。\x02\x03",

            "#3600F我还是会有不少利润的，\x01",
            "请您不必担心。\x02",
        )
    )

    CloseMessageWindow()

    #N0276
    NpcTalk(
        0x8,
        "老人",
        (
            "#11P是吗……\x01",
            "哎呀，真是承蒙你照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #N0277
    NpcTalk(
        0x8,
        "老人",
        (
            "#11P下次带你的夫人和儿子\x01",
            "一起来玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0278
    NpcTalk(
        0x8,
        "老人",
        "#11P我会好好招待他们的。\x02",
    )

    CloseMessageWindow()

    #N0279
    NpcTalk(
        0xD,
        "面容温和的男性",
        (
            "#3609F#6P哈哈……\x01",
            "谢谢您了。\x02\x03",

            "#3600F那么，村长。\x01",
            "我下次再来。\x02",
        )
    )

    CloseMessageWindow()

    #N0280
    NpcTalk(
        0x8,
        "老人",
        "#11P唔，下次见啊。\x02",
    )

    CloseMessageWindow()

    def lambda_4D72():

        label("loc_4D72")

        TurnDirection(0x8, 0xD, 500)
        Yield()
        Jump("loc_4D72")

    QueueWorkItem2(0x8, 1, lambda_4D72)
    OP_93(0xD, 0x10E, 0x12C)
    OP_68(-44550, 1200, -2490, 2000)

    def lambda_4D9C():
        OP_95(0xFE, -43890, 0, -1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4D9C)
    WaitChrThread(0xD, 1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0281
    NpcTalk(
        0xD,
        "面容温和的男性",
        "#3605F啊，不好意思……\x02",
    )

    CloseMessageWindow()
    OP_68(-45790, 1200, -1120, 3000)

    def lambda_4E0B():
        OP_96(0xFE, 0xFFFF498A, 0x0, 0xFFFFFD08, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E0B)

    def lambda_4E25():
        OP_96(0xFE, 0xFFFF461A, 0x0, 0xFFFFF9C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E25)

    def lambda_4E3F():
        OP_96(0xFE, 0xFFFF41D8, 0x0, 0xFFFFF434, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4E3F)

    def lambda_4E59():
        OP_96(0xFE, 0xFFFF4296, 0x0, 0xFFFFF966, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4E59)

    def lambda_4E73():

        label("loc_4E73")

        TurnDirection(0x101, 0xD, 500)
        Yield()
        Jump("loc_4E73")

    QueueWorkItem2(0x101, 1, lambda_4E73)

    def lambda_4E85():

        label("loc_4E85")

        TurnDirection(0x102, 0xD, 500)
        Yield()
        Jump("loc_4E85")

    QueueWorkItem2(0x102, 1, lambda_4E85)

    def lambda_4E97():

        label("loc_4E97")

        TurnDirection(0x103, 0xD, 500)
        Yield()
        Jump("loc_4E97")

    QueueWorkItem2(0x103, 1, lambda_4E97)

    def lambda_4EA9():

        label("loc_4EA9")

        TurnDirection(0x104, 0xD, 500)
        Yield()
        Jump("loc_4EA9")

    QueueWorkItem2(0x104, 1, lambda_4EA9)
    OP_68(-47580, 1200, -1450, 2000)

    def lambda_4ECC():
        OP_95(0xFE, -46980, 0, -3680, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4ECC)
    WaitChrThread(0xD, 1)
    OP_93(0xD, 0xB4, 0x1F4)
    Sound(103, 0, 100, 0)

    def lambda_4EF7():
        OP_95(0xFE, -47000, 0, -4530, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4EF7)

    def lambda_4F11():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_4F11)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xD, 2)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x1)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)
    Sleep(300)
    Sound(104, 0, 100, 0)
    Sleep(700)

    #C0282
    ChrTalk(
        0x101,
        "#0005F#11P刚才的人……\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x102,
        "#0100F#5P好像是个商人……\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x104,
        (
            "#0300F#5P嗯，看来这里\x01",
            "的确是村长家没错啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FD1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4FD1)
    WaitChrThread(0x8, 1)

    #N0285
    NpcTalk(
        0x8,
        "老人的声音",
        "#1P你们几位是……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5051():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5051)

    def lambda_505E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_505E)

    def lambda_506B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_506B)

    def lambda_5078():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5078)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_68(-44030, 1200, -1870, 2500)

    def lambda_50A6():
        OP_96(0xFE, 0xFFFF59DE, 0x0, 0xFFFFF862, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_50A6)
    Sleep(800)

    def lambda_50C3():
        OP_96(0xFE, 0xFFFF5420, 0x0, 0xFFFFF862, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50C3)
    Sleep(50)

    def lambda_50E0():
        OP_96(0xFE, 0xFFFF4F3E, 0x0, 0xFFFFFB82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50E0)
    Sleep(50)

    def lambda_50FD():
        OP_96(0xFE, 0xFFFF4F3E, 0x0, 0xFFFFF542, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_50FD)
    Sleep(50)

    def lambda_511A():
        OP_96(0xFE, 0xFFFF4A5C, 0x0, 0xFFFFF862, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_511A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x8, 1)
    OP_6F(0x1)

    #C0286
    ChrTalk(
        0x101,
        "#0000F#5P──打扰了。\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x102,
        (
            "#0100F#5P请问您是\x01",
            "这个村子的村长吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0288
    NpcTalk(
        0x8,
        "老人",
        "#2P唔，正是。\x02",
    )

    CloseMessageWindow()

    #N0289
    NpcTalk(
        0x8,
        "老人",
        (
            "#2P我叫特鲁塔……\x01",
            "你们是游客吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#0003F不……\x02\x03",

            "#0001F其实我们是来调查\x01",
            "这个村子发生的魔兽灾害的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0291
    ChrTalk(
        0x8,
        "#2P哦哦，那件事吗！\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        (
            "#2P哎呀，警备队的人\x01",
            "也来调查了好几次……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        (
            "#2P但最后什么也没查出来。\x01",
            "你们能来，我也就放心啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0294
    ChrTalk(
        0x103,
        "#0206F#5P（这个，莫非……）\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x104,
        "#5P#0306F（嗯，又是那种误会吧。）\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x102,
        (
            "#5P#0106F（唉……\x01",
            "  都已经见怪不怪了啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        (
            "#0006F#5P……不好意思，\x01",
            "是我没解释清楚。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0298
    ChrTalk(
        0x8,
        "#2P嗯，怎么说……？\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#0003F#5P很遗憾，我们\x01",
            "并非游击士协会的人。\x02\x03",

            "#0000F而是克洛斯贝尔警察局，\x01",
            "隶属于特别任务支援科的搜查官——\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    OP_68(-36090, 2400, -2550, 0)
    MoveCamera(327, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -38500, 200, -1500, 90)
    SetChrPos(0x102, -38500, 200, -2800, 90)
    SetChrPos(0x103, -34300, 200, -1700, 270)
    SetChrPos(0x104, -34300, 200, -3000, 270)
    SetChrPos(0x8, -36300, 200, 100, 180)
    SetMapObjFrame(0xFF, "kage03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ha03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika00", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_68(-36090, 1400, -2550, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0300
    ChrTalk(
        0x8,
        (
            "#11P唔……\x01",
            "原来是克洛斯贝尔警察局的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x8,
        "#11P真抱歉，是我搞错了。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x8,
        (
            "#11P毕竟市里的警察\x01",
            "很少会来我们村子嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x8,
        (
            "#11P以那位亚里欧斯先生为首的\x01",
            "游击士倒是来过几次。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        "#5P#0006F是、是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x104,
        (
            "#6P#0306F那位大叔……\x01",
            "身为大红人，办事还挺认真的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x102,
        (
            "#0103F#6P对了，特鲁塔村长……\x02\x03",

            "#0101F我们来调查的原委，\x01",
            "正如刚才所说。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        (
            "#5P#0001F能麻烦您\x01",
            "再把受害情况\x01",
            "说明一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x8,
        "#11P唔，这个啊……\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "#11P──那是在三个星期前的事情，\x01",
            "那天晚上，新月刚好挂在天空。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x8,
        (
            "#11P一群魔兽潜进了我们的村子，\x01",
            "把农作物什么的全都糟蹋了。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x8,
        (
            "#11P各家的家畜、水果，\x01",
            "还有小麦都遭了灾。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#5P#0001F听说……\x01",
            "好像没有任何目击者吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x8,
        (
            "#11P唔，和克洛斯贝尔市市民不同，\x01",
            "我们村的人晚上都睡得很早。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x8,
        (
            "#11P早上还要早起干农活，\x01",
            "所以当时几乎全村人都睡熟了。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x8,
        (
            "#11P结果，早上起来一看，\x01",
            "就发现了魔兽们的足迹\x01",
            "和受害的惨状。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        "#5P#0003F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x103,
        (
            "#12P#0200F所以才确定\x01",
            "是狼形魔兽吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "#11P唔……因为现场留下的足迹\x01",
            "形状就是犬科生物的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x8,
        (
            "#11P正好当天有警备队的\x01",
            "巡逻人员过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x8,
        (
            "#11P保险起见，他们就在周边地域\x01",
            "进行了搜索……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        (
            "#0103F#6P可是完全没有发现\x01",
            "狼形魔兽的踪迹……\x02\x03",

            "#0101F原来如此，\x01",
            "和警备队的调查书内容吻合呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        "#11P唔，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x8,
        (
            "#11P之后过了三个星期……\x01",
            "一直到今天，\x01",
            "也没有再次发生灾害。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x8,
        (
            "#11P老实说，我还以为\x01",
            "再也不会发生那种事了……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x8,
        (
            "#11P唔唔，但没想到，\x01",
            "其它地方竟然又受灾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        "#5P#0003F是的……\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x104,
        (
            "#6P#0300F话说回来……\x01",
            "尽管被魔兽袭击了，\x01",
            "但这个村子好像却非常平静啊。\x02\x03",

            "损失金额应该也不小吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    #C0328
    ChrTalk(
        0x8,
        (
            "#11P不，其实\x01",
            "也没多少。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        (
            "#11P每家的损失\x01",
            "都只有一点点而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1500)

    #C0330
    ChrTalk(
        0x101,
        "#5P#0005F……是这样吗？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(200)

    #C0331
    ChrTalk(
        0x8,
        (
            "#11P唔，损失总额\x01",
            "也就十万米拉左右吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        (
            "#11P话虽如此，\x01",
            "到底也都是损失嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x8,
        (
            "#11P本来还真是有点消沉，\x01",
            "不过，好在刚做了一笔不错的买卖。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        (
            "#11P大家所受的损失\x01",
            "基本也都补回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        "#5P#0005F不错的买卖……\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x103,
        (
            "#12P#0205F难不成……\x01",
            "就是和刚才的那位客人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x8,
        (
            "#11P嗯，他是这几年来\x01",
            "和我们一直交情很好的\x01",
            "克洛斯贝尔市贸易商。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#11P听说了受灾的事情，\x01",
            "就把收购价提高了一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x8,
        (
            "#11P哎呀呀，\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x102,
        "#0100F#6P原来是这样……\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x104,
        (
            "#6P#0300F是贸易商啊，\x01",
            "难怪穿着那么\x01",
            "考究的衣服。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x8,
        "#11P嗯，而且……\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x8,
        (
            "#11P……考虑到克洛斯贝尔目前的情况，\x01",
            "这种程度的损害或许已经算是很轻的了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0344
    ChrTalk(
        0x101,
        "#5P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x102,
        "#0101F#6P请问，您这话是……\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x8,
        (
            "#11P啊……\x01",
            "是我多言了。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        "#11P抱歉抱歉，请忘了吧。\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        (
            "#6P#0306F喂喂，村长先生。\x02\x03",

            "#0301F你这样说，\x01",
            "只会让人更加在意啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x103,
        (
            "#0203F#12P……的确是呢，\x01",
            "这样也太吊人胃口了。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x8,
        "#11P哈哈哈，那倒也是啊。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x8,
        (
            "#11P可能只是老人的一点胡言乱语而已，\x01",
            "即使这样，你们也要听吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x101,
        (
            "#5P#0003F嗯……\x01",
            "请务必说给我们听听。\x02\x03",

            "#0001F在如今这种情况下，\x01",
            "也不知道能在哪里得到有用的线索。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x8,
        "#11P唔……既然如此。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7202", 0)
    Sleep(500)

    #C0354
    ChrTalk(
        0x8,
        (
            "#11P──你们\x01",
            "听说过\x01",
            "『神狼』这个词吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0355
    ChrTalk(
        0x101,
        "#5P#0005F『神狼』……\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x102,
        "#0105F#6P神之狼吗？\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        (
            "#0200F#12P……这个词在数据库里\x01",
            "也没见过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        "#11P唔，果然是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x8,
        (
            "#11P也就是说，在市里已经听不到\x01",
            "这个传说了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x8,
        "#11P真令人唏嘘啊。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x101,
        (
            "#5P#0001F嗯……\x01",
            "您说的『神狼』到底是？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#11P是很久以前栖息在\x01",
            "克洛斯贝尔本地的野兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x8,
        (
            "#11P据说，它们的毛色雪白，\x01",
            "外形像狼一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0364
    ChrTalk(
        0x101,
        "#5P#0005F这个……！？\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x103,
        (
            "#0205F#12P和造成这次\x01",
            "破坏的魔兽一样……？\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x8,
        (
            "#11P虽然还没有确凿的证据──不过，\x01",
            "就算是它们干的，也并不奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        (
            "#11P根据自古以来的传说，\x01",
            "神狼们不是普通的魔兽，\x01",
            "而是被女神派遣而来的圣兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x8,
        (
            "#11P在古代，克洛斯贝尔\x01",
            "曾被卷入腥风血雨的战争……\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x8,
        (
            "#11P那时，它们见证着人类发动战争的愚蠢行径，\x01",
            "时而也随性拯救一些弱小的人们……\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x8,
        "#11P似乎就是这样的存在。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        "#0101F#6P竟然有这样的传说……\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#5P#0008F如此说来……\x01",
            "以前好像还看过\x01",
            "有白狼登场的童话呢。\x02\x03",

            "#0003F我记得市里的\x01",
            "图书馆中应该就有。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        (
            "#11P唔，那部童话多半就是\x01",
            "以传说为蓝本而创作的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x8,
        (
            "#11P──可是，在这几十年来，\x01",
            "克洛斯贝尔已经变了。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        (
            "#11P在帝国、共和国双方的影响下，\x01",
            "发展成贸易都市的同时，\x01",
            "也忘却了过去的历史。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x8,
        (
            "#11P而不知不觉间……\x01",
            "『神狼』们也消失了踪影。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x103,
        "#0208F#12P………………………………\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        (
            "#6P#0306F唔……想必是已经\x01",
            "对人类绝望了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        (
            "#11P唔……\x01",
            "我也是这么想的。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        (
            "#11P总之，『神狼』们就这么\x01",
            "消失在了时代的夹缝中。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "#11P如果它们重新出现……\x01",
            "我想，可能是来\x01",
            "为什么事而敲响警钟的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#5P#0001F警钟吗……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x8,
        (
            "#11P这么说或许不大好……\x01",
            "但我总觉得克洛斯贝尔市现在\x01",
            "发展得太急进了。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x8,
        (
            "#11P偶尔乘巴士进城，\x01",
            "都会对其变化感到愕然。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x8,
        (
            "#11P仿佛人人都在忙着追逐现在，\x01",
            "却失去了回顾过去的闲暇……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x8,
        "#11P在我看来，就是这样。\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        "#5P#0008F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x102,
        "#0106F#6P……真是无言以对。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x8,
        (
            "#11P啊，别误会。\x01",
            "我也不是想说教。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x8,
        (
            "#11P只不过呢，如此想来，\x01",
            "我们村子遭到的损害，\x01",
            "或许也是来自它们的一种警告……\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x8,
        (
            "#11P这样理解的话，\x01",
            "应该也讲得通吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0392
    ChrTalk(
        0x8,
        (
            "#11P唔，看来你们好像\x01",
            "都当真了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x8,
        (
            "#11P算啦，只是老人家说的胡话而已。\x01",
            "也不用那么当真。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x101,
        (
            "#5P#0004F不……\x01",
            "您的话很有参考价值。\x02\x03",

            "#0000F关于这次魔兽灾害的调查，\x01",
            "我感觉，似乎已经有了新的视角。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x8,
        "#11P唔，那就好……\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x8,
        (
            "#11P你们说是来调查的吧，\x01",
            "还有没有什么我能帮得上忙的？\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        (
            "#5P#0000F这个嘛……\x02\x03",

            "我们打算再找其他村民们\x01",
            "打听一下，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x8,
        (
            "#11P嗯，如果是你们几个的话，\x01",
            "应该没什么问题吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x8,
        (
            "#11P正好到中午了，\x01",
            "外出干农活的人\x01",
            "应该也都回来了吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x4)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    SetChrPos(0x0, -41820, 0, -1890, 270)
    SetChrPos(0x8, -38480, 180, -1780, 90)
    OP_4C(0x8, 0xFF)
    SetMapObjFrame(0xFF, "kage03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ha03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kage02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika00", 0x1, 0x1)
    SetScenarioFlags(0x60, 5)
    OP_29(0x3F, 0x1, 0x3)
    ClearMapFlags(0x10000000)
    PlayBGM("ed7120", 0)
    EventEnd(0x5)
    Return()

    # Function_14_4A27 end

    def Function_15_6B96(): pass

    label("Function_15_6B96")

    EventBegin(0x0)
    Fade(500)
    OP_68(40430, 1500, -580, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23400, 0)
    SetChrPos(0x101, 40500, 0, 0, 270)
    SetChrPos(0x102, 40500, 0, 1200, 270)
    SetChrPos(0x103, 41700, 0, 0, 270)
    SetChrPos(0x104, 41700, 0, 1200, 270)
    SetChrSubChip(0xB, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C43")
    SetChrPos(0x109, 41100, 0, -1200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_6C6E")

    label("loc_6C43")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C6E")
    SetChrPos(0x10A, 41100, 0, -1200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_6C6E")

    OP_0D()

    #C0400
    ChrTalk(
        0x101,
        (
            "#12P#0000F那个……\x01",
            "请问您是\x01",
            "多纳尔德先生吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xB,
        (
            "#5P俺就是多纳尔德啊。\x01",
            "……有事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        (
            "#12P#0000F我们是克洛斯贝尔警察局的人。\x01",
            "稍微有点事情找您……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0403
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德说明了回收\x01",
            "逾期未还图书的事由。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0404
    ChrTalk(
        0xB,
        (
            "#5P……啊，原来是来\x01",
            "取那本书的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xB,
        (
            "#5P嗯～这样的话，\x01",
            "可得向你们道歉了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E1A")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_6E1A")

    Sleep(1000)

    #C0406
    ChrTalk(
        0x101,
        "#12P#0005F道歉……难不成！？\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x104,
        (
            "#12P#0305F四重转借了吗？\x02\x03",

            "#0306F我说～这也\x01",
            "太离谱了吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xB,
        "#5P不，俺倒是没有转借……\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xB,
        (
            "#5P只是在干农活的间隙看了看，\x01",
            "之后就不知道丢到哪里去了哇。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xB,
        (
            "#5P看样子，像是\x01",
            "搞丢了哇。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F83")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_6F83")

    Sleep(1000)

    #C0411
    ChrTalk(
        0x102,
        "#11P#0105F怎、怎么会……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FE5")

    #C0412
    ChrTalk(
        0x109,
        (
            "#6P#0506F这情况好像比转借\x01",
            "更糟糕啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7050")

    label("loc_6FE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7050")

    #C0413
    ChrTalk(
        0x10A,
        (
            "#6P#0601F………………………………\x01",
            "（所以说，不守规则的人\x01",
            "  真是让人无法忍受………！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7050")


    #C0414
    ChrTalk(
        0x103,
        (
            "#12P#0200F您还有什么印象吗？\x01",
            "比如说，最后看书的地方之类的。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xB,
        (
            "#5P哦，就是那里，喏。\x01",
            "村长家的前面，\x01",
            "那个养蜂场的小屋。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xB,
        (
            "#5P俺没事时就在那里面看书，\x01",
            "结果不知几时就找不到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xB,
        "#5P呀，真是抱歉啊。\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x101,
        (
            "#12P#0006F总、总而言之……\x02\x03",

            "#0000F如果书还在的话，\x01",
            "似乎也只会在那间小屋里了。\x01",
            "去那里找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_71AA")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_71AA")

    SetChrPos(0x0, 40500, 0, 0, 270)
    SetChrSubChip(0xB, 0x0)
    OP_29(0x28, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_15_6B96 end

    def Function_16_71C8(): pass

    label("Function_16_71C8")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0419
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '彩虹·FanBook'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('彩虹·FanBook', 1)
    EventBegin(0x0)
    Fade(500)
    OP_68(76390, 1500, -1840, 0)
    MoveCamera(340, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23510, 0)
    SetChrPos(0x101, 75420, 0, -450, 135)
    SetChrPos(0x102, 76950, 0, -530, 225)
    SetChrPos(0x103, 75550, 0, -1930, 45)
    SetChrPos(0x104, 77080, 0, -2020, 315)
    SetChrSubChip(0xB, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72C0")
    SetChrPos(0x109, 76640, 0, -2920, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_72EB")

    label("loc_72C0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72EB")
    SetChrPos(0x10A, 76640, 0, -2920, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_72EB")

    OP_0D()

    #C0420
    ChrTalk(
        0x101,
        (
            "#5P#0000F……盖有图书馆的印章，\x01",
            "阿尔弗雷德先生借了没还的\x01",
            "应该就是这本书了。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x102,
        (
            "#11P#0106F呼，还好找到了。\x02\x03",

            "#0105F话说回来……\x01",
            "原来是彩虹剧团的\x01",
            "FanBook啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73C9")

    #C0422
    ChrTalk(
        0x109,
        "#6P#0500F我记得这本书好像相当稀有呢。\x02",
    )

    CloseMessageWindow()

    label("loc_73C9")


    #C0423
    ChrTalk(
        0x104,
        (
            "#12P#0306F所以人人\x01",
            "都想看，\x01",
            "这也是没办法的事啊。\x02\x03",

            "#0309F呼，连我都想\x01",
            "偷偷拿走呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7473")

    #C0424
    ChrTalk(
        0x10A,
        "#6P#0601F（瞪……）\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x104,
        "#12P#0306F不不，开玩笑，开个玩笑啦。\x02",
    )

    CloseMessageWindow()

    label("loc_7473")


    #C0426
    ChrTalk(
        0x103,
        (
            "#6P#0206F……这种玩笑还是等把书还给\x01",
            "图书馆以后再开吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_74D4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_74D4")

    SetChrPos(0x0, 76380, 0, -1420, 180)
    SetChrSubChip(0xB, 0x0)
    OP_29(0x28, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7512")
    OP_29(0x28, 0x1, 0x1F)

    label("loc_7512")

    OP_65(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_16_71C8 end

    SaveToFile()

Try(main)
