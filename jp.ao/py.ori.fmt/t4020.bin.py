from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4020.bin",                # FileName
        "t4020",                    # MapName
        "t4020",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4020",                  # 0
        "クイント老人",           # 1
        "ニールセン",             # 2
        "シュリ",                 # 3
        "ココア",                 # 4
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
        "chr/ch45100.itc",                   # 01
        "chr/ch10102.itc",                   # 02
        "apl/ch51090.itc",                   # 03
    ))

    DeclNpc(260260,  0,       250,     0,    385,  0x0, 0,   0,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(260149,  0,       -1750,   135,  389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(257899,  50,      2880,    90,   389,  0x0, 0,   2,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(258209,  500,     2099,    0,    502,  0x0, 7,   3,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(262920,  0,       3100,    1200,    262920,  1200,    3100,    0x007C, 0,  4,  0x0000)
    DeclActor(257930,  0,       1240,    1200,    257899,  1000,    2880,    0x007E, 0,  9,  0x0000)

    ChipFrameInfo(396, 0)                                        # 0

    ScpFunction((
        "Function_0_18C",          # 00, 0
        "Function_1_23C",          # 01, 1
        "Function_2_267",          # 02, 2
        "Function_3_44F",          # 03, 3
        "Function_4_4F5",          # 04, 4
        "Function_5_5A8",          # 05, 5
        "Function_6_13A2",         # 06, 6
        "Function_7_1736",         # 07, 7
        "Function_8_186A",         # 08, 8
        "Function_9_18FE",         # 09, 9
        "Function_10_1902",        # 0A, 10
        "Function_11_1A8D",        # 0B, 11
    ))


    def Function_0_18C(): pass

    label("Function_0_18C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1C4"),
        (1, "loc_1D0"),
        (2, "loc_1DC"),
        (3, "loc_1E8"),
        (4, "loc_1F4"),
        (5, "loc_200"),
        (6, "loc_20C"),
        (SWITCH_DEFAULT, "loc_218"),
    )


    label("loc_1C4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_1D0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_1DC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_1E8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_1F4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_200")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_20C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_218")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_224")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_23B")

    Return()

    # Function_0_18C end

    def Function_1_23C(): pass

    label("Function_1_23C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_266")
    OP_94(0xFE, 0x3F516, 0xFFFFFA38, 0x3FD0E, 0x8B6, 0x3E8)
    Sleep(600)
    Jump("Function_1_23C")

    label("loc_266")

    Return()

    # Function_1_23C end

    def Function_2_267(): pass

    label("Function_2_267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_275")
    Jump("loc_44E")

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_283")
    Jump("loc_44E")

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_29C")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_29C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B5")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2CE")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_2CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E7")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_2E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_300")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_319")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_332")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_340")
    Jump("loc_44E")

    label("loc_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34E")
    Jump("loc_44E")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_367")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B7")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x8, 260209, 0, -130, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 260260, 0, 1420, 180)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Jump("loc_44E")

    label("loc_3B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C5")
    Jump("loc_44E")

    label("loc_3C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_41E")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0x8, 259550, 0, 2840, 270)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_419")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_419")

    Jump("loc_44E")

    label("loc_41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_437")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_445")
    Jump("loc_44E")

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_44E")

    label("loc_44E")

    Return()

    # Function_2_267 end

    def Function_3_44F(): pass

    label("Function_3_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46B")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_482")

    label("loc_46B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_482")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CB")
    SetMapObjFrame(0xFF, "hikari00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "footlight00", 0x0, 0x1)
    Sound(128, 1, 50, 0)
    Jump("loc_4DE")

    label("loc_4CB")

    SetMapObjFrame(0xFF, "footlight01", 0x0, 0x1)

    label("loc_4DE")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F4")
    OP_66(0x1, 0x1)

    label("loc_4F4")

    Return()

    # Function_3_44F end

    def Function_4_4F5(): pass

    label("Function_4_4F5")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『一分クッキング・軽食編』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_5A4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『フレッシュサンド』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5A4")

    TalkEnd(0xFF)
    Return()

    # Function_4_4F5 end

    def Function_5_5A8(): pass

    label("Function_5_5A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65E")

    #C0003
    ChrTalk(
        0xFE,
        (
            "ニールセン君が\x01",
            "ガイの墓参りに来ておるようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "彼は最近、ガイの事件について\x01",
            "調べておったようだが……\x01",
            "進展があったんじゃろうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E4")

    label("loc_65E")


    #C0005
    ChrTalk(
        0xFE,
        (
            "国家としての独立……\x01",
            "それがクロスベルに何をもたらすか……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "……願わくば、この地に眠る者たちに\x01",
            "見守っていて欲しいものじゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E4")

    Jump("loc_139E")

    label("loc_6E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_801")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_798")

    #C0007
    ChrTalk(
        0xFE,
        (
            "先ほどアリオスがここに来てな。\x01",
            "挨拶していってくれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "昔のように一緒に酒を\x01",
            "飲むことはなくなったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "あやつも変わっておらんのう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7FC")

    label("loc_798")


    #C0010
    ChrTalk(
        0xFE,
        (
            "アリオスは今でも、\x01",
            "墓地に寄ると律儀に\x01",
            "挨拶をしにきてくれる。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "あやつも変わっておらんのう。\x02",
    )

    CloseMessageWindow()

    label("loc_7FC")

    Jump("loc_139E")

    label("loc_801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_896")

    #C0012
    ChrTalk(
        0xFE,
        (
            "山道では警備隊の者たちに\x01",
            "甚大な被害が出ているという。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "……未来ある若者たちが\x01",
            "命を散らしていくのは、\x01",
            "わしには耐えられんわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_139E")

    label("loc_896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_977")

    #C0014
    ChrTalk(
        0xFE,
        (
            "雨風にさらされれば、\x01",
            "墓に刻まれた墓標なども\x01",
            "少しずつ削れて消えていく。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "そうして人々からその存在を\x01",
            "忘れられていく墓も多い……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "そうならないためにも、\x01",
            "わしのような墓守が必要なのじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A0C")

    label("loc_977")


    #C0017
    ChrTalk(
        0xFE,
        (
            "長い年月、雨風にさらされ\x01",
            "墓標が削られれば、その存在は\x01",
            "人々に忘れられてしまう……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "そうならないためにも、\x01",
            "わしのような墓守が必要なのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0C")

    Jump("loc_139E")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B20")

    #C0019
    ChrTalk(
        0xFE,
        (
            "ガイの奴は、幼馴染と婚約して\x01",
            "これからだというときに殉職した。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "アリオスの奴は、妻の命と\x01",
            "愛娘の目の光を事故で失った。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "他人の為に、クロスベルの為に\x01",
            "身を粉にしていた彼らに\x01",
            "不幸がふりかかってしまうなど……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "……やり切れん話じゃ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BA9")

    label("loc_B20")


    #C0023
    ChrTalk(
        0xFE,
        (
            "ガイとアリオスは誰よりも、\x01",
            "他人の為に、クロスベルの為に\x01",
            "身を粉にしていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "そんな彼らに不幸がふりかかる……\x01",
            "やり切れん話じゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA9")

    Jump("loc_139E")

    label("loc_BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCA")

    #C0025
    ChrTalk(
        0xFE,
        (
            "今では有名なアリオスも、\x01",
            "昔はたまにガイに引っ張られて\x01",
            "わしらと一緒に酒を飲んだもんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "あやつは節度を弁えておってな。\x01",
            "わしとガイと酔っ払っておるのを、\x01",
            "すました顔で眺めておったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "ふふ、奴が酔って乱れた姿を\x01",
            "一度くらいは見たかったがのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D74")

    label("loc_CCA")


    #C0028
    ChrTalk(
        0xFE,
        (
            "昔はアリオスのやつも、\x01",
            "たまにガイに引っ張られて\x01",
            "ここで一緒に酒を飲んでおった。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "節度を弁えておる奴じゃから、\x01",
            "わしやガイのように\x01",
            "酔っ払ったりはせんかったがのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D74")

    Jump("loc_139E")

    label("loc_D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_E49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF3")

    #C0030
    ChrTalk(
        0xFE,
        "お前さんがた、今から墓参りか？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "夜になるとここは少々冷える。\x01",
            "早めに済ませるがええぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E44")

    label("loc_DF3")


    #C0032
    ChrTalk(
        0xFE,
        (
            "ここは高台にあるから、\x01",
            "夜になると少々冷える。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "早めに済ませるがええぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_E44")

    Jump("loc_139E")

    label("loc_E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_E57")
    Jump("loc_139E")

    label("loc_E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E65")
    Jump("loc_139E")

    label("loc_E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_103A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F92")

    #C0034
    ChrTalk(
        0xFE,
        (
            "《クロスベル問題》は、\x01",
            "そう呼ばれるようになる前から\x01",
            "長い間この地に根付いていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "帝国と共和国の度重なる紛争に\x01",
            "巻き込まれ、罪のない命が\x01",
            "数え切れぬほど失われてきたのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "わしはガイのおかげで\x01",
            "その悲しみを乗り越えられたが……\x01",
            "今も傷を抱えている者は多かろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1035")

    label("loc_F92")


    #C0037
    ChrTalk(
        0xFE,
        (
            "今来ておるリベールの姫さんは、\x01",
            "《クロスベル問題》の痛みを\x01",
            "我が身の様に考えておられる。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "まだ若いのに、大きな慈悲と慈愛に\x01",
            "満ち溢れたお方じゃと感じたわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1035")

    Jump("loc_139E")

    label("loc_103A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_10C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1055")
    Call(0, 7)
    Jump("loc_10BF")

    label("loc_1055")


    #C0039
    ChrTalk(
        0xFE,
        (
            "ふむ、しかしニールセン君が\x01",
            "帰って来ていたとはのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "どれ、今夜は色々と\x01",
            "話を聞かせてもらうぞい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BF")

    Jump("loc_139E")

    label("loc_10C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10D2")
    Jump("loc_139E")

    label("loc_10D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1189")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10ED")
    Call(0, 11)
    Jump("loc_1184")

    label("loc_10ED")


    #C0041
    ChrTalk(
        0xFE,
        (
            "ノーザンブリアの出身か……\x01",
            "この子も苦労したんじゃろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "さすがに子供相手に酒は出せんが、\x01",
            "次に遊びに来た時には茶菓子くらい\x01",
            "用意せねばのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1184")

    Jump("loc_139E")

    label("loc_1189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_1387")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A4")
    Call(0, 6)
    Jump("loc_1382")

    label("loc_11A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12DE")

    #C0043
    ChrTalk(
        0xFE,
        (
            "ガイが死んでしもうて、\x01",
            "わしも飲む酒の量が随分減った。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "気のいい飲み仲間を失うというのは、\x01",
            "やはり寂しいもんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x153,
        (
            "#01108Fおじーちゃん……\x02\x03",

            "#01100F……キーア、おっきくなったら\x01",
            "ロイドたちと一緒に飲みに来るから！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)

    #C0046
    ChrTalk(
        0xFE,
        (
            "はは、そうかそうか。\x01",
            "その時を楽しみに\x01",
            "待たせてもらうかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1382")

    label("loc_12DE")


    #C0047
    ChrTalk(
        0xFE,
        (
            "ほほ、お嬢ちゃんが\x01",
            "酒を飲めるようになる頃には\x01",
            "相当な別嬪#4Rべっぴん#さんになっとるじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "せいぜい長生きして、\x01",
            "その時を楽しみに\x01",
            "待たせてもらうかのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1382")

    Jump("loc_139E")

    label("loc_1387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1395")
    Jump("loc_139E")

    label("loc_1395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_139E")

    label("loc_139E")

    TalkEnd(0xFE)
    Return()

    # Function_5_5A8 end

    def Function_6_13A2(): pass

    label("Function_6_13A2")

    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0049
    ChrTalk(
        0x8,
        (
            "おお、お前さんはロイド……\x01",
            "久しぶりじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        "いつ戻ってきたんじゃ？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#00000Fええ、ついこの間です。\x01",
            "ご無沙汰していました。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x109,
        "#10105Fロイドさん、この方は……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_14B0")

    #C0053
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、以前ある依頼で\x01",
            "知り合ったのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B0")


    #C0054
    ChrTalk(
        0x101,
        (
            "#00000Fああ……\x01",
            "俺の兄貴と飲み仲間だった\x01",
            "クイントさんだよ。\x02\x03",

            "#00004F弟の俺にもよくしてくれててさ。\x01",
            "教団事件のあと一緒に飲んだときも\x01",
            "色々と昔話を聞かせてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        "あの時は楽しませてもらったぞい。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "まあ、ロイドはガイほど飲まんから\x01",
            "少々つまらんかったがのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00012Fはは……すいません。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、その時は私たちも\x01",
            "同席させてもらったの。\x02\x03",

            "#00109F未成年のティオちゃんは\x01",
            "ジュースだけで不満そうだったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、なるほどね。\x02\x03",

            "#10304Fまあ、これからは僕たちとも\x01",
            "よろしく頼むよ、ご老人。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        "うむ、ロイドの同僚なら大歓迎じゃ。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "普段、わしはこの墓地の管理をしておる。\x01",
            "気が向いたらいつでも来るがええ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 4)
    Return()

    # Function_6_13A2 end

    def Function_7_1736(): pass

    label("Function_7_1736")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0062
    ChrTalk(
        0x8,
        (
            "悪いのう、ニールセン君。\x01",
            "こんないい酒を。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        "かなり高いんじゃろう？\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "いえ、もらい物なので\x01",
            "気にしないでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "ここで飲んで頂けると\x01",
            "嬉しいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "ふぉふぉ、ならさっそく\x01",
            "今晩一緒に飲んでいかんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "ふふ、いいですね。\x01",
            "久しぶりにお相手させて頂きます。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    Return()

    # Function_7_1736 end

    def Function_8_186A(): pass

    label("Function_8_186A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_18FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1888")
    Call(0, 7)
    Jump("loc_18FA")

    label("loc_1888")


    #C0068
    ChrTalk(
        0xFE,
        (
            "ふふ、私などのくだらない話で\x01",
            "よければいくらでも。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "それにしても、クイントさんも\x01",
            "お元気そうで何よりです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18FA")

    TalkEnd(0xFE)
    Return()

    # Function_8_186A end

    def Function_9_18FE(): pass

    label("Function_9_18FE")

    Call(0, 10)
    Return()

    # Function_9_18FE end

    def Function_10_1902(): pass

    label("Function_10_1902")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1917")
    Call(0, 11)
    Jump("loc_1A89")

    label("loc_1917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F8")

    #C0070
    ChrTalk(
        0xA,
        (
            "#14008Fなんていうか……\x01",
            "クロスベルって本当に\x01",
            "不思議な街だよな。\x02\x03",

            "#14003F……とにかく、おかげさまで\x01",
            "今は目の前に目標と呼べるものも\x01",
            "できたんだ。\x02\x03",

            "#14002Fイリアさんに恩を返すためにも、\x01",
            "色々と頑張らないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A89")

    label("loc_19F8")


    #C0071
    ChrTalk(
        0xA,
        (
            "#14003F……とにかく、おかげさまで\x01",
            "今は目の前に目標と呼べるものも\x01",
            "できたんだ。\x02\x03",

            "#14002Fイリアさんに恩を返すためにも、\x01",
            "色々と頑張らないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A89")

    TalkEnd(0xA)
    Return()

    # Function_10_1902 end

    def Function_11_1A8D(): pass

    label("Function_11_1A8D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(258420, 1500, 830, 0)
    MoveCamera(28, 23, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33960, 0)
    SetChrPos(0x101, 258709, 0, 120, 0)
    SetChrPos(0x102, 259860, 0, -120, 0)
    SetChrPos(0x109, 259010, 0, -1110, 0)
    SetChrPos(0x105, 260160, 0, -1370, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu14000.itp")
    OP_4B(0x8, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xA, 0x64, 0x0)
    SetChrSubChip(0xA, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BFC")

    #C0072
    ChrTalk(
        0x101,
        (
            "#12P#00005Fあれ、君はシュリ……？\x01",
            "珍しいところで会うな。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        "#14000F……よう、あんたたちか。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        "#12P#00100Fえっと、一体どうしてここに？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DC5")

    label("loc_1BFC")


    #C0075
    ChrTalk(
        0x101,
        (
            "#12P#00005Fあれ、君はアルカンシェルの……\x01",
            "珍しいところで会うな。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xA,
        (
            "#14000F……あんたたちは、\x01",
            "イリアさんとリーシャ姉の\x01",
            "知り合いだったっけ。\x02\x03",

            "そういや自己紹介を\x01",
            "してなかったな。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0077
    AnonymousTalk(
        0xA,
        (
            "オレは劇団の下働きの\x01",
            "シュリ・アトレイドだ。\x02\x03",

            "……えっと、よろしく。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0078
    ChrTalk(
        0x102,
        (
            "#12P#00109Fふふ、よろしくねシュリちゃん。\x02\x03",

            "#00100Fえっと、一体どうしてここに？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC5")


    #C0079
    ChrTalk(
        0x8,
        (
            "この雨の中、傘も差さずに\x01",
            "墓地を歩いておったのでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "小屋に誘って、\x01",
            "温かいココアを淹れてやった\x01",
            "ところだったんじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)

    #C0081
    ChrTalk(
        0xA,
        (
            "#14002F……雨宿りさせてくれて\x01",
            "ありがとう、じーさん。\x02\x03",

            "#14004Fこのココアも……\x01",
            "おかげで体があったまったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)

    #C0082
    ChrTalk(
        0x8,
        "#11Pほっほ、それは何よりじゃ。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x109,
        "#12P#10100Fでも、どうして墓地に……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)

    #C0084
    ChrTalk(
        0xA,
        (
            "#14001F……本当は教会に\x01",
            "お祈りに行くつもりだったんだ。\x02\x03",

            "#14003Fでも、なんだか尻込みしちゃってさ。\x02\x03",

            "#14008F……ノーザンブリアには、\x01",
            "あそこまで立派な教会はなかったから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0085
    ChrTalk(
        0x101,
        "#12P#00001Fノーザンブリアって確か……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x105,
        "#12P#10303Fああ、大陸北部にある自治州だね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_210F")

    #C0087
    ChrTalk(
        0x102,
        (
            "#12P#00105Fそれじゃあ、シュリちゃんが\x01",
            "いたっていうスラムは……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        "#14008Fああ……オレはそこの出身なんだ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2147")

    label("loc_210F")


    #C0089
    ChrTalk(
        0xA,
        (
            "#14008Fああ……オレはあそこの\x01",
            "スラムの出身なんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2147")


    #C0090
    ChrTalk(
        0x109,
        "#12P#10108Fそうだったんだ……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "#11Pふむ、ノーザンブリアは\x01",
            "色々と厳しい場所と聞くが……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xA,
        (
            "#14003Fああ……\x01",
            "それもとんでもなく、な。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    #C0093
    ChrTalk(
        0xA,
        (
            "#14008Fあそこでは、みんな\x01",
            "その日を生きるのに必死だった。\x02\x03",

            "人を気遣ってる余裕なんて……\x01",
            "これっぽっちもなかった。\x02\x03",

            "#14003F……よく分からないけど、\x01",
            "ここは本当に不思議な街だと思う。\x02\x03",

            "いけ好かないヤツも多いけど……\x02\x03",

            "オレなんかを劇団を入れてくれる\x01",
            "イリアさんみたいな人がいれば……\x02\x03",

            "こうして、わざわざ声をかけてくれる\x01",
            "じーさんみたいな人もいる。\x02\x03",

            "#14000Fそれに、いつの間にか\x01",
            "アーティストとしての稽古なんかも\x01",
            "付けて貰えるまでになったし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0094
    ChrTalk(
        0x101,
        (
            "#12P#00002Fアーティストの稽古を……\x01",
            "へえ、それは凄いじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "#14005Fあ、ああ……\x02\x03",

            "#14003Fただ、まだ何となく\x01",
            "戸惑いはあるんだけどさ。\x02\x03",

            "#14008Fオレみたいな人間が\x01",
            "アーティストを目指せるなんて……\x01",
            "考えたこともなかったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        "#12P#00108Fシュリちゃん……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        (
            "#14003Fま、あんまり悩んでも\x01",
            "仕方ないことだってのは\x01",
            "オレも分かってるんだけどさ。\x02\x03",

            "#14002Fそれにしても……\x01",
            "あんたたちも相当、\x01",
            "変わり者の部類だよな。\x02\x03",

            "こうやって、オレなんかの話に\x01",
            "わざわざ耳を傾けたりしてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#12P#00005Fそ、そうか……？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#12P#00100Fふふ、でも否定は\x01",
            "できないかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x109,
        (
            "#12P#10102F確かに、警察の中でも\x01",
            "支援課はかなりイレギュラーな\x01",
            "部署ですしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、それになんといっても\x01",
            "特にリーダーが変わり者だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#12P#00006Fワジ、お前が言うなって。\x02\x03",

            "#00000Fま、なんていうか\x01",
            "俺たちとシュリがこうして\x01",
            "知り合えたのも何かの縁だろう。\x02\x03",

            "もし、困ったことがあったら\x01",
            "いつでも相談してくれていいからな？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#11Pほっほ、この小屋にも、\x01",
            "いつでも来てくれていいからの。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "#11P今度は茶菓子の一つでも\x01",
            "用意させてもらおうじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)

    #C0105
    ChrTalk(
        0xA,
        "#14002Fはは……ありがとう。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x133, 6)
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x1, 0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x5A, 0x0)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 259230, 0, -370, 0)
    EventEnd(0x5)
    Return()

    # Function_11_1A8D end

    SaveToFile()

Try(main)
