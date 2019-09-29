from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c020b.bin",                # FileName
        "c020b",                    # MapName
        "c020b",                    # Location
        0x000A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 10, 0, 0, 0, 1],
    )

    BuildStringList((
        "c020b",                  # 0
        "赛尔盖科长",             # 1
        "蔡特",                   # 2
        "奥斯卡",                 # 3
        "哈罗德",                 # 4
        "伊安律师",               # 5
        "塔利兹",                 # 6
        "小桃",                   # 7
        "警备队员",               # 8
        "警备队员",               # 9
        "警备队员",               # 10
        "警备队员",               # 11
        "警备队员",               # 12
        "警备队员",               # 13
        "警备队员",               # 14
        "车１",                   # 15
        "车２",                   # 16
        "SE控制",                 # 17
        "中央广场",               # 18
        "西街",                   # 19
        "行政区",                 # 20
        "住宅街",                 # 21
        "欢乐街",                 # 22
        "东街",                   # 23
        "旧城区",                 # 24
        "港湾区",                 # 25
        "ＩＢＣ",                 # 26
        "站前街道",               # 27
        "后巷",                   # 28
        "乌尔斯拉间道",           # 29
        "东克洛斯贝尔街道",       # 30
        "西克洛斯贝尔街道",       # 31
        "玛因兹山道",             # 32
    ))

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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(14410,   -6500,   -13590,  1200,    14410,   -5500,   -13590,  0x007C, 0,  2,  0x0000)
    DeclActor(-32070,  -1000,   11050,   1200,    -32070,  0,       11050,   0x007C, 0,  3,  0x0000)

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "中央广场")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "西街")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "行政区")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "住宅街")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "欢乐街")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "东街")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "旧城区")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "港湾区")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "站前街道")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "后巷")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(48.75, 0.0, -21.0, 0x0000, 0x0051, "")
    PlaceName(102.5, 0.0, 5.0, 0x0000, 0x0054, "")
    PlaceName(73.25, 0.0, -29.0, 0x0000, 0x0057, "")
    PlaceName(48.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(68.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(17.75, 0.0, 3.0, 0x0000, 0x0053, "")
    PlaceName(8.0, 0.0, 24.0, 0x0000, 0x0053, "")
    PlaceName(32.0, 0.0, 56.0, 0x0000, 0x0052, "")
    PlaceName(36.75, 0.0, 43.0, 0x0000, 0x0053, "")
    PlaceName(45.5, 0.0, 34.5, 0x0000, 0x0053, "")
    PlaceName(74.0, 0.0, 105.5, 0x0000, 0x0051, "")
    PlaceName(186.0, 0.0, -30.0, 0x0000, 0x0052, "")
    PlaceName(169.0, 0.0, -120.5, 0x0000, 0x0053, "")
    PlaceName(156.0, 0.0, -102.0, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_5E0",          # 00, 0
        "Function_1_5F0",          # 01, 1
        "Function_2_61F",          # 02, 2
        "Function_3_774",          # 03, 3
        "Function_4_8AA",          # 04, 4
        "Function_5_1708",         # 05, 5
        "Function_6_1D79",         # 06, 6
        "Function_7_1E99",         # 07, 7
        "Function_8_1EC2",         # 08, 8
        "Function_9_1EE8",         # 09, 9
        "Function_10_200A",        # 0A, 10
        "Function_11_205E",        # 0B, 11
        "Function_12_2214",        # 0C, 12
        "Function_13_23BF",        # 0D, 13
        "Function_14_25A0",        # 0E, 14
        "Function_15_266D",        # 0F, 15
        "Function_16_271B",        # 10, 16
        "Function_17_27C9",        # 11, 17
        "Function_18_2877",        # 12, 18
        "Function_19_2925",        # 13, 19
        "Function_20_29C5",        # 14, 20
        "Function_21_2B1C",        # 15, 21
        "Function_22_2B8F",        # 16, 22
        "Function_23_2C08",        # 17, 23
        "Function_24_2C81",        # 18, 24
        "Function_25_2CF4",        # 19, 25
        "Function_26_2D0E",        # 1A, 26
    ))


    def Function_0_5E0(): pass

    label("Function_0_5E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_5EF")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)

    label("loc_5EF")

    Return()

    # Function_0_5E0 end

    def Function_1_5F0(): pass

    label("Function_1_5F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_603")
    OP_70(0x7, 0x0)
    Jump("loc_607")

    label("loc_603")

    OP_70(0x7, 0x1E)

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61A")
    OP_70(0x8, 0x0)
    Jump("loc_61E")

    label("loc_61A")

    OP_70(0x8, 0x1E)

    label("loc_61E")

    Return()

    # Function_1_5F0 end

    def Function_2_61F(): pass

    label("Function_2_61F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_745")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x7, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×８０\x01\x07\x02",

            "#57I水之耀晶片×８０\x01\x07\x02",

            "#58I火之耀晶片×８０\x01\x07\x02",

            "#59I风之耀晶片×８０\x01\x07\x02",

            "#60I时之耀晶片×８０\x01\x07\x02",

            "#61I空之耀晶片×８０\x01\x07\x02",

            "#62I幻之耀晶片×８０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x110, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_762")

    label("loc_745")


    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_762")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_61F end

    def Function_3_774(): pass

    label("Function_3_774")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_861")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA7, 1)"), scpexpr(EXPR_END)), "loc_7F3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_85C")

    label("loc_7F3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_85C")

    Jump("loc_89E")

    label("loc_861")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
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

    label("loc_89E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_774 end

    def Function_4_8AA(): pass

    label("Function_4_8AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50506.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("chr/ch02751.itc", 0x21)
    LoadChrToIndex("chr/ch02752.itc", 0x22)
    LoadChrToIndex("chr/ch31252.itc", 0x23)
    LoadChrToIndex("chr/ch31251.itc", 0x24)
    LoadChrToIndex("chr/ch31350.itc", 0x25)
    LoadChrToIndex("chr/ch31351.itc", 0x26)
    LoadChrToIndex("chr/ch07000.itc", 0x27)
    LoadChrToIndex("chr/ch05900.itc", 0x28)
    LoadChrToIndex("chr/ch09300.itc", 0x29)
    LoadChrToIndex("chr/ch00150.itc", 0x2A)
    LoadChrToIndex("chr/ch00151.itc", 0x2B)
    LoadChrToIndex("chr/ch00250.itc", 0x2C)
    LoadChrToIndex("chr/ch00251.itc", 0x2D)
    LoadChrToIndex("chr/ch00950.itc", 0x2E)
    LoadChrToIndex("chr/ch00951.itc", 0x2F)
    LoadChrToIndex("chr/ch00952.itc", 0x30)
    LoadChrToIndex("apl/ch50509.itc", 0x31)
    LoadChrToIndex("chr/ch00152.itc", 0x32)
    LoadChrToIndex("chr/ch24800.itc", 0x33)
    LoadChrToIndex("chr/ch20700.itc", 0x34)
    OP_68(33000, -2900, -19000, 0)
    MoveCamera(53, 15, -5, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 41000, -4000, -19000, 270)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x102, 41000, -4000, -19000, 270)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x103, 41000, -4000, -19000, 270)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x104, 41000, -4000, -19000, 270)
    SetChrChipByIndex(0x10A, 0x2E)
    SetChrSubChip(0x10A, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10A, 41000, -4000, -19000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 41000, -4000, -19000, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x4)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xF, 4200, 500, -700, 120)
    SetChrPos(0x10, 4200, 500, -700, 120)
    SetChrPos(0x11, 4200, 500, -700, 120)
    SetChrPos(0x12, 4200, 500, -700, 120)
    SetChrPos(0x13, 6900, 0, -9000, 90)
    SetChrPos(0x14, 6400, 0, -7400, 90)
    SetChrPos(0x15, 4900, 0, -8600, 90)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 5500, 3000, 14800, 180)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 9500, 3000, 14100, 180)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x29)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 8200, 3000, 14200, 180)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x33)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 8700, 3000, 17050, 180)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x34)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 8200, 3000, 17620, 180)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_78(0x10, 0x16)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFlags(0x10, 0x4)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x4)
    OP_49()
    SetChrPos(0x16, -27000, 0, 3500, 0)
    OP_D3(0x16, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x10, 0x1E)
    OP_71(0x10, 0xB5, 0xF0, 0x0, 0x20)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0xA)
    LoadEffect(0x0, "event\\ev606_00.eff")
    LoadEffect(0x1, "event\\eva04_00.eff")
    LoadEffect(0x2, "battle\\btgun00.eff")
    LoadEffect(0x3, "event\\eva03_00.eff")
    Sound(103, 0, 100, 0)
    SetCameraDistance(15000, 2000)
    FadeToBright(2000, 0)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(450)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(450)
    BeginChrThread(0x102, 3, 0, 16)
    Sleep(450)
    BeginChrThread(0x103, 3, 0, 17)
    Sleep(450)
    BeginChrThread(0x10A, 3, 0, 18)
    Sleep(450)
    BeginChrThread(0x8, 3, 0, 19)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(19400, 1000, -8600, 0)
    MoveCamera(57, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    MoveCamera(47, 19, 0, 2500)
    SetCameraDistance(16500, 2500)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x8, 3)
    OP_0D()
    OP_6F(0x79)

    #C0006
    ChrTalk(
        0x101,
        (
            "#11P#0010F呜，刚才那些人难道是\x01",
            "贝尔加德门警备队的吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#0307F#11P嗯……！\x01",
            "其中还有我认识的人呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0108F#5P难道和那些黑手党一样，\x01",
            "被人操纵了吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        "#12P#0201F极有可能……！\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x10A,
        (
            "#6P#0610F总、总之，\x01",
            "先想办法回到警察局总部……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_90(0x9, 18600, -1500, -17500, 1)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)

    def lambda_F09():
        OP_92(0xFE, 0x4E20, 0xFFFFD120, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F09)
    SetChrChip(0x0, 0x9, 0x1E, 0xC8)
    Sound(854, 0, 100, 0)

    def lambda_F2A():
        OP_9D(0xFE, 0x4E20, 0x3E8, 0xFFFFD120, 0xC80, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F2A)
    Sleep(600)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_F90():
        OP_92(0xFE, 0x3458, 0xFFFFE0C0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F90)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)
    OP_68(16400, 1000, -8600, 1000)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_FC5():
        OP_9D(0xFE, 0x3458, 0x0, 0xFFFFE0C0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FC5)
    Sleep(400)
    SetChrSubChip(0x9, 0x1)
    WaitChrThread(0x9, 1)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1024():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1024)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    Sound(925, 0, 100, 0)
    WaitChrThread(0x9, 2)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    OP_6F(0x1)
    #Sound(2054, 255, 100, 0)    #voice#Zeit

    #C0011
    ChrTalk(
        0x9,
        "#1207F#11P嗷呜～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_110C():
        OP_93(0xFE, 0x10E, 0x258)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_110C)
    Sleep(30)

    def lambda_111C():
        OP_93(0xFE, 0x10E, 0x258)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_111C)
    Sleep(30)

    def lambda_112C():
        OP_93(0xFE, 0x10E, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_112C)
    Sleep(30)

    def lambda_113C():
        OP_93(0xFE, 0x10E, 0x258)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_113C)
    WaitChrThread(0x10A, 2)
    Sleep(300)
    Fade(500)
    OP_68(-15000, 1500, 3500, 0)
    MoveCamera(53, 15, -5, 0)
    OP_6E(750, 0)
    SetCameraDistance(17500, 0)
    OP_68(-5000, 1500, 3500, 3000)
    MoveCamera(45, 15, -5, 3000)
    SetCameraDistance(14500, 3000)
    ClearMapObjFlags(0x10, 0x4)

    def lambda_11AE():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xDAC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_11AE)
    PlayEffect(0x3, 0x0, 0x16, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x1, 0x16, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x2, 0x16, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(493, 0, 100, 0)
    OP_6F(0x79)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    Fade(250)
    OP_68(-2000, 1000, 3500, 0)
    MoveCamera(330, 27, 5, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_68(3400, 1000, -700, 1000)
    SetCameraDistance(16000, 1000)
    WaitChrThread(0x16, 1)

    def lambda_12CF():
        OP_9E(0xFE, 0xFFFFF830, 0xFFFFFA24, 0x13880, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_12CF)

    def lambda_12EA():
        OP_D3(0xFE, 0x0, 0x30D40, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_12EA)
    BeginChrThread(0x16, 3, 0, 6)
    Sound(495, 0, 100, 0)
    WaitChrThread(0x16, 1)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    OP_24(0x1ED)
    SetMapObjFlags(0x10, 0x20)
    OP_71(0x10, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x10)
    OP_71(0x10, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x10)
    OP_68(4900, 1000, -1000, 1500)
    MoveCamera(330, 23, 0, 1500)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    BeginChrThread(0xF, 3, 0, 21)
    Sleep(400)
    BeginChrThread(0x10, 3, 0, 22)
    Sleep(400)
    BeginChrThread(0x11, 3, 0, 23)
    Sleep(400)
    BeginChrThread(0x12, 3, 0, 24)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)

    #N0012
    NpcTalk(
        0x101,
        "琪雅",
        "#1105F哇哇，又来了吗～！？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#0010F呜……\x01",
            "走那边也不行吗……！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        "#1007F暂且前往中央广场！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(17400, 1000, -8600, 0)
    MoveCamera(47, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(20400, 1000, -8600, 7000)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 7)
    BeginChrThread(0x104, 3, 0, 8)
    BeginChrThread(0x102, 3, 0, 9)
    BeginChrThread(0x103, 3, 0, 10)
    BeginChrThread(0x10A, 3, 0, 11)
    BeginChrThread(0x8, 3, 0, 12)
    BeginChrThread(0x9, 3, 0, 13)
    BeginChrThread(0xF, 3, 0, 5)
    Sleep(6000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x18, 0x2)

    def lambda_14D1():
        OP_97(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_14D1)
    Sleep(50)

    def lambda_14EE():
        OP_97(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_14EE)
    Sleep(50)

    def lambda_150B():
        OP_97(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_150B)
    Sleep(3000)
    OP_6F(0x1)
    Fade(1000)
    OP_68(7500, 4000, 14200, 0)
    MoveCamera(42, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetCameraDistance(16000, 2000)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    EndChrThread(0x15, 0xFF)
    OP_64(0xA)
    OP_64(0xB)
    OP_64(0xC)
    OP_64(0xD)
    OP_64(0xE)

    #C0015
    ChrTalk(
        0xA,
        "#5P这、这是怎么回事……！？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        "#5P#3601F伊安律师，这是……！？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xC,
        (
            "#2205F#5P看、看起来，\x01",
            "情况似乎很严重呢！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    #C0018
    ChrTalk(
        0xC,
        (
            "#2201F#11P──哈罗德先生！\x01",
            "你先回家吧！\x02\x03",

            "其他人也赶快回家去！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    SetScenarioFlags(0x5C, 6)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_8AA end

    def Function_5_1708(): pass

    label("Function_5_1708")

    Sound(956, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14100, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15600, 0, -6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14300, 0, -7300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12300, 0, -10700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 11300, 0, -8500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(956, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14100, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15600, 0, -6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14300, 0, -7300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12300, 0, -10700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 11300, 0, -8500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(956, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14100, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15600, 0, -6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14300, 0, -7300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12300, 0, -10700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 11300, 0, -8500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(956, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14100, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15600, 0, -6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14300, 0, -7300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12300, 0, -10700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 11300, 0, -8500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Return()

    # Function_5_1708 end

    def Function_6_1D79(): pass

    label("Function_6_1D79")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -4000, 0, 5500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(230)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1300, 0, 5000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(230)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 300, 0, 3700, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(230)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 2000, 0, 2300, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(230)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 5000, -30, 1000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_6_1D79 end

    def Function_7_1E99(): pass

    label("Function_7_1E99")

    Sleep(100)
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_1EA8():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EA8)
    WaitChrThread(0x101, 1)
    Return()

    # Function_7_1E99 end

    def Function_8_1EC2(): pass

    label("Function_8_1EC2")

    OP_93(0x104, 0x5A, 0x1F4)

    def lambda_1ECE():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1ECE)
    WaitChrThread(0x104, 1)
    Return()

    # Function_8_1EC2 end

    def Function_9_1EE8(): pass

    label("Function_9_1EE8")

    SetChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(600)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)

    def lambda_1F48():
        OP_98(0xFE, 0x64, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F48)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(600)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)

    def lambda_1FB4():
        OP_98(0xFE, 0x64, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FB4)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x20)
    OP_93(0x102, 0x5A, 0x1F4)

    def lambda_1FF0():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FF0)
    WaitChrThread(0x102, 1)
    Return()

    # Function_9_1EE8 end

    def Function_10_200A(): pass

    label("Function_10_200A")

    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    def lambda_2017():
        OP_98(0xFE, 0x5DC, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2017)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    OP_93(0x103, 0x5A, 0x1F4)

    def lambda_2044():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2044)
    WaitChrThread(0x103, 1)
    Return()

    # Function_10_200A end

    def Function_11_205E(): pass

    label("Function_11_205E")

    SetChrChipByIndex(0x10A, 0x30)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x10A, 0x2E)
    SetChrSubChip(0x10A, 0x0)
    OP_93(0x10A, 0x5A, 0x1F4)

    def lambda_21FA():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_21FA)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_11_205E end

    def Function_12_2214(): pass

    label("Function_12_2214")

    SetChrChipByIndex(0x8, 0x31)
    SetChrSubChip(0x8, 0x4)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0x8, 0x5)
    Sleep(150)
    SetChrSubChip(0x8, 0x6)
    Sleep(100)
    SetChrSubChip(0x8, 0x7)
    Sleep(100)
    SetChrSubChip(0x8, 0x4)
    Sleep(100)
    SetChrSubChip(0x8, 0x3)
    Sleep(70)
    SetChrSubChip(0x8, 0x2)
    Sleep(70)
    SetChrSubChip(0x8, 0x1)
    Sleep(70)
    SetChrSubChip(0x8, 0x0)
    Sound(531, 0, 100, 0)
    Sleep(70)
    SetChrSubChip(0x8, 0x1)
    Sleep(70)
    SetChrSubChip(0x8, 0x2)
    Sleep(70)
    SetChrSubChip(0x8, 0x3)
    Sleep(70)
    SetChrSubChip(0x8, 0x4)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0x8, 0x5)
    Sleep(150)
    SetChrSubChip(0x8, 0x6)
    Sleep(100)
    SetChrSubChip(0x8, 0x7)
    Sleep(100)
    SetChrSubChip(0x8, 0x4)
    Sleep(100)
    SetChrSubChip(0x8, 0x3)
    Sleep(70)
    SetChrSubChip(0x8, 0x2)
    Sleep(70)
    SetChrSubChip(0x8, 0x1)
    Sleep(70)
    SetChrSubChip(0x8, 0x0)
    Sound(531, 0, 100, 0)
    Sleep(70)
    SetChrSubChip(0x8, 0x1)
    Sleep(70)
    SetChrSubChip(0x8, 0x2)
    Sleep(70)
    SetChrSubChip(0x8, 0x3)
    Sleep(70)
    SetChrSubChip(0x8, 0x4)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0x8, 0x5)
    Sleep(150)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x5A, 0x1F4)

    def lambda_23A5():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23A5)
    WaitChrThread(0x8, 1)
    Return()

    # Function_12_2214 end

    def Function_13_23BF(): pass

    label("Function_13_23BF")


    def lambda_23C4():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_23C4)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x3)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1300)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_241C():
        OP_92(0xFE, 0x4E20, 0xFFFFD120, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_241C)
    WaitChrThread(0x9, 2)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_247B():
        OP_9D(0xFE, 0x4E20, 0x3E8, 0xFFFFD120, 0x6A4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_247B)
    Sleep(600)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)

    def lambda_24AA():
        OP_92(0xFE, 0x5F50, 0xFFFFE890, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_24AA)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_24CE():
        OP_9D(0xFE, 0x5F50, 0x0, 0xFFFFE890, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_24CE)
    Sleep(400)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x9, 0x3)

    def lambda_2501():
        OP_93(0xFE, 0x5A, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2501)
    Sleep(50)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_251B():
        OP_9D(0xFE, 0x8660, 0x44C, 0xFFFFE890, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_251B)
    Sleep(500)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_255B():
        OP_9D(0xFE, 0xA1B8, 0x834, 0xFFFFE890, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_255B)
    Sleep(500)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x9, 0x3)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_23BF end

    def Function_14_25A0(): pass

    label("Function_14_25A0")


    def lambda_25A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25A5)

    def lambda_25B6():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25B6)
    Sleep(1000)

    def lambda_25D3():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25D3)
    Sleep(500)
    OP_68(18000, -900, -19000, 4000)
    MoveCamera(25, 10, 5, 4000)
    WaitChrThread(0xFE, 1)

    def lambda_2610():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2610)
    WaitChrThread(0xFE, 1)

    def lambda_262E():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_262E)
    WaitChrThread(0xFE, 1)

    def lambda_264C():
        OP_95(0xFE, 20100, 0, -7400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_264C)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_14_25A0 end

    def Function_15_266D(): pass

    label("Function_15_266D")


    def lambda_2672():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2672)

    def lambda_2683():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2683)
    Sleep(1000)

    def lambda_26A0():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26A0)
    WaitChrThread(0xFE, 1)

    def lambda_26BE():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26BE)
    WaitChrThread(0xFE, 1)

    def lambda_26DC():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26DC)
    WaitChrThread(0xFE, 1)

    def lambda_26FA():
        OP_95(0xFE, 20500, 0, -8700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26FA)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_15_266D end

    def Function_16_271B(): pass

    label("Function_16_271B")


    def lambda_2720():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2720)

    def lambda_2731():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2731)
    Sleep(1000)

    def lambda_274E():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_274E)
    WaitChrThread(0xFE, 1)

    def lambda_276C():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_276C)
    WaitChrThread(0xFE, 1)

    def lambda_278A():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_278A)
    WaitChrThread(0xFE, 1)

    def lambda_27A8():
        OP_95(0xFE, 18400, 0, -7300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27A8)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_16_271B end

    def Function_17_27C9(): pass

    label("Function_17_27C9")


    def lambda_27CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27CE)

    def lambda_27DF():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27DF)
    Sleep(1000)

    def lambda_27FC():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27FC)
    WaitChrThread(0xFE, 1)

    def lambda_281A():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_281A)
    WaitChrThread(0xFE, 1)

    def lambda_2838():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2838)
    WaitChrThread(0xFE, 1)

    def lambda_2856():
        OP_95(0xFE, 18500, 0, -9200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2856)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x2D, 0x1F4)
    Return()

    # Function_17_27C9 end

    def Function_18_2877(): pass

    label("Function_18_2877")


    def lambda_287C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_287C)

    def lambda_288D():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_288D)
    Sleep(1000)

    def lambda_28AA():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28AA)
    WaitChrThread(0xFE, 1)

    def lambda_28C8():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28C8)
    WaitChrThread(0xFE, 1)

    def lambda_28E6():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28E6)
    WaitChrThread(0xFE, 1)

    def lambda_2904():
        OP_95(0xFE, 17100, 0, -9300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2904)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0x5A, 0x1F4)
    Return()

    # Function_18_2877 end

    def Function_19_2925(): pass

    label("Function_19_2925")

    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)

    def lambda_2932():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2932)

    def lambda_2943():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2943)
    Sleep(1000)

    def lambda_2960():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2960)
    WaitChrThread(0xFE, 1)

    def lambda_297E():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_297E)
    WaitChrThread(0xFE, 1)

    def lambda_299C():
        OP_95(0xFE, 18800, 0, -10600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_299C)
    WaitChrThread(0x8, 1)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x0, 0x1F4)
    Return()

    # Function_19_2925 end

    def Function_20_29C5(): pass

    label("Function_20_29C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B1B")

    def lambda_29D5():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_29D5)
    SetChrSubChip(0xFE, 0x3)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(700)
    Jump("Function_20_29C5")

    label("loc_2B1B")

    Return()

    # Function_20_29C5 end

    def Function_21_2B1C(): pass

    label("Function_21_2B1C")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2B29():
        OP_95(0xFE, 5600, 0, -1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B29)

    def lambda_2B43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B43)
    WaitChrThread(0xFE, 1)

    def lambda_2B58():
        OP_95(0xFE, 6300, 0, -3300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2B58)
    WaitChrThread(0xF, 1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    BeginChrThread(0xFE, 0, 0, 20)
    Return()

    # Function_21_2B1C end

    def Function_22_2B8F(): pass

    label("Function_22_2B8F")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2B9C():
        OP_95(0xFE, 5600, 0, -1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B9C)

    def lambda_2BB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BB6)
    WaitChrThread(0xFE, 1)

    def lambda_2BCB():
        OP_95(0xFE, 7600, 0, -2000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2BCB)
    WaitChrThread(0x10, 1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    BeginChrThread(0xFE, 0, 0, 20)
    BeginChrThread(0x18, 1, 0, 25)
    Return()

    # Function_22_2B8F end

    def Function_23_2C08(): pass

    label("Function_23_2C08")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2C15():
        OP_95(0xFE, 5600, 0, -1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C15)

    def lambda_2C2F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C2F)
    WaitChrThread(0xFE, 1)

    def lambda_2C44():
        OP_95(0xFE, 5000, 0, -3500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C44)
    WaitChrThread(0x11, 1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    BeginChrThread(0xFE, 0, 0, 20)
    BeginChrThread(0x18, 2, 0, 26)
    Return()

    # Function_23_2C08 end

    def Function_24_2C81(): pass

    label("Function_24_2C81")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2C8E():
        OP_95(0xFE, 5600, 0, -1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C8E)

    def lambda_2CA8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CA8)
    WaitChrThread(0xFE, 1)

    def lambda_2CBD():
        OP_95(0xFE, 6400, 0, -2000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2CBD)
    WaitChrThread(0x12, 1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    BeginChrThread(0xFE, 0, 0, 20)
    Return()

    # Function_24_2C81 end

    def Function_25_2CF4(): pass

    label("Function_25_2CF4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D0D")
    Sound(356, 0, 90, 0)
    Sleep(1200)
    Jump("Function_25_2CF4")

    label("loc_2D0D")

    Return()

    # Function_25_2CF4 end

    def Function_26_2D0E(): pass

    label("Function_26_2D0E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D27")
    Sound(957, 0, 80, 0)
    Sleep(1200)
    Jump("Function_26_2D0E")

    label("loc_2D27")

    Return()

    # Function_26_2D0E end

    SaveToFile()

Try(main)
