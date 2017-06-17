from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1040.bin",                # FileName
        "c1040",                    # MapName
        "c1040",                    # Location
        0x0015,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 21, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1040",                  # 0
        "マーシー",               # 1
        "マーシー",               # 2
        "サリナ",                 # 3
        "ユゴット",               # 4
        "クラリス",               # 5
        "アゼル",                 # 6
        "エステル",               # 7
        "エステル",               # 8
        "ヨシュア",               # 9
        "フラン",                 # 10
    ))

    AddCharChip((
        "chr/ch21800.itc",                   # 00
        "chr/ch20500.itc",                   # 01
        "chr/ch34200.itc",                   # 02
        "chr/ch10400.itc",                   # 03
        "apl/ch50375.itc",                   # 04
        "chr/ch21802.itc",                   # 05
        "chr/ch00600.itc",                   # 06
        "chr/ch00602.itc",                   # 07
        "chr/ch00702.itc",                   # 08
        "chr/ch08500.itc",                   # 09
    ))

    DeclNpc(48880,   29,      -55000,  135,  261,  0x0, 0,   0,   0,   0,   2,   0,   6,   255,  0)
    DeclNpc(46400,   29,      -53479,  270,  389,  0x0, 0,   5,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(3789,    0,       55279,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-2410,   29,      52169,   225,  261,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(3660,    29,      -56599,  90,   261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(1029,    29,      55659,   90,   405,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(53740,   0,       51459,   90,   405,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(52040,   150,     53650,   270,  469,  0x0, 0,   7,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(49200,   150,     53560,   90,   469,  0x0, 0,   8,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-400,    29,      -53770,  135,  389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)

    DeclActor(51690,   0,       5670,    1200,    51690,   1500,    5670,    0x007C, 0,  22, 0x0000)
    DeclActor(-4890,   0,       -52820,  1200,    -4890,   1500,    -52820,  0x007C, 0,  23, 0x0000)

    ScpFunction((
        "Function_0_27C",          # 00, 0
        "Function_1_334",          # 01, 1
        "Function_2_35F",          # 02, 2
        "Function_3_38A",          # 03, 3
        "Function_4_3B5",          # 04, 4
        "Function_5_647",          # 05, 5
        "Function_6_6E8",          # 06, 6
        "Function_7_15CD",         # 07, 7
        "Function_8_17CE",         # 08, 8
        "Function_9_25E8",         # 09, 9
        "Function_10_2CDA",        # 0A, 10
        "Function_11_4276",        # 0B, 11
        "Function_12_4319",        # 0C, 12
        "Function_13_44A8",        # 0D, 13
        "Function_14_452E",        # 0E, 14
        "Function_15_459C",        # 0F, 15
        "Function_16_47C1",        # 10, 16
        "Function_17_4B84",        # 11, 17
        "Function_18_513F",        # 12, 18
        "Function_19_520D",        # 13, 19
        "Function_20_58C1",        # 14, 20
        "Function_21_5F29",        # 15, 21
        "Function_22_653D",        # 16, 22
        "Function_23_66C3",        # 17, 23
    ))


    def Function_0_27C(): pass

    label("Function_0_27C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2BC"),
        (1, "loc_2C8"),
        (2, "loc_2D4"),
        (3, "loc_2E0"),
        (4, "loc_2EC"),
        (5, "loc_2F8"),
        (6, "loc_304"),
        (SWITCH_DEFAULT, "loc_310"),
    )


    label("loc_2BC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2C8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2D4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2E0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2EC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2F8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_304")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_310")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_31C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_333")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_333")

    Return()

    # Function_0_27C end

    def Function_1_334(): pass

    label("Function_1_334")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35E")
    OP_94(0xFE, 0xFFFFF204, 0xCD3C, 0xFFFFFA24, 0xC602, 0x3E8)
    Sleep(300)
    Jump("Function_1_334")

    label("loc_35E")

    Return()

    # Function_1_334 end

    def Function_2_35F(): pass

    label("Function_2_35F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_389")
    OP_94(0xFE, 0xBC16, 0xFFFF213A, 0xBDCE, 0xFFFF2FB8, 0x3E8)
    Sleep(300)
    Jump("Function_2_35F")

    label("loc_389")

    Return()

    # Function_2_35F end

    def Function_3_38A(): pass

    label("Function_3_38A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B4")
    OP_94(0xFE, 0xFFFFFC90, 0xFFFF2F04, 0xFFFFF6F0, 0xFFFF263A, 0x3E8)
    Sleep(300)
    Jump("Function_3_38A")

    label("loc_3B4")

    Return()

    # Function_3_38A end

    def Function_4_3B5(): pass

    label("Function_4_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3C3")
    Jump("loc_646")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3D1")
    Jump("loc_646")

    label("loc_3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_40D")
    SetChrPos(0xA, 2500, 30, 55660, 270)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_408")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_408")

    Jump("loc_646")

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_420")
    SetChrFlags(0xB, 0x80)
    Jump("loc_646")

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_46F")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 3790, 0, 55280, 180)
    SetChrPos(0xB, 3990, 30, 54010, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_646")

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_487")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_646")

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_49F")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_646")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4B7")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_646")

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4C5")
    Jump("loc_646")

    label("loc_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrPos(0xB, 2590, 30, 55740, 135)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_646")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_520")
    SetChrPos(0xA, 3790, 0, 55280, 180)
    SetChrPos(0xB, 3990, 30, 54010, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_646")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_55B")
    SetChrPos(0xA, 3790, 0, 55280, 180)
    SetChrPos(0xB, 3990, 30, 54010, 0)
    SetChrFlags(0xA, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_646")

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_59B")
    SetChrPos(0xA, 3790, 0, 55280, 180)
    SetChrPos(0xB, 3990, 30, 54010, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_646")

    label("loc_59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5B3")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_646")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5DD")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, -1120, 30, -53900, 225)
    BeginChrThread(0xB, 0, 0, 3)
    Jump("loc_646")

    label("loc_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5EB")
    Jump("loc_646")

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5F9")
    Jump("loc_646")

    label("loc_5F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_622")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61D")
    SetChrFlags(0x8, 0x80)

    label("loc_61D")

    Jump("loc_646")

    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_646")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_646")
    SetChrFlags(0x8, 0x80)

    label("loc_646")

    Return()

    # Function_4_3B5 end

    def Function_5_647(): pass

    label("Function_5_647")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_660")
    OP_10(0x0, 0x0)
    OP_10(0xB, 0x1)
    Jump("loc_666")

    label("loc_660")

    OP_10(0x0, 0x1)
    OP_10(0xB, 0x0)

    label("loc_666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_682")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_699")

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_699")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_699")

    label("loc_699")

    OP_65(0x0, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BB")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_6BB")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D5")
    OP_66(0x1, 0x1)

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E7")
    OP_66(0x1, 0x1)

    label("loc_6E7")

    Return()

    # Function_5_647 end

    def Function_6_6E8(): pass

    label("Function_6_6E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_77C")

    #C0001
    ChrTalk(
        0xFE,
        (
            "うちのお向かいさんは\x01",
            "半月ほど前に引っ越されてね。\x01",
            "今は空家になっているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "そういえば……結構\x01",
            "適当な性格の人だったなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C9")

    label("loc_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7F6")

    #C0003
    ChrTalk(
        0xFE,
        (
            "そういえば……\x01",
            "予算議会はどうなったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "予算がどう回されるかで\x01",
            "株価にもかなり影響がありそうだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C9")

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_87A")

    #C0005
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズは……\x01",
            "そうか、明日だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "うーむ、臨時休刊なんてするから\x01",
            "ちょっと調子が狂っちゃうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C9")

    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8FF")

    #C0007
    ChrTalk(
        0xFE,
        (
            "港湾区で大きな事件が\x01",
            "あったそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "港湾区って言ったら\x01",
            "通りを通ってすぐの場所だろ？\x01",
            "ぶ、物騒だな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C9")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DC")

    #C0009
    ChrTalk(
        0xFE,
        (
            "贈っていた記念祭の写真が\x01",
            "家族の元に届いたらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "通信で子供たちにありがとー、\x01",
            "なんて言われてしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "……ぐすっ。\x01",
            "久しぶりに話すとなんかこう……\x01",
            "里心がついていけないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A44")

    label("loc_9DC")


    #C0012
    ChrTalk(
        0xFE,
        (
            "いかんいかん、ホームシックに\x01",
            "なってる場合じゃないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "単身赴任、\x01",
            "しっかりやり遂げないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A44")

    Jump("loc_15C9")

    label("loc_A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A57")
    Jump("loc_15C9")

    label("loc_A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF4")

    #C0014
    ChrTalk(
        0xFE,
        (
            "おっと、オーバルカメラの\x01",
            "導力が切れてしまっているな。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "花火を撮影しなきゃいかんのだが……\x01",
            "まぁ、夜までには元に戻るかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B3C")

    label("loc_AF4")


    #C0016
    ChrTalk(
        0xFE,
        (
            "導力器の導力は\x01",
            "しばらく経つと回復する。\x01",
            "やっぱりとても便利だよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3C")

    Jump("loc_15C9")

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_BBA")

    #C0017
    ChrTalk(
        0xFE,
        "パレードは素晴らしかったよ……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "カメラを使うのは初めてだったが\x01",
            "きっといい写真が撮れたに違いない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C9")

    label("loc_BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3C")

    #C0019
    ChrTalk(
        0xFE,
        (
            "パレードの写真を撮って\x01",
            "家族に見せてやると約束したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "い、急いで仕事を終わらせないと……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C71")

    label("loc_C3C")


    #C0021
    ChrTalk(
        0xFE,
        (
            "ああ、急がないと\x01",
            "パレードが始まってしまう……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C71")

    Jump("loc_15C9")

    label("loc_C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CD5")

    #C0022
    ChrTalk(
        0xFE,
        "本社から急に指示が入ったんだ。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "とほほ、今日は\x01",
            "出かけられそうに無いよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C9")

    label("loc_CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D36")

    #C0024
    ChrTalk(
        0xFE,
        "よし、財布は持ったと……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "……できれば帝国に居る家族と\x01",
            "回りたかったなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C9")

    label("loc_D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_DA6")

    #C0026
    ChrTalk(
        0xFE,
        (
            "ふむ……来月は\x01",
            "休暇が取れるのだろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "創立記念祭はできれば\x01",
            "家族と回りたいところだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C9")

    label("loc_DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_F09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E80")

    #C0028
    ChrTalk(
        0xFE,
        (
            "ＩＢＣグループの\x01",
            "証券会社は世界最大手だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "わが社にとっては\x01",
            "ライバルだが……\x01",
            "実は頼っている点もある。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "証券の持ち合いといってね、\x01",
            "わが社の証券の一部を\x01",
            "預かってもらっているんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F04")

    label("loc_E80")


    #C0031
    ChrTalk(
        0xFE,
        (
            "ＩＢＣグループの証券会社は\x01",
            "わが社の最大のライバルだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "しかし頼っている面もあるんだよ。\x01",
            "世の中も争いばかりではないからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F04")

    Jump("loc_15C9")

    label("loc_F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_103B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC4")

    #C0033
    ChrTalk(
        0xFE,
        (
            "最近事件が多いせいか\x01",
            "株価の動きが思わしくないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "事件現場になった貸倉庫会社なんて\x01",
            "随分と値を下げてしまった……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "巻き込まれる会社も気の毒だな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1036")

    label("loc_FC4")


    #C0036
    ChrTalk(
        0xFE,
        (
            "最近事件が多いせいか\x01",
            "株価の動きが思わしくないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "まあすぐに戻るだろうが\x01",
            "巻き込まれる会社も気の毒だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1036")

    Jump("loc_15C9")

    label("loc_103B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_10F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CC")

    #C0038
    ChrTalk(
        0xFE,
        (
            "たまには休暇を取って\x01",
            "家族に会いに帰りたい所だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "わが社は証券会社だ、\x01",
            "なかなか休暇など取れそうもないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10F2")

    label("loc_10CC")


    #C0040
    ChrTalk(
        0xFE,
        "ふむ、単身赴任のつらい所だな……\x02",
    )

    CloseMessageWindow()

    label("loc_10F2")

    Jump("loc_15C9")

    label("loc_10F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_11A2")

    #C0041
    ChrTalk(
        0xFE,
        (
            "マインツで採掘される七耀石#6Rセプチウム#の\x01",
            "取引価格が微落しているな……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "むむ、これはわが社の相場にも\x01",
            "影響がある取引だ。\x01",
            "原因を調べておかないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C9")

    label("loc_11A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1220")

    #C0043
    ChrTalk(
        0xFE,
        (
            "表通りの喧騒が\x01",
            "気になって昼寝ができないぞ……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "このアパルトメント、\x01",
            "やっぱり壁が薄いのではないかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C9")

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_137A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FC")

    #C0045
    ChrTalk(
        0xFE,
        (
            "最近お隣に\x01",
            "引っ越してきた若者がいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "一度挨拶したが、\x01",
            "ツインテールの娘と\x01",
            "黒髪の青年だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "確か遊撃士をしているって\x01",
            "言っていたなぁ。\x01",
            "さすがにハキハキした子たちだったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1375")

    label("loc_12FC")


    #C0048
    ChrTalk(
        0xFE,
        (
            "最近お隣に\x01",
            "引っ越してきた若者がいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "ツインテールの元気な子と\x01",
            "黒髪の青年でね、\x01",
            "遊撃士をしているそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1375")

    Jump("loc_15C9")

    label("loc_137A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_14B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1446")

    #C0050
    ChrTalk(
        0xFE,
        (
            "クロスベルでの相場の動きを\x01",
            "詳細に調べるのが自分の仕事だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "クロスベルには周辺諸国の\x01",
            "情報が流れ込んでくるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "証券会社にとって\x01",
            "情報は何より大切なものだからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14AC")

    label("loc_1446")


    #C0053
    ChrTalk(
        0xFE,
        (
            "ふむふむ、共和国の方じゃ\x01",
            "天候不順が続いたのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "相場の動きと纏めて\x01",
            "本社に報告しないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14AC")

    Jump("loc_15C9")

    label("loc_14B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_15C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1567")

    #C0055
    ChrTalk(
        0xFE,
        (
            "自分はエレボニア帝国で\x01",
            "証券会社に勤めていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "このたび本場のクロスベルに\x01",
            "単身赴任してきたのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "やはり現地の方が\x01",
            "何かと便利だからねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15C9")

    label("loc_1567")


    #C0058
    ChrTalk(
        0xFE,
        (
            "ふむ、しかし……\x01",
            "この辺りは何でも東方風だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "帝国人としては\x01",
            "物珍しくて仕方がないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C9")

    TalkEnd(0xFE)
    Return()

    # Function_6_6E8 end

    def Function_7_15CD(): pass

    label("Function_7_15CD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1661")
    Jump("loc_16AB")

    label("loc_1661")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1681")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16AB")

    label("loc_1681")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16AB")

    label("loc_16A1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16AB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_17C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176F")

    #C0060
    ChrTalk(
        0xFE,
        (
            "記念祭で撮った写真を\x01",
            "これから帝国の家族に送るんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "とても見ごたえのある写真が撮れた。\x01",
            "これなら子供たちも喜んでくれるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17C6")

    label("loc_176F")


    #C0062
    ChrTalk(
        0xFE,
        (
            "そうだ、手紙を添えるのを\x01",
            "すっかり忘れていたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        "えーと、お元気ですか、と……\x02",
    )

    CloseMessageWindow()

    label("loc_17C6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_15CD end

    def Function_8_17CE(): pass

    label("Function_8_17CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188D")

    #C0064
    ChrTalk(
        0xFE,
        (
            "テスタメンツの印象も\x01",
            "昔とは大分変わりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "今度ユゴットと一緒に、\x01",
            "アゼルの職場に食べに行って\x01",
            "みようと思っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        "……あの子には内緒ですよ？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18FB")

    label("loc_188D")


    #C0067
    ChrTalk(
        0xFE,
        (
            "今度ユゴットと一緒に、\x01",
            "アゼルの職場に食べに行って\x01",
            "みようと思っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        "……あの子には内緒ですよ？\x02",
    )

    CloseMessageWindow()

    label("loc_18FB")

    Jump("loc_25E4")

    label("loc_1900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_199D")

    #C0069
    ChrTalk(
        0xFE,
        (
            "アゼルが働くようになって、\x01",
            "なんだか家族がうまく\x01",
            "噛みあっている気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "生活はまだ苦しいけど……\x01",
            "この調子ならやっていけそうです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E4")

    label("loc_199D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1AC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A68")
    OP_4B(0xD, 0xFF)

    #C0071
    ChrTalk(
        0xFE,
        "うん、こっちは平気よ。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……それで急いで帰ってきてくれたの？\x01",
            "ふふ、アゼルも可愛いところがあるのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xD,
        (
            "あのね……\x01",
            "本気で心配したんだから\x01",
            "茶化すなって。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ABB")

    label("loc_1A68")


    #C0074
    ChrTalk(
        0xFE,
        (
            "アゼルが昨夜の事件を心配して\x01",
            "帰ってきてくれてるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "……嬉しいです。\x02",
    )

    CloseMessageWindow()

    label("loc_1ABB")

    Jump("loc_25E4")

    label("loc_1AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B42")

    #C0076
    ChrTalk(
        0xFE,
        (
            "今日はユゴットは\x01",
            "日曜学校に行ってるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "家で一人でお留守番させるのは\x01",
            "心配ですから、助かっていますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E4")

    label("loc_1B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1BB1")

    #C0078
    ChrTalk(
        0xFE,
        (
            "じゃあユゴット、\x01",
            "お姉ちゃんお仕事に行ってくるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        "いい子にしてお留守番しているのよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25E4")

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C2D")

    #C0080
    ChrTalk(
        0xFE,
        (
            "昨日、旧市街の不良グループが\x01",
            "大きな騒ぎを起こしたそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "全くあの子たちったら……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C6C")

    label("loc_1C2D")


    #C0082
    ChrTalk(
        0xFE,
        (
            "まったく……アゼルが\x01",
            "帰ってきたら怒らないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C6C")

    Jump("loc_25E4")

    label("loc_1C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D1D")

    #C0083
    ChrTalk(
        0xFE,
        (
            "アゼルったら、\x01",
            "記念祭の半分はグループの友達と\x01",
            "遊びたいんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "……テスタメンツ、だったかしら。\x01",
            "そんなに悪い人達じゃ\x01",
            "ないのかもしれないですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E4")

    label("loc_1D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1DEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB8")

    #C0085
    ChrTalk(
        0xFE,
        (
            "来月の記念祭には必ず帰ってくるよう\x01",
            "アゼルに言って来ました。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "折角の記念祭……\x01",
            "家族で過ごしたいですからね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DE5")

    label("loc_1DB8")


    #C0087
    ChrTalk(
        0xFE,
        (
            "……ふふ。\x01",
            "来月がたのしみね、ユゴット。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE5")

    Jump("loc_25E4")

    label("loc_1DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1E5E")

    #C0088
    ChrTalk(
        0xFE,
        (
            "そうね、あまり高いものは\x01",
            "買ったりできないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "久しぶりに姉弟揃って\x01",
            "ゆっくりしたいわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E4")

    label("loc_1E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1EE4")

    #C0090
    ChrTalk(
        0xFE,
        (
            "じゃ、ユゴット……\x01",
            "お姉ちゃん、お仕事行ってくるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "この間、休みをもらった分は\x01",
            "しっかり働いて返さないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E4")

    label("loc_1EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2118")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2058")

    #C0092
    ChrTalk(
        0xFE,
        (
            "不良グループに入っていた\x01",
            "弟のアゼル……旧市街で\x01",
            "アルバイトを始めたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "グループを辞めない代わりに、\x01",
            "きちんと働いて、ちゃんと家にも\x01",
            "帰ってくると約束しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "ふう……といっても仲間のバーで\x01",
            "手伝いをするだけみたいですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "まあ入院していた間の治療費は\x01",
            "責任をもって返すって言っているし……\x01",
            "しばらく様子を見てみようかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2113")

    label("loc_2058")


    #C0096
    ChrTalk(
        0xFE,
        (
            "まだアゼルが\x01",
            "不良グループにいるのは\x01",
            "心配ですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "家にも戻るようになったのは\x01",
            "少し安心しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "……やっぱり、\x01",
            "普段怒らない私が怒ったのが\x01",
            "一番効いたのかも知れませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2113")

    Jump("loc_25E4")

    label("loc_2118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_225A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_220A")

    #C0099
    ChrTalk(
        0xFE,
        (
            "旧市街に入り浸ってる弟を\x01",
            "連れ戻す為に、\x01",
            "仕事のお休みをとってきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "完全に家族の問題なのに、\x01",
            "有給で処理しておいてくれると\x01",
            "言ってくれて……助かりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "……明日は旧市街に\x01",
            "行ってみようと思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2255")

    label("loc_220A")


    #C0102
    ChrTalk(
        0xFE,
        (
            "……私、明日は\x01",
            "旧市街に行ってみます。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        "アゼルを連れ戻さなくちゃ。\x02",
    )

    CloseMessageWindow()

    label("loc_2255")

    Jump("loc_25E4")

    label("loc_225A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_23AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230C")

    #C0104
    ChrTalk(
        0xFE,
        (
            "上の弟が旧市街から\x01",
            "帰ってこないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "病院に連絡したら、\x01",
            "もう退院しているっていうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "やっぱり、私が連れ戻しに\x01",
            "行かなくっちゃ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23A9")

    label("loc_230C")


    #C0107
    ChrTalk(
        0xFE,
        (
            "生活が苦しいので、お仕事を休むのは\x01",
            "ちょっと気が引けますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "今は私が保護者なんです。\x01",
            "近いうちになんとしても\x01",
            "アゼルを連れ戻しにいかなくちゃ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A9")

    Jump("loc_25E4")

    label("loc_23AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_24E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2479")

    #C0109
    ChrTalk(
        0xFE,
        (
            "さっき病院から\x01",
            "アゼルが入院しているっていう\x01",
            "報せがありました。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "命に別状はないみたいなんですけど\x01",
            "結構な重傷みたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "あの子ったら一体\x01",
            "何をしてたのかしら……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24E2")

    label("loc_2479")


    #C0112
    ChrTalk(
        0xFE,
        (
            "私の見ていないところで\x01",
            "入院なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "アゼルったら\x01",
            "何度心配をかけさせれば\x01",
            "気が済むのかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E2")

    Jump("loc_25E4")

    label("loc_24E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_25E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_256C")

    #C0114
    ChrTalk(
        0xFE,
        (
            "上の弟は、もう\x01",
            "一週間も帰ってこないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "きっと例の不良仲間の所で\x01",
            "寝泊りしているんですね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25E4")

    label("loc_256C")


    #C0116
    ChrTalk(
        0xFE,
        (
            "上の弟は、もう一週間も\x01",
            "家に帰っていません。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "もしアゼルって子を見かけたら\x01",
            "帰るように言っておいてくれませんか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E4")

    TalkEnd(0xFE)
    Return()

    # Function_8_17CE end

    def Function_9_25E8(): pass

    label("Function_9_25E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2676")

    #C0118
    ChrTalk(
        0xFE,
        (
            "僕も、日曜学校を卒業したら\x01",
            "働くつもりだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "出来たら遊撃士になって、\x01",
            "お姉ちゃんと兄ちゃんに\x01",
            "ご馳走してあげたいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_2676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2700")

    #C0120
    ChrTalk(
        0xFE,
        "お姉ちゃん、最近嬉しそうなんだ。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "お兄ちゃんが帰るようになる前は\x01",
            "いつもツラそうだったから、\x01",
            "なんだか僕も嬉しいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_2700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2736")

    #C0122
    ChrTalk(
        0xFE,
        "兄ちゃん、今日お仕事はいいのかな？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_2736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2744")
    Jump("loc_2CD6")

    label("loc_2744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_27BC")

    #C0123
    ChrTalk(
        0xFE,
        (
            "うん、大丈夫だよ～。\x01",
            "またクラリスおばさんの\x01",
            "ところに行ってるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "お姉ちゃんもお仕事頑張ってね！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_27BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2842")

    #C0125
    ChrTalk(
        0xFE,
        (
            "きのう、アゼル兄ちゃんたちのいる\x01",
            "旧市街でおもしろいことが\x01",
            "あったんだってね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        "いいな～、僕も見たかったな～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_2842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2908")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D6")

    #C0127
    ChrTalk(
        0xFE,
        (
            "ちぇっ……\x01",
            "アゼル兄ちゃんとずっと一緒に\x01",
            "いられると思ったのにな……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "……でもいいや。\x01",
            "お姉ちゃん、遊びにいこ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2903")

    label("loc_28D6")


    #C0129
    ChrTalk(
        0xFE,
        (
            "お姉ちゃんがいるから\x01",
            "寂しくないもんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2903")

    Jump("loc_2CD6")

    label("loc_2908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2951")

    #C0130
    ChrTalk(
        0xFE,
        (
            "えへへ、アゼル兄ちゃんと\x01",
            "遊撃士ごっこして遊ぶんだー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_2951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_29AA")

    #C0131
    ChrTalk(
        0xFE,
        "来月は記念祭なんだよ。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "アゼル兄ちゃんと久しぶりに\x01",
            "遊びたいな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_29AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_29E1")

    #C0133
    ChrTalk(
        0xFE,
        (
            "クラリスおばさんの所で\x01",
            "待ってるね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_29E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A5F")

    #C0134
    ChrTalk(
        0xFE,
        "お姉ちゃん、嬉しそうだね。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "アゼル兄ちゃんも働き始めて、\x01",
            "ちょっとだけ生活が楽になったって\x01",
            "言ってたよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_2A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2AC4")

    #C0136
    ChrTalk(
        0xFE,
        (
            "お姉ちゃんが旧市街に\x01",
            "アゼル兄ちゃんを迎えに行ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "だ、大丈夫かなぁ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_2AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2B38")

    #C0138
    ChrTalk(
        0xFE,
        (
            "アゼル兄ちゃんは\x01",
            "ずっと帰ってこないんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "お姉ちゃんに心配掛けて\x01",
            "何やってんだろ、もう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_2B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2B9C")

    #C0140
    ChrTalk(
        0xFE,
        (
            "ねえねえ\x01",
            "遊撃士ごっこしようよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "とうとう、やー！\x01",
            "遊撃士は無敵なんだぞっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_2B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2BE9")

    #C0142
    ChrTalk(
        0xFE,
        (
            "アゼル兄ちゃん、\x01",
            "怪我しちゃったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        "大丈夫かな……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_2BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2CD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C66")

    #C0144
    ChrTalk(
        0xFE,
        (
            "遊撃士ってね、\x01",
            "スゴクかっこいいんだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "ぼくね、アリオスさんに\x01",
            "あった事があるんだ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CD6")

    label("loc_2C66")


    #C0146
    ChrTalk(
        0xFE,
        (
            "ぼくね、アリオスさんに\x01",
            "あった事があるんだ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "えへへ～、スゴイでしょ。\x01",
            "スゴクかっこよかったんだよ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD6")

    TalkEnd(0xFE)
    Return()

    # Function_9_25E8 end

    def Function_10_2CDA(): pass

    label("Function_10_2CDA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2D5C")

    #C0148
    ChrTalk(
        0xFE,
        "……あら、もうこんな時間じゃない。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "フランは昼間、随分急がしそうだったけど\x01",
            "きちんと食事をとったかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426F")

    label("loc_2D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2E04")

    #C0150
    ChrTalk(
        0xFE,
        (
            "フランがお弁当を忘れていったから\x01",
            "警察まで届けに行ったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "なにやら随分忙しそうにしてて\x01",
            "渡せなかったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "何かあったのかしらねぇ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_426F")

    label("loc_2E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2F54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EDF")

    #C0153
    ChrTalk(
        0xFE,
        "港湾区で抗争があったって噂よ。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "フランは受付だから\x01",
            "現場に駆り出されることは\x01",
            "少ないでしょうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "最近、警察は危ない事件に\x01",
            "関わることも多いらしいから、\x01",
            "たまに心配になるのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F4F")

    label("loc_2EDF")


    #C0156
    ChrTalk(
        0xFE,
        (
            "あなたたちも、警察として\x01",
            "事件に関わっていくのはいいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "周りの人にあまり\x01",
            "心配をかけないようにね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F4F")

    Jump("loc_426F")

    label("loc_2F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_31EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3171")
    TurnDirection(0xFE, 0x109, 0)

    #C0158
    ChrTalk(
        0xFE,
        "あら、ノエルじゃないの。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x109,
        "#0505Fあ、母さん。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x104,
        (
            "#0306Fな、なんだなんだ。\x01",
            "妙にアッサリした再会シーンだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x109,
        (
            "#0500Fいえ、まぁ……\x01",
            "最近よく会ってましたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#0000Fはは、なかなか親孝行なんだな。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x102,
        "#0102Fお母様も嬉しいんじゃないですか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    #C0164
    ChrTalk(
        0xFE,
        "ふふ、まあね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 500)

    #C0165
    ChrTalk(
        0xFE,
        (
            "ノエル、あんたも出来れば\x01",
            "マメに連絡をよこしなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "母さんもフランも、\x01",
            "これでも心配してるのよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x109,
        (
            "#0506Fも、もう母さん……\x01",
            "皆さんの前でそんなこと言わないでよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        "#0200F流石のノエルさんも形無しですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_31E9")

    label("loc_3171")


    #C0169
    ChrTalk(
        0xFE,
        (
            "いい？　ノエル。\x01",
            "これからはマメに連絡をよこすのよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x109,
        (
            "#0506Fそんなに何回も言わなくても\x01",
            "分かってるって、もう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E9")

    Jump("loc_426F")

    label("loc_31EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3376")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E0")

    #C0171
    ChrTalk(
        0xFE,
        (
            "記念祭の最終日の夜に、\x01",
            "サリナちゃんの家族と\x01",
            "食事会をしたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "でも、フランは困ってた観光客を\x01",
            "助けてたらしくて、\x01",
            "夜遅くに帰ってきたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "彼氏の１人でもできたかと思って\x01",
            "ちょっと喜んでたんだけどねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3371")

    label("loc_32E0")


    #C0174
    ChrTalk(
        0xFE,
        (
            "フラン、記念祭の最終日は\x01",
            "困ってた観光客を助けてたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "年頃の娘なんだから、\x01",
            "彼氏の１人くらい作って\x01",
            "安心させてくれればいいのにねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3371")

    Jump("loc_426F")

    label("loc_3376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_340B")

    #C0176
    ChrTalk(
        0xFE,
        (
            "そういえば、今日は\x01",
            "サリナちゃんとこの上の弟が\x01",
            "もどってるんだっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "せっかくだし、みんなまとめて\x01",
            "お食事に呼んでみようかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426F")

    label("loc_340B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3496")

    #C0178
    ChrTalk(
        0xFE,
        (
            "パレード中に空いた百貨店で\x01",
            "買い物を済ませてきたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "パレード終わり際の\x01",
            "いいシーンも見れたし……\x01",
            "ふふ、作戦勝ちね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426F")

    label("loc_3496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3561")

    #C0180
    ChrTalk(
        0xFE,
        (
            "んんっと、今日は４日目だから……\x01",
            "パレードがある日よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "皆がそっちに気を向けてるうちに、\x01",
            "ぱっと買い物を済ましてこようかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "パレード中の百貨店なんて\x01",
            "穴場もいいところなのよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426F")

    label("loc_3561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3604")

    #C0183
    ChrTalk(
        0xFE,
        (
            "さぁて、あたしも記念祭に\x01",
            "繰り出すとしましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "初日は、ノエルやフランが港湾区で\x01",
            "楽しんでたのよね。\x01",
            "あたしもちょっと覗いてみようかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426F")

    label("loc_3604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3778")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36DB")

    #C0185
    ChrTalk(
        0xFE,
        (
            "昨日はノエルとフランが\x01",
            "家に戻ってきていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "夜は２人で港湾区のイベントに\x01",
            "出かけていたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "ほんと、昔から姉妹仲はいいのよ。\x01",
            "あんなのじゃ男が\x01",
            "近寄りにくいだろうにね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3773")

    label("loc_36DB")


    #C0188
    ChrTalk(
        0xFE,
        (
            "ノエルとフランは昔から\x01",
            "姉妹仲がよくてね。\x01",
            "いつも一緒に遊んでいたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "あんな仲がよくちゃ、\x01",
            "男も寄りにくいだろうに。\x01",
            "姉妹揃って苦労しそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3773")

    Jump("loc_426F")

    label("loc_3778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_38DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3856")

    #C0190
    ChrTalk(
        0xFE,
        (
            "そういえばノエル、\x01",
            "記念祭の初日は\x01",
            "帰省するって言ってたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "フランが毎日毎日、\x01",
            "『来月が楽しみ』なんて言って\x01",
            "うるさいったらないのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "……ふふ、まぁ仲が良くて\x01",
            "いいとは思うけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38D9")

    label("loc_3856")


    #C0193
    ChrTalk(
        0xFE,
        (
            "ノエル、記念祭の初日は\x01",
            "こっちに戻ってくるらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "警備隊も忙しいだろうに、\x01",
            "無理して休みをとったんじゃ\x01",
            "ないだろうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D9")

    Jump("loc_426F")

    label("loc_38DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A3")

    #C0195
    ChrTalk(
        0xFE,
        (
            "私は昔、露店商をやっていてね。\x01",
            "そこの通りでは随分と活躍したものよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "店を出していた場所は今、\x01",
            "クロンク君が引き継いでるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        "ふふ、商売熱心な子でよかったわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A38")

    label("loc_39A3")


    #C0198
    ChrTalk(
        0xFE,
        (
            "私が店を出していた場所は今、\x01",
            "クロンク君が引き継いでるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "引退した露天商は次の露天商に\x01",
            "場所を継承する。\x01",
            "これは露店街の伝統的な風習なのよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A38")

    Jump("loc_426F")

    label("loc_3A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3AF6")

    #C0200
    ChrTalk(
        0xFE,
        (
            "さーて、今日はユゴット君を\x01",
            "預かる日だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "折角だし、腕によりをかけて\x01",
            "ご馳走をつくっちゃおうかしらね。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "余ったらフランの\x01",
            "晩御飯にすればいいしね、ふふ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426F")

    label("loc_3AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3C76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BF6")

    #C0203
    ChrTalk(
        0xFE,
        (
            "この間、タングラム門に務めてる\x01",
            "ノエルから手紙が届いたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "手紙の内容は\x01",
            "とりとめもないものだったけど、\x01",
            "まぁ元気にやってるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "あの子ったらこういうのを\x01",
            "ほとんどよこさないから、\x01",
            "あたしもフランも心配してたのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C71")

    label("loc_3BF6")


    #C0206
    ChrTalk(
        0xFE,
        (
            "ノエルったらなかなか\x01",
            "連絡をよこさないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "まぁ、曹長っていう立場じゃ\x01",
            "なかなか時間が\x01",
            "とれないものなのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C71")

    Jump("loc_426F")

    label("loc_3C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3D51")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3C93")
    Call(0, 11)
    Jump("loc_3D4C")

    label("loc_3C93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_3D34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3CB1")
    Call(0, 11)
    Jump("loc_3D2F")

    label("loc_3CB1")


    #C0208
    ChrTalk(
        0xC,
        (
            "お隣の小さな弟さんに\x01",
            "読んであげようと思って\x01",
            "本を借りていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xC,
        (
            "あなた達も、機会があったら\x01",
            "読んでみるといいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3D2F")

    Jump("loc_3D4C")

    label("loc_3D34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3D49")
    Call(0, 21)
    Jump("loc_3D4C")

    label("loc_3D49")

    Call(0, 11)

    label("loc_3D4C")

    Jump("loc_426F")

    label("loc_3D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3E2C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3D6E")
    Call(0, 12)
    Jump("loc_3E27")

    label("loc_3D6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_3E0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3D8C")
    Call(0, 12)
    Jump("loc_3E0A")

    label("loc_3D8C")


    #C0210
    ChrTalk(
        0xC,
        (
            "お隣の小さな弟さんに\x01",
            "読んであげようと思って\x01",
            "本を借りていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xC,
        (
            "あなた達も、機会があったら\x01",
            "読んでみるといいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3E0A")

    Jump("loc_3E27")

    label("loc_3E0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3E24")
    Call(0, 21)
    Jump("loc_3E27")

    label("loc_3E24")

    Call(0, 12)

    label("loc_3E27")

    Jump("loc_426F")

    label("loc_3E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3F07")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3E49")
    Call(0, 13)
    Jump("loc_3F02")

    label("loc_3E49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_3EEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3E67")
    Call(0, 13)
    Jump("loc_3EE5")

    label("loc_3E67")


    #C0212
    ChrTalk(
        0xC,
        (
            "お隣の小さな弟さんに\x01",
            "読んであげようと思って\x01",
            "本を借りていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xC,
        (
            "あなた達も、機会があったら\x01",
            "読んでみるといいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3EE5")

    Jump("loc_3F02")

    label("loc_3EEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3EFF")
    Call(0, 21)
    Jump("loc_3F02")

    label("loc_3EFF")

    Call(0, 13)

    label("loc_3F02")

    Jump("loc_426F")

    label("loc_3F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_412B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4092")

    #C0214
    ChrTalk(
        0xFE,
        (
            "あたしの娘は警察本部で、\x01",
            "『オペレーター』っていう仕事を\x01",
            "やっているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "あたしはどうも、そういう\x01",
            "新しめのモノに疎くてねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "何度仕事の内容を聞かされても\x01",
            "ちんぷんかんぷんだわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_408A")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x101,
        "#0005F（あれ、もしかして……）\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x102,
        "#0100F（どうやら、フランさんのお母様みたいね。）\x02",
    )

    CloseMessageWindow()

    label("loc_408A")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4126")

    label("loc_4092")


    #C0219
    ChrTalk(
        0xFE,
        (
            "あたしの娘は警察本部で、\x01",
            "『オペレーター』っていう仕事を\x01",
            "やっているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "仕事の内容は何回も\x01",
            "説明してもらったけど、\x01",
            "ちんぷんかんぷんだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4126")

    Jump("loc_426F")

    label("loc_412B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_426F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4211")

    #C0221
    ChrTalk(
        0xFE,
        "うちには娘が２人いるの。\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "姉は警備隊、妹は警察で\x01",
            "それぞれ働いてるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "ふふふ、立派に育ってくれて\x01",
            "母親冥利に尽きるってもんよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#0005F（警察……もしかして、\x01",
            "  会ったことある人かな？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_426F")

    label("loc_4211")


    #C0225
    ChrTalk(
        0xFE,
        (
            "うちの娘は警備隊と警察で\x01",
            "立派に働いているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "ふふ、母親冥利に\x01",
            "尽きるってもんよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426F")

    SetScenarioFlags(0x71, 6)
    TalkEnd(0xFE)
    Return()

    # Function_10_2CDA end

    def Function_11_4276(): pass

    label("Function_11_4276")


    #C0227
    ChrTalk(
        0xFE,
        (
            "今日はサリナちゃんに頼まれて、\x01",
            "ユゴット君の面倒を見てるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "なんでも、上の弟を探しに\x01",
            "旧市街に行くらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "治安の悪い場所だから少し心配ね。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_11_4276 end

    def Function_12_4319(): pass

    label("Function_12_4319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4429")

    #C0230
    ChrTalk(
        0xFE,
        (
            "お向かいのサリナちゃんは、\x01",
            "家族を支えるために１人で\x01",
            "お仕事を頑張ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "若いのに偉いわよね。\x01",
            "感心、感心。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "フランも、もう警察の受付として\x01",
            "立派に働いているんだし、\x01",
            "家を出てもいい頃なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "あの子、ちょっと\x01",
            "寂しがり屋だからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44A7")

    label("loc_4429")


    #C0234
    ChrTalk(
        0xFE,
        (
            "フラン、ああ見えて\x01",
            "けっこう寂しがり屋なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "お向かいのサリナちゃんみたいに\x01",
            "もっと自立心をつけてもらわないとねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44A7")

    Return()

    # Function_12_4319 end

    def Function_13_44A8(): pass

    label("Function_13_44A8")


    #C0236
    ChrTalk(
        0xFE,
        (
            "フランは警察のお仕事、\x01",
            "頑張ってるかしらねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "ま、あの子はああ見えて\x01",
            "意外としっかりしてるし、\x01",
            "心配することもそうないか。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_13_44A8 end

    def Function_14_452E(): pass

    label("Function_14_452E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4598")

    #C0238
    ChrTalk(
        0xFE,
        "姉さん、大丈夫……？\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "いや、その……\x01",
            "うちは港湾公園に近いし、\x01",
            "心配になったからさ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4598")

    TalkEnd(0xFE)
    Return()

    # Function_14_452E end

    def Function_15_459C(): pass

    label("Function_15_459C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_47BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46DC")
    SetChrName("")

    #A0240
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エステルは棚に並んだスニーカーを\x01",
            "真剣な顔で眺め回している。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0241
    ChrTalk(
        0xE,
        (
            "#0801Fさてと、念のため\x01",
            "とっておきのスニーカーに\x01",
            "履き替えておこうかな。\x02\x03",

            "#0803Fうーん、記念モデルの方が\x01",
            "グリップは利きそうだけど\x01",
            "限定モデルの方が頑丈だし……\x02\x03",

            "#0802Fどっちもお気に入りだから\x01",
            "迷っちゃうわね～。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 5)
    Jump("loc_47BD")

    label("loc_46DC")


    #C0242
    ChrTalk(
        0xE,
        (
            "#0809Fあはは、マフィアの件で\x01",
            "キナ臭くなりそうだったから\x01",
            "念のために装備の確認をね。\x02\x03",

            "#0802Fロイド君たちも、靴は良いのを\x01",
            "履いた方がいいわよ？\x02\x03",

            "#0804Fやっぱストレガーがお勧めね！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        "#0012F（ストレガーファンなのか……？）\x02",
    )

    CloseMessageWindow()

    label("loc_47BD")

    TalkEnd(0xFE)
    Return()

    # Function_15_459C end

    def Function_16_47C1(): pass

    label("Function_16_47C1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4855")
    Jump("loc_489F")

    label("loc_4855")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4875")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_489F")

    label("loc_4875")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4895")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_489F")

    label("loc_4895")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_489F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4B7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB3")

    #C0244
    ChrTalk(
        0x10,
        "#0900Fやあ、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xF,
        "#0809Fこんにちは～、ロイド君たち！\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#0005Fこんにちは……\x01",
            "って、もしかして。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x102,
        (
            "#0105Fこちらの部屋が\x01",
            "エステルさんたちの……？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xF,
        (
            "#0804Fうん、クロスベルで借りてる\x01",
            "あたしたちの部屋ってわけ。\x02\x03",

            "#0802F日中は殆んどいないけど\x01",
            "よかったら遊びに来てね？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#0002Fあ、ああ……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x103,
        (
            "#0200F（結局この２人って\x01",
            "  どういう関係なんでしょう？）\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x104,
        (
            "#0303F（姓は同じみてぇだが\x01",
            "  兄妹には見えねぇし……）\x02\x03",

            "#0305F（ハッ、まさか夫婦とか……！？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 5)
    Jump("loc_4B7C")

    label("loc_4AB3")


    #C0252
    ChrTalk(
        0xF,
        (
            "#0802Fさてと、遅くなったけど\x01",
            "そろそろ仕事に出かけようかな。\x02\x03",

            "#0809Fクロスベルって、毎日のように\x01",
            "依頼が大量に入ってくるから\x01",
            "すっごくやり甲斐があるのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#0012F（もの凄くイイ表情だな……）\x02",
    )

    CloseMessageWindow()

    label("loc_4B7C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_47C1 end

    def Function_17_4B84(): pass

    label("Function_17_4B84")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C18")
    Jump("loc_4C62")

    label("loc_4C18")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C38")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C62")

    label("loc_4C38")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C58")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C62")

    label("loc_4C58")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C62")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4EBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_4D88")

    #C0254
    ChrTalk(
        0x101,
        (
            "#0005Fあれ、ヨシュア。\x01",
            "ギルドから戻ってきたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x10,
        (
            "#0900Fあ、うん。\x01",
            "いったん解散になったんだ。\x02\x03",

            "#0903Fどうやらすぐに報復が\x01",
            "始まるわけでもなさそうだしね。\x02\x03",

            "#0901Fただ、予断は許さないから\x01",
            "みんな市内に待機しているよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E58")

    label("loc_4D88")


    #C0256
    ChrTalk(
        0x10,
        (
            "#0900Fマフィアの抗争に備えて\x01",
            "ギルドで待機してたんだけど\x01",
            "いったん解散になったんだ。\x02\x03",

            "#0903Fどうやらすぐに報復が\x01",
            "始まるわけでもなさそうだしね。\x02\x03",

            "#0901Fただ、予断は許さないから\x01",
            "みんな市内に待機しているよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E58")

    SetScenarioFlags(0x0, 6)
    Jump("loc_4EB9")

    label("loc_4E60")


    #C0257
    ChrTalk(
        0x10,
        (
            "#0903Fマフィア同士の抗争か……\x02\x03",

            "#0901F何とか未然に食い止められると\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EB9")

    Jump("loc_5137")

    label("loc_4EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5137")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED9")
    Call(0, 16)
    Jump("loc_5137")

    label("loc_4ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_507A")

    #C0258
    ChrTalk(
        0x104,
        (
            "#0303F（おい、色男……）\x02\x03",

            "#0301F（それで結局、\x01",
            "  お前とエステルちゃんの\x01",
            "  関係は何なんだ？）\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x10,
        (
            "#0905F（ああ……\x01",
            "  義理の姉弟なんです。）\x02\x03",

            "#0910F（その、一応恋人同士でも\x01",
            "  ありますけど。）\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x104,
        (
            "#0306F（ガクッ……\x01",
            "  やっぱそうかよ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        "#0204F（これで謎は解けましたね。）\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        (
            "#0000F（しかし家族でもあり、\x01",
            "  恋人同士でもあるのか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x102,
        (
            "#0109F（ふふ、息がピッタリなのも\x01",
            "  頷けるわね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5137")

    label("loc_507A")


    #C0264
    ChrTalk(
        0x10,
        (
            "#0901Fそういえば……\x01",
            "マフィアの軍用犬の事件は\x01",
            "大変だったみたいだね？\x02\x03",

            "#0902F色々と難しい所だけど……\x01",
            "お互い、頑張っていこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        (
            "#0002F……ああ。\x01",
            "そう言ってもらえると\x01",
            "励みになるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5137")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_4B84 end

    def Function_18_513F(): pass

    label("Function_18_513F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5154")
    Call(0, 19)
    Jump("loc_5209")

    label("loc_5154")


    #C0266
    ChrTalk(
        0x11,
        (
            "#11P#6405Fそういえば、今日は夕方に\x01",
            "お姉ちゃんが帰ってくるんです。\x02\x03",

            "#6409F家族揃っての夕食は\x01",
            "１０日ぶりくらいなんです。\x02\x03",

            "生キーアちゃんにも会えたし、\x01",
            "今日は最高の休日ですよ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5209")

    TalkEnd(0xFE)
    Return()

    # Function_18_513F end

    def Function_19_520D(): pass

    label("Function_19_520D")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1050, 1500, -53430, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17330, 0)
    SetChrPos(0x101, -400, 30, -52100, 180)
    SetChrPos(0xEF, -1600, 30, -52500, 135)
    SetChrPos(0x153, -1500, 30, -53770, 90)
    SetChrSubChip(0x11, 0x0)
    OP_93(0x11, 0x87, 0x0)
    OP_0D()

    #C0267
    ChrTalk(
        0x153,
        "#6P#1105Fあ、フランだー！\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x11, 0x153, 500)

    #C0268
    ChrTalk(
        0x11,
        "#11P#6405Fあ、キーアちゃん！？\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        (
            "#5P#0002Fそっか……\x01",
            "ここがフランの実家か。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5350")

    #C0270
    ChrTalk(
        0x102,
        "#6P#0102F今日はお休みみたいね？\x02",
    )

    CloseMessageWindow()
    Jump("loc_53C3")

    label("loc_5350")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_538E")

    #C0271
    ChrTalk(
        0x103,
        "#6P#0202F今日はお休みみたいですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_53C3")

    label("loc_538E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53C3")

    #C0272
    ChrTalk(
        0x104,
        "#6P#0300F今日は休みみたいだな？\x02",
    )

    CloseMessageWindow()

    label("loc_53C3")

    TurnDirection(0x11, 0xEF, 500)

    #C0273
    ChrTalk(
        0x11,
        (
            "#11P#6406Fそうなんですよ～。\x01",
            "記念祭からやっと\x01",
            "休みがもらえまして～……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x153, 500)
    Sleep(300)

    #C0274
    ChrTalk(
        0x11,
        (
            "#11P#6409F──でもでも！\x01",
            "まさかキーアちゃんが\x01",
            "会いに来てくれるなんて～！\x02\x03",

            "#6400F端末で話しただけで\x01",
            "実際に会うの初めてだよね？\x01",
            "……ようこそ我が家へっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x153,
        (
            "#6P#1100Fうんっ。\x02\x03",

            "#1110Fでもフラン、端末でみたのと\x01",
            "ちがうフク着てるね～。\x02\x03",

            "#1109Fえへへ、ピンクいろで\x01",
            "すっごくカワイイかもー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x11,
        (
            "#11P#6409Fあ、ありがと～。\x02\x03",

            "#6401F……キーアちゃんの方こそ\x01",
            "モニター越しよりも\x01",
            "はるかにカワイイような……\x02\x03",

            "#6406Fか、かわいいよ～、かわいいな～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)
    TurnDirection(0x11, 0x101, 500)
    Sleep(300)

    #C0277
    ChrTalk(
        0x11,
        (
            "#11P#6401Fロ、ロイドさん！\x01",
            "わたしもキーアちゃんと\x01",
            "お散歩したいであります！\x02\x03",

            "#6406Fえ～ん、一緒に\x01",
            "連れて行ってくださいよう～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(892, 0, 100, 0)
    OP_63(0x11, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5731")

    #C0278
    ChrTalk(
        0x102,
        (
            "#6P#0109Fフ、フランさん……\x01",
            "少し落ち着いてね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57BD")

    label("loc_5731")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5784")

    #C0279
    ChrTalk(
        0x103,
        (
            "#6P#0203Fコホン……フランさん。\x01",
            "少し落ち着いてください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57BD")

    label("loc_5784")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57BD")

    #C0280
    ChrTalk(
        0x104,
        "#6P#0309Fお、落ち着けフランちゃん。\x02",
    )

    CloseMessageWindow()

    label("loc_57BD")


    #C0281
    ChrTalk(
        0x101,
        (
            "#5P#0012Fわ、悪いけど\x01",
            "これから行く所があってさ……\x02\x03",

            "#0002Fまた今度、\x01",
            "ちゃんと機会を作るよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x11,
        (
            "#11P#6401Fううっ……\x01",
            "ゼッタイですよ～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x153, 500)
    Sleep(300)

    #C0283
    ChrTalk(
        0x11,
        (
            "#11P#6409Fキーアちゃん！\x01",
            "こんど一緒に散歩しようね？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x153,
        "#6P#1109Fうんっ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -1150, 30, -53080, 135)
    OP_66(0x1, 0x1)
    SetScenarioFlags(0xB6, 5)
    EventEnd(0x5)
    Return()

    # Function_19_520D end

    def Function_20_58C1(): pass

    label("Function_20_58C1")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_68(51230, 1420, 3870, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 50930, 0, 3560, 0)
    SetChrPos(0x102, 52070, 0, 3560, 0)
    SetChrPos(0x103, 50930, 0, 2150, 0)
    SetChrPos(0x104, 52070, 0, 2150, 0)
    SetChrPos(0x8, 45830, -1840, 0, 0)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_95(0x101, 51620, 0, 4810, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)
    Sound(810, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    #A0285
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    #C0286
    ChrTalk(
        0x101,
        (
            "#11P#0000Fすみません！\x01",
            "どなたかいらっしゃいますか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1400)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    #C0287
    ChrTalk(
        0x103,
        "#12P#0200F人の気配はないようですね。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        "#11P#0003Fああ、そうみたいだな……\x02",
    )

    CloseMessageWindow()

    #N0289
    NpcTalk(
        0x8,
        "男性の声",
        "おや、何をやっているのかな。\x02",
    )

    CloseMessageWindow()

    def lambda_5ADB():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5ADB)

    def lambda_5AE8():

        label("loc_5AE8")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_5AE8")

    QueueWorkItem2(0x102, 1, lambda_5AE8)

    def lambda_5AFA():

        label("loc_5AFA")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_5AFA")

    QueueWorkItem2(0x103, 1, lambda_5AFA)

    def lambda_5B0C():

        label("loc_5B0C")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_5B0C")

    QueueWorkItem2(0x104, 1, lambda_5B0C)
    OP_68(50380, 1420, 1610, 2000)
    OP_95(0x8, 49910, 0, 0, 2000, 0x0)
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(500)
    OP_6F(0x1)

    #C0290
    ChrTalk(
        0x8,
        "#12Pそこは空家だよ？\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x104,
        "#11P#0305Fおっと、やっぱそうスか。\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        (
            "#12Pうん、半月ほど前に\x01",
            "引っ越されてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        (
            "#12P入居したいなら大家さんに\x01",
            "直接連絡する事だね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_5BF8():

        label("loc_5BF8")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_5BF8")

    QueueWorkItem2(0x101, 1, lambda_5BF8)
    OP_95(0x8, 51410, 30, -1640, 2000, 0x0)
    OP_95(0x8, 51410, 0, -7420, 2000, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Sleep(300)
    Fade(500)
    OP_68(51230, 1420, 3870, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    Sleep(100)

    def lambda_5C7B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C7B)

    def lambda_5C88():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C88)

    def lambda_5C95():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C95)
    Sleep(300)

    #C0294
    ChrTalk(
        0x101,
        (
            "#5P#0003Fどうやら東通りの空家ってのは\x01",
            "ここの事みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x104,
        (
            "#0306F前の住民が転居するときに\x01",
            "いい加減な届けを\x01",
            "出したんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        (
            "#12P#0200Fそういえば……市役所の人も\x01",
            "書類が正確でないとか\x01",
            "仰っていましたね。\x02\x03",

            "#0206Fこういう事ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x102,
        (
            "#0103Fええと、空家は\x01",
            "アカシア荘の２０２号室ね……\x01",
            "（メモをしておかないと……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E88")

    #C0298
    ChrTalk(
        0x101,
        (
            "#0003Fよし、これで３箇所全ての\x01",
            "空家が確認できたみたいだし……\x02\x03",

            "#0000F市役所の受付まで\x01",
            "報告に戻るとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x1E)
    Jump("loc_5EBD")

    label("loc_5E88")


    #C0299
    ChrTalk(
        0x101,
        (
            "#0000Fよし、それじゃ\x01",
            "残りの件を当たってみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EBD")

    Sleep(200)
    SetChrPos(0x0, 51710, 0, 4590, 180)
    SetChrPos(0x1, 51710, 0, 4590, 180)
    SetChrPos(0x2, 51710, 0, 4590, 180)
    SetChrPos(0x3, 51710, 0, 4590, 180)
    ClearChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 48880, 30, -55000, 135)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 7)
    EventEnd(0x5)
    Return()

    # Function_20_58C1 end

    def Function_21_5F29(): pass

    label("Function_21_5F29")

    EventBegin(0x0)
    Fade(500)
    OP_68(3230, 1530, -56000, 0)
    MoveCamera(62, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19760, 0)
    SetChrPos(0x101, 2610, 30, -55580, 135)
    SetChrPos(0x102, 4019, 0, -54690, 180)
    SetChrPos(0x103, 2360, 30, -54400, 135)
    SetChrPos(0x104, 3880, 0, -53400, 180)
    TurnDirection(0xC, 0x101, 0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 6)), scpexpr(EXPR_END)), "loc_5FF8")

    #C0300
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあの、クラリスさん。\x01",
            "少しよろしいでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6026")

    label("loc_5FF8")


    #C0301
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあの……\x01",
            "クラリスさんですよね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6026")


    #C0302
    ChrTalk(
        0xC,
        "#11Pあら……私に何かご用かしら？\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#6P#0003Fええ、実は……\x01",
            "図書館の司書さんから\x01",
            "頼まれごとがありまして。\x02\x03",

            "#0000Fクラリスさん、\x01",
            "図書館の本を借りたままに\x01",
            "していませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0304
    ChrTalk(
        0xC,
        (
            "#11Pあーあー！\x01",
            "すっかり忘れてたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xC,
        (
            "#11Pそういえば返却期限を\x01",
            "過ぎちゃっていたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x103,
        (
            "#6P#0200Fどうやらただ忘れてらした\x01",
            "だけのようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xC,
        (
            "#11Pふふ、歳をとると\x01",
            "物忘れしやすくなってだめね。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xC,
        (
            "#11Pこんなのじゃノエルに\x01",
            "叱られてしまうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xC,
        (
            "#11Pええと……\x01",
            "ちょっと待って頂戴。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_95(0xC, 2250, 0, -57250, 2000, 0x0)
    OP_95(0xC, -1980, 0, -57290, 2000, 0x0)
    OP_0D()
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 3660, 30, -56600, 315)
    FadeToBright(500, 0)
    OP_0D()

    #C0310
    ChrTalk(
        0xC,
        "#11P……はい、これね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0311
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D6, 1)
    TurnDirection(0x102, 0x101, 500)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0312
    ChrTalk(
        0x102,
        "#11P#0105Fあら、この本って……\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x104,
        "#5P#0305Fなんだお嬢、知ってんのか？\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        (
            "#11P#0100Fええ。\x02\x03",

            "図書館で一番借りられている\x01",
            "有名な童話なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xC,
        (
            "#11Pうちはお隣のサリナちゃんが\x01",
            "お仕事に行く時は、\x01",
            "小さい弟さんを預かっててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xC,
        (
            "#11Pその時に読んであげようと思って\x01",
            "借りていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        "#11Pふふ、とっても喜んでくれたんだから。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#6P#0005Fへぇ……\x01",
            "（ちょっと興味あるなぁ……）\x02\x03",

            "#0000Fえっと、それでは\x01",
            "ご協力ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xC,
        "#11Pいえいえ、ご苦労さま。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xC,
        (
            "#11P今度からは返却期限には\x01",
            "気を付けるようにするわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x5, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6529")
    OP_29(0x5, 0x1, 0x1F)

    label("loc_6529")

    SetChrPos(0x0, 2610, 30, -55580, 135)
    EventEnd(0x5)
    Return()

    # Function_21_5F29 end

    def Function_22_653D(): pass

    label("Function_22_653D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6566")
    Call(0, 20)
    Jump("loc_66BF")

    label("loc_6566")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6694")
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0321
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0322
    ChrTalk(
        0x102,
        "#0100Fここも空家なのかしら……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#0000Fいや、住民が留守に\x01",
            "しているだけかもしれない。\x01",
            "断定は出来ないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x103,
        (
            "#0200F住所によると、東通りの空家は\x01",
            "遊撃士協会の右隣ですよね。\x02\x03",

            "そちらの民家を\x01",
            "訪れてみるべきかと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_66BF")

    label("loc_6694")

    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_66BF")

    TalkEnd(0xFF)
    Return()

    # Function_22_653D end

    def Function_23_66C3(): pass

    label("Function_23_66C3")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69A0")
    OP_4B(0x11, 0xFF)

    #C0326
    ChrTalk(
        0x101,
        "#0005Fこのぬいぐるみは……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x0, 500)
    Sleep(500)

    #C0327
    ChrTalk(
        0x11,
        (
            "#6400Fあ、その子はですね、\x01",
            "私の心の友、熊のバンバンです。\x02\x03",

            "#6409Fえへへ、可愛いでしょ？\x01",
            "大切な人とお揃いで買ったんですよ～。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x11, 500)
    Sleep(200)

    #C0328
    ChrTalk(
        0x153,
        (
            "#1109Fほんとだ、スッゴク\x01",
            "かわいいね～！\x02\x03",

            "#1110Fねえフラン～、\x01",
            "バンバンは何歳なの？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x11,
        (
            "#6409Fバンバンは３歳だよ！\x01",
            "……やっぱりキーアちゃんも\x01",
            "バンバンの可愛さが判るんだね！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68BD")

    #C0330
    ChrTalk(
        0x102,
        (
            "#0102F（この２人、本当に\x01",
            "  気が合うわよね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6948")

    label("loc_68BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6905")

    #C0331
    ChrTalk(
        0x103,
        (
            "#0202F（この２人は本当に\x01",
            "  気が合いますね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6948")

    label("loc_6905")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6948")

    #C0332
    ChrTalk(
        0x104,
        (
            "#0302F（この２人、本当に\x01",
            "  気が合うよなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6948")


    #C0333
    ChrTalk(
        0x101,
        (
            "#0004F（今まで端末ごしでだけ\x01",
            "  話していたとは思えないよな……）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_93(0x11, 0x87, 0x1F4)
    SetScenarioFlags(0xD1, 0)
    Jump("loc_69F6")

    label("loc_69A0")

    SetChrName("")

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フランの可愛がっているぬいぐるみがある。\x01",
            "……名前はバンバンというらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_69F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D1F")

    #C0335
    ChrTalk(
        0x109,
        "#0505Fあ、これは……\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        "#0100Fノエルさん、どうかしたの？\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x109,
        (
            "#0500Fはは、このぬいぐるみは\x01",
            "フランの持ち物でして。\x02\x03",

            "#0503F確かバンバンとかいう名前で\x01",
            "可愛がってるみたいですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 2)), scpexpr(EXPR_END)), "loc_6B40")

    #C0338
    ChrTalk(
        0x104,
        (
            "#0300Fああ、ノエル曹長と\x01",
            "お揃いのやつだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#0004F名前をつけて可愛がってる辺りが\x01",
            "フランらしいよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BBB")

    label("loc_6B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 0)), scpexpr(EXPR_END)), "loc_6BBB")

    #C0340
    ChrTalk(
        0x101,
        (
            "#0000Fはは、そういやフランも\x01",
            "そんな話をしてたっけ。\x02\x03",

            "#0004F名前をつけて可愛がってる辺りが\x01",
            "フランらしいよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C8B")

    #C0341
    ChrTalk(
        0x109,
        (
            "#0503F（……じ、実はあたしも……\x01",
            "  ぬいぐるみを持ってるんですが。）\x02\x03",

            "#0508F（恥ずかしくて言い出せない……）\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        (
            "#0200F…………………………？\x01",
            "（ノエルさんから\x01",
            "  何か言いたそうな気配が。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D17")

    label("loc_6C8B")


    #C0343
    ChrTalk(
        0x109,
        (
            "#0500Fそうなんですよね……\x02\x03",

            "#0508Fあたしにもそういう愛嬌があったら。\x01",
            "はあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x103,
        (
            "#0200F（ノエルさんにも\x01",
            "  悩みがあるみたいですね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D17")

    SetScenarioFlags(0xD1, 1)
    Jump("loc_6E4E")

    label("loc_6D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D82")
    SetChrName("")

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フランの可愛がっている\x01",
            "ぬいぐるみがある。\x02\x03",

            "名前はバンバンというらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6E4E")

    label("loc_6D82")

    SetChrName("")

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フランのぬいぐるみがある。\x01",
            "ノエルとはお揃いのようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0347
    ChrTalk(
        0x109,
        (
            "#0503F（あたしもあのぬいぐるみに\x01",
            "  名前くらい付けてあげようかな……）\x02\x03",

            "#0506F（いやいや、そんな真似\x01",
            "  いくらなんでも恥ずかしいし。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E4E")

    TalkEnd(0xFF)
    Return()

    # Function_23_66C3 end

    SaveToFile()

Try(main)
