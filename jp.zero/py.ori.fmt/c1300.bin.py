from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1300.bin",                # FileName
        "c1300",                    # MapName
        "c1300",                    # Location
        0x001B,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 27, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1300",                  # 0
        "警備員ビルス",           # 1
        "警備員ウォング",         # 2
        "秘書アーネスト",         # 3
        "グレイス",               # 4
        "ダミーだよん",           # 5
        "中央広場",               # 6
        "西通り",                 # 7
        "行政区",                 # 8
        "住宅街",                 # 9
        "歓楽街",                 # 10
        "東通り",                 # 11
        "旧市街",                 # 12
        "港湾区",                 # 13
        "ＩＢＣ",                 # 14
        "駅前通り",               # 15
        "裏通り",                 # 16
        "ウルスラ間道",           # 17
        "東クロスベル街道",       # 18
        "西クロスベル街道",       # 19
        "マインツ山道",           # 20
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
    ))

    DeclNpc(3910,    0,       5050,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(1700,    0,       -22129,  180,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(1750,    0,       -1799,   0,    510,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(7000,    0,       2300,    1200,    7000,    1700,    2300,    0x007C, 0,  10, 0x0000)
    DeclActor(1750,    0,       -1800,   1500,    1750,    1500,    -1800,   0x007C, 0,  5,  0x0000)

    PlaceName(-133.72000122070312, 0.0, -187.47999572753906, 0x0000, 0x0000, "中央広場")
    PlaceName(-223.1999969482422, 0.0, -181.35000610351562, 0x0000, 0x0000, "西通り")
    PlaceName(-96.97000122070312, 0.0, -66.3499984741211, 0x0000, 0x0000, "行政区")
    PlaceName(-306.2300109863281, 0.0, -79.95999908447266, 0x0000, 0x0000, "住宅街")
    PlaceName(-206.8699951171875, 0.0, -90.8499984741211, 0x0000, 0x0000, "歓楽街")
    PlaceName(-23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0000, "東通り")
    PlaceName(25.18000030517578, 0.0, -293.6400146484375, 0x0000, 0x0000, "旧市街")
    PlaceName(14.970000267028809, 0.0, -128.9499969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-20.420000076293945, 0.0, -1.0199999809265137, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-118.41000366210938, 0.0, -281.3900146484375, 0x0000, 0x0000, "駅前通り")
    PlaceName(-182.3699951171875, 0.0, -139.83999633789062, 0x0000, 0x0000, "裏通り")
    PlaceName(-122.48999786376953, 0.0, -323.5799865722656, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(50.36000061035156, 0.0, -199.72999572753906, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-292.6199951171875, 0.0, -183.38999938964844, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-284.45001220703125, 0.0, -47.290000915527344, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-163.66000366210938, 0.0, -206.52999877929688, 0x0000, 0x0051, "")
    PlaceName(-90.51000213623047, 0.0, -171.14999389648438, 0x0000, 0x0054, "")
    PlaceName(-130.32000732421875, 0.0, -217.4199981689453, 0x0000, 0x0057, "")
    PlaceName(-164.67999267578125, 0.0, -167.05999755859375, 0x0000, 0x0053, "")
    PlaceName(-136.77999877929688, 0.0, -134.39999389648438, 0x0000, 0x0053, "")
    PlaceName(-205.85000610351562, 0.0, -173.8699951171875, 0x0000, 0x0053, "")
    PlaceName(-219.1199951171875, 0.0, -145.2899932861328, 0x0000, 0x0053, "")
    PlaceName(-186.4600067138672, 0.0, -101.7300033569336, 0x0000, 0x0052, "")
    PlaceName(-179.99000549316406, 0.0, -119.43000030517578, 0x0000, 0x0053, "")
    PlaceName(-168.0800018310547, 0.0, -131.0, 0x0000, 0x0053, "")
    PlaceName(-129.3000030517578, 0.0, -34.369998931884766, 0x0000, 0x0051, "")
    PlaceName(23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0052, "")
    PlaceName(0.0, 0.0, -341.95001220703125, 0x0000, 0x0053, "")
    PlaceName(-17.690000534057617, 0.0, -316.7699890136719, 0x0000, 0x0053, "")
    PlaceName(-118.41000366210938, 0.0, -203.80999755859375, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_3F0",          # 00, 0
        "Function_1_4A8",          # 01, 1
        "Function_2_6C0",          # 02, 2
        "Function_3_813",          # 03, 3
        "Function_4_1658",         # 04, 4
        "Function_5_172B",         # 05, 5
        "Function_6_19B8",         # 06, 6
        "Function_7_1A43",         # 07, 7
        "Function_8_1F62",         # 08, 8
        "Function_9_3AFB",         # 09, 9
        "Function_10_4423",        # 0A, 10
    ))


    def Function_0_3F0(): pass

    label("Function_0_3F0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_430"),
        (1, "loc_43C"),
        (2, "loc_448"),
        (3, "loc_454"),
        (4, "loc_460"),
        (5, "loc_46C"),
        (6, "loc_478"),
        (SWITCH_DEFAULT, "loc_484"),
    )


    label("loc_430")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_43C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_448")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_454")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_460")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_46C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_478")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_484")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_490")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_4A7")

    Return()

    # Function_0_3F0 end

    def Function_1_4A8(): pass

    label("Function_1_4A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_557")
    SetChrPos(0x0, -230, -1450, -33980, 0)
    SetChrPos(0x1, -230, -1450, -33980, 0)
    SetChrPos(0x2, -230, -1450, -33980, 0)
    SetChrPos(0x3, -230, -1450, -33980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52F")
    SetChrPos(0x4, -230, -1450, -33980, 0)
    SetChrPos(0x5, -230, -1450, -33980, 0)
    Jump("loc_54E")

    label("loc_52F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54E")
    SetChrPos(0x4, -230, -1450, -33980, 0)

    label("loc_54E")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_557")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_56F")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 6)

    label("loc_56F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A")
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_5AD")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A0")
    Event(0, 9)
    Jump("loc_5AD")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AD")
    SetScenarioFlags(0x53, 2)

    label("loc_5AD")

    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5DB")
    SetChrPos(0x8, -2040, 0, -21950, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_6A8")

    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5E9")
    Jump("loc_6A8")

    label("loc_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5F7")
    Jump("loc_6A8")

    label("loc_5F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_616")
    SetChrPos(0x8, 2610, 0, 2230, 160)
    Jump("loc_6A8")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_635")
    SetChrPos(0x8, -180, 0, -22030, 180)
    Jump("loc_6A8")

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_643")
    Jump("loc_6A8")

    label("loc_643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_651")
    Jump("loc_6A8")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_65F")
    Jump("loc_6A8")

    label("loc_65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_66D")
    Jump("loc_6A8")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_67B")
    Jump("loc_6A8")

    label("loc_67B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_689")
    Jump("loc_6A8")

    label("loc_689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_697")
    Jump("loc_6A8")

    label("loc_697")

    SetChrPos(0x8, -180, 0, -22030, 180)

    label("loc_6A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BF")
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_6BF")

    Return()

    # Function_1_4A8 end

    def Function_2_6C0(): pass

    label("Function_2_6C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_718")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_779")

    label("loc_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_754")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_779")

    label("loc_754")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_779")

    SetMapObjFlags(0x2, 0x4)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A8")
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_7A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B6")

    label("loc_7B6")

    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D2")
    OP_70(0x1, 0x0)

    label("loc_7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E4")
    OP_70(0x1, 0x0)

    label("loc_7E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7F1")
    OP_70(0x1, 0x0)

    label("loc_7F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80D")
    Jump("loc_812")

    label("loc_80D")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_812")

    Return()

    # Function_2_6C0 end

    def Function_3_813(): pass

    label("Function_3_813")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_886")

    #C0001
    ChrTalk(
        0xFE,
        (
            "悪いね、ＩＢＣの営業は\x01",
            "４時半までなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "またのご利用ってことでお願いするよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C6")

    label("loc_886")


    #C0003
    ChrTalk(
        0xFE,
        "ゲートロックＯＫ。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "ロック異常なし、クリアー！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    ClearChrFlags(0x8, 0x10)

    label("loc_8C6")

    Jump("loc_1654")

    label("loc_8CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_958")

    #C0005
    ChrTalk(
        0xFE,
        (
            "我が保安部は優秀だ。\x01",
            "市内の事件も一通り報告が入って来るよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "だがまあ、行方不明者\x01",
            "なんてのは警察の仕事かな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A09")

    label("loc_958")


    #C0007
    ChrTalk(
        0xFE,
        (
            "保安部から\x01",
            "気になる報告が入っているな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "市内で行方不明者が\x01",
            "相次いでいるらしいとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "ふむ、だがまあ\x01",
            "これは警察の仕事だな。\x01",
            "ＩＢＣは今日も平和そのものだしね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_A09")

    Jump("loc_1654")

    label("loc_A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_AFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A67")

    #C0010
    ChrTalk(
        0xFE,
        (
            "港湾区では\x01",
            "発砲事件があったばかりだ、\x01",
            "警備も気が抜けないな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF9")

    label("loc_A67")


    #C0011
    ChrTalk(
        0xFE,
        (
            "港湾区では発砲事件が\x01",
            "あったという報告があってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "どうやらマフィア同士の\x01",
            "抗争らしい……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "今日はいつもより\x01",
            "警備を増やしているよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AF9")

    Jump("loc_1654")

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B78")

    #C0014
    ChrTalk(
        0xFE,
        "妙に話が弾んでいるようなんだ。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "一見遊び人みたいな格好だが\x01",
            "……総裁のお知り合いなのかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C01")

    label("loc_B78")


    #C0016
    ChrTalk(
        0xFE,
        (
            "クロイス総裁がお戻りになったんでね、\x01",
            "いつも通り出迎えたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "うーん、あの若者は誰なんだ？\x01",
            "総裁のお知り合いだろうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C01")

    Jump("loc_1654")

    label("loc_C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_D15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CA0")

    #C0018
    ChrTalk(
        0xFE,
        (
            "ちなみに総裁は外国に出張中、\x01",
            "マリアベルさんは市内に\x01",
            "お出掛けになっているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "確か行政区の方に用事があると\x01",
            "仰っていたな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D10")

    label("loc_CA0")


    #C0020
    ChrTalk(
        0xFE,
        (
            "おやお客さんか。\x01",
            "悪いが今日は休行日だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "関係者以外の立ち入りは\x01",
            "原則できない。\x01",
            "ま、勘弁してくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D10")

    Jump("loc_1654")

    label("loc_D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_E98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DC9")

    #C0022
    ChrTalk(
        0xFE,
        (
            "聞けば、導力ネットの回線を通じた\x01",
            "侵入を掛けられたらしいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "やれやれ、俺たちの警備対象外だ。\x01",
            "技術部の連中には\x01",
            "もっと頑張ってもらわないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E93")

    label("loc_DC9")


    #C0024
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ本社ビルの\x01",
            "警備体制には何の問題もない。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "俺たち保安部の者が\x01",
            "２４時間詰めているからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "だが……ハッキングなんて\x01",
            "よく判らないものは防ぎようがないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "やれやれ、警備対象外だ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E93")

    Jump("loc_1654")

    label("loc_E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_F77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EEF")

    #C0028
    ChrTalk(
        0xFE,
        "用事なら中へどうぞ。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "ロビーの正面に総合受付があるよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F72")

    label("loc_EEF")

    SetScenarioFlags(0x0, 0)

    #C0030
    ChrTalk(
        0xFE,
        (
            "こんにちは。\x01",
            "今日もいい天気だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "ここは市街から離れているから\x01",
            "朝は空気が美味い。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "一日頑張ろうという気になるな。\x02",
    )

    CloseMessageWindow()

    label("loc_F72")

    Jump("loc_1654")

    label("loc_F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_107B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FDB")

    #C0033
    ChrTalk(
        0xFE,
        (
            "顧客の人生に\x01",
            "干渉しないのが警備員だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        "……保安上の問題もあるしね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1076")

    label("loc_FDB")


    #C0035
    ChrTalk(
        0xFE,
        (
            "今日はひどく\x01",
            "しょげ返ったお客さんがいたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "取引にでも失敗したんだろうか。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "……ま、こちらは警備員だ。\x01",
            "声を掛けるようなことはしないがね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1076")

    Jump("loc_1654")

    label("loc_107B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_11C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10FA")

    #C0038
    ChrTalk(
        0xFE,
        (
            "クロイス総裁を出迎えるのは\x01",
            "俺の役目なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "ちなみに市内の移動には\x01",
            "赤いリムジンを使われるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11BB")

    label("loc_10FA")


    #C0040
    ChrTalk(
        0xFE,
        (
            "ＩＢＣグループのトップ、\x01",
            "クロイス総裁は\x01",
            "とてもお忙しい人でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "普段は外国を飛び回っていて\x01",
            "中々お戻りにならない。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "たまにお戻りになられるときは\x01",
            "誠意を込めてお迎えしなくてはね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_11BB")

    Jump("loc_1654")

    label("loc_11C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1336")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1264")

    #C0043
    ChrTalk(
        0xFE,
        (
            "ここは高台だから\x01",
            "警備をするにも見通しがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "職場としては申し分ないし、\x01",
            "ビルで働く職員の人たちも\x01",
            "ここが気に入っているみたいだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1331")

    label("loc_1264")


    #C0045
    ChrTalk(
        0xFE,
        (
            "常々思うんだが、\x01",
            "ＩＢＣの立地は素晴らしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "街を一望できる高台に\x01",
            "ゆったりと流れる川。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "近くには緑も多いし\x01",
            "職場としては申し分ないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "見通しがいいから\x01",
            "保安上の安全性も高いしね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1331")

    Jump("loc_1654")

    label("loc_1336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1464")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13B3")

    #C0049
    ChrTalk(
        0xFE,
        (
            "そうそう、あの年は\x01",
            "５年に一度の市長選もあったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "新人の俺には\x01",
            "何かと忙しい年だったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145F")

    label("loc_13B3")


    #C0051
    ChrTalk(
        0xFE,
        (
            "自分は保安部に配属になって\x01",
            "もう１０年になる。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "丁度このビルが完成した頃だな。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "あの年は何かと忙しかったよ。\x01",
            "着任早々、本社ビルへの\x01",
            "移転作業があったからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_145F")

    Jump("loc_1654")

    label("loc_1464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1567")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14CA")

    #C0054
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ本社ビルへようこそ。\x01",
            "なにか用事かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "ゆっくりしていくといい。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1562")

    label("loc_14CA")


    #C0056
    ChrTalk(
        0xFE,
        (
            "こんにちは、\x01",
            "ＩＢＣ本社ビルへようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "はっは、驚いたかい？\x01",
            "立派なビルだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "初めての人は大抵驚く。\x01",
            "まあ、勤めていれば慣れるがね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1562")

    Jump("loc_1654")

    label("loc_1567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15CD")

    #C0059
    ChrTalk(
        0xFE,
        (
            "ＩＢＣは、本日は\x01",
            "休行日になっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "関係者以外の立ち入りは\x01",
            "原則できないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1654")

    label("loc_15CD")


    #C0061
    ChrTalk(
        0xFE,
        "こんにちは、いい天気だね。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "ＩＢＣは、本日は\x01",
            "休行日となっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "ミラを下ろしに来たのなら悪いね。\x01",
            "また後日来てくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1654")

    TalkEnd(0xFE)
    Return()

    # Function_3_813 end

    def Function_4_1658(): pass

    label("Function_4_1658")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16B4")

    #C0064
    ChrTalk(
        0xFE,
        (
            "ゲートロックの\x01",
            "確認をしている所だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        "悪いが邪魔をせんでくれんか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1727")

    label("loc_16B4")


    #C0066
    ChrTalk(
        0xFE,
        "おや、もう終行時間だぞ。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "客も皆帰ってしまった所だ。\x01",
            "ミラを下ろしに来たのなら\x01",
            "また明日にすることだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1727")

    TalkEnd(0xFE)
    Return()

    # Function_4_1658 end

    def Function_5_172B(): pass

    label("Function_5_172B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_194C")
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)

    #N0068
    NpcTalk(
        0xC,
        "男性の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#N#2Sはっはっは……\x01",
            "面白いことを言うじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #N0069
    NpcTalk(
        0xC,
        "男性の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#N#2Sいや正にその通り！\x01",
            "まさかこのクロスベルで\x01",
            "君のような人物と出会えるとは……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("青年の声")
    SetMessageWindowPos(240, 150, -1, -1)

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2Sいやいや、おっさんも大したもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2Sただの銀行家に\x01",
            "収まってねぇあたりなんて\x01",
            "オレも見習わねえとなァ～㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0072
    ChrTalk(
        0x101,
        (
            "#0005Fこれって……\x01",
            "ディーター総裁のリムジン？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#0105F何か話しているみたいだけど……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_194C")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "中を覗いてみる\x01",      # 0
            "やめておく\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19AA")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("e0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_19B7")

    label("loc_19AA")

    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_19B7")

    Return()

    # Function_5_172B end

    def Function_6_19B8(): pass

    label("Function_6_19B8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1020, 2500, -560, 0)
    MoveCamera(45, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, 1020, 0, -560, 135)
    SetChrPos(0x1, 1020, 0, -560, 135)
    SetChrPos(0x2, 1020, 0, -560, 135)
    SetChrPos(0x3, 1020, 0, -560, 135)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_6_19B8 end

    def Function_7_1A43(): pass

    label("Function_7_1A43")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, -970, 0, -25140, 0)
    SetChrPos(0x102, 630, 0, -25140, 0)
    SetChrPos(0x103, 630, 0, -26970, 0)
    SetChrPos(0x104, -970, 0, -26970, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-3130, 2500, -17030, 0)
    MoveCamera(48, 16, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21000, 0)
    FadeToBright(1000, 0)
    OP_68(-140, 4630, 2210, 8000)
    MoveCamera(24, 23, 0, 8000)
    OP_6E(750, 8000)
    SetCameraDistance(39300, 8000)
    PlaceName2(340, 200, "c_plac06", 0x0, 4000)
    OP_6F(0x79)
    Sleep(1000)

    #A0074
    AnonymousTalk(
        0x101,
        (
            "#0000Fここは……あの\x01",
            "ＩＢＣの本部があるビルだな。\x02",
        )
    )

    CloseMessageWindow()

    #A0075
    AnonymousTalk(
        0x102,
        (
            "#0104Fクロスベル国際銀行\x01",
            "（International Bank of Crossbell）……\x02\x03",

            "幾つもの支店を持つ巨大銀行にして\x01",
            "幅広い事業を展開する一大グループ。\x02\x03",

            "#0102F十年前には総資産額も\x01",
            "大陸一を達成したし……\x01",
            "今やクロスベルの実質的な柱ね。\x02",
        )
    )

    CloseMessageWindow()

    #A0076
    AnonymousTalk(
        0x103,
        (
            "#0200Fええ、特に\x01",
            "金融・建設・不動産業界では\x01",
            "無くてはならない存在と聞きます。\x02\x03",

            "#0203Fクロスベルで進められている\x01",
            "大きな公共事業計画……\x02\x03",

            "ジオフロントや導力ネットワークの整備にも\x01",
            "ＩＢＣの資本が投入されているそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #A0077
    AnonymousTalk(
        0x104,
        (
            "#0305Fはー……\x01",
            "なんか俺には縁遠い場所みてぇだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-1890, 2500, -27740, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(10800, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    TurnDirection(0x103, 0x104, 500)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    #C0078
    ChrTalk(
        0x103,
        (
            "#0200F#11P……あの、ランディさん。\x01",
            "わたしたちのお給料も\x01",
            "ＩＢＣの口座振込みですよ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0079
    ChrTalk(
        0x104,
        "#0301F#6Pな……そうだったのかよ！？\x02",
    )

    CloseMessageWindow()

    def lambda_1E76():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E76)
    Sleep(50)
    TurnDirection(0x101, 0x103, 500)

    #C0080
    ChrTalk(
        0x101,
        (
            "#0000F#5Pクロスベル市内だと\x01",
            "そっちの方が便利なんだよな。\x02\x03",

            "#0006Fでも……\x01",
            "今日は休みみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        (
            "#0104F#11Pまあ、週末は休行日だから……\x02\x03",

            "#0100Fまた今度\x01",
            "立ち寄ってみることにしましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -970, 0, -25140, 0)
    SetScenarioFlags(0x47, 4)
    EventEnd(0x5)
    Return()

    # Function_7_1A43 end

    def Function_8_1F62(): pass

    label("Function_8_1F62")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02300.itc", 0x1E)
    LoadChrToIndex("chr/ch06000.itc", 0x1F)
    OP_68(0, -1000, -34200, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15000, 0)
    OP_90(0x101, -650, -1700, -37200, 0)
    OP_90(0x102, 650, -1700, -37200, 0)
    OP_90(0x103, -1200, -1900, -38400, 0)
    OP_90(0x104, 1200, -1900, -38400, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 0, -10500, 180)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 0, 0, -12500, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02600.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    ClearMapFlags(0x10000000)

    def lambda_2092():
        OP_96(0xFE, 0xFFFFFD76, 0x0, 0xFFFF9D90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2092)
    Sleep(200)

    def lambda_20AF():
        OP_96(0xFE, 0x28A, 0x0, 0xFFFF9D90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20AF)
    Sleep(100)

    def lambda_20CC():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0xFFFF98E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20CC)
    Sleep(200)

    def lambda_20E9():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFF98E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20E9)
    OP_68(0, 4700, -17700, 8000)
    MoveCamera(0, -9, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(13000, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x41)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2209")

    #C0082
    ChrTalk(
        0x104,
        (
            "#0305FここがＩＢＣビルか……\x02\x03",

            "#0302Fこうして間近で見てみると\x01",
            "すげえ建物だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        (
            "#0204F……そうですね。\x02\x03",

            "#0202Fこれだけ先進的なビルは\x01",
            "大陸でも少ないかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x53, 2)
    Jump("loc_2240")

    label("loc_2209")


    #C0084
    ChrTalk(
        0x104,
        (
            "#0302FＩＢＣビルか……\x01",
            "何度見てもすげぇビルだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2240")


    #C0085
    ChrTalk(
        0x101,
        (
            "#0002F#5Pこうして見ると……\x01",
            "余裕で１０階以上あるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        (
            "#0104F#11Pたしか１６階建てのはずよ。\x02\x03",

            "#0100Fそのうち、５階から１０階までは\x01",
            "外部の会社が入っているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#0000F#5Pそうなのか……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        (
            "#0204Fクロスベル市の税収に\x01",
            "相当、貢献していそうですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1000, -25800, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0089
    ChrTalk(
        0x101,
        (
            "#6P#0001Fそれで、どうするんだ？\x02\x03",

            "アポイントもなしに\x01",
            "来ちゃったけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    #C0090
    ChrTalk(
        0x102,
        (
            "#11P#0101Fそうね、まずは中の\x01",
            "受付で聞いてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    #N0091
    NpcTalk(
        0xA,
        "男性の声",
        "エリィ……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_249A():
        OP_95(0xFE, 0, 0, -22600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_249A)
    Sleep(1000)

    def lambda_24B7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_24B7)

    def lambda_24C4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24C4)
    OP_68(0, 1000, -24000, 3000)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)

    #C0092
    ChrTalk(
        0x102,
        "#0105Fアーネストさん……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0093
    AnonymousTalk(
        0xA,
        (
            "奇遇だな……\x01",
            "こんな所で会うなんて。\x02\x03",

            "みんな一緒ということは\x01",
            "警察の用事で来たのかい？\x02",
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

    #C0094
    ChrTalk(
        0x102,
        (
            "#0104Fええ……\x01",
            "少し調べる事がありまして。\x02\x03",

            "#0100Fアーネストさんは\x01",
            "おじいさまの御用ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "#2604F#5Pああ、事務所の運営資金の\x01",
            "管理についての相談をね。\x02\x03",

            "#2600F来月から特に忙しくなるし\x01",
            "色々やりくりが大変なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        "#0108F……そうですか。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        (
            "#2603F#5Pそれで、エリィ……\x02\x03",

            "#2601F少しは考えてくれたかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#0103F…………はい。\x02\x03",

            "#0101Fやはり、今警察を\x01",
            "辞めるわけにはいきません。\x02\x03",

            "私はまだ何も掴めていない……\x02\x03",

            "少なくとも、その何かが掴めるまでは\x01",
            "半人前だと思いますから。\x02\x03",

            "#0103F却っておじいさまの足を\x01",
            "引っ張ってしまうと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "#2605F#5Pだが……\x02\x03",

            "#2601F君が求めているものは\x01",
            "本当にその道の先にあるのかい？\x02\x03",

            "ひょっとしたらそれは\x01",
            "ただの蜃気楼かもしれないぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#0106Fそうかもしれません。\x02\x03",

            "#0102Fでも、この２ヶ月……\x01",
            "色々見えてきたことがあります。\x02\x03",

            "一つ一つの問題を解決することで\x01",
            "少しずつ成長できた実感もあります。\x02\x03",

            "#0109F多分、あのまま事務所に入って\x01",
            "おじいさまの秘書の１人になっていたら\x01",
            "手に入らなかった貴重な経験です。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        "#2605F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#0104F……ですから、ごめんなさい。\x02\x03",

            "#0100F少なくとも一人前になるまで……\x01",
            "今の立場で頑張りたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "#2606F#5P……ふう。\x02\x03",

            "#2600Fどうやら迷いが消えたようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        "#0105Fえ……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "#2600F#5Pわかった、もう何も言わないよ。\x02\x03",

            "#2604Fやれやれ、せっかく事務所に\x01",
            "有能な後輩が入ると思ったんだが。\x02\x03",

            "当てが外れてしまったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        "#0102Fアーネストさん……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "#2603F#5Pただ、そうだな……\x02\x03",

            "#2600F来月の創立記念祭の時には\x01",
            "式典にぜひ出席して欲しい。\x02\x03",

            "本来なら、君のお母様に\x01",
            "出ていただきたかったんだが……\x02\x03",

            "さすがに、市長のご家族が一人も\x01",
            "出席しないのは寂しいからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#0104F……分かりました。\x02\x03",

            "#0100Fアーネストさん。\x01",
            "色々とありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        (
            "#2604F#5Pはは、いちおう君の\x01",
            "先生だったこともあるしね。\x02\x03",

            "#2600Fこれくらいは気にかけさせてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0110
    ChrTalk(
        0xA,
        (
            "#2605F#5Pおっと、こんな場所で\x01",
            "時間を取らせてしまったな。\x02\x03",

            "#2604F君たちも、お仕事頑張ってくれ。\x02\x03",

            "#2600Fそれと……\x01",
            "エリィお嬢さんを頼んだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#12P#0002F……はい。\x02",
    )

    CloseMessageWindow()

    def lambda_2D4A():

        label("loc_2D4A")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_2D4A")

    QueueWorkItem2(0x101, 2, lambda_2D4A)

    def lambda_2D5C():

        label("loc_2D5C")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_2D5C")

    QueueWorkItem2(0x102, 2, lambda_2D5C)

    def lambda_2D6E():
        OP_95(0xFE, -1900, 0, -24200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2D6E)
    Sleep(500)

    def lambda_2D8B():

        label("loc_2D8B")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_2D8B")

    QueueWorkItem2(0x104, 2, lambda_2D8B)

    def lambda_2D9D():

        label("loc_2D9D")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_2D9D")

    QueueWorkItem2(0x103, 2, lambda_2D9D)
    WaitChrThread(0xA, 1)
    OP_68(0, 1000, -27000, 3000)

    def lambda_2DC4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD120, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2DC4)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)
    EndChrThread(0x101, 0x2)

    def lambda_2DE8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2DE8)
    Sleep(50)
    EndChrThread(0x102, 0x2)

    def lambda_2DFC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2DFC)
    EndChrThread(0x103, 0x2)

    def lambda_2E0D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2E0D)
    Sleep(50)
    EndChrThread(0x104, 0x2)

    def lambda_2E21():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2E21)
    WaitChrThread(0x104, 2)
    ClearChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    #C0112
    ChrTalk(
        0x102,
        "#5P#0108F………………………………\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, -25800, 1000)

    def lambda_2E79():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E79)
    Sleep(150)

    def lambda_2E89():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2E89)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)
    OP_6F(0x1)

    #C0113
    ChrTalk(
        0x101,
        (
            "#6P#0000F随分、エリィのことを\x01",
            "考えてくれている人みたいだな。\x02\x03",

            "先生をしてたとか言ってたけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(150)

    #C0114
    ChrTalk(
        0x102,
        (
            "#5P#0102Fええ……私が小さい頃に\x01",
            "家庭教師をしてくれていたの。\x02\x03",

            "#0104F留学してからはちょっと\x01",
            "疎遠になってしまっていたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#6P#0200F……やっぱり\x01",
            "政治家志望なんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        (
            "#5P#0100Fええ、来年の議員選挙では\x01",
            "新人として出馬するみたいね。\x02\x03",

            "#0108F帝国派と共和国派のどちらにも\x01",
            "属さないつもりらしいから\x01",
            "とても苦労すると思うけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        (
            "#12P#0303F政治家の卵ってわけか。\x02\x03",

            "#0300Fしかし、政治家の秘書にしちゃ\x01",
            "結構いいガタイをしてたよな。\x02\x03",

            "なんか武術でもやってんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#5P#0105Fたしか剣術の経験があるはずよ。\x02\x03",

            "#0100F結構な腕前みたいだから\x01",
            "おじいさまの護衛も兼ねてるって\x01",
            "聞いたことがあるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#6P#0000Fなるほど……\x01",
            "体格がいいのも納得だな。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)

    #N0120
    NpcTalk(
        0xB,
        "女性の声",
        "おやおや～？\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_3215():
        OP_95(0xFE, 0, 0, -22600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3215)
    Sleep(1000)
    OP_68(0, 1000, -24000, 3000)

    def lambda_3243():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3243)
    Sleep(50)

    def lambda_3253():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3253)
    Sleep(50)

    def lambda_3263():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3263)
    Sleep(50)

    def lambda_3273():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3273)
    WaitChrThread(0xB, 1)
    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 3)), scpexpr(EXPR_END)), "loc_338F")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0121
    AnonymousTalk(
        0xB,
        "うふふん、また会ったわね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0122
    ChrTalk(
        0x101,
        "#12P#0005Fグレイスさん……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "#2105F#5Pなに、ＩＢＣに用事？\x02\x03",

            "#2102F一緒に来てるってことは\x01",
            "捜査にでも来たのかしらん？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3678")

    label("loc_338F")

    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0124
    AnonymousTalk(
        0xB,
        (
            "いや～、久しぶりねぇ。\x02\x03",

            "先月の魔獣騒ぎの件、\x01",
            "読ませてもらったわよん？\x02\x03",

            "うんうん。\x01",
            "頑張ってるみたいじゃない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0125
    ChrTalk(
        0x101,
        "#12P#0005Fグレイスさん……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#0100Fそういえば、あの記事は\x01",
            "グレイスさんでは無かったんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        (
            "#2106F#5Pうん、取材があって\x01",
            "クロスベルを離れててね。\x02\x03",

            "#2102F出来れば君たちの取材は\x01",
            "あたしがしたかったんだけどなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        "#12P#0206F……結果的に正解かと。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        (
            "#0302Fま、いつもあの調子だと\x01",
            "こっちもヘコむッスからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "#2104F#5Pやれやれ、君たちの成長を見守る\x01",
            "あたしの深い愛情が分からないかな～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0131
    ChrTalk(
        0xB,
        (
            "#2105F#5Pそれはそうと……\x01",
            "ＩＢＣに何か用事？\x02\x03",

            "#2102F一緒に来てるってことは\x01",
            "捜査にでも来たのかしらん？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3678")


    #C0132
    ChrTalk(
        0x101,
        (
            "#12P#0012Fい、いや別に……\x01",
            "大したことじゃないですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        (
            "#0100Fええ、ちょっとした\x01",
            "問い合わせに来ただけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        (
            "#2101F#5Pふーん……ま、いっか。\x02\x03",

            "#2104Fあたしも忙しいから\x01",
            "この場は見逃してあげる。\x02\x03",

            "#2110Fそれじゃあ、まったね～！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3769():

        label("loc_3769")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_3769")

    QueueWorkItem2(0x101, 2, lambda_3769)

    def lambda_377B():

        label("loc_377B")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_377B")

    QueueWorkItem2(0x102, 2, lambda_377B)

    def lambda_378D():
        OP_95(0xFE, 1900, 0, -24200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_378D)
    Sleep(500)

    def lambda_37AA():

        label("loc_37AA")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_37AA")

    QueueWorkItem2(0x104, 2, lambda_37AA)

    def lambda_37BC():

        label("loc_37BC")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_37BC")

    QueueWorkItem2(0x103, 2, lambda_37BC)
    WaitChrThread(0xB, 1)
    OP_68(0, 1000, -27000, 3000)

    def lambda_37E3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD120, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_37E3)
    WaitChrThread(0xB, 1)
    OP_6F(0x1)
    EndChrThread(0x104, 0x2)

    def lambda_3807():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3807)
    Sleep(50)
    EndChrThread(0x102, 0x2)

    def lambda_381B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_381B)
    EndChrThread(0x103, 0x2)

    def lambda_382C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_382C)
    Sleep(50)
    EndChrThread(0x101, 0x2)

    def lambda_3840():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3840)
    WaitChrThread(0x101, 2)
    ClearChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_68(0, 1000, -25800, 1000)
    OP_6F(0x1)

    #C0135
    ChrTalk(
        0x104,
        (
            "#0306F#5Pやれやれ、相変わらず\x01",
            "マイペースな姉さんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x103,
        (
            "#6P#0200Fでも、グレイスさんにしては\x01",
            "喰い付きが悪かったですね……\x02\x03",

            "そんなに忙しいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        (
            "#5P#0100Fまあ、記念祭の前ともなると\x01",
            "取材する事も多いんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#5P#0006Fうーん、できればこっちの記事も\x01",
            "諦めてくれるといいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(150)

    #C0139
    ChrTalk(
        0x101,
        (
            "#6P#0000Fまあいい……\x01",
            "そろそろビルに入ろう。\x02\x03",

            "総裁に面会できないか\x01",
            "受付で問い合わせてみないとな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A18():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3A18)
    Sleep(50)

    def lambda_3A28():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3A28)
    Sleep(50)

    def lambda_3A38():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A38)
    Sleep(150)

    #C0140
    ChrTalk(
        0x102,
        "#11P#0102Fええ、行きましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(0, 2500, -24000, 0)
    MoveCamera(45, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, 0, 0, -24000, 0)
    SetChrPos(0x1, 0, 0, -24000, 0)
    SetChrPos(0x2, 0, 0, -24000, 0)
    SetChrPos(0x3, 0, 0, -24000, 0)
    SetScenarioFlags(0x82, 1)
    OP_29(0x43, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_8_1F62 end

    def Function_9_3AFB(): pass

    label("Function_9_3AFB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1100, 10800, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29500, 0)
    SetChrPos(0x101, 0, 400, 8500, 180)
    SetChrPos(0x102, 700, 400, 8500, 180)
    SetChrPos(0x103, -700, 400, 8500, 180)
    SetChrPos(0x104, 0, 400, 8500, 180)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_68(0, 1100, 1800, 4000)
    MoveCamera(0, 25, 0, 4000)
    SetCameraDistance(19500, 4000)

    def lambda_3BFE():
        OP_96(0xFE, 0x0, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3BFE)

    def lambda_3C18():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3C18)
    Sleep(500)

    def lambda_3C2C():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C2C)

    def lambda_3C46():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3C46)
    Sleep(400)

    def lambda_3C5A():
        OP_96(0xFE, 0x384, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C5A)

    def lambda_3C74():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3C74)
    Sleep(500)

    def lambda_3C88():
        OP_96(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C88)

    def lambda_3CA2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CA2)
    Sleep(1500)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x104, 1)

    def lambda_3CD5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3CD5)
    WaitChrThread(0x103, 1)

    def lambda_3CE6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3CE6)
    WaitChrThread(0x102, 1)

    def lambda_3CF7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3CF7)
    WaitChrThread(0x101, 1)

    #C0141
    ChrTalk(
        0x101,
        (
            "#5P#0006Fはあ……\x02\x03",

            "手がかりが入ったのはいいけど\x01",
            "何だかどっと疲れたな……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        (
            "#6P#0309Fはは、そうだな。\x02\x03",

            "#0302F特にロイドは、あのお嬢様に\x01",
            "さんざん絡まれてたからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#5P#0001F誰のせいだよ、誰の……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        (
            "#0202Fでも、専門ではない導力技術に\x01",
            "あそこまで通じてる人は珍しいです。\x02\x03",

            "マリアベルさんは\x01",
            "技術者ではないんですよね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#0104Fええ、経営の方が専門ね。\x02\x03",

            "#0100Fおじさまの右腕として\x01",
            "幾つかの事業を任されていると\x01",
            "聞いたことがあるけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(150)

    #C0146
    ChrTalk(
        0x101,
        (
            "#5P#0000Fそれは凄いな……\x02\x03",

            "#0005Fああ、ひょっとしてそれで\x01",
            "エリィを欲しがっているのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        (
            "#0106Fう、うん……\x01",
            "気持ちはありがたいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x104,
        (
            "#6P#0306Fしかし、あの親父さんの方も\x01",
            "相当強烈な感じだったよな。\x02\x03",

            "#0301Fいきなり凄い演説みたいなのを\x01",
            "始めちまうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x103,
        (
            "#0203Fでも……\x01",
            "なかなか興味深い話でした。\x02\x03",

            "#0201F人は正義を求める生き物ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#0104F昔から、ためになる話を\x01",
            "よくしてくださったけど……\x02\x03",

            "#0100F今日の話はとりわけ、\x01",
            "考えさせられてしまったかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#5P#0003F……そうだな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)
    TurnDirection(0x101, 0x104, 500)

    #C0152
    ChrTalk(
        0x101,
        (
            "#0000F#5P──ともかく、\x01",
            "これで手がかりは掴めた。\x02\x03",

            "市庁舎の受付に頼んで\x01",
            "ジオフロントの鍵を借りよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x102,
        "#0102Fええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        "#6P#0302Fそんじゃ、行くとするか。\x02",
    )

    CloseMessageWindow()

    def lambda_4197():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4197)
    Sleep(100)

    def lambda_41A7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_41A7)
    Sleep(50)

    def lambda_41B7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_41B7)
    WaitChrThread(0x104, 2)
    OP_68(0, 1100, -4200, 3000)

    def lambda_41D9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_41D9)
    Sleep(150)
    WaitChrThread(0x103, 2)

    def lambda_41FA():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_41FA)
    Sleep(150)
    WaitChrThread(0x102, 2)

    def lambda_421B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_421B)
    Sleep(150)

    def lambda_4238():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4238)
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_6F(0x1)
    OP_93(0x101, 0x0, 0x12C)
    Fade(500)
    OP_68(0, 1100, -2200, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13000, 0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 2200, -2200, 1500)
    MoveCamera(0, 0, 0, 1500)
    OP_6F(0x41)
    Sleep(500)

    #C0155
    ChrTalk(
        0x101,
        (
            "#0001F#6P#N（……………………………………）\x02\x03",

            "#0003F（……《正義》か……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x190)

    def lambda_4338():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4338)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x104, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x101, 0x1)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(0, 2500, -10000, 0)
    MoveCamera(45, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, 0, 0, -10000, 180)
    SetChrPos(0x1, 0, 0, -10000, 180)
    SetChrPos(0x2, 0, 0, -10000, 180)
    SetChrPos(0x3, 0, 0, -10000, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetScenarioFlags(0x83, 1)
    Sleep(10)
    PlayBGM("ed7102", 0)
    EventEnd(0x5)
    Return()

    # Function_9_3AFB end

    def Function_10_4423(): pass

    label("Function_10_4423")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ｉ．Ｂ．Ｃ\x01",
            "International Bank of Crossbell\x01\x01",
            " 入居各社にお問い合わせの方は\x01",
            " １階ロビーカウンターにて\x01",
            " 声をおかけ下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_4423 end

    SaveToFile()

Try(main)
