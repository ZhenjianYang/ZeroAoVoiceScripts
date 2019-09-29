from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c013b.bin",                # FileName
        "c013b",                    # MapName
        "c013b",                    # Location
        0x0009,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 0, 0, 1],
    )

    BuildStringList((
        "c013b",                  # 0
        "琪雅",                   # 1
        "假",                     # 2
        "SE控制",                 # 3
    ))

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch08202.itc",                   # 01
    ))

    DeclNpc(0,       0,       0,       0,    385,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(13960,   0,       63640,   1500,    13960,   1500,    63640,   0x007C, 0,  3,  0x0000)
    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  2,  0x0000)
    DeclActor(158830,  0,       125480,  1200,    158830,  2000,    125480,  0x007C, 0,  19, 0x0000)
    DeclActor(155320,  30,      123780,  1200,    155320,  1500,    123780,  0x007C, 0,  20, 0x0000)
    DeclActor(205730,  0,       130250,  1200,    205730,  1500,    130250,  0x007C, 0,  22, 0x0000)
    DeclActor(208820,  0,       123770,  1200,    208820,  2500,    123770,  0x007C, 0,  23, 0x0000)
    DeclActor(259740,  0,       121980,  1200,    259740,  3000,    121980,  0x007C, 0,  24, 0x0000)
    DeclActor(259339,  0,       126100,  1200,    259339,  1500,    126100,  0x007C, 0,  25, 0x0000)
    DeclActor(255780,  30,      65319,   1200,    255780,  1500,    65319,   0x007C, 0,  26, 0x0000)
    DeclActor(257120,  30,      68930,   1200,    257120,  1030,    68930,   0x007C, 0,  27, 0x0000)
    DeclActor(259010,  0,       66930,   1200,    259010,  1000,    66930,   0x007C, 0,  28, 0x0000)
    DeclActor(255680,  30,      73720,   1200,    255680,  1500,    73720,   0x007C, 0,  29, 0x0000)
    DeclActor(258000,  0,       63980,   1200,    258000,  2000,    63980,   0x007C, 0,  30, 0x0000)
    DeclActor(153580,  30,      127880,  1200,    153370,  1530,    128389,  0x007C, 0,  16, 0x0000)
    DeclActor(207040,  30,      128539,  1200,    207640,  1500,    129090,  0x007C, 0,  17, 0x0000)
    DeclActor(258360,  0,       128430,  1200,    258360,  1500,    128430,  0x007C, 0,  18, 0x0000)

    ChipFrameInfo(948, 0)                                        # 0

    ScpFunction((
        "Function_0_3B4",          # 00, 0
        "Function_1_3C4",          # 01, 1
        "Function_2_5E1",          # 02, 2
        "Function_3_61A",          # 03, 3
        "Function_4_61B",          # 04, 4
        "Function_5_7D8",          # 05, 5
        "Function_6_9A7",          # 06, 6
        "Function_7_B64",          # 07, 7
        "Function_8_D21",          # 08, 8
        "Function_9_EE5",          # 09, 9
        "Function_10_10A9",        # 0A, 10
        "Function_11_12F3",        # 0B, 11
        "Function_12_153D",        # 0C, 12
        "Function_13_1787",        # 0D, 13
        "Function_14_19D1",        # 0E, 14
        "Function_15_1C1B",        # 0F, 15
        "Function_16_1C6E",        # 10, 16
        "Function_17_1D0D",        # 11, 17
        "Function_18_1DAC",        # 12, 18
        "Function_19_1E4B",        # 13, 19
        "Function_20_1EFC",        # 14, 20
        "Function_21_1FD5",        # 15, 21
        "Function_22_1FDE",        # 16, 22
        "Function_23_2091",        # 17, 23
        "Function_24_2142",        # 18, 24
        "Function_25_21F1",        # 19, 25
        "Function_26_22A4",        # 1A, 26
        "Function_27_2355",        # 1B, 27
        "Function_28_2406",        # 1C, 28
        "Function_29_24B7",        # 1D, 29
        "Function_30_256C",        # 1E, 30
        "Function_31_2623",        # 1F, 31
        "Function_32_2698",        # 20, 32
    ))


    def Function_0_3B4(): pass

    label("Function_0_3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3C3")
    ClearScenarioFlags(0x22, 0)
    Event(0, 32)

    label("loc_3C3")

    Return()

    # Function_0_3B4 end

    def Function_1_3C4(): pass

    label("Function_1_3C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_449")
    SetMapObjFrame(0xFF, "danbo", 0x1, 0x1)
    SetMapObjFrame(0xFF, "n01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "n02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "n03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "asihuki", 0x0, 0x1)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 255600, -1000, 128900, 8000, 5000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 258899, -1000, 126000, 5000, 5000, 90000)
    Jump("loc_486")

    label("loc_449")

    SetMapObjFrame(0xFF, "danbo", 0x0, 0x1)
    SetMapObjFrame(0xFF, "n01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "n02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "n03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "asihuki", 0x1, 0x1)

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A0")
    SetMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x12, 0x2)
    OP_65(0x2, 0x1)

    label("loc_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB")
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x13, 0x2)
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x1E, 0x4)
    ClearMapObjFlags(0x1E, 0x2)
    Jump("loc_4D1")

    label("loc_4CB")

    SetMapObjFlags(0x1D, 0x4)

    label("loc_4D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB")
    SetMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x14, 0x2)
    OP_65(0x4, 0x1)

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_505")
    SetMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x15, 0x2)
    OP_65(0x5, 0x1)

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_523")
    SetMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x16, 0x2)
    OP_65(0x6, 0x1)

    label("loc_523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_541")
    SetMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x17, 0x2)
    OP_65(0x7, 0x1)

    label("loc_541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55B")
    SetMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x18, 0x2)
    OP_65(0x8, 0x1)

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_575")
    SetMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x19, 0x2)
    OP_65(0x9, 0x1)

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58F")
    SetMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1A, 0x2)
    OP_65(0xA, 0x1)

    label("loc_58F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A9")
    SetMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1B, 0x2)
    OP_65(0xB, 0x1)

    label("loc_5A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C3")
    SetMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1C, 0x2)
    OP_65(0xC, 0x1)

    label("loc_5C3")

    OP_65(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5E0")
    SetMapObjFlags(0x4, 0x10)
    OP_65(0x1, 0x1)

    label("loc_5E0")

    Return()

    # Function_1_3C4 end

    def Function_2_5E1(): pass

    label("Function_2_5E1")

    TalkBegin(0xFF)

    #C0001
    ChrTalk(
        0x101,
        (
            "#00000F这是缇欧的房间，\x01",
            "还是不要随便进去了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_2_5E1 end

    def Function_3_61A(): pass

    label("Function_3_61A")

    Return()

    # Function_3_61A end

    def Function_4_61B(): pass

    label("Function_4_61B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x2)
    OP_68(157620, 1330, 125080, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_675")
    SetChrFlags(0x0, 0x8)

    label("loc_675")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_688")
    SetChrFlags(0x1, 0x8)

    label("loc_688")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69B")
    SetChrFlags(0x2, 0x8)

    label("loc_69B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AE")
    SetChrFlags(0x3, 0x8)

    label("loc_6AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C1")
    SetChrFlags(0x4, 0x8)

    label("loc_6C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D4")
    SetChrFlags(0x5, 0x8)

    label("loc_6D4")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 157620, 30, 125080, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0002
    ChrTalk(
        0x102,
        "#0100F放在这里如何？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34A, 1)
    SetScenarioFlags(0x13C, 6)
    OP_66(0x2, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_765")
    ClearChrFlags(0x0, 0x8)

    label("loc_765")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_778")
    ClearChrFlags(0x1, 0x8)

    label("loc_778")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78B")
    ClearChrFlags(0x2, 0x8)

    label("loc_78B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79E")
    ClearChrFlags(0x3, 0x8)

    label("loc_79E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B1")
    ClearChrFlags(0x4, 0x8)

    label("loc_7B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C4")
    ClearChrFlags(0x5, 0x8)

    label("loc_7C4")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_4_61B end

    def Function_5_7D8(): pass

    label("Function_5_7D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x2)
    SetMapObjFlags(0x1D, 0x4)
    ClearMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1E, 0x2)
    OP_68(154920, 1330, 122580, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_844")
    SetChrFlags(0x0, 0x8)

    label("loc_844")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_857")
    SetChrFlags(0x1, 0x8)

    label("loc_857")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86A")
    SetChrFlags(0x2, 0x8)

    label("loc_86A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87D")
    SetChrFlags(0x3, 0x8)

    label("loc_87D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_890")
    SetChrFlags(0x4, 0x8)

    label("loc_890")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A3")
    SetChrFlags(0x5, 0x8)

    label("loc_8A3")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154920, 30, 122580, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0004
    ChrTalk(
        0x102,
        "#0100F放在这里如何？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34B, 1)
    SetScenarioFlags(0x13C, 7)
    OP_66(0x3, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_934")
    ClearChrFlags(0x0, 0x8)

    label("loc_934")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_947")
    ClearChrFlags(0x1, 0x8)

    label("loc_947")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95A")
    ClearChrFlags(0x2, 0x8)

    label("loc_95A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_96D")
    ClearChrFlags(0x3, 0x8)

    label("loc_96D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_980")
    ClearChrFlags(0x4, 0x8)

    label("loc_980")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_993")
    ClearChrFlags(0x5, 0x8)

    label("loc_993")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_5_7D8 end

    def Function_6_9A7(): pass

    label("Function_6_9A7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x2)
    OP_68(206000, 1300, 129509, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A01")
    SetChrFlags(0x0, 0x8)

    label("loc_A01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A14")
    SetChrFlags(0x1, 0x8)

    label("loc_A14")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A27")
    SetChrFlags(0x2, 0x8)

    label("loc_A27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3A")
    SetChrFlags(0x3, 0x8)

    label("loc_A3A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A4D")
    SetChrFlags(0x4, 0x8)

    label("loc_A4D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A60")
    SetChrFlags(0x5, 0x8)

    label("loc_A60")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 206000, 0, 129509, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0006
    ChrTalk(
        0x103,
        "#0200F就放在这里吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34C, 1)
    SetScenarioFlags(0x13D, 0)
    OP_66(0x4, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF1")
    ClearChrFlags(0x0, 0x8)

    label("loc_AF1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B04")
    ClearChrFlags(0x1, 0x8)

    label("loc_B04")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B17")
    ClearChrFlags(0x2, 0x8)

    label("loc_B17")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2A")
    ClearChrFlags(0x3, 0x8)

    label("loc_B2A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B3D")
    ClearChrFlags(0x4, 0x8)

    label("loc_B3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B50")
    ClearChrFlags(0x5, 0x8)

    label("loc_B50")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_6_9A7 end

    def Function_7_B64(): pass

    label("Function_7_B64")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x2)
    OP_68(208220, 1300, 123970, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBE")
    SetChrFlags(0x0, 0x8)

    label("loc_BBE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD1")
    SetChrFlags(0x1, 0x8)

    label("loc_BD1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE4")
    SetChrFlags(0x2, 0x8)

    label("loc_BE4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF7")
    SetChrFlags(0x3, 0x8)

    label("loc_BF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0A")
    SetChrFlags(0x4, 0x8)

    label("loc_C0A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1D")
    SetChrFlags(0x5, 0x8)

    label("loc_C1D")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208220, 0, 123970, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0008
    ChrTalk(
        0x103,
        "#0200F就放在这里吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34D, 1)
    SetScenarioFlags(0x13D, 1)
    OP_66(0x5, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CAE")
    ClearChrFlags(0x0, 0x8)

    label("loc_CAE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC1")
    ClearChrFlags(0x1, 0x8)

    label("loc_CC1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD4")
    ClearChrFlags(0x2, 0x8)

    label("loc_CD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE7")
    ClearChrFlags(0x3, 0x8)

    label("loc_CE7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFA")
    ClearChrFlags(0x4, 0x8)

    label("loc_CFA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0D")
    ClearChrFlags(0x5, 0x8)

    label("loc_D0D")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_7_B64 end

    def Function_8_D21(): pass

    label("Function_8_D21")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x2)
    OP_68(258329, 1300, 122180, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7B")
    SetChrFlags(0x0, 0x8)

    label("loc_D7B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D8E")
    SetChrFlags(0x1, 0x8)

    label("loc_D8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA1")
    SetChrFlags(0x2, 0x8)

    label("loc_DA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB4")
    SetChrFlags(0x3, 0x8)

    label("loc_DB4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC7")
    SetChrFlags(0x4, 0x8)

    label("loc_DC7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDA")
    SetChrFlags(0x5, 0x8)

    label("loc_DDA")

    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 258329, 0, 122180, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0010
    ChrTalk(
        0x109,
        "#10100F放在这里应该不错。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "诺艾尔的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x350, 1)
    SetScenarioFlags(0x13D, 2)
    OP_66(0x6, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E72")
    ClearChrFlags(0x0, 0x8)

    label("loc_E72")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E85")
    ClearChrFlags(0x1, 0x8)

    label("loc_E85")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E98")
    ClearChrFlags(0x2, 0x8)

    label("loc_E98")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EAB")
    ClearChrFlags(0x3, 0x8)

    label("loc_EAB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBE")
    ClearChrFlags(0x4, 0x8)

    label("loc_EBE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED1")
    ClearChrFlags(0x5, 0x8)

    label("loc_ED1")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_8_D21 end

    def Function_9_EE5(): pass

    label("Function_9_EE5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x2)
    OP_68(258149, 1300, 125700, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F3F")
    SetChrFlags(0x0, 0x8)

    label("loc_F3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F52")
    SetChrFlags(0x1, 0x8)

    label("loc_F52")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F65")
    SetChrFlags(0x2, 0x8)

    label("loc_F65")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F78")
    SetChrFlags(0x3, 0x8)

    label("loc_F78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F8B")
    SetChrFlags(0x4, 0x8)

    label("loc_F8B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9E")
    SetChrFlags(0x5, 0x8)

    label("loc_F9E")

    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 258149, 0, 125700, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0012
    ChrTalk(
        0x109,
        "#10100F放在这里应该不错。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "诺艾尔的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x351, 1)
    SetScenarioFlags(0x13D, 3)
    OP_66(0x7, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1036")
    ClearChrFlags(0x0, 0x8)

    label("loc_1036")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1049")
    ClearChrFlags(0x1, 0x8)

    label("loc_1049")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105C")
    ClearChrFlags(0x2, 0x8)

    label("loc_105C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106F")
    ClearChrFlags(0x3, 0x8)

    label("loc_106F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1082")
    ClearChrFlags(0x4, 0x8)

    label("loc_1082")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1095")
    ClearChrFlags(0x5, 0x8)

    label("loc_1095")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_9_EE5 end

    def Function_10_10A9(): pass

    label("Function_10_10A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00000F对了，这个玩偶……\x01",
            "和琪雅的房间似乎很相称呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德找到琪雅，\x01",
            "把玩偶送给了她。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x2)
    OP_68(256110, 1330, 66720, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116C")
    SetChrFlags(0x0, 0x8)

    label("loc_116C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_117F")
    SetChrFlags(0x1, 0x8)

    label("loc_117F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1192")
    SetChrFlags(0x2, 0x8)

    label("loc_1192")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11A5")
    SetChrFlags(0x3, 0x8)

    label("loc_11A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B8")
    SetChrFlags(0x4, 0x8)

    label("loc_11B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11CB")
    SetChrFlags(0x5, 0x8)

    label("loc_11CB")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 256980, 30, 66530, 225)
    ClearChrFlags(0x8, 0x8)
    SetChrPos(0x8, 256019, 30, 66750, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    #C0016
    ChrTalk(
        0x8,
        "#01100F就放在这里！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "琪雅的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x355, 1)
    SetScenarioFlags(0x13D, 4)
    OP_66(0x8, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1278")
    ClearChrFlags(0x0, 0x8)

    label("loc_1278")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_128B")
    ClearChrFlags(0x1, 0x8)

    label("loc_128B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_129E")
    ClearChrFlags(0x2, 0x8)

    label("loc_129E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B1")
    ClearChrFlags(0x3, 0x8)

    label("loc_12B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C4")
    ClearChrFlags(0x4, 0x8)

    label("loc_12C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D7")
    ClearChrFlags(0x5, 0x8)

    label("loc_12D7")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_10_10A9 end

    def Function_11_12F3(): pass

    label("Function_11_12F3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00000F对了，这个玩偶……\x01",
            "和琪雅的房间似乎很相称呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德找到琪雅，\x01",
            "把玩偶送给了她。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x2)
    OP_68(255780, 1300, 68700, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B6")
    SetChrFlags(0x0, 0x8)

    label("loc_13B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C9")
    SetChrFlags(0x1, 0x8)

    label("loc_13C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DC")
    SetChrFlags(0x2, 0x8)

    label("loc_13DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13EF")
    SetChrFlags(0x3, 0x8)

    label("loc_13EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1402")
    SetChrFlags(0x4, 0x8)

    label("loc_1402")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1415")
    SetChrFlags(0x5, 0x8)

    label("loc_1415")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 255780, 30, 69500, 135)
    ClearChrFlags(0x8, 0x8)
    SetChrPos(0x8, 255780, 0, 68700, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    #C0020
    ChrTalk(
        0x8,
        "#01100F就放在这里！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "琪雅的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x354, 1)
    SetScenarioFlags(0x13D, 5)
    OP_66(0x9, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C2")
    ClearChrFlags(0x0, 0x8)

    label("loc_14C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D5")
    ClearChrFlags(0x1, 0x8)

    label("loc_14D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E8")
    ClearChrFlags(0x2, 0x8)

    label("loc_14E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FB")
    ClearChrFlags(0x3, 0x8)

    label("loc_14FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_150E")
    ClearChrFlags(0x4, 0x8)

    label("loc_150E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1521")
    ClearChrFlags(0x5, 0x8)

    label("loc_1521")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_11_12F3 end

    def Function_12_153D(): pass

    label("Function_12_153D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00000F对了，这个玩偶……\x01",
            "和琪雅的房间似乎很相称呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德找到琪雅，\x01",
            "把玩偶送给了她。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1A, 0x2)
    OP_68(258110, 1300, 67120, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1600")
    SetChrFlags(0x0, 0x8)

    label("loc_1600")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1613")
    SetChrFlags(0x1, 0x8)

    label("loc_1613")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1626")
    SetChrFlags(0x2, 0x8)

    label("loc_1626")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1639")
    SetChrFlags(0x3, 0x8)

    label("loc_1639")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_164C")
    SetChrFlags(0x4, 0x8)

    label("loc_164C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_165F")
    SetChrFlags(0x5, 0x8)

    label("loc_165F")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 259010, 0, 65730, 0)
    ClearChrFlags(0x8, 0x8)
    SetChrPos(0x8, 258110, 0, 67120, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    #C0024
    ChrTalk(
        0x8,
        "#01100F就放在这里！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "琪雅的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x356, 1)
    SetScenarioFlags(0x13D, 6)
    OP_66(0xA, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_170C")
    ClearChrFlags(0x0, 0x8)

    label("loc_170C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_171F")
    ClearChrFlags(0x1, 0x8)

    label("loc_171F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1732")
    ClearChrFlags(0x2, 0x8)

    label("loc_1732")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1745")
    ClearChrFlags(0x3, 0x8)

    label("loc_1745")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1758")
    ClearChrFlags(0x4, 0x8)

    label("loc_1758")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_176B")
    ClearChrFlags(0x5, 0x8)

    label("loc_176B")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_12_153D end

    def Function_13_1787(): pass

    label("Function_13_1787")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    #C0026
    ChrTalk(
        0x101,
        (
            "#00000F对了，这个玩偶……\x01",
            "和琪雅的房间似乎很相称呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德找到琪雅，\x01",
            "把玩偶送给了她。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    ClearMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1B, 0x2)
    OP_68(255730, 1330, 72650, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_184A")
    SetChrFlags(0x0, 0x8)

    label("loc_184A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_185D")
    SetChrFlags(0x1, 0x8)

    label("loc_185D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1870")
    SetChrFlags(0x2, 0x8)

    label("loc_1870")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1883")
    SetChrFlags(0x3, 0x8)

    label("loc_1883")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1896")
    SetChrFlags(0x4, 0x8)

    label("loc_1896")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18A9")
    SetChrFlags(0x5, 0x8)

    label("loc_18A9")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 254270, 30, 72640, 45)
    ClearChrFlags(0x8, 0x8)
    SetChrPos(0x8, 255730, 30, 72650, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    #C0028
    ChrTalk(
        0x8,
        "#01100F就放在这里！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "琪雅的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x357, 1)
    SetScenarioFlags(0x13D, 7)
    OP_66(0xB, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1956")
    ClearChrFlags(0x0, 0x8)

    label("loc_1956")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1969")
    ClearChrFlags(0x1, 0x8)

    label("loc_1969")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_197C")
    ClearChrFlags(0x2, 0x8)

    label("loc_197C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_198F")
    ClearChrFlags(0x3, 0x8)

    label("loc_198F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A2")
    ClearChrFlags(0x4, 0x8)

    label("loc_19A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19B5")
    ClearChrFlags(0x5, 0x8)

    label("loc_19B5")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_13_1787 end

    def Function_14_19D1(): pass

    label("Function_14_19D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    #C0030
    ChrTalk(
        0x101,
        (
            "#00000F对了，这个玩偶……\x01",
            "和琪雅的房间似乎很相称呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德找到琪雅，\x01",
            "把玩偶送给了她。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    ClearMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1C, 0x2)
    OP_68(256839, 1330, 63970, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A94")
    SetChrFlags(0x0, 0x8)

    label("loc_1A94")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AA7")
    SetChrFlags(0x1, 0x8)

    label("loc_1AA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ABA")
    SetChrFlags(0x2, 0x8)

    label("loc_1ABA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ACD")
    SetChrFlags(0x3, 0x8)

    label("loc_1ACD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AE0")
    SetChrFlags(0x4, 0x8)

    label("loc_1AE0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AF3")
    SetChrFlags(0x5, 0x8)

    label("loc_1AF3")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 258410, 0, 65590, 180)
    ClearChrFlags(0x8, 0x8)
    SetChrPos(0x8, 256839, 30, 63970, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    #C0032
    ChrTalk(
        0x8,
        "#01100F就放在这里！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0033
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "琪雅的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x358, 1)
    SetScenarioFlags(0x13E, 0)
    OP_66(0xC, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA0")
    ClearChrFlags(0x0, 0x8)

    label("loc_1BA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB3")
    ClearChrFlags(0x1, 0x8)

    label("loc_1BB3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC6")
    ClearChrFlags(0x2, 0x8)

    label("loc_1BC6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD9")
    ClearChrFlags(0x3, 0x8)

    label("loc_1BD9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BEC")
    ClearChrFlags(0x4, 0x8)

    label("loc_1BEC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BFF")
    ClearChrFlags(0x5, 0x8)

    label("loc_1BFF")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_14_19D1 end

    def Function_15_1C1B(): pass

    label("Function_15_1C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6D")
    SetChrName("")

    #A0034
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果得到了家具类道具，\x01",
            "可以放置在支援科各成员的房间中。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x13B, 7)

    label("loc_1C6D")

    Return()

    # Function_15_1C1B end

    def Function_16_1C6E(): pass

    label("Function_16_1C6E")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CEF")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1CEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D0B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1D0B")

    Return()

    # Function_16_1C6E end

    def Function_17_1D0D(): pass

    label("Function_17_1D0D")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D8E")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1D8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DAA")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1DAA")

    Return()

    # Function_17_1D0D end

    def Function_18_1DAC(): pass

    label("Function_18_1DAC")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2D")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1E2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E49")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1E49")

    Return()

    # Function_18_1DAC end

    def Function_19_1E4B(): pass

    label("Function_19_1E4B")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis362.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着优雅衣镜。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_19_1E4B end

    def Function_20_1EFC(): pass

    label("Function_20_1EFC")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis363.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着八音盒。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    BeginChrThread(0xA, 1, 0, 21)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_20_1EFC end

    def Function_21_1FD5(): pass

    label("Function_21_1FD5")

    PlayBGM("ed7591", 0)
    Sleep(19000)
    OP_1F()
    Return()

    # Function_21_1FD5 end

    def Function_22_1FDE(): pass

    label("Function_22_1FDE")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis364.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着影丸储蓄罐。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_22_1FDE end

    def Function_23_2091(): pass

    label("Function_23_2091")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis365.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0038
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着咪雪玩偶。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_23_2091 end

    def Function_24_2142(): pass

    label("Function_24_2142")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis370.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着竞赛旗。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_24_2142 end

    def Function_25_21F1(): pass

    label("Function_25_21F1")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis371.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着小径自行车。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_25_21F1 end

    def Function_26_22A4(): pass

    label("Function_26_22A4")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis373.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着波波靠垫。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_26_22A4 end

    def Function_27_2355(): pass

    label("Function_27_2355")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis372.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着古怪靠垫。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_27_2355 end

    def Function_28_2406(): pass

    label("Function_28_2406")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis374.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着黑泰迪熊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_28_2406 end

    def Function_29_24B7(): pass

    label("Function_29_24B7")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis375.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着苦番茄人玩偶。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_29_24B7 end

    def Function_30_256C(): pass

    label("Function_30_256C")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis376.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着ＺＷＥＩ２企鹅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_30_256C end

    def Function_31_2623(): pass

    label("Function_31_2623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2697")
    OP_E0(0x16, 0x0)

    label("loc_2697")

    Return()

    # Function_31_2623 end

    def Function_32_2698(): pass

    label("Function_32_2698")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51420.itc", 0x1E)
    LoadChrToIndex("apl/ch51421.itc", 0x1F)
    LoadChrToIndex("apl/ch51422.itc", 0x20)
    LoadChrToIndex("apl/ch51425.itc", 0x21)
    SetChrPos(0x101, 5000, 0, 65500, 0)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x10)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 153550, 320, 129100, 0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x10)
    SetChrFlags(0x103, 0x2)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 208550, 280, 129000, 0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 14000, 0, 65000, 180)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x109, 0x10)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x4)
    SetChrPos(0x109, 258500, 280, 128949, 0)
    SetChrPos(0x105, 5000, 0, 65500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x9, 14000, 800, 63000, 270)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x1F, 0x1000)
    SetMapObjFrame(0xFF, "nhuton", 0x0, 0x1)
    SetMapObjFrame(0xFF, "huton", 0x0, 0x1)
    OP_7D(0x77, 0x77, 0x8B, 0x0, 0x0)
    OP_68(153400, 1100, 128850, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(18000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(208500, 1900, 129000, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18500, 0)
    OP_68(208500, 900, 129000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(258300, 1100, 128600, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(20500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(14000, 1300, 63000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
    StopBGM(0xFA0)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(103, 0, 70, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_296E():
        OP_96(0xFE, 0x36B0, 0x0, 0xF618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_296E)

    def lambda_2988():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2988)
    WaitChrThread(0x104, 1)
    Sound(104, 0, 70, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_93(0x104, 0x10E, 0x1F4)
    OP_6B(0x9)

    def lambda_29C2():
        OP_95(0xFE, -1000, 0, 63000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29C2)

    def lambda_29DC():
        OP_95(0xFE, -1000, 800, 63000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_29DC)
    WaitChrThread(0x104, 1)
    Sleep(300)
    OP_6B(0xFF)
    OP_68(1000, 1300, 63000, 1500)
    MoveCamera(57, 19, 0, 1500)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_6F(0x79)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)
    Sleep(500)
    OP_93(0x104, 0x0, 0x1F4)
    SetCameraDistance(23000, 7000)

    def lambda_2A50():
        OP_95(0xFE, -1000, 0, 70500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A50)
    WaitChrThread(0x104, 1)

    def lambda_2A6E():
        OP_95(0xFE, 1500, 0, 70500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A6E)
    WaitChrThread(0x104, 1)
    FadeToDark(2000, 0, -1)

    def lambda_2A96():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A96)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x10)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x10)
    ClearChrFlags(0x103, 0x2)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x109, 0x10)
    ClearChrFlags(0x109, 0x2)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_2698 end

    SaveToFile()

Try(main)
