from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c134b.bin",                # FileName
        "c134b",                    # MapName
        "c134b",                    # Location
        0x001D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 29, 0, 1, 0, 3],
    )

    BuildStringList((
        "c134b",                  # 0
        "ディーター総裁",         # 1
        "マリアベル",             # 2
        "キーア",                 # 3
        "シズク",                 # 4
        "エリィ",                 # 5
        "ティオ",                 # 6
        "ランディ",               # 7
        "人形",                   # 8
        "人形",                   # 9
    ))

    AddCharChip((
        "chr/ch05602.itc",                   # 00
        "chr/ch05500.itc",                   # 01
        "apl/ch50512.itc",                   # 02
        "apl/ch50512.itc",                   # 03
        "chr/ch05502.itc",                   # 04
        "apl/ch50093.itc",                   # 05
        "chr/ch00102.itc",                   # 06
        "chr/ch00100.itc",                   # 07
        "chr/ch00200.itc",                   # 08
        "chr/ch00300.itc",                   # 09
    ))

    DeclNpc(55000,   150,     128800,  180,  261,  0x0, 0,   0,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(57799,   29,      126400,  225,  261,  0x0, 0,   1,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(171500,  200,     123500,  270,  343,  0x0, 1,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(171500,  200,     124400,  270,  343,  0x0, 0,   3,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(59090,   29,      121360,  0,    341,  0x0, 0,   6,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(59090,   0,       -1070,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(59090,   0,       -1070,   135,  389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(172360,  800,     120099,  0,    374,  0x0, 3,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(172360,  800,     120800,  0,    374,  0x0, 4,   5,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(55000,   150,     128800,  2500,    55000,   1800,    128800,  0x007E, 0,  8,  0x0000)
    DeclActor(170460,  0,       122680,  1500,    171500,  1200,    123000,  0x007E, 0,  6,  0x0000)
    DeclActor(170300,  0,       125140,  1500,    171500,  1200,    124000,  0x007E, 0,  4,  0x0000)
    DeclActor(172500,  0,       121000,  1200,    172500,  1500,    121000,  0x007C, 0,  21, 0x0000)
    DeclActor(172500,  0,       120000,  1200,    172500,  1500,    120250,  0x007C, 0,  21, 0x0000)

    ScpFunction((
        "Function_0_2C4",          # 00, 0
        "Function_1_37C",          # 01, 1
        "Function_2_480",          # 02, 2
        "Function_3_487",          # 03, 3
        "Function_4_4CA",          # 04, 4
        "Function_5_4CE",          # 05, 5
        "Function_6_5C3",          # 06, 6
        "Function_7_5C7",          # 07, 7
        "Function_8_636",          # 08, 8
        "Function_9_63A",          # 09, 9
        "Function_10_940",         # 0A, 10
        "Function_11_E40",         # 0B, 11
        "Function_12_15DA",        # 0C, 12
        "Function_13_3143",        # 0D, 13
        "Function_14_4EA4",        # 0E, 14
        "Function_15_6F5D",        # 0F, 15
        "Function_16_876B",        # 10, 16
        "Function_17_8BC1",        # 11, 17
        "Function_18_A2A1",        # 12, 18
        "Function_19_A2D4",        # 13, 19
        "Function_20_A311",        # 14, 20
        "Function_21_A365",        # 15, 21
    ))


    def Function_0_2C4(): pass

    label("Function_0_2C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_304"),
        (1, "loc_310"),
        (2, "loc_31C"),
        (3, "loc_328"),
        (4, "loc_334"),
        (5, "loc_340"),
        (6, "loc_34C"),
        (SWITCH_DEFAULT, "loc_358"),
    )


    label("loc_304")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_310")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_31C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_328")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_334")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_340")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_34C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_358")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_364")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_37B")

    Return()

    # Function_0_2C4 end

    def Function_1_37C(): pass

    label("Function_1_37C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_394")
    ClearScenarioFlags(0x5F, 1)
    Event(0, 2)

    label("loc_394")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AE")
    Event(0, 17)

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_3BD")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 15)

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 4)), scpexpr(EXPR_END)), "loc_3CB")
    Jump("loc_47F")

    label("loc_3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_47F")
    ClearChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x4)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 59090, 30, 124780, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_448")
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, 59090, 0, -1070, 135)
    Jump("loc_47F")

    label("loc_448")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_466")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_47F")

    label("loc_466")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47F")
    ClearChrFlags(0xE, 0x80)

    label("loc_47F")

    Return()

    # Function_1_37C end

    def Function_2_480(): pass

    label("Function_2_480")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_480 end

    def Function_3_487(): pass

    label("Function_3_487")

    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_487 end

    def Function_4_4CA(): pass

    label("Function_4_4CA")

    Call(0, 5)
    Return()

    # Function_4_4CA end

    def Function_5_4CE(): pass

    label("Function_5_4CE")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56C")

    #C0001
    ChrTalk(
        0xB,
        "#1503F#40Wスー……スー……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#0006F（２人とも\x01",
            "  怪我一つ無くてよかった……）\x02\x03",

            "#0000F（………守れてよかったよ………）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5BF")

    label("loc_56C")


    #C0003
    ChrTalk(
        0xB,
        "#1503F#40Wスー……スー……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "シズクは静かな寝息を立てている。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xA)

    label("loc_5BF")

    TalkEnd(0xB)
    Return()

    # Function_5_4CE end

    def Function_6_5C3(): pass

    label("Function_6_5C3")

    Call(0, 7)
    Return()

    # Function_6_5C3 end

    def Function_7_5C7(): pass

    label("Function_7_5C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DD")
    Call(0, 16)
    Jump("loc_635")

    label("loc_5DD")

    TalkBegin(0xA)

    #C0005
    ChrTalk(
        0xA,
        "#1113F#40W……すーすー………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キーアは静かな寝息を立てている。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xA)

    label("loc_635")

    Return()

    # Function_7_5C7 end

    def Function_8_636(): pass

    label("Function_8_636")

    Call(0, 9)
    Return()

    # Function_8_636 end

    def Function_9_63A(): pass

    label("Function_9_63A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CE")
    Jump("loc_718")

    label("loc_6CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6EE")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_718")

    label("loc_6EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70E")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_718")

    label("loc_70E")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_718")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_756")
    SetScenarioFlags(0xEE, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7EA")

    #C0007
    ChrTalk(
        0x8,
        (
            "#2800F１階のカウンターに声を掛ければ\x01",
            "各種のサービスが受けられるだろう。\x02\x03",

            "ロイド君、有事に備えて\x01",
            "体を休めることも忘れぬようにな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_938")

    label("loc_7EA")


    #C0008
    ChrTalk(
        0x8,
        (
            "#2803FＩＢＣの保安部は優秀だ。\x01",
            "警備は任せておいて構わないだろう。\x02\x03",

            "#2800Fロイド君、補給をしたいなら\x01",
            "１階のカウンターに声を掛けたまえ。\x02\x03",

            "#2804Fそれと……有事に備えて\x01",
            "体を休めることも忘れぬように。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#0002Fはい、何から何まで\x01",
            "ありがとうございます。\x02\x03",

            "#0003F（とりあえず補給だけはしておこう。\x01",
            "  ……この先何があるか判らない。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_938")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_9_63A end

    def Function_10_940(): pass

    label("Function_10_940")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D4")
    Jump("loc_A1E")

    label("loc_9D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9F4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1E")

    label("loc_9F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A14")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1E")

    label("loc_A14")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5C")
    SetScenarioFlags(0xEF, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABD")

    #C0010
    ChrTalk(
        0x9,
        "#2901Fジロッ……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#0005F？？？\x01",
            "（どうしたんだろう……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B54")

    label("loc_ABD")


    #C0012
    ChrTalk(
        0x9,
        (
            "#2903Fまったく油断も隙もない……\x02\x03",

            "#2901F……事が片付いたら策を練って\x01",
            "何としても邪魔しておきませんと。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#0006F（なんか不穏な事を言ってる……）\x02",
    )

    CloseMessageWindow()

    label("loc_B54")

    Jump("loc_E38")

    label("loc_B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BFC")

    #C0014
    ChrTalk(
        0x9,
        (
            "#2904F通信網の復旧については\x01",
            "技術部に指示を出してあります。\x01",
            "じきに何とかなるでしょう。\x02\x03",

            "#2900F……ともかく今は\x01",
            "事態の把握に努めることですわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E38")

    label("loc_BFC")


    #C0015
    ChrTalk(
        0x9,
        (
            "#2903Fこの状況を打開するプランを\x01",
            "いくつか考えてみましたけれど……\x02\x03",

            "#2901Fいかんせん、手数が足りませんわね。\x02\x03",

            "何より、相手の正体も目的も\x01",
            "よく分かっていないのでは\x01",
            "こちらも動きようがありませんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0008Fまずは事態の把握に努めること。\x02\x03",

            "#0006Fその上で相手の出方を読み\x01",
            "考えうる最も有効な行動を取る……\x01",
            "くらいでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "#2905F……妙な所で気が合いますわね。\x02\x03",

            "#2904Fまあいいですわ。\x01",
            "通信網の復旧については\x01",
            "技術部に指示を出してあります。\x02\x03",

            "#2902Fティオさんも協力してくださる\x01",
            "そうですから、例の端末室に\x01",
            "行ってみてはいかがかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#0000Fええ、そうしてみます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_E38")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_940 end

    def Function_11_E40(): pass

    label("Function_11_E40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E58")
    Call(0, 12)
    Return()

    label("loc_E58")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EEC")
    Jump("loc_F36")

    label("loc_EEC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F0C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F36")

    label("loc_F0C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F2C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F36")

    label("loc_F2C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F36")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1479")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_END)), "loc_1284")

    #C0019
    ChrTalk(
        0xC,
        (
            "#0112Fあ、ロイド……\x02\x03",

            "#0113Fえ、えっと、貴方も少しは\x01",
            "休んだ方がいいんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0012Fあ、ああ……\x01",
            "少し回ったらそうするよ。\x02\x03",

            "#0002Fエリィも、走り回ったんだから\x01",
            "せめて身体を休めておいてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xC,
        "#0102Fええ、ありがとう。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0022
    ChrTalk(
        0x9,
        "#2901F……怪しいですわね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    SetChrSubChip(0xC, 0x0)
    TurnDirection(0x101, 0x9, 500)

    #C0023
    ChrTalk(
        0x101,
        "#0011Fええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xC,
        (
            "#0112Fも、もうベルったら……！\x01",
            "いきなり何を言い出すの！？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_64(0xC)

    #C0025
    ChrTalk(
        0x9,
        (
            "#2903Fだって、さっきもエリィが\x01",
            "赤い顔をして戻って来ましたし。\x02\x03",

            "#2901Fまさか……\x01",
            "このシリアスな状況に付け込んで\x01",
            "不埒#4Rふらち#な事はしてませんわよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#0012Fめ、滅相もない……！\x01",
            "（しそうになったけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xC,
        "#0113F…………………………（カアッ）\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        "#2910F……………………（ギリリッ）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1465")

    label("loc_1284")


    #C0029
    ChrTalk(
        0xC,
        (
            "#0108Fロイド……\x01",
            "大変な事になっちゃったわね。\x02\x03",

            "#0101F『教団』の……\x01",
            "ヨアヒム先生の目的は何なのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#0008F判らない……\x02\x03",

            "#0006Fけど、ここの人たちも\x01",
            "結局巻き込んでしまったな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0031
    ChrTalk(
        0xC,
        (
            "#0102Fふふっ……\x01",
            "あなたは相変わらずね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#0005F……………………？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xC,
        (
            "#0104F大丈夫よ。\x01",
            "おじさまもベルも、\x01",
            "みんな強い人たちだから。\x02\x03",

            "#0100Fそれより今は\x01",
            "キーアちゃんとシズクちゃんを\x01",
            "守る事を考えましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#0000Fああ、そうだな。\x01",
            "一回り見てくることにするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1465")

    SetScenarioFlags(0xE4, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15D2")

    label("loc_1479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_END)), "loc_1545")

    #C0035
    ChrTalk(
        0xC,
        (
            "#0109Fえ、えっと……\x01",
            "補給と装備の方はよろしくね。\x02\x03",

            "#0102F私はベルたちと一緒に\x01",
            "今後の対応を話しておくから……\x02\x03",

            "お互い、倒れない程度に\x01",
            "頑張りましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1540")

    #C0036
    ChrTalk(
        0x101,
        "#0000Fああ……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1540")

    Jump("loc_15D2")

    label("loc_1545")


    #C0037
    ChrTalk(
        0xC,
        (
            "#0103Fベルと色々話してみたけれど\x01",
            "今の所、打つ手無しね。\x02\x03",

            "#0108F夜が明ければ……\x01",
            "あるいはどこかと連絡が取れれば\x01",
            "希望はあるはずだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_E40 end

    def Function_12_15DA(): pass

    label("Function_12_15DA")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0xC, 0xFF)
    LoadChrToIndex("apl/ch50541.itc", 0x1E)
    OP_68(58810, 1400, -420, 0)
    MoveCamera(125, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16550, 0)
    SetChrPos(0x101, 59090, 0, 360, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00101.itp")
    SetCameraDistance(15550, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0038
    ChrTalk(
        0xC,
        "#0108F#5P#40W………………………………\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0000F#5Pエリィ……\x01",
            "ここにいたのか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x0, 0x190)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    #Sound(1178, 255, 90, 0)    #voice#Elie
    Sleep(150)

    #A0040
    AnonymousTalk(
        0xC,
        "#40Wロイド……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0041
    ChrTalk(
        0x101,
        (
            "#0006F#5P……改めて言うのも何だけど\x01",
            "大変な事になったよな。\x02\x03",

            "#0001F市内にいる人たち……\x01",
            "無事でいるといいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "#0106F#11P#30Wそうね……\x02\x03",

            "#0108F#40W………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0043
    ChrTalk(
        0x101,
        (
            "#0004F#5P……エリィ。\x01",
            "マクダエル市長なら大丈夫だ。\x02\x03",

            "#0000F警備隊を操る黒幕にも\x01",
            "市長を害するメリットはないさ。\x02\x03",

            "何とかこの事態を打破して\x01",
            "市長たちを解放しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xC,
        (
            "#0102F#11Pロイド……\x01",
            "うん、ありがとう。\x02\x03",

            "#0104Fそうよね、おじいさまは\x01",
            "何度も紛争を経験されている……\x02\x03",

            "この程度の危機くらい\x01",
            "何とか切り抜けられるはずよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#0002F#5Pああ……\x01",
            "あの人なら絶対に大丈夫さ！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xC,
        (
            "#0102F#11P……ふふっ………\x02\x03",

            "#0106Fあーあ、何で貴方はそんな風に\x01",
            "私のことが判っちゃうのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#0005F#5Pえ。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        (
            "#0113F#11P……考えてみれば不公平よね。\x02\x03",

            "私はもう……色々なものを\x01",
            "貴方に曝#2Rさら#け出してしまった。\x02\x03",

            "#0111Fなのに貴方の方は……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#0011F#5Pえ、えっとエリィ……？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    #C0050
    ChrTalk(
        0xC,
        (
            "#0103F#11P──ねえ、ロイド。\x02\x03",

            "#0100Fお兄さんの背中、\x01",
            "少しは近づいてきた？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0051
    ChrTalk(
        0x101,
        "#0005F#5Pあ……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xC,
        (
            "#0104F#11Pたぶん貴方は……\x01",
            "お兄さんの背中をずっと\x01",
            "追い続けて来たのよね。\x02\x03",

            "貴方が良く言っている\x01",
            "《壁》という言葉……\x02\x03",

            "#0100Fあれはひょっとして\x01",
            "お兄さん自身の事を指しても\x01",
            "いるんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0053
    ChrTalk(
        0x101,
        (
            "#0004F#5P……ああ。\x01",
            "多分そうだと思う。\x02\x03",

            "#0008F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_68(57610, 1500, 240, 2800)
    MoveCamera(105, 24, 0, 2800)
    OP_6E(500, 2800)
    SetCameraDistance(13000, 2800)
    OP_93(0x101, 0x10E, 0x1F4)

    def lambda_1CCC():
        OP_96(0x101, 0xE10A, 0x0, 0xF0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CCC)
    Sleep(1000)

    def lambda_1CE9():
        OP_93(0xC, 0x122, 0x12C)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1CE9)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xC, 2)
    OP_6F(0x79)
    Fade(200)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1B)
    OP_0D()
    Sleep(500)

    #C0054
    ChrTalk(
        0x101,
        (
            "#0004F#5P──昔からさ、\x01",
            "兄貴は俺のヒーローだったんだ。\x02\x03",

            "どんな逆境にもめげずに、\x01",
            "何でもやり遂げる凄いヤツ。\x02\x03",

            "#0008Fだけど３年前……\x01",
            "いきなりその背中が無くなって\x01",
            "途方にくれてしまって……\x02\x03",

            "多分、俺は逃げたんだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xC,
        "#0105F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#0006F#5Pだって俺は……\x01",
            "兄貴みたいになれる自信が\x01",
            "無かったから。\x02\x03",

            "兄貴みたいに色んなものを\x01",
            "守れる自信が無かったから……\x02\x03",

            "#0008Fだから……\x01",
            "知らない町へ逃げ出したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xC,
        (
            "#0103F#11P……でも、貴方は\x01",
            "クロスベルに戻ってきた。\x02\x03",

            "#0100Fそれは、どうして？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#0004F#5Pはは、やっぱり……\x01",
            "この街が好きだったからかな。\x02\x03",

            "兄貴や、セシル姉。\x01",
            "一緒に過ごした友人たち……\x02\x03",

            "他の町で暮らしていても\x01",
            "やっぱりそれは俺の一部で、\x01",
            "忘れることは出来なかったから……\x02\x03",

            "#0000Fだから俺は無理して\x01",
            "警察学校のうちに捜査官資格を　\x01",
            "取ったんだと思う。\x02\x03",

            "#0008F少しでも兄貴に追いつけないと……\x02\x03",

            "#0003F兄貴の代わりになれないと\x01",
            "クロスベルに戻ってくる資格は\x01",
            "ないと思ったから……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xC,
        (
            "#0105F#11Pで、でもそれで本当に\x01",
            "捜査官資格を取るんだもの。\x02\x03",

            "#0102Fお兄さんに負けないくらい\x01",
            "素質はあったのでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0006F#5Pいや……白状すると\x01",
            "それもズルしたようなものさ。\x02\x03",

            "#0002Fなにせ規格外ではあるけど\x01",
            "捜査官としては一流の人間を\x01",
            "ずっと見てきたから……\x02\x03",

            "#0004F兄貴だったらどうするだろう、\x01",
            "兄貴だったら絶対に諦めない……\x02\x03",

            "そう自分に言い聞かせて\x01",
            "俺は何とかやって来れたと思う。\x02\x03",

            "#0008Fでも……\x01",
            "それは俺が、俺自身として\x01",
            "強くなれたわけじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xC,
        "#0101F#11P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#0000F#5P……最近になって\x01",
            "やっと気付けた気がするんだ。\x02\x03",

            "兄貴の背中を追い続けるだけじゃ\x01",
            "本当の意味で強くはなれないってね。\x02\x03",

            "#0012Fはは、それに気付けるのに\x01",
            "どれだけ掛かってるんだよって\x01",
            "話なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        "#0103F#11P……ロイド。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    SetChrFlags(0xC, 0x40)
    OP_95(0xC, 57880, 0, -270, 800, 0x0)
    Fade(500)
    SetChrFlags(0xC, 0x8)
    SetChrPos(0xC, 57970, 0, -180, 300)
    SetChrSubChip(0x101, 0x0)
    MoveCamera(75, 27, 0, 0)
    SetCameraDistance(14500, 0)
    OP_68(57640, 1500, 140, 0)
    OP_0D()
    Sound(804, 0, 70, 0)
    Sound(910, 0, 80, 0)
    OP_A1(0x101, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0064
    ChrTalk(
        0x101,
        "#0011F#5Pエ、エリィ……？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    SetCameraDistance(13500, 60000)
    OP_A1(0x101, 0x3E8, 0x3, 0x18, 0x19, 0x1A)

    #C0065
    ChrTalk(
        0xC,
        (
            "#0100F#11P……ねえ、ロイド。\x02\x03",

            "私はガイさんを……\x01",
            "貴方のお兄さんを知らない。\x02\x03",

            "#0104Fでも、一つ言える事があるわ。\x02\x03",

            "今まで私たちを\x01",
            "引っ張っていってくれたのは\x01",
            "他ならぬ貴方自身だってこと。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#0005F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xC,
        (
            "#0102F#11Pいつだって貴方は……\x01",
            "私を──私たちを導いてくれた。\x02\x03",

            "この灰色の街で迷うだけだった\x01",
            "私や、ティオちゃんや、\x01",
            "多分ランディも……\x02\x03",

            "#0104F……優しくて、ひたむきで\x01",
            "肝心なところではニブいけど……\x02\x03",

            "でもやっぱり、\x01",
            "大切な時には側にいてくれて\x01",
            "一緒に答えを探してくれる……\x02\x03",

            "#0102Fそんな貴方がいてくれたから\x01",
            "私たちはここまで辿り着けた。\x02\x03",

            "ガイさんでも、他の誰でもなく\x01",
            "貴方だから出来たことよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0005F#5P……あ………\x02",
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x3E8, 0x3, 0x1A, 0x19, 0x18)
    Sleep(300)

    #C0069
    ChrTalk(
        0xC,
        (
            "#0104F#11Pだから私は……\x01",
            "この街で貴方に出会えた幸運を\x01",
            "空の女神に感謝しているわ。\x02\x03",

            "ふふっ、幼い頃に日曜学校で\x01",
            "出会っていればもっと良かった……\x02\x03",

            "#0102Fそんな益体#4Rやくたい#もないことを\x01",
            "考えてしまうくらいに。\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x384, 0x2, 0x4, 0x5)

    #C0070
    ChrTalk(
        0x101,
        "#0004F#5Pエリィ……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "#0104F#11P自信を持って。\x01",
            "ロイド・バニングス。\x02\x03",

            "お兄さんに憧れている所も\x01",
            "自分自身であろうと足掻く所も\x01",
            "すべてが貴方だから……\x02\x03",

            "そんな貴方が私たちは……\x01",
            "ううん──私は好きだから。\x02\x03",

            "#0102Fだから……\x01",
            "貴方は貴方であるだけでいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#0004F#5P……エリィ………\x02\x03",

            "#0002F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x514, 0x4, 0x6, 0x7, 0x8, 0x9)
    Sleep(500)

    #C0073
    ChrTalk(
        0xC,
        "#0112F#11P………ぁ……………\x02",
    )

    CloseMessageWindow()
    Sound(820, 0, 100, 0)
    OP_A1(0x101, 0x4B0, 0x6, 0xA, 0xB, 0xC, 0x15, 0x16, 0x17)
    Sleep(500)
    Sound(801, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    VolumeBGM(0x3C, 0x5DC)
    SetChrSubChip(0x101, 0x1E)
    Sleep(8)
    SetChrSubChip(0x101, 0x1F)
    OP_63(0x101, 0xFFFFFFB0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0xFFFFFF9C, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性の声")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──ビル内に残っている\x01",
            "皆様にお知らせいたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "非常時につき、\x01",
            "これより一部フロアの照明を\x01",
            "落とさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "また、保安上の理由から\x01",
            "エントランス以外の非常口は\x01",
            "全て閉鎖させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どうかご理解の上、火元などには\x01",
            "くれぐれもお気をつけ下さるよう\x01",
            "お願い申し上げます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0xBB8)
    OP_63(0x101, 0xFFFFFFB0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0xFFFFFF9C, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xC)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0xC, 0x8)
    TurnDirection(0x101, 0xC, 0)
    OP_0D()
    Sleep(500)

    #C0078
    ChrTalk(
        0x101,
        "#0012F#5Pはは……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xC,
        (
            "#0109F#11Pふふっ……\x02\x03",

            "#0112F……え、えっと……\x01",
            "私、ベルの所に戻るわね。\x02\x03",

            "#0113F何かおじさまたちに\x01",
            "協力できることがあるかも\x01",
            "しれないから……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#0004F#5Pあ、ああ……\x01",
            "俺も今のうちに補給と\x01",
            "装備の確認をしてくるよ。\x02\x03",

            "#0002F……また、後でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        (
            "#0102F#11Pええ……\x02\x03",

            "#0113F……その、さっきの続きは、\x01",
            "ぜんぶ解決した後にでも……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#0005F#5Pえ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_2C97():

        label("loc_2C97")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2C97")

    QueueWorkItem2(0x101, 2, lambda_2C97)
    OP_96(0xC, 0xE394, 0x0, 0xFFFFFD3A, 0x3E8, 0x0)

    #C0083
    ChrTalk(
        0xC,
        (
            "#0112F#11Pな、なんでもないっ。\x02\x03",

            "#0109Fそ、それじゃあまた後でね！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x12C)
    OP_95(0xC, 58570, 0, 1430, 2000, 0x0)
    OP_95(0xC, 57880, 0, 4330, 2000, 0x0)
    ClearChrFlags(0xC, 0x40)

    def lambda_2D37():
        OP_95(0xFE, 53120, 0, 17620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2D37)
    EndChrThread(0x101, 0x2)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xC)
    Fade(500)
    MoveCamera(105, 24, 0, 0)
    SetCameraDistance(14000, 0)
    OP_93(0x101, 0x14A, 0x0)
    OP_0D()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1B)
    OP_0D()
    Sleep(300)

    #C0084
    ChrTalk(
        0x101,
        (
            "#0002F#5P（……エリィ、\x01",
            "  柔らかかったな……）\x02\x03",

            "#0002F（それに良い匂いがして……）\x02\x03",

            "#0006F（はあ……\x01",
            "  あともう少しで──）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0085
    ChrTalk(
        0x101,
        "#0011F#5P──じゃなくて！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x3E8, 0x2, 0x1C, 0x1D)
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0086
    ChrTalk(
        0x101,
        (
            "#0004F#5P（……俺は俺自身で\x01",
            "  あるだけでいいか……）\x02\x03",

            "（少し前なら、そんな風に言われても\x01",
            "  逆に迷った気がするけど……）\x02\x03",

            "#0000F（でも今は……\x01",
            "  不思議と納得できる気がする。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x4B0, 0x2, 0x1C, 0x1B)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_49()
    OP_D5(0x1E)
    OP_0D()
    Sleep(300)
    OP_93(0x101, 0x13B, 0x12C)

    #C0087
    ChrTalk(
        0x101,
        "#0002F#11P──ありがとう、エリィ。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30BB")
    StopBGM(0xFA0)
    WaitBGM()
    Sound(517, 0, 100, 0)
    AddCraft(0x0, 0x154)
    AddCraft(0x1, 0x154)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ロイドとエリィは\x01",
            "スターブラストⅡを習得した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとエリィのコンビクラフト、\x01",
            "《スターブラスト》が強化されました。\x02",
        )
    )

    CloseMessageWindow()

    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "攻撃力や射程・範囲の他、\x01",
            "硬直時間などの性能がアップします。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7513", 0)

    label("loc_30BB")

    OP_CA(0x1, 0xFF, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xC, 0x1)
    OP_4C(0xC, 0xFF)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x40)
    SetChrChipByIndex(0xC, 0x6)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 59090, 30, 121360, 0)
    OP_68(57610, 1500, 240, 0)
    MoveCamera(88, 16, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 57610, 0, 240, 315)
    SetScenarioFlags(0xE7, 2)
    OP_DE(0x2D, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_12_15DA end

    def Function_13_3143(): pass

    label("Function_13_3143")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0xD, 0xFF)
    LoadChrToIndex("apl/ch50543.itc", 0x1E)
    OP_68(58810, 1400, -420, 0)
    MoveCamera(125, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16550, 0)
    SetChrPos(0x101, 59090, 0, 360, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00200.itp")
    SetCameraDistance(15550, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0091
    ChrTalk(
        0xD,
        "#0208F#5P#30W………………………………\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        "#0005F#5Pティオ……？\x02",
    )

    CloseMessageWindow()
    Sound(1269, 255, 90, 0)    #voice#Tio
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(1267, 255, 90, 0)    #voice#Tio
    OP_93(0xD, 0x0, 0x190)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0093
    AnonymousTalk(
        0xD,
        "……ロイドさん。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, -1, -1)

    #A0094
    AnonymousTalk(
        0x101,
        (
            "#0005Fどうしたんだ──って、そうか。\x02\x03",

            "#0000F外の様子を\x01",
            "伺っててくれたんだな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0095
    ChrTalk(
        0xD,
        (
            "#0203F#11P……ええ、まあ。\x01",
            "やっぱり気になりますし。\x02\x03",

            "#0205Fでも、よく判りましたね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#0000F#5Pそりゃ、ティオの力には\x01",
            "いつも助けられてるからな。\x02\x03",

            "#0001Fそれで……\x01",
            "市内の方はどんな様子なんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xD,
        (
            "#0206F#11P……散発的に銃撃戦が\x01",
            "起きているようですね。\x02\x03",

            "#0208F多分、警官隊あたりと\x01",
            "警備隊が衝突しているのでは\x01",
            "ないかと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#0008F#5Pそうか……\x02\x03",

            "#0003F……せめて市民に被害が\x01",
            "及んでいないといいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xD,
        "#0208F#11P……………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x101,
        (
            "#0005F#5P……？\x01",
            "ひょっとしてティオ、\x01",
            "疲れてるんじゃないのか？\x02\x03",

            "#0001F街中を走り回ったばかりだし、\x01",
            "キーアたちと一緒に休んだ方が……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xD,
        "#0211F#11P……ジロッ。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#0011F#5Pい、いや別に\x01",
            "子供扱いしてるわけじゃ！\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xD,
        (
            "#0202F#11Pふふ……判ってます。\x02\x03",

            "ずっとロイドさんたちと\x01",
            "一緒に行動していたおかげで\x01",
            "体力も付いてしまいましたし。\x02\x03",

            "#0204Fそれに、少し興奮気味みたいで\x01",
            "眠れそうにないですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#0002F#5Pそっか……\x02\x03",

            "#0006F……しかし本当に\x01",
            "とんでもない事になったな。\x02\x03",

            "#0001Fティオは本来、警察官じゃないのに\x01",
            "こんな状況に巻き込んじゃって……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    #C0105
    ChrTalk(
        0xD,
        "#0211F#11Pジロッ。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#0012F#5Pいや別に、関係ないとか\x01",
            "言ってるわけじゃなくって！\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xD,
        "#0206F#11P……まったく。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)

    #C0108
    ChrTalk(
        0xD,
        (
            "#0206F#11Pで、でも……\x01",
            "確かにこんな事態になったら\x01",
            "今後どうなるかは心配ですね。\x02\x03",

            "わたしの出向についても\x01",
            "財団がどう判断するか……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        "#0005F#5Pえ。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xD,
        (
            "#0208F#11P魔導杖のテストに関しては\x01",
            "クロスベル以外でも出来ますし。\x02\x03",

            "財団の方針しだいでは\x01",
            "わたしの出向も取りやめに\x01",
            "なることだって……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#0001F#5Pそ、そうか……\x02\x03",

            "#0003F………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xD,
        (
            "#0208F#11P……その………\x02\x03",

            "#0200Fそうなったら少しは\x01",
            "寂しく思ってくれますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#0006F#5Pう、うーん……\x02\x03",

            "それ以前に、ちょっと\x01",
            "想像しにくいものがあるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xD,
        "#0205F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#0012F#5Pいや、ティオがいない\x01",
            "支援課っていうのが\x01",
            "何だか想像できなくって……\x02\x03",

            "#0000Fあの端末だって\x01",
            "ティオの特等席みたいな\x01",
            "ものだったじゃないか。\x02\x03",

            "俺たちや、他の人間が座って\x01",
            "操作するのはピンと来なくてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xD,
        "#0205F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0008F#5Pでも、そうか……\x01",
            "出向が取りやめになることも\x01",
            "あり得るのか……\x02\x03",

            "#0006F……参ったな。\x01",
            "そんなこと考えもしなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xD,
        (
            "#0206F#11P──あくまで\x01",
            "可能性としてはです。\x02\x03",

            "#0202F財団は最先端の技術を\x01",
            "クロスベルに投入していますし\x01",
            "かなりの投資もしています。\x02\x03",

            "こんな大事件が起こったとしても\x01",
            "引き上げる可能性は低いと思います。\x02\x03",

            "#0204Fそうである限り、魔導杖のテストも\x01",
            "この地で行うのがベストですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#0002F#5Pそ、そっか……\x02\x03",

            "#0000F──うん、だったら\x01",
            "何としてもこの事態を打開して\x01",
            "事件を解決しないとな！\x02\x03",

            "#0009Fティオに支援課に\x01",
            "居続けてもらうためにも！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x50, 0x0, 0x7D0, 0xC8)

    #C0120
    ChrTalk(
        0xD,
        "#0205F#11P…………っ………………\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x1F4)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0121
    ChrTalk(
        0x101,
        (
            "#0011F#5Pって、また俺、\x01",
            "無神経なことを言ったか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xD,
        (
            "#0203F#5P……ええ。\x01",
            "正直、言語道断ですね。\x02\x03",

            "#0211Fやっぱりエリィさんの言う通り\x01",
            "ロイドさんは危険です……\x02\x03",

            "まさかそんな反応を\x01",
            "されるとは思いませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        "#0005F#5Pそんな反応……？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xD,
        (
            "#0208F#5Pっ……ロイドさんが\x01",
            "ダメダメで、にぶちんで、\x01",
            "ヘタレ弟キャラということです！\x02\x03",

            "#0201Fある意味、その点においては\x01",
            "ガイさんを越えていますね……！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#0006F#5Pいや、意味不明なんだけど……\x02\x03",

            "#0001F……うーん、でも兄貴か。\x02\x03",

            "確かにニブいっていうか\x01",
            "朴念仁なところはあったよな。\x02\x03",

            "#0008F長い間、セシル姉の気持ちに\x01",
            "気付いてなかったみたいだし……\x02\x03",

            "#0006F何度、蹴っ飛ばして\x01",
            "気付かせてやろうと思った事か。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xD)
    OP_93(0xD, 0x0, 0x1F4)
    Sleep(300)
    OP_68(58920, 1400, -10, 1200)
    OP_96(0xD, 0xE6F0, 0x0, 0xFFFFFE52, 0x320, 0x0)
    Sound(1197, 255, 85, 0)    #voice#Tio
    Sleep(500)
    Fade(150)
    Sound(819, 0, 100, 0)
    OP_82(0x50, 0x0, 0x7D0, 0xC8)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sound(1029, 255, 90, 1)    #voice#Lloyd

    def lambda_4079():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4079)
    Sleep(390)
    Fade(250)
    SetChrChipByIndex(0xD, 0x8)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0126
    ChrTalk(
        0x101,
        "#0012F#5Pって、ティオさん……？\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "#0203F#11P──失礼、何となく。\x02\x03",

            "#0211Fですが今のは正直、\x01",
            "自業自得なのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#0011F#5P？？？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(801, 0, 100, 0)
    Sleep(500)
    VolumeBGM(0x3C, 0x5DC)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性の声")

    #A0129
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──ビル内に残っている\x01",
            "皆様にお知らせいたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0130
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "非常時につき、\x01",
            "これより一部フロアの照明を\x01",
            "落とさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #A0131
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "また、保安上の理由から\x01",
            "エントランス以外の非常口は\x01",
            "全て閉鎖させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #A0132
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どうかご理解の上、火元などには\x01",
            "くれぐれもお気をつけ下さるよう\x01",
            "お願い申し上げます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0xBB8)

    #C0133
    ChrTalk(
        0x101,
        (
            "#0001F#5Pっと……いよいよ\x01",
            "本格的な篭城になってきたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xD,
        (
            "#0204F#11Pわたしは地下の端末室で\x01",
            "手伝いをしようと思います。\x02\x03",

            "ヨナあたりと連絡が取れれば\x01",
            "色々選択肢も出てきますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#0002F#5Pそっか……\x01",
            "よろしく頼んだよ。\x02\x03",

            "俺は補給や装備の確認を\x01",
            "してくるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xD,
        "#0202F#11Pよろしくお願いします。\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    StopBGM(0xFA0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    #C0137
    ChrTalk(
        0x101,
        (
            "#0011F#5P……ティオ？\x01",
            "（また怒らせちゃったか……？）\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    SetCameraDistance(14500, 60000)

    #C0138
    ChrTalk(
        0xD,
        (
            "#0208F#11P……以前、ロイドさんが\x01",
            "してくれるといった“約束”……\x02\x03",

            "#0201F覚えていますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0005F#5Pあ、ああ……\x02\x03",

            "#0000F兄貴との約束じゃなくて、\x01",
            "俺自身の言葉でってやつか。\x02\x03",

            "#0006Fゴメン、あれから\x01",
            "色々と考えてはいるんだけど\x01",
            "良いのが思いつかなくてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xD,
        (
            "#0203F#11Pでしたら……\x01",
            "わたしの方から希望があります。\x02\x03",

            "#0201Fそれでもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0005F#5Pあ、ああ……\x01",
            "もちろん構わないけど。\x02\x03",

            "#0000Fよし──どんと来い！\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xD,
        "#0202F#11P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x190)
    Sleep(300)
    OP_68(58720, 1400, -290, 1500)
    OP_96(0xD, 0xE6D2, 0x0, 0xFFFFFBD2, 0x320, 0x0)
    OP_6F(0x1)

    #C0143
    ChrTalk(
        0xD,
        (
            "#0204F#5P……ミシュラムのテーマパーク。\x02\x03",

            "この騒ぎが無事解決したら\x01",
            "あそこに連れて行ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        "#0005F#5Pへ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0145
    ChrTalk(
        0x101,
        (
            "#0011F#5Pええっ……\x01",
            "そんなのでいいのか！？\x02\x03",

            "#0001Fいや、でも……\x01",
            "もうちょっとこうシリアスな\x01",
            "約束の方がいいんじゃないか？\x02\x03",

            "ティオが困った時には\x01",
            "何があっても助けに行くとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xD,
        (
            "#0204F#5Pいえ、これで十分です。\x02\x03",

            "#0208Fそれに、この事態を解決しないと\x01",
            "この約束も果たされない……\x02\x03",

            "#0202Fその意味では十分、\x01",
            "シリアスなのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#0004F#5Pそうか……\x01",
            "……うん、確かにそうだな。\x02\x03",

            "#0002Fよし──約束だ。\x02\x03",

            "この事件が無事解決できたら\x01",
            "一緒にテーマパークに遊びに行こう。\x02\x03",

            "#0005Fあっと、他のみんなも\x01",
            "一緒の方がいいかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x320)
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    #C0148
    ChrTalk(
        0xD,
        "#0211F#11Pジロッ……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#0012F#5Pだ、だよな。\x01",
            "ティオとの約束なんだし。\x02\x03",

            "#0006Fうーん、できたらキーアも\x01",
            "連れて行ってあげたかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xD,
        (
            "#0204F#11Pでしたら内容を修正です。\x02\x03",

            "#0202Fまずは支援課のみんなで……\x01",
            "その後、ロイドさんとわたしで。\x02\x03",

            "それでノープロブレムでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#0000F#5Pあ、ああ……\x01",
            "それなら確かに問題ないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xD,
        (
            "#0209F#11Pふふっ……\x01",
            "楽しみにしていますね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_4ADD():

        label("loc_4ADD")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_4ADD")

    QueueWorkItem2(0x101, 2, lambda_4ADD)
    OP_93(0xD, 0x13B, 0x1F4)
    OP_68(55630, 1500, 13810, 8000)
    MoveCamera(54, 22, 0, 8000)
    OP_6E(500, 8000)
    SetCameraDistance(21500, 8000)
    Sleep(300)
    OP_95(0xD, 58140, 0, -380, 2000, 0x0)
    OP_95(0xD, 58350, 0, 1520, 2000, 0x0)
    OP_95(0xD, 57740, 0, 4190, 2000, 0x0)
    OP_95(0xD, 53180, 0, 8070, 2000, 0x0)
    OP_95(0xD, 53190, 0, 13960, 2000, 0x0)
    OP_95(0xD, 55730, 0, 13960, 2000, 0x0)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    ClearMapObjFlags(0x0, 0x10)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)

    def lambda_4BC4():
        OP_96(0xFE, 0xE4E8, 0x0, 0x3688, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4BC4)
    Sleep(1000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    Sleep(600)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)
    SetMapObjFlags(0x0, 0x10)
    EndChrThread(0xD, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(58830, 1500, 600, 0)
    MoveCamera(127, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    OP_93(0x101, 0x0, 0x0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0153
    ChrTalk(
        0x101,
        (
            "#0006F#11Pうーん、あんな簡単な\x01",
            "約束で良かったのかな……\x02\x03",

            "#0002F……まあ、いいか。\x01",
            "楽しみにしてるみたいだし。\x02\x03",

            "#0004Fティオとの約束のためにも……\x01",
            "絶対に事件を解決しないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E49")
    StopBGM(0xFA0)
    WaitBGM()
    Sound(517, 0, 100, 0)
    AddCraft(0x0, 0x155)
    AddCraft(0x2, 0x155)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ロイドとティオは\x01",
            "Ω#2Rオメガ#ストライクⅡを習得した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0155
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとティオのコンビクラフト、\x01",
            "《Ωストライク》が強化されました。\x02",
        )
    )

    CloseMessageWindow()

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "攻撃力や射程・範囲の他、\x01",
            "硬直時間などの性能がアップします。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7513", 0)

    label("loc_4E49")

    OP_D5(0x1E)
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(59090, 1500, 360, 0)
    MoveCamera(88, 16, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 59090, 0, 360, 315)
    SetScenarioFlags(0xE7, 3)
    OP_DE(0x2E, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_13_3143 end

    def Function_14_4EA4(): pass

    label("Function_14_4EA4")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0xE, 0xFF)
    OP_68(58810, 1400, -420, 0)
    MoveCamera(125, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16550, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00300.itp")
    SetChrPos(0x101, 59090, 0, 360, 180)
    SetCameraDistance(15550, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0157
    ChrTalk(
        0xE,
        "#0308F#5P#30W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        "#0005F#5Pあれ、ランディ……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    #Sound(1364, 255, 100, 0)    #voice#Randy
    OP_93(0xE, 0x0, 0x1F4)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0159
    AnonymousTalk(
        0xE,
        (
            "──よう、相棒。\x02\x03",

            "マジでとんでもない事に\x01",
            "なっちまったなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0160
    ChrTalk(
        0x101,
        "#0005F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xE,
        (
            "#0305F#11Pん、なんだ？\x01",
            "何か変なことを言ったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#0012F#5Pい、いや……\x02\x03",

            "#0008F……でも、率直な所、\x01",
            "ランディはどう思う？\x02\x03",

            "#0001F警備隊に本格的に攻められたら\x01",
            "ここがどこまで保#2Rも#つのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xE,
        (
            "#0303F#11Pま、正直厳しいだろうな。\x02\x03",

            "#0301Fクロスベルの警備隊は\x01",
            "れっきとした軍事組織だ。\x02\x03",

            "戦車や飛行船こそ持ってねぇが\x01",
            "練度も高いし、個人レベルじゃ\x01",
            "最高の武装が供給されている。\x02\x03",

            "#0306Fいくら最新のビルとはいえ、\x01",
            "要塞でもない民間施設が\x01",
            "そうそう保つもんじゃねぇだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#0008F#5Pやっぱりそうか……\x02\x03",

            "#0003F……となると、何とかして\x01",
            "警察本部や遊撃士たちと\x01",
            "連携する必要があるな……\x02\x03",

            "#0013Fせめて通信が回復するまでは\x01",
            "このビルを守りきらないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xE,
        (
            "#0303F#11Pま、そういうこった。\x02\x03",

            "#0308F……ったく、こんな事なら\x01",
            "アレを持ってくるんだったな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0166
    ChrTalk(
        0x101,
        "#0005F#5Pアレ？\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xE,
        "#0303F#11P…………………………………\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(500)

    #C0168
    ChrTalk(
        0xE,
        (
            "#0304F#5P……俺が２年前まで\x01",
            "使っていた導力ライフルだ。\x02\x03",

            "#0300F途轍#4Rとてつ#もない火力を持った、な。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        "#0008F#5Pそうか、猟兵時代の……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)

    #C0170
    ChrTalk(
        0x101,
        (
            "#0003F#5P……《赤い星座》だったか。\x02\x03",

            "#0000Fあれから少し調べたけど\x01",
            "その筋ではかなり有名みたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xE,
        (
            "#0309F#5Pハハッ……\x01",
            "“悪名高い”の間違いだろ。\x02\x03",

            "#0304F大陸西部最凶の猟兵団……\x01",
            "戦場を蹂躙する赤き死神……\x02\x03",

            "#0300Fちょっと前には、共和国方面で\x01",
            "《黒月》とやり合ってたらしい。\x02\x03",

            "それこそ正真正銘の殺し合いをな。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#0008F#5P……そうなのか……\x02\x03",

            "…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)
    Sleep(300)

    #C0173
    ChrTalk(
        0xE,
        (
            "#0302F#11P……悪ぃ。\x01",
            "引かせるつもりじゃなかった。\x02\x03",

            "#0303Fま、警備隊が本気を出したら\x01",
            "かなりヤバイことになるだろう。\x02\x03",

            "#0301Fしかも配備されたばかりって話の\x01",
            "新型装甲車まで持ち出されたら──\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#0004F#5P──なあ、ランディ。\x02\x03",

            "#0002F前に言った事だけど……\x01",
            "撤回させてもらってもいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xE,
        "#0305F#11Pへ……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#0000F#5P旧市街のレースの後の話さ。\x02\x03",

            "兄貴みたいな一人前になるまで\x01",
            "ランディの過去は聞かないっていう。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xE,
        "#0305F#11Pあ……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#0008F#5P──前にも話したけど、\x01",
            "兄貴は俺にとって\x01",
            "ヒーローみたいな存在だった。\x02\x03",

            "#0003F課長やダドリーさん、\x01",
            "アリオスさんも言ってたけど……\x02\x03",

            "#0000Fそこにいるだけで\x01",
            "どんな逆境も何とかしてくれるって\x01",
            "思わせてくれるような人だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xE,
        (
            "#0300F#11P……らしいな。\x02\x03",

            "#0306Fったく、どんだけ\x01",
            "化物じみたヤツだっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0002F#5Pはは、別にそこまで腕っ節が\x01",
            "強かったわけじゃないと思うけど。\x02\x03",

            "#0006F……最初はさ、\x01",
            "そんな兄貴の代わりにならなきゃ\x01",
            "いけないと思ってたんだ。\x02\x03",

            "じゃないと、クロスベルに\x01",
            "俺が戻ってくる資格はない……\x02\x03",

            "#0008Fそう思って、死にものぐるいで\x01",
            "捜査官資格を取って\x01",
            "今まで頑張ってきたけど……\x02\x03",

            "#0002Fやっぱり……\x01",
            "どこか無理があったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xE,
        (
            "#0303F#11P……そうか………\x02\x03",

            "#0300Fしかし、その割にゃ妙に\x01",
            "スッキリした顔をしてやがるな？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#0012F#5Pハハ、まあね。\x02\x03",

            "#0004F……そこまで行くと\x01",
            "逆に変な風に前向きになってさ。\x02\x03",

            "俺は兄貴みたいには凄くなれない……\x02\x03",

            "#0000F──だったら、\x01",
            "俺は俺として凄くなれれば\x01",
            "いいんじゃないかと思ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xE,
        "#0305F#11P！\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#0006F#5Pまあ、どんな風に凄くなるのかは\x01",
            "まだ分からないけど……\x02\x03",

            "キーアも引き取って\x01",
            "みんなも一応引っ張ってる立場で\x01",
            "ウジウジ悩んでもいられないだろう？\x02\x03",

            "#0002F幸い、ランディたちも助けてくれるし、\x01",
            "俺が凄くなくても何とかやれる……\x02\x03",

            "だったら今はその状況に\x01",
            "甘えさせてもらおうと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xE,
        (
            "#0309F#11Pはは……なんだよお前……\x02\x03",

            "#0302F……もう十分、\x01",
            "一人前のツラしてんじゃねーか。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#0004F#5Pランディはさ、判ってたんだろう？\x02\x03",

            "#0000F兄貴の背中を追い続けてるだけじゃ\x01",
            "いずれ俺が行き詰まるって……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xE,
        (
            "#0306F#11P……まーな。\x02\x03",

            "#0304Fだが、そうして挫折すんのも\x01",
            "お前の糧になるんじゃねーかと思った。\x02\x03",

            "#0302Fしかし、まさか挫折する前に\x01",
            "自分で気付いちまうとはなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#0004F#5Pはは、俺一人だったら\x01",
            "気付けなかったと思うけどね。\x02\x03",

            "#0002F──だから、あの時、\x01",
            "カッコ付けて聞かなかったことを\x01",
            "聞いてみたいと思ったんだ。\x02\x03",

            "兄貴みたいに俺の成長を\x01",
            "見守ってくれた誰かさんのことを\x01",
            "もっと知りたいと思ったから。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xE,
        "#0309F#11P#40W………ハハ……………\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    OP_93(0xE, 0xB4, 0x190)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0xE)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7001", 0)
    SetCameraDistance(14500, 60000)
    Sleep(1000)

    #C0190
    ChrTalk(
        0xE,
        (
            "#0308F#5P──なあ、ロイド。\x02\x03",

            "#0304Fお前、俺が今までどれだけ\x01",
            "戦場で敵を殺してきたと思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#0006F#5P……想像も付かないな。\x02\x03",

            "#0001F多分、俺の生きていた世界とは\x01",
            "かけ離れた所の話だろうから。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xE,
        (
            "#0312F#5Pクク、正解だ。\x01",
            "俺も正直覚えてねぇくらいだ。\x02\x03",

            "#0304F……物心付いた時から\x01",
            "戦場という世界で生きてきた。\x02\x03",

            "４つの時にナイフを渡され、\x01",
            "６つで拳銃の撃ち方を習った。\x02\x03",

            "#0303F……実戦は９歳だ。\x01",
            "親父の部隊で斥候として働き、\x01",
            "ふたりの敵兵を殺した。\x02\x03",

            "そして１２で小隊を、\x01",
            "１４で中隊を任されて……\x02\x03",

            "#0311F５年間……\x01",
            "犬のように戦場を駆け回った。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        "#0005F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xE,
        (
            "#0308F#5P……だが、俺は逃げた。\x02\x03",

            "ガルシアのオッサンみてぇに\x01",
            "望まれて抜けたわけじゃねえ……\x02\x03",

            "クソみたいな殺し合いに\x01",
            "嫌気が差したわけでもねぇ……\x02\x03",

            "#0303Fただ、何かを見失って\x01",
            "戦場からさ迷い出てきただけだ。\x02\x03",

            "#0311F腐った死人#4Rしびと#みてぇにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        "#0001F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xE,
        (
            "#0304F#5Pその後、あちこちさ迷って\x01",
            "最後にクロスベルに流れ着いて……\x02\x03",

            "警備隊に潜り込んだはいいが\x01",
            "ライフル使うのを拒否ってたら\x01",
            "阿呆司令にクビにされかけて……\x02\x03",

            "#0308Fそして課長に拾われて……\x01",
            "何故かこんな場所に立っている。\x02\x03",

            "#0312Fそれが俺……\x01",
            "ランドルフ・オルランドって男だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#0003F#5Pランディ……\x02\x03",

            "#0002F……ありがとう。\x01",
            "話してくれて。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x190)
    Sleep(300)

    #C0198
    ChrTalk(
        0xE,
        (
            "#0306F#11Pったく……お前、\x01",
            "Ｍっ気でもあるんじゃねえか？\x02\x03",

            "#0308Fどうしてこんな\x01",
            "クソみてぇな野郎の過去を\x01",
            "わざわざ知りたがるんだか……\x02\x03",

            "#0301F……引いてねぇとは言わさねぇぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        (
            "#0004F#5Pはは……\x01",
            "引いたといえば引いたけど。\x02\x03",

            "それでもやっぱり\x01",
            "どうしても知りたかったんだ。\x02\x03",

            "#0000Fそれに、俺の事情ばっかり\x01",
            "ランディに知られているのも\x01",
            "シャクだったし……\x02\x03",

            "#0002Fお互いをある程度知ってこその\x01",
            "“相棒”なんじゃないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0200
    ChrTalk(
        0xE,
        "#0305F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#0001F#5Pだってランディが\x01",
            "“相棒”って言ったんだろう？\x02\x03",

            "さっき俺が声をかけた時に。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xE,
        (
            "#0305F#11Pいや、あれは\x01",
            "挨拶代わりっつーか……\x02\x03",

            "#0301F……え、あれ。\x01",
            "俺、今までお前をそんな風に\x01",
            "呼んだことなかったっけ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#0002F#5P……多分。\x02\x03",

            "#0012Fえっと、だからさっきは\x01",
            "ちょっと嬉しかったんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)
    #Sound(1376, 255, 100, 0)    #voice#Randy
    Sleep(150)
    OP_82(0x64, 0x0, 0x7D0, 0x12C)

    #C0204
    ChrTalk(
        0xE,
        (
            "#0309F#11Pククッ……\x01",
            "#4Sははははははっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0205
    ChrTalk(
        0x101,
        (
            "#0011F#5Pそ、そんなに\x01",
            "笑うことないだろ？\x02\x03",

            "#0006F自分でもちょっと\x01",
            "気恥ずかしいんだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xE,
        (
            "#0302F#11Pクク……それが理由で\x01",
            "ここまで引っ張ったのかよ……\x02\x03",

            "#0304Fしかも先に自分曝#2Rさら#け出して\x01",
            "俺を追い込みやがるとは……\x02\x03",

            "#0309Fいやいや、Ｍと思わせておいて\x01",
            "実はＳってパターンだったとはなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        "#0011F#5Pな、なんだそりゃ……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(801, 0, 100, 0)
    Sleep(500)
    VolumeBGM(0x3C, 0x5DC)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性の声")

    #A0208
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──ビル内に残っている\x01",
            "皆様にお知らせいたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "非常時につき、\x01",
            "これより一部フロアの照明を\x01",
            "落とさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "また、保安上の理由から\x01",
            "エントランス以外の非常口は\x01",
            "全て閉鎖させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どうかご理解の上、火元などには\x01",
            "くれぐれもお気をつけ下さるよう\x01",
            "お願い申し上げます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0x7D0)

    #C0212
    ChrTalk(
        0xE,
        (
            "#0304F#11Pさぁて、いよいよ本格的な\x01",
            "篭城になってきやがったな。\x02\x03",

            "#0300F俺は念のため\x01",
            "１階のエントランスに\x01",
            "降りておくことにするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#0000F#5P分かった、俺の方は補給と\x01",
            "装備の確認をしておくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xE,
        "#0302F#11Pおお、任せたぜ。\x02",
    )

    CloseMessageWindow()

    def lambda_6B3D():

        label("loc_6B3D")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_6B3D")

    QueueWorkItem2(0x101, 2, lambda_6B3D)
    OP_68(57170, 1500, 860, 2500)
    MoveCamera(119, 22, 0, 2500)
    OP_95(0xE, 58140, 0, -380, 1200, 0x0)
    OP_6F(0x1)

    #C0215
    ChrTalk(
        0xE,
        (
            "#0303F#11P──警備隊が押し寄せたら\x01",
            "最後まで動けるのは俺らだろう。\x02\x03",

            "#0300Fお嬢やティオすけには\x01",
            "あんま無茶させたくないしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#0004F#5P……ああ、分かってる。\x02\x03",

            "#0000F俺とランディの２人で\x01",
            "何とか喰い止める必要があるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xE,
        (
            "#0302F#11Pそういう事だ。\x02\x03",

            "#0309F背中は任せたぜ──相棒。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#0005F#5Pあ……\x02\x03",

            "#0002F──了解！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_93(0xE, 0x13B, 0x1F4)
    OP_68(55630, 1500, 13810, 8000)
    MoveCamera(54, 22, 0, 8000)
    OP_6E(550, 8000)
    SetCameraDistance(21500, 8000)
    OP_95(0xE, 58350, 0, 1520, 2000, 0x0)
    OP_95(0xE, 57740, 0, 4190, 2000, 0x0)
    OP_95(0xE, 53180, 0, 8070, 2000, 0x0)
    OP_95(0xE, 53190, 0, 13960, 2000, 0x0)
    OP_95(0xE, 55730, 0, 13960, 2000, 0x0)
    StopBGM(0x2AF8)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    ClearMapObjFlags(0x0, 0x10)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)

    def lambda_6D8C():
        OP_96(0xFE, 0xE4E8, 0x0, 0x3688, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6D8C)
    Sleep(1000)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    Sleep(600)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)
    SetMapObjFlags(0x0, 0x10)
    EndChrThread(0xE, 0x1)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F00")
    Sound(517, 0, 100, 0)
    AddCraft(0x0, 0x156)
    AddCraft(0x3, 0x156)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ロイドとランディは\x01",
            "バーニングレイジⅡを習得した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとランディのコンビクラフト、\x01",
            "《バーニングレイジ》が強化されました。\x02",
        )
    )

    CloseMessageWindow()

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "攻撃力や射程・範囲の他、\x01",
            "硬直時間などの性能がアップします。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6F00")

    OP_CA(0x1, 0xFF, 0x0)
    OP_68(59090, 1500, 360, 0)
    MoveCamera(88, 16, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 59090, 0, 360, 315)
    PlayBGM("ed7513", 0)
    SetScenarioFlags(0xE7, 4)
    OP_DE(0x2F, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_14_4EA4 end

    def Function_15_6F5D(): pass

    label("Function_15_6F5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(171000, 1400, 123500, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0xA, 171500, 200, 123500, 270)
    SetChrPos(0xB, 171500, 200, 124400, 270)
    MoveCamera(40, 23, 0, 6000)
    SetCameraDistance(19000, 6000)
    FadeToBright(2000, 0)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(55000, 1200, 125000, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 54500, 30, 124600, 0)
    SetChrPos(0x102, 55500, 30, 124600, 0)
    SetChrPos(0x103, 54300, 30, 123500, 0)
    SetChrPos(0x104, 55700, 30, 123500, 0)
    SetChrPos(0x8, 55000, 150, 128800, 180)
    SetChrPos(0x9, 56600, 30, 126100, 315)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_68(55000, 1200, 126500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0222
    ChrTalk(
        0x8,
        "#5P#2803F………………………………\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x9,
        "#2901F#11P……お父様……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#12P#0006F──現状で判明している事は\x01",
            "確証があるわけではありません。\x02\x03",

            "#0008Fいずれきちんとした証拠を\x01",
            "揃える必要があると思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x8,
        (
            "#5P#2800Fああ……\x01",
            "君たちの立場ならそうだろう。\x02\x03",

            "#2806F……だが私は……\x01",
            "今、大きな失望感を感じている。\x02\x03",

            "その《教団》の残党とやらの\x01",
            "罪深さはもちろんだが……\x02\x03",

            "#2801Fそんな連中に付け込まれ、\x01",
            "ここまでの事態を引き起こした\x01",
            "愚か者たちには心底呆れ果てたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        "#12P#0003F………はい。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "#5P#2803F私とて、クロスベルの状況が\x01",
            "難しいものであるのは判っている。\x02\x03",

            "ルバーチェのような存在や\x01",
            "議員や役人たちの腐敗についても\x01",
            "ある程度は仕方ないと諦めていたが……\x02\x03",

            "#2801F……どうやら私は\x01",
            "とんだ愚か者だったようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x102,
        "#0108F#12P……おじさま……\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x9,
        (
            "#2903F#11Pそうですわね……\x02\x03",

            "ＩＢＣは少なからず、\x01",
            "クロスベルの政界に影響力がある。\x02\x03",

            "#2901Fお父様は今まで、あえて中立で\x01",
            "あろうとしていましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        (
            "#5P#2801Fその怠惰が今回の事態を\x01",
            "引き起こす一因にもなったようだ。\x02\x03",

            "#2803F……すまない。\x01",
            "お詫びのしようもないくらいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        "#12P#0011Fそ、そんな……\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x104,
        (
            "#12P#0306Fいや、さすがにそれは\x01",
            "気にしすぎじゃないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        (
            "#12P#0200F実際、権限や責任が\x01",
            "あるわけでもないですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        (
            "#5P#2800Fいや、時の政権に対して\x01",
            "財界がある程度働きかけるのは\x01",
            "本来は常識的なことだろう。\x02\x03",

            "#2803F……それ以前に、私にも\x01",
            "クロスベルを愛する市民の\x01",
            "一人という自負があったはずだ。\x02\x03",

            "#2801Fだが忙しさにかまけ……\x01",
            "その愛郷心も薄れていたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#12P#0008F………………………………\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x102,
        (
            "#0106F#12P……それは私たち市民、\x01",
            "一人一人がそうだったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "#5P#2803Fああ……\x02\x03",

            "#2800F……いずれにせよ、\x01",
            "ここで愚痴っていても仕方ない。\x02\x03",

            "この事態を解決するために\x01",
            "我がＩＢＣは総力をもって\x01",
            "君たちに協力させてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        (
            "#12P#0002F総裁……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x102,
        "#0102F#12P……とても心強いです。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    #C0240
    ChrTalk(
        0x9,
        (
            "#5P#2906Fといっても、この状況は\x01",
            "如何#4Rいかん#ともしがたいですわね。\x02\x03",

            "#2901F警察本部やタングラム門とも\x01",
            "連絡が途絶しているのだったかしら？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7824():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7824)
    Sleep(50)

    def lambda_7834():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7834)
    Sleep(50)

    def lambda_7844():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7844)
    Sleep(150)

    #C0241
    ChrTalk(
        0x101,
        (
            "#6P#0006Fはい……\x01",
            "何度か連絡してみたんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        (
            "#6P#0206F……何らかの理由で\x01",
            "通信妨害がかかっているようです。\x02\x03",

            "#0201F導力ネットワークによる連絡を\x01",
            "試すことはできないんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x9,
        (
            "#5P#2903F……どうやら何者かによって\x01",
            "ジオフロントの導力ケーブルが\x01",
            "遮断されているらしいですわね。\x02\x03",

            "#2901F何とか迂回ルートを確保すれば\x01",
            "通信網を回復できると思いますが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)

    #C0244
    ChrTalk(
        0x8,
        (
            "#5P#2801Fならば技術部のスタッフに\x01",
            "最優先でやらせたまえ。\x02\x03",

            "#2803F警察本部、タングラム門、\x01",
            "遊撃士協会との連絡は勿論だが……\x02\x03",

            "#2800F市内の各端末との連絡も取れれば\x01",
            "さらに状況も掴めるようになるだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)

    #C0245
    ChrTalk(
        0x9,
        "#2902F#11P判りましたわ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0246
    ChrTalk(
        0x8,
        (
            "#5P#2801Fそして……\x01",
            "もう一つの心配はキーア君か。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7AEB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7AEB)
    Sleep(50)

    def lambda_7AFB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7AFB)
    Sleep(50)

    def lambda_7B0B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B0B)
    Sleep(50)

    def lambda_7B1B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7B1B)
    Sleep(200)

    #C0247
    ChrTalk(
        0x101,
        (
            "#12P#0008Fはい……\x02\x03",

            "#0013F……操られた警備隊が\x01",
            "俺たちを執拗に追った目的は\x01",
            "キーアの可能性が高いと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x104,
        (
            "#12P#0303F実際、俺たちに発砲した時は\x01",
            "ほとんど威嚇射撃だったしな。\x02\x03",

            "#0301F一方、しんがりの課長たちには\x01",
            "容赦なく撃ってきてたみてぇだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x103,
        (
            "#12P#0203Fキーアを決して傷つけずに\x01",
            "身柄を奪い取れ……\x02\x03",

            "#0201F……そんな風に\x01",
            "操られているのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x9,
        (
            "#5P#2904Fまあ、あれだけ可愛かったら\x01",
            "攫#2Rさら#いたく気持ちも判りますけど。\x02\x03",

            "#2901Fヨアヒムといったかしら？\x01",
            "随分、不気味な男みたいですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#12P#0006Fいや……\x01",
            "正直、彼が何を考えているのか\x01",
            "はっきりとした事は判らないんです。\x02\x03",

            "#0008F何のためにキーアが必要なのか……\x02\x03",

            "#0013F白いファイルの最後にあった写真が\x01",
            "どこで撮ったものなのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        (
            "#0106F#12P……そもそもキーアちゃんが\x01",
            "どうしてあの競売会の場にいたのか\x01",
            "それすら分かっていないの。\x02\x03",

            "#0108Fあの子の記憶が戻っていたら\x01",
            "手がかりになったんでしょうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x9,
        "#5P#2901Fなるほど……歯がゆいですわね。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x8,
        (
            "#5P#2803Fいずれにせよ、これだけの事態を\x01",
            "引き起こしたと思われる人物だ。\x02\x03",

            "恐ろしく危険な男であるのは\x01",
            "間違いないと思った方がいいだろう。\x02\x03",

            "#2801F君たちをこのビルに匿#2Rかくま#ったのは\x01",
            "簡単には特定できないだろうが……\x02\x03",

            "万が一の事はあり得る。\x01",
            "覚悟だけはした方が良さそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        "#12P#0013F……はい。\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x104,
        "#12P#0301Fそうッスね……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        (
            "#5P#2804F各所との連絡などは引き続き、\x01",
            "ＩＢＣのスタッフにやらせておく。\x02\x03",

            "キーア君たちも休んだことだし、\x01",
            "君たちも少し休憩したまえ。\x02\x03",

            "#2800Fそれともベッドを用意しようか？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        (
            "#12P#0002Fいや……\x01",
            "それは遠慮しておきます。\x02\x03",

            "#0000Fそれより、このビルの中で\x01",
            "補給できる場所はないですか？\x02\x03",

            "少々、装備が心許なくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x104,
        (
            "#12P#0306F確かにさっきは\x01",
            "いきなり襲撃されたからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "#5P#2800Fそれなら、１階のカウンターで\x01",
            "各種のサービスが受けられるよう、\x01",
            "取り計らっておこう。\x02\x03",

            "各メーカーの支社もあるので\x01",
            "武器の融通も利くかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x9,
        (
            "#5P#2902Fエプスタイン財団も入ってますから\x01",
            "工房機能も使えるでしょうし……\x02\x03",

            "緊急時の備えもしていますから\x01",
            "食料なども融通できるはずですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x102,
        "#0102F#12Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x103,
        (
            "#12P#0202F確かに何でも\x01",
            "揃いそうな勢いですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x104,
        (
            "#12P#0309Fいや、さすがは\x01",
            "天下のＩＢＣビルだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        (
            "#12P#0004F……ご配慮、感謝します。\x02\x03",

            "#0002Fそれでは少しの間、\x01",
            "休憩させていただきます。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0266
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "パーティがいったん解散しました。\x02",
        )
    )

    CloseMessageWindow()

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "１階のカウンターに話しかけると\x01",
            "各ショップの機能を使う事が出来ます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なお、パーティ外のメンバーでも\x01",
            "装備・クオーツの変更などは\x01",
            "引き続き行う事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    SetMapFlags(0x10000)
    OP_68(53000, 1500, 45000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 53000, 0, 45000, 180)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x4)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 59090, 30, 124780, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_853A")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8573")

    label("loc_853A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8559")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8573")

    label("loc_8559")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8573")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8573")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8592")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_85CB")

    label("loc_8592")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_85B1")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_85CB")

    label("loc_85B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_85CB")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_85CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_85EA")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8623")

    label("loc_85EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8609")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8623")

    label("loc_8609")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8623")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_END)), "loc_8638")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_END)), "loc_864D")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_864D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_8662")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_END)), "loc_8677")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_END)), "loc_868C")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_868C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_86A1")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_86A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_END)), "loc_86B6")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_86B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_END)), "loc_86CB")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_86CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_86E0")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_86E0")

    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8728")
    ClearChrFlags(0xC, 0x40)
    SetChrChipByIndex(0xC, 0x7)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xC, 0x10)
    SetChrPos(0xC, 59090, 0, -1070, 135)
    Jump("loc_875F")

    label("loc_8728")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8746")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_875F")

    label("loc_8746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_875F")
    ClearChrFlags(0xE, 0x80)

    label("loc_875F")

    SetScenarioFlags(0xE3, 7)
    OP_C7(0x0, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_15_6F5D end

    def Function_16_876B(): pass

    label("Function_16_876B")

    EventBegin(0x0)
    Fade(1000)
    OP_68(171500, 900, 122600, 0)
    MoveCamera(50, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 171000, 0, 121600, 0)
    OP_0D()
    Sleep(500)

    #C0269
    ChrTalk(
        0xA,
        "#5P#1113F#80W……すーすー………\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#11P#0002F（はは……\x01",
            "  よく寝てるみたいだな……）\x02\x03",

            "#0004F（無理もないか……\x01",
            "  あれだけの大立ち回りだったし……）\x02",
        )
    )

    CloseMessageWindow()
    Sound(820, 0, 100, 0)

    def lambda_885B():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_885B)
    WaitChrThread(0xA, 2)
    Sleep(500)

    #C0271
    ChrTalk(
        0xA,
        (
            "#5P#1114F#80W……んんっ………\x02\x03",

            "#70W……ロイド……どこぉ……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetCameraDistance(21000, 30000)

    #C0272
    ChrTalk(
        0xA,
        (
            "#1P#1114F#60W#5Pエリィ……ティオ……\x01",
            "……ランディ……\x02\x03",

            "……暗い……暗いよ……\x02\x03",

            "どこ……どこに行ったのぉ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        "#11P#0001F（……キーア………）\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(820, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0274
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはキーアの頭をそっと撫でた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    #C0275
    ChrTalk(
        0x101,
        (
            "#11P#0004F……大丈夫。\x01",
            "絶対に俺たちが守るから。\x02\x03",

            "#0002Fだからキーア……安心してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xA,
        (
            "#5P#1113F#70W………ん…………\x02\x03",

            "#5P#1104F#70W……………スゥ………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    #C0277
    ChrTalk(
        0x101,
        (
            "#11P#0008F（今まで自分たちの事だけで\x01",
            "  精一杯だったけど……）\x02\x03",

            "#0004F（やっと……分かった気がする。）\x02\x03",

            "（何のためにクロスベルに戻って\x01",
            "  捜査官を目指したのか……）\x02\x03",

            "#0002F（……兄貴も同じだったのかな？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(169830, 1400, 121000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 169830, 0, 121000, 270)
    SetScenarioFlags(0xE4, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_876B end

    def Function_17_8BC1(): pass

    label("Function_17_8BC1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08700.itc", 0x1F)
    SoundLoad(806)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    ClearMapFlags(0x10000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01100.itp")
    OP_68(55000, 1000, 128000, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 55000, 30, 118000, 0)
    SetChrPos(0x102, 56200, 30, 125800, 90)
    SetChrPos(0x103, 54500, 30, 117000, 0)
    SetChrPos(0x104, 55600, 30, 117000, 0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 55000, 150, 128800, 180)
    SetChrPos(0x9, 57800, 30, 126400, 270)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    SetCameraDistance(18500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0278
    ChrTalk(
        0x101,
        "#0001F──失礼します。\x02",
    )

    CloseMessageWindow()
    OP_68(55000, 1000, 126500, 2000)

    def lambda_8D20():
        OP_95(0xFE, 55000, 0, 124100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D20)
    Sleep(200)

    def lambda_8D3D():

        label("loc_8D3D")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_8D3D")

    QueueWorkItem2(0x102, 2, lambda_8D3D)
    Sleep(100)

    def lambda_8D52():

        label("loc_8D52")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_8D52")

    QueueWorkItem2(0x9, 2, lambda_8D52)
    Sleep(1200)

    #C0279
    ChrTalk(
        0x102,
        "#5P#0101Fロイド……！\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x8,
        "#5P#2800Fおお、来てくれたか。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x9, 0x2)

    #C0281
    ChrTalk(
        0x101,
        "#12P#0001F一体、何かあったんですか？\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "#5P#2803Fああ、警備隊の隊員が\x01",
            "２人ほどゲート前に来たらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x101,
        "#12P#0013Fそれで……！？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x9,
        (
            "#11P#2903F今のところ、攻撃する事もなく\x01",
            "留まっているだけみたいですわね。\x02\x03",

            "#2901Fまあ特殊合金製のゲートですから\x01",
            "突破も難しいでしょうけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#12P#0006Fそうですか……\x02\x03",

            "#0008F……俺たちがここにいると\x01",
            "バレた可能性は高そうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        "#5P#0106F……ええ……\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)

    #C0287
    ChrTalk(
        0x103,
        "#0201F……失礼します。\x02",
    )

    CloseMessageWindow()

    def lambda_8F7A():
        OP_95(0xFE, 55600, 30, 122600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8F7A)

    def lambda_8F94():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8F94)
    Sleep(150)

    def lambda_8FA8():
        OP_95(0xFE, 54500, 30, 122500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8FA8)

    def lambda_8FC2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8FC2)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0288
    ChrTalk(
        0x101,
        "#5P#0005Fティオ、ランディ。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)

    #C0289
    ChrTalk(
        0x104,
        (
            "#12P#0301F何でも警備隊員が\x01",
            "ゲート前に来たらしいな？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#5P#0001Fああ、今のところ、\x01",
            "何もしていないみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_911B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_911B)

    def lambda_9128():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9128)

    def lambda_9135():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9135)
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(500)

    #C0291
    ChrTalk(
        0x8,
        (
            "#5P#2801F──私だ。\x02\x03",

            "#2805F……なに……\x02\x03",

            "#2803F……ふむ……ふむ……\x02\x03",

            "………………………………\x02\x03",

            "#2801F………なんだと？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        "#12P#0001F（……どうしたんだ……？）\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        "#0108F（嫌な予感がするわね……）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0294
    ChrTalk(
        0x8,
        (
            "#5P#2803F……ゲート前の警備隊員が\x01",
            "妙なことをし始めたらしい。\x02\x03",

            "#2801F円筒状の装置のようなものを\x01",
            "設置しているとの事だが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0295
    ChrTalk(
        0x103,
        "#12P#0201Fまさか……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x104,
        "#12P#0307F指向性の導力爆弾か！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_9388():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9388)
    Sleep(50)

    def lambda_9398():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9398)
    Sleep(50)

    def lambda_93A8():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_93A8)

    #C0297
    ChrTalk(
        0x101,
        "#5P#0011Fな、なんだそれは！？\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x104,
        (
            "#12P#0301F軍隊で使われている\x01",
            "破壊工作用の導力爆弾だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x103,
        (
            "#12P#0206F特殊合金製のゲートでも\x01",
            "さすがに保たないかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        "#5P#0101Fそんな……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x8,
        "#5P#2801Fくっ、そんなものが……\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x9,
        (
            "#11P#2901F……操られているくせに\x01",
            "知恵が回りますわね。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)

    #C0303
    ChrTalk(
        0x101,
        (
            "#5P#0003F──仕方ない。\x02\x03",

            "#0000Fランディ、打って出よう。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x104,
        (
            "#12P#0304Fああ……\x01",
            "それしか無さそうだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_9592():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9592)

    #C0305
    ChrTalk(
        0x8,
        "#5P#2805Fロイド君……！？\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x9,
        (
            "#11P#2910Fあなたたち……\x01",
            "無駄死にをするつもり！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    #C0307
    ChrTalk(
        0x101,
        (
            "#6P#0000Fいや、その導力爆弾の設置を\x01",
            "妨害するだけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#12P#0309Fま、そのまま小競り合いに\x01",
            "なっちまう気はしますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x102,
        "#5P#0100F勿論、私たちも行くわよ？\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x103,
        "#12P#0202Fメンバーとして当然です。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ……\x01",
            "サポートは頼んだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x9,
        "#11P#2901Fエリィ、ティオさん……\x02",
    )

    CloseMessageWindow()

    def lambda_971A():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_971A)
    Sleep(100)
    TurnDirection(0x103, 0x9, 500)
    Sleep(200)

    #C0313
    ChrTalk(
        0x102,
        (
            "#6P#0109Fふふっ……\x01",
            "これが私の仕事だから。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x103,
        "#12P#0204F……心配ご無用です。\x02",
    )

    CloseMessageWindow()

    def lambda_9788():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9788)
    Sleep(150)

    def lambda_9798():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9798)
    Sleep(50)
    TurnDirection(0x103, 0x8, 500)
    Sleep(200)

    #C0315
    ChrTalk(
        0x101,
        (
            "#12P#0004F無論、俺たちも無駄死に\x01",
            "するつもりはありません。\x02\x03",

            "#0000F警察本部か副司令の部隊か……\x01",
            "応援が来るまでの辛抱ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#12P#0300Fゲート前なら地形の利もある。\x02\x03",

            "ま、俺たちに任せてくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x8,
        (
            "#5P#2803F……分かった。\x02\x03",

            "#2801F女神#4Rエイドス#の加護を──\x01",
            "くれぐれも気をつけたまえ！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(52700, 1100, 45900, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 52200, 0, 46500, 180)
    SetChrPos(0x102, 53200, 0, 46500, 180)
    SetChrPos(0x103, 52200, 0, 46500, 180)
    SetChrPos(0x104, 53200, 0, 46500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 52700, 0, 46500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0xA, 56500, 0, 38800, 270)
    SetChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xB, 56500, 0, 38800, 270)
    SetChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x2)
    OP_68(52700, 1100, 39800, 4000)

    def lambda_9A50():
        OP_96(0xFE, 0xCB84, 0x0, 0x9B78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A50)

    def lambda_9A6A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A6A)
    Sleep(400)

    def lambda_9A7E():
        OP_96(0xFE, 0xD034, 0x0, 0x9B78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A7E)

    def lambda_9A98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9A98)
    Sleep(400)

    def lambda_9AAC():
        OP_96(0xFE, 0xCB84, 0x0, 0x9FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9AAC)

    def lambda_9AC6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9AC6)
    Sleep(400)

    def lambda_9ADA():
        OP_96(0xFE, 0xD034, 0x0, 0x9FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9ADA)

    def lambda_9AF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9AF4)
    Sleep(700)

    def lambda_9B08():
        OP_96(0xFE, 0xCDDC, 0x0, 0xA604, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9B08)

    def lambda_9B22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9B22)
    Sleep(700)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    WaitChrThread(0x101, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9B7C():

        label("loc_9B7C")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9B7C")

    QueueWorkItem2(0x101, 2, lambda_9B7C)
    WaitChrThread(0x102, 1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9BAA():

        label("loc_9BAA")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9BAA")

    QueueWorkItem2(0x102, 2, lambda_9BAA)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9BD8():

        label("loc_9BD8")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9BD8")

    QueueWorkItem2(0x103, 2, lambda_9BD8)
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9C06():

        label("loc_9C06")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9C06")

    QueueWorkItem2(0x104, 2, lambda_9C06)

    def lambda_9C18():

        label("loc_9C18")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9C18")

    QueueWorkItem2(0x9, 2, lambda_9C18)
    Sleep(1000)
    OP_79(0x1)
    OP_79(0x2)
    WaitChrThread(0x9, 1)
    OP_6F(0x1)
    Fade(500)
    OP_68(53200, 1100, 39730, 0)
    MoveCamera(67, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)

    def lambda_9C6C():
        OP_95(0xFE, 54100, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9C6C)

    def lambda_9C86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_9C86)
    Sound(2040, 255, 100, 0)    #voice#KeA
    WaitChrThread(0xA, 2)
    WaitChrThread(0xA, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x9, 0x2)
    OP_93(0xA, 0x12C, 0x1F4)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0318
    AnonymousTalk(
        0xA,
        "#40W……ロイドたち、どこ行くのー？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0319
    ChrTalk(
        0x101,
        "#6P#0005Fキーア……\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x104,
        (
            "#5P#0309Fはは……\x01",
            "ちょいとお仕事でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xA,
        (
            "#11P#1100Fふぅん……\x02\x03",

            "#1109Fキーアも付いてっていい？\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x102,
        "#5P#0108Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x103,
        "#6P#0208F……えっと……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        (
            "#6P#0003F……だめだめ。\x01",
            "子供はもう寝る時間だろう？\x02\x03",

            "#0000Fシズクちゃんだって\x01",
            "ちゃんと寝てるんだから──\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9E72():
        OP_95(0xFE, 55200, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9E72)

    def lambda_9E8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_9E8C)
    WaitChrThread(0xB, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9EEC():

        label("loc_9EEC")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_9EEC")

    QueueWorkItem2(0x102, 2, lambda_9EEC)

    def lambda_9EFE():

        label("loc_9EFE")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_9EFE")

    QueueWorkItem2(0x103, 2, lambda_9EFE)
    WaitChrThread(0xB, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    OP_93(0xB, 0x12C, 0x1F4)

    #C0325
    ChrTalk(
        0x102,
        "#5P#0105Fシズクちゃん……\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x104,
        "#5P#0306F……起こしちまったか。\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xB,
        (
            "#11P#6005Fご、ごめんなさい……\x01",
            "目が覚めてしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        (
            "#6P#0002Fいや……\x01",
            "うるさくしてゴメンな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Sleep(300)

    #C0329
    ChrTalk(
        0x101,
        (
            "#12P#0003F──マリアベルさん。\x01",
            "２人のことを頼みます。\x02\x03",

            "#0000Fちゃんと寝かせておいてください。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(150)

    #C0330
    ChrTalk(
        0x9,
        "#2904F#5P……ええ、分かりましたわ。\x02",
    )

    CloseMessageWindow()

    def lambda_A070():

        label("loc_A070")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_A070")

    QueueWorkItem2(0x101, 2, lambda_A070)
    OP_68(53790, 1100, 39870, 1000)

    def lambda_A093():
        OP_95(0xFE, 54700, 0, 41500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A093)
    WaitChrThread(0x9, 1)

    def lambda_A0B1():
        OP_95(0xFE, 54700, 0, 40000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A0B1)
    WaitChrThread(0x9, 1)
    OP_6F(0x1)

    #C0331
    ChrTalk(
        0x9,
        (
            "#5P#2902F──さあ２人とも。\x01",
            "ココアでも淹れてあげますわ。\x02\x03",

            "暖かくしてお休みなさい。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A129():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_A129)
    Sleep(50)
    TurnDirection(0xB, 0x9, 500)

    #C0332
    ChrTalk(
        0xA,
        "#11P#1112Fえ、え……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xB,
        "#11P#6008F………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 5000)
    BeginChrThread(0xB, 3, 0, 18)
    BeginChrThread(0xA, 3, 0, 19)
    BeginChrThread(0x9, 3, 0, 20)

    def lambda_A19D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A19D)
    Sleep(50)

    def lambda_A1AD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A1AD)
    Sleep(50)

    def lambda_A1BD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A1BD)
    Sleep(50)

    def lambda_A1CD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A1CD)
    WaitChrThread(0x101, 2)

    def lambda_A1DE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A1DE)
    Sleep(50)

    def lambda_A1FB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A1FB)
    Sleep(50)

    def lambda_A218():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A218)
    Sleep(50)

    def lambda_A235():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A235)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0x9, 3)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_CA(0x1, 0xFF, 0x0)
    ReplaceBGM("ed7513", "ed7512")
    OP_24(0x326)
    SetScenarioFlags(0x5C, 0)
    NewScene("c133B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_8BC1 end

    def Function_18_A2A1(): pass

    label("Function_18_A2A1")


    def lambda_A2A6():
        OP_95(0xFE, 56500, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A2A6)
    Sleep(300)

    def lambda_A2C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_A2C3)
    WaitChrThread(0xB, 1)
    Return()

    # Function_18_A2A1 end

    def Function_19_A2D4(): pass

    label("Function_19_A2D4")

    OP_93(0xA, 0x12C, 0x1F4)
    Sleep(500)

    def lambda_A2E3():
        OP_96(0xFE, 0xDCB4, 0x0, 0x9790, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A2E3)
    Sleep(500)

    def lambda_A300():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_A300)
    WaitChrThread(0xA, 1)
    Return()

    # Function_19_A2D4 end

    def Function_20_A311(): pass

    label("Function_20_A311")

    Sleep(900)

    def lambda_A319():
        OP_95(0xFE, 55200, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A319)
    WaitChrThread(0x9, 1)

    def lambda_A337():
        OP_95(0xFE, 56500, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A337)
    Sleep(300)

    def lambda_A354():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A354)
    WaitChrThread(0x9, 1)
    Return()

    # Function_20_A311 end

    def Function_21_A365(): pass

    label("Function_21_A365")

    TalkBegin(0xFF)
    SetChrName("")

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "まるで生きているかのような\x01",
            "精巧な人形がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_21_A365 end

    SaveToFile()

Try(main)
