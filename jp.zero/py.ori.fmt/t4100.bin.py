from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4100.bin",                # FileName
        "t4100",                    # MapName
        "t4100",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4100",                  # 0
        "ミュシャ夫人",           # 1
        "クイント老人",           # 2
        "観光客リューマ",         # 3
        "ガイ墓前の花",           # 4
        "アリオス家墓前の花",     # 5
        "グリムウッド家墓前の墓", # 6
    ))

    AddCharChip((
        "chr/ch20100.itc",                   # 00
        "chr/ch20000.itc",                   # 01
        "apl/ch50423.itc",                   # 02
        "chr/ch34200.itc",                   # 03
    ))

    DeclNpc(8579,    2000,    25379,   0,    257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-8869,   0,       11800,   0,    385,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(24340,   0,       33569,   45,   385,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(20600,   0,       34000,   0,    502,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(12000,   4000,    37000,   0,    502,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(190,     4200,    45040,   1200,    190,     5700,    45040,   0x007C, 0,  8,  0x0000)
    DeclActor(-23050,  0,       25770,   1200,    -22620,  1500,    25860,   0x007C, 0,  9,  0x0000)
    DeclActor(5560,    4000,    44710,   5000,    5560,    4000,    44710,   0x007C, 0,  12, 0x0000)
    DeclActor(20570,   0,       34830,   1500,    20570,   1500,    34830,   0x007C, 0,  10, 0x0000)
    DeclActor(12080,   4000,    37650,   1500,    12080,   5500,    37650,   0x007C, 0,  11, 0x0000)

    ScpFunction((
        "Function_0_238",          # 00, 0
        "Function_1_2F0",          # 01, 1
        "Function_2_74D",          # 02, 2
        "Function_3_897",          # 03, 3
        "Function_4_962",          # 04, 4
        "Function_5_17F4",         # 05, 5
        "Function_6_1E13",         # 06, 6
        "Function_7_1EED",         # 07, 7
        "Function_8_2751",         # 08, 8
        "Function_9_2826",         # 09, 9
        "Function_10_2C70",        # 0A, 10
        "Function_11_2D16",        # 0B, 11
        "Function_12_2DF4",        # 0C, 12
        "Function_13_3A66",        # 0D, 13
    ))


    def Function_0_238(): pass

    label("Function_0_238")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_278"),
        (1, "loc_284"),
        (2, "loc_290"),
        (3, "loc_29C"),
        (4, "loc_2A8"),
        (5, "loc_2B4"),
        (6, "loc_2C0"),
        (SWITCH_DEFAULT, "loc_2D8"),
    )


    label("loc_278")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_284")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_290")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_29C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_2A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_2B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_2C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_2D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_2EF")

    Return()

    # Function_0_238 end

    def Function_1_2F0(): pass

    label("Function_1_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74C")
    OP_95(0xFE, -8870, 0, 11800, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -16950, 0, 11340, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -19140, 0, 11340, 2000, 0x0)
    OP_95(0xFE, -19140, 0, 16070, 2000, 0x0)
    OP_95(0xFE, -21040, 0, 16090, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -16960, 0, 16090, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -1200, 0, 16090, 2000, 0x0)
    OP_95(0xFE, -1200, 2000, 25270, 2000, 0x0)
    OP_95(0xFE, -10990, 2000, 25270, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -4930, 2000, 25270, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -1200, 2000, 25270, 2000, 0x0)
    OP_95(0xFE, -1200, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, -8460, 4000, 35990, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -170, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, -50, 4200, 43970, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, -170, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, 12000, 4000, 35990, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 4970, 4000, 36140, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 1310, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, 1310, 0, 8039, 2000, 0x0)
    OP_95(0xFE, 15920, 0, 8039, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 22720, 0, 8039, 2000, 0x0)
    OP_95(0xFE, 22720, 0, 13250, 2000, 0x0)
    OP_95(0xFE, 20500, 0, 13250, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 11500, 0, 13250, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 9240, 0, 13250, 2000, 0x0)
    OP_95(0xFE, 9240, 0, 16390, 2000, 0x0)
    OP_95(0xFE, 15980, 0, 19640, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 23050, 0, 19550, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 21270, 0, 25620, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 27500, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 27500, 0, 31330, 2000, 0x0)
    OP_95(0xFE, 20470, 0, 33170, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x6A, 0x190)
    Sleep(100)
    OP_95(0xFE, 27500, 0, 31330, 2000, 0x0)
    OP_95(0xFE, 27500, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 19550, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 6410, 2000, 0x0)
    OP_95(0xFE, 30, 0, 6690, 2000, 0x0)
    Jump("Function_1_2F0")

    label("loc_74C")

    Return()

    # Function_1_2F0 end

    def Function_2_74D(): pass

    label("Function_2_74D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_75C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 7)

    label("loc_75C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_774")
    Event(0, 13)

    label("loc_774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_782")
    Jump("loc_83E")

    label("loc_782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_790")
    Jump("loc_83E")

    label("loc_790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_79E")
    Jump("loc_83E")

    label("loc_79E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7B1")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_83E")

    label("loc_7B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7C4")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_83E")

    label("loc_7C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7D7")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_83E")

    label("loc_7D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7E5")
    Jump("loc_83E")

    label("loc_7E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7F8")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_83E")

    label("loc_7F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_806")
    Jump("loc_83E")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_814")
    Jump("loc_83E")

    label("loc_814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_827")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_83E")

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_835")
    Jump("loc_83E")

    label("loc_835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_83E")

    label("loc_83E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_87D")
    SetChrChipByIndex(0xB, 0x2)
    SetChrPos(0xB, -23000, 0, 25500, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)

    label("loc_87D")

    BeginChrThread(0x9, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_896")
    ClearChrFlags(0xA, 0x80)

    label("loc_896")

    Return()

    # Function_2_74D end

    def Function_3_897(): pass

    label("Function_3_897")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8A9")
    Jump("loc_8E6")

    label("loc_8A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8E6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C3")
    Jump("loc_8E6")

    label("loc_8C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_8D5")
    Jump("loc_8E6")

    label("loc_8D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_8E6")
    OP_66(0x2, 0x1)

    label("loc_8E6")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_902")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)

    label("loc_902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_919")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_919")

    SoundDistance(0x84, 0xFFFFD878, 0xFA0, 0xDEA8, 0x2710, 0x186A0, 0x64, 0x0)
    OP_E1(0x6C2, 0xFA0, 0xDEA8)
    OP_E1(0x4F60, 0xFA0, 0xDEA8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_961")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)

    label("loc_961")

    Return()

    # Function_3_897 end

    def Function_4_962(): pass

    label("Function_4_962")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A23")

    #C0001
    ChrTalk(
        0xFE,
        (
            "あなたたち……\x01",
            "あのお墓を調べていたわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "随分前から、\x01",
            "あのお墓は名前の部分が\x01",
            "潰れてしまっているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "一体、どなたのお墓\x01",
            "なんでしょうね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AA4")

    label("loc_A23")


    #C0004
    ChrTalk(
        0xFE,
        (
            "毎日お参りに来る私も、\x01",
            "あのお墓にお客さんがいるのを\x01",
            "見たことが無いわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "あのお墓は一体、\x01",
            "どなたのものなんでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA4")

    TalkEnd(0xFE)
    Return()

    label("loc_AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA0")

    #C0006
    ChrTalk(
        0xFE,
        (
            "時々、人に言われる事があるの。\x01",
            "故人に縛られて余生を無駄に\x01",
            "しているんじゃないかって……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "……ふふ、でも、\x01",
            "この人を忘れない為には\x01",
            "ここに来るしかないでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "だから私はこれからも\x01",
            "お墓参りに来続けると思うわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C2D")

    label("loc_BA0")


    #C0009
    ChrTalk(
        0xFE,
        (
            "人にどう言われようと……\x01",
            "私はこれからもこの人のもとに\x01",
            "訪ねに来ると思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "あの世とこの世に分かたれた夫婦の\x01",
            "唯一の繋がりだもの……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2D")

    Jump("loc_17F0")

    label("loc_C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_D15")

    #C0011
    ChrTalk(
        0xFE,
        "人と人が戦うのは悲しいことだわ……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "それが組織や、国どうしの戦いになると\x01",
            "どうしても巻き込まれる人が出てくる。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "リベールの女王様が\x01",
            "《不戦条約》を提案したように……\x01",
            "戦わずに済む術を考えていきたいわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F0")

    label("loc_D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DB5")

    #C0014
    ChrTalk(
        0xFE,
        (
            "墓守さん、毎日あんなふうに\x01",
            "墓の様子を見てくださっているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "墓石はただの目印でしかないけれど……\x01",
            "ここで眠る人達は皆、喜んでいるわよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F0")

    label("loc_DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1011")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1E")
    OP_93(0xFE, 0x0, 0x0)

    #C0016
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x153,
        (
            "#1110F……ねえおばあちゃん。\x01",
            "目をつむって何してるの？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0018
    ChrTalk(
        0xFE,
        "え……？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#0005Fっとと……！\x01",
            "こら、キーア……！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "ふふ、いいのよ。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "……私の主人がこの地面の下で\x01",
            "眠っているから、お祈りしていたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x153,
        "#1106Fおいのり…………\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "そう……ここに来ると\x01",
            "主人とお話できる気がするから……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_100C")

    label("loc_F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_F79")

    #C0024
    ChrTalk(
        0xFE,
        (
            "さぁて……\x01",
            "お家にもどるとしましょうかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "あなた……また来るわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_100C")

    label("loc_F79")


    #C0026
    ChrTalk(
        0xFE,
        (
            "ふふ……\x01",
            "久しぶりにあなたみたいな子と\x01",
            "お話したかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "私の息子は外国で暮らしているけど……\x01",
            "あの子が小さかった頃を思い出すわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100C")

    Jump("loc_17F0")

    label("loc_1011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_10CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1097")

    #C0028
    ChrTalk(
        0xFE,
        (
            "クロスベルの７０年が\x01",
            "静かに過ぎてゆく……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "……今日はここで\x01",
            "景色でも眺めながら\x01",
            "過ごそうかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10C8")

    label("loc_1097")


    #C0030
    ChrTalk(
        0xFE,
        (
            "……今日はここで、\x01",
            "静かに過ごそうかしらね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C8")

    Jump("loc_17F0")

    label("loc_10CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_11D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1189")

    #C0031
    ChrTalk(
        0xFE,
        (
            "昨日の夜は賑やかな街を\x01",
            "ゆっくり歩いてみたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "ライトアップされた街並みが\x01",
            "とても綺麗だったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "ふふ……できればこの人と\x01",
            "一緒に歩きたかったものね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11D1")

    label("loc_1189")


    #C0034
    ChrTalk(
        0xFE,
        (
            "クロスベル市の綺麗な夜景……\x01",
            "出来ればこの人と\x01",
            "一緒に見たかったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D1")

    Jump("loc_17F0")

    label("loc_11D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1376")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CE")

    #C0035
    ChrTalk(
        0xFE,
        (
            "昨日、お祈りをしていたら\x01",
            "墓守のおじいさんと\x01",
            "話す機会があってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "ずっとここで祈り続けていたら、\x01",
            "折角の記念祭がもったいない……\x01",
            "そんな気がしてきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "今日の夜はゆっくり、\x01",
            "クロスベルの夜景を楽しんでくるわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1371")

    label("loc_12CE")


    #C0038
    ChrTalk(
        0xFE,
        (
            "ずっとここで祈り続けていたら、\x01",
            "折角の記念祭がもったいない……\x01",
            "そんな気がしてきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "ここで眠ってる夫には悪いけど……\x01",
            "今日はゆっくり楽しませてもらうわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1371")

    Jump("loc_17F0")

    label("loc_1376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1432")
    OP_93(0xFE, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1413")

    #C0040
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#0001F（熱心にお祈りしてるな……）\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#0108F（……邪魔をしては悪いわ。\x01",
            "  行きましょう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_142D")

    label("loc_1413")


    #C0043
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_142D")

    Jump("loc_17F0")

    label("loc_1432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_15CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1553")

    #C0044
    ChrTalk(
        0xFE,
        (
            "私の夫は、３０年前の紛争で\x01",
            "突然この世を去ったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "喧嘩して家を出て行ったあの人は\x01",
            "突然の戦闘に巻き込まれて……\x01",
            "私は死に目にも会えなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        "……あなた達にも、大事な人はいるでしょう？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "私みたいに、後悔がのこるような\x01",
            "付き合い方をしてはだめよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15C5")

    label("loc_1553")


    #C0048
    ChrTalk(
        0xFE,
        "……あなた達にも、大事な人はいるでしょう？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "私みたいに、後悔がのこるような\x01",
            "付き合い方をしてはだめよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_15C5")

    Jump("loc_17F0")

    label("loc_15CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_16CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1675")

    #C0050
    ChrTalk(
        0xFE,
        (
            "……私の夫は、３０年ほど前の\x01",
            "帝国と共和国の紛争に\x01",
            "巻き込まれてしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "喧嘩ばかりしてたけど、\x01",
            "こうなってしまうと\x01",
            "寂しいものね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16C9")

    label("loc_1675")


    #C0052
    ChrTalk(
        0xFE,
        (
            "３０年ほど前の\x01",
            "紛争のせいとはいえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "こうなってしまうと\x01",
            "寂しいものね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C9")

    Jump("loc_17F0")

    label("loc_16CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_17F0")
    OP_93(0xFE, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_177B")

    #C0054
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0055
    ChrTalk(
        0xFE,
        (
            "あ、あらごめんなさい。\x01",
            "気づかなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "お祈りを捧げていたものだから……\x01",
            "どうか許して頂戴ね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17F0")

    label("loc_177B")


    #C0057
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#0105F（熱心にお祈りしてる……）\x02\x03",

            "#0108F（……邪魔をしては悪いわ。\x01",
            "  行きましょう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F0")

    TalkEnd(0xFE)
    Return()

    # Function_4_962 end

    def Function_5_17F4(): pass

    label("Function_5_17F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1805")
    Jump("loc_1E0F")

    label("loc_1805")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1813")
    Jump("loc_1E0F")

    label("loc_1813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1821")
    Jump("loc_1E0F")

    label("loc_1821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1962")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B8")

    #C0059
    ChrTalk(
        0xFE,
        "墓を一通り掃除しておるんだ。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "これだけ墓があると、\x01",
            "放っておかれてしまうものも多いでな。\x01",
            "……嘆かわしいことだがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_195D")

    label("loc_18B8")


    #C0061
    ChrTalk(
        0xFE,
        (
            "これだけ墓があると、\x01",
            "放っておかれてしまうものも多い。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "それぞれ事情があるのだろうが……\x01",
            "魂はこの寂しい地で眠っておる。\x01",
            "たまには参りに来てやって欲しいのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_195D")

    Jump("loc_1E0F")

    label("loc_1962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1A06")

    #C0063
    ChrTalk(
        0xFE,
        (
            "……墓地になど、日曜学校の子供でも\x01",
            "あまり近づきたがらない場所なのだが……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)

    #C0064
    ChrTalk(
        0xFE,
        "ほっほっほ、お嬢さんは変わっておるな。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x153,
        "#1111Fほえー？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E0F")

    label("loc_1A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1BC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7F")

    #C0066
    ChrTalk(
        0xFE,
        "おや……見慣れない子供を連れているな。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x153,
        (
            "#1110Fねぇ、おじーさんは\x01",
            "こんなところでなにしてるの？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)

    #C0068
    ChrTalk(
        0xFE,
        (
            "ああ……この地に眠る者たちの\x01",
            "安らかなる眠りを妨げないように\x01",
            "見守っているのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "もっとも、今時墓荒らしのようなことは\x01",
            "滅多に起こらないがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x153,
        "#1106Fふーん……？\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "……ほっほっほ、すまんな。\x01",
            "お嬢さんにはまだ難しい話だったな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BC2")

    label("loc_1B7F")


    #C0072
    ChrTalk(
        0xFE,
        (
            "ほっほっほ、お嬢さんくらいの歳じゃ\x01",
            "墓守のことなど分かるまい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC2")

    Jump("loc_1E0F")

    label("loc_1BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1BD5")
    Jump("loc_1E0F")

    label("loc_1BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1C8E")

    #C0073
    ChrTalk(
        0xFE,
        (
            "不戦条約締結前には\x01",
            "数多くの命が失われていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "犠牲となったものたちの葬儀は\x01",
            "胸を締め付けられる思いだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "……もうあのような気分は\x01",
            "味わいたくないものだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E0F")

    label("loc_1C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C9C")
    Jump("loc_1E0F")

    label("loc_1C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CAA")
    Jump("loc_1E0F")

    label("loc_1CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D6C")

    #C0076
    ChrTalk(
        0xFE,
        "日曜学校のある日は救われる。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "この寂しい場所にいても\x01",
            "子供たちの楽しそうな声が\x01",
            "聞こえてくるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "授業が休みの日の墓地は、\x01",
            "それはそれは寂しいもんだぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DF3")

    label("loc_1D6C")


    #C0079
    ChrTalk(
        0xFE,
        (
            "日曜学校のある日は、\x01",
            "子供たちの楽しそうな声のおかげで\x01",
            "救われる想いだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "授業が休みの日の墓地は、\x01",
            "それはそれは寂しいもんだぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF3")

    Jump("loc_1E0F")

    label("loc_1DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1E06")
    Jump("loc_1E0F")

    label("loc_1E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1E0F")

    label("loc_1E0F")

    TalkEnd(0xFE)
    Return()

    # Function_5_17F4 end

    def Function_6_1E13(): pass

    label("Function_6_1E13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9E")

    #C0081
    ChrTalk(
        0xFE,
        (
            "お墓がいっぱいの所に\x01",
            "入り込んじゃったけど……\x01",
            "ここ、すごく眺めがいいね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "やっぱり、高いところはいいなぁ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1EE9")

    label("loc_1E9E")


    #C0083
    ChrTalk(
        0xFE,
        (
            "ここ、眺めがいいし\x01",
            "空気も澄んでるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "けっこういい場所かも～。\x02",
    )

    CloseMessageWindow()

    label("loc_1EE9")

    TalkEnd(0xFE)
    Return()

    # Function_6_1E13 end

    def Function_7_1EED(): pass

    label("Function_7_1EED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50013.itc", 0x1E)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis009.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis010.itp")
    Sleep(500)
    SetChrName("声")

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W──天に坐#2Rま#します我らが女神#4Rエイドス#よ。\x02\x03",

            "御身の元へ向かう魂のため、\x01",
            "天の門を開き賜#2Rたまわ#らんことを──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    PlayBGM("ed7534", 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1500)
    SetChrName("声")

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W（信じられないぜ……\x01",
            "  あの元気の塊みたいだったヤツが……）\x02\x03",

            "（可愛い恋人もいて\x01",
            "  そろそろ結婚かと思ってたのに\x01",
            "  ……どうしてこんな事に……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(150)
    SetChrName("声")

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W（クソ……！\x01",
            "  警察は何をやってるんだ！？）\x02\x03",

            "（身内が殺されたんだろう！？\x01",
            "  また迷宮入りにするつもりかよ！？）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(150)
    SetChrName("声")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W（たしか……\x01",
            "  ご両親は亡くされてるのよね？）\x02\x03",

            "（弟さん、どうするのかしら……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(800)
    SetChrName("女性")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W……大丈夫、ロイド？\x02\x03",

            "無理したらダメよ？\x01",
            "あまり寝ていないんでしょう？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0090
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W……セシル姉こそ。\x02\x03",

            "色々手伝ってもらってゴメン。\x01",
            "本当なら俺が一人で片付けなきゃ\x01",
            "いけなかったのに……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("女性")

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W……水臭いことを言わないで。\x01",
            "家族同然の付き合いじゃない。\x02\x03",

            "#40Wそれに……ガイさんのことは\x01",
            "私にとっても……\x02\x03",

            "#40W……………………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0092
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W………セシル姉………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("女性")

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W……ごめんね。\x01",
            "一番つらいのはロイドなのに。\x02\x03",

            "これから大変だと思うけど\x01",
            "遠慮なく頼ってちょうだいね……？\x02\x03",

            "あなたが一人立ちするまで、\x01",
            "ちゃんと見守らせてもらうから……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_68(11000, 1500, 18800, 0)
    MoveCamera(312, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrPos(0x101, -23000, 0, 24500, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x2)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -23000, 0, 25500, 0)
    MoveCamera(322, 13, 0, 6000)
    SetCameraDistance(37500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x50)
    Fade(1000)
    OP_68(-23300, 600, 21800, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(-23300, 600, 25800, 4000)
    SetCameraDistance(15500, 4000)
    OP_6F(0x11)

    #C0094
    ChrTalk(
        0x101,
        (
            "#6P#0008F……………………………………\x02\x03",

            "#0004F……はは。\x01",
            "我ながらガキだったんだな。\x02\x03",

            "素直に頼ればよかったのに\x01",
            "……変な意地を張ったりして……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x101, 0x1)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    Sound(46, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0095
    ChrTalk(
        0x101,
        (
            "#6P#0003F（──兄貴、ただいま。）\x02\x03",

            "#0008F（今まで顔を見せなくてゴメン。\x01",
            "  少し、意地を張ってたみたいだ。）\x02\x03",

            "#0002F（でも俺……帰ってきたから。）\x02\x03",

            "（兄貴と同じ捜査官として\x01",
            "  クロスベルに戻ってきたから。）\x02\x03",

            "#0004F（一人前には程遠いし……\x01",
            "  ……なんか変な部署に\x01",
            "  配属されちゃったけど……）\x02\x03",

            "#0000F（まあ、何とか頑張るから\x01",
            "  せいぜい見守っててくれよな。）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1EED end

    def Function_8_2751(): pass

    label("Function_8_2751")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "鐘の下より生まれし子羊たちよ\x01",
            "  どうか安らかに眠りたまえ\x02",
        )
    )

    CloseMessageWindow()

    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            " 純白の雲間から差す黄金の陽光が\x01",
            "蒼き大空へと続く一筋の道となりて\x01",
            "    魂を女神の元へと導かん\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_2751 end

    def Function_9_2826(): pass

    label("Function_9_2826")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            " 　　　ガイ・バニングス\x01",
            "　　　　　ここに眠る\x01",
            "───────────────\x01",
            "　Ｓ１１７６　～　Ｓ１２０１　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28FD")

    #C0099
    ChrTalk(
        0x101,
        "#6P#0008F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_28FD")

    TalkEnd(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C6F")
    Sleep(150)
    EventBegin(0x0)
    StopBGM(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    SetChrPos(0x101, -22900, 0, 24540, 0)
    SetChrPos(0x102, -23050, 0, 21800, 0)
    SetChrPos(0x103, -21380, 0, 22100, 350)
    SetChrPos(0x104, -24580, 0, 22100, 0)
    OP_68(-22960, 2500, 24900, 0)
    MoveCamera(334, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(14810, 0)
    Sleep(10)
    PlayBGM("ed7001", 0)
    FadeToBright(1000, 0)
    OP_68(-22960, 1500, 24900, 3000)
    OP_0D()
    OP_6F(0x79)

    #C0100
    ChrTalk(
        0x101,
        (
            "#6P#0003F（兄貴のバッジ……\x01",
            "  ようやく取り戻したよ。）\x02\x03",

            "（……これでやっと\x01",
            "  兄貴の敵討ちができる……）\x02\x03",

            "#0008F（でもゴメン、今は目の前の\x01",
            "  事件に集中させてくれ。）\x02\x03",

            "（薬物被害に市民の失踪……\x01",
            "  今までにない大きな事件が\x01",
            "  クロスベルで起きようとしている。）\x02\x03",

            "#0001F（兄貴も絶対に\x01",
            "  見過ごせないだろうからさ……）\x02\x03",

            "#0004F（……まだまだ半人前だけど\x01",
            "  エリィやティオ、ランディ……\x01",
            "  心強い仲間たちがいる。）\x02\x03",

            "（それと……何があっても\x01",
            "  守りたい存在が出来たんだ。）\x02\x03",

            "#0000F（だから兄貴……\x01",
            "  どうか安心して見ててくれ！）\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        "#0105F……ロイド？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        "#0300Fハハ……どうした？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0103
    ChrTalk(
        0x101,
        (
            "#0004F#11P……ああ、なんでもないんだ。\x02\x03",

            "#0000Fさぁみんな……行こう！\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x103,
        "#0202F#2P………はい……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0xE7, 1)
    EventEnd(0x5)

    label("loc_2C6F")

    Return()

    # Function_9_2826 end

    def Function_10_2C70(): pass

    label("Function_10_2C70")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0105
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　 サヤ・マクレイン\x01",
            "　　　　　ここに眠る\x01",
            "───────────────\x01",
            "　Ｓ１１７５　～　Ｓ１１９９　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_10_2C70 end

    def Function_11_2D16(): pass

    label("Function_11_2D16")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0106
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            " 　………………　……　　　　　\x01",
            " 　……　……………………\x01",
            "　　　　　こ……眠……\x01",
            "───────────────……\x01",
            "　Ｓ１………　～　Ｓ１…８…　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF0")
    SetScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 0)

    label("loc_2DF0")

    TalkEnd(0xFF)
    Return()

    # Function_11_2D16 end

    def Function_12_2DF4(): pass

    label("Function_12_2DF4")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(4760, 5200, 45880, 0)
    MoveCamera(339, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19410, 0)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, 7090, 4000, 45490, 320)
    SetChrPos(0x102, 5840, 4000, 45440, 320)
    SetChrPos(0x103, 6560, 4000, 43510, 320)
    SetChrPos(0x104, 5070, 4000, 43640, 320)
    FadeToBright(500, 0)
    OP_0D()

    #C0107
    ChrTalk(
        0x104,
        (
            "#6P#0305Fおっとと……あぶねえな。\x01",
            "柵もなにも無ぇじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#12P#0003Fこんなガケ、まず誰も\x01",
            "立たないだろうからなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        (
            "#6P#0105Fここから見える谷底……\x01",
            "相当深いみたい。\x02\x03",

            "#0103Fじーっと見てると、\x01",
            "なんだか吸い込まれそうに\x01",
            "なるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        (
            "#12P#0200Fこの場所は墓地……\x01",
            "死者の眠る場所です。\x02\x03",

            "#0204Fもしかしたら、\x01",
            "向こう側から誰かが手招きを\x01",
            "しているのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#6P#0105Fティ、ティオちゃんったら。\x01",
            "怖いこと言わないでよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#12P#0003Fと、とにかく。\x02\x03",

            "#0000Fグレイスさんに依頼された写真、\x01",
            "ここならいいものが撮れそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36E1")
    TurnDirection(0x101, 0x102, 500)

    #C0113
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれじゃあエリィ、\x01",
            "撮影をお願いできるかな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0114
    ChrTalk(
        0x102,
        (
            "#6P#0108Fえ、ええ。\x01",
            "ちょっと自信はないけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0115
    ChrTalk(
        0x104,
        (
            "#6P#0300Fいやいや、大丈夫だろ。\x02\x03",

            "ちょっとレンズを覗いて\x01",
            "パチリと撮っちまえば\x01",
            "終わりじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0116
    ChrTalk(
        0x102,
        (
            "#6P#0103Fあのねぇ……\x01",
            "いい写真を撮るのは\x01",
            "そんな簡単なことじゃないのよ。\x02\x03",

            "#0100Fフレームの中に\x01",
            "対象物をどう収めるか、\x01",
            "構成を練らなきゃいけないし……\x02\x03",

            "天気や風の影響で\x01",
            "写真の印象もガラリと変わってしまう。\x02\x03",

            "ある一瞬を逃したら\x01",
            "二度と撮れないことだって\x01",
            "あるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        (
            "#12P#0200F素人とプロの写真を見比べると\x01",
            "一目で違いが分かりますからね。\x02\x03",

            "#0203F粗雑な人には、その繊細さが\x01",
            "理解できないかも知れませんが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0118
    ChrTalk(
        0x104,
        (
            "#6P#0306Fぐっ……\x01",
            "誰のことを言ってんだ、誰の。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#12P#0000Fま、まぁまぁ。\x01",
            "ここはエリィに任せてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        (
            "#6P#0100Fそれじゃあ……\x01",
            "やってみるわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x12C, 0x1F4)
    OP_93(0x101, 0x12C, 0x1F4)
    OP_93(0x103, 0x12C, 0x1F4)
    OP_93(0x104, 0x12C, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0121
    ChrTalk(
        0x102,
        (
            "#6P#0103F……ふぅ。\x01",
            "念のため何枚か撮っておいたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#12P#0000Fどうやら撮れたみたいだな。\x02\x03",

            "出来栄えはどんな感じだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        (
            "#6P#0100F実際に現像してみないと\x01",
            "分からないけど……\x02\x03",

            "少なくとも、\x01",
            "悪い写真ではないとは思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        (
            "#12P#0200Fエリィさんも\x01",
            "カンを取り戻せたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        (
            "#6P#0300Fふーん……\x01",
            "俺にはさっぱりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#12P#0000Fまたこういう場所を見つけたら\x01",
            "写真に収めていこう。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A30")

    label("loc_36E1")

    TurnDirection(0x101, 0x102, 500)

    #C0127
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれじゃあ……\x01",
            "エリィ、撮影を頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x102,
        "#6P#0100Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x12C, 0x1F4)
    OP_93(0x101, 0x12C, 0x1F4)
    OP_93(0x103, 0x12C, 0x1F4)
    OP_93(0x104, 0x12C, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0129
    ChrTalk(
        0x102,
        (
            "#6P#0103F……ふぅ。\x01",
            "こんなところかしら。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_3878")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3878")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_388F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_388F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_38A6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_38A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_38BD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_38BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_38D4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_38D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_38EB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_38EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_3902")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3902")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_3919")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3919")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_3930")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3930")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39DB")

    #C0130
    ChrTalk(
        0x101,
        (
            "#12P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "これでグレイスさんに提示された\x01",
            "５枚ってノルマは達成できた。\x01",
            "これでいつでも提出できそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A30")

    label("loc_39DB")


    #C0131
    ChrTalk(
        0x101,
        (
            "#12P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A30")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5840, 4000, 45440, 320)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x5)
    Sleep(500)
    OP_65(0x2, 0x1)
    EventEnd(0x5)
    Return()

    # Function_12_2DF4 end

    def Function_13_3A66(): pass

    label("Function_13_3A66")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(21970, 1500, 30960, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 21500, 0, 30200, 0)
    SetChrPos(0x102, 20300, 0, 30200, 0)
    SetChrPos(0x103, 21500, 0, 29000, 0)
    SetChrPos(0x104, 20300, 0, 29000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B0F")
    SetChrPos(0x10A, 22710, 0, 29860, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_3B0F")

    SetChrPos(0x9, 20830, 0, 32299, 0)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    OP_4B(0x9, 0xFF)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xB, 0x2)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -23000, 0, 25500, 0)
    SetCameraDistance(16000, 3000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    Sound(46, 0, 100, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0132
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　 サヤ・マクレイン\x01",
            "　　　　　ここに眠る\x01",
            "───────────────\x01",
            "　Ｓ１１７５　～　Ｓ１１９９　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0133
    ChrTalk(
        0x101,
        "#6P#0005F（この墓は……）\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        "#6P#0105F（アリオスさんの奥様の……？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C9A")

    #C0135
    ChrTalk(
        0x10A,
        "#12P#0608F（……………………）\x02",
    )

    CloseMessageWindow()

    label("loc_3C9A")

    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0136
    ChrTalk(
        0x9,
        "#11P……次はこっちだ。\x02",
    )

    CloseMessageWindow()

    def lambda_3CD3():
        OP_95(0xFE, 24000, 0, 32299, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3CD3)
    WaitChrThread(0x9, 1)

    def lambda_3CF1():
        OP_95(0xFE, 24000, 0, 29000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3CF1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x9, 1)
    OP_68(13470, 5500, 33550, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16200, 0)
    SetChrPos(0x101, 13200, 4000, 33300, 0)
    SetChrPos(0x102, 12000, 4000, 33300, 0)
    SetChrPos(0x103, 13200, 4000, 32100, 0)
    SetChrPos(0x104, 12000, 4000, 32100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DA8")
    SetChrPos(0x10A, 14210, 4000, 32460, 0)

    label("loc_3DA8")

    SetChrPos(0x9, 12330, 4000, 35000, 0)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    OP_4B(0x9, 0xFF)
    SetChrSubChip(0x9, 0x0)
    SetCameraDistance(15200, 3000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Sound(46, 0, 100, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0137
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            " 　………………　……　　　　　\x01",
            " 　……　……………………\x01",
            "　　　　　こ……眠……\x01",
            "───────────────……\x01",
            "　Ｓ１………　～　Ｓ１…８…　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0138
    ChrTalk(
        0x104,
        (
            "#6P#0303F（えらくボロい墓だな……\x01",
            "  名前なんかほとんど潰れちまってる。）\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x103,
        "#6P#0200F（知り合い……なのでしょうか。）\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        "#11P……次で最後だ。\x02",
    )

    CloseMessageWindow()

    def lambda_3F5D():
        OP_95(0xFE, 10300, 4000, 35000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3F5D)
    WaitChrThread(0x9, 1)

    def lambda_3F7B():
        OP_95(0xFE, 10300, 4000, 33300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3F7B)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x9, 1)
    OP_68(-21390, 1500, 21840, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -21500, 0, 21800, 0)
    SetChrPos(0x102, -22700, 0, 21800, 0)
    SetChrPos(0x103, -21500, 0, 20600, 0)
    SetChrPos(0x104, -22700, 0, 20600, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4032")
    SetChrPos(0x10A, -20400, 0, 20980, 0)

    label("loc_4032")

    SetChrPos(0x9, -22460, 0, 23700, 0)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    OP_4B(0x9, 0xFF)
    SetChrSubChip(0x9, 0x0)
    SetCameraDistance(16000, 3000)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(1000)
    OP_6F(0x79)

    #C0141
    ChrTalk(
        0x101,
        "#6P#0005Fこ、ここは……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    Sound(46, 0, 100, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0142
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            " 　　　ガイ・バニングス\x01",
            "　　　　　ここに眠る\x01",
            "───────────────\x01",
            "　Ｓ１１７６　～　Ｓ１２０１　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0143
    ChrTalk(
        0x104,
        "#5P#0305Fもしかして、ここは……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x102,
        "#5P#0105Fロイドのお兄様の……\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x103,
        "#6P#0208F……………………\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        "#11P……君たちに３色の花を頼んだ理由……\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "#11Pそれは、ガイ・バニングスに……\x01",
            "そして、彼が大切にしていた人々に\x01",
            "供えるためだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            "#11P大事な友人たちの墓なのだ……\x01",
            "葬儀だろうがなんだろうが、\x01",
            "最大の敬意を表すのが当然だろう？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_431A")

    #C0149
    ChrTalk(
        0x10A,
        (
            "#12P#0603F……ご老人。\x01",
            "あの男を知っているのですね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_435B")

    label("loc_431A")


    #C0150
    ChrTalk(
        0x101,
        (
            "#6P#0005Fお爺さん……\x01",
            "ガイ・バニングスを\x01",
            "知ってるんですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435B")

    OP_93(0x9, 0xB4, 0x1F4)

    #C0151
    ChrTalk(
        0x9,
        (
            "#11Pああ、知っているとも。\x01",
            "忘れるわけがない。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x9,
        (
            "#11Pガイは生きていた頃、\x01",
            "よく墓守小屋に遊びに来ていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        (
            "#11P何度も酒を酌み交わした\x01",
            "飲み仲間なんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        (
            "#11P家族のいない私は、\x01",
            "何度心を救われたことか分からんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#6P#0003Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        "#6P#0203F……分かる気がします。\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        (
            "#11P……その分、やつの葬儀のときは\x01",
            "身を裂かれる思いだったがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        (
            "#11Pロイド……と言ったか。\x01",
            "お前はガイの弟なのだろう？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0159
    ChrTalk(
        0x101,
        "#6P#0005Fお、俺のことも知ってるんですか？\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x9,
        "#11Pガイの葬儀で一度見かけていたからな。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x9,
        (
            "#11P４ヶ月前のクロスベルタイムズに\x01",
            "写真が載っていたのを見て\x01",
            "それを思い出したのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x9,
        (
            "#11Pふふ、顔は似ていないが\x01",
            "こうして見ると面影があるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#6P#0012Fはは……\x01",
            "まだ足元にも及びませんけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x102,
        "#5P#0108Fロイド……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x9,
        (
            "#11P……今回、３色の花を集めろなどという\x01",
            "面倒な依頼を出した理由はもう一つある。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "#11Pガイの後輩であるお前たちが育っているか、\x01",
            "この目で確かめたかったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x104,
        (
            "#5P#0300Fそんで……\x01",
            "俺たちは合格なのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x9,
        (
            "#11P任務はこなしたが……\x01",
            "あらゆる面で荒削りで\x01",
            "一人前とは言いがたかろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        "#5P#0306Fズ、ズバっと言いやがって……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47FB")

    #C0170
    ChrTalk(
        0x10A,
        "#12P#0603F……ヒヨッコには当然の評価だ。\x02",
    )

    CloseMessageWindow()

    label("loc_47FB")


    #C0171
    ChrTalk(
        0x9,
        (
            "#11Pほっほっほ、だが……\x01",
            "お前たち若い者には未来がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x9,
        (
            "#11Pいつかガイに追いつき、\x01",
            "追い越すこともできるかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        (
            "#11Pそうなったら……\x01",
            "ここに遊びに来い。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x9,
        (
            "#11Pかつてのガイのように、\x01",
            "一緒に酒でも飲もうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        (
            "#6P#0004F……ええ、そうですね。\x01",
            "楽しみにしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x102,
        (
            "#5P#0100Fロイド……\x01",
            "あなたのお兄様は\x01",
            "色んな人々の中で生きてるのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x103,
        (
            "#6P#0202F……ですね。\x02\x03",

            "#0204F（そう、わたしの中にも……）\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x104,
        (
            "#5P#0306F追いつくにはちょっとばかし\x01",
            "時間が掛かりそうな目標だよな。\x02\x03",

            "#0309Fある意味、マフィアだの\x01",
            "歪んだ体制だのよりも\x01",
            "よっぽど大きな壁かもしれねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#6P#0004Fああ……そう思うよ。\x02\x03",

            "#0001F（それでも、いつか……\x01",
            "  いつか乗り越えていかないとな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x9,
        (
            "#11Pふふ、喋りすぎたようだ。\x01",
            "そろそろ中に戻るとしよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("t4020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_3A66 end

    SaveToFile()

Try(main)
