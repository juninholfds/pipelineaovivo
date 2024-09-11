import streamlit as st 

def main():

    st.title('Sistema de CRM de Vendas da ZapFlow - FrontEnd Simples')
    st.text_input("Campo de Texto para Inserção do email do vendedor")
    st.date_input("Campo para inserir a Data em que a venda foi realizada")
    st.time_input("Campo para inserir a Hora em que a venda foi realizada")
    st.number_input("Campo numérico para inserir o valor monetário da Venda Realizada")
    st.number_input("Campo numérico para inserir a quantidade de produtos vendidos")
    st.selectbox("Campo de seleção para escolher o produto vendido", ['ZapFlow com Gemini'])

if __name__=="__main__":
    main()