from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t4000.bin",                # FileName
        "t4000",                    # MapName
        "t4000",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 4, 0, 5],
    )

    BuildStringList((
        "t4000",                  # 0
        "莉丝修女",               # 1
        "罗兰德祭司",             # 2
        "久久修女",               # 3
        "塔米尔",                 # 4
        "哈米尔",                 # 5
        "普鲁娜",                 # 6
        "利娜莉",                 # 7
        "布利克",                 # 8
        "伊安律师",               # 9
        "玛因兹山道",             # 10
    ))

    AddCharChip((
        "chr/ch14000.itc",                   # 00
        "chr/ch25400.itc",                   # 01
        "chr/ch25500.itc",                   # 02
        "chr/ch23800.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch22100.itc",                   # 05
        "chr/ch20400.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-9399,   500,     14000,   90,   389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-2630,   0,       9369,    180,  257,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(2299,    0,       14270,   180,  257,  0x0, 0,   2,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(-5780,   0,       14529,   180,  385,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-5780,   0,       13680,   0,    385,  0x0, 0,   3,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(5809,    0,       19469,   90,   385,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(7619,    0,       19180,   270,  385,  0x0, 0,   5,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-3640,   2000,    31379,   135,  385,  0x0, 0,   6,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-10390,  500,     13820,   1200,    -10390,  2000,    13820,   0x007C, 0,  24, 0x0000)

    PlaceName(5.0, -0.0, -35.0, 0x0000, 0x0000, "玛因兹山道")

    ChipFrameInfo(680, 0)                                        # 0

    ScpFunction((
        "Function_0_2A8",          # 00, 0
        "Function_1_358",          # 01, 1
        "Function_2_4A9",          # 02, 2
        "Function_3_50A",          # 03, 3
        "Function_4_56B",          # 04, 4
        "Function_5_88F",          # 05, 5
        "Function_6_997",          # 06, 6
        "Function_7_9D8",          # 07, 7
        "Function_8_18D2",         # 08, 8
        "Function_9_2369",         # 09, 9
        "Function_10_244D",        # 0A, 10
        "Function_11_266A",        # 0B, 11
        "Function_12_27AE",        # 0C, 12
        "Function_13_2C81",        # 0D, 13
        "Function_14_2D37",        # 0E, 14
        "Function_15_2E14",        # 0F, 15
        "Function_16_2F5A",        # 10, 16
        "Function_17_362F",        # 11, 17
        "Function_18_369F",        # 12, 18
        "Function_19_37D1",        # 13, 19
        "Function_20_3819",        # 14, 20
        "Function_21_39C2",        # 15, 21
        "Function_22_4B33",        # 16, 22
        "Function_23_4E34",        # 17, 23
        "Function_24_503A",        # 18, 24
        "Function_25_50B2",        # 19, 25
    ))


    def Function_0_2A8(): pass

    label("Function_0_2A8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2E0"),
        (1, "loc_2EC"),
        (2, "loc_2F8"),
        (3, "loc_304"),
        (4, "loc_310"),
        (5, "loc_31C"),
        (6, "loc_328"),
        (SWITCH_DEFAULT, "loc_334"),
    )


    label("loc_2E0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_2EC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_2F8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_304")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_310")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_31C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_328")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_334")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_340")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_357")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_340")

    label("loc_357")

    Return()

    # Function_0_2A8 end

    def Function_1_358(): pass

    label("Function_1_358")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A8")
    OP_95(0xFE, -2510, 0, 14270, 2000, 0x0)
    OP_95(0xFE, -2510, 0, 12920, 2000, 0x0)
    OP_95(0xFE, 11020, 0, 12920, 2000, 0x0)
    OP_95(0xFE, 18830, 0, 20000, 2000, 0x0)
    OP_95(0xFE, 18830, 0, 24520, 2000, 0x0)
    OP_95(0xFE, 26350, 0, 31740, 2000, 0x0)
    OP_95(0xFE, 26350, 0, 46780, 2000, 0x0)
    OP_95(0xFE, 23030, 0, 51110, 2000, 0x0)
    OP_95(0xFE, 23030, 0, 54060, 2000, 0x0)
    OP_95(0xFE, 21080, 0, 54060, 2000, 0x0)
    OP_95(0xFE, 21080, 0, 48950, 2000, 0x0)
    OP_95(0xFE, 25050, 0, 44720, 2000, 0x0)
    OP_95(0xFE, 25050, 0, 34580, 2000, 0x0)
    OP_95(0xFE, 17430, 0, 27090, 2000, 0x0)
    OP_95(0xFE, 17430, 0, 21180, 2000, 0x0)
    OP_95(0xFE, 9240, 0, 14270, 2000, 0x0)
    Jump("Function_1_358")

    label("loc_4A8")

    Return()

    # Function_1_358 end

    def Function_2_4A9(): pass

    label("Function_2_4A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_509")
    OP_95(0xFE, 23000, 0, 42000, 6000, 0x0)
    OP_95(0xFE, 19000, 0, 42000, 6000, 0x0)
    OP_95(0xFE, 19000, 0, 39000, 6000, 0x0)
    OP_95(0xFE, 23000, 0, 39000, 6000, 0x0)
    Jump("Function_2_4A9")

    label("loc_509")

    Return()

    # Function_2_4A9 end

    def Function_3_50A(): pass

    label("Function_3_50A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56A")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(100)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(100)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(100)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(100)
    Jump("Function_3_50A")

    label("loc_56A")

    Return()

    # Function_3_50A end

    def Function_4_56B(): pass

    label("Function_4_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C1")
    SetChrPos(0xA, -6830, 0, 14190, 90)
    BeginChrThread(0xA, 0, 0, 0)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B2")
    SetChrFlags(0xB, 0x10)

    label("loc_5B2")

    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_861")

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5CF")
    Jump("loc_861")

    label("loc_5CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5FB")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F6")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_5F6")

    Jump("loc_861")

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_620")
    SetChrPos(0xA, -1840, 2000, 32590, 180)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_861")

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_62E")
    Jump("loc_861")

    label("loc_62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_641")
    SetChrFlags(0xA, 0x80)
    Jump("loc_861")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_69E")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, 21060, 0, 40570, 90)
    BeginChrThread(0xA, 0, 0, 3)
    SetChrPos(0xB, 23000, 0, 41500, 0)
    SetChrPos(0xC, 23000, 0, 39000, 0)
    BeginChrThread(0xC, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_861")

    label("loc_69E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6C0")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_861")

    label("loc_6C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_6D3")
    SetChrFlags(0xA, 0x80)
    Jump("loc_861")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_6FA")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_861")

    label("loc_6FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_721")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_861")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_739")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_861")

    label("loc_739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_788")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 23000, 0, 41500, 180)
    SetChrPos(0xA, 23000, 0, 39000, 0)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_861")

    label("loc_788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7E3")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 11860, 0, 22480, 270)
    SetChrPos(0xA, 10060, 0, 21470, 90)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xC, 13660, 0, 23480, 135)
    Jump("loc_861")

    label("loc_7E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7F6")
    SetChrFlags(0xA, 0x80)
    Jump("loc_861")

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_83B")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81D")
    SetChrFlags(0xD, 0x10)

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82C")
    SetChrFlags(0xE, 0x10)

    label("loc_82C")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_861")

    label("loc_83B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_858")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_861")

    label("loc_858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_861")

    label("loc_861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_874")
    ClearChrFlags(0x8, 0x80)

    label("loc_874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88E")
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_88E")

    Return()

    # Function_4_56B end

    def Function_5_88F(): pass

    label("Function_5_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_913")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x5A, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_92A")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_92A")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_956")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x64, 0x0)
    Jump("loc_97D")

    label("loc_956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97D")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x64, 0x0)

    label("loc_97D")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_996")
    OP_1B(0x0, 0x0, 0x19)

    label("loc_996")

    Return()

    # Function_5_88F end

    def Function_6_997(): pass

    label("Function_6_997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A9")
    Call(0, 22)
    Return()

    label("loc_9A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9BA")
    Jump("loc_9D4")

    label("loc_9BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9C8")
    Jump("loc_9D4")

    label("loc_9C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9D4")
    Call(0, 10)

    label("loc_9D4")

    TalkEnd(0xFE)
    Return()

    # Function_6_997 end

    def Function_7_9D8(): pass

    label("Function_7_9D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7C")

    #C0001
    ChrTalk(
        0xFE,
        (
            "那棵散发着蓝白色光芒的\x01",
            "大树究竟是因何而出现在\x01",
            "克洛斯贝尔的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "它会给这片土地带来光明\x01",
            "还是灾厄……\x01",
            "连我们圣职者都无法预测。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AC0")

    label("loc_A7C")


    #C0003
    ChrTalk(
        0xFE,
        "那棵散发着蓝白色光芒的大树到底是……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "这也是女神的意志吗？\x02",
    )

    CloseMessageWindow()

    label("loc_AC0")

    Jump("loc_18CE")

    label("loc_AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B50")

    #C0005
    ChrTalk(
        0xFE,
        (
            "结界突然消失后，\x01",
            "市内出现了大量身着\x01",
            "甲胄的怪物……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "如果这也是迪塔总统所为，\x01",
            "那真是绝不能原谅的\x01",
            "行为。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B85")

    label("loc_B50")


    #C0007
    ChrTalk(
        0xFE,
        (
            "居然让怪物在市内徘徊……\x01",
            "真是绝不能原谅的行为。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B85")

    Jump("loc_18CE")

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C26")

    #C0008
    ChrTalk(
        0xFE,
        (
            "听说市内播放了\x01",
            "迪塔阁下的演讲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的独立\x01",
            "恐怕会给这片大陆\x01",
            "带来混乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "女神啊，请您引领人类走向光明吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C83")

    label("loc_C26")


    #C0011
    ChrTalk(
        0xFE,
        (
            "如今恐怕已经无法避免\x01",
            "与帝国和共和国发生冲突了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "女神啊，请您引领人类走向光明吧……\x02",
    )

    CloseMessageWindow()

    label("loc_C83")

    Jump("loc_18CE")

    label("loc_C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4A")

    #C0013
    ChrTalk(
        0xFE,
        (
            "今天将在大圣堂的礼拜堂内\x01",
            "举行一场弥撒。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "这次弥撒主要是为那些在袭击事件中牺牲的\x01",
            "人们祈愿，祈祷女神引渡他们的灵魂……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "各位如果有时间的话，\x01",
            "也请来参加吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DCC")

    label("loc_D4A")


    #C0016
    ChrTalk(
        0xFE,
        (
            "为了哀悼之前那起袭击事件，\x01",
            "今天将会举办一场祈福弥撒，\x01",
            "到时将会有很多参拜者前来。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "各位如果有时间的话，\x01",
            "也请来参加吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_DCC")

    Jump("loc_18CE")

    label("loc_DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_EAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E49")

    #C0018
    ChrTalk(
        0xFE,
        (
            "从昨晚开始，就能频繁听到\x01",
            "枪击声和爆破声。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "看来玛因兹那边的\x01",
            "交战状况十分\x01",
            "激烈呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EA8")

    label("loc_E49")


    #C0020
    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "武装集团未必不会\x01",
            "跑到这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "必须要尽早商讨一下\x01",
            "保卫大圣堂的对策才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA8")

    Jump("loc_18CE")

    label("loc_EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F01")

    #C0022
    ChrTalk(
        0xFE,
        (
            "整个克洛斯贝尔自治州\x01",
            "今天都在下雨。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "所以郊外的行人\x01",
            "非常少。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F5E")

    #C0024
    ChrTalk(
        0xFE,
        (
            "哈哈……\x01",
            "久久修女真受\x01",
            "孩子们欢迎呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "那也算是一种才能，\x01",
            "我很羡慕呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_105A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1005")

    #C0026
    ChrTalk(
        0xFE,
        (
            "罗赞贝尔克工房……\x01",
            "这个名字并不陌生。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "那间工房很久以前就存在了，\x01",
            "可那里的主人从没有\x01",
            "来过我们大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "到底是位什么样的\x01",
            "人呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1055")

    label("loc_1005")


    #C0029
    ChrTalk(
        0xFE,
        (
            "罗赞贝尔克工房的主人从没有\x01",
            "来过我们大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "那到底是位什么样的\x01",
            "人呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1055")

    Jump("loc_18CE")

    label("loc_105A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_10B6")

    #C0031
    ChrTalk(
        0xFE,
        (
            "塔米尔和哈米尔都\x01",
            "已经回家了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "好了，我也得开始\x01",
            "晚间清扫工作了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_10B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_11BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1160")

    #C0033
    ChrTalk(
        0xFE,
        (
            "伊安律师偶尔\x01",
            "会来大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "在接到特别棘手的案子时，\x01",
            "他一般就会到\x01",
            "我们这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "不知他今天在为\x01",
            "什么事情而烦恼……\x01",
            "希望他多加努力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11B7")

    label("loc_1160")


    #C0036
    ChrTalk(
        0xFE,
        (
            "伊安律师偶尔\x01",
            "会来大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "不知他今天在为\x01",
            "什么事情而烦恼……\x01",
            "希望他多加努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B7")

    Jump("loc_18CE")

    label("loc_11BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_12B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1250")

    #C0038
    ChrTalk(
        0xFE,
        (
            "听说最近在各地都出现了\x01",
            "来历不明的怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "警备队呼吁市民\x01",
            "不要独自一人到\x01",
            "太偏僻的地方去。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "各位也请多加小心。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12AD")

    label("loc_1250")


    #C0041
    ChrTalk(
        0xFE,
        (
            "听说最近在各地\x01",
            "都出现了来历不明的\x01",
            "怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "各位也请多加小心，\x01",
            "不要去太偏僻的地方哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AD")

    Jump("loc_18CE")

    label("loc_12B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1339")

    #C0043
    ChrTalk(
        0xFE,
        (
            "利贝尔王国的\x01",
            "科洛蒂娅王太女殿下\x01",
            "刚刚来到了大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "她和艾拉尔达大主教打过招呼后，\x01",
            "就往墓地那边去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B6")

    label("loc_1339")


    #C0045
    ChrTalk(
        0xFE,
        (
            "科洛蒂娅王太女殿下\x01",
            "已经在不久前动身\x01",
            "前往兰花塔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "今天这场正式会议的讨论结果……\x01",
            "还有殿下的动向，都很令人关注呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B6")

    Jump("loc_18CE")

    label("loc_13BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_14E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1483")

    #C0047
    ChrTalk(
        0xFE,
        (
            "大圣堂位于高地，\x01",
            "站在这里也能观看到\x01",
            "揭幕式的状况……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "揭去神秘面纱的兰花塔，\x01",
            "可真是壮观至极啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "人类居然能建造出\x01",
            "那么宏伟的建筑物……\x01",
            "哎呀呀，真叫人震惊不已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14E3")

    label("loc_1483")


    #C0050
    ChrTalk(
        0xFE,
        (
            "兰花塔的真面目\x01",
            "可真是壮观至极啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "那居然是人类建造出来的……\x01",
            "哎呀呀，真叫人震惊不已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E3")

    Jump("loc_18CE")

    label("loc_14E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_155E")

    #C0052
    ChrTalk(
        0xFE,
        (
            "听说为了确保通商会议顺利进行，\x01",
            "市内的警备力度有了大幅度强化。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "我在巡视大圣堂时也要\x01",
            "多加注意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_155E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_167E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160B")

    #C0054
    ChrTalk(
        0xFE,
        "今天的天气可真糟啊。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "不过，听说下雨的地区只有\x01",
            "市街区一带，玛因兹山道那边\x01",
            "就很晴朗呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "天气这种现象，\x01",
            "说不定就是女神的\x01",
            "心血来潮吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1679")

    label("loc_160B")


    #C0057
    ChrTalk(
        0xFE,
        (
            "听说只有市街区这一带下雨了，\x01",
            "玛因兹山道那边\x01",
            "就很晴朗。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "天气这种现象，\x01",
            "说不定就是女神的\x01",
            "心血来潮吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1679")

    Jump("loc_18CE")

    label("loc_167E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_1753")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1705")

    #C0059
    ChrTalk(
        0xFE,
        (
            "哦……？\x01",
            "要回去了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "随时都可以再来哦。\x01",
            "愿女神明天也\x01",
            "保佑大家平安……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x153,
        "#01109F嗯，再见啦～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_174E")

    label("loc_1705")


    #C0062
    ChrTalk(
        0xFE,
        "天色已晚，四周都有些昏暗了。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "各位下台阶的时候，\x01",
            "请注意脚下哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174E")

    Jump("loc_18CE")

    label("loc_1753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_17C5")

    #C0064
    ChrTalk(
        0xFE,
        (
            "我刚才看到的那个女孩\x01",
            "好像就是今天来赴任的修女。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "估计她现在正在和艾拉尔达大主教\x01",
            "打招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_17C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_18CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186B")

    #C0066
    ChrTalk(
        0xFE,
        "欢迎来到克洛斯贝尔大圣堂。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "在这里，将由克洛斯贝尔教区\x01",
            "之长，艾拉尔达大主教为大家\x01",
            "讲述七耀之教义。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "请各位在教会内\x01",
            "保持安静。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18CE")

    label("loc_186B")


    #C0069
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔大圣堂，\x01",
            "将由艾拉尔达大主教\x01",
            "为大家讲述七耀之教义。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "请各位在教会内\x01",
            "保持安静。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CE")

    TalkEnd(0xFE)
    Return()

    # Function_7_9D8 end

    def Function_8_18D2(): pass

    label("Function_8_18D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1937")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F0")
    Call(0, 9)
    Jump("loc_1932")

    label("loc_18F0")


    #C0071
    ChrTalk(
        0xFE,
        (
            "那库塔和\x01",
            "尤格特他们也\x01",
            "都没受伤吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "呼……真是太好了……\x02",
    )

    CloseMessageWindow()

    label("loc_1932")

    Jump("loc_2365")

    label("loc_1937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1989")

    #C0073
    ChrTalk(
        0xFE,
        "市内那些孩子现在还平安吗……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "塔米尔、哈米尔，还有大家……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2365")

    label("loc_1989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1A7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A2B")

    #C0075
    ChrTalk(
        0xFE,
        (
            "我觉得最重要的就是\x01",
            "孩子们的未来。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "独立能保护他们的未来吗……？\x01",
            "还是说，会给他们的未来带来威胁呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "我已经无法\x01",
            "判断了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A78")

    label("loc_1A2B")


    #C0078
    ChrTalk(
        0xFE,
        (
            "独立之后，\x01",
            "孩子们的未来\x01",
            "将会变成什么样呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "我已经无法\x01",
            "判断了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A78")

    Jump("loc_2365")

    label("loc_1A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B7E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AAF")
    Call(0, 23)
    Return()

    label("loc_1AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B12")

    #C0080
    ChrTalk(
        0xFE,
        (
            "我们会给前来参加弥撒的\x01",
            "孩子们分发曲奇饼。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "如果可以，请各位也来参加吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B79")

    label("loc_1B12")


    #C0082
    ChrTalk(
        0xFE,
        (
            "在那起袭击事件发生之后，\x01",
            "有不少人都对现在的\x01",
            "治安状况感到不安……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "真希望别再发生\x01",
            "那种事了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B79")

    Jump("loc_2365")

    label("loc_1B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C0C")

    #C0084
    ChrTalk(
        0xFE,
        (
            "塔米尔和哈米尔今天跑到\x01",
            "这里来玩，我马上就让\x01",
            "他们回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "毕竟发生了那样的事件，\x01",
            "还是留在家里，\x01",
            "才能让他们的父母放心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2365")

    label("loc_1C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C1A")
    Jump("loc_2365")

    label("loc_1C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA0")

    #C0086
    ChrTalk(
        0xFE,
        "你、你们给我站住！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "谁是掀了我裙子的\x01",
            "坏孩子塔米尔！？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xB,
        "嘿嘿，你猜猜看呀～☆\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        "呼……呼……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CFE")

    label("loc_1CA0")


    #C0090
    ChrTalk(
        0xFE,
        (
            "让、让我看看……\x01",
            "你、你是塔米尔吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "咦？等等，我再想想……\x01",
            "不对，你其实是哈米尔吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CFE")

    Jump("loc_2365")

    label("loc_1D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DF0")

    #C0092
    ChrTalk(
        0xFE,
        (
            "玛布尔修女昨天\x01",
            "教我授课方法时，\x01",
            "我注意到了一个问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "对于孩子们而言，\x01",
            "兴趣和干劲是完全成正比的。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "如果想教给他们什么东西，\x01",
            "最重要的就是让他们\x01",
            "产生兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "……不过，这一点\x01",
            "也正是最难做到的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E73")

    label("loc_1DF0")


    #C0096
    ChrTalk(
        0xFE,
        (
            "听玛布尔修女讲解了\x01",
            "主日学校的授课方式后，\x01",
            "我觉得自己成长了一点……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "不过，要想成为一名够格的修女，\x01",
            "我的修行还远远不足呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E73")

    Jump("loc_2365")

    label("loc_1E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_1E86")
    Jump("loc_2365")

    label("loc_1E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_1E94")
    Jump("loc_2365")

    label("loc_1E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EA2")
    Jump("loc_2365")

    label("loc_1EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1FD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F5E")

    #C0098
    ChrTalk(
        0xFE,
        (
            "那位负责保护科洛蒂娅公主的\x01",
            "尤莉亚准校……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "近距离一看，果然如传闻一般，\x01",
            "是位十分精神的女性呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "呵呵，我似乎有些理解\x01",
            "为何会有那么多女性对她痴迷了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FD0")

    label("loc_1F5E")


    #C0101
    ChrTalk(
        0xFE,
        (
            "听说尤莉亚准校是一位无论多么忙碌，\x01",
            "也不会忘记来教会祈祷的\x01",
            "虔诚之人。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "呵呵，说不定她\x01",
            "很适合穿\x01",
            "修道服呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FD0")

    Jump("loc_2365")

    label("loc_1FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FE6")
    Call(0, 10)
    Jump("loc_2365")

    label("loc_1FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FF7")
    Call(0, 11)
    Jump("loc_2365")

    label("loc_1FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2005")
    Jump("loc_2365")

    label("loc_2005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2134")
    TurnDirection(0xFE, 0x153, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C8")

    #C0103
    ChrTalk(
        0xFE,
        (
            "啊，小琪雅，\x01",
            "你要回去了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x153,
        (
            "#01100F嗯！罗伊德他们\x01",
            "来接我了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        "呵呵，那真是太好了。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "那我们下次上课时\x01",
            "再见啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x153,
        "#01109F嗯，拜拜～修女～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_212F")

    label("loc_20C8")


    #C0108
    ChrTalk(
        0xFE,
        (
            "小琪雅，\x01",
            "我们下次上课时再见啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "下次我会再烤些\x01",
            "曲奇饼给大家的。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x153,
        "#01109F嗯，我很期待哦！\x02",
    )

    CloseMessageWindow()

    label("loc_212F")

    Jump("loc_2365")

    label("loc_2134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_224E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E1")

    #C0111
    ChrTalk(
        0xFE,
        (
            "刚刚走进礼拜堂的那个女孩\x01",
            "就是新来的修女吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "我来这里不满一年，\x01",
            "还是个新人，\x01",
            "如今终于也要有后辈了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "总、总觉得有些\x01",
            "紧张呢……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2249")

    label("loc_21E1")


    #C0114
    ChrTalk(
        0xFE,
        (
            "我终于也要有后辈了……！\x01",
            "真有点紧张呢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "我一定要拿出前辈的样子，\x01",
            "教导她各种注意事项才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2249")

    Jump("loc_2365")

    label("loc_224E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2365")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F1")

    #C0116
    ChrTalk(
        0xFE,
        (
            "哎呀，你们好。\x01",
            "今天有主日学校的\x01",
            "授课哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "……各位莫非是\x01",
            "孩子的监护人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "进入礼拜堂后，右手边的房间\x01",
            "就是正在授课的教室。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2365")

    label("loc_22F1")


    #C0119
    ChrTalk(
        0xFE,
        (
            "进入礼拜堂后，右手边的房间\x01",
            "就是正在授课的教室。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "呵呵，如果有兴趣的话，要不要\x01",
            "去看看孩子们听课时的样子呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2365")

    TalkEnd(0xFE)
    Return()

    # Function_8_18D2 end

    def Function_9_2369(): pass

    label("Function_9_2369")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0121
    ChrTalk(
        0xA,
        (
            "塔米尔、哈米尔，\x01",
            "你们平安无事，真是太好了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        (
            "呜呜……啊啊，女神啊！\x01",
            "感谢您的慈悲……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    #C0123
    ChrTalk(
        0xB,
        (
            "喂、喂喂，修女，\x01",
            "你也不用哭成这样吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xC,
        "呵呵，谢谢你，修女。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_9_2369 end

    def Function_10_244D(): pass

    label("Function_10_244D")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_259E")

    #C0125
    ChrTalk(
        0x8,
        (
            "#04400F久久修女，\x01",
            "关于我明天的出差地点玛因兹，\x01",
            "我听说了一些令人在意的事情……\x02\x03",

            "#04403F据说在不久之前，\x01",
            "那里发生了怪异的事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "啊，说起来，\x01",
            "我也听过那个传闻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "好像是有人目击到\x01",
            "玛因兹地区的遗迹中\x01",
            "出现了幽灵。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "#04401F……可以告诉我\x01",
            "那件事的详情吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "嗯，当然没问题，\x01",
            "虽然我也不是很清楚。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2661")

    label("loc_259E")


    #C0130
    ChrTalk(
        0xA,
        (
            "……对了对了，\x01",
            "以前我跟哈缇娜修女一起到玛因兹\x01",
            "讲课的时候，发生了很夸张的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        (
            "有个名叫奇米的小女孩在听课时，\x01",
            "她爸爸因为太过担心，\x01",
            "居然偷偷跑进了课堂……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        "#04403F（有点离题了啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_2661")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_10_244D end

    def Function_11_266A(): pass

    label("Function_11_266A")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2733")

    #C0133
    ChrTalk(
        0xA,
        "塔米尔可真是的……！\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "居然偷偷钻到女性的裙子里，\x01",
            "这可是十分可耻的行为！\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xB,
        "嘿嘿，不好意思啦～\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        "今后我会尽量不做这种事的。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        "不、不是尽量，而是绝对不能再做！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27A5")

    label("loc_2733")


    #C0138
    ChrTalk(
        0xB,
        (
            "可是，修女啊……\x01",
            "有一句话我一直都很想说。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        (
            "你就不能把自己打扮得\x01",
            "稍微有魅力一点吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        "多、多管闲事！！\x02",
    )

    CloseMessageWindow()

    label("loc_27A5")

    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_266A end

    def Function_12_27AE(): pass

    label("Function_12_27AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2853")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CC")
    Call(0, 9)
    Jump("loc_284E")

    label("loc_27CC")


    #C0141
    ChrTalk(
        0xFE,
        (
            "啧，完全打乱了人家的计划。\x01",
            "明明是我们担心她，\x01",
            "结果她却哭起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "嘿嘿，算啦。\x01",
            "等她平静下来之后，\x01",
            "再拿这件事来取笑她吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_284E")

    Jump("loc_2C7D")

    label("loc_2853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2861")
    Jump("loc_2C7D")

    label("loc_2861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_28B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_287C")
    Call(0, 13)
    Jump("loc_28AF")

    label("loc_287C")


    #C0143
    ChrTalk(
        0xFE,
        (
            "既然连哈米尔都不明白，\x01",
            "我自然就更不明白了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28AF")

    Jump("loc_2C7D")

    label("loc_28B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_28C2")
    Jump("loc_2C7D")

    label("loc_28C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_28D0")
    Jump("loc_2C7D")

    label("loc_28D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_28DE")
    Jump("loc_2C7D")

    label("loc_28DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2904")

    #C0144
    ChrTalk(
        0xFE,
        "嘿嘿，我是谁呢～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_2904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_294A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_291F")
    Call(0, 14)
    Jump("loc_2945")

    label("loc_291F")


    #C0145
    ChrTalk(
        0xFE,
        "好吧，既然决定了，就要马上行动！\x02",
    )

    CloseMessageWindow()

    label("loc_2945")

    Jump("loc_2C7D")

    label("loc_294A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_2958")
    Jump("loc_2C7D")

    label("loc_2958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_2969")
    Call(0, 15)
    Jump("loc_2C7D")

    label("loc_2969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_29C5")

    #C0146
    ChrTalk(
        0xFE,
        (
            "今天是东街那些家伙来\x01",
            "这里上课啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "嘿嘿，干脆从那个窗口\x01",
            "偷看一下吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_29C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2AC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A5D")

    #C0148
    ChrTalk(
        0xFE,
        (
            "能分清我和哈米尔的人\x01",
            "非常少～\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "所以我偶尔也会冒充哈米尔\x01",
            "去做些恶作剧。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "不过，如果向妈妈出手，\x01",
            "立刻就会露陷呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2ABF")

    label("loc_2A5D")


    #C0151
    ChrTalk(
        0xFE,
        (
            "如果对妈妈恶作剧，\x01",
            "就算冒充成哈米尔，\x01",
            "也会立刻露陷呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "唔唔，她是不是有什么辨别方法呢？\x02",
    )

    CloseMessageWindow()

    label("loc_2ABF")

    Jump("loc_2C7D")

    label("loc_2AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B1D")

    #C0153
    ChrTalk(
        0xFE,
        (
            "那个叫兰花塔的建筑\x01",
            "真是好高大啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "老实说，让我觉得自己好渺小呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_2B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B2E")
    Call(0, 11)
    Jump("loc_2C7D")

    label("loc_2B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2B3C")
    Jump("loc_2C7D")

    label("loc_2B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2C20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BCD")

    #C0155
    ChrTalk(
        0xFE,
        (
            "刚才我试着去掀\x01",
            "那个新修女的\x01",
            "裙子……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "但她却用十分巧妙的\x01",
            "动作躲开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "唔唔唔……看来\x01",
            "不是个等闲之辈啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C1B")

    label("loc_2BCD")


    #C0158
    ChrTalk(
        0xFE,
        (
            "居然能躲过我的\x01",
            "掀裙子绝技……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "看来那个新来的修女\x01",
            "不是个等闲之辈啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C1B")

    Jump("loc_2C7D")

    label("loc_2C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_2C74")

    #C0160
    ChrTalk(
        0xFE,
        (
            "刚才看到了一个\x01",
            "新来的修女呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "嘿嘿，待会就去\x01",
            "捉弄捉弄她吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_2C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2C7D")

    label("loc_2C7D")

    TalkEnd(0xFE)
    Return()

    # Function_12_27AE end

    def Function_13_2C81(): pass

    label("Function_13_2C81")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0162
    ChrTalk(
        0xB,
        (
            "不知为何，大人们都在\x01",
            "议论纷纷呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "独立到底是\x01",
            "什么东西？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xB,
        (
            "哈米尔，你一向学习很好吧？\x01",
            "快给我讲讲。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xC,
        (
            "不、不可能啦。\x01",
            "我也不大明白呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_13_2C81 end

    def Function_14_2D37(): pass

    label("Function_14_2D37")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0166
    ChrTalk(
        0xB,
        (
            "……然后呢，如果修女发火了，\x01",
            "你就这么做……这样那样……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        (
            "咦咦，为什么连我都得\x01",
            "去干那种事啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "你就听我的嘛，我答应你，\x01",
            "不会把你前不久尿床的事告诉琪雅的！\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xC,
        "唔……既然你都这么说了……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_14_2D37 end

    def Function_15_2E14(): pass

    label("Function_15_2E14")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ECE")

    #C0170
    ChrTalk(
        0xB,
        (
            "连我们都被抓进\x01",
            "主日学校的教室听课了。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xB,
        (
            "唉……都怪哈米尔提议\x01",
            "偷看他们上课。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xC,
        (
            "不、不对啊，\x01",
            "明明是你提议的呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "别一脸无辜地推到我身上，\x01",
            "真是的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F51")

    label("loc_2ECE")


    #C0174
    ChrTalk(
        0xC,
        (
            "不过，这不也挺好的吗。\x01",
            "学到了好多东西，\x01",
            "等于是提前预习了功课呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "我跟你可不一样，我讨厌学习啊！\x01",
            "啧，真讨厌这种书呆子……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F51")

    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_15_2E14 end

    def Function_16_2F5A(): pass

    label("Function_16_2F5A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2FCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F78")
    Call(0, 9)
    Jump("loc_2FC6")

    label("loc_2F78")


    #C0176
    ChrTalk(
        0xFE,
        (
            "嗯，市内的孩子们\x01",
            "全都平安无事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "呵呵，修女，\x01",
            "谢谢你这么担心我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FC6")

    Jump("loc_362B")

    label("loc_2FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2FD9")
    Jump("loc_362B")

    label("loc_2FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3060")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF4")
    Call(0, 13)
    Jump("loc_305B")

    label("loc_2FF4")


    #C0178
    ChrTalk(
        0xFE,
        (
            "虽说我也不大明白\x01",
            "独立是怎么一回事……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "但从市里那些大人的\x01",
            "谈话来看，\x01",
            "应该是件很重要的事呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_305B")

    Jump("loc_362B")

    label("loc_3060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_306E")
    Jump("loc_362B")

    label("loc_306E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_307C")
    Jump("loc_362B")

    label("loc_307C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_308A")
    Jump("loc_362B")

    label("loc_308A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_30E3")

    #C0180
    ChrTalk(
        0xFE,
        (
            "呼……呼……\x01",
            "为、为什么连我也得干这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        "事后一定会挨骂的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_362B")

    label("loc_30E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_312C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30FE")
    Call(0, 14)
    Jump("loc_3127")

    label("loc_30FE")


    #C0182
    ChrTalk(
        0xFE,
        (
            "呜呜，没办法了……\x01",
            "就只有这一次哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3127")

    Jump("loc_362B")

    label("loc_312C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_313A")
    Jump("loc_362B")

    label("loc_313A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_314B")
    Call(0, 15)
    Jump("loc_362B")

    label("loc_314B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3188")

    #C0183
    ChrTalk(
        0xFE,
        (
            "不要啦……\x01",
            "如果修女发火了，我可不管你哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_362B")

    label("loc_3188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_326D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_321E")

    #C0184
    ChrTalk(
        0xFE,
        (
            "妈妈和爸爸都能\x01",
            "完美辨别我们\x01",
            "这对双胞胎呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "我们的脸几乎一模一样，\x01",
            "可他们一眼就能认出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "父母还真厉害呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3268")

    label("loc_321E")


    #C0187
    ChrTalk(
        0xFE,
        (
            "妈妈和爸爸只看一眼\x01",
            "就能完美辨别\x01",
            "我和塔米尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        "父母还真厉害呢……\x02",
    )

    CloseMessageWindow()

    label("loc_3268")

    Jump("loc_362B")

    label("loc_326D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32D7")

    #C0189
    ChrTalk(
        0xFE,
        (
            "唉……难得的机会，\x01",
            "我真想跟琪雅一起\x01",
            "观看揭幕式啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        "……啊！我、我什么都没说哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_362B")

    label("loc_32D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_33BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3360")

    #C0191
    ChrTalk(
        0xFE,
        (
            "塔米尔居然在捉迷藏的\x01",
            "时候躲进修女的\x01",
            "裙子里。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "唉……明知这么干\x01",
            "会惹怒修女，\x01",
            "为什么还非要那么做呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_33B7")

    label("loc_3360")


    #C0193
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "塔米尔被骂的时候，\x01",
            "连我都会感同身受呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "双胞胎还真是\x01",
            "吃亏啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B7")

    Jump("loc_362B")

    label("loc_33BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_33CA")
    Jump("loc_362B")

    label("loc_33CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_35C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_356D")
    TurnDirection(0xFE, 0x153, 0)

    #C0195
    ChrTalk(
        0xFE,
        (
            "啊！琪雅！\x01",
            "高年级班的授课结束了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x153,
        (
            "#01109F嗯，刚刚结束了～\x02\x03",

            "#01100F哈米尔，你从下课之后\x01",
            "一直玩到现在吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "嗯，是啊，\x01",
            "和塔米尔一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "话说回来，琪雅，\x01",
            "你已经能完美辨别出\x01",
            "我就是哈米尔了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x153,
        (
            "#01105F哎～这有什么奇怪？\x02\x03",

            "#01109F虽然你和塔米尔的样子一模一样，\x01",
            "可哈米尔就是哈米尔啊，当然能看出来～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0200
    ChrTalk(
        0xFE,
        "（哇，不知为何，总觉得好开心……！）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_35C1")

    label("loc_356D")

    TurnDirection(0xFE, 0x153, 0)

    #C0201
    ChrTalk(
        0xFE,
        "总之……回家的路上小心哦，琪雅。\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x153,
        "#01109F嗯，我们下次再一起玩哦～！\x02",
    )

    CloseMessageWindow()

    label("loc_35C1")

    Jump("loc_362B")

    label("loc_35C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_3622")

    #C0203
    ChrTalk(
        0xFE,
        (
            "不行啊，塔米尔……\x01",
            "如果她是个很凶的人怎么办。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "说不定会\x01",
            "对你发火呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_362B")

    label("loc_3622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_362B")

    label("loc_362B")

    TalkEnd(0xFE)
    Return()

    # Function_16_2F5A end

    def Function_17_362F(): pass

    label("Function_17_362F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3644")
    Call(0, 18)
    Jump("loc_369B")

    label("loc_3644")


    #C0205
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "既然琪雅都那么说了，\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "今后我就认认真真地\x01",
            "把作业做完吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_369B")

    TalkEnd(0xFE)
    Return()

    # Function_17_362F end

    def Function_18_369F(): pass

    label("Function_18_369F")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0207
    ChrTalk(
        0xD,
        (
            "被修女委婉地\x01",
            "训斥了一顿呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xE,
        (
            "因为你不做作业，\x01",
            "这完全是咎由自取吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xD,
        (
            "唉……以前明明挺宽松的呀，\x01",
            "升上高年级班以后，\x01",
            "就严厉了很多……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x153,
        (
            "#01105F今后要记得把\x01",
            "作业做完哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0xD, 0x153, 500)
    Sleep(500)

    #C0211
    ChrTalk(
        0xD,
        "知道啦……\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x101,
        "#00012F（真、真不愧是琪雅啊……）\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    TurnDirection(0xD, 0xE, 0)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_18_369F end

    def Function_19_37D1(): pass

    label("Function_19_37D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37E6")
    Call(0, 18)
    Jump("loc_3815")

    label("loc_37E6")


    #C0213
    ChrTalk(
        0xFE,
        (
            "哈哈，你在这孩子面前\x01",
            "也是完全没有办法啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3815")

    TalkEnd(0xFE)
    Return()

    # Function_19_37D1 end

    def Function_20_3819(): pass

    label("Function_20_3819")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3951")
    TurnDirection(0xFE, 0x153, 0)

    #C0214
    ChrTalk(
        0xFE,
        (
            "啊，小琪雅，\x01",
            "你要回家了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x153,
        "#01110F嗯！布利克，你也正要回家吗～？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "是啊，打算顺路\x01",
            "到西街买本\x01",
            "克洛斯贝尔时代周刊再回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "小琪雅……\x01",
            "下次上课时，我可不会再输了哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x153,
        "#01111F咦～我们之间有过比试吗～？\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0219
    ChrTalk(
        0xFE,
        (
            "没、没什么。\x01",
            "忘了我刚刚的话吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_39BE")

    label("loc_3951")


    #C0220
    ChrTalk(
        0xFE,
        (
            "看到小琪雅来我们\x01",
            "高年级班上课的时候，\x01",
            "我真是吃了一惊……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "不过，以此为契机，\x01",
            "我决定今后要认真学习。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BE")

    TalkEnd(0xFE)
    Return()

    # Function_20_3819 end

    def Function_21_39C2(): pass

    label("Function_21_39C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05900.itc", 0x1E)
    LoadChrToIndex("apl/ch51020.itc", 0x1F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    OP_11(0xA0, 0xDC, 0xDC, 0x3C, 0x64, 0x0)
    OP_68(13460, 3600, 9960, 0)
    MoveCamera(310, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31000, 0)
    OP_68(13460, 10600, 9960, 7500)
    SetChrPos(0x101, 0, 0, 2450, 0)
    SetChrPos(0x102, 1000, 0, 2100, 0)
    SetChrPos(0x103, -750, 0, 1900, 0)
    SetChrPos(0x104, 0, 0, 350, 0)
    SetChrPos(0x109, 1000, 0, 850, 0)
    SetChrPos(0x105, -1000, 0, 150, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    SetChrPos(0x10, 70, 2000, 28890, 180)
    FadeToBright(1000, 0)

    def lambda_3B09():
        OP_9B(0x0, 0x101, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3B09)
    Sleep(100)

    def lambda_3B21():
        OP_9B(0x0, 0x102, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3B21)
    Sleep(100)

    def lambda_3B39():
        OP_9B(0x0, 0x103, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3B39)
    Sleep(100)

    def lambda_3B51():
        OP_9B(0x0, 0x104, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3B51)
    Sleep(100)

    def lambda_3B69():
        OP_9B(0x0, 0x109, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3B69)
    Sleep(100)

    def lambda_3B81():
        OP_9B(0x0, 0x105, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3B81)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_11(0xA0, 0xDC, 0xDC, 0x3C, 0x64, 0x0)
    OP_68(0, 900, 16750, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18880, 0)
    SetCameraDistance(18380, 1500)
    OP_0D()
    OP_6F(0x79)

    def lambda_3C00():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C00)
    Sleep(50)

    def lambda_3C10():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C10)
    Sleep(50)

    def lambda_3C20():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3C20)
    Sleep(50)

    def lambda_3C30():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3C30)
    Sleep(50)

    def lambda_3C40():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3C40)
    Sleep(50)

    def lambda_3C50():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C50)
    Sleep(50)

    def lambda_3C60():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3C60)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 2)

    #C0222
    ChrTalk(
        0x101,
        (
            "#00003F#11P……天已经快黑了。\x02\x03",

            "#00001F我想今天就把报告书交上去，\x01",
            "得想办法收集些情报才行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x102,
        (
            "#00108F#12P是啊……\x01",
            "真希望能找到什么线索。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3D95")

    #C0224
    ChrTalk(
        0x103,
        (
            "#00200F总之，\x01",
            "我们先去拜访一下莉丝修女\x01",
            "或玛布尔老师吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#00000F#11P嗯，先到主日学校的\x01",
            "教室去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DFB")

    label("loc_3D95")


    #C0226
    ChrTalk(
        0x103,
        (
            "#00200F总之，我们先去\x01",
            "拜访一下玛布尔老师吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#00000F#11P嗯，希望她现在\x01",
            "没在主日学校授课……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DFB")

    ClearChrFlags(0x10, 0x80)

    #N0228
    NpcTalk(
        0x10,
        "男性的声音",
        "哦，是你们啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_3E9B():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E9B)
    Sleep(0)

    def lambda_3EAB():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3EAB)
    Sleep(0)

    def lambda_3EBB():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3EBB)
    Sleep(0)

    def lambda_3ECB():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3ECB)
    Sleep(0)

    def lambda_3EDB():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3EDB)
    Sleep(0)

    def lambda_3EEB():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3EEB)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_68(-30, 1100, 18180, 3000)
    MoveCamera(318, 18, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(18330, 3000)
    OP_9B(0x0, 0x10, 0x0, 0x1F40, 0x7D0, 0x0)
    OP_6F(0x79)

    #C0229
    ChrTalk(
        0x101,
        "#00005F#6P伊安律师……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 1)), scpexpr(EXPR_END)), "loc_4193")

    #C0230
    ChrTalk(
        0x102,
        "#00104F#6P好久不见了。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0231
    AnonymousTalk(
        0x10,
        (
            "是啊，上次见面还是在通商会议时呢。\x02\x03",

            "啊，对了，你们白天\x01",
            "来过我的事务所吧？\x02\x03",

            "不好意思啊，\x01",
            "让你们白跑了一趟。\x02",
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

    #C0232
    ChrTalk(
        0x101,
        (
            "#00012F#6P哪里……\x01",
            "话说回来，您好像很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x109,
        (
            "#10100F#6P听说您正在协助政府\x01",
            "拟定宪法草案？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x10,
        (
            "#02210F#11P这个嘛……哈哈……\x02\x03",

            "市长十分热情地拜托我帮忙，\x01",
            "我也不好拒绝啊。\x02\x03",

            "#02200F不过，就我个人来说，\x01",
            "也是十分赞成他这个想法的。\x02\x03",

            "要想实现，肯定困难重重……\x01",
            "但我还是想为此略尽绵力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_456A")

    label("loc_4193")


    #C0235
    ChrTalk(
        0x102,
        (
            "#00104F#6P好久不见了。\x02\x03",

            "#00108F听说您最近\x01",
            "相当忙啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0236
    ChrTalk(
        0x101,
        "#00005F#5P咦，是吗？\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0237
    AnonymousTalk(
        0x10,
        (
            "这个嘛……哈哈……\x02\x03",

            "……其实是市长请我协助政府\x01",
            "拟定有关独立的宪法草案。\x02",
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
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)

    #C0238
    ChrTalk(
        0x101,
        "#00007F#6P什么！？\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x109,
        (
            "#10101F#6P是『宪法』……\x01",
            "而不是自治州法吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0240
    ChrTalk(
        0x102,
        (
            "#00104F#11P所谓的『宪法』，\x01",
            "是以主权国家为基本前提\x01",
            "而制定的根本法。\x02\x03",

            "#00100F它是决定国家统治权、政治结构，\x01",
            "以及各种重要原则问题的最高法律，\x01",
            "不容别国干涉。\x02\x03",

            "如果想以国家的形式独立，\x01",
            "宪法绝对必不可少。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x104,
        (
            "#00305F#6P呼……\x01",
            "又是个复杂的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        (
            "#00204F#6P说起来，伊安律师\x01",
            "似乎正是最合适的人选……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x10,
        (
            "#02210F#11P哈哈……\x01",
            "市长十分热情地拜托我帮忙，\x01",
            "我也不好拒绝啊。\x02\x03",

            "#02200F不过，就我个人来说，\x01",
            "也是十分赞成他这个想法的。\x02\x03",

            "要想实现，肯定困难重重……\x01",
            "但我还是想为此略尽绵力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_456A")


    def lambda_456F():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_456F)

    #C0244
    ChrTalk(
        0x101,
        "#00002F#6P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x105,
        (
            "#10302F#6P莫非您是想忙中偷闲，\x01",
            "所以来这里祈祷吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x10,
        (
            "#02210F#11P是啊，在工作中遇到了瓶颈。\x01",
            "但来这里一趟之后，已经把心情调整好了。\x02\x03",

            "#02202F在遇到困难的时候，\x01",
            "向女神祈祷一下也是个不错的选择呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x104,
        (
            "#00309F#6P哈哈……\x01",
            "确实如此。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        "#00104F#6P您真是辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x10,
        (
            "#02210F#11P哈哈，你们才辛苦呢。\x02\x03",

            "#02200F天都快黑了……\x01",
            "你们难道是为工作而来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#00000F#6P是的，有点问题想\x01",
            "请教一下教会的人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x10,
        (
            "#02203F#11P唔，听起来，好像有什么隐情啊。\x02\x03",

            "#02200F虽然我现在很忙……\x01",
            "但如果有什么需要帮忙的事情，\x01",
            "请不要客气，随时来事务所找我吧。\x02\x03",

            "我十分欢迎你们来访。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        "#00004F#6P谢谢您了。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    OP_0D()

    #C0253
    ChrTalk(
        0x109,
        "#10100F#6P回去的路上请多加小心！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()

    def lambda_482C():

        label("loc_482C")

        TurnDirection(0x101, 0x10, 500)
        Yield()
        Jump("loc_482C")

    QueueWorkItem2(0x101, 2, lambda_482C)

    def lambda_483E():

        label("loc_483E")

        TurnDirection(0x102, 0x10, 500)
        Yield()
        Jump("loc_483E")

    QueueWorkItem2(0x102, 2, lambda_483E)

    def lambda_4850():

        label("loc_4850")

        TurnDirection(0x103, 0x10, 500)
        Yield()
        Jump("loc_4850")

    QueueWorkItem2(0x103, 2, lambda_4850)

    def lambda_4862():

        label("loc_4862")

        TurnDirection(0x104, 0x10, 500)
        Yield()
        Jump("loc_4862")

    QueueWorkItem2(0x104, 2, lambda_4862)

    def lambda_4874():

        label("loc_4874")

        TurnDirection(0x109, 0x10, 500)
        Yield()
        Jump("loc_4874")

    QueueWorkItem2(0x109, 2, lambda_4874)

    def lambda_4886():

        label("loc_4886")

        TurnDirection(0x105, 0x10, 500)
        Yield()
        Jump("loc_4886")

    QueueWorkItem2(0x105, 2, lambda_4886)
    OP_9B(0x0, 0x10, 0x13B, 0xBB8, 0x8FC, 0x1)
    OP_68(-670, 900, 16640, 3000)
    MoveCamera(315, 23, 0, 3000)
    OP_9B(0x0, 0x10, 0x32, 0x2710, 0x9C4, 0x0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x10, 0x80)
    OP_6F(0x79)
    Sleep(1000)

    #C0254
    ChrTalk(
        0x101,
        "#00001F#11P……看来他很忙呢。\x02",
    )

    CloseMessageWindow()

    def lambda_4917():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4917)
    Sleep(0)

    def lambda_4927():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4927)
    Sleep(0)

    def lambda_4937():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4937)
    Sleep(0)

    def lambda_4947():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4947)
    Sleep(0)

    def lambda_4957():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4957)
    Sleep(0)

    def lambda_4967():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4967)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0255
    ChrTalk(
        0x102,
        (
            "#00103F#12P是啊，既然是宪法草案，\x01",
            "要求肯定相当高……\x02\x03",

            "#00101F如果草率制定法案，在对外发表之后，\x01",
            "肯定会被帝国、共和国等势力横加指责，\x01",
            "遭到不具备说服力之类的批评……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x104,
        "#00306F#6P唉……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x105,
        (
            "#10304F#6P呵呵，与我们的忙碌相比，\x01",
            "他似乎更加操心劳神呢。\x02\x03",

            "#10300F先不说这个了……\x01",
            "我们不是要去主日学校的教室吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        "#00000F#11P嗯，这就去看看吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrPos(0x0, 0, 0, 17450, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    OP_CC(0x1, 0xFF, 0x0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x161, 5)
    OP_29(0xA6, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_21_39C2 end

    def Function_22_4B33(): pass

    label("Function_22_4B33")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-8010, 1550, 13580, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17850, 0)
    SetChrPos(0x101, -7750, 250, 14000, 270)
    SetChrPos(0x102, -8000, 250, 15050, 225)
    SetChrPos(0x103, -7900, 250, 12900, 315)
    SetChrPos(0x104, -6850, 0, 14900, 225)
    SetChrPos(0x109, -6750, 0, 12450, 315)
    SetChrPos(0x105, -6250, 0, 13500, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0259
    ChrTalk(
        0x8,
        (
            "#04403F#5P……请随我进来。\x02\x03",

            "#04400F因为我不想被\x01",
            "其他人看到。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        "#00001F#12P哦……\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x102,
        "#00103F#12P……那就打扰了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sound(121, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)

    def lambda_4CA4():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4CA4)
    OP_9B(0x0, 0x8, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0x8, 3)

    def lambda_4CC8():
        OP_95(0x102, -11400, 500, 14750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4CC8)
    Sleep(200)

    def lambda_4CE5():
        OP_95(0x103, -11400, 500, 13250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4CE5)
    Sleep(100)

    def lambda_4D02():
        OP_95(0x101, -11400, 500, 14000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D02)
    Sleep(100)

    def lambda_4D1F():
        OP_95(0x104, -11400, 500, 14750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4D1F)
    Sleep(100)

    def lambda_4D3C():
        OP_95(0x109, -11400, 500, 13250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4D3C)
    Sleep(200)

    def lambda_4D59():
        OP_95(0x105, -11400, 500, 14000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4D59)
    Sleep(500)
    FadeToDark(1000, 0, -1)

    def lambda_4D80():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_4D80)
    Sleep(50)

    def lambda_4D94():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_4D94)
    Sleep(50)

    def lambda_4DA8():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4DA8)
    Sleep(150)

    def lambda_4DBC():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_4DBC)
    Sleep(50)

    def lambda_4DD0():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4DD0)
    Sleep(50)

    def lambda_4DE4():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_4DE4)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t4030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_4B33 end

    def Function_23_4E34(): pass

    label("Function_23_4E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FDC")

    #C0262
    ChrTalk(
        0xA,
        "今天是弥撒日。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xA,
        (
            "各位要不要一起来\x01",
            "参加呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#00003F（不知道她肯不肯担任职业女性\x01",
            "  选秀活动中的『修女』……）\x02\x03",

            "#00000F那个，不好意思。\x01",
            "有点事情想和你商量……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0265
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人邀请对方参加\x01",
            "慈善宴会中的职业女性选秀活动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0266
    ChrTalk(
        0xA,
        (
            "咦、咦咦……？\x01",
            "让我去参加选秀活动……？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xA,
        (
            "不、不可能啦～\x01",
            "像我这样的人，\x01",
            "真的毫无魅力可言……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xA,
        (
            "不好意思，请各位\x01",
            "去邀请其他人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        "#00012F这、这样啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 1)
    Jump("loc_5036")

    label("loc_4FDC")


    #C0270
    ChrTalk(
        0xA,
        (
            "让、让我去参加选秀活动，\x01",
            "实在是太强人所难了。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xA,
        (
            "你们一定能找到\x01",
            "比我更合适的人选。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5036")

    TalkEnd(0xA)
    Return()

    # Function_23_4E34 end

    def Function_24_503A(): pass

    label("Function_24_503A")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0272
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～克洛斯贝尔大圣堂宿舍～\x01",
            "　　　参拜者请前往\x01",
            "　　　　礼拜堂。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_24_503A end

    def Function_25_50B2(): pass

    label("Function_25_50B2")

    EventBegin(0x1)

    #C0273
    ChrTalk(
        0x101,
        (
            "#00001F……总之，\x01",
            "我们先去找莉丝小姐吧。\x01",
            "说不定能得到什么情报。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 370, 0, -7350, 0)
    EventEnd(0x4)
    Return()

    # Function_25_50B2 end

    SaveToFile()

Try(main)
