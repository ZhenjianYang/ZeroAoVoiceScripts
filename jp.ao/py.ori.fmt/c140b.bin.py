from ScenarioHelper import *

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
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 46, 0, 0, 0, 1],
    )

    BuildStringList((
        "c140b",                  # 0
        "中央広場",               # 1
        "西通り",                 # 2
        "行政区",                 # 3
        "住宅街",                 # 4
        "歓楽街",                 # 5
        "東通り",                 # 6
        "旧市街",                 # 7
        "港湾区",                 # 8
        "ＩＢＣ",                 # 9
        "駅前通り",               # 10
        "裏通り",                 # 11
        "ウルスラ間道",           # 12
        "東クロスベル街道",       # 13
        "西クロスベル街道",       # 14
        "マインツ山道",           # 15
        "オルキスタワー",         # 16
    ))

    DeclActor(47720,   -1100,   -33160,  1200,    47720,   100,     -33160,  0x007C, 0,  2,  0x0000)

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
    PlaceName(-88.0, 0.0, 360.0, 0x0000, 0x0000, "オルキスタワー")
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

    ChipFrameInfo(796, 0)                                        # 0

    ScpFunction((
        "Function_0_31C",          # 00, 0
        "Function_1_31D",          # 01, 1
        "Function_2_335",          # 02, 2
    ))


    def Function_0_31C(): pass

    label("Function_0_31C")

    Return()

    # Function_0_31C end

    def Function_1_31D(): pass

    label("Function_1_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330")
    OP_70(0x7, 0x0)
    Jump("loc_334")

    label("loc_330")

    OP_70(0x7, 0x1E)

    label("loc_334")

    Return()

    # Function_1_31D end

    def Function_2_335(): pass

    label("Function_2_335")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3D, 1)"), scpexpr(EXPR_END)), "loc_3BE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_430")

    label("loc_3BE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_430")

    Jump("loc_47A")

    label("loc_435")

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

    label("loc_47A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_335 end

    SaveToFile()

Try(main)
