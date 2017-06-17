from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c000b.bin",                # FileName
        "c000b",                    # MapName
        "c000b",                    # Location
        0x0002,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1],
    )

    BuildStringList((
        "c000b",                  # 0
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

    PlaceName(-9.25, 0.0, 67.0, 0x0000, 0x0000, "中央広場")
    PlaceName(-75.0, 0.0, 71.5, 0x0000, 0x0000, "西通り")
    PlaceName(17.75, 0.0, 156.0, 0x0000, 0x0000, "行政区")
    PlaceName(-136.0, 0.0, 146.0, 0x0000, 0x0000, "住宅街")
    PlaceName(-63.0, 0.0, 138.0, 0x0000, 0x0000, "歓楽街")
    PlaceName(72.0, 0.0, 44.0, 0x0000, 0x0000, "東通り")
    PlaceName(107.5, 0.0, -11.0, 0x0000, 0x0000, "旧市街")
    PlaceName(100.0, 0.0, 110.0, 0x0000, 0x0000, "港湾区")
    PlaceName(74.0, 0.0, 204.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(2.0, 0.0, -2.0, 0x0000, 0x0000, "駅前通り")
    PlaceName(-45.0, 0.0, 102.0, 0x0000, 0x0000, "裏通り")
    PlaceName(-1.0, 0.0, -33.0, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(126.0, 0.0, 58.0, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-126.0, 0.0, 70.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-120.0, 0.0, 170.0, 0x0000, 0x0000, "マインツ山道")
    PlaceName(11.0, 0.0, 286.0, 0x0000, 0x0000, "オルキスタワー")
    PlaceName(-31.25, 0.0, 53.0, 0x0000, 0x0051, "")
    PlaceName(22.5, 0.0, 79.0, 0x0000, 0x0054, "")
    PlaceName(-6.75, 0.0, 45.0, 0x0000, 0x0057, "")
    PlaceName(-32.0, 0.0, 82.0, 0x0000, 0x0053, "")
    PlaceName(-11.5, 0.0, 106.0, 0x0000, 0x0053, "")
    PlaceName(-62.25, 0.0, 77.0, 0x0000, 0x0053, "")
    PlaceName(-72.0, 0.0, 98.0, 0x0000, 0x0053, "")
    PlaceName(-48.0, 0.0, 130.0, 0x0000, 0x0052, "")
    PlaceName(-43.25, 0.0, 117.0, 0x0000, 0x0053, "")
    PlaceName(-34.5, 0.0, 108.5, 0x0000, 0x0053, "")
    PlaceName(-6.0, 0.0, 179.5, 0x0000, 0x0051, "")
    PlaceName(106.0, 0.0, 44.0, 0x0000, 0x0052, "")
    PlaceName(89.0, 0.0, -46.5, 0x0000, 0x0053, "")
    PlaceName(76.0, 0.0, -28.0, 0x0000, 0x0053, "")

    ChipFrameInfo(756, 0)                                        # 0

    ScpFunction((
        "Function_0_2F4",          # 00, 0
        "Function_1_2F5",          # 01, 1
    ))


    def Function_0_2F4(): pass

    label("Function_0_2F4")

    Return()

    # Function_0_2F4 end

    def Function_1_2F5(): pass

    label("Function_1_2F5")

    Return()

    # Function_1_2F5 end

    SaveToFile()

Try(main)
