from ..shared import sameVrsIndicator
from ..backend import rtTrns

from .aggregates_test import *


jinn_iblis_dhurriya = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "*rr", 
                    "strTyp": "root",
            "wrdDisPos": 35,
                },
                {
                    "stri": "<iboliys", 
                    "strTyp": "lem",
            "wrdDisPos": 35,
                },
            ],
        },
    ],
]

jinn_iblis = [
    *jinn_iblis_dhurriya,
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "<iboliys", 
                    "strTyp": "lem",
            "wrdDisPos": 30,
                },
            ],
        },
    ],
]

iblis_shaytan = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n",
                    "strTyp": "lem",
                },
                {
                    "stri": "<iboliys", 
                    "strTyp": "lem",
            "wrdDisPos": 45
                },
                {
                    "stri": "wEd", 
                    "strTyp": "lem",
            "wrdDisPos": 45
                },
            ],
        },
    ],
]

iblis_nar = [
    [
        {
            "strL": [
                {
                    "stri": "naAr",
                    "strTyp": "lem",
                },
                {
                    "stri": "<iboliys", 
                    "strTyp": "lem",
            "wrdDisPos": 20
                },
            ],
        },
    ],
]

iblis_malak = [
    [
        {
            "strL": [
                {
                    "stri": "malak", 
                    "strTyp": "lem",
                },
                {
                    "stri": "<iboliys",
                    "strTyp": "lem",
            "wrdDisPos": 35
                },
            ],
        },
    ],
]

iblis = [
    *iblis_nar,
    *iblis_malak,
    *jinn_iblis,
]

jinn_malak = [
    *iblis_malak,
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "malak", 
                    "strTyp": "lem",
            "wrdDisPos": 35
                },
            ],
        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "jin~ap",
                    "strTyp": "lem",
                },
                {
                    "stri": "malak", 
                    "strTyp": "lem",
            "wrdDisPos": 35
                },
            ],
        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "jaA^n~",
                    "strTyp": "lem",
                },
                {
                    "stri": "malak", 
                    "strTyp": "lem",
            "wrdDisPos": 35
                },
            ],
        },
    ],
]

untha_dua_shirk = [
    [
        {
            "strL": [
                {
                    "stri": "$rk",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": ">unvaY`", 
                    "strTyp": "lem",
            "wrdDisPos": 11
                },
                {
                    "stri": "dEw",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 11
                },
                {
                    "stri": "duwn", 
                    "strTyp": "lem",
            "wrdDisPos": 11
                },
            ],
        },
    ],
]

lat_uzza_manat_untha_ism = [
    [
    {
      "strL": [
                {
                    "stri": ">unvaY`", 
                    "strTyp": "lem",
                },
                {
                    "stri": "smw", 
                    "strTyp": "root",
      "wrdDisPos": 75,
                    # "poSp": "N",
                    # "frm": "ii"
                },
        { 
            "stri": goddess, 
            "strTyp":"lem",  
            "flt": "",
      "wrdDisPos": 75,
            },
                {
                    "stri": "A^baA'", 
                    "strTyp": "lem",
      "wrdDisPos": 75,
                },
                {
                    "stri": "Znn", 
                    "strTyp": "root",
                    # "poSp": "N",
                    # "frm": "ii"
      "wrdDisPos": 75,
                },
                {
                    "stri": "hwy", 
                    "strTyp": "root",
                    # "poSp": "N",
                    # "frm": "ii"
      "wrdDisPos": 75,
                },
      ],
    },
  ]
    for goddess in ["{ll~a`t","{loEuz~aY`","manaw`p"]
]

lat_uzza_manat_untha_ism_malak = [
    [
    {
      "strL": optO[0]["strL"] + [ {"stri": "malak","strTyp": "lem",},]
    },
  ]
    for optO in lat_uzza_manat_untha_ism
]

malak_tasmiya_untha = [
    *lat_uzza_manat_untha_ism_malak,
    # [
    #     {
    #         "strL": [
    #             {
    #                 "stri": "malak",
    #                 "strTyp": "lem",
    #             },
    #         ],
    #         "wrdDisPos": 20,
    #     },
    # ],
]

tasmiya_untha = [
    # *lat_uzza_manat_untha_ism,
    *lat_uzza_manat_untha_ism_malak,
]

ism_liqab = [
        [
    {
      "strL": [
                {
                    "stri": "smw", 
                    "strTyp": "root",
                    # "poSp": "N",
                    # "frm": "ii"
                },
                {
      "wrdDisPos": 10,
                    "stri": "lqb", 
                    "strTyp": "root",
                    # "frm": "ii"
                },
                {
      "wrdDisPos": 10,
                    "stri": "fsq", 
                    "strTyp": "root",
                    # "frm": "ii"
                },
      ],
    },
  ],
]

# ism_jdl = [
#         [
#     {
#       "wrdDisPos": 10,
#       "strL": [
#                 {
#                     "stri": "smw", 
#                     "strTyp": "root",
#                     "poSp": "V",
#                     "frm": "ii"
#                 },
#                 {
#                     "stri": "jdl", 
#                     "strTyp": "root",
#                     # "frm": "ii"
#                 },
#       ],
#     },
#   ],
# ]

tasmiya_abd = [
    # *malak_tasmiya_untha,
        [
    {
      "strL": [
                {
                    "stri": "A^baA'", 
                    "strTyp": "lem",
                },
                {
      "wrdDisPos": 20,
                    "stri": "smw", 
                    "strTyp": "root",
                    "poSp": "V",
                    "frm": "ii"
                },
                {
      "wrdDisPos": 20,
                    "stri": "Ebd", 
                    "strTyp": "root",
                    # "frm": "ii"
                },
      ],
    },
  ],
        [
    {
      "strL": [
                {
                    "stri": "$ariyk", 
                    "strTyp": "lem",
                },
                {
      "wrdDisPos": 10,
                    "stri": "smw", 
                    "strTyp": "root",
                    "poSp": "V",
                    "frm": "ii"
                },
      ],
    },
  ],
    
]

tasmiya_abd_malak_untha = [
    *malak_tasmiya_untha,
    *tasmiya_untha,
    *tasmiya_abd,
]

malak_banat = [
    [
        {
            "strL": [
                {
                    "stri": ">unvaY`", 
                    "strTyp": "lem",
                },
                {
            "wrdDisPos": 50,
                    "stri": "malak",
                    "strTyp": "lem",
                },
                {
            "wrdDisPos": 50,
                    "stri": "banaAt", 
                    "strTyp": "lem",
                },
            ],
        },
    ],
]

malak_untha = [
    *malak_tasmiya_untha,
    *malak_banat,
    [
        {
            "strL": [
                {
                    "stri": "malak",
                    "strTyp": "lem",
                },
                {
                    "stri": ">unvaY`", 
                    "strTyp": "lem",
            "wrdDisPos": 20,
                },
            ],
        },
    ],

]

malak_ism = [
    *malak_tasmiya_untha,
            [
    {
      
      "strL": [
        { "stri": "jiboriyl", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "miykaY`l", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "ma`lik2", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "ha`ruwt", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "ma`ruwt", "strTyp": "lem",},
      ],
    },
  ],
]

malak_khazanah_zabaniya = [
            [
    {
      
      "strL": [
        { "stri": "z~abaAniyap", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "strL": [
        { 
            "stri": "xazanat", "strTyp": "lem",},
        { 
      "wrdDisPos": 20,
            "stri": "jan~ap", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "strL": [
        { 
            "stri": "xazanat", "strTyp": "lem",
            },
        { 
      "wrdDisPos": 20,
            "stri": "jahan~am", "strTyp": "lem",},
      ],
    },
  ],
]

malak_mala = [
            [
    {
      
      "strL": [
        { "stri": "mala>", "strTyp": "lem",},
        { "stri": ">aEolaY`", "strTyp": "lem",},
      ],
    },
  ],
]

malak_jund = [
            [
    {
      
      "strL": [
        { "stri": "jund", "strTyp": "lem",},
        { "stri": "lam", "strTyp": "lem",},
        { "stri": "rAy", "strTyp": "root",},
      ],
    },
  ],
        [
    {
      "strL": [
        { "stri": "jund", "strTyp": "lem",},
        { 
      "wrdDisPos": 1,
            "stri": "rab~", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "strL": [
        { "stri": "jund", "strTyp": "lem",},
        { 
      "wrdDisPos": 4,
            "stri": "samaA^'", "strTyp": "lem",},
      ],
    },
  ],
]

malak_janah = [
        [
    {
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { 
      "wrdDisPos": 10,
            "stri": "janaAH", "strTyp": "lem",},
      ],
    },
  ],
]

malak_rasul = [
            [
    {
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { 
      "wrdDisPos": 5,
            "stri": "rasuwl", "strTyp": "lem",},
        { "stri": "jEl", "strTyp": "root",},
      ],
    },
  ],
        [
    {
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { 
      "wrdDisPos": 4,
            "stri": "rasuwl", "strTyp": "lem",},
        { "stri": "nzl", "strTyp": "root",},
      ],
    },
  ],
          [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "rasuwl", "strTyp": "lem",},
        { "stri": "Sfw", "strTyp": "root",},
      ],
    },
  ],
]

malak_ruh = [
        [
    {
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { 
      "wrdDisPos": 11,
            "stri": ">amor", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "ruwH", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": ">amor", "strTyp": "lem",},
        { "stri": "ruwH", "strTyp": "lem",},
      ],
    },
  ],
]

malak_amr = [
            [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "laA", "strTyp": "lem",},
        { "stri": "ESy", "strTyp": "root",},
        { "stri": "Amr", "strTyp": "root",},
      ],
    },
  ],
        [
    {
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { 
      "wrdDisPos": 11,
            "stri": ">amor", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "ruwH", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": ">amor", "strTyp": "lem",},
        { "stri": "ruwH", "strTyp": "lem",},
      ],
    },
  ],
]

malak_arsh = [
            [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "Hml", "strTyp": "root",},
        { "stri": "Earo$", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "Earo$", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Hml", "strTyp": "root",},
        { "stri": "Earo$", "strTyp": "lem",},
      ],
    },
  ],
]

malak_muqarrab = [
            [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "muqar~abuwn", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "strL": [
        { "stri": "muqar~abuwn", "strTyp": "lem",},
        { 
      "wrdDisPos": 5,
            "stri": "Eil~iy~iyn", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "muqar~abuwn", "strTyp": "lem",},
      ],
    },
  ],
]

malak_rabb_akhadh = [
            [
    {
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "rab~", "strTyp": "lem",},
        { 
      "wrdDisPos": 3,
            "stri": "Ax*", "strTyp": "root",},
      ],
    },
  ],
]

malak_shafaah = [
    [
      {
        "strL": [
          { "stri": "malak", "strTyp": "lem",},
          { 
        "wrdDisPos": 10,
              "stri": "$afa`Eap", "strTyp": "lem",},
        ],
      }
        
    ]
]

jinnah_malak_maqam_saff = [
  [
      
        {
          "strL": [
            { "stri": "malak", "strTyp": "lem",},
            { 
          "wrdDisPos": 70,
                "stri": "jin~ap", "strTyp": "lem",},
            { 
          "wrdDisPos": 70,
                "stri": "S~aA^f~uwn", "strTyp": "lem",},
          ],
        },

  ],
  [

      {
        "strL": [
          { "stri": "malak", "strTyp": "lem",},
          { 
        "wrdDisPos": 70,
              "stri": "jin~ap", "strTyp": "lem",},
          { 
        "wrdDisPos": 70,
              "stri": "maqaAm", "strTyp": "lem",},
        ],
      },
    ],
]


malak_qabil = [
                [
            {
                "strL": [
                    {
                        "stri": "qabiyl",
                        "strTyp": "lem",
                        "frm": "All",
                    },
                    {
                        "stri": "malak",
                        "strTyp": "lem",
                    },
                ],
            },
        ],
]

malak = [
  *jinn_malak,
  *malak_ism,
  *malak_untha,
  *malak_khazanah_zabaniya,
  *malak_mala,
  *malak_jund,
  *malak_rasul,
  *malak_ruh,
  *malak_amr,
  *malak_arsh,
  *malak_muqarrab,
  *malak_rabb_akhadh,
  *malak_shafaah,
  *malak_janah,
  *jinnah_malak_maqam_saff,
  *malak_qabil,
        [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "Erj", "strTyp": "root",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "mdd", "strTyp": "root",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "sbH", "strTyp": "root",},
      ],
    },
  ],
  #     [

  #     {
  #     "wrdDisPos": 20,
  #       "strL": [
  #         { "stri": "malak", "strTyp": "lem",},
  #         { "stri": "jan~ap", "strTyp": "lem",},
  #       ],
  #     },

  # ]
]

# malak = list(set(malak))

angels = malak

shaytan_qabil = [
                [
            {
                "strL": [
                    {
                        "stri": "qabiyl",
                        "strTyp": "lem",
                        "frm": "All",
                    },
                    {
                        "stri": "$ayoTa`n",
                        "strTyp": "lem",
                    },
                ],
            },
        ],
]

qabil = [
    malak_qabil,
    shaytan_qabil,
]

shaytan_mareed_dua_shirk = [
    [
        {
            "strL": [
                {
                    "stri": "$rk",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
            "wrdDisPos": 16,
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
            "wrdDisPos": 16,
                    "stri": "dEw",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
            "wrdDisPos": 16,
                    "stri": "m~ariyd", 
                    "strTyp": "lem",
                },
                # {
                #     "stri": "duwn", 
                #     "strTyp": "lem",
                # },
            ],
        },
    ],
]

shaytan_mareed = [
    *shaytan_mareed_dua_shirk,
        [
        {
            "strL": [
                # {
                #     "stri": "tbE",
                #     "strTyp": "root",
                #     # "poSp": "V",
                # },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "m~ariyd", 
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
            ],
        },
    ],
]

shaytan_sam_srq_sama_buruj = [
    [
        {
            "strL": [
                {
                    "stri": "samoE", 
                    "strTyp": "lem",
                },
                {
                    "stri": "buruwj", 
                    "strTyp": "lem",
            "wrdDisPos": 30,
                },
                {
                    "stri": "samaA^'", 
                    "strTyp": "lem",
            "wrdDisPos": 30,
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
            "wrdDisPos": 30,
                },
                {
                    "stri": "rajiym", 
                    "strTyp": "lem",
            "wrdDisPos": 30,
                },
                {
                    "stri": "srq",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30,
                },
            ],
        },
    ],
    
]

shaytan_zyn_duwn = [
    [
        {
            "strL": [
                {
                    "stri": "duwn", 
                    "strTyp": "lem",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
            "wrdDisPos": 5,
                },
                {
                    "stri": "zyn",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 5,
                },
            ],
        },
    ],
    
]

shaytan_marid_sama_dunya_kawkab = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "kawokab", 
                    "strTyp": "lem",
            "wrdDisPos": 20,
                },
                {
                    "stri": "d~unoyaA", 
                    "strTyp": "lem",
            "wrdDisPos": 20,
                },
                {
                    "stri": "samaA^'", 
                    "strTyp": "lem",
            "wrdDisPos": 20,
                },
                {
                    "stri": "m~aArid", 
                    "strTyp": "lem",
            "wrdDisPos": 20,
                },
            ],
        },
    ],
]

shaytan_maarid = [
    *shaytan_marid_sama_dunya_kawkab,   
]

shaytan_abd = [
    [
        {
            "strL": [
                {
                    "stri": "Ebd",
                    "strTyp": "root",
                    "poSp": "V",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
            "wrdDisPos": 5,
                },
            #     {
            #         "stri": "<ila`h", 
            #         "strTyp": "lem",
            #     },
            ],
        },
    ],
]

shaytan_akhi_bdhr = [
    [
        {
            "strL": [
                {
                    "stri": ">ax",
                    "strTyp": "lem",
                    # "poSp": "V",
                },
                {
                    "stri": "b*r",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 20,
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
            "wrdDisPos": 20,
                },
            ],
        },
    ], 
]
shaytan_mani = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "mny",
                    "strTyp": "root",
                    "poSp": "V",
                    "frm": "ii",
            "wrdDisPos": 10
                },
            ],
        },
    ],
]

shaytan_nabi_tamanna_ilqa_naskh_fitna = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "mny",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 20
                },
                {
                    "stri": "ftn",
                    "strTyp": "root",
                    # "poSp": "V",
                    # "frm": "ii",
            "wrdDisPos": 20
                },
                {
                    "stri": "nsx",
                    "strTyp": "root",
                    # "poSp": "V",
                    # "frm": "ii",
            "wrdDisPos": 20
                },
                {
                    "stri": "lqy",
                    "strTyp": "root",
                    # "poSp": "V",
                    # "frm": "ii",
            "wrdDisPos": 20
                },
                {
                    "stri": "n~abiY~", 
                    "strTyp": "lem",
            "wrdDisPos": 20
                },
            ],
        },
    ], 
]

shaytan_amr_btk_anam_adhan = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "btk",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": ">u*unN",
                    "strTyp": "lem",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "n~aEam", 
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
            ],
        },
    ],    
]

shaytan_amr_ghayr_khalq = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "gyr",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "xaloq",
                    "strTyp": "lem",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
            ],
        },
    ], 
]

shaytan_amr_munkar = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "munkar",
                    "strTyp": "lem",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
            ],
        },
    ], 
]

shaytan_amr_sayyiah = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "suw^'",
                    "strTyp": "lem",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
            ],
        },
    ], 
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "say~i}ap",
                    "strTyp": "lem",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
            ],
        },
    ], 
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "say~i_#aAt",
                    "strTyp": "lem",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
            ],
        },
    ], 
]

shaytan_amr_fahisha = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "faHo$aA^'",
                    "strTyp": "lem",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
            ],
        },
    ], 
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "fa`Hi$ap",
                    "strTyp": "lem",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
            ],
        },
    ], 
]

shaytan_amr = [
    *shaytan_amr_ghayr_khalq,
    *shaytan_amr_btk_anam_adhan,
    *shaytan_amr_fahisha,
    # [
    #     {
    #         "strL": [
    #             {
    #                 "stri": "Amr",
    #                 "strTyp": "root",
    #                 # "poSp": "V",
    #             },
    #             {
    #                 "stri": "$ayoTa`n", 
    #                 "strTyp": "lem",
    #             },
    #         ],
    #         "wrdDisPos": 30
    #     },
    # ],
]

shaytan_shirk = [
    *shaytan_mareed_dua_shirk,
    *shaytan_abd,
    [
        {
            "strL": [
                {
                    "stri": "TwE",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "$rk",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
                # {
                #     "stri": "<ins", 
                #     "strTyp": "lem",
                # },
                # {
                #     "stri": "waliY~", 
                #     "strTyp": "lem",
                # },
            ],
        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "tbE",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "$rk",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
                # {
                #     "stri": "<ins", 
                #     "strTyp": "lem",
                # },
                # {
                #     "stri": "waliY~", 
                #     "strTyp": "lem",
                # },
            ],
        },
    ],
]

shaytan_sharik_awlad = [
    [
        {
            "strL": [
                # {
                #     "stri": "jin~",
                #     "strTyp": "lem",
                # },
                {
                    "stri": "$rk",
                    "strTyp": "root",
                    "poSp": "V",
                    "frm": "iii",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
            "wrdDisPos": 10
                },
                # {
                #     "stri": "maAl", 
                #     "strTyp": "lem",
                # },
                {
                    "stri": "walad", 
                    "strTyp": "lem",
            "wrdDisPos": 10
                },
            ],
        },
    ],
]

shaytan_why = [
    [
        {
            "strL": [
                # {
                #     "stri": "jin~",
                #     "strTyp": "lem",
                # },
                {
                    "stri": "wHy",
                    "strTyp": "root",
                    "poSp": "V",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
            "wrdDisPos": 10
                },
                # {
                #     "stri": "<ins", 
                #     "strTyp": "lem",
                # },
                # {
                #     "stri": "waliY~", 
                #     "strTyp": "lem",
                # },
            ],
        },
    ],
]

# jinn_qarin = [
#         [
#         {
#             "strL": [
#                 {
#                     "stri": "jin~",
#                     "strTyp": "lem",
#                 },
#                 {
#                     "stri": "qariyn", 
#                     "strTyp": "lem",
#                 },
#             ],
#             "wrdDisPos": 20
#         },
#     ],
# ]

shaytan_qarin = [
    [
        {
            "strL": [
                {
                    "stri": "qariyn", 
                    "strTyp": "lem",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
            "wrdDisPos": 25
                },
                {
                    "stri": "ri}aA^'", 
                    "strTyp": "root",
            "wrdDisPos": 25
                },
            ],
        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "qariyn", 
                    "strTyp": "lem",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
            "wrdDisPos": 25
                },
                {
                    "stri": "E$w", 
                    "strTyp": "root",
            "wrdDisPos": 25
                },
            ],
        },
    ],
]

qarin = [
    # *jinn_qarin,
    *shaytan_qarin,
    [
        {
            "strL": [
                {
                    "stri": "qariyn", 
                    "strTyp": "lem",
                },
            ],
            # "wrdDisPos": 25
        },
    ],
]

shaytan_muqarran = [
        [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "m~uqar~aniyn", 
                    "strTyp": "lem",
            "wrdDisPos": 20
                },
            ],
        },
    ],
]

shaytan_wiswas = [
        [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "wsws",
                    "strTyp": "root",
                    # "poSp": "V",
                    # "frm": "ii",
            "wrdDisPos": 20
                },
            ],
        },
    ],
]

shaytan = [
    *shaytan_sam_srq_sama_buruj,
    *shaytan_maarid,
    *shaytan_mareed,
    *shaytan_qarin,
    *shaytan_muqarran,
    *shaytan_sharik_awlad,
    *shaytan_shirk,
    *shaytan_akhi_bdhr,
    *shaytan_mani,
    *shaytan_amr,
    *shaytan_why,
    *shaytan_wiswas,
    *shaytan_qabil,
    *iblis,
]

# shaytan = list(set(shaytan))

muqarran = [
    *shaytan_muqarran,
        [
        {
            
            "strL": [
                {
                    "stri": "m~uqar~aniyn", 
                    "strTyp": "lem",
                },
            ],
        },
    ],
]

qarin_muqarran = [
    *qarin,
    *muqarran,
]

kahin_majnun = [
        [
        {
            "strL": [
                {
                    "stri": "majonuwn",
                    "strTyp": "lem",
                },
                {
                    "stri": "kaAhin", 
                    "strTyp": "lem",
            "wrdDisPos": 20
                },
            ],
        },
    ],
]

ifrit_jinn = [
        [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "Eiforiyt", 
                    "strTyp": "lem",
            "wrdDisPos": 35
                },
            ],
        },
    ],
]

ifrit = [
    *ifrit_jinn,
]

jinna_wiswas = [
    [
        {
            "strL": [
                {
                    "stri": "jin~ap", 
                    "strTyp": "lem",
                },
                {
                    "stri": "wsws",
                    "strTyp": "root",
                    # "poSp": "V",
                    # "frm": "ii",
            "wrdDisPos": 20
                },
            ],
        },
    ],
]

wiswas = [
    jinna_wiswas,
    *shaytan_wiswas,
]

jinn_sama_mss_qEd_sam = [
    [
        {
            "strL": [
                {
                    "stri": "jin~", 
                    "strTyp": "lem",
                },
                {
                    "stri": "samoE", 
                    "strTyp": "lem",
            "wrdDisPos": 75,
                },
                {
                    "stri": "samaA^'", 
                    "strTyp": "lem",
            "wrdDisPos": 75,
                },
                {
                    "stri": "lms",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 75,
                },
                {
                    "stri": "qEd",
                    "strTyp": "root",
                    # "poSp": "V",
            "wrdDisPos": 75,
                },
            ],
        },
    ],
]

jinn_rasul_ins = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "rasuwl", 
                    "strTyp": "lem",
            "wrdDisPos": 10
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
            "wrdDisPos": 10
                },
            ],
        },
    ], 
]

jinn_ins_ummah_khala = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": ">um~ap", 
                    "strTyp": "lem",
            "wrdDisPos": 10
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
            "wrdDisPos": 10
                },
                {
                    "stri": "xlw", 
                    "strTyp": "root",
                    "poSp": "V",
            "wrdDisPos": 10
                },
            ],
        },
    ], 
]

jinn_ins_nfdh_sama = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "samaA^'", 
                    "strTyp": "lem",
            "wrdDisPos": 10
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
            "wrdDisPos": 10
                },
                {
                    "stri": "nf*", 
                    "strTyp": "root",
                    "poSp": "V",
            "wrdDisPos": 10
                },
            ],
        },
    ], 
]

jinn_ins_abd = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "Ebd", 
                    "strTyp": "root",
            "wrdDisPos": 10
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
            "wrdDisPos": 10
                },
            ],
        },
    ],
]

jinn_ins_dll = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
            "wrdDisPos": 5
                },
                {
                    "stri": "Dll", 
                    "strTyp": "root",
                    "poSp": "V",
            "wrdDisPos": 5
                },
            ],
        },
    ], 
]

jinn_wHy_ins_shaytan = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "wHy",
                    "strTyp": "root",
                    "poSp": "V",
            "wrdDisPos": 10
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
            "wrdDisPos": 10
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
            "wrdDisPos": 10
                },
            ],
        },
    ],
]

jinn_wHy_ins = [
    *jinn_wHy_ins_shaytan,  
]

jinn_shaytan = [
    *jinn_wHy_ins_shaytan,
]

jinn_sharik_kharaq_bani = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "$ariyk", 
                    "strTyp": "lem",
                    # "poSp": "N",
                    # "frm": "i",
            "wrdDisPos": 35
                },
                {
                    "stri": "xrq", 
                    "strTyp": "root",
            "wrdDisPos": 35
                },
                {
                    "stri": "banaAt", 
                    "strTyp": "lem",
            "wrdDisPos": 35
                },
            ],
        },
    ],    
]

jinn_sharik = [
    *jinn_sharik_kharaq_bani,
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "$ariyk", 
                    "strTyp": "lem",
                    # "poSp": "N",
                    # "frm": "i",
            "wrdDisPos": 35
                },
            ],
        },
    ], 
]

jinn_abd = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "Ebd", 
                    "strTyp": "root",
                    "poSp": "V",
                    "frm": "i",
            "wrdDisPos": 15
                },
                {
                    "stri": ">akovar",
                    "strTyp": "lem",
            "wrdDisPos": 15
                },
                {
                    "stri": "malak",
                    "strTyp": "lem",
            "wrdDisPos": 15
                },
            ],
        },
    ],
]

jinna_nasab = [
    [
        {
            "strL": [
                {
                    "stri": "jin~ap",
                    "strTyp": "lem",
                },
                {
                    "stri": "nsb", 
                    "strTyp": "root",
            "wrdDisPos": 20
                },
            ],
        },
    ],
]

jinnah_nas_khannas = [
    [
        {
            "strL": [
                {
                    "stri": "jin~ap",
                    "strTyp": "lem",
                },
                {
                    "stri": "n~aAs", 
                    "strTyp": "lem",
            "wrdDisPos": 20
                },
                {
                    "stri": "xan~aAs", 
                    "strTyp": "lem",
            "wrdDisPos": 20
                },
            ],
        },
    ],
    
]

jinnah_khannas = [
    *jinnah_nas_khannas,
]

khannas = [
    *jinnah_nas_khannas,
    [
        {
            "strL": [
                {
                    "stri": "xan~aAs", 
                    "strTyp": "lem",
                },
            ],
        },
    ],
]

jinn_wali_ins = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "wly", 
                    "strTyp": "root",
            "wrdDisPos": 7
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
            "wrdDisPos": 7
                },
            ],
        },
    ],
]

jinn_awdh_ins = [
        [
        {
            "strL": [
                {
                    "stri": "Ew*", 
                    "strTyp": "root",
                },
                {
                    "stri": "jin~",
                    "strTyp": "lem",
            "wrdDisPos": 25
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
            "wrdDisPos": 25
                },
            ],
        },
    ],
]

jinn_istikthar_ins = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "kvr",
                    "strTyp": "root",
                    "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
            ],
        },
    ],
]

jinn_tayr = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "Tayor", 
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
            ],
        },
    ],
]

jinn_ijtima_ins = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "jmE",
                    "strTyp": "root",
                    "poSp": "V",
            "wrdDisPos": 30
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
            ],
        },
    ],
]

jinn_shirk = [
    *jinna_wiswas,
    *jinn_ijtima_ins,
    *jinn_istikthar_ins,
    *jinn_wHy_ins_shaytan,
    *jinn_wali_ins,
    *jinn_awdh_ins,
    *jinn_sharik,
    *jinn_abd,
    *jinna_nasab,
    *jinn_sharik_kharaq_bani
]

jinn_ins_jahannam = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "jahan~am",
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
            ],
        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "jin~ap",
                    "strTyp": "lem",
                },
                {
                    "stri": "jahan~am",
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
                {
                    "stri": "n~aAs", 
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
            ],
        },
    ],
]

jann_ins_Tmth = [
    [
        {
            "strL": [
                {
                    "stri": "jaA^n~",
                    "strTyp": "lem",
                },
                {
                    "stri": "<ins",
                    "strTyp": "lem",
                },
                {
                    "stri": "Tmv",
                    "strTyp": "root",
                },
            ],

        },
    ],   
]

jinn_ins = [
    *jinn_wali_ins,
    *jinn_awdh_ins,
    *jinn_istikthar_ins,
    *jinn_ijtima_ins,
    *jinn_wHy_ins_shaytan,
    *jinn_ins_jahannam,
    *jinnah_nas_khannas,
    *jinn_ins_nfdh_sama,
    *jinn_ins_dll,
    *jinn_ins_ummah_khala,
    *jinn_rasul_ins,
    *jann_ins_Tmth,
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
            ],
        },
    ],
]

jann_dhanb = [
    [
        {
            "strL": [
                {
                    "stri": "jaA^n~",
                    "strTyp": "lem",
                },
                {
                    "stri": "*anb",
                    "strTyp": "lem",
                },
            ],

        },
    ],   
]

jann_nar = [
    [
        {
            "strL": [
                {
                    "stri": "jaA^n~",
                    "strTyp": "lem",
                },
                {
                    "stri": "naAr",
                    "strTyp": "lem",
                },
            ],

        },
    ],   
]

jann_hzz = [
    [
        {
            "strL": [
                {
                    "stri": "jaA^n~",
                    "strTyp": "lem",
                },
                {
                    "stri": "hzz",
                    "strTyp": "root",
                },
            ],

        },
    ],   
]

jinn = [
    *kahin_majnun,
    *jinn_malak,
    *ifrit_jinn,
    # *jinn_qarin,
    *jinn_iblis,
    *jinn_shaytan,
    *jinn_ins,
    *jinn_tayr,
    *jinn_shirk,
    *jann_nar,
    *jann_dhanb,
    *jann_hzz,
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
            ],

        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "jin~ap",
                    "strTyp": "lem",
                },
            ],

        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "majonuwn",
                    "strTyp": "lem",
                },
            ],
        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "jnn",
                    "strTyp": "root",
                    "poSp": "V",
                    "frm": "i",
                },
            ],
        },
    ],
]

# jinn = list(set(jinn))

jinn_shaytan = [
    *jinn,
    *shaytan,
]

kahin_shair = [
    [
        {
            "strL": [
                {
                    "stri": "kaAhin", 
                    "strTyp": "lem",
                },
                {
                    "stri": "$aAEir",
                    "strTyp": "lem",
            "wrdDisPos": 20
                },
            ],
        },
    ],
]

kahin = [
    *kahin_majnun,
    *kahin_shair,

]


evil_spirits = [
        [
    {
      
      "strL": [
        { "stri": "$Tn", "flt": "(?:devil|[^d]evil|demon|shaitaan)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "<iboliys", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "bls", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jin~", "flt": "(?:[jJ]inn)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jin~ap", "flt": "(?:[Jj]inn|mad)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jnn", "flt": "(?:^mad$|mad man|madman|surely mad)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jaAn~", "flt": "(?:snake|jinn)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Hyy", "flt": "snake",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qrn", "flt": "companion",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "qrn", "flt": "",},
      ],
    },
  ],
      [
        {
            "strL": [
                {
                    "stri": "<iboliys",
                    "strTyp": "lem",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
            "wrdDisPos": 30
                },
            ],
        },
    ],
        [
    {
      
      "strL": [
        { "stri": "jnn", "flt": "jinn",},
        { "stri": "$Tn", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "mrd", "flt": "rebellious",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Eiforiyt", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "mss", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jnd", "flt": "(?:host|troop|force)",},
        { "stri": "<iboliys", "flt": "(?:iblis|devil|satan)",},
      ],
    },
  ],

        [
    {
      
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "wly", "flt": "(?:ally|allies|guardian|protector|friend)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "Ebd", "flt": "",},
        { "stri": "laA", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "Anv", "flt": "",},
        { "stri": "dEw", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "qrn", "flt": "",},
      ],
    },
  ],

        [
    {
      
      "strL": [
        { "stri": "jnn", "flt": "(?:jinn)",},
        { "stri": "dwn", "flt": "",},
        { "stri": "Ebd", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jnn", "flt": "(?:jinn)",},
        { "stri": "$rk", "flt": "",},
      ],
    },
  ],
]


magic = [

        [
    {
      
      "strL": [
        { "stri": "$Er", "flt": "poetry",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Er", "flt": "hair",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Er", "flt": "Sirius",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Er", "flt": "monument",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Er", "flt": "(?:symbol|rite)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Er", "flt": "poet(?!r)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Er", "flt": "", "strTyp": "root",  "frm": "i",  "poSp": "V", },
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Er", "flt": "", "strTyp": "root",  "frm": "iv",  "poSp": "V", },
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sHr", "flt": "magic(?!i)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sHr", "flt": "magician",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sHr", "flt": "(?<!they )bewitched",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sHr", "flt": "(?:they bewitch|you bewitch|delude)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "baAbil", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jbt", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nfv", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "khn", "flt": "",},
      ],
    },
  ],
]

ruh = [
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": ">amiyn", "strTyp": "lem", "flt": "",},
        { "stri": "nzl", "strTyp": "root", "flt": "",},
      ],
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": ">amor", "strTyp": "lem", "flt": "",},
        { "stri": "nzl", "strTyp": "root", "flt": "",},
      ],
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": ">amor", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": ">amor", "strTyp": "lem", "flt": "",},
        { "stri": "malak", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": ">amor", "strTyp": "lem", "flt": "",},
        { "stri": "malak", "strTyp": "lem", "flt": "",},
        { "stri": "nzl", "strTyp": "root", "flt": "",},
      ],
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "malak", "strTyp": "lem", "flt": "",},
        { "stri": "Erj", "strTyp": "root", "flt": "",},
        { "stri": "yawom", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "malak", "strTyp": "lem", "flt": "",},
        { "stri": "qwm", "strTyp": "root", "flt": "",},
        { "stri": "yawom", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "malak", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "qds", "strTyp": "root", "flt": "",},
        { "stri": "nzl", "strTyp": "root", "flt": "",},
        { "stri": "vbt", "strTyp": "root", "flt": "",},
        { "stri": "Amn", "strTyp": "root", "flt": "",},
      ],
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "qds", "strTyp": "root", "flt": "",},
        { "stri": "Ayd", "strTyp": "root", "flt": "",},
        { "stri": "EiysaY", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "EiysaY", "strTyp": "lem", "flt": "",},
        { "stri": "glw", "strTyp": "root", "flt": "",},
      ],
      "lbl": "ruh isa"
    },
  ],
    [
    {
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { 
            "stri": "Ayd", "strTyp": "root", "flt": "",},
        { 
      "wrdDisPos": 10,
            "stri": "<iyma`n", "strTyp": "root","poSp": "N","frm": "iv",},
      ],
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "wHy", "strTyp": "root", "flt": "",},
        { "stri": ">amor", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "lqy", "strTyp": "root", "flt": "",},
        { "stri": ">amor", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { 
      "wrdDisPos": 12,
            "stri": "nfx", "strTyp": "root", "flt": "",},
        { 
      "wrdDisPos": 12,
            "stri": "ba$ar", "strTyp": "lem", "flt": "",},
      ],
      "lbl": "روح نفخ بشر"
    },
    {
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { 
      "wrdDisPos": 14,
            "stri": "nfx", "strTyp": "root", "flt": "",},
        { 
      "wrdDisPos": 14,
            "stri": "<insa`n", "strTyp": "lem", "flt": "",},
      ],
      "lbl": "روح نفخ إنسان"
    },
  ],
    [
    {
      
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "nfx", "strTyp": "root", "flt": "",},
        { "stri": "faroj", "strTyp": "lem", "flt": "",},
      ],
      "lbl": "روح نفخ مريم"
    },
  ],
    [
    {
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { 
      "wrdDisPos": 12,
            "stri": "rsl", "strTyp": "root", "flt": "",},
        { 
      "wrdDisPos": 12,
            "stri": "maroyam", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
]

nafs = [
        [
    {
      
      "strL": [
        { "stri": "nfs", "flt": "(?:soul|self)",},
      ],
    },
  ],
]

spirits = [
    *ruh,

        [
    {
      
      "strL": [
        { "stri": "nfx", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Suwr", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Swr", "flt": "",},
      ],
    },
  ],

]

spirituals = [
        *angels,
        *evil_spirits,
        *ruh,
]

isa = [

        [
    {
      
      "strL": [
        { "stri": "masiyH", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "EiysaY", "flt": "isa",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "maryam", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "yaHoyaY`", "flt": "yahya",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "zakariy~aA", "flt": "zakariya",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "EimoraAn", "flt": "imran",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "kalimap", "flt": "(?:word|.*)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "kalaAm", "flt": "(?:word|.*)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Tayor", "flt": "(?:bird)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "mahod", "flt": "bed",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "fTr", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "ftr", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "muwsaY`", "flt": "musa",},
      ],
    },
  ],
]


idols_base = [
        [
    {
      
      "strL": [
        { "stri": "wad~", "strTyp":"lem", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "{ll~a`t", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "{loEuz~aY`", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "manaw`p", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "baEol2", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "ma`lik2", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "suwaAE", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "yaguwv", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "yaEuwq", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nasor", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "T~a`guwt", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],    
]


idols = [
        [
    {
      
      "strL": [
        { "stri": "wad~", "strTyp":"lem", "flt": "wadd",},
        { "stri": "wdd", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "{ll~a`t", "strTyp":"lem",  "flt": "",},
        { "stri": "lwt", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "{ll~a`t", "strTyp":"lem",  "flt": "",},
        { "stri": "lwy", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "{ll~a`t", "strTyp":"lem",  "flt": "",},
        { "stri": "lyt", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "{loEuz~aY`", "strTyp":"lem",  "flt": "",},
        { "stri": "Ezz", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "{loEuz~aY`", "strTyp":"lem",  "flt": "",},
        { "stri": "Ezw", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "manaw`p", "strTyp":"lem",  "flt": "",},
        { "stri": "mny", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "baEol2", "strTyp":"lem",  "flt": "",},
        { "stri": "bEl", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "ma`lik2", "strTyp":"lem",  "flt": "malik",},
        { "stri": "mlk", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "suwaAE", "strTyp":"lem",  "flt": "",},
        { "stri": "swE", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "yaguwv", "strTyp":"lem",  "flt": "",},
        { "stri": "gyv", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "yaguwv", "strTyp":"lem",  "flt": "",},
        { "stri": "gwv", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "yaEuwq", "strTyp":"lem",  "flt": "",},
        { "stri": "Ewq", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nasor", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "T~a`guwt", "strTyp":"lem",  "flt": "",},
        { "stri": "Tgy", "strTyp":"root", "flt": "",},
      ],
    },
  ],
]

heavenlies = [
        [
    {
      
      "strL": [
        { "stri": "kwkb", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "njm", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$ms", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qmr", "flt": "",},
      ],
    },
  ],
            [
    {
      
      "strL": [
        { "stri": "$Er", "flt": "[Ss]irius",},
      ],
    },
  ],

]

ilah = [
  *ilah_duwn_baEd_gayr,
        [
    {
      
      "strL": [
        { "stri": "<ila`h", "strTyp": "lem",},
      ],
    },
  ],
]

rituals = [
        [
    {
      
      "strL": [
        { "stri": "wvn", "flt": "idol",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Snm", "flt": "idol",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nuSub", "strTyp": "stem", "flt": "",},
        { "stri": "naSiyb", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nuSub", "strTyp": "stem", "flt": "",},
        { "stri": "nuSob", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nuSub", "strTyp": "stem", "flt": "",},
        { "stri": "naSiyb", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nuSub", "strTyp": "stem", "flt": "",},
        { "stri": "naSab", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nuSub", "strTyp": "stem", "flt": "",},
        { "stri": "n~aASibap", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nuSub", "strTyp": "stem", "flt": "",},
        { "stri": "nSb", "strTyp": "root", "poSp": "V", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "naSiyb", "strTyp": "stem", "flt": "",},
        { "stri": "jEl", "strTyp": "root", "flt": "assign",},
      ],
    },
  ],

        [
    {
      
      "strL": [
        { "stri": "saA^}ibap", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "waSiylap", "strTyp": "stem", "flt": "",},
        { "stri": "wSl", "strTyp": "root", "poSp":"V", "frm": "i", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "waSiylap", "strTyp": "stem", "flt": "",},
        { "stri": "wSl", "strTyp": "root", "poSp":"V", "frm": "ii", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "baHor", "strTyp": "stem", "flt": "",},
        { "stri": "baHiyrap", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "HaAm", "strTyp": "stem", "flt": "",},
        { "stri": "Hamiy~ap", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "HaAm", "strTyp": "stem", "flt": "",},
        { "stri": "Hmy", "strTyp": "root", "poSp": "V", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": ">azolaAm", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Hrm", "flt": "",},
        { "stri": "Anv", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "xlS", "flt": "",},
        { "stri": "bTn", "flt": "",},
        { "stri": "*kr", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Er", "flt": "[Pp]oet(?!r)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$Er", "flt": "(?:[Pp]oetry)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "ma$oEar", "strTyp": "lem", "flt": "",},
        { "stri": "$Er", "strTyp": "root", "poSp":"V", "frm": "i", "flt": "(?:[Hh]air)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$aAEir", "strTyp": "lem", "flt": "(?:[Ss]ymbol|rite)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$iEor", "strTyp": "lem", "flt": "(?:[Mm]onument)",},
      ],
    },
  ],
            [
    {
      
      "strL": [
        { "stri": "$Er", "flt": "[Ss]irius",},
      ],
    },
  ],
]


shirk = [
    *ilah_duwn_baEd_gayr,
    *ilah,
    *waliy_duwn_baEd_gayr,
    *shrk,
    *shaytan_shirk,
    *jinn_shirk,
    # *shirk2,
    *idols,
    # *heavenlies,
    *rituals,
    *evil_spirits,
        [
    {
      
      "strL": [
        { "stri": "Alh", "flt": "(?:^((?!Allah).)*$)",},
        { "stri": "Axr", "flt": "",},
        { "stri": "maEa", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Ebd", "flt": "(?:worship|serv)",},
        { "stri": "dwn", "flt": "(?:other|esides|exclud|Us|instead)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "dEw", "flt": "",},
        { "stri": "maEa", "flt": "",},
        { "stri": "AHd", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "dEw", "flt": "(?:^((?!caller).)*$)",},
        { "stri": "dwn", "flt": "(?:other|esides|exclud|Us|instead)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Ax*", "flt": "", "strTyp": "root",  "frm": "viii", },
        { "stri": "Alh", "flt": "(?:^((?!Allah).)*$)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Ax*", "flt": "", "strTyp": "root",  "frm": "viii", },
        { "stri": "dwn", "flt": "",},
      ],
    },
  ],

        [
    {
      
      "strL": [
        { "stri": "Ax*", "flt": "(?:^((?!we).)*$)", "strTyp": "root",  "frm": "viii", },
        { "stri": "wld", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "wld", "flt": "(?:begot|beget)",},
        { "stri": "Alh", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "wld", "flt": "",},
        { "stri": "sbH", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "lam", "flt": "",},
        { "stri": "wld", "flt": "(?:begot|beget)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Ax*", "flt": "",},
        { "stri": "SHb", "flt": "(?:wife)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "<an~aY", "flt": "",},
        { "stri": "wld", "flt": "(?:son)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "<an~aY", "flt": "",},
        { "stri": "SaAHibap", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Ax*", "flt": "",},
        { "stri": "Anv", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "malak", "flt": "(?:[Aa]ngel)",},
        { "stri": "Anv", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Ax*", "flt": "",},
        { "stri": "bny", "flt": "(?:[Dd]aughter)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jEl", "flt": "assign",},
        { "stri": "bny", "flt": "(?:[Dd]aughter)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "xrq", "flt": "",},
        { "stri": "bny", "flt": "(?:[Ss]on|[Ss]hild|[Dd]aughter)",},
      ],
    },
  ],

        [
    {
      
      "strL": [
        { "stri": "$ariyk", "flt": "",},
      ],
    },
  ],

        [
    {
      
      "strL": [
        { "stri": "sjd", "flt": "",},
        { "stri": "A^dam", "flt": "",},
        { "stri": "malak", "flt": "(?:[Aa]ngel)",},
      ],
    },
  ],

        [
    {
      
      "strL": [
        { "stri": "kwkb", "flt": "star",},
        { "stri": "rAy", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "kwkb", "flt": "",},
        { "stri": "rab~", "flt": "",},
        { "stri": "ha`*aA", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "njm", "flt": "",},
        { "stri": "nZr", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$ms", "flt": "",},
        { "stri": "rab~", "flt": "",},
        { "stri": "ha`*aA", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$ms", "flt": "",},
        { "stri": "sjd", "flt": "",},
        { "stri": "dwn", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$ms", "flt": "",},
        { "stri": "sjd", "flt": "",},
        { "stri": "laA", "flt": "",},
        { "stri": "Ebd", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qmr", "flt": "",},
        { "stri": "rab~", "flt": "",},
        { "stri": "ha`*aA", "flt": "",},
      ],
    },
  ],
        
        [
    {
      
      "strL": [
        { "stri": "rhb", "flt": "",},
        { "stri": "rbb", "flt": "",},
        { "stri": "Ax*", "flt": "(?:taken)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Hbr", "flt": "",},
        { "stri": "rbb", "flt": "",},
        { "stri": "Ax*", "flt": "(?:taken)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "mlk", "flt": "(?:[Aa]ngel)",},
        { "stri": "Ax*", "flt": "", "strTyp": "root",  "frm": "viii", },
        { "stri": "rbb", "flt": "(?:[Ll]ords)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nbA", "flt": "",},
        { "stri": "Ax*", "flt": "", "strTyp": "root",  "frm": "viii", },
        { "stri": "rbb", "flt": "(?:[Ll]ords)",},
      ],
    },
  ],


        [
    {
      
      "strL": [
        { "stri": "jzA", "flt": "",},
        { "stri": "Ebd", "flt": "",},
      ],
    },
  ],

]

places = [

        [
    {
      
      "strL": [
        { "stri": "SafaA", "flt": "safa",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "marowap", "flt": "marwa",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "siyniyn", "flt": "sin",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qurayo$", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "tub~aE", "flt": "tubba",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "saba<", "flt": "saba",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "misor", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "ruwm", "flt": "rom",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "ramaDaAn", "flt": "ramadan",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "EarafaAt", "flt": "arafa",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "bak~ap", "flt": "bakka",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "bador", "flt": "badr",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "yavorib", "flt": "yathrib",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "makkap", "flt": "makka",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "kaEobap", "flt": "ka",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Hunayon", "flt": "hunayn",},
      ],
    },
  ],
]

animals = [

        [
    {
      
      "strL": [
        { "stri": "nml", "flt": "ant",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qrd", "flt": "(?:monkey|ape)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nHl", "flt": "bee",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Tyr", "flt": "bird",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "TaA}ir", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Ejl", "flt": "calf",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jml", "flt": "camel",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "bEr", "flt": "camel",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nwq", "flt": "camel",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "<ibil", "flt": "camel",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "hym", "flt": "camel",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "E$r", "flt": "camel",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "bqr", "flt": "(?:heifer|cow)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "grb", "flt": "(?:raven|crow)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "klb", "flt": "(?:dog|hound)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Hmr", "flt": "(?:donkey|ass)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "fyl", "flt": "elephant",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nEj", "flt": "ewe",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Hwt", "flt": "fish",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "*bb", "flt": "(?:fly|flies)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "DfdE", "flt": "frog",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "mEz", "flt": "goat",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "hdhd", "flt": "hoopoe",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "xyl", "flt": "(?:horse|cavalry)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jwd", "flt": "steed",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qml", "flt": "lice",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qsr", "flt": "lion",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jrd", "flt": "locust",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "bED", "flt": "mosquito",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "fr$", "flt": "moth",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "bgl", "flt": "mule",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "xnzr", "flt": "(?:pig|swine)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "slw", "flt": "quail",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "gnm", "flt": "sheep",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "vEb", "flt": "(?:serpent|snake)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Hyy", "flt": "(?:serpent|snake)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jaAn~", "flt": "(?:snake|serpent|jinn)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Enkb", "flt": "spider",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "*#b", "flt": "wolf",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nEm", "flt": "(?:cattle|livestock)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "bhm", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "dbb", "flt": "(?:creature|animal|beast)",},
      ],
    },
  ],
]

hindi = [
        [
    {
      
      "strL": [
        { "stri": "msk", "flt": "musk",},
      ],
    },
  ],
]

geez = [

        [
    {
      
      "strL": [
        { "stri": "Hwr", "flt": "disciple",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "zrb", "flt": "",},
      ],
    },
  ],
]

copt_gypt = [

        [
    {
      
      "strL": [
        { "stri": "xtm", "flt": "seal",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "taAbuwt", "flt": "(?:ark|chest|.*)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Tgy", "flt": "(?:idol|deit|god|evil)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jbt", "flt": "(?:copt|gypsy|superstition)",},
      ],
    },
  ],
]

latin = [

        [
    {
      
      "strL": [
        { "stri": "sij~iyl", "flt": "clay",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sjl", "flt": "scroll",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qnTr", "flt": "(?:centenarium|heap|wealth|store)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "dnr", "flt": "(?:denarius|coin)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qmS", "flt": "shirt",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qSr", "flt": "(?:castle|palace|fort)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "SrT", "flt": "(?:path|way)",},
      ],
    },
  ],
]

greek = [

        [
    {
      
      "strL": [
        { "stri": "qsTs", "flt": "balance",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qrTs", "flt": "parchment",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "drhm", "flt": "dirham",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qld", "flt": "key",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qld", "flt": "garland",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qlm", "flt": "(?:pen|reed|cane)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sTr", "flt": "(?:story|tale)",},
      ],
    },
  ],
]

syr_christ = [

        [
    {
      
      "strL": [
        { "stri": "nHs", "flt": "(?:copper|bronze|brass|smoke)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "krs", "flt": "throne",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Abb", "flt": "(?:pasture|grass)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Ajr", "flt": "(?:reward)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sbl", "flt": "(?:way|path)",},
      ],
    },
  ],
]

aram_jew = [

        [
    {
      
      "strL": [
        { "stri": "jlw", "flt": "exile",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sbt", "flt": "(?:sabbath|rest)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sbT", "flt": "(?:tribe|descendants|scepter|rod|stick)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "safarap", "flt": "scribe",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sfr", "flt": "book",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "rbb", "flt": "(?:the rabbis|worshipper)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "rib~iy~uwn", "flt": "(?:scholar)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "bhm", "flt": "(?:beast|quadruped)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Sdq", "flt": "charity",},
      ],
    },
  ],
]

akkadian = [

        [
    {
      
      "strL": [
        { "stri": "fxr", "flt": "pottery",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": ">asowaAq", "flt": "market",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "swq", "flt": "(?:leg|shin|stem)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "frt", "flt": "(?:sweet|fresh)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "swr", "flt": "(?:bracelet|fetter|chain)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "k#s", "flt": "cup",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sunodus", "flt": "silk",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sTr", "flt": "(?:writ)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sTr", "flt": "(?:control)",},
      ],
    },
  ],
]

farsi = [

        [
    {
      
      "strL": [
        { "stri": "fyl", "flt": "elephant",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "fxr", "flt": "boast",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "fwj", "flt": "(?:group|company|.*)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "srj", "flt": "(?:lamp|.*)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": ">abaAriyq", "flt": "(?:jug)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Efr", "flt": "strong",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "tan~uwr", "flt": "oven",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jnh", "flt": "(?:blame|sin)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "jnd", "flt": "(?:host|troop|army|force)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "srd", "flt": "link",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "srdq", "flt": "wall",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "firodaws", "flt": "paradise",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "mjs", "flt": "mag",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "srbl", "flt": "(?:trouser|pants|garment)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "kaAfuwr", "flt": "(?:camphor|kafur)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "zanjabiyl", "flt": "(?:ginger|zanjabil)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "barozax", "flt": "barrier",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "knz", "flt": "(?:treasure|hoard)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "<isotibraq", "flt": "(?:brocade|silk)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Ebqr", "flt": "carpet",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "namaAriq", "flt": "cushion",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Ark", "flt": "(?:couch|throne)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "zmhr", "flt": "cold",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "m$j", "flt": "mix",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "mzj", "flt": "mix",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "wzr", "flt": "(?:minister|assist|bear|burden|refuge)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Er$", "flt": "(?:erect|construct|roof|throne|trellis)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "dwl", "flt": "(?:circul|alter)",},
      ],
    },
  ],
]


nabis = [

        [
    {
      
      "strL": [
        { "stri": "A^dam", "flt": "(?:Adam|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nuwH", "flt": "(?:Nuh|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "<idoriys", "flt": "(?:Idris|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "huwd", "flt": "(?:Hud|)",},
      ],
    },
    {
      
      "strL": [
        { "stri": "Ewd", "flt": "Aad",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "SaAliH", "flt": "(?:Salih)",},
      ],
    },
    {
      
      "strL": [
        { "stri": "vamuwd", "flt": "Thamud",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "tub~aE", "flt": "Tubba",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": ">ayokap", "flt": "wood",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "ras~", "flt": "(?:rass|Raas)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Hijor", "flt": "(?:the Rocky Tract)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "<iram", "flt": "(?:Aram|Iram)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "<iboraAhiym", "flt": "(?:Ibrahim|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "luwT", "flt": "(?:Lut)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "<isoma`Eiyl", "flt": "(?:Ishmael|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "<isoHaAq", "flt": "(?:Isaac|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "yaEquwb", "flt": "(?:Yaqub|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "yuwsuf", "flt": "(?:Yusuf|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": ">ay~uwb", "flt": "(?:Ayyub|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "$uEayb", "flt": "(?:Shuaib|)",},
      ],
    },
    {
      
      "strL": [
        { "stri": "madoyan", "flt": "(?:Midian|Madyan)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "muwsaY`", "flt": "(?:Musa|)",},
      ],
    },
    {
      
      "strL": [
        { "stri": "firoEawon", "flt": "(?:Pharaoh|Firaun)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "ha`ruwn", "flt": "(?:Harun|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "TaAluwt", "flt": "(?:Saul|Talut)",},
      ],
    },
    {
      
      "strL": [
        { "stri": "jaAluwt", "flt": "(?:Goliath|Jalut)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "daAwud", "flt": "(?:Dawood|Dawud|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sulaymaAn", "flt": "(?:Sulaiman|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "kifol", "flt": "(?:Kifl)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "nuwn", "flt": "(?:Nun)",},
      ],
    },
    {
      
      "strL": [
        { "stri": "yuwnus", "flt": "(?:Yunus)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "<iloyaAs", "flt": "(?:Elijah|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "yasaE", "flt": "(?:Elisha)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "qrn", "flt": "(?:Qarnain)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Euzayor", "flt": "(?:Uzair)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "luqomaAn", "flt": "(?:Luqman)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "zakariy~aA", "flt": "(?:Zakariya|)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "yaHoyaY", "flt": "(?:Yahya)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "maroyam", "flt": "(?:Mary)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "EiysaY", "flt": "isa",},
      ],
    },
    {
      
      "strL": [
        { "stri": "Aibn", "flt": "son",},
        { "stri": "maryam", "flt": "Mary",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "muHam~ad", "flt": "(?:Muhammad|)",},
      ],
    },
  ],
]

islam_iman = [
  *iman,
  *iman_amn,
  *islam,
  *islam_slm,
]

salah = [
  *salah_waqt,
  *sjd,
  *rkE,
  *Slw,
  *sbH,
  *kbr,
  *qiyam_layl,
  *qwm_Slw,
  *qnt,
  *qwm_tlw,
  *qDy_salah,
  *tlw_salah,
]

mamluk_yaman = [
      [
    {
      
      "strL": [
        { "stri": "Asr", "flt": "(?:captive|prisoner)",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Asr", "flt": "(?:form)",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "mlk", "flt": "",},
        { "stri": "ymn", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "fty", "flt": "(?:boy|youth|young|servant)",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "fty", "flt": "girl",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Arb", "flt": "(?:use)",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Arb", "flt": "(?:physical)",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Amw", "flt": "",},
      ],
    },
  ]
]

nisa = [
      [
    {
      
      "strL": [
        { "stri": "nsw", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "mrA", "flt": "(?:woman|women|wife)",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Anv", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "wAd", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "HfZ", "flt": "",},
        { "stri": "frj", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "xmr", "flt": "",},
        { "stri": "jyb", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "bdw", "flt": "",},
        { "stri": "zyn", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "brj", "flt": "displaying",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "wDE", "flt": "",},
        { "stri": "vwb", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "wDE", "flt": "",},
        { "stri": "vwb", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "lam", "flt": "",},
        { "stri": "HyD", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "HyD", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Ahl", "flt": "",},
        { "stri": "byt", "flt": "",},
        { "stri": "qrr", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Ahl", "flt": "",},
        { "stri": "brj", "flt": "display(?!i)",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Ahl", "flt": "",},
        { "stri": "brj", "flt": "display$",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "brj", "flt": "(?:tower|constellation)",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "msk", "flt": "",},
        { "stri": "byt", "flt": "",},
        { "stri": "mwt", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "fH$", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "zny", "flt": " ",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "Drb", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Amw", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "fty", "flt": "girl",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "HSn", "flt": "(?:married|he.*chaste)",},
        { "stri": "nkH", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "HSn", "flt": "",},
        { "stri": "frj", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "HSn", "flt": "(?:store|protect)",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "HSn", "flt": "",},
        { "stri": "qry", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "HSn", "flt": "fortress",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "HSn", "flt": "ing.*chaste",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "HSn", "flt": "chastity",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "HSn", "flt": "(?:married|he.*chaste)",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nkH", "flt": "",},
        { "stri": "mtE", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nkH", "flt": "",},
        { "stri": "wj", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nkH", "flt": "",},
        { "stri": "nsw", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nkH", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "bny", "flt": "[Dd]aughter",},
      ],
    },
  ],
]

ahl_kitab = [
      [
    {
      
      "strL": [
        { "stri": "Aty", "flt": "", "strTyp": "root",  "frm": "iv",  "poSp": "V", },
        { "stri": "ktb", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Aty", "flt": "", "strTyp": "root",  "frm": "iv", },
        { "stri": "ktb", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Ahl", "flt": "",},
        { "stri": "ktb", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "<inojiyl", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "taworaY`p", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "zbr", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "SHf", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "sfr", "flt": "book",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "lwH", "flt": "scorching",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "lwH", "flt": "(?:[Tt]ablet|plank)",},
      ],
    },
  ],
]

badr = [
      [
    {
      
      "strL": [
        { "stri": "Amn", "flt": "",},
        { "stri": "xrj", "flt": "",},
        { "stri": "byt", "flt": "",},
        { "stri": "frq", "flt": "",},
        { "stri": "krh", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Twf", "flt": "",},
        { "stri": "$wk", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "mdd", "flt": "",},
        { "stri": "Alf", "flt": "",},
        { "stri": "mlk", "flt": "",},
        { "stri": "rdf", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nEs", "flt": "",},
        { "stri": "Amn", "flt": "",},
        { "stri": "g$w", "flt": "",},
        { "stri": "smw", "flt": "",},
        { "stri": "mwh", "flt": "",},
        { "stri": "vbt", "flt": "",},
        { "stri": "qdm", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "ywm", "flt": "",},
        { "stri": "lqy", "flt": "",},
        { "stri": "jmE", "flt": "",},
        { "stri": "frq", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "wHy", "flt": "",},
        { "stri": "mlk", "flt": "",},
        { "stri": "Drb", "flt": "",},
        { "stri": "Enq", "flt": "",},
        { "stri": "bnn", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Alh", "flt": "",},
        { "stri": "rmy", "flt": "",},
        { "stri": "qtl", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "fAy", "flt": "",},
        { "stri": "qtl", "flt": "",},
        { "stri": "nSr", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "bdr", "flt": "Badr",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "xrj", "flt": "",},
        { "stri": "dyr", "flt": "",},
        { "stri": "bTr", "flt": "",},
        { "stri": "rAy", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "nkS", "flt": "",},
        { "stri": "fAy", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "rAy", "flt": "",},
        { "stri": "qll", "flt": "",},
        { "stri": "nwm", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "rAy", "flt": "",},
        { "stri": "qll", "flt": "",},
        { "stri": "lqy", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Edw", "flt": "",},
        { "stri": "qSw", "flt": "",},
        { "stri": "dnw", "flt": "",},
      ],
    },
  ],
]

qaynuqa = [
      [
    {
      
      "strL": [
        { "stri": "nfq", "flt": "",},
        { "stri": "mrD", "flt": "",},
        { "stri": "grr", "flt": "",},
        { "stri": "dyn", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Ehd", "flt": "",},
        { "stri": "nqD", "flt": "",},
        { "stri": "mrr", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "xwn", "flt": "",},
        { "stri": "xwf", "flt": "",},
        { "stri": "nb*", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "$rd", "flt": "",},
      ],
    },
  ],
]

najran = [
      [
    {
      
      "strL": [
        { "stri": "bhl", "flt": "",},
      ],
    },
  ],
]

uhud = [
      [
    {
      
      "strL": [
        { "stri": "bwA", "flt": "",},
        { "stri": "qEd", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "hmm", "flt": "",},
        { "stri": "Twf", "flt": "",},
        { "stri": "f$l", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "mdd", "flt": "",},
        { "stri": "vlv", "flt": "",},
        { "stri": "Alf", "flt": "",},
        { "stri": "mlk", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "mdd", "flt": "",},
        { "stri": "xms", "flt": "",},
        { "stri": "Alf", "flt": "",},
        { "stri": "mlk", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "qTE", "flt": "",},
        { "stri": "kbt", "flt": "",},
        { "stri": "kfr", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Amn", "flt": "",},
        { "stri": "TwE", "flt": "",},
        { "stri": "kfr", "flt": "",},
        { "stri": "rdd", "flt": "",},
        { "stri": "xsr", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "f$l", "flt": "",},
        { "stri": "ESy", "flt": "",},
        { "stri": "Srf", "flt": "",},
        { "stri": "blw", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "SEd", "flt": "",},
        { "stri": "rsl", "flt": "",},
        { "stri": "Axr", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "jhl", "flt": "",},
        { "stri": "Amr", "flt": "",},
        { "stri": "naA", "flt": "",},
        { "stri": "$yA", "flt": " ",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "ywm", "flt": "",},
        { "stri": "lqy", "flt": "",},
        { "stri": "jmE", "flt": "",},
        { "stri": "wly", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "ywm", "flt": "",},
        { "stri": "lqy", "flt": "",},
        { "stri": "jmE", "flt": "",},
        { "stri": "Swb", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nfq", "flt": "",},
        { "stri": "qtl", "flt": "",},
        { "stri": "tbE", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Axw", "flt": "",},
        { "stri": "qEd", "flt": "",},
        { "stri": "qtl", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nEs", "flt": "",},
        { "stri": "Amn", "flt": "",},
        { "stri": "g$w", "flt": "",},
        { "stri": "Twf", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "End", "flt": "",},
        { "stri": "kfr", "flt": "",},
        { "stri": "qtl", "flt": "",},
        { "stri": "mwt", "flt": "",},
        { "stri": "maA", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "lyn", "flt": "",},
        { "stri": "rHm", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "gll", "flt": "",},
        { "stri": "nbA", "flt": "",},
        { "stri": "maA", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "jwb", "flt": "",},
        { "stri": "rsl", "flt": "",},
        { "stri": "qrH", "flt": "",},
      ],
    },
  ],
]


bir_mauna = [

]


hamra = [

]

ahzab = [
      [
    {
      
      "strL": [
        { "stri": "jnd", "flt": "",},
        { "stri": "jyA", "flt": "",},
        { "stri": "lam", "flt": "",},
        { "stri": "rAy", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nfq", "flt": "",},
        { "stri": "mrD", "flt": "",},
        { "stri": "wEd", "flt": "",},
        { "stri": "grr", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Twf", "flt": "",},
        { "stri": "yavorib", "flt": "",},
        { "stri": "laA", "flt": "",},
        { "stri": "qwm", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "A*n", "flt": "",},
        { "stri": "byt", "flt": "",},
        { "stri": "Ewr", "flt": "",},
        { "stri": "frr", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "dxl", "flt": "",},
        { "stri": "sAl", "flt": "",},
        { "stri": "ftn", "flt": "",},
        { "stri": "Aty", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Ehd", "flt": "",},
        { "stri": "laA", "flt": "",},
        { "stri": "wly", "flt": "",},
        { "stri": "dbr", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Ewq", "flt": "",},
        { "stri": "Axw", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "xwf", "flt": "",},
        { "stri": "slq", "flt": "",},
        { "stri": "lsn", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Hsb", "flt": "",},
        { "stri": "Hzb", "flt": "",},
        { "stri": "*hb", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Amn", "flt": "",},
        { "stri": "rAy", "flt": "",},
        { "stri": "Hzb", "flt": "",},
        { "stri": "wEd", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "rdd", "flt": "",},
        { "stri": "kfr", "flt": "",},
        { "stri": "gyZ", "flt": "",},
      ],
    },
  ],
]

qurayza = [
      [
    {
      
      "strL": [
        { "stri": "SyS", "flt": "",},
        { "stri": "Ahl", "flt": "",},
        { "stri": "ktb", "flt": "",},
        { "stri": "qtl", "flt": "",},
        { "stri": "Asr", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "wrv", "flt": "",},
        { "stri": "ArD", "flt": "",},
        { "stri": "dwr", "flt": "",},
        { "stri": "wTA", "flt": "",},
      ],
    },
  ],
]

fidak = [

]

nadir = [
      [
    {
      
      "strL": [
        { "stri": "HSn", "flt": "",},
        { "stri": "Ahl", "flt": "",},
        { "stri": "ktb", "flt": "",},
        { "stri": "H$r", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "fyA", "flt": "",},
        { "stri": "Ahl", "flt": "",},
        { "stri": "qry", "flt": "",},
        { "stri": "rsl", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "nfq", "flt": "",},
        { "stri": "Axw", "flt": "",},
        { "stri": "Ahl", "flt": "",},
        { "stri": "ktb", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "jlw", "flt": "",},
        { "stri": "E*b", "flt": "",},
        { "stri": "dnw", "flt": "",},
      ],
    },
  ],
]

hudaybiya = [
      [
    {
      
      "strL": [
        { "stri": "byE", "flt": "",},
        { "stri": "$jr", "flt": "",},
      ],
    },
  ]
]

khaybar = [
      [
    {
      
      "strL": [
        { "stri": "wEd", "flt": "",},
        { "stri": "gnm", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "gnm", "flt": "",},
        { "stri": "xlf", "flt": "",},
        { "stri": "tbE", "flt": "",},
      ],
    },
  ],
]

dhu_amr = [

]

dhat_riqa = [

]

kurz = [

]

mutah = [

]

hunayn = [

]

tabuk = [
      [
    {
      
      "strL": [
        { "stri": "nfr", "flt": "",},
        { "stri": "vql", "flt": "",},
        { "stri": "ArD", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "bEd", "flt": "",},
        { "stri": "$qq", "flt": "",},
        { "stri": "tbE", "flt": "",},
        { "stri": "Hlf", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "krh", "flt": "",},
        { "stri": "jhd", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "A*n", "flt": "",},
        { "stri": "jhd", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "A*n", "flt": "",},
        { "stri": "qEd", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "xlf", "flt": "",},
        { "stri": "qEd", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "E*r", "flt": "",},
        { "stri": "Erb", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Aty", "flt": "",},
        { "stri": "Hml", "flt": "",},
        { "stri": "dmE", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Erb", "flt": "",},
        { "stri": "nfq", "flt": "",},
        { "stri": "grm", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "rDw", "flt": "",},
        { "stri": "maEa", "flt": "",},
        { "stri": "xlf", "flt": "",},
      ],
    },
  ],
]

dirar = [
      [
    {
      
      "strL": [
        { "stri": "sjd", "flt": "",},
        { "stri": "Drr", "flt": "",},
      ],
    },
  ],
]

sufyan = [

]

jhd = [
    *badr,
    *qaynuqa,
    *najran,
    *uhud,
    *bir_mauna,
    *hamra,
    *ahzab,
    *qurayza,
    *fidak,
    *nadir,
    *hudaybiya,
    *khaybar,
    *dhu_amr,
    *dhat_riqa,
    *kurz,
    *mutah,
    *hunayn,
    *tabuk,
    *dirar,
    *sufyan,
]

fadl = [
        [
    {
      
      "strL": [
        { "stri": "fDl", "flt": "",},
        { "stri": "EalaY", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "fDl", "flt": "",},
        { "stri": "drj", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "drj", "flt": "(?:[Dd]egree|[Rr]ank)",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "drj", "flt": "",},
        { "stri": "EalaY", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "rfE", "flt": "",},
        { "stri": "drj", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "sxr", "flt": "",},
        { "stri": "bED", "flt": "",},
      ],
    },
  ],
]

zann = [
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "jhl", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Amr", "flt": "",},
        { "stri": "naA", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Hrm", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "tbE", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "$bh", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Slb", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "EiysaY", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "masiyH", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "nfs", "flt": "",},
        { "stri": "xyr", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Amn", "flt": "",},
        { "stri": "xyr", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Afk", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "jnb", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Avm", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Alh", "flt": "Allah",},
        { "stri": "swA", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "Znn", "flt": "assum",},
        { "stri": "swA", "flt": "",},
      ],
    },
  ],
]

ftn = [
    [
    {
      
      "strL": [
        { "stri": "Ehd", "flt": "",},
      ],
    },
  ],
        [
    {
      
      "strL": [
        { "stri": "wvq", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "blw", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "ftn", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "Hml", "flt": "",},
        { "stri": "Ans", "flt": "",},
        { "stri": "Amn", "flt": "",},
      ],
    },
  ],
      [
    {
      
      "strL": [
        { "stri": "*rr", "flt": "",},
        { "stri": "bnw", "flt": "",},
        { "stri": "A^dam", "flt": "",},
      ],
    },
  ],
]

araf = [
        [
            {
                "strL": [
                    {
                      "stri": "Erf",
                      "strTyp": "root",
                      "poSp": "V",
                      "frm": "i"
                    },
                ],
                "lbl": "Erf i"
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": "Erf",
                      "strTyp": "root",
                      "poSp": "V",
                      "frm": "ii"
                    },
                ],
                "lbl": "Erf ii"
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": "Erf",
                      "strTyp": "root",
                      "poSp": "V",
                      "frm": "vi"
                    },
                ],
                "lbl": "Erf vi"
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": "Erf",
                      "strTyp": "root",
                      "poSp": "V",
                      "frm": "viii"
                    },
                ],
                "lbl": "Erf viii"
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": ">aEoraAf",
                      "strTyp": "lem",
                      "poSp": "N",
                    },
                ],
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": "Eurof",
                      "strTyp": "lem",
                      "poSp": "N",
                    },
                ],
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": "maEoruwfap",
                      "strTyp": "stem",
                      "poSp": "ADJ",
                    },
                ],
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": "m~aEoruwf",
                      "strTyp": "lem",
                      "poSp": "N",
                      # "frm": "i"
                    },

                ],
            },
        ],
]

shahada = [
	*araf,
]

naSara = [
    [
      {
        "strL": [
          {
            "stri": "naSoraAniy~",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
      }
    ],
    # *nSr_isa_maryam,
    [
      {
        "strL": [
          {
            "stri": "naSiyr",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
              "stri": "masiyH",
              "strTyp": "lem",
              # "poSp": "N",
              # "frm": "i",
          },
        ],
      }
    ],
    [
      {
        "strL": [
          {
            "stri": "naSiyr",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
              "stri": "EiysaY",
              "strTyp": "lem",
              # "poSp": "N",
              # "frm": "i",
          },
        ],
      },
    ],
    [
      {
        "strL": [
          {
            "stri": "HawaAriy~uwn",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
        # "lbl": "حور iii"
      }
    ],
    # *Hwr_isa_maryam
]

hwd_yahudi = [
    *hwd,
    [
      {
        "strL": [
          {
            "stri": "yahuwdiy~",
            "strTyp": "lem",
            # "poSp": "PN",
            # "frm": "i",
          }
        ],
      }
    ],
]

hwd_yahudi_israel = [
    *hwd_yahudi,
    *israel,
]

kitab_munir = [
    [
      {
        "strL": [
          {
            "stri": "kita`b",
            "strTyp": "lem",
            # "poSp": "PN",
            # "frm": "i",
          },
          {
            "stri": "m~uniyr",
            "strTyp": "lem",
            # "poSp": "PN",
            # "frm": "i",
          }
        ],
      }
    ],
]

kutub = [
    *SHf,
    *torah,
    *injil,
    *zbr,
    *kitab_munir,
    [
      {
        "strL": [
          {
            # "stri": "kita`b",
            # "strTyp": "lem",
            "stri": "kita`bu",
            "strTyp": "stem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
            "stri": "muwsaY`",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
      }
    ],
    [
      {
        "strL": [
          {
            "stri": "nzl",
            "strTyp": "root",
            # "poSp": "V",
            # "frm": "iv",
          },
          {
        "wrdDisPos": 2,
            "stri": "maA",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
        "wrdDisPos": 2,
            "stri": "qabol",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
      }
    ],
    [
      {
        "strL": [
          {
            "stri": "nzl",
            "strTyp": "root",
            # "poSp": "V",
            # "frm": "iv",
          },
          {
        "wrdDisPos": 2,
            "stri": "kita`b",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
        "wrdDisPos": 2,
            "stri": "qabol",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
      }
    ],
    [
      {
        "strL": [
          {
            "stri": "nzl",
            "strTyp": "root",
            # "poSp": "V",
            # "frm": "iv",
          },
          {
        "wrdDisPos": 2,
            "stri": "{l~a*iY",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
        "wrdDisPos": 2,
            "stri": "qabol",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
      }
    ],
    [
      {
        "strL": [
          {
            "stri": "maE",
            "strTyp": "lem",
            # "poSp": "V",
            # "frm": "iv",
          },
          {
        "wrdDisPos": 1,
            "stri": "maA",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
        "wrdDisPos": 1,
            # "stri": "qabol",
            # "strTyp": "lem",
            # # "poSp": "N",
            # # "frm": "i",
          }
        ],
      }
    ],
]

milla_ibrahim = [
    [
      {
        "strL": [
          {
            "stri": "mil~ap",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
            "stri": "<iboraAhiym",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
      }
    ],
]

Hanif_milla_ibrahim = [
    *milla_ibrahim,
    *Hanif,
]

ahl_kitab = [
# ahl_kitab_majus_sabian = [
    *kitab_ahl,
    *majus,
    *sabian,
    *Hanif_milla_ibrahim,
    *kutub,
    *naSara,
    *hwd_yahudi_israel,
]

qiyamah_saah_hashr = [
        *nushur,
        *hayy_mawt,
        *qbr_ajdath_bEthr_bEth,
        *qiyamah_saah,
]