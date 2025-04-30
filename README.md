# coleta_cebrap
Repositório para armazenar notebooks de coleta, tratamento e construção de indicadores

## Index
Tema|Notebook|Parquet|Excel - Google|Documentação|
|:-:|:-:|:-:|:-:|:-:|
|Todos Indicadores|X|X|[:link:][todos-indicadores-excel-google]|X|
|Dimensões SP|[:link:][dimensoes_sp-notebook]|X|[:link:][dimensoes_sp-excel]|[:link:][dimensoes_sp-doc]|
|Censo|[:link:][Censo-notebook]|[:link:][Censo-parquet]|[:link:][Censo-Excel-Google]|X|
|Inep|[:link:][Inep-notebook]|[:link:][Inep-parquet]|X|X|
|Indicadores Educação|[:link:][Indicadores-Educação-notebook]|X|[:link:][Indicadores-Educação-Excel-Google]|X|
|Indicadores Rais|[:link:][Indicadores-Rais-notebook]|X|[:link:][Indicadores-Rais-Excel-Google]|X|
|Indicadores Mortalidade|[:link:][indicadores-mortalidade-notebook]|X|[:link:][indicadores-mortalidade-excel-google]|X|
|Arborização Viária|[:link:][arborizacao-viaria-notebook]|[:link:][arborizacao-viaria-parquet]|[:link:][arborizacao-viaria-excel]|X|
|Distritos|[:link:][distritos-notebook]|[:link:][distritos-parquet]|[:link:][distritos-excel]|X|
|Distritos com quantidade de Árvores no Viário|[:link:][distritos-qtdd-arv-notebook]|[:link:][distritos-qtdd-arv-parquet]|[:link:][distritos-qtdd-arv-excel]|X|
|Árvores no Viário per capita|[:link:][arvores-per-capita-notebook]|[:link:][arvores-per-capita-parquet]|[:link:][arvores-per-capita-excel]|X|
|Árvores no Viário por Km²|[:link:][arvores-km-2-notebook]|[:link:][arvores-km-2-parquet]|[:link:][arvores-km-2-excel]|X|
|Cobertura Vegetal 2020|[:link:][cobertura-vegetal-notebook]|[:link:][cobertura-vegetal-parquet]|[:link:][cobertura-vegetal-excel]|X|
|Porcentagem de Cobertura Vegetal|[:link:][pct-cobertura-vegetal-notebook]|[:link:][pct-cobertura-vegetal-parquet]|[:link:][pct-cobertura-vegetal-excel]|X|
|Cobertura Vegetal per capita|[:link:][cobertura-vegetal-pcapita-notebook]|[:link:][cobertura-vegetal-pcapita-parquet]|[:link:][cobertura-vegetal-pcapita-excel]|X|

[Censo-notebook]: notebooks/colab/[cebrap]ibge_censo_setor_censitario.ipynb
[Censo-parquet]: https://drive.google.com/file/d/1WNv6iCmwaJzcXZvR2eHJSUcJvLUgnB1p/view?usp=sharing
[Censo-Excel-Google]: https://docs.google.com/spreadsheets/d/1DmwjVZN6-JCkBcyCk9vjl8IHpKY3sJ4Q/edit?usp=sharing&ouid=115854210799010302684&rtpof=true&sd=true

[dimensoes_sp-notebook]: notebooks/colab/Pol%C3%ADticas%20Sociais/%5Bcebrap%5Dpoliticas_sociais.ipynb
[dimensoes_sp-excel]: https://docs.google.com/spreadsheets/d/1c9SFkieO3DxosE4dspzBH3siB6c-j2UP/edit?gid=149366672#gid=149366672
[dimensoes_sp-doc]: docs/dimensoes_sp.md

[Inep-notebook]: notebooks/colab/[cebrap]coleta_dados_educacao.ipynb
[Inep-parquet]: https://drive.google.com/file/d/1VCEejCcjFTEWfzPnCN4RWltAVZ3sZXxd/view?usp=sharing

[Indicadores-Educação-notebook]: notebooks/colab/[cebrap]indicadores_educacao.ipynb
[Indicadores-Educação-Excel-Google]: https://docs.google.com/spreadsheets/d/1QhZWl12L0Zu5zb5YQt6hscLNxvo2DWwx/edit?usp=sharing&ouid=115854210799010302684&rtpof=true&sd=true

[Indicadores-Rais-notebook]: notebooks/colab/[cebrap]indicadores_rais.ipynb
[Indicadores-Rais-Excel-Google]: https://docs.google.com/spreadsheets/d/12-92rKnLDn2XzJ3ESS-qJGu_ijRveM3L/edit?gid=1044977796#gid=1044977796

[indicadores-mortalidade-notebook]: notebooks/colab/[cebrap]indicadores_mortalidade.ipynb
[indicadores-mortalidade-excel-google]: https://docs.google.com/spreadsheets/d/1wDRZC8e1xuYIk99AHdjL5LkIFevf_6HU/edit?usp=sharing&ouid=115854210799010302684&rtpof=true&sd=true

[todos-indicadores-excel-google]: https://docs.google.com/spreadsheets/d/130ygeu4QAfmYdpcrA5C7I4BTrzUEJIM8/edit?usp=drive_web&ouid=115854210799010302684&rtpof=true

[arborizacao-viaria-notebook]: notebooks/jupyter/arborizacao_viaria/carregar_dados/malha_arborizacao_viaria.ipynb
[arborizacao-viaria-parquet]: https://drive.google.com/file/d/1yVm9x89TgSTJv6iaaHuG92VVMC-QpGCp/view?usp=drive_link
[arborizacao-viaria-excel]: https://docs.google.com/spreadsheets/d/1JFG6UZ21n286V6e6O2eISYnnfbnk7SB8/edit?usp=drive_link&ouid=104569777283565556490&rtpof=true&sd=true

[distritos-notebook]: notebooks/jupyter/arborizacao_viaria/carregar_dados/malha_distritos.ipynb
[distritos-parquet]: https://drive.google.com/file/d/1pofZK47J5I80Ipv4HByFlUC1fsCm9PE5/view?usp=drive_link
[distritos-excel]: https://docs.google.com/spreadsheets/d/1MZ38WV7JoVY1XawRmXvzz8eeghPW65TY/edit?usp=drive_link&ouid=104569777283565556490&rtpof=true&sd=trues

[distritos-qtdd-arv-notebook]: notebooks/jupyter/arborizacao_viaria/tratamento_dados/[prefeitura]arborizacao_viaria_qtd.ipynb
[distritos-qtdd-arv-parquet]: https://drive.google.com/file/d/1L6xnz-wBuo-mhTbtFcm4PxkfAZwldtkz/view?usp=drive_link
[distritos-qtdd-arv-excel]: https://docs.google.com/spreadsheets/d/1GfPqYOX_vOqR1yvJj5VQElmeX6-jBvLO/edit?usp=drive_link&ouid=104569777283565556490&rtpof=true&sd=true

[arvores-per-capita-notebook]: notebooks/jupyter/arborizacao_viaria/tratamento_dados/[prefeitura]arborizacao_viaria_per_capita.ipynb
[arvores-per-capita-parquet]: https://drive.google.com/file/d/1x8orGry56RBNNDXa10KYSB6ZdoKMdPUO/view?usp=drive_link
[arvores-per-capita-excel]: https://docs.google.com/spreadsheets/d/1EZft0Dkt4h5tyrpIMww70oux-PZY29nG/edit?usp=drive_link&ouid=104569777283565556490&rtpof=true&sd=true

[arvores-km-2-notebook]: notebooks/jupyter/arborizacao_viaria/tratamento_dados/[prefeitura]arborizacao_viaria_km_2.ipynb
[arvores-km-2-parquet]: https://drive.google.com/file/d/15muVH24CP03qk3y60ctnd6NX7gkPeZya/view?usp=drive_link
[arvores-km-2-excel]: https://docs.google.com/spreadsheets/d/1jNweHIS7YvwtNN98Y1Zj4twWJxYyI99Q/edit?usp=drive_link&ouid=104569777283565556490&rtpof=true&sd=true

 
[cobertura-vegetal-notebook]: notebooks/jupyter/cobertura_vegetal/download_data/malha_cobertura_vegetal.ipynb
[cobertura-vegetal-parquet]: https://drive.google.com/file/d/11h0X3DGcLN1_dy-HLl1boXynvUt29obx/view?usp=drive_link
[cobertura-vegetal-excel]: https://docs.google.com/spreadsheets/d/1ysS6IgFyk-HturNcIYkAzv-Y-984kVzk/edit?usp=drive_link&ouid=104569777283565556490&rtpof=true&sd=true

[pct-cobertura-vegetal-notebook]: notebooks/jupyter/cobertura_vegetal/treat_data/[cebrap]cobertura_vegetal_por_distrito.ipynb
[pct-cobertura-vegetal-parquet]: https://drive.google.com/file/d/11PQ_Ah6Rlu0AL3RMGomcWim-Dt81bg9I/view?usp=drive_link
[pct-cobertura-vegetal-excel]: https://docs.google.com/spreadsheets/d/16d2gSjdFUXJF6eXJvGI629bkiBfPKuDm/edit?usp=drive_link&ouid=104569777283565556490&rtpof=true&sd=true

[cobertura-vegetal-pcapita-notebook]: notebooks/jupyter/cobertura_vegetal/treat_data/[cebrap]cobertura_vegetal_per_capita.ipynb
[cobertura-vegetal-pcapita-parquet]: https://drive.google.com/file/d/1D8pel4LfYwACuTKXNZNAUfcxr87ruXOi/view?usp=drive_link
[cobertura-vegetal-pcapita-excel]: https://docs.google.com/spreadsheets/d/1N3iPIzF6w2BxaEF9AfyTym-7fdhl1GTb/edit?usp=drive_link&ouid=104569777283565556490&rtpof=true&sd=true

[intersec-cobertura-vegetal-notebook]: notebooks/jupyter/cobertura_vegetal/treat_data/overlay_distrito_cobertura_vegetal.ipynb

# 
> [Indicadores Educação][Inep-notebook] precisa de arquivos resultados de [Censo][Censo-notebook] e [Inep][Inep-notebook] para conseguir funcionar com exito.
> 
> [Distritos com quantidade de Árvores no Viário][distritos-qtdd-arv-notebook] precisa de arquivos resultados de [Arborização Viária][arborizacao-viaria-notebook] e [Distritos][distritos-notebook] para funcionar.
> 
> [Árvores no Viário per capita][arvores-per-capita-notebook] e [Árvores no Viário por Km²][arvores-km-2-notebook] precisam do arquivo resultado de [Distritos com quantidade de Árvores no Viário][distritos-qtdd-arv-notebook] para funcionar.
> 
> [Porcentagem de Cobertura Vegetal][pct-cobertura-vegetal-notebook] precisa dos arquivos resultados de [Cobertura Vegetal interseccionada por Distrito][intersec-cobertura-vegetal-notebook] e [Distritos][distritos-notebook] para funcionar.
> 
> [Cobertura Vegetal per capita][cobertura-vegetal-pcapita-notebook] precisa do arquivo resultado de [Porcentagem de Cobertura Vegetal][pct-cobertura-vegetal-notebook] 
