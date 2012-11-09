# -*- coding: utf-8 -*-

TEST = {
        'TYPE' : (('function', '功能测试'),
                  ('performance', '性能测试')
                  ),
        'STRATEGY' : (('regress', '回归测试'),
                      ('increment', '增量测试')
                      )
        }
        
STATUS = {
        'FUNCTION' : (('plan', '计划中'),
                      ('online', '已上线'),
                      ('discard', '已废弃')
                      )

        }
        
ENV = {
           'OS' : (('', '---------'),
                   ('hp_unix', 'HP-Unix'),
                   ('aix', 'AIX'),
                   ('win_nt', 'Window NT'),
                   ('linux', 'Linux')),
           'CHR' : (('', '---------'),
                    ('utf-8', 'UTF-8'),
                    ('gbk', 'GBK')),
           'DB' : (('', '---------'),
                   ('oracle_9', 'Oracle 9i'),
                   ('oracle_10', 'Oracle 10g'),
                   ('oracle_11', 'Oracle 11g'),
                   ('db2_8.3', 'DB2 v8.3'),
                   ('db2_8.7', 'DB2 v8.7'),
                   ('db2_9.1', 'DB2 v9.1'),
                   ('db2_9.5', 'DB2 v9.5'),
                   ('db2_9.7', 'DB2 v9.7'),
                   ('kingbase', 'KingBase')
                   ),
           'JRE' : (('', '---------'),
                    ('jre5', 'JRE_1.5(5.0)'),
                    ('jre6', 'JRE_6.0'),
                    ('jre7', 'JRE_7.0')),
           'BROWSER' : (('', '---------'),
                        ('ie6', 'Internet Explorer 6'),
                        ('ie7', 'Internet Explorer 7'),
                        ('ie8', 'Internet Explorer 8'),
                        ('ie9', 'Internet Explorer 9'),
                        ('ff', 'FireFox'),
                        ('chrome', 'Chrome'),
                        )
           }
