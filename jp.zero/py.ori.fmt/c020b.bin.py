from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "セルゲイ課長",           # 1
        "ツァイト",               # 2
        "オスカー",               # 3
        "ハロルド",               # 4
        "イアン弁護士",           # 5
        "タリーズ",               # 6
        "モモ",                   # 7
        "警備隊員",               # 8
        "警備隊員",               # 9
        "警備隊員",               # 10
        "警備隊員",               # 11
        "警備隊員",               # 12
        "警備隊員",               # 13
        "警備隊員",               # 14
        "車１",                   # 15
        "車２",                   # 16
        "SE制御",                 # 17
        "中央広場",               # 18
        "西通り",                 # 19
        "行政区",                 # 20
        "住宅街",                 # 21
        "歓楽街",                 # 22
        "東通り",                 # 23
        "旧市街",                 # 24
        "港湾区",                 # 25
        "ＩＢＣ",                 # 26
        "駅前通り",               # 27
        "裏通り",                 # 28
        "ウルスラ間道",           # 29
        "東クロスベル街道",       # 30
        "西クロスベル街道",       # 31
        "マインツ山道",           # 32
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

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "中央広場")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "西通り")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "行政区")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "住宅街")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "歓楽街")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "東通り")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "旧市街")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "港湾区")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "駅前通り")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "裏通り")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "マインツ山道")
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
        "Function_3_782",          # 03, 3
        "Function_4_8CF",          # 04, 4
        "Function_5_1769",         # 05, 5
        "Function_6_1DDA",         # 06, 6
        "Function_7_1EFA",         # 07, 7
        "Function_8_1F23",         # 08, 8
        "Function_9_1F49",         # 09, 9
        "Function_10_206B",        # 0A, 10
        "Function_11_20BF",        # 0B, 11
        "Function_12_2275",        # 0C, 12
        "Function_13_2420",        # 0D, 13
        "Function_14_2601",        # 0E, 14
        "Function_15_26CE",        # 0F, 15
        "Function_16_277C",        # 10, 16
        "Function_17_282A",        # 11, 17
        "Function_18_28D8",        # 12, 18
        "Function_19_2986",        # 13, 19
        "Function_20_2A26",        # 14, 20
        "Function_21_2B7D",        # 15, 21
        "Function_22_2BF0",        # 16, 22
        "Function_23_2C69",        # 17, 23
        "Function_24_2CE2",        # 18, 24
        "Function_25_2D55",        # 19, 25
        "Function_26_2D6F",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74B")
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
            "#56I地のセピス×８０\x01\x07\x02",

            "#57I水のセピス×８０\x01\x07\x02",

            "#58I火のセピス×８０\x01\x07\x02",

            "#59I風のセピス×８０\x01\x07\x02",

            "#60I時のセピス×８０\x01\x07\x02",

            "#61I空のセピス×８０\x01\x07\x02",

            "#62I幻のセピス×８０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x110, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_770")

    label("loc_74B")


    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_770")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_61F end

    def Function_3_782(): pass

    label("Function_3_782")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87E")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA7, 1)"), scpexpr(EXPR_END)), "loc_807")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_879")

    label("loc_807")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_879")

    Jump("loc_8C3")

    label("loc_87E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
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

    label("loc_8C3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_782 end

    def Function_4_8CF(): pass

    label("Function_4_8CF")

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
            "#11P#0010Fくっ、まさか今のは\x01",
            "ベルガード門の警備隊か！？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#0307F#11Pああ……！\x01",
            "見知った顔がいたぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0108F#5Pまさかマフィアと同じように\x01",
            "操られているというの……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        "#12P#0201Fその可能性は高そうです……！\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x10A,
        (
            "#6P#0610Fと、とにかく\x01",
            "何とか警察本部まで……！\x02",
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

    def lambda_F46():
        OP_92(0xFE, 0x4E20, 0xFFFFD120, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F46)
    SetChrChip(0x0, 0x9, 0x1E, 0xC8)
    Sound(854, 0, 100, 0)

    def lambda_F67():
        OP_9D(0xFE, 0x4E20, 0x3E8, 0xFFFFD120, 0xC80, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F67)
    Sleep(600)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_FCD():
        OP_92(0xFE, 0x3458, 0xFFFFE0C0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_FCD)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)
    OP_68(16400, 1000, -8600, 1000)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_1002():
        OP_9D(0xFE, 0x3458, 0x0, 0xFFFFE0C0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1002)
    Sleep(400)
    SetChrSubChip(0x9, 0x1)
    WaitChrThread(0x9, 1)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1061():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1061)
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
        "#1207F#11Pウォン！\x02",
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

    def lambda_1149():
        OP_93(0xFE, 0x10E, 0x258)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1149)
    Sleep(30)

    def lambda_1159():
        OP_93(0xFE, 0x10E, 0x258)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1159)
    Sleep(30)

    def lambda_1169():
        OP_93(0xFE, 0x10E, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1169)
    Sleep(30)

    def lambda_1179():
        OP_93(0xFE, 0x10E, 0x258)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_1179)
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

    def lambda_11EB():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xDAC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_11EB)
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

    def lambda_130C():
        OP_9E(0xFE, 0xFFFFF830, 0xFFFFFA24, 0x13880, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_130C)

    def lambda_1327():
        OP_D3(0xFE, 0x0, 0x30D40, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_1327)
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
        "キーア",
        "#1105Fわわ、また来たよ～！？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#0010Fくっ……\x01",
            "あっちは無理か……！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        "#1007Fいったん中央広場に出るぞ！\x02",
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

    def lambda_151C():
        OP_97(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_151C)
    Sleep(50)

    def lambda_1539():
        OP_97(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1539)
    Sleep(50)

    def lambda_1556():
        OP_97(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1556)
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
        "#5Pな、なんだありゃ……！？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        "#5P#3601F先生、これは……！？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xC,
        (
            "#2205F#5Pど、どうやら\x01",
            "タダ事ではなさそうだ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    #C0018
    ChrTalk(
        0xC,
        (
            "#2201F#11P──ハロルドさん！\x01",
            "あんたは家に戻りたまえ！\x02\x03",

            "他の人たちも早く家の中に！\x02",
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

    # Function_4_8CF end

    def Function_5_1769(): pass

    label("Function_5_1769")

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

    # Function_5_1769 end

    def Function_6_1DDA(): pass

    label("Function_6_1DDA")

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

    # Function_6_1DDA end

    def Function_7_1EFA(): pass

    label("Function_7_1EFA")

    Sleep(100)
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_1F09():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F09)
    WaitChrThread(0x101, 1)
    Return()

    # Function_7_1EFA end

    def Function_8_1F23(): pass

    label("Function_8_1F23")

    OP_93(0x104, 0x5A, 0x1F4)

    def lambda_1F2F():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F2F)
    WaitChrThread(0x104, 1)
    Return()

    # Function_8_1F23 end

    def Function_9_1F49(): pass

    label("Function_9_1F49")

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

    def lambda_1FA9():
        OP_98(0xFE, 0x64, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FA9)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(600)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)

    def lambda_2015():
        OP_98(0xFE, 0x64, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2015)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x20)
    OP_93(0x102, 0x5A, 0x1F4)

    def lambda_2051():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2051)
    WaitChrThread(0x102, 1)
    Return()

    # Function_9_1F49 end

    def Function_10_206B(): pass

    label("Function_10_206B")

    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    def lambda_2078():
        OP_98(0xFE, 0x5DC, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2078)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    OP_93(0x103, 0x5A, 0x1F4)

    def lambda_20A5():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20A5)
    WaitChrThread(0x103, 1)
    Return()

    # Function_10_206B end

    def Function_11_20BF(): pass

    label("Function_11_20BF")

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

    def lambda_225B():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_225B)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_11_20BF end

    def Function_12_2275(): pass

    label("Function_12_2275")

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

    def lambda_2406():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2406)
    WaitChrThread(0x8, 1)
    Return()

    # Function_12_2275 end

    def Function_13_2420(): pass

    label("Function_13_2420")


    def lambda_2425():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2425)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x3)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1300)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_247D():
        OP_92(0xFE, 0x4E20, 0xFFFFD120, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_247D)
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

    def lambda_24DC():
        OP_9D(0xFE, 0x4E20, 0x3E8, 0xFFFFD120, 0x6A4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_24DC)
    Sleep(600)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)

    def lambda_250B():
        OP_92(0xFE, 0x5F50, 0xFFFFE890, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_250B)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_252F():
        OP_9D(0xFE, 0x5F50, 0x0, 0xFFFFE890, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_252F)
    Sleep(400)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x9, 0x3)

    def lambda_2562():
        OP_93(0xFE, 0x5A, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2562)
    Sleep(50)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_257C():
        OP_9D(0xFE, 0x8660, 0x44C, 0xFFFFE890, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_257C)
    Sleep(500)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_25BC():
        OP_9D(0xFE, 0xA1B8, 0x834, 0xFFFFE890, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25BC)
    Sleep(500)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x9, 0x3)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_2420 end

    def Function_14_2601(): pass

    label("Function_14_2601")


    def lambda_2606():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2606)

    def lambda_2617():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2617)
    Sleep(1000)

    def lambda_2634():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2634)
    Sleep(500)
    OP_68(18000, -900, -19000, 4000)
    MoveCamera(25, 10, 5, 4000)
    WaitChrThread(0xFE, 1)

    def lambda_2671():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2671)
    WaitChrThread(0xFE, 1)

    def lambda_268F():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_268F)
    WaitChrThread(0xFE, 1)

    def lambda_26AD():
        OP_95(0xFE, 20100, 0, -7400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26AD)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_14_2601 end

    def Function_15_26CE(): pass

    label("Function_15_26CE")


    def lambda_26D3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26D3)

    def lambda_26E4():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26E4)
    Sleep(1000)

    def lambda_2701():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2701)
    WaitChrThread(0xFE, 1)

    def lambda_271F():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_271F)
    WaitChrThread(0xFE, 1)

    def lambda_273D():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_273D)
    WaitChrThread(0xFE, 1)

    def lambda_275B():
        OP_95(0xFE, 20500, 0, -8700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_275B)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_15_26CE end

    def Function_16_277C(): pass

    label("Function_16_277C")


    def lambda_2781():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2781)

    def lambda_2792():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2792)
    Sleep(1000)

    def lambda_27AF():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27AF)
    WaitChrThread(0xFE, 1)

    def lambda_27CD():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27CD)
    WaitChrThread(0xFE, 1)

    def lambda_27EB():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27EB)
    WaitChrThread(0xFE, 1)

    def lambda_2809():
        OP_95(0xFE, 18400, 0, -7300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2809)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_16_277C end

    def Function_17_282A(): pass

    label("Function_17_282A")


    def lambda_282F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_282F)

    def lambda_2840():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2840)
    Sleep(1000)

    def lambda_285D():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_285D)
    WaitChrThread(0xFE, 1)

    def lambda_287B():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_287B)
    WaitChrThread(0xFE, 1)

    def lambda_2899():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2899)
    WaitChrThread(0xFE, 1)

    def lambda_28B7():
        OP_95(0xFE, 18500, 0, -9200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_28B7)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x2D, 0x1F4)
    Return()

    # Function_17_282A end

    def Function_18_28D8(): pass

    label("Function_18_28D8")


    def lambda_28DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28DD)

    def lambda_28EE():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28EE)
    Sleep(1000)

    def lambda_290B():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_290B)
    WaitChrThread(0xFE, 1)

    def lambda_2929():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2929)
    WaitChrThread(0xFE, 1)

    def lambda_2947():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2947)
    WaitChrThread(0xFE, 1)

    def lambda_2965():
        OP_95(0xFE, 17100, 0, -9300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2965)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0x5A, 0x1F4)
    Return()

    # Function_18_28D8 end

    def Function_19_2986(): pass

    label("Function_19_2986")

    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)

    def lambda_2993():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2993)

    def lambda_29A4():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29A4)
    Sleep(1000)

    def lambda_29C1():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29C1)
    WaitChrThread(0xFE, 1)

    def lambda_29DF():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29DF)
    WaitChrThread(0xFE, 1)

    def lambda_29FD():
        OP_95(0xFE, 18800, 0, -10600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29FD)
    WaitChrThread(0x8, 1)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x0, 0x1F4)
    Return()

    # Function_19_2986 end

    def Function_20_2A26(): pass

    label("Function_20_2A26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B7C")

    def lambda_2A36():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A36)
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
    Jump("Function_20_2A26")

    label("loc_2B7C")

    Return()

    # Function_20_2A26 end

    def Function_21_2B7D(): pass

    label("Function_21_2B7D")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2B8A():
        OP_95(0xFE, 5600, 0, -1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B8A)

    def lambda_2BA4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BA4)
    WaitChrThread(0xFE, 1)

    def lambda_2BB9():
        OP_95(0xFE, 6300, 0, -3300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2BB9)
    WaitChrThread(0xF, 1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    BeginChrThread(0xFE, 0, 0, 20)
    Return()

    # Function_21_2B7D end

    def Function_22_2BF0(): pass

    label("Function_22_2BF0")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2BFD():
        OP_95(0xFE, 5600, 0, -1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BFD)

    def lambda_2C17():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C17)
    WaitChrThread(0xFE, 1)

    def lambda_2C2C():
        OP_95(0xFE, 7600, 0, -2000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2C2C)
    WaitChrThread(0x10, 1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    BeginChrThread(0xFE, 0, 0, 20)
    BeginChrThread(0x18, 1, 0, 25)
    Return()

    # Function_22_2BF0 end

    def Function_23_2C69(): pass

    label("Function_23_2C69")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2C76():
        OP_95(0xFE, 5600, 0, -1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C76)

    def lambda_2C90():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C90)
    WaitChrThread(0xFE, 1)

    def lambda_2CA5():
        OP_95(0xFE, 5000, 0, -3500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2CA5)
    WaitChrThread(0x11, 1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    BeginChrThread(0xFE, 0, 0, 20)
    BeginChrThread(0x18, 2, 0, 26)
    Return()

    # Function_23_2C69 end

    def Function_24_2CE2(): pass

    label("Function_24_2CE2")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2CEF():
        OP_95(0xFE, 5600, 0, -1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CEF)

    def lambda_2D09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D09)
    WaitChrThread(0xFE, 1)

    def lambda_2D1E():
        OP_95(0xFE, 6400, 0, -2000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2D1E)
    WaitChrThread(0x12, 1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    BeginChrThread(0xFE, 0, 0, 20)
    Return()

    # Function_24_2CE2 end

    def Function_25_2D55(): pass

    label("Function_25_2D55")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D6E")
    Sound(356, 0, 90, 0)
    Sleep(1200)
    Jump("Function_25_2D55")

    label("loc_2D6E")

    Return()

    # Function_25_2D55 end

    def Function_26_2D6F(): pass

    label("Function_26_2D6F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D88")
    Sound(957, 0, 80, 0)
    Sleep(1200)
    Jump("Function_26_2D6F")

    label("loc_2D88")

    Return()

    # Function_26_2D6F end

    SaveToFile()

Try(main)
