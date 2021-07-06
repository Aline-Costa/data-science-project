import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('Vendas.csv', encoding = 'ISO-8859-1', decimal=',',engine='python', sep=';')
dados['Mes'] = dados['Data Venda'].apply(lambda x: str(x)[3:5])
dados['Ano'] = dados['Data Venda'].apply(lambda x: str(x)[6:10])

st.set_option('deprecation.showPyplotGlobalUse', False)

def vendas_ano():
    Vendas_Ano = pd.DataFrame(dados.groupby('Ano',as_index=False).ValorVenda.sum())
    st.pyplot(sns.catplot(x="Ano", y="ValorVenda", kind="bar", data=Vendas_Ano).set(title='Total de Vendas por Ano'))


def vendas_categoria():
    Vendas_Categoria = pd.DataFrame(dados.groupby('Categoria',as_index=False).ValorVenda.sum())
    st.pyplot(sns.catplot(x='Categoria', y='ValorVenda', kind="bar", data=Vendas_Categoria).set(title='Total de Vendas por Categoria'))


def vendas_cat_ano():
    vendas_cat_ano= pd.DataFrame(dados.groupby(['Categoria','Ano'],as_index=False).ValorVenda.sum())
    st.pyplot(sns.catplot(x='Categoria', y="ValorVenda", hue="Ano", kind="bar", data=vendas_cat_ano).set(title='Total de vendas de Categoria por Ano'))


def vendas_ano_cat():
    vendas_cat_ano= pd.DataFrame(dados.groupby(['Categoria','Ano'],as_index=False).ValorVenda.sum())
    st.pyplot(sns.catplot(x="Ano", y="ValorVenda", hue="Categoria", kind="bar", data=vendas_cat_ano).set(title='Total de vendas do Ano por Categoria'))


def vendas_cat_mes_ano():
    vendas = pd.DataFrame(dados.groupby(['Categoria','Ano','Mes'], as_index=False).ValorVenda.sum())
    st.pyplot(sns.catplot(data=vendas, x="Categoria", y="ValorVenda", hue="Mes", col="Ano",kind='bar',col_wrap=3,palette="bright",dodge=False))


def vendas_prods_fab(fab_escolhido):

    prod_fabricante = pd.DataFrame(dados.groupby(['Fabricante','Produto']).ValorVenda.count())
    prod_fabricante = prod_fabricante.sort_values(by='ValorVenda')

    lista_prod = []
    lista_fab = []

    for i in range(len(prod_fabricante)):
        lista_fab.append(prod_fabricante['ValorVenda'].index[i][0])
        lista_prod.append(prod_fabricante['ValorVenda'].index[i][1])
        
    prod_fabricante['Produto'] = lista_prod
    prod_fabricante['Fabricante'] = lista_fab
    prod_fabricante = prod_fabricante.reset_index(drop=True)

    fabricantes = prod_fabricante.loc[:,['Fabricante']]
    fabricantes = fabricantes.drop_duplicates()

    v_fab = []

    def vendas_prod_fab(fabricante):
        
        lista_vendas = []
        lista_prods = []

        for i in range(len(prod_fabricante)):
            if prod_fabricante['Fabricante'][i] == fabricante:
                lista_vendas.append(prod_fabricante['ValorVenda'][i])
                lista_prods.append(prod_fabricante['Produto'][i])

        return lista_vendas,lista_prods


    for i in range(len(fabricantes)): 
        v_fab.append(vendas_prod_fab(fabricantes.iloc[i,0]))

    
    if fab_escolhido == 'LG':
        plt.barh(v_fab[0][1], v_fab[0][0], color='black')
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela LG')
        st.pyplot(plt.show())

    if fab_escolhido == 'Electrolux':
        plt.barh(v_fab[1][1], v_fab[1][0])
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela Electrolux')
        st.pyplot(plt.show())

    if fab_escolhido == 'Sony':
        plt.barh(v_fab[2][1], v_fab[2][0], color='red')
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela Sony')
        st.pyplot(plt.show())

    if fab_escolhido == 'Panasonic':
        plt.barh(v_fab[3][1], v_fab[3][0], color='purple')
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela Panasonic')
        st.pyplot(plt.show())

    if fab_escolhido == 'Cônsul':
        plt.barh(v_fab[4][1], v_fab[4][0], color='green')
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela Consul')
        st.pyplot(plt.show())

    if fab_escolhido == 'Arno':
        plt.barh(v_fab[5][1], v_fab[5][0], color='yellow')
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela Arno')
        st.pyplot(plt.show())

    if fab_escolhido == 'Dell':
        plt.barh(v_fab[6][1], v_fab[6][0], color='gray')
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela Dell')
        st.pyplot(plt.show())

    if fab_escolhido == 'Brastemp':
        plt.barh(v_fab[7][1], v_fab[7][0], color='black')
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela Brastemp')
        st.pyplot(plt.show())

    if fab_escolhido == 'Philco':
        plt.barh(v_fab[8][1], v_fab[8][0])
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela Philco')
        st.pyplot(plt.show())

    if fab_escolhido == 'Samsung':
        plt.barh(v_fab[9][1], v_fab[9][0], color='red')
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela Samsung')
        st.pyplot(plt.show())

    if fab_escolhido == 'HP':
        plt.barh(v_fab[10][1], v_fab[10][0], color='purple')
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela HP')
        st.pyplot(plt.show())

    if fab_escolhido == 'Epson':
        plt.barh(v_fab[11][1], v_fab[11][0], color='green')
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela Epson')
        st.pyplot(plt.show())

    if fab_escolhido == 'Motorola':   
        plt.barh(v_fab[12][1], v_fab[12][0], color='yellow')
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela Motorola')
        st.pyplot(plt.show())
    
    if fab_escolhido == 'Britânia':
        plt.barh(v_fab[13][1], v_fab[13][0],color='gray')
        plt.ylabel('Produtos')
        plt.xlabel('Quantidade de Vendas')
        plt.title('Produtos mais vendidos pela Britânia')
        st.pyplot(plt.show())


def vendas_lojas_cat():
    vendas_loja_cat= pd.DataFrame(dados.groupby(['Categoria','Loja'],as_index=False).ValorVenda.sum())
    st.pyplot(sns.catplot(x="Loja", y="ValorVenda", hue="Categoria", kind="bar", data=vendas_loja_cat).set(title='Total de vendas das lojas por Categoria'))


def vendas_prod_maior():
    vendas_produto = pd.DataFrame(dados.groupby(['Produto']).ValorVenda.sum())
    vendas_produto = vendas_produto.sort_values(by='ValorVenda')

    plt.barh(vendas_produto.index, vendas_produto['ValorVenda'])
    plt.ylabel('Produtos')
    plt.xlabel('Valor de Vendas')
    plt.title('Ranking de Produtos com Maiores Vendas')
    st.pyplot(plt.show())


def vendas_prod_maior_lj(loja_escolhida):

    vendas_prod_lj = pd.DataFrame(dados.groupby(['Loja','Produto']).ValorVenda.sum())
    vendas_prod_lj = vendas_prod_lj.sort_values(by='ValorVenda', ascending=True)

    lista_prod = []
    lista_lj = []

    for i in range(len(vendas_prod_lj)):
        lista_lj.append(vendas_prod_lj['ValorVenda'].index[i][0])
        lista_prod.append(vendas_prod_lj['ValorVenda'].index[i][1])
        
    vendas_prod_lj['Produto'] = lista_prod
    vendas_prod_lj['Loja'] = lista_lj
    vendas_prod_lj = vendas_prod_lj.reset_index(drop=True)

    lojas = vendas_prod_lj.loc[:,['Loja']]
    lojas = lojas.drop_duplicates()

    v_p =[]

    def vendas_prod_lojas(loja):
        
        lista_vendas = []
        lista_prods = []

        for i in range(len(vendas_prod_lj)):
            if vendas_prod_lj['Loja'][i] == loja:
                lista_vendas.append(vendas_prod_lj['ValorVenda'][i])
                lista_prods.append(vendas_prod_lj['Produto'][i])

        return lista_vendas,lista_prods

    for i in range(len(lojas)): 
        v_p.append(vendas_prod_lojas(lojas.iloc[i,0]))


    if loja_escolhida == 'RG7742':
        plt.barh(v_p[0][1], v_p[0][0], color='black')
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Maiores Vendas na Loja RG7742')
        st.pyplot(plt.show())
   
    if loja_escolhida == 'JP8825':
        plt.barh(v_p[1][1], v_p[1][0])
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Maiores Vendas na Loja JP8825')
        st.pyplot(plt.show())
    
    if loja_escolhida == 'R1296':
        plt.barh(v_p[2][1], v_p[2][0], color='red')
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Maiores Vendas na Loja R1296')
        st.pyplot(plt.show())

    if loja_escolhida == 'BA7783':
        plt.barh(v_p[3][1], v_p[3][0], color='purple')
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Maiores Vendas na Loja BA7783')
        st.pyplot(plt.show())

    if loja_escolhida == 'GA7751':
        plt.barh(v_p[4][1], v_p[4][0], color='green')
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Maiores Vendas na Loja GA7751')
        st.pyplot(plt.show())

    if loja_escolhida == 'JB6325':
        plt.barh(v_p[5][1], v_p[5][0], color='yellow')
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Maiores Vendas na Loja JB6325')
        st.pyplot(plt.show())

    if loja_escolhida == 'AL1312':
        plt.barh(v_p[6][1], v_p[6][0], color='gray')
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Maiores Vendas na Loja AL1312')
        st.pyplot(plt.show())


def vendas_prod_menor():
    vendas_produto = pd.DataFrame(dados.groupby(['Produto']).ValorVenda.sum())
    vendas_produto = vendas_produto.sort_values(by='ValorVenda', ascending=False)

    plt.barh(vendas_produto.index, vendas_produto['ValorVenda'])
    plt.ylabel('Produtos')
    plt.xlabel('Valor de Vendas')
    plt.title('Ranking de Produtos com Menores Vendas')
    st.pyplot(plt.show())


def vendas_prod_menor_lj(loja_escolhida):

    vendas_prod_lj = pd.DataFrame(dados.groupby(['Loja','Produto']).ValorVenda.sum())
    vendas_prod_lj = vendas_prod_lj.sort_values(by='ValorVenda', ascending=False)

    lista_prod = []
    lista_lj = []

    for i in range(len(vendas_prod_lj)):
        lista_lj.append(vendas_prod_lj['ValorVenda'].index[i][0])
        lista_prod.append(vendas_prod_lj['ValorVenda'].index[i][1])
        
    vendas_prod_lj['Produto'] = lista_prod
    vendas_prod_lj['Loja'] = lista_lj
    vendas_prod_lj = vendas_prod_lj.reset_index(drop=True)

    lojas = vendas_prod_lj.loc[:,['Loja']]
    lojas = lojas.drop_duplicates()

    v_p =[]

    def vendas_prod_lojas(loja):
        
        lista_vendas = []
        lista_prods = []

        for i in range(len(vendas_prod_lj)):
            if vendas_prod_lj['Loja'][i] == loja:
                lista_vendas.append(vendas_prod_lj['ValorVenda'][i])
                lista_prods.append(vendas_prod_lj['Produto'][i])

        return lista_vendas,lista_prods

    for i in range(len(lojas)): 
        v_p.append(vendas_prod_lojas(lojas.iloc[i,0]))

    if loja_escolhida == 'R1296':
        plt.barh(v_p[0][1], v_p[0][0], color='black')
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Menores Vendas na Loja R1296')
        st.pyplot(plt.show())

    if loja_escolhida == 'JP8825':
        plt.barh(v_p[1][1], v_p[1][0])
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Menores Vendas na Loja JP8825')
        st.pyplot(plt.show())

    if loja_escolhida == 'AL1312':
        plt.barh(v_p[2][1], v_p[2][0], color='red')
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Menores Vendas na Loja AL1312')
        st.pyplot(plt.show())

    if loja_escolhida == 'GA7751':
        plt.barh(v_p[3][1], v_p[3][0], color='purple')
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Menores Vendas na Loja GA7751')
        st.pyplot(plt.show())

    if loja_escolhida == 'RG7742':
        plt.barh(v_p[4][1], v_p[4][0], color='green')
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Menores Vendas na Loja RG7742')
        st.pyplot(plt.show())
    if loja_escolhida == 'BA7783':
        plt.barh(v_p[5][1], v_p[5][0], color='yellow')
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Menores Vendas na Loja BA7783')
        st.pyplot(plt.show())
    if loja_escolhida == 'JB6325':
        plt.barh(v_p[6][1], v_p[6][0], color='gray')
        plt.ylabel('Produtos')
        plt.xlabel('Valor de Vendas')
        plt.title('Ranking de Produtos com Menores Vendas na Loja JB6325')
        st.pyplot(plt.show())                                                                                                                                              

    

def prods_rentaveis():
    dados['Lucro'] = dados['ValorVenda'] - dados['preço Custo']
    lucro_produtos = pd.DataFrame(dados.groupby(['Produto']).Lucro.sum())
    lucro_produtos = lucro_produtos.sort_values(by='Lucro')

    plt.barh(lucro_produtos.index, lucro_produtos['Lucro'],color='black')
    plt.ylabel('Produtos')
    plt.xlabel('Lucro')
    plt.title('Ranking dos produtos mais rentáveis')
    st.pyplot(plt.show())


def prods_rentaveis_lojas(loja_escolhida):

    dados['Lucro'] = dados['ValorVenda'] - dados['preço Custo']
    lucro_prod_lj = pd.DataFrame(dados.groupby(['Loja','Produto']).Lucro.sum())
    lucro_prod_lj = lucro_prod_lj.sort_values(by='Lucro')

    lista_prod = []
    lista_lj = []

    for i in range(len(lucro_prod_lj)):
        lista_lj.append(lucro_prod_lj['Lucro'].index[i][0])
        lista_prod.append(lucro_prod_lj['Lucro'].index[i][1])
        
    lucro_prod_lj['Produto'] = lista_prod
    lucro_prod_lj['Loja'] = lista_lj
    lucro_prod_lj = lucro_prod_lj.reset_index(drop=True)

    lojas = lucro_prod_lj.loc[:,['Loja']]
    lojas = lojas.drop_duplicates()

    l_p= []

    def lucro_prod_lojas(loja):
        
        lista_lucros = []
        lista_prods = []

        for i in range(len(lucro_prod_lj)):
            if lucro_prod_lj['Loja'][i] == loja:
                lista_lucros.append(lucro_prod_lj['Lucro'][i])
                lista_prods.append(lucro_prod_lj['Produto'][i])

        return lista_lucros,lista_prods

    for i in range(len(lojas)): 
        l_p.append(lucro_prod_lojas(lojas.iloc[i,0]))

    if loja_escolhida == 'RG7742':
        plt.barh(l_p[0][1], l_p[0][0], color='black')
        plt.ylabel('Produtos')
        plt.xlabel('Lucro')
        plt.title('Ranking de Produtos mais rentáveis na Loja RG7742')
        st.pyplot(plt.show())

    if loja_escolhida == 'JP8825':
        plt.barh(l_p[1][1], l_p[1][0])
        plt.ylabel('Produtos')
        plt.xlabel('Lucro')
        plt.title('Ranking de Produtos mais rentáveis na Loja JP8825')
        st.pyplot(plt.show())

    if loja_escolhida == 'R1296':
        plt.barh(l_p[2][1], l_p[2][0], color='red')
        plt.ylabel('Produtos')
        plt.xlabel('Lucro')
        plt.title('Ranking de Produtos mais rentáveis na Loja R1296')
        st.pyplot(plt.show())

    if loja_escolhida == 'BA7783':
        plt.barh(l_p[3][1], l_p[3][0], color='purple')
        plt.ylabel('Produtos')
        plt.xlabel('Lucro')
        plt.title('Ranking de Produtos mais rentáveis na Loja BA7783')
        st.pyplot(plt.show())

    if loja_escolhida == 'GA7751':
        plt.barh(l_p[4][1], l_p[4][0], color='green')
        plt.ylabel('Produtos')
        plt.xlabel('Lucro')
        plt.title('Ranking de Produtos mais rentáveis na Loja GA7751')
        st.pyplot(plt.show())

    if loja_escolhida == 'JB6325':
        plt.barh(l_p[5][1], l_p[5][0], color='yellow')
        plt.ylabel('Produtos')
        plt.xlabel('Lucro')
        plt.title('Ranking de Produtos mais rentáveis na Loja JB6325')
        st.pyplot(plt.show())

    if loja_escolhida == 'AL1312':
        plt.barh(l_p[6][1], l_p[6][0], color='gray')
        plt.ylabel('Produtos')
        plt.xlabel('Lucro')
        plt.title('Ranking de Produtos mais rentáveis na Loja AL1312')
        st.pyplot(plt.show())  


def vendas_lojas():
    vendas_lojas = pd.DataFrame(dados.groupby(['Loja']).ValorVenda.sum())
    vendas_lojas = vendas_lojas.sort_values(by='ValorVenda')

    plt.barh(vendas_lojas.index, vendas_lojas['ValorVenda'],color='red')
    plt.ylabel('Lojas')
    plt.xlabel('Valor de Vendas')
    plt.title('Ranking de Vendas por Loja')
    st.pyplot(plt.show())


def vendas_vendedor():
    melhores_vendedores = pd.DataFrame(dados.groupby(['Loja','Vendedor','Ano'], as_index=False).ValorVenda.sum())
    st.pyplot(sns.catplot(data=melhores_vendedores, x="Ano", y="ValorVenda", hue="Vendedor", col="Loja",kind='bar',col_wrap=2,palette="bright",dodge=False))

st.title("Análise das vendas da redeX")
st.write("Bem-vindo ao sistema de relatórios gerenciais para apoio a tomada de decisão da empresa redeX.")


st.sidebar.title("Relatórios")
st.sidebar.write("Selecione os gráficos que deseja visualizar")
b1 = st.sidebar.button("Vendas por Ano", key="1")
b2 = st.sidebar.button("Vendas por Categoria", key="2")
b3 = st.sidebar.button("Vendas por Categoria e por Ano", key="3")
b4 = st.sidebar.button("Vendas por Ano e Categoria", key="4")
b5 = st.sidebar.button("Vendas por categoria pelos meses para cada ano", key="5")
b6 = st.sidebar.button("Vendas das lojas por Categoria", key="6")
b7 = st.sidebar.button("Produtos com maiores vendas", key="7")
b8 = st.sidebar.button("Produtos com menores vendas", key="8")
b9 = st.sidebar.button("Produtos mais Rentáveis", key="9")
b10 = st.sidebar.button("Ranking de Vendas por loja", key="10")
b11 = st.sidebar.button("Ranking dos vendedores por loja e ano", key="11")
st.sidebar.write("Produtos mais vendidos por Fabricante")
fab_escolhido = st.sidebar.selectbox("Selecione o Fabricante.", ['','Cônsul','Brastemp', 'Panasonic', 'Arno', 'HP','Samsung','Electrolux','Britânia', 'Motorola', 'Epson','Philco','Dell','Sony','LG'])
st.sidebar.write("Produtos com maiores vendas por loja")
lj_escolhida = st.sidebar.selectbox("Selecione uma loja.", ['','JP8825', 'R1296', 'BA7783', 'GA7751', 'JB6325', 'AL1312'])
st.sidebar.write("Produtos com menores vendas por loja")
loja_escolhida = st.sidebar.selectbox("Selecione a loja.", ['','JP8825', 'R1296', 'BA7783', 'GA7751', 'JB6325', 'AL1312'])
st.sidebar.write("Produtos mais rentáveis por loja")
loja_esc = st.sidebar.selectbox("Selecione a loja", ['','JP8825', 'R1296', 'BA7783', 'GA7751', 'JB6325', 'AL1312'])


if b1:
    vendas_ano()
if b2:
    vendas_categoria()
if b3:
    vendas_cat_ano()
if b4:
    vendas_ano_cat()
if b5:
    vendas_cat_mes_ano()
if b6:
    vendas_lojas_cat()
if b7:
    vendas_prod_maior()
if b8:
    vendas_prod_menor()
if b9:
    prods_rentaveis()
if b10:
    vendas_lojas()
if b11:
    vendas_vendedor()

vendas_prods_fab(fab_escolhido)
vendas_prod_maior_lj(lj_escolhida)
vendas_prod_menor_lj(loja_escolhida)
prods_rentaveis_lojas(loja_esc)
