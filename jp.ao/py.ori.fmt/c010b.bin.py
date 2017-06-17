from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c010b.bin",                # FileName
        "c010b",                    # MapName
        "c010b",                    # Location
        0x0004,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 4, 0, 4, 0, 5],
    )

    BuildStringList((
        "c010b",                  # 0
        "ジーナ",                 # 1
        "コンテ老人",             # 2
        "アベル",                 # 3
        "ミミ",                   # 4
        "プルーナ",               # 5
        "リナリー",               # 6
        "ハース",                 # 7
        "サリー",                 # 8
        "警官",                   # 9
        "警官",                   # 10
        "コッペ",                 # 11
        "キーア",                 # 12
        "ツァイト",               # 13
        "シャーリィ",             # 14
        "猟兵ガレス",             # 15
        "車",                     # 16
        "ダミー",                 # 17
        "警官",                   # 18
        "ケイト巡査",             # 19
        "市民１",                 # 20
        "SE制御",                 # 21
        "中央広場",               # 22
        "西通り",                 # 23
        "行政区",                 # 24
        "住宅街",                 # 25
        "歓楽街",                 # 26
        "東通り",                 # 27
        "旧市街",                 # 28
        "港湾区",                 # 29
        "ＩＢＣ",                 # 30
        "駅前通り",               # 31
        "裏通り",                 # 32
        "ウルスラ間道",           # 33
        "東クロスベル街道",       # 34
        "西クロスベル街道",       # 35
        "マインツ山道",           # 36
        "オルキスタワー",         # 37
    ))

    AddCharChip((
        "chr/ch21300.itc",                   # 00
        "chr/ch20002.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20700.itc",                   # 03
        "chr/ch34600.itc",                   # 04
        "chr/ch22100.itc",                   # 05
        "chr/ch20500.itc",                   # 06
        "chr/ch26000.itc",                   # 07
        "chr/ch30000.itc",                   # 08
        "chr/ch39200.itc",                   # 09
    ))

    DeclNpc(12619,   0,       2160,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-6090,   150,     4449,    270,  325,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-6099,   0,       -9409,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-289,    0,       -10319,  225,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(850,     0,       17969,   90,   277,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(2539,    0,       17870,   270,  277,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(14130,   0,       340,     270,  261,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-6099,   0,       -9409,   90,   389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(13850,   0,       24000,   180,  385,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(10050,   0,       24000,   180,  385,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-22809,  1299,    -18829,  180,  389,  0x0, 0,   9,   0,   0,   2,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    236,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 45,  12.449999809265137,    27.34000015258789,     -1.0,                  625.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.2450000047683716,   -5.4679999351501465,   0.20000000298023224,   1.0])

    DeclActor(0,       0,       -1600,   1000,    0,       2500,    0,       0x007C, 0,  46, 0x0000)

    PlaceName(-5.449999809265137, 0.0, -2.7200000286102295, 0x0000, 0x0000, "中央広場")
    PlaceName(-70.54000091552734, 0.0, 1.7300000190734863, 0x0000, 0x0000, "西通り")
    PlaceName(21.290000915527344, 0.0, 85.38999938964844, 0x0000, 0x0000, "行政区")
    PlaceName(-130.92999267578125, 0.0, 75.48999786376953, 0x0000, 0x0000, "住宅街")
    PlaceName(-58.65999984741211, 0.0, 67.56999969482422, 0x0000, 0x0000, "歓楽街")
    PlaceName(74.98999786376953, 0.0, -25.489999771118164, 0x0000, 0x0000, "東通り")
    PlaceName(110.13999938964844, 0.0, -79.94000244140625, 0x0000, 0x0000, "旧市街")
    PlaceName(102.70999908447266, 0.0, 39.849998474121094, 0x0000, 0x0000, "港湾区")
    PlaceName(76.97000122070312, 0.0, 132.91000366210938, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(5.690000057220459, 0.0, -71.02999877929688, 0x0000, 0x0000, "駅前通り")
    PlaceName(-40.84000015258789, 0.0, 31.93000030517578, 0x0000, 0x0000, "裏通り")
    PlaceName(2.7200000286102295, 0.0, -101.72000122070312, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(128.4499969482422, 0.0, -11.630000114440918, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-121.02999877929688, 0.0, 0.25, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-115.08999633789062, 0.0, 99.25, 0x0000, 0x0000, "マインツ山道")
    PlaceName(15.0, 0.0, 216.75, 0x0000, 0x0000, "オルキスタワー")
    PlaceName(-27.229999542236328, 0.0, -16.579999923706055, 0x0000, 0x0051, "")
    PlaceName(25.989999771118164, 0.0, 9.15999984741211, 0x0000, 0x0054, "")
    PlaceName(-2.9700000286102295, 0.0, -24.5, 0x0000, 0x0057, "")
    PlaceName(-27.969999313354492, 0.0, 12.130000114440918, 0x0000, 0x0053, "")
    PlaceName(-7.670000076293945, 0.0, 35.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-57.91999816894531, 0.0, 7.179999828338623, 0x0000, 0x0053, "")
    PlaceName(-67.56999969482422, 0.0, 27.969999313354492, 0x0000, 0x0053, "")
    PlaceName(-43.810001373291016, 0.0, 59.650001525878906, 0x0000, 0x0052, "")
    PlaceName(-39.11000061035156, 0.0, 46.779998779296875, 0x0000, 0x0053, "")
    PlaceName(-30.440000534057617, 0.0, 38.36000061035156, 0x0000, 0x0053, "")
    PlaceName(-2.2300000190734863, 0.0, 108.6500015258789, 0x0000, 0x0051, "")
    PlaceName(108.6500015258789, 0.0, -25.489999771118164, 0x0000, 0x0052, "")
    PlaceName(91.81999969482422, 0.0, -115.08999633789062, 0x0000, 0x0053, "")
    PlaceName(78.94999694824219, 0.0, -96.7699966430664, 0x0000, 0x0053, "")

    ChipFrameInfo(1712, 0)                                       # 0

    ScpFunction((
        "Function_0_6B0",          # 00, 0
        "Function_1_760",          # 01, 1
        "Function_2_7AD",          # 02, 2
        "Function_3_7D8",          # 03, 3
        "Function_4_802",          # 04, 4
        "Function_5_8E5",          # 05, 5
        "Function_6_96D",          # 06, 6
        "Function_7_9C7",          # 07, 7
        "Function_8_AF7",          # 08, 8
        "Function_9_B51",          # 09, 9
        "Function_10_B91",         # 0A, 10
        "Function_11_BED",         # 0B, 11
        "Function_12_C53",         # 0C, 12
        "Function_13_D6D",         # 0D, 13
        "Function_14_DFE",         # 0E, 14
        "Function_15_E70",         # 0F, 15
        "Function_16_F0C",         # 10, 16
        "Function_17_1015",        # 11, 17
        "Function_18_10A2",        # 12, 18
        "Function_19_119B",        # 13, 19
        "Function_20_254F",        # 14, 20
        "Function_21_2585",        # 15, 21
        "Function_22_25C9",        # 16, 22
        "Function_23_260D",        # 17, 23
        "Function_24_2651",        # 18, 24
        "Function_25_268E",        # 19, 25
        "Function_26_26D2",        # 1A, 26
        "Function_27_2716",        # 1B, 27
        "Function_28_275A",        # 1C, 28
        "Function_29_279E",        # 1D, 29
        "Function_30_27EF",        # 1E, 30
        "Function_31_2851",        # 1F, 31
        "Function_32_28CA",        # 20, 32
        "Function_33_294D",        # 21, 33
        "Function_34_29D0",        # 22, 34
        "Function_35_2FAB",        # 23, 35
        "Function_36_31BC",        # 24, 36
        "Function_37_3295",        # 25, 37
        "Function_38_32E9",        # 26, 38
        "Function_39_34D1",        # 27, 39
        "Function_40_3697",        # 28, 40
        "Function_41_372E",        # 29, 41
        "Function_42_3738",        # 2A, 42
        "Function_43_4190",        # 2B, 43
        "Function_44_4360",        # 2C, 44
        "Function_45_4385",        # 2D, 45
        "Function_46_445F",        # 2E, 46
        "Function_47_45A5",        # 2F, 47
        "Function_48_45CF",        # 30, 48
        "Function_49_45F9",        # 31, 49
        "Function_50_4623",        # 32, 50
    ))


    def Function_0_6B0(): pass

    label("Function_0_6B0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6E8"),
        (1, "loc_6F4"),
        (2, "loc_700"),
        (3, "loc_70C"),
        (4, "loc_718"),
        (5, "loc_724"),
        (6, "loc_730"),
        (SWITCH_DEFAULT, "loc_73C"),
    )


    label("loc_6E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_6F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_700")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_70C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_718")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_724")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_730")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_73C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_748")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_75F")

    Return()

    # Function_0_6B0 end

    def Function_1_760(): pass

    label("Function_1_760")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AC")
    OP_95(0xFE, 11850, 0, -1800, 2000, 0x0)
    OP_95(0xFE, 11850, 0, 39440, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 30000, 0, -3010, 270)
    Jump("Function_1_760")

    label("loc_7AC")

    Return()

    # Function_1_760 end

    def Function_2_7AD(): pass

    label("Function_2_7AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D7")
    OP_94(0xFE, 0xFFFFA484, 0xFFFFB348, 0xFFFFA722, 0xFFFFB9BA, 0x3E8)
    Sleep(300)
    Jump("Function_2_7AD")

    label("loc_7D7")

    Return()

    # Function_2_7AD end

    def Function_3_7D8(): pass

    label("Function_3_7D8")

    SetMapObjFlags(0x17, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_7F2")
    ClearMapObjFlags(0x17, 0x2000000)
    Jump("loc_801")

    label("loc_7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_801")
    ClearMapObjFlags(0x17, 0x2000000)

    label("loc_801")

    Return()

    # Function_3_7D8 end

    def Function_4_802(): pass

    label("Function_4_802")

    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xF, -4240, 0, -7750, 225)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_871")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)
    Jump("loc_8E4")

    label("loc_871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_885")
    ClearScenarioFlags(0x22, 1)
    Event(0, 34)
    Jump("loc_8E4")

    label("loc_885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_899")
    ClearScenarioFlags(0x22, 2)
    Event(0, 35)
    Jump("loc_8E4")

    label("loc_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_8AD")
    ClearScenarioFlags(0x22, 3)
    Event(0, 38)
    Jump("loc_8E4")

    label("loc_8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_8C1")
    ClearScenarioFlags(0x22, 4)
    Event(0, 39)
    Jump("loc_8E4")

    label("loc_8C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_8D5")
    ClearScenarioFlags(0x22, 5)
    Event(0, 42)
    Jump("loc_8E4")

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_8E4")
    ClearScenarioFlags(0x22, 6)
    Event(0, 43)

    label("loc_8E4")

    Return()

    # Function_4_802 end

    def Function_5_8E5(): pass

    label("Function_5_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8FA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)

    label("loc_8FA")

    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFrame(0xFF, "black", 0x0, 0x1)
    SetMapObjFrame(0xFF, "nwindow", 0x0, 0x1)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96C")
    OP_1B(0x0, 0x0, 0x2F)
    OP_1B(0x1, 0x0, 0x30)
    OP_1B(0x3, 0x0, 0x31)

    label("loc_96C")

    Return()

    # Function_5_8E5 end

    def Function_6_96D(): pass

    label("Function_6_96D")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        "あら、もうこんな時間なのね。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "早くお家に帰って\x01",
            "ママのお手伝いをしないと。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_96D end

    def Function_7_9C7(): pass

    label("Function_7_9C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A86")

    #C0003
    ChrTalk(
        0xFE,
        (
            "おや、気付けばもうすっかり\x01",
            "日が暮れてしまっておるではないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "ほっほっ、これも通商会議の\x01",
            "空気にあてられたせいかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "婆さんが心配せん内に早く帰らんとな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AF3")

    label("loc_A86")


    #C0006
    ChrTalk(
        0xFE,
        (
            "おや、気付けばもうすっかり\x01",
            "日が暮れてしまっておるではないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "婆さんが心配せん内に早く帰らんとな。\x02",
    )

    CloseMessageWindow()

    label("loc_AF3")

    TalkEnd(0xFE)
    Return()

    # Function_7_9C7 end

    def Function_8_AF7(): pass

    label("Function_8_AF7")

    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0xFE,
        (
            "さてと、待たせてしまって\x01",
            "すまなかったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "それじゃ、早速行くとしようか。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_AF7 end

    def Function_9_B51(): pass

    label("Function_9_B51")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        (
            "ええ、早く行きましょう。\x01",
            "ミミも私もお腹ペコペコよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_B51 end

    def Function_10_B91(): pass

    label("Function_10_B91")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xFE,
        "外食、外食、今日は外食♪\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "ミミ、東通りのお店の\x01",
            "『ちゅーか』が食べたいのっ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_B91 end

    def Function_11_BED(): pass

    label("Function_11_BED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C02")
    Call(0, 12)
    Jump("loc_C4F")

    label("loc_C02")


    #C0013
    ChrTalk(
        0xFE,
        "ふーん、なるほどね～。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "（……この調子だと\x01",
            "  全然やってないわね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4F")

    TalkEnd(0xFE)
    Return()

    # Function_11_BED end

    def Function_12_C53(): pass

    label("Function_12_C53")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0015
    ChrTalk(
        0xC,
        (
            "そういえば、リナリーって\x01",
            "ジョギング続けてんの？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xD,
        (
            "え、あ、うん……\x01",
            "まあ、それなりにはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xD,
        (
            "無理してダイエットってのも\x01",
            "良くないって思ったから、\x01",
            "最近は気が向いたらだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xC,
        "ふ～ん、そうなんだ。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xC,
        (
            "（……この調子だと\x01",
            "  全然やってないわね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_12_C53 end

    def Function_13_D6D(): pass

    label("Function_13_D6D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D82")
    Call(0, 12)
    Jump("loc_DFA")

    label("loc_D82")


    #C0020
    ChrTalk(
        0xFE,
        (
            "き、気が向いたらって言っても\x01",
            "ちゃんと続けてはいるんだからね？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "えっと、それじゃあ、\x01",
            "今日は走って帰ろうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFA")

    TalkEnd(0xFE)
    Return()

    # Function_13_D6D end

    def Function_14_DFE(): pass

    label("Function_14_DFE")

    TalkBegin(0xFE)

    #C0022
    ChrTalk(
        0xFE,
        "さてと、今日もぼちぼち帰るかな。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "おかげ様で今日は人通りも多くて\x01",
            "一杯、風船を配ることができたよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_DFE end

    def Function_15_E70(): pass

    label("Function_15_E70")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E85")
    Call(0, 16)
    Jump("loc_F08")

    label("loc_E85")


    #C0024
    ChrTalk(
        0xFE,
        (
            "首脳たちをミシュラムに\x01",
            "送り届けるまで、この先は\x01",
            "通行止めとなります。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "支援課の皆さんにも、\x01",
            "ご理解とご協力をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F08")

    TalkEnd(0xFE)
    Return()

    # Function_15_E70 end

    def Function_16_F0C(): pass

    label("Function_16_F0C")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0x10, 0x0, 0)

    #C0026
    ChrTalk(
        0x10,
        (
            "支援課の皆さんに、\x01",
            "それにダドリー捜査官……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x0, 500)

    #C0027
    ChrTalk(
        0x11,
        (
            "首脳たちの観劇が終わるまで\x01",
            "この先は封鎖となりますが、\x01",
            "中に入られますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x10A,
        (
            "#00600Fいや、大丈夫だ。\x01",
            "引き続き警戒に当たってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x10,
        "了解です！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x11,
        "了解です！\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x0)
    OP_93(0x11, 0xB4, 0x0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x149, 1)
    Return()

    # Function_16_F0C end

    def Function_17_1015(): pass

    label("Function_17_1015")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102A")
    Call(0, 16)
    Jump("loc_109E")

    label("loc_102A")


    #C0031
    ChrTalk(
        0xFE,
        (
            "首脳たちの観劇が終わるまで、\x01",
            "歓楽街から港湾区までの一帯は\x01",
            "封鎖となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "ここは蟻の子一匹通しませんよ。\x02",
    )

    CloseMessageWindow()

    label("loc_109E")

    TalkEnd(0xFE)
    Return()

    # Function_17_1015 end

    def Function_18_10A2(): pass

    label("Function_18_10A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1185")

    #C0033
    ChrTalk(
        0x12,
        "にゃーご。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x10A,
        (
            "#00600F支援課で飼っている猫か。\x02\x03",

            "#00603F（なでなで……）\x01",
            "……お前も難儀な場所に\x01",
            "居ついたものだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x12,
        "にやぁ～～お……㈱\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00002F（ダドリーさん、\x01",
            "  意外と猫の扱いが上手いな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1197")

    label("loc_1185")


    #C0037
    ChrTalk(
        0x12,
        "にゃおん……\x02",
    )

    CloseMessageWindow()

    label("loc_1197")

    TalkEnd(0xFE)
    Return()

    # Function_18_10A2 end

    def Function_19_119B(): pass

    label("Function_19_119B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02710.itc", 0x1E)
    LoadChrToIndex("chr/ch08200.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("apl/ch51200.itc", 0x21)
    OP_68(9400, 1400, -5200, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 15800, 0, -4900, 270)
    SetChrPos(0x102, 16000, 0, -6500, 270)
    SetChrPos(0x104, 16700, 0, -3400, 270)
    SetChrPos(0x109, 18000, 0, -3800, 270)
    SetChrPos(0x105, 18800, 0, -4400, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrPos(0x14, 17500, 0, -7000, 270)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    SetChrPos(0x13, 17000, 0, -5200, 270)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0x18, 0x80)
    OP_90(0x18, -12500, -4200, -16400, 225)
    SetChrFlags(0x8, 0x80)

    def lambda_12D7():
        OP_97(0x101, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12D7)
    Sleep(50)

    def lambda_12F4():
        OP_97(0x102, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_12F4)
    Sleep(50)

    def lambda_1311():
        OP_97(0x104, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1311)
    Sleep(50)

    def lambda_132E():
        OP_97(0x14, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_132E)
    Sleep(50)

    def lambda_134B():
        OP_97(0x13, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_134B)
    Sleep(50)

    def lambda_1368():
        OP_97(0x109, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1368)
    Sleep(50)

    def lambda_1385():
        OP_97(0x105, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1385)
    SetCameraDistance(14700, 3500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_6F(0x79)
    TurnDirection(0x101, 0x13, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 2)), scpexpr(EXPR_END)), "loc_141B")

    #C0038
    ChrTalk(
        0x101,
        (
            "#6P#00000Fそういえば、明日はシズクちゃんと\x01",
            "デパートの屋上に行くんだったっけ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1464")

    label("loc_141B")


    #C0039
    ChrTalk(
        0x101,
        (
            "#6P#00000Fそっか、明日はシズクちゃんと\x01",
            "デパートの屋上に行くんだな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1464")


    def lambda_1469():
        TurnDirection(0x102, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1469)
    Sleep(50)

    def lambda_1479():
        TurnDirection(0x104, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1479)
    Sleep(50)

    def lambda_1489():
        TurnDirection(0x109, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1489)
    Sleep(50)

    def lambda_1499():
        TurnDirection(0x105, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1499)
    Sleep(50)

    def lambda_14A9():
        TurnDirection(0x14, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_14A9)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x14, 0)
    SetChrSubChip(0x14, 0x5)

    #C0040
    ChrTalk(
        0x13,
        (
            "#11P#01109Fうんっ！\x01",
            "じょまくしき、だっけ？\x02\x03",

            "#01110Fいっしょに見ようって\x01",
            "ヤクソクしたのー。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#12P#00109Fふふっ、そうなんだ。\x02\x03",

            "#00105Fあら、でもシズクちゃん、\x01",
            "除幕式の様子を見るのは……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x102, 500)

    #C0042
    ChrTalk(
        0x13,
        (
            "#5P#01100Fえっとね、ふんいきだけでも\x01",
            "感じたいって言ってたよー。\x02\x03",

            "どんな感じかは\x01",
            "キーアが教えてあげるんだー。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#6P#00002Fそっか……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        "#5P#00300F#30W……あの子も健気だよな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x13, 0x104, 500)

    #C0045
    ChrTalk(
        0x13,
        (
            "#12P#01105Fねえねえ、ランディー。\x02\x03",

            "#01112Fさっきから元気ないねー？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(9400, 1400, -4700, 1000)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_16E2():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_16E2)
    Sleep(50)

    def lambda_16F2():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_16F2)
    Sleep(50)

    def lambda_1702():
        TurnDirection(0x104, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1702)
    Sleep(50)

    def lambda_1712():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1712)
    Sleep(50)

    def lambda_1722():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1722)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(100)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    BeginChrThread(0x104, 3, 0, 20)
    Sleep(300)

    #C0046
    ChrTalk(
        0x104,
        "#5P#00309Fハハ、そんな事ねぇって。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    SetChrSubChip(0x104, 0x5)
    Sleep(110)
    SetChrSubChip(0x104, 0x6)
    Sleep(110)
    SetChrSubChip(0x104, 0x7)
    Sound(822, 0, 100, 0)
    OP_63(0x104, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1300)
    SetChrSubChip(0x104, 0x8)
    Sleep(110)
    SetChrSubChip(0x104, 0x9)
    Sleep(110)
    SetChrSubChip(0x104, 0xA)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0047
    ChrTalk(
        0x104,
        (
            "#5P#00303Fシャキーン、ホレ見ろ！\x02\x03",

            "#00302Fいつも通りのクールで\x01",
            "ハンサムなナイスガイだろ？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x104)

    #C0048
    ChrTalk(
        0x13,
        "#12P#01111Fないすがいー？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        (
            "#11P#10112F先輩、ナイスガイは\x01",
            "さすがに死語なんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x105,
        (
            "#10302F#11Pフフ、空元気も\x01",
            "元気のうちってことかな？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0xB)
    Sleep(90)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sleep(150)
    TurnDirection(0x104, 0x109, 500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0051
    ChrTalk(
        0x104,
        (
            "#5P#00301Fええい！\x01",
            "混ぜっ返すな、後輩ども。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#12P#00012Fはは……\x02\x03",

            "#00000Fでもランディ、あまり一人で\x01",
            "思いつめないでくれよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#12P#00106Fそうね、こういう時のために\x01",
            "私たちがいるんだから……\x02\x03",

            "#00101Fくれぐれも自分だけで\x01",
            "何とかしようと思わないでね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x13, 500)

    #C0054
    ChrTalk(
        0x104,
        (
            "#5P#00304Fハハ、分かってるって。\x02\x03",

            "#00308F──ただまあ一応、\x01",
            "俺の身内でもある連中だ。\x02\x03",

            "#00300F一度、腹を割って\x01",
            "話してみようとは思ってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        "#12P#00105Fそれは……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#12P#00001F……危険じゃないのか？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_END)), "loc_1BB9")

    #C0057
    ChrTalk(
        0x104,
        (
            "#5P#00304Fま、勝手知ったるってヤツだ。\x02\x03",

            "#00301Fしかし叔父貴のヤツ、\x01",
            "話があるとか抜かしながら\x01",
            "全然、音沙汰がねぇんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#12P#00001Fああ、昼に訪ねてみた時も\x01",
            "不在だったみたいだしな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8C")

    label("loc_1BB9")


    #C0059
    ChrTalk(
        0x104,
        (
            "#5P#00304Fま、勝手知ったるってヤツだ。\x02\x03",

            "#00301Fしかし叔父貴のヤツ、\x01",
            "話があるとか抜かしながら\x01",
            "全然、音沙汰がねぇんだよな。\x02\x03",

            "ルバーチェ跡を訪ねても\x01",
            "居留守を使ってるみてぇだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#12P#00001Fそうなのか……\x02",
    )

    CloseMessageWindow()

    label("loc_1C8C")


    def lambda_1C91():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C91)

    def lambda_1C9E():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C9E)
    Sleep(50)

    def lambda_1CAE():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1CAE)
    Sleep(50)

    def lambda_1CBE():
        OP_93(0x14, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1CBE)
    Sleep(50)

    def lambda_1CCE():
        OP_93(0x13, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1CCE)
    Sleep(50)

    def lambda_1CDE():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1CDE)
    Sleep(50)

    def lambda_1CEE():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1CEE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    SetCameraDistance(17500, 3000)

    def lambda_1D1C():
        OP_97(0x101, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D1C)
    Sleep(50)

    def lambda_1D39():
        OP_97(0x102, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D39)
    Sleep(50)

    def lambda_1D56():
        OP_97(0x104, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D56)
    Sleep(50)

    def lambda_1D73():
        OP_97(0x14, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1D73)
    Sleep(50)

    def lambda_1D90():
        OP_97(0x13, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1D90)
    Sleep(50)

    def lambda_1DAD():
        OP_97(0x109, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DAD)
    Sleep(50)

    def lambda_1DCA():
        OP_97(0x105, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1DCA)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0x2, 0x0)
    OP_6B(0x18)
    OP_68(-12500, -3000, -16400, 0)
    MoveCamera(33, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x101, -13100, -4200, -17800, 225)
    SetChrPos(0x104, -13900, -4200, -17000, 225)
    SetChrPos(0x13, -12100, -4200, -16800, 225)
    SetChrPos(0x109, -12900, -4200, -16000, 225)
    SetChrPos(0x102, -11100, -4200, -15800, 225)
    SetChrPos(0x105, -11900, -4200, -15000, 225)
    SetChrPos(0x14, -13900, -4200, -18700, 225)
    BeginChrThread(0x14, 3, 0, 28)
    BeginChrThread(0x18, 3, 0, 24)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 22)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 23)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 27)
    MoveCamera(40, 23, 0, 10000)
    SetCameraDistance(16000, 10000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0061
    ChrTalk(
        0x104,
        (
            "#00306F#5Pふう、さすがに腹が減ったな。\x02\x03",

            "#00305Fそういや課長は、\x01",
            "今夜は遅くなるんだったよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00000F#11Pああ、明日の除幕式の段取りが\x01",
            "長引いてるみたいだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        (
            "#00102F#11Pふふ、だったら\x01",
            "今日は外食で済ませるのも\x01",
            "いいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        "#10109F#5Pあ、たまにはいいですね。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x105,
        (
            "#10302F#11Pすると、そこのレストランか\x01",
            "龍老飯店あたりになるかな？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)

    #C0066
    ChrTalk(
        0x101,
        (
            "#6P#00002Fああ、荷物を置いたら\x01",
            "みんなで出かけようか──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x105, 3)
    OP_6B(0xFF)
    OP_6F(0x79)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    #Sound(2937, 255, 100, 0)    #voice#Zeit

    #C0067
    ChrTalk(
        0x14,
        "#01201F#40W#11Pグルルルルル……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-26700, -7000, -24400, 2000)
    SetCameraDistance(17000, 2000)

    def lambda_21A6():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21A6)
    Sleep(50)

    def lambda_21B6():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_21B6)
    Sleep(50)

    def lambda_21C6():
        OP_93(0x13, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_21C6)
    Sleep(50)

    def lambda_21D6():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_21D6)
    Sleep(50)

    def lambda_21E6():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_21E6)
    Sleep(50)

    def lambda_21F6():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_21F6)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    def lambda_221B():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_221B)
    OP_6F(0x79)

    def lambda_2236():
        OP_97(0x101, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2236)
    Sleep(100)

    def lambda_2253():
        OP_97(0x104, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2253)
    Sleep(100)

    def lambda_2270():
        OP_97(0x13, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2270)
    Sleep(100)

    def lambda_228D():
        OP_97(0x109, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_228D)
    Sleep(100)

    def lambda_22AA():
        OP_97(0x102, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_22AA)
    Sleep(100)

    def lambda_22C7():
        OP_97(0x105, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_22C7)
    WaitChrThread(0x104, 0)

    def lambda_22E5():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_22E5)
    WaitChrThread(0x109, 0)

    def lambda_22F6():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_22F6)

    #C0068
    ChrTalk(
        0x101,
        "#11P#00001Fツァイト？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#00105F#11Pどうしたの？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x13,
        (
            "#12P#01105Fんー、なんかお客さんが\x01",
            "来てるって言ってるよー？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#11P#00005Fお客さん？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0x104, 0x13B, 0x1F4)
    Sleep(300)

    #C0072
    ChrTalk(
        0x104,
        "#11P#00311F#40W………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_23D3():
        OP_95(0xFE, -28500, -8200, -22800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23D3)
    Sleep(500)

    def lambda_23F0():

        label("loc_23F0")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_23F0")

    QueueWorkItem2(0x101, 2, lambda_23F0)
    Sleep(100)

    def lambda_2405():

        label("loc_2405")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_2405")

    QueueWorkItem2(0x109, 2, lambda_2405)

    def lambda_2417():

        label("loc_2417")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_2417")

    QueueWorkItem2(0x13, 2, lambda_2417)
    Sleep(50)

    def lambda_242C():

        label("loc_242C")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_242C")

    QueueWorkItem2(0x102, 2, lambda_242C)

    def lambda_243E():

        label("loc_243E")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_243E")

    QueueWorkItem2(0x105, 2, lambda_243E)
    WaitChrThread(0x104, 1)

    def lambda_2454():
        OP_95(0xFE, -28500, -8200, -19800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2454)
    Sleep(100)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    Sleep(400)

    #C0073
    ChrTalk(
        0x101,
        "#11P#00011Fランディ？\x02",
    )


    def lambda_24A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_24A9)
    WaitChrThread(0x104, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x13, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x105,
        "#10301F#11P……とにかく入ろうか。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    BeginChrThread(0x101, 3, 0, 29)
    Sleep(400)
    BeginChrThread(0x109, 3, 0, 29)
    Sleep(400)
    BeginChrThread(0x13, 3, 0, 29)
    Sleep(400)
    BeginChrThread(0x105, 3, 0, 29)
    Sleep(400)
    BeginChrThread(0x102, 3, 0, 29)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetScenarioFlags(0x22, 1)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_119B end

    def Function_20_254F(): pass

    label("Function_20_254F")

    SetChrSubChip(0x104, 0x2)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    Sleep(100)
    SetChrSubChip(0x104, 0x4)
    Sleep(100)
    SetChrSubChip(0x104, 0x5)
    Sleep(100)
    SetChrSubChip(0x104, 0x4)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    Sleep(100)
    SetChrSubChip(0x104, 0x4)
    Sleep(100)
    SetChrSubChip(0x104, 0x5)
    Return()

    # Function_20_254F end

    def Function_21_2585(): pass

    label("Function_21_2585")


    def lambda_258A():
        OP_95(0xFE, -20000, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_258A)
    WaitChrThread(0xFE, 1)

    def lambda_25A8():
        OP_95(0xFE, -23800, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25A8)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_21_2585 end

    def Function_22_25C9(): pass

    label("Function_22_25C9")


    def lambda_25CE():
        OP_95(0xFE, -20000, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25CE)
    WaitChrThread(0xFE, 1)

    def lambda_25EC():
        OP_95(0xFE, -23800, -8200, -23700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25EC)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_22_25C9 end

    def Function_23_260D(): pass

    label("Function_23_260D")


    def lambda_2612():
        OP_95(0xFE, -20000, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2612)
    WaitChrThread(0xFE, 1)

    def lambda_2630():
        OP_95(0xFE, -23000, -8200, -25700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2630)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_23_260D end

    def Function_24_2651(): pass

    label("Function_24_2651")


    def lambda_2656():
        OP_95(0xFE, -20000, -8200, -24400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2656)
    WaitChrThread(0xFE, 1)

    def lambda_2674():
        OP_95(0xFE, -22700, -8200, -24400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2674)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_2651 end

    def Function_25_268E(): pass

    label("Function_25_268E")


    def lambda_2693():
        OP_95(0xFE, -20000, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2693)
    WaitChrThread(0xFE, 1)

    def lambda_26B1():
        OP_95(0xFE, -22400, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26B1)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_25_268E end

    def Function_26_26D2(): pass

    label("Function_26_26D2")


    def lambda_26D7():
        OP_95(0xFE, -20000, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26D7)
    WaitChrThread(0xFE, 1)

    def lambda_26F5():
        OP_95(0xFE, -21600, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26F5)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_26_26D2 end

    def Function_27_2716(): pass

    label("Function_27_2716")


    def lambda_271B():
        OP_95(0xFE, -20000, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_271B)
    WaitChrThread(0xFE, 1)

    def lambda_2739():
        OP_95(0xFE, -21600, -8200, -23700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2739)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_27_2716 end

    def Function_28_275A(): pass

    label("Function_28_275A")


    def lambda_275F():
        OP_95(0xFE, -20000, -8200, -25100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_275F)
    WaitChrThread(0xFE, 1)

    def lambda_277D():
        OP_95(0xFE, -28500, -8200, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_277D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_28_275A end

    def Function_29_279E(): pass

    label("Function_29_279E")


    def lambda_27A3():
        OP_95(0xFE, -28500, -8200, -22800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27A3)
    WaitChrThread(0xFE, 1)

    def lambda_27C1():
        OP_95(0xFE, -28500, -8200, -19800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27C1)
    Sleep(500)

    def lambda_27DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27DE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_279E end

    def Function_30_27EF(): pass

    label("Function_30_27EF")


    def lambda_27F4():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27F4)
    WaitChrThread(0xFE, 1)

    def lambda_2812():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2812)
    WaitChrThread(0xFE, 1)

    def lambda_2830():
        OP_95(0xFE, 2500, 0, -14700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2830)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_30_27EF end

    def Function_31_2851(): pass

    label("Function_31_2851")


    def lambda_2856():
        OP_95(0xFE, -19800, -4200, -23800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2856)
    WaitChrThread(0xFE, 1)

    def lambda_2874():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2874)
    WaitChrThread(0xFE, 1)

    def lambda_2892():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2892)
    WaitChrThread(0xFE, 1)

    def lambda_28B0():
        OP_95(0xFE, 1700, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28B0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_31_2851 end

    def Function_32_28CA(): pass

    label("Function_32_28CA")

    Sleep(500)

    def lambda_28D2():
        OP_95(0xFE, -19800, -4200, -23800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28D2)
    WaitChrThread(0xFE, 1)

    def lambda_28F0():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28F0)
    WaitChrThread(0xFE, 1)

    def lambda_290E():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_290E)
    WaitChrThread(0xFE, 1)

    def lambda_292C():
        OP_95(0xFE, 900, 0, -16000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_292C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_32_28CA end

    def Function_33_294D(): pass

    label("Function_33_294D")

    Sleep(800)

    def lambda_2955():
        OP_95(0xFE, -19800, -4200, -23800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2955)
    WaitChrThread(0xFE, 1)

    def lambda_2973():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2973)
    WaitChrThread(0xFE, 1)

    def lambda_2991():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2991)
    WaitChrThread(0xFE, 1)

    def lambda_29AF():
        OP_95(0xFE, 600, 0, -17200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29AF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_33_294D end

    def Function_34_29D0(): pass

    label("Function_34_29D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    LoadChrToIndex("chr/ch42900.itc", 0x1F)
    SetChrPos(0x101, -22100, -8200, -23800, 90)
    SetChrPos(0x104, -20600, -8200, -23800, 90)
    SetChrPos(0x105, -23600, -8200, -23800, 90)
    SetChrPos(0x102, -22000, -8200, -20000, 0)
    SetChrPos(0x109, -22000, -8200, -20000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x4)
    SetChrPos(0x15, -19800, -4200, -23800, 0)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 4700, 500, -16800, 270)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x16, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x80)
    OP_78(0x16, 0x17)
    OP_49()
    SetChrPos(0x17, 5800, 0, -16500, 0)
    OP_D5(0x17, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x1000)
    OP_74(0x16, 0x1E)
    OP_70(0x16, 0x1)
    OP_68(-16500, -3900, -20500, 0)
    MoveCamera(5, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    BeginChrThread(0x15, 3, 0, 30)
    BeginChrThread(0x104, 3, 0, 31)
    BeginChrThread(0x101, 3, 0, 32)
    BeginChrThread(0x105, 3, 0, 33)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(3700, 1300, -16800, 12500)
    MoveCamera(35, 27, 0, 12500)
    SetCameraDistance(15000, 12500)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    #C0075
    ChrTalk(
        0x101,
        "#00011Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x105,
        (
            "#6P#10305Fたしかラインフォルト社の\x01",
            "防弾リムジンだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        (
            "#6P#00303Fフン、さっそく\x01",
            "こんな代物まで買ったのか。\x02\x03",

            "#00302Fさすがに景気がいいじゃねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x15,
        (
            "#5P#04609Fあはは、おかげさまで\x01",
            "ガッポリ稼いでるからねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(462, 0, 100, 0)
    OP_71(0x16, 0xF1, 0x10E, 0x0, 0x0)
    OP_79(0x16)
    OP_68(3200, 1200, -16800, 1000)
    ClearChrFlags(0x16, 0x80)

    def lambda_2C9C():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFBE60, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2C9C)

    def lambda_2CB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2CB6)
    WaitChrThread(0x16, 1)
    TurnDirection(0x16, 0x15, 500)

    #C0079
    ChrTalk(
        0x16,
        "#11Pシャーリィ様、お疲れさまです。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x104, 500)
    Sleep(300)

    #C0080
    ChrTalk(
        0x16,
        (
            "#11Pそれと若──\x01",
            "ご無沙汰しておりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        (
            "#6P#00300Fガレス……久しぶりだな。\x02\x03",

            "#00306Fそれはともかく、\x01",
            "さすがに若ってのはよせよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x16,
        (
            "#11P……バルデル様の件、\x01",
            "お聞きになったかと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x16,
        (
            "#11P本当に惜しい方を……\x01",
            "心よりお悔やみを申し上げます。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        "#6P#00308F………ああ。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x15,
        (
            "#5P#04604F湿っぽい話はナシナシ！\x01",
            "今夜はパーッと行くんだから！\x02\x03",

            "#04602Fささ、乗って！\x01",
            "お兄さんたちも早く早く！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E96():
        OP_95(0xFE, 3200, 0, -18400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2E96)
    WaitChrThread(0x16, 1)
    TurnDirection(0x16, 0x104, 500)

    #C0086
    ChrTalk(
        0x101,
        (
            "#00001Fああ……\x01",
            "それじゃあ遠慮なく。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x105,
        "#6P#10304Fフフ、お邪魔するよ。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14500, 2000)
    FadeToDark(2000, 0, -1)

    def lambda_2F1C():
        OP_95(0xFE, 3700, 0, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2F1C)
    Sleep(500)

    def lambda_2F39():
        OP_95(0xFE, 3700, 0, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F39)
    WaitChrThread(0x104, 1)

    def lambda_2F57():
        OP_95(0xFE, 4700, 500, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2F57)

    def lambda_2F71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2F71)

    def lambda_2F82():
        OP_95(0xFE, 3700, 0, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2F82)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x104, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("e0111", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_29D0 end

    def Function_35_2FAB(): pass

    label("Function_35_2FAB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30600.itc", 0x1E)
    SoundLoad(835)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrChipByIndex(0x19, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x17, 0x17)
    OP_49()
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFrame(0x17, "chukin", 0x0, 0x1)
    OP_71(0x17, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0xF, -6100, 0, -9410, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -5000, 0, -9410, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0x1A, -1200, 0, -2400, 180)
    BeginChrThread(0x1A, 0, 0, 0)
    SetChrPos(0x19, -18700, 0, 3950, 180)
    BeginChrThread(0x19, 0, 0, 36)
    SetChrPos(0x17, 4700, 0, -30500, 90)
    OP_D5(0x17, 0x0, 0x15F90, 0x0, 0x0)
    BeginChrThread(0x17, 0, 0, 37)
    OP_68(-1000, 3500, 11000, 0)
    MoveCamera(40, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    OP_68(-1000, 1500, 11000, 10000)
    MoveCamera(23, 6, 0, 10000)
    SetCameraDistance(34500, 10000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    Sound(457, 0, 70, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 4)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_2FAB end

    def Function_36_31BC(): pass

    label("Function_36_31BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3294")
    OP_95(0xFE, -15910, 0, 1150, 1000, 0x0)
    OP_95(0xFE, -290, 0, 16770, 1000, 0x0)
    OP_95(0xFE, -300, 800, 24250, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xD7, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -290, 0, 16770, 1000, 0x0)
    OP_95(0xFE, -15910, 0, 1150, 1000, 0x0)
    OP_95(0xFE, -18720, 0, 3960, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    Jump("Function_36_31BC")

    label("loc_3294")

    Return()

    # Function_36_31BC end

    def Function_37_3295(): pass

    label("Function_37_3295")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 4700, 0, -30500)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 8580, 0, 4180)
    OP_9F(0x1, 11000, 0, 30000)
    OP_9F(0x1, 11000, 0, 60000)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_37_3295 end

    def Function_38_32E9(): pass

    label("Function_38_32E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30600.itc", 0x1E)
    SoundLoad(835)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x17, 0x17)
    OP_49()
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFrame(0x17, "chukin", 0x0, 0x1)
    OP_71(0x17, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x1A, -1200, 0, -2400, 180)
    BeginChrThread(0x1A, 0, 0, 0)
    SetChrPos(0xA, -6100, 0, -9400, 90)
    SetChrPos(0xB, -5000, 0, -9400, 270)
    SetChrPos(0x17, 15000, 0, -5000, 270)
    OP_D5(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(25, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_68(-1000, 1500, 11000, 7000)
    MoveCamera(23, 5, 0, 7000)
    Sound(458, 0, 80, 0)

    def lambda_3452():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3452)
    StopSound(835, 1000, 100)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 6)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_32E9 end

    def Function_39_34D1(): pass

    label("Function_39_34D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23400.itc", 0x1E)
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
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetMapObjFlags(0x0, 0x4)
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
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFrame(0xFF, "white", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lwindow", 0x0, 0x1)
    SetMapObjFrame(0xFF, "black", 0x1, 0x1)
    SetMapObjFrame(0xFF, "nwindow", 0x1, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x1B, 1500, 0, -4700, 270)
    BeginChrThread(0x1B, 1, 0, 40)
    OP_68(-15350, 1800, 5500, 0)
    MoveCamera(10, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    OP_68(3000, 1800, -6000, 12000)
    MoveCamera(45, 5, 0, 12000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x1C, 1, 0, 41)
    Sleep(10000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 7)
    NewScene("c012B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_39_34D1 end

    def Function_40_3697(): pass

    label("Function_40_3697")

    OP_63(0xFE, 0x0, 1850, 0x26, 0x27, 0xFA, 0x0)

    label("loc_36A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_372D")
    OP_9B(0x1, 0xFE, 0x28, 0x3E8, 0x7D0, 0x0)

    def lambda_36C8():
        OP_A6(0xFE, 0x1E, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_36C8)
    OP_9B(0x1, 0xFE, 0x37, 0x1F4, 0x3E8, 0x0)
    Sleep(1500)
    OP_9B(0x1, 0xFE, 0xFFD3, 0x5DC, 0x7D0, 0x0)

    def lambda_3702():
        OP_A6(0xFE, 0x1E, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3702)
    OP_9B(0x1, 0xFE, 0xFFD3, 0x1F4, 0x3E8, 0x0)
    Sleep(2000)
    Jump("loc_36A9")

    label("loc_372D")

    Return()

    # Function_40_3697 end

    def Function_41_372E(): pass

    label("Function_41_372E")

    Sleep(3000)
    Sound(1012, 0, 80, 0)
    Return()

    # Function_41_372E end

    def Function_42_3738(): pass

    label("Function_42_3738")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51425.itc", 0x1E)
    LoadChrToIndex("apl/ch51443.itc", 0x1F)
    LoadChrToIndex("apl/ch51426.itc", 0x20)
    SoundLoad(2916)
    SoundLoad(2760)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_68(-28700, -7200, -22000, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(13500, 0)
    SetChrPos(0x101, -22000, -8200, -20000, 0)
    SetChrPos(0x102, -22000, -8200, -20000, 0)
    SetChrPos(0x103, -22000, -8200, -20000, 0)
    SetChrPos(0x109, -22000, -8200, -20000, 0)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, -28700, -8200, -20000, 180)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x10)
    SetChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    SetChrFlags(0x105, 0x40)
    SetChrPos(0x105, -21000, -8200, -22800, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
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
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFrame(0xFF, "white", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lwindow", 0x0, 0x1)
    SetMapObjFrame(0xFF, "black", 0x1, 0x1)
    SetMapObjFrame(0xFF, "nwindow", 0x1, 0x1)
    SetCameraDistance(15000, 3000)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(103, 0, 70, 0)
    ClearMapObjFlags(0xF, 0x10)
    OP_71(0xF, 0x0, 0xA, 0x0, 0x0)
    OP_79(0xF)

    def lambda_3950():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA2A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3950)

    def lambda_396A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_396A)
    WaitChrThread(0x104, 1)
    Sound(104, 0, 70, 0)
    OP_71(0xF, 0xA, 0x0, 0x0, 0x0)
    OP_79(0xF)
    SetMapObjFlags(0xF, 0x10)
    OP_C9(0x0, 0x80000000)

    #N0088
    NpcTalk(
        0x105,
        "少年の声",
        "#2916V#30W──行くのかい？\x02",
    )

    CloseMessageWindow()
    OP_24(0xB64)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0089
    ChrTalk(
        0x104,
        "#5P#00308F#2760V#30Wお前か……\x02",
    )

    CloseMessageWindow()
    OP_24(0xAC8)
    OP_C9(0x1, 0x80000000)
    VolumeBGM(0x64, 0x64)
    PlayBGM("ed7568", 0)
    OP_68(-22350, -7200, -23350, 2000)
    MoveCamera(31, 13, 0, 2000)
    SetCameraDistance(13000, 2000)
    TurnDirection(0x104, 0x105, 350)
    OP_6F(0x79)
    Sleep(300)

    #C0090
    ChrTalk(
        0x104,
        (
            "#00301F#5P#Nったく、なんでこんな夜更けに\x01",
            "起きてやがるんだっつーの。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_3A95():
        OP_96(0xFE, 0xFFFFA36C, 0xFFFFDFF8, 0xFFFFA2A4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A95)
    Sleep(1000)
    OP_68(-21400, -7200, -22930, 2500)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetCameraDistance(12000, 40000)

    #C0091
    ChrTalk(
        0x105,
        (
            "#10302F#5Pフフ、行きつけのバーに\x01",
            "ちょっと引っ掛けに行っててね。\x02\x03",

            "#10306Fま、僕はこういう性格だし\x01",
            "別になんとも思わないけど……\x02\x03",

            "#10301Fさすがにみんな、怒るんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        (
            "#6P#00306F……だろうな。\x02\x03",

            "#00301Fだが──こいつは俺の問題だ。\x02\x03",

            "叔父貴やシャーリィは関係ねぇ。\x02\x03",

            "ましてやロイドたちを\x01",
            "巻き込んでいいわけがねぇ。\x02\x03",

            "#00303F俺は……俺自身のケリを\x01",
            "付けるためにここを出て行く。\x02\x03",

            "#00300Fただ、それだけの話だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x105,
        (
            "#10308F#5Pふぅん、まあいいけど。\x02\x03",

            "#10306F君といい、ヴァルドといい……\x01",
            "男ってのは馬鹿ばっかりだよね。\x02\x03",

            "#10302Fどうしてそんな不器用にしか\x01",
            "生きられないんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        (
            "#6P#00306Fほっとけっつーの。\x02\x03",

            "#00305F……しかしお前……\x01",
            "前から聞きたいと思ってたんだが。\x02\x03",

            "#00302F本当のところ、どっち#6R㈲　㈲　㈲#なんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x105,
        (
            "#10304F#5Pフフ、何を言ってるのか\x01",
            "サッパリ分からないね。\x02\x03",

            "#10300F君のもう一つの推測については\x01",
            "当たってるとは思うけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0096
    ChrTalk(
        0x104,
        (
            "#6P#00303F……なるほどな。\x02\x03",

            "#00311F昔、何度かやり合った連中と\x01",
            "似た匂いを感じてたんだが……\x02\x03",

            "あの娘と初対面っぽかったのも\x01",
            "フリだったってわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x105,
        (
            "#10304F#5Pフフ、そうなるかな？\x02\x03",

            "#10302F──黙ってくれていたお礼に\x01",
            "明日の朝、しらばっくれてあげるよ。\x02\x03",

            "好きなように暴れてくるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        "#6P#00304Fああ……恩に着る。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x104, 0x7)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    Sleep(80)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    SetCameraDistance(12000, 2000)
    OP_68(-20360, -7200, -22560, 2500)

    def lambda_3FBE():

        label("loc_3FBE")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_3FBE")

    QueueWorkItem2(0x104, 3, lambda_3FBE)

    def lambda_3FD0():
        OP_95(0xFE, -20000, -8200, -23900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3FD0)
    Sleep(800)
    SetChrSubChip(0x105, 0x1)
    WaitChrThread(0x104, 1)
    EndChrThread(0x104, 0x3)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)

    def lambda_4010():
        OP_95(0xFE, -13000, -4200, -17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4010)
    Sleep(500)
    SetChrSubChip(0x105, 0x2)
    Sleep(500)
    OP_6F(0x79)
    OP_68(-20360, -6600, -23560, 2000)
    WaitChrThread(0x104, 1)

    def lambda_404B():
        OP_95(0xFE, 0, 0, -17000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_404B)
    Sleep(1000)
    OP_6F(0x79)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x105)
    Sleep(500)

    #C0099
    ChrTalk(
        0x105,
        (
            "#5P#10306F……ま、彼が抜けると\x01",
            "ちょっと戦力が不安かな？\x02\x03",

            "#10308F場合によったらアッバスに\x01",
            "フォローに回ってもらうか……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(12500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x104, 0x1)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x105, 0x10)
    ClearChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x20)
    ClearChrFlags(0x105, 0x40)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x3, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x23, 2)
    NewScene("c0120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_3738 end

    def Function_43_4190(): pass

    label("Function_43_4190")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02750.itc", 0x1E)
    SoundLoad(868)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x14, -28800, -8200, -23050, 180)
    BeginChrThread(0x14, 0, 0, 44)
    OP_68(7000, 7500, 11000, 0)
    MoveCamera(35, -5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_68(5000, 2500, 11000, 7000)
    MoveCamera(30, 5, 0, 7000)
    Sound(868, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-28700, -6900, -21200, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18000, 0)
    MoveCamera(40, 20, 0, 4000)
    SetCameraDistance(15000, 4000)
    StopSound(868, 1000, 20)
    StopBGM(0x1388)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7560", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x230), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(14000, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 0)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_4190 end

    def Function_44_4360(): pass

    label("Function_44_4360")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4384")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x2, 0x1)
    Jump("Function_44_4360")

    label("loc_4384")

    Return()

    # Function_44_4360 end

    def Function_45_4385(): pass

    label("Function_45_4385")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4399")
    Call(0, 16)
    Jump("loc_4448")

    label("loc_4399")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0x10, 0x0, 0)
    TurnDirection(0x11, 0x0, 0)

    #C0100
    ChrTalk(
        0x10,
        (
            "首脳たちをミシュラムに\x01",
            "送り届けるまで、この先は\x01",
            "通行止めとなります。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x10,
        (
            "支援課の皆さんにも、\x01",
            "ご理解とご協力をお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x0)
    OP_93(0x11, 0xB4, 0x0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)

    label("loc_4448")

    Sleep(50)
    SetChrPos(0x0, 11850, 0, 22430, 180)
    EventEnd(0x4)
    Return()

    # Function_45_4385 end

    def Function_46_445F(): pass

    label("Function_46_445F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0102
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "       《クロスベルの鐘》\x01",
            "Ｓ１１８５、クロスベル自治州で\x01",
            "発掘された巨大な鐘。\x01",
            "出土した遺跡の状況から\x01",
            "中世の頃の物と考えられている。\x01",
            "複数の金属から成り、\x01",
            "打つと心地よい低音を響かせる。\x02",
        )
    )

    CloseMessageWindow()

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当時の有力者によって\x01",
            "作られたと推察されているが、\x01",
            "その用途には未だ諸説がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_46_445F end

    def Function_47_45A5(): pass

    label("Function_47_45A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45CE")
    EventBegin(0x1)
    Call(0, 50)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_45CE")

    Return()

    # Function_47_45A5 end

    def Function_48_45CF(): pass

    label("Function_48_45CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45F8")
    EventBegin(0x1)
    Call(0, 50)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_45F8")

    Return()

    # Function_48_45CF end

    def Function_49_45F9(): pass

    label("Function_49_45F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4622")
    EventBegin(0x1)
    Call(0, 50)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_4622")

    Return()

    # Function_49_45F9 end

    def Function_50_4623(): pass

    label("Function_50_4623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46BB")

    #C0104
    ChrTalk(
        0x10A,
        (
            "#00603FジオフロントＢ区画への\x01",
            "入り口は住宅街にあったはずだ。\x02\x03",

            "#00600F寄り道せずにさっさと向かうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        "#00000Fええ、了解です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4724")

    label("loc_46BB")


    #C0106
    ChrTalk(
        0x10A,
        (
            "#00603FジオフロントＢ区画への\x01",
            "入り口は住宅街にあったはずだ。\x02\x03",

            "#00600F寄り道せずにさっさと向かうぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4724")

    Return()

    # Function_50_4623 end

    SaveToFile()

Try(main)
