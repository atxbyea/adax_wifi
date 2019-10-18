"""Parameter file for Adax integration"""

def set_param(api_call):
    switcher= {
    "account_id": '70810',
    "appVersion": 'iOS-adax-2.4.0',
    "device": 'iPhone10,4',
    "os": 'iOS 2012.4',
    "timeOffset": '120',
    "timeZone": 'Europe/Stockholm',
    "zone_signature": '302C02142396D58EF80C3E7630649E9B58ADCB4018FDF93F0214079A870064DBFE22691A27FC09F3AFE23B7A7B22',
    "heat_signature": '302D0214035B337E5CDDC9EE3C5974E1604EA55653689A710215009740C147DAAB144859E592B9BC4493DBC2CAA004',
    0: '302D02146DB0C8258FF87CE123E1C8A511C481485434226B02150080BD1B0DE19DEABD3D8EE007AA09B93EB3BBBFBA', #Set as HVAC_OFF
    5: '302D02142572F806E126F9F4DEF0510AF7A9526ED3AC91D70215008C2CC57D6EA974FB928423C50E366261D4DD315B',
    6: '302C02144763E7F1040A8E64F7BD77CDFDA5F8CF39D6803102145392E9E8C20EF4ED9B64866210F2C6D2A1C5DF87',
    7: '302C021447D6CA84DB4C9B23670D25B1916E9A985572591F02141150F3CCE6C95F57917133B8A04FB75E0BAB1F98',
    8: '302D02142D2F9D45728144E2511A7AABA8C3763F2259A4EB0215008D2285BF1A1B6D43B30EF9124BD310C10737D0E6',
    9: '302C02144E2CC077E5E086A97E334E475D8C3D109D85B571021412DCEB01D4DA5A828D26F3CEBA16DE0D9C4C0CD8',
    10:'302C02142B6B67AA0CAE177F045E2588B393ACD0492E4F37021412050471849CDAF516C69632779979E5D3044A28',
    11: '302D0214127FB7A6B92670E124FF9E9DE2EDA5E9830C90E3021500930B2FB00B4D14B87B8A3984F193E56F44D3C44D',
    12: '302D0214265B8D5FF85F7D751910B8395F7B630CD3BBD022021500810D9AF862FB3CD21A0EE73F91BE4224E1A66A3C',
    13: '302D02147CF2CB76495A2588A855EEEC8D7A38830149E4120215008256A296AB449A836ED3BBA1C48E968474418CD5',
    14: '302C02142C4C055EFE9E8F538DE9348F6A9064BF9CC32B320214786782194A27F9B12C7B25CE878736E5CC5D6093',
    15: '302C0214691350126E048643205F4B6C37D25F2706DF3EA40214607107BB6BA7BD4A01EF4608FB200BF46EEBC03F',
    16: '302C0214735998FF089C3B6725DFEEADCFBB7039A3F5AF430214526B98025A4B39EBCDA0F4C6CF633E8FED64174B',
    17: '302C02141B0BCBFFD4B7231D23CC4E08395DDE052703EEDB021472D598717D83E3DF15CC8FB579F7EBA266041356',
    18: '302C0214538958EF88687DD6204B2FF6046F6B907E1B3CA00214238D26100DAE2D5432F7ACD04E24D363ED29D4F4',
    19: '302C02142A545AA54CE95B944E83ACFDF46CB300BAD360A702144F4E005610E9009D5FC0531C1C49F32F1FDC1960',
    20: '302C0214075AEC9AC550E169E6DA599F0B1884F8EBEC87DC02144E61FC761F683484BD45D56D2A884C15BFBF90FA',
    21: '302D021436CC3B6905AED3FF924DB5861400246FC4C678D10215008F9ECF26C988F695F10A782396E18B351605D029',
    22: '302C021441A94907C65BAE1D10ECDB773A14E0742AF595EF02144673A43A22ED3E4F0BBA16FC94F043273492C5B0',
    23: '302C02146118E38DE67D61116D0B561211BF3F50CCFCD21E021425B1E22D547BFFC79AC15C24DF103EBFBA6F63AB',
    24: '302D02150094C85DBA9306B43F11ECEF85DB0BEC101AF628EF0214273F8BEBD09E07AFAB871AD67D2493D598738C3A',
    25: '302C021475A78DDF64920ED6FCD23F364EA43B8D22C1822E02144C1659BAE905BCE0C79171A1555D730A09F258F1',
    26: '302C0214079D216F7B7D58A01C0E33766BFAC1107725EFD702143B21F3AF79EB0B4B02B546EB584FE63E1245D4F1',
    27: '302C02143C3226D11ACB16E98DDC530DD7086D6702CD7AE90214543AB787A43791075B77A92669C2DD5E7B0AB5D0',
    28: '302D02145A3C251281DAEE4306BB03F1B122FD3C2D7DBE9A0215009466D294247FE45DB6C580F242FAB77E4FE48AE1',
    29: '302C02144FC0BBDF191C99FA25422C9F8B29267B3649AD0C021422B76133F0D47DB68774920F31186334DB4CF5F0',
    30: '302C0214409F748BCBAFC5C0A2B94F33854F77D5DD04D5B902143FCF3302336F0CAD835FFAE7AC764FD146FE70FE',
    31: '302C02144F87CE1BAE7523C47ADC29E7B0B24E67FC8FC55E02140F00C5F27969A708F59464B9747E437D10A07384',
    32: '302C021465D8E8BD80497799BC01A494F55231610E98F53C021414DE375C9350BC0B30CF950FF721CFD2249E0567',
    33: '302C02141FD2B42B6F98F2051F61AA35BDB0D75AFB0A7A7D02140FD0F9C58C95F6A5DA1FA2496F516371DBAE2961',
    34: '302C02145DBF0067070E0B2FABBFA818146B7BB90C772FB102145408A1D8A5B383D492601797AA159ADF77BACCF0',
    35: '302C021405CA12F5839A518B8E2D8F9C66C6068FF32DCE3902147939A2C065633A71D87ABC022C9A6D3C95B2FA0C'
    }
    return switcher.get(api_call,"Key missing")