from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "シスター・リース",       # 1
        "ロランド司祭",           # 2
        "シスター・ジュジュ",     # 3
        "タミル",                 # 4
        "ハミル",                 # 5
        "プルーナ",               # 6
        "リナリー",               # 7
        "ブリック",               # 8
        "イアン弁護士",           # 9
        "マインツ山道",           # 10
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

    PlaceName(5.0, -0.0, -35.0, 0x0000, 0x0000, "マインツ山道")

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
        "Function_8_1CCC",         # 08, 8
        "Function_9_2999",         # 09, 9
        "Function_10_2A9B",        # 0A, 10
        "Function_11_2D36",        # 0B, 11
        "Function_12_2EC6",        # 0C, 12
        "Function_13_34B3",        # 0D, 13
        "Function_14_3595",        # 0E, 14
        "Function_15_368A",        # 0F, 15
        "Function_16_3814",        # 10, 16
        "Function_17_4017",        # 11, 17
        "Function_18_4093",        # 12, 18
        "Function_19_420D",        # 13, 19
        "Function_20_4257",        # 14, 20
        "Function_21_443C",        # 15, 21
        "Function_22_56F3",        # 16, 22
        "Function_23_5A12",        # 17, 23
        "Function_24_5C54",        # 18, 24
        "Function_25_5CD6",        # 19, 25
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9C")

    #C0001
    ChrTalk(
        0xFE,
        (
            "あの青白く光る大樹は、\x01",
            "どんな因果でクロスベルに\x01",
            "現れたのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "この地に光をもたらすか、\x01",
            "あるいは災いをもたらすのか……\x01",
            "我々聖職者にも計り知れません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AEA")

    label("loc_A9C")


    #C0003
    ChrTalk(
        0xFE,
        "あの青白く光る大樹は、一体……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "これも女神の思し召しなのでしょうか。\x02",
    )

    CloseMessageWindow()

    label("loc_AEA")

    Jump("loc_1CC8")

    label("loc_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA6")

    #C0005
    ChrTalk(
        0xFE,
        (
            "突如、結界が消えたと思えば、\x01",
            "街では甲冑姿の化物が\x01",
            "徘徊を始めたそうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "これもディーター大統領の\x01",
            "意向だとしたら、\x01",
            "絶対に許されない行いです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BE5")

    label("loc_BA6")


    #C0007
    ChrTalk(
        0xFE,
        (
            "街に化物を徘徊させるなんて……\x01",
            "絶対に許されない行いです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE5")

    Jump("loc_1CC8")

    label("loc_BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC4")

    #C0008
    ChrTalk(
        0xFE,
        (
            "ディーター殿によるの演説が\x01",
            "街で行われたそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "クロスベルが独立することで、\x01",
            "大陸に混乱が訪れることは\x01",
            "避けられないのではないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "女神よ、どうか人々を導きたまえ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D27")

    label("loc_CC4")


    #C0011
    ChrTalk(
        0xFE,
        (
            "もはや、帝国や共和国との\x01",
            "衝突は避けられないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "女神よ、どうか人々を導きたまえ……\x02",
    )

    CloseMessageWindow()

    label("loc_D27")

    Jump("loc_1CC8")

    label("loc_D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E08")

    #C0013
    ChrTalk(
        0xFE,
        (
            "本日は、大聖堂内の礼拝堂にて\x01",
            "ミサを行っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "襲撃事件の犠牲になった方々に\x01",
            "女神の導きがあらんことを願う催しです。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "お時間がよろしければ、\x01",
            "皆様も是非ご参加なさってください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E94")

    label("loc_E08")


    #C0016
    ChrTalk(
        0xFE,
        (
            "先の襲撃事件を悼んで、\x01",
            "本日のミサには\x01",
            "多くの参拝客が訪れております。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "お時間がよろしければ、\x01",
            "皆様も是非ご参加なさってください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E94")

    Jump("loc_1CC8")

    label("loc_E99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_FB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F37")

    #C0018
    ChrTalk(
        0xFE,
        (
            "昨晩から、銃声や爆発音などが\x01",
            "頻繁に聞こえてくるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "マインツ方面の戦闘は\x01",
            "かなり激しいものに\x01",
            "なっているようですね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FB4")

    label("loc_F37")


    #C0020
    ChrTalk(
        0xFE,
        (
            "ともかく……\x01",
            "万一、武装集団がここまで\x01",
            "降りてこないとも限りません。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "大聖堂の守りについても\x01",
            "早急に検討しなくては……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB4")

    Jump("loc_1CC8")

    label("loc_FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1035")

    #C0022
    ChrTalk(
        0xFE,
        (
            "今日はクロスベル自治州全域で\x01",
            "雨が降っているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "さすがに街道まで出歩く人は\x01",
            "少ないようですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_1035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_10BA")

    #C0024
    ChrTalk(
        0xFE,
        (
            "はは……\x01",
            "シスター・ジュジュは\x01",
            "本当に子供に好かれていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "あれは一種の才能ですよ。\x01",
            "うらやましいものです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_10BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_120A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1195")

    #C0026
    ChrTalk(
        0xFE,
        (
            "ローゼンベルク工房……\x01",
            "時々聞く名前ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "かなり前からある工房ですが、\x01",
            "あそこの主が大聖堂を訪れることは\x01",
            "なかったように思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "一体どのような人が\x01",
            "いらっしゃるのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1205")

    label("loc_1195")


    #C0029
    ChrTalk(
        0xFE,
        (
            "ローゼンベルク工房の主が\x01",
            "大聖堂を訪れた事はありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "一体どのような人が\x01",
            "いらっしゃるのでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1205")

    Jump("loc_1CC8")

    label("loc_120A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_1280")

    #C0031
    ChrTalk(
        0xFE,
        (
            "タミルくんとハミルくんは\x01",
            "お家に帰ったようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "さてと、そろそろ\x01",
            "夕方の掃除を始めないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_1280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_1404")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1374")

    #C0033
    ChrTalk(
        0xFE,
        (
            "イアン殿は、たまにああして\x01",
            "大聖堂に顔を出されるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "特に難しい案件を\x01",
            "取り扱っているときなどは、\x01",
            "よくいらしているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "今はどのようなことに\x01",
            "お悩みかは存じませんが……\x01",
            "頑張ってほしいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FF")

    label("loc_1374")


    #C0036
    ChrTalk(
        0xFE,
        (
            "イアン殿は、たまにああして\x01",
            "大聖堂に顔を出されるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "今はどのようなことに\x01",
            "お悩みかは存じませんが……\x01",
            "頑張ってほしいものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FF")

    Jump("loc_1CC8")

    label("loc_1404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_154E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CA")

    #C0038
    ChrTalk(
        0xFE,
        (
            "近頃、各地で得体の知れない化物が\x01",
            "目撃されているとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "警備隊も、人里外れた場所に\x01",
            "１人で入らないよう\x01",
            "呼びかけているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "皆様も充分お気をつけください。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1549")

    label("loc_14CA")


    #C0041
    ChrTalk(
        0xFE,
        (
            "近頃、各地で\x01",
            "得体の知れない化物が\x01",
            "目撃されているとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "人里外れた場所に入らないよう、\x01",
            "皆様も充分お気をつけください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1549")

    Jump("loc_1CC8")

    label("loc_154E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_168F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15FF")

    #C0043
    ChrTalk(
        0xFE,
        (
            "先ほど、リベールの\x01",
            "クローディア王太女殿下が\x01",
            "大聖堂にいらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "エラルダ大司教にご挨拶されてから、\x01",
            "墓地のほうに向かわれたようですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_168A")

    label("loc_15FF")


    #C0045
    ChrTalk(
        0xFE,
        (
            "クローディア王太女殿下は\x01",
            "先ほどオルキスタワーへと\x01",
            "向かわれたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "今日の本会議の行方……\x01",
            "殿下の動向も気になるところですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_168A")

    Jump("loc_1CC8")

    label("loc_168F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1802")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1785")

    #C0047
    ChrTalk(
        0xFE,
        (
            "除幕式の様子は、\x01",
            "高台にあるここからでも\x01",
            "見ることができたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "ヴェールを脱いだオルキスタワーは、\x01",
            "まさに圧巻の一言でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "あれほどの建造物が\x01",
            "人の手で作られたとは……\x01",
            "いやはや、驚きを隠せませんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17FD")

    label("loc_1785")


    #C0050
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの姿は、\x01",
            "まさに圧巻の一言でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "あれが人の手で作られたとは……\x01",
            "いやはや、驚きを隠せませんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FD")

    Jump("loc_1CC8")

    label("loc_1802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_187E")

    #C0052
    ChrTalk(
        0xFE,
        (
            "通商会議のため、\x01",
            "街では警備が強化されているとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "私も大聖堂の見回りを\x01",
            "気をつけていこうと思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_187E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_19F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195B")

    #C0054
    ChrTalk(
        0xFE,
        "今日は生憎の天気となりましたね。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "ただ、雨なのは市街地のみらしく、\x01",
            "マインツ山道方面まで行けば\x01",
            "さわやかな晴れ模様なんだとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "天候とは単なる、\x01",
            "女神の気まぐれなのかも\x01",
            "しれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19F1")

    label("loc_195B")


    #C0057
    ChrTalk(
        0xFE,
        (
            "雨なのは市街地のみらしく、\x01",
            "マインツ山道方面まで行けば\x01",
            "さわやかな晴れ模様なんだとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "天候とは単なる、\x01",
            "女神の気まぐれなのかも\x01",
            "しれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F1")

    Jump("loc_1CC8")

    label("loc_19F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_1AFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA3")

    #C0059
    ChrTalk(
        0xFE,
        (
            "おや……\x01",
            "そろそろお帰りでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "またいつでもお越しください。\x01",
            "明日も皆様に\x01",
            "女神の加護があらんことを……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x153,
        "#01109Fうん、またねー！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AFA")

    label("loc_1AA3")


    #C0062
    ChrTalk(
        0xFE,
        "日も暮れて薄暗くなってきています。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "階段を下りる時は、\x01",
            "足元にご注意ください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AFA")

    Jump("loc_1CC8")

    label("loc_1AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1B93")

    #C0064
    ChrTalk(
        0xFE,
        (
            "本日赴任を予定されていたシスターが\x01",
            "先ほど、お見えになったようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "今頃はエラルダ大司教に\x01",
            "ご挨拶なさっている所でしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_1B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1CC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4D")

    #C0066
    ChrTalk(
        0xFE,
        "クロスベル大聖堂へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "ここでは、クロスベル教区の長\x01",
            "エラルダ大司教が\x01",
            "七耀の教えを説いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "敷地内ではどうか、\x01",
            "お静かにお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CC8")

    label("loc_1C4D")


    #C0069
    ChrTalk(
        0xFE,
        (
            "ここクロスベル大聖堂では、\x01",
            "エラルダ大司教が\x01",
            "七耀の教えを説いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "敷地内ではどうか、\x01",
            "お静かにお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC8")

    TalkEnd(0xFE)
    Return()

    # Function_7_9D8 end

    def Function_8_1CCC(): pass

    label("Function_8_1CCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CEA")
    Call(0, 9)
    Jump("loc_1D4E")

    label("loc_1CEA")


    #C0071
    ChrTalk(
        0xFE,
        (
            "それじゃあ、クータくんや\x01",
            "ユゴットくんたちも\x01",
            "怪我はないんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "はあ、本当によかった……\x02",
    )

    CloseMessageWindow()

    label("loc_1D4E")

    Jump("loc_2995")

    label("loc_1D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1DAB")

    #C0073
    ChrTalk(
        0xFE,
        "街の子供たちは無事でしょうか……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "タミル君、ハミル君、みんな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2995")

    label("loc_1DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1EE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E75")

    #C0075
    ChrTalk(
        0xFE,
        (
            "一番大事なのは、\x01",
            "子供たちの未来なんだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "独立は、それらを守るもの……？\x01",
            "それとも脅かすものなのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "私には分からなくなってきて\x01",
            "しまいました……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EE4")

    label("loc_1E75")


    #C0078
    ChrTalk(
        0xFE,
        (
            "独立することで、\x01",
            "子供たちの未来は\x01",
            "どうなるのでしょう……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "私には分からなくなってきて\x01",
            "しまいました……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE4")

    Jump("loc_2995")

    label("loc_1EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_201E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F1B")
    Call(0, 23)
    Return()

    label("loc_1F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8C")

    #C0080
    ChrTalk(
        0xFE,
        (
            "ミサに来たお子様には\x01",
            "クッキーをさしあげています。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "よろしければ参加なさってください。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2019")

    label("loc_1F8C")


    #C0082
    ChrTalk(
        0xFE,
        (
            "やっぱり、あの襲撃事件で\x01",
            "今の平和に不安を感じた方は\x01",
            "かなりいるみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "もう二度と、あんなことが\x01",
            "起きなければいいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2019")

    Jump("loc_2995")

    label("loc_201E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_20D8")

    #C0084
    ChrTalk(
        0xFE,
        (
            "今日はタミルくんとハミルくんが\x01",
            "遊びに来ていたのですが、\x01",
            "すぐにお家に帰しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "あんな事件が起きている最中です、\x01",
            "お家にいたほうが親御さんも\x01",
            "安心できるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2995")

    label("loc_20D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_20E6")
    Jump("loc_2995")

    label("loc_20E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_21FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218E")

    #C0086
    ChrTalk(
        0xFE,
        "と、止まりなさいあなたたち！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "私のスカートをめくった、\x01",
            "悪いタミルくんはどっちです！？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xB,
        "へへ、どっちかな～☆\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        "はあ、はあ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21F8")

    label("loc_218E")


    #C0090
    ChrTalk(
        0xFE,
        (
            "え、えーとえーと……\x01",
            "こ、こっちがタミルくんです？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "あれ、でも、やっぱり……\x01",
            "こっちはハミルくん？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F8")

    Jump("loc_2995")

    label("loc_21FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_23CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_232E")

    #C0092
    ChrTalk(
        0xFE,
        (
            "昨日、シスター・マーブルに\x01",
            "授業のやり方を教えてもらって\x01",
            "気づいたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "子供って、興味のある事かどうかで\x01",
            "全然やる気が違うんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "何かを教えるためには、\x01",
            "それに興味をもってもらうのが\x01",
            "一番大事なんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "……まあ、そもそも\x01",
            "それが一番難しいんですけれど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23C5")

    label("loc_232E")


    #C0096
    ChrTalk(
        0xFE,
        (
            "日曜学校の授業の仕方を\x01",
            "教えてもらったりして、\x01",
            "少しは成長できたと思ってましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "一人前のシスターになるには、\x01",
            "まだまだ修行が足りませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C5")

    Jump("loc_2995")

    label("loc_23CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_23D8")
    Jump("loc_2995")

    label("loc_23D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_23E6")
    Jump("loc_2995")

    label("loc_23E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_23F4")
    Jump("loc_2995")

    label("loc_23F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_254B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B6")

    #C0098
    ChrTalk(
        0xFE,
        (
            "クローディア姫を護衛していた\x01",
            "ユリア准佐という方……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "間近で見ると噂どおり、\x01",
            "キリリとした方でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "ふふ、女性の方々が騒ぐのも\x01",
            "なんだか分かる気がします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2546")

    label("loc_24B6")


    #C0101
    ChrTalk(
        0xFE,
        (
            "ユリア准佐は、お忙しくても\x01",
            "教会に通うのは欠かさない\x01",
            "敬虔な方なのだとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "ふふ、意外と修道服も\x01",
            "似合っちゃったり\x01",
            "するかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2546")

    Jump("loc_2995")

    label("loc_254B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_255C")
    Call(0, 10)
    Jump("loc_2995")

    label("loc_255C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_256D")
    Call(0, 11)
    Jump("loc_2995")

    label("loc_256D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_257B")
    Jump("loc_2995")

    label("loc_257B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2700")
    TurnDirection(0xFE, 0x153, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2674")

    #C0103
    ChrTalk(
        0xFE,
        (
            "あ、キーアちゃん。\x01",
            "今日はもう帰るんです？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x153,
        (
            "#01100Fうん！　ロイドたちが\x01",
            "迎えに来てくれたんだー。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        "ふふ、それはよかったです。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "それじゃあ、\x01",
            "また次の授業の日にね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x153,
        "#01109Fうん、ばいばいシスター！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26FB")

    label("loc_2674")


    #C0108
    ChrTalk(
        0xFE,
        (
            "キーアちゃん、\x01",
            "また次の授業の日にね。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "今度また、みんなに\x01",
            "クッキーを焼いてあげますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x153,
        "#01109Fうん、楽しみにしてるね！\x02",
    )

    CloseMessageWindow()

    label("loc_26FB")

    Jump("loc_2995")

    label("loc_2700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_284A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D5")

    #C0111
    ChrTalk(
        0xFE,
        (
            "今、礼拝堂に入っていったのが\x01",
            "新入りのシスターでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "私、ここに勤めて\x01",
            "１年も経ってない新米なんですが、\x01",
            "ついに私にも後輩が……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "な、なんだか\x01",
            "どきどきしてきました……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2845")

    label("loc_27D5")


    #C0114
    ChrTalk(
        0xFE,
        (
            "いよいよ私にも後輩が……\x01",
            "どきどきしてきました……！\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "先輩らしく、いろいろな事を\x01",
            "教えてあげませんとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2845")

    Jump("loc_2995")

    label("loc_284A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2995")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2913")

    #C0116
    ChrTalk(
        0xFE,
        (
            "あら、こんにちは。\x01",
            "今日は日曜学校の授業が\x01",
            "行われていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "……もしかして、\x01",
            "子供たちの保護者の方です？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "授業をやっている講堂は\x01",
            "礼拝堂に入って右の部屋ですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2995")

    label("loc_2913")


    #C0119
    ChrTalk(
        0xFE,
        (
            "日曜学校の授業をやっている講堂は\x01",
            "礼拝堂に入って右の部屋ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "ふふ、よかったら授業の様子を\x01",
            "覗いてみてはいかがですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2995")

    TalkEnd(0xFE)
    Return()

    # Function_8_1CCC end

    def Function_9_2999(): pass

    label("Function_9_2999")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0121
    ChrTalk(
        0xA,
        (
            "タミル君、ハミル君、\x01",
            "本当に無事でよかった……！\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        (
            "くすん……ああ、女神様。\x01",
            "お慈悲に感謝いたします……！\x02",
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
            "ちょ、ちょっとシスター、\x01",
            "そんな泣かなくてもさぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xC,
        "ふふ、ありがとうシスター。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_9_2999 end

    def Function_10_2A9B(): pass

    label("Function_10_2A9B")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C56")

    #C0125
    ChrTalk(
        0x8,
        (
            "#04400Fシスター・ジュジュ。\x01",
            "明日出張するマインツ方面について\x01",
            "気になる話を聞いたのですが……\x02\x03",

            "#04403F少し前に、あのあたりで\x01",
            "奇妙な事件があったとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "ああ、そういえば確か\x01",
            "そんな話がありましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "マインツ方面の旧い遺跡で、\x01",
            "幽霊のようなものが目撃された\x01",
            "とかいう話だったような。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "#04401F……その話、もう少し詳しく\x01",
            "聞かせてもらってもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "ええ、いいですよ。\x01",
            "私はあまり詳しくないですけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D2D")

    label("loc_2C56")


    #C0130
    ChrTalk(
        0xA,
        (
            "……そうそう、\x01",
            "以前にシスター・ハティナと一緒に\x01",
            "マインツに行った時は大変でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        (
            "キミィちゃんという女の子の\x01",
            "お父さんが、授業が気になったのか\x01",
            "乗り込んできちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        "#04403F（ちょっと脱線してる……）\x02",
    )

    CloseMessageWindow()

    label("loc_2D2D")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_10_2A9B end

    def Function_11_2D36(): pass

    label("Function_11_2D36")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E23")

    #C0133
    ChrTalk(
        0xA,
        "もう、タミル君ったら……！\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "女性のスカートの中に潜り込むなんて、\x01",
            "ハレンチ極まりない行いですよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xB,
        "てへへ、ごめんな～。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        "もうなるべくしないようにするよ。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        "な、なるべくじゃなくて絶対ですッ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EBD")

    label("loc_2E23")


    #C0138
    ChrTalk(
        0xB,
        (
            "でもシスターさあ……\x01",
            "いっこだけ言っときたいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        (
            "もうちょっとイロケがあるのを\x01",
            "はいたほうがいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        "よ、余計なお世話ですッ！！\x02",
    )

    CloseMessageWindow()

    label("loc_2EBD")

    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_2D36 end

    def Function_12_2EC6(): pass

    label("Function_12_2EC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE4")
    Call(0, 9)
    Jump("loc_2F8C")

    label("loc_2EE4")


    #C0141
    ChrTalk(
        0xFE,
        (
            "ちぇっ、調子狂うなあ。\x01",
            "心配したのはこっちなのに、\x01",
            "イキナリ泣いちゃったりしてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "へへ、まあいいや。\x01",
            "こんどほとぼりが冷めたころに\x01",
            "からかうネタにしてやろっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8C")

    Jump("loc_34AF")

    label("loc_2F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F9F")
    Jump("loc_34AF")

    label("loc_2F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FBA")
    Call(0, 13)
    Jump("loc_2FF3")

    label("loc_2FBA")


    #C0143
    ChrTalk(
        0xFE,
        (
            "ハミルに分からねえんじゃ、\x01",
            "俺にも分からねえなあ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF3")

    Jump("loc_34AF")

    label("loc_2FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3006")
    Jump("loc_34AF")

    label("loc_3006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3014")
    Jump("loc_34AF")

    label("loc_3014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3022")
    Jump("loc_34AF")

    label("loc_3022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3052")

    #C0144
    ChrTalk(
        0xFE,
        "へへっ、どっちがど～っちだ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_3052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3096")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306D")
    Call(0, 14)
    Jump("loc_3091")

    label("loc_306D")


    #C0145
    ChrTalk(
        0xFE,
        "よーし、そんじゃ早速決行だぜ！\x02",
    )

    CloseMessageWindow()

    label("loc_3091")

    Jump("loc_34AF")

    label("loc_3096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_30A4")
    Jump("loc_34AF")

    label("loc_30A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_30B5")
    Call(0, 15)
    Jump("loc_34AF")

    label("loc_30B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3129")

    #C0146
    ChrTalk(
        0xFE,
        (
            "今日は東通りのヤツらが\x01",
            "授業うけてるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "へへ、あっちの窓から\x01",
            "のぞいてやろうかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_3129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31FD")

    #C0148
    ChrTalk(
        0xFE,
        (
            "俺とハミルを見分けられる奴は\x01",
            "なかなかいないんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "だから、たまーにハミルのふりして\x01",
            "イタズラしたりするんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "でも、母ちゃんが相手だと\x01",
            "すぐにバレちまうんだよなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3271")

    label("loc_31FD")


    #C0151
    ChrTalk(
        0xFE,
        (
            "母ちゃんが相手だと、\x01",
            "ハミルと入れ替わっても\x01",
            "すぐにバレちまうんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "うむむ、見分け方とかあんのかな？\x02",
    )

    CloseMessageWindow()

    label("loc_3271")

    Jump("loc_34AF")

    label("loc_3276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32E1")

    #C0153
    ChrTalk(
        0xFE,
        (
            "オルキスタワーってのは\x01",
            "ほんとにでっかかったなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "正直、チビっちゃいそうだったよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_32E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32F2")
    Call(0, 11)
    Jump("loc_34AF")

    label("loc_32F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3300")
    Jump("loc_34AF")

    label("loc_3300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_343A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D3")

    #C0155
    ChrTalk(
        0xFE,
        (
            "さっき新入りのシスターに\x01",
            "スカートめくりしてやろうと\x01",
            "思ったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "なんかものすごいアザヤカに\x01",
            "かわされちゃったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "むむむ……どうやら\x01",
            "タダモノじゃなさそーだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3435")

    label("loc_33D3")


    #C0158
    ChrTalk(
        0xFE,
        (
            "俺のスカートめくりを\x01",
            "かわすなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "あの新入りのシスター、\x01",
            "タダモノじゃなさそーだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3435")

    Jump("loc_34AF")

    label("loc_343A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_34A6")

    #C0160
    ChrTalk(
        0xFE,
        (
            "さっき新入りのシスターが\x01",
            "来たみたいだなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "へへっ、あとでちょっと\x01",
            "からかってやろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AF")

    label("loc_34A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34AF")

    label("loc_34AF")

    TalkEnd(0xFE)
    Return()

    # Function_12_2EC6 end

    def Function_13_34B3(): pass

    label("Function_13_34B3")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0162
    ChrTalk(
        0xB,
        (
            "大人たちがなんだか\x01",
            "騒いでるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "ドクリツっていったい、\x01",
            "どういうことなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xB,
        (
            "ハミル、お前って勉強得意だろ。\x01",
            "教えてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xC,
        (
            "む、むりだよ。\x01",
            "僕にもよく分からないし……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_13_34B3 end

    def Function_14_3595(): pass

    label("Function_14_3595")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0166
    ChrTalk(
        0xB,
        (
            "……それで、シスターに怒られたら\x01",
            "こうするんだよ……ゴニョゴニョ……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        (
            "ええっ、なんで僕まで\x01",
            "そんなことをしなきゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "いいじゃん、この間おねしょしたの\x01",
            "キーアにだまっといてやるから！\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xC,
        "うっ、それをいわれると……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_14_3595 end

    def Function_15_368A(): pass

    label("Function_15_368A")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377C")

    #C0170
    ChrTalk(
        0xB,
        (
            "俺たちまで日曜学校の授業に\x01",
            "参加させられちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xB,
        (
            "あーあ、ハミルが授業をのぞこう\x01",
            "なんて言わなけりゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xC,
        (
            "い、いやいや。\x01",
            "それを言ったのはタミルでしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "さりげなく僕のせいにしないでよ、\x01",
            "まったく。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_380B")

    label("loc_377C")


    #C0174
    ChrTalk(
        0xC,
        (
            "でも、よかったじゃない。\x01",
            "たくさん勉強できて\x01",
            "予習にもなったんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "お前と違って俺は勉強嫌いなの！\x01",
            "ちぇっ、これだからガリ勉野郎は……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_380B")

    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_15_368A end

    def Function_16_3814(): pass

    label("Function_16_3814")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3832")
    Call(0, 9)
    Jump("loc_3894")

    label("loc_3832")


    #C0176
    ChrTalk(
        0xFE,
        (
            "うん、街の子供たちは\x01",
            "みんな無事みたいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "ふふ、心配してくれて\x01",
            "ありがとう、シスター。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3894")

    Jump("loc_4013")

    label("loc_3899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_38A7")
    Jump("loc_4013")

    label("loc_38A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C2")
    Call(0, 13)
    Jump("loc_3943")

    label("loc_38C2")


    #C0178
    ChrTalk(
        0xFE,
        (
            "ドクリツのことは\x01",
            "よく分からないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "街のオトナたちが\x01",
            "話しているのを聞く限りじゃ、\x01",
            "なんだか大変なことみたいだね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3943")

    Jump("loc_4013")

    label("loc_3948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3956")
    Jump("loc_4013")

    label("loc_3956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3964")
    Jump("loc_4013")

    label("loc_3964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3972")
    Jump("loc_4013")

    label("loc_3972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_39D3")

    #C0180
    ChrTalk(
        0xFE,
        (
            "はあ、はあ……\x01",
            "な、なんで僕までこんなことを……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        "あとで絶対叱られるよ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4013")

    label("loc_39D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39EE")
    Call(0, 14)
    Jump("loc_3A1D")

    label("loc_39EE")


    #C0182
    ChrTalk(
        0xFE,
        (
            "うう、仕方ないなあ……\x01",
            "今回だけだからね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A1D")

    Jump("loc_4013")

    label("loc_3A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_3A30")
    Jump("loc_4013")

    label("loc_3A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_3A41")
    Call(0, 15)
    Jump("loc_4013")

    label("loc_3A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A88")

    #C0183
    ChrTalk(
        0xFE,
        (
            "やめときなって……\x01",
            "シスターに怒られても知らないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4013")

    label("loc_3A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B42")

    #C0184
    ChrTalk(
        0xFE,
        (
            "お母さんやお父さんは、\x01",
            "僕たち双子の区別が\x01",
            "ちゃんとついてるらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "ほとんど同じ顔なのに、\x01",
            "見るだけで分かるんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "親ってすごいかも……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3BB2")

    label("loc_3B42")


    #C0187
    ChrTalk(
        0xFE,
        (
            "お母さんやお父さんは、\x01",
            "どっちが僕でどっちがタミルか\x01",
            "見るだけで分かるんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        "親ってすごいかも……\x02",
    )

    CloseMessageWindow()

    label("loc_3BB2")

    Jump("loc_4013")

    label("loc_3BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C35")

    #C0189
    ChrTalk(
        0xFE,
        (
            "はあ、せっかくだから\x01",
            "除幕式はキーアちゃんと\x01",
            "いっしょに見たかったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        "……あっ、な、なんでもないよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4013")

    label("loc_3C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE0")

    #C0191
    ChrTalk(
        0xFE,
        (
            "タミル、かくれんぼで\x01",
            "シスターのスカートの中に\x01",
            "隠れちゃったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "はあ、怒られるのが\x01",
            "分かりきってるのに、\x01",
            "なんでそんなことするかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3D57")

    label("loc_3CE0")


    #C0193
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "タミルが怒られてると、\x01",
            "僕まで怒られてる気になるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "双子っていうのは\x01",
            "なんだかソンだよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D57")

    Jump("loc_4013")

    label("loc_3D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D6A")
    Jump("loc_4013")

    label("loc_3D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_3F9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F3F")
    TurnDirection(0xFE, 0x153, 0)

    #C0195
    ChrTalk(
        0xFE,
        (
            "あっ、キーアちゃん！\x01",
            "年長クラスの授業は終わったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x153,
        (
            "#01109Fうん、今終わったトコー。\x02\x03",

            "#01100Fハミルは授業終わったあとから\x01",
            "今まで遊んでたのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "う、うん。\x01",
            "タミルと一緒にね。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "ていうか、キーアちゃんも\x01",
            "もうちゃんと僕がハミルって\x01",
            "カンペキに分かるんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x153,
        (
            "#01105Fえー、なんで？\x02\x03",

            "#01109Fタミルと顔はソックリだけど\x01",
            "ハミルはハミルだし、分かるよー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0200
    ChrTalk(
        0xFE,
        "（やばい、すっごくうれしいかも……！）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F99")

    label("loc_3F3F")

    TurnDirection(0xFE, 0x153, 0)

    #C0201
    ChrTalk(
        0xFE,
        "えっと、気をつけてねキーアちゃん。\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x153,
        "#01109Fうん、またみんなで遊ぼーねー！\x02",
    )

    CloseMessageWindow()

    label("loc_3F99")

    Jump("loc_4013")

    label("loc_3F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_400A")

    #C0203
    ChrTalk(
        0xFE,
        (
            "だめだよタミル……\x01",
            "怖いヒトだったらどうすんのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "怒られちゃっても\x01",
            "知らないからね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4013")

    label("loc_400A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4013")

    label("loc_4013")

    TalkEnd(0xFE)
    Return()

    # Function_16_3814 end

    def Function_17_4017(): pass

    label("Function_17_4017")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402C")
    Call(0, 18)
    Jump("loc_408F")

    label("loc_402C")


    #C0205
    ChrTalk(
        0xFE,
        (
            "はー……\x01",
            "キーアに言われちゃったら\x01",
            "仕方ないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "今度からちゃんと\x01",
            "宿題やるようにしよっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_408F")

    TalkEnd(0xFE)
    Return()

    # Function_17_4017 end

    def Function_18_4093(): pass

    label("Function_18_4093")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0207
    ChrTalk(
        0xD,
        (
            "シスターにやんわり\x01",
            "怒られちゃったのよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xE,
        (
            "あんた、宿題やらなかったんだし\x01",
            "ジゴージトクってやつじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xD,
        (
            "はー、昔は結構ユルかったのに\x01",
            "年長クラスになってから\x01",
            "キビしくなったよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x153,
        (
            "#01105F宿題、今度はちゃんと\x01",
            "やんないとダメだよー？\x02",
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
        "あ～い……\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x101,
        "#00012F（さ、さすがキーアだな……）\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    TurnDirection(0xD, 0xE, 0)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_18_4093 end

    def Function_19_420D(): pass

    label("Function_19_420D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4222")
    Call(0, 18)
    Jump("loc_4253")

    label("loc_4222")


    #C0213
    ChrTalk(
        0xFE,
        (
            "ぷっ、あんたも\x01",
            "この子にかかれば形無しねー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4253")

    TalkEnd(0xFE)
    Return()

    # Function_19_420D end

    def Function_20_4257(): pass

    label("Function_20_4257")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B1")
    TurnDirection(0xFE, 0x153, 0)

    #C0214
    ChrTalk(
        0xFE,
        (
            "お、キーアちゃん、\x01",
            "今帰りかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x153,
        "#01110Fうん！　ブリックも帰るとこー？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "ああ、ついでだから\x01",
            "西通りでクロスベルタイムズを\x01",
            "買って帰ろうと思ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "キーアちゃん……\x01",
            "次の授業では負けないからね！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x153,
        "#01111Fほえー、勝ち負けがあったのー？\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0219
    ChrTalk(
        0xFE,
        (
            "い、いや何でもない。\x01",
            "忘れてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4438")

    label("loc_43B1")


    #C0220
    ChrTalk(
        0xFE,
        (
            "キーアちゃんが年長クラスに\x01",
            "参加してきたときは、\x01",
            "流石にビックリしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "これを機に、改めてちゃんと\x01",
            "勉強しようと思ったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4438")

    TalkEnd(0xFE)
    Return()

    # Function_20_4257 end

    def Function_21_443C(): pass

    label("Function_21_443C")

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

    def lambda_4583():
        OP_9B(0x0, 0x101, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4583)
    Sleep(100)

    def lambda_459B():
        OP_9B(0x0, 0x102, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_459B)
    Sleep(100)

    def lambda_45B3():
        OP_9B(0x0, 0x103, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_45B3)
    Sleep(100)

    def lambda_45CB():
        OP_9B(0x0, 0x104, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_45CB)
    Sleep(100)

    def lambda_45E3():
        OP_9B(0x0, 0x109, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_45E3)
    Sleep(100)

    def lambda_45FB():
        OP_9B(0x0, 0x105, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_45FB)
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

    def lambda_467A():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_467A)
    Sleep(50)

    def lambda_468A():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_468A)
    Sleep(50)

    def lambda_469A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_469A)
    Sleep(50)

    def lambda_46AA():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_46AA)
    Sleep(50)

    def lambda_46BA():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_46BA)
    Sleep(50)

    def lambda_46CA():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_46CA)
    Sleep(50)

    def lambda_46DA():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_46DA)
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
            "#00003F#11P……そろそろ夕方か。\x02\x03",

            "#00001F今日中に報告書は提出したいし、\x01",
            "何とか情報を集めないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x102,
        (
            "#00108F#12Pええ……\x01",
            "手がかりがあるといいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4835")

    #C0224
    ChrTalk(
        0x103,
        (
            "#00200Fとりあえず、\x01",
            "リースさんかマーブル先生を\x01",
            "訪ねてみるんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#00000F#11Pああ、まずは日曜学校の\x01",
            "教室を訪ねてみよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B5")

    label("loc_4835")


    #C0226
    ChrTalk(
        0x103,
        (
            "#00200Fとりあえずマーブル先生を\x01",
            "訪ねてみるんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#00000F#11Pああ、日曜学校の授業が\x01",
            "入ってないといいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B5")

    ClearChrFlags(0x10, 0x80)

    #N0228
    NpcTalk(
        0x10,
        "男性の声",
        "おや、君たちは……\x02",
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

    def lambda_4955():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4955)
    Sleep(0)

    def lambda_4965():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4965)
    Sleep(0)

    def lambda_4975():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4975)
    Sleep(0)

    def lambda_4985():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4985)
    Sleep(0)

    def lambda_4995():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4995)
    Sleep(0)

    def lambda_49A5():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_49A5)
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
        "#00005F#6Pイアン先生……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 1)), scpexpr(EXPR_END)), "loc_4C7F")

    #C0230
    ChrTalk(
        0x102,
        "#00104F#6Pご無沙汰しています。\x02",
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
            "ああ、通商会議の時以来だね。\x02\x03",

            "おっと、そういえば昼間、\x01",
            "事務所に来てくれたんだって？\x02\x03",

            "すまなかったね。\x01",
            "わざわざ訪ねてくれたのに。\x02",
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
            "#00012F#6Pいえ……\x01",
            "でも、お忙しそうですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x109,
        (
            "#10100F#6P何でも憲法草案の作成に\x01",
            "協力されているとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x10,
        (
            "#02210F#11Pいや、はは……\x02\x03",

            "市長が熱心に頼んでくるから\x01",
            "断りきれなくってね。\x02\x03",

            "#02200Fまあ、私個人としても\x01",
            "彼のアイデアには賛成だ。\x02\x03",

            "実現は困難かもしれないが……\x01",
            "せめて力になれないかと思ってね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50C6")

    label("loc_4C7F")


    #C0235
    ChrTalk(
        0x102,
        (
            "#00104F#6Pご無沙汰しています。\x02\x03",

            "#00108F何でも最近、相当お忙しく\x01",
            "されてらっしゃるそうですね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0236
    ChrTalk(
        0x101,
        "#00005F#5Pそうなのか？\x02",
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
            "いや、はは……\x02\x03",

            "……実は例の国家独立に関する\x01",
            "憲法草案の作成を市長に頼まれてね。\x02",
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
        "#00007F#6Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x109,
        (
            "#10101F#6P《憲法》……\x01",
            "自治州法ではなく、ですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0240
    ChrTalk(
        0x102,
        (
            "#00104F#11P《憲法》というのは\x01",
            "国家存立の基本条件を定めた\x01",
            "根本的な法律になるの。\x02\x03",

            "#00100F国の統治権や仕組み、\x01",
            "大原則を定めた最高法規で\x01",
            "他国の干渉を許さないものよ。\x02\x03",

            "国家としての体裁を持つためには\x01",
            "絶対欠かせないものになるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x104,
        (
            "#00305F#6Pは～……\x01",
            "また難しげなシロモンだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        (
            "#00204F#6Pしかしイアン先生ならば\x01",
            "まさに適任ではないかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x10,
        (
            "#02210F#11Pはは……\x01",
            "市長が熱心に頼んでくるから\x01",
            "断りきれなくってね。\x02\x03",

            "#02200Fまあ、私個人としても\x01",
            "彼のアイデアには賛成だ。\x02\x03",

            "実現は困難かもしれないが……\x01",
            "せめて力になれないかと思ってね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C6")


    def lambda_50CB():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50CB)

    #C0244
    ChrTalk(
        0x101,
        "#00002F#6Pそうですか……\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x105,
        (
            "#10302F#6Pひょっとして息抜きがてら\x01",
            "お祈りにでも来てたのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x10,
        (
            "#02210F#11Pああ、ちょっと煮詰まっていたが\x01",
            "いい気分転換になったようだ。\x02\x03",

            "#02202Fやはり人間、困った時は\x01",
            "女神頼みというのも悪くないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x104,
        (
            "#00309F#6Pハハ……\x01",
            "確かに言えてるッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        "#00104F#6P本当にお疲れさまです。\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x10,
        (
            "#02210F#11Pはは、君たちの方こそ。\x02\x03",

            "#02200Fそろそろ夕方だが……\x01",
            "もしかして仕事で来たのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#00000F#6Pええ、ちょっと教会関係者に\x01",
            "相談したいことがありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x10,
        (
            "#02203F#11Pふむ、事情がありそうだね。\x02\x03",

            "#02200Fこちらも忙しくはあるが……\x01",
            "何か力になれそうな事があったら\x01",
            "遠慮なく事務所を訪ねてくれたまえ。\x02\x03",

            "君たちならば大歓迎だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        "#00004F#6Pありがとうございます。\x02",
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
        "#10100F#6Pお気をつけてお帰りください！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()

    def lambda_53DC():

        label("loc_53DC")

        TurnDirection(0x101, 0x10, 500)
        Yield()
        Jump("loc_53DC")

    QueueWorkItem2(0x101, 2, lambda_53DC)

    def lambda_53EE():

        label("loc_53EE")

        TurnDirection(0x102, 0x10, 500)
        Yield()
        Jump("loc_53EE")

    QueueWorkItem2(0x102, 2, lambda_53EE)

    def lambda_5400():

        label("loc_5400")

        TurnDirection(0x103, 0x10, 500)
        Yield()
        Jump("loc_5400")

    QueueWorkItem2(0x103, 2, lambda_5400)

    def lambda_5412():

        label("loc_5412")

        TurnDirection(0x104, 0x10, 500)
        Yield()
        Jump("loc_5412")

    QueueWorkItem2(0x104, 2, lambda_5412)

    def lambda_5424():

        label("loc_5424")

        TurnDirection(0x109, 0x10, 500)
        Yield()
        Jump("loc_5424")

    QueueWorkItem2(0x109, 2, lambda_5424)

    def lambda_5436():

        label("loc_5436")

        TurnDirection(0x105, 0x10, 500)
        Yield()
        Jump("loc_5436")

    QueueWorkItem2(0x105, 2, lambda_5436)
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
        "#00001F#11P……忙しそうだな。\x02",
    )

    CloseMessageWindow()

    def lambda_54C7():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_54C7)
    Sleep(0)

    def lambda_54D7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_54D7)
    Sleep(0)

    def lambda_54E7():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_54E7)
    Sleep(0)

    def lambda_54F7():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_54F7)
    Sleep(0)

    def lambda_5507():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5507)
    Sleep(0)

    def lambda_5517():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5517)
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
            "#00103F#12Pええ、憲法草案ともなると\x01",
            "相当なものが求められるから……\x02\x03",

            "#00101F下手なものを発表してしまったら\x01",
            "それだけで帝国、共和国あたりから\x01",
            "説得力なしと言われるだろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x104,
        "#00306F#6Pうへぇ……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x105,
        (
            "#10304F#6Pフフ、僕たちの忙しさとは\x01",
            "気苦労も違うんだろうね。\x02\x03",

            "#10300Fそれはそうと……\x01",
            "日曜学校の教室を訪ねるのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        "#00000F#11Pああ、行ってみよう。\x02",
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

    # Function_21_443C end

    def Function_22_56F3(): pass

    label("Function_22_56F3")

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
            "#04403F#5P……さあ、こちらへ。\x02\x03",

            "#04400Fあまり他の方々には\x01",
            "見られたくありませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        "#00001F#12Pは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x102,
        "#00103F#12P……失礼します。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sound(121, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)

    def lambda_5882():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5882)
    OP_9B(0x0, 0x8, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0x8, 3)

    def lambda_58A6():
        OP_95(0x102, -11400, 500, 14750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58A6)
    Sleep(200)

    def lambda_58C3():
        OP_95(0x103, -11400, 500, 13250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58C3)
    Sleep(100)

    def lambda_58E0():
        OP_95(0x101, -11400, 500, 14000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58E0)
    Sleep(100)

    def lambda_58FD():
        OP_95(0x104, -11400, 500, 14750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_58FD)
    Sleep(100)

    def lambda_591A():
        OP_95(0x109, -11400, 500, 13250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_591A)
    Sleep(200)

    def lambda_5937():
        OP_95(0x105, -11400, 500, 14000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5937)
    Sleep(500)
    FadeToDark(1000, 0, -1)

    def lambda_595E():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_595E)
    Sleep(50)

    def lambda_5972():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_5972)
    Sleep(50)

    def lambda_5986():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5986)
    Sleep(150)

    def lambda_599A():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_599A)
    Sleep(50)

    def lambda_59AE():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_59AE)
    Sleep(50)

    def lambda_59C2():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_59C2)
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

    # Function_22_56F3 end

    def Function_23_5A12(): pass

    label("Function_23_5A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE8")

    #C0262
    ChrTalk(
        0xA,
        "今日はミサの日です。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xA,
        (
            "皆さんも参加しては\x01",
            "いかがでしょうか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#00003F（ミスコンの『シスター』枠で\x01",
            "  出てもらえないかな……？）\x02\x03",

            "#00000Fあの、すみません。\x01",
            "ちょっと相談なのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0265
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "チャリティイベントの\x01",
            "ミスコンへの参加を頼んでみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0266
    ChrTalk(
        0xA,
        (
            "え、ええっ……？\x01",
            "私がミスコンって……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xA,
        (
            "む、無理ですよ～。\x01",
            "私なんかほんと、\x01",
            "色気とか全然ないですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xA,
        (
            "すみませんが、他の人を\x01",
            "誘ってみてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        "#00012Fそ、そうですか……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 1)
    Jump("loc_5C50")

    label("loc_5BE8")


    #C0270
    ChrTalk(
        0xA,
        (
            "わ、私なんかが\x01",
            "ミスコンに出るなんて無理ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xA,
        (
            "ふさわしいひとは\x01",
            "もっと他にいると思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C50")

    TalkEnd(0xA)
    Return()

    # Function_23_5A12 end

    def Function_24_5C54(): pass

    label("Function_24_5C54")

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
            "～クロスベル大聖堂寄宿舎～\x01",
            "　　参拝の方は礼拝堂へ\x01",
            "　    お回り下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_24_5C54 end

    def Function_25_5CD6(): pass

    label("Function_25_5CD6")

    EventBegin(0x1)

    #C0273
    ChrTalk(
        0x101,
        (
            "#00001F……とりあえず、\x01",
            "リースさんの所に行こう。\x01",
            "何か情報が得られるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 370, 0, -7350, 0)
    EventEnd(0x4)
    Return()

    # Function_25_5CD6 end

    SaveToFile()

Try(main)
