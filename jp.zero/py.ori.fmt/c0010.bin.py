from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0010.bin",                # FileName
        "c0010",                    # MapName
        "c0010",                    # Location
        0x0003,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 3, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0010",                  # 0
        "駅員ルクス",             # 1
        "駅員リサ",               # 2
        "駅員エイム",             # 3
        "駅員シェンリー",         # 4
        "駅員マッジス",           # 5
        "臨検官クワトロ",         # 6
        "遊撃士スコット",         # 7
        "遊撃士ヴェンツェル",     # 8
        "遊撃士リン",             # 9
        "遊撃士エオリア",         # 10
        "乗客",                   # 11
        "乗客",                   # 12
        "乗客",                   # 13
        "乗客",                   # 14
        "乗客",                   # 15
        "乗客",                   # 16
        "乗客",                   # 17
        "乗客",                   # 18
    ))

    AddCharChip((
        "chr/ch28300.itc",                   # 00
        "chr/ch28400.itc",                   # 01
        "chr/ch28500.itc",                   # 02
        "chr/ch22002.itc",                   # 03
        "chr/ch22102.itc",                   # 04
        "chr/ch21202.itc",                   # 05
        "chr/ch20000.itc",                   # 06
        "chr/ch20400.itc",                   # 07
        "chr/ch34200.itc",                   # 08
        "chr/ch21600.itc",                   # 09
        "chr/ch27200.itc",                   # 0A
        "chr/ch27300.itc",                   # 0B
        "chr/ch32000.itc",                   # 0C
        "chr/ch32100.itc",                   # 0D
    ))

    DeclNpc(4750,    0,       7500,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(9500,    0,       7500,    180,  257,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(33000,   4000,    8000,    270,  257,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(33000,   4000,    -8000,   270,  257,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(18260,   0,       10229,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(28000,   4000,    10000,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(12439,   29,      -409,    180,  389,  0x0, 0,   10,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(12439,   29,      -2549,   0,    405,  0x0, 0,   11,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(6420,    29,      -2569,   180,  389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(6420,    0,       -4050,   0,    389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(14000,   100,     -8899,   0,    469,  0x0, 0,   3,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(13000,   100,     -8899,   0,    469,  0x0, 0,   4,   0,   255, 255, 0,   21,  255,  0)
    DeclNpc(5500,    100,     -5400,   0,    469,  0x0, 0,   5,   0,   255, 255, 0,   22,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   385,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(28500,   4000,    1350,    90,   385,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(13500,   100,     -8899,   0,    469,  0x0, 0,   4,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(11000,   0,       0,       90,   385,  0x0, 0,   8,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(12000,   0,       0,       270,  385,  0x0, 0,   9,   0,   0,   0,   0,   27,  255,  0)

    DeclActor(4750,    0,       6500,    1000,    4750,    1500,    7500,    0x007E, 0,  5,  0x0000)
    DeclActor(9500,    0,       6500,    1000,    9500,    1500,    7500,    0x007E, 0,  7,  0x0000)
    DeclActor(32000,   4000,    8000,    1000,    33000,   5500,    8000,    0x007E, 0,  9,  0x0000)
    DeclActor(32000,   4000,    -8000,   1000,    33000,   5500,    -8000,   0x007E, 0,  11, 0x0000)
    DeclActor(20560,   0,       4090,    1000,    20560,   1500,    4090,    0x007C, 0,  35, 0x0000)
    DeclActor(20130,   0,       -4810,   1000,    20130,   1500,    -4810,   0x007C, 0,  36, 0x0000)
    DeclActor(31150,   4000,    1130,    1000,    31150,   5500,    1130,    0x007C, 0,  37, 0x0000)
    DeclActor(28100,   4000,    11510,   1000,    28100,   5500,    11510,   0x007C, 0,  38, 0x0000)
    DeclActor(30940,   4000,    -1900,   1000,    30940,   5500,    -1900,   0x007C, 0,  39, 0x0000)

    ScpFunction((
        "Function_0_4A8",          # 00, 0
        "Function_1_560",          # 01, 1
        "Function_2_58B",          # 02, 2
        "Function_3_600",          # 03, 3
        "Function_4_6F4",          # 04, 4
        "Function_5_781",          # 05, 5
        "Function_6_785",          # 06, 6
        "Function_7_B60",          # 07, 7
        "Function_8_B64",          # 08, 8
        "Function_9_1215",         # 09, 9
        "Function_10_1219",        # 0A, 10
        "Function_11_1411",        # 0B, 11
        "Function_12_1415",        # 0C, 12
        "Function_13_191A",        # 0D, 13
        "Function_14_1F51",        # 0E, 14
        "Function_15_209C",        # 0F, 15
        "Function_16_2403",        # 10, 16
        "Function_17_2775",        # 11, 17
        "Function_18_286B",        # 12, 18
        "Function_19_2C9B",        # 13, 19
        "Function_20_2E16",        # 14, 20
        "Function_21_3024",        # 15, 21
        "Function_22_3209",        # 16, 22
        "Function_23_341F",        # 17, 23
        "Function_24_34E2",        # 18, 24
        "Function_25_3642",        # 19, 25
        "Function_26_3888",        # 1A, 26
        "Function_27_393C",        # 1B, 27
        "Function_28_3A42",        # 1C, 28
        "Function_29_3D70",        # 1D, 29
        "Function_30_3F67",        # 1E, 30
        "Function_31_405A",        # 1F, 31
        "Function_32_41C0",        # 20, 32
        "Function_33_465B",        # 21, 33
        "Function_34_49FC",        # 22, 34
        "Function_35_4A6C",        # 23, 35
        "Function_36_4AE4",        # 24, 36
        "Function_37_4B5C",        # 25, 37
        "Function_38_4B95",        # 26, 38
        "Function_39_4C11",        # 27, 39
    ))


    def Function_0_4A8(): pass

    label("Function_0_4A8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4E8"),
        (1, "loc_4F4"),
        (2, "loc_500"),
        (3, "loc_50C"),
        (4, "loc_518"),
        (5, "loc_524"),
        (6, "loc_530"),
        (SWITCH_DEFAULT, "loc_53C"),
    )


    label("loc_4E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_4F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_500")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_50C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_518")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_524")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_530")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_53C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_548")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_55F")

    Return()

    # Function_0_4A8 end

    def Function_1_560(): pass

    label("Function_1_560")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58A")
    OP_94(0xFE, 0x4D12, 0x686, 0x3F6F, 0xFFFFF81C, 0x3E8)
    Sleep(300)
    Jump("Function_1_560")

    label("loc_58A")

    Return()

    # Function_1_560 end

    def Function_2_58B(): pass

    label("Function_2_58B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FF")
    OP_95(0xFE, 20920, 4000, -8210, 1000, 0x0)
    OP_95(0xFE, 20920, 4000, 760, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0xC8)
    Sleep(2500)
    OP_95(0xFE, 20920, 4000, -8210, 1000, 0x0)
    OP_95(0xFE, 18700, 4000, -8210, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0xC8)
    Sleep(4500)
    Jump("Function_2_58B")

    label("loc_5FF")

    Return()

    # Function_2_58B end

    def Function_3_600(): pass

    label("Function_3_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_614")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 33)
    Jump("loc_621")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_621")
    Event(0, 28)

    label("loc_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6A1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_668")
    SetChrPos(0xD, 18820, 0, 4500, 90)
    SetChrPos(0xC, 19970, 0, 4500, 270)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_679")

    label("loc_668")

    SetChrPos(0xD, 19970, 0, -4490, 90)

    label("loc_679")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_6F3")

    label("loc_6A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D0")
    SetChrFlags(0xD, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C6")
    Jump("loc_6CB")

    label("loc_6C6")

    SetChrFlags(0xD, 0x80)

    label("loc_6CB")

    Jump("loc_6DF")

    label("loc_6D0")

    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)

    label("loc_6DF")

    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)

    label("loc_6F3")

    Return()

    # Function_3_600 end

    def Function_4_6F4(): pass

    label("Function_4_6F4")

    ClearMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71D")
    SetMapObjFlags(0x2, 0x10)

    label("loc_71D")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_731")
    Jump("loc_769")

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_769")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_751")
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_769")

    label("loc_751")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_769")
    SetMapObjFlags(0x1, 0x10)
    OP_1B(0x0, 0x0, 0x22)

    label("loc_769")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_780")
    SetMapObjFlags(0x1, 0x10)

    label("loc_780")

    Return()

    # Function_4_6F4 end

    def Function_5_781(): pass

    label("Function_5_781")

    Call(0, 6)
    Return()

    # Function_5_781 end

    def Function_6_785(): pass

    label("Function_6_785")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A24")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_956")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A4")

    #C0001
    ChrTalk(
        0x8,
        (
            "１０数年前の《百日戦役》では\x01",
            "帝国と共和国は対立関係にあったろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "鉄道も運行を停止したために、\x01",
            "クロスベルに来ていた旅行者たちは\x01",
            "足止めを喰らうことになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "今ではそういったことが起こらないよう\x01",
            "充分に体制が見直されたけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_951")

    label("loc_8A4")


    #C0004
    ChrTalk(
        0x8,
        (
            "１０数年前の《百日戦役》で\x01",
            "この鉄道は一時運行を停止して、\x01",
            "多くの人々を難民としてしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "今ではそういったことが起こらないよう\x01",
            "充分に体制が見直されたけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_951")

    Jump("loc_A1F")

    label("loc_956")


    #C0006
    ChrTalk(
        0x8,
        (
            "マクダエル市長も、\x01",
            "帝国や共和国で会議があるときは\x01",
            "列車を使って移動しているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "飛行艇で行くとなると確かに早いけど、\x01",
            "ミラがそれなりにかかるからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "いやはや、まさに堅実な市長らしいよ。\x02",
    )

    CloseMessageWindow()

    label("loc_A1F")

    Jump("loc_B5C")

    label("loc_A24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABB")

    #C0009
    ChrTalk(
        0x8,
        (
            "本日もクロスベル駅を\x01",
            "ご利用いただきありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "列車の到着時は\x01",
            "大変込み合いますので\x01",
            "どうかお気をつけ下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5C")

    label("loc_ABB")


    #C0011
    ChrTalk(
        0x8,
        (
            "鉄道は《大陸鉄道公社》によって\x01",
            "運営されているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "ちなみにクワトロさんは、\x01",
            "臨検のために帝国から派遣されてきた人で\x01",
            "公社の社員ってワケじゃないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5C")

    TalkEnd(0x8)
    Return()

    # Function_6_785 end

    def Function_7_B60(): pass

    label("Function_7_B60")

    Call(0, 8)
    Return()

    # Function_7_B60 end

    def Function_8_B64(): pass

    label("Function_8_B64")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1211")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCF")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_BCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_BEE")
    OP_AF(0x89)
    Jump("loc_C50")

    label("loc_BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BFE")
    OP_AF(0x88)
    Jump("loc_C50")

    label("loc_BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C0E")
    OP_AF(0x87)
    Jump("loc_C50")

    label("loc_C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_C1E")
    OP_AF(0x86)
    Jump("loc_C50")

    label("loc_C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C2E")
    OP_AF(0x85)
    Jump("loc_C50")

    label("loc_C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C3E")
    OP_AF(0x84)
    Jump("loc_C50")

    label("loc_C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_C4E")
    OP_AF(0x83)
    Jump("loc_C50")

    label("loc_C4E")

    OP_AF(0x82)

    label("loc_C50")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_120C")

    label("loc_C5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C73")
    Jump("loc_120C")

    label("loc_C73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F1F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D32")

    #C0013
    ChrTalk(
        0x9,
        (
            "間もなく、共和国行き列車が\x01",
            "１番ホームから発車いたします。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "ご搭乗ならお急ぎいただくか、\x01",
            "次の列車をお待ちくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_DB2")

    label("loc_D32")


    #C0015
    ChrTalk(
        0x9,
        (
            "間もなく、共和国行き列車が\x01",
            "１番ホームから発車いたしますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "かけ込み乗車は危険ですので、\x01",
            "余裕を持ってご搭乗ください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB2")

    Jump("loc_F1A")

    label("loc_DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E92")

    #C0017
    ChrTalk(
        0x9,
        (
            "国境の門からも\x01",
            "帝国・共和国への\x01",
            "定期バスが出ております。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "お時間はかかりますが、\x01",
            "そちらでの帰省の方法も\x01",
            "ご案内しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "万一にも列車に間に合わない場合、\x01",
            "お気軽にご相談くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F1A")

    label("loc_E92")


    #C0020
    ChrTalk(
        0x9,
        (
            "国境門から出るバスを利用した\x01",
            "陸路での帰省もご案内しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "万一にも列車に間に合わない場合、\x01",
            "お気軽にご相談くださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1A")

    Jump("loc_120C")

    label("loc_F1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1072")

    #C0022
    ChrTalk(
        0x9,
        "あっ……\x02",
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
    Sleep(1000)

    #C0023
    ChrTalk(
        0x9,
        (
            "……失礼しました。\x01",
            "最近クロスベルタイムズで、\x01",
            "お見かけしたものですから……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        (
            "今日は依頼の件で\x01",
            "来られたのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "クワトロさんなら、\x01",
            "階段を上って左手の\x01",
            "臨検官室前でお待ちですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_10E5")

    label("loc_1072")


    #C0026
    ChrTalk(
        0x9,
        (
            "今日は依頼の件で\x01",
            "来られたのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "クワトロさんなら、\x01",
            "階段を上って左手の\x01",
            "臨検官室前でお待ちですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E5")

    Jump("loc_120C")

    label("loc_10EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1192")

    #C0028
    ChrTalk(
        0x9,
        (
            "警備隊の詰める東西の国境門への\x01",
            "貨物列車も当駅から出ています。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "直接物資を運搬することができるので、\x01",
            "警備隊ではとても重宝しているそうですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_120C")

    label("loc_1192")


    #C0030
    ChrTalk(
        0x9,
        (
            "警備隊の詰める東西の国境門への\x01",
            "貨物列車も当駅から出ています。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "一般の方はご利用になれないので\x01",
            "ご注意くださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120C")

    Jump("loc_B71")

    label("loc_1211")

    TalkEnd(0x9)
    Return()

    # Function_8_B64 end

    def Function_9_1215(): pass

    label("Function_9_1215")

    Call(0, 10)
    Return()

    # Function_9_1215 end

    def Function_10_1219(): pass

    label("Function_10_1219")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_12F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1286")

    #C0032
    ChrTalk(
        0xA,
        "おや……お急ぎですか？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xA,
        (
            "危険ですので、\x01",
            "ホームでは走らないで下さいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F0")

    label("loc_1286")


    #C0034
    ChrTalk(
        0xA,
        "近頃物騒な事件が多いようです。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xA,
        (
            "お客様には、\x01",
            "気をつけて列車の旅を\x01",
            "楽しんできてほしいものですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F0")

    Jump("loc_140D")

    label("loc_12F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135F")

    #C0036
    ChrTalk(
        0xA,
        (
            "列車内では飲食物の\x01",
            "販売もしております。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xA,
        (
            "長旅の際には\x01",
            "ぜひご利用くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140D")

    label("loc_135F")


    #C0038
    ChrTalk(
        0xA,
        (
            "駅を利用するビジネスマンには、\x01",
            "毎日帝国や共和国と\x01",
            "行き来している方もおられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "そういう方がクロスベルの経済を\x01",
            "支えているかと思うと、\x01",
            "ただただ頭の下がる想いです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140D")

    TalkEnd(0xA)
    Return()

    # Function_10_1219 end

    def Function_11_1411(): pass

    label("Function_11_1411")

    Call(0, 12)
    Return()

    # Function_11_1411 end

    def Function_12_1415(): pass

    label("Function_12_1415")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1634")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1538")

    #C0040
    ChrTalk(
        0xB,
        (
            "あっ……すみません、\x01",
            "少しお待ちいただけますか。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "……お客様にお知らせします。\x02\x03",

            "車両発車のベルが鳴りましたら\x01",
            "ホーム中ほどまでお下がりください。\x02\x03",

            "車両が通過する際に\x01",
            "身を乗り出したりしないよう\x01",
            "お願い申し上げます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_157A")

    label("loc_1538")


    #C0042
    ChrTalk(
        0xB,
        (
            "えっと……\x01",
            "とにかく危ないので\x01",
            "身を乗り出さないでくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157A")

    Jump("loc_162F")

    label("loc_157F")


    #C0043
    ChrTalk(
        0xB,
        (
            "本来私は内気な方なのですが、\x01",
            "構内アナウンスの担当になってから\x01",
            "軽やかに舌が回るようになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xB,
        (
            "うふふ……\x01",
            "うってつけの役を任されて\x01",
            "本当に良かったと思っていますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_162F")

    Jump("loc_1916")

    label("loc_1634")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1709")

    #C0045
    ChrTalk(
        0xB,
        (
            "本日もクロスベル駅を\x01",
            "ご利用いただき\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "こちらでは切符の発券のほか\x01",
            "ご利用案内もさせて頂いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xB,
        (
            "ご不明な点がありましたら\x01",
            "ぜひお尋ねくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1786")

    label("loc_1709")


    #C0048
    ChrTalk(
        0xB,
        (
            "私は構内のアナウンスも\x01",
            "担当しているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        (
            "もし鉄道のご利用について\x01",
            "不明な点がありましたら\x01",
            "ぜひお尋ねくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1786")

    Jump("loc_1916")

    label("loc_178B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189E")

    #C0050
    ChrTalk(
        0xB,
        (
            "あっ……すみません、\x01",
            "少しお待ちいただけますか。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "……お客様にお知らせします。\x02\x03",

            "１番ホームは共和国方面、\x01",
            "２番ホームは帝国方面行きと\x01",
            "なっております。\x02\x03",

            "３番ホームは貨物・特別車両専用\x01",
            "ですので、お立ち入りのないよう\x01",
            "お願い申し上げます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1916")

    label("loc_189E")


    #C0052
    ChrTalk(
        0xB,
        (
            "３番線は、一般の方は\x01",
            "乗り降りできないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "警備隊の特別車両も止まりますから\x01",
            "入らないようにお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1916")

    TalkEnd(0xB)
    Return()

    # Function_12_1415 end

    def Function_13_191A(): pass

    label("Function_13_191A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1C31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E4")
    OP_4B(0xD, 0xFF)

    #C0054
    ChrTalk(
        0xFE,
        (
            "共和国行き列車の臨検、\x01",
            "ごくろうさんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "相変わらず急がしそうですね。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xD,
        (
            "いやなに……\x01",
            "記念祭中の忙しさに比べれば\x01",
            "序の口といった所だろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    Jump("loc_1A57")

    label("loc_19E4")


    #C0057
    ChrTalk(
        0xFE,
        (
            "そういや、\x01",
            "さっき見かけたお嬢さん……\x01",
            "なんか変だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "金持ちそうなのに\x01",
            "付き人もいなかったみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A57")

    Jump("loc_1C2C")

    label("loc_1A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6E")
    Call(0, 14)
    Jump("loc_1C2C")

    label("loc_1A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9B")

    #C0059
    ChrTalk(
        0xFE,
        (
            "記念祭のときは忙しかったけど、\x01",
            "面白い乗客もいたんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "見るからに遊び人って感じの\x01",
            "男なんだが、あのクワトロさんを\x01",
            "手玉にとっておちょくってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "クワトロさんはキレてたけど、\x01",
            "ハタからみてて楽しかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#0000F（そういうことをしそうな人、\x01",
            "  知り合いにいるけど……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1C2C")

    label("loc_1B9B")


    #C0063
    ChrTalk(
        0xFE,
        (
            "記念祭のときは忙しかったけど、\x01",
            "面白い乗客もいたんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "あの赤毛の遊び人が\x01",
            "クワトロさんをおちょくる様子、\x01",
            "ハタからみてて楽しかったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C2C")

    Jump("loc_1F4D")

    label("loc_1C31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D30")

    #C0065
    ChrTalk(
        0xFE,
        (
            "毎日、共和国や帝国から\x01",
            "沢山の人々がクロスベルを訪れる。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "様々な文化が混ざったような\x01",
            "クロスベル市の町並みは、\x01",
            "まさに彼らからもたらされたものだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "……本来のクロスベル市の姿ってのは、\x01",
            "どういうものなんだろうな？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1DD1")

    label("loc_1D30")


    #C0068
    ChrTalk(
        0xFE,
        (
            "様々な文化が混ざったような\x01",
            "クロスベル市の町並みは、\x01",
            "共和国や帝国からもたらされたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "……本来のクロスベル市の姿ってのは、\x01",
            "どういうものなんだろうな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD1")

    Jump("loc_1F4D")

    label("loc_1DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB4")

    #C0070
    ChrTalk(
        0xFE,
        (
            "俺がここに務め始めてから\x01",
            "５年くらい経つかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "最初はお客さんの顔を\x01",
            "全員覚えてやろうと思っていたけど、\x01",
            "それも随分前に諦めてしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "無理なことでも信じられるのは\x01",
            "若気の至りってやつだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1F4D")

    label("loc_1EB4")


    #C0073
    ChrTalk(
        0xFE,
        (
            "最初はお客さんの顔を\x01",
            "全員覚えてやろうと思っていたけど、\x01",
            "それも随分前に諦めてしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "無理なことでも信じられるのは\x01",
            "若気の至りってやつだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F4D")

    TalkEnd(0xFE)
    Return()

    # Function_13_191A end

    def Function_14_1F51(): pass

    label("Function_14_1F51")


    #C0075
    ChrTalk(
        0xFE,
        (
            "あんたたち、さっき共和国の方に\x01",
            "出かけたかと思ったが……\x01",
            "頻繁に旅行する方なのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "列車に慣れちまったら\x01",
            "道中、退屈することも多いだろう。\x01",
            "そういう時は本でも読むといいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "そうだな、読み終わった本だが\x01",
            "良かったらあんたらにくれてやるよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D2, 1)
    SetScenarioFlags(0x9D, 4)
    Return()

    # Function_14_1F51 end

    def Function_15_209C(): pass

    label("Function_15_209C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_23A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214F")
    OP_4B(0xC, 0xFF)

    #C0079
    ChrTalk(
        0xFE,
        (
            "次は少し休憩をいれて、\x01",
            "帝国行き列車の臨検だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "休憩しすぎて\x01",
            "気を抜かないように\x01",
            "しなければな。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        "（相変わらず厳しい人だなぁ……）\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    Jump("loc_239D")

    label("loc_214F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2330")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22C9")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0082
    ChrTalk(
        0xFE,
        "む、君たちは特務支援課の。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#0000F臨検官さん、\x01",
            "ご無沙汰しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "ふむ……\x01",
            "その節は世話になったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "私は今から、２番ホームで\x01",
            "臨検を行なう予定なのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "君たちも共和国に\x01",
            "行っていたのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0006Fえ、ええまぁ。\x01",
            "仕事の一環というか……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "ふむ……結構結構。\x01",
            "懸命に働いているようで\x01",
            "なによりだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_232B")

    label("loc_22C9")


    #C0089
    ChrTalk(
        0xFE,
        (
            "懸命に働いているようで\x01",
            "なによりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "君たちも忙しいようだが、\x01",
            "せいぜいがんばるといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232B")

    Jump("loc_239D")

    label("loc_2330")


    #C0091
    ChrTalk(
        0xFE,
        (
            "今から、２番ホームで\x01",
            "臨検を行なう予定なのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "帝国への入国者には\x01",
            "入念なチェックが\x01",
            "欠かせんのだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_239D")

    Jump("loc_23FF")

    label("loc_23A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_23B3")
    Jump("loc_23FF")

    label("loc_23B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_23C8")
    Call(0, 30)
    Jump("loc_23FF")

    label("loc_23C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_23DC")
    Call(0, 29)
    Jump("loc_23FF")

    label("loc_23DC")


    #C0093
    ChrTalk(
        0xFE,
        (
            "うむむ……\x01",
            "まだ来ないのか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23FF")

    TalkEnd(0xFE)
    Return()

    # Function_15_209C end

    def Function_16_2403(): pass

    label("Function_16_2403")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2771")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CA")
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xE, 0x0, 0)
    TurnDirection(0xF, 0x0, 0)

    #C0094
    ChrTalk(
        0xE,
        (
            "おや、君たちは……\x01",
            "確か警察の子たちだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 7)), scpexpr(EXPR_END)), "loc_248A")

    #C0095
    ChrTalk(
        0x101,
        "#0005Fあ、お疲れ様です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24E9")

    label("loc_248A")


    #C0096
    ChrTalk(
        0x101,
        (
            "#0005Fあ、お疲れ様です。\x02\x03",

            "#0003F（遊撃士のスコットさんと\x01",
            "  ヴェンツェルさん、だったな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E9")


    #C0097
    ChrTalk(
        0x102,
        "#0100Fお二人は仕事帰りですか？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xF,
        "先刻、帝国方面から戻ったところだ。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xF,
        "そういうお前たちは何をしている？\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        (
            "#0300Fちょいと\x01",
            "支援要請を片付けてたのさ。\x02\x03",

            "臨検の手伝いって奴でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xE,
        (
            "へぇ……\x01",
            "意外と責任のありそうな\x01",
            "仕事を任されてるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xE,
        "ま、その調子で頑張れよ。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xF,
        (
            "……俺たちの仕事を\x01",
            "邪魔しない程度にな。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x103,
        (
            "#0200F（……まだ全然認められては\x01",
            "  いないようですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#0006F（ま、まぁ仕方ないさ。\x01",
            "  これからこれから。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x0)
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 7)
    Jump("loc_2771")

    label("loc_26CA")


    #C0106
    ChrTalk(
        0xFE,
        (
            "もうエステルとヨシュアには\x01",
            "会ったかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "ほんと、彼らはあの若さで\x01",
            "たいしたもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "確か歳は君らと同じくらいだろ？\x01",
            "はは、事あるごとに比べられそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2771")

    TalkEnd(0xFE)
    Return()

    # Function_16_2403 end

    def Function_17_2775(): pass

    label("Function_17_2775")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2867")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2793")
    Call(0, 16)
    Jump("loc_2867")

    label("loc_2793")


    #C0109
    ChrTalk(
        0xFE,
        (
            "臨検か……\x01",
            "遊撃士という立場上、\x01",
            "関わりづらい仕事ではあるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "こっちの手からこぼれた仕事を\x01",
            "やってくれる分には助かる。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "あとは我々の邪魔にならぬよう\x01",
            "気をつけるがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        "#0200F（えらそうです……）\x02",
    )

    CloseMessageWindow()

    label("loc_2867")

    TalkEnd(0xFE)
    Return()

    # Function_17_2775 end

    def Function_18_286B(): pass

    label("Function_18_286B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_2C97")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28ED")

    #C0113
    ChrTalk(
        0xFE,
        (
            "例のマフィアの件で\x01",
            "聞き込みを始めるところさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "……君たちはなんだか、\x01",
            "急いでいるようだな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C97")

    label("loc_28ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF4")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0x10, 0x0, 0)
    TurnDirection(0x11, 0x0, 0)

    #C0115
    ChrTalk(
        0x10,
        (
            "……共和国方面のホームから\x01",
            "出てこなかったかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x11,
        (
            "日帰りで外国に行くなんて\x01",
            "あなた達も忙しいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0012Fは、はは……\x01",
            "ちょっと支援要請の関係で\x01",
            "仕方なかったというか……\x02\x03",

            "#0001F……それより、\x01",
            "例の襲撃事件の調査に\x01",
            "進展はありましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x10,
        "……うーん、それがね。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x10,
        (
            "どうも、少し前に\x01",
            "帝国方面から物騒なブツが\x01",
            "密輸されてたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        "#0105F物騒なブツ……？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x11,
        (
            "昨日の襲撃に使用された\x01",
            "ラインフォルト製の重機関銃よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x11,
        (
            "ルバーチェは前々から\x01",
            "綿密に準備をしていたみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        "#0301F例の重機関銃か……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        (
            "#0203F綿密に準備した割には、\x01",
            "結局黒月には退けられて\x01",
            "しまったようですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x10,
        (
            "うん、そうなんだよな。\x01",
            "昨夜の襲撃事件には\x01",
            "妙に粗が目立ってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x10,
        (
            "その辺の違和感も含めて\x01",
            "調査していかないとね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x0)
    OP_93(0x11, 0x0, 0x0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x1, 0)
    Jump("loc_2C97")

    label("loc_2BF4")


    #C0127
    ChrTalk(
        0xFE,
        (
            "しかしまぁ、いくら帝国から\x01",
            "クロスベルに入ってくる積荷が\x01",
            "臨検されないとはいえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "もう少し取締りを\x01",
            "厳しく出来ないものかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#0006F（耳が痛いな……）\x02",
    )

    CloseMessageWindow()

    label("loc_2C97")

    TalkEnd(0xFE)
    Return()

    # Function_18_286B end

    def Function_19_2C9B(): pass

    label("Function_19_2C9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_2E12")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D79")

    #C0130
    ChrTalk(
        0xFE,
        (
            "ヴェンツェルたちと手分けして\x01",
            "今日から調査を始めるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "あなた達も何か分かったら\x01",
            "教えて頂戴ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#0003F（あの錠剤のことは……\x01",
            "  まだ不確定な情報だし\x01",
            "  話さない方がよさそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E12")

    label("loc_2D79")


    #C0133
    ChrTalk(
        0xFE,
        (
            "それにしてもラインフォルトの\x01",
            "重機関銃か……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "そんな、警備隊にも配備されてない\x01",
            "強力な装備を手に入れるなんて、\x01",
            "つくづくルバーチェって不気味よね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E12")

    TalkEnd(0xFE)
    Return()

    # Function_19_2C9B end

    def Function_20_2E16(): pass

    label("Function_20_2E16")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EAA")
    Jump("loc_2EF4")

    label("loc_2EAA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2ECA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF4")

    label("loc_2ECA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EEA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF4")

    label("loc_2EEA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EF4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB2")

    #C0135
    ChrTalk(
        0xFE,
        (
            "フフ……帝国から列車で来る\x01",
            "というのも中々優雅だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "飛行船でレミフェリアあたりに\x01",
            "行ったことはあるが、\x01",
            "列車も悪くないものだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301C")

    label("loc_2FB2")


    #C0137
    ChrTalk(
        0xFE,
        (
            "フフ……今日は君を\x01",
            "素敵な所に連れて行ってあげよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "ミシュラムの高級レストラン\x01",
            "なんてどうだい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_301C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_2E16 end

    def Function_21_3024(): pass

    label("Function_21_3024")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30B8")
    Jump("loc_3102")

    label("loc_30B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30D8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3102")

    label("loc_30D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30F8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3102")

    label("loc_30F8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3102")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CE")

    #C0139
    ChrTalk(
        0xFE,
        "私は飛行船の方が好きだなぁ。\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "でも、列車に比べて飛行船の便は少ないのよね。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "帝国からクロスベルへの飛行船、\x01",
            "もう少し増えればいいのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3201")

    label("loc_31CE")


    #C0142
    ChrTalk(
        0xFE,
        (
            "私の彼ったらやる事が\x01",
            "いちいちベタなのよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3201")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_3024 end

    def Function_22_3209(): pass

    label("Function_22_3209")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_329D")
    Jump("loc_32E7")

    label("loc_329D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32BD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32E7")

    label("loc_32BD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32DD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32E7")

    label("loc_32DD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32E7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339B")

    #C0143
    ChrTalk(
        0xFE,
        (
            "共和国からの\x01",
            "列車に乗ってきたんだけど、\x01",
            "切符を落としちゃったみたいでさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "とほほ、駅員さん\x01",
            "判ってくれるかなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3417")

    label("loc_339B")


    #C0145
    ChrTalk(
        0xFE,
        (
            "失くしたと思ってたチケット、\x01",
            "列車の座席に挟まってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "はぁ、良かったよ～。\x01",
            "これで晴れてクロスベル入りだぁ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3417")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_3209 end

    def Function_23_341F(): pass

    label("Function_23_341F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34AF")

    #C0147
    ChrTalk(
        0xFE,
        (
            "なんでも腰に効く\x01",
            "温泉があるらしくてのう。\x01",
            "共和国に向かうんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "湯治っちゅーやつじゃな。\x01",
            "今から楽しみじゃわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DE")

    label("loc_34AF")


    #C0149
    ChrTalk(
        0xFE,
        (
            "さてさて、\x01",
            "次の共和国行きは何時発かのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34DE")

    TalkEnd(0xFE)
    Return()

    # Function_23_341F end

    def Function_24_34E2(): pass

    label("Function_24_34E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_356E")

    #C0150
    ChrTalk(
        0xFE,
        (
            "共和国の東方人街に行く\x01",
            "つもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "あの小説『賭博師ジャック』の\x01",
            "舞台を見てみたいと思ってね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_35C3")

    label("loc_356E")


    #C0152
    ChrTalk(
        0xFE,
        (
            "予約していた列車は\x01",
            "今から出る列車の次に来るやつだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        "うう、興奮してきたぁ！\x02",
    )

    CloseMessageWindow()

    label("loc_35C3")

    Jump("loc_363E")

    label("loc_35C8")


    #C0154
    ChrTalk(
        0xFE,
        (
            "共和国の東方人街って\x01",
            "治安とか大丈夫なのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "ジャックの世界そのまま、\x01",
            "ゴロツキばかりだったらどうしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_363E")

    TalkEnd(0xFE)
    Return()

    # Function_24_34E2 end

    def Function_25_3642(): pass

    label("Function_25_3642")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36D6")
    Jump("loc_3720")

    label("loc_36D6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36F6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3720")

    label("loc_36F6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3716")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3720")

    label("loc_3716")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3720")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37F1")

    #C0156
    ChrTalk(
        0xFE,
        (
            "彼氏に捨てられちゃってね……\x01",
            "いまから傷心旅行にしゃれ込むの。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        "……でも、私はめげないわ。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "外国でもっとかっこいい人を\x01",
            "見つけるんだから……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3880")

    label("loc_37F1")


    #C0159
    ChrTalk(
        0xFE,
        (
            "うーん、傷心旅行に行くなら\x01",
            "帝国かしら、共和国かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "どうせならかっこいい男の人が\x01",
            "いそうな方がいいけど……\x01",
            "どっちも捨てがたいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3880")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_3642 end

    def Function_26_3888(): pass

    label("Function_26_3888")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38FD")

    #C0161
    ChrTalk(
        0xFE,
        (
            "お爺ちゃんを\x01",
            "駅まで送ってきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "外国でのお仕事、\x01",
            "大変だろうけど頑張ってほしいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3938")

    label("loc_38FD")


    #C0163
    ChrTalk(
        0xFE,
        (
            "少しの間寂しくなるけど……\x01",
            "頑張ってね、おじいちゃん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3938")

    TalkEnd(0xFE)
    Return()

    # Function_26_3888 end

    def Function_27_393C(): pass

    label("Function_27_393C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39D5")

    #C0164
    ChrTalk(
        0xFE,
        (
            "若い頃勤めていた帝国の会社に\x01",
            "よく相談役として呼ばれるのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "仕事はなかなか大変だが……\x01",
            "老後も退屈しなくて済んでいるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A3E")

    label("loc_39D5")


    #C0166
    ChrTalk(
        0xFE,
        (
            "そろそろ帝国行き列車が\x01",
            "出発した頃だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "名残惜しいが、\x01",
            "ホームに降りて\x01",
            "待っているとするかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A3E")

    TalkEnd(0xFE)
    Return()

    # Function_27_393C end

    def Function_28_3A42(): pass

    label("Function_28_3A42")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(5300, 1500, 6460, 0)
    MoveCamera(44, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 2500, 0, -500, 90)
    SetChrPos(0x102, 2250, 0, 500, 90)
    SetChrPos(0x103, 1000, 0, -500, 90)
    SetChrPos(0x104, 750, 0, 500, 90)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    OP_68(6300, 1500, 6460, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3900)
    Fade(500)
    OP_68(29620, 5500, -8119, 0)
    MoveCamera(42, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(29590, 5500, 9120, 7000)
    Sleep(6900)
    Fade(500)
    OP_68(12760, 3000, -8000, 0)
    MoveCamera(48, 8, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    OP_68(5320, 1530, 440, 5000)
    Sleep(5000)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3C7D")

    #C0168
    ChrTalk(
        0x103,
        (
            "#5P#0200Fクロスベル駅……\x01",
            "議員令嬢さんが\x01",
            "こちらに来ているはずですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#11P#0001F共和国行きの鉄道は\x01",
            "１番ホームのはずだ。\x01",
            "……急ごう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D3B")

    label("loc_3C7D")


    #C0170
    ChrTalk(
        0x101,
        (
            "#11P#0005F……相変わらず、立派な駅だなぁ。\x02\x03",

            "#0004Fここに来るのは１ヶ月ぶりか。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#5P#0100F確か、駅の臨検官さんが\x01",
            "支援要請を出していたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#11P#0000Fああ、早速たずねてみよう。\x02",
    )

    CloseMessageWindow()

    label("loc_3D3B")

    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    SetChrPos(0x0, 2500, 0, 0, 90)
    SetScenarioFlags(0x44, 3)
    EventEnd(0x5)
    Return()

    # Function_28_3A42 end

    def Function_29_3D70(): pass

    label("Function_29_3D70")

    EventBegin(0x0)
    Fade(500)
    OP_68(27680, 5500, 8290, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, 28500, 4000, 8500, 0)
    SetChrPos(0x102, 27500, 4000, 8250, 0)
    SetChrPos(0x103, 28500, 4000, 7000, 0)
    SetChrPos(0x104, 27500, 4000, 6750, 0)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    #C0173
    ChrTalk(
        0xD,
        (
            "#5Pうむむ……\x01",
            "まだ来ないのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#11P#0000Fあの……もしかして\x01",
            "臨検官の方でしょうか。\x02\x03",

            "支援要請を確認して\x01",
            "伺ったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xD,
        (
            "#5Pということは……\x01",
            "君たちが例の支援課かね。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xD,
        (
            "#5P私はエレボニア帝国の軍部より\x01",
            "臨検官として出向している\x01",
            "クワトロという者だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xD,
        (
            "#5P早速仕事の話をしたいが……\x01",
            "引き受けてくれるかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x9, 0x1, 0x0)
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F53")
    Call(0, 32)
    Jump("loc_3F66")

    label("loc_3F53")

    SetChrPos(0x0, 28000, 4000, 8500, 0)
    EventEnd(0x5)

    label("loc_3F66")

    Return()

    # Function_29_3D70 end

    def Function_30_3F67(): pass

    label("Function_30_3F67")

    EventBegin(0x0)
    Fade(500)
    OP_68(27680, 5500, 8290, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, 28500, 4000, 8500, 0)
    SetChrPos(0x102, 27500, 4000, 8250, 0)
    SetChrPos(0x103, 28500, 4000, 7000, 0)
    SetChrPos(0x104, 27500, 4000, 6750, 0)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    #C0178
    ChrTalk(
        0xD,
        "#5Pふむ、君たち……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xD,
        (
            "#5Pこちらの仕事を\x01",
            "引き受けてくれるかね？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4046")
    Call(0, 32)
    Jump("loc_4059")

    label("loc_4046")

    SetChrPos(0x0, 28000, 4000, 8500, 0)
    EventEnd(0x5)

    label("loc_4059")

    Return()

    # Function_30_3F67 end

    def Function_31_405A(): pass

    label("Function_31_405A")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【はい】\x01",        # 0
            "【いいえ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40ED")

    #C0180
    ChrTalk(
        0x101,
        (
            "#11P#0000Fええ、大丈夫です。\x02\x03",

            "仕事の内容を\x01",
            "説明していただけますか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41BF")

    label("loc_40ED")


    #C0181
    ChrTalk(
        0x101,
        (
            "#11P#0006Fすみません、今ちょっと\x01",
            "外せない用を抱えてまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xD,
        (
            "#5P……そうかね。\x01",
            "仕方ないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xD,
        (
            "#5Pなら、できるだけ早く\x01",
            "その用とやらを片付けたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xD,
        (
            "#5Pこちらも急ぎなのだ、\x01",
            "よろしく頼むぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_41BF")

    Return()

    # Function_31_405A end

    def Function_32_41C0(): pass

    label("Function_32_41C0")


    #C0185
    ChrTalk(
        0xD,
        "#5Pいいだろう。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xD,
        "#5P……ふむ……それにしても………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0187
    ChrTalk(
        0x101,
        "#11P#0005Fあ、あの……？\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xD,
        "#5P……妙に若いのが来たものだな。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xD,
        (
            "#5Pフン、まぁ仕方あるまい。\x01",
            "誰も来ないよりはマシだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        (
            "#12P#0301F（なんだこのオッサン……\x01",
            "  偉そうだな、オイ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xD,
        "#5P……何か言ったかね？\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x103,
        (
            "#12P#0203F……お気になさらず。\x02\x03",

            "#0200Fそれよりも、要請では\x01",
            "『臨検の手伝いを頼みたい』\x01",
            "とのことでしたが……？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xD,
        "#5Pああ……その通りだ。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xD,
        (
            "#5P間もなく、帝国行きの列車が\x01",
            "ホームに到着する。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xD,
        (
            "#5P君たちにはそこで行われる\x01",
            "列車内の臨検を手伝ってもらいたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        (
            "#11P#0005F臨検、というと……\x02\x03",

            "#0000F帝国入りする列車に\x01",
            "不審者や不審物が乗っていないか\x01",
            "チェックするわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xD,
        "#5Pうむ。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xD,
        (
            "#5P本来なら他の臨検官もいるのだが、\x01",
            "生憎、病欠が重なってしまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xD,
        (
            "#5P今回は仕方なく手伝いを呼ぶことに\x01",
            "したというわけなのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x102,
        (
            "#12P#0100F……なるほど。\x01",
            "概ね事情は把握いたしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xD,
        "#5Pよろしい。\x02",
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("駅員の声")

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……間もなく、２番ホームに\x01",
            "帝国行き列車が到着いたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ご搭乗の方は\x01",
            "ホームにお急ぎ下さいませ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()
    SetScenarioFlags(0x5C, 1)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_41C0 end

    def Function_33_465B(): pass

    label("Function_33_465B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x1, 0x5, 0x5, 0x0, 0x0)
    OP_68(28050, 5500, 8960, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, 28500, 4000, 8500, 0)
    SetChrPos(0x102, 27500, 4000, 8250, 0)
    SetChrPos(0x103, 28500, 4000, 7000, 0)
    SetChrPos(0x104, 27500, 4000, 6750, 0)
    SetChrPos(0xD, 28000, 4000, 10000, 180)
    OP_4B(0xD, 0xFF)
    SetChrSubChip(0xD, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0204
    ChrTalk(
        0xD,
        "#5P……列車が到着したようだな。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xD,
        (
            "#5Pでは、早速だが\x01",
            "２番ホームで仕事の内容を\x01",
            "説明しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xD,
        "#5Pついてきたまえ。\x02",
    )

    CloseMessageWindow()
    OP_97(0xD, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_479C():
        OP_93(0x101, 0xFF79, 0x96)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_479C)

    def lambda_47A9():
        OP_93(0x102, 0xFF79, 0x96)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47A9)

    def lambda_47B6():
        OP_93(0x103, 0xFF79, 0x96)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_47B6)

    def lambda_47C3():
        OP_93(0x104, 0xFF79, 0x96)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_47C3)
    OP_97(0xD, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
    Fade(500)
    SetChrPos(0xD, 18000, 0, -8000, 90)
    SetChrFlags(0xD, 0x8000)
    OP_68(19030, 1500, -9110, 0)
    MoveCamera(29, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    OP_68(20030, 1500, -9110, 3000)
    OP_97(0xD, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
    ClearChrFlags(0xD, 0x8000)
    OP_0D()
    Fade(500)
    OP_68(27830, 5500, 7060, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    OP_0D()

    #C0207
    ChrTalk(
        0x101,
        (
            "#5P#0006Fうーん……\x01",
            "まさかこんな仕事まで\x01",
            "舞いこんでくるなんてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x104,
        (
            "#12P#0303F偉そうなカンジは気に食わねぇが……\x02\x03",

            "#0300Fま、困ってるのは確かっぽいし\x01",
            "やってやろうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x102,
        "#6P#0100Fじゃあ、ホームに行くとしましょうか。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【臨検官補佐求ム】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 28000, 4000, 8500, 180)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x10)
    OP_1B(0x0, 0x0, 0x22)
    OP_29(0x9, 0x1, 0x1)
    OP_4C(0xD, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_33_465B end

    def Function_34_49FC(): pass

    label("Function_34_49FC")

    EventBegin(0x1)

    #C0211
    ChrTalk(
        0x101,
        (
            "#0000F臨検官さんが２番ホームで\x01",
            "俺たちを待ってる。\x02\x03",

            "早く行ったほうがよさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 500, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_34_49FC end

    def Function_35_4A6C(): pass

    label("Function_35_4A6C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "←共和国方面行き・１番線ホーム\x01",
            "　　　共和国アルタイル市　３５分\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_35_4A6C end

    def Function_36_4AE4(): pass

    label("Function_36_4AE4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "帝国方面行き・２番線ホーム→\x01",
            "　　　　帝国ガレリア要塞　　３２分\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_36_4AE4 end

    def Function_37_4B5C(): pass

    label("Function_37_4B5C")

    TalkBegin(0xFF)
    SetChrName("")

    #A0214
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州周辺の\x01",
            "時刻表がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_37_4B5C end

    def Function_38_4B95(): pass

    label("Function_38_4B95")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※※　臨検官事務所　※※\x01",
            " 関係者以外の立ち入りを\x01",
            "      固く禁ずる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_4B95 end

    def Function_39_4C11(): pass

    label("Function_39_4C11")

    TalkBegin(0xFF)
    SetChrName("")

    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州周辺の\x01",
            "路線図がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_39_4C11 end

    SaveToFile()

Try(main)
