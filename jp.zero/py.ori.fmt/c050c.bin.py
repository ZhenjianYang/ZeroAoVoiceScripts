from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c050c.bin",                # FileName
        "c050c",                    # MapName
        "c050c",                    # Location
        0x0026,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 38, 0, 2, 0, 3],
    )

    BuildStringList((
        "c050c",                  # 0
        "マフィア",               # 1
        "マフィア",               # 2
        "客引きビッシュ",         # 3
        "アイリス",               # 4
        "見物客",                 # 5
        "見物客",                 # 6
        "見物客",                 # 7
        "見物客",                 # 8
        "見物客",                 # 9
        "見物客",                 # 10
        "中央広場",               # 11
        "西通り",                 # 12
        "行政区",                 # 13
        "住宅街",                 # 14
        "歓楽街",                 # 15
        "東通り",                 # 16
        "旧市街",                 # 17
        "港湾区",                 # 18
        "ＩＢＣ",                 # 19
        "駅前通り",               # 20
        "裏通り",                 # 21
        "ウルスラ間道",           # 22
        "東クロスベル街道",       # 23
        "西クロスベル街道",       # 24
        "マインツ山道",           # 25
    ))

    AddCharChip((
        "chr/ch20200.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch23500.itc",                   # 02
        "chr/ch23600.itc",                   # 03
        "chr/ch24200.itc",                   # 04
        "chr/ch24400.itc",                   # 05
        "chr/ch26700.itc",                   # 06
        "chr/ch26900.itc",                   # 07
        "chr/ch31000.itc",                   # 08
        "chr/ch31100.itc",                   # 09
    ))

    DeclNpc(-2000,   0,       41700,   180,  261,  0x0, 0,   8,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(2000,    0,       41700,   180,  261,  0x0, 0,   9,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-16590,  0,       2980,    90,   277,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-6170,   0,       1399,    90,   261,  0x0, 0,   7,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(-14979,  0,       2980,    270,  405,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-14979,  0,       2980,    270,  405,  0x0, 0,   1,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-14100,  0,       2549,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-14979,  0,       2980,    270,  405,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-14979,  0,       2980,    270,  405,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-14100,  0,       2549,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   20,  255,  0)

    DeclEvent(0x0000, 0, 24,  -0.10000000149011612,  43.849998474121094,    -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.05000000074505806,   -21.924999237060547,   0.10000000149011612,   1.0])

    DeclActor(-3210,   5800,    22030,   1200,    -3210,   6800,    22030,   0x007C, 0,  4,  0x0000)
    DeclActor(-10590,  5900,    9660,    1200,    -10590,  6900,    9660,    0x007C, 0,  5,  0x0000)
    DeclActor(11410,   0,       7030,    1200,    11410,   1000,    7030,    0x007C, 0,  6,  0x0000)

    PlaceName(79.5, 0.0, -9.0, 0x0000, 0x0000, "中央広場")
    PlaceName(0.0, 0.0, -76.5, 0x0000, 0x0000, "西通り")
    PlaceName(11.0, 0.0, 116.0, 0x0000, 0x0000, "行政区")
    PlaceName(-148.0, 0.0, -60.0, 0x0000, 0x0000, "住宅街")
    PlaceName(-57.25, 0.0, 10.0, 0x0000, 0x0000, "歓楽街")
    PlaceName(196.0, 0.0, 56.0, 0x0000, 0x0000, "東通り")
    PlaceName(294.0, 0.0, 31.0, 0x0000, 0x0000, "旧市街")
    PlaceName(154.0, 0.0, 158.0, 0x0000, 0x0000, "港湾区")
    PlaceName(20.0, 0.0, 233.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(168.0, 0.0, -73.0, 0x0000, 0x0000, "駅前通り")
    PlaceName(1.0, 0.0, -9.0, 0x0000, 0x0000, "裏通り")
    PlaceName(200.0, 0.0, -112.0, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(240.0, 0.0, 130.0, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-52.0, 0.0, -134.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-156.0, 0.0, -17.0, 0x0000, 0x0000, "マインツ山道")
    PlaceName(71.0, 0.0, -49.0, 0x0000, 0x0051, "")
    PlaceName(100.5, 0.0, 38.5, 0x0000, 0x0054, "")
    PlaceName(106.0, 0.0, -31.0, 0x0000, 0x0057, "")
    PlaceName(38.0, 0.0, -18.5, 0x0000, 0x0053, "")
    PlaceName(35.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(9.0, 0.0, -57.0, 0x0000, 0x0053, "")
    PlaceName(-23.5, 0.0, -45.0, 0x0000, 0x0053, "")
    PlaceName(-33.0, 0.0, 16.0, 0x0000, 0x0052, "")
    PlaceName(-15.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(6.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(-41.0, 0.0, 118.0, 0x0000, 0x0051, "")
    PlaceName(233.0, 0.0, 91.0, 0x0000, 0x0052, "")
    PlaceName(313.0, 0.0, -26.0, 0x0000, 0x0053, "")
    PlaceName(278.0, 0.0, -19.5, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_54C",          # 00, 0
        "Function_1_604",          # 01, 1
        "Function_2_66B",          # 02, 2
        "Function_3_8A4",          # 03, 3
        "Function_4_9B0",          # 04, 4
        "Function_5_AFD",          # 05, 5
        "Function_6_C4A",          # 06, 6
        "Function_7_D97",          # 07, 7
        "Function_8_FCF",          # 08, 8
        "Function_9_126F",         # 09, 9
        "Function_10_1705",        # 0A, 10
        "Function_11_17BD",        # 0B, 11
        "Function_12_1885",        # 0C, 12
        "Function_13_1941",        # 0D, 13
        "Function_14_1A09",        # 0E, 14
        "Function_15_21F1",        # 0F, 15
        "Function_16_2244",        # 10, 16
        "Function_17_22B6",        # 11, 17
        "Function_18_22E6",        # 12, 18
        "Function_19_2358",        # 13, 19
        "Function_20_23C4",        # 14, 20
        "Function_21_2419",        # 15, 21
        "Function_22_24AD",        # 16, 22
        "Function_23_27BD",        # 17, 23
        "Function_24_3715",        # 18, 24
        "Function_25_37B9",        # 19, 25
    ))


    def Function_0_54C(): pass

    label("Function_0_54C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_58C"),
        (1, "loc_598"),
        (2, "loc_5A4"),
        (3, "loc_5B0"),
        (4, "loc_5BC"),
        (5, "loc_5C8"),
        (6, "loc_5D4"),
        (SWITCH_DEFAULT, "loc_5E0"),
    )


    label("loc_58C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_598")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_603")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_603")

    Return()

    # Function_0_54C end

    def Function_1_604(): pass

    label("Function_1_604")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66A")
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -240, 0, 15530, 1000, 0x0)
    Sleep(3600)
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -24330, 0, 1400, 1000, 0x0)
    Sleep(1200)
    Jump("Function_1_604")

    label("loc_66A")

    Return()

    # Function_1_604 end

    def Function_2_66B(): pass

    label("Function_2_66B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FB")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_75A")
    SetChrPos(0x0, 20160, 0, 650, 270)
    SetChrPos(0x1, 20160, 0, 650, 270)
    SetChrPos(0x2, 20160, 0, 650, 270)
    SetChrPos(0x3, 20160, 0, 650, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72D")
    SetChrPos(0x4, 20160, 0, 650, 270)
    SetChrPos(0x5, 20160, 0, 650, 270)
    Jump("loc_74C")

    label("loc_72D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74C")
    SetChrPos(0x4, 20160, 0, 650, 270)

    label("loc_74C")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7FB")

    label("loc_75A")

    SetChrPos(0x0, -24900, 0, 220, 90)
    SetChrPos(0x1, -24900, 0, 220, 90)
    SetChrPos(0x2, -24900, 0, 220, 90)
    SetChrPos(0x3, -24900, 0, 220, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D3")
    SetChrPos(0x4, -24900, 0, 220, 90)
    SetChrPos(0x5, -24900, 0, 220, 90)
    Jump("loc_7F2")

    label("loc_7D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F2")
    SetChrPos(0x4, -24900, 0, 220, 90)

    label("loc_7F2")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7FB")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81A")
    SetMapFlags(0x10000000)
    Event(0, 22)

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_841")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83C")
    SetChrFlags(0x9, 0x10)

    label("loc_83C")

    Jump("loc_88B")

    label("loc_841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_85B")
    OP_93(0xA, 0xB4, 0x0)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_88B")

    label("loc_85B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_86E")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_88B")

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_886")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_88B")

    label("loc_886")

    ClearChrFlags(0xC, 0x80)

    label("loc_88B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A3")
    OP_C7(0x1, 0x1000)

    label("loc_8A3")

    Return()

    # Function_2_66B end

    def Function_3_8A4(): pass

    label("Function_3_8A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B7")
    OP_70(0x4, 0x0)
    Jump("loc_8BB")

    label("loc_8B7")

    OP_70(0x4, 0x1E)

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CE")
    OP_70(0x5, 0x0)
    Jump("loc_8D2")

    label("loc_8CE")

    OP_70(0x5, 0x1E)

    label("loc_8D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E5")
    OP_70(0x6, 0x0)
    Jump("loc_8E9")

    label("loc_8E5")

    OP_70(0x6, 0x1E)

    label("loc_8E9")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_901")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_901")

    OP_1B(0x1, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_919")
    OP_1B(0x1, 0x0, 0x19)

    label("loc_919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92C")
    OP_1B(0x1, 0x0, 0x17)

    label("loc_92C")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 13000, -4000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -13000, -4000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_3_8A4 end

    def Function_4_9B0(): pass

    label("Function_4_9B0")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAC")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_A35")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_AA7")

    label("loc_A35")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_AA7")

    Jump("loc_AF1")

    label("loc_AAC")

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

    label("loc_AF1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_9B0 end

    def Function_5_AFD(): pass

    label("Function_5_AFD")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF9")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x397, 1)"), scpexpr(EXPR_END)), "loc_B82")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_BF4")

    label("loc_B82")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_BF4")

    Jump("loc_C3E")

    label("loc_BF9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_C3E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_AFD end

    def Function_6_C4A(): pass

    label("Function_6_C4A")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D46")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x69, 1)"), scpexpr(EXPR_END)), "loc_CCF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_D41")

    label("loc_CCF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D41")

    Jump("loc_D8B")

    label("loc_D46")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_D8B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_C4A end

    def Function_7_D97(): pass

    label("Function_7_D97")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E21")

    #C0010
    ChrTalk(
        0x8,
        (
            "今日は大切な催し物があってな。\x01",
            "ケチを付ける訳にはいかねえのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "うろちょろしてっと\x01",
            "ドブにぶち込むぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E69")

    label("loc_E21")


    #C0012
    ChrTalk(
        0x8,
        "あア？　なんだ坊主。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "うろちょろしてっと\x01",
            "ドブにぶち込むぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E69")

    Jump("loc_FCB")

    label("loc_E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_F61")

    #C0014
    ChrTalk(
        0x8,
        "くく、祭りは華やかでいいな。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "たまに迷い込んでくる\x01",
            "馬鹿な観光客さえいなきゃ\x01",
            "見張りも楽なんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0006F（さすがにこっちには\x01",
            "  来てないみたいだな……\x01",
            "  ……良かったよ。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_F5C")

    #C0017
    ChrTalk(
        0x160,
        "#3308F（…………………………）\x02",
    )

    CloseMessageWindow()

    label("loc_F5C")

    Jump("loc_FCB")

    label("loc_F61")


    #C0018
    ChrTalk(
        0x8,
        "くく、祭りは華やかでいいな。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "たまに迷い込んでくる\x01",
            "馬鹿な観光客さえいなきゃ\x01",
            "見張りも楽なんだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FCB")

    TalkEnd(0xFE)
    Return()

    # Function_7_D97 end

    def Function_8_FCF(): pass

    label("Function_8_FCF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_10E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_103C")

    #C0020
    ChrTalk(
        0x9,
        "何もできねえ警察のハエどもが。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "さっさと失せな！\x01",
            "こっちも暇じゃねえんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E3")

    label("loc_103C")


    #C0022
    ChrTalk(
        0x9,
        "ちっ、今日に限って居残りとはな。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        "ついてないぜ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x0, 750)
    Sleep(750)

    #C0024
    ChrTalk(
        0x9,
        "……テメエは………\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "さっさと失せな！\x01",
            "こっちも暇じゃねえんだ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)

    label("loc_10E3")

    Jump("loc_126B")

    label("loc_10E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_11DD")

    #C0026
    ChrTalk(
        0x9,
        (
            "オイオイ、なんだ？\x01",
            "用事が無いならさっさと失せろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "若頭も、ガキの相手を\x01",
            "してるほど暇じゃねえだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0006F（さすがにこっちには\x01",
            "  来てないみたいだな……\x01",
            "  ……良かったよ。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_11D8")

    #C0029
    ChrTalk(
        0x160,
        "#3308F（…………………………）\x02",
    )

    CloseMessageWindow()

    label("loc_11D8")

    Jump("loc_126B")

    label("loc_11DD")


    #C0030
    ChrTalk(
        0x9,
        (
            "……またテメエらか。\x01",
            "懲りずに顔を出しやがって。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        "用事が無いならさっさと失せろ。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "若頭も、ガキの相手を\x01",
            "してるほど暇じゃねえだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126B")

    TalkEnd(0xFE)
    Return()

    # Function_8_FCF end

    def Function_9_126F(): pass

    label("Function_9_126F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1283")
    Call(0, 10)
    Jump("loc_1701")

    label("loc_1283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_END)), "loc_133A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_12E9")

    #C0033
    ChrTalk(
        0xA,
        (
            "うっし、今日もバンバン\x01",
            "お客さん取り込むで～！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xA,
        "うっひゃっひゃっひゃ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1335")

    label("loc_12E9")


    #C0035
    ChrTalk(
        0xA,
        (
            "ハア……仕事した後の\x01",
            "一服は最ッ高やね……！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        "人生充実してるわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1335")

    Jump("loc_1701")

    label("loc_133A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_14FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 4)), scpexpr(EXPR_END)), "loc_13E2")

    #C0037
    ChrTalk(
        0xA,
        (
            "まあパレードは大した騒ぎやったし\x01",
            "ジャリの１人や２人\x01",
            "通ったかも知れんけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "ビッシュさんは知らんなぁ。\x01",
            "そんなミラにならん話は知らんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F5")

    label("loc_13E2")


    #C0039
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0041
    ChrTalk(
        0xA,
        "うっひゃっひゃっひゃ……！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xA,
        (
            "…………知らんね。\x01",
            "見てへんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#0008Fそうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 21)

    label("loc_14F5")

    Jump("loc_1701")

    label("loc_14FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_15B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1560")

    #C0044
    ChrTalk(
        0xA,
        (
            "うっし、今日もバンバン\x01",
            "お客さん取り込むで～！\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xA,
        "うっひゃっひゃっひゃ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_15AC")

    label("loc_1560")


    #C0046
    ChrTalk(
        0xA,
        (
            "ハア……仕事した後の\x01",
            "一服は最ッ高やね……！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xA,
        "人生充実してるわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_15AC")

    Jump("loc_1701")

    label("loc_15B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_163B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1633")
    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0048
    ChrTalk(
        0xA,
        (
            "クロスベルに来たからには\x01",
            "めいっぱい遊ばんとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xA,
        "ほらほら、ワテが案内してあげよ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Jump("loc_1636")

    label("loc_1633")

    Call(0, 11)

    label("loc_1636")

    Jump("loc_1701")

    label("loc_163B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_16A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_169D")
    OP_4B(0xA, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0050
    ChrTalk(
        0xA,
        (
            "遠慮することないよ～。\x01",
            "２人とも大歓迎やって！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_16A0")

    label("loc_169D")

    Call(0, 12)

    label("loc_16A0")

    Jump("loc_1701")

    label("loc_16A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_16FE")
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0051
    ChrTalk(
        0xA,
        (
            "ささ、おじさんこっちや。\x01",
            "きっといい土産話になるで～？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Jump("loc_1701")

    label("loc_16FE")

    Call(0, 13)

    label("loc_1701")

    TalkEnd(0xFE)
    Return()

    # Function_9_126F end

    def Function_10_1705(): pass

    label("Function_10_1705")

    OP_4B(0xA, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0052
    ChrTalk(
        0xA,
        (
            "嫌やな～、そんなつもりで\x01",
            "声掛けたんやないで～。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xA,
        (
            "お兄さんやったらスターになれる。\x01",
            "そう見込んでのことやんか～。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x10,
        "わ、私はそんなつもりはないぞ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_10_1705 end

    def Function_11_17BD(): pass

    label("Function_11_17BD")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0055
    ChrTalk(
        0xA,
        (
            "どうどう、お兄さん。\x01",
            "最近遊んでないんとちゃう？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        (
            "アカンで～、クロスベルに来たからには\x01",
            "めいっぱい遊ばんと。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xA,
        "それが礼儀ちゅうもんやろ～！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xF,
        "そ、そうなんスか……！？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_11_17BD end

    def Function_12_1885(): pass

    label("Function_12_1885")

    OP_4B(0xA, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0059
    ChrTalk(
        0xA,
        (
            "大歓迎、大歓迎。\x01",
            "２人ともばっちり\x01",
            "楽しませてあげるさかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        (
            "このビッシュさんに\x01",
            "どーんと任せといてえや。\x01",
            "ひゃひゃひゃ！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xD,
        "い、いやあ僕たちはその……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_12_1885 end

    def Function_13_1941(): pass

    label("Function_13_1941")

    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0062
    ChrTalk(
        0xA,
        (
            "うわ～、おじさんやったら\x01",
            "うちの店でもモテモテやわ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        (
            "ささ、寄ってこ寄ってこ。\x01",
            "きっといい土産話になるで。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        "はは、そ、そうかな。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xC,
        "いやでも、家族のこともあるし……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_1941 end

    def Function_14_1A09(): pass

    label("Function_14_1A09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1A6B")

    #C0066
    ChrTalk(
        0xB,
        "記念祭も今日で終わりよねー。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xB,
        "ガンバって最後に大稼ぎしないと。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AEF")

    label("loc_1A6B")


    #C0068
    ChrTalk(
        0xB,
        "創立記念祭、ばんざーい！\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        (
            "……客の人に聞いたの。\x01",
            "今日は自治州ができた日なんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        "あたしゼンゼンしらなかったー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1AEF")

    Jump("loc_21ED")

    label("loc_1AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_END)), "loc_1BBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1B4E")

    #C0071
    ChrTalk(
        0xB,
        (
            "おっと……\x01",
            "いけない、いけない。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xB,
        "まじめに仕事しないとね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BB6")

    label("loc_1B4E")

    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0073
    ChrTalk(
        0xB,
        "パレード、凄かったわね！\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "あたしも一緒になって\x01",
            "手を振っちゃった～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1BB6")

    Jump("loc_21ED")

    label("loc_1BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1E36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1C49")

    #C0075
    ChrTalk(
        0xB,
        (
            "あたしもパレード\x01",
            "見に行ってたの～。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xB,
        (
            "うん、パレードの車と一緒に\x01",
            "歩いてた子だ～。\x01",
            "可愛かったから覚えてるわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E31")

    label("loc_1C49")


    #C0077
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0079
    ChrTalk(
        0xFE,
        "んっとぉ、えっとぉ……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "……そういえば\x01",
            "子供は２、３人見たかも～。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0000F本当ですか……？\x02\x03",

            "その中にこの写真の子は……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "ん～、どうだったかな～……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "ホラあたしって、\x01",
            "頭つかうの苦手だし～。\x01",
            "すぐ忘れちゃうんだもん。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "モヤモヤっとしてて\x01",
            "よく思い出せな～い。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#0006Fそ、そうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 21)

    label("loc_1E31")

    Jump("loc_21ED")

    label("loc_1E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1EFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1E90")

    #C0086
    ChrTalk(
        0xB,
        (
            "おっと……\x01",
            "いけない、いけない。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xB,
        "まじめに仕事しないとね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EF8")

    label("loc_1E90")

    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0088
    ChrTalk(
        0xB,
        "パレード、凄かったわね！\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        (
            "あたしも一緒になって\x01",
            "手を振っちゃった～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1EF8")

    Jump("loc_21ED")

    label("loc_1EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2031")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F85")

    #C0090
    ChrTalk(
        0xB,
        "うふ、いらっしゃいませ㈱\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xB,
        "お兄さん、遊んでいこっ☆\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xB,
        (
            "ふわ～……なんだか\x01",
            "もう疲れてきちゃったかも～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_202C")

    label("loc_1F85")


    #C0093
    ChrTalk(
        0xB,
        "うふ、いらっしゃいませ㈱\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xB,
        "お兄さん、遊んでいこっ☆\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xB,
        (
            "……どお？\x01",
            "ちょっとイメージ変えてみたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xB,
        (
            "観光客にはこっちの方が\x01",
            "受けがいいみたいなのよね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_202C")

    Jump("loc_21ED")

    label("loc_2031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2115")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2087")

    #C0097
    ChrTalk(
        0xB,
        (
            "さっすが、おっきなお祭りよね。\x01",
            "バンバン儲かっちゃうわ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2110")

    label("loc_2087")


    #C0098
    ChrTalk(
        0xB,
        (
            "うふふ、昨日の売り上げ\x01",
            "ライバルの子より\x01",
            "あたしの方がちょっと多かったの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0099
    ChrTalk(
        0xB,
        "やっぱり記念祭、さいこー！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2110")

    Jump("loc_21ED")

    label("loc_2115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_217F")

    #C0100
    ChrTalk(
        0xB,
        (
            "あたし、ライバルの子と\x01",
            "売り上げを競ってンの。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xB,
        (
            "お祭の間で\x01",
            "差をつけてやんないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21ED")

    label("loc_217F")


    #C0102
    ChrTalk(
        0xB,
        "わーい、記念祭ばんざい！\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        "お客さんがいっぱい！\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xB,
        (
            "今日も頑張って、\x01",
            "売り上げアップを狙うわよ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_21ED")

    TalkEnd(0xFE)
    Return()

    # Function_14_1A09 end

    def Function_15_21F1(): pass

    label("Function_15_21F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_223D")
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0105
    ChrTalk(
        0xC,
        (
            "いやでも、\x01",
            "家族のこともあるしねぇ……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Jump("loc_2240")

    label("loc_223D")

    Call(0, 13)

    label("loc_2240")

    TalkEnd(0xFE)
    Return()

    # Function_15_21F1 end

    def Function_16_2244(): pass

    label("Function_16_2244")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_22AF")
    OP_4B(0xA, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0106
    ChrTalk(
        0xD,
        "い、いやあ僕たちはその……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xD,
        "これから行く所もあるんで……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_22B2")

    label("loc_22AF")

    Call(0, 12)

    label("loc_22B2")

    TalkEnd(0xFE)
    Return()

    # Function_16_2244 end

    def Function_17_22B6(): pass

    label("Function_17_22B6")

    TalkBegin(0xFE)

    #C0108
    ChrTalk(
        0xE,
        (
            "わーん、変な人に\x01",
            "捕まっちまったよ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_22B6 end

    def Function_18_22E6(): pass

    label("Function_18_22E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2351")
    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0109
    ChrTalk(
        0xF,
        "オレはパレードを見に来ただけで……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xF,
        "そ、そういう物なんスか……？\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Jump("loc_2354")

    label("loc_2351")

    Call(0, 11)

    label("loc_2354")

    TalkEnd(0xFE)
    Return()

    # Function_18_22E6 end

    def Function_19_2358(): pass

    label("Function_19_2358")

    TalkBegin(0xFE)
    OP_4B(0xA, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0111
    ChrTalk(
        0x10,
        "つ、妻の前でなんて事を言うんだ。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x10,
        (
            "けしからん！\x01",
            "まったくけしからん！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_19_2358 end

    def Function_20_23C4(): pass

    label("Function_20_23C4")

    TalkBegin(0xFE)

    #C0113
    ChrTalk(
        0x11,
        (
            "クロスベルの裏通りって\x01",
            "怖いって聞いていたけど……\x01",
            "本当のことみたいね……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_23C4 end

    def Function_21_2419(): pass

    label("Function_21_2419")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24AC")
    OP_29(0x46, 0x1, 0x4)

    #C0114
    ChrTalk(
        0x101,
        (
            "#0003F（よし、裏通りの聞き込みは\x01",
            "  これで十分だな。）\x02\x03",

            "#0001F（次は中央広場で\x01",
            "  聞き込みをしてみよう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 4)
    OP_1B(0x1, 0x0, 0x17)

    label("loc_24AC")

    Return()

    # Function_21_2419 end

    def Function_22_24AD(): pass

    label("Function_22_24AD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-23300, 2300, 1000, 0)
    MoveCamera(330, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -28300, 0, 1000, 90)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(-23300, 1300, 1000, 2500)

    def lambda_2551():
        OP_96(0xFE, 0xFFFFA4FC, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2551)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(1084, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0115
    AnonymousTalk(
        0x101,
        "#0001Fこちらロイドです。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1364, 255, 100, 0)    #voice#Randy
    Sleep(500)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ランディの声")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こちらランディ。\x01",
            "東通りは一通り調べた。\x02\x03",

            "ギルドの受付にも聞いたが\x01",
            "それっぽい手がかりはないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0117
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0008Fわかった。\x01",
            "こちらも歓楽街はシロ。\x02\x03",

            "#0001F引き続き捜索を続けてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ランディの声")

    #A0118
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アイアイ・サー。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    Sleep(300)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -23900, 0, 1000, 90)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA2, 0)
    OP_29(0x46, 0x1, 0x3)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_22_24AD end

    def Function_23_27BD(): pass

    label("Function_23_27BD")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    AddParty(0x5F, 0xFF, 0xFF)
    OP_68(18000, 1100, 1000, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 15000, 0, 1000, 90)
    SetChrPos(0x160, 8000, 0, 1000, 90)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis056.itp")

    def lambda_287A():
        OP_96(0xFE, 0x4650, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_287A)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    #N0119
    NpcTalk(
        0x160,
        "少女の声",
        (
            "#2Pうふふ……\x01",
            "お兄さん、お久しぶりね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x101,
        "#0005F#5Pえ……\x02",
    )

    CloseMessageWindow()

    def lambda_2907():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2907)
    Fade(500)
    SetChrPos(0x160, 13000, 0, 1000, 90)
    OP_68(17160, 1300, 1300, 0)
    MoveCamera(27, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(13500, 1600)

    def lambda_2961():
        OP_96(0xFE, 0x3EE4, 0x0, 0x3E8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2961)
    WaitChrThread(0x160, 1)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 0)), scpexpr(EXPR_END)), "loc_2B18")

    #C0121
    ChrTalk(
        0x101,
        "#11P#0002Fやあ、レンちゃんか。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0122
    AnonymousTalk(
        0x160,
        (
            "ご機嫌よう、お兄さん。\x02\x03",

            "ふふっ、１ヶ月ぶりかしら？\x02",
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

    #C0123
    ChrTalk(
        0x101,
        (
            "#11P#0004Fああ、それくらいになるかな。\x02\x03",

            "#0002Fまた一人で\x01",
            "アンティークショップに\x01",
            "遊びに来たのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x160,
        (
            "#3309F#5Pええ、それとお祭りの見物をね。\x02\x03",

            "#3302Fパレードがあったけど\x01",
            "お兄さんも見物したのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F4E")

    label("loc_2B18")


    #C0125
    ChrTalk(
        0x101,
        "#11P#0005F君は……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("ドレスの少女")

    #A0126
    AnonymousTalk(
        0xFF,
        (
            "ご機嫌よう、お兄さん。\x02\x03",

            "ふふっ、２ヶ月ぶりかしら？\x02",
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

    #C0127
    ChrTalk(
        0x101,
        (
            "#11P#0005Fああ……人形工房の。\x02\x03",

            "#0002Fお久しぶり。\x01",
            "確か、レンちゃんだったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x160,
        (
            "#3306F#5Pもう、レディの名前を\x01",
            "わざわざ確認するものじゃないわ。\x02\x03",

            "#3301F当然のように覚えていて\x01",
            "再会の挨拶をするのが紳士でしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#11P#0012Fはは……ゴメン、悪かったよ。\x02\x03",

            "#0000Fこんな所でどうしたんだい？\x02\x03",

            "#0005F一人でいるみたいだけど……\x01",
            "もしかして迷子になったとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x160,
        (
            "#3304F#5P別にレンは迷子じゃないわ。\x02\x03",

            "そこのアンティーク屋さんには\x01",
            "たまに一人で遊びに来ているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#11P#0005Fそ、そうなのか？\x02\x03",

            "#0001Fでもこの辺り、\x01",
            "子供が一人でうろつくのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x160,
        (
            "#3309F#5Pクスクス。\x01",
            "別に危ないことはないわ。\x02\x03",

            "#3302F呼び込みのお兄さんも\x01",
            "お水のお姉さんも優しいし……\x02\x03",

            "路地の奥の黒メガネさんたちも\x01",
            "けっこう楽しい人たちだもの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0133
    ChrTalk(
        0x101,
        "#11P#0011Fそ、そうなのか……？\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x160,
        (
            "#3304F#5Pそれと今日は、\x01",
            "お祭りを見物しに来てるの。\x02\x03",

            "#3302Fパレードがあったけど\x01",
            "お兄さんも見物したのかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F4E")


    #C0135
    ChrTalk(
        0x101,
        (
            "#11P#0006Fいや、仕事を片付けているうちに\x01",
            "見逃しちゃってさ。\x02\x03",

            "#0008F（しかし困ったな……）\x02\x03",

            "（一人にするのもなんだし\x01",
            "  用事が無ければ人形工房まで\x01",
            "  送っていくところなんだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x160,
        (
            "#3305F#5P？？？\x02\x03",

            "#3300Fところでお兄さん、\x01",
            "一人で何をしてるの？\x02\x03",

            "また誰かと\x01",
            "かくれんぼをしてるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#11P#0006Fいや……\x01",
            "実は迷子を捜していてさ。\x02\x03",

            "#0000F今日のパレードで\x01",
            "はぐれちゃったらしいんだけど\x01",
            "まだ見つかっていないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x160,
        (
            "#3300F#5Pふぅん、そうだったの。\x02\x03",

            "写真かなにか持っている？\x01",
            "レンが知ってるかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#11P#0002Fそうだな……\x01",
            "一応、見てもらえるかな？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真をレンに見せた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(18, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)

    #A0141
    AnonymousTalk(
        0x160,
        (
            "#3300F……………………………………………\x02\x03",

            "#3305F#30W………………え…………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0142
    ChrTalk(
        0x101,
        (
            "#11P#0005Fどうした？\x02\x03",

            "#0000Fひょっとして\x01",
            "見覚えがある子だったか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x160, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x160)
    Sleep(300)

    #C0143
    ChrTalk(
        0x160,
        (
            "#5P#60W───ううん。\x02\x01",

            "レン#500W、#60Wこんな子#500W、#60W見覚えないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        "#11P#0006Fそうか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x160, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x160)

    #C0145
    ChrTalk(
        0x160,
        (
            "#3303F#5Pでも……可愛い男の子ね。\x02\x03",

            "#3300Fお兄さんは……\x01",
            "この子を捜しているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#11P#0000Fああ、仲間と手分けしてね。\x02\x03",

            "#0008F早く捜して、ご両親の元に\x01",
            "帰してあげたいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x160,
        (
            "#3304F#5Pふふっ……\x02\x03",

            "#3302Fだったら、レンもこの子を\x01",
            "捜すのを手伝ってあげるわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0148
    ChrTalk(
        0x101,
        "#11P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x160,
        (
            "#3302F#5P前に言ったでしょう？\x01",
            "レンはかくれんぼが得意だって。\x02\x03",

            "この子がどこにいるか\x01",
            "多分、突き止められると思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#11P#0011Fいや、でも……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x101,
        (
            "#11P#0004F（この子を一人にするのも何だし\x01",
            "  とりあえず一緒にいてもらうか……）\x02\x03",

            "（いざとなったら支援課で\x01",
            "  待っててもらってもいいし……）\x02\x03",

            "#0000F──わかった。\x01",
            "それじゃあよろしく頼むよ。\x02\x03",

            "しばらくお兄さんと\x01",
            "一緒に付いてきてくれるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x160,
        (
            "#3304F#5Pうふふ、いいわ。\x02\x03",

            "#3302Fよろしくね、ロイドお兄さん。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        "#11P#0002Fああ、こちらこそ。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(13750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(18000, 1950, 1000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x0, 18000, 0, 1000, 270)
    SetChrPos(0x1, 18000, 0, 1000, 270)
    OP_1B(0x1, 0xFF, 0xFFFF)
    SetScenarioFlags(0xA2, 1)
    OP_29(0x46, 0x1, 0x5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_23_27BD end

    def Function_24_3715(): pass

    label("Function_24_3715")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    def lambda_3724():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3724)
    Sleep(50)

    def lambda_3734():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3734)
    WaitChrThread(0x8, 1)

    #C0154
    ChrTalk(
        0x8,
        (
            "おい、ウロチョロ\x01",
            "してんじゃねえぞ……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        "痛い目見る前にとっとと失せな！\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    SetChrPos(0x0, -100, 0, 41020, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_24_3715 end

    def Function_25_37B9(): pass

    label("Function_25_37B9")

    EventBegin(0x1)

    #C0156
    ChrTalk(
        0x101,
        (
            "#0001Fいや、まだ十分に\x01",
            "聞き込みをしていない……\x02\x03",

            "もう少しこの辺りで\x01",
            "情報を集めてみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 20170, 0, 940, 274)
    EventEnd(0x4)
    Return()

    # Function_25_37B9 end

    SaveToFile()

Try(main)
