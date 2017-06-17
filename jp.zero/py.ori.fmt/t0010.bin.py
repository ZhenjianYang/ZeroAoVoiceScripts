from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "トルタ村長",             # 1
        "エナ夫人",               # 2
        "ミリア",                 # 3
        "ドナルド",               # 4
        "アンジェ",               # 5
        "ハロルド",               # 6
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

    DeclNpc(-38479,  180,     -1779,   90,   341,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
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
        "Function_5_68D",          # 05, 5
        "Function_6_19E6",         # 06, 6
        "Function_7_24F4",         # 07, 7
        "Function_8_2EA1",         # 08, 8
        "Function_9_4063",         # 09, 9
        "Function_10_4064",        # 0A, 10
        "Function_11_480F",        # 0B, 11
        "Function_12_490D",        # 0C, 12
        "Function_13_51F1",        # 0D, 13
        "Function_14_5683",        # 0E, 14
        "Function_15_7CE0",        # 0F, 15
        "Function_16_839C",        # 10, 16
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63C")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x85, 1)"), scpexpr(EXPR_END)), "loc_5C5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x85),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x103, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_637")

    label("loc_5C5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x85),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x85),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_637")

    Jump("loc_681")

    label("loc_63C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_681")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_540 end

    def Function_5_68D(): pass

    label("Function_5_68D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6AF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AF")
    Call(0, 12)
    Return()

    label("loc_6AF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_743")
    Jump("loc_78D")

    label("loc_743")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_763")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_78D")

    label("loc_763")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_783")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_78D")

    label("loc_783")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_78D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_918")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89C")

    #C0004
    ChrTalk(
        0xFE,
        (
            "……今の暮らしは\x01",
            "女神よりもたらされた\x01",
            "アルモリカ村の自然な姿なんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "無闇に発展を求めては\x01",
            "先の魔獣騒動のようなことが\x01",
            "再び起こるに違いない。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "……あやつの考えることは\x01",
            "分からんでもないがのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_913")

    label("loc_89C")


    #C0007
    ChrTalk(
        0xFE,
        (
            "村人により豊かな暮らしをという\x01",
            "デリックの考えは分からんでもないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "現村長として、これだけは譲れんのじゃ。\x02",
    )

    CloseMessageWindow()

    label("loc_913")

    Jump("loc_19DE")

    label("loc_918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9F6")

    #C0009
    ChrTalk(
        0xFE,
        (
            "デリックのように\x01",
            "村とクロスベル市と比較するなど\x01",
            "意味のない事だと思う……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "クロスベル市はクロスベル市、\x01",
            "アルモリカ村はアルモリカ村……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "どちらもあるべき姿に落ち着くのが\x01",
            "自然の摂理というものじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19DE")

    label("loc_9F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B08")

    #C0012
    ChrTalk(
        0xFE,
        (
            "先日、デリックと\x01",
            "村の今後について話し合ったのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "やはりどうしても\x01",
            "村を発展させるべきと言って\x01",
            "聞かんのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "記念祭中は欲を出したために\x01",
            "必要以上に観光客を呼び、\x01",
            "多くの問題も生じたというのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "デリックにも困ったものだ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B82")

    label("loc_B08")


    #C0016
    ChrTalk(
        0xFE,
        (
            "デリックのやつは、\x01",
            "村の現状を維持しようという\x01",
            "わしの考えが気に入らないんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "……一体どうしたらいいのかのう。\x02",
    )

    CloseMessageWindow()

    label("loc_B82")

    Jump("loc_19DE")

    label("loc_B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC1")

    #C0018
    ChrTalk(
        0xFE,
        (
            "ふむ……観光客も殆どは\x01",
            "クロスベル市へ戻ったようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "今回の観光客集めの為の出店……\x01",
            "本当に正しかったんじゃろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "確かに村としては潤ったが……\x01",
            "観光客が古戦場に迷い込むなど\x01",
            "迷惑もあったわけじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "……デリックが帰ってきたら、\x01",
            "一度しっかり話す必要がありそうじゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D50")

    label("loc_CC1")


    #C0022
    ChrTalk(
        0xFE,
        (
            "観光客が増え\x01",
            "村には利潤がもたらされたが\x01",
            "一部で迷惑の声も出た……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "……デリックが帰ってきたら、\x01",
            "一度しっかり話す必要がありそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D50")

    Jump("loc_19DE")

    label("loc_D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_E74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E01")

    #C0024
    ChrTalk(
        0xFE,
        (
            "……今年の記念祭は\x01",
            "やはり観光客が多かったのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "デリックの狙いは\x01",
            "成功したのだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "これが村の発展に\x01",
            "繋がったのだろうか……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E6F")

    label("loc_E01")


    #C0027
    ChrTalk(
        0xFE,
        (
            "観光客が来るのも、\x01",
            "今日あたりがピークじゃろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "果たしてこれが村の発展に\x01",
            "繋がったのだろうか……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6F")

    Jump("loc_19DE")

    label("loc_E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1023")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F96")

    #C0029
    ChrTalk(
        0xFE,
        (
            "ふむ……記念祭から観光客が流れてきて\x01",
            "村が賑やかになったのはいいが……\x01",
            "いつまで続くことやら。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "彼らは結局は観光客じゃからな。\x01",
            "記念祭が終わりに近づけば、\x01",
            "徐々に去っていくじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "農作業の邪魔だという話もある……\x01",
            "やはり、いいことばかりではないのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_101E")

    label("loc_F96")


    #C0032
    ChrTalk(
        0xFE,
        (
            "村が賑やかになるのも\x01",
            "この一時だけのような気がするわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "農作業の邪魔だという話もある……\x01",
            "やはり、いいことばかりではないのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101E")

    Jump("loc_19DE")

    label("loc_1023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1155")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CB")

    #C0034
    ChrTalk(
        0xFE,
        (
            "出店の様子もなかなか\x01",
            "好評だったようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "昔からハチミツ作りをしてきた\x01",
            "アルモリカ村の長として、\x01",
            "これほど誇りに思うことはないわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1150")

    label("loc_10CB")


    #C0036
    ChrTalk(
        0xFE,
        (
            "出店も好評だったようだし……\x01",
            "デリックに任せて\x01",
            "正解じゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "アルモリカ村の長として、\x01",
            "これほど誇りに思うことはないわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1150")

    Jump("loc_19DE")

    label("loc_1155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1288")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1219")

    #C0038
    ChrTalk(
        0xFE,
        (
            "デリックの進めておる出店……\x01",
            "なかなか順調に進んでおるようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "ふむ、村人も\x01",
            "なかなか楽しんでおるようだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "これは許可して\x01",
            "正解だったかもしれんのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1283")

    label("loc_1219")


    #C0041
    ChrTalk(
        0xFE,
        (
            "あとは実際に創立記念祭が\x01",
            "訪れてからの話か。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "観光客が来過ぎて、\x01",
            "よくないことが起こらねばいいが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1283")

    Jump("loc_19DE")

    label("loc_1288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_15FE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1322")

    #C0043
    ChrTalk(
        0xFE,
        "特務支援課か……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "最初会った時は、\x01",
            "警察がここまで頼れるとは\x01",
            "思いもよらなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        "また何かあったらよろしく頼む。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F9")

    label("loc_1322")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_13D0")

    #C0046
    ChrTalk(
        0xFE,
        (
            "魔獣の入り込んだ私有地は、\x01",
            "街道を南東方向に\x01",
            "進んでいったところにある。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "私有地内にあるものは、\x01",
            "自由に使ってくれて構わん。\x01",
            "どうかよろしく頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F9")

    label("loc_13D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F4")

    #C0048
    ChrTalk(
        0xFE,
        (
            "息子のデリックに\x01",
            "村興しの提案をされてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "余り派手にやりすぎて\x01",
            "慎ましやかな暮らしを忘れるのは\x01",
            "良くないとは思うたのじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "創立記念祭の出店程度なら\x01",
            "以前行われた時にも参加したので、\x01",
            "やってみるよう勧めたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "はてさて、\x01",
            "どのような結果になるのやら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15F9")

    label("loc_14F4")


    #C0052
    ChrTalk(
        0xFE,
        (
            "クロスベル市の姿を見ると、\x01",
            "発展することが必ずしも\x01",
            "いいことではない、と思うんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "わしはこの村くらいは\x01",
            "昔のまま質素でいいと思っておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "息子のデリックは\x01",
            "それが気に入らんようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "はてさて、記念祭への出店が\x01",
            "どのような結果になるのやら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F9")

    Jump("loc_19DE")

    label("loc_15FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1706")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A5")

    #C0056
    ChrTalk(
        0xFE,
        (
            "昨日、君たちに聞いた話をもとに\x01",
            "村人に注意を促しておいたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "まだ魔獣は見つかっていないんじゃろう？\x01",
            "この村もまだ安心は出来ぬのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1701")

    label("loc_16A5")


    #C0058
    ChrTalk(
        0xFE,
        (
            "魔獣はまだ見つかっていないんじゃろう？\x01",
            "村人もそうだが、\x01",
            "君たちも充分気をつけるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1701")

    Jump("loc_19DE")

    label("loc_1706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_1851")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D2")

    #C0059
    ChrTalk(
        0xFE,
        "ふむ、やはり何も分からんかったか……\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "すでに３週間も前の話じゃ。\x01",
            "ある程度仕方ないじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "この村の外でも被害があったなら\x01",
            "そっちを当たった方が\x01",
            "賢明かもしれんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_184C")

    label("loc_17D2")


    #C0062
    ChrTalk(
        0xFE,
        (
            "それと『神狼』のことじゃが……\x01",
            "あくまであれはただの伝承じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "話しておいてなんだが\x01",
            "あまり捉われすぎんようにな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184C")

    Jump("loc_19DE")

    label("loc_1851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_19DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1938")

    #C0064
    ChrTalk(
        0xFE,
        (
            "しかし、聞き込みか……\x01",
            "警察の仕事も、\x01",
            "遊撃士に劣らず大変じゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "コトが起こったのは\x01",
            "なにぶん夜中じゃったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "大した情報があるかは分からんが……\x01",
            "村の者に一通り、聞いてみるとよかろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19DE")

    label("loc_1938")


    #C0067
    ChrTalk(
        0xFE,
        (
            "今の時間なら、\x01",
            "農作業に出ておった者も\x01",
            "村に戻っておるじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "川のほとりにある宿酒場、\x01",
            "《トネリコ亭》で昼食をとる者も多い。\x01",
            "よければ行ってみてはどうかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19DE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_68D end

    def Function_6_19E6(): pass

    label("Function_6_19E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A95")

    #C0069
    ChrTalk(
        0xFE,
        (
            "昨日も夫とデリックが\x01",
            "言い争いになってしまったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "親子なのだから、\x01",
            "どうにか分かり合って欲しいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "やはりしばらくは難しいでしょうね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F0")

    label("loc_1A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1B21")

    #C0072
    ChrTalk(
        0xFE,
        (
            "夫とデリックには\x01",
            "確固たる思想がありますから\x01",
            "対立はどうしても避けられません。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "……なかなかうまくいかないものですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F0")

    label("loc_1B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1BB5")
    SetChrSubChip(0xFE, 0x1)

    #C0074
    ChrTalk(
        0xFE,
        (
            "村長とその子供が対立していると\x01",
            "村の人にも不安を与えてしまうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "あなたもデリックを\x01",
            "優しく見守ってあげてくださいな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_24F0")

    label("loc_1BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C60")

    #C0076
    ChrTalk(
        0xFE,
        (
            "夫もデリックも\x01",
            "やり方は違いますが\x01",
            "常に村を想って行動してます。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "考えが対立するのは\x01",
            "ある程度仕方が無いのですが\x01",
            "私にとっては複雑です……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CDF")

    label("loc_1C60")


    #C0078
    ChrTalk(
        0xFE,
        (
            "親と子なのだから、\x01",
            "対立などせずに手を取り合って\x01",
            "ほしいのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "考え方が違う以上、\x01",
            "仕方が無いのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDF")

    Jump("loc_24F0")

    label("loc_1CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1DE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D99")

    #C0080
    ChrTalk(
        0xFE,
        (
            "夫は、昨日あたりから\x01",
            "記念祭の出店の是非について\x01",
            "悩んでいるようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "今回は上手く行くと思ったのに、\x01",
            "またデリックと\x01",
            "対立してしまいそうですね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DE1")

    label("loc_1D99")


    #C0082
    ChrTalk(
        0xFE,
        (
            "妻として、母として……\x01",
            "夫とデリックが対立するのは\x01",
            "複雑な想いです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE1")

    Jump("loc_24F0")

    label("loc_1DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1F00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E82")

    #C0083
    ChrTalk(
        0xFE,
        (
            "夫が観光客について\x01",
            "心配してるのもわかるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "まずは村を盛り上げようと\x01",
            "色々と取り成した\x01",
            "デリックを褒めてあげたいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EFB")

    label("loc_1E82")


    #C0085
    ChrTalk(
        0xFE,
        (
            "結果がどうあれ、\x01",
            "デリックが次期村長として\x01",
            "充分の素質があると分かった……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "それだけでも私には\x01",
            "充分の収穫だもの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFB")

    Jump("loc_24F0")

    label("loc_1F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1FAA")

    #C0087
    ChrTalk(
        0xFE,
        (
            "記念祭は今日もあわせて\x01",
            "あと４日もあるのだし、\x01",
            "まだまだ観光客は増えそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "丁寧にもてなすよう、\x01",
            "宿酒場のゴーファンさんに\x01",
            "お願いしておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F0")

    label("loc_1FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_20DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_204F")

    #C0089
    ChrTalk(
        0xFE,
        (
            "デリックが\x01",
            "あんな生き生きとしてるのを\x01",
            "久しぶりに見た気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "あの子も次期村長として\x01",
            "具体的な考えを\x01",
            "持っているのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20D5")

    label("loc_204F")


    #C0091
    ChrTalk(
        0xFE,
        (
            "デリックが積極的に\x01",
            "ことを進めている姿を見ると\x01",
            "安心しますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "あの子も次期村長として\x01",
            "具体的な考えを\x01",
            "持っているのでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D5")

    Jump("loc_24F0")

    label("loc_20DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_226C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F5")

    #C0093
    ChrTalk(
        0xFE,
        (
            "デリックと夫は\x01",
            "余り仲が良くないのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "夫は村長として\x01",
            "今の村の形を守ること……\x01",
            "それを大事にしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "ですが息子は次期村長として\x01",
            "村の皆に楽な暮らしをさせるよう\x01",
            "発展させていきたい、と。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "どちらも間違っていないので\x01",
            "難しい問題なんです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2267")

    label("loc_21F5")


    #C0097
    ChrTalk(
        0xFE,
        (
            "主張の違う夫と息子は\x01",
            "どうしても仲が良くなくって……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "あぁ、どうにか仲を取り持つ\x01",
            "いい方法はないのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2267")

    Jump("loc_24F0")

    label("loc_226C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_234B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FE")

    #C0099
    ChrTalk(
        0xFE,
        (
            "狼型魔獣がそんなに広範囲に\x01",
            "出没してたなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "いつまた村に来ても\x01",
            "おかしくないでしょうね。\x01",
            "あぁ怖い怖い……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2346")

    label("loc_22FE")


    #C0101
    ChrTalk(
        0xFE,
        (
            "とにかく、今度は人が\x01",
            "襲われるかもしれないわ。\x01",
            "用心しなくてはねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2346")

    Jump("loc_24F0")

    label("loc_234B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_23BD")

    #C0102
    ChrTalk(
        0xFE,
        (
            "あの事件には\x01",
            "村中が騒然としたものよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "あんなことが起こるなんて\x01",
            "滅多に無いことだからねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F0")

    label("loc_23BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_24F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2482")

    #C0104
    ChrTalk(
        0xFE,
        (
            "私もあの人と同じで\x01",
            "事件の夜はぐっすり寝ていたから……\x01",
            "お役には立てないと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "……そうねぇ。\x01",
            "もっと被害があった場所の近くにいる人に\x01",
            "聞いてみたらどうかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24F0")

    label("loc_2482")


    #C0106
    ChrTalk(
        0xFE,
        (
            "被害があったのは\x01",
            "養蜂場や家畜や畑の作物……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "それらを管理してた人に\x01",
            "聞いた方がいいんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F0")

    TalkEnd(0xFE)
    Return()

    # Function_6_19E6 end

    def Function_7_24F4(): pass

    label("Function_7_24F4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2588")
    Jump("loc_25D2")

    label("loc_2588")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25A8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25D2")

    label("loc_25A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25C8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25D2")

    label("loc_25C8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25D2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_26E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269C")

    #C0108
    ChrTalk(
        0xFE,
        (
            "昨日はちょっと多めに野菜がとれたから、\x01",
            "エルキンと一緒に卸しに行くの。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "あまり車に乗る機会がないから\x01",
            "ちょっと楽しみにしてるのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26DF")

    label("loc_269C")


    #C0110
    ChrTalk(
        0xFE,
        (
            "それにしてもエルキンめ、\x01",
            "車の点検にいつまでかかってんだか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26DF")

    Jump("loc_2E99")

    label("loc_26E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2764")

    #C0111
    ChrTalk(
        0xFE,
        (
            "今日は仕事に行く前に\x01",
            "お弁当でも作っとこうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "毎日《トネリコ亭》で食べてたら\x01",
            "飽きちゃうだろうしね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E99")

    label("loc_2764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_28A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2834")

    #C0113
    ChrTalk(
        0xFE,
        (
            "弟のエルキンは、興奮すると\x01",
            "言葉に訛りが出ちゃうのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "あれはアルモリカ訛りっていう\x01",
            "昔の村人の訛りだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "今じゃドナルドおじさんと\x01",
            "エルキンくらいしか訛らないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28A4")

    label("loc_2834")


    #C0116
    ChrTalk(
        0xFE,
        (
            "エルキンは昔、ドナルドおじさんに\x01",
            "結構遊んでもらってたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "だからいつの間にか訛りが\x01",
            "移っちゃったのね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A4")

    Jump("loc_2E99")

    label("loc_28A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_28B7")
    Jump("loc_2E99")

    label("loc_28B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_28C5")
    Jump("loc_2E99")

    label("loc_28C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28D3")
    Jump("loc_2E99")

    label("loc_28D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_28E1")
    Jump("loc_2E99")

    label("loc_28E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2971")

    #C0118
    ChrTalk(
        0xFE,
        (
            "村も記念祭に向けて\x01",
            "本格的に動き出してるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "……ってあたしも他人事じゃないか。\x01",
            "んー、何か手伝えることあるかしらね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E99")

    label("loc_2971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A27")

    #C0120
    ChrTalk(
        0xFE,
        (
            "弟のエルキンが\x01",
            "導力車に目がなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "村の皆でお金を出して買った\x01",
            "導力トラックを\x01",
            "私物化しちゃってるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "……ま、誰も文句言わないから\x01",
            "いいんだけどさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E99")

    label("loc_2A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2B53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B06")

    #C0123
    ChrTalk(
        0xFE,
        (
            "村の養蜂場にいくつか\x01",
            "木箱が並んでるの見たでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "あれは養蜂箱って言ってね、\x01",
            "中に蜂の巣を入れて\x01",
            "甘～いハチミツを作らせてるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "うっかり触らないようにね。\x01",
            "刺されても知らないわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B4E")

    label("loc_2B06")


    #C0126
    ChrTalk(
        0xFE,
        (
            "養蜂場の養蜂箱には\x01",
            "蜂の巣が入ってるの。\x01",
            "うっかり触らないようにね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B4E")

    Jump("loc_2E99")

    label("loc_2B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_2C54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0E")

    #C0127
    ChrTalk(
        0xFE,
        (
            "養蜂場で働いてるデリック……\x01",
            "いい奴なんだけど\x01",
            "どうにも真面目すぎてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "村長の息子だから\x01",
            "責任感じてるんだろうけど……\x01",
            "もっとラクに生きればいいのにね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C4F")

    label("loc_2C0E")


    #C0129
    ChrTalk(
        0xFE,
        (
            "のどかな村に住んでるんだもん。\x01",
            "のんびりラクに生きなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C4F")

    Jump("loc_2E99")

    label("loc_2C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_2D7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D13")

    #C0130
    ChrTalk(
        0xFE,
        (
            "農作業は時間をかけて\x01",
            "愛情もってやらないといけないわけ。\x01",
            "作物はさながら我が子みたいなもんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "それが荒らされた……\x01",
            "私達がどれだけ悲しんだか\x01",
            "分かるわよね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D79")

    label("loc_2D13")


    #C0132
    ChrTalk(
        0xFE,
        (
            "丹精込めて育てた\x01",
            "農作物が荒らされた……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "私達にとっちゃ、\x01",
            "我が子を傷つけられたようなもんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D79")

    Jump("loc_2E99")

    label("loc_2D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2E99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E1C")

    #C0134
    ChrTalk(
        0xFE,
        (
            "この村の眺めの良さは\x01",
            "サイコーのご馳走よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "あー、何だか眠くなってきちゃった。\x01",
            "村の納屋に忍び込んで\x01",
            "昼寝でもしようかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E99")

    label("loc_2E1C")


    #C0136
    ChrTalk(
        0xFE,
        (
            "村の納屋に忍び込んで\x01",
            "昼寝でもしようかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "……デリックに見つかったら\x01",
            "説教されるだろうし、\x01",
            "やっぱやめとこうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E99")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_24F4 end

    def Function_8_2EA1(): pass

    label("Function_8_2EA1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F35")
    Jump("loc_2F7F")

    label("loc_2F35")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F55")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F7F")

    label("loc_2F55")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F75")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F7F")

    label("loc_2F75")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F7F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3048")

    #C0138
    ChrTalk(
        0xFE,
        "お、本は見つかっただな。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "うーん、人のモノを\x01",
            "なくしちまうとは、\x01",
            "オラも配慮がたりなかっただ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "今後は気を付けるだよ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_3048")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_311F")

    #C0141
    ChrTalk(
        0xFE,
        (
            "オラが本をなくしたのは\x01",
            "村長の家の前の、\x01",
            "養蜂場に立ってる小屋だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "あの中で読んでたら\x01",
            "いつの間にか無くなっててよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "いや、ほんにすまねぇな。\x01",
            "悪いが探してみてくんろ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_311F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3140")
    Call(0, 15)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_3140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3279")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3220")
    SetChrSubChip(0xB, 0x0)

    #C0144
    ChrTalk(
        0xB,
        "いつもありがとなぁ、アンジェ。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "子供たちのこと、\x01",
            "ちゃんと面倒みてくれてよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xC,
        "あっは、何言ってんだい水臭い。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xC,
        (
            "そんなことはいいから、\x01",
            "これからもしっかりと\x01",
            "仕事を頑張っとくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3274")

    label("loc_3220")


    #C0148
    ChrTalk(
        0xFE,
        (
            "アンジェが子供たちを\x01",
            "ちゃんと面倒みてくれるから、\x01",
            "心置きなく仕事ができるだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3274")

    Jump("loc_405B")

    label("loc_3279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_33C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3353")

    #C0149
    ChrTalk(
        0xFE,
        (
            "村長の息子のデリックくんは\x01",
            "村を何とか発展させようと\x01",
            "がんばってるけんど……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "おらは今の村の姿が\x01",
            "一番だと思うだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "アルモリカ村が\x01",
            "クロスベル市みたいになったら\x01",
            "なんだか寂しいべ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_33C2")

    label("loc_3353")


    #C0152
    ChrTalk(
        0xFE,
        (
            "おらは今の村の姿が\x01",
            "一番だと思うだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "アルモリカ村が\x01",
            "クロスベル市みたいになったら\x01",
            "なんだか寂しいべ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33C2")

    Jump("loc_405B")

    label("loc_33C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_344B")

    #C0154
    ChrTalk(
        0xFE,
        "今年はなかなか豊作だべ。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "大分前に《神狼》のフリしてた犬が\x01",
            "人間の手で捕まったから、\x01",
            "きっとそのご褒美だべよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_405B")

    label("loc_344B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_34DD")

    #C0156
    ChrTalk(
        0xFE,
        (
            "記念祭……\x01",
            "今年も仕事、仕事で\x01",
            "終わっちまっただな。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "ま、農家の日常だなんて\x01",
            "そんなもんだから\x01",
            "今さらなんとも思わねぇけどな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_405B")

    label("loc_34DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_356A")

    #C0158
    ChrTalk(
        0xFE,
        (
            "今日の仕事も終わったし……\x01",
            "あとで《トネリコ亭》に\x01",
            "飲みにいくだかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "折角の記念祭中だ、\x01",
            "この位の楽しみは許されるべ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_405B")

    label("loc_356A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_36C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3640")

    #C0160
    ChrTalk(
        0xFE,
        (
            "観光客が増えて\x01",
            "賑やかになったのはいいだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "あんまり危ねぇ所に入らないよう\x01",
            "注意した方がいいかもしれねェなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "特にアルモリカ古道の途中にある\x01",
            "古戦場なんかは危ねぇかんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36BD")

    label("loc_3640")


    #C0163
    ChrTalk(
        0xFE,
        (
            "観光客には\x01",
            "危ねぇトコに入んねぇように\x01",
            "注意しねぇとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "特にアルモリカ古道の途中にある\x01",
            "古戦場なんかは危ねぇかんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36BD")

    Jump("loc_405B")

    label("loc_36C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D1")
    OP_4B(0xC, 0xFF)

    #C0165
    ChrTalk(
        0xFE,
        (
            "人づてに聞いたけんど、\x01",
            "今年の《アルカンシェル》は\x01",
            "すっげぇ出来だったらしいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "おらもチケットさえありゃあ、\x01",
            "畑仕事をほっぽり出してでも\x01",
            "行くンだけどな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    #C0167
    ChrTalk(
        0xC,
        "……なんか言ったかい？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    #C0168
    ChrTalk(
        0xFE,
        "……冗談だべよ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    OP_93(0xC, 0xCC, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_3860")

    label("loc_37D1")


    #C0169
    ChrTalk(
        0xFE,
        (
            "ま、まぁ、仕事をサボるってのは\x01",
            "冗談だとしても……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "このクロスベルに住んでりゃ\x01",
            "《アルカンシェル》を見たいってのは\x01",
            "誰でも思うことだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3860")

    Jump("loc_405B")

    label("loc_3865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3997")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_392E")

    #C0171
    ChrTalk(
        0xFE,
        (
            "創立記念祭が始まったら\x01",
            "ぽつぽつ、観光客が来るんだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "いや、出店を出すことをを考えると、\x01",
            "思った以上に人が来るかもしれねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        "うーん、緊張してくるだなァ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3992")

    label("loc_392E")


    #C0174
    ChrTalk(
        0xFE,
        (
            "たまに観光客や商人が来ることはあるけど、\x01",
            "来ても１、２人だからなぁ。\x01",
            "今回は覚悟しとかねェと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3992")

    Jump("loc_405B")

    label("loc_3997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3B47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A71")

    #C0175
    ChrTalk(
        0xFE,
        (
            "そういや、アルモリカ古道の途中に\x01",
            "通れなくなってる橋があるべ？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "あれの先にはな、\x01",
            "遥か昔の古戦場があンだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "なかなか雰囲気のある場所だけんど\x01",
            "魔獣がわんさかいるから気をつけるだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B42")

    label("loc_3A71")


    #C0178
    ChrTalk(
        0xFE,
        (
            "アルモリカ古道の途中の古戦場は、\x01",
            "なかなか雰囲気のある場所だぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "魔獣がいて危ねぇけど……\x01",
            "あんたらなら大丈夫かもしれねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "……ま、今は通れなくなってるけんど\x01",
            "機会があったら行ってみるといいべ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B42")

    Jump("loc_405B")

    label("loc_3B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C89")

    #C0181
    ChrTalk(
        0xFE,
        (
            "村の導力トラックは\x01",
            "皆で金を出し合って買っただ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "結構な値段だっただが、\x01",
            "作物をクロスベル市に持ってくのに\x01",
            "必要だから仕方ないだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "まぁ、ああいう便利なもんは\x01",
            "普及していくにつれて\x01",
            "安くなるもんだかんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "うちの子が自分の車を持つころにゃ\x01",
            "もう少し現実的な値段に\x01",
            "なってるはずだべ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D25")

    label("loc_3C89")


    #C0185
    ChrTalk(
        0xFE,
        (
            "導力車みたいな便利なもんは\x01",
            "普及していくにつれて\x01",
            "安くなるもんだかんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "うちの子が自分の車を持つころにゃ\x01",
            "もう少し現実的な値段に\x01",
            "なってるはずだべ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D25")

    Jump("loc_405B")

    label("loc_3D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_3EBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E1E")

    #C0187
    ChrTalk(
        0xFE,
        (
            "貿易商は各国を渡り歩いて……\x01",
            "ってイメージだけんど、\x01",
            "例のハロルドさんは違ってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "自治州内だけで\x01",
            "こつこつとやってきた\x01",
            "なかなかの努力家らしいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "今時、あんな堅実な貿易商も珍しいだ。\x01",
            "とにかくいい人だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3EB9")

    label("loc_3E1E")


    #C0190
    ChrTalk(
        0xFE,
        (
            "ハロルドさんとは結構親交があってな。\x01",
            "よく商売の相談に乗ってくれるだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "地道にこつこつと\x01",
            "地域の信用を得ていく……\x01",
            "今時あんな貿易商も珍しいだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EB9")

    Jump("loc_405B")

    label("loc_3EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_4052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FCD")

    #C0192
    ChrTalk(
        0xFE,
        (
            "少し前、農場が魔獣に荒らされてなぁ。\x01",
            "大事な作物や家畜にも被害が出ただよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "狼型魔獣の足跡が残ってたけんど、\x01",
            "ありゃあこの辺にはいない種類のモンだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "案外村長の言うとおり、\x01",
            "『神狼』の仕業かもしれねェだなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC5")
    SetScenarioFlags(0x68, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3FC5")

    SetScenarioFlags(0x0, 3)
    Jump("loc_404D")

    label("loc_3FCD")


    #C0195
    ChrTalk(
        0xFE,
        (
            "農場を荒らした狼型魔獣は、\x01",
            "この辺にはいない種類みてぇだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "案外村長の言うとおり、\x01",
            "『神狼』の仕業かもしれねェだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_404D")

    Jump("loc_405B")

    label("loc_4052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_405B")

    label("loc_405B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_2EA1 end

    def Function_9_4063(): pass

    label("Function_9_4063")

    Return()

    # Function_9_4063 end

    def Function_10_4064(): pass

    label("Function_10_4064")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4187")
    TurnDirection(0xC, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4119")

    #C0197
    ChrTalk(
        0xFE,
        (
            "今日はステファン君が朝早くから\x01",
            "カミーユたちと遊んでくれてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "あの子も今日はウチで食べてくだろう。\x01",
            "昼ごはんを多めに用意しないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4182")

    label("loc_4119")


    #C0199
    ChrTalk(
        0xFE,
        (
            "ステファン君も、元気のいい\x01",
            "ウチの子たちとよく遊んでくれるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        "今度奥さんにもお礼しなきゃねぇ。\x02",
    )

    CloseMessageWindow()

    label("loc_4182")

    Jump("loc_480B")

    label("loc_4187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4195")
    Jump("loc_480B")

    label("loc_4195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4232")

    #C0201
    ChrTalk(
        0xFE,
        (
            "《トネリコ亭》に宿をとってる\x01",
            "アレサさんとこの息子さんが\x01",
            "最近よく遊びに来るんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "うちの子供たちが\x01",
            "怪我とかさせなきゃいいけどねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_480B")

    label("loc_4232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_42C3")

    #C0203
    ChrTalk(
        0xFE,
        (
            "子供たちを記念祭に\x01",
            "連れてってやりたかったが……\x01",
            "まぁ仕方ないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "何にも仕事がないより\x01",
            "忙しいほうが何倍もマシってもんさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_480B")

    label("loc_42C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_439F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435D")

    #C0205
    ChrTalk(
        0xFE,
        (
            "記念祭、出来れば子供たちを\x01",
            "連れて行ってやりたかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "ま、来年はこの時期に\x01",
            "休めるように、\x01",
            "がんばるとするかねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_439A")

    label("loc_435D")


    #C0207
    ChrTalk(
        0xFE,
        (
            "来年こそは子供たちを\x01",
            "記念祭に連れて行ってやんないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_439A")

    Jump("loc_480B")

    label("loc_439F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_43AD")
    Jump("loc_480B")

    label("loc_43AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_44B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_444A")

    #C0208
    ChrTalk(
        0xFE,
        (
            "畑仕事が忙しくてね。\x01",
            "残念だけど記念祭にはいけないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "アレサさんとステファン君は\x01",
            "里帰りを兼ねて行ってるらしいけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_44B0")

    label("loc_444A")


    #C0210
    ChrTalk(
        0xFE,
        (
            "アレサさんとステファン君は\x01",
            "里帰りも兼ねて記念祭に行ってるらしい。\x01",
            "あはは、うらやましい限りだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44B0")

    Jump("loc_480B")

    label("loc_44B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_462C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44D1")
    Call(0, 11)
    Jump("loc_4627")

    label("loc_44D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_459E")

    #C0211
    ChrTalk(
        0xFE,
        (
            "一応、クロスベル市の知り合いに\x01",
            "確認とってもらったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの公演は\x01",
            "もう２ヶ月先まで予約一杯らしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "はぁー、やっぱり都会の人は\x01",
            "かける情熱がちがうねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4627")

    label("loc_459E")


    #C0214
    ChrTalk(
        0xFE,
        (
            "２ヵ月先までの予約か……\x01",
            "気の長いことだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "クロスベル市の人にとって\x01",
            "《アルカンシェル》には\x01",
            "それだけの価値があるんだろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4627")

    Jump("loc_480B")

    label("loc_462C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_47D8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4648")
    Call(0, 11)
    Jump("loc_47D3")

    label("loc_4648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_473F")

    #C0216
    ChrTalk(
        0xFE,
        (
            "頻発してた魔獣被害もなくなったから\x01",
            "安心して子供を外で遊ばせられるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "ただ、農家ってのは忙しくてね。\x01",
            "なかなか村の外に\x01",
            "連れ出してやれないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "創立記念祭へ連れて行け、\x01",
            "なんてせがまれたけど……\x01",
            "ちょっと厳しいねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_47D3")

    label("loc_473F")


    #C0219
    ChrTalk(
        0xFE,
        (
            "農家ってのは忙しくてね。\x01",
            "なかなか村の外に\x01",
            "連れ出してやれないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "創立記念祭へ連れて行け、\x01",
            "なんてせがまれたけど……\x01",
            "ちょっと厳しいねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47D3")

    Jump("loc_480B")

    label("loc_47D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_47E6")
    Jump("loc_480B")

    label("loc_47E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_47F4")
    Jump("loc_480B")

    label("loc_47F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_4802")
    Jump("loc_480B")

    label("loc_4802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_480B")

    label("loc_480B")

    TalkEnd(0xFE)
    Return()

    # Function_10_4064 end

    def Function_11_480F(): pass

    label("Function_11_480F")


    #C0221
    ChrTalk(
        0xFE,
        (
            "今、カルボナーラを作ってたんだ。\x01",
            "ウチの家族はみんな好きでねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "良かったら覚えていきなさいな。\x01",
            "自分で作って食べると格別だよ。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1AC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0224
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xA)
    Return()

    # Function_11_480F end

    def Function_12_490D(): pass

    label("Function_12_490D")

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
        "#5P#0000Fご無沙汰しています、トルタ村長。\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        (
            "#12P特務支援課の……！\x01",
            "よくぞ来て下さった。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "#12P先日の狼魔獣の事件解決、\x01",
            "村にもニュースが届いてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x8,
        (
            "#12P警察もなかなか\x01",
            "捨てたものじゃないと\x01",
            "皆で話したものじゃったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x104,
        (
            "#5P#0309Fいやぁ、それほどでも。\x02\x03",

            "#0301F……って世間話をしてる\x01",
            "場合じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        (
            "#5P#0100Fよろしければ、\x01",
            "依頼について詳しく事情を\x01",
            "聞かせていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x8,
        (
            "#12Pおお、そうじゃった。\x01",
            "重ねて、来てくれたことに\x01",
            "感謝しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x8,
        (
            "#12Pうむ……早速だが\x01",
            "説明をさせていただくと\x01",
            "しようかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        (
            "#5P#0200F要請では……\x01",
            "村の私有地に魔獣が侵入した、\x01",
            "ということでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        "#12Pうむ、いかにも。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x8,
        (
            "#12P村に来る道中に\x01",
            "見かけたかもしれんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "#12Pアルモリカ古道には、\x01",
            "資材置き場として使っている\x01",
            "村の私有地があるのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "#12Pそこに魔獣の群れが\x01",
            "進入してしまって、\x01",
            "困っておったのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        (
            "#5P#0103F魔獣の群れ……\x01",
            "確かに……それは危険ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        "#5P#0005F村の人に怪我人は？\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        "#12Pそれは今のところ出ておらん。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        (
            "#12Pただ、あそこには\x01",
            "農作業の道具なども置いているから\x01",
            "放っておくわけにもいかなくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x8,
        (
            "#12Pそこで、先の事件解決の腕を見込んで、\x01",
            "遊撃士ではなく諸君らに\x01",
            "支援要請を出したというわけなのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x104,
        (
            "#5P#0309Fへへっ……俺たちの株も\x01",
            "少しは上がってきたじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)

    #C0244
    ChrTalk(
        0x103,
        (
            "#5P#0203F……喜ばしいことですが、\x01",
            "今は浮かれている場合ではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x104,
        (
            "#5P#0304Fわーってるっつの。\x01",
            "……んじゃま、さっさと魔獣どもを\x01",
            "追い払いに行こうぜ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0246
    ChrTalk(
        0x101,
        (
            "#5P#0001Fああ……\x01",
            "急いだ方がよさそうだな。\x02\x03",

            "このままじゃ\x01",
            "仕事にならないだろうし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F68():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F68)
    Sleep(50)

    def lambda_4F78():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F78)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    #C0247
    ChrTalk(
        0x8,
        (
            "#12Pおお、請け負ってくれるか……\x01",
            "感謝するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x8,
        (
            "#12Pでは……これを\x01",
            "受け取ってくれるかね。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x33A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33A, 1)

    #C0250
    ChrTalk(
        0x8,
        (
            "#12Pその鍵があれば、\x01",
            "私有地に入ることができるじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "#12P私有地は、古道を南東方向に\x01",
            "進んでいったところにある。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x8,
        (
            "#12P途中まではバスを利用したほうが\x01",
            "いいかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "#12P私有地内にあるものは、\x01",
            "自由に使ってくれて構わん。\x01",
            "どうかよろしく頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        "#5P#0001F分かりました……お任せください。\x02",
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
            "クエスト【古道私有地の魔獣退治】\x07\x00",
            "を開始した！\x02",
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

    # Function_12_490D end

    def Function_13_51F1(): pass

    label("Function_13_51F1")

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
        "#12P……そうか、魔獣は殲滅できたか。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        (
            "#12Pうむ……これで安心して\x01",
            "農作業に取り組むことが出来そうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "#12P礼を言わせてもらうよ、\x01",
            "特務支援課の諸君。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x104,
        "#5P#0309Fいやいや、当然のことをしたまでッス。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        "#5P#0106Fまったく、調子がいいんだから。\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        (
            "#5P#0001Fただ……\x01",
            "街道に私有地がある以上、\x01",
            "これからも警戒は必要そうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        (
            "#12Pうむ、そうじゃな……\x01",
            "村の者でどうにかしていく\x01",
            "しかあるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x8,
        (
            "#12Pしかし、先日の魔獣事件が\x01",
            "事の発端だったとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x8,
        (
            "#12Pあれから一月近くも\x01",
            "経つというのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#5P#0203F推測の域は出ませんが\x01",
            "可能性は高いかと。\x02\x03",

            "#0200Fただ、今回退治されたことで\x01",
            "あれほどの魔獣が私有地に近づくことは\x01",
            "なくなると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x8,
        (
            "#12Pそうか……\x01",
            "それを聞いて安心したよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x8,
        (
            "#12Pとにかく、今回は助かった。\x01",
            "また何かあったらよろしく頼む。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x101,
        (
            "#5P#0000Fお任せください。\x01",
            "できるだけ迅速に駆けつけますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x102,
        "#5P#0100Fでは、これで失礼しますね。\x02",
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
            "クエスト【古道私有地の魔獣退治】\x07\x00",
            "を達成した！\x02",
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

    # Function_13_51F1 end

    def Function_14_5683(): pass

    label("Function_14_5683")

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
        "温和そうな男性",
        (
            "#3609F#6P……おかげさまで\x01",
            "良い取引をさせて頂きました。\x02\x03",

            "#3600F今後ともよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #N0272
    NpcTalk(
        0x8,
        "老人",
        "#11Pああ、こちらこそ。\x02",
    )

    CloseMessageWindow()

    #N0273
    NpcTalk(
        0x8,
        "老人",
        (
            "#11Pそれにしても……\x01",
            "本当にあの価格でいいのかね？\x02",
        )
    )

    CloseMessageWindow()

    #N0274
    NpcTalk(
        0x8,
        "老人",
        "#11P他の商人よりも２割は高いぞ？\x02",
    )

    CloseMessageWindow()

    #N0275
    NpcTalk(
        0xD,
        "温和そうな男性",
        (
            "#3604F#6Pそれだけ、この村の特産品が\x01",
            "認められているというだけです。\x02\x03",

            "#3600F十分儲けさせていただいてますから\x01",
            "どうかご心配なく。\x02",
        )
    )

    CloseMessageWindow()

    #N0276
    NpcTalk(
        0x8,
        "老人",
        (
            "#11Pそうか……\x01",
            "いや、本当に世話になるのう。\x02",
        )
    )

    CloseMessageWindow()

    #N0277
    NpcTalk(
        0x8,
        "老人",
        (
            "#11P今度は奥さんやお子さんと一緒に\x01",
            "遊びに来なさい。\x02",
        )
    )

    CloseMessageWindow()

    #N0278
    NpcTalk(
        0x8,
        "老人",
        "#11P歓迎させてもらいますぞ。\x02",
    )

    CloseMessageWindow()

    #N0279
    NpcTalk(
        0xD,
        "温和そうな男性",
        (
            "#3609F#6Pはは……\x01",
            "ありがとうございます。\x02\x03",

            "#3600Fそれでは村長。\x01",
            "また寄らせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #N0280
    NpcTalk(
        0x8,
        "老人",
        "#11Pうむ、またな。\x02",
    )

    CloseMessageWindow()

    def lambda_5A3E():

        label("loc_5A3E")

        TurnDirection(0x8, 0xD, 500)
        Yield()
        Jump("loc_5A3E")

    QueueWorkItem2(0x8, 1, lambda_5A3E)
    OP_93(0xD, 0x10E, 0x12C)
    OP_68(-44550, 1200, -2490, 2000)

    def lambda_5A68():
        OP_95(0xFE, -43890, 0, -1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5A68)
    WaitChrThread(0xD, 1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0281
    NpcTalk(
        0xD,
        "温和そうな男性",
        "#3605Fおっと、失礼……\x02",
    )

    CloseMessageWindow()
    OP_68(-45790, 1200, -1120, 3000)

    def lambda_5AD7():
        OP_96(0xFE, 0xFFFF498A, 0x0, 0xFFFFFD08, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5AD7)

    def lambda_5AF1():
        OP_96(0xFE, 0xFFFF461A, 0x0, 0xFFFFF9C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5AF1)

    def lambda_5B0B():
        OP_96(0xFE, 0xFFFF41D8, 0x0, 0xFFFFF434, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5B0B)

    def lambda_5B25():
        OP_96(0xFE, 0xFFFF4296, 0x0, 0xFFFFF966, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5B25)

    def lambda_5B3F():

        label("loc_5B3F")

        TurnDirection(0x101, 0xD, 500)
        Yield()
        Jump("loc_5B3F")

    QueueWorkItem2(0x101, 1, lambda_5B3F)

    def lambda_5B51():

        label("loc_5B51")

        TurnDirection(0x102, 0xD, 500)
        Yield()
        Jump("loc_5B51")

    QueueWorkItem2(0x102, 1, lambda_5B51)

    def lambda_5B63():

        label("loc_5B63")

        TurnDirection(0x103, 0xD, 500)
        Yield()
        Jump("loc_5B63")

    QueueWorkItem2(0x103, 1, lambda_5B63)

    def lambda_5B75():

        label("loc_5B75")

        TurnDirection(0x104, 0xD, 500)
        Yield()
        Jump("loc_5B75")

    QueueWorkItem2(0x104, 1, lambda_5B75)
    OP_68(-47580, 1200, -1450, 2000)

    def lambda_5B98():
        OP_95(0xFE, -46980, 0, -3680, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5B98)
    WaitChrThread(0xD, 1)
    OP_93(0xD, 0xB4, 0x1F4)
    Sound(103, 0, 100, 0)

    def lambda_5BC3():
        OP_95(0xFE, -47000, 0, -4530, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5BC3)

    def lambda_5BDD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_5BDD)
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
        "#0005F#11P今の人は……\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x102,
        "#0100F#5P商人の方みたいだけど……\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x104,
        (
            "#0300F#5Pま、ここが村長の家なのは\x01",
            "確かみてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CAD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5CAD)
    WaitChrThread(0x8, 1)

    #N0285
    NpcTalk(
        0x8,
        "老人の声",
        "#1Pお前さんたちは……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5D2F():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D2F)

    def lambda_5D3C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D3C)

    def lambda_5D49():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D49)

    def lambda_5D56():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5D56)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_68(-44030, 1200, -1870, 2500)

    def lambda_5D84():
        OP_96(0xFE, 0xFFFF59DE, 0x0, 0xFFFFF862, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5D84)
    Sleep(800)

    def lambda_5DA1():
        OP_96(0xFE, 0xFFFF5420, 0x0, 0xFFFFF862, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DA1)
    Sleep(50)

    def lambda_5DBE():
        OP_96(0xFE, 0xFFFF4F3E, 0x0, 0xFFFFFB82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DBE)
    Sleep(50)

    def lambda_5DDB():
        OP_96(0xFE, 0xFFFF4F3E, 0x0, 0xFFFFF542, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5DDB)
    Sleep(50)

    def lambda_5DF8():
        OP_96(0xFE, 0xFFFF4A5C, 0x0, 0xFFFFF862, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5DF8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x8, 1)
    OP_6F(0x1)

    #C0286
    ChrTalk(
        0x101,
        "#0000F#5P──失礼します。\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x102,
        (
            "#0100F#5Pあなたがこの村の\x01",
            "村長でいらっしゃいますか？\x02",
        )
    )

    CloseMessageWindow()

    #N0288
    NpcTalk(
        0x8,
        "老人",
        "#2Pうむ、いかにも。\x02",
    )

    CloseMessageWindow()

    #N0289
    NpcTalk(
        0x8,
        "老人",
        (
            "#2Pトルタという者じゃが……\x01",
            "あんたたち、観光客か何かかの？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#0003Fいえ……\x02\x03",

            "#0001F実は、この村であったという\x01",
            "魔獣被害を調べに来まして。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0291
    ChrTalk(
        0x8,
        "#2Pおお、あの件についてか！\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        (
            "#2Pいやな、警備隊の方でも\x01",
            "何度か調べてくれたんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        (
            "#2P結局、何も分からなくてな。\x01",
            "アンタたちが来てくれて一安心だ。\x02",
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
        "#0206F#5P（あの、これって……）\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x104,
        "#5P#0306F（ああ、またあのパターンだろ。）\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x102,
        (
            "#5P#0106F（ふう……\x01",
            "  もう驚かなくなってきたわね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        (
            "#0006F#5P……すみません。\x01",
            "言葉が足りませんでした。\x02",
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
        "#2Pん、それは……？\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#0003F#5P残念ながら、自分たちは\x01",
            "遊撃士協会の者ではありません。\x02\x03",

            "#0000Fクロスベル警察、特務支援課に\x01",
            "所属している捜査官です──\x02",
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
            "#11Pふむ……\x01",
            "クロスベル警察の方じゃったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x8,
        "#11P間違えて済まんかったのう。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x8,
        (
            "#11Pなにせこの村に、街の警察が\x01",
            "来ることなど滅多になくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x8,
        (
            "#11Pあのアリオス殿を始め、\x01",
            "遊撃士なら何度も来てるんじゃが。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        "#5P#0006Fそ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x104,
        (
            "#6P#0306Fあのオッサン……\x01",
            "売れっ子のくせにマメだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x102,
        (
            "#0103F#6Pそれで、トルタ村長……\x02\x03",

            "#0101F私たちが捜査に来た経緯は\x01",
            "先ほど話した通りです。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        (
            "#5P#0001Fお手数ですが、\x01",
            "もう一度、被害状況などを\x01",
            "聞かせていただけませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x8,
        "#11Pふむ、そうじゃな……\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "#11P──あれは３週間前、\x01",
            "ちょうど新月の晩のことじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x8,
        (
            "#11Pこの村に魔獣の群れが忍び込み、\x01",
            "農作物などを荒らしていったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x8,
        (
            "#11Pどの家も、家畜や果物、\x01",
            "小麦などが荒らされてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#5P#0001F確か……\x01",
            "目撃者は居なかったんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x8,
        (
            "#11Pうむ、クロスベル市とは違って\x01",
            "この村の夜は早いからのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x8,
        (
            "#11P朝早くの農作業もあるし、\x01",
            "ほとんどの村人は夢の中じゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x8,
        (
            "#11Pそして朝起きてみれば\x01",
            "魔獣どもの足跡と一緒に\x01",
            "被害が明らかになったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        "#5P#0003Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x103,
        (
            "#12P#0200Fそれで狼型の魔獣だと\x01",
            "判明したわけですね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "#11Pうむ……残された足跡の形状が\x01",
            "イヌ科のものじゃったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x8,
        (
            "#11P丁度、その日に警備隊の\x01",
            "巡回パトロールが訪れてのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x8,
        (
            "#11P念のため、周辺地域を\x01",
            "捜索してくれたんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        (
            "#0103F#6P狼型魔獣の痕跡は\x01",
            "影も形もなかった……\x02\x03",

            "#0101Fなるほど、\x01",
            "警備隊の調書通りですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        "#11Pうむ、その通りじゃ。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x8,
        (
            "#11Pそれから３週間……\x01",
            "再び被害が起きることはなく、\x01",
            "今日までに至っておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x8,
        (
            "#11P正直、二度は起こらんと\x01",
            "高を括#2Rくく#っていたのじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x8,
        (
            "#11Pううむ、まさか他の場所で\x01",
            "被害が起きていたとはのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        "#5P#0003Fはい……\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x104,
        (
            "#6P#0300Fしかし……\x01",
            "魔獣に襲われたにしちゃあ、\x01",
            "村は平穏そのものって感じだよな。\x02\x03",

            "被害額も結構なモンだったんじゃ？\x02",
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
            "#11Pいや、それが\x01",
            "それ程でもなかったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        (
            "#11Pどの家も少しずつ、\x01",
            "何らかの被害を受けただけでの。\x02",
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
        "#5P#0005F……そうなんですか？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(200)

    #C0331
    ChrTalk(
        0x8,
        (
            "#11Pうむ、被害の総額にして\x01",
            "１０万ミラといったところか。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        (
            "#11Pまあそれでも、\x01",
            "被害は被害じゃからの。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x8,
        (
            "#11Pさすがに気落ちしておったが\x01",
            "丁度、良い取引が出来てなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        (
            "#11P皆、受けた被害を\x01",
            "だいたい帳消しにできたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        "#5P#0005F良い取引……\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x103,
        (
            "#12P#0205Fもしかして……\x01",
            "先ほどのお客さんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x8,
        (
            "#11Pうむ、彼はここ数年、\x01",
            "ワシらと懇意#4Rこんい#にしてくれている\x01",
            "クロスベル市の貿易商でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#11P被害の話を聞いて、取引額を\x01",
            "少し上乗せしてくれたんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x8,
        (
            "#11Pいやはや。\x01",
            "何ともありがたい話じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x102,
        "#0100F#6Pそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x104,
        (
            "#6P#0300F貿易商か。\x01",
            "道理で仕立ての良さそうな\x01",
            "格好をしていたわけだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x8,
        "#11Pまあ、それに……\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x8,
        (
            "#11P……今のクロスベルの状況を考えれば\x01",
            "この程度の被害はむしろ軽いかもしれん。\x02",
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
        "#5P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x102,
        "#0101F#6Pあの、それは一体……\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x8,
        (
            "#11Pおっと……\x01",
            "これは余計な事を言ったかの。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        "#11Pスマンスマン、忘れてくれ。\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        (
            "#6P#0306Fおいおい、村長さん。\x02\x03",

            "#0301Fそんな言い方をされたら\x01",
            "余計に気になるっての。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x103,
        (
            "#0203F#12P……そうですね。\x01",
            "思わせぶりすぎるかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x8,
        "#11Pハハハ、それもそうか。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x8,
        (
            "#11P年寄りの世迷言かもしれんが\x01",
            "それでも構わんかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x101,
        (
            "#5P#0003Fいや……\x01",
            "どうか聞かせてください。\x02\x03",

            "#0001Fどこにどんな手がかりが\x01",
            "あるか分からない状況ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x8,
        "#11Pふむ……それならば。\x02",
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
            "#11P──お前さんたち\x01",
            "『神狼』という言葉を\x01",
            "聞いたことはあるかね？\x02",
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
        "#0105F#6P神の狼、ですか？\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        (
            "#0200F#12P……データベースでも\x01",
            "見かけた事のない言葉ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        "#11Pふむ、やはりか……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x8,
        (
            "#11Pそうなると、街でこの話は\x01",
            "もう伝わっておらんのじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x8,
        "#11P何とも寂しい限りじゃのう。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x101,
        (
            "#5P#0001Fえっと……\x01",
            "その『神狼』というのは一体？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#11Pその昔、このクロスベルの地に\x01",
            "棲んでいたという獣たちじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x8,
        (
            "#11P白い毛並みを持つ\x01",
            "狼の姿をしておったという。\x02",
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
        "#5P#0005Fそれって……！？\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x103,
        (
            "#0205F#12P今回の被害を\x01",
            "起こしたのと同じ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x8,
        (
            "#11P確証はない──が、\x01",
            "そうであっても不思議はない。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        (
            "#11P古い伝承によれば、\x01",
            "神狼たちはただの魔獣ではなく\x01",
            "女神が遣わした聖獣じゃったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x8,
        (
            "#11P古より、血で血を洗うような戦に\x01",
            "巻き込まれてきたクロスベルの地……\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x8,
        (
            "#11Pそこで人の愚かさを見守りながら\x01",
            "時に気まぐれに無力な人を助ける……\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x8,
        "#11Pそんな存在だったらしい。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        "#0101F#6Pそんな伝承が……\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#5P#0008Fそういえば……\x01",
            "白い狼が出てくる童話を\x01",
            "昔読んだことがあるような。\x02\x03",

            "#0003Fたしか街の図書館に\x01",
            "置いてあった気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        (
            "#11Pふむ、おそらくその童話は\x01",
            "伝承を下敷きにしとるのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x8,
        (
            "#11P──しかし、この数十年で\x01",
            "クロスベルは変わってしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        (
            "#11P帝国、共和国双方の影響下で\x01",
            "貿易都市として発展するうちに\x01",
            "過去の記憶は忘れ去られていった。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x8,
        (
            "#11Pそしていつしか……\x01",
            "『神狼』たちは姿を消したという。\x02",
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
            "#6P#0306Fふむ……さしずめ人間に\x01",
            "愛想を尽かしたってところかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        (
            "#11Pうむ……\x01",
            "わしはそう考えておるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        (
            "#11Pただまあ、そんな時代の狭間で\x01",
            "姿を消した『神狼』たちのことじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "#11Pもし戻ってきたのだとすれば……\x01",
            "何かの警鐘を鳴らしに\x01",
            "現れたのかもしれんと思ってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#5P#0001F警鐘……ですか。\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x8,
        (
            "#11Pこう言っては何だが……\x01",
            "今のクロスベル市の発展は\x01",
            "あまりに急すぎる気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x8,
        (
            "#11Pたまにバスで街に出ると\x01",
            "変わりように愕然#4Rがくぜん#とするくらいじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x8,
        (
            "#11P誰もが現在#4Rい  ま#だけに追いたてられ、\x01",
            "過去を振り返る余裕がないような……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x8,
        "#11Pそんな風にも見えてしまうんじゃ。\x02",
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
        "#0106F#6P……返す言葉もありません。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x8,
        (
            "#11Pおっと、いやいや。\x01",
            "説教するつもりではないんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x8,
        (
            "#11Pただまあ、そう考えると\x01",
            "この村が襲われた被害というのも\x01",
            "彼らなりの警告……\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x8,
        (
            "#11Pそんな風にも捉えられるのでは\x01",
            "ないかと思ってな。\x02",
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
            "#11Pふむ、どうやら真面目に\x01",
            "受け取られてしまったようじゃの。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x8,
        (
            "#11Pまあ年寄りの世迷言じゃ。\x01",
            "本気に捉えん方がいいじゃろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x101,
        (
            "#5P#0004Fいえ……\x01",
            "色々と参考になりました。\x02\x03",

            "#0000F今回の魔獣被害について\x01",
            "別の視点が持てた気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x8,
        "#11Pふむ、それならいいが……\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x8,
        (
            "#11P捜査に来たと言っておったが\x01",
            "他に協力できることはあるかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        (
            "#5P#0000Fそうですね……\x02\x03",

            "一応、他の村の方々に\x01",
            "聞き込みをしても構いませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x8,
        (
            "#11Pああ、お前さんたちなら\x01",
            "特に問題ないじゃろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x8,
        (
            "#11Pちょうど昼時じゃ。\x01",
            "外に農作業に出ていた者も\x01",
            "帰ってきていると思うぞ。\x02",
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

    # Function_14_5683 end

    def Function_15_7CE0(): pass

    label("Function_15_7CE0")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D8D")
    SetChrPos(0x109, 41100, 0, -1200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_7DB8")

    label("loc_7D8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DB8")
    SetChrPos(0x10A, 41100, 0, -1200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_7DB8")

    OP_0D()

    #C0400
    ChrTalk(
        0x101,
        (
            "#12P#0000Fえっと……\x01",
            "ドナルドさんっていうのは\x01",
            "あなたですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xB,
        (
            "#5Pドナルドは確かにオラだな。\x01",
            "……何か用か？\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        (
            "#12P#0000Fクロスベル警察のものです。\x01",
            "実は、お話がありまして……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0403
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは延滞本の回収をしている\x01",
            "事情を話した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0404
    ChrTalk(
        0xB,
        (
            "#5P……はんはん、あの本を\x01",
            "取りに来たでか。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xB,
        (
            "#5Pうーん、だとすると、\x01",
            "謝らなきゃなんねぇだなぁ。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F9E")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_7F9E")

    Sleep(1000)

    #C0406
    ChrTalk(
        0x101,
        "#12P#0005F謝るって……まさか！？\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x104,
        (
            "#12P#0305F又又又又貸しってか？\x02\x03",

            "#0306Fつーか、いい加減\x01",
            "ワケわからねぇっつの！\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xB,
        "#5Pいンや、又貸しはしてねぇけど……\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xB,
        (
            "#5P農作業の合間に読んでたら\x01",
            "どっかに行っちまってなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xB,
        (
            "#5Pどうも、失くしちまった\x01",
            "みてぇでさぁ。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8135")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_8135")

    Sleep(1000)

    #C0411
    ChrTalk(
        0x102,
        "#11P#0105Fそ、そんな……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81A1")

    #C0412
    ChrTalk(
        0x109,
        (
            "#6P#0506F又貸しより悪い結果に\x01",
            "なってるような……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8206")

    label("loc_81A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8206")

    #C0413
    ChrTalk(
        0x10A,
        (
            "#6P#0601F………………………………\x01",
            "（これだから規則を守らない\x01",
            "  連中は………！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8206")


    #C0414
    ChrTalk(
        0x103,
        (
            "#12P#0200F何か心当たりは無いんですか？\x01",
            "最後に読んでいた場所とか。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xB,
        (
            "#5Pああ、あそこだ、ホレ。\x01",
            "村長の家の前の、\x01",
            "養蜂場に立ってる小屋。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xB,
        (
            "#5Pあの中で読んでたら\x01",
            "いつの間にか無くなっててよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xB,
        "#5Pいや、ほんにすまねぇな。\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x101,
        (
            "#12P#0006Fと、とにかく……\x02\x03",

            "#0000F本があるとしたら\x01",
            "その小屋しかなさそうだ。\x01",
            "一度調べに行ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_837E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_837E")

    SetChrPos(0x0, 40500, 0, 0, 270)
    SetChrSubChip(0xB, 0x0)
    OP_29(0x28, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_15_7CE0 end

    def Function_16_839C(): pass

    label("Function_16_839C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0419
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2DA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2DA, 1)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_849A")
    SetChrPos(0x109, 76640, 0, -2920, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_84C5")

    label("loc_849A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84C5")
    SetChrPos(0x10A, 76640, 0, -2920, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_84C5")

    OP_0D()

    #C0420
    ChrTalk(
        0x101,
        (
            "#5P#0000F……図書館のマークが入ってる。\x01",
            "アルフレッドさんが借りた\x01",
            "延滞本に間違いなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x102,
        (
            "#11P#0106Fはぁ、見つかってよかったわね。\x02\x03",

            "#0105Fそれにしても……\x01",
            "アルカンシェルの\x01",
            "ファンブックだなんて。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85D6")

    #C0422
    ChrTalk(
        0x109,
        "#6P#0500F確か、相当稀少な本だそうですよ。\x02",
    )

    CloseMessageWindow()

    label("loc_85D6")


    #C0423
    ChrTalk(
        0x104,
        (
            "#12P#0306Fどいつもこいつも\x01",
            "読みたがるのは\x01",
            "仕方のないことかもな。\x02\x03",

            "#0309Fつか、俺だって\x01",
            "借りパクしちまいそうだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_869E")

    #C0424
    ChrTalk(
        0x10A,
        "#6P#0601Fギロッ……\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x104,
        "#12P#0306Fいや、冗談、冗談っすよ。\x02",
    )

    CloseMessageWindow()

    label("loc_869E")


    #C0426
    ChrTalk(
        0x103,
        (
            "#6P#0206F……図書館に返却してからに\x01",
            "してください。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_86FB")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_86FB")

    SetChrPos(0x0, 76380, 0, -1420, 180)
    SetChrSubChip(0xB, 0x0)
    OP_29(0x28, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8739")
    OP_29(0x28, 0x1, 0x1F)

    label("loc_8739")

    OP_65(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_16_839C end

    SaveToFile()

Try(main)
