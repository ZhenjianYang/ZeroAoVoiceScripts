from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c140b.bin",                # FileName
        "c140b",                    # MapName
        "c140b",                    # Location
        0x002E,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 46, 0, 1, 0, 2],
    )

    BuildStringList((
        "c140b",                  # 0
        "ワジ",                   # 1
        "ヴァルド",               # 2
        "変装ロイド",             # 3
        "アッバス",               # 4
        "グレイス",               # 5
        "青装束の青年",           # 6
        "青装束の青年",           # 7
        "青装束の青年",           # 8
        "ディーノ",               # 9
        "赤ジャージの青年",       # 10
        "赤ジャージの青年",       # 11
        "赤ジャージの青年",       # 12
        "赤ジャージの青年",       # 13
        "マフィア",               # 14
        "マフィア",               # 15
        "マフィア",               # 16
        "マフィア",               # 17
        "バット",                 # 18
        "BC141b",                 # 19
        "中央広場",               # 20
        "西通り",                 # 21
        "行政区",                 # 22
        "住宅街",                 # 23
        "歓楽街",                 # 24
        "東通り",                 # 25
        "旧市街",                 # 26
        "港湾区",                 # 27
        "ＩＢＣ",                 # 28
        "駅前通り",               # 29
        "裏通り",                 # 30
        "ウルスラ間道",           # 31
        "東クロスベル街道",       # 32
        "西クロスベル街道",       # 33
        "マインツ山道",           # 34
    ))

    ATBonus("ATBonus_59C", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_5BC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_63C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_640", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_644", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_648", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_64C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_650", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_654", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_658", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_65C", 0x0002, 3, 6, 180, 0, 0, 55, 0, "BC141b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31000.dat", "ms31100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5BC", "MonsterBattlePostion_63C", "ed7507", "ed7403", "ATBonus_59C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    470,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-28460,  2800,    -29590,  1200,    -28460,  3800,    -29590,  0x007C, 0,  3,  0x0000)

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "中央広場")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "西通り")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "行政区")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "住宅街")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "歓楽街")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "東通り")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "旧市街")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "駅前通り")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "裏通り")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-238.0500030517578, 0.0, 225.39999389648438, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-135.99000549316406, 0.0, 90.8499984741211, 0x0000, 0x0051, "")
    PlaceName(-74.18000030517578, 0.0, 120.75, 0x0000, 0x0054, "")
    PlaceName(-107.80999755859375, 0.0, 81.6500015258789, 0x0000, 0x0057, "")
    PlaceName(-136.85000610351562, 0.0, 124.19999694824219, 0x0000, 0x0053, "")
    PlaceName(-113.27999877929688, 0.0, 151.8000030517578, 0x0000, 0x0053, "")
    PlaceName(-171.63999938964844, 0.0, 118.44999694824219, 0x0000, 0x0053, "")
    PlaceName(-182.85000610351562, 0.0, 142.60000610351562, 0x0000, 0x0053, "")
    PlaceName(-155.25, 0.0, 179.39999389648438, 0x0000, 0x0052, "")
    PlaceName(-149.7899932861328, 0.0, 164.4499969482422, 0x0000, 0x0053, "")
    PlaceName(-139.72999572753906, 0.0, 154.67999267578125, 0x0000, 0x0053, "")
    PlaceName(-106.94999694824219, 0.0, 236.3300018310547, 0x0000, 0x0051, "")
    PlaceName(21.850000381469727, 0.0, 80.5, 0x0000, 0x0052, "")
    PlaceName(2.299999952316284, 0.0, -23.579999923706055, 0x0000, 0x0053, "")
    PlaceName(-12.649999618530273, 0.0, -2.299999952316284, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_6F8",          # 00, 0
        "Function_1_7B0",          # 01, 1
        "Function_2_7D4",          # 02, 2
        "Function_3_7EC",          # 03, 3
        "Function_4_939",          # 04, 4
        "Function_5_3608",         # 05, 5
        "Function_6_3794",         # 06, 6
        "Function_7_38C0",         # 07, 7
        "Function_8_395D",         # 08, 8
        "Function_9_39C8",         # 09, 9
        "Function_10_3A33",        # 0A, 10
        "Function_11_3A70",        # 0B, 11
        "Function_12_3AAD",        # 0C, 12
        "Function_13_3AEA",        # 0D, 13
        "Function_14_3B00",        # 0E, 14
        "Function_15_3B41",        # 0F, 15
        "Function_16_3B99",        # 10, 16
        "Function_17_3BF8",        # 11, 17
        "Function_18_3C17",        # 12, 18
        "Function_19_6A7A",        # 13, 19
        "Function_20_6ABB",        # 14, 20
        "Function_21_6AFC",        # 15, 21
    ))


    def Function_0_6F8(): pass

    label("Function_0_6F8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_738"),
        (1, "loc_744"),
        (2, "loc_750"),
        (3, "loc_75C"),
        (4, "loc_768"),
        (5, "loc_774"),
        (6, "loc_780"),
        (SWITCH_DEFAULT, "loc_78C"),
    )


    label("loc_738")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_798")

    label("loc_744")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_798")

    label("loc_750")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_798")

    label("loc_75C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_798")

    label("loc_768")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_798")

    label("loc_774")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_798")

    label("loc_780")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_798")

    label("loc_78C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_798")

    label("loc_798")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_798")

    label("loc_7AF")

    Return()

    # Function_0_6F8 end

    def Function_1_7B0(): pass

    label("Function_1_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_7C4")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_7D3")

    label("loc_7C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_7D3")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 18)

    label("loc_7D3")

    Return()

    # Function_1_7B0 end

    def Function_2_7D4(): pass

    label("Function_2_7D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E7")
    OP_70(0x7, 0x0)
    Jump("loc_7EB")

    label("loc_7E7")

    OP_70(0x7, 0x1E)

    label("loc_7EB")

    Return()

    # Function_2_7D4 end

    def Function_3_7EC(): pass

    label("Function_3_7EC")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E8")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x642, 1)"), scpexpr(EXPR_END)), "loc_871")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_8E3")

    label("loc_871")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_8E3")

    Jump("loc_92D")

    label("loc_8E8")

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

    label("loc_92D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7EC end

    def Function_4_939(): pass

    label("Function_4_939")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30800.itc", 0x1E)
    LoadChrToIndex("chr/ch30900.itc", 0x1F)
    LoadChrToIndex("chr/ch31700.itc", 0x20)
    LoadChrToIndex("chr/ch31800.itc", 0x21)
    LoadChrToIndex("chr/ch00400.itc", 0x22)
    LoadChrToIndex("chr/ch00450.itc", 0x23)
    LoadChrToIndex("chr/ch00451.itc", 0x24)
    LoadChrToIndex("chr/ch02100.itc", 0x25)
    LoadChrToIndex("apl/ch50019.itc", 0x26)
    LoadChrToIndex("chr/ch02150.itc", 0x27)
    LoadChrToIndex("chr/ch02151.itc", 0x28)
    LoadChrToIndex("chr/ch06700.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00150.itc", 0x2B)
    LoadChrToIndex("chr/ch00250.itc", 0x2C)
    LoadChrToIndex("chr/ch00350.itc", 0x2D)
    LoadChrToIndex("chr/ch31000.itc", 0x2E)
    LoadChrToIndex("chr/ch31001.itc", 0x2F)
    LoadChrToIndex("chr/ch31050.itc", 0x30)
    LoadChrToIndex("chr/ch31051.itc", 0x31)
    LoadChrToIndex("chr/ch31100.itc", 0x32)
    LoadChrToIndex("chr/ch31101.itc", 0x33)
    LoadChrToIndex("chr/ch31152.itc", 0x34)
    LoadChrToIndex("chr/ch31151.itc", 0x35)
    LoadChrToIndex("chr/ch08800.itc", 0x36)
    LoadChrToIndex("apl/ch50020.itc", 0x37)
    LoadChrToIndex("apl/ch50021.itc", 0x38)
    LoadChrToIndex("apl/ch50022.itc", 0x39)
    LoadChrToIndex("apl/ch50023.itc", 0x3A)
    LoadChrToIndex("apl/ch50024.itc", 0x3B)
    LoadChrToIndex("apl/ch50025.itc", 0x3C)
    LoadChrToIndex("apl/ch50027.itc", 0x3D)
    LoadChrToIndex("apl/ch50029.itc", 0x3E)
    LoadChrToIndex("chr/ch00456.itc", 0x3F)
    LoadChrToIndex("chr/ch06800.itc", 0x40)
    OP_68(18500, 500, -25000, 0)
    MoveCamera(32, 4, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40500, 0)
    SetChrPos(0x0, -10000, 0, 5000, 0)
    SetChrPos(0x1, -10000, 0, 5000, 0)
    SetChrPos(0x2, -10000, 0, 5000, 0)
    SetChrPos(0x3, -10000, 0, 5000, 0)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x18, 0x32)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x15, 1100, 0, 13000, 180)
    SetChrPos(0x16, 2500, 0, 13000, 180)
    SetChrPos(0x17, 1100, 0, 14400, 180)
    SetChrPos(0x18, 2500, 0, 14400, 180)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    LoadEffect(0x0, "battle\\ms00000.eff")
    LoadEffect(0x1, "event\\eva01_01.eff")
    LoadEffect(0x2, "event\\eva04_00.eff")
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──３日が過ぎた。\x02\x03",

            "一触即発だった不良たちの争いは\x01",
            "それから一度も起こる事はなく……\x02\x03",

            "旧市街は不自然なほど\x01",
            "平穏な雰囲気を取り戻していた。\x02\x03",

            "そして──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(27, 4, 0, 6000)
    SetCameraDistance(45500, 6000)
    PlayBGM("ed7302", 0)
    FadeToBright(2000, 0)
    Sleep(4000)

    def lambda_C34():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C34)
    Sleep(50)

    def lambda_C51():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_C51)
    Sleep(50)

    def lambda_C6E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_C6E)
    Sleep(50)

    def lambda_C8B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_C8B)
    OP_6F(0x50)
    Fade(1000)
    OP_68(1800, 1000, 2700, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26500, 0)
    SetCameraDistance(21500, 4000)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x18, 1)
    OP_6F(0x10)

    #N0005
    NpcTalk(
        0x15,
        "サングラスの男",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5Pチッ……静かなもんだな。\x02",
        )
    )

    CloseMessageWindow()

    #N0006
    NpcTalk(
        0x15,
        "サングラスの男",
        (
            "#5Pあそこまで仕込んだのに\x01",
            "どうして潰し合いが始まらない？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x15, 500)

    #N0007
    NpcTalk(
        0x18,
        "サングラスの男",
        (
            "#5Pクク……\x01",
            "最後の一押しが足りんだけさ。\x02",
        )
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x18,
        "サングラスの男",
        (
            "#5P導火線に火が点けば、\x01",
            "勝手に潰し合いが始まるだろう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E03():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_E03)
    Sleep(100)

    def lambda_E13():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_E13)
    Sleep(50)
    TurnDirection(0x17, 0x16, 500)
    Sleep(300)

    #N0009
    NpcTalk(
        0x16,
        "サングラスの男",
        (
            "#2Pバイパーとテスタメンツ、\x01",
            "どっちのガキでもいい……\x02",
        )
    )

    CloseMessageWindow()

    #N0010
    NpcTalk(
        0x16,
        "サングラスの男",
        "#2P目に付いたヤツをやるぞ。\x02",
    )

    CloseMessageWindow()

    #N0011
    NpcTalk(
        0x15,
        "サングラスの男",
        "#6Pくれぐれも姿を見られるなよ？\x02",
    )

    CloseMessageWindow()

    #N0012
    NpcTalk(
        0x15,
        "サングラスの男",
        (
            "#6Pバイパーならスリングショット、\x01",
            "テスタメンツなら背後から一撃だ。\x02",
        )
    )

    CloseMessageWindow()

    #N0013
    NpcTalk(
        0x17,
        "サングラスの男",
        "#1Pああ……\x02",
    )

    CloseMessageWindow()

    #N0014
    NpcTalk(
        0x18,
        "サングラスの男",
        "#5Pクク……狩りの始まりだ。\x02",
    )

    CloseMessageWindow()
    OP_E5()

    def lambda_F82():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_F82)
    Sleep(100)

    def lambda_F92():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_F92)
    Sleep(50)

    def lambda_FA2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_FA2)
    Sleep(50)

    def lambda_FB2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_FB2)
    WaitChrThread(0x15, 2)

    def lambda_FC3():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_FC3)
    WaitChrThread(0x16, 2)
    Sleep(100)

    def lambda_FE4():
        OP_97(0xFE, 0x5DC, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_FE4)
    WaitChrThread(0x18, 2)
    Sleep(100)

    def lambda_1005():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1005)
    WaitChrThread(0x17, 2)
    Sleep(100)

    def lambda_1026():
        OP_97(0xFE, 0xBB8, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1026)
    SetCameraDistance(23500, 3000)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x15, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x18, 0x1)
    OP_68(-19000, 2000, -10300, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x15, 10600, -6500, -31800, 135)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrChipByIndex(0xA, 0x36)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, -19000, -1460, -5300, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetCameraDistance(21500, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_10F5():
        OP_95(0xFE, -19000, 0, -10300, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10F5)
    WaitChrThread(0xA, 1)
    OP_6B(0xA)

    def lambda_1116():
        OP_95(0xFE, -12400, 0, -12800, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1116)
    MoveCamera(55, 33, 0, 3000)
    WaitChrThread(0xA, 1)

    def lambda_113F():
        OP_95(0xFE, -12400, -3050, -23500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_113F)
    MoveCamera(30, 23, 0, 3000)
    WaitChrThread(0xA, 1)

    def lambda_1168():
        OP_95(0xFE, -2800, -3950, -27800, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1168)
    WaitChrThread(0xA, 1)

    def lambda_1186():
        OP_95(0xFE, 8100, -6350, -37500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1186)
    MoveCamera(55, 23, 0, 6000)
    WaitChrThread(0xA, 1)

    def lambda_11AF():
        OP_95(0xFE, 13600, -6500, -38400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11AF)
    Sleep(1700)
    OP_6B(0xFF)
    Fade(500)
    OP_68(11900, -5500, -38400, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(13600, -5500, -38400, 1500)
    MoveCamera(55, 19, 0, 1500)
    SetCameraDistance(19000, 1500)
    OP_A7(0x15, 0x37, 0x37, 0x37, 0xFF, 0x0)

    def lambda_1232():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1232)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)

    def lambda_124B():
        OP_95(0xFE, 11100, -6500, -31800, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_124B)
    WaitChrThread(0x15, 1)

    def lambda_1269():
        OP_95(0xFE, 11900, -6500, -38400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1269)
    WaitChrThread(0x15, 1)
    OP_93(0x15, 0x5A, 0x0)
    SetChrChipByIndex(0x15, 0x37)
    SetChrSubChip(0x15, 0x0)
    OP_6F(0x79)
    SetChrSubChip(0x15, 0x1)
    Sound(808, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0x15, 0x2)
    Sleep(300)
    SetChrFlags(0x15, 0x20)

    def lambda_12B1():
        OP_96(0xFE, 0x3070, 0xFFFFE69C, 0xFFFF6A00, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_12B1)
    SetChrSubChip(0x15, 0x3)
    PlayEffect(0x0, 0xFF, 0xA, 0x0, 200, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_E6()
    SetChrChipByIndex(0xA, 0x38)
    SetChrSubChip(0xA, 0x0)

    def lambda_130F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_130F)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Sound(830, 0, 100, 0)

    #N0015
    NpcTalk(
        0xA,
        "青装束の青年",
        "#2P#4Sがっ……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 2)
    WaitChrThread(0x15, 1)
    Sleep(300)

    def lambda_136B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_136B)
    SetChrSubChip(0xA, 0x1)
    Sleep(250)
    Fade(250)
    SetChrSubChip(0xA, 0x2)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x20)

    def lambda_13C9():
        OP_96(0xFE, 0x2CEC, 0xFFFFE69C, 0xFFFF6A00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_13C9)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x37)
    SetChrSubChip(0x15, 0x0)
    Sleep(300)

    #N0016
    NpcTalk(
        0x15,
        "サングラスの男",
        (
            "#6Pクク……\x01",
            "青ウサギを一匹と。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x17, 3, 0, 15)
    Sleep(400)
    BeginChrThread(0x16, 3, 0, 14)
    Sleep(400)
    BeginChrThread(0x18, 3, 0, 16)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x18, 3)

    #N0017
    NpcTalk(
        0x16,
        "サングラスの男",
        (
            "ハハ……\x01",
            "あっさり掛かってくれたな。\x02",
        )
    )

    CloseMessageWindow()

    #N0018
    NpcTalk(
        0x17,
        "サングラスの男",
        (
            "#11P時間はない……\x01",
            "とっとと痛めつけるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #N0019
    NpcTalk(
        0x17,
        "サングラスの男",
        "#11Pただし、殺さない程度にな。\x02",
    )

    CloseMessageWindow()

    #N0020
    NpcTalk(
        0x15,
        "サングラスの男",
        "#6Pクク……悪く思うなよ。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)

    def lambda_152B():
        OP_96(0xFE, 0x3070, 0xFFFFE69C, 0xFFFF6B2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_152B)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x37)
    SetChrSubChip(0x15, 0x0)
    Sleep(100)
    SetChrSubChip(0x15, 0x1)
    Sound(808, 0, 100, 0)
    Sleep(150)
    SetChrSubChip(0x15, 0x2)
    Sleep(500)
    StopBGM(0x5DC)
    #Sound(1091, 255, 100, 0)    #voice#Lloyd

    #N0021
    NpcTalk(
        0xA,
        "青装束の青年",
        "#8A──させるか！\x02",
    )
    #Auto

    Sleep(800)
    MoveCamera(53, 17, 0, 500)
    SetCameraDistance(17000, 500)
    Fade(100)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x20)

    def lambda_15E0():
        TurnDirection(0xFE, 0x15, 1000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15E0)
    Sleep(100)
    SetChrSubChip(0x15, 0x3)
    Sleep(50)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    PlayEffect(0x1, 0xFF, 0xA, 0x40, -300, 1000, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sound(830, 0, 100, 0)
    Sound(511, 0, 100, 0)
    OP_6F(0x50)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7507", 0)

    def lambda_1655():
        OP_A6(0xFE, 0x0, 0x14, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1655)

    def lambda_166E():
        OP_A6(0xFE, 0x0, 0x14, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_166E)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0xA, 2)
    WaitChrThread(0x15, 2)
    SetCameraDistance(18500, 500)
    PlayEffect(0x1, 0xFF, 0xA, 0x40, -300, 1000, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0x19, 0x3E)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x19, 12400, -5800, -38400, 0)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    BeginChrThread(0x19, 3, 0, 17)
    Sound(511, 0, 100, 0)
    Sound(532, 0, 100, 0)

    def lambda_177A():
        OP_9C(0xFE, 0xFFFFE4A8, 0xFFFFE69C, 0xFFFFE4A8, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_177A)
    SetChrChipByIndex(0x15, 0x3B)
    SetChrSubChip(0x15, 0x0)

    def lambda_179F():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_179F)

    def lambda_17B8():
        OP_9D(0xFE, 0x2B5C, 0xFFFFE69C, 0xFFFF68D4, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_17B8)
    WaitChrThread(0x15, 1)

    #N0022
    NpcTalk(
        0x15,
        "サングラスの男",
        "#6Pなっ……\x02",
    )

    CloseMessageWindow()

    #N0023
    NpcTalk(
        0x17,
        "サングラスの男",
        "#11Pなにぃ……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0xA, 0x3C)
    SetChrSubChip(0xA, 0x0)
    OP_0D()

    #N0024
    NpcTalk(
        0xA,
        "青装束の青年",
        "#11P……まったく。\x02",
    )

    CloseMessageWindow()

    #N0025
    NpcTalk(
        0xA,
        "青装束の青年",
        (
            "#11Pまさかここまで見事に\x01",
            "引っかかってくれるとはね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0026
    NpcTalk(
        0x18,
        "サングラスの男",
        "こ、こいつ……！？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x800)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 13600, -6500, -38400, 270)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    BeginChrThread(0xA, 3, 0, 13)
    BeginChrThread(0x101, 3, 0, 13)

    def lambda_1978():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1978)

    def lambda_1989():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1989)
    Sound(534, 0, 100, 0)
    WaitChrThread(0xA, 2)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    WaitChrThread(0x101, 3)
    ClearChrFlags(0x101, 0x800)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    #C0027
    ChrTalk(
        0x101,
        (
            "#0006F#11P現行犯逮捕と\x01",
            "行きたいところだけど……\x02\x03",

            "#0001F微妙に囮捜査くさいし、\x01",
            "今回は勘弁するしかないか。\x02",
        )
    )

    CloseMessageWindow()

    #N0028
    NpcTalk(
        0x16,
        "サングラスの男",
        "#6Pこいつ、まさか……\x02",
    )

    CloseMessageWindow()

    #N0029
    NpcTalk(
        0x17,
        "サングラスの男",
        "#11P警察の人間か……！？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 16050, -1100, -34600, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    #N0030
    NpcTalk(
        0x8,
        "少年の声",
        (
            "#12Pフフ……\x01",
            "彼はあくまで助っ人さ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x102, 14500, -1600, -34000, 180)
    SetChrPos(0x103, 14400, -1600, -32700, 180)
    SetChrPos(0x104, 15600, -1300, -32299, 180)
    OP_68(15200, -500, -35200, 2000)
    MoveCamera(53, 13, 0, 2000)
    SetCameraDistance(18000, 2000)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)

    def lambda_1BC2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1BC2)
    Sleep(50)

    def lambda_1BD2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_1BD2)
    Sleep(50)

    def lambda_1BE2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1BE2)
    Sleep(50)

    def lambda_1BF2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1BF2)
    OP_6F(0x79)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)

    #C0031
    ChrTalk(
        0x104,
        (
            "#5P#0309Fおーおー。\x01",
            "本当に引っかかるとはなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        "#5P#0202F……なかなかの読みですね。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#5P#0101Fロイド、大丈夫！？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#0004F#11Pああ……無傷だよ。\x02\x03",

            "#0000F念のため防護クッションを\x01",
            "頭巾に仕込んでおいて助かった。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    OP_68(13600, -5500, -38400, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    Sleep(500)

    #N0035
    NpcTalk(
        0x17,
        "サングラスの男",
        "クッ……\x02",
    )

    CloseMessageWindow()

    #N0036
    NpcTalk(
        0x18,
        "サングラスの男",
        (
            "まさか俺たちの存在を\x01",
            "嗅ぎ付けられていたとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#0400F#6Pさてと……\x01",
            "どうする、お兄さんたち？\x02\x03",

            "#0404Fこの場で投降するなら\x01",
            "大目に見てもいいけど……\x02\x03",

            "#0402F──それとも今度は、\x01",
            "アンタたちが狩られてみる？\x02",
        )
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0x15,
        "サングラスの男",
        "#5Pチッ……\x02",
    )

    CloseMessageWindow()

    #N0039
    NpcTalk(
        0x16,
        "サングラスの男",
        "２手に分かれるぞ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 3, 0, 12)
    Sleep(100)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)
    BeginChrThread(0x16, 3, 0, 11)
    Sleep(200)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)
    BeginChrThread(0x18, 3, 0, 12)
    Sleep(100)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)
    BeginChrThread(0x15, 3, 0, 11)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)

    #C0040
    ChrTalk(
        0x101,
        "#6P#0007Fま、待て……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 3)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)

    def lambda_1F17():
        OP_9D(0xFE, 0x3DB8, 0xFFFFE69C, 0xFFFF6A00, 0x190, 0x9C4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F17)
    WaitChrThread(0x8, 1)
    PlayEffect(0x2, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x3F)
    SetChrSubChip(0x8, 0x0)
    Sound(326, 0, 90, 0)
    Sleep(100)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    OP_93(0x8, 0x5A, 0x1F4)

    #C0041
    ChrTalk(
        0x8,
        "#0402F#5P──２人、付いてきて。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    BeginChrThread(0x8, 3, 0, 10)
    Sleep(300)

    #C0043
    ChrTalk(
        0x101,
        (
            "#6P#0011Fお、おい──\x02\x03",

            "#0013Fくっ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x8, 3)
    Fade(500)
    OP_68(13920, -500, -34160, 0)
    MoveCamera(53, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15500, 0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_0D()

    #C0044
    ChrTalk(
        0x102,
        "#5P#0101Fロイド、どうするの！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【エリィを呼ぶ】\x01",        # 0
            "【ティオを呼ぶ】\x01",        # 1
            "【ランディを呼ぶ】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20F2"),
        (1, "loc_218D"),
        (2, "loc_2224"),
        (SWITCH_DEFAULT, "loc_22BB"),
    )


    label("loc_20F2")

    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0045
    ChrTalk(
        0x101,
        (
            "#0007F#11Pエリィ、頼む！\x02\x03",

            "ランディとティオは\x01",
            "もう一組を追ってくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#5P#0101Fわかったわ！\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        "#5P#0302Fがってん承知の介だ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x45, 5)
    Jump("loc_22BB")

    label("loc_218D")

    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0048
    ChrTalk(
        0x101,
        (
            "#0007F#11Pティオ、来てくれ！\x02\x03",

            "エリィとランディは\x01",
            "もう一組の方を頼む！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        "#5P#0201F了解です……！\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        "#5P#0101Fわかったわ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x45, 6)
    Jump("loc_22BB")

    label("loc_2224")

    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0051
    ChrTalk(
        0x101,
        (
            "#0007F#11Pランディ、頼む！\x02\x03",

            "エリィとティオは\x01",
            "もう一組の方を！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        "#5P#0302Fがってん承知の介だ！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        "#5P#0201F了解です……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x45, 7)
    Jump("loc_22BB")

    label("loc_22BB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    OP_68(-12000, -500, -18000, 0)
    MoveCamera(30, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_EE(0x0, 0x1)
    SetChrPos(0x17, -12000, -3050, -24000, 0)
    SetChrPos(0x18, -12000, -3050, -24000, 0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x29)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x40)
    SetChrSubChip(0x10, 0x0)
    SetCameraDistance(17000, 2400)
    FadeToBright(1000, 0)
    BeginChrThread(0x17, 3, 0, 8)
    Sleep(400)
    BeginChrThread(0x18, 3, 0, 9)
    OP_6F(0x10)
    Fade(500)
    OP_68(-6200, 1000, -9000, 0)
    MoveCamera(30, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23500, 0)
    OP_68(1800, 1000, 2100, 4000)
    MoveCamera(45, 23, 0, 4000)
    SetCameraDistance(20500, 4000)
    WaitChrThread(0x17, 3)
    TurnDirection(0x17, 0x18, 500)
    WaitChrThread(0x18, 3)
    OP_6F(0x79)

    #N0054
    NpcTalk(
        0x17,
        "サングラスの男",
        (
            "#5Pクソ、まさか腰抜けの警察が\x01",
            "出張ってきてるとは……\x02",
        )
    )

    CloseMessageWindow()

    #N0055
    NpcTalk(
        0x17,
        "サングラスの男",
        (
            "#5Pこうなったら\x01",
            "いったん戻って応援を──\x02",
        )
    )

    CloseMessageWindow()

    #N0056
    NpcTalk(
        0x18,
        "サングラスの男",
        "#4Pま、待て！\x02",
    )

    CloseMessageWindow()

    #N0057
    NpcTalk(
        0x18,
        "サングラスの男",
        (
            "#4Pこんな失態、若頭にでも\x01",
            "知られちまったら……！\x02",
        )
    )

    CloseMessageWindow()

    #N0058
    NpcTalk(
        0x17,
        "サングラスの男",
        "#5Pくっ……\x02",
    )

    CloseMessageWindow()

    #N0059
    NpcTalk(
        0x17,
        "サングラスの男",
        (
            "#5Pまあいい、とにかく\x01",
            "俺たちだけでも先に──\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 1800, 0, 17500, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Sleep(200)
    Sound(1807, 255, 100, 0)    #voice#Wald
    Sleep(500)

    #N0060
    NpcTalk(
        0x9,
        "獰猛そうな声",
        "……どこに行くんだァ？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xB, -3800, 50, -4600, 45)
    SetChrPos(0xD, -4100, 0, -6300, 45)
    SetChrPos(0xE, -5400, 0, -5600, 45)
    SetChrPos(0xF, -700, 0, -7900, 0)
    SetChrPos(0x11, 8200, 50, -4000, 315)
    SetChrPos(0x12, 8000, 50, -5800, 315)
    SetChrPos(0x13, 3700, 0, -7600, 0)
    SetChrPos(0x14, 4700, 0, -8400, 0)
    SetChrPos(0x10, 9600, 0, -5700, 315)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2703():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2703)

    def lambda_2710():
        OP_96(0xFE, 0x708, 0x0, 0x1964, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2710)
    Sleep(1000)
    OP_68(1800, 1000, 0, 3000)
    MoveCamera(35, 25, 0, 3000)
    SetCameraDistance(21500, 3000)

    def lambda_2752():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_2752)

    def lambda_275F():
        OP_96(0xFE, 0xFFFFFCE0, 0x32, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_275F)

    def lambda_2779():
        OP_96(0xFE, 0x1450, 0x32, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2779)

    def lambda_2793():
        OP_96(0xFE, 0x1388, 0x32, 0xFFFFF510, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2793)
    Sleep(50)

    def lambda_27B0():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_27B0)

    def lambda_27CA():
        OP_96(0xFE, 0xFFFFF6A0, 0x0, 0xFFFFF5D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_27CA)
    Sleep(50)

    def lambda_27E7():
        OP_96(0xFE, 0x12C, 0x0, 0xFFFFF0C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_27E7)

    def lambda_2801():
        OP_96(0xFE, 0xA8C, 0x0, 0xFFFFF1F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2801)

    def lambda_281B():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFEED0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_281B)

    def lambda_2835():
        OP_96(0xFE, 0x19C8, 0x0, 0xFFFFF574, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2835)
    Sleep(2000)

    #N0061
    NpcTalk(
        0x17,
        "サングラスの男",
        "#6Pなっ……！？\x02",
    )

    WaitChrThread(0x9, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x14, 1)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)
    CloseMessageWindow()

    #N0062
    NpcTalk(
        0x18,
        "サングラスの男",
        "#5Pいつのまに……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-5500, 1500, -8400, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(17500, 1500)
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_29E7")
    SetChrPos(0x104, -9300, 0, -11500, 45)
    SetChrPos(0x103, -8700, 0, -12300, 45)

    def lambda_2958():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2958)
    Sleep(50)

    def lambda_2975():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0xFFFFDBAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2975)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x10)

    #C0063
    ChrTalk(
        0x103,
        "#12P#0204F詰み、ですね。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#6P#0300Fああ……\x01",
            "後はロイドたちの方だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B62")

    label("loc_29E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_2AAA")
    SetChrPos(0x104, -9300, 0, -11500, 45)
    SetChrPos(0x102, -8700, 0, -12300, 45)

    def lambda_2A17():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A17)
    Sleep(50)

    def lambda_2A34():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0xFFFFDBAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A34)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x10)

    #C0065
    ChrTalk(
        0x104,
        "#6P#0300Fこっちは詰み、だな。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#12P#0100Fええ……\x01",
            "後はロイドたちの方ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B62")

    label("loc_2AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_2B62")
    SetChrPos(0x102, -9300, 0, -11500, 45)
    SetChrPos(0x103, -8700, 0, -12300, 45)

    def lambda_2ADA():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2ADA)
    Sleep(50)

    def lambda_2AF7():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0xFFFFDBAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2AF7)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x10)

    #C0067
    ChrTalk(
        0x103,
        "#12P#0204F詰み、ですね。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#6P#0100Fええ……\x01",
            "後はロイドたちの方ね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B62")

    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_2B88")
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_2BA7")

    label("loc_2B88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_2B9A")
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_2BA7")

    label("loc_2B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_2BA7")
    AddParty(0x3, 0xEF, 0xFF)

    label("loc_2BA7")

    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    AddParty(0x4, 0xFF, 0xFF)
    OP_32(0x4, 0x0, 0x8)
    RemoveCraft(0x4, 0xFFFF)
    OP_38(0x4, 0x80, 0x1)
    OP_38(0x4, 0x81, 0x1)
    OP_38(0x4, 0x82, 0x1)
    OP_38(0x4, 0x83, 0x1)
    OP_38(0x4, 0x84, 0x1)
    OP_38(0x4, 0x85, 0x1)
    OP_42(0x4, 0x438, 0xFF)
    OP_42(0x4, 0x5DC, 0xFF)
    OP_42(0x4, 0x640, 0xFF)
    AddCraft(0x4, 0xBE)
    AddCraft(0x4, 0xBF)
    AddCraft(0x4, 0x10E)
    SetChrChipPat(0x4, 0x6, 0x10E)
    OP_42(0x4, 0x85, 0x0)
    OP_42(0x4, 0x76, 0x3)
    OP_42(0x4, 0x64, 0x4)
    OP_42(0x4, 0x6A, 0x5)
    OP_42(0x4, 0x7C, 0x6)
    OP_42(0x4, 0x70, 0x1)
    OP_42(0x4, 0x7F, 0x2)
    OP_68(10100, 800, -14500, 0)
    MoveCamera(15, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x105, 41400, -300, -34700, 270)
    SetChrPos(0x15, 16600, -2500, -21900, 315)
    SetChrPos(0x16, 17600, -2500, -21100, 315)

    def lambda_2C89():
        OP_96(0xFE, 0x2580, 0xFFFFFF38, 0xFFFFC5CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2C89)
    Sleep(50)

    def lambda_2CA6():
        OP_96(0xFE, 0x2968, 0xFFFFFF38, 0xFFFFC8EC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2CA6)
    SetCameraDistance(21000, 2000)
    FadeToBright(1000, 0)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x10)
    OP_68(1800, 1000, 0, 2000)
    MoveCamera(35, 25, 0, 2000)
    SetCameraDistance(21500, 2000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(10100, 800, -14500, 0)
    MoveCamera(15, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    OP_0D()

    #N0069
    NpcTalk(
        0x16,
        "サングラスの男",
        "#2P（チッ……マヌケが。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x16, 500)

    #N0070
    NpcTalk(
        0x15,
        "サングラスの男",
        (
            "#6P（仕方ない……\x01",
            "  抜け道を使うぞ……！）\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 5)
    Sleep(300)
    BeginChrThread(0x16, 3, 0, 6)
    Sleep(1200)
    Fade(500)
    OP_6B(0x15)
    OP_68(15450, 70, -20130, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)

    #C0071
    ChrTalk(
        0x105,
        "#0402F#2Pフフ、ご苦労さま。\x02",
    )

    CloseMessageWindow()

    #N0072
    NpcTalk(
        0x15,
        "サングラスの男",
        "#5Pい、いつの間に……！\x02",
    )

    CloseMessageWindow()

    #N0073
    NpcTalk(
        0x16,
        "サングラスの男",
        "#1Pクソ……下だ！\x02",
    )

    CloseMessageWindow()
    OP_68(35000, -5500, -39000, 1500)
    MoveCamera(37, 19, 0, 1500)
    SetCameraDistance(18000, 1500)
    SetChrPos(0x101, 22600, -6500, -39300, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_2F07")
    SetChrPos(0x102, 21700, -6500, -38700, 90)
    Jump("loc_2F40")

    label("loc_2F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_2F26")
    SetChrPos(0x103, 21700, -6500, -38700, 90)
    Jump("loc_2F40")

    label("loc_2F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_2F40")
    SetChrPos(0x104, 21700, -6500, -38700, 90)

    label("loc_2F40")

    BeginChrThread(0x16, 3, 0, 7)
    Sleep(150)
    OP_93(0x15, 0xB4, 0x2BC)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x4)
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2F68():
        OP_9D(0xFE, 0x8980, 0xFFFFE69C, 0xFFFF6AC8, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2F68)
    WaitChrThread(0x15, 1)
    PlayEffect(0x2, 0xFF, 0x15, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 0x3D)
    SetChrSubChip(0x15, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    OP_6F(0x79)
    SetChrPos(0x105, 31200, -800, -34200, 180)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(33130, -5500, -38360, 1000)

    def lambda_3038():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3038)

    def lambda_3045():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_3045)

    def lambda_3052():
        OP_96(0xFE, 0x7788, 0xFFFFE69C, 0xFFFF667C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3052)
    Sleep(50)

    def lambda_306F():
        OP_96(0xFE, 0x7404, 0xFFFFE69C, 0xFFFF68D4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_306F)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    #C0074
    ChrTalk(
        0x101,
        "#6P#0001F……ここまでだ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_30E9")

    #C0075
    ChrTalk(
        0x102,
        (
            "#6P#0103Fふう……\x01",
            "振り回してくれたわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3162")

    label("loc_30E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_3127")

    #C0076
    ChrTalk(
        0x103,
        (
            "#6P#0202F飛んで火に入る\x01",
            "夏の虫……ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3162")

    label("loc_3127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3162")

    #C0077
    ChrTalk(
        0x104,
        (
            "#6P#0302F飛んで火に入る\x01",
            "夏の虫ってヤツだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3162")


    #N0078
    NpcTalk(
        0x15,
        "サングラスの男",
        "#11Pくっ……！\x02",
    )

    CloseMessageWindow()
    SetChrChip(0x0, 0x105, 0x1E, 0x12C)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x1)

    def lambda_319A():
        OP_9D(0xFE, 0x79E0, 0xFFFFE69C, 0xFFFF6E4C, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_319A)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x105, 1)
    PlayEffect(0x2, 0xFF, 0x105, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x105, 0x3F)
    SetChrSubChip(0x105, 0x0)
    Sound(326, 0, 90, 0)
    Sleep(100)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrChip(0x1, 0x105, 0x0, 0x0)
    Sleep(300)
    OP_93(0x105, 0x5A, 0x1F4)
    Sleep(300)

    #C0079
    ChrTalk(
        0x105,
        (
            "#0404Fフフ……\x01",
            "鬼ごっこは終わりだよ。\x02\x03",

            "#0402Fそろそろ観念したかい？\x02",
        )
    )

    CloseMessageWindow()

    #N0080
    NpcTalk(
        0x15,
        "サングラスの男",
        "#11Pククク……\x02",
    )

    CloseMessageWindow()

    #N0081
    NpcTalk(
        0x16,
        "サングラスの男",
        "ははは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x15, 0x30)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x34)
    SetChrSubChip(0x16, 0x1)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0082
    NpcTalk(
        0x16,
        "サングラスの男",
        (
            "ガキどもが……\x01",
            "いい気になりやがって。\x02",
        )
    )

    CloseMessageWindow()

    #N0083
    NpcTalk(
        0x15,
        "サングラスの男",
        (
            "#11P俺たちプロを\x01",
            "本気にさせたこと……\x02",
        )
    )

    CloseMessageWindow()

    #N0084
    NpcTalk(
        0x15,
        "サングラスの男",
        "#11Pせいぜい後悔させてやる。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#6P#0013Fくっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_3427")
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 80, 0)
    Jump("loc_3466")

    label("loc_3427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_3449")
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Jump("loc_3466")

    label("loc_3449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3466")
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)

    label("loc_3466")

    OP_0D()
    Sleep(300)

    #C0086
    ChrTalk(
        0x105,
        (
            "#0404Fフフ、どうやら一戦、\x01",
            "交える必要がありそうだね。\x02\x03",

            "#0402F君たちの援護……\x01",
            "期待してもいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#6P#0000F……そっちこそ。\x01",
            "足手まといになるなよ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_3533")

    #C0088
    ChrTalk(
        0x102,
        "#6P#0107F……来るわ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3580")

    label("loc_3533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_355C")

    #C0089
    ChrTalk(
        0x103,
        "#6P#0207F……来ます！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3580")

    label("loc_355C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3580")

    #C0090
    ChrTalk(
        0x104,
        "#6P#0307F来るぞ……！\x02",
    )

    CloseMessageWindow()

    label("loc_3580")

    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15500, 300)
    SetChrChipByIndex(0x15, 0x31)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x0)

    def lambda_35B0():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_35B0)

    def lambda_35CA():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_35CA)
    Sleep(300)
    Battle("BattleInfo_65C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    Call(0, 18)
    Return()

    # Function_4_939 end

    def Function_5_3608(): pass

    label("Function_5_3608")

    ClearChrFlags(0x15, 0x4)
    OP_92(0xFE, 0x46B4, 0xFFFFA81C, 0x2BC)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)

    def lambda_3627():
        OP_95(0xFE, 18100, -2500, -22500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3627)
    WaitChrThread(0xFE, 1)

    def lambda_3645():
        OP_95(0xFE, 22000, -2500, -22500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3645)
    WaitChrThread(0xFE, 1)

    def lambda_3663():
        OP_95(0xFE, 22000, -3500, -28200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3663)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3694():
        OP_9D(0xFE, 0x55F0, 0xFFFFFDA8, 0xFFFF7F7C, 0xCE4, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3694)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 0x3D)
    SetChrSubChip(0x15, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)

    def lambda_36D9():
        OP_95(0xFE, 25200, -300, -32500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36D9)
    WaitChrThread(0xFE, 1)

    def lambda_36F7():
        OP_95(0xFE, 36500, -800, -34200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36F7)
    Sleep(1100)
    OP_6B(0xFF)
    Fade(500)
    OP_68(36500, 200, -34200, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_68(39000, 200, -33710, 1000)
    MoveCamera(50, 17, 0, 1000)
    SetCameraDistance(17000, 1000)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)
    Return()

    # Function_5_3608 end

    def Function_6_3794(): pass

    label("Function_6_3794")

    ClearChrFlags(0x16, 0x4)
    OP_92(0xFE, 0x46B4, 0xFFFFA81C, 0x2BC)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)

    def lambda_37B3():
        OP_95(0xFE, 18100, -2500, -22500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37B3)
    WaitChrThread(0xFE, 1)

    def lambda_37D1():
        OP_95(0xFE, 22000, -2500, -22500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37D1)
    WaitChrThread(0xFE, 1)

    def lambda_37EF():
        OP_95(0xFE, 22000, -3500, -28200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37EF)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3820():
        OP_9D(0xFE, 0x55F0, 0xFFFFFDA8, 0xFFFF7F7C, 0xCE4, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3820)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x16, 0x3D)
    SetChrSubChip(0x16, 0x1)
    Sleep(50)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)

    def lambda_3865():
        OP_95(0xFE, 25200, -300, -32500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3865)
    WaitChrThread(0xFE, 1)

    def lambda_3883():
        OP_95(0xFE, 35100, -800, -34200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3883)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Return()

    # Function_6_3794 end

    def Function_7_38C0(): pass

    label("Function_7_38C0")

    OP_93(0x16, 0xB4, 0x2BC)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x4)
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_38DF():
        OP_9D(0xFE, 0x87F0, 0xFFFFE69C, 0xFFFF6424, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_38DF)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x16, 1)
    PlayEffect(0x2, 0xFF, 0x16, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x16, 0x3D)
    SetChrSubChip(0x16, 0x1)
    Sound(326, 0, 90, 0)
    Sleep(100)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    Return()

    # Function_7_38C0 end

    def Function_8_395D(): pass

    label("Function_8_395D")

    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)

    def lambda_396A():
        OP_95(0xFE, -12000, 0, -12000, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_396A)
    WaitChrThread(0xFE, 1)

    def lambda_3988():
        OP_95(0xFE, 1800, 0, -5500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3988)
    WaitChrThread(0xFE, 1)

    def lambda_39A6():
        OP_95(0xFE, 1800, 0, 3000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_39A6)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    Return()

    # Function_8_395D end

    def Function_9_39C8(): pass

    label("Function_9_39C8")

    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)

    def lambda_39D5():
        OP_95(0xFE, -12000, 0, -12000, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39D5)
    WaitChrThread(0xFE, 1)

    def lambda_39F3():
        OP_95(0xFE, 1800, 0, -5500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39F3)
    WaitChrThread(0xFE, 1)

    def lambda_3A11():
        OP_95(0xFE, 1800, 0, 1500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3A11)
    WaitChrThread(0x18, 1)
    SetChrChipByIndex(0x18, 0x32)
    SetChrSubChip(0x18, 0x0)
    Return()

    # Function_9_39C8 end

    def Function_10_3A33(): pass

    label("Function_10_3A33")


    def lambda_3A38():
        OP_95(0xFE, 20900, -6500, -37000, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3A38)
    WaitChrThread(0x8, 1)

    def lambda_3A56():
        OP_95(0xFE, 20900, -5500, -33000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3A56)
    WaitChrThread(0x8, 1)
    Return()

    # Function_10_3A33 end

    def Function_11_3A70(): pass

    label("Function_11_3A70")


    def lambda_3A75():
        OP_95(0xFE, 7200, -6500, -36300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A75)
    WaitChrThread(0xFE, 1)

    def lambda_3A93():
        OP_95(0xFE, 2200, -4750, -32900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A93)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_3A70 end

    def Function_12_3AAD(): pass

    label("Function_12_3AAD")


    def lambda_3AB2():
        OP_95(0xFE, 21500, -6500, -36500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AB2)
    WaitChrThread(0xFE, 1)

    def lambda_3AD0():
        OP_95(0xFE, 21500, -4550, -30500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AD0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_3AAD end

    def Function_13_3AEA(): pass

    label("Function_13_3AEA")

    OP_A1(0xFE, 0x7D0, 0x8, 0x7, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6)
    Sleep(50)
    SetChrSubChip(0xFE, 0x7)
    Return()

    # Function_13_3AEA end

    def Function_14_3B00(): pass

    label("Function_14_3B00")

    ClearChrFlags(0xFE, 0x8)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0x16, 6000, -5100, -37200, 135)

    def lambda_3B20():
        OP_95(0xFE, 11100, -6450, -37200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3B20)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0x87, 0x1F4)
    Return()

    # Function_14_3B00 end

    def Function_15_3B41(): pass

    label("Function_15_3B41")

    ClearChrFlags(0xFE, 0x8)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0x17, 21000, -5750, -33500, 180)

    def lambda_3B61():
        OP_95(0xFE, 21000, -6500, -37000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3B61)
    WaitChrThread(0x17, 1)

    def lambda_3B7F():
        OP_95(0xFE, 16300, -6500, -37800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3B7F)
    WaitChrThread(0x17, 1)
    Return()

    # Function_15_3B41 end

    def Function_16_3B99(): pass

    label("Function_16_3B99")

    ClearChrFlags(0xFE, 0x8)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0x18, 21000, -5750, -33500, 180)

    def lambda_3BB9():
        OP_95(0xFE, 21000, -6500, -37000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3BB9)
    WaitChrThread(0x18, 1)

    def lambda_3BD7():
        OP_95(0xFE, 16300, -6500, -39500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3BD7)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x13B, 0x1F4)
    Return()

    # Function_16_3B99 end

    def Function_17_3BF8(): pass

    label("Function_17_3BF8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C16")
    OP_A1(0xFE, 0xFA0, 0x8, 0x1, 0x0, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2)
    Jump("Function_17_3BF8")

    label("loc_3C16")

    Return()

    # Function_17_3BF8 end

    def Function_18_3C17(): pass

    label("Function_18_3C17")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch30800.itc", 0x1E)
    LoadChrToIndex("chr/ch30900.itc", 0x1F)
    LoadChrToIndex("chr/ch31700.itc", 0x20)
    LoadChrToIndex("chr/ch31800.itc", 0x21)
    LoadChrToIndex("chr/ch00400.itc", 0x22)
    LoadChrToIndex("chr/ch00450.itc", 0x23)
    LoadChrToIndex("chr/ch00451.itc", 0x24)
    LoadChrToIndex("chr/ch02100.itc", 0x25)
    LoadChrToIndex("apl/ch50019.itc", 0x26)
    LoadChrToIndex("chr/ch02150.itc", 0x27)
    LoadChrToIndex("chr/ch02151.itc", 0x28)
    LoadChrToIndex("chr/ch06700.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00150.itc", 0x2B)
    LoadChrToIndex("chr/ch00250.itc", 0x2C)
    LoadChrToIndex("chr/ch00350.itc", 0x2D)
    LoadChrToIndex("chr/ch31000.itc", 0x2E)
    LoadChrToIndex("chr/ch31001.itc", 0x2F)
    LoadChrToIndex("chr/ch31053.itc", 0x30)
    LoadChrToIndex("chr/ch31100.itc", 0x31)
    LoadChrToIndex("chr/ch31101.itc", 0x32)
    LoadChrToIndex("chr/ch31153.itc", 0x33)
    LoadChrToIndex("chr/ch06000.itc", 0x34)
    LoadChrToIndex("apl/ch50010.itc", 0x35)
    LoadChrToIndex("apl/ch50015.itc", 0x36)
    LoadChrToIndex("apl/ch50028.itc", 0x37)
    LoadChrToIndex("apl/ch50027.itc", 0x38)
    LoadChrToIndex("apl/ch50363.itc", 0x39)
    LoadChrToIndex("chr/ch06800.itc", 0x3A)
    RemoveParty(0x4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_3D0C")
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_3D33")

    label("loc_3D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_3D22")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_3D33")

    label("loc_3D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3D33")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_3D33")

    OP_68(33260, -5500, -37300, 0)
    MoveCamera(31, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrChipByIndex(0x15, 0x30)
    SetChrSubChip(0x15, 0x3)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x3)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 35200, -6500, -38200, 270)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 34800, -6500, -39900, 270)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 31200, -6500, -37300, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 30600, -6500, -39300, 90)
    SetChrFlags(0x101, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_3E23")
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 29700, -6500, -38700, 90)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    Jump("loc_3E80")

    label("loc_3E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_3E54")
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 29700, -6500, -38700, 90)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x104, 0x8)
    Jump("loc_3E80")

    label("loc_3E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3E80")
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 29700, -6500, -38700, 90)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x102, 0x8)

    label("loc_3E80")

    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetCameraDistance(18000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    def lambda_3F52():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3F52)
    WaitChrThread(0x15, 2)

    #C0091
    ChrTalk(
        0x15,
        "#11P#50Wグッ……\x02",
    )

    CloseMessageWindow()

    def lambda_3F85():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_3F85)
    WaitChrThread(0x16, 2)

    #C0092
    ChrTalk(
        0x16,
        "#50W……ガキどもが……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_93(0x15, 0x13B, 0x0)
    SetChrChipByIndex(0x15, 0x39)
    SetChrSubChip(0x15, 0x0)
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x16, 0x39)
    SetChrSubChip(0x16, 0x1)
    OP_52(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    OP_0D()
    Sleep(500)
    PlayBGM("ed7103", 0)
    Sleep(300)

    #C0093
    ChrTalk(
        0x101,
        (
            "#6P#0006Fふう……\x01",
            "さすがに手強かったな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_40B5")

    #C0094
    ChrTalk(
        0x102,
        (
            "#3P#0101F使っていた銃も\x01",
            "最新の軍用拳銃みたいね。\x02\x03",

            "帝国製みたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_416A")

    label("loc_40B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_4117")

    #C0095
    ChrTalk(
        0x103,
        (
            "#3P#0201F……使っていた銃は\x01",
            "帝国製の軍用拳銃ですね。\x02\x03",

            "しかも最新のモデルかと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_416A")

    label("loc_4117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_416A")

    #C0096
    ChrTalk(
        0x104,
        (
            "#3P#0301F最新の軍用拳銃を\x01",
            "使ってやがったな……\x02\x03",

            "多分、帝国製だろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_416A")


    #C0097
    ChrTalk(
        0x8,
        (
            "#0404F密貿易で扱っている\x01",
            "武器の一部って所かな？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(31420, -5500, -37250, 1200)
    MoveCamera(31, 19, 0, 1200)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)
    OP_6F(0x79)

    #C0098
    ChrTalk(
        0x8,
        (
            "#5P#0402Fフフ、それにしても\x01",
            "君の演技もなかなかだったね。\x02\x03",

            "あの倒れ方……\x01",
            "堂に入っていたじゃない？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    ClearChrFlags(0x101, 0x800)

    def lambda_4269():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4269)
    Sleep(100)
    OP_93(0xEF, 0x5A, 0x1F4)

    #C0099
    ChrTalk(
        0x101,
        (
            "#12P#0003F……あんな作戦を伝えられたら\x01",
            "協力しないわけにいかないだろ。\x02\x03",

            "#0001F囮なんて役目、他の誰かに\x01",
            "やらせる訳にもいかないしな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_43A4")
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0100
    ChrTalk(
        0x102,
        (
            "#5P#0106Fはあ、それで危険な囮役を\x01",
            "買って出るんだもの……\x02\x03",

            "#0101Fこっちは気が気じゃなかったわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0101
    ChrTalk(
        0x101,
        "#12P#0006Fご、ごめん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_44F4")

    label("loc_43A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_4447")
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0102
    ChrTalk(
        0x103,
        (
            "#5P#0206Fでも、それで危険な囮役を\x01",
            "買って出るのはどうかと……\x02\x03",

            "#0211Fちょっとお人好し過ぎです。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0103
    ChrTalk(
        0x101,
        "#12P#0005Fそ、そうか……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_44F4")

    label("loc_4447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_44F4")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0104
    ChrTalk(
        0x104,
        (
            "#5P#0304Fま、それでヤバイ囮役を\x01",
            "買って出るんだからなぁ。\x02\x03",

            "#0302Fお人好しっつーか、\x01",
            "利用されるタイプっつーか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0105
    ChrTalk(
        0x101,
        "#12P#0001Fわ、悪かったな。\x02",
    )

    CloseMessageWindow()

    label("loc_44F4")


    #C0106
    ChrTalk(
        0x8,
        (
            "#5P#0402Fフフ、そんなお人好しじゃ\x01",
            "この先大変だと思うけどねぇ。\x02\x03",

            "#0409Fま、そういうタイプは\x01",
            "個人的には嫌いじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4576():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4576)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_459C")

    def lambda_458F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_458F)
    Jump("loc_45CD")

    label("loc_459C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_45B7")

    def lambda_45AA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_45AA)
    Jump("loc_45CD")

    label("loc_45B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_45CD")

    def lambda_45C5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_45C5)

    label("loc_45CD")

    Sleep(300)

    #C0107
    ChrTalk(
        0x101,
        "#12P#0011Fえ゛。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "#5P#0404Fフフ……\x02\x03",

            "#0402Fともかくこれで、落とし前を\x01",
            "付けることが出来そうだ。\x02\x03",

            "君たちの協力を感謝するよ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(1800, 900, 1500, 0)
    MoveCamera(30, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrChipByIndex(0x15, 0x38)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x17, 0x38)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x16, 0x38)
    SetChrSubChip(0x16, 0x1)
    SetChrChipByIndex(0x18, 0x38)
    SetChrSubChip(0x18, 0x1)
    SetChrPos(0x15, 1000, 0, 2000, 180)
    SetChrPos(0x16, 2600, 0, 2000, 180)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2600, 0, 3500, 90)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 1000, 0, 3500, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x29)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x3A)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x9, 4500, 0, 2800, 270)
    SetChrPos(0x11, 5600, 0, 1900, 270)
    SetChrPos(0x12, 5100, 0, 400, 315)
    SetChrPos(0x13, 6900, 0, 2100, 270)
    SetChrPos(0x14, 6500, 0, 100, 315)
    SetChrPos(0x10, 8000, 0, 500, 315)
    SetChrPos(0x8, -900, 0, 2800, 90)
    SetChrPos(0xB, -2000, 0, 1900, 90)
    SetChrPos(0xD, -1500, 0, 400, 45)
    SetChrPos(0xE, -3300, 0, 2100, 90)
    SetChrPos(0xF, -2900, 0, 100, 45)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x101, 1100, 0, -1200, 0)
    SetChrPos(0x102, 2500, 0, -1200, 0)
    SetChrPos(0x103, 800, 0, -2200, 0)
    SetChrPos(0x104, 2800, 0, -2200, 0)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    MoveCamera(37, 25, 0, 3000)
    SetCameraDistance(19500, 3000)
    FadeToBright(2000, 0)
    OP_6F(0x50)
    Sleep(500)

    #C0109
    ChrTalk(
        0x18,
        (
            "#11P#30Wガキどもが……\x01",
            "……調子に乗りやがって……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x17,
        (
            "#5P#30Wクク……\x01",
            "やっちまったなぁ、ガキども。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x17,
        (
            "#5P#30W俺たち《ルバーチェ》を\x01",
            "本気で怒らせちまうとはな……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x15,
        "#6P#30W警察のガキ共も同じだ……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x15,
        (
            "#6P#30Wこっちには偉い議員先生もいる。\x01",
            "タダで済むと思うなよ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#12P#0001F……こいつら………\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        "#1604F#4Pククク……\x02",
    )

    CloseMessageWindow()
    MoveCamera(33, 25, 0, 700)
    SetCameraDistance(18500, 700)

    def lambda_4A98():
        OP_96(0xFE, 0xC80, 0x0, 0xD48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4A98)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x17, 0x31)
    SetChrSubChip(0x17, 0x0)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x20)

    def lambda_4AD3():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_4AD3)

    def lambda_4AEC():
        OP_98(0xFE, 0xC8, 0x1C2, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4AEC)
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x9, 0x36)
    SetChrSubChip(0x9, 0x0)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x17, 2)
    OP_6F(0x50)

    #C0116
    ChrTalk(
        0x17,
        "#40Wぐっ……？\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "#4P#1602Fどうやらお仕置きが\x01",
            "足りなかったみてぇだなァ……？\x02\x03",

            "全員サンドバックみたいに吊るして\x01",
            "血ダルマにしてもいいんだぜ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x17,
        "#40Wくっ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    #C0119
    ChrTalk(
        0x101,
        (
            "#6P#0007F待ってくれ！\x01",
            "さすがにそれは……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0120
    ChrTalk(
        0x8,
        (
            "#0400Fまあまあ。\x01",
            "ここは僕たちに任せてよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    def lambda_4C41():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C41)
    Sleep(300)

    #C0121
    ChrTalk(
        0x8,
        (
            "#6P#0403F──ヴァルド。\x01",
            "あまりやり過ぎは良くない。\x02\x03",

            "#0400Fこのお兄さんたちだってプロだ。\x02\x03",

            "あまりメンツを潰しちゃったら\x01",
            "なりふり構わなくなるんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        "#4P#1603Fケッ……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 0x37)
    SetChrSubChip(0x9, 0x0)

    def lambda_4D0D():
        OP_9D(0xFE, 0x6A4, 0x0, 0xDAC, 0x32, 0xFA0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4D0D)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x30)
    SetChrSubChip(0x17, 0x3)

    def lambda_4D3C():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_4D3C)
    Sound(819, 0, 100, 0)
    WaitChrThread(0x17, 2)
    ClearChrFlags(0x17, 0x4)
    ClearChrFlags(0x17, 0x20)

    #C0123
    ChrTalk(
        0x17,
        "#50Wゴホッ、ゴホッ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(37, 25, 0, 700)
    SetCameraDistance(19500, 700)
    Fade(250)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)

    def lambda_4DA9():
        OP_96(0xFE, 0x1068, 0x0, 0xAF0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4DA9)
    WaitChrThread(0x9, 1)
    OP_6F(0x50)
    Sleep(300)

    #C0124
    ChrTalk(
        0x8,
        (
            "#3P#0404Fフフ、お兄さんたちだって\x01",
            "表沙汰にはしたくないだろう？\x02\x03",

            "#0402F僕たちガキども相手に\x01",
            "プロがちょっかいかけた挙句に\x01",
            "返り討ちに遭ったなんて……\x02\x03",

            "#0409F……みっともなくて\x01",
            "上には報告できないよねぇ？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x18,
        "#11Pぐっ……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x16,
        (
            "#6P……ふざけろ……\x01",
            "その気になればいくらでも……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 1800, 0, 20000, 180)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    Sleep(150)

    #N0127
    NpcTalk(
        0xC,
        "女性の声",
        (
            "#4Pいや～、さすがに\x01",
            "ここが退き時じゃないかしら？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(817, 0, 100, 0)
    FadeToDark(100, 16777215, -1)
    OP_0D()
    Sleep(100)
    FadeToBright(500, 16777215)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x18, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_510F():

        label("loc_510F")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_510F")

    QueueWorkItem2(0x8, 2, lambda_510F)

    def lambda_5121():

        label("loc_5121")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5121")

    QueueWorkItem2(0xB, 2, lambda_5121)

    def lambda_5133():

        label("loc_5133")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5133")

    QueueWorkItem2(0xD, 2, lambda_5133)

    def lambda_5145():

        label("loc_5145")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5145")

    QueueWorkItem2(0xE, 2, lambda_5145)

    def lambda_5157():

        label("loc_5157")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5157")

    QueueWorkItem2(0xF, 2, lambda_5157)

    def lambda_5169():

        label("loc_5169")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5169")

    QueueWorkItem2(0x9, 2, lambda_5169)

    def lambda_517B():

        label("loc_517B")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_517B")

    QueueWorkItem2(0x11, 2, lambda_517B)

    def lambda_518D():

        label("loc_518D")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_518D")

    QueueWorkItem2(0x12, 2, lambda_518D)

    def lambda_519F():

        label("loc_519F")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_519F")

    QueueWorkItem2(0x13, 2, lambda_519F)

    def lambda_51B1():

        label("loc_51B1")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_51B1")

    QueueWorkItem2(0x14, 2, lambda_51B1)

    def lambda_51C3():

        label("loc_51C3")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_51C3")

    QueueWorkItem2(0x10, 2, lambda_51C3)
    Fade(500)
    OP_68(1800, 1000, 9000, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0xC, 1800, 0, 15000, 180)
    ClearChrFlags(0xC, 0x8)
    SetChrPos(0x15, 1000, 0, 2000, 0)
    SetChrPos(0x16, 2600, 0, 2000, 0)
    SetChrChipByIndex(0x17, 0x38)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x17, 2600, 0, 3500, 0)
    SetChrPos(0x18, 1000, 0, 3500, 0)
    OP_68(1800, 1000, 4000, 3500)
    SetCameraDistance(20500, 3500)

    def lambda_5284():
        OP_95(0xFE, 1800, 0, 6000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5284)
    WaitChrThread(0xC, 1)
    SetChrChipByIndex(0xC, 0x35)
    SetChrSubChip(0xC, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xC, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xC, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    EndChrThread(0x8, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xE, 0x2)
    EndChrThread(0xF, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x12, 0x2)
    EndChrThread(0x13, 0x2)
    EndChrThread(0x14, 0x2)
    EndChrThread(0x10, 0x2)
    OP_6F(0x11)

    #C0128
    ChrTalk(
        0x101,
        "#0011Fグレイスさん……！？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        "#0105Fどうしてここに……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0130
    AnonymousTalk(
        0xC,
        (
            "うふふん、実はこの数日、\x01",
            "君たちの動きに注目してたのよ。\x02\x03",

            "そしたら予想通り、\x01",
            "色々やらかしてくれるじゃない！\x02\x03",

            "いや～、なかなか\x01",
            "面白い記事が書けそうだわ♪\x02",
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

    #C0131
    ChrTalk(
        0x15,
        "#12Pて、てめえ……！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x16,
        (
            "#4P雑誌社ごときが\x01",
            "《ルバーチェ》相手に……！\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        (
            "#5P#2106Fま、ウチも色々あるから\x01",
            "名前は出せないと思うけどね。\x02\x03",

            "#2100Fでもこれ以上、\x01",
            "みっともない真似をしたら\x01",
            "どうなるか判らないわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x16,
        "#4Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x17,
        (
            "#2P……いいだろう。\x01",
            "この場は退いてやる……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x17,
        "#2Pだが、もし約束を破ったら……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xC,
        (
            "#5P#2104Fはいはい、判ったわ。\x02\x03",

            "#2101Fあなた達こそ\x01",
            "これで手打ちっていう約束は\x01",
            "ちゃんと守りなさいよね。\x02\x03",

            "これ以上、一線を越えたら\x01",
            "遊撃士が出張ってくるかもよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0138
    ChrTalk(
        0x17,
        "#2Pなっ……！\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        "#0005Fえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xC,
        (
            "#5P#2103F実はこの件、アリオスさんが\x01",
            "介入するつもりだったらしいの。\x02\x03",

            "#2100Fでも、多忙だったらしいし、\x01",
            "あなたたちが先に介入してたから\x01",
            "今回は譲ってあげたんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#0011Fそ、そんな……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        "#0306Fまた掌#2Rてのひら#の上、ってか？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        "#0211F……みたいですね。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x15,
        "#6Pば、馬鹿馬鹿しい……！\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x15,
        (
            "#6Pアリオス・マクレイン相手に\x01",
            "こんなケチな事をやってられるか！\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x18,
        (
            "#5P……これ以上、\x01",
            "この薄汚い場所には用はねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x18,
        "#5P引き上げるぞ……！\x02",
    )

    CloseMessageWindow()
    Fade(250)

    def lambda_58DF():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_58DF)
    SetChrChipByIndex(0x18, 0x31)
    SetChrSubChip(0x18, 0x0)
    Sleep(350)

    def lambda_5903():

        label("loc_5903")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_5903")

    QueueWorkItem2(0xC, 2, lambda_5903)

    def lambda_5915():
        OP_96(0xFE, 0x9C4, 0x0, 0x189C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5915)
    SetChrChipByIndex(0x18, 0x32)
    SetChrSubChip(0x18, 0x0)
    BeginChrThread(0x18, 3, 0, 21)
    Fade(250)

    def lambda_5942():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_5942)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    Sleep(350)
    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 3, 0, 21)
    Fade(250)

    def lambda_5979():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5979)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    Sleep(350)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)
    BeginChrThread(0x15, 3, 0, 21)
    Fade(250)

    def lambda_59B0():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_59B0)
    SetChrChipByIndex(0x16, 0x31)
    SetChrSubChip(0x16, 0x0)
    Sleep(350)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    BeginChrThread(0x16, 3, 0, 21)
    Sleep(2000)
    OP_68(1800, 1000, 2000, 3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    EndChrThread(0xC, 0x2)

    def lambda_5A42():
        OP_95(0xFE, 1800, 0, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5A42)
    WaitChrThread(0xC, 1)

    def lambda_5A60():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_5A60)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_6F(0x1)
    WaitChrThread(0x18, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)

    #C0148
    ChrTalk(
        0x8,
        (
            "#3P#0406Fやれやれ……\x01",
            "《風の剣聖》アリオスか。\x02\x03",

            "#0400F噂だけは聞いてるけど\x01",
            "あそこまで効果覿面#8Rこうかてきめん#とはねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        "#1601Fケッ……気に喰わねぇな。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x1F4)
    Sleep(300)

    #C0150
    ChrTalk(
        0x9,
        (
            "#6P#1604Fまあいい……\x01",
            "今回の件はこれで終わりだ！\x02\x03",

            "#1602Fお前ら、引き上げるぞ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5BB7():

        label("loc_5BB7")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5BB7")

    QueueWorkItem2(0x101, 2, lambda_5BB7)

    def lambda_5BC9():

        label("loc_5BC9")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5BC9")

    QueueWorkItem2(0x102, 2, lambda_5BC9)

    def lambda_5BDB():

        label("loc_5BDB")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5BDB")

    QueueWorkItem2(0x103, 2, lambda_5BDB)

    def lambda_5BED():

        label("loc_5BED")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5BED")

    QueueWorkItem2(0x104, 2, lambda_5BED)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(400, 10, -1, -1)
    SetChrName("サーベルバイパーたち")

    #A0151
    AnonymousTalk(
        0xFF,
        "#4Sオッス！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_5C4F():

        label("loc_5C4F")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5C4F")

    QueueWorkItem2(0x8, 2, lambda_5C4F)

    def lambda_5C61():

        label("loc_5C61")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5C61")

    QueueWorkItem2(0xB, 2, lambda_5C61)

    def lambda_5C73():

        label("loc_5C73")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5C73")

    QueueWorkItem2(0xD, 2, lambda_5C73)

    def lambda_5C85():

        label("loc_5C85")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5C85")

    QueueWorkItem2(0xE, 2, lambda_5C85)

    def lambda_5C97():

        label("loc_5C97")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5C97")

    QueueWorkItem2(0xF, 2, lambda_5C97)

    def lambda_5CA9():

        label("loc_5CA9")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5CA9")

    QueueWorkItem2(0x11, 2, lambda_5CA9)

    def lambda_5CBB():

        label("loc_5CBB")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5CBB")

    QueueWorkItem2(0x12, 2, lambda_5CBB)

    def lambda_5CCD():

        label("loc_5CCD")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5CCD")

    QueueWorkItem2(0x13, 2, lambda_5CCD)

    def lambda_5CDF():

        label("loc_5CDF")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5CDF")

    QueueWorkItem2(0x14, 2, lambda_5CDF)

    def lambda_5CF1():

        label("loc_5CF1")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5CF1")

    QueueWorkItem2(0x10, 2, lambda_5CF1)

    def lambda_5D03():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5D03)
    Sleep(500)

    def lambda_5D20():
        OP_96(0xFE, 0xFA0, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5D20)
    Sleep(800)
    BeginChrThread(0x11, 3, 0, 19)
    WaitChrThread(0x12, 1)
    Sleep(1500)
    EndChrThread(0x12, 0x2)

    def lambda_5D4E():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5D4E)
    Sleep(100)
    BeginChrThread(0x13, 3, 0, 19)
    Sleep(1000)
    EndChrThread(0x14, 0x2)

    def lambda_5D78():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5D78)
    Sleep(600)
    EndChrThread(0x10, 0x2)

    def lambda_5D99():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5D99)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 1)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x8, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xE, 0x2)
    EndChrThread(0xF, 0x2)

    def lambda_5E1F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5E1F)
    Sleep(150)

    def lambda_5E2F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5E2F)
    Sleep(50)

    def lambda_5E3F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_5E3F)

    def lambda_5E4C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_5E4C)
    TurnDirection(0xF, 0x101, 500)

    #C0152
    ChrTalk(
        0x8,
        (
            "#5P#0404Fフフ……\x01",
            "君たちもお疲れさま。\x02\x03",

            "#0400Fこれにて任務、無事完了かい？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5EB0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5EB0)
    Sleep(50)

    def lambda_5EC0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5EC0)
    Sleep(50)

    def lambda_5ED0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5ED0)
    Sleep(50)

    def lambda_5EE0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5EE0)
    Sleep(300)

    #C0153
    ChrTalk(
        0x101,
        (
            "#0005F#11Pあ、ああ……そうだな。\x02\x03",

            "#0004F元々は、君たちの喧嘩を\x01",
            "止めるのが任務だったけど……\x02\x03",

            "#0000Fまあ、今後はもう、\x01",
            "お互い争わなくて済むだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        "#5P#0405Fえ、なに言ってるの？\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#0011F#11Pへ……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "#5P……マフィアが\x01",
            "絡んでいようがいまいが\x01",
            "バイパーとの関係は変わらん。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "#5Pお互い目障りというのは\x01",
            "変わるわけではないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x8,
        (
            "#5P#0404F全員揃っての潰し合いは\x01",
            "さすがにやらないだろうけど……\x02\x03",

            "#0402Fま、普通の喧嘩や小競り合いは\x01",
            "これからも続けて行くだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#0001F#11Pちょ、待ってくれ……！\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "#5P#0402Fフフ、大事#4Rおおごと#にしたくなければ\x01",
            "また介入してきたらどうだい？\x02\x03",

            "なんだったらそのまま\x01",
            "喧嘩に参加してくれてもいい。\x02\x03",

            "#0409F君たちなら大歓迎さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        "#0006F#11Pあ、あのな……\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        (
            "#0106Fあんまり冗談には\x01",
            "聞こえないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "#5P#0404Fフフ……\x01",
            "それでは良い夢を。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(200)

    #C0164
    ChrTalk(
        0x8,
        "#5P#0402F──行くよ。\x02",
    )

    CloseMessageWindow()

    def lambda_6234():

        label("loc_6234")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6234")

    QueueWorkItem2(0xD, 2, lambda_6234)

    def lambda_6246():

        label("loc_6246")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6246")

    QueueWorkItem2(0xE, 2, lambda_6246)

    def lambda_6258():

        label("loc_6258")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6258")

    QueueWorkItem2(0xF, 2, lambda_6258)
    OP_93(0xB, 0xE1, 0x1F4)
    Sleep(300)

    #C0165
    ChrTalk(
        0xB,
        "#5P聖戦終了──撤収する。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(50, 170, -1, -1)
    SetChrName("テスタメンツたち")

    #A0166
    AnonymousTalk(
        0xFF,
        "#4S了解#4R ヤー#！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_62E4():

        label("loc_62E4")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_62E4")

    QueueWorkItem2(0x101, 2, lambda_62E4)

    def lambda_62F6():

        label("loc_62F6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_62F6")

    QueueWorkItem2(0x102, 2, lambda_62F6)

    def lambda_6308():

        label("loc_6308")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6308")

    QueueWorkItem2(0x103, 2, lambda_6308)

    def lambda_631A():

        label("loc_631A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_631A")

    QueueWorkItem2(0x104, 2, lambda_631A)

    def lambda_632C():

        label("loc_632C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_632C")

    QueueWorkItem2(0xC, 2, lambda_632C)

    def lambda_633E():
        OP_95(0xFE, -4200, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_633E)
    Sleep(500)

    def lambda_635B():
        OP_96(0xFE, 0xFFFFFE70, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_635B)
    Sleep(800)
    BeginChrThread(0xB, 3, 0, 20)
    WaitChrThread(0xD, 1)
    Sleep(1500)
    EndChrThread(0xD, 0x2)

    def lambda_6389():
        OP_95(0xFE, -4200, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6389)
    Sleep(100)
    EndChrThread(0xC, 0x2)

    def lambda_63AA():
        OP_95(0xFE, 1800, 0, 1000, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_63AA)
    BeginChrThread(0xE, 3, 0, 20)
    Sleep(1000)
    EndChrThread(0xF, 0x2)

    def lambda_63D1():
        OP_95(0xFE, -4200, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_63D1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xC, 1)
    TurnDirection(0xC, 0x8, 500)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    Fade(500)
    OP_68(1800, 1000, -1200, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_0D()

    #C0167
    ChrTalk(
        0x101,
        "#5P#0011F……………………………\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        "#5P#0203F……懲りない人たちですね。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        (
            "#0300F#11Pま、血の気の多い連中だし、\x01",
            "喧嘩くらいは仕方ないかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        (
            "#5P#0106Fふう……そうみたいね。\x02\x03",

            "#0100Fまあ、今回の件に関しては\x01",
            "解決でいいんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0171
    ChrTalk(
        0x102,
        "#11P#0102Fね、ロイド？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0172
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあ、ああ……そうだな。\x02\x03",

            "#0008Fちょっとばかり……\x01",
            "スッキリしない気分だけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    #C0173
    ChrTalk(
        0xC,
        (
            "#2104Fふふ、自分たちの力だけで\x01",
            "解決できた気になれない……\x02\x03",

            "#2100Fそんな気分ってところかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1800, 1000, -100, 1000)

    def lambda_668C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_668C)
    Sleep(100)

    def lambda_669C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_669C)

    def lambda_66A9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_66A9)

    def lambda_66B6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_66B6)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    #C0174
    ChrTalk(
        0x101,
        "#12P#0005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xC,
        (
            "#5P#2101F小さい、小さいわねぇ。\x02\x03",

            "#2103F必要とあらば、\x01",
            "ためらわずに他人の力も借りて\x01",
            "より大きな真実を掴み取る……\x02\x03",

            "それが出来てこそ、\x01",
            "一人前の捜査官じゃないの？\x02\x03",

            "#2102F──あなたのお兄さんみたいな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0176
    ChrTalk(
        0x101,
        "#12P#0005Fなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xC,
        (
            "#2104F#5Pふふ、さてと……\x01",
            "お姉さんも撤退しようかな。\x02\x03",

            "#2110Fそろそろお肌の年齢が\x01",
            "気になる年頃なのよね～。\x02\x03",

            "#2109Fそれじゃ、おやすみなさ～い♪\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x1F4)

    def lambda_6884():
        OP_95(0xFE, 1600, 0, 15000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6884)
    Sleep(2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)
    OP_68(2600, 1000, -1250, 1200)

    def lambda_68CD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_68CD)
    Sleep(50)

    def lambda_68DD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_68DD)
    Sleep(50)

    def lambda_68ED():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_68ED)
    WaitChrThread(0x103, 2)
    OP_6F(0x1)

    #C0178
    ChrTalk(
        0x104,
        (
            "#0300Fお前の兄貴……\x01",
            "結構、知られてるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x102,
        (
            "#11P#0100F何だかとっても\x01",
            "優秀な人だったみたいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#5P#0002F……はは。\x02\x03",

            "#0004F押しの強さと行動力だけは\x01",
            "ピカイチだったみたいだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        "#12P#0200F………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0182
    ChrTalk(
        0x101,
        (
            "#5P#0003F──任務完了だ。\x02\x03",

            "#0000F支援課に戻って\x01",
            "セルゲイ課長に報告しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 3)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_3C17 end

    def Function_19_6A7A(): pass

    label("Function_19_6A7A")

    EndChrThread(0xFE, 0x2)

    def lambda_6A83():
        OP_95(0xFE, 5100, 0, 400, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A83)
    WaitChrThread(0xFE, 1)

    def lambda_6AA1():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6AA1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_6A7A end

    def Function_20_6ABB(): pass

    label("Function_20_6ABB")

    EndChrThread(0xFE, 0x2)

    def lambda_6AC4():
        OP_95(0xFE, -1500, 0, 400, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6AC4)
    WaitChrThread(0xFE, 1)

    def lambda_6AE2():
        OP_95(0xFE, -4200, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6AE2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_6ABB end

    def Function_21_6AFC(): pass

    label("Function_21_6AFC")


    def lambda_6B01():
        OP_95(0xFE, 800, 0, 5000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B01)
    WaitChrThread(0xFE, 1)

    def lambda_6B1F():
        OP_95(0xFE, 800, 0, 25000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B1F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_6AFC end

    SaveToFile()

Try(main)
