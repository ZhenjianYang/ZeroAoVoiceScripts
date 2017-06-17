from ZeroScenarioHelper import *

def main():
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
        "瓦吉",                   # 1
        "瓦鲁多",                 # 2
        "变装罗伊德",             # 3
        "阿巴斯",                 # 4
        "格蕾丝",                 # 5
        "蓝衣青年",               # 6
        "蓝衣青年",               # 7
        "蓝衣青年",               # 8
        "迪诺",                   # 9
        "红衣青年",               # 10
        "红衣青年",               # 11
        "红衣青年",               # 12
        "红衣青年",               # 13
        "黑手党",                 # 14
        "黑手党",                 # 15
        "黑手党",                 # 16
        "黑手党",                 # 17
        "巴特",                   # 18
        "BC141b",                 # 19
        "中央广场",               # 20
        "西街",                   # 21
        "行政区",                 # 22
        "住宅街",                 # 23
        "欢乐街",                 # 24
        "东街",                   # 25
        "旧城区",                 # 26
        "港湾区",                 # 27
        "ＩＢＣ",                 # 28
        "站前街道",               # 29
        "后巷",                   # 30
        "乌尔斯拉间道",           # 31
        "东克洛斯贝尔街道",       # 32
        "西克洛斯贝尔街道",       # 33
        "玛因兹山道",             # 34
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

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "中央广场")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "西街")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "行政区")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "住宅街")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "欢乐街")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "东街")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "旧城区")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "站前街道")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "后巷")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-238.0500030517578, 0.0, 225.39999389648438, 0x0000, 0x0000, "玛因兹山道")
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
        "Function_4_922",          # 04, 4
        "Function_5_3473",         # 05, 5
        "Function_6_35FF",         # 06, 6
        "Function_7_372B",         # 07, 7
        "Function_8_37C8",         # 08, 8
        "Function_9_3833",         # 09, 9
        "Function_10_389E",        # 0A, 10
        "Function_11_38DB",        # 0B, 11
        "Function_12_3918",        # 0C, 12
        "Function_13_3955",        # 0D, 13
        "Function_14_396B",        # 0E, 14
        "Function_15_39AC",        # 0F, 15
        "Function_16_3A04",        # 10, 16
        "Function_17_3A63",        # 11, 17
        "Function_18_3A82",        # 12, 18
        "Function_19_6726",        # 13, 19
        "Function_20_6767",        # 14, 20
        "Function_21_67A8",        # 15, 21
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D9")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('加速跑鞋', 1)"), scpexpr(EXPR_END)), "loc_86B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '加速跑鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_8D4")

    label("loc_86B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '加速跑鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '加速跑鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_8D4")

    Jump("loc_916")

    label("loc_8D9")

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

    label("loc_916")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7EC end

    def Function_4_922(): pass

    label("Function_4_922")

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
            "──三天过去了。\x02\x03",

            "原本一触即发的不良团伙斗争，\x01",
            "自那之后就再没发生过一起……\x02\x03",

            "旧城区恢复了和平的氛围，\x01",
            "平静得甚至有些不自然。\x02\x03",

            "随后──\x07\x00\x02",
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

    def lambda_C0F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C0F)
    Sleep(50)

    def lambda_C2C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_C2C)
    Sleep(50)

    def lambda_C49():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_C49)
    Sleep(50)

    def lambda_C66():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_C66)
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
        "戴墨镜的男人",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P嘁……真是安静啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0006
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        (
            "#5P我们都已经做到那种地步了，\x01",
            "他们怎么还不开始互相残杀啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x15, 500)

    #N0007
    NpcTalk(
        0x18,
        "戴墨镜的男人",
        (
            "#5P哼哼……\x01",
            "只缺少最后的关键一步而已啦。\x02",
        )
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x18,
        "戴墨镜的男人",
        (
            "#5P只要点燃导火线，\x01",
            "他们马上就会杀作一团。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DC6():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_DC6)
    Sleep(100)

    def lambda_DD6():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_DD6)
    Sleep(50)
    TurnDirection(0x17, 0x16, 500)
    Sleep(300)

    #N0009
    NpcTalk(
        0x16,
        "戴墨镜的男人",
        (
            "#2P剑蛇帮和圣书会，\x01",
            "向哪边的小鬼下手都可以……\x02",
        )
    )

    CloseMessageWindow()

    #N0010
    NpcTalk(
        0x16,
        "戴墨镜的男人",
        "#2P只要看到了就可以动手。\x02",
    )

    CloseMessageWindow()

    #N0011
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        "#6P小鬼们，要小心别被我们发现哦！\x02",
    )

    CloseMessageWindow()

    #N0012
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        (
            "#6P如果发现了剑蛇帮成员就用弹弓，\x01",
            "圣书会成员就从背后给他一击。\x02",
        )
    )

    CloseMessageWindow()

    #N0013
    NpcTalk(
        0x17,
        "戴墨镜的男人",
        "#1P嗯……\x02",
    )

    CloseMessageWindow()

    #N0014
    NpcTalk(
        0x18,
        "戴墨镜的男人",
        "#5P呵呵……狩猎开始啦。\x02",
    )

    CloseMessageWindow()
    OP_E5()

    def lambda_F29():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_F29)
    Sleep(100)

    def lambda_F39():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_F39)
    Sleep(50)

    def lambda_F49():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_F49)
    Sleep(50)

    def lambda_F59():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_F59)
    WaitChrThread(0x15, 2)

    def lambda_F6A():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_F6A)
    WaitChrThread(0x16, 2)
    Sleep(100)

    def lambda_F8B():
        OP_97(0xFE, 0x5DC, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_F8B)
    WaitChrThread(0x18, 2)
    Sleep(100)

    def lambda_FAC():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_FAC)
    WaitChrThread(0x17, 2)
    Sleep(100)

    def lambda_FCD():
        OP_97(0xFE, 0xBB8, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_FCD)
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

    def lambda_109C():
        OP_95(0xFE, -19000, 0, -10300, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_109C)
    WaitChrThread(0xA, 1)
    OP_6B(0xA)

    def lambda_10BD():
        OP_95(0xFE, -12400, 0, -12800, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10BD)
    MoveCamera(55, 33, 0, 3000)
    WaitChrThread(0xA, 1)

    def lambda_10E6():
        OP_95(0xFE, -12400, -3050, -23500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10E6)
    MoveCamera(30, 23, 0, 3000)
    WaitChrThread(0xA, 1)

    def lambda_110F():
        OP_95(0xFE, -2800, -3950, -27800, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_110F)
    WaitChrThread(0xA, 1)

    def lambda_112D():
        OP_95(0xFE, 8100, -6350, -37500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_112D)
    MoveCamera(55, 23, 0, 6000)
    WaitChrThread(0xA, 1)

    def lambda_1156():
        OP_95(0xFE, 13600, -6500, -38400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1156)
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

    def lambda_11D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_11D9)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)

    def lambda_11F2():
        OP_95(0xFE, 11100, -6500, -31800, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_11F2)
    WaitChrThread(0x15, 1)

    def lambda_1210():
        OP_95(0xFE, 11900, -6500, -38400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1210)
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

    def lambda_1258():
        OP_96(0xFE, 0x3070, 0xFFFFE69C, 0xFFFF6A00, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1258)
    SetChrSubChip(0x15, 0x3)
    PlayEffect(0x0, 0xFF, 0xA, 0x0, 200, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_E6()
    SetChrChipByIndex(0xA, 0x38)
    SetChrSubChip(0xA, 0x0)

    def lambda_12B6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_12B6)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Sound(830, 0, 100, 0)

    #N0015
    NpcTalk(
        0xA,
        "蓝衣青年",
        "#2P#4S啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 2)
    WaitChrThread(0x15, 1)
    Sleep(300)

    def lambda_130C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_130C)
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

    def lambda_136A():
        OP_96(0xFE, 0x2CEC, 0xFFFFE69C, 0xFFFF6A00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_136A)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x37)
    SetChrSubChip(0x15, 0x0)
    Sleep(300)

    #N0016
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        (
            "#6P呵呵……\x01",
            "一只穿着蓝衣的兔子。\x02",
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
        "戴墨镜的男人",
        (
            "哈哈……\x01",
            "这么轻松就上钩了啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0018
    NpcTalk(
        0x17,
        "戴墨镜的男人",
        (
            "#11P没时间了……\x01",
            "赶快下重手吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0019
    NpcTalk(
        0x17,
        "戴墨镜的男人",
        "#11P只是，注意不要重到杀了他啊。\x02",
    )

    CloseMessageWindow()

    #N0020
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        "#6P呵呵……不要恨我哦。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)

    def lambda_14B4():
        OP_96(0xFE, 0x3070, 0xFFFFE69C, 0xFFFF6B2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_14B4)
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
        "蓝衣青年",
        "#8A──怎会让你得逞！\x02",
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

    def lambda_1569():
        TurnDirection(0xFE, 0x15, 1000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1569)
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

    def lambda_15DE():
        OP_A6(0xFE, 0x0, 0x14, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15DE)

    def lambda_15F7():
        OP_A6(0xFE, 0x0, 0x14, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_15F7)
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

    def lambda_1703():
        OP_9C(0xFE, 0xFFFFE4A8, 0xFFFFE69C, 0xFFFFE4A8, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1703)
    SetChrChipByIndex(0x15, 0x3B)
    SetChrSubChip(0x15, 0x0)

    def lambda_1728():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1728)

    def lambda_1741():
        OP_9D(0xFE, 0x2B5C, 0xFFFFE69C, 0xFFFF68D4, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1741)
    WaitChrThread(0x15, 1)

    #N0022
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        "#6P什么……\x02",
    )

    CloseMessageWindow()

    #N0023
    NpcTalk(
        0x17,
        "戴墨镜的男人",
        "#11P什么……！？\x02",
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
        "蓝衣青年",
        "#11P……真是的。\x02",
    )

    CloseMessageWindow()

    #N0025
    NpcTalk(
        0xA,
        "蓝衣青年",
        (
            "#11P没想到能这么顺利地\x01",
            "把你们引出来啊。\x02",
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
        "戴墨镜的男人",
        "这、这家伙是……！？\x02",
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

    def lambda_18E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_18E5)

    def lambda_18F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18F6)
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
            "#0006F#11P本来是想将你们作为\x01",
            "现行犯当场逮捕的……\x02\x03",

            "#0001F但诱导取证并没有法律效力，\x01",
            "也只能先放你们一马了。\x02",
        )
    )

    CloseMessageWindow()

    #N0028
    NpcTalk(
        0x16,
        "戴墨镜的男人",
        "#6P这家伙，难道是……\x02",
    )

    CloseMessageWindow()

    #N0029
    NpcTalk(
        0x17,
        "戴墨镜的男人",
        "#11P警察吗……！？\x02",
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
        "少年的声音",
        (
            "#12P呵呵……\x01",
            "他只是个协助者而已。\x02",
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

    def lambda_1B27():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1B27)
    Sleep(50)

    def lambda_1B37():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_1B37)
    Sleep(50)

    def lambda_1B47():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1B47)
    Sleep(50)

    def lambda_1B57():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1B57)
    OP_6F(0x79)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)

    #C0031
    ChrTalk(
        0x104,
        (
            "#5P#0309F噢～噢～\x01",
            "他们还真上钩了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        "#5P#0202F……预测得相当准确呢。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#5P#0101F罗伊德，没事吧！？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#0004F#11P嗯……没受伤。\x02\x03",

            "#0000F幸好我为了保险，事先把防护垫\x01",
            "包在了头巾里。\x02",
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
        "戴墨镜的男人",
        "唔……\x02",
    )

    CloseMessageWindow()

    #N0036
    NpcTalk(
        0x18,
        "戴墨镜的男人",
        (
            "居然能察觉到\x01",
            "我们的存在……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#0400F#6P那么……\x01",
            "几位老兄，你们打算怎么办呢？\x02\x03",

            "#0404F如果在此老实投降，\x01",
            "我倒也可以既往不咎……\x02\x03",

            "#0402F──还是说，你们这次\x01",
            "想转换身份，尝尝当猎物的滋味呢？\x02",
        )
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        "#5P嘁……\x02",
    )

    CloseMessageWindow()

    #N0039
    NpcTalk(
        0x16,
        "戴墨镜的男人",
        "兵分两路！\x02",
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
        "#6P#0007F等、等一下……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 3)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)

    def lambda_1E3C():
        OP_9D(0xFE, 0x3DB8, 0xFFFFE69C, 0xFFFF6A00, 0x190, 0x9C4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E3C)
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
        "#0402F#5P──来两个人跟上我！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
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
            "#6P#0011F喂、喂──\x02\x03",

            "#0013F唔……！\x02",
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
        "#5P#0101F罗伊德，怎么办！？\x02",
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
            "【叫上艾莉】\x01",      # 0
            "【叫上缇欧】\x01",      # 1
            "【叫上兰迪】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1FFF"),
        (1, "loc_2078"),
        (2, "loc_20FD"),
        (SWITCH_DEFAULT, "loc_2176"),
    )


    label("loc_1FFF")

    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0045
    ChrTalk(
        0x101,
        (
            "#0007F#11P艾莉，拜托了！\x02\x03",

            "兰迪和缇欧\x01",
            "去追另外一组！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#5P#0101F明白了！\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        "#5P#0302F收到！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x45, 5)
    Jump("loc_2176")

    label("loc_2078")

    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0048
    ChrTalk(
        0x101,
        (
            "#0007F#11P缇欧，跟我来！\x02\x03",

            "艾莉，兰迪，\x01",
            "另一组就拜托你们了！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        "#5P#0201F了解……！\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        "#5P#0101F明白了！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x45, 6)
    Jump("loc_2176")

    label("loc_20FD")

    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0051
    ChrTalk(
        0x101,
        (
            "#0007F#11P兰迪，拜托了！\x02\x03",

            "艾莉和缇欧\x01",
            "去追另一组！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        "#5P#0302F收到！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        "#5P#0201F了解……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x45, 7)
    Jump("loc_2176")

    label("loc_2176")

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
        "戴墨镜的男人",
        (
            "#5P可恶，没想到胆小怕事的警察\x01",
            "居然会出动……\x02",
        )
    )

    CloseMessageWindow()

    #N0055
    NpcTalk(
        0x17,
        "戴墨镜的男人",
        (
            "#5P这样一来，\x01",
            "我们只能先回去请求支援──\x02",
        )
    )

    CloseMessageWindow()

    #N0056
    NpcTalk(
        0x18,
        "戴墨镜的男人",
        "#4P等、等等！\x02",
    )

    CloseMessageWindow()

    #N0057
    NpcTalk(
        0x18,
        "戴墨镜的男人",
        (
            "#4P我们表现得如此失败，\x01",
            "要是被副头目知道了……！\x02",
        )
    )

    CloseMessageWindow()

    #N0058
    NpcTalk(
        0x17,
        "戴墨镜的男人",
        "#5P呜……\x02",
    )

    CloseMessageWindow()

    #N0059
    NpcTalk(
        0x17,
        "戴墨镜的男人",
        (
            "#5P算了，总而言之，\x01",
            "我们至少也要先──\x02",
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
        "凶狠的声音",
        "……要去哪里啊？\x02",
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

    def lambda_259A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_259A)

    def lambda_25A7():
        OP_96(0xFE, 0x708, 0x0, 0x1964, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25A7)
    Sleep(1000)
    OP_68(1800, 1000, 0, 3000)
    MoveCamera(35, 25, 0, 3000)
    SetCameraDistance(21500, 3000)

    def lambda_25E9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_25E9)

    def lambda_25F6():
        OP_96(0xFE, 0xFFFFFCE0, 0x32, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_25F6)

    def lambda_2610():
        OP_96(0xFE, 0x1450, 0x32, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2610)

    def lambda_262A():
        OP_96(0xFE, 0x1388, 0x32, 0xFFFFF510, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_262A)
    Sleep(50)

    def lambda_2647():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2647)

    def lambda_2661():
        OP_96(0xFE, 0xFFFFF6A0, 0x0, 0xFFFFF5D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2661)
    Sleep(50)

    def lambda_267E():
        OP_96(0xFE, 0x12C, 0x0, 0xFFFFF0C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_267E)

    def lambda_2698():
        OP_96(0xFE, 0xA8C, 0x0, 0xFFFFF1F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2698)

    def lambda_26B2():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFEED0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_26B2)

    def lambda_26CC():
        OP_96(0xFE, 0x19C8, 0x0, 0xFFFFF574, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_26CC)
    Sleep(2000)

    #N0061
    NpcTalk(
        0x17,
        "戴墨镜的男人",
        "#6P什么……！？\x02",
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
        "戴墨镜的男人",
        "#5P什么时候出现的……！？\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_2882")
    SetChrPos(0x104, -9300, 0, -11500, 45)
    SetChrPos(0x103, -8700, 0, -12300, 45)

    def lambda_27EF():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_27EF)
    Sleep(50)

    def lambda_280C():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0xFFFFDBAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_280C)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x10)

    #C0063
    ChrTalk(
        0x103,
        "#12P#0204F已经包围起来了呢。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#6P#0300F是啊……\x01",
            "之后就看罗伊德那边的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A07")

    label("loc_2882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_2949")
    SetChrPos(0x104, -9300, 0, -11500, 45)
    SetChrPos(0x102, -8700, 0, -12300, 45)

    def lambda_28B2():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_28B2)
    Sleep(50)

    def lambda_28CF():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0xFFFFDBAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28CF)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x10)

    #C0065
    ChrTalk(
        0x104,
        "#6P#0300F这边已经彻底包围了呢。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#12P#0100F嗯……\x01",
            "接下来就看罗伊德他们的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A07")

    label("loc_2949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_2A07")
    SetChrPos(0x102, -9300, 0, -11500, 45)
    SetChrPos(0x103, -8700, 0, -12300, 45)

    def lambda_2979():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2979)
    Sleep(50)

    def lambda_2996():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0xFFFFDBAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2996)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x10)

    #C0067
    ChrTalk(
        0x103,
        "#12P#0204F已经包围起来了呢。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#6P#0100F嗯……\x01",
            "接下来就看罗伊德他们的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A07")

    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_2A2D")
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_2A4C")

    label("loc_2A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_2A3F")
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_2A4C")

    label("loc_2A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_2A4C")
    AddParty(0x3, 0xEF, 0xFF)

    label("loc_2A4C")

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

    def lambda_2B2E():
        OP_96(0xFE, 0x2580, 0xFFFFFF38, 0xFFFFC5CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2B2E)
    Sleep(50)

    def lambda_2B4B():
        OP_96(0xFE, 0x2968, 0xFFFFFF38, 0xFFFFC8EC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2B4B)
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
        "戴墨镜的男人",
        "#2P（嘁……中计了吗？）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x16, 500)

    #N0070
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        (
            "#6P（没办法了……\x01",
            "  抄小道走吧……！）\x02",
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
        "#0402F#2P呵呵，辛苦你们了呢。\x02",
    )

    CloseMessageWindow()

    #N0072
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        "#5P什、什么时候来的……！\x02",
    )

    CloseMessageWindow()

    #N0073
    NpcTalk(
        0x16,
        "戴墨镜的男人",
        "#1P可恶……下去！\x02",
    )

    CloseMessageWindow()
    OP_68(35000, -5500, -39000, 1500)
    MoveCamera(37, 19, 0, 1500)
    SetCameraDistance(18000, 1500)
    SetChrPos(0x101, 22600, -6500, -39300, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_2DA2")
    SetChrPos(0x102, 21700, -6500, -38700, 90)
    Jump("loc_2DDB")

    label("loc_2DA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_2DC1")
    SetChrPos(0x103, 21700, -6500, -38700, 90)
    Jump("loc_2DDB")

    label("loc_2DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_2DDB")
    SetChrPos(0x104, 21700, -6500, -38700, 90)

    label("loc_2DDB")

    BeginChrThread(0x16, 3, 0, 7)
    Sleep(150)
    OP_93(0x15, 0xB4, 0x2BC)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x4)
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2E03():
        OP_9D(0xFE, 0x8980, 0xFFFFE69C, 0xFFFF6AC8, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2E03)
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

    def lambda_2ED3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2ED3)

    def lambda_2EE0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2EE0)

    def lambda_2EED():
        OP_96(0xFE, 0x7788, 0xFFFFE69C, 0xFFFF667C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EED)
    Sleep(50)

    def lambda_2F0A():
        OP_96(0xFE, 0x7404, 0xFFFFE69C, 0xFFFF68D4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2F0A)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    #C0074
    ChrTalk(
        0x101,
        "#6P#0001F……到此为止了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_2F7E")

    #C0075
    ChrTalk(
        0x102,
        (
            "#6P#0103F呼……\x01",
            "一直在跑来跑去呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF5")

    label("loc_2F7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_2FBA")

    #C0076
    ChrTalk(
        0x103,
        (
            "#6P#0202F简直就像是\x01",
            "自投烈火的飞蛾呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF5")

    label("loc_2FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_2FF5")

    #C0077
    ChrTalk(
        0x104,
        (
            "#6P#0302F这些家伙简直\x01",
            "就是自投烈火的蛾子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF5")


    #N0078
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        "#11P唔……！\x02",
    )

    CloseMessageWindow()
    SetChrChip(0x0, 0x105, 0x1E, 0x12C)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x1)

    def lambda_3029():
        OP_9D(0xFE, 0x79E0, 0xFFFFE69C, 0xFFFF6E4C, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3029)
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
            "#0404F呵呵……\x01",
            "捉迷藏的游戏结束了哦。\x02\x03",

            "#0402F差不多也该举手投降了吧？\x02",
        )
    )

    CloseMessageWindow()

    #N0080
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        "#11P呵呵……\x02",
    )

    CloseMessageWindow()

    #N0081
    NpcTalk(
        0x16,
        "戴墨镜的男人",
        "哈哈哈……\x02",
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
        "戴墨镜的男人",
        (
            "一群小鬼……\x01",
            "竟敢如此得意忘形。\x02",
        )
    )

    CloseMessageWindow()

    #N0083
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        (
            "#11P非要逼我们这些\x01",
            "职业人士认真……\x02",
        )
    )

    CloseMessageWindow()

    #N0084
    NpcTalk(
        0x15,
        "戴墨镜的男人",
        "#11P一定会让你们后悔莫及的。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#6P#0013F哼……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_32A2")
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 80, 0)
    Jump("loc_32E1")

    label("loc_32A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_32C4")
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Jump("loc_32E1")

    label("loc_32C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_32E1")
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)

    label("loc_32E1")

    OP_0D()
    Sleep(300)

    #C0086
    ChrTalk(
        0x105,
        (
            "#0404F呵呵，看样子，\x01",
            "这一战似乎是无可避免了啊。\x02\x03",

            "#0402F我可以期待一下……\x01",
            "各位的支援吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#6P#0000F……那正是我要说的，\x01",
            "可别碍手碍脚啊！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_33A0")

    #C0088
    ChrTalk(
        0x102,
        "#6P#0107F……来了哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_33EB")

    label("loc_33A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_33C7")

    #C0089
    ChrTalk(
        0x103,
        "#6P#0207F……来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_33EB")

    label("loc_33C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_33EB")

    #C0090
    ChrTalk(
        0x104,
        "#6P#0307F来了啊……！\x02",
    )

    CloseMessageWindow()

    label("loc_33EB")

    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15500, 300)
    SetChrChipByIndex(0x15, 0x31)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x0)

    def lambda_341B():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_341B)

    def lambda_3435():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3435)
    Sleep(300)
    Battle("BattleInfo_65C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    Call(0, 18)
    Return()

    # Function_4_922 end

    def Function_5_3473(): pass

    label("Function_5_3473")

    ClearChrFlags(0x15, 0x4)
    OP_92(0xFE, 0x46B4, 0xFFFFA81C, 0x2BC)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)

    def lambda_3492():
        OP_95(0xFE, 18100, -2500, -22500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3492)
    WaitChrThread(0xFE, 1)

    def lambda_34B0():
        OP_95(0xFE, 22000, -2500, -22500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34B0)
    WaitChrThread(0xFE, 1)

    def lambda_34CE():
        OP_95(0xFE, 22000, -3500, -28200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34CE)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_34FF():
        OP_9D(0xFE, 0x55F0, 0xFFFFFDA8, 0xFFFF7F7C, 0xCE4, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34FF)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 0x3D)
    SetChrSubChip(0x15, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)

    def lambda_3544():
        OP_95(0xFE, 25200, -300, -32500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3544)
    WaitChrThread(0xFE, 1)

    def lambda_3562():
        OP_95(0xFE, 36500, -800, -34200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3562)
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

    # Function_5_3473 end

    def Function_6_35FF(): pass

    label("Function_6_35FF")

    ClearChrFlags(0x16, 0x4)
    OP_92(0xFE, 0x46B4, 0xFFFFA81C, 0x2BC)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)

    def lambda_361E():
        OP_95(0xFE, 18100, -2500, -22500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_361E)
    WaitChrThread(0xFE, 1)

    def lambda_363C():
        OP_95(0xFE, 22000, -2500, -22500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_363C)
    WaitChrThread(0xFE, 1)

    def lambda_365A():
        OP_95(0xFE, 22000, -3500, -28200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_365A)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_368B():
        OP_9D(0xFE, 0x55F0, 0xFFFFFDA8, 0xFFFF7F7C, 0xCE4, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_368B)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x16, 0x3D)
    SetChrSubChip(0x16, 0x1)
    Sleep(50)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)

    def lambda_36D0():
        OP_95(0xFE, 25200, -300, -32500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36D0)
    WaitChrThread(0xFE, 1)

    def lambda_36EE():
        OP_95(0xFE, 35100, -800, -34200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36EE)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Return()

    # Function_6_35FF end

    def Function_7_372B(): pass

    label("Function_7_372B")

    OP_93(0x16, 0xB4, 0x2BC)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x4)
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_374A():
        OP_9D(0xFE, 0x87F0, 0xFFFFE69C, 0xFFFF6424, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_374A)
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

    # Function_7_372B end

    def Function_8_37C8(): pass

    label("Function_8_37C8")

    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)

    def lambda_37D5():
        OP_95(0xFE, -12000, 0, -12000, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37D5)
    WaitChrThread(0xFE, 1)

    def lambda_37F3():
        OP_95(0xFE, 1800, 0, -5500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37F3)
    WaitChrThread(0xFE, 1)

    def lambda_3811():
        OP_95(0xFE, 1800, 0, 3000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3811)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    Return()

    # Function_8_37C8 end

    def Function_9_3833(): pass

    label("Function_9_3833")

    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)

    def lambda_3840():
        OP_95(0xFE, -12000, 0, -12000, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3840)
    WaitChrThread(0xFE, 1)

    def lambda_385E():
        OP_95(0xFE, 1800, 0, -5500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_385E)
    WaitChrThread(0xFE, 1)

    def lambda_387C():
        OP_95(0xFE, 1800, 0, 1500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_387C)
    WaitChrThread(0x18, 1)
    SetChrChipByIndex(0x18, 0x32)
    SetChrSubChip(0x18, 0x0)
    Return()

    # Function_9_3833 end

    def Function_10_389E(): pass

    label("Function_10_389E")


    def lambda_38A3():
        OP_95(0xFE, 20900, -6500, -37000, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_38A3)
    WaitChrThread(0x8, 1)

    def lambda_38C1():
        OP_95(0xFE, 20900, -5500, -33000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_38C1)
    WaitChrThread(0x8, 1)
    Return()

    # Function_10_389E end

    def Function_11_38DB(): pass

    label("Function_11_38DB")


    def lambda_38E0():
        OP_95(0xFE, 7200, -6500, -36300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38E0)
    WaitChrThread(0xFE, 1)

    def lambda_38FE():
        OP_95(0xFE, 2200, -4750, -32900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38FE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_38DB end

    def Function_12_3918(): pass

    label("Function_12_3918")


    def lambda_391D():
        OP_95(0xFE, 21500, -6500, -36500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_391D)
    WaitChrThread(0xFE, 1)

    def lambda_393B():
        OP_95(0xFE, 21500, -4550, -30500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_393B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_3918 end

    def Function_13_3955(): pass

    label("Function_13_3955")

    OP_A1(0xFE, 0x7D0, 0x8, 0x7, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6)
    Sleep(50)
    SetChrSubChip(0xFE, 0x7)
    Return()

    # Function_13_3955 end

    def Function_14_396B(): pass

    label("Function_14_396B")

    ClearChrFlags(0xFE, 0x8)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0x16, 6000, -5100, -37200, 135)

    def lambda_398B():
        OP_95(0xFE, 11100, -6450, -37200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_398B)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0x87, 0x1F4)
    Return()

    # Function_14_396B end

    def Function_15_39AC(): pass

    label("Function_15_39AC")

    ClearChrFlags(0xFE, 0x8)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0x17, 21000, -5750, -33500, 180)

    def lambda_39CC():
        OP_95(0xFE, 21000, -6500, -37000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_39CC)
    WaitChrThread(0x17, 1)

    def lambda_39EA():
        OP_95(0xFE, 16300, -6500, -37800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_39EA)
    WaitChrThread(0x17, 1)
    Return()

    # Function_15_39AC end

    def Function_16_3A04(): pass

    label("Function_16_3A04")

    ClearChrFlags(0xFE, 0x8)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0x18, 21000, -5750, -33500, 180)

    def lambda_3A24():
        OP_95(0xFE, 21000, -6500, -37000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3A24)
    WaitChrThread(0x18, 1)

    def lambda_3A42():
        OP_95(0xFE, 16300, -6500, -39500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3A42)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x13B, 0x1F4)
    Return()

    # Function_16_3A04 end

    def Function_17_3A63(): pass

    label("Function_17_3A63")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A81")
    OP_A1(0xFE, 0xFA0, 0x8, 0x1, 0x0, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2)
    Jump("Function_17_3A63")

    label("loc_3A81")

    Return()

    # Function_17_3A63 end

    def Function_18_3A82(): pass

    label("Function_18_3A82")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_3B77")
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_3B9E")

    label("loc_3B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_3B8D")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_3B9E")

    label("loc_3B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3B9E")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_3B9E")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_3C8E")
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 29700, -6500, -38700, 90)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    Jump("loc_3CEB")

    label("loc_3C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_3CBF")
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 29700, -6500, -38700, 90)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x104, 0x8)
    Jump("loc_3CEB")

    label("loc_3CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3CEB")
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 29700, -6500, -38700, 90)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x102, 0x8)

    label("loc_3CEB")

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

    def lambda_3DBD():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3DBD)
    WaitChrThread(0x15, 2)

    #C0091
    ChrTalk(
        0x15,
        "#11P#50W唔……\x02",
    )

    CloseMessageWindow()

    def lambda_3DEE():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_3DEE)
    WaitChrThread(0x16, 2)

    #C0092
    ChrTalk(
        0x16,
        "#50W……可恶的小鬼们……\x02",
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
            "#6P#0006F呼……\x01",
            "的确挺棘手的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_3F18")

    #C0094
    ChrTalk(
        0x102,
        (
            "#3P#0101F他们使用的枪似乎也是\x01",
            "最新型的军用手枪呢。\x02\x03",

            "好像是帝国制造的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FC1")

    label("loc_3F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_3F72")

    #C0095
    ChrTalk(
        0x103,
        (
            "#3P#0201F……他们用的枪也是\x01",
            "帝国制造的军用手枪呢。\x02\x03",

            "而且还是最新型的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FC1")

    label("loc_3F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3FC1")

    #C0096
    ChrTalk(
        0x104,
        (
            "#3P#0301F竟然用上最新型的\x01",
            "军用手枪了啊……\x02\x03",

            "多半是帝国制造的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FC1")


    #C0097
    ChrTalk(
        0x8,
        (
            "#0404F这就是他们在地下交易中\x01",
            "所经手的武器之一吧？\x02",
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
            "#5P#0402F呵呵，话说回来，\x01",
            "你的演技可真是不错啊。\x02\x03",

            "那种倒地的方式……\x01",
            "简直都能以假乱真了吧？\x02",
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

    def lambda_40BC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_40BC)
    Sleep(100)
    OP_93(0xEF, 0x5A, 0x1F4)

    #C0099
    ChrTalk(
        0x101,
        (
            "#12P#0003F……既然你都告诉我要进行那种作战了，\x01",
            "我也就只有全力以赴呢。\x02\x03",

            "#0001F诱饵这种任务，又不能\x01",
            "交给其他人来做。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_41E3")
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0100
    ChrTalk(
        0x102,
        (
            "#5P#0106F唉，所以你才提出由自己来扮演\x01",
            "诱饵这个危险的角色啊……\x02\x03",

            "#0101F我们也担心得要命呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0101
    ChrTalk(
        0x101,
        "#12P#0006F抱、抱歉了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4323")

    label("loc_41E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_427E")
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0102
    ChrTalk(
        0x103,
        (
            "#5P#0206F不过，竟然因此自愿接下扮演诱饵\x01",
            "那么危险的任务……\x02\x03",

            "#0211F未免也太过老好人了吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0103
    ChrTalk(
        0x101,
        "#12P#0005F是、是吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4323")

    label("loc_427E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_4323")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0104
    ChrTalk(
        0x104,
        (
            "#5P#0304F哈，所以你才自愿揽下\x01",
            "这么危险的差事啊。\x02\x03",

            "#0302F该说你是老好人型呢，\x01",
            "还是那种易遭利用型呢～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0105
    ChrTalk(
        0x101,
        "#12P#0001F真是让你见笑了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4323")


    #C0106
    ChrTalk(
        0x8,
        (
            "#5P#0402F呵呵，这种老好人的性格，\x01",
            "会让你以后十分辛苦哦。\x02\x03",

            "#0409F不过呢，我个人倒是\x01",
            "并不讨厌这种类型呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4395():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4395)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_43BB")

    def lambda_43AE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_43AE)
    Jump("loc_43EC")

    label("loc_43BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_43D6")

    def lambda_43C9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_43C9)
    Jump("loc_43EC")

    label("loc_43D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_43EC")

    def lambda_43E4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_43E4)

    label("loc_43EC")

    Sleep(300)

    #C0107
    ChrTalk(
        0x101,
        "#12P#0011F哎？\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "#5P#0404F呵呵……\x02\x03",

            "#0402F总之，这样一来，\x01",
            "我们就算报了一箭之仇了。\x02\x03",

            "非常感谢你们的协助啊。\x02",
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
            "#11P#30W你们这群小鬼……\x01",
            "……越来越得意忘形……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x17,
        (
            "#5P#30W呵呵……\x01",
            "你们死定了，小鬼们。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x17,
        (
            "#5P#30W居然敢把我们『鲁巴彻』\x01",
            "彻底惹火……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x15,
        "#6P#30W几个警察小鬼也是一样……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x15,
        (
            "#6P#30W我们可是有位高权重的议员先生当后台，\x01",
            "你们以为自己会被轻易放过吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#12P#0001F……这些家伙………\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        "#1604F#4P哼哼哼……\x02",
    )

    CloseMessageWindow()
    MoveCamera(33, 25, 0, 700)
    SetCameraDistance(18500, 700)

    def lambda_4899():
        OP_96(0xFE, 0xC80, 0x0, 0xD48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4899)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x17, 0x31)
    SetChrSubChip(0x17, 0x0)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x20)

    def lambda_48D4():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_48D4)

    def lambda_48ED():
        OP_98(0xFE, 0xC8, 0x1C2, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_48ED)
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
        "#40W呜……？\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "#4P#1602F看来你们这些混蛋\x01",
            "还没受够教训啊……？\x02\x03",

            "那我就把你们全都当成沙袋吊起来，\x01",
            "然后砍成血肉模糊的人棍如何啊……？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x17,
        "#40W唔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    #C0119
    ChrTalk(
        0x101,
        (
            "#6P#0007F等一下！\x01",
            "再怎么说也不能……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0120
    ChrTalk(
        0x8,
        (
            "#0400F好啦好啦，\x01",
            "这里就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    def lambda_4A2A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A2A)
    Sleep(300)

    #C0121
    ChrTalk(
        0x8,
        (
            "#6P#0403F──瓦鲁多，\x01",
            "干得太过火也不好啊。\x02\x03",

            "#0400F这些老兄可都是职业的。\x02\x03",

            "你要是让他们彻底尊严扫地，\x01",
            "未免也太不给人家面子了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        "#4P#1603F嘁……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 0x37)
    SetChrSubChip(0x9, 0x0)

    def lambda_4ADC():
        OP_9D(0xFE, 0x6A4, 0x0, 0xDAC, 0x32, 0xFA0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4ADC)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x30)
    SetChrSubChip(0x17, 0x3)

    def lambda_4B0B():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_4B0B)
    Sound(819, 0, 100, 0)
    WaitChrThread(0x17, 2)
    ClearChrFlags(0x17, 0x4)
    ClearChrFlags(0x17, 0x20)

    #C0123
    ChrTalk(
        0x17,
        "#50W咳、咳……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(37, 25, 0, 700)
    SetCameraDistance(19500, 700)
    Fade(250)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)

    def lambda_4B70():
        OP_96(0xFE, 0x1068, 0x0, 0xAF0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4B70)
    WaitChrThread(0x9, 1)
    OP_6F(0x50)
    Sleep(300)

    #C0124
    ChrTalk(
        0x8,
        (
            "#3P#0404F呵呵，话说回来，几位老兄也\x01",
            "不想把事情张扬出去吧？\x02\x03",

            "#0402F身为职业人士，和我们\x01",
            "几个小辈如此认真地动手，\x01",
            "却还被打得落花流水……\x02\x03",

            "#0409F……这种颜面扫地的事情\x01",
            "也没法向上面报告吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x18,
        "#11P唔……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x16,
        (
            "#6P……开什么玩笑……\x01",
            "我们要是认真起来，你们就算再来几个人也……\x02",
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
        "女性的声音",
        (
            "#4P哎呀～你们现在还是\x01",
            "快些退场比较好吧？\x02",
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

    def lambda_4ED0():

        label("loc_4ED0")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_4ED0")

    QueueWorkItem2(0x8, 2, lambda_4ED0)

    def lambda_4EE2():

        label("loc_4EE2")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_4EE2")

    QueueWorkItem2(0xB, 2, lambda_4EE2)

    def lambda_4EF4():

        label("loc_4EF4")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_4EF4")

    QueueWorkItem2(0xD, 2, lambda_4EF4)

    def lambda_4F06():

        label("loc_4F06")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_4F06")

    QueueWorkItem2(0xE, 2, lambda_4F06)

    def lambda_4F18():

        label("loc_4F18")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_4F18")

    QueueWorkItem2(0xF, 2, lambda_4F18)

    def lambda_4F2A():

        label("loc_4F2A")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_4F2A")

    QueueWorkItem2(0x9, 2, lambda_4F2A)

    def lambda_4F3C():

        label("loc_4F3C")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_4F3C")

    QueueWorkItem2(0x11, 2, lambda_4F3C)

    def lambda_4F4E():

        label("loc_4F4E")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_4F4E")

    QueueWorkItem2(0x12, 2, lambda_4F4E)

    def lambda_4F60():

        label("loc_4F60")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_4F60")

    QueueWorkItem2(0x13, 2, lambda_4F60)

    def lambda_4F72():

        label("loc_4F72")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_4F72")

    QueueWorkItem2(0x14, 2, lambda_4F72)

    def lambda_4F84():

        label("loc_4F84")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_4F84")

    QueueWorkItem2(0x10, 2, lambda_4F84)
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

    def lambda_5045():
        OP_95(0xFE, 1800, 0, 6000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5045)
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
        "#0011F格蕾丝小姐……！？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        "#0105F您为什么会在这里……\x02",
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
            "呵呵，其实我这几天一直\x01",
            "都在注意你们的动向哦。\x02\x03",

            "然后，就如我所料，\x01",
            "你们果然能给我提供很多素材啊！\x02\x03",

            "呀～看来可以写篇\x01",
            "很有趣的报道了哦¤\x02",
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
        "#12P你、你……！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x16,
        (
            "#4P区区一个杂志社，\x01",
            "竟敢公然与『鲁巴彻』作对……！\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        (
            "#5P#2106F话说回来，我们这边的情况也很复杂啦，\x01",
            "所以大概也没法把你们的名字公布出来。\x02\x03",

            "#2100F但是，如果你们再做出\x01",
            "一些见不得人的事情，\x01",
            "结果如何，我可就无法保证了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x16,
        "#4P唔……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x17,
        (
            "#2P……好吧，\x01",
            "我们就先撤退……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x17,
        "#2P但是，如果你敢违背约定……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xC,
        (
            "#5P#2104F好好，我知道啦。\x02\x03",

            "#2101F倒是你们，可一定\x01",
            "要好好遵守从此\x01",
            "罢手的约定。\x02\x03",

            "如果越过界线一步，\x01",
            "也许就轮到游击士出动了哦。\x02",
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
        "#2P什么……！\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        "#0005F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xC,
        (
            "#5P#2103F其实，亚里欧斯先生\x01",
            "都已经准备介入这件事了。\x02\x03",

            "#2100F不过由于他实在太忙，\x01",
            "而且你们又抢先一步介入，\x01",
            "所以他这次就让给你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#0011F怎、怎么会……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        "#0306F到头来，一切都还是在他的掌控之中吗？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        "#0211F……似乎是这样呢。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x15,
        "#6P说、说什么蠢话……！\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x15,
        (
            "#6P要是早知道亚里欧斯·马克莱因会插手的话，\x01",
            "我们又怎会把事情做得如此草率！\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x18,
        (
            "#5P……我们没必要再待在\x01",
            "这种肮脏破旧的地方了……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x18,
        "#5P撤退……！\x02",
    )

    CloseMessageWindow()
    Fade(250)

    def lambda_5662():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_5662)
    SetChrChipByIndex(0x18, 0x31)
    SetChrSubChip(0x18, 0x0)
    Sleep(350)

    def lambda_5686():

        label("loc_5686")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_5686")

    QueueWorkItem2(0xC, 2, lambda_5686)

    def lambda_5698():
        OP_96(0xFE, 0x9C4, 0x0, 0x189C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5698)
    SetChrChipByIndex(0x18, 0x32)
    SetChrSubChip(0x18, 0x0)
    BeginChrThread(0x18, 3, 0, 21)
    Fade(250)

    def lambda_56C5():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_56C5)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    Sleep(350)
    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 3, 0, 21)
    Fade(250)

    def lambda_56FC():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_56FC)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    Sleep(350)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)
    BeginChrThread(0x15, 3, 0, 21)
    Fade(250)

    def lambda_5733():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_5733)
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

    def lambda_57C5():
        OP_95(0xFE, 1800, 0, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_57C5)
    WaitChrThread(0xC, 1)

    def lambda_57E3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_57E3)
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
            "#3P#0406F哎呀呀……\x01",
            "『风之剑圣』亚里欧斯吗？\x02\x03",

            "#0400F虽然听过关于他的传闻，\x01",
            "但没想到竟然会有如此强大的震慑效果呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        "#1601F嘁……听了就让人讨厌的家伙。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x1F4)
    Sleep(300)

    #C0150
    ChrTalk(
        0x9,
        (
            "#6P#1604F算啦……\x01",
            "这次的事情就到此结束！\x02\x03",

            "#1602F你们几个，撤退了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_592A():

        label("loc_592A")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_592A")

    QueueWorkItem2(0x101, 2, lambda_592A)

    def lambda_593C():

        label("loc_593C")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_593C")

    QueueWorkItem2(0x102, 2, lambda_593C)

    def lambda_594E():

        label("loc_594E")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_594E")

    QueueWorkItem2(0x103, 2, lambda_594E)

    def lambda_5960():

        label("loc_5960")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5960")

    QueueWorkItem2(0x104, 2, lambda_5960)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(400, 10, -1, -1)
    SetChrName("剑蛇帮众成员")

    #A0151
    AnonymousTalk(
        0xFF,
        "#4S收到！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_59B8():

        label("loc_59B8")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_59B8")

    QueueWorkItem2(0x8, 2, lambda_59B8)

    def lambda_59CA():

        label("loc_59CA")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_59CA")

    QueueWorkItem2(0xB, 2, lambda_59CA)

    def lambda_59DC():

        label("loc_59DC")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_59DC")

    QueueWorkItem2(0xD, 2, lambda_59DC)

    def lambda_59EE():

        label("loc_59EE")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_59EE")

    QueueWorkItem2(0xE, 2, lambda_59EE)

    def lambda_5A00():

        label("loc_5A00")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5A00")

    QueueWorkItem2(0xF, 2, lambda_5A00)

    def lambda_5A12():

        label("loc_5A12")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5A12")

    QueueWorkItem2(0x11, 2, lambda_5A12)

    def lambda_5A24():

        label("loc_5A24")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5A24")

    QueueWorkItem2(0x12, 2, lambda_5A24)

    def lambda_5A36():

        label("loc_5A36")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5A36")

    QueueWorkItem2(0x13, 2, lambda_5A36)

    def lambda_5A48():

        label("loc_5A48")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5A48")

    QueueWorkItem2(0x14, 2, lambda_5A48)

    def lambda_5A5A():

        label("loc_5A5A")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5A5A")

    QueueWorkItem2(0x10, 2, lambda_5A5A)

    def lambda_5A6C():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5A6C)
    Sleep(500)

    def lambda_5A89():
        OP_96(0xFE, 0xFA0, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5A89)
    Sleep(800)
    BeginChrThread(0x11, 3, 0, 19)
    WaitChrThread(0x12, 1)
    Sleep(1500)
    EndChrThread(0x12, 0x2)

    def lambda_5AB7():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5AB7)
    Sleep(100)
    BeginChrThread(0x13, 3, 0, 19)
    Sleep(1000)
    EndChrThread(0x14, 0x2)

    def lambda_5AE1():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5AE1)
    Sleep(600)
    EndChrThread(0x10, 0x2)

    def lambda_5B02():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5B02)
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

    def lambda_5B88():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5B88)
    Sleep(150)

    def lambda_5B98():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5B98)
    Sleep(50)

    def lambda_5BA8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_5BA8)

    def lambda_5BB5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_5BB5)
    TurnDirection(0xF, 0x101, 500)

    #C0152
    ChrTalk(
        0x8,
        (
            "#5P#0404F呵呵……\x01",
            "你们也辛苦啦。\x02\x03",

            "#0400F这样就算是顺利完成任务了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C13():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C13)
    Sleep(50)

    def lambda_5C23():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5C23)
    Sleep(50)

    def lambda_5C33():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5C33)
    Sleep(50)

    def lambda_5C43():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5C43)
    Sleep(300)

    #C0153
    ChrTalk(
        0x101,
        (
            "#0005F#11P嗯……是啊。\x02\x03",

            "#0004F我们的任务原本是\x01",
            "阻止你们斗殴……\x02\x03",

            "#0000F算啦，反正你们以后\x01",
            "应该也不用再互相争斗了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        "#5P#0405F哎，你在说什么啊？\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#0011F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "#5P……无论有没有\x01",
            "黑手党从中作梗，\x01",
            "我们和剑蛇帮的关系都不会产生任何变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "#5P因为我们一直都会视对方为眼中钉，\x01",
            "这点是不会改变的。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x8,
        (
            "#5P#0404F全员出动的生死大战\x01",
            "确实应该是不会发生了……\x02\x03",

            "#0402F不过，普通的争斗和冲突\x01",
            "大概会一直持续下去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#0001F#11P等、等一下……！\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "#5P#0402F呵呵，如果你们不希望事态变得严重，\x01",
            "到时也可以再次介入啊，如何？\x02\x03",

            "如果有兴趣，\x01",
            "直接参战也可以哦。\x02\x03",

            "#0409F如果对手是你们，我们非常欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        "#0006F#11P我、我说啊……\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        (
            "#0106F听起来似乎并不像\x01",
            "是在开玩笑呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "#5P#0404F呵呵……\x01",
            "那么，祝你们做个好梦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(200)

    #C0164
    ChrTalk(
        0x8,
        "#5P#0402F──回去吧。\x02",
    )

    CloseMessageWindow()

    def lambda_5F51():

        label("loc_5F51")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5F51")

    QueueWorkItem2(0xD, 2, lambda_5F51)

    def lambda_5F63():

        label("loc_5F63")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5F63")

    QueueWorkItem2(0xE, 2, lambda_5F63)

    def lambda_5F75():

        label("loc_5F75")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5F75")

    QueueWorkItem2(0xF, 2, lambda_5F75)
    OP_93(0xB, 0xE1, 0x1F4)
    Sleep(300)

    #C0165
    ChrTalk(
        0xB,
        "#5P圣战结束──撤退。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(50, 170, -1, -1)
    SetChrName("圣书会众成员")

    #A0166
    AnonymousTalk(
        0xFF,
        "#4S了解！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_5FF0():

        label("loc_5FF0")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5FF0")

    QueueWorkItem2(0x101, 2, lambda_5FF0)

    def lambda_6002():

        label("loc_6002")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6002")

    QueueWorkItem2(0x102, 2, lambda_6002)

    def lambda_6014():

        label("loc_6014")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6014")

    QueueWorkItem2(0x103, 2, lambda_6014)

    def lambda_6026():

        label("loc_6026")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6026")

    QueueWorkItem2(0x104, 2, lambda_6026)

    def lambda_6038():

        label("loc_6038")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6038")

    QueueWorkItem2(0xC, 2, lambda_6038)

    def lambda_604A():
        OP_95(0xFE, -4200, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_604A)
    Sleep(500)

    def lambda_6067():
        OP_96(0xFE, 0xFFFFFE70, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6067)
    Sleep(800)
    BeginChrThread(0xB, 3, 0, 20)
    WaitChrThread(0xD, 1)
    Sleep(1500)
    EndChrThread(0xD, 0x2)

    def lambda_6095():
        OP_95(0xFE, -4200, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6095)
    Sleep(100)
    EndChrThread(0xC, 0x2)

    def lambda_60B6():
        OP_95(0xFE, 1800, 0, 1000, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_60B6)
    BeginChrThread(0xE, 3, 0, 20)
    Sleep(1000)
    EndChrThread(0xF, 0x2)

    def lambda_60DD():
        OP_95(0xFE, -4200, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_60DD)
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
        "#5P#0203F……真是一群不知悔改的人啊。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        (
            "#0300F#11P算啦，都是些血气方刚的家伙，\x01",
            "偶尔打打架也是没办法的。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        (
            "#5P#0106F呼……看来是这样呢。\x02\x03",

            "#0100F不过，能顺利解决此次事件，\x01",
            "不是已经很好了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0171
    ChrTalk(
        0x102,
        "#11P#0102F是吧，罗伊德？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0172
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯……是啊。\x02\x03",

            "#0008F但还是觉得……\x01",
            "有些无法释怀呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    #C0173
    ChrTalk(
        0xC,
        (
            "#2104F呵呵，因为不是完全靠自己的力量\x01",
            "解决的，所以有些不舒服……\x02\x03",

            "#2100F大概就是那种心情吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1800, 1000, -100, 1000)

    def lambda_6376():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6376)
    Sleep(100)

    def lambda_6386():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6386)

    def lambda_6393():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6393)

    def lambda_63A0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_63A0)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    #C0174
    ChrTalk(
        0x101,
        "#12P#0005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xC,
        (
            "#5P#2101F小心眼，太小心眼啦。\x02\x03",

            "#2103F在必要的时候，\x01",
            "就要毫不犹豫地借助他人的力量，\x01",
            "从而进一步探明真相……\x02\x03",

            "只有做到这一点，\x01",
            "才算是一名真正合格的搜查官哦。\x02\x03",

            "#2102F──就像你的哥哥一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0176
    ChrTalk(
        0x101,
        "#12P#0005F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xC,
        (
            "#2104F#5P呵呵，那么……\x01",
            "姐姐我也该撤退啦。\x02\x03",

            "#2110F差不多也到了需要\x01",
            "注意保养皮肤的年纪了呢～\x02\x03",

            "#2109F那么，晚安啦～¤\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x1F4)

    def lambda_6548():
        OP_95(0xFE, 1600, 0, 15000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6548)
    Sleep(2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)
    OP_68(2600, 1000, -1250, 1200)

    def lambda_6591():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6591)
    Sleep(50)

    def lambda_65A1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_65A1)
    Sleep(50)

    def lambda_65B1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_65B1)
    WaitChrThread(0x103, 2)
    OP_6F(0x1)

    #C0178
    ChrTalk(
        0x104,
        (
            "#0300F你的大哥……\x01",
            "似乎相当有名气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x102,
        (
            "#11P#0100F不管怎么说，\x01",
            "反正是个非常优秀的人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#5P#0002F……哈哈。\x02\x03",

            "#0004F如果单说执著程度与行动力，\x01",
            "确实算得上超一流呢。\x02",
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
            "#5P#0003F──任务完成。\x02\x03",

            "#0000F我们这就返回支援科，\x01",
            "向赛尔盖科长报告吧。\x02",
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

    # Function_18_3A82 end

    def Function_19_6726(): pass

    label("Function_19_6726")

    EndChrThread(0xFE, 0x2)

    def lambda_672F():
        OP_95(0xFE, 5100, 0, 400, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_672F)
    WaitChrThread(0xFE, 1)

    def lambda_674D():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_674D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_6726 end

    def Function_20_6767(): pass

    label("Function_20_6767")

    EndChrThread(0xFE, 0x2)

    def lambda_6770():
        OP_95(0xFE, -1500, 0, 400, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6770)
    WaitChrThread(0xFE, 1)

    def lambda_678E():
        OP_95(0xFE, -4200, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_678E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_6767 end

    def Function_21_67A8(): pass

    label("Function_21_67A8")


    def lambda_67AD():
        OP_95(0xFE, 800, 0, 5000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_67AD)
    WaitChrThread(0xFE, 1)

    def lambda_67CB():
        OP_95(0xFE, 800, 0, 25000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_67CB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_67A8 end

    SaveToFile()

Try(main)
