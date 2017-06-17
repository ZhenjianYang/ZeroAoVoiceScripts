from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "a0002.bin",                # FileName
        "a0002",                    # MapName
        "a0002",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 25000, 500, 20, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "a0002",                  # 0
        "ダミー",                 # 1
        "ダミー",                 # 2
        "ダミー",                 # 3
        "ダミー",                 # 4
        "ダミー",                 # 5
        "パーティーキャラ",       # 6
        "ＮＰＣ１",               # 7
        "ＮＰＣ２",               # 8
        "別バージョン１",         # 9
        "別バージョン２",         # 10
        "ダミー",                 # 11
        "ダミー",                 # 12
        "ダミー",                 # 13
        "ダミー",                 # 14
        "ダミー",                 # 15
        "ダミー",                 # 16
        "ダミー",                 # 17
        "ダミー",                 # 18
        "ダミー",                 # 19
        "ダミー",                 # 20
        "コンシェル",             # 21
    ))

    AddCharChip((
        "chr/ch40010.itc",                   # 00
        "chr/ch40011.itc",                   # 01
        "chr/ch40012.itc",                   # 02
        "chr/ch40013.itc",                   # 03
        "chr/ch40014.itc",                   # 04
        "chr/ch40015.itc",                   # 05
        "chr/ch40016.itc",                   # 06
        "chr/ch40017.itc",                   # 07
        "chr/ch40018.itc",                   # 08
        "chr/ch40018.itc",                   # 09
        "chr/ch40018.itc",                   # 0A
        "chr/ch40018.itc",                   # 0B
        "chr/ch40018.itc",                   # 0C
        "chr/ch40018.itc",                   # 0D
        "chr/ch40018.itc",                   # 0E
        "chr/ch40018.itc",                   # 0F
        "chr/ch40018.itc",                   # 10
        "chr/ch40018.itc",                   # 11
        "chr/ch40018.itc",                   # 12
        "chr/ch40018.itc",                   # 13
        "monster/ch60050.itc",               # 14
    ))

    DeclNpc(4000,    0,       4000,    180,  257,  0x0, 0,   0,   0,   0,   3,   0,   5,   255,  0)
    DeclNpc(8000,    0,       4000,    180,  257,  0x0, 0,   1,   0,   0,   3,   0,   6,   255,  0)
    DeclNpc(12000,   0,       4000,    180,  257,  0x0, 0,   2,   0,   0,   3,   0,   7,   255,  0)
    DeclNpc(16000,   0,       4000,    180,  257,  0x0, 0,   3,   0,   0,   3,   0,   8,   255,  0)
    DeclNpc(4000,    0,       8000,    180,  257,  0x0, 0,   4,   0,   0,   3,   0,   9,   255,  0)
    DeclNpc(8000,    0,       8000,    180,  257,  0x0, 0,   5,   0,   0,   3,   0,   10,  255,  0)
    DeclNpc(12000,   0,       8000,    180,  257,  0x0, 0,   6,   0,   0,   3,   0,   11,  255,  0)
    DeclNpc(16000,   0,       8000,    180,  257,  0x0, 0,   7,   0,   0,   3,   0,   12,  255,  0)
    DeclNpc(4000,    0,       12000,   180,  257,  0x0, 0,   8,   0,   0,   3,   0,   13,  255,  0)
    DeclNpc(8000,    0,       12000,   180,  257,  0x0, 0,   9,   0,   0,   3,   0,   14,  255,  0)
    DeclNpc(12000,   0,       12000,   180,  257,  0x0, 0,   10,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(16000,   0,       12000,   180,  257,  0x0, 0,   11,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(4000,    0,       16000,   180,  257,  0x0, 0,   12,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(8000,    0,       16000,   180,  257,  0x0, 0,   13,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(12000,   0,       16000,   180,  257,  0x0, 0,   14,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(16000,   0,       16000,   180,  257,  0x0, 0,   15,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(4000,    0,       20000,   180,  257,  0x0, 0,   16,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(8000,    0,       20000,   180,  257,  0x0, 0,   17,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(12000,   0,       20000,   180,  257,  0x0, 0,   18,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(16000,   0,       20000,   180,  257,  0x0, 0,   19,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(1000,    0,       4000,    180,  257,  0x0, 0,   20,  0,   255, 255, 0,   2,   255,  0)

    ScpFunction((
        "Function_0_370",          # 00, 0
        "Function_1_371",          # 01, 1
        "Function_2_372",          # 02, 2
        "Function_3_149E",         # 03, 3
        "Function_4_15A6",         # 04, 4
        "Function_5_15B5",         # 05, 5
        "Function_6_1684",         # 06, 6
        "Function_7_17C3",         # 07, 7
        "Function_8_190E",         # 08, 8
        "Function_9_1ADF",         # 09, 9
        "Function_10_1CE6",        # 0A, 10
        "Function_11_2C53",        # 0B, 11
        "Function_12_3FDB",        # 0C, 12
        "Function_13_5323",        # 0D, 13
        "Function_14_63A6",        # 0E, 14
    ))


    def Function_0_370(): pass

    label("Function_0_370")

    Return()

    # Function_0_370 end

    def Function_1_371(): pass

    label("Function_1_371")

    Return()

    # Function_1_371 end

    def Function_2_372(): pass

    label("Function_2_372")

    TalkBegin(0xFE)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrFlags(0x4, 0x8)
    SetChrFlags(0x5, 0x8)
    SetChrFlags(0x6, 0x8)
    SetChrFlags(0x7, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x8)
    OP_49()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ch00000 - ch01500\x01",      # 0
            "ch05000 - ch05900\x01",      # 1
            "ch06000 - ch06900\x01",      # 2
            "ch07000 - ch07900\x01",      # 3
            "ch20000 - ch21900\x01",      # 4
            "ch22000 - ch23900\x01",      # 5
            "ch24000 - ch25900\x01",      # 6
            "ch26000 - ch27900\x01",      # 7
            "ch28000 - ch29900\x01",      # 8
            "ch30000 - ch31900\x01",      # 9
            "ch40040 - ch40090\x01",      # 10
            "キャンセル\x01",             # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_535"),
        (1, "loc_664"),
        (2, "loc_7A5"),
        (3, "loc_8EB"),
        (4, "loc_A24"),
        (5, "loc_C81"),
        (6, "loc_DE4"),
        (7, "loc_F3D"),
        (8, "loc_1096"),
        (9, "loc_11EF"),
        (10, "loc_1348"),
        (SWITCH_DEFAULT, "loc_13F7"),
    )


    label("loc_535")

    LoadChrToIndex("chr/ch00000.itc", 0x0)
    LoadChrToIndex("chr/ch00100.itc", 0x1)
    LoadChrToIndex("chr/ch00200.itc", 0x2)
    LoadChrToIndex("chr/ch00300.itc", 0x3)
    LoadChrToIndex("chr/ch00400.itc", 0x4)
    LoadChrToIndex("chr/ch00500.itc", 0x5)
    LoadChrToIndex("chr/ch00600.itc", 0x6)
    LoadChrToIndex("chr/ch00700.itc", 0x7)
    LoadChrToIndex("chr/ch00800.itc", 0x8)
    LoadChrToIndex("chr/ch00900.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH00000 ロイド")
    OP_8E(0x9, "CH00100 エリィ")
    OP_8E(0xA, "CH00200 ティオ")
    OP_8E(0xB, "CH00300 ランディ")
    OP_8E(0xC, "CH00400 ワジ")
    OP_8E(0xD, "CH00500 イン")
    OP_8E(0xE, "CH00600 エス")
    OP_8E(0xF, "CH00700 ヨシャ")
    OP_8E(0x10, "CH00800 ノエル")
    OP_8E(0x11, "CH00900 ダドリー")
    Jump("loc_1406")

    label("loc_664")

    LoadChrToIndex("chr/ch05000.itc", 0x0)
    LoadChrToIndex("chr/ch05100.itc", 0x1)
    LoadChrToIndex("chr/ch05200.itc", 0x2)
    LoadChrToIndex("chr/ch05300.itc", 0x3)
    LoadChrToIndex("chr/ch05400.itc", 0x4)
    LoadChrToIndex("chr/ch05500.itc", 0x5)
    LoadChrToIndex("chr/ch05600.itc", 0x6)
    LoadChrToIndex("chr/ch05700.itc", 0x7)
    LoadChrToIndex("chr/ch05800.itc", 0x8)
    LoadChrToIndex("chr/ch05900.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH05000 キーア")
    OP_8E(0x9, "CH05100 イリア")
    OP_8E(0xA, "CH05200 リーシャ")
    OP_8E(0xB, "CH05300 セシル")
    OP_8E(0xC, "CH05400 シズク")
    OP_8E(0xD, "CH05500 マリアベル")
    OP_8E(0xE, "CH05600 ディーター")
    OP_8E(0xF, "CH05700 ソーニャ")
    OP_8E(0x10, "CH05800 マクダエル")
    OP_8E(0x11, "CH05900 イアン")
    Jump("loc_1406")

    label("loc_7A5")

    LoadChrToIndex("chr/ch06000.itc", 0x0)
    LoadChrToIndex("chr/ch06100.itc", 0x1)
    LoadChrToIndex("chr/ch06200.itc", 0x2)
    LoadChrToIndex("chr/ch06300.itc", 0x3)
    LoadChrToIndex("chr/ch06400.itc", 0x4)
    LoadChrToIndex("chr/ch06500.itc", 0x5)
    LoadChrToIndex("chr/ch06600.itc", 0x6)
    LoadChrToIndex("chr/ch06700.itc", 0x7)
    LoadChrToIndex("chr/ch06800.itc", 0x8)
    LoadChrToIndex("chr/ch06900.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH06000 グレイス")
    OP_8E(0x9, "CH06100 ヨナ")
    OP_8E(0xA, "CH06200 マルコーニ")
    OP_8E(0xB, "CH06300 ツァオ?リ")
    OP_8E(0xC, "CH06400 ピエール")
    OP_8E(0xD, "CH06500 ハルトマン")
    OP_8E(0xE, "CH06600 ヨルグ")
    OP_8E(0xF, "CH06700 ドーミトリィ")
    OP_8E(0x10, "CH06800 ディーノ")
    OP_8E(0x11, "CH06900 フラン")
    Jump("loc_1406")

    label("loc_8EB")

    LoadChrToIndex("chr/ch07000.itc", 0x0)
    LoadChrToIndex("chr/ch07100.itc", 0x1)
    LoadChrToIndex("chr/ch07200.itc", 0x2)
    LoadChrToIndex("chr/ch07300.itc", 0x3)
    LoadChrToIndex("chr/ch07400.itc", 0x4)
    LoadChrToIndex("chr/ch07500.itc", 0x5)
    LoadChrToIndex("chr/ch40018.itc", 0x6)
    LoadChrToIndex("chr/ch40018.itc", 0x7)
    LoadChrToIndex("chr/ch40018.itc", 0x8)
    LoadChrToIndex("chr/ch40018.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH07000 オスカー")
    OP_8E(0x9, "CH07100 ウェンディ")
    OP_8E(0xA, "CH07200 コリン")
    OP_8E(0xB, "CH07300 キリカ")
    OP_8E(0xC, "CH07400 レクター")
    OP_8E(0xD, "CH07500 セシル")
    OP_8E(0xE, "CH07600 キーア")
    OP_8E(0xF, "CH07700 キーア")
    OP_8E(0x10, "CH07800 イリア")
    OP_8E(0x11, "CH07900 イリア")
    Jump("loc_1406")

    label("loc_A24")

    LoadChrToIndex("chr/ch20000.itc", 0x0)
    LoadChrToIndex("chr/ch20100.itc", 0x1)
    LoadChrToIndex("chr/ch20200.itc", 0x2)
    LoadChrToIndex("chr/ch20300.itc", 0x3)
    LoadChrToIndex("chr/ch20400.itc", 0x4)
    LoadChrToIndex("chr/ch20500.itc", 0x5)
    LoadChrToIndex("chr/ch20600.itc", 0x6)
    LoadChrToIndex("chr/ch20700.itc", 0x7)
    LoadChrToIndex("chr/ch20800.itc", 0x8)
    LoadChrToIndex("chr/ch20900.itc", 0x9)
    LoadChrToIndex("chr/ch21000.itc", 0xA)
    LoadChrToIndex("chr/ch21100.itc", 0xB)
    LoadChrToIndex("chr/ch21200.itc", 0xC)
    LoadChrToIndex("chr/ch21300.itc", 0xD)
    LoadChrToIndex("chr/ch21400.itc", 0xE)
    LoadChrToIndex("chr/ch21500.itc", 0xF)
    LoadChrToIndex("chr/ch21600.itc", 0x10)
    LoadChrToIndex("chr/ch21700.itc", 0x11)
    LoadChrToIndex("chr/ch21800.itc", 0x12)
    LoadChrToIndex("chr/ch21900.itc", 0x13)
    OP_8E(0x8, "CH20000 西通り?老人")
    OP_8E(0x9, "CH20100 西通り?老婆")
    OP_8E(0xA, "CH20200 西通り?中年男性")
    OP_8E(0xB, "CH20300 西通り?中年女性")
    OP_8E(0xC, "CH20400 西通り?若者")
    OP_8E(0xD, "CH20500 西通り?娘")
    OP_8E(0xE, "CH20600 西通り?男の子")
    OP_8E(0xF, "CH20700 西通り?女の子")
    OP_8E(0x10, "CH20800 東通り?老人")
    OP_8E(0x11, "CH20900 東通り?老婆")
    OP_8E(0x12, "CH21000 東通り?中年男性")
    OP_8E(0x13, "CH21100 東通り?中年女性")
    OP_8E(0x14, "CH21200 東通り?若者")
    OP_8E(0x15, "CH21300 東通り?娘")
    OP_8E(0x16, "CH21400 東通り?男の子")
    OP_8E(0x17, "CH21500 東通り?女の子")
    OP_8E(0x18, "CH21600 上流?老人")
    OP_8E(0x19, "CH21700 上流?老婆")
    OP_8E(0x1A, "CH21800 上流?中年男性")
    OP_8E(0x1B, "CH21900 上流?中年女性")
    Jump("loc_1406")

    label("loc_C81")

    LoadChrToIndex("chr/ch22000.itc", 0x0)
    LoadChrToIndex("chr/ch22100.itc", 0x1)
    LoadChrToIndex("chr/ch22200.itc", 0x2)
    LoadChrToIndex("chr/ch22300.itc", 0x3)
    LoadChrToIndex("chr/ch22400.itc", 0x4)
    LoadChrToIndex("chr/ch22500.itc", 0x5)
    LoadChrToIndex("chr/ch22600.itc", 0x6)
    LoadChrToIndex("chr/ch22700.itc", 0x7)
    LoadChrToIndex("chr/ch22800.itc", 0x8)
    LoadChrToIndex("chr/ch22900.itc", 0x9)
    LoadChrToIndex("chr/ch23000.itc", 0xA)
    LoadChrToIndex("chr/ch23100.itc", 0xB)
    LoadChrToIndex("chr/ch23200.itc", 0xC)
    LoadChrToIndex("chr/ch23300.itc", 0xD)
    LoadChrToIndex("chr/ch23400.itc", 0xE)
    LoadChrToIndex("chr/ch23500.itc", 0xF)
    LoadChrToIndex("chr/ch23600.itc", 0x10)
    LoadChrToIndex("chr/ch23700.itc", 0x11)
    LoadChrToIndex("chr/ch23800.itc", 0x12)
    LoadChrToIndex("chr/ch23900.itc", 0x13)
    OP_8E(0x8, "CH22000 上流?若者")
    OP_8E(0x9, "CH22100")
    OP_8E(0xA, "CH22200")
    OP_8E(0xB, "CH22300")
    OP_8E(0xC, "CH22400")
    OP_8E(0xD, "CH22500")
    OP_8E(0xE, "CH22600")
    OP_8E(0xF, "CH22700")
    OP_8E(0x10, "CH22800")
    OP_8E(0x11, "CH22900")
    OP_8E(0x12, "CH23000")
    OP_8E(0x13, "CH23100")
    OP_8E(0x14, "CH23200")
    OP_8E(0x15, "CH23300")
    OP_8E(0x16, "CH23400")
    OP_8E(0x17, "CH23500")
    OP_8E(0x18, "CH23600")
    OP_8E(0x19, "CH23700")
    OP_8E(0x1A, "CH23800")
    OP_8E(0x1B, "CH23900")
    Jump("loc_1406")

    label("loc_DE4")

    LoadChrToIndex("chr/ch24000.itc", 0x0)
    LoadChrToIndex("chr/ch24100.itc", 0x1)
    LoadChrToIndex("chr/ch24200.itc", 0x2)
    LoadChrToIndex("chr/ch24300.itc", 0x3)
    LoadChrToIndex("chr/ch24400.itc", 0x4)
    LoadChrToIndex("chr/ch24500.itc", 0x5)
    LoadChrToIndex("chr/ch24600.itc", 0x6)
    LoadChrToIndex("chr/ch24700.itc", 0x7)
    LoadChrToIndex("chr/ch24800.itc", 0x8)
    LoadChrToIndex("chr/ch24900.itc", 0x9)
    LoadChrToIndex("chr/ch25000.itc", 0xA)
    LoadChrToIndex("chr/ch25100.itc", 0xB)
    LoadChrToIndex("chr/ch25200.itc", 0xC)
    LoadChrToIndex("chr/ch25300.itc", 0xD)
    LoadChrToIndex("chr/ch25400.itc", 0xE)
    LoadChrToIndex("chr/ch25500.itc", 0xF)
    LoadChrToIndex("chr/ch25600.itc", 0x10)
    LoadChrToIndex("chr/ch25700.itc", 0x11)
    LoadChrToIndex("chr/ch25800.itc", 0x12)
    LoadChrToIndex("chr/ch25900.itc", 0x13)
    OP_8E(0x8, "CH24000")
    OP_8E(0x9, "CH24100")
    OP_8E(0xA, "CH24200")
    OP_8E(0xB, "CH24300")
    OP_8E(0xC, "CH24400")
    OP_8E(0xD, "CH24500")
    OP_8E(0xE, "CH24600")
    OP_8E(0xF, "CH24700")
    OP_8E(0x10, "CH24800")
    OP_8E(0x11, "CH24900")
    OP_8E(0x12, "CH25000")
    OP_8E(0x13, "CH25100")
    OP_8E(0x14, "CH25200")
    OP_8E(0x15, "CH25300")
    OP_8E(0x16, "CH25400")
    OP_8E(0x17, "CH25500")
    OP_8E(0x18, "CH25600")
    OP_8E(0x19, "CH25700")
    OP_8E(0x1A, "CH25800")
    OP_8E(0x1B, "CH25900")
    Jump("loc_1406")

    label("loc_F3D")

    LoadChrToIndex("chr/ch26000.itc", 0x0)
    LoadChrToIndex("chr/ch26100.itc", 0x1)
    LoadChrToIndex("chr/ch26200.itc", 0x2)
    LoadChrToIndex("chr/ch26300.itc", 0x3)
    LoadChrToIndex("chr/ch26400.itc", 0x4)
    LoadChrToIndex("chr/ch26500.itc", 0x5)
    LoadChrToIndex("chr/ch26600.itc", 0x6)
    LoadChrToIndex("chr/ch26700.itc", 0x7)
    LoadChrToIndex("chr/ch26800.itc", 0x8)
    LoadChrToIndex("chr/ch26900.itc", 0x9)
    LoadChrToIndex("chr/ch27000.itc", 0xA)
    LoadChrToIndex("chr/ch27100.itc", 0xB)
    LoadChrToIndex("chr/ch27200.itc", 0xC)
    LoadChrToIndex("chr/ch27300.itc", 0xD)
    LoadChrToIndex("chr/ch27400.itc", 0xE)
    LoadChrToIndex("chr/ch27500.itc", 0xF)
    LoadChrToIndex("chr/ch27600.itc", 0x10)
    LoadChrToIndex("chr/ch27700.itc", 0x11)
    LoadChrToIndex("chr/ch27800.itc", 0x12)
    LoadChrToIndex("chr/ch27900.itc", 0x13)
    OP_8E(0x8, "CH26000")
    OP_8E(0x9, "CH26100")
    OP_8E(0xA, "CH26200")
    OP_8E(0xB, "CH26300")
    OP_8E(0xC, "CH26400")
    OP_8E(0xD, "CH26500")
    OP_8E(0xE, "CH26600")
    OP_8E(0xF, "CH26700")
    OP_8E(0x10, "CH26800")
    OP_8E(0x11, "CH26900")
    OP_8E(0x12, "CH27000")
    OP_8E(0x13, "CH27100")
    OP_8E(0x14, "CH27200")
    OP_8E(0x15, "CH27300")
    OP_8E(0x16, "CH27400")
    OP_8E(0x17, "CH27500")
    OP_8E(0x18, "CH27600")
    OP_8E(0x19, "CH27700")
    OP_8E(0x1A, "CH27800")
    OP_8E(0x1B, "CH27900")
    Jump("loc_1406")

    label("loc_1096")

    LoadChrToIndex("chr/ch28000.itc", 0x0)
    LoadChrToIndex("chr/ch28100.itc", 0x1)
    LoadChrToIndex("chr/ch28200.itc", 0x2)
    LoadChrToIndex("chr/ch28300.itc", 0x3)
    LoadChrToIndex("chr/ch28400.itc", 0x4)
    LoadChrToIndex("chr/ch28500.itc", 0x5)
    LoadChrToIndex("chr/ch28600.itc", 0x6)
    LoadChrToIndex("chr/ch28700.itc", 0x7)
    LoadChrToIndex("chr/ch28800.itc", 0x8)
    LoadChrToIndex("chr/ch28900.itc", 0x9)
    LoadChrToIndex("chr/ch29000.itc", 0xA)
    LoadChrToIndex("chr/ch29100.itc", 0xB)
    LoadChrToIndex("chr/ch29200.itc", 0xC)
    LoadChrToIndex("chr/ch29300.itc", 0xD)
    LoadChrToIndex("chr/ch29400.itc", 0xE)
    LoadChrToIndex("chr/ch29500.itc", 0xF)
    LoadChrToIndex("chr/ch29600.itc", 0x10)
    LoadChrToIndex("chr/ch29700.itc", 0x11)
    LoadChrToIndex("chr/ch29800.itc", 0x12)
    LoadChrToIndex("chr/ch29900.itc", 0x13)
    OP_8E(0x8, "CH28000")
    OP_8E(0x9, "CH28100")
    OP_8E(0xA, "CH28200")
    OP_8E(0xB, "CH28300")
    OP_8E(0xC, "CH28400")
    OP_8E(0xD, "CH28500")
    OP_8E(0xE, "CH28600")
    OP_8E(0xF, "CH28700")
    OP_8E(0x10, "CH28800")
    OP_8E(0x11, "CH28900")
    OP_8E(0x12, "CH29000")
    OP_8E(0x13, "CH29100")
    OP_8E(0x14, "CH29200")
    OP_8E(0x15, "CH29300")
    OP_8E(0x16, "CH29400")
    OP_8E(0x17, "CH29500")
    OP_8E(0x18, "CH29600")
    OP_8E(0x19, "CH29700")
    OP_8E(0x1B, "CH29800")
    OP_8E(0x1B, "CH29900")
    Jump("loc_1406")

    label("loc_11EF")

    LoadChrToIndex("chr/ch30000.itc", 0x0)
    LoadChrToIndex("chr/ch30100.itc", 0x1)
    LoadChrToIndex("chr/ch30200.itc", 0x2)
    LoadChrToIndex("chr/ch30300.itc", 0x3)
    LoadChrToIndex("chr/ch30400.itc", 0x4)
    LoadChrToIndex("chr/ch30500.itc", 0x5)
    LoadChrToIndex("chr/ch30600.itc", 0x6)
    LoadChrToIndex("chr/ch30700.itc", 0x7)
    LoadChrToIndex("chr/ch30800.itc", 0x8)
    LoadChrToIndex("chr/ch30900.itc", 0x9)
    LoadChrToIndex("chr/ch31000.itc", 0xA)
    LoadChrToIndex("chr/ch31100.itc", 0xB)
    LoadChrToIndex("chr/ch31200.itc", 0xC)
    LoadChrToIndex("chr/ch31300.itc", 0xD)
    LoadChrToIndex("chr/ch31400.itc", 0xE)
    LoadChrToIndex("chr/ch31500.itc", 0xF)
    LoadChrToIndex("chr/ch31600.itc", 0x10)
    LoadChrToIndex("chr/ch31700.itc", 0x11)
    LoadChrToIndex("chr/ch31800.itc", 0x12)
    LoadChrToIndex("chr/ch31900.itc", 0x13)
    OP_8E(0x8, "CH30000")
    OP_8E(0x9, "CH30100")
    OP_8E(0xA, "CH30200")
    OP_8E(0xB, "CH30300")
    OP_8E(0xC, "CH30400")
    OP_8E(0xD, "CH30500")
    OP_8E(0xE, "CH30600")
    OP_8E(0xF, "CH30700")
    OP_8E(0x10, "CH30800")
    OP_8E(0x11, "CH30900")
    OP_8E(0x12, "CH31000")
    OP_8E(0x13, "CH31100")
    OP_8E(0x14, "CH31200")
    OP_8E(0x15, "CH31300")
    OP_8E(0x16, "CH31400")
    OP_8E(0x17, "CH31500")
    OP_8E(0x18, "CH31600")
    OP_8E(0x19, "CH31700")
    OP_8E(0x1A, "CH31800")
    OP_8E(0x1B, "CH31900")
    Jump("loc_1406")

    label("loc_1348")

    LoadChrToIndex("chr/ch40040.itc", 0x0)
    LoadChrToIndex("chr/ch40041.itc", 0x1)
    LoadChrToIndex("chr/ch40042.itc", 0x2)
    LoadChrToIndex("chr/ch40043.itc", 0x3)
    LoadChrToIndex("chr/ch40044.itc", 0x4)
    LoadChrToIndex("chr/ch40045.itc", 0x5)
    LoadChrToIndex("chr/ch40046.itc", 0x6)
    LoadChrToIndex("chr/ch40047.itc", 0x7)
    LoadChrToIndex("chr/ch40048.itc", 0x8)
    LoadChrToIndex("chr/ch40049.itc", 0x9)
    OP_8E(0x8, "CH40040")
    OP_8E(0x9, "CH40041")
    OP_8E(0xA, "CH40042")
    OP_8E(0xB, "CH40043")
    OP_8E(0xC, "CH40044")
    OP_8E(0xD, "CH40045")
    OP_8E(0xE, "CH40046")
    OP_8E(0xF, "CH40047")
    OP_8E(0x10, "CH40048")
    OP_8E(0x11, "CH40049")
    Jump("loc_1406")

    label("loc_13F7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1406")

    label("loc_1406")

    OP_60(0x0)
    OP_57(0x0)
    OP_DB()
    LoadChrChipPat()
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x8)
    ClearChrFlags(0x16, 0x8)
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)
    ClearChrFlags(0x1A, 0x8)
    ClearChrFlags(0x1B, 0x8)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    OP_49()
    TalkEnd(0xFE)
    Return()

    # Function_2_372 end

    def Function_3_149E(): pass

    label("Function_3_149E")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14C1")
    Sleep(100)
    Jump("loc_155D")

    label("loc_14C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14D8")
    Sleep(200)
    Jump("loc_155D")

    label("loc_14D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14EF")
    Sleep(300)
    Jump("loc_155D")

    label("loc_14EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1506")
    Sleep(400)
    Jump("loc_155D")

    label("loc_1506")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_151D")
    Sleep(500)
    Jump("loc_155D")

    label("loc_151D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1534")
    Sleep(600)
    Jump("loc_155D")

    label("loc_1534")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_154B")
    Sleep(700)
    Jump("loc_155D")

    label("loc_154B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_155D")
    Sleep(800)

    label("loc_155D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15A5")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Jump("loc_155D")

    label("loc_15A5")

    Return()

    # Function_3_149E end

    def Function_4_15A6(): pass

    label("Function_4_15A6")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        "　\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_15A6 end

    def Function_5_15B5(): pass

    label("Function_5_15B5")

    TalkBegin(0xFE)

    #C0002
    ChrTalk(
        0xFE,
        "#0000Fロイド\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "#0100Fエリィ\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "#0200Fティオ\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "#0300Fランディ\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "#0400Fワジ\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "#0500Fノエル曹長\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "#0600Fダドリー捜査官\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "#0700F銀#2Rイン#\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "#0800Fエステル\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "#0900Fヨシュア\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_15B5 end

    def Function_6_1684(): pass

    label("Function_6_1684")

    TalkBegin(0xFE)

    #C0012
    ChrTalk(
        0xFE,
        "#1000Fセルゲイ課長\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "#1100Fキーア\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "#1200Fツァイト\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "#1300Fセシル\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "#1400Fアリオス\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "#1500Fシズク\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "#1600Fヴァルド\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "#1700Fイリア\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "#1800Fリーシャ\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "#1900F受付嬢フラン\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "#2000Fソーニャ副司令\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "#2100Fグレイス\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "#2200Fイアン弁護士\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "#2300Fヨナ\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        "#2400Fヨアヒム准教授\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1684 end

    def Function_7_17C3(): pass

    label("Function_7_17C3")

    TalkBegin(0xFE)

    #C0027
    ChrTalk(
        0xFE,
        "#2500Fマクダエル市長\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "#2600F秘書アーネスト\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "#2700Fハルトマン議長\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "#2800Fディーター総裁\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "#2900Fマリアベル\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "#3000Fマルコーニ会長\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "#3100Fガルシア\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        "#3200Fツァオ\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "#3300Fレン\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "#3400Fキリカ\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "#3500Fレクター\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "#3600Fハロルド\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        "#3700Fソフィア\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "#3800Fコリン\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        "#3900Fヨルグ老人\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_17C3 end

    def Function_8_190E(): pass

    label("Function_8_190E")

    TalkBegin(0xFE)

    #C0042
    ChrTalk(
        0xFE,
        "#5000Fロイド正装\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        "#5100Fロイド正装眼鏡\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        "#5200Fロイド部屋着\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        "#5300Fエリィ正装\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        "#5400Fティオ正装\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "#5500Fティオ部屋着\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "#5600Fランディ正装\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "#5700Fワジ正装\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "#5800Fキーア私服\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "#5900Fセシル私服\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "#6000Fシズク外出着\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "#6100Fイリア舞台服\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        "#6200Fリーシャ舞台服\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "#6300Fノエル私服\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "#6400Fフラン私服\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        "#6500Fマクダエル部屋着\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "#6600Fアーネスト魔人化\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "#6700Fヨアヒム司祭服\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "#6800Fヨアヒム司祭服白髪\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_190E end

    def Function_9_1ADF(): pass

    label("Function_9_1ADF")

    EventBegin(0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00000.itp")

    #C0061
    ChrTalk(
        0xFE,
        "#0000Fロイド\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0062
    ChrTalk(
        0xFE,
        "#0001F#1P＃１Ｐ\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        "#0002F#2P＃２Ｐ\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        "#0003F#3P＃３Ｐ\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        "#0004F#4P＃４Ｐ\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        "#0005F#5P＃５Ｐ\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "#0006F#6P＃６Ｐ\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        "#0007F#7P＃７Ｐ\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "#0008F#8P＃８Ｐ\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "#0009F#9P＃９Ｐ\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "#0009F#10P＃１０Ｐ\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "#0009F#11P＃１１Ｐ\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "#0009F#12P＃１２Ｐ\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "#0009F#13P＃１３Ｐ\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "#0009F#14P＃１４Ｐ\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "#0009F#15P＃１５Ｐ\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "#0009F#16P＃１６Ｐ\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_9_1ADF end

    def Function_10_1CE6(): pass

    label("Function_10_1CE6")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C50")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ロイド\x01",              # 0
            "エリィ\x01",              # 1
            "ティオ\x01",              # 2
            "ランディ\x01",            # 3
            "ワジ\x01",                # 4
            "ノエル曹長\x01",          # 5
            "ダドリー捜査官\x01",      # 6
            "銀\x01",                  # 7
            "エステル\x01",            # 8
            "ヨシュア\x01",            # 9
            "キャンセル\x01",          # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1DB5"),
        (1, "loc_1F3F"),
        (2, "loc_20E3"),
        (3, "loc_228B"),
        (4, "loc_2419"),
        (5, "loc_2573"),
        (6, "loc_26DD"),
        (7, "loc_2839"),
        (8, "loc_291F"),
        (9, "loc_2AC9"),
        (SWITCH_DEFAULT, "loc_2C4B"),
    )


    label("loc_1DB5")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0078
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0079
    ChrTalk(
        0xFE,
        "#0000F通常\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        "#0001F真剣\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "#0002F微笑\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "#0003F瞑目\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "#0004F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "#0005F驚き\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        "#0006F溜息\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "#0007F叫び\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        "#0008F悲哀\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "#0009F笑い\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "#0010F苦痛\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        "#0011F慌て\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "#0012F苦笑\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_1F3F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00100.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0092
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0093
    ChrTalk(
        0xFE,
        "#0100F通常\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "#0101F真剣\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        "#0102F微笑\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        "#0103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        "#0104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "#0105F驚き\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        "#0106F溜息\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        "#0107F叫び\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        "#0108F悲哀\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        "#0109F笑い\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        "#0110F苦痛\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "#0111Fジト目\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        "#0112F照れ驚き\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "#0113F照れ瞑目\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_20E3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00200.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0107
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0108
    ChrTalk(
        0xFE,
        "#0200F通常\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "#0201F真剣\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        "#0202F微笑\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        "#0203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        "#0204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "#0205F驚き\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        "#0206F溜息\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "#0207F叫び\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        "#0208F悲哀\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "#0209F笑い\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        "#0210F苦痛\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        "#0211Fジト目\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        "#0212F泣き笑い\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "#0213F泣き笑い瞑目\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_228B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00300.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0122
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0123
    ChrTalk(
        0xFE,
        "#0300F通常\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "#0301F真剣\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        "#0302F微笑\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        "#0303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "#0304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        "#0305F驚き\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        "#0306F溜息\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        "#0307F叫び\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        "#0308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        "#0309F笑い\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "#0310F苦痛\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        "#0311F殺意\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "#0312F殺意微笑\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_2419")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00400.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0136
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0137
    ChrTalk(
        0xFE,
        "#0400F通常\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        "#0401F真剣\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        "#0402F微笑\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "#0403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "#0404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        "#0405F驚き\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        "#0406F溜息\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        "#0407F叫び\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        "#0409F笑い\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        "#0410F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_2573")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00500.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0147
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0148
    ChrTalk(
        0xFE,
        "#0500F通常\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        "#0501F真剣\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        "#0502F微笑\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "#0503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "#0504F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        "#0505F驚き\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "#0506F溜息\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        "#0507F叫び\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "#0508F悲哀\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        "#0509F笑い\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        "#0510F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_26DD")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00600.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0159
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0160
    ChrTalk(
        0xFE,
        "#0600F通常\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "#0601F真剣\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        "#0602F微笑\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        "#0603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        "#0604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        "#0605F驚き\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        "#0606F溜息\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "#0607F叫び\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "#0608F悲哀\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "#0610F悔しい\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_2839")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00700.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0170
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0171
    ChrTalk(
        0xFE,
        "#0700F通常\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        "#0702F微笑\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        "#0707F叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_291F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00800.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0174
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0175
    ChrTalk(
        0xFE,
        "#0800F通常\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        "#0801F真剣\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        "#0802F微笑\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        "#0803F瞑目\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "#0804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "#0805F驚き\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        "#0806F溜息\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "#0807F叫び\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        "#0808F悲哀\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        "#0809F笑い\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        "#0810F泣き瞑目\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "#0811F泣き笑い\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "#0812F泣き笑い瞑目\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        "#0813F驚愕\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_2AC9")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00900.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0189
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0190
    ChrTalk(
        0xFE,
        "#0900F通常\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        "#0901F真剣\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        "#0902F微笑\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "#0903F瞑目\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        "#0904F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "#0905F驚き\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        "#0906F溜息\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        "#0907F叫び\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        "#0908F悲哀\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        "#0909F笑い\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        "#0910F感極まる\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        "#0911F泣き笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_2C4B")

    Jump("loc_1CF2")

    label("loc_2C50")

    EventEnd(0x1)
    Return()

    # Function_10_1CE6 end

    def Function_11_2C53(): pass

    label("Function_11_2C53")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FD8")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "セルゲイ課長\x01",        # 0
            "キーア\x01",              # 1
            "ツァイト\x01",            # 2
            "セシル\x01",              # 3
            "アリオス\x01",            # 4
            "シズク\x01",              # 5
            "ヴァルド\x01",            # 6
            "イリア\x01",              # 7
            "リーシャ\x01",            # 8
            "受付嬢フラン\x01",        # 9
            "ソーニャ副司令\x01",      # 10
            "グレイス\x01",            # 11
            "イアン弁護士\x01",        # 12
            "ヨナ\x01",                # 13
            "ヨアヒム准教授\x01",      # 14
            "キャンセル\x01",          # 15
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D81"),
        (1, "loc_2EC7"),
        (2, "loc_307B"),
        (3, "loc_3171"),
        (4, "loc_32BB"),
        (5, "loc_33E5"),
        (6, "loc_34EB"),
        (7, "loc_3625"),
        (8, "loc_375F"),
        (9, "loc_38A9"),
        (10, "loc_39E3"),
        (11, "loc_3B0D"),
        (12, "loc_3C47"),
        (13, "loc_3D4D"),
        (14, "loc_3EBD"),
        (SWITCH_DEFAULT, "loc_3FD3"),
    )


    label("loc_2D81")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0202
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0203
    ChrTalk(
        0xFE,
        "#1000F通常\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        "#1001F真剣\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        "#1002F微笑\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        "#1003F瞑目\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "#1005F驚き\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        "#1006F溜息\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        "#1007F叫び\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        "#1009F笑い\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        "#1010F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_2EC7")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01100.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0212
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0213
    ChrTalk(
        0xFE,
        "#1100F通常\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        "#1101F真剣\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        "#1102F微笑\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "#1103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        "#1104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "#1105F驚き\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        "#1106F溜息\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        "#1107F叫び\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        "#1108F悲哀\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "#1109F笑い\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "#1110F通常口開き\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        "#1111F思案\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        "#1112F不安\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        "#1113F睡眠\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        "#1114F睡眠苦悶\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_307B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01200.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0228
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0229
    ChrTalk(
        0xFE,
        "#1200F通常\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        "#1201F真剣\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        "#1203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        "#1207F叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_3171")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01300.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0233
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0234
    ChrTalk(
        0xFE,
        "#1300F通常\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        "#1301F真剣\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        "#1302F微笑\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        "#1303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        "#1304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        "#1305F驚き\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        "#1306F溜息\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        "#1308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        "#1309F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_32BB")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01400.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0243
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0244
    ChrTalk(
        0xFE,
        "#1400F通常\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        "#1401F真剣\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        "#1402F微笑\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        "#1403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        "#1404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        "#1405F驚き\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        "#1407F叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_33E5")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01500.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0251
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0252
    ChrTalk(
        0xFE,
        "#1500F通常\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "#1501F真剣\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        "#1502F微笑\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        "#1505F驚き\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        "#1508F悲哀\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_34EB")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01600.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0257
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0258
    ChrTalk(
        0xFE,
        "#1600F通常\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        "#1601F真剣\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        "#1602F微笑\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        "#1603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        "#1604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        "#1605F驚き\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        "#1607F叫び\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        "#1609F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_3625")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01700.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0266
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0267
    ChrTalk(
        0xFE,
        "#1700F通常\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        "#1701F真剣\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        "#1702F微笑\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        "#1703F瞑目\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        "#1704F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        "#1705F驚き\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        "#1706F溜息\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        "#1709F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_375F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01800.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0275
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0276
    ChrTalk(
        0xFE,
        "#1800F通常\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        "#1801F真剣\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        "#1802F微笑\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        "#1803F瞑目\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        "#1804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        "#1805F驚き\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        "#1806F溜息\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        "#1808F悲哀\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        "#1809F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_38A9")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01900.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0285
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0286
    ChrTalk(
        0xFE,
        "#1900F通常\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        "#1901F真剣\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        "#1902F微笑\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        "#1903F瞑目\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        "#1904F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        "#1905F驚き\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        "#1906F溜息\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        "#1909F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_39E3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0294
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0295
    ChrTalk(
        0xFE,
        "#2000F通常\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        "#2001F真剣\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        "#2002F微笑\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        "#2003F瞑目\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        "#2004F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        "#2005F驚き\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        "#2006F溜息\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_3B0D")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0302
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0303
    ChrTalk(
        0xFE,
        "#2100F通常\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        "#2101F真剣\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        "#2102F微笑\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        "#2103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        "#2104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        "#2105F驚き\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        "#2106F溜息\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        "#2109F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_3C47")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02200.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0311
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0312
    ChrTalk(
        0xFE,
        "#2200F通常\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        "#2201F真剣\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        "#2202F微笑\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        "#2203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        "#2205F驚き\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_3D4D")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02300.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0317
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0318
    ChrTalk(
        0xFE,
        "#2300F通常\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        "#2301F真剣\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "#2302F微笑\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        "#2303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        "#2304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        "#2305F驚き\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        "#2306F溜息\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        "#2307F叫び\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "#2309F笑い\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        "#2310F悔しい\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        "#2311F瞑目叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_3EBD")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02400.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0329
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0330
    ChrTalk(
        0xFE,
        "#2400F通常\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        "#2401F真剣\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        "#2403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        "#2405F驚き\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        "#2406F溜息\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        "#2409F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FD3")

    label("loc_3FD3")

    Jump("loc_2C5F")

    label("loc_3FD8")

    EventEnd(0x1)
    Return()

    # Function_11_2C53 end

    def Function_12_3FDB(): pass

    label("Function_12_3FDB")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3FE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5320")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "マクダエル市長\x01",      # 0
            "秘書アーネスト\x01",      # 1
            "ハルトマン議長\x01",      # 2
            "ディーター総裁\x01",      # 3
            "マリアベル\x01",          # 4
            "マルコーニ会長\x01",      # 5
            "ガルシア\x01",            # 6
            "ツァオ\x01",              # 7
            "レン\x01",                # 8
            "キリカ\x01",              # 9
            "レクター\x01",            # 10
            "ハロルド\x01",            # 11
            "ソフィア\x01",            # 12
            "コリン\x01",              # 13
            "ヨルグ老人\x01",          # 14
            "キャンセル\x01",          # 15
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4115"),
        (1, "loc_422B"),
        (2, "loc_43C1"),
        (3, "loc_44C7"),
        (4, "loc_45F1"),
        (5, "loc_472B"),
        (6, "loc_4855"),
        (7, "loc_498F"),
        (8, "loc_4AC9"),
        (9, "loc_4C7F"),
        (10, "loc_4D99"),
        (11, "loc_4EF3"),
        (12, "loc_5009"),
        (13, "loc_511F"),
        (14, "loc_5235"),
        (SWITCH_DEFAULT, "loc_531B"),
    )


    label("loc_4115")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02500.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0336
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0337
    ChrTalk(
        0xFE,
        "#2500F通常\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        "#2501F真剣\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        "#2503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        "#2505F驚き\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        "#2507F叫び\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        "#2509F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_422B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02600.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0343
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0344
    ChrTalk(
        0xFE,
        "#2600F通常\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        "#2601F真剣\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        "#2603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        "#2604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        "#2605F驚き\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        "#2606F溜息\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        "#2610F通常\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        "#2611F悪役通常\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        "#2612F悪役真剣\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        "#2613F悪役瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        "#2614F悪役叫び\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        "#2615F悪役瞑目叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_43C1")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02700.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0356
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0357
    ChrTalk(
        0xFE,
        "#2700F通常\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        "#2701F真剣\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        "#2702F微笑\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        "#2703F瞑目\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        "#2705F驚き\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_44C7")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02800.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0362
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0363
    ChrTalk(
        0xFE,
        "#2800F通常\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        "#2801F真剣\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        "#2803F瞑目\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        "#2804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        "#2805F驚き\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        "#2806F溜息\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        "#2809F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_45F1")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02900.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0370
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0371
    ChrTalk(
        0xFE,
        "#2900F通常\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        "#2901F真剣\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        "#2902F微笑\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        "#2903F瞑目\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        "#2904F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        "#2905F驚き\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        "#2906F溜息\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        "#2909F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_472B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0379
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0380
    ChrTalk(
        0xFE,
        "#3000F通常\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        "#3001F真剣\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        "#3002F微笑\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        "#3003F瞑目\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        "#3004F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        "#3005F驚き\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        "#3007F叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_4855")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0387
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0388
    ChrTalk(
        0xFE,
        "#3100F通常\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        "#3101F真剣\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        "#3102F微笑\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        "#3103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        "#3104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        "#3105F驚き\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        "#3107F叫び\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        "#3109F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_498F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03200.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0396
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0397
    ChrTalk(
        0xFE,
        "#3200F通常\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        "#3201F真剣\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        "#3202F微笑\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        "#3203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        "#3204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        "#3205F驚き\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        "#3206F溜息\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        "#3209F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_4AC9")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0405
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0406
    ChrTalk(
        0xFE,
        "#3300F通常\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        "#3301F真剣\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        "#3302F微笑\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        "#3303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        "#3304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        "#3305F驚き\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        "#3306F溜息\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        "#3307F叫び\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        "#3308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        "#3309F笑い\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        "#3310F瞑目叫び\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        "#3311F驚愕\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        "#3312F泣き\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        "#3313F泣き瞑目\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        "#3314F泣き笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_4C7F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03400.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0421
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0422
    ChrTalk(
        0xFE,
        "#3400F通常\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        "#3401F真剣\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        "#3402F微笑\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        "#3403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        "#3404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        "#3405F驚き\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_4D99")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03500.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0428
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0429
    ChrTalk(
        0xFE,
        "#3500F通常\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        "#3501F真剣\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        "#3502F微笑\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        "#3503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        "#3504F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xFE,
        "#3505F驚き\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        "#3506F溜息\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xFE,
        "#3507F叫び\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        "#3509F笑い\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        "#3510F思案\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_4EF3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03600.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0439
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0440
    ChrTalk(
        0xFE,
        "#3600F通常\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xFE,
        "#3601F真剣\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        "#3603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xFE,
        "#3605F驚き\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        "#3608F悲哀\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xFE,
        "#3609F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_5009")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03700.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0446
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0447
    ChrTalk(
        0xFE,
        "#3700F通常\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        "#3701F真剣\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        "#3707F叫び\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        "#3708F悲哀\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        "#3709F笑い\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        "#3710F悲嘆\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_511F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03800.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0453
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0454
    ChrTalk(
        0xFE,
        "#3800F通常\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xFE,
        "#3802F微笑\x02",
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xFE,
        "#3805F驚き\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        "#3809F笑い\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xFE,
        "#3810F呆然\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xFE,
        "#3811F泣き\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_5235")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03900.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0460
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0461
    ChrTalk(
        0xFE,
        "#3900F通常\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        "#3901F真剣\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xFE,
        "#3903F瞑目\x02",
    )

    CloseMessageWindow()
    Jump("loc_531B")

    label("loc_531B")

    Jump("loc_3FE7")

    label("loc_5320")

    EventEnd(0x1)
    Return()

    # Function_12_3FDB end

    def Function_13_5323(): pass

    label("Function_13_5323")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_532F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63A3")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ロイド正装\x01",          # 0
            "ロイド正装眼鏡\x01",      # 1
            "ロイド部屋着\x01",        # 2
            "エリィ正装\x01",          # 3
            "ティオ正装\x01",          # 4
            "ティオ部屋着\x01",        # 5
            "ランディ正装\x01",        # 6
            "ワジ正装\x01",            # 7
            "キーア私服\x01",          # 8
            "セシル私服\x01",          # 9
            "キャンセル\x01",          # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5416"),
        (1, "loc_55A0"),
        (2, "loc_572A"),
        (3, "loc_58B4"),
        (4, "loc_5A58"),
        (5, "loc_5C00"),
        (6, "loc_5DA8"),
        (7, "loc_5F36"),
        (8, "loc_60A0"),
        (9, "loc_6254"),
        (SWITCH_DEFAULT, "loc_639E"),
    )


    label("loc_5416")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0464
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0465
    ChrTalk(
        0xFE,
        "#5000F通常\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xFE,
        "#5001F真剣\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        "#5002F微笑\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xFE,
        "#5003F瞑目\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xFE,
        "#5004F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xFE,
        "#5005F驚き\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0xFE,
        "#5006F溜息\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xFE,
        "#5007F叫び\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xFE,
        "#5008F悲哀\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xFE,
        "#5009F笑い\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0xFE,
        "#5010F苦痛\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xFE,
        "#5011F慌て\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xFE,
        "#5012F苦笑\x02",
    )

    CloseMessageWindow()
    Jump("loc_639E")

    label("loc_55A0")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05100.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0478
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0479
    ChrTalk(
        0xFE,
        "#5100F通常\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xFE,
        "#5101F真剣\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xFE,
        "#5102F微笑\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xFE,
        "#5103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xFE,
        "#5104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xFE,
        "#5105F驚き\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xFE,
        "#5106F溜息\x02",
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xFE,
        "#5107F叫び\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0xFE,
        "#5108F悲哀\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xFE,
        "#5109F笑い\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xFE,
        "#5110F苦痛\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xFE,
        "#5111F慌て\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xFE,
        "#5112F苦笑\x02",
    )

    CloseMessageWindow()
    Jump("loc_639E")

    label("loc_572A")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05200.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0492
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0493
    ChrTalk(
        0xFE,
        "#5200F通常\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        "#5201F真剣\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xFE,
        "#5202F微笑\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xFE,
        "#5203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xFE,
        "#5204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xFE,
        "#5205F驚き\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xFE,
        "#5206F溜息\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xFE,
        "#5207F叫び\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xFE,
        "#5208F悲哀\x02",
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xFE,
        "#5209F笑い\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xFE,
        "#5210F苦痛\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xFE,
        "#5211F慌て\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xFE,
        "#5212F苦笑\x02",
    )

    CloseMessageWindow()
    Jump("loc_639E")

    label("loc_58B4")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05300.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0506
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0507
    ChrTalk(
        0xFE,
        "#5300F通常\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xFE,
        "#5301F真剣\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xFE,
        "#5302F微笑\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xFE,
        "#5303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xFE,
        "#5304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xFE,
        "#5305F驚き\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xFE,
        "#5306F溜息\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xFE,
        "#5307F叫び\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xFE,
        "#5308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xFE,
        "#5309F笑い\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xFE,
        "#5310F苦痛\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xFE,
        "#5311Fジト目\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        "#5312F照れ驚き\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xFE,
        "#5313F照れ瞑目\x02",
    )

    CloseMessageWindow()
    Jump("loc_639E")

    label("loc_5A58")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05400.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0521
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0522
    ChrTalk(
        0xFE,
        "#5400F通常\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xFE,
        "#5401F真剣\x02",
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xFE,
        "#5402F微笑\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        "#5403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xFE,
        "#5404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xFE,
        "#5405F驚き\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xFE,
        "#5406F溜息\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xFE,
        "#5407F叫び\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xFE,
        "#5408F悲哀\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xFE,
        "#5409F笑い\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xFE,
        "#5410F苦痛\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xFE,
        "#5411Fジト目\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xFE,
        "#5412F泣き笑い\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xFE,
        "#5412F泣き笑い瞑目\x02",
    )

    CloseMessageWindow()
    Jump("loc_639E")

    label("loc_5C00")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05500.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0536
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0537
    ChrTalk(
        0xFE,
        "#5500F通常\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xFE,
        "#5501F真剣\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xFE,
        "#5502F微笑\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xFE,
        "#5503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xFE,
        "#5504F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xFE,
        "#5505F驚き\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xFE,
        "#5506F溜息\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xFE,
        "#5507F叫び\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xFE,
        "#5508F悲哀\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xFE,
        "#5509F笑い\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xFE,
        "#5510F苦痛\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xFE,
        "#5511Fジト目\x02",
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xFE,
        "#5512F泣き笑い\x02",
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xFE,
        "#5512F泣き笑い瞑目\x02",
    )

    CloseMessageWindow()
    Jump("loc_639E")

    label("loc_5DA8")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05600.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0551
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0552
    ChrTalk(
        0xFE,
        "#5600F通常\x02",
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xFE,
        "#5601F真剣\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xFE,
        "#5602F微笑\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xFE,
        "#5603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xFE,
        "#5604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xFE,
        "#5605F驚き\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xFE,
        "#5606F溜息\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xFE,
        "#5607F叫び\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xFE,
        "#5608F悲哀\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xFE,
        "#5609F笑い\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xFE,
        "#5610F苦痛\x02",
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xFE,
        "#5611F殺意\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xFE,
        "#5612F殺意微笑\x02",
    )

    CloseMessageWindow()
    Jump("loc_639E")

    label("loc_5F36")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05700.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0565
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0566
    ChrTalk(
        0xFE,
        "#5700F通常\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xFE,
        "#5701F真剣\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0xFE,
        "#5702F微笑\x02",
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xFE,
        "#5703F瞑目\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xFE,
        "#5704F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xFE,
        "#5705F驚き\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        "#5706F溜息\x02",
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xFE,
        "#5707F叫び\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xFE,
        "#5708F悲哀\x02",
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xFE,
        "#5709F笑い\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xFE,
        "#5710F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_639E")

    label("loc_60A0")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05800.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0577
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0578
    ChrTalk(
        0xFE,
        "#5800F通常\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0xFE,
        "#5801F真剣\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0xFE,
        "#5802F微笑\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xFE,
        "#5803F瞑目\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        "#5804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0xFE,
        "#5805F驚き\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xFE,
        "#5806F溜息\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xFE,
        "#5807F叫び\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xFE,
        "#5808F悲哀\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xFE,
        "#5809F笑い\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xFE,
        "#5810F通常口開き\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xFE,
        "#5811F思案\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xFE,
        "#5812F不安\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xFE,
        "#5813F睡眠\x02",
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0xFE,
        "#5814F睡眠苦悶\x02",
    )

    CloseMessageWindow()
    Jump("loc_639E")

    label("loc_6254")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05900.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0593
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0594
    ChrTalk(
        0xFE,
        "#5900F通常\x02",
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xFE,
        "#5901F真剣\x02",
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xFE,
        "#5902F微笑\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0xFE,
        "#5903F瞑目\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xFE,
        "#5904F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xFE,
        "#5905F驚き\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0xFE,
        "#5906F溜息\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        "#5908F悲哀\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0xFE,
        "#5909F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_639E")

    label("loc_639E")

    Jump("loc_532F")

    label("loc_63A3")

    EventEnd(0x1)
    Return()

    # Function_13_5323 end

    def Function_14_63A6(): pass

    label("Function_14_63A6")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_63B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_702B")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "シズク外出着\x01",            # 0
            "イリア舞台服\x01",            # 1
            "リーシャ舞台服\x01",          # 2
            "ノエル私服\x01",              # 3
            "フラン私服\x01",              # 4
            "マクダエル部屋着\x01",        # 5
            "アーネスト魔人化\x01",        # 6
            "ヨアヒム司祭服\x01",          # 7
            "ヨアヒム司祭服白髪\x01",      # 8
            "キャンセル\x01",              # 9
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_64A0"),
        (1, "loc_65A6"),
        (2, "loc_66E0"),
        (3, "loc_683E"),
        (4, "loc_69A8"),
        (5, "loc_6AE2"),
        (6, "loc_6BF8"),
        (7, "loc_6D8E"),
        (8, "loc_6EDA"),
        (SWITCH_DEFAULT, "loc_7026"),
    )


    label("loc_64A0")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0603
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0604
    ChrTalk(
        0xFE,
        "#6000F通常\x02",
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xFE,
        "#6001F真剣\x02",
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xFE,
        "#6002F微笑\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xFE,
        "#6005F驚き\x02",
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0xFE,
        "#6008F悲哀\x02",
    )

    CloseMessageWindow()
    Jump("loc_7026")

    label("loc_65A6")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06100.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0609
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0610
    ChrTalk(
        0xFE,
        "#6100F通常\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0xFE,
        "#6101F真剣\x02",
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xFE,
        "#6102F微笑\x02",
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xFE,
        "#6103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xFE,
        "#6104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xFE,
        "#6105F驚き\x02",
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0xFE,
        "#6106F溜息\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        "#6109F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_7026")

    label("loc_66E0")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06200.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0618
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0619
    ChrTalk(
        0xFE,
        "#6200F通常\x02",
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0xFE,
        "#6201F真剣\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xFE,
        "#6202F微笑\x02",
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xFE,
        "#6203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0xFE,
        "#6204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0xFE,
        "#6205F驚き\x02",
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0xFE,
        "#6206F溜息\x02",
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xFE,
        "#6208F悲哀\x02",
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0xFE,
        "#6209F笑い\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xFE,
        "#6210F憂い笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_7026")

    label("loc_683E")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06300.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0629
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0630
    ChrTalk(
        0xFE,
        "#6300F通常\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0xFE,
        "#6301F真剣\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xFE,
        "#6302F微笑\x02",
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xFE,
        "#6303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xFE,
        "#6304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xFE,
        "#6305F驚き\x02",
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xFE,
        "#6306F溜息\x02",
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0xFE,
        "#6307F叫び\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0xFE,
        "#6308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0xFE,
        "#6309F笑い\x02",
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0xFE,
        "#6310F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_7026")

    label("loc_69A8")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06400.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0641
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0642
    ChrTalk(
        0xFE,
        "#6400F通常\x02",
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0xFE,
        "#6401F真剣\x02",
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0xFE,
        "#6402F微笑\x02",
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0xFE,
        "#6403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0xFE,
        "#6404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xFE,
        "#6405F驚き\x02",
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0xFE,
        "#6406F溜息\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xFE,
        "#6409F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_7026")

    label("loc_6AE2")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06500.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0650
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0651
    ChrTalk(
        0xFE,
        "#6500F通常\x02",
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0xFE,
        "#6501F真剣\x02",
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xFE,
        "#6503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0xFE,
        "#6505F驚き\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0xFE,
        "#6507F叫び\x02",
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0xFE,
        "#6509F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_7026")

    label("loc_6BF8")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06600.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0657
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0658
    ChrTalk(
        0xFE,
        "#6600F通常\x02",
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xFE,
        "#6601F真剣\x02",
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0xFE,
        "#6603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0xFE,
        "#6604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0xFE,
        "#6605F驚き\x02",
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0xFE,
        "#6606F溜息\x02",
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0xFE,
        "#6610F通常\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0xFE,
        "#6611F悪役通常\x02",
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0xFE,
        "#6612F悪役真剣\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0xFE,
        "#6613F悪役瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0xFE,
        "#6614F悪役叫び\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0xFE,
        "#6615F悪役瞑目叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_7026")

    label("loc_6D8E")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06700.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0670
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0671
    ChrTalk(
        0xFE,
        "#6700F通常\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0xFE,
        "#6701F真剣\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0xFE,
        "#6703F瞑目\x02",
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0xFE,
        "#6704F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0xFE,
        "#6705F驚き\x02",
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0xFE,
        "#6707F叫び\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0xFE,
        "#6709F笑い\x02",
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0xFE,
        "#6710F愕然\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0xFE,
        "#6711F悔しい\x02",
    )

    CloseMessageWindow()
    Jump("loc_7026")

    label("loc_6EDA")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06800.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0680
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0681
    ChrTalk(
        0xFE,
        "#6800F通常\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0xFE,
        "#6801F真剣\x02",
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0xFE,
        "#6803F瞑目\x02",
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0xFE,
        "#6804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0xFE,
        "#6805F驚き\x02",
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0xFE,
        "#6807F叫び\x02",
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0xFE,
        "#6809F笑い\x02",
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0xFE,
        "#6810F愕然\x02",
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0xFE,
        "#6811F悔しい\x02",
    )

    CloseMessageWindow()
    Jump("loc_7026")

    label("loc_7026")

    Jump("loc_63B2")

    label("loc_702B")

    EventEnd(0x1)
    Return()

    # Function_14_63A6 end

    SaveToFile()

Try(main)
