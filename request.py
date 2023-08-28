import requests

# URL and headers from the provided request
url = "https://ids.priceline.com/idp/idx/introspect"
headers = {
    "Host": "ids.priceline.com",
    "Cookie": "vid=v20230828173731588c9754; Referral=CLICKID=&WEBENTRYTIME=8%2F28%2F2023%2017%3A45%3A39&ID=DIRECT&PRODUCTID=&SOURCEID=DT; DCS=MnwxNjkzMjU5MTQxfnVua25vd25fZmFzdGx5X3BvcA==.N2ZyV1RySEVFVi9USHAvanFlRldoMVZmTmFrSWFadUFXYlVkYzdBeGpsWT0=; PL_CINFO=38c661d42d596ba826c53eae651fef2d~1693258959~v2; SITESERVER=ID=38c661d42d596ba826c53eae651fef2d; forterToken=04ac6daeaa9e45db91964aa0d95ff0ef_1693259140733__UDF43-m4_17ck; _ga_DC72C50JN6=GS1.1.1693258656.1.1.1693259141.59.0.0; _ga=GA1.2.1408732199.1693258656; ftr_blst_1h=1693258656208; _pxvid=17cfaaff-45eb-11ee-a4c4-b79cae465d52; pxcts=1a547068-45eb-11ee-ac22-4c704f744466; _pxde=cad63bca678a1db85b770e75f99de5fa8cc4e0de3063a877b341d40a45a3991e:eyJ0aW1lc3RhbXAiOjE2OTMyNTkxNDEwMTUsImZfa2IiOjB9; AMP_TOKEN=%24NOT_FOUND; __pxvid=1b081f36-45eb-11ee-b446-0242ac120003; OptanonConsent=isIABGlobal=false&datestamp=Tue+Aug+29+2023+03%3A42%3A54+GMT%2B0600+(Bangladesh+Standard+Time)&version=6.6.0&hosts=&consentId=c954480c-e5e9-4cb1-90e5-3262672b2b6e&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0003%3A1%2CSPD_BG%3A1&AwaitingReconsent=false; _gid=GA1.2.1331227125.1693258657; _px2=eyJ1IjoiZDc4MWU3NzAtNDVlYi0xMWVlLWE3ZDYtYmYzZTY3OTgyNzEyIiwidiI6IjE3Y2ZhYWZmLTQ1ZWItMTFlZS1hNGM0LWI3OWNhZTQ2NWQ1MiIsInQiOjE2OTMyNTkyNzUxMDgsImgiOiIyNzkwMGU0YjU2ZGFjOTNlZGU0YjQzZmJlMDhhNjVkOTg4Yzk5YjA0ZWE0ZDZhNWJmMTlkOTQ3NDM1YTFkNGUxIn0=; utag_main=v_id:018a3e14ae8d00132e0a00fb185505050001a00d0093c$_sn:1$_se:2$_ss:0$_st:1693260580551$ses_id:1693258657421%3Bexp-session$_pn:2%3Bexp-session$cookiesyncran:true%3Bexp-session; _cq_duid=1.1693258658.Mb9cO0Avkij290YJ; _cq_suid=1.1693258658.v0gUlbyGh2VN4LLU; _gcl_au=1.1.1972271661.1693258659; _scid=e1e4e45c-67a5-4bd9-92f2-b35df1923361; _sctr=1%7C1693245600000; _fbp=fb.1.1693258662383.363928045; _tt_enable_cookie=1; _ttp=VUHlNEKtM8GNCeA2V98ok-yw1g5; cto_bundle=VfSrqF9JbWs5SXFQN2MybTVkZ0c2QThMU2pQVmZKOVVybHNtZzd1eVBmczd6TXlBQVpLd3FQczFsQWZqQ0hKR1RObHV0SGJMc2JGZUFOMlNlTkpHR1laVmhyZmNoSW1DVEZQaHlhYVlBc0FtQVVkUWUlMkJkazVIQTFUQTB1Q1l2T2FFTG1tOE1IemVrSnFpNVdoYll3bWslMkJHdE5RJTNEJTNE; __gads=ID=e607a529b8f1b78e:T=1693258664:RT=1693258664:S=ALNI_MYAXPtTr5nIf0NxpvO0BnF_Gw9S7g; __gpi=UID=00000c353e5318a7:T=1693258664:RT=1693258664:S=ALNI_MaU1D3UQrenB1rcp-n6Jz4jqOlgLA; JSESSIONID=4718E47B9F36EAD86E69D264BB502383; t=default; DT=DI1SUVPl1-1S0KjPibyUP-ZHA; _pxhd=eOInaz1gMnI0JtDVaK3LAdUZ7o5bQidKN7JT9QUpRGn7vDj0WUsxdzC8OOf5lZ0S2ROw617Mn9ZzyuyVOS2fQQ==:4jXMG6z/gGjP44sgxlAyDKzdlWA5-tWeH90xduC0wNY5EXvWXbWyCF2Cc7-121Adn3GXdRmvwVRmoyGRtpBqhKttL3iUfWdC1kkHHLDCquI=; LogIn=DATA=E128FAD68FBC0D76BE36AF8846928259F1A0CAB55A51590B68926A3DAFFCAAE1D0B58FFF60B5DA3ED39F02EB2CC2D592E4989E2DFB1E1CA394C1ABA56231E5FD8B5F445B379DCF6BA21EEB150E5BFD4B; _scid_r=e1e4e45c-67a5-4bd9-92f2-b35df1923361; _uetsid=1c633b9045eb11eeb276b9580c9fc831; _uetvid=1c633d5045eb11ee92c8057e3861b527; FCNEC=%5B%5B%22AKsRol8Ziw6NIsIVUAGAUHH1NudI0bNL-4C2fRPXtiMEOnl-dn9FwaPtWqx8MGcLw5VBtijMnIycyujjYc969-Rt04wJWa5Rl4ftJVEy6KRABlFbUDVj2UjXLhYwwBEN2XGvyy4nOYLj_W2wUqUWrS3B9RzCTp7zUw%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; LPVID=Q3MzA1YWEzMGM5Mzc3YTQ5; LPSID-38721557=wUb94j9yRYe9nwKXz7rXRw; luf_-519401772=eyJ6aXAiOiJERUYiLCJ2ZXIiOiIxIiwiYWxpYXMiOiJlbmNyeXB0aW9ua2V5Iiwib2lkIjoiMDBvNDMwMzM0ZkpTM1lSaUk2OTYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIiwidGltZXN0YW1wIjoxNjkzMjU4OTU4MTY1fQ..Nrz760KmGQlwyRS0.1e4mQ24lcmIhGN85-cOtF-erxDLK3Rj_QAiNpfOkRiFyo5bqtHPAE78vuBVmS3WI2m6n36UXWk-8xoeSFNniFNAfg5DPaNzwgQGThEKb_f13lbYAIoqyCqH3m1FfckKWAbEgSAdNO7CL83967KtQ931cCDJTh0twc2BEPSf6MLfESZPpFza57Tw5Nv2bK0x1QhDzHPsj.LGfVHFtJLY3So9Vd5OTkRg; _dc_gtm_UA-2975581-1=1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Accept": "application/ion+json; okta-version=1.0.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://www.priceline.com/",
    "Content-Type": "application/ion+json; okta-version=1.0.0",
    "X-Okta-User-Agent-Extended": "okta-auth-js/7.1.0 okta-signin-widget-7.0.2",
    "Content-Length": "1193",
    "Origin": "https://www.priceline.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Te": "trailers"
}

# JSON payload from the provided request
payload = {
    "interactionHandle": "eyJ6aXAiOiJERUYiLCJhbGlhcyI6ImVuY3J5cHRpb25rZXkiLCJ2ZXIiOiIxIiwib2lkIjoiMDBvNDMwMzM0ZkpTM1lSaUk2OTYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0..OXHCP_MGSjHIlScw.DBMMTSE9Tcc7-i6U4VUx7xE-CvyuPqnmwaQ-ZJhvFMNc0aeswbaWpm-6e1ACXDVohYI6SvicyhchTu4wylNxVnTDvktJf0JPx6r6CV2KcCJxqSbtgHEJLqxzExwExNf2yYSjg0lk9YUb63uqjpZT1VrxVNUPVfFV6q4tgSNbAr2wIuJ-_5172bmZoVJpq8ciUi_UrAheKqGZvejwFaKrL_Hp_GXTSbMTnNugqcyezxuTuJhx3I_cpR6DxWVmrP3DdtjJqRIPiCQpGvLPFwwy_IHFUp6J0KKsKY0Jy7cUSG2IS-gRwRqpnsC-BMUaFG441RkICYhEMfJvUlqLAzU7sy_V43HbCc8f-U57UtzeOPwHU58_bd9KK8RLz38BxO9pOatBNyVRf0NTY0cC1g8L1MvsBeJbE716zK7CyfE3tflr15cvTPuqx1grd5Juki0T707h7Avds6FJAOQXD96Y6IaaW4FTjO3NC-BFM7q7tWfIUGcj7Jl7u38cDYDpE44ybXW3b4kvFC3llyHIavNUTsjSYuSUZCXmF-oqk6vITHAcb0oDd37Wafs78gNLOYYQDm-bZ9Bn-VVVdQrY-0D3flHbnG33JZ4_fkpK2Y54xcnPAqO9vHwPd5ZOo6FXjEfkGfgVYpE-t09ZrQ9IvzV_mGopLahp6qBaPHRhhvX4WorQNjmQL5mo0UFpeVktAQtM5GCTNlXheVdtKhyPxWen97os0sg3LLfSUMvn0dI-0glxNmdUjkcY7qFlALEE5YN_uwfVRl78P-t52-hQ5m3e9Z2Bc4OXOoOwMRXpg9c0efsnzTsSlM8dN2fUbX2ov2P_HEhIyYr4oa2bZ4f0gGduXjpghL2MOlmCO0RvNhz9aQPrTM5Hk5j2SYs3D4sJy4xtfOGnBP3wjwyGxLuclLPgt16rnZBB3hh07Wjz6BBvNK5xYNfKXLKhxOHwGjOq7yTS6CIGSFnjHKZsEse6pubVrQK38k9T.pqCt3hxh1lPdZUvplzjmLg"
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Print the response content
print(response.text)
