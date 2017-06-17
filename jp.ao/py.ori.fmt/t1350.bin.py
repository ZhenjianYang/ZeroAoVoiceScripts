from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1350.bin",                # FileName
        "t1350",                    # MapName
        "t1350",                    # Location
        0x00B8,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 184, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1350",                  # 0
        "エリィ",                 # 1
        "ティオ",                 # 2
        "ランディ",               # 3
        "キーア",                 # 4
        "フラン",                 # 5
        "イリア",                 # 6
        "リーシャ",               # 7
        "シュリ",                 # 8
        "メルスン",               # 9
        "コロナ",                 # 10
        "リマ",                   # 11
        "ＭＷＬスタッフ",         # 12
        "観光客",                 # 13
        "観光客",                 # 14
        "観光客",                 # 15
        "観光客",                 # 16
        "ダミー",                 # 17
        "みーしぇ",               # 18
        "ワンダーランド入口広場方面",# 19
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch00300.itc",                   # 02
        "chr/ch08200.itc",                   # 03
        "chr/ch08500.itc",                   # 04
        "chr/ch05100.itc",                   # 05
        "chr/ch05200.itc",                   # 06
        "chr/ch10100.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch22700.itc",                   # 09
        "chr/ch20700.itc",                   # 0A
        "chr/ch25900.itc",                   # 0B
        "chr/ch20400.itc",                   # 0C
        "chr/ch23700.itc",                   # 0D
        "chr/ch21000.itc",                   # 0E
        "chr/ch24600.itc",                   # 0F
        "chr/ch45400.itc",                   # 10
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

    DeclNpc(-1500,   0,       -2299,   270,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-2599,   0,       -9300,   350,  389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-2500,   0,       -2299,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-2910,   0,       -4469,   45,   389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-1669,   0,       -9319,   350,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-2930,   0,       -4030,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-2049,   0,       -4869,   315,  389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-1759,   0,       -4469,   315,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-2910,   0,       -3269,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-1759,   0,       -3269,   225,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-2309,   0,       -4469,   0,    389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       800,     2250,    180,  389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-1549,   -4000,   -24340,  90,   389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-550,    -4000,   -24340,  270,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3019,    0,       -4440,   125,  389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(3670,    0,       -5219,   305,  389,  0x0, 0,   15,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-6000,   0,       -3170,   270,  389,  0x0, 0,   16,  0,   0,   0,   0,   25,  255,  0)

    DeclActor(-5620,   0,       2730,    1200,    -5620,   2000,    2730,    0x007C, 0,  26, 0x0000)

    PlaceName(-0.17000000178813934, 0.0, -65.44999694824219, 0x0000, 0x0000, "ワンダーランド入口広場方面")

    ChipFrameInfo(936, 0)                                        # 0

    ScpFunction((
        "Function_0_3A8",          # 00, 0
        "Function_1_460",          # 01, 1
        "Function_2_4F1",          # 02, 2
        "Function_3_531",          # 03, 3
        "Function_4_624",          # 04, 4
        "Function_5_716",          # 05, 5
        "Function_6_7FD",          # 06, 6
        "Function_7_8D3",          # 07, 7
        "Function_8_9F4",          # 08, 8
        "Function_9_BA3",          # 09, 9
        "Function_10_D01",         # 0A, 10
        "Function_11_DA0",         # 0B, 11
        "Function_12_E66",         # 0C, 12
        "Function_13_EF7",         # 0D, 13
        "Function_14_FC4",         # 0E, 14
        "Function_15_1101",        # 0F, 15
        "Function_16_11F4",        # 10, 16
        "Function_17_12E0",        # 11, 17
        "Function_18_1347",        # 12, 18
        "Function_19_13DB",        # 13, 19
        "Function_20_146B",        # 14, 20
        "Function_21_15CA",        # 15, 21
        "Function_22_2B94",        # 16, 22
        "Function_23_2BBD",        # 17, 23
        "Function_24_2BE6",        # 18, 24
        "Function_25_3B44",        # 19, 25
        "Function_26_4228",        # 1A, 26
    ))


    def Function_0_3A8(): pass

    label("Function_0_3A8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3E8"),
        (1, "loc_3F4"),
        (2, "loc_400"),
        (3, "loc_40C"),
        (4, "loc_418"),
        (5, "loc_424"),
        (6, "loc_430"),
        (SWITCH_DEFAULT, "loc_43C"),
    )


    label("loc_3E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_3F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_400")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_40C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_418")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_424")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_430")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_43C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_448")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_45F")

    Return()

    # Function_0_3A8 end

    def Function_1_460(): pass

    label("Function_1_460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_46F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 24)

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_47D")
    Jump("loc_4F0")

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_48B")
    Jump("loc_4F0")

    label("loc_48B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_499")
    Jump("loc_4F0")

    label("loc_499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_4AA")
    Call(0, 20)
    Jump("loc_4F0")

    label("loc_4AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4BD")
    ClearChrFlags(0x13, 0x80)
    Jump("loc_4F0")

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4CB")
    Jump("loc_4F0")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4D9")
    Jump("loc_4F0")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4E7")
    Jump("loc_4F0")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_4F0")

    label("loc_4F0")

    Return()

    # Function_1_460 end

    def Function_2_4F1(): pass

    label("Function_2_4F1")

    ClearMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)

    label("loc_52A")

    Sound(944, 0, 100, 0)
    Return()

    # Function_2_4F1 end

    def Function_3_531(): pass

    label("Function_3_531")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54A")
    Jump("loc_620")

    label("loc_54A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D")
    Call(0, 19)
    Jump("loc_5DE")

    label("loc_56D")


    #C0001
    ChrTalk(
        0x8,
        (
            "#00106Fはあ……\x01",
            "苦手なのよね、こういうの。\x02\x03",

            "#00111Fもしかしたら\x01",
            "ベルが私を脅かすためだけに\x01",
            "作ったのかも……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DE")

    Jump("loc_620")

    label("loc_5E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F9")
    Jump("loc_620")

    label("loc_5F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60F")
    Jump("loc_620")

    label("loc_60F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_620")

    label("loc_620")

    TalkEnd(0xFE)
    Return()

    # Function_3_531 end

    def Function_4_624(): pass

    label("Function_4_624")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63D")
    Jump("loc_712")

    label("loc_63D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_653")
    Jump("loc_712")

    label("loc_653")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_669")
    Jump("loc_712")

    label("loc_669")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_701")

    #C0002
    ChrTalk(
        0x9,
        (
            "#00203Fここからでも、絶叫や悲鳴が\x01",
            "はっきりと聞こえてきますね。\x02\x03",

            "#00204Fああいうのを聞くと、\x01",
            "怖いと同時にワクワクしてきます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_712")

    label("loc_701")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_712")

    label("loc_712")

    TalkEnd(0xFE)
    Return()

    # Function_4_624 end

    def Function_5_716(): pass

    label("Function_5_716")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72F")
    Jump("loc_7F9")

    label("loc_72F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_752")
    Call(0, 19)
    Jump("loc_7B7")

    label("loc_752")


    #C0003
    ChrTalk(
        0xA,
        (
            "#00309Fハハ、お嬢も怖がりだよなあ。\x02\x03",

            "#00304Fまあ、こういうタイプほど\x01",
            "乗せてみたくなるもんだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B7")

    Jump("loc_7F9")

    label("loc_7BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D2")
    Jump("loc_7F9")

    label("loc_7D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E8")
    Jump("loc_7F9")

    label("loc_7E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F9")

    label("loc_7F9")

    TalkEnd(0xFE)
    Return()

    # Function_5_716 end

    def Function_6_7FD(): pass

    label("Function_6_7FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_816")
    Jump("loc_8CF")

    label("loc_816")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82C")
    Jump("loc_8CF")

    label("loc_82C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_842")
    Jump("loc_8CF")

    label("loc_842")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_858")
    Jump("loc_8CF")

    label("loc_858")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CF")

    #C0004
    ChrTalk(
        0xB,
        (
            "#01106Fキーアも最後は何がいいか\x01",
            "考え中だけど……\x02\x03",

            "#01109Fイリアと一緒に乗るのも\x01",
            "楽しそうだねー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CF")

    TalkEnd(0xFE)
    Return()

    # Function_6_7FD end

    def Function_7_8D3(): pass

    label("Function_7_8D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EC")
    Jump("loc_9F0")

    label("loc_8EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_902")
    Jump("loc_9F0")

    label("loc_902")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_918")
    Jump("loc_9F0")

    label("loc_918")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DF")

    #C0005
    ChrTalk(
        0xC,
        (
            "#06402Fこのアトラクションの建物は、\x01",
            "ミシュラムにもともとあった屋敷を\x01",
            "ＩＢＣが改築した物らしいです。\x02\x03",

            "#06409Fいやー、相当本格的ですよね～。\x01",
            "なんだかため息が出ちゃいますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F0")

    label("loc_9DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F0")

    label("loc_9F0")

    TalkEnd(0xFE)
    Return()

    # Function_7_8D3 end

    def Function_8_9F4(): pass

    label("Function_8_9F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7A")

    #C0006
    ChrTalk(
        0xD,
        (
            "#01702Fヒュウ♪\x01",
            "雰囲気出てるわね～！\x02\x03",

            "#01709Fうーん、ワクワクしてきた。\x01",
            "早く乗りたいわ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_AB4")

    label("loc_A7A")


    #C0007
    ChrTalk(
        0xD,
        (
            "#01709Fうーん、ワクワクしてきた。\x01",
            "早く乗りたいわ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB4")

    Jump("loc_B9F")

    label("loc_AB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACF")
    Jump("loc_B9F")

    label("loc_ACF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE5")
    Jump("loc_B9F")

    label("loc_AE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFB")
    Jump("loc_B9F")

    label("loc_AFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9F")

    #C0008
    ChrTalk(
        0xD,
        (
            "#01702F最後だし、どうせなら\x01",
            "スカッとするヤツに乗らない？\x02\x03",

            "#01700Fあんたたちだけだと\x01",
            "制限に引っかかるだろうけど、\x01",
            "あたしがいれば大丈夫でしょ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9F")

    TalkEnd(0xFE)
    Return()

    # Function_8_9F4 end

    def Function_9_BA3(): pass

    label("Function_9_BA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C56")

    #C0009
    ChrTalk(
        0xE,
        (
            "#01805Fあっちに見えるのって……\x01",
            "もしかして乗り物の\x01",
            "コースでしょうか？\x02\x03",

            "#01806Fあんな風に外に出てるなんて、\x01",
            "相当スリルがありそうですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CA5")

    label("loc_C56")


    #C0010
    ChrTalk(
        0xE,
        (
            "#01802Fコースがあんな風に\x01",
            "外に出てるなんて、\x01",
            "相当スリルがありそうですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA5")

    Jump("loc_CFD")

    label("loc_CAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC0")
    Jump("loc_CFD")

    label("loc_CC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD6")
    Jump("loc_CFD")

    label("loc_CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEC")
    Jump("loc_CFD")

    label("loc_CEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFD")

    label("loc_CFD")

    TalkEnd(0xFE)
    Return()

    # Function_9_BA3 end

    def Function_10_D01(): pass

    label("Function_10_D01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1A")
    Jump("loc_D9C")

    label("loc_D1A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D30")
    Jump("loc_D9C")

    label("loc_D30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D46")
    Jump("loc_D9C")

    label("loc_D46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5C")
    Jump("loc_D9C")

    label("loc_D5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9C")

    #C0011
    ChrTalk(
        0xF,
        "#14006Fんー、オレは別に何でもいいけど……\x02",
    )

    CloseMessageWindow()

    label("loc_D9C")

    TalkEnd(0xFE)
    Return()

    # Function_10_D01 end

    def Function_11_DA0(): pass

    label("Function_11_DA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB9")
    Jump("loc_E62")

    label("loc_DB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCF")
    Jump("loc_E62")

    label("loc_DCF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3B")

    #C0012
    ChrTalk(
        0x10,
        (
            "ふう……\x01",
            "物凄いスリルだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x10,
        (
            "でも、リマにいい所を\x01",
            "見せられてよかったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E62")

    label("loc_E3B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E51")
    Jump("loc_E62")

    label("loc_E51")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E62")

    label("loc_E62")

    TalkEnd(0xFE)
    Return()

    # Function_11_DA0 end

    def Function_12_E66(): pass

    label("Function_12_E66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7F")
    Jump("loc_EF3")

    label("loc_E7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E95")
    Jump("loc_EF3")

    label("loc_E95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECC")

    #C0014
    ChrTalk(
        0x11,
        (
            "ふふ……\x01",
            "お疲れ様、あなた。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF3")

    label("loc_ECC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE2")
    Jump("loc_EF3")

    label("loc_EE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF3")

    label("loc_EF3")

    TalkEnd(0xFE)
    Return()

    # Function_12_E66 end

    def Function_13_EF7(): pass

    label("Function_13_EF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F10")
    Jump("loc_FC0")

    label("loc_F10")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F26")
    Jump("loc_FC0")

    label("loc_F26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F99")

    #C0015
    ChrTalk(
        0x12,
        "パパ、すっごくかっこよかったの。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x12,
        (
            "モンスターをたっくさん\x01",
            "やっつけてくれたんだよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC0")

    label("loc_F99")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAF")
    Jump("loc_FC0")

    label("loc_FAF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC0")

    label("loc_FC0")

    TalkEnd(0xFE)
    Return()

    # Function_13_EF7 end

    def Function_14_FC4(): pass

    label("Function_14_FC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10FD")
    TalkBegin(0xFE)

    #C0017
    ChrTalk(
        0xFE,
        (
            "ホラーコースター、人呼んで\x01",
            "《ルナティックゾーン》へようこそ……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "こちらは、モンスターの住まう館を\x01",
            "たった一丁の導力銃で駆け抜ける、\x01",
            "恐怖のアトラクションでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00003F（みーしぇとかくれんぼ中だし……\x01",
            "　今アトラクションで遊ぶのは\x01",
            "　やめておくとしよう。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1100")

    label("loc_10FD")

    Call(0, 21)

    label("loc_1100")

    Return()

    # Function_14_FC4 end

    def Function_15_1101(): pass

    label("Function_15_1101")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118A")
    OP_4B(0x15, 0xFF)

    #C0020
    ChrTalk(
        0x14,
        (
            "ハ、ハハハ、ハ……\x01",
            "怖いなんてこと、\x01",
            "あるわけないじゃないか……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x15,
        "（明らかに怖がってるわね……）\x02",
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    Jump("loc_11F0")

    label("loc_118A")


    #C0022
    ChrTalk(
        0x14,
        (
            "何度も乗ってるうちに、\x01",
            "怖いのを通り越して\x01",
            "楽しくなってきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x14,
        "ハハハ、さあもう一度乗ろう！\x02",
    )

    CloseMessageWindow()

    label("loc_11F0")

    TalkEnd(0xFE)
    Return()

    # Function_15_1101 end

    def Function_16_11F4(): pass

    label("Function_16_11F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1248")

    #C0024
    ChrTalk(
        0x15,
        (
            "大丈夫？　イヤだったら\x01",
            "無理して乗らなくてもいいけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DC")

    label("loc_1248")


    #C0025
    ChrTalk(
        0x15,
        (
            "彼ったら調子に乗っちゃって\x01",
            "何度もホラーコースターに\x01",
            "乗ろうとするのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x15,
        (
            "はあ、ほかにももっと\x01",
            "色々なアトラクションを\x01",
            "遊びたいんだけどなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12DC")

    TalkEnd(0xFE)
    Return()

    # Function_16_11F4 end

    def Function_17_12E0(): pass

    label("Function_17_12E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1343")

    #C0027
    ChrTalk(
        0x16,
        (
            "いやー、叫んだ叫んだ！\x01",
            "絶叫系のアトラクションは\x01",
            "やっぱり楽しいねえ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1343")

    label("loc_1343")

    TalkEnd(0xFE)
    Return()

    # Function_17_12E0 end

    def Function_18_1347(): pass

    label("Function_18_1347")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D7")

    #C0028
    ChrTalk(
        0x17,
        (
            "お父さんったら、\x01",
            "銃で撃つのも忘れて\x01",
            "叫んでばっかりだったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x17,
        (
            "次に乗るときは\x01",
            "僕が銃を撃たせてもらおうっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D7")

    label("loc_13D7")

    TalkEnd(0xFE)
    Return()

    # Function_18_1347 end

    def Function_19_13DB(): pass

    label("Function_19_13DB")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0030
    ChrTalk(
        0xA,
        (
            "#00309Fよっしゃ、お嬢。\x01",
            "さっそく入るとしようぜ～♪\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#00106Fちょ、ちょっと待って。\x01",
            "もう少し心の準備を……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_19_13DB end

    def Function_20_146B(): pass

    label("Function_20_146B")

    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B3")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_15C9")

    label("loc_14B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DD")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    Jump("loc_15C9")

    label("loc_14DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1507")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_15C9")

    label("loc_1507")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157F")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_155F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_1551")
    SetChrFlags(0x9, 0x80)
    Jump("loc_155F")

    label("loc_1551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_155F")
    SetChrFlags(0xC, 0x80)

    label("loc_155F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157A")
    ClearChrFlags(0x19, 0x80)

    label("loc_157A")

    Jump("loc_15C9")

    label("loc_157F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C9")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -2310, 0, -3270, 180)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_15C9")

    Return()

    # Function_20_146B end

    def Function_21_15CA(): pass

    label("Function_21_15CA")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1800, 1650, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(10500, 0)
    OP_4B(0x13, 0xFF)
    SetChrPos(0x101, 0, 800, 1000, 0)
    Call(0, 22)
    OP_0D()

    #C0032
    ChrTalk(
        0x13,
        (
            "ホラーコースター、人呼んで\x01",
            "《ルナティックゾーン》へようこそ……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x13,
        (
            "こちらは、モンスターの住まう館を\x01",
            "たった一丁の導力銃で駆け抜ける、\x01",
            "恐怖のアトラクションでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x13,
        (
            "よろしければ、どなたかとご一緒に\x01",
            "ご入場される事をおすすめしますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#00004F#6P（……誰を誘おうかな？）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K誰を誘う？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "エリィ")
    MenuCmd(1, 0, "ティオ")
    MenuCmd(1, 0, "ランディ")
    MenuCmd(1, 0, "ノエル")
    MenuCmd(1, 0, "ワジ")
    MenuCmd(1, 0, "キーア")
    MenuCmd(1, 0, "フラン")
    MenuCmd(1, 0, "セシル")
    MenuCmd(1, 0, "イリア")
    MenuCmd(1, 0, "リーシャ")
    MenuCmd(1, 0, "シュリ")
    MenuCmd(1, 0, "やめる")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1801")
    MenuCmd(3, 0, 0x0)

    label("loc_1801")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1813")
    MenuCmd(3, 0, 0x1)

    label("loc_1813")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1825")
    MenuCmd(3, 0, 0x2)

    label("loc_1825")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1837")
    MenuCmd(3, 0, 0x3)

    label("loc_1837")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1849")
    MenuCmd(3, 0, 0x4)

    label("loc_1849")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_185B")
    MenuCmd(3, 0, 0x5)

    label("loc_185B")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_186D")
    MenuCmd(3, 0, 0x6)

    label("loc_186D")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_187F")
    MenuCmd(3, 0, 0x7)

    label("loc_187F")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1891")
    MenuCmd(3, 0, 0x8)

    label("loc_1891")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18A3")
    MenuCmd(3, 0, 0x9)

    label("loc_18A3")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18B5")
    MenuCmd(3, 0, 0xA)

    label("loc_18B5")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B2B")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_193B"),
        (1, "loc_1ABB"),
        (2, "loc_1C1D"),
        (3, "loc_1DBD"),
        (4, "loc_1F0C"),
        (5, "loc_2085"),
        (6, "loc_2217"),
        (7, "loc_2385"),
        (8, "loc_24FD"),
        (9, "loc_268D"),
        (10, "loc_27E2"),
        (SWITCH_DEFAULT, "loc_2963"),
    )


    label("loc_193B")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0037
    ChrTalk(
        0x101,
        "#00000F#6P（よし……エリィを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0038
    NpcTalk(
        0x18,
        "エリィ",
        (
            "#00106F#6Pホラーコースター……\x01",
            "うう、本当に入るのね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0039
    ChrTalk(
        0x101,
        (
            "#00004F#5Pはは、俺がついてるし\x01",
            "大丈夫だよ。\x02\x03",

            "#00002Fしっかりエスコート\x01",
            "させてもらうからさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0040
    NpcTalk(
        0x18,
        "エリィ",
        "#00100F#12Pええ、頼りにしてるわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_1ABB")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0041
    ChrTalk(
        0x101,
        "#00000F#6P（よし……ティオを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0042
    NpcTalk(
        0x18,
        "ティオ",
        (
            "#00204F#6P噂の新アトラクション……\x01",
            "ちょっと楽しみです。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0043
    ChrTalk(
        0x101,
        (
            "#00004F#5P少し怖いヤツみたいだけど、\x01",
            "ティオは平気そうだな。\x02\x03",

            "#00000Fさっそく入ってみるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0044
    NpcTalk(
        0x18,
        "ティオ",
        "#00200F#12Pええ、行きましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_1C1D")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0045
    ChrTalk(
        0x101,
        "#00000F#6P（よし……ランディを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x2)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CA4")
    SetChrFlags(0xA, 0x8)

    label("loc_1CA4")

    FadeToBright(1000, 0)
    OP_0D()

    #N0046
    NpcTalk(
        0x18,
        "ランディ",
        (
            "#00303F#6Pうーむ、ホラー系は\x01",
            "お目当ての女の子と入るのが\x01",
            "定石なんだがなあ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00002F#5Pはは、まあ男２人でも\x01",
            "楽しいかもしれないしさ。\x02\x03",

            "#00000Fさっそく入るとしようか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0048
    NpcTalk(
        0x18,
        "ランディ",
        (
            "#00300F#12Pま、せっかく来たし\x01",
            "付き合ってやるとするか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_1DBD")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0049
    ChrTalk(
        0x101,
        "#00000F#6P（よし……ノエルを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0050
    NpcTalk(
        0x18,
        "ノエル",
        (
            "#10100F#6Pモンスター退治……\x01",
            "なんだか燃えてきますね！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0051
    ChrTalk(
        0x101,
        (
            "#00009F#5Pはは、ノリノリだなあ。\x02\x03",

            "#00000Fそれじゃ、入ってみようか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0052
    NpcTalk(
        0x18,
        "ノエル",
        "#10100F#12Pええ、行きましょう！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_1F0C")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0053
    ChrTalk(
        0x101,
        "#00000F#6P（よし……ワジを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch03000.itc", 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0054
    NpcTalk(
        0x18,
        "ワジ",
        (
            "#10304F#6Pホラーコースターか……\x01",
            "フフ、悲鳴をあげつつ\x01",
            "抱きついてあげようか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0055
    ChrTalk(
        0x101,
        (
            "#00006F#5Pそんなこと期待してないから。\x02\x03",

            "#00000Fまあいいや、入るとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0056
    NpcTalk(
        0x18,
        "ワジ",
        "#10300F#12Pフフ、了解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_2085")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0057
    ChrTalk(
        0x101,
        "#00000F#6P（よし……キーアを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x3)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x18, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #N0058
    NpcTalk(
        0x18,
        "キーア",
        (
            "#01109F#6Pここってオバケが出るのー？\x01",
            "わくわくっ、すっごく楽しみー！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0059
    ChrTalk(
        0x101,
        (
            "#00012F#5Pはは、さすがに本物は\x01",
            "出ないだろうけど……\x01",
            "雰囲気は楽しめると思うよ。\x02\x03",

            "#00000Fそれじゃあ、入ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0060
    NpcTalk(
        0x18,
        "キーア",
        "#01109F#12Pれっつごー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_2217")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0061
    ChrTalk(
        0x101,
        "#00000F#6P（よし……フランを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x4)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0062
    NpcTalk(
        0x18,
        "フラン",
        (
            "#06409F#6P噂の新アトラクション……\x01",
            "ドキドキしてきました～！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0063
    ChrTalk(
        0x101,
        (
            "#00004F#5Pはは、ホラー系なのに\x01",
            "随分ノリノリなんだなあ。\x02\x03",

            "#00000Fよし、そろそろ入るか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0064
    NpcTalk(
        0x18,
        "フラン",
        "#06400F#12Pふふ、よろしくお願いしますね～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_2385")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0065
    ChrTalk(
        0x101,
        "#00000F#6P（よし……セシル姉を誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch07500.itc", 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0066
    NpcTalk(
        0x18,
        "セシル",
        (
            "#05902F#6P噂の新アトラクションね。\x01",
            "ふふ、楽しみだわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0067
    ChrTalk(
        0x101,
        (
            "#00002F#5Pはは、ホラー系なのに結構余裕だね。\x02\x03",

            "#00000Fセシル姉は俺がしっかりと\x01",
            "エスコートさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0068
    NpcTalk(
        0x18,
        "セシル",
        "#05900F#12Pええ、頼りにしてるわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_24FD")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0069
    ChrTalk(
        0x101,
        "#00000F#6P（よし……イリアさんを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2586")
    SetChrFlags(0xD, 0x8)

    label("loc_2586")

    FadeToBright(1000, 0)
    OP_0D()

    #N0070
    NpcTalk(
        0x18,
        "イリア",
        (
            "#01709F#6Pこういう絶叫系のヤツを\x01",
            "楽しみにしてたのよね～！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0071
    ChrTalk(
        0x101,
        (
            "#00009F#5Pはは、いかにもイリアさんが\x01",
            "好きそうなアトラクションですよね。\x02\x03",

            "#00000Fそれじゃあ、行きましょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0072
    NpcTalk(
        0x18,
        "イリア",
        "#01700F#12Pええ、さっそく行きましょ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_268D")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0073
    ChrTalk(
        0x101,
        "#00000F#6P（よし……リーシャを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x6)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0074
    NpcTalk(
        0x18,
        "リーシャ",
        (
            "#01802F#6Pふふ、いかにも雰囲気がある\x01",
            "アトラクションみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0075
    ChrTalk(
        0x101,
        (
            "#00002F#5Pはは、結構余裕みたいだな。\x02\x03",

            "#00000Fそれじゃあ、入ってみようか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0076
    NpcTalk(
        0x18,
        "リーシャ",
        "#01809F#12Pはいっ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_27E2")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0077
    ChrTalk(
        0x101,
        "#00000F#6P（よし……シュリを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x7)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0078
    NpcTalk(
        0x18,
        "シュリ",
        (
            "#14004F#6Pフ、フン……\x01",
            "どうせ大したことないんだろ？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0079
    ChrTalk(
        0x101,
        (
            "#00004F#5Pはは、どうかな？\x01",
            "意外と怖かったりして……\x02\x03",

            "#00000Fよし、それじゃあ入るぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x18)
    OP_93(0x18, 0x10E, 0x1F4)

    #N0080
    NpcTalk(
        0x18,
        "シュリ",
        (
            "#14011F#12Pちょ、ちょっと待って。\x01",
            "心の準備が……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_2963")


    #C0081
    ChrTalk(
        0x13,
        "では、チケットをお預かりします。\x02",
    )

    CloseMessageWindow()

    def lambda_298E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_298E)
    Sleep(50)

    def lambda_299E():
        OP_93(0x18, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_299E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x18, 0)
    SubItemNumber(0x35D, 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スタッフにチケットを１枚渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0083
    ChrTalk(
        0x13,
        (
            "モンスターを倒すための導力銃は\x01",
            "乗り物内に設置されております。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x13,
        (
            "フフ……\x01",
            "どうかご無事に帰られますよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x13, 0x0, 0x1F4)
    OP_9B(0x0, 0x13, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(200)
    Sound(121, 0, 100, 0)
    OP_71(0x0, 0x1, 0xA, 0x1, 0x0)
    OP_79(0x0)

    def lambda_2AB7():
        OP_98(0xFE, 0xFFFFFA88, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2AB7)
    OP_93(0x13, 0x5A, 0x1F4)
    WaitChrThread(0x13, 1)
    Sleep(300)
    FadeToDark(1000, 0, -1)

    def lambda_2AE9():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AE9)
    Sleep(50)

    def lambda_2B01():
        OP_9B(0x0, 0x18, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2B01)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x18, 0)
    OP_0D()
    NewScene("t1360", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B79")

    label("loc_2B2B")


    #C0085
    ChrTalk(
        0x13,
        "フフ、お止めになりますか？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x13,
        (
            "またのご来場を\x01",
            "お待ちしております……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2B79")

    Call(0, 23)
    OP_4C(0x13, 0xFF)
    SetChrPos(0x0, 0, 400, -350, 180)
    EventEnd(0x5)
    Return()

    # Function_21_15CA end

    def Function_22_2B94(): pass

    label("Function_22_2B94")

    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xF, 0x8)
    Return()

    # Function_22_2B94 end

    def Function_23_2BBD(): pass

    label("Function_23_2BBD")

    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xF, 0x8)
    Return()

    # Function_23_2BBD end

    def Function_24_2BE6(): pass

    label("Function_24_2BE6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    LoadChrToIndex("chr/ch03000.itc", 0x1F)
    LoadChrToIndex("chr/ch07500.itc", 0x20)
    OP_4B(0x13, 0xFF)
    ClearChrFlags(0x18, 0x80)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2C58"),
        (1, "loc_2C61"),
        (2, "loc_2C6A"),
        (3, "loc_2C73"),
        (4, "loc_2C7C"),
        (5, "loc_2C85"),
        (6, "loc_2C8E"),
        (7, "loc_2C97"),
        (8, "loc_2CA0"),
        (9, "loc_2CA9"),
        (10, "loc_2CB2"),
        (SWITCH_DEFAULT, "loc_2CBB"),
    )


    label("loc_2C58")

    SetChrChipByIndex(0x18, 0x0)
    Jump("loc_2CBB")

    label("loc_2C61")

    SetChrChipByIndex(0x18, 0x1)
    Jump("loc_2CBB")

    label("loc_2C6A")

    SetChrChipByIndex(0x18, 0x2)
    Jump("loc_2CBB")

    label("loc_2C73")

    SetChrChipByIndex(0x18, 0x1E)
    Jump("loc_2CBB")

    label("loc_2C7C")

    SetChrChipByIndex(0x18, 0x1F)
    Jump("loc_2CBB")

    label("loc_2C85")

    SetChrChipByIndex(0x18, 0x3)
    Jump("loc_2CBB")

    label("loc_2C8E")

    SetChrChipByIndex(0x18, 0x4)
    Jump("loc_2CBB")

    label("loc_2C97")

    SetChrChipByIndex(0x18, 0x20)
    Jump("loc_2CBB")

    label("loc_2CA0")

    SetChrChipByIndex(0x18, 0x5)
    Jump("loc_2CBB")

    label("loc_2CA9")

    SetChrChipByIndex(0x18, 0x6)
    Jump("loc_2CBB")

    label("loc_2CB2")

    SetChrChipByIndex(0x18, 0x7)
    Jump("loc_2CBB")

    label("loc_2CBB")

    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x4)
    SetChrPos(0x101, -600, 800, 1000, 90)
    SetChrPos(0x18, 600, 800, 1000, 270)
    Call(0, 22)
    OP_68(0, 1800, 1650, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(11500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(10500, 2500)
    OP_6F(0x79)
    OP_0D()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2D77"),
        (1, "loc_2EA8"),
        (2, "loc_2FBB"),
        (3, "loc_30CC"),
        (4, "loc_31E5"),
        (5, "loc_32EC"),
        (6, "loc_33F5"),
        (7, "loc_3515"),
        (8, "loc_3638"),
        (9, "loc_3770"),
        (10, "loc_388F"),
        (SWITCH_DEFAULT, "loc_39CE"),
    )


    label("loc_2D77")


    #N0087
    NpcTalk(
        0x18,
        "エリィ",
        (
            "#00106F#12Pはあ……オバケがあんなに\x01",
            "近づいてくるなんて、\x01",
            "びっくりしちゃったわ。\x02\x03",

            "#00100Fふふ、まあ思っていたよりも\x01",
            "怖くはなかったし、\x01",
            "楽しかったのは確かだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00009Fはは、楽しんでくれたなら\x01",
            "誘ってよかったよ。\x02\x03",

            "#00000Fそれじゃあ、また後で。\x02",
        )
    )

    CloseMessageWindow()

    #N0089
    NpcTalk(
        0x18,
        "エリィ",
        "#00100F#12Pええ、また後で。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_2EA8")


    #N0090
    NpcTalk(
        0x18,
        "ティオ",
        (
            "#00204F#12P迫りくるオバケたち……\x01",
            "なかなかスリルがありました。\x02\x03",

            "#00200Fさすがは新アトラクションですね。\x01",
            "大人気というのも頷けます。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00009Fはは、楽しんでくれた\x01",
            "みたいでよかったよ。\x02\x03",

            "#00000Fそれじゃあ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0092
    NpcTalk(
        0x18,
        "ティオ",
        "#00200F#12Pええ、ではまた。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_2FBB")


    #N0093
    NpcTalk(
        0x18,
        "ランディ",
        (
            "#00300F#12Pはは、ホラー系にしては\x01",
            "なかなかよくできてたよな。\x02\x03",

            "#00306F相手が綺麗なお姉さんじゃなくて\x01",
            "お前だったのがちっと残念だが。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#00009Fま、まあ楽しかったし\x01",
            "いいじゃないか。\x02\x03",

            "#00000Fそれじゃあ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0095
    NpcTalk(
        0x18,
        "ランディ",
        "#00300F#12Pおう、またな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_30CC")


    #N0096
    NpcTalk(
        0x18,
        "ノエル",
        (
            "#10100F#12Pふう、とっても楽しかったです。\x02\x03",

            "#10109F警備隊での射撃訓練も、\x01",
            "こういうゲーム式にすれば\x01",
            "結構上達しそうな気がしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00009Fはは、確かに……\x01",
            "いつかそういう時代がきたりしてな。\x02\x03",

            "#00000Fそれじゃあ、また後で。\x02",
        )
    )

    CloseMessageWindow()

    #N0098
    NpcTalk(
        0x18,
        "ノエル",
        "#10100F#12Pはい、ではまた！\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_31E5")


    #N0099
    NpcTalk(
        0x18,
        "ワジ",
        (
            "#10304F#12Pフフ、なかなか\x01",
            "骨太なアトラクションだったね。\x02\x03",

            "#10302F僕としたことが\x01",
            "なかなか夢中になっちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#00009F俺も熱中しちゃったけど……\x01",
            "楽しんでくれたならよかったよ。\x02\x03",

            "#00000Fそれじゃあ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0101
    NpcTalk(
        0x18,
        "ワジ",
        "#10300F#12Pフフ、また。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_32EC")


    #N0102
    NpcTalk(
        0x18,
        "キーア",
        (
            "#01109F#12Pはー、面白かったー！\x02\x03",

            "真っ暗な中を駆け抜けて、\x01",
            "風がビュンビュンあたって\x01",
            "すっごい気持ちよかった！\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#00009Fはは、そこまで\x01",
            "楽しんでくれたなら\x01",
            "誘ってよかったよ。\x02\x03",

            "#00000Fそれじゃあ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0104
    NpcTalk(
        0x18,
        "キーア",
        "#01100F#12Pうん、あとでねー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_33F5")


    #N0105
    NpcTalk(
        0x18,
        "フラン",
        (
            "#06400F#12Pはあ、スリル満点でしたね～！\x02\x03",

            "#06409Fロイドさんが\x01",
            "撃つのを頑張ってくれて\x01",
            "助かっちゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#00009Fあの数のオバケを相手するのは\x01",
            "なかなか大変だったけど……\x01",
            "楽しんでくれてよかったよ。\x02\x03",

            "#00000Fそれじゃあ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0107
    NpcTalk(
        0x18,
        "フラン",
        "#06400F#12Pはい、また～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_3515")


    #N0108
    NpcTalk(
        0x18,
        "セシル",
        (
            "#05900F#12Pふふ、とっても楽しかったわ。\x02\x03",

            "#05909Fロイドの射撃している姿も\x01",
            "なかなか頼もしかったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#00009Fはは、さすがに実際の銃とは\x01",
            "扱いが全然違うみたいだけど……\x01",
            "まあ、楽しんでくれてよかったよ。\x02\x03",

            "#00000Fそれじゃあ、また後で。\x02",
        )
    )

    CloseMessageWindow()

    #N0110
    NpcTalk(
        0x18,
        "セシル",
        "#05900F#12Pええ、また後でね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_3638")


    #N0111
    NpcTalk(
        0x18,
        "イリア",
        (
            "#01704F#12Pうーん、これは期待通りの\x01",
            "アトラクションだったわね！\x02\x03",

            "#01702Fフフ、もっとたっくさん\x01",
            "オバケが出てきてもよかったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00012Fさ、さすがにそれは\x01",
            "大変すぎると思いますけど……\x01",
            "まあ、楽しんでくれてよかったです。\x02\x03",

            "#00000Fそれじゃあ、また後で。\x02",
        )
    )

    CloseMessageWindow()

    #N0113
    NpcTalk(
        0x18,
        "イリア",
        "#01700F#12Pうん、じゃあね～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_3770")


    #N0114
    NpcTalk(
        0x18,
        "リーシャ",
        (
            "#01802F#12Pはあ、なかなか楽しかったです。\x02\x03",

            "#01806F怪物がめまぐるしく動いて、\x01",
            "撃っているロイドさんが\x01",
            "すごく大変そうでしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00009Fはは、ちょっと大変だったけど\x01",
            "俺もなかなか楽しめたよ。\x02\x03",

            "#00000Fそれじゃあ、また後で。\x02",
        )
    )

    CloseMessageWindow()

    #N0116
    NpcTalk(
        0x18,
        "リーシャ",
        "#01802F#12Pはい、ではまた。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_388F")


    #N0117
    NpcTalk(
        0x18,
        "シュリ",
        (
            "#14006F#12Pはー……乗り物が速くて、\x01",
            "全然目を開けてらんなかったけど\x01",
            "スリルはなかなかだったな。\x02\x03",

            "#14002Fそれにしてもアンタ、\x01",
            "楽しそうだったな。\x01",
            "オレも撃つ方がやりたかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#00009Fはは……これでも\x01",
            "結構大変だったんだけどな。\x02\x03",

            "#00000Fそれじゃあ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0119
    NpcTalk(
        0x18,
        "シュリ",
        "#14000F#12Pん、そんじゃな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_39CE")


    def lambda_39D3():

        label("loc_39D3")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_39D3")

    QueueWorkItem2(0x101, 2, lambda_39D3)
    OP_93(0x18, 0xB4, 0x1F4)

    def lambda_39EC():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_39EC)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x18, 1)
    EndChrThread(0x101, 0x2)
    SetChrFlags(0x18, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3A69"),
        (1, "loc_3A77"),
        (2, "loc_3A85"),
        (3, "loc_3A93"),
        (4, "loc_3AA1"),
        (5, "loc_3AAF"),
        (6, "loc_3ABD"),
        (7, "loc_3ACB"),
        (8, "loc_3AD9"),
        (9, "loc_3AE7"),
        (10, "loc_3AF5"),
        (SWITCH_DEFAULT, "loc_3B03"),
    )


    label("loc_3A69")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3A77")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3A85")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3A93")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3AA1")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3AAF")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3ABD")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3ACB")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3AD9")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3AE7")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3AF5")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3B03")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B29")
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_3B29")

    Call(0, 23)
    OP_4C(0x13, 0xFF)
    SetChrPos(0x0, 0, 0, -2000, 180)
    EventEnd(0x5)
    Return()

    # Function_24_2BE6 end

    def Function_25_3B44(): pass

    label("Function_25_3B44")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-3070, 2300, -4040, 0)
    MoveCamera(310, 39, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(8910, 0)
    SetChrPos(0x101, -2970, 0, -3760, 270)
    SetChrPos(0xEF, -2050, 0, -2510, 270)
    OP_4B(0x19, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0120
    ChrTalk(
        0x101,
        "#00002F見つけたぞっ！\x02",
    )

    CloseMessageWindow()
    OP_9C(0x19, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    OP_93(0x19, 0x5A, 0x1F4)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0121
    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "きゃっ、見つかっちゃった☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-630, 2300, -4310, 0)
    MoveCamera(330, 32, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(8910, 0)
    SetChrPos(0x19, -2930, 0, -3100, 90)
    SetChrPos(0x101, -1440, 0, -4040, 270)
    SetChrPos(0xEF, -940, 0, -2450, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0122
    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "もー、こんなに早く\x01",
            "４回も見つかるなんて、\x01",
            "信じられないナ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "みししっ、ノロマな\x01",
            "みっしぃお兄ちゃんとは\x01",
            "大違いだヨ～☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_3D66")
    OP_63(0x153, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_3D7E")

    label("loc_3D66")

    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3D7E")

    Sleep(1000)

    #C0124
    ChrTalk(
        0x101,
        (
            "#00006F（みーしぇって、みっしぃに\x01",
            "  けっこう手厳しいなあ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "……むむっ、次は最後だネ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "よ～し、最後はもっと難しい場所に\x01",
            "隠れてるから、頑張って見つけてネ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E3D():

        label("loc_3E3D")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_3E3D")

    QueueWorkItem2(0x101, 1, lambda_3E3D)

    def lambda_3E4F():

        label("loc_3E4F")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_3E4F")

    QueueWorkItem2(0xEF, 1, lambda_3E4F)
    SetChrFlags(0x19, 0x1000)
    OP_95(0x19, -1430, 0, -8620, 4000, 0x0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(2740, 4000, -15010, 0)
    MoveCamera(322, 28, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(8039, 0)
    SetChrPos(0x101, -430, 0, -11830, 180)
    SetChrPos(0xEF, 960, 0, -11900, 180)
    SetChrFlags(0x19, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    #C0127
    ChrTalk(
        0x101,
        (
            "#00006Fいよいよ最後の隠れ場所か……\x02\x03",

            "#00000Fテーマパークの中だけだから\x01",
            "そこまで難しくはなさそうだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_3F97")

    #C0128
    ChrTalk(
        0x102,
        (
            "#00100Fそれじゃあ、\x01",
            "探しに行ってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_3F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_3FD5")

    #C0129
    ChrTalk(
        0x103,
        (
            "#00200Fそれでは、\x01",
            "探しに行ってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_3FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_4011")

    #C0130
    ChrTalk(
        0x104,
        (
            "#00300Fそれじゃあ、\x01",
            "探しに行ってみっか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_4011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_4051")

    #C0131
    ChrTalk(
        0x109,
        (
            "#10100Fそれじゃあ、\x01",
            "探しに行ってみましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_4051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_4095")

    #C0132
    ChrTalk(
        0x105,
        (
            "#10300Fそれじゃあ、\x01",
            "探しに行ってみるとしようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_4095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_40C8")

    #C0133
    ChrTalk(
        0x153,
        "#01100Fそれじゃ、探しにいこー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_40C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_410A")

    #C0134
    ChrTalk(
        0x156,
        (
            "#06400Fそれじゃあ、\x01",
            "探しに行ってみましょう～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_410A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_414E")

    #C0135
    ChrTalk(
        0x14C,
        (
            "#05900Fふふ、それじゃあ\x01",
            "探しに行ってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_414E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4192")

    #C0136
    ChrTalk(
        0x134,
        (
            "#01700Fフフ、それじゃあ、\x01",
            "探しに行ってみましょ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_4192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_41D0")

    #C0137
    ChrTalk(
        0x135,
        (
            "#01802Fそれでは、\x01",
            "探しに行ってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_41D0")


    #C0138
    ChrTalk(
        0x166,
        (
            "#14000Fそんじゃ、\x01",
            "探しに行ってみるか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41FC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x7F, 0x1, 0xE)
    SetScenarioFlags(0x1C9, 6)
    SetChrPos(0x0, 160, 0, -12030, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_3B44 end

    def Function_26_4228(): pass

    label("Function_26_4228")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "テーマパークの\x01",
            "見取り図が描かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_26_4228 end

    SaveToFile()

Try(main)
