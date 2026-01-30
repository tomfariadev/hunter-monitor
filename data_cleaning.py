import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
        
    # Converte preço para numérico
    df["preco"] = df["preco"].str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
    df["preco"] = pd.to_numeric(df["preco"], errors="coerce")
    
    # Remove nulos que podem ter surgido na conversão
    df = df.dropna(subset=["preco"])

    # preços abaixo de 10% da média
    media = df["preco"].mean()
    df = df[df["preco"] > (media * 0.1)] # Mantém itens acima de 10% da média

    df = df.drop_duplicates(subset=["produto", "preco"])
    df = df.sort_values(by="preco", ascending=True)    

    return df