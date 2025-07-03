







@dataclass
class PessoaFisica(Pessoa):
    nome: str
    cpf: str
    profissao: str

    def __str__(self):
        # return f"Somos da empresa {self.nome_fantasia}, de razão social {self.razao_social} {self,razao_social}, nosso CNPJ é {self.cnpj}. Pode nos contratar pelo email "
        yield f"self"








def __del__(self):
    print(f"Obketo (self.nome) destruido com sucesso.")

@dataclass
class PessoaJuridica(Pessoa):
    razao_social: str
    nome_fantasia: str
    cnpj: str

    def __str__(self):
        return f"Somos da empresa {self.nome_fantasia}, de razão social {self.razao_social} {self,razao_social} "