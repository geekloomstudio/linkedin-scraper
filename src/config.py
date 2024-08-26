import os

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env_name = os.getenv("ENVIRONMENT")
if env_name is None:
    raise Exception("ENVIRONMENT name is required.")
else:
    ENV_FILE = os.path.join(BASE_DIR, "environment/{}".format(env_name))

load_dotenv(ENV_FILE)

cookies = {
    "bcookie": '"v=2&85d1f2f6-385e-4877-89cc-f5ff9ca4967f"',
    "li_sugr": "94e66fe7-febb-4e0f-94bc-2d66fb22e5cf",
    "bscookie": '"v=1&20240824111153cabaf884-0cf6-4666-838c-abe1d2f71d0fAQGOZBjcjZuJBrKuTc0yggX7bHiSa3vi"',
    "UserMatchHistory": "AQIiS7-uHtaGLQAAAZGKOKOS4IxsL9ExMJJzVu1A00dS83wVi3eej8WInXRV8OKqox5DYVH4PtYCQw",
    "AnalyticsSyncHistory": "AQLfQ7vcvzoVzwAAAZGKOKOSj0whG4gHli0F01fxwD17WOjqfF1xbX0d69CJDaZGrLSma3O4PiVfRYXmUW5tSQ",
    "lang": "v=2&lang=en-us",
    "AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg": "1",
    "AMCV_14215E3D5995C57C0A495C55%40AdobeOrg": "-637568504%7CMCIDTS%7C19961%7CMCMID%7C31784810351289779673511960927649323225%7CMCAAMLH-1725223389%7C12%7CMCAAMB-1725223389%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1724625789s%7CNONE%7CvVersion%7C5.1.1",
    "aam_uuid": "32299479921799521003491366029905636114",
    "g_state": '{"i_t":1724704992115,"i_l":1,"i_p":1724625794045}',
    "li_rm": "AQGGvqXKTCpIngAAAZGLR1rVXpkLbP0TEPrYaghsPbj6ntV0zLNyrEEnIeCCqN8YncWTznfZlzbq9yGRX-rv3LMRc95KdSeGk-xHrQ-MTE-kUc9eUPiIOuHx",
    "_gcl_au": "1.1.336130508.1724618597",
    "liap": "true",
    "li_at": "AQEDASsBRUoBAXfuAAABkYtIW7gAAAGRr1TfuE4AwejSGxHhaqe4faewCKVGfd9wC5bX9Np6WRfh1U0OrszkwG1px0Zt90aIXkuBENvZDplcjmV4eHgUcU2z63-2GVPcNIRObSzBKePb5_1u3O4yzSlH",
    "JSESSIONID": '"ajax:7375956543741358092"',
    "timezone": "Asia/Calcutta",
    "li_theme": "light",
    "li_theme_set": "app",
    "dfpfpt": "e0778f2831334a24b83478f8d4ab26cd",
    "fptctx2": "taBcrIH61PuCVH7eNCyH0FWPWMZs3CpAZMKmhMiLe%252bEsVtMKWFaxwfi%252bu349WzxDUai7ufm5X%252bN6Soy4BQjn6Duv2b8B9MW5fHweFrhOS3lrBS4SNZ%252f%252bcPMdvOF1cnCfjUjqFDpqhKhrZ%252b0YAOYjIuseA9so7bcjVkq6pUEGM6VQruY6pQBcQv8rPml%252fY%252fl2w8UoZxgOSWVv8elLGqiqu6m3FafnmlABiWcSskGsdFIKy9A6d2Sk%252bH6k8dxShh%252baj3gLNqdFb7wK1y6kBaQfgxkxB8nj907UC2uVg9QXK1bOhvChw7lagVSAL6JuD08I7e%252f%252fM4nEs2T3s%252bYLbXEtOHBi0cr%252bkt0F01DGbgerX6s%253d",
    "s_fid": "24CF82E5EA2F4706-06A7A1D06023D0F1",
    "gpv_pn": "www.linkedin.com%2Fcompany%2Fid-redacted%2Fadmin%2Fanalytics%2Fvisitors%2F",
    "s_plt": "5.45",
    "s_pltp": "www.linkedin.com%2Fcompany%2Fid-redacted%2Fadmin%2Fanalytics%2Fvisitors%2F",
    "s_cc": "true",
    "s_ips": "617",
    "lidc": '"b=OB62:s=O:r=O:a=O:p=O:g=5997:u=950:x=1:i=1724620944:t=1724626094:v=2:sig=AQGQszbeeDtT2PgVdgCwz0EckBlSNzSV"',
    "s_tslv": "1724623124844",
    "s_sq": "lnkdprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dwww.linkedin.com%25252Fcompany%25252Fid-redacted%25252Fadmin%25252Fanalytics%25252Fvisitors%25252F%2526link%253DMember%2525E2%252580%252599s%252520name%252520Sai%252520Shandilia%252520S%252520S%252520K%252520Sai%252520Shandilia%252520S%252520S%252520K%252520Member%2525E2%252580%252599s%252520occupation%252520Product%252520%252540%252520OkCredit%252520%25257C%252520Ex-Zilingo%252520%25257C%252520IIT%252520Madras%2526region%253Dember6166%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dwww.linkedin.com%25252Fcompany%25252Fid-redacted%25252Fadmin%25252Fanalytics%25252Fvisitors%25252F%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.linkedin.com%25252Fin%25252Fssk-sai-shandilia%2526ot%253DA",
    "s_tp": "8426",
    "s_ppv": "www.linkedin.com%2Fcompany%2Fid-redacted%2Fadmin%2Fanalytics%2Fvisitors%2F%2C94%2C7%2C7951%2C4%2C13",
}

headers = {
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    # 'cookie': 'bcookie="v=2&85d1f2f6-385e-4877-89cc-f5ff9ca4967f"; li_sugr=94e66fe7-febb-4e0f-94bc-2d66fb22e5cf; bscookie="v=1&20240824111153cabaf884-0cf6-4666-838c-abe1d2f71d0fAQGOZBjcjZuJBrKuTc0yggX7bHiSa3vi"; UserMatchHistory=AQIiS7-uHtaGLQAAAZGKOKOS4IxsL9ExMJJzVu1A00dS83wVi3eej8WInXRV8OKqox5DYVH4PtYCQw; AnalyticsSyncHistory=AQLfQ7vcvzoVzwAAAZGKOKOSj0whG4gHli0F01fxwD17WOjqfF1xbX0d69CJDaZGrLSma3O4PiVfRYXmUW5tSQ; lang=v=2&lang=en-us; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19961%7CMCMID%7C31784810351289779673511960927649323225%7CMCAAMLH-1725223389%7C12%7CMCAAMB-1725223389%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1724625789s%7CNONE%7CvVersion%7C5.1.1; aam_uuid=32299479921799521003491366029905636114; g_state={"i_t":1724704992115,"i_l":1,"i_p":1724625794045}; li_rm=AQGGvqXKTCpIngAAAZGLR1rVXpkLbP0TEPrYaghsPbj6ntV0zLNyrEEnIeCCqN8YncWTznfZlzbq9yGRX-rv3LMRc95KdSeGk-xHrQ-MTE-kUc9eUPiIOuHx; _gcl_au=1.1.336130508.1724618597; liap=true; li_at=AQEDASsBRUoBAXfuAAABkYtIW7gAAAGRr1TfuE4AwejSGxHhaqe4faewCKVGfd9wC5bX9Np6WRfh1U0OrszkwG1px0Zt90aIXkuBENvZDplcjmV4eHgUcU2z63-2GVPcNIRObSzBKePb5_1u3O4yzSlH; JSESSIONID="ajax:7375956543741358092"; timezone=Asia/Calcutta; li_theme=light; li_theme_set=app; dfpfpt=e0778f2831334a24b83478f8d4ab26cd; fptctx2=taBcrIH61PuCVH7eNCyH0FWPWMZs3CpAZMKmhMiLe%252bEsVtMKWFaxwfi%252bu349WzxDUai7ufm5X%252bN6Soy4BQjn6Duv2b8B9MW5fHweFrhOS3lrBS4SNZ%252f%252bcPMdvOF1cnCfjUjqFDpqhKhrZ%252b0YAOYjIuseA9so7bcjVkq6pUEGM6VQruY6pQBcQv8rPml%252fY%252fl2w8UoZxgOSWVv8elLGqiqu6m3FafnmlABiWcSskGsdFIKy9A6d2Sk%252bH6k8dxShh%252baj3gLNqdFb7wK1y6kBaQfgxkxB8nj907UC2uVg9QXK1bOhvChw7lagVSAL6JuD08I7e%252f%252fM4nEs2T3s%252bYLbXEtOHBi0cr%252bkt0F01DGbgerX6s%253d; s_fid=24CF82E5EA2F4706-06A7A1D06023D0F1; gpv_pn=www.linkedin.com%2Fcompany%2Fid-redacted%2Fadmin%2Fanalytics%2Fvisitors%2F; s_plt=5.45; s_pltp=www.linkedin.com%2Fcompany%2Fid-redacted%2Fadmin%2Fanalytics%2Fvisitors%2F; s_cc=true; s_ips=617; lidc="b=OB62:s=O:r=O:a=O:p=O:g=5997:u=950:x=1:i=1724620944:t=1724626094:v=2:sig=AQGQszbeeDtT2PgVdgCwz0EckBlSNzSV"; s_tslv=1724623124844; s_sq=lnkdprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dwww.linkedin.com%25252Fcompany%25252Fid-redacted%25252Fadmin%25252Fanalytics%25252Fvisitors%25252F%2526link%253DMember%2525E2%252580%252599s%252520name%252520Sai%252520Shandilia%252520S%252520S%252520K%252520Sai%252520Shandilia%252520S%252520S%252520K%252520Member%2525E2%252580%252599s%252520occupation%252520Product%252520%252540%252520OkCredit%252520%25257C%252520Ex-Zilingo%252520%25257C%252520IIT%252520Madras%2526region%253Dember6166%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dwww.linkedin.com%25252Fcompany%25252Fid-redacted%25252Fadmin%25252Fanalytics%25252Fvisitors%25252F%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.linkedin.com%25252Fin%25252Fssk-sai-shandilia%2526ot%253DA; s_tp=8426; s_ppv=www.linkedin.com%2Fcompany%2Fid-redacted%2Fadmin%2Fanalytics%2Fvisitors%2F%2C94%2C7%2C7951%2C4%2C13',
    "csrf-token": "ajax:7375956543741358092",
    "priority": "u=1, i",
    "referer": "https://www.linkedin.com/search/results/people/?keywords=cto&network=%5B%22O%22%5D&origin=FACETED_SEARCH&sid=Z.S",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "x-li-lang": "en_US",
    "x-li-page-instance": "urn:li:page:d_flagship3_profile_view_base;1D7cl1sBQ2mlYO+SG0haqg==",
    "x-li-pem-metadata": "Voyager - Profile=profile-top-card-supplementary",
    "x-li-track": '{"clientVersion":"1.13.22093","mpVersion":"1.13.22093","osName":"web","timezoneOffset":5.5,"timezone":"Asia/Calcutta","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1366,"displayHeight":768}',
    "x-restli-protocol-version": "2.0.0",
}
