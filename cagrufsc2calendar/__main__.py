import os
import argparse
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
    args = parser.parse_args()

    FILE = args.file
    OUTPUT = args.output
    REPEAT = args.repeat
    END_DATE = args.end

    if not END_DATE:
        END_DATE = "2020-7-14"

    print("Starting to extract information from", FILE, "...")
    daily_events, day2abrev, day2key, code2name = extract(FILE)
    print("Building calendar...")
    build(OUTPUT, END_DATE, REPEAT, daily_events, day2abrev, day2key, code2name)


if __name__ == "__main__":
  run()
