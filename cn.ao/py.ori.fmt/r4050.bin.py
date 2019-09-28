from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r4050.bin",                # FileName
        "r4050",                    # MapName
        "r4050",                    # Location
        0x00A6,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x26,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 12000, 0, 41000, 0, 0, 1, 166, 0, 1, 0, 2],
    )

    BuildStringList((
        "r4050",                  # 0
        "军犬",                   # 1
        "国防军士兵",             # 2
        "国防军士兵",             # 3
        "MapThread",              # 4
        "军团变色龙",             # 5
        "SE控制",                 # 6
        "br4010",                 # 7
        "br4010",                 # 8
        "br4010",                 # 9
        "br4010",                 # 10
        "br4010",                 # 11
        "br4010",                 # 12
    ))

    ATBonus("ATBonus_3D4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_3E4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_3C4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_221C", 6,   0,   2,   15,  8,   4,   0)
    Sepith("Sepith_2224", 4,   10,  4,   6,   0,   9,   0)
    Sepith("Sepith_222C", 6,   3,   12,  3,   0,   0,   11)
    Sepith("Sepith_2234", 10,  6,   4,   10,  0,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_424", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_488", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_48C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_490", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_494", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_498", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_49C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_404", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 0, 0, 180)

    # monster count: 10

    BattleInfo(
        "BattleInfo_4C4", 0x0000, 68, 6, 60, 8, 1, 40, 0, "br4010", "Sepith_221C", 40, 30, 20, 10,
        (
            ("ms78400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms78400.dat", "ms78400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms78400.dat", "ms78400.dat", "ms78400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms78400.dat", "ms78400.dat", "ms78400.dat", "ms78400.dat", 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
        )
    )

    BattleInfo(
        "BattleInfo_58C", 0x0000, 68, 6, 60, 8, 1, 20, 0, "br4010", "Sepith_2224", 40, 30, 20, 10,
        (
            ("ms82400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms82400.dat", "ms82400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms82400.dat", "ms82400.dat", "ms82400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms82400.dat", "ms82400.dat", "ms82400.dat", "ms82400.dat", 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
        )
    )

    BattleInfo(
        "BattleInfo_654", 0x0000, 68, 6, 60, 8, 1, 30, 0, "br4010", "Sepith_222C", 40, 30, 20, 10,
        (
            ("ms82800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms82800.dat", "ms82800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms82800.dat", "ms82800.dat", "ms82800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
        )
    )

    BattleInfo(
        "BattleInfo_71C", 0x0000, 68, 6, 60, 8, 1, 30, 0, "br4010", "Sepith_2234", 50, 30, 20, 0,
        (
            ("ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_7B8", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7451", "ed7453", "ATBonus_3E4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7FC", 0x004A, 3, 6, 45, 3, 3, 30, 0, "br4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41400.dat", "ms80800.dat", "ms41500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4A4", "MonsterBattlePostion_484", "ed7453", "ed7453", "ATBonus_3C4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch78450.itc",               # 10
        "monster/ch78450.itc",               # 11
        "monster/ch82450.itc",               # 12
        "monster/ch82450.itc",               # 13
        "monster/ch82850.itc",               # 14
        "monster/ch82851.itc",               # 15
        "monster/ch86750.itc",               # 16
        "monster/ch86750.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(54709,   6750,    -26420,  0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(7790,    10850,   0,       0x101008C,    "BattleInfo_4C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(8750,    -27930,  0,       0x101008C,    "BattleInfo_58C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-2690,   -8260,   560,     0x1010032,    "BattleInfo_654", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-18680,  5210,    4000,    0x101005F,    "BattleInfo_58C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-14660,  19180,   4000,    0x1010140,    "BattleInfo_71C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(37200,   30540,   4000,    0x101008C,    "BattleInfo_4C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(44100,   6010,    -3000,   0x1010140,    "BattleInfo_71C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(32500,   -23230,  -5000,   0x1010032,    "BattleInfo_654", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(44700,   -4090,   -1750,   0x101008C,    "BattleInfo_4C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(41250,   -37180,  -6000,   0x101008C,    "BattleInfo_58C", 0,   18,  0xFFFF, 2,  3)

    DeclActor(54710,   6250,    -26420,  1200,    54710,   7250,    -26420,  0x007C, 0,  3,  0x0000)
    DeclActor(-20000,  4000,    23000,   1200,    -20000,  5000,    23000,   0x007C, 0,  4,  0x0000)
    DeclActor(48300,   -1750,   -1940,   1200,    48300,   -750,    -1940,   0x007C, 0,  5,  0x0000)
    DeclActor(10050,   0,       48930,   1200,    10050,   1000,    48930,   0x007C, 0,  6,  0x0000)
    DeclActor(44070,   4000,    23010,   1200,    44070,   4500,    23010,   0x007C, 0,  7,  0x0000)
    DeclActor(42740,   -3000,   20440,   1200,    42740,   -2000,   20440,   0x007C, 0,  8,  0x0000)

    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4])                       # 0
    ChipFrameInfo(1700, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4])                       # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4])                       # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_8F4",          # 00, 0
        "Function_1_910",          # 01, 1
        "Function_2_934",          # 02, 2
        "Function_3_EAE",          # 03, 3
        "Function_4_10AC",         # 04, 4
        "Function_5_11E7",         # 05, 5
        "Function_6_1322",         # 06, 6
        "Function_7_13AE",         # 07, 7
        "Function_8_146F",         # 08, 8
        "Function_9_1530",         # 09, 9
        "Function_10_1587",        # 0A, 10
        "Function_11_198C",        # 0B, 11
        "Function_12_1D8A",        # 0C, 12
        "Function_13_1E56",        # 0D, 13
        "Function_14_1E90",        # 0E, 14
        "Function_15_1EAC",        # 0F, 15
        "Function_16_1EC8",        # 10, 16
        "Function_17_1F01",        # 11, 17
        "Function_18_1F2B",        # 12, 18
        "Function_19_1F55",        # 13, 19
        "Function_20_1F6F",        # 14, 20
    ))


    def Function_0_8F4(): pass

    label("Function_0_8F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90F")
    OP_A1(0xFE, 0x2BC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_8F4")

    label("loc_90F")

    Return()

    # Function_0_8F4 end

    def Function_1_910(): pass

    label("Function_1_910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_924")
    ClearScenarioFlags(0x22, 0)
    Event(0, 10)
    Jump("loc_933")

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_933")
    ClearScenarioFlags(0x22, 1)
    Event(0, 11)

    label("loc_933")

    Return()

    # Function_1_910 end

    def Function_2_934(): pass

    label("Function_2_934")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF2D100C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x1, 0x0, 28990, 0, 2680, 4000, 2000, 330000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 19220, 10, 8290, 2000, 2000, 300000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x210, 6)), scpexpr(EXPR_END)), "loc_E45")
    SetMapObjFrame(0xFF, "brake00", 0x2, "stop")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    EndChrThread(0xB, 0x0)
    Jump("loc_E5D")

    label("loc_E45")

    BeginChrThread(0xB, 0, 0, 9)
    SetMapObjFrame(0xFF, "brake00", 0x2, "defolt")

    label("loc_E5D")

    OP_1C(0x0, 0x3, 0x0, 0x0, 0x0, 0x0, 0x1086, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7B")
    OP_70(0x0, 0x0)
    Jump("loc_E7F")

    label("loc_E7B")

    OP_70(0x0, 0x1E)

    label("loc_E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E92")
    OP_70(0x1, 0x0)
    Jump("loc_E96")

    label("loc_E92")

    OP_70(0x1, 0x1E)

    label("loc_E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA9")
    OP_70(0x2, 0x0)
    Jump("loc_EAD")

    label("loc_EA9")

    OP_70(0x2, 0x1E)

    label("loc_EAD")

    Return()

    # Function_2_934 end

    def Function_3_EAE(): pass

    label("Function_3_EAE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106E")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAB")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_F0B():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_F0B)

    def lambda_F25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_F25)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_7B8", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_F8C"),
        (2, "loc_F9B"),
        (1, "loc_FA8"),
        (SWITCH_DEFAULT, "loc_FAB"),
    )


    label("loc_F8C")

    SetScenarioFlags(0x217, 2)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_FAB")

    label("loc_F9B")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_FA8")

    OP_B9(0x0)
    Return()

    label("loc_FAB")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('攻击３', 1)"), scpexpr(EXPR_END)), "loc_1002")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E4, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1069")

    label("loc_1002")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x6E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x6E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1069")

    Jump("loc_10A0")

    label("loc_106E")

    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_10A0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_EAE end

    def Function_4_10AC(): pass

    label("Function_4_10AC")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119E")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('圣灵药', 1)"), scpexpr(EXPR_END)), "loc_112F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E4, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1199")

    label("loc_112F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1199")

    Jump("loc_11DB")

    label("loc_119E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_11DB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_10AC end

    def Function_5_11E7(): pass

    label("Function_5_11E7")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D9")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('结晶碎片', 1)"), scpexpr(EXPR_END)), "loc_126A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E4, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_12D4")

    label("loc_126A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12D4")

    Jump("loc_1316")

    label("loc_12D9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1316")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_11E7 end

    def Function_6_1322(): pass

    label("Function_6_1322")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "攀爬绳索，前往森林道\x01",      # 0
            "离开此处\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1381"),
        (1, "loc_13A1"),
        (SWITCH_DEFAULT, "loc_13AD"),
    )


    label("loc_1381")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    NewScene("r4000", 102, 0, 0)
    IdleLoop()
    Jump("loc_13AD")

    label("loc_13A1")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_13AD")

    label("loc_13AD")

    Return()

    # Function_6_1322 end

    def Function_7_13AE(): pass

    label("Function_7_13AE")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "顺着绳索下去\x01",      # 0
            "离开此处\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1405"),
        (1, "loc_1462"),
        (SWITCH_DEFAULT, "loc_146E"),
    )


    label("loc_1405")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 42400, -3000, 18950, 180)
    SetChrPos(0x1, 42400, -3000, 18950, 180)
    SetChrPos(0x2, 42400, -3000, 18950, 180)
    SetChrPos(0x3, 42400, -3000, 18950, 180)
    OP_E2(0x2)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_146E")

    label("loc_1462")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_146E")

    label("loc_146E")

    Return()

    # Function_7_13AE end

    def Function_8_146F(): pass

    label("Function_8_146F")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "攀爬绳索上去\x01",      # 0
            "离开此处\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14C6"),
        (1, "loc_1523"),
        (SWITCH_DEFAULT, "loc_152F"),
    )


    label("loc_14C6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 44640, 4000, 24150, 0)
    SetChrPos(0x1, 44640, 4000, 24150, 0)
    SetChrPos(0x2, 44640, 4000, 24150, 0)
    SetChrPos(0x3, 44640, 4000, 24150, 0)
    OP_E2(0x2)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_152F")

    label("loc_1523")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_152F")

    label("loc_152F")

    Return()

    # Function_8_146F end

    def Function_9_1530(): pass

    label("Function_9_1530")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1586")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x210, 6)), scpexpr(EXPR_END)), "loc_157E")
    SetMapObjFrame(0xFF, "brake00", 0x2, "anime")
    Sound(156, 0, 100, 0)
    Sleep(1650)
    OP_82(0x0, 0xC8, 0x7D0, 0x190)
    Sleep(400)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    EndChrThread(0xFE, 0x0)

    label("loc_157E")

    Sleep(1)
    Jump("Function_9_1530")

    label("loc_1586")

    Return()

    # Function_9_1530 end

    def Function_10_1587(): pass

    label("Function_10_1587")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SetChrPos(0x101, 10300, 0, 43800, 180)
    SetChrPos(0x102, 9700, 0, 45200, 180)
    SetChrPos(0x103, 10950, 0, 46100, 180)
    SetChrPos(0x104, 11100, 0, 44550, 180)
    SetChrPos(0x109, 10450, 0, 47550, 180)
    SetChrPos(0x105, 9550, 0, 46650, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    Sleep(1000)
    OP_11(0x3C, 0x41, 0x69, 0x32, 0x96, 0x0)
    OP_68(31600, 8700, 2100, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(33000, 0)
    FadeToBright(1000, 0)
    OP_68(45650, 8700, -11950, 8000)
    OP_6F(0x79)
    Fade(500)
    OP_68(35900, 4500, -28100, 0)
    MoveCamera(340, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(42950, 0)
    MoveCamera(300, 16, 0, 8000)
    PlaceName2(340, 200, "c_plac55", 0x0, 2000)
    OP_6F(0x79)
    Fade(1000)
    OP_11(0x3C, 0x41, 0x69, 0x1E, 0x78, 0x0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    OP_68(10300, 4200, 44800, 0)
    MoveCamera(315, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19650, 0)
    OP_68(10300, 1200, 44800, 3500)
    OP_6F(0x79)
    OP_0D()

    #C0011
    ChrTalk(
        0x102,
        "#00107F#11P这、这是……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x109,
        "#10110F#11P蓝、蓝花……！？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#00307F#11P啧……两个月之前，\x01",
            "不是完全没有这种东西吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00003F#5P大概是最近才\x01",
            "开始盛开的。\x02\x03",

            "#00008F缇欧，属性的气息如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        (
            "#00203F#11P……感知到了时、空、幻属性。\x02\x03",

            "#00201F看来之前感觉到的那股奇妙\x01",
            "气息就是源自这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#00006F#5P是吗……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x105,
        (
            "#10301F#11P……前进的难度\x01",
            "似乎比预想的更高。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        (
            "#00303F#11P嗯，这里的道路错综复杂，\x01",
            "原本就很容易迷路。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x109,
        (
            "#10101F#11P我们谨慎前进，\x01",
            "注意不要遭到魔兽的偷袭！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00013F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 12370, 0, 41660, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x163, 7)
    OP_29(0xA8, 0x1, 0xA)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_1587 end

    def Function_11_198C(): pass

    label("Function_11_198C")

    EventBegin(0x0)
    OP_E2(0x1)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41450.itc", 0x1E)
    LoadChrToIndex("chr/ch41451.itc", 0x1F)
    LoadChrToIndex("chr/ch41550.itc", 0x20)
    LoadChrToIndex("chr/ch41551.itc", 0x21)
    LoadChrToIndex("monster/ch80850.itc", 0x22)
    LoadChrToIndex("monster/ch80851.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 0, 0, 0)
    SetChrFlags(0x9, 0x8)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 0, 0, 0)
    SetChrFlags(0xA, 0x8)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 0, 0)
    SetChrFlags(0x8, 0x20)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 15)
    SetChrFlags(0x8, 0x8)
    OP_68(11800, 2000, 18000, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    BeginChrThread(0x101, 3, 0, 12)
    FadeToBright(1000, 0)
    OP_68(14300, 1000, -7000, 8000)
    MoveCamera(315, 26, 0, 8000)
    SetCameraDistance(35000, 8000)
    OP_0D()
    Sleep(6500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 13)
    FadeToBright(1000, 0)
    OP_68(22500, -3000, -3550, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(25500, 0)
    SetCameraDistance(21500, 3000)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x101, 3)

    #C0021
    ChrTalk(
        0x101,
        (
            "#00015F#11P（啧……不愧是前警备队成员。）\x02\x03",

            "#00013F（怎么办……\x01",
            "  ……罗伊德·班宁斯……！）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 26000, -4000, -13200, 0)
    Sound(911, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x8, 0x8)
    BeginChrThread(0x8, 3, 0, 16)
    BeginChrThread(0xD, 1, 0, 19)
    OP_68(22500, -3000, -4550, 1000)
    OP_6F(0x79)
    EndChrThread(0xD, 0x1)
    WaitChrThread(0x8, 3)
    OP_68(22500, -3000, -3550, 750)
    OP_9B(0x1, 0x101, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    #C0022
    ChrTalk(
        0x101,
        "#00010F#11P唔……！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    SetChrPos(0x9, 24850, -4000, 7900, 180)
    SetChrPos(0xA, 26000, -3750, 8900, 180)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0023
    ChrTalk(
        0x9,
        "#2S在这里……！\x02",
    )

    CloseMessageWindow()
    OP_68(22500, -3000, -2850, 2000)
    BeginChrThread(0x9, 3, 0, 17)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 18)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0024
    ChrTalk(
        0xA,
        "#11P抓住他！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)

    def lambda_1CDB():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1CDB)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)

    def lambda_1CF8():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1CF8)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 15)
    BeginChrThread(0xD, 1, 0, 19)

    def lambda_1D30():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1D30)
    SetCameraDistance(15500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0xD, 0x1)
    Battle("BattleInfo_7FC", 0x0, 0x1, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 20)
    Return()

    # Function_11_198C end

    def Function_12_1D8A(): pass

    label("Function_12_1D8A")

    SetChrPos(0xFE, 9970, 0, 25800, 180)
    OP_95(0xFE, 12070, 0, 17430, 6000, 0x1)
    OP_95(0xFE, 13620, 0, 6960, 6000, 0x1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x35A2, 0x5DC, 0xD02, 0x7D0, 0x1388)
    SetChrFlags(0xFE, 0x1)
    OP_95(0xFE, 13240, 1500, -5870, 6000, 0x1)
    SetChrSubChip(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x3B4C, 0x0, 0xFFFFD896, 0x3E8, 0x1770)
    SetChrFlags(0xFE, 0x1)
    OP_95(0xFE, 20850, 0, -15300, 6000, 0x1)
    OP_95(0xFE, 20470, 0, -20750, 6000, 0x0)
    Return()

    # Function_12_1D8A end

    def Function_13_1E56(): pass

    label("Function_13_1E56")

    SetChrPos(0xFE, 24950, -4000, 8050, 180)
    OP_95(0xFE, 23350, -4000, 3200, 5000, 0x1)
    OP_95(0xFE, 22500, -4000, -3550, 5000, 0x0)
    Return()

    # Function_13_1E56 end

    def Function_14_1E90(): pass

    label("Function_14_1E90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EAB")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_14_1E90")

    label("loc_1EAB")

    Return()

    # Function_14_1E90 end

    def Function_15_1EAC(): pass

    label("Function_15_1EAC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EC7")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_15_1EAC")

    label("loc_1EC7")

    Return()

    # Function_15_1EAC end

    def Function_16_1EC8(): pass

    label("Function_16_1EC8")

    OP_96(0xFE, 0x5BCC, 0xFFFFF060, 0xFFFFDE9A, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 14)
    Return()

    # Function_16_1EC8 end

    def Function_17_1F01(): pass

    label("Function_17_1F01")

    OP_95(0xFE, 22250, -4000, 3150, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(531, 0, 100, 0)
    Return()

    # Function_17_1F01 end

    def Function_18_1F2B(): pass

    label("Function_18_1F2B")

    OP_95(0xFE, 23850, -4000, 2900, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(805, 0, 100, 0)
    Return()

    # Function_18_1F2B end

    def Function_19_1F55(): pass

    label("Function_19_1F55")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F6E")
    Sound(845, 0, 100, 0)
    Sleep(500)
    Jump("Function_19_1F55")

    label("loc_1F6E")

    Return()

    # Function_19_1F55 end

    def Function_20_1F6F(): pass

    label("Function_20_1F6F")

    EventBegin(0x0)
    OP_E2(0x1)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("apl/ch51611.itc", 0x1F)
    SoundLoad(863)
    SoundLoad(861)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 22500, -4000, -3550, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x3)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 24600, -4000, 350, 0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, 21500, -4000, 1050, 45)
    SetChrFlags(0x8, 0x80)
    OP_68(22500, -3000, -3550, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(19500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00008F#6P（唔，既然如此，就通过货运轨道\x01",
            "  潜入克洛斯贝尔市……）\x02",
        )
    )

    CloseMessageWindow()
    Sound(355, 0, 80, 0)
    Sound(863, 2, 100, 0)
    Sound(861, 2, 50, 0)
    Sleep(700)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(355, 0, 80, 0)
    OP_68(22460, -3000, -4220, 1500)
    OP_9B(0x1, 0x101, 0xB4, 0x12C, 0x4B0, 0x0)
    Sleep(500)
    OP_9B(0x1, 0x101, 0xB4, 0x1F4, 0x4B0, 0x0)
    Sleep(300)

    #C0026
    ChrTalk(
        0x101,
        (
            "#00015F#6P（总而言之……）\x02\x03",

            "#00010F（……无论多艰苦，\x01",
            "  也要从这里逃走……！）\x02",
        )
    )

    CloseMessageWindow()
    Sound(355, 0, 80, 0)
    OP_93(0x101, 0xB4, 0x28A)
    SetCameraDistance(25000, 1500)

    def lambda_217A():
        OP_9B(0x0, 0xFE, 0x163, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_217A)
    Sleep(500)
    StopSound(863, 3000, 90)
    StopSound(861, 3000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(355, 0, 40, 0)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x101, 0x1)
    OP_6F(0x79)
    SetScenarioFlags(0x22, 1)
    NewScene("r4090", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_1F6F end

    SaveToFile()

Try(main)
