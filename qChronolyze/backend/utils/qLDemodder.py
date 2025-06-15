def qLDemodder(qLMod,):
    qL = [
                # [combClass(**comb).combObj for comb in optLs]
                [
                    [
                        {
                            **comb,
                            "strL": [
                                strObj.__dict__
                                for strObj in comb["strL"]
                            ]
                        }
                        for combObj in optLs
                        if (comb := combObj.__dict__)
                    ]
                    for optObj in optLs
                ]
                for optLs in qLMod
            ]
    return qL