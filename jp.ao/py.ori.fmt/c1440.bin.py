from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1440.bin",                # FileName
        "c1440",                    # MapName
        "c1440",                    # Location
        0x0031,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 49, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1440",                  # 0
        "アシュリー",             # 1
        "ジンゴ",                 # 2
        "ディーノ",               # 3
        "コウキ",                 # 4
        "ヴァン",                 # 5
        "ルゼ",                   # 6
    ))

    AddCharChip((
        "chr/ch09200.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch06800.itc",                   # 02
        "chr/ch23000.itc",                   # 03
        "chr/ch24700.itc",                   # 04
        "chr/ch30800.itc",                   # 05
    ))

    DeclNpc(-2859,   0,       13750,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(5670,    29,      8649,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       15090,   225,  389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(2000,    0,       15090,   0,    389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(9640,    0,       850,     180,  389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10279,   0,       -550,    315,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)

    DeclEvent(0x0000, 0, 21,  9.899999618530273,     14.0,                  -0.5,                  16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.4749999046325684,   -7.0,                  0.10000000149011612,   1.0])

    DeclActor(4590,    0,       7540,    1000,    5670,    1500,    8650,    0x007E, 0,  6,  0x0000)
    DeclActor(-51020,  0,       6820,    1200,    -51020,  1150,    6820,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(596, 0)                                        # 0

    ScpFunction((
        "Function_0_254",          # 00, 0
        "Function_1_304",          # 01, 1
        "Function_2_4F2",          # 02, 2
        "Function_3_5BB",          # 03, 3
        "Function_4_672",          # 04, 4
        "Function_5_26B9",         # 05, 5
        "Function_6_2935",         # 06, 6
        "Function_7_2939",         # 07, 7
        "Function_8_3BCC",         # 08, 8
        "Function_9_3EBF",         # 09, 9
        "Function_10_3F0F",        # 0A, 10
        "Function_11_417D",        # 0B, 11
        "Function_12_41D5",        # 0C, 12
        "Function_13_4245",        # 0D, 13
        "Function_14_42A1",        # 0E, 14
        "Function_15_441D",        # 0F, 15
        "Function_16_45C2",        # 10, 16
        "Function_17_4985",        # 11, 17
        "Function_18_4E60",        # 12, 18
        "Function_19_5B79",        # 13, 19
        "Function_20_5EAB",        # 14, 20
        "Function_21_6738",        # 15, 21
    ))


    def Function_0_254(): pass

    label("Function_0_254")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_28C"),
        (1, "loc_298"),
        (2, "loc_2A4"),
        (3, "loc_2B0"),
        (4, "loc_2BC"),
        (5, "loc_2C8"),
        (6, "loc_2D4"),
        (SWITCH_DEFAULT, "loc_2E0"),
    )


    label("loc_28C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_298")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_303")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_303")

    Return()

    # Function_0_254 end

    def Function_1_304(): pass

    label("Function_1_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_312")
    Jump("loc_4DB")

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_320")
    Jump("loc_4DB")

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32E")
    Jump("loc_4DB")

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346")
    SetChrFlags(0x8, 0x10)

    label("loc_346")

    Jump("loc_4DB")

    label("loc_34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_359")
    Jump("loc_4DB")

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A7")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, -2960, 20, 8530, 315)
    SetChrPos(0xD, -3010, 30, 7170, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A2")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_3A2")

    Jump("loc_4DB")

    label("loc_3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_441")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -2240, 20, 13000, 225)
    SetChrPos(0xB, -2630, 20, 11000, 0)
    SetChrPos(0xA, -3850, 0, 11830, 45)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_406")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_406")

    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, 4930, 0, 4600, 315)
    SetChrPos(0xD, 5930, 0, 4600, 315)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4DB")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_454")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4DB")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_491")
    SetChrPos(0x8, 1750, 30, 10220, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D")
    SetChrFlags(0x8, 0x10)

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C")
    SetChrFlags(0x9, 0x10)

    label("loc_48C")

    Jump("loc_4DB")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_49F")
    Jump("loc_4DB")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4AD")
    Jump("loc_4DB")

    label("loc_4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4BB")
    Jump("loc_4DB")

    label("loc_4BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D6")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_4D6")

    SetChrFlags(0x8, 0x10)

    label("loc_4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F1")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_4F1")

    Return()

    # Function_1_304 end

    def Function_2_4F2(): pass

    label("Function_2_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_505")
    OP_1B(0x0, 0x0, 0x13)

    label("loc_505")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_51E")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_524")

    label("loc_51E")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 7)), scpexpr(EXPR_END)), "loc_532")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_57B")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BA")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_5BA")

    Return()

    # Function_2_4F2 end

    def Function_3_5BB(): pass

    label("Function_3_5BB")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『わくわくファミリーランチ』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_66E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『行楽ランチボックス』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_66E")

    TalkEnd(0xFF)
    Return()

    # Function_3_5BB end

    def Function_4_672(): pass

    label("Function_4_672")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_693")
    Call(0, 18)
    Return()

    label("loc_693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A5")
    Call(0, 20)
    Return()

    label("loc_6A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_811")

    #C0003
    ChrTalk(
        0xFE,
        (
            "大統領の拘束と同時に、\x01",
            "あんな《大樹》なんぞが\x01",
            "現れちまうとはねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "結界が消えて２大国への警戒も\x01",
            "しなきゃならないって時に……\x01",
            "つくづく難儀な地だよ、ここは。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "クク……面白くなってきたじゃないか。\x01",
            "こうなったら武器商人として、\x01",
            "とことん関わらせてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#00300Fはは、頼もしいねえ。\x01",
            "……また色々と都合を頼むぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8BE")

    label("loc_811")


    #C0007
    ChrTalk(
        0xFE,
        (
            "２大国への警戒も高まる今、\x01",
            "アタシの仕事も需要が高まりそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "クク……面白くなってきたじゃないか。\x01",
            "こうなったら武器商人として、\x01",
            "とことん関わらせてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BE")

    Jump("loc_26B5")

    label("loc_8C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C15")

    #C0009
    ChrTalk(
        0xFE,
        "おや、アンタたちか。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "クク……久しぶりだねえ。\x01",
            "意外と元気そうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#00000Fアシュリーさん、お久しぶりです。\x02\x03",

            "#00012F……というか、この状況に\x01",
            "全く動じてないみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2B")

    #C0012
    ChrTalk(
        0x10A,
        (
            "#00600F彼女には、警察の地下活動を\x01",
            "サポートしてもらっていた。\x02\x03",

            "#00603F起こりうる事態を予測していても\x01",
            "なんら不思議はあるまい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A90")

    label("loc_A2B")


    #C0013
    ChrTalk(
        0xFE,
        "ま、うすうす感づいてた事態だしね。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "ダドリーたちの地下活動を\x01",
            "手伝ってるんだから、当然だろ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A90")


    #C0015
    ChrTalk(
        0x102,
        "#00105Fそ、そうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        (
            "#00200F民間にもそれなりに\x01",
            "協力者がいるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#00300Fま、あんたなら地下組織相手の\x01",
            "商売なんかも慣れてるだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "クク、そういうことさ。\x01",
            "おかげで儲けさせてもらってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "……うちも万が一に備えて、\x01",
            "色々と準備している最中だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "倉庫の奥から引っ張り出した\x01",
            "それなりにいいブツも揃ってる。\x01",
            "必要ならジンゴと交渉しな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 4)
    Jump("loc_CA6")

    label("loc_C15")


    #C0021
    ChrTalk(
        0xFE,
        (
            "うちも万が一に備えて、\x01",
            "色々と準備している最中だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "倉庫の奥から引っ張り出した\x01",
            "それなりにいいブツも揃ってる。\x01",
            "必要ならジンゴと交渉しな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA6")

    Jump("loc_26B5")

    label("loc_CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3D")

    #C0023
    ChrTalk(
        0xFE,
        (
            "クロスベルの独立か……\x01",
            "ハッ、あの銀行屋も\x01",
            "大した決断をしたもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "……クク、赤毛の。\x01",
            "あんたなら気づいてるだろう？\x01",
            "戦場が近づいてくる匂いにさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#00301F……確かにな。\x01",
            "２大国も黙ってるとは思えねえし……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "クク、武器商人としての血ってヤツが\x01",
            "どうにもたぎってきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "クロスベルを出ることも考えたが、\x01",
            "こうなったらトコトン\x01",
            "付き合わせてもらうとするかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EF7")

    label("loc_E3D")


    #C0028
    ChrTalk(
        0xFE,
        (
            "戦場の近づいてくる匂い……\x01",
            "クク、武器商人としての血ってヤツが\x01",
            "たぎってきちまいやがった。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "クロスベルを出ることも考えたが、\x01",
            "こうなったらトコトン\x01",
            "付き合わせてもらうとするかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF7")

    Jump("loc_26B5")

    label("loc_EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1582")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D2")
    OP_4B(0xFE, 0xFF)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 0)

    #C0030
    ChrTalk(
        0xFE,
        "ああ、特務支援課か。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "この間の襲撃事件だが……\x01",
            "アンタたちはどう見てる？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00003F……そうですね。\x02\x03",

            "#00001Fまだ色々と分からない部分は\x01",
            "多いといったところですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#00101Fただ、事件を起こしたのが\x01",
            "《赤い星座》であることは\x01",
            "紛れもない事実です。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#00203Fそうなると雇い主、\x01",
            "つまり帝国政府の差し金と\x01",
            "考えるのが自然かもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "ああ、既に市民の間でも\x01",
            "似たような噂が広まってるようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "ヤツらがさっさと撤収した辺り\x01",
            "どうにも釈然としないが……\x01",
            "フン、まあいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#00305Fそういやアンタ、\x01",
            "このあたりで魔人化したヴァルドと\x01",
            "やり合ったんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "ああ、やっぱりアレは\x01",
            "ヴァルドに間違いなかったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "アイツには苦戦させられたが……\x01",
            "例の妙な薬を使ってたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "あんな化け物になっちまう薬を\x01",
            "一体どこで手に入れたのやら。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        (
            "#10108Fそれもそうなんですよね……\x02\x03",

            "#10106F捜査は続けているんですが、\x01",
            "未だに入手ルートは\x01",
            "明らかになっていなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "ハ、アンタらもそんなもんか。\x01",
            "全く分からないことばかりで\x01",
            "イヤになっちまうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "とにかく、あの事件以降\x01",
            "自治州の治安問題が再燃したせいで、\x01",
            "商売にならなくなってきた。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "長く拠点にしてた旧市街も\x01",
            "こんなことになっちまったし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0045
    ChrTalk(
        0xFE,
        (
            "……そろそろ、\x01",
            "ここを離れる頃合いかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#00005Fアシュリーさん……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x105,
        "#10303F……まあ、仕方ないかもしれないね。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#00300Fアンタなら\x01",
            "色々とツテはあるんだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "まあ、まだ決めたワケじゃないけどね。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "ジンゴのこともあるし、\x01",
            "そのうち身の振り方を決めないとね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x18D, 6)
    Jump("loc_157D")

    label("loc_14D2")


    #C0051
    ChrTalk(
        0xFE,
        (
            "……そろそろ、クロスベルを\x01",
            "離れる頃合いかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "分からないことばかりなのは\x01",
            "シャクだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "ジンゴのこともあるし、\x01",
            "そのうち身の振り方を決めないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157D")

    Jump("loc_26B5")

    label("loc_1582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1636")

    #C0054
    ChrTalk(
        0xFE,
        (
            "アンタら、あの物騒な連中と\x01",
            "コトを構えるってんなら、\x01",
            "ぜいぜい気合い入れて行きなよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "分かってるとは思うが、\x01",
            "生半可な覚悟じゃあ\x01",
            "叩き潰されるのがオチだからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B5")

    label("loc_1636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_16DE")

    #C0056
    ChrTalk(
        0xFE,
        (
            "通商会議以降、\x01",
            "若干だけどクロスベルに\x01",
            "ブツが流れにくくなってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "何でも裏で２大国が規制に\x01",
            "乗り出し始めたって話だけど、\x01",
            "カンベンして欲しいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B5")

    label("loc_16DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_18D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1823")

    #C0058
    ChrTalk(
        0xFE,
        (
            "そういえば昨日、例の通商会議で\x01",
            "暴れた『反移民政策主義』の残党が\x01",
            "捕まったらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "黒月を巻き込んで列車の中で\x01",
            "一騒動あったって話だけど、\x01",
            "もう少し静かに出来なかったのかねェ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_17F0")

    #C0060
    ChrTalk(
        0x101,
        (
            "#00012F（流石はアシュリーさん、\x01",
            "  耳が早いな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181B")

    label("loc_17F0")


    #C0061
    ChrTalk(
        0x101,
        "#00005F（そんなことがあったのか……）\x02",
    )

    CloseMessageWindow()

    label("loc_181B")

    SetScenarioFlags(0x0, 0)
    Jump("loc_18D1")

    label("loc_1823")


    #C0062
    ChrTalk(
        0xFE,
        (
            "昨日、例の通商会議で暴れた\x01",
            "『反移民政策主義』の残党が\x01",
            "捕まったらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "黒月を巻き込んで列車の中で\x01",
            "一騒動あったって話だけど、\x01",
            "もう少し静かに出来なかったのかねェ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D1")

    Jump("loc_26B5")

    label("loc_18D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_196D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F1")
    Call(0, 10)
    Jump("loc_1968")

    label("loc_18F1")


    #C0064
    ChrTalk(
        0xFE,
        (
            "それにしても、\x01",
            "今日は何だか変に賑やかだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "ここはいつからガキンチョ共の\x01",
            "たまり場になったんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1968")

    Jump("loc_26B5")

    label("loc_196D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_197B")
    Jump("loc_26B5")

    label("loc_197B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1996")
    Call(0, 5)
    Jump("loc_19EE")

    label("loc_1996")


    #C0066
    ChrTalk(
        0xFE,
        (
            "そういえば、\x01",
            "自分で動かしたんだっけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "アタシも、もう歳かねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EE")

    Jump("loc_26B5")

    label("loc_19F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_1BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B57")

    #C0068
    ChrTalk(
        0xFE,
        (
            "店の上で騒がしいヤツがいたから\x01",
            "ここからぶっ放して\x01",
            "やろうかと思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "屋根に穴が空くのもなんだし\x01",
            "ジンゴに任せたのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00006Fさ、さすがに街中での発砲は\x01",
            "見過ごせませんけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "フン、だからやってないだろう？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……にしてもあの金髪、\x01",
            "どっかで見たことあるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "まあ、気のせいだろうけどね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BB4")

    label("loc_1B57")


    #C0074
    ChrTalk(
        0xFE,
        (
            "……にしてもあの金髪、\x01",
            "どっかで見たことあるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "まあ、気のせいだろうけどね。\x02",
    )

    CloseMessageWindow()

    label("loc_1BB4")

    Jump("loc_1C3E")

    label("loc_1BB9")


    #C0076
    ChrTalk(
        0xFE,
        (
            "各国のＶＩＰが\x01",
            "クロスベルに勢揃い、か……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "正直何が起こるか読めないが、\x01",
            "何かしら巻き込まれることだけは\x01",
            "カンベン願いたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C3E")

    Jump("loc_26B5")

    label("loc_1C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6D")
    OP_4B(0xFE, 0xFF)

    #C0078
    ChrTalk(
        0xFE,
        "おや、赤毛じゃないか。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "どうやら支援課に\x01",
            "復帰したみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#00300Fああ、おかげさんでな。\x02\x03",

            "#00306Fそれにしても……\x01",
            "相変わらずキナ臭ぇ店だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "ハ、悪かったね。\x01",
            "生憎こちとら零細経営なもんで\x01",
            "上辺を気遣ってる余裕がないのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "ところでアンタ、裏通りには……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "……ああ、やっぱよそう。\x01",
            "下手に首を突っ込むと、\x01",
            "面倒が増えるだけだからねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        (
            "#00303F（……ハッ、この様子だと\x01",
            "  俺と《赤い星座》の関係も\x01",
            "  一通り調べがついてるみてえだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#00101F（一体どこまで\x01",
            "  知っているんでしょうね……）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x14D, 4)
    Jump("loc_1F13")

    label("loc_1E6D")


    #C0086
    ChrTalk(
        0xFE,
        (
            "しかし、通商会議とやらのせいで\x01",
            "今日は普段見ない警官連中が\x01",
            "出張って来てるみたいだねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "店の方にでも来ようもんなら\x01",
            "あしらうのが面倒臭そうだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F13")

    Jump("loc_26B5")

    label("loc_1F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2389")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2285")
    OP_4B(0xFE, 0xFF)

    #C0088
    ChrTalk(
        0xFE,
        (
            "そういえば、アンタら……\x01",
            "チビッ子と赤毛はどうしてんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x109,
        "#10106Fチ、チビッ子と赤毛……？\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#00000Fああ……\x01",
            "ティオとランディですね。\x02\x03",

            "#00003F２人はまだ、それぞれ\x01",
            "別の仕事が残っていまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        (
            "#00100Fええ、合流するのは\x01",
            "もう少し後になりそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "なるほどね、さすがに\x01",
            "チビッ子の方は分からないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "赤毛の方は大方、\x01",
            "警備隊のリハビリ訓練にでも\x01",
            "付き合ってるって所か。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0094
    ChrTalk(
        0x101,
        "#00005Fど、どうしてそこまで……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x105,
        "#10302Fフフ、流石に伊達じゃないね。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "まあ、この商売をやってると\x01",
            "そのへんの当たりは付くさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        "ふむ………\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        "#00105Fアシュリーさん？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        "ああ……いや、何でもないさ。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "まあ、ともかく仕事に\x01",
            "精を出してるんなら何よりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "とりあえず、アンタらも\x01",
            "あの男に遅れを取らないように\x01",
            "せいぜい鍛えておくんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#00000Fえ、ええ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x137, 6)
    Jump("loc_2384")

    label("loc_2285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_234B")

    #C0103
    ChrTalk(
        0xFE,
        (
            "ああ、これ以上アタシから\x01",
            "何か引き出そうとしても\x01",
            "無駄だからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "不確かな事は言いたかないし、\x01",
            "義理ってモンもある。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "ま、あとはせいぜい\x01",
            "自分たちの力で追ってみるんだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2384")

    label("loc_234B")


    #C0106
    ChrTalk(
        0xFE,
        (
            "ま、あとはせいぜい\x01",
            "自分たちの力で追ってみるんだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2384")

    Jump("loc_26B5")

    label("loc_2389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_26B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2639")
    OP_4B(0xFE, 0xFF)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0107
    ChrTalk(
        0xFE,
        "おや、特務支援課か。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "しばらく見なかったけど\x01",
            "久しぶりじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#00009Fはは……\x01",
            "ご無沙汰しています。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)

    #C0110
    ChrTalk(
        0xFE,
        (
            "フフ、噂には聞いてたけど\x01",
            "まさかアンタが入るとはねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "どういう風の吹き回しだい、\x01",
            "ワジ・ヘミスフィア？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x105,
        (
            "#10304Fま、思うところがあってね。\x02\x03",

            "#10302F今度トリニティあたりで\x01",
            "ツマミに話させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "フン、まあいいか。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "それで？\x01",
            "あたしに何か用かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "ルバーチェの放出品なら\x01",
            "一通り捌#2Rさば#いちまったけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#00006F（そんな事をしてたのか……）\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        (
            "#00100Fいえ、今日は特には。\x01",
            "お邪魔してすみませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "そうかい。\x01",
            "ま、それじゃ適当に\x01",
            "店の品でも見て行くんだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x137, 5)
    Jump("loc_26B5")

    label("loc_2639")

    TurnDirection(0xFE, 0x105, 0)

    #C0119
    ChrTalk(
        0xFE,
        (
            "しかしワジ、まさかアンタが\x01",
            "特務支援課に入るとはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "こりゃあ、近い内に\x01",
            "雪でも降るんじゃないのかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)

    label("loc_26B5")

    TalkEnd(0xFE)
    Return()

    # Function_4_672 end

    def Function_5_26B9(): pass

    label("Function_5_26B9")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x9, 0)

    #C0121
    ChrTalk(
        0x8,
        (
            "おう、ジンゴ。\x01",
            "昨日運び込んだグレネード弾は\x01",
            "どこへやったか覚えてるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "確かこの辺りに\x01",
            "置いたはずと思うんだが……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 0)

    #C0123
    ChrTalk(
        0x9,
        "ママ、覚えてねーの？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "そこじゃ邪魔になるからって\x01",
            "あとでママが自分で地下倉庫に\x01",
            "移動させたんじゃん。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0125
    ChrTalk(
        0x8,
        "ああ、そうだったっけか。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "サンクス、ジンゴ。\x01",
            "やっぱ持つべきものは娘だな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0127
    ChrTalk(
        0x101,
        (
            "#00006F（グレネード弾さえ除けば、\x01",
            "  普通の会話なんだけどな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        (
            "#00200F（相変わらず、\x01",
            "  この母娘は規格外ですね。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2912")
    OP_4C(0x9, 0xFF)

    label("loc_2912")

    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x87, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_5_26B9 end

    def Function_6_2935(): pass

    label("Function_6_2935")

    Call(0, 7)
    Return()

    # Function_6_2935 end

    def Function_7_2939(): pass

    label("Function_7_2939")

    TalkBegin(0x9)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2950")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BC8")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                # 0
            "交換する(装備)\x01",          # 1
            "交換する(クオーツ)\x01",      # 2
            "交換する(その他)\x01",        # 3
            "やめる\x01",                  # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29DE")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_29DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29FE")
    OP_AF(0x8C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BC3")

    label("loc_29FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A1E")
    OP_AF(0x96)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BC3")

    label("loc_2A1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A6A")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2FB, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AF(0xA3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2FB, 0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A62")
    ClearScenarioFlags(0x0, 1)

    label("loc_2A62")

    SetScenarioFlags(0x189, 5)

    label("loc_2A65")

    Jump("loc_2AAC")

    label("loc_2A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2A7A")
    OP_AF(0xA2)
    Jump("loc_2AAC")

    label("loc_2A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A8A")
    OP_AF(0xA1)
    Jump("loc_2AAC")

    label("loc_2A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A9A")
    OP_AF(0xA1)
    Jump("loc_2AAC")

    label("loc_2A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2AAA")
    OP_AF(0xA0)
    Jump("loc_2AAC")

    label("loc_2AAA")

    OP_AF(0xA0)

    label("loc_2AAC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BC3")

    label("loc_2ABB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ACF")
    Jump("loc_3BC3")

    label("loc_2ACF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BC3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_END)), "loc_2C9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C30")

    #C0129
    ChrTalk(
        0x9,
        (
            "おお……\x01",
            "やっぱカゲマルグッズは\x01",
            "イキでイナセだなー！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "そーいや倉庫にカタナあったっけ。\x01",
            "あれを持てばバッチリだなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        (
            "ヴァンとルゼにもこれ着せて、\x01",
            "チャンバラすっかー。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#00006Fこ、子供の遊びの範疇を\x01",
            "超えてるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        (
            "#00200Fカゲマルのキャラも\x01",
            "微妙に湾曲して伝わってますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C98")

    label("loc_2C30")


    #C0134
    ChrTalk(
        0x9,
        (
            "やっぱカゲマルグッズは\x01",
            "イキでイナセだなー！\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x9,
        (
            "ヴァンとルゼにもこれ着せて、\x01",
            "チャンバラすっかー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C98")

    Jump("loc_2F71")

    label("loc_2C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D88")

    #C0136
    ChrTalk(
        0x9,
        "お客ー、まっくろいネコ知ってる？\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#00000Fまっくろいネコ……？\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        (
            "#00200F……もしかして、\x01",
            "『カゲマル』のことでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        "それー。\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        "ジンゴ、それのフク探してんだ。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        "いっぱい集めてもってこいなー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x189, 6)
    Jump("loc_2F71")

    label("loc_2D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE2")

    #C0142
    ChrTalk(
        0x9,
        "お客ー、あのでっけー樹は見たかー？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x9,
        (
            "すっげーよなー。\x01",
            "あんだけの樹をなぎたおすのに、\x01",
            "導力砲が何門いるんだろうなー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0144
    ChrTalk(
        0x101,
        "#00006F（すごいワクワクしてる……）\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        "#00106F（相変わらず物騒な子ねぇ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F71")

    label("loc_2EE2")


    #C0146
    ChrTalk(
        0x9,
        (
            "あのでっけー樹をなぎたおすのに、\x01",
            "導力砲が何門いるんだろうなー？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "ニシシ……\x01",
            "帝国の戦車がたくさんあっても\x01",
            "ムヅカシーかもしれねーなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F71")

    Jump("loc_3BC3")

    label("loc_2F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3117")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D3")

    #C0148
    ChrTalk(
        0x9,
        "おー、お客かー？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            "外はなんかあぶねーみたいだぞ。\x01",
            "護身用になんか買ってけー。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "街の方に出てるヨロイをフッとばすなら、\x01",
            "炸裂手榴弾くらいはいるかもしんねーぞー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x101,
        "#00006F（それは多分、護身用じゃないと思う……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3112")

    label("loc_30D3")


    #C0152
    ChrTalk(
        0x9,
        (
            "外はなんかあぶねーみたいだぞ。\x01",
            "護身用になんか買ってけー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3112")

    Jump("loc_3BC3")

    label("loc_3117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3189")

    #C0153
    ChrTalk(
        0x9,
        (
            "ママと相談して、クロスベルに\x01",
            "残ることになったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        (
            "お客、何か\x01",
            "欲しいモンがあったら言えよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC3")

    label("loc_3189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_321C")

    #C0155
    ChrTalk(
        0x9,
        (
            "相変わらず、みんな\x01",
            "復興作業で忙しいみてえだなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        (
            "名誉のために言っとくけどな、\x01",
            "ママとジンゴもちょこちょこ\x01",
            "手伝ってんだぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC3")

    label("loc_321C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3317")

    #C0157
    ChrTalk(
        0x9,
        "ふわ～あ、ネムネム……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        (
            "昨日の夜は急な仕事が入って、\x01",
            "ママと倉庫をひっかき回してたから\x01",
            "あんま寝られてねえんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x9,
        (
            "でも、ママもあんな急な発注、\x01",
            "よく引き受けたよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x9,
        (
            "あのお客、\x01",
            "ママとそんな仲良かったっけか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_337F")

    label("loc_3317")


    #C0161
    ChrTalk(
        0x9,
        (
            "でも、ママもあんな急な発注、\x01",
            "よく引き受けたよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x9,
        (
            "あのお客、\x01",
            "ママとそんな仲良かったっけか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_337F")

    Jump("loc_3BC3")

    label("loc_3384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3408")

    #C0163
    ChrTalk(
        0x9,
        "むー、またシトシトいってんなー。\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x9,
        (
            "どうせ降るなら、もっと\x01",
            "ドバーッと降ってくれた方が\x01",
            "スッキリすんだけどなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC3")

    label("loc_3408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3486")
    OP_93(0x9, 0x10E, 0x0)

    #C0165
    ChrTalk(
        0x9,
        "しかし、あいつらも懲りねーなー。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "前にママの張り手くらったこと、\x01",
            "すっかり忘れてんじゃねーのか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC3")

    label("loc_3486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3501")

    #C0167
    ChrTalk(
        0x9,
        (
            "よー、お客ら。\x01",
            "こいつらのことは\x01",
            "気にしなくていいからなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x9,
        (
            "今日もいいブツあるから、\x01",
            "交換してけー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC3")

    label("loc_3501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_35EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A6")

    #C0169
    ChrTalk(
        0x9,
        "ママなら飲みに行ってんぞー。\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "今日は朝から在庫整理で\x01",
            "忙しかったからなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "ご褒美に、ちょいと一杯\x01",
            "引っかけて来るんだってさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_35E7")

    label("loc_35A6")


    #C0172
    ChrTalk(
        0x9,
        (
            "ママ、店の客には厳しいけど、\x01",
            "自分にはトコトン甘いからなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35E7")

    Jump("loc_3BC3")

    label("loc_35EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_366C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3607")
    Call(0, 5)
    Jump("loc_3667")

    label("loc_3607")

    TurnDirection(0x9, 0x0, 0)

    #C0173
    ChrTalk(
        0x9,
        "ママ、たまにど忘れすっからなー。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x9,
        (
            "ニシシ……\x01",
            "やっぱ、ジンゴがいねえとダメだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3667")

    Jump("loc_3BC3")

    label("loc_366C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_36F4")

    #C0175
    ChrTalk(
        0x9,
        (
            "あのキンパツ、\x01",
            "屋根からおちたのに\x01",
            "ワリと元気だったなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x9,
        (
            "もうすこし強く\x01",
            "蹴ってやればよかったかもなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C3")

    label("loc_36F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3781")

    #C0177
    ChrTalk(
        0x9,
        (
            "午前中は珍しく店閉めて、\x01",
            "ママと除幕式見てきたぞー。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x9,
        (
            "あのビル、\x01",
            "ほんとバカデケーのなー。\x01",
            "ジンゴもビックリしたぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_37C3")

    label("loc_3781")


    #C0179
    ChrTalk(
        0x9,
        (
            "あのビル、\x01",
            "ほんとバカデケーのなー。\x01",
            "ジンゴもビックリしたぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C3")

    Jump("loc_3BC3")

    label("loc_37C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_390C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3899")

    #C0180
    ChrTalk(
        0x9,
        (
            "新しいシスターのねーちゃんが\x01",
            "本読むから来いっつってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x9,
        (
            "いつもみたいに行かねーって言ったら、\x01",
            "宿題だって別の本を置いてったぞー。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x9,
        "なんだかあなどれねーヤツなー……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3907")

    label("loc_3899")


    #C0183
    ChrTalk(
        0x9,
        (
            "あのシスターのねーちゃん、\x01",
            "なんだかあなどれねーヤツなー……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        (
            "まー、せっかくだし……\x01",
            "この本読むかー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3907")

    Jump("loc_3BC3")

    label("loc_390C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3927")
    Call(0, 8)
    Jump("loc_3B01")

    label("loc_3927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A95")

    #C0185
    ChrTalk(
        0x9,
        (
            "雨のヤロー、じめじめじめじめ\x01",
            "うっとーしーぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x9,
        (
            "導力砲を撃ち込んで\x01",
            "雨雲を蒸発させれば晴れるかなー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0187
    ChrTalk(
        0x101,
        "#00005Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        (
            "#00106F（う～ん、\x01",
            "  何というかこの子には……）\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x109,
        (
            "#10106F（ええ……ちょっと\x01",
            "  ツッコミようがないですね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B01")

    label("loc_3A95")


    #C0190
    ChrTalk(
        0x9,
        (
            "雨のヤロー、じめじめじめじめ\x01",
            "うっとーしーぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x9,
        (
            "導力爆弾を使えば\x01",
            "雨雲を根こそぎ吹っ飛ばせるかなー？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B01")

    Jump("loc_3BC3")

    label("loc_3B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B21")
    Call(0, 8)
    Jump("loc_3BC3")

    label("loc_3B21")


    #C0192
    ChrTalk(
        0x9,
        (
            "分かってると思うけど、\x01",
            "お客らとできんのは\x01",
            "ブツの交換だけだかんなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        (
            "薬にクオーツにアクセサリ……\x01",
            "その他もテキトーに用意してるから\x01",
            "よかったら見てけー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BC3")

    Jump("loc_2950")

    label("loc_3BC8")

    TalkEnd(0x9)
    Return()

    # Function_7_2939 end

    def Function_8_3BCC(): pass

    label("Function_8_3BCC")


    #C0194
    ChrTalk(
        0x9,
        "おー、お客、久しぶりだなー。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x9,
        (
            "ブキは売れねえけど、\x01",
            "何か交換でもしてくかー？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "イッパン向けのブツも前よか\x01",
            "そこそこ揃ってんからなー。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C82")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3C82")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CA8")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3CA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CCE")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3CCE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CF4")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3CF4")

    Sleep(1000)

    #C0197
    ChrTalk(
        0x101,
        "#00006Fあ、相変わらず物騒な発言だな。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x109,
        (
            "#10106Fえっと、本当にこのお店を\x01",
            "利用してもいいんでしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#00100Fま、まあ、表に出ている商品は\x01",
            "違法なものではなさそうだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、ある程度なら\x01",
            "問題はないんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x9,
        (
            "あー、あとなー。\x01",
            "最近はウチも手広くやっててなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "うまそーなゴチソーとかも\x01",
            "あったら持ってこいなー？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x9,
        (
            "それなりにいーもんと\x01",
            "交換してやっから。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#00012Fはは、分かった。\x01",
            "また利用させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x137, 7)
    Return()

    # Function_8_3BCC end

    def Function_9_3EBF(): pass

    label("Function_9_3EBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED4")
    Call(0, 10)
    Jump("loc_3F0B")

    label("loc_3ED4")


    #C0205
    ChrTalk(
        0xFE,
        (
            "じゅ、１０万ミラか……\x01",
            "そんなの見たこともねえな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0B")

    TalkEnd(0xFE)
    Return()

    # Function_9_3EBF end

    def Function_10_3F0F(): pass

    label("Function_10_3F0F")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0206
    ChrTalk(
        0x8,
        (
            "ああ、お前たちが言ってるのは\x01",
            "このエニグマのことだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x8,
        (
            "ほれ、こうやって耳に当てりゃあ\x01",
            "通信器に早変わりってワケだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        "そ、そうだ、それに違いない。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xA,
        (
            "そういや、警察や遊撃士……\x01",
            "あとワジも使ってましたよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xA,
        (
            "ちなみにアシュリーさん。\x01",
            "これって、まともに買ったら\x01",
            "どれくらいするモンなんスかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x8,
        (
            "ん？　まあ基本は\x01",
            "オーダーメイドだからね。\x01",
            "最低でも１０万ミラって所か。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "ウチにあるワケアリ品なら\x01",
            "少しは融通が利くが……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x8,
        (
            "もしかして、\x01",
            "お前らコイツが欲しいのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xB,
        "じゅ、１０万……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xA,
        "い、１ミラチョコが１０万個……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "ははっ、お前ら\x01",
            "なかなかいい反応するじゃねえか。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x16E, 5)
    Return()

    # Function_10_3F0F end

    def Function_11_417D(): pass

    label("Function_11_417D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4192")
    Call(0, 10)
    Jump("loc_41D1")

    label("loc_4192")


    #C0217
    ChrTalk(
        0xFE,
        (
            "１ミラチョコが１０万個……\x01",
            "じゅ、１０万個ってどんな量だ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41D1")

    TalkEnd(0xFE)
    Return()

    # Function_11_417D end

    def Function_12_41D5(): pass

    label("Function_12_41D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4235")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F3")
    Call(0, 14)
    Jump("loc_4230")

    label("loc_41F3")


    #C0218
    ChrTalk(
        0xFE,
        (
            "くっそー、ジンゴの母ちゃん、\x01",
            "相変わらずおっかねえな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4230")

    Jump("loc_4241")

    label("loc_4235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4241")
    Call(0, 15)

    label("loc_4241")

    TalkEnd(0xFE)
    Return()

    # Function_12_41D5 end

    def Function_13_4245(): pass

    label("Function_13_4245")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4291")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4263")
    Call(0, 14)
    Jump("loc_428C")

    label("loc_4263")


    #C0219
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "また作戦シッパイだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_428C")

    Jump("loc_429D")

    label("loc_4291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_429D")
    Call(0, 15)

    label("loc_429D")

    TalkEnd(0xFE)
    Return()

    # Function_13_4245 end

    def Function_14_42A1(): pass

    label("Function_14_42A1")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0220
    ChrTalk(
        0xC,
        (
            "うおっ、これって導力銃じゃんか。\x01",
            "かっけーなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xD,
        (
            "ねえねえ、ヴァン。\x01",
            "それでニク焼けるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xC,
        (
            "んー、まあ楽勝じゃねえ？\x01",
            "ニヒヒ、今度こっそり試してみっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x8,
        "……おい、ガキンチョども。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 0)

    #C0224
    ChrTalk(
        0x8,
        (
            "その辺のモン、\x01",
            "勝手に触るんじゃねえぞ。（ギロリ）\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        "お、おお……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xD,
        (
            "クスクス……\x01",
            "ジンゴちゃんのお母さん、\x01",
            "迫力あるよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_93(0x8, 0x0, 0x0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_14_42A1 end

    def Function_15_441D(): pass

    label("Function_15_441D")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_452C")

    #C0227
    ChrTalk(
        0xC,
        (
            "よお、ジンゴ。\x01",
            "遊びに来てやったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xC,
        "なんか恵んでくれー。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x9,
        (
            "おー、おめえら。\x01",
            "ミラあんのかー？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xC,
        (
            "ヒャハハ、あったけど\x01",
            "昨日使っちまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xD,
        (
            "クスクス……\x01",
            "ニク食ったの、ニク。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x9,
        (
            "はぁ～、相変わらず\x01",
            "計画性ねえのな、おめえら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_45B5")

    label("loc_452C")


    #C0233
    ChrTalk(
        0xC,
        (
            "ゴタクはいいから\x01",
            "恵んでくれよ、ジンゴ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x9,
        (
            "んん～？　おめえらまだ\x01",
            "元気そうだからダメー。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xD,
        (
            "クスクス……\x01",
            "ジンゴちゃんのオニー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B5")

    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_15_441D end

    def Function_16_45C2(): pass

    label("Function_16_45C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_68(0, 1100, 12800, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -600, 0, 1800, 0)
    SetChrPos(0x102, 600, 0, 1800, 0)
    SetChrPos(0x109, 900, 0, 700, 0)
    SetChrPos(0x105, -900, 0, 700, 0)
    OP_68(0, 1100, 2800, 6000)
    MoveCamera(45, 19, 0, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0236
    ChrTalk(
        0x101,
        (
            "#12P#00001Fうーん、相変わらず\x01",
            "怪しい店だなぁ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    #C0237
    ChrTalk(
        0x102,
        (
            "#6P#00108F相変わらずジンゴちゃんが\x01",
            "店番をやっているのね……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x109,
        (
            "#12P#10103Fクロスベル市に幾つかある\x01",
            "闇ブローカーのひとつですね。\x02\x03",

            "#10101F武器弾薬も扱っているって\x01",
            "警備隊で噂されていますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x105,
        (
            "#12P#10304Fまあ、そういう店の中では\x01",
            "まだ良心的な方だよ。\x02\x03",

            "#10300F主人はかなりの女傑だけどね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47E5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_47E5)
    Sleep(50)

    def lambda_47F5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_47F5)
    Sleep(50)
    TurnDirection(0x102, 0x105, 500)

    #C0240
    ChrTalk(
        0x101,
        (
            "#5P#00003Fそうみたいだな……\x02\x03",

            "#00001Fとりあえず、用事があれば\x01",
            "さっさと済ませるか。\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    SetChrName("")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※交換屋《ナインヴァリ》では、\x01",
            "　特定のアイテムを消費する代わりに\x01",
            "　希少価値の高いアイテムが入手できます。\x02\x03",

            "※カウンターにいるジンゴに話しかけて\x01",
            "　『交換する』を選択すると、\x01",
            "　メニューが表示され、交換を行えます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 0, 0, 1000, 0)
    SetScenarioFlags(0x138, 4)
    EventEnd(0x5)
    Return()

    # Function_16_45C2 end

    def Function_17_4985(): pass

    label("Function_17_4985")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, -600, 0, 1800, 0)
    SetChrPos(0x102, 600, 0, 1800, 0)
    SetChrPos(0x109, 900, 0, 700, 0)
    SetChrPos(0x105, -900, 0, 700, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3F")
    OP_68(0, 1100, 12800, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(0, 1100, 2800, 6000)
    MoveCamera(45, 19, 0, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0242
    ChrTalk(
        0x101,
        (
            "#12P#00001Fうーん、相変わらず\x01",
            "怪しい店だなぁ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    #C0243
    ChrTalk(
        0x102,
        (
            "#6P#00108F相変わらずジンゴちゃんが\x01",
            "店番をやっているのね……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x109,
        (
            "#12P#10103Fクロスベル市に幾つかある\x01",
            "闇ブローカーのひとつですね。\x02\x03",

            "#10101F武器弾薬も扱っているって\x01",
            "警備隊で噂されていますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x105,
        (
            "#12P#10304Fまあ、そういう店の中では\x01",
            "まだ良心的な方だよ。\x02\x03",

            "#10300F主人はかなりの女傑だけどね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BB2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4BB2)
    Sleep(50)

    def lambda_4BC2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4BC2)
    Sleep(50)
    TurnDirection(0x102, 0x105, 500)

    #C0246
    ChrTalk(
        0x101,
        (
            "#5P#00003Fそうみたいだな……\x02\x03",

            "#00001Fとにかくアシュリーさんに\x01",
            "例の男について聞いてみよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0247
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※交換屋《ナインヴァリ》では、\x01",
            "　特定のアイテムを消費する代わりに\x01",
            "　希少価値の高いアイテムが入手できます。\x02\x03",

            "※カウンターにいるジンゴに話しかけて\x01",
            "　『交換する』を選択すると、\x01",
            "　メニューが表示され、交換を行えます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_4E46")

    label("loc_4D3F")

    OP_68(0, 1100, 2800, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0248
    ChrTalk(
        0x101,
        (
            "#12P#00006Fうーん、やっぱり\x01",
            "怪しい店だなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        (
            "#12P#00106Fそうね、何度来ても\x01",
            "慣れないというか……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0250
    ChrTalk(
        0x102,
        (
            "#11P#00101Fとりあえず、アシュリーさんに\x01",
            "例の男について聞いてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_4E46")

    SetChrPos(0x0, 0, 0, 1000, 0)
    SetScenarioFlags(0x138, 5)
    SetScenarioFlags(0x128, 3)
    EventEnd(0x5)
    Return()

    # Function_17_4985 end

    def Function_18_4E60(): pass

    label("Function_18_4E60")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-2860, 1000, 12800, 0)
    MoveCamera(37, 22, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -3100, 20, 11800, 0)
    SetChrPos(0x102, -4400, 20, 11000, 45)
    SetChrPos(0x109, -2900, 20, 10800, 0)
    SetChrPos(0x105, -1700, 20, 12000, 315)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5188")

    #C0251
    ChrTalk(
        0x8,
        "#5Pおや、特務支援課か。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x8,
        (
            "#5Pしばらく見なかったけど\x01",
            "久しぶりじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        (
            "#12P#00012Fはは……\x01",
            "ご無沙汰しています。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)
    Sleep(300)

    #C0254
    ChrTalk(
        0x8,
        (
            "#5Pフフ、噂には聞いてたけど\x01",
            "まさかアンタが入るとはねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        (
            "#5Pどういう風の吹き回しだい、\x01",
            "ワジ・ヘミスフィア？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x105,
        (
            "#10304Fま、思うところがあってね。\x02\x03",

            "#10302F今度トリニティあたりで\x01",
            "ツマミに話させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        "#5Pフン、まあいいか。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    #C0258
    ChrTalk(
        0x8,
        (
            "#5Pそれで？\x01",
            "あたしに何か用かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x8,
        (
            "#5Pルバーチェの放出品なら\x01",
            "一通り捌#2Rさば#いちまったけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        "#12P#00006F（そんな事をしてたのか……）\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x102,
        (
            "#6P#00103F実は、アシュリーさんに\x01",
            "伺いたいことがあるんです。\x02\x03",

            "#00100F元武器商人としての貴女に。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x137, 5)
    Jump("loc_5228")

    label("loc_5188")


    #C0262
    ChrTalk(
        0x8,
        "#5Pん、特務支援課か。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x8,
        "#5Pあたしに何か用かい？\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        (
            "#6P#00103Fはい、実はアシュリーさんに\x01",
            "伺いたいことがあるんです。\x02\x03",

            "#00100F元武器商人としての貴女に。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5228")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0265
    ChrTalk(
        0x8,
        "#5Pふーん、何だい？\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x8,
        (
            "#5Pツァオたちが本格的に\x01",
            "動き始めた件についてかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#12P#00003Fさすがにご存知でしたか。\x02\x03",

            "#00001F多分、それとは\x01",
            "別件だとは思うんですが……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_64(0x8)

    #C0268
    ChrTalk(
        0x8,
        "#5P隻眼#4Rせきがん#……赤毛の偉丈夫#6Rいじょうぶ#か……\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x8,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#12P#00001F心当たりはありませんか？\x02\x03",

            "裏社会に属する男なのは\x01",
            "間違いなさそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#5P該当しそうなヤツだったら\x01",
            "何人か心当たりがある。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x8,
        (
            "#5Pだが、今この状況で\x01",
            "クロスベルに来るとしたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x8,
        "#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x102,
        "#6P#00108Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x105,
        (
            "#10305Fへえ、そんなにヤバイ\x01",
            "心当たりがあるのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x8,
        "#5Pさてね……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x8,
        (
            "#5Pただ、あたしの想像が\x01",
            "もし最悪のケースだった場合。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x8,
        (
            "#5Pアンタらの手に負える相手じゃ\x01",
            "無いのは間違いないだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x102,
        "#6P#00101Fそこまで……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x109,
        (
            "#12P#10101Fや、やはり猟兵か\x01",
            "テロリストあたりですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        "#5Pフフ、さてねぇ。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "#5Pもしその男だった場合、\x01",
            "一応、こちらも付き合いがある。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x8,
        "#5Pペラペラ喋るわけには行かないさ。\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x109,
        "#12P#10107Fで、でも……！\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#12P#00006F──猟兵ならともかく\x01",
            "テロリストなら放置できません。\x02\x03",

            "#00003Fいくらクロスベルとはいえ、\x01",
            "テロ行為を罰する法律はあります。\x02\x03",

            "#00013F最低限の情報だけでも\x01",
            "教えてもらうわけにはいきませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        "#6P#00108Fロイド……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x8,
        "#5Pふふ、悪くない。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x8,
        (
            "#5P──ガイの弟だったか。\x01",
            "いい眼をするようになったね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0289
    ChrTalk(
        0x101,
        (
            "#12P#00005Fアシュリーさん、\x01",
            "兄貴と面識が……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "#5P今じゃダドリーあたりも\x01",
            "たまに顔を見せるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x8,
        (
            "#5P当時、旧市街くんだりまで\x01",
            "足を運んでくる酔狂な捜査官は\x01",
            "ヤツくらいだったからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        "#5P面白い男を亡くしたもんだよ。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        "#12P#00008F………………………………\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x8,
        (
            "#5Pあの馬鹿に免じて\x01",
            "これだけは答えてやろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x8,
        (
            "#5Pあたしの最悪の心当たりは\x01",
            "テロリストってわけじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x8,
        (
            "#5Pただ、人食い虎みたいな\x01",
            "危険な男ではあるけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x109,
        "#12P#10108Fひ、人喰い虎……\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x105,
        (
            "#10306Fやれやれ……\x01",
            "最悪な相手じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x8,
        (
            "#5Pま、その男かどうかは\x01",
            "まだ決まったわけじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x8,
        (
            "#5Pアンタたちが見た男ってのは\x01",
            "一人きりだったんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x8,
        (
            "#5Pヤツなら大抵、部下か連れが\x01",
            "同行しているはずだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        "#12P#00005Fそ、そうなんですか？\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x102,
        (
            "#6P#00101Fとなると……\x01",
            "やはり軍隊関係者ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x8,
        "#5Pフフ、ここまでだ。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x8,
        (
            "#5Pこれ以上は自分たちの力で\x01",
            "迫ってみるんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        "#12P#00006F……分かりました。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        "#6P#00104F情報、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -2860, 20, 11750, 180)
    SetScenarioFlags(0x128, 4)
    OP_1B(0x0, 0x0, 0x13)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_4E60 end

    def Function_19_5B79(): pass

    label("Function_19_5B79")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(300, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_68(0, 1200, 500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    Sleep(500)
    OP_68(5100, 1200, 8100, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(150)

    #C0308
    ChrTalk(
        0x9,
        "#5Pむー、シトシトいってんなー。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(300)

    #C0309
    ChrTalk(
        0x9,
        (
            "#11Pそうだママ、昨日とどいたブツ、\x01",
            "荷ほどきしなくていーのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x0)

    #C0310
    ChrTalk(
        0x8,
        (
            "ああ、この天気だし\x01",
            "急ぐことはないだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x8,
        "……それよりジンゴ。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        (
            "アンタ昨日、街に出たとき、\x01",
            "変なヤツを見かけなかったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x9,
        (
            "#11Pヘンなヤツ？\x01",
            "そんなのいっぱいいたぞー？\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x9,
        (
            "#11Pバカンスルックの若ぞーとか\x01",
            "パンを山ほど買ってた\x01",
            "シスターのねーちゃんとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x9,
        "#11Pあのワジもヘンなヤツだしなー。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x8,
        "そうか、ならいいんだ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(-2860, 1200, 13750, 3500)
    MoveCamera(15, 26, 0, 3500)
    OP_6F(0x79)
    OP_64(0x8)
    Sleep(500)

    #C0317
    ChrTalk(
        0x8,
        "#5P（……まあ、気にしすぎか。）\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "#5P（もしヤツが来たんだとしたら\x01",
            "  娘も連れているだろうからね。）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetScenarioFlags(0x22, 0)
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_5B79 end

    def Function_20_5EAB(): pass

    label("Function_20_5EAB")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-2860, 1000, 12800, 0)
    MoveCamera(37, 22, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -3100, 20, 11800, 0)
    SetChrPos(0x102, -4400, 20, 11000, 45)
    SetChrPos(0x103, -3700, 20, 10500, 0)
    SetChrPos(0x109, -2600, 20, 10800, 0)
    SetChrPos(0x105, -1900, 20, 12000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0319
    ChrTalk(
        0x8,
        "#5Pおや……\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x8,
        (
            "#5P……さすがというか、\x01",
            "早速、辿りついたかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        (
            "#12P#00001Fということは……\x01",
            "やはりランディはこちらに？\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        (
            "#5Pああ、昨日の夜に連絡があって\x01",
            "朝早くブツを受け取っていったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x8,
        (
            "#5Pアンタらが訪ねてきたら\x01",
            "シラを切って欲しいと頼まれたが\x01",
            "そこまでの義理は無いしねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x105,
        "#10309Fアハハ、確かに。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x102,
        (
            "#6P#00101Fそれで……結局ランディは\x01",
            "何を注文したんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x103,
        "#12P#00201Fやはり導力式のライフルとか？\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x8,
        (
            "#5Pいや、そんな真っ当な\x01",
            "シロモンじゃなかったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x8,
        (
            "#5P炸裂弾やら徹甲弾、\x01",
            "グレネード弾なんかは勿論、\x01",
            "火薬を使った旧式の弾薬まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        (
            "#5P店にあった在庫を\x01",
            "洗いざらい買い占めていったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        (
            "#5Pそれと闇に流れていた\x01",
            "無登録の《エニグマⅡ》だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#12P#00006Fなるほど……\x02\x03",

            "#00008F……さすがに用意周到だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        (
            "#12P#00206Fええ……無登録のエニグマでは\x01",
            "こちらも番号が分かりませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x109,
        (
            "#12P#10105Fでも、重火器の本体#4R㈲　㈲#は\x01",
            "購入していかなかったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        (
            "#5Pああ、ウチもそれなりに強力な\x01",
            "導力式・火薬式のライフルを\x01",
            "扱っているつもりだったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x8,
        (
            "#5P《赤い星座》の次期団長には\x01",
            "お気に召さなかったようだねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0336
    ChrTalk(
        0x101,
        "#12P#00011Fアシュリーさん……\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x102,
        "#6P#00106Fご存知だったんですか……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#5Pハ、あたりまえだろ。\x01",
            "こちとら情報が命だからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x8,
        (
            "#5Pどうやら古巣に一泡吹かせる\x01",
            "つもりみたいだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x8,
        (
            "#5P《赤の戦鬼#8Rオーガ・ロッソ#》と\x01",
            "《血染めの#8Rブ ラ ッ デ ィ#シャーリィ》といえば\x01",
            "正真正銘の化物どもだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x8,
        (
            "#5P半端な元猟兵ごときじゃ\x01",
            "間違いなく返り討ちだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        "#12P#00201F……させません。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        (
            "#12P#00013Fそうさせないために\x01",
            "俺たちがいるつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、さっきから\x01",
            "ずっとこの調子でね。\x02\x03",

            "#10302F挑発してもムダみたいだよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x8,
        "#5Pやれやれ、そうみたいだね。\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x8,
        (
            "#5Pま、あの若造がくたばろうが\x01",
            "アタシの知ったこっちゃないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "#5Pお得意様が減ってもつまらない。\x01",
            "せいぜい助けてやるんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x109,
        "#12P#10101Fはい……！\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        "#6P#00103F情報、ありがとうございました。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -2860, 20, 11750, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x165, 6)
    OP_29(0xAA, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_20_5EAB end

    def Function_21_6738(): pass

    label("Function_21_6738")

    EventBegin(0x1)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67F8")

    #C0350
    ChrTalk(
        0x9,
        "倉庫に入るつもりかー？\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x9,
        (
            "んー……\x01",
            "ま、お客ならいっかー。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x9,
        (
            "ヘンなもんさわんなよー。\x01",
            "死んでもしらねーから。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        "#00012F……お、お心遣い感謝します。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x189, 7)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_6901")

    label("loc_67F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6891")

    #C0354
    ChrTalk(
        0x9,
        (
            "……おい、お客。\x01",
            "ジンゴの目はごまかせねえかんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x9,
        (
            "そっちは地下倉庫、\x01",
            "カンケー者以外立ち入り禁止だ。\x01",
            "買い物なら、ここでしろ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6901")

    label("loc_6891")


    #C0356
    ChrTalk(
        0x9,
        (
            "おい、お客？\x01",
            "ジンゴのハナシ聞いてたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x9,
        (
            "地下倉庫はいんなっつってるだろ！！\x01",
            "買い物なら、ここでしろ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6901")

    Sleep(50)
    SetChrPos(0x0, 9940, 0, 11910, 180)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_21_6738 end

    SaveToFile()

Try(main)
