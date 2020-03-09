# cagrUFSC2calendar

cagrUFSC2calendar é uma ferramenta para converter a grade de horários da UFSC, disponível no CAGR, em formato de iCalendar. Com isso, é possível importar o arquivo para algum aplicativo de calendário de seu interesse (ex: Google Agenda).

Por enquanto, o programa espera que você tenha baixado o HTML da página da sua grade de horários, disponível em https://cagr.sistemas.ufsc.br/modules/aluno/grade/ (para alunos da graduação da UFSC). Se você não sabe como fazê-lo, basta acessar a página > botão direito > salvar página como > escolher um nome e selecionar formato HTML. 

O formato iCalendar suporta repetições. Atualmente, como padrão, a quantidade de eventos que serão repetidos será a quantidade de semanas que faltam para o semestre da graduação da UFSC (2020.1, no momento) acabar. Entretanto, você pode definir a quantidade exata de repetições desejada ou a data final para contabilização. Exemplo disponível logo abaixo.

## Guia de utilização:

### Instalação
Recomenda-se a utilização do <b>poetry</b> para lidar com o pacote e as dependências. Após clonar o repositório e entrar em sua respectiva pasta, basta realizar:
```console
$ poetry install
```

### Uso
```console
$ poetry shell
```

### Comandos disponíveis
```console
$ python cagrufsc2calendar --help
cagrUFSC2calendar transforma sua grade de horarios em um formato para calendario (.ics)
            Por padrão, as repetições dos eventos das matérias estão ligadas à data do fim do semestre
            da graduação na UFSC. Entretanto, você pode definir um numero personalizado de repetições
            com --repeat NUM ou uma data de fim --end Y-m-d

positional arguments:
  file             grade de horarios em HTML
  output           nome do arquivo de saida

optional arguments:
  -h, --help       show this help message and exit
  --repeat REPEAT  quantidade de repetições dos eventos
  --end END        data final para computar repetições
```

### Exemplo 1
```console
$ python cagrufsc2calendar meu_horario.html meu_calendario
```
### Exemplo 2: repetições (3 semanas)
```console
$ python cagrufsc2calendar meu_horario.html meu_calendario --repeat 3
```
### Exemplo 3: data final personalizada
```console
$ python cagrufsc2calendar meu_horario.html meu_calendario --end 2020-6-6
```

## Importar arquivo para Google Agenda
https://support.google.com/calendar/answer/37118?hl=pt-BR
