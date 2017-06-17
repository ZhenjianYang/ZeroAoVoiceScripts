from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1520.bin",                # FileName
        "t1520",                    # MapName
        "t1520",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 6, 0, 7],
    )

    BuildStringList((
        "t1520",                  # 0
        "アーシュラ主任",         # 1
        "マローネ",               # 2
        "研修医シャルール",       # 3
        "研修医リットン",         # 4
        "研修医グェン",           # 5
        "看護師メイファ",         # 6
        "診察医ベルダイン",       # 7
        "アーシュラ主任",         # 8
        "セシル",                 # 9
    ))

    AddCharChip((
        "apl/ch50146.itc",                   # 00
        "chr/ch25600.itc",                   # 01
        "chr/ch32800.itc",                   # 02
        "chr/ch29400.itc",                   # 03
        "chr/ch29500.itc",                   # 04
        "chr/ch29800.itc",                   # 05
        "chr/ch29300.itc",                   # 06
        "chr/ch05300.itc",                   # 07
        "chr/ch32900.itc",                   # 08
    ))

    DeclNpc(92529,   400,     49430,   315,  469,  0x0, 0,   0,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-5199,   0,       17700,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-47439,  0,       55720,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3630,    0,       54689,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(202830,  0,       340,     0,    389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(204669,  0,       53000,   90,   389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-98839,  0,       53500,   180,  389,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(94459,   0,       52029,   90,   389,  0x0, 0,   8,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)

    DeclActor(155770,  0,       53330,   1500,    155770,  1500,    53330,   0x007C, 0,  19, 0x0000)

    ScpFunction((
        "Function_0_228",          # 00, 0
        "Function_1_2E0",          # 01, 1
        "Function_2_341",          # 02, 2
        "Function_3_3A2",          # 03, 3
        "Function_4_3CD",          # 04, 4
        "Function_5_3F8",          # 05, 5
        "Function_6_40B",          # 06, 6
        "Function_7_6AC",          # 07, 7
        "Function_8_7F5",          # 08, 8
        "Function_9_DDD",          # 09, 9
        "Function_10_1925",        # 0A, 10
        "Function_11_1B36",        # 0B, 11
        "Function_12_1DE0",        # 0C, 12
        "Function_13_227A",        # 0D, 13
        "Function_14_2372",        # 0E, 14
        "Function_15_2572",        # 0F, 15
        "Function_16_2673",        # 10, 16
        "Function_17_3126",        # 11, 17
        "Function_18_33DF",        # 12, 18
        "Function_19_37E8",        # 13, 19
    ))


    def Function_0_228(): pass

    label("Function_0_228")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_268"),
        (1, "loc_274"),
        (2, "loc_280"),
        (3, "loc_28C"),
        (4, "loc_298"),
        (5, "loc_2A4"),
        (6, "loc_2B0"),
        (SWITCH_DEFAULT, "loc_2BC"),
    )


    label("loc_268")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_274")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_280")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_28C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_298")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2A4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2DF")

    Return()

    # Function_0_228 end

    def Function_1_2E0(): pass

    label("Function_1_2E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_340")
    OP_95(0xFE, -310, 0, 17700, 2000, 0x0)
    OP_95(0xFE, -310, 0, 3650, 2000, 0x0)
    OP_95(0xFE, -310, 0, 17700, 2000, 0x0)
    OP_95(0xFE, -14660, 0, 17700, 2000, 0x0)
    Jump("Function_1_2E0")

    label("loc_340")

    Return()

    # Function_1_2E0 end

    def Function_2_341(): pass

    label("Function_2_341")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A1")
    OP_95(0xFE, 79630, 0, 11390, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 11390, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 2680, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 11390, 2000, 0x0)
    Jump("Function_2_341")

    label("loc_3A1")

    Return()

    # Function_2_341 end

    def Function_3_3A2(): pass

    label("Function_3_3A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CC")
    OP_94(0xFE, 0x3124A, 0x1CC, 0x31BC8, 0xE1A, 0x3E8)
    Sleep(400)
    Jump("Function_3_3A2")

    label("loc_3CC")

    Return()

    # Function_3_3A2 end

    def Function_4_3CD(): pass

    label("Function_4_3CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F7")
    OP_94(0xFE, 0xFFFE741A, 0xCD5A, 0xFFFE86D0, 0xD548, 0x3E8)
    Sleep(400)
    Jump("Function_4_3CD")

    label("loc_3F7")

    Return()

    # Function_4_3CD end

    def Function_5_3F8(): pass

    label("Function_5_3F8")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Return()

    # Function_5_3F8 end

    def Function_6_40B(): pass

    label("Function_6_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_44B")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 203030, 0, 4610, 0)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 154520, 0, 53680, 90)
    Jump("loc_6AB")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_475")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_49F")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 203030, 0, 4610, 0)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4CF")
    ClearChrFlags(0xE, 0x80)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_4E8")
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_6AB")

    label("loc_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_507")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 5)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_54D")
    ClearChrFlags(0xE, 0x80)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 154520, 0, 53680, 90)
    Jump("loc_6AB")

    label("loc_54D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_566")
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5A0")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5BF")
    ClearChrFlags(0xC, 0x80)
    BeginChrThread(0xC, 0, 0, 3)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_5BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5E3")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    BeginChrThread(0xC, 0, 0, 3)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_61E")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 154520, 0, 53680, 90)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_648")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_672")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_691")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 5)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6AB")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0x8, 0, 0, 5)

    label("loc_6AB")

    Return()

    # Function_6_40B end

    def Function_7_6AC(): pass

    label("Function_7_6AC")

    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6D8")
    OP_65(0x0, 0x1)
    Jump("loc_79A")

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6E6")
    Jump("loc_79A")

    label("loc_6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_701")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    Jump("loc_79A")

    label("loc_701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_71C")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    Jump("loc_79A")

    label("loc_71C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_72E")
    OP_65(0x0, 0x1)
    Jump("loc_79A")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_740")
    OP_65(0x0, 0x1)
    Jump("loc_79A")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_74E")
    Jump("loc_79A")

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_769")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    Jump("loc_79A")

    label("loc_769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_784")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    Jump("loc_79A")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_79A")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)

    label("loc_79A")

    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C1")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7F4")

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DD")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7F4")

    label("loc_7DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F4")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_7F4")

    Return()

    # Function_7_6AC end

    def Function_8_7F5(): pass

    label("Function_8_7F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_806")
    Jump("loc_DD9")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_814")
    Jump("loc_DD9")

    label("loc_814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_822")
    Jump("loc_DD9")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_830")
    Jump("loc_DD9")

    label("loc_830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_92F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D3")

    #C0001
    ChrTalk(
        0xFE,
        (
            "むにゃむにゃ……\x01",
            "おはようございま……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0002
    ChrTalk(
        0xFE,
        (
            "ああっいけない！\x01",
            "今日は診察室に行かなきゃ\x01",
            "いけなかったのに！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_92A")

    label("loc_8D3")


    #C0003
    ChrTalk(
        0xFE,
        (
            "シャルール君、とっくに\x01",
            "診察室に行ってるんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "あわわ……どーしましょ！？\x02",
    )

    CloseMessageWindow()

    label("loc_92A")

    Jump("loc_DD9")

    label("loc_92F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_9EE")
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_997")

    #C0005
    ChrTalk(
        0xFE,
        "……すー……すぴー…………\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "……あ、あと５分……むにゃむにゃ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9D7")

    label("loc_997")


    #C0007
    ChrTalk(
        0xFE,
        (
            "あと５分……\x01",
            "いや、１５分したら起きる……\x01",
            "むにゃむにゃ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D7")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_DD9")

    label("loc_9EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9FC")
    Jump("loc_DD9")

    label("loc_9FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A9F")
    OP_64(0xFE)

    #C0008
    ChrTalk(
        0xFE,
        "……すー……すぴー……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "わぁ……これが最新式の\x01",
            "導力レーザーメス…………\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "ううん……\x01",
            "こんなの開発されてたっけ……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_DD9")

    label("loc_A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_AAD")
    Jump("loc_DD9")

    label("loc_AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_ABB")
    Jump("loc_DD9")

    label("loc_ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_AC9")
    Jump("loc_DD9")

    label("loc_AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_AD7")
    Jump("loc_DD9")

    label("loc_AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_AE5")
    Jump("loc_DD9")

    label("loc_AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_C15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B95")

    #C0011
    ChrTalk(
        0xFE,
        "……むにゃむにゃ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0012
    ChrTalk(
        0xFE,
        "……あれっ、もうこんな時間！？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "い・け・な～い！\x01",
            "夕方から診察室に\x01",
            "入る予定なのに～！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C10")

    label("loc_B95")


    #C0014
    ChrTalk(
        0xFE,
        (
            "徹夜明けで疲れてたから\x01",
            "ぐっすり眠っちゃってましたぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "急いで行かないと、\x01",
            "またゲイリー教授に\x01",
            "叱られちゃいます！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C10")

    Jump("loc_DD9")

    label("loc_C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_END)), "loc_C67")

    #C0016
    ChrTalk(
        0xFE,
        "すー……すぴー……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#0000F……起こさない方がよさそうだな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_DD9")

    label("loc_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_DA3")
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6C")

    #C0018
    ChrTalk(
        0xFE,
        "すー……すぴー……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "……ふがっ！？\x01",
            "……爆発するぅ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "…………すー…………すぴー……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#0006F……な、何の夢を見てるんだろう……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x136,
        (
            "#1302Fアーシュラ主任は\x01",
            "いつも忙しい方だから……\x01",
            "今は寝かせておいてあげましょ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D8C")

    label("loc_D6C")


    #C0023
    ChrTalk(
        0xFE,
        "……すー…………すぴー……\x02",
    )

    CloseMessageWindow()

    label("loc_D8C")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_DD9")

    label("loc_DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_DD9")
    OP_64(0xFE)

    #C0024
    ChrTalk(
        0xFE,
        "すー……すぴー……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)

    label("loc_DD9")

    TalkEnd(0xFE)
    Return()

    # Function_8_7F5 end

    def Function_9_DDD(): pass

    label("Function_9_DDD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_EEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E87")

    #C0025
    ChrTalk(
        0xFE,
        (
            "あ、昨日セシルさんの部屋に\x01",
            "運び込まれた……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        "#0203F……心配をおかけしました。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "ふぅ、本当ですよ。\x01",
            "でもお元気そうで何よりです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EE6")

    label("loc_E87")


    #C0028
    ChrTalk(
        0xFE,
        (
            "また具合が悪くなったら\x01",
            "すぐに相談してくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "なんたってここは病院なんですから。\x02",
    )

    CloseMessageWindow()

    label("loc_EE6")

    Jump("loc_1921")

    label("loc_EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_F4E")

    #C0030
    ChrTalk(
        0xFE,
        "あれ、もうこんな時間！？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "あわわ、早く今日の掃除を\x01",
            "済ませてしまわないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1921")

    label("loc_F4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_FE0")

    #C0032
    ChrTalk(
        0xFE,
        (
            "ヨアヒム准教授もこちらの寮に\x01",
            "住まわれているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "朝はいつもだらしなさそうに出かけるので\x01",
            "私が喝をいれてあげるんです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1921")

    label("loc_FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1074")

    #C0034
    ChrTalk(
        0xFE,
        (
            "今日はめずらしく、アーシュラ主任が\x01",
            "定時通りに研究棟に向かいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "うーん、いつもは朝帰りなのに……\x01",
            "昨日は寝れたのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1921")

    label("loc_1074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_10DD")

    #C0036
    ChrTalk(
        0xFE,
        (
            "小さい女の子？\x01",
            "ここは通らなかったと思いますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "病棟のほうも探してみました？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1921")

    label("loc_10DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1256")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CA")

    #C0038
    ChrTalk(
        0xFE,
        (
            "看護師のシロンさんは\x01",
            "この時間、よく屋上でシーツを\x01",
            "干してるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "この間、何気なくそこのベランダで\x01",
            "空を見上げてみたんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "……見えちゃいました。\x01",
            "もう少し気を付けてもらわないと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1251")

    label("loc_11CA")


    #C0041
    ChrTalk(
        0xFE,
        (
            "シロンさんは無防備というか、\x01",
            "なんというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "とにかく、ベランダに積極的に\x01",
            "行こうとする男の人には\x01",
            "注意しなきゃいけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1251")

    Jump("loc_1921")

    label("loc_1256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EE")

    #C0043
    ChrTalk(
        0x9,
        (
            "今日はアーシュラ主任、\x01",
            "教授会とやらに行ってるそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "随分朝早かったから、\x01",
            "いまごろ寝ぼけまなこかも\x01",
            "しれないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_134E")

    label("loc_12EE")


    #C0045
    ChrTalk(
        0x9,
        (
            "アーシュラ主任って\x01",
            "寝ぼすけさんなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "教授会でもうつらうつら\x01",
            "してるんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_134E")

    Jump("loc_1921")

    label("loc_1353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_146B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EE")

    #C0047
    ChrTalk(
        0xFE,
        (
            "しずか～……\x01",
            "先生も研修医さんも看護師さんも\x01",
            "みんな出払ってるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "……はっ！\x01",
            "これは隅々まで\x01",
            "お掃除するチャンス！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1466")

    label("loc_13EE")


    #C0049
    ChrTalk(
        0xFE,
        (
            "ふふふ、そうと決まれば……\x01",
            "みんなが帰ってくるまでに\x01",
            "ピカピカにしてあげなきゃね！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "ごしごしごしごしごしごしっ！\x02",
    )

    CloseMessageWindow()

    label("loc_1466")

    Jump("loc_1921")

    label("loc_146B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_14EF")

    #C0051
    ChrTalk(
        0xFE,
        "こっちは女子寮だから男子禁制よ！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "……とはいえないのよね。\x01",
            "職員寮からはここ通らないと\x01",
            "研究棟に行けないし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1921")

    label("loc_14EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1570")

    #C0053
    ChrTalk(
        0xFE,
        (
            "ごしごし……\x01",
            "職員寮はほんと、綺麗なもんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "先生も看護師も\x01",
            "遅くまで仕事してるから\x01",
            "殆ど使われてないのよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1921")

    label("loc_1570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_169A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1643")

    #C0055
    ChrTalk(
        0xFE,
        (
            "リットンさんがさっき、\x01",
            "休憩しに部屋に戻ってきたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "先月の事件で休んでから\x01",
            "ヨアヒム先生にかなりの仕事を\x01",
            "押し付けられてたみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "まぁ、休める時に\x01",
            "休んでおくべきよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1695")

    label("loc_1643")


    #C0058
    ChrTalk(
        0xFE,
        (
            "うーん、\x01",
            "私もそろそろ昼食をとろうかしら。\x01",
            "掃除しっぱなしでお腹ペコペコだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1695")

    Jump("loc_1921")

    label("loc_169A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_171A")

    #C0059
    ChrTalk(
        0xFE,
        (
            "さっき、アーシュラ主任が\x01",
            "あわてて出かけていきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "今日も相変わらず、\x01",
            "お寝坊しちゃったみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1921")

    label("loc_171A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_17B3")

    #C0061
    ChrTalk(
        0xFE,
        (
            "１回一通り掃除したのに、\x01",
            "結局細かい汚れが気になって\x01",
            "もう１回しちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "……女子寮ですもの、\x01",
            "綺麗過ぎるくらいが丁度良いわよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1921")

    label("loc_17B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1829")

    #C0063
    ChrTalk(
        0xFE,
        (
            "よし、掃除はこんなところね。\x01",
            "……の、はずよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "なんだか細かな汚れが\x01",
            "気になってきちゃった……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1921")

    label("loc_1829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_18D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A0")

    #C0065
    ChrTalk(
        0xFE,
        (
            "今、男子寮生は\x01",
            "みんな出払ってるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "大体研究棟か病棟で\x01",
            "仕事とかしてると思うわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18D1")

    label("loc_18A0")


    #C0067
    ChrTalk(
        0xFE,
        (
            "さ、がんばってる皆のために\x01",
            "お掃除お掃除～☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D1")

    Jump("loc_1921")

    label("loc_18D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1921")

    #C0068
    ChrTalk(
        0xFE,
        "ごしごし……ごしごし……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "お・そ・う・じ・た～のしいな☆\x02",
    )

    CloseMessageWindow()

    label("loc_1921")

    TalkEnd(0xFE)
    Return()

    # Function_9_DDD end

    def Function_10_1925(): pass

    label("Function_10_1925")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1936")
    Jump("loc_1B32")

    label("loc_1936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1944")
    Jump("loc_1B32")

    label("loc_1944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1952")
    Jump("loc_1B32")

    label("loc_1952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1960")
    Jump("loc_1B32")

    label("loc_1960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_196E")
    Jump("loc_1B32")

    label("loc_196E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_197C")
    Jump("loc_1B32")

    label("loc_197C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_198A")
    Jump("loc_1B32")

    label("loc_198A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1998")
    Jump("loc_1B32")

    label("loc_1998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A3B")

    #C0070
    ChrTalk(
        0xFE,
        (
            "アーシュラ主任が仕事にでていて\x01",
            "僕が寮にいるというのも……\x01",
            "なかなか珍しい状況だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "……せっかく休みがとれたんだ。\x01",
            "休める時に休まないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B32")

    label("loc_1A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A49")
    Jump("loc_1B32")

    label("loc_1A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1A57")
    Jump("loc_1B32")

    label("loc_1A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1A65")
    Jump("loc_1B32")

    label("loc_1A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1B0D")

    #C0072
    ChrTalk(
        0xFE,
        (
            "アーシュラ主任、\x01",
            "今日も遅刻かと思ったけど\x01",
            "なんとか間に合ったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "夜中まで研究に没頭しすぎて\x01",
            "時間に間に合わないのは\x01",
            "いつものことだからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B32")

    label("loc_1B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1B1B")
    Jump("loc_1B32")

    label("loc_1B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1B29")
    Jump("loc_1B32")

    label("loc_1B29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1B32")

    label("loc_1B32")

    TalkEnd(0xFE)
    Return()

    # Function_10_1925 end

    def Function_11_1B36(): pass

    label("Function_11_1B36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B47")
    Jump("loc_1DDC")

    label("loc_1B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1BC5")

    #C0074
    ChrTalk(
        0xFE,
        (
            "今日は部屋に戻ったら\x01",
            "ゆっくりするつもりだったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "試験も近いし、少しでも\x01",
            "勉強しておかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDC")

    label("loc_1BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1BD3")
    Jump("loc_1DDC")

    label("loc_1BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1BE1")
    Jump("loc_1DDC")

    label("loc_1BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1BEF")
    Jump("loc_1DDC")

    label("loc_1BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1BFD")
    Jump("loc_1DDC")

    label("loc_1BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1C0B")
    Jump("loc_1DDC")

    label("loc_1C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1CA1")

    #C0076
    ChrTalk(
        0xFE,
        (
            "くあー……\x01",
            "ようやく休みが取れたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "相変わらず予定はないけどね。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "僕もヨアヒム先生よろしく、\x01",
            "釣りでもはじめてみようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDC")

    label("loc_1CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1CAF")
    Jump("loc_1DDC")

    label("loc_1CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CBD")
    Jump("loc_1DDC")

    label("loc_1CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1D9B")

    #C0079
    ChrTalk(
        0xFE,
        (
            "ヨアヒム先生の考えてることは\x01",
            "いまいち掴みづらいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "最初は、僕の勉強のために\x01",
            "ガンガン仕事回してくれてるのかと\x01",
            "思ってたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "あれは、結局自分が楽をしたかった\x01",
            "だけだったのかもしれない……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDC")

    label("loc_1D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1DA9")
    Jump("loc_1DDC")

    label("loc_1DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1DB7")
    Jump("loc_1DDC")

    label("loc_1DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1DC5")
    Jump("loc_1DDC")

    label("loc_1DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1DD3")
    Jump("loc_1DDC")

    label("loc_1DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1DDC")

    label("loc_1DDC")

    TalkEnd(0xFE)
    Return()

    # Function_11_1B36 end

    def Function_12_1DE0(): pass

    label("Function_12_1DE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1FAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE7")

    #C0082
    ChrTalk(
        0xFE,
        (
            "……ゲイリー・ロイツェル著……\x01",
            "こっちは……ラゴー・ニクソン著……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "沢山持ってる医学書の中にも、\x01",
            "いくつかうちの教授たちの\x01",
            "著書があるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "普段あまり意識しないけど、\x01",
            "最先端の医療研究施設に恥じない\x01",
            "人たちばかりなのね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1FA5")

    label("loc_1EE7")


    #C0085
    ChrTalk(
        0xFE,
        (
            "そうだ、ヨアヒム先生の\x01",
            "著書はあるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "ヨアヒム・ギュンター著……\x01",
            "……見当たらないなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "まぁ、本を出すとかには\x01",
            "あんまり興味なさそうな人だし、\x01",
            "私が持ってなくても無理ないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA5")

    Jump("loc_2276")

    label("loc_1FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1FB8")
    Jump("loc_2276")

    label("loc_1FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2042")

    #C0088
    ChrTalk(
        0xFE,
        (
            "夕方まで時間があるし……\x01",
            "ちょっとくらい勉強しないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "実家からためになる医学書、\x01",
            "いっぱい持ってきてるんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2276")

    label("loc_2042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2050")
    Jump("loc_2276")

    label("loc_2050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_205E")
    Jump("loc_2276")

    label("loc_205E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_206C")
    Jump("loc_2276")

    label("loc_206C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_207A")
    Jump("loc_2276")

    label("loc_207A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2088")
    Jump("loc_2276")

    label("loc_2088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2096")
    Jump("loc_2276")

    label("loc_2096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2102")

    #C0090
    ChrTalk(
        0xFE,
        (
            "夕方からは診察室に入って\x01",
            "実地研修の予定なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "教授に優秀なところを\x01",
            "みせなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2276")

    label("loc_2102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2235")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EA")

    #C0092
    ChrTalk(
        0xFE,
        (
            "今日はお休みなんだけど……\x01",
            "きちっと勉強しなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "同室のフローラも、\x01",
            "ご飯を食べる時間まで\x01",
            "勉強にあててるんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "私も来月あたり、\x01",
            "実地研修の予定だし……\x01",
            "今のうちに予習しておかなくちゃ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2230")

    label("loc_21EA")


    #C0095
    ChrTalk(
        0xFE,
        (
            "次の実地研修で\x01",
            "良い評価を貰うためにも、\x01",
            "バリバリ勉強するわよ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2230")

    Jump("loc_2276")

    label("loc_2235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2243")
    Jump("loc_2276")

    label("loc_2243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2251")
    Jump("loc_2276")

    label("loc_2251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_225F")
    Jump("loc_2276")

    label("loc_225F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_226D")
    Jump("loc_2276")

    label("loc_226D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2276")

    label("loc_2276")

    TalkEnd(0xFE)
    Return()

    # Function_12_1DE0 end

    def Function_13_227A(): pass

    label("Function_13_227A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2316")

    #C0096
    ChrTalk(
        0xFE,
        (
            "昨日は休暇だったんだけど……\x01",
            "シロンと一緒だったせいで\x01",
            "疲れっぱなしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "いちいち何をしでかすか心配でね。\x01",
            "あー、心臓に悪い……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_236E")

    label("loc_2316")


    #C0098
    ChrTalk(
        0xFE,
        (
            "……ま、ドタバタしてたけど\x01",
            "それなりにストレス発散できたし\x01",
            "いい休日だった……かな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_236E")

    TalkEnd(0xFE)
    Return()

    # Function_13_227A end

    def Function_14_2372(): pass

    label("Function_14_2372")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2383")
    Jump("loc_256E")

    label("loc_2383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2391")
    Jump("loc_256E")

    label("loc_2391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_239F")
    Jump("loc_256E")

    label("loc_239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_240A")

    #C0099
    ChrTalk(
        0xFE,
        (
            "……今日は夜勤の予定でな。\x01",
            "早めに仮眠を取る予定だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        "……分かったら出ていきたまえ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_256E")

    label("loc_240A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2418")
    Jump("loc_256E")

    label("loc_2418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2426")
    Jump("loc_256E")

    label("loc_2426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_249D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2441")
    Call(0, 15)
    Jump("loc_2498")

    label("loc_2441")


    #C0101
    ChrTalk(
        0xFE,
        (
            "ふぅ……\x01",
            "思いがけず休みが続いてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        "仕事をしていた方が楽なんだがな……\x02",
    )

    CloseMessageWindow()

    label("loc_2498")

    Jump("loc_256E")

    label("loc_249D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_24AB")
    Jump("loc_256E")

    label("loc_24AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2511")

    #C0103
    ChrTalk(
        0xFE,
        (
            "人の部屋に勝手に入るとは\x01",
            "随分不躾だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "急患でもないなら\x01",
            "出て行ってもらおう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_256E")

    label("loc_2511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_251F")
    Jump("loc_256E")

    label("loc_251F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_252D")
    Jump("loc_256E")

    label("loc_252D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_253B")
    Jump("loc_256E")

    label("loc_253B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2549")
    Jump("loc_256E")

    label("loc_2549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2557")
    Jump("loc_256E")

    label("loc_2557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2565")
    Jump("loc_256E")

    label("loc_2565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_256E")

    label("loc_256E")

    TalkEnd(0xFE)
    Return()

    # Function_14_2372 end

    def Function_15_2572(): pass

    label("Function_15_2572")


    #C0105
    ChrTalk(
        0xFE,
        (
            "医者を扱っている小説を\x01",
            "取り寄せて読んでみた。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "もう少し実用的な技術などが\x01",
            "書いていればよかったが……\x01",
            "まぁ、良くも悪くも娯楽小説だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "……これは君たちにやろう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0108
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2CE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2CE, 1)
    SetScenarioFlags(0x9D, 0)
    Return()

    # Function_15_2572 end

    def Function_16_2673(): pass

    label("Function_16_2673")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2888")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2691")
    Call(0, 18)
    Jump("loc_2883")

    label("loc_2691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27BC")

    #C0109
    ChrTalk(
        0x10,
        (
            "#1304F……さてと、今日はミハイル君に\x01",
            "つきっきりになっちゃおうかな。\x02\x03",

            "#1300F今日はシズクちゃんの外出日だし、\x01",
            "やっぱり寂しがってるはずだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0000Fはは……セシル姉って、\x01",
            "誰にとっても『お姉ちゃん』だな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27B4")

    #C0111
    ChrTalk(
        0x10A,
        "#0608F（……この女性は、確か奴の……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEC, 6)

    label("loc_27B4")

    SetScenarioFlags(0x0, 4)
    Jump("loc_2883")

    label("loc_27BC")


    #C0112
    ChrTalk(
        0x10,
        (
            "#1304Fさて、ミハイル君には……\x01",
            "絵本でも読んであげようかしら。\x02\x03",

            "#1302Fこういう時のために、\x01",
            "子供の頃ロイドに読んであげてた\x01",
            "絵本を持ってきてるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        "#0006F（微妙に恥ずかしいな、それ……）\x02",
    )

    CloseMessageWindow()

    label("loc_2883")

    Jump("loc_3122")

    label("loc_2888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2896")
    Jump("loc_3122")

    label("loc_2896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B1")
    Call(0, 17)
    Jump("loc_2A33")

    label("loc_28B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29AF")

    #C0114
    ChrTalk(
        0x10,
        (
            "#1300Fそうそう、これからシズクちゃんと\x01",
            "敷地内を散歩に行くのよ。\x02\x03",

            "#1304Fシズクちゃんは耳がいいから、\x01",
            "私が気づかないような\x01",
            "動物の動きなんかも教えてくれるの。\x02\x03",

            "#1300Fふふ、看護師の仕事の一つなのに\x01",
            "こればっかりは楽しみにしちゃうわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2A33")

    label("loc_29AF")


    #C0115
    ChrTalk(
        0x10,
        (
            "#1300Fシズクちゃんとの散歩は\x01",
            "色々な発見があって面白いわ。\x02\x03",

            "ふふ、看護師の仕事の一つなのに\x01",
            "こればっかりは楽しみにしちゃうわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A33")

    Jump("loc_3122")

    label("loc_2A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_END)), "loc_2E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A53")
    Call(0, 17)
    Jump("loc_2E81")

    label("loc_2A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 0)), scpexpr(EXPR_END)), "loc_2AFC")

    #C0116
    ChrTalk(
        0x10,
        "#1309Fふふ、また来てくれたのね。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0005Fあ、そういえば、セシル姉……\x02\x03",

            "#0000F昨日通信で話してた友達って\x01",
            "アルカンシェルのイリアさんの事？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C89")

    label("loc_2AFC")


    #C0118
    ChrTalk(
        0x10,
        (
            "#1306F私も寮暮らしだから\x01",
            "お互いなかなか\x01",
            "会う機会が作れないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#0004Fはは、そうだね。\x02\x03",

            "#0001Fでもセシル姉……\x01",
            "仕事、忙しそうだけど\x01",
            "あまり無理しないでくれよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x10,
        (
            "#1309Fふふ、無理はしてないわ。\x02\x03",

            "たまに通信で友達とお喋りして\x01",
            "気晴らしとかもしているしね。\x02\x03",

            "#1302F昨日の夜も、久しぶりに\x01",
            "その友達と長話をしちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#0005Fそ、それってもしかして……\x01",
            "アルカンシェルのイリアさんの事？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C89")


    #C0122
    ChrTalk(
        0x10,
        (
            "#1305Fあら、知ってたの？\x02\x03",

            "#1300F変ねぇ、いつ教えたかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#0011F……えっ！？\x02\x03",

            "（マズい、いくらセシル姉でも\x01",
            "  捜査のことを漏らすわけには……）\x02\x03",

            "#0012Fえ、えーっと……\x01",
            "……大分前に通信で\x01",
            "教えてくれたじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x10,
        (
            "#1303Fうーん…………\x02\x03",

            "#1300F……そうね、そう言われると\x01",
            "言った覚えがあるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#0006F（あ、危なかった……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 1)
    Jump("loc_2E81")

    label("loc_2DE9")


    #C0126
    ChrTalk(
        0x10,
        (
            "#1306Fあーあ、ちょっと残念かな。\x02\x03",

            "今度イリアにこっそり会わせて\x01",
            "驚かせてあげようと思ったのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#0012Fは、はは……\x01",
            "（もう会ってるんだけど……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E81")

    Jump("loc_3122")

    label("loc_2E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3122")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EA1")
    Call(0, 17)
    Jump("loc_3122")

    label("loc_2EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B1")

    #C0128
    ChrTalk(
        0x10,
        (
            "#1306F私も寮暮らしだから\x01",
            "お互いなかなか\x01",
            "会う機会が作れないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#0004Fはは、そうだね。\x02\x03",

            "#0001Fでもセシル姉……\x01",
            "仕事、忙しそうだけど\x01",
            "あまり無理しないでくれよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x10,
        (
            "#1309Fふふ、無理はしてないわ。\x02\x03",

            "たまに通信で友達とお喋りして\x01",
            "気晴らしとかもしているしね。\x02\x03",

            "#1302F昨日の夜も、久しぶりに\x01",
            "その友達と長話をしちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#0009Fはは、そっか。\x02\x03",

            "#0000Fその友達って\x01",
            "俺も知っている人かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x10,
        (
            "#1304Fふふ……どうかしら。\x02\x03",

            "#1302Fロイドって意外と世間知らずだから\x01",
            "知らないかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#0005F？？？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 0)
    Jump("loc_3122")

    label("loc_30B1")


    #C0134
    ChrTalk(
        0x10,
        (
            "#1304F彼女も頑張ってるみたいだし……\x01",
            "私も一生懸命やっていかないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#0005F（誰のことなんだろう……）\x02",
    )

    CloseMessageWindow()

    label("loc_3122")

    TalkEnd(0xFE)
    Return()

    # Function_16_2673 end

    def Function_17_3126(): pass

    label("Function_17_3126")

    EventBegin(0x0)
    Fade(500)
    OP_68(153900, 1000, 53760, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 153000, 0, 54180, 90)
    SetChrPos(0x102, 153000, 0, 53180, 90)
    SetChrPos(0x103, 151800, 0, 53180, 90)
    SetChrPos(0x104, 151800, 0, 54180, 90)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x10, 0x10E, 0x0)
    OP_0D()

    #C0136
    ChrTalk(
        0x10,
        (
            "#1302Fあら、みんな。\x01",
            "ふふっ、いらっしゃい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3224")

    #C0137
    ChrTalk(
        0x101,
        (
            "#0005Fあ、もしかしてここが\x01",
            "セシル姉の寮部屋なんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3257")

    label("loc_3224")


    #C0138
    ChrTalk(
        0x101,
        (
            "#0005Fやっぱりここが\x01",
            "セシル姉の寮部屋なんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3257")


    #C0139
    ChrTalk(
        0x10,
        (
            "#1300Fええ、そうよ。\x02\x03",

            "#1304Fもっとも病棟の\x01",
            "仮眠室で寝ることも多いから\x01",
            "半分くらいしか使っていないけど。\x02",
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

    #C0140
    ChrTalk(
        0x102,
        "#0106Fセシルさん……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x103,
        "#0208F……働きすぎです。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        (
            "#0306Fもうちょっと自分を\x01",
            "労わってやってくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x10,
        (
            "#1309F大丈夫、大丈夫。\x01",
            "無理はしてないから。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153000, 0, 53680, 90)
    SetScenarioFlags(0xAE, 5)
    EventEnd(0x5)
    Return()

    # Function_17_3126 end

    def Function_18_33DF(): pass

    label("Function_18_33DF")

    EventBegin(0x0)
    Fade(500)
    OP_68(153900, 1000, 53760, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_343F")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, 150600, 0, 53680, 90)

    label("loc_343F")

    SetChrPos(0x101, 153000, 0, 54180, 90)
    SetChrPos(0x102, 153000, 0, 53180, 90)
    SetChrPos(0x103, 151800, 0, 53180, 90)
    SetChrPos(0x104, 151800, 0, 54180, 90)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x10, 0x5A, 0x0)
    OP_0D()

    #C0144
    ChrTalk(
        0x10,
        "#1308F………………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0145
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セシルは棚にある写真立てを眺めている。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_352B")

    #C0146
    ChrTalk(
        0x101,
        (
            "#0005Fセシル姉……？\x01",
            "（って、あの写真は……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3556")

    label("loc_352B")


    #C0147
    ChrTalk(
        0x101,
        (
            "#0005Fセシル姉……\x01",
            "（あの写真は……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3556")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3595")

    #C0148
    ChrTalk(
        0x10A,
        "#0608F（……この女性は、確か奴の……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEC, 6)

    label("loc_3595")

    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x10, 0x10E, 0x1F4)

    #C0149
    ChrTalk(
        0x10,
        (
            "#1302Fあら、みんないらっしゃい。\x02\x03",

            "#1305F………？\x01",
            "何だか急いでいるみたいだけど\x01",
            "どうしたのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#0000Fはは、うん。\x01",
            "ちょっと捜査で忙しくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        "#0100Fセシルさんの方は休憩ですか？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x10,
        (
            "#1304Fふふ、そんな所かしら。\x02\x03",

            "大切な仕事だとは思うけど\x01",
            "くれぐれも無理はしないでね。\x02\x03",

            "#1300Fあんまり無理ばかりしてると\x01",
            "強制入院させちゃうんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        "#0011Fわ、分かったよ。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        "#0100Fふふ、肝に銘じておきます。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        (
            "#0309F（うーん、セシルさんになら\x01",
            "  強引に入院させられてぇ～！）\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        "#0206F（……言うと思いました。）\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153000, 0, 53680, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37E2")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_37E2")

    SetScenarioFlags(0xEC, 5)
    EventEnd(0x5)
    Return()

    # Function_18_33DF end

    def Function_19_37E8(): pass

    label("Function_19_37E8")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetChrName("")

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セシルとロイド、\x01",
            "そして精悍な顔つきの青年が写った\x01",
            "写真が立てかけられている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3915")

    #A0158
    AnonymousTalk(
        0x101,
        (
            "#0008F（……セシル姉と\x01",
            "  兄貴と撮った写真だ。）\x02\x03",

            "（俺も肌身離さず持ってるけど、\x01",
            "  セシル姉も飾ってたんだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399E")

    label("loc_3915")


    #A0159
    AnonymousTalk(
        0x101,
        (
            "#0005F（あ……セシル姉と\x01",
            "  兄貴と撮った写真だ。）\x02\x03",

            "#0003F（この写真があるって事は\x01",
            "  もしかしてここが\x01",
            "  セシル姉の寮部屋なのかな？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399E")

    SetScenarioFlags(0x69, 5)

    label("loc_39A1")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_19_37E8 end

    SaveToFile()

Try(main)
