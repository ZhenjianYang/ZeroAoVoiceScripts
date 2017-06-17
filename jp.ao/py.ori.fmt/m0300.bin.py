from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0300.bin",                # FileName
        "m0300",                    # MapName
        "m0300",                    # Location
        0x00A8,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("m0300", "r0000_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 168, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0300",                  # 0
        "bm0300",                 # 1
        "bm0300",                 # 2
        "bm0300",                 # 3
    ))

    ATBonus("ATBonus_2BC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1477", 5,   5,   5,   5,   10,  0,   0)

    MonsterBattlePostion("MonsterBattlePostion_31C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_32C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_380", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_384", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_388", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_38C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_390", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_394", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 2, 13, 180)

    # monster count: 5

    BattleInfo(
        "BattleInfo_39C", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_1477", 35, 35, 30, 0,
        (
            ("ms84100.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_31C", "MonsterBattlePostion_37C", "ed7450", "ed7453", "ATBonus_2BC"),
            ("ms84100.dat", "ms84100.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_2FC", "MonsterBattlePostion_37C", "ed7450", "ed7453", "ATBonus_2BC"),
            ("ms84100.dat", "ms84200.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_31C", "MonsterBattlePostion_37C", "ed7450", "ed7453", "ATBonus_2BC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_438", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_1477", 35, 35, 30, 0,
        (
            ("ms84200.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_31C", "MonsterBattlePostion_37C", "ed7450", "ed7453", "ATBonus_2BC"),
            ("ms84200.dat", "ms84200.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_2FC", "MonsterBattlePostion_37C", "ed7450", "ed7453", "ATBonus_2BC"),
            ("ms84200.dat", "ms84100.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_31C", "MonsterBattlePostion_37C", "ed7450", "ed7453", "ATBonus_2BC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4D4", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_1477", 35, 35, 30, 0,
        (
            ("ms84300.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_31C", "MonsterBattlePostion_37C", "ed7450", "ed7453", "ATBonus_2BC"),
            ("ms84300.dat", "ms84300.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_2FC", "MonsterBattlePostion_37C", "ed7450", "ed7453", "ATBonus_2BC"),
            ("ms84300.dat", "ms84200.dat", "ms84100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_31C", "MonsterBattlePostion_37C", "ed7450", "ed7453", "ATBonus_2BC"),
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
        "monster/ch84150.itc",               # 10
        "monster/ch84150.itc",               # 11
        "monster/ch84250.itc",               # 12
        "monster/ch84250.itc",               # 13
        "monster/ch84350.itc",               # 14
        "monster/ch84350.itc",               # 15
    ))

    DeclMonster(7670,    -200050, 0,       0x101013B,    "BattleInfo_39C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(200110,  -199540, 0,       0x10100E1,    "BattleInfo_438", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-4080,   -300140, -8000,   0x1010077,    "BattleInfo_4D4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-200100, -205080, -7540,   0x10100BB,    "BattleInfo_39C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-200170, -188030, -2000,   0x10100AB,    "BattleInfo_438", 0,   18,  0xFFFF, 2,  3)

    DeclActor(4000,    0,       -300000, 1200,    4000,    1000,    -300000, 0x007C, 0,  2,  0x0000)
    DeclActor(-4000,   -4000,   -200000, 1200,    -4000,   -3000,   -200000, 0x007C, 0,  3,  0x0000)
    DeclActor(203500,  0,       93000,   1200,    203500,  1000,    93000,   0x007C, 0,  4,  0x0000)
    DeclActor(212000,  -8000,   -8500,   1200,    212000,  -7000,   -8500,   0x007C, 0,  5,  0x0000)
    DeclActor(200000,  0,       -100000, 1200,    200000,  1000,    -100000, 0x007C, 0,  6,  0x0000)
    DeclActor(206000,  0,       223500,  1200,    206000,  1000,    223500,  0x007C, 0,  9,  0x0000)
    DeclActor(6000,    0,       223500,  1200,    6000,    1000,    223500,  0x007C, 0,  11, 0x0000)
    DeclActor(-196000, 0,       100000,  1200,    -196000, 1000,    100000,  0x007C, 0,  8,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_5EC",          # 00, 0
        "Function_1_61B",          # 01, 1
        "Function_2_7C6",          # 02, 2
        "Function_3_917",          # 03, 3
        "Function_4_A7E",          # 04, 4
        "Function_5_BCF",          # 05, 5
        "Function_6_D20",          # 06, 6
        "Function_7_E71",          # 07, 7
        "Function_8_E75",          # 08, 8
        "Function_9_F71",          # 09, 9
        "Function_10_10D1",        # 0A, 10
        "Function_11_11E0",        # 0B, 11
        "Function_12_1340",        # 0C, 12
    ))


    def Function_0_5EC(): pass

    label("Function_0_5EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_603")
    Event(0, 10)

    label("loc_603")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61A")
    Event(0, 12)

    label("loc_61A")

    Return()

    # Function_0_5EC end

    def Function_1_61B(): pass

    label("Function_1_61B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62F")
    OP_C9(0x0, 0x8)

    label("loc_62F")

    OP_10(0x1A, 0x0)
    OP_10(0x1, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_673")
    SetMapObjFrame(0x16, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x16, "Null_color2", 0x0, 0x1)
    Jump("loc_698")

    label("loc_673")

    SetMapObjFrame(0x16, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x16, "Null_color2", 0x1, 0x1)

    label("loc_698")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D6")
    SetMapObjFrame(0x17, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x17, "Null_color2", 0x0, 0x1)
    Jump("loc_6FB")

    label("loc_6D6")

    SetMapObjFrame(0x17, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x17, "Null_color2", 0x1, 0x1)

    label("loc_6FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70E")
    OP_70(0x0, 0x0)
    Jump("loc_712")

    label("loc_70E")

    OP_70(0x0, 0x1E)

    label("loc_712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_725")
    OP_70(0x1, 0x0)
    Jump("loc_729")

    label("loc_725")

    OP_70(0x1, 0x1E)

    label("loc_729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73C")
    OP_70(0x2, 0x0)
    Jump("loc_740")

    label("loc_73C")

    OP_70(0x2, 0x1E)

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_753")
    OP_70(0x3, 0x0)
    Jump("loc_757")

    label("loc_753")

    OP_70(0x3, 0x1E)

    label("loc_757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76A")
    OP_70(0x4, 0x0)
    Jump("loc_76E")

    label("loc_76A")

    OP_70(0x4, 0x1E)

    label("loc_76E")

    OP_1C(0x0, 0x5, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    OP_1C(0x0, 0x11, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    OP_1C(0x0, 0x12, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    OP_1C(0x0, 0x13, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    OP_1C(0x0, 0x14, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    OP_1C(0x0, 0x15, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Return()

    # Function_1_61B end

    def Function_2_7C6(): pass

    label("Function_2_7C6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C6")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x648, 1)"), scpexpr(EXPR_END)), "loc_84F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x648),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F0, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_8C1")

    label("loc_84F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x648),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x648),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_8C1")

    Jump("loc_90B")

    label("loc_8C6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_90B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_7C6 end

    def Function_3_917(): pass

    label("Function_3_917")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A47")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 60)
    AddSepith(0x1, 60)
    AddSepith(0x2, 60)
    AddSepith(0x3, 60)
    AddSepith(0x4, 60)
    AddSepith(0x5, 60)
    AddSepith(0x6, 60)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×６０\x01\x07\x02",

            "#57I水のセピス×６０\x01\x07\x02",

            "#58I火のセピス×６０\x01\x07\x02",

            "#59I風のセピス×６０\x01\x07\x02",

            "#60I時のセピス×６０\x01\x07\x02",

            "#61I空のセピス×６０\x01\x07\x02",

            "#62I幻のセピス×６０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F0, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_A6C")

    label("loc_A47")


    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_A6C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_917 end

    def Function_4_A7E(): pass

    label("Function_4_A7E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7E")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_B07")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F0, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_B79")

    label("loc_B07")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_B79")

    Jump("loc_BC3")

    label("loc_B7E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_BC3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_A7E end

    def Function_5_BCF(): pass

    label("Function_5_BCF")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCF")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x192, 1)"), scpexpr(EXPR_END)), "loc_C58")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x192),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F0, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_CCA")

    label("loc_C58")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x192),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x192),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_CCA")

    Jump("loc_D14")

    label("loc_CCF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_D14")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_BCF end

    def Function_6_D20(): pass

    label("Function_6_D20")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E20")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E3, 1)"), scpexpr(EXPR_END)), "loc_DA9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F0, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_E1B")

    label("loc_DA9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5E3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5E3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E1B")

    Jump("loc_E65")

    label("loc_E20")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_E65")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_D20 end

    def Function_7_E71(): pass

    label("Function_7_E71")

    Call(1, 6)
    Return()

    # Function_7_E71 end

    def Function_8_E75(): pass

    label("Function_8_E75")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0015
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F62")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x19, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x19, 0x0)
    OP_71(0x19, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x19)
    OP_71(0x19, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x19, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_F62")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_8_E75 end

    def Function_9_F71(): pass

    label("Function_9_F71")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "リフトの制御パネルがある。\x01",
            "操作しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C9")
    Fade(500)
    SetChrPos(0x0, 205500, 0, 224500, 180)
    SetChrPos(0x1, 206500, 0, 224500, 180)
    SetChrPos(0x2, 205500, 0, 225500, 180)
    SetChrPos(0x3, 206500, 0, 225500, 180)
    OP_68(205150, 0, 224810, 0)
    MoveCamera(39, 46, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x16, 0x2F8, 0x352, 0x0, 0x0)
    Sleep(200)
    OP_68(206500, -2000, 212000, 3800)
    MoveCamera(22, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0301", 100, 0, 0)
    IdleLoop()

    label("loc_10C9")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_F71 end

    def Function_10_10D1(): pass

    label("Function_10_10D1")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x16, 0x352)
    Sleep(1)
    OP_68(204790, -2500, 213730, 0)
    MoveCamera(21, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 203500, -2500, 214000, 270)
    OP_90(0x1, 203500, -2500, 213000, 270)
    OP_90(0x2, 204500, -2500, 214000, 270)
    OP_90(0x3, 204500, -2500, 213000, 270)
    Sound(145, 0, 100, 0)
    OP_68(205270, 0, 226390, 3200)
    MoveCamera(43, 43, 0, 3200)
    OP_71(0x16, 0x352, 0x2F8, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x16)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x16, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x16, "Null_color2", 0x1, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_10D1 end

    def Function_11_11E0(): pass

    label("Function_11_11E0")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "リフトの制御パネルがある。\x01",
            "操作しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1338")
    Fade(500)
    SetChrPos(0x0, 5500, 0, 224500, 180)
    SetChrPos(0x1, 6500, 0, 224500, 180)
    SetChrPos(0x2, 5500, 0, 225500, 180)
    SetChrPos(0x3, 6500, 0, 225500, 180)
    OP_68(5150, 0, 224810, 0)
    MoveCamera(39, 46, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x17, 0x2F8, 0x3B6, 0x0, 0x0)
    Sleep(200)
    OP_68(6500, -2000, 212000, 3800)
    MoveCamera(22, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0309", 100, 0, 0)
    IdleLoop()

    label("loc_1338")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_11E0 end

    def Function_12_1340(): pass

    label("Function_12_1340")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x17, 0x352)
    Sleep(1)
    OP_68(4790, -2500, 213730, 0)
    MoveCamera(21, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 3500, -2500, 213500, 270)
    OP_90(0x1, 3500, -2500, 212500, 270)
    OP_90(0x2, 4500, -2500, 213500, 270)
    OP_90(0x3, 4500, -2500, 212500, 270)
    Sound(145, 0, 100, 0)
    OP_68(5270, 0, 226390, 3200)
    MoveCamera(43, 43, 0, 3200)
    OP_71(0x17, 0x352, 0x2F8, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x17)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x17, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x17, "Null_color2", 0x1, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_1340 end

    SaveToFile()

Try(main)
