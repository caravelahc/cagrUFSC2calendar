import os
import argparse
import json
from extractor import extract
from builder import build

def run():
    text = "cagrUFSC2calendar transforma sua grade de horarios em um formato para calendario (.ics)\n\
            Por padrão, as repetições dos eventos das matérias estão ligadas à data do fim do semestre\n\
            da graduação na UFSC. Entretanto, você pode definir um numero personalizado de repetições\n\
            com --repeat NUM ou uma data de fim --end Y-m-d"

    parser = argparse.ArgumentParser(description=text, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("file", help="grade de horarios em HTML")
    parser.add_argument("output", help="nome do arquivo de saida")
    parser.add_argument("--repeat", help="quantidade de repetições dos eventos")
    parser.add_argument("--end", help="data final para computar repetições")
    parser.add_argument("--json", help="especifica formato de arquivo como .json", action="store_true")
    args = parser.parse_args()

    FILE = args.file
    OUTPUT = args.output
    REPEAT = args.repeat
    END_DATE = args.end
    FILE_JSON = args.json

    if not END_DATE:
        END_DATE = "2020-7-14"

    print("Starting to extract information from", FILE, "...")
    if not FILE_JSON:
        daily_events = extract(FILE)
    else:
        with open(FILE, 'r') as file:
            daily_events = json.load(file)

    print("Building calendar...")
    build(OUTPUT, END_DATE, REPEAT, daily_events)

if __name__ == "__main__":
  run()
