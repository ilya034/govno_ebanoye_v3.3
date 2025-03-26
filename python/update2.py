import urllib.request as urllib
import pymupdf

import os
from os import path

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Cookie': '__ddg1_=EKc899XJwoULGPq3PAqO',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'DNT': '1',
        'Priority': 'u=0, i',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers'
}

PDF_URL = "https://docs.cspu.ru/raspisanie-zanyatiy/och/fizmat(Inf)/Raspisanie/1k.pdf"
PDF_FILENAME = "full_schedule.pdf"
IMG_FULLPATH = path.join(os.getcwd(), "img", "schedule.png")

r = urllib.Request(PDF_URL, headers=HEADERS)

for pair in HEADERS.items():
    r.add_header(pair[0], pair[1])

r = urllib.urlopen(r).read()

with open(PDF_FILENAME, "wb") as f:
    f.write(r)
    print("pdf saved")

schedule_pdf = pymupdf.open(PDF_FILENAME)
out_image = schedule_pdf[1].get_pixmap()
out_image.save(IMG_FULLPATH)

print("image saved")
