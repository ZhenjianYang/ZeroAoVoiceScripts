from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0350.bin",                # FileName
        "c0350",                    # MapName
        "c0350",                    # Location
        0x002D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 45, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0350",                  # 0
        "ユーリ",                 # 1
        "サイクス",               # 2
        "レジー",                 # 3
        "ホステス",               # 4
        "ホステス",               # 5
        "ホステス",               # 6
        "ホステス",               # 7
    ))

    AddCharChip((
        "chr/ch44100.itc",                   # 00
        "chr/ch47500.itc",                   # 01
        "chr/ch23600.itc",                   # 02
        "chr/ch44102.itc",                   # 03
        "chr/ch26802.itc",                   # 04
        "chr/ch26900.itc",                   # 05
    ))

    DeclNpc(7989,    200,     1600,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(5699,    0,       469,     45,   261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(7780,    0,       -810,    0,    261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(7989,    200,     2200,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(2309,    0,       3529,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(6270,    0,       1580,    1000,    7990,    1500,    2200,    0x007E, 0,  11, 0x0000)

    ChipFrameInfo(496, 0)                                        # 0

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_2A0",          # 01, 1
        "Function_2_2CB",          # 02, 2
        "Function_3_6FA",          # 03, 3
        "Function_4_7B2",          # 04, 4
        "Function_5_150D",         # 05, 5
        "Function_6_16D5",         # 06, 6
        "Function_7_17E7",         # 07, 7
        "Function_8_2061",         # 08, 8
        "Function_9_2112",         # 09, 9
        "Function_10_22D1",        # 0A, 10
        "Function_11_2AD1",        # 0B, 11
        "Function_12_2AD5",        # 0C, 12
        "Function_13_2B4B",        # 0D, 13
        "Function_14_2BEC",        # 0E, 14
        "Function_15_3A0D",        # 0F, 15
        "Function_16_4E17",        # 10, 16
        "Function_17_4E5B",        # 11, 17
        "Function_18_4EB3",        # 12, 18
        "Function_19_4EFE",        # 13, 19
        "Function_20_4F56",        # 14, 20
        "Function_21_4FA1",        # 15, 21
        "Function_22_4FD1",        # 16, 22
    ))


    def Function_0_1F0(): pass

    label("Function_0_1F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_228"),
        (1, "loc_234"),
        (2, "loc_240"),
        (3, "loc_24C"),
        (4, "loc_258"),
        (5, "loc_264"),
        (6, "loc_270"),
        (SWITCH_DEFAULT, "loc_27C"),
    )


    label("loc_228")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_234")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_240")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_24C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_258")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_264")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_270")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_27C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_29F")

    Return()

    # Function_0_1F0 end

    def Function_1_2A0(): pass

    label("Function_1_2A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CA")
    OP_94(0xFE, 0x334, 0x2904, 0xFFFFF31C, 0x3804, 0x3E8)
    Sleep(300)
    Jump("Function_1_2A0")

    label("loc_2CA")

    Return()

    # Function_1_2A0 end

    def Function_2_2CB(): pass

    label("Function_2_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_320")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_31B")

    Jump("loc_6B8")

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_367")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -1100, 4000, 12070, 90)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 6510, 0, -2040, 180)
    Jump("loc_6B8")

    label("loc_367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_397")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 6510, 0, -2040, 180)
    Jump("loc_6B8")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3DE")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -1100, 4000, 12070, 90)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 6510, 0, -2040, 180)
    Jump("loc_6B8")

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3FB")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_442")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -1100, 4000, 12070, 90)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 8119, 0, -2400, 135)
    Jump("loc_6B8")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_45F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47C")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4CB")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -2370, 4000, 13480, 90)
    SetChrPos(0xA, -840, 4000, 13480, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4C6")
    SetChrFlags(0xFE, 0x10)

    label("loc_4C6")

    Jump("loc_6B8")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_516")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 1000, 0, 3700, 270)
    SetChrPos(0xA, -500, 0, 3700, 90)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    Jump("loc_6B8")

    label("loc_516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BD")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_569")
    SetChrPos(0x9, -1100, 4000, 12070, 90)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 6510, 0, -2040, 180)
    Jump("loc_5B8")

    label("loc_569")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B8")
    SetChrPos(0x8, 7140, 4500, 5660, 180)
    SetChrPos(0x9, 7910, 0, -1840, 90)
    SetChrPos(0xA, 5410, 4000, 5440, 90)
    Jump("loc_5B8")

    label("loc_5B8")

    Jump("loc_6B8")

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5DA")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_5DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6A0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_604")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_69B")

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_69B")

    label("loc_61D")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65D")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_65D")

    SetChrSubChip(0xB, 0x1)
    SetChrSubChip(0x8, 0x2)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0x9, 1000, 0, 3730, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68A")
    SetChrFlags(0x9, 0x10)

    label("loc_68A")

    SetChrPos(0xA, 8060, 0, -2310, 135)

    label("loc_69B")

    Jump("loc_6B8")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6B8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_6B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6CC")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F9")
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_6F9")

    Return()

    # Function_2_2CB end

    def Function_3_6FA(): pass

    label("Function_3_6FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73F")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_73F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77A")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)

    label("loc_77A")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79E")
    Jump("loc_7B1")

    label("loc_79E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AD")
    Jump("loc_7B1")

    label("loc_7AD")

    OP_66(0x0, 0x1)

    label("loc_7B1")

    Return()

    # Function_3_6FA end

    def Function_4_7B2(): pass

    label("Function_4_7B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7C3")
    Jump("loc_1509")

    label("loc_7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_810")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DE")
    Call(0, 5)
    Jump("loc_80B")

    label("loc_7DE")


    #C0001
    ChrTalk(
        0xFE,
        (
            "くそっ……\x01",
            "なんで俺たちがこんな目に……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80B")

    Jump("loc_1509")

    label("loc_810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_995")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_900")

    #C0002
    ChrTalk(
        0xFE,
        (
            "早くクロスベルを離れろと\x01",
            "共和国政府から通達があったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "フン、混雑している列車で\x01",
            "もみくちゃになって帰るなど\x01",
            "まっぴらごめんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "免停が解けるのを待って、\x01",
            "調達したクルマで\x01",
            "悠々と帰国させてもらうさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_990")

    label("loc_900")


    #C0005
    ChrTalk(
        0xFE,
        (
            "混雑している列車で\x01",
            "もみくちゃになって帰るなど\x01",
            "まっぴらごめんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "免停が解けるのを待って、\x01",
            "調達したクルマで\x01",
            "悠々と帰国させてもらうさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_990")

    Jump("loc_1509")

    label("loc_995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACC")

    #C0007
    ChrTalk(
        0xFE,
        (
            "この間の襲撃事件で、\x01",
            "警察や警備隊にかなりの被害が\x01",
            "出たそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "ククク……いい気味だな。\x01",
            "俺たちに無礼を働いた罰が\x01",
            "下ったんじゃないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#00103F（……行きましょう。\x01",
            "  こんな連中に構っている暇はないわ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x105,
        (
            "#10300F（ま、愚か者には\x01",
            "  何を言ってもムダってね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B36")

    label("loc_ACC")


    #C0011
    ChrTalk(
        0xFE,
        (
            "この間の襲撃事件で、\x01",
            "警察や警備隊にかなりの被害が\x01",
            "出たそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "ククク……いい気味だな。\x02",
    )

    CloseMessageWindow()

    label("loc_B36")

    Jump("loc_1509")

    label("loc_B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C7A")

    #C0013
    ChrTalk(
        0xFE,
        (
            "フン、罰則は罰則だからな。\x01",
            "しばらくは大人しくしておいてやる。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "……さっさとどこかへ行け。\x01",
            "お前たちに構ってる暇なんかないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x109,
        (
            "#10100F（ケイトさんに怒られたのが\x01",
            "  けっこう堪えてるみたいですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00004F（ああ……\x01",
            "  しばらくは馬鹿な真似をする\x01",
            "  心配もなさそうだ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D43")

    label("loc_C7A")


    #C0017
    ChrTalk(
        0xFE,
        "……何の用だ。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "警察の人間なんかに\x01",
            "構っている暇はない。\x01",
            "……さっさと出て行け。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#00005F（何かあったのか……？）\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x109,
        (
            "#10105F（そういえば、いつもあった場所に\x01",
            "  導力車が無かったような……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D43")

    SetScenarioFlags(0x0, 0)
    Jump("loc_D8E")

    label("loc_D4B")


    #C0021
    ChrTalk(
        0xFE,
        (
            "……さっさとどこかへ行け。\x01",
            "お前たちに構ってる暇なんかないぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8E")

    Jump("loc_1509")

    label("loc_D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DA1")
    Jump("loc_1509")

    label("loc_DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E0B")

    #C0022
    ChrTalk(
        0xFE,
        (
            "ちっ、レジーの奴は\x01",
            "運転以外はノロマだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "紅茶くらいさっさと\x01",
            "入れて欲しいものだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1509")

    label("loc_E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E19")
    Jump("loc_1509")

    label("loc_E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E27")
    Jump("loc_1509")

    label("loc_E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFC")

    #C0024
    ChrTalk(
        0xFE,
        (
            "今日は歓楽街の\x01",
            "《ノイエ＝ブラン》とやらに\x01",
            "行ってみるとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "クク、お前たちみたいな庶民には\x01",
            "まったく縁のない店だろうがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#00012F（わ、割とそうでもなかったりして……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F3D")

    label("loc_EFC")


    #C0027
    ChrTalk(
        0xFE,
        (
            "……それにしても、遅い。\x01",
            "サイクスとレジーは何をやってる……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3D")

    Jump("loc_1509")

    label("loc_F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_117F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10EE")

    #C0028
    ChrTalk(
        0xFE,
        "……こんな夜中に何の用だ？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "昼間にお前たちがしたこと……\x01",
            "忘れたとは言わせないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x10A,
        (
            "#00605F（お前たち……\x01",
            "  彼らと何かあったのか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#00306F（いや、ありゃあ\x01",
            "  仕方なかったっつーか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x10A,
        (
            "#00603F（まったく……この微妙な時期に\x01",
            "  下らないトラブルを起こすな。）\x02\x03",

            "#00600F（明日の本会議が終わるまで、\x01",
            "  絶対に気を抜くんじゃないぞ。\x01",
            "  ……いいな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#00005F（りょ、了解です。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x149, 3)
    Jump("loc_117A")

    label("loc_10EE")


    #C0034
    ChrTalk(
        0xFE,
        (
            "昼間にお前たちがしたこと……\x01",
            "忘れたとは言わせないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "いつか必ず後悔させてやる。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        "#00306F（いい加減しつこいっつーの……）\x02",
    )

    CloseMessageWindow()

    label("loc_117A")

    Jump("loc_1509")

    label("loc_117F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1463")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_125C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121A")

    #C0037
    ChrTalk(
        0xFE,
        (
            "お前たちが俺にした仕打ち……\x01",
            "タダでは済まさないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "自治州の警察ごときが\x01",
            "図に乗るんじゃあないぞ……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1257")

    label("loc_121A")


    #C0039
    ChrTalk(
        0xFE,
        (
            "お前たちが俺にした仕打ち……\x01",
            "タダでは済まさないからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1257")

    Jump("loc_145E")

    label("loc_125C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1400")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B9")

    #C0040
    ChrTalk(
        0xFE,
        (
            "……くそっ……\x01",
            "この俺にこんな仕打ち……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "お前たち……\x01",
            "……タダで済むと思うなよ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x1A3,
        (
            "#04609Fあはは、弱っちいくせに\x01",
            "な～に強がってんのさ。\x02\x03",

            "#04604Fま、かかってくるってんなら\x01",
            "いつでもおいでよ。\x02\x03",

            "#04611Fもちろん、殺される覚悟でね♪\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        "……くっ……！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        "#00303F……もういい、行くぞシャーリィ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FB")

    label("loc_13B9")


    #C0045
    ChrTalk(
        0xFE,
        (
            "……くそっ……\x01",
            "この俺にこんな仕打ち……\x01",
            "絶対に許さんぞ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FB")

    Jump("loc_145E")

    label("loc_1400")


    #C0046
    ChrTalk(
        0xFE,
        (
            "クク、勝手に俺たちの城に\x01",
            "入ってきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "あれくらいの罰は\x01",
            "与えられて当然だろうさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145E")

    Jump("loc_1509")

    label("loc_1463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1471")
    Jump("loc_1509")

    label("loc_1471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1500")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1494")
    Call(0, 6)
    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x2)
    Return()

    label("loc_1494")


    #C0048
    ChrTalk(
        0xFE,
        "なんだお前達、まだいたのか？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "フン、仕事は済んだんだろう？\x01",
            "さっさとお引取り願おうか。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x2)
    Return()

    label("loc_1500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1509")

    label("loc_1509")

    TalkEnd(0xFE)
    Return()

    # Function_4_7B2 end

    def Function_5_150D(): pass

    label("Function_5_150D")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0050
    ChrTalk(
        0x9,
        "おい、外は化物で一杯だぜ！？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        (
            "もしかしたらあいつら、\x01",
            "俺たちまで襲ってくるんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xA,
        "ど、どうしようユーリ！？\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        "い、今考えてる、黙ってろ！\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "くそっ……\x01",
            "なんで俺たちがこんな目に……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16BA")

    #C0055
    ChrTalk(
        0x101,
        (
            "#00005F（《ハイブラッズ》……\x01",
            "  まだクロスベルにいたのか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        (
            "#00200F（共和国に帰るタイミングを\x01",
            "  逃してしまったようですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#00303F（まあ、家にいる以上は\x01",
            "  放っておいても大丈夫だろ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BA")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_5_150D end

    def Function_6_16D5(): pass

    label("Function_6_16D5")


    #C0058
    ChrTalk(
        0xB,
        (
            "それにしても、みんな若いのに\x01",
            "こんな大きなお屋敷に\x01",
            "住んでるなんてすごいわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        "フフ、大したことはないさ。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "共和国にある実家に比べれば\x01",
            "犬小屋みたいなもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x109,
        "#10105F（い、犬小屋って……）\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        (
            "#10309F（ハハ、本当に\x01",
            "  調子に乗ってるなあ。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_6_16D5 end

    def Function_7_17E7(): pass

    label("Function_7_17E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_17F8")
    Jump("loc_205D")

    label("loc_17F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1877")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1813")
    Call(0, 5)
    Jump("loc_1872")

    label("loc_1813")


    #C0063
    ChrTalk(
        0xFE,
        "ああもう、どうなってんだあ！？\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "俺たちが襲われたら、\x01",
            "誰が責任をとってくれるんだよ！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1872")

    Jump("loc_205D")

    label("loc_1877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1910")

    #C0065
    ChrTalk(
        0xFE,
        (
            "独立宣言ねえ。\x01",
            "そういえば、なんだか\x01",
            "以前から騒がれてたみてえだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "ま、ユーリが大丈夫って言ってるし\x01",
            "多分大丈夫なんだろうけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_205D")

    label("loc_1910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D5")

    #C0067
    ChrTalk(
        0xFE,
        (
            "あーあー、ここ最近\x01",
            "街中がジメジメした雰囲気で\x01",
            "やんなっちまったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "よっしゃ、ここらでいっちょ\x01",
            "ドライブにでも……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "はあ、でも……\x01",
            "クルマがないんだったな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A50")

    label("loc_19D5")


    #C0070
    ChrTalk(
        0xFE,
        (
            "はあ……\x01",
            "クルマ、壊れちまったんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "気晴らしにドライブにでも\x01",
            "行きたかったんだが……\x01",
            "ガマンするしかねえか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A50")

    Jump("loc_205D")

    label("loc_1A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1ABE")

    #C0072
    ChrTalk(
        0xFE,
        (
            "あーあ、あの導力車は\x01",
            "乗り心地が最高だったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "しばらくは退屈しそうだぜ～……\x02",
    )

    CloseMessageWindow()
    Jump("loc_205D")

    label("loc_1ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1ACC")
    Jump("loc_205D")

    label("loc_1ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B33")

    #C0074
    ChrTalk(
        0xFE,
        (
            "ヘヘっ、最近使ってる\x01",
            "ドライブコースが最高でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "やっぱ市内よりも街道だよなー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_205D")

    label("loc_1B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B41")
    Jump("loc_205D")

    label("loc_1B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B4F")
    Jump("loc_205D")

    label("loc_1B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1C78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C0B")

    #C0076
    ChrTalk(
        0xFE,
        (
            "ユーリのやつ、昨晩の夜のドライブで\x01",
            "すっかり機嫌が直ったみたいでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "やれやれ、アイツは案外手がかかるよな。\x01",
            "……本人の前じゃ絶対言わないけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    TalkEnd(0xFE)
    SetChrFlags(0xFE, 0x10)
    Return()

    label("loc_1C0B")


    #C0078
    ChrTalk(
        0xFE,
        (
            "さあ、《ノイエ＝ブラン》に\x01",
            "行く準備をするとすっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "……どした、レジー。\x01",
            "なんだか眠そうだが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_205D")

    label("loc_1C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1C89")
    Call(0, 9)
    Jump("loc_205D")

    label("loc_1C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FD1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D24")

    #C0080
    ChrTalk(
        0xFE,
        "ひっ……！？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "……って、あの赤毛のガキは\x01",
            "もういないのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "……ハ、ハン！\x01",
            "調子に乗るんじゃねえぞ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D7A")

    label("loc_1D24")


    #C0083
    ChrTalk(
        0xFE,
        "俺は別にビビッてなんかねえからな……！\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "……ちょ、調子に乗るんじゃねえぞ！？\x02",
    )

    CloseMessageWindow()

    label("loc_1D7A")

    Jump("loc_1FCC")

    label("loc_1D7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE9")
    OP_93(0xFE, 0x5A, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x1A3, 500)

    #C0085
    ChrTalk(
        0xFE,
        "ひっ……また来たのか！？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "そ、それ以上近寄るんじゃねえ！！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1A3,
        (
            "#04606Fんー、シャーリィはもう\x01",
            "お兄さんたちに興味ないんだけどな。\x02\x03",

            "#04609Fねえねえ、早くマリーを探しに行こうよ♪\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00003Fあ、ああ……そうだな。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x105,
        (
            "#10302Fさっきまでの殺気が\x01",
            "ウソみたいな無邪気さだねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F3C")

    label("loc_1EE9")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0090
    ChrTalk(
        0xFE,
        (
            "そ、それ以上近寄るんじゃねえ！！\x01",
            "あっち行けっつの！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3C")

    Jump("loc_1FCC")

    label("loc_1F41")


    #C0091
    ChrTalk(
        0xFE,
        (
            "はは、見たかよさっきの。\x01",
            "ちょっと脅かしたくらいで\x01",
            "飛んで逃げちまいやがったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "弱い者イジメって\x01",
            "何でこんなに楽しいんだろうな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCC")

    Jump("loc_205D")

    label("loc_1FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FDF")
    Jump("loc_205D")

    label("loc_1FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2054")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFA")
    Call(0, 8)
    Jump("loc_204F")

    label("loc_1FFA")


    #C0093
    ChrTalk(
        0xFE,
        (
            "……何だお前ら、\x01",
            "仲間に入れてほしいのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "クク、そこで指でもくわえてな。\x02",
    )

    CloseMessageWindow()

    label("loc_204F")

    Jump("loc_205D")

    label("loc_2054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_205D")

    label("loc_205D")

    TalkEnd(0xFE)
    Return()

    # Function_7_17E7 end

    def Function_8_2061(): pass

    label("Function_8_2061")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0095
    ChrTalk(
        0x9,
        "ささっ、そっちに座って座って。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "いいワインを用意してるんだ、\x01",
            "お姉さんも一緒に飲みましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xC,
        (
            "ウフフ、それじゃあ\x01",
            "お酌させてもらおうかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_8_2061 end

    def Function_9_2112(): pass

    label("Function_9_2112")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_225F")

    #C0098
    ChrTalk(
        0x9,
        (
            "ユーリのやつ、\x01",
            "さすがに機嫌悪いな……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "歓楽街で気分転換しようにも、\x01",
            "ＶＩＰの警備とかで\x01",
            "警官がけっこういるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        (
            "うーん、それじゃあ……\x01",
            "クルマで山道のほうに\x01",
            "夜のドライブとかどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "この時間なら通行者も\x01",
            "少ないだろうし、思う存分\x01",
            "かっとばせそうだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        "おお、結構いい考えかもな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22C8")

    label("loc_225F")


    #C0103
    ChrTalk(
        0x9,
        (
            "よっしゃ、そうと決まれば\x01",
            "ユーリに提案してみるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        "レジー、お前車の準備しとけよ。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        "了解っ。\x02",
    )

    CloseMessageWindow()

    label("loc_22C8")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_2112 end

    def Function_10_22D1(): pass

    label("Function_10_22D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22E2")
    Jump("loc_2ACD")

    label("loc_22E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2350")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FD")
    Call(0, 5)
    Jump("loc_234B")

    label("loc_22FD")


    #C0106
    ChrTalk(
        0xFE,
        (
            "やっぱり独立宣言のとき、\x01",
            "無理してでも共和国に\x01",
            "帰るべきだったのかもな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_234B")

    Jump("loc_2ACD")

    label("loc_2350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23EB")

    #C0107
    ChrTalk(
        0xFE,
        (
            "ユーリは余裕を見せてるけど……\x01",
            "……だ、大丈夫なのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "このタイミングを逃したら、\x01",
            "下手すりゃ共和国に\x01",
            "帰れなくなっちまうんじゃ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACD")

    label("loc_23EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2490")

    #C0109
    ChrTalk(
        0xFE,
        (
            "（ユーリはあんな事言ってるけど……\x01",
            "  さすがにヒドいよな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "（俺たちのほうから\x01",
            "  さりげなく言っておくから、\x01",
            "  あんまり気にしないでくれよ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACD")

    label("loc_2490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_25DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2546")

    #C0111
    ChrTalk(
        0xFE,
        (
            "……へっくしょん！！\x01",
            "風邪引いちまったかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "やっぱ昨日、\x01",
            "池に落ちたのが悪かったのかなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "……はあ、自業自得ってやつか。\x01",
            "やるせねえ～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_25DA")

    label("loc_2546")


    #C0114
    ChrTalk(
        0xFE,
        (
            "ずびずび……\x01",
            "ウルスラ病院に行って\x01",
            "薬もらってこようかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "なんだかマインツで\x01",
            "大変な事があったらしいけど、\x01",
            "バスとか普通に出てんのかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25DA")

    Jump("loc_2ACD")

    label("loc_25DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_25ED")
    Jump("loc_2ACD")

    label("loc_25ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_26AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267E")

    #C0116
    ChrTalk(
        0xFE,
        (
            "あれ、なんだかさっき、\x01",
            "サイレンの音が聞こえたような……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "……まあいいか。\x01",
            "えーっと、ユーリの好きな紅茶は……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26A6")

    label("loc_267E")


    #C0118
    ChrTalk(
        0xFE,
        "えーっと、ユーリの好きな紅茶は……\x02",
    )

    CloseMessageWindow()

    label("loc_26A6")

    Jump("loc_2ACD")

    label("loc_26AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_26B9")
    Jump("loc_2ACD")

    label("loc_26B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_26C7")
    Jump("loc_2ACD")

    label("loc_26C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2765")

    #C0119
    ChrTalk(
        0xFE,
        (
            "昨晩から今朝まで、\x01",
            "山道を何往復もさせられてさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "ふああ、眠い……\x01",
            "ユーリもサイクスも、\x01",
            "運転する方の身になってほしいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27CB")

    label("loc_2765")


    #C0121
    ChrTalk(
        0xFE,
        (
            "ユーリの機嫌が直ったのは\x01",
            "よかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "ふああ、眠い……\x01",
            "飲みに行く前に眠らせてくれえ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CB")

    Jump("loc_2ACD")

    label("loc_27D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_27E1")
    Call(0, 9)
    Jump("loc_2ACD")

    label("loc_27E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A2C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2872")

    #C0123
    ChrTalk(
        0xFE,
        (
            "も、もう金輪際、\x01",
            "猫なんかイジメない……\x01",
            "それだけは絶対守らないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "もしまたあのガキが来たら……\x01",
            "……ぶるっ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A27")

    label("loc_2872")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2988")
    OP_93(0xFE, 0x5A, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x1A3, 500)

    #C0125
    ChrTalk(
        0xFE,
        "うわっ、また……！？\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x1A3,
        "#4S#04602F……わっ！！\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "ひいいいいっ！？\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x1A3,
        "#04609Fあはははっ、なにビビッてんの～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A3, 500)

    #C0129
    ChrTalk(
        0x102,
        (
            "#00106F（ふう……この無邪気さは\x01",
            "  ある意味タチが悪いわね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29CD")

    label("loc_2988")


    #C0130
    ChrTalk(
        0xFE,
        (
            "も、もうやめてくれよ……\x01",
            "もう絶対猫なんかイジメないから、な！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29CD")

    Jump("loc_2A27")

    label("loc_29D2")


    #C0131
    ChrTalk(
        0xFE,
        "くくっ、傑作だったよな～。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "ま、ちっちゃかったし\x01",
            "ちょっとだけ可哀想だけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A27")

    Jump("loc_2ACD")

    label("loc_2A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A3A")
    Jump("loc_2ACD")

    label("loc_2A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2AC4")

    #C0133
    ChrTalk(
        0xFE,
        (
            "さーて、ちゃちゃっと\x01",
            "ツマミなんかを作っちまうかなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "へへ、共和国から持ってきた\x01",
            "高級ワインなんかも空けちまうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACD")

    label("loc_2AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2ACD")

    label("loc_2ACD")

    TalkEnd(0xFE)
    Return()

    # Function_10_22D1 end

    def Function_11_2AD1(): pass

    label("Function_11_2AD1")

    Call(0, 12)
    Return()

    # Function_11_2AD1 end

    def Function_12_2AD5(): pass

    label("Function_12_2AD5")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEA")
    Call(0, 6)
    Jump("loc_2B43")

    label("loc_2AEA")


    #C0135
    ChrTalk(
        0xB,
        "（久しぶりの上客じゃな～い☆）\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "（フフ、ジャンジャン\x01",
            "  稼がせてもらおうっと。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B43")

    TalkEnd(0xB)
    SetChrSubChip(0xB, 0x1)
    Return()

    # Function_12_2AD5 end

    def Function_13_2B4B(): pass

    label("Function_13_2B4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B60")
    Call(0, 8)
    Jump("loc_2BE8")

    label("loc_2B60")

    OP_4B(0xFE, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0137
    ChrTalk(
        0xFE,
        (
            "え、じゃあ外に置いてあった\x01",
            "あのクルマもあなたたちのなの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "へへ、すごいっしょ～。\x01",
            "今度乗せてやりましょーか？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0x9, 0xFF)

    label("loc_2BE8")

    TalkEnd(0xFE)
    Return()

    # Function_13_2B4B end

    def Function_14_2BEC(): pass

    label("Function_14_2BEC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch47502.itc", 0x1E)
    LoadChrToIndex("chr/ch26800.itc", 0x1F)
    LoadChrToIndex("chr/ch26900.itc", 0x20)
    LoadChrToIndex("chr/ch44102.itc", 0x21)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5700, 200, 4900, 180)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 7900, 200, 2450, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 5700, 0, 470, 360)
    OP_4B(0xA, 0xFF)
    OP_68(5030, 1500, 1370, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24150, 0)
    SetCameraDistance(23150, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0139
    ChrTalk(
        0x8,
        (
            "#5Pはー、しかし今朝のドライブは\x01",
            "最高だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "#12Pへへっ、今日は雨を活かして\x01",
            "ドリフトを決めまくったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#5Pああ、確かに\x01",
            "なかなかのスリルだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#5Pそれより、レジー。\x01",
            "今朝頼んでおいたお姉さん方は\x01",
            "ちゃんと来るんだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "#12Pああ、ちょっと待ってなって。\x01",
            "たぶんそろそろ――\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(300)
    Fade(500)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x105, 0x80)
    OP_68(2670, 1400, -1580, 0)
    MoveCamera(19, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 1500, 50, -2250, 45)
    SetChrPos(0x109, 500, 50, -2500, 45)
    SetChrPos(0x102, 1500, 50, -3500, 45)
    SetChrPos(0x105, 500, 50, -3750, 45)
    OP_0D()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2EDE():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2EDE)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)

    #C0144
    ChrTalk(
        0xA,
        "お、来た来た♪\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        "#5Pフフ、グッドタイミングだな。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_31CA")
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0146
    ChrTalk(
        0xA,
        "って、お前らは昨日のお巡り！？\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        "な、何でこんな所に……！\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        (
            "#6P#00105F……昨日の暴走車の３人組ね。\x02\x03",

            "#00103F一体どういうことかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x105,
        "#6P#10302Fもしかして泥棒中、とか？\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x109,
        "#6P#10101Fだったら現行犯逮捕、ですね。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xA,
        "バ、バカ言え……！\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            "泥棒だったら\x01",
            "とっととトンズラこいてらぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "#5Pというより、\x01",
            "お巡りが一体何の用だ？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        (
            "#5P俺たちの家に、勝手に\x01",
            "上がり込むとはいい度胸だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        "#6P#00105Fということはつまり……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#6P#00003Fああ、どうやら彼らが\x01",
            "この家の新たな住民みたいだな。\x02\x03",

            "#00000Fなあ君たち、今日ここへ来たのは\x01",
            "他でもない警察の仕事のためだ。\x02\x03",

            "時間は取らせないから\x01",
            "事情聴取に付き合ってもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B9")

    label("loc_31CA")

    OP_63(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0157
    ChrTalk(
        0xA,
        "へへっ、なかなかの上玉じゃん。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        "だな、こいつぁ期待以上だぜ。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x102,
        "#6P#00105F……えっと？\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x109,
        "#6P#10106Fどういうことでしょう？\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "#5Pああ、送迎の人もご苦労さん。\x01",
            "チップをやるから取りに来なよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x105,
        (
            "#6P#10306Fやれやれ……どうやら\x01",
            "自宅に呼んだホステスか何かと\x01",
            "勘違いしてるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#6P#00003F……ここは単刀直入に行こう。\x02\x03",

            "#00000F申し訳ないんだが、\x01",
            "自分たちはクロスベル警察の\x01",
            "特務支援課という者だ。\x02\x03",

            "時間は取らせないから\x01",
            "事情聴取に付き合ってもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -700, 0, 3250, 180)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 300, 0, 3250, 180)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -1700, 0, 3250, 180)
    SetChrPos(0x101, -1260, 0, -250, 0)
    SetChrPos(0x102, -100, 0, -250, 0)
    SetChrPos(0x109, -1260, 0, -1800, 0)
    SetChrPos(0x105, -100, 0, -1800, 0)
    OP_68(-890, 1400, 510, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(190, 0)
    SetCameraDistance(42740, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0164
    ChrTalk(
        0x101,
        (
            "#12P#00003Fつまり、君たち３人が\x01",
            "クロスベル入りした目的は社会勉強……\x02\x03",

            "滞在先を探していたら、たまたま\x01",
            "売りに出されていたこの家を見つけて\x01",
            "そちらのユーリ君が購入した……\x02\x03",

            "#00001F……そういう事情か。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        "#5Pああ、理解したか？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#12P#00105Fちなみに――\x01",
            "《ハイブラッズ》という名前は\x01",
            "いったい何のことかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "#5Pへへっ、聞きたいか？\x01",
            "そいつは俺たち３人のチーム名だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "#5P《高貴なる血》――\x01",
            "女神に愛された俺たちに\x01",
            "ピッタリだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x9,
        (
            "#5Pクク、ってのも実は俺たちの\x01",
            "親父はみんなあのヴェルヌ社の\x01",
            "お偉いさんでなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "#5P中でもユーリの親父さんは取締役――\x01",
            "コビを売るなら今の内だぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        "#5Pフフン、まあそういうことだ。\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_68(-580, 1400, -640, 3000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xD, 1260, 0, -4800, 0)
    SetChrPos(0xE, 1260, 0, -6000, 0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_377A():
        OP_95(0xD, 1260, 0, -2000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_377A)
    Sleep(50)

    def lambda_3797():
        OP_95(0xE, 1260, 0, -3000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3797)
    Sleep(50)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_6F(0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xD, 1)
    Sound(104, 0, 100, 0)

    def lambda_37E8():
        OP_93(0xD, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_37E8)
    Sleep(50)
    WaitChrThread(0xE, 1)

    def lambda_37FC():
        OP_93(0xE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_37FC)
    Sleep(50)

    def lambda_380C():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_380C)
    Sleep(50)

    def lambda_381C():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_381C)
    Sleep(50)

    def lambda_382C():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_382C)
    Sleep(50)

    def lambda_383C():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_383C)

    #C0172
    ChrTalk(
        0xA,
        "#5Pおっ、待ってました♪\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        "#5Pハ、今度こそ本物みてえだな。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xD,
        (
            "#12Pえっと……\x01",
            "《ハイブラッズ》さんは\x01",
            "どちら様かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xE,
        (
            "#12Pふう、何だか\x01",
            "取り込み中みたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "#5Pああ、お姉さんたち。\x01",
            "もう終わったから大丈夫さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x8,
        (
            "#5Pそういうわけでお前たち、\x01",
            "ただちにお引取り願おうか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_396C():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_396C)
    Sleep(50)

    def lambda_397C():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_397C)
    Sleep(50)

    def lambda_398C():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_398C)
    Sleep(50)

    def lambda_399C():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_399C)
    Sleep(300)

    #C0178
    ChrTalk(
        0x101,
        (
            "#12P#00003Fああ、言われなくても\x01",
            "そのつもりだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(128, 2000, 40)
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c0300", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2BEC end

    def Function_15_3A0D(): pass

    label("Function_15_3A0D")

    EventBegin(0x0)
    LoadChrToIndex("apl/ch51269.itc", 0x1E)
    SoundLoad(3975)
    SoundLoad(3976)
    SoundLoad(3977)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5700, 200, 4900, 180)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 950, 0, 700, 180)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 5700, 0, 470, 360)
    OP_68(1710, 2500, -380, 0)
    MoveCamera(24, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23750, 0)
    SetChrPos(0x101, 980, 0, -6650, 0)
    SetChrPos(0x102, 980, 0, -6650, 0)
    SetChrPos(0x109, 980, 0, -6650, 0)
    SetChrPos(0x105, 980, 0, -6650, 0)
    SetChrPos(0x104, 980, 0, -6650, 0)
    SetChrPos(0x1A3, 980, 0, -6650, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(1710, 1400, -380, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(103, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 16)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 20)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 18)
    Sleep(700)
    BeginChrThread(0x1A3, 3, 0, 21)
    WaitChrThread(0x1A3, 3)
    OP_6F(0x1)

    #C0179
    ChrTalk(
        0x9,
        "おっと……なんだ？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    TurnDirection(0xA, 0x101, 500)
    WaitChrThread(0xA, 1)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0180
    ChrTalk(
        0xA,
        (
            "って、\x01",
            "この前のお巡りじゃねえか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x8,
        (
            "#11Pフン……\x01",
            "《特務支援課》とか言ったか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0182
    ChrTalk(
        0x101,
        (
            "#6P#00003Fその節はどうも。\x02\x03",

            "#6P#00000Fちょっと話を\x01",
            "聞きたいんだけどいいかな？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0x8, -700, 0, 3250, 180)
    SetChrPos(0xA, 300, 0, 3250, 180)
    SetChrPos(0x9, -1700, 0, 3250, 180)
    OP_68(-1040, 1400, 630, 0)
    MoveCamera(38, 26, 0, 0)
    OP_6E(190, 0)
    SetCameraDistance(42740, 0)
    SetChrPos(0x101, -1240, 0, 500, 0)
    SetChrPos(0x102, 160, 0, 200, 0)
    SetChrPos(0x109, -1180, 0, -900, 0)
    SetChrPos(0x105, 120, 120, -1080, 0)
    SetChrPos(0x104, -1140, 120, -2300, 0)
    SetChrPos(0x1A3, 90, 0, -2500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0183
    ChrTalk(
        0xA,
        "へえ、猫ねえ……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        (
            "クク……\x01",
            "そういうことかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        "#12P#00105F心当たり、あるみたいね？\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x104,
        (
            "#12P#00300Fお互い時間を取るのも何だし、\x01",
            "とっとと話しちゃくれねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        "んー、どうすっかなぁ。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        "ユーリ、どうするよ？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FB9")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆暴走車の取り締まり１を？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",            # 0
            "【クリアしている】\x01",        # 1
            "【クリアしていない】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FA5")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_3FB9")

    label("loc_3FA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FB9")
    OP_29(0x69, 0x3, 0x10)

    label("loc_3FB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_406C")

    #C0190
    ChrTalk(
        0x8,
        "フフン、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x8,
        (
            "例のふざけた取り締まりで\x01",
            "世話になったことだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        (
            "それなりの“誠意”を\x01",
            "見せて欲しいところだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        "土下座とか、裸踊りとか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_410A")

    label("loc_406C")


    #C0194
    ChrTalk(
        0x8,
        "フフン、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "ずいぶん舐めた態度で\x01",
            "聞き込みをしてきたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x8,
        (
            "それなりの“誠意”を\x01",
            "見せて欲しいところだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        "土下座とか、裸踊りとか。\x02",
    )

    CloseMessageWindow()

    label("loc_410A")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0198
    ChrTalk(
        0xA,
        "#11Pははっ、そりゃいいや！\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x9,
        (
            "そういうわけでー、\x01",
            "土下座か裸踊りに決定。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        "あ、野郎の裸とかいらねぇから。\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x109,
        "#12P#10101F（こ、この人たち……）\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x102,
        "#12P#00106F（思った以上に最低ね……）\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x105,
        (
            "#12P#10306F（やれやれ、何か勘違い\x01",
            "  しちゃってるみたいだね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x104,
        (
            "#12P#00301F（チッ……\x01",
            "  脅すワケにもいかねぇし。）\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        "#12P#00000F（ああ、ここは俺に任せて──）\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #C0206
    ChrTalk(
        0x1A3,
        (
            "#12P#04605F#3975Vねえねえ、お兄さんたち。\x02\x03",

            "#3976Vなんでこんなのに\x01",
            "手間取っちゃってるわけ？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF88)
    OP_C9(0x1, 0x80000000)

    def lambda_43B7():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43B7)
    Sleep(50)

    def lambda_43C7():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43C7)
    Sleep(50)

    def lambda_43D7():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43D7)
    Sleep(50)

    def lambda_43E7():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43E7)
    Sleep(50)

    def lambda_43F7():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43F7)
    Sleep(500)

    #C0207
    ChrTalk(
        0x101,
        "#00005Fへ……\x02",
    )

    CloseMessageWindow()
    OP_68(-1220, 1400, 1530, 1000)
    SetChrChip(0x0, 0x1A3, 0x1E, 0x12C)
    Sound(809, 0, 100, 0)
    OP_95(0x1A3, -440, 0, -330, 8000, 0x0)
    OP_95(0x1A3, -660, 0, 2440, 8000, 0x0)
    SetChrChip(0x1, 0x1A3, 0x0, 0x0)
    OP_0D()
    SetChrChipByIndex(0x1A3, 0x1E)
    SetChrSubChip(0x1A3, 0x0)
    SetChrFlags(0x1A3, 0x2)
    OP_0D()
    SetChrPos(0x8, -700, 0, 3000, 180)
    Sleep(300)
    Sound(802, 0, 100, 0)
    Sound(811, 0, 30, 0)
    SetChrSubChip(0x1A3, 0x1)
    SetChrPos(0x8, -700, 200, 3000, 180)
    BeginChrThread(0x8, 3, 0, 22)
    OP_6F(0x1)

    def lambda_44B5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44B5)
    Sleep(50)

    def lambda_44C5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44C5)
    Sleep(50)

    def lambda_44D5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_44D5)
    Sleep(50)

    def lambda_44E5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_44E5)
    Sleep(50)

    def lambda_44F5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_44F5)
    Sleep(50)

    def lambda_4505():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4505)
    Sleep(50)

    def lambda_4515():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4515)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0208
    ChrTalk(
        0x8,
        "#5Pうぐっ……！？\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x1A3,
        (
            "#12P#04609Fはいはい。\x01",
            "さっさと吐こうかー。\x02\x03",

            "#04611Fそれとも抵抗して\x01",
            "胃の中ぜんぶブチまける？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x8,
        "#5Pうぐっ、なっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_46B0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_46B0)
    Sleep(50)

    def lambda_46CD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_46CD)
    WaitChrThread(0x9, 1)

    def lambda_46EB():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_46EB)
    WaitChrThread(0xA, 1)

    def lambda_46FC():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_46FC)
    Sleep(300)

    #C0211
    ChrTalk(
        0xA,
        (
            "#11Pお、おい！\x01",
            "いきなり何を……！\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x9,
        (
            "#5Pこのガキ！\x01",
            "ユーリに何をしやが──\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    #C0213
    ChrTalk(
        0x1A3,
        (
            "#12P#04611F#3977V──ウザイな。\x01",
            "こいつ殺しちゃうよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF89)
    OP_C9(0x1, 0x80000000)
    OP_64(0x9)
    OP_64(0xA)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0214
    ChrTalk(
        0x9,
        "#5Pな……！？\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        "#12P#00011Fちょ、ちょっと待った！\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x102,
        "#12P#00101Fさ、さすがにそれは……\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x104,
        (
            "#12P#00303Fふう……やれやれ。\x02\x03",

            "#00301F──お前ら。\x01",
            "とっとと言うとおりにしろ。\x02\x03",

            "そいつはヤバイ。\x01",
            "ためらいなく本気でやるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        "#5Pっ……\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xA,
        "#11Pわ、分かった……言うから！\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xA,
        (
            "#11Pね、猫なら来たよ！\x01",
            "あんたらが来るちょっと前だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xA,
        (
            "#11Pか、軽く脅してやったら\x01",
            "すぐに飛び出して行ったんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xA,
        "#11Pだから、まだ近くにいるんじゃねえか？\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xA,
        (
            "#11P――こ、これでいいだろ！？\x01",
            "ユ、ユーリを放してやってくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x1A3,
        (
            "#12P#04604Fへー、可愛い仔猫を脅したんだ。\x02\x03",

            "#04609Fそれってこんな感じ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A3, 0x2)
    SetChrPos(0x9, -1500, 0, 2400, 90)
    Sleep(300)
    Sound(802, 0, 100, 0)
    Sound(811, 0, 30, 0)
    SetChrSubChip(0x1A3, 0x3)
    SetChrPos(0x9, -1500, 200, 2400, 90)
    BeginChrThread(0x9, 3, 0, 22)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0225
    ChrTalk(
        0x9,
        "#5Pうぐぅ……！\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        "#5Pあぁう……！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A3, 0x4)

    #C0227
    ChrTalk(
        0x1A3,
        "#6P#04611Fお兄さんもこうなりたい？\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xA, 0xB4, 0x1F4, 0x7D0, 0x0)

    #C0228
    ChrTalk(
        0xA,
        "#11Pぶるぶるぶる……！\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x1A3,
        (
            "#6P#04609Fあはは、よく分かってんじゃん。\x02\x03",

            "#04604Fさてと──\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0x1A3, 0xFF)
    SetChrSubChip(0x1A3, 0x0)
    ClearChrFlags(0x1A3, 0x2)
    SetChrPos(0x8, -700, 0, 3250, 180)
    SetChrPos(0x9, -1700, 0, 2400, 90)
    Sleep(100)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    OP_93(0x9, 0xB4, 0x0)

    def lambda_4C2E():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4C2E)
    Sleep(50)

    def lambda_4C46():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4C46)

    #C0230
    ChrTalk(
        0x8,
        "ぷはッ……ハア、ハア！\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x9,
        "……ゼエ、ゼエ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)

    #C0232
    ChrTalk(
        0x1A3,
        (
            "#5P#04600Fどうやらマリーは\x01",
            "近くにいるみたいだよ？\x02\x03",

            "#04609F急いで捜しに行こう㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#12P#00005Fあ、ああ……\x02\x03",

            "#12P#00003Fえっと……\x01",
            "ご協力、感謝するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、ちなみに彼女は\x01",
            "警察とは何の関係もないから。\x02\x03",

            "#10309F猫に噛まれたとでも思うんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x9,
        (
            "#5Pう、うるせぇ……！\x01",
            "とっとと行っちまえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "#5Pお前たち……\x01",
            "……タダで済むと思うなよ……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("c0300", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_15_3A0D end

    def Function_16_4E17(): pass

    label("Function_16_4E17")


    def lambda_4E1C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E1C)

    def lambda_4E2D():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E2D)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 920, 0, -1940, 2000, 0x0)
    Return()

    # Function_16_4E17 end

    def Function_17_4E5B(): pass

    label("Function_17_4E5B")


    def lambda_4E60():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E60)

    def lambda_4E71():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E71)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -100, 0, -3320, 2000, 0x0)
    OP_95(0x102, -100, 0, -1870, 2000, 0x0)
    Return()

    # Function_17_4E5B end

    def Function_18_4EB3(): pass

    label("Function_18_4EB3")


    def lambda_4EB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4EB8)

    def lambda_4EC9():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4EC9)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 2210, 0, -3320, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_18_4EB3 end

    def Function_19_4EFE(): pass

    label("Function_19_4EFE")


    def lambda_4F03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4F03)

    def lambda_4F14():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4F14)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 2210, 0, -3320, 2000, 0x0)
    OP_95(0x109, 2210, 0, -1870, 2000, 0x0)
    Return()

    # Function_19_4EFE end

    def Function_20_4F56(): pass

    label("Function_20_4F56")


    def lambda_4F5B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4F5B)

    def lambda_4F6C():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F6C)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -100, 0, -3320, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_20_4F56 end

    def Function_21_4FA1(): pass

    label("Function_21_4FA1")


    def lambda_4FA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_4FA6)

    def lambda_4FB7():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_4FB7)
    WaitChrThread(0x1A3, 1)
    Return()

    # Function_21_4FA1 end

    def Function_22_4FD1(): pass

    label("Function_22_4FD1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5001")

    def lambda_4FE1():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4FE1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_22_4FD1")

    label("loc_5001")

    Return()

    # Function_22_4FD1 end

    SaveToFile()

Try(main)
