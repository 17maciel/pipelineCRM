import streamlit as st
from datetime import datetime, time

def main():

    st.title("Sistema de CRM e Vendas")
    email = st.text_input("Email vendedor")
    data = st.date_input("Data da Venda", datetime.now())
    hora = st.time_input("Hora da venda", value=time(9,0))
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade produtos")
    produto = st.selectbox("Escolher produto.", ["Zapflow com Gemini", "Zapflow com ChatGPT", "Zapflow com Llmama3.0"])

    if st.button("Salvar"):

        data_hora = datetime.combine(data,hora)
        st.write("**Dados da Venda:**")
        st.write(f"Email: {email}") 
        st.write(f"Data e hora da venda: {data_hora}")
        st.write(f"Valor da venda: R$ {valor:2f}")
        st.write(f"Quantidade de produtos: {quantidade}")   
        st.write(f"Produto: {produto}")
        st.write(f"Valor total da venda: R$ {valor * quantidade:2f}")

if __name__=="__main__":
    main()
