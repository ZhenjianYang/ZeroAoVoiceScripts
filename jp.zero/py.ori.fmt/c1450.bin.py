from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1450.bin",                # FileName
        "c1450",                    # MapName
        "c1450",                    # Location
        0x0033,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 51, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1450",                  # 0
        "タントス老人",           # 1
        "ガイトナー",             # 2
        "コロナ",                 # 3
        "リマ",                   # 4
        "メルスン",               # 5
        "タントス老人",           # 6
        "ミショー",               # 7
        "ガイトナー",             # 8
        "リーシャ",               # 9
        "議員風の男",             # 10
        "スーツの男",             # 11
        "男の声",                 # 12
    ))

    AddCharChip((
        "chr/ch24000.itc",                   # 00
        "chr/ch24002.itc",                   # 01
        "chr/ch21000.itc",                   # 02
        "chr/ch21002.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch24402.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch27700.itc",                   # 09
        "chr/ch27600.itc",                   # 0A
        "chr/ch23000.itc",                   # 0B
        "chr/ch24700.itc",                   # 0C
        "chr/ch05200.itc",                   # 0D
    ))

    DeclNpc(4269,    0,       -52159,  90,   261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(52340,   29,      959,     180,  261,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(51200,   0,       54049,   0,    261,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10270,   3500,    11050,   135,  261,  0x0, 0,   7,   0,   0,   2,   0,   13,  255,  0)
    DeclNpc(9609,    3500,    13869,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-1399,   200,     -55000,  90,   389,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-46349,  200,     1899,    180,  261,  0x0, 0,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(1549,    200,     -55159,  270,  389,  0x0, 0,   3,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-1639,   29,      56029,   0,    389,  0x0, 0,   13,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(3809,    0,       1059,    135,  389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(2700,    0,       1490,    135,  389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(17899,   3500,    -39,     0,    126,  0x0, 0,   10,  0,   255, 255, 255, 255, 255,  0)

    DeclActor(17900,   3500,    -40,     1500,    17900,   4800,    -40,     0x007C, 0,  16, 0x0000)
    DeclActor(-140,    3500,    21470,   1500,    -140,    5000,    21470,   0x007C, 0,  29, 0x0000)

    ScpFunction((
        "Function_0_2DC",          # 00, 0
        "Function_1_394",          # 01, 1
        "Function_2_3BF",          # 02, 2
        "Function_3_3EA",          # 03, 3
        "Function_4_415",          # 04, 4
        "Function_5_6F2",          # 05, 5
        "Function_6_76D",          # 06, 6
        "Function_7_19AD",         # 07, 7
        "Function_8_1B03",         # 08, 8
        "Function_9_1BF3",         # 09, 9
        "Function_10_2C74",        # 0A, 10
        "Function_11_2E1B",        # 0B, 11
        "Function_12_4055",        # 0C, 12
        "Function_13_522B",        # 0D, 13
        "Function_14_5E72",        # 0E, 14
        "Function_15_5EFB",        # 0F, 15
        "Function_16_5F7D",        # 10, 16
        "Function_17_68BA",        # 11, 17
        "Function_18_68F5",        # 12, 18
        "Function_19_6A33",        # 13, 19
        "Function_20_6B69",        # 14, 20
        "Function_21_70B2",        # 15, 21
        "Function_22_7289",        # 16, 22
        "Function_23_77FB",        # 17, 23
        "Function_24_7E64",        # 18, 24
        "Function_25_7E8C",        # 19, 25
        "Function_26_7EC8",        # 1A, 26
        "Function_27_7EFA",        # 1B, 27
        "Function_28_7F2C",        # 1C, 28
        "Function_29_8328",        # 1D, 29
    ))


    def Function_0_2DC(): pass

    label("Function_0_2DC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_31C"),
        (1, "loc_328"),
        (2, "loc_334"),
        (3, "loc_340"),
        (4, "loc_34C"),
        (5, "loc_358"),
        (6, "loc_364"),
        (SWITCH_DEFAULT, "loc_370"),
    )


    label("loc_31C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_328")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_334")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_340")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_34C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_358")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_364")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_370")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_37C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_393")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_393")

    Return()

    # Function_0_2DC end

    def Function_1_394(): pass

    label("Function_1_394")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BE")
    OP_94(0xFE, 0xC602, 0xFFFFF538, 0xCFDA, 0xF50, 0x3E8)
    Sleep(300)
    Jump("Function_1_394")

    label("loc_3BE")

    Return()

    # Function_1_394 end

    def Function_2_3BF(): pass

    label("Function_2_3BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E9")
    OP_94(0xFE, 0x1CFC, 0x208A, 0x2FBC, 0x337C, 0x3E8)
    Sleep(300)
    Jump("Function_2_3BF")

    label("loc_3E9")

    Return()

    # Function_2_3BF end

    def Function_3_3EA(): pass

    label("Function_3_3EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_414")
    OP_94(0xFE, 0xCC74, 0xBCCA, 0xD8C2, 0xC4C2, 0x3E8)
    Sleep(300)
    Jump("Function_3_3EA")

    label("loc_414")

    Return()

    # Function_3_3EA end

    def Function_4_415(): pass

    label("Function_4_415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_453")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 10270, 3500, 13330, 315)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_44E")

    Jump("loc_6D0")

    label("loc_453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_466")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_6D0")

    label("loc_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_474")
    Jump("loc_6D0")

    label("loc_474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_499")
    SetChrPos(0xB, 53980, 30, 49050, 135)
    BeginChrThread(0xB, 0, 0, 3)
    Jump("loc_6D0")

    label("loc_499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4AC")
    SetChrFlags(0xE, 0x80)
    Jump("loc_6D0")

    label("loc_4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_4D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3")
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3")
    SetChrFlags(0x10, 0x10)

    label("loc_4D3")

    Jump("loc_6D0")

    label("loc_4D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_50B")
    SetChrPos(0xE, -48650, 200, 4460, 270)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506")
    SetChrFlags(0x10, 0x10)

    label("loc_506")

    Jump("loc_6D0")

    label("loc_50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_528")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_6D0")

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_540")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_6D0")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_56C")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_6D0")

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_57A")
    Jump("loc_6D0")

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5B4")
    SetChrPos(0x8, 10280, 3500, 14670, 180)
    SetChrPos(0xA, 10270, 3500, 13330, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_6D0")

    label("loc_5B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_636")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x8, 3880, 0, -500, 45)
    SetChrPos(0xA, 10270, 3500, 13330, 315)
    SetChrPos(0xB, 53980, 30, 49050, 135)
    SetChrPos(0x11, 9270, 3500, 14320, 135)
    SetChrPos(0x12, 8210, 3500, 14680, 135)
    BeginChrThread(0xB, 0, 0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_631")
    SetChrFlags(0xA, 0x10)

    label("loc_631")

    Jump("loc_6D0")

    label("loc_636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_65F")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x8, 5020, 0, -150, 315)
    Jump("loc_6D0")

    label("loc_65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_66D")
    Jump("loc_6D0")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6A0")
    SetChrPos(0xB, 51970, 0, 53350, 315)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_69B")
    SetChrFlags(0xA, 0x10)

    label("loc_69B")

    Jump("loc_6D0")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_6BF")
    SetChrPos(0xA, 10060, 3500, 14220, 180)
    Jump("loc_6D0")

    label("loc_6BF")

    SetChrPos(0xA, 10060, 3500, 14220, 180)

    label("loc_6D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F1")
    Event(0, 23)

    label("loc_6F1")

    Return()

    # Function_4_415 end

    def Function_5_6F2(): pass

    label("Function_5_6F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70B")
    OP_10(0x0, 0x0)
    OP_10(0xD, 0x1)
    Jump("loc_711")

    label("loc_70B")

    OP_10(0x0, 0x1)
    OP_10(0xD, 0x0)

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_744")

    label("loc_72D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_744")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_744")

    label("loc_744")

    ClearMapObjFlags(0x4, 0x10)
    OP_65(0x1, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76C")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_76C")

    Return()

    # Function_5_6F2 end

    def Function_6_76D(): pass

    label("Function_6_76D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7F7")

    #C0001
    ChrTalk(
        0xFE,
        (
            "このアパートの空家は\x01",
            "今は１つしかないはずじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "ふむ、２階の一番奥じゃ。\x01",
            "気になるのなら\x01",
            "見てきてはどうじゃ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A9")

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_861")

    #C0003
    ChrTalk(
        0x8,
        (
            "さて、今夜の夕メシは\x01",
            "何にするかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "どんな事件があっても\x01",
            "メシだけは食わんとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A9")

    label("loc_861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_99F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8E2")

    #C0005
    ChrTalk(
        0x8,
        (
            "今朝から不良たちが\x01",
            "お仲間を探しておるようなんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "ふむ、他人事ながら\x01",
            "心配してしまうのう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99A")

    label("loc_8E2")


    #C0007
    ChrTalk(
        0x8,
        (
            "今朝から不良たちが\x01",
            "お仲間を探しておるようなんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "はて旧市街の若者じゃ、どこかを\x01",
            "遊び回っとるのかもしれんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "お仲間にくらい、行き先は\x01",
            "告げておくもんじゃろのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_99A")

    Jump("loc_19A9")

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A40")

    #C0010
    ChrTalk(
        0x8,
        (
            "さっき表を歩いておったら\x01",
            "不良に絡まれてしもうての。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "ふむ……あの青髪の子は\x01",
            "たしか新米だったはずじゃが。\x01",
            "妙に険悪な目つきじゃったのう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A9")

    label("loc_A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AA6")

    #C0012
    ChrTalk(
        0x8,
        (
            "不良どもは随分と\x01",
            "大人しくなったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        "ついに仲直りをしたんじゃろうか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B75")

    label("loc_AA6")


    #C0014
    ChrTalk(
        0x8,
        (
            "この一月、不良どもは\x01",
            "随分と大人しくしておるようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "以前のような\x01",
            "乱闘騒ぎはなくなったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "じゃが……柄が\x01",
            "悪くなったという話は聞く。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "おんしら、旧市街を\x01",
            "歩くなら気を付けなされよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B75")

    Jump("loc_19A9")

    label("loc_B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BEA")

    #C0018
    ChrTalk(
        0x8,
        (
            "この旧市街であの子ほど\x01",
            "できた子はそうそうおらん。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "ほっほ、ほんに良い子じゃて。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C7E")

    label("loc_BEA")


    #C0020
    ChrTalk(
        0x8,
        (
            "今朝そこでリーシャ君と\x01",
            "ばったり会ってのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "これから友達と\x01",
            "遊びに行くと言っておったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "ほっほ、あの子は\x01",
            "明るくて良い子じゃのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C7E")

    Jump("loc_19A9")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CF8")

    #C0023
    ChrTalk(
        0x8,
        (
            "今日は市長のお顔を\x01",
            "拝んでくるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "ほっほ、閉会式は\x01",
            "混まんしタダじゃからのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5F")

    label("loc_CF8")


    #C0025
    ChrTalk(
        0x8,
        (
            "さてさて、今日は\x01",
            "閉会式を拝んでこようかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "ほっほ、わしは毎年\x01",
            "見に行っておるんじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D5F")

    Jump("loc_19A9")

    label("loc_D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DCC")

    #C0027
    ChrTalk(
        0x8,
        (
            "こんなボロアパートでも\x01",
            "我が家が一番落ち着くのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "不思議なもんじゃて。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E3D")

    label("loc_DCC")


    #C0029
    ChrTalk(
        0x8,
        (
            "パレードを見に出かけたら\x01",
            "歩き疲れてしもうたわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "こんなボロアパートでも\x01",
            "我が家が一番落ち着くのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E3D")

    Jump("loc_19A9")

    label("loc_E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_F3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E9C")

    #C0031
    ChrTalk(
        0x8,
        (
            "わしら旧市街民の目から見ても\x01",
            "マクダエル市長は立派な方じゃよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F35")

    label("loc_E9C")


    #C0032
    ChrTalk(
        0x8,
        "マクダエル市長も立派な方じゃのう。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "あんな事件があってからも\x01",
            "クロスベルの政治に尽力し、\x01",
            "記念祭も無事に執り行われた。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        "実に気丈な方じゃ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F35")

    Jump("loc_19A9")

    label("loc_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_10C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FBB")

    #C0035
    ChrTalk(
        0x8,
        (
            "受験生の子には\x01",
            "差し入れなぞ持って行ってやるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "わしは近所の者は\x01",
            "見捨てておけんタチなのでのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C1")

    label("loc_FBB")


    #C0037
    ChrTalk(
        0x8,
        (
            "このアパルトメントの住人も\x01",
            "めいめい楽しんでおるようじゃな。\x01",
            "ほっほ、結構結構。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0038
    ChrTalk(
        0x8,
        "いや、一人忘れておったのう。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "確か受験生の子が\x01",
            "一人で寂しそうに\x01",
            "しておった気がするわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "やれやれ、後で差し入れなぞ\x01",
            "持って行ってやるか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10C1")

    Jump("loc_19A9")

    label("loc_10C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_11B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1145")

    #C0041
    ChrTalk(
        0x8,
        (
            "旧市街民とはいえ\x01",
            "多少の贅沢はしたいもんじゃて。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "今のうちにヘソクリを\x01",
            "かき集めておかんとのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11AC")

    label("loc_1145")


    #C0043
    ChrTalk(
        0x8,
        (
            "確かこの辺りに\x01",
            "ヘソクリが、と……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "ほっほ、記念祭に向けて\x01",
            "手持ちの貯金をかき集めんとのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_11AC")

    Jump("loc_19A9")

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CC")
    Call(0, 12)
    Jump("loc_129D")

    label("loc_11CC")

    TurnDirection(0xFE, 0x0, 0)

    #C0045
    ChrTalk(
        0xFE,
        (
            "まさかリーシャ君のような子が\x01",
            "旧市街にいるとは\x01",
            "予想外だったんじゃろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "ははは、腹黒い議員どもめ\x01",
            "モゴモゴ言いながら\x01",
            "引き上げていきおったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "これも気立てのよい\x01",
            "あの子のお陰じゃな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    label("loc_129D")

    Jump("loc_19A9")

    label("loc_12A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_13E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1348")

    #C0048
    ChrTalk(
        0xFE,
        (
            "あの議員たち、コロナさんの所に\x01",
            "行ったようじゃのう……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "わしらは慣れておるから\x01",
            "何とかあしらえるが……\x01",
            "コロナさんは大丈夫かのう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13E1")

    label("loc_1348")


    #C0050
    ChrTalk(
        0xFE,
        (
            "以前から旧市街を\x01",
            "再開発しようという計画があってな……\x01",
            "時折議員が嫌がらせに来るんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "コロナさんも何とか\x01",
            "やり過ごしてくれるといいんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E1")

    Jump("loc_19A9")

    label("loc_13E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1462")

    #C0052
    ChrTalk(
        0xFE,
        (
            "（やれやれ、\x01",
            "  また議員の嫌がらせじゃよ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "（時折やってくるんじゃ……\x01",
            "  何とか追い返さんとのう。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A9")

    label("loc_1462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_14CD")

    #C0054
    ChrTalk(
        0x8,
        "今日もいい天気じゃのう。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "どれ、東通りに出かけて\x01",
            "店のあまり物でも恵んでもらおうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A9")

    label("loc_14CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1537")

    #C0056
    ChrTalk(
        0x8,
        (
            "若い娘が一人で\x01",
            "越してきたそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "わしのように\x01",
            "身寄りがないのかもしれんのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A9")

    label("loc_1537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1697")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15B2")

    #C0058
    ChrTalk(
        0x8,
        (
            "わしはこの旧市街に住んで\x01",
            "６０年になるんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "いまさら他の場所に\x01",
            "移る気にはなれんのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1692")

    label("loc_15B2")


    #C0060
    ChrTalk(
        0x8,
        (
            "わしはこの旧市街に住んで\x01",
            "６０年になるんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "ほほ、昔はこの辺りも活気があった。\x01",
            "新しいオフィス街やら\x01",
            "歓楽街やらが出来る前はな。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "まるで行政に\x01",
            "見捨てられたような場所じゃが、\x01",
            "それでも離れる気にはなれんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1692")

    Jump("loc_19A9")

    label("loc_1697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_17E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_172A")

    #C0063
    ChrTalk(
        0x8,
        (
            "旧市街に暮らす者は\x01",
            "それぞれに事情を抱えておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "だが誰も拒まんのが旧市街じゃよ。\x01",
            "それだけにいざこざもあるがのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E2")

    label("loc_172A")


    #C0065
    ChrTalk(
        0x8,
        (
            "仕事を求めてきた者や\x01",
            "借金に追われ落ちぶれた者……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "この旧市街には\x01",
            "外国からの流れ者も多いんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "だが、ここに暮らす以上は同志じゃ。\x01",
            "みな支えあって生きていかねばのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_17E2")

    Jump("loc_19A9")

    label("loc_17E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_18BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1841")

    #C0068
    ChrTalk(
        0x8,
        (
            "同じ旧市街に暮らす仲間なんじゃ。\x01",
            "少しは仲良うできんのかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BA")

    label("loc_1841")


    #C0069
    ChrTalk(
        0x8,
        (
            "やれやれ、若者ども。\x01",
            "またやってしもうたようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "元気があり余っとるのは分かるが\x01",
            "喧嘩はいかん、喧嘩はな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18BA")

    Jump("loc_19A9")

    label("loc_18BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1954")

    #C0071
    ChrTalk(
        0x8,
        (
            "このアパルトメントは\x01",
            "広さはあるんじゃが。\x01",
            "広いばっかりで隙間風が多くてのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "ほれ、こうしとっても\x01",
            "外からの風を感じるじゃろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A9")

    label("loc_1954")


    #C0073
    ChrTalk(
        0x8,
        (
            "おお、今日は\x01",
            "中々の好天気じゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "ルピナス川からの\x01",
            "空気が心地よいわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19A9")

    TalkEnd(0xFE)
    Return()

    # Function_6_76D end

    def Function_7_19AD(): pass

    label("Function_7_19AD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A41")
    Jump("loc_1A8B")

    label("loc_1A41")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A61")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A8B")

    label("loc_1A61")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A81")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A8B")

    label("loc_1A81")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A8B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AF8")

    #C0075
    ChrTalk(
        0xD,
        "お前さんらも飲むか？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xD,
        "ほっほ、芋焼酎じゃがのう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFB")

    label("loc_1AF8")

    Call(0, 8)

    label("loc_1AFB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_19AD end

    def Function_8_1B03(): pass

    label("Function_8_1B03")

    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)

    #C0077
    ChrTalk(
        0xD,
        "何はともあれ乾杯じゃ。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xD,
        (
            "しかし、さすがに\x01",
            "リーシャ君は参加できんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xF,
        (
            "アルカンシェルでは\x01",
            "準主役だとか……\x01",
            "いやはや、大したものですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xF,
        (
            "私もゼンゼン知らなくて、\x01",
            "今まで普通に接してましたけどねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_8_1B03 end

    def Function_9_1BF3(): pass

    label("Function_9_1BF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1D30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1CB4")

    #C0081
    ChrTalk(
        0x9,
        (
            "しかしリーシャさんは\x01",
            "随分、頑張っているようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "私もいい加減、再起できるよう\x01",
            "頑張らなくては……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "せめてアルカンシェルの\x01",
            "チケットを買えるくらいにはね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D2B")

    label("loc_1CB4")


    #C0084
    ChrTalk(
        0x9,
        (
            "昼間、リーシャさんが\x01",
            "慌しく部屋から出て行ったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "昼の公演が遅れていたらしいが\x01",
            "無事、始まったんだろうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1D2B")

    Jump("loc_2C70")

    label("loc_1D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1D9D")

    #C0086
    ChrTalk(
        0x9,
        (
            "やはり経済は面白いな。\x01",
            "私もいつか……生活を立て直して\x01",
            "商売人に戻りたいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1A")

    label("loc_1D9D")


    #C0087
    ChrTalk(
        0x9,
        "百貨店で経済雑誌を購入してきたよ。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "ふむふむ……今回のトップ記事は\x01",
            "マリアベルさんの特集か。\x01",
            "読み応えがあるなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1E1A")

    Jump("loc_2C70")

    label("loc_1E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1F0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E71")

    #C0089
    ChrTalk(
        0x9,
        (
            "ふむ、今日は久し振りに\x01",
            "百貨店まで買いに行ってみるか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F05")

    label("loc_1E71")


    #C0090
    ChrTalk(
        0x9,
        (
            "おっと、今日はたしか\x01",
            "あの経済雑誌の発売日だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "以前私も定期購読していたんだよ。\x01",
            "ははは……今はすっかり\x01",
            "落ちぶれてしまったけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1F05")

    Jump("loc_2C70")

    label("loc_1F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2015")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F87")

    #C0092
    ChrTalk(
        0x9,
        (
            "最近ミショー君とも\x01",
            "親しくなったばかりなんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "心配だよ。\x01",
            "体を壊してしまったんだろうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2010")

    label("loc_1F87")


    #C0094
    ChrTalk(
        0x9,
        (
            "お隣のミショー君は\x01",
            "ウルスラ病院に行っているんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "近頃根を詰めて勉強していたからね、\x01",
            "体を壊してしまったのかもしれないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2010")

    Jump("loc_2C70")

    label("loc_2015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2134")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2089")

    #C0096
    ChrTalk(
        0x9,
        (
            "旧市街も悪い所ではないが、\x01",
            "小さい子には酷な話だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        "君たちで何とかしてあげなさい。\x02",
    )

    CloseMessageWindow()
    Jump("loc_212F")

    label("loc_2089")


    #C0098
    ChrTalk(
        0x9,
        (
            "おや……こんな小さい子が\x01",
            "旧市街に流れてきたんじゃあるまいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "いかんよ、君たち。\x01",
            "断じていかん。\x02\x03",

            "遊撃士協会か大聖堂あたりに\x01",
            "頼って何とかしてあげなさい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_212F")

    Jump("loc_2C70")

    label("loc_2134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_228A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_21AE")

    #C0100
    ChrTalk(
        0x9,
        (
            "あそこまで爽快に暴れてくれると\x01",
            "逆にスッキリしてしまうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        "何だか元気を貰った気がするよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2285")

    label("loc_21AE")


    #C0102
    ChrTalk(
        0x9,
        (
            "昨日、みんなで鍋をつついていたら\x01",
            "不良たちのレースが始まってね……\x01",
            "突然のことに驚いてしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "だがまあ、手に汗を握る戦いで\x01",
            "非常に楽しませてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "はは、ああいうのも\x01",
            "悪くないんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2285")

    Jump("loc_2C70")

    label("loc_228A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_239F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_22F6")

    #C0105
    ChrTalk(
        0x9,
        (
            "なにぶん、旧市街で\x01",
            "記念祭を過ごすのは初めてなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        "今年はどうするかな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_239A")

    label("loc_22F6")


    #C0107
    ChrTalk(
        0x9,
        "さて、記念祭はどうするかな……\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "お隣のタントスさんには\x01",
            "一緒に鍋でもしないかと\x01",
            "誘われてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "はは……懐具合を考えると\x01",
            "一番の名案かもしれないね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_239A")

    Jump("loc_2C70")

    label("loc_239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_24BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2420")

    #C0110
    ChrTalk(
        0x9,
        (
            "私は株に手を出してな……\x01",
            "全てを失ってしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "それに較べれば\x01",
            "タントスさんは誠実な人だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24BA")

    label("loc_2420")


    #C0112
    ChrTalk(
        0x9,
        (
            "タントスさんは\x01",
            "本当に面倒見のいい人だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        (
            "旧市街育ちと言うと\x01",
            "悪いイメージしかなかったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "あの人は私より\x01",
            "よほど誠実な人間に見えるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_24BA")

    Jump("loc_2C70")

    label("loc_24BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_25A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2539")

    #C0115
    ChrTalk(
        0x9,
        (
            "旧市街暮らしになると\x01",
            "役人どもの不誠実さがよく分かるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        "フン、さっさと帰ればいいものを。\x02",
    )

    CloseMessageWindow()
    Jump("loc_259C")

    label("loc_2539")


    #C0117
    ChrTalk(
        0x9,
        (
            "役人どもめ、こんな時だけ\x01",
            "威張りおって……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "普段は怖がって\x01",
            "近づこうともしないくせにな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_259C")

    Jump("loc_2C70")

    label("loc_25A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2736")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2639")

    #C0119
    ChrTalk(
        0x9,
        (
            "ハロルドとはもう何年ぶりか……\x01",
            "落ちぶれた私にも\x01",
            "何も変わらずに接してくれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "とほほ……思わず\x01",
            "ほろっと来てしまうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2731")

    label("loc_2639")


    #C0121
    ChrTalk(
        0x9,
        (
            "昨日、昔取引のあった\x01",
            "ハロルドという男に会ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "あの頃は気弱で小さい男だと\x01",
            "バカにしていたものだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "久々に会っても、変わらず\x01",
            "のほほんとした調子でな。\x01",
            "私と一杯付き合ってくれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "とほほ……思わず\x01",
            "ほろっと来てしまったな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2731")

    Jump("loc_2C70")

    label("loc_2736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_285E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_27B7")

    #C0125
    ChrTalk(
        0x9,
        (
            "さっき不良たちに\x01",
            "絡まれそうになったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "ぶるぶる、どうしてあんな\x01",
            "場所で待ち伏せていたんだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2859")

    label("loc_27B7")


    #C0127
    ChrTalk(
        0x9,
        (
            "さっき不良たちに\x01",
            "絡まれそうになったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x9,
        (
            "ぶるぶる、これだから\x01",
            "治安の悪い場所は嫌なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "でもなぜアパートの前なんかで\x01",
            "待ち伏せていたんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2859")

    Jump("loc_2C70")

    label("loc_285E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_295D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_28D3")

    #C0130
    ChrTalk(
        0x9,
        (
            "落ちぶれた今でも\x01",
            "経済誌を買ってしまうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        (
            "とほほ……\x01",
            "みっともないがやめられんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2958")

    label("loc_28D3")


    #C0132
    ChrTalk(
        0x9,
        "今週の株価は……と。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "……恥ずかしい事に、今でも\x01",
            "経済誌を買ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "商人をやっていた頃の\x01",
            "習慣が抜けなくてな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2958")

    Jump("loc_2C70")

    label("loc_295D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2A45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_29C8")

    #C0135
    ChrTalk(
        0x9,
        "私は元々商人だったんだが……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "ご覧の通り\x01",
            "落ちぶれてしまってな。\x01",
            "とほほ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A40")

    label("loc_29C8")


    #C0137
    ChrTalk(
        0x9,
        (
            "このアパルトメントは\x01",
            "家賃が安くてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "私のように落ちぶれた人間でも\x01",
            "何とか暮らしていけるんだよ。\x01",
            "とほほ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2A40")

    Jump("loc_2C70")

    label("loc_2A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2AF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A8B")

    #C0139
    ChrTalk(
        0x9,
        (
            "くそう、何故私が\x01",
            "旧市街暮らしなんかに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AEE")

    label("loc_2A8B")


    #C0140
    ChrTalk(
        0x9,
        (
            "わ、私は元々\x01",
            "立派な商人だったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        (
            "柄の悪い旧市街育ちの連中と\x01",
            "一緒にしないでくれよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2AEE")

    Jump("loc_2C70")

    label("loc_2AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_2B30")

    #C0142
    ChrTalk(
        0x9,
        (
            "そ、外が騒がしかったな。\x01",
            "何かあったのか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C70")

    label("loc_2B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B95")

    #C0143
    ChrTalk(
        0x9,
        (
            "ううっ、くそ……\x01",
            "こんな筈じゃなかったんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        "私は間違ってなんかないぞ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C70")

    label("loc_2B95")


    #C0145
    ChrTalk(
        0x9,
        (
            "ううっ、くそ……\x01",
            "こんな筈じゃなかったんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        (
            "あの株は絶対に買いだった！\x01",
            "私は間違ってなんかないぞ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0147
    ChrTalk(
        0x9,
        "な、何だ君達は！？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            "例の不良どもの仲間か？\x01",
            "さ、さっさと出て行ってくれ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C70")

    TalkEnd(0xFE)
    Return()

    # Function_9_1BF3 end

    def Function_10_2C74(): pass

    label("Function_10_2C74")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D08")
    Jump("loc_2D52")

    label("loc_2D08")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D28")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D52")

    label("loc_2D28")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D48")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D52")

    label("loc_2D48")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D52")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2E10")

    #C0149
    ChrTalk(
        0xF,
        (
            "遊び回るほどのミラはないのでね。\x01",
            "アパートの住人で祝いがてら\x01",
            "鍋をつつくことにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xF,
        (
            "タントスさんは\x01",
            "面倒見のいい人だからなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E13")

    label("loc_2E10")

    Call(0, 8)

    label("loc_2E13")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_2C74 end

    def Function_11_2E1B(): pass

    label("Function_11_2E1B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EAF")
    Jump("loc_2EF9")

    label("loc_2EAF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2ECF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF9")

    label("loc_2ECF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EEF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EF9")

    label("loc_2EEF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EF9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2FF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2F7E")

    #C0151
    ChrTalk(
        0xE,
        (
            "夕方ってどうしても眠くなっちまう。\x01",
            "くそっ、ここは踏ん張るんだ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEE")

    label("loc_2F7E")

    SetChrSubChip(0xE, 0x0)

    #C0152
    ChrTalk(
        0xE,
        "うつら、うつら……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0153
    ChrTalk(
        0xE,
        "ハッ、い、いかん！\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xE,
        "この時間帯は魔の領域だな……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2FEE")

    Jump("loc_404D")

    label("loc_2FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_30E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3066")

    #C0155
    ChrTalk(
        0xE,
        (
            "今年の試験こそは\x01",
            "絶対に合格するんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xE,
        (
            "不良ども、どうか\x01",
            "邪魔しないでくれよっ！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E2")

    label("loc_3066")


    #C0157
    ChrTalk(
        0xE,
        "不良たち……最近妙に静かだな。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xE,
        "……いや、それならいいんだ。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xE,
        (
            "僕の邪魔さえしなけりゃ\x01",
            "なんだっていいよ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_30E2")

    Jump("loc_404D")

    label("loc_30E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3182")

    #C0160
    ChrTalk(
        0xE,
        (
            "昨日はウルスラ病院へ行ってね。\x01",
            "先生と沢山話をしてきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xE,
        (
            "フフフ……貴重な体験だったな。\x01",
            "ますますウルスラ大に\x01",
            "通いたくなったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_404D")

    label("loc_3182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_329D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3213")

    #C0162
    ChrTalk(
        0xE,
        (
            "模試の成績はバッチリだったよ。\x01",
            "このまま勉強を続ければ\x01",
            "ウルスラ大合格、８０％！\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xE,
        "よーし、この調子で頑張るぞ～っ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3298")

    label("loc_3213")

    SetChrSubChip(0xE, 0x0)

    #C0164
    ChrTalk(
        0xE,
        (
            "模試の成功を祈って\x01",
            "一人かんぱーい！\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xE,
        "むしゃむしゃ、ぱくぱく……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xE,
        (
            "よーし、この調子で\x01",
            "本試験に向けて頑張るぞ～っ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3298")

    Jump("loc_404D")

    label("loc_329D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_32E7")

    #C0167
    ChrTalk(
        0xE,
        (
            "今日だけは……\x01",
            "今日だけはやめてくれよぉ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_334E")

    label("loc_32E7")


    #C0168
    ChrTalk(
        0xE,
        "ま、また表が騒がしいぞ！？\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xE,
        (
            "やめてくれよぉ……\x01",
            "明日はウルスラ大の\x01",
            "入試模試なんだよぉ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_334E")

    Jump("loc_404D")

    label("loc_3353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_342F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_33A3")

    #C0170
    ChrTalk(
        0xE,
        (
            "模試まであと２日……\x01",
            "模試だからって手は抜けないぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_342A")

    label("loc_33A3")


    #C0171
    ChrTalk(
        0xE,
        (
            "昼メシを食いに出たら\x01",
            "人ごみに捕まっちまってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xE,
        "抜け出すのに一苦労だったよ。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xE,
        (
            "まったく……\x01",
            "無駄な時間を使っちまった。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_342A")

    Jump("loc_404D")

    label("loc_342F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_34E0")

    #C0174
    ChrTalk(
        0xE,
        (
            "昨日はタントスさんが\x01",
            "焼き魚を差し入れてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xE,
        (
            "……なんでも、焼き魚は\x01",
            "記憶力がアップするらしいよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xE,
        (
            "へへ、へへへ……\x01",
            "これで暗記もはかどるかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_404D")

    label("loc_34E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_356D")

    #C0177
    ChrTalk(
        0xE,
        (
            "今度の模試で\x01",
            "大学に合格する確率が分かるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xE,
        (
            "もしいい点が取れなかったら……\x01",
            "僕はショックで寝込んじゃうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_360D")

    label("loc_356D")


    #C0179
    ChrTalk(
        0xE,
        "ふ、不良どもめ……\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xE,
        (
            "昨日はゼンゼン\x01",
            "勉強がはかどらなかったじゃないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xE,
        (
            "マズイ、マズイよ……\x01",
            "記念祭が終わったら\x01",
            "すぐに模試があるっていうのに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_360D")

    Jump("loc_404D")

    label("loc_3612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_36D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3685")

    #C0182
    ChrTalk(
        0xE,
        "畜生、みんな浮かれやがって……\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xE,
        (
            "僕だって本当は\x01",
            "遊びに行きたいのに……\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36CC")

    label("loc_3685")


    #C0184
    ChrTalk(
        0xE,
        "……受験生に休みなんて無いんだ。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xE,
        "僕の気持ち、分かるだろ？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_36CC")

    Jump("loc_404D")

    label("loc_36D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_37DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_373B")

    #C0186
    ChrTalk(
        0xE,
        (
            "だ、だめだ。\x01",
            "暗記物をしていたら眠くなるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xE,
        "暗記って苦手なんだよなぁ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_37D6")

    label("loc_373B")

    SetChrSubChip(0xE, 0x0)

    #C0188
    ChrTalk(
        0xE,
        "うつら、うつら……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0189
    ChrTalk(
        0xE,
        (
            "ハッ、い、いかん！\x01",
            "つい居眠りを……！\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xE,
        (
            "３０分の睡眠が命取り！\x01",
            "試験勉強に居眠りは禁物だ！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_37D6")

    Jump("loc_404D")

    label("loc_37DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3901")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3851")

    #C0191
    ChrTalk(
        0xE,
        (
            "ウルスラ大は医科大学だけど\x01",
            "一般教養も試験に出るんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xE,
        "とほほ、覚える事が山積みだよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38FC")

    label("loc_3851")


    #C0193
    ChrTalk(
        0xE,
        (
            "ええと、エレボニア帝国宰相\x01",
            "オズボーン氏は\x01",
            "軍部出身の政治家で……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xE,
        (
            "主な功績は\x01",
            "帝国全土への鉄道網の敷設と……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xE,
        (
            "あと《鉄血政策》の宣言が……\x01",
            "ええっと…………\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_38FC")

    Jump("loc_404D")

    label("loc_3901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_39EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3947")

    #C0196
    ChrTalk(
        0xE,
        (
            "僕の勉強の\x01",
            "邪魔をしないでほしいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39E7")

    label("loc_3947")


    #C0197
    ChrTalk(
        0xE,
        (
            "どっかのお偉いさんが\x01",
            "住民登録の確認に来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xE,
        (
            "フン、そのくらい\x01",
            "登録してるに決まってるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xE,
        (
            "なんだってそんな物の\x01",
            "確認に来るんだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_39E7")

    Jump("loc_404D")

    label("loc_39EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3A77")

    #C0200
    ChrTalk(
        0xE,
        (
            "記念祭の直後に、ウルスラ大の\x01",
            "入試の模擬試験があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xE,
        (
            "今年はちゃんと受けて\x01",
            "本番も絶対に合格しないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B6C")

    label("loc_3A77")


    #C0202
    ChrTalk(
        0xE,
        (
            "記念祭の直後に、ウルスラ大の\x01",
            "入試の模擬試験があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xE,
        (
            "これを受けとけば\x01",
            "自分の実力が分かるし\x01",
            "本番でも慌てずにすむってワケさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xE,
        (
            "……僕、去年は模試を受けずに\x01",
            "本番で大コケしちゃったからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xE,
        "今年はちゃんと受けることにするよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3B6C")

    Jump("loc_404D")

    label("loc_3B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3CD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C67")

    #C0206
    ChrTalk(
        0xFE,
        (
            "表にいる不良たち、\x01",
            "ここの上の部屋に越してきた\x01",
            "女の子目当てらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "まああの子はスゴク可愛くって\x01",
            "元気に挨拶を返してくれる\x01",
            "いい子だからなぁ……㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0208
    ChrTalk(
        0xFE,
        (
            "……っていやいや、\x01",
            "そうじゃなくって！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CCF")

    label("loc_3C67")


    #C0209
    ChrTalk(
        0xFE,
        (
            "はあ、余計な考えは捨てて\x01",
            "勉強に集中しないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "不良連中はいいよなぁ……\x01",
            "いつもヒマでさぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CCF")

    Jump("loc_404D")

    label("loc_3CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D5B")

    #C0211
    ChrTalk(
        0xE,
        (
            "家族からの仕送りだけで\x01",
            "受験生やるのも辛いんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xE,
        (
            "うーん、どうしよっかなー……\x01",
            "今月厳しいしなー……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E14")

    label("loc_3D5B")


    #C0213
    ChrTalk(
        0xE,
        (
            "くはー、この参考書、\x01",
            "ちょっと難しすぎるな……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xE,
        (
            "もうちょっと\x01",
            "分かりやすいのが欲しいけど、\x01",
            "あんまりミラが無いんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xE,
        (
            "うーん、どうしよっかなー……\x01",
            "今月厳しいしなー……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3E14")

    Jump("loc_404D")

    label("loc_3E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3E52")

    #C0216
    ChrTalk(
        0xE,
        "来年こそは合格しないとな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ED3")

    label("loc_3E52")


    #C0217
    ChrTalk(
        0xE,
        (
            "僕はウルスラ医科大学を目指して\x01",
            "田舎から出てきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xE,
        (
            "……でも今年も失敗しちゃってね。\x01",
            "来年の試験に懸けてるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3ED3")

    Jump("loc_404D")

    label("loc_3ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3F68")

    #C0219
    ChrTalk(
        0xE,
        (
            "不良グループの連中、\x01",
            "そろそろ喧嘩に飽きたのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xE,
        "うん、それがいいよ。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xE,
        (
            "そして僕みたいに\x01",
            "試験勉強に励めばいいんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_404D")

    label("loc_3F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_3F94")

    #C0222
    ChrTalk(
        0xE,
        "ん？　急に静かになった？\x02",
    )

    CloseMessageWindow()
    Jump("loc_404D")

    label("loc_3F94")


    #C0223
    ChrTalk(
        0xE,
        (
            "この辺りには『テスタメンツ』と\x01",
            "『サーベルバイパー』っていう\x01",
            "２つの不良グループがあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xE,
        "連中、いつも騒ぎ立てやがって……\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xE,
        (
            "今度の試験に落ちたら\x01",
            "どうしてくれるんだよっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_404D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_2E1B end

    def Function_12_4055(): pass

    label("Function_12_4055")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_412F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_40CF")

    #C0226
    ChrTalk(
        0xA,
        (
            "家族で食卓を囲むのは久し振り。\x01",
            "ふふっ……たまにこんな日があると\x01",
            "嬉しくなってしまいますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_412A")

    label("loc_40CF")


    #C0227
    ChrTalk(
        0xA,
        (
            "うちの人、帰って\x01",
            "来たみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xA,
        (
            "よかった……\x01",
            "今日は家族で食卓が囲めます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_412A")

    Jump("loc_5227")

    label("loc_412F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_41E4")

    #C0229
    ChrTalk(
        0xA,
        (
            "建設日程の調整とかで……\x01",
            "今日は主人が\x01",
            "早く帰ってくるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xA,
        "ふふっ、さっき連絡があったんです。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        (
            "……今日はちょっぴり\x01",
            "ご馳走を用意しなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5227")

    label("loc_41E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_42DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_423F")

    #C0232
    ChrTalk(
        0xA,
        (
            "リーシャさん、\x01",
            "お仕事も大変なのに……\x01",
            "本当に朝が早起きですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42D5")

    label("loc_423F")


    #C0233
    ChrTalk(
        0xA,
        (
            "お隣のリーシャさん、\x01",
            "今朝はとても早くに\x01",
            "出かけられたみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xA,
        (
            "主人が起きるよりも早かったから……\x01",
            "まだ２時か３時くらいじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_42D5")

    Jump("loc_5227")

    label("loc_42DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_442E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4360")

    #C0235
    ChrTalk(
        0xA,
        (
            "最近は現場に出ても\x01",
            "仕事をしなかったりするそうです。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFF)

    #C0236
    ChrTalk(
        0xA,
        (
            "……それならお休みを\x01",
            "貰えればいいんですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4429")

    label("loc_4360")


    #C0237
    ChrTalk(
        0xA,
        (
            "自治州議会が\x01",
            "開かれている間は、\x01",
            "ビルの建設は控えられるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xA,
        (
            "予算が付くかどうか判らなくなって\x01",
            "様子見になるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xA,
        (
            "主人は建設現場にいるので……\x01",
            "最近生活が不規則になってきました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4429")

    Jump("loc_5227")

    label("loc_442E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_44BF")

    #C0240
    ChrTalk(
        0xA,
        (
            "記念祭にはお休みが\x01",
            "もらえましたけど、\x01",
            "主人の仕事は相変わらずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xA,
        (
            "もう少し休みを増やしてくれると\x01",
            "リマも喜ぶんですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5227")

    label("loc_44BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_45CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4549")

    #C0242
    ChrTalk(
        0xA,
        (
            "夫が休暇を取るなんて久し振りです。\x01",
            "これで家族で記念祭を過ごせますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xA,
        "ふふ、私も楽しみになってきました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_45C5")

    label("loc_4549")


    #C0244
    ChrTalk(
        0xA,
        "もうリマったらはしゃいで……\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xA,
        (
            "でも、夫が休暇を\x01",
            "取るなんて久し振りです。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xA,
        "ふふ、私も楽しみになってきました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_45C5")

    Jump("loc_5227")

    label("loc_45CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_490C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_484A")
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0xA, 0x0, 0)
    TurnDirection(0x8, 0x0, 0)

    #C0247
    ChrTalk(
        0xA,
        (
            "今日も議員の人たちがやってきて\x01",
            "意地悪を言われたんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xA,
        (
            "そこに丁度、お隣に住んでいる\x01",
            "リーシャさんが通りがかったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xA,
        (
            "リーシャさんが元気よく挨拶したら、\x01",
            "議員の人たちは目をまん丸にして\x01",
            "黙ってしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x8,
        (
            "そうそう、あの時の連中の顔なぞ\x01",
            "まさに見ものじゃったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "リーシャ君は\x01",
            "あのアルカンシェルの団員なんじゃ。\x01",
            "……よっぽど驚いたんじゃろ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)
    Sleep(300)

    #C0252
    ChrTalk(
        0xA,
        (
            "ふふ、もごもご言って……\x01",
            "今日は帰ってしまいましたね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 500)
    Sleep(300)

    #C0253
    ChrTalk(
        0x8,
        (
            "うむ、あのイヤミな議員が\x01",
            "尻尾を巻いてのう……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x8,
        (
            "ははは、立派立派。\x01",
            "あの子の笑顔は\x01",
            "まさにワシらを救ってくれたわい。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_4907")

    label("loc_484A")

    TurnDirection(0xFE, 0x0, 0)

    #C0255
    ChrTalk(
        0xFE,
        (
            "議員の人たちは時々嫌がらせに\x01",
            "来るみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "リーシャさんがいれば、\x01",
            "なんだかもう大丈夫な気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "ふふっ、後でお礼に\x01",
            "おかずでも持っていかなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)

    label("loc_4907")

    Jump("loc_5227")

    label("loc_490C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4AD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A60")
    OP_4B(0x11, 0xFF)

    #C0258
    ChrTalk(
        0xFE,
        (
            "滞在許可証……\x01",
            "住民登録……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "すみません、\x01",
            "クロスベルに来たのは\x01",
            "もう５年も前なんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x11,
        (
            "ほう、もし登録がないとなると\x01",
            "面倒な事になりますな。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x11,
        (
            "自治州法により\x01",
            "退去命令を下す事になるが……\x01",
            "それとも自主的に出て行くかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0262
    ChrTalk(
        0xFE,
        (
            "そ、そんな……\x01",
            "#2S……どうしましょう……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_4ACE")

    label("loc_4A60")

    TurnDirection(0xA, 0x0, 0)

    #C0263
    ChrTalk(
        0xFE,
        "困りました……\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "届けを出していないと\x01",
            "不法滞在ということに\x01",
            "なってしまうそうなんです……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x13B, 0x0)

    label("loc_4ACE")

    Jump("loc_5227")

    label("loc_4AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4C51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4B7B")

    #C0265
    ChrTalk(
        0xA,
        (
            "お隣の娘さん、\x01",
            "最近少し元気が無いみたいなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xA,
        (
            "お節介かもしれませんけど……\x01",
            "若い女の子で一人暮らしですもの、\x01",
            "気になってしまいます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C4C")

    label("loc_4B7B")


    #C0267
    ChrTalk(
        0xA,
        (
            "お隣に引っ越してきた娘さんは\x01",
            "いつも明るくて\x01",
            "元気一杯な方なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xA,
        (
            "リマにもいつも\x01",
            "良くしてもらっているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xA,
        (
            "でも……最近少し\x01",
            "元気が無いみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xA,
        "何か心配事でもあるんでしょうか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4C4C")

    Jump("loc_5227")

    label("loc_4C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4D82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4D02")

    #C0271
    ChrTalk(
        0xA,
        "リマは主人の事が大好きなんです。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xA,
        (
            "主人は日雇いの仕事ばかりで\x01",
            "家に居ない事が多いんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xA,
        (
            "いつの間に父親っ子に\x01",
            "なってしまったのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7D")

    label("loc_4D02")


    #C0274
    ChrTalk(
        0xA,
        "リマったら無理をして……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xA,
        (
            "きっと今日は\x01",
            "お昼寝するって言い出すわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xA,
        (
            "その前に洗濯物を\x01",
            "済ませておかないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4D7D")

    Jump("loc_5227")

    label("loc_4D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4EEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4E2E")

    #C0277
    ChrTalk(
        0xA,
        (
            "旧市街はお家賃も安くて、\x01",
            "私達でも何とか生活していけます。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xA,
        (
            "でもここが立派な\x01",
            "アパルトメントになったら……\x01",
            "出て行くしかないかもしれません……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EE9")

    label("loc_4E2E")


    #C0279
    ChrTalk(
        0xA,
        "この前お役人さんが来ていたんです。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xA,
        (
            "旧市街を取り壊して\x01",
            "再開発するとかで……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    #C0281
    ChrTalk(
        0xA,
        (
            "旧市街、無くなって\x01",
            "しまうんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xA,
        "そうなったら私たちは……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4EE9")

    Jump("loc_5227")

    label("loc_4EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4F6B")

    #C0283
    ChrTalk(
        0xA,
        (
            "若い娘さんが\x01",
            "一人暮らしだなんて……\x01",
            "何かあったら心配ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xA,
        "私たちが力になってあげないと。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FDE")

    label("loc_4F6B")


    #C0285
    ChrTalk(
        0xA,
        (
            "お隣に若い娘さんが\x01",
            "引っ越してきたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xA,
        (
            "それも一人暮らしだそうで……\x01",
            "私、ビックリしてしまいました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4FDE")

    Jump("loc_5227")

    label("loc_4FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_50C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5048")
    OP_4B(0xB, 0xFF)

    #C0287
    ChrTalk(
        0xA,
        "はーい、ちょっと待っててねー。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xA,
        "いまシチューが出来ますよ～！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_50C0")

    label("loc_5048")


    #C0289
    ChrTalk(
        0xA,
        (
            "こうして暖かい食事ができるのも\x01",
            "夫が毎日働きに出てくれるお陰です。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xA,
        "感謝しなくちゃいけませんね。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 3)

    label("loc_50C0")

    Jump("loc_5227")

    label("loc_50C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_51A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5115")

    #C0291
    ChrTalk(
        0xA,
        (
            "その、治安が悪いのは\x01",
            "確かにこの辺りの欠点ですよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A4")

    label("loc_5115")


    #C0292
    ChrTalk(
        0xA,
        (
            "治安が悪いのは\x01",
            "この辺りの欠点ですよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xA,
        (
            "あ、でも私たちは\x01",
            "ここを離れるつもりはないんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xA,
        "他に行くあてもありませんし……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_51A4")

    Jump("loc_5227")

    label("loc_51A9")


    #C0295
    ChrTalk(
        0xA,
        (
            "娘は元気がよくって\x01",
            "すぐにトコトコ出掛けてしまいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xA,
        (
            "ふう、お料理していても気になって\x01",
            "時々様子を見に来てしまうわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5227")

    TalkEnd(0xFE)
    Return()

    # Function_12_4055 end

    def Function_13_522B(): pass

    label("Function_13_522B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_52C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_52BA")
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0297
    ChrTalk(
        0xB,
        "パパがはやく帰ってきてくれたの！\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xB,
        (
            "わーい、今日は\x01",
            "いっぱいいっぱい遊んでもらえるの！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52BD")

    label("loc_52BA")

    Call(0, 14)

    label("loc_52BD")

    Jump("loc_5E6E")

    label("loc_52C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_535D")

    #C0299
    ChrTalk(
        0xB,
        (
            "あのね、パパが\x01",
            "はやく帰れるかもしれないんだって。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0300
    ChrTalk(
        0xB,
        "わーい、ほんとかな？\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xB,
        "パパいつ帰ってくるのかなぁ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E6E")

    label("loc_535D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5436")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_53B4")

    #C0302
    ChrTalk(
        0xB,
        "まずはゴミひろいするっ！\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xB,
        "リマがぴかぴかにするも～ん！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5431")

    label("loc_53B4")


    #C0304
    ChrTalk(
        0xB,
        (
            "ママがね、お手伝いたくさんしたら\x01",
            "パパがはやく帰ってくるかも、だって！\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xB,
        (
            "……リマ、今日から\x01",
            "お手伝いがんばるっ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5431")

    Jump("loc_5E6E")

    label("loc_5436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_54BA")

    #C0306
    ChrTalk(
        0xB,
        (
            "リーシャさん、さっき\x01",
            "おでかけして行ったよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xB,
        (
            "いつもみたいに\x01",
            "頭なでてくれたの～。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xB,
        "わ～い、うれしいな～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E6E")

    label("loc_54BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_55B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_550A")

    #C0309
    ChrTalk(
        0xB,
        (
            "……パパ、いつになったら\x01",
            "はやく帰ってくるのかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55AC")

    label("loc_550A")


    #C0310
    ChrTalk(
        0xB,
        (
            "パパの作ってたビルが\x01",
            "完成したんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xB,
        (
            "でもね、また\x01",
            "次のビルを作るんだって。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)

    #C0312
    ChrTalk(
        0xB,
        (
            "……パパ、今日は\x01",
            "はやく帰ってくるかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_55AC")

    Jump("loc_5E6E")

    label("loc_55B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5697")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_561B")

    #C0313
    ChrTalk(
        0xB,
        "パパ、今度お休みなんだって！\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xB,
        (
            "わーい、一緒に\x01",
            "お祭りにいけるんだって～っ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5692")

    label("loc_561B")


    #C0315
    ChrTalk(
        0xB,
        "あのねあのね～！\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xB,
        "今度ね、パパがお休みなんだって！\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0317
    ChrTalk(
        0xB,
        "わーい！　パパ大好き～っ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5692")

    Jump("loc_5E6E")

    label("loc_5697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_57E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5722")

    #C0318
    ChrTalk(
        0xB,
        (
            "リーシャお姉ちゃんってね、\x01",
            "すごくやさしいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xB,
        (
            "あれー、でも飛んだりはねたりする\x01",
            "お仕事ってなんだろー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57DE")

    label("loc_5722")


    #C0320
    ChrTalk(
        0xB,
        (
            "おとなりに住んでる\x01",
            "リーシャお姉ちゃんってね、\x01",
            "すごくやさしいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xB,
        (
            "それでね、\x01",
            "飛んだりはねたりするのが\x01",
            "お仕事なんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xB,
        (
            "きょうも元気よく\x01",
            "おでかけしていったんだよー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_57DE")

    Jump("loc_5E6E")

    label("loc_57E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5837")

    #C0323
    ChrTalk(
        0xB,
        "ママがね、お家にいなさいって言うの。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xB,
        "なにかあったのかなー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E6E")

    label("loc_5837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_58DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_586A")

    #C0325
    ChrTalk(
        0xB,
        "パパに会いたいよう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_58D8")

    label("loc_586A")


    #C0326
    ChrTalk(
        0xB,
        (
            "最近パパのお仕事\x01",
            "いそがしいんだって……\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xB,
        "夜も帰ってこなかったりするの。\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xB,
        "くすん、さみしい……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_58D8")

    Jump("loc_5E6E")

    label("loc_58DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5A3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5966")

    #C0329
    ChrTalk(
        0xB,
        (
            "きのうはがんばって起きてたのに……\x01",
            "あんまりお話できなかった……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xB,
        (
            "うううぅ～……\x01",
            "パパ、ごめんなさぁい……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A36")

    label("loc_5966")


    #C0331
    ChrTalk(
        0xB,
        (
            "うううぅ～……\x01",
            "なんだかねむいかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xB,
        (
            "きのうはパパがかえってくるまで\x01",
            "がんばって起きてたの……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xB,
        (
            "でもね、パパにだっこしてもらったら\x01",
            "そのままねちゃったんだー。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xB,
        "あんまりお話できなかった……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5A36")

    Jump("loc_5E6E")

    label("loc_5A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5B94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5AAA")

    #C0335
    ChrTalk(
        0xB,
        (
            "リマ、あんまり\x01",
            "パパに会えないの……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xB,
        (
            "パパ、きょうは\x01",
            "はやく帰ってこないかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B8F")

    label("loc_5AAA")


    #C0337
    ChrTalk(
        0xB,
        (
            "リマのパパは\x01",
            "毎日お仕事してるんだよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xB,
        (
            "ビルのけんせつげんばで\x01",
            "働いててね、\x01",
            "朝早くに出かけちゃうの。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xB,
        (
            "夜もね、リマが寝ちゃってから\x01",
            "帰ってくるんだってー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)

    #C0340
    ChrTalk(
        0xB,
        "リマ、あんまり会えないの……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5B8F")

    Jump("loc_5E6E")

    label("loc_5B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5C82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5BF9")

    #C0341
    ChrTalk(
        0xB,
        "お姉さん、とってもやさしかったの。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xB,
        "えへへ、頭なでてくれたんだよ～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C7D")

    label("loc_5BF9")


    #C0343
    ChrTalk(
        0xB,
        (
            "あのねー、きのう\x01",
            "知らないお姉さんに会ったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xB,
        (
            "お姉さん、おとなりに\x01",
            "引っ越してきたんだってー。\x01",
            "頭なでてくれたんだよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5C7D")

    Jump("loc_5E6E")

    label("loc_5C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5D3A")

    #C0345
    ChrTalk(
        0xB,
        "くんくん、いい匂い！\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xB,
        (
            "ね？　いい匂いでしょ？\x01",
            "お腹へっちゃうよね～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0347
    ChrTalk(
        0xB,
        (
            "パパにも食べさせてあげたいな～。\x01",
            "はやく帰ってくればいいのにー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E6E")

    label("loc_5D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_5D95")

    #C0348
    ChrTalk(
        0xB,
        "るんるんるん、るる～ん♪\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xB,
        (
            "パパ、きょうは\x01",
            "はやく帰ってこないかなー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E6E")

    label("loc_5D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5DEF")

    #C0350
    ChrTalk(
        0xB,
        "パパが帰ってくるの、まってるの。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xB,
        "パパ、はやく帰ってこないかなー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E6E")

    label("loc_5DEF")


    #C0352
    ChrTalk(
        0xB,
        (
            "パパはけんせつげんばで\x01",
            "働いてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xB,
        (
            "パパ、きょうは\x01",
            "何時くらいに帰ってくるのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xB,
        "はやく帰ってこないかなー！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5E6E")

    TalkEnd(0xFE)
    Return()

    # Function_13_522B end

    def Function_14_5E72(): pass

    label("Function_14_5E72")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0355
    ChrTalk(
        0xB,
        "わーい、パパ、お帰りなさい！！\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xC,
        (
            "ただいま、リマ。\x01",
            "お待たせしちゃったかな？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_5E72 end

    def Function_15_5EFB(): pass

    label("Function_15_5EFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5F76")

    #C0357
    ChrTalk(
        0xC,
        (
            "今日はいろいろあってね……\x01",
            "思ったより早く帰れたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xC,
        (
            "お陰で家族で\x01",
            "あったかい夕食が頂けそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F79")

    label("loc_5F76")

    Call(0, 14)

    label("loc_5F79")

    TalkEnd(0xFE)
    Return()

    # Function_15_5EFB end

    def Function_16_5F7D(): pass

    label("Function_16_5F7D")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5FE6")
    Call(0, 17)

    #C0359
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごご。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ヴァン、食いモンより酒だ。\x01",
            "酒をもらって来～いぃ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_5FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6089")
    Call(0, 17)

    #C0361
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "いでで……\x01",
            "ベッドから落ちちまったあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒……いや、先にしょんべんか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "………………………………\x01",
            "……んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_6089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_60E7")
    Call(0, 17)

    #C0364
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "……幸せがあんのは～……\x01",
            "天国だけだぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_60E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_61CB")
    Call(0, 17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_613E")

    #C0366
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んがー……んごー……\x01",
            "むにゃにゃ、次は許さんぞォ……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61C6")

    label("loc_613E")


    #C0367
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んがー……んごー……\x01",
            "んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "誰だぁ、俺の酒盗みやがったのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "飲んでねえのに空っぽじゃねかぁ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_61C6")

    Jump("loc_68B6")

    label("loc_61CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6242")
    Call(0, 17)

    #C0370
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x01",
            "俺は……医者に掛かる\x01",
            "ミラがあったら酒を飲む……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "そういう男だぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_6242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6298")
    Call(0, 17)

    #C0372
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ウ～……なんだぁ？\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "なんで外に\x01",
            "紙ふぶきが舞ってんだぁ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_6298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_62FC")
    Call(0, 17)

    #C0374
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x01",
            "酒、酒がたりねーぞぉ……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごごー……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_62FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_635A")
    Call(0, 17)

    #C0376
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒～……だけがぁ……\x01",
            "……俺の友達ぃ～……\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "へっくしょーん……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_635A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_63AD")
    Call(0, 17)

    #C0378
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "うー、しょんべん行きてえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "どこだ……しょんべん……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_63AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_63FA")
    Call(0, 17)

    #C0380
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒、酒くだしゃ～い……！\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んがー……んごー……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_63FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6499")
    Call(0, 17)

    #C0382
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "仕事に捨てられ、酔い潰れぇ～……\x01",
            "ヒック……\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "……オイ、からっぽじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ヴァン、ヴァン！\x01",
            "さっさと酒を買ってきやがれ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_6499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6503")
    Call(0, 17)

    #C0385
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ヴァン……うるせーぞぉ……\x01",
            "静かにできねーのかぁ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_6503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_656B")
    Call(0, 17)

    #C0387
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ヴァン、ヴァンどこだぁ！？\x01",
            "……酒は、まだかぁ……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_656B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_65CF")
    Call(0, 17)

    #C0389
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "人生ぃなんてそんなものォ……！\x01",
            "酒だけぇ……がぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ウー、ヒック……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_65CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_662F")
    Call(0, 17)

    #C0391
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ヒック……\x01",
            "……目が覚めちまったぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒、酒持ってきてくれぇ～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_662F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_668B")
    Call(0, 17)

    #C0393
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒～……だけが～……\x01",
            "オレの人生ぃ～……\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_668B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_66EF")
    Call(0, 17)

    #C0395
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ヴァン、うるせーぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "デカイ声出すなぁ……！\x01",
            "……んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B6")

    label("loc_66EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6791")
    Call(0, 17)

    #C0397
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ヴァン、酒だ！\x01",
            "酒をもってこい～ぃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_678C")

    #C0399
    ChrTalk(
        0x101,
        (
            "#0003F（ここは空家じゃない\x01",
            "  みたいだな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_678C")

    Jump("loc_68B6")

    label("loc_6791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_681E")
    Call(0, 17)

    #C0400
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ん？　んんー……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6819")

    #C0402
    ChrTalk(
        0x101,
        (
            "#0003F（ここは空家じゃない\x01",
            "  みたいだな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6819")

    Jump("loc_68B6")

    label("loc_681E")

    Call(0, 17)

    #C0403
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒だぁ～、酒。\x01",
            "……酒もってこいぃ～……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68B6")

    #C0405
    ChrTalk(
        0x101,
        (
            "#0003F（ここは空家じゃない\x01",
            "  みたいだな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68B6")

    TalkEnd(0x13)
    Return()

    # Function_16_5F7D end

    def Function_17_68BA(): pass

    label("Function_17_68BA")

    SetChrName("")

    #A0406
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされており、\x01",
            "中から声が聞こえる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Return()

    # Function_17_68BA end

    def Function_18_68F5(): pass

    label("Function_18_68F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_696A")

    #C0407
    ChrTalk(
        0xFE,
        (
            "このアパートの連中、\x01",
            "意外としぶといな。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "フフ、まあよい……\x01",
            "いずれ全員追い出してやるわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A2F")

    label("loc_696A")

    OP_93(0xFE, 0x87, 0x0)
    OP_4B(0x8, 0xFF)

    #C0409
    ChrTalk(
        0xFE,
        (
            "それではまず住民登録を\x01",
            "確認させてもらいましょうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "フフ……まさか\x01",
            "未登録ということはありますまい？\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x8,
        (
            "ああ、もちろんじゃよ……\x01",
            "ワシはここに６０年も住んどるんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 7)

    label("loc_6A2F")

    TalkEnd(0xFE)
    Return()

    # Function_18_68F5 end

    def Function_19_6A33(): pass

    label("Function_19_6A33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6AD5")

    #C0412
    ChrTalk(
        0xFE,
        (
            "再開発計画が纏まれば\x01",
            "また業者の入札なんかがあるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "くくく……また大きなミラが動く。\x01",
            "共和国派に先んじて\x01",
            "手を打っておかないとねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B65")

    label("loc_6AD5")


    #C0414
    ChrTalk(
        0xFE,
        (
            "旧市街の人間なんて\x01",
            "後ろめたいことの１つや２つは\x01",
            "あるものだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "ふふふ……\x01",
            "連中にもクロスベルの発展に\x01",
            "貢献してもらおうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B65")

    TalkEnd(0xFE)
    Return()

    # Function_19_6A33 end

    def Function_20_6B69(): pass

    label("Function_20_6B69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6EF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6C2A")

    #C0416
    ChrTalk(
        0x10,
        (
            "#1808F劇団長とイリアさん、\x01",
            "脚本の調整は付いたかな……\x02\x03",

            "#1802Fそろそろ私も戻って\x01",
            "リハーサルに参加しますね。\x02\x03",

            "皆さん、どうかニコルさんの事は\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EEE")

    label("loc_6C2A")


    #C0417
    ChrTalk(
        0x101,
        (
            "#0005Fリーシャ？\x01",
            "こんな時間にどうしたんだ？\x02\x03",

            "#0001Fそろそろ公演の時間じゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x10,
        (
            "#1805Fあ、その……\x02\x03",

            "#1800F昼の公演が少し延びたので\x01",
            "忘れ物を取りに来たんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10)

    #C0419
    ChrTalk(
        0x10,
        (
            "#1808F皆さん、その、\x01",
            "ニコルさんの方は……\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        (
            "#0006Fああ、こっちでも\x01",
            "探しているけど……\x02\x03",

            "#0001F今のところ手がかりは\x01",
            "見つかっていないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x104,
        (
            "#0300Fま、ちょうど心当たりを\x01",
            "当たってる最中でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x10,
        (
            "#1806Fそうですか……\x02\x03",

            "#1801Fすみません、ニコルさんの事\x01",
            "よろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        "#0100Fええ、任せてちょうだい。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x103,
        (
            "#0204Fあの#4R ･  ･ #市長暗殺事件も\x01",
            "未然に防いだ特務支援課です。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x10A,
        "#0601F（ムッ……）\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x10,
        (
            "#1809Fふふっ……そうですね。\x02\x03",

            "#1804F…………………………（ペコリ）\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_6EEE")

    Jump("loc_70AE")

    label("loc_6EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6FD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_END)), "loc_6FCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6FC6")

    #C0427
    ChrTalk(
        0x10,
        (
            "#1809F今日は久々のオフで\x01",
            "友達と遊びに行く予定なんです。\x02\x03",

            "#1804Fイリアさんも誘ったんですけど\x01",
            "多分、起きてくれないかな……\x02\x03",

            "#1802Fオフの日は大抵、\x01",
            "夕方近くまで寝ていますから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FC9")

    label("loc_6FC6")

    Call(0, 21)

    label("loc_6FC9")

    Jump("loc_6FD1")

    label("loc_6FCE")

    Call(0, 22)

    label("loc_6FD1")

    Jump("loc_70AE")

    label("loc_6FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_END)), "loc_70AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_70A3")

    #C0428
    ChrTalk(
        0x10,
        (
            "#1802F今日は久々のオフで\x01",
            "友達と遊びに行く予定なんです。\x02\x03",

            "#1804Fイリアさんも誘ったんですけど\x01",
            "多分、起きてくれないかな……\x02\x03",

            "#1810Fオフの日は大抵、\x01",
            "夕方近くまで寝ていますから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB3, 2)
    Jump("loc_70A6")

    label("loc_70A3")

    Call(0, 21)

    label("loc_70A6")

    Jump("loc_70AE")

    label("loc_70AB")

    Call(0, 22)

    label("loc_70AE")

    TalkEnd(0xFE)
    Return()

    # Function_20_6B69 end

    def Function_21_70B2(): pass

    label("Function_21_70B2")

    TurnDirection(0x10, 0x153, 0)

    #C0429
    ChrTalk(
        0x10,
        (
            "#1808F（そうか……\x01",
            "  この子があの時の……）\x02\x03",

            "#1803F（……見たところ\x01",
            "  普通の子みたいだけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0430
    ChrTalk(
        0x153,
        (
            "#1110Fんー？\x01",
            "キーアのカオに\x01",
            "なにかついてるー？\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#0005Fひょっとして……\x01",
            "知ってる子だったりするかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x10,
        (
            "#1802Fいえ、あんまり可愛いから\x01",
            "見とれてしまって……\x02\x03",

            "#1809Fふふっ、一緒に散歩している\x01",
            "ロイドさんたちが羨ましいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x153,
        (
            "#1109Fえへへー。\x01",
            "リーシャもかわいいよー？\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x10,
        (
            "#1810Fあ、ありがとう。\x01",
            "（本当に可愛いな、この子……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_21_70B2 end

    def Function_22_7289(): pass

    label("Function_22_7289")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-1640, 1330, 55710, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -1630, 30, 54460, 0)
    SetChrPos(0xEF, -520, 30, 54660, 315)
    SetChrPos(0x153, -2610, 30, 55090, 45)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x10, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7385")

    #C0435
    ChrTalk(
        0x10,
        (
            "#1805Fあれ、ロイドさん？\x01",
            "それにエリィさんも……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x102,
        "#0102Fふふ、こんにちは。\x02",
    )

    CloseMessageWindow()
    Jump("loc_744E")

    label("loc_7385")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73E7")

    #C0437
    ChrTalk(
        0x10,
        (
            "#1805Fあれ、ロイドさん？\x01",
            "それにティオさんも……\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x103,
        "#0202Fどうもです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_744E")

    label("loc_73E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_744E")

    #C0439
    ChrTalk(
        0x10,
        (
            "#1805Fあれ、ロイドさん？\x01",
            "それにランディさんも……\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x104,
        "#0309Fよ、リーシャちゃん！\x02",
    )

    CloseMessageWindow()

    label("loc_744E")


    #C0441
    ChrTalk(
        0x101,
        (
            "#0002Fやあ、リーシャ。\x02\x03",

            "旧市街に住んでいるって\x01",
            "聞いてたけど、ここだったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x10,
        (
            "#1809Fふふっ、そうなんです。\x02\x03",

            "#1800Fお家賃が安かったので\x01",
            "決めてしまったんですけど。\x02\x03",

            "#1805Fえっと、ところで……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x10, 0x153, 500)
    Sleep(500)

    #C0443
    ChrTalk(
        0x101,
        (
            "#0012Fああ、この子はその、\x01",
            "ウチで預かってる子で──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(892, 0, 100, 0)
    Sleep(1000)
    OP_64(0x153)

    #C0444
    ChrTalk(
        0x153,
        (
            "#1105Fほええ～～っ……\x02\x03",

            "#1109Fねえねえロイド！\x01",
            "このおねえちゃん、おっぱい大きいね！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7653")

    #C0445
    ChrTalk(
        0x102,
        "#0105Fキ、キーアちゃん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_76D0")

    label("loc_7653")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7695")

    #C0446
    ChrTalk(
        0x103,
        (
            "#0206Fキーア……\x01",
            "さすがに直球過ぎです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76D0")

    label("loc_7695")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76D0")

    #C0447
    ChrTalk(
        0x104,
        (
            "#0305Fおお……\x01",
            "さすがキー坊だぜ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76D0")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x101, 0x153, 500)
    Sleep(1000)
    OP_64(0x101)

    #C0448
    ChrTalk(
        0x101,
        "#0011Fこ、こらキーア！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 500)

    #C0449
    ChrTalk(
        0x101,
        (
            "#0006Fごめんリーシャ。\x01",
            "なんか失礼なことを……\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x10,
        (
            "#1810Fい、いえ、いいんです。\x02\x03",

            "#1809F……ふふっ。\x01",
            "キーアちゃんって言うんだ。\x02\x03",

            "私はリーシャ。\x01",
            "リーシャ・マオっていうの。\x02\x03",

            "#1802Fよろしくね？\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x153,
        "#1109Fうんっ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x0)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0xB3, 1)
    EventEnd(0x5)
    Return()

    # Function_22_7289 end

    def Function_23_77FB(): pass

    label("Function_23_77FB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_68(8420, 4790, 16630, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19850, 0)
    SetChrPos(0x101, 1590, 0, 2420, 0)
    SetChrPos(0x102, 2600, 0, 1420, 45)
    SetChrPos(0x103, 440, 0, 1710, 0)
    SetChrPos(0x104, 1800, 0, 210, 135)
    SetChrPos(0x8, 3900, 2000, 11730, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)
    FadeToBright(1000, 0)
    OP_68(2260, 1300, 1970, 4800)
    MoveCamera(45, 30, 0, 4800)
    OP_6E(500, 4800)
    SetCameraDistance(19850, 4800)
    Sleep(4800)
    BeginChrThread(0x101, 3, 0, 24)
    BeginChrThread(0x102, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 26)
    BeginChrThread(0x104, 3, 0, 27)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7983")

    #C0452
    ChrTalk(
        0x102,
        (
            "#11P#0100Fここがロータスハイツ……で\x01",
            "間違いないみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        (
            "#5P#0000F市役所の書類によると\x01",
            "空室が３つもあるそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A67")

    label("loc_7983")


    #C0454
    ChrTalk(
        0x101,
        (
            "#5P#0000Fええと、表じゃ色々あったけど……\x01",
            "他の仕事も片付けておくか。\x02\x03",

            "ここが市庁舎から頼まれてた\x01",
            "アパートみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x102,
        (
            "#11P#0100F旧市街の『ロータスハイツ』ね……\x02\x03",

            "市役所の書類によると\x01",
            "空室が３つあるんだったかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A67")

    ClearChrFlags(0x8, 0x80)
    OP_95(0x8, 3900, 0, 3680, 2000, 0x0)
    OP_93(0x8, 0xE1, 0x1F4)

    #C0456
    ChrTalk(
        0x8,
        "#11Pおや、お役人かね？\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x0, 0x3)
    EndChrThread(0x1, 0x3)
    EndChrThread(0x2, 0x3)
    EndChrThread(0x3, 0x3)

    def lambda_7AB8():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7AB8)

    def lambda_7AC5():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7AC5)

    def lambda_7AD2():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_7AD2)

    def lambda_7ADF():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_7ADF)
    Sleep(300)

    #C0457
    ChrTalk(
        0x101,
        (
            "#6P#0005Fああ、いえ、警察の者でして。\x02\x03",

            "#0000F防犯上の都合で\x01",
            "こちらの空家３つを\x01",
            "確認させていただこうかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x8,
        (
            "#11Pおや、空家か。\x01",
            "空家は１室だけのはずじゃぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0459
    ChrTalk(
        0x103,
        "#6P#0205Fそうなんですか……？\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x8,
        "#5Pうむ、まあな。\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        (
            "#5P旧市街の人の出入りは\x01",
            "役所は把握しておらん。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x8,
        (
            "#5Pだからこそここが\x01",
            "旧市街と呼ばれるのじゃろうがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x8,
        (
            "#5Pまあ見たければ見ていくがいい。\x01",
            "ここのみんなを驚かさんようにな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7CCE():

        label("loc_7CCE")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_7CCE")

    QueueWorkItem2(0x0, 1, lambda_7CCE)

    def lambda_7CE0():

        label("loc_7CE0")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_7CE0")

    QueueWorkItem2(0x1, 1, lambda_7CE0)

    def lambda_7CF2():

        label("loc_7CF2")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_7CF2")

    QueueWorkItem2(0x2, 1, lambda_7CF2)

    def lambda_7D04():

        label("loc_7D04")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_7D04")

    QueueWorkItem2(0x3, 1, lambda_7D04)
    OP_95(0x8, 4330, 0, 0, 2000, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    def lambda_7D3A():
        OP_93(0xFE, 0x5A, 0x1E)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7D3A)

    def lambda_7D47():
        OP_93(0xFE, 0x5A, 0x1E)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7D47)

    def lambda_7D54():
        OP_93(0xFE, 0x5A, 0x1E)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_7D54)

    def lambda_7D61():
        OP_93(0xFE, 0x5A, 0x1E)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_7D61)
    OP_95(0x8, 7800, 0, 0, 2000, 0x0)

    def lambda_7D82():
        OP_95(0xFE, 7800, 0, -5680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7D82)

    #C0464
    ChrTalk(
        0x101,
        (
            "#5P#0000Fとりあえず\x01",
            "確認だけはしてみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x104,
        (
            "#11P#0300Fだな。\x01",
            "行ってみようぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x0, 1590, 0, 1570, 45)
    SetChrPos(0x1, 1590, 0, 1570, 45)
    SetChrPos(0x2, 1590, 0, 1570, 45)
    SetChrPos(0x3, 1590, 0, 1570, 45)
    EndChrThread(0x8, 0x1)
    SetChrPos(0x8, 4270, 0, -52160, 90)
    OP_29(0x3, 0x1, 0x6)
    SetScenarioFlags(0x1, 2)
    EventEnd(0x5)
    Return()

    # Function_23_77FB end

    def Function_24_7E64(): pass

    label("Function_24_7E64")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E8B")
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(10000)
    Jump("Function_24_7E64")

    label("loc_7E8B")

    Return()

    # Function_24_7E64 end

    def Function_25_7E8C(): pass

    label("Function_25_7E8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EC7")
    Sleep(1200)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1600)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1200)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(10000)
    Jump("Function_25_7E8C")

    label("loc_7EC7")

    Return()

    # Function_25_7E8C end

    def Function_26_7EC8(): pass

    label("Function_26_7EC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EF9")
    Sleep(1300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(10000)
    Jump("Function_26_7EC8")

    label("loc_7EF9")

    Return()

    # Function_26_7EC8 end

    def Function_27_7EFA(): pass

    label("Function_27_7EFA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F2B")
    Sleep(1000)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(10000)
    Jump("Function_27_7EFA")

    label("loc_7F2B")

    Return()

    # Function_27_7EFA end

    def Function_28_7F2C(): pass

    label("Function_28_7F2C")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-200, 4800, 21200, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, -1000, 3500, 19700, 0)
    SetChrPos(0x102, 370, 3500, 19700, 0)
    SetChrPos(0x103, 370, 3500, 18420, 0)
    SetChrPos(0x104, -1000, 3500, 18420, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_95(0x101, -460, 3500, 20950, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0466
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

    #C0467
    ChrTalk(
        0x101,
        (
            "#0001Fすみません！\x01",
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

    #C0468
    ChrTalk(
        0x103,
        "#0200F人の気配はないようですね。\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x101,
        "#0003Fああ、それに……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0470
    ChrTalk(
        0x101,
        (
            "#0001Fドアノブの上に\x01",
            "ホコリが積もっている。\x02\x03",

            "どうやらしばらくの間は\x01",
            "空家になっているみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x104,
        (
            "#0300Fなるほど、\x01",
            "間違いはなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x103,
        (
            "#0200F他の部屋には\x01",
            "住民の方がいるようですし……\x01",
            "空家は１軒のみですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#0103Fロータスハイツの……\x01",
            "ええと２０３号室ね。\x01",
            "（サラサラ……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82A6")

    #C0474
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
    Jump("loc_82DB")

    label("loc_82A6")


    #C0475
    ChrTalk(
        0x101,
        (
            "#0000Fよし、それじゃ\x01",
            "残りの件を当たってみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82DB")

    Sleep(200)
    SetChrPos(0x0, -250, 3500, 20480, 180)
    SetChrPos(0x1, -250, 3500, 20480, 180)
    SetChrPos(0x2, -250, 3500, 20480, 180)
    SetChrPos(0x3, -250, 3500, 20480, 180)
    SetScenarioFlags(0x1, 3)
    EventEnd(0x5)
    Return()

    # Function_28_7F2C end

    def Function_29_8328(): pass

    label("Function_29_8328")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8351")
    Call(0, 28)
    Jump("loc_83D0")

    label("loc_8351")

    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0476
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_83D0")

    #C0477
    ChrTalk(
        0x101,
        (
            "#0001Fドアノブにホコリが積もっている……\x01",
            "誰も掃除してないみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83D0")

    TalkEnd(0xFF)
    Return()

    # Function_29_8328 end

    SaveToFile()

Try(main)
