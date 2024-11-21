
# Como instalar no Windows

## Instalar uv
Caso ainda não tenha instalado uv abra o powershell e execute o comando abaixo para instalar

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Instalar git
Caso ainda não tenha instalado git utilize o comando abaixo no powershell para instalar

```powershell
winget install git
```

## Clonar o projeto

```powershell
git clone https://github.com/renatormc/whatsapp_report
```

# Como utilizar

Após exportar uma conversa do WhatsaApp você pode utilizar o comando abaixo para gerar um arquivo html dentro da pasta da conversa.
Suponha que o whatsapp exportou a conversa para uma pasta de nome "C:\temp\Conversa do WhatsApp com Fulano".

```powershell
whatsapp_report.ps1 render "C:\temp\Conversa do WhatsApp com Fulano"
```

Será gerado um arquivo html com o mesmo nome do arquivo txt na mesma pasta.