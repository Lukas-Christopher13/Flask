from .ext.db import db
from .models import Pessoas, PessoasModel
from sqlalchemy import or_
from sqlalchemy.orm import aliased
from sqlalchemy import func as F


class PessoasRepository:
    def create(self, apelido, nome, nascimento, stack=None):
        pessoa = Pessoas(
            apelido=apelido, 
            nome=nome, 
            nascimento=nascimento,
            stack=stack
        )

        PessoasModel.model_validate(pessoa)

        db.session.add(pessoa)
        db.session.commit()

    def get_pessoa(self, id) -> Pessoas:
        pessoa: Pessoas = db.session.query(Pessoas) \
                                    .filter(Pessoas.id == id).first()
        return pessoa
            
    #Melhorar as o select por 'termo'
    def get_pessoa_by_termo(self, termo):
        pessoas = db.session \
            .query(Pessoas) \
            .filter(
                or_(
                    Pessoas.nome.like(f"%{termo}%"),
                    Pessoas.apelido.like(f"%{termo}%"),
                    F.array_to_string(Pessoas.stack, ',').like(f"%{termo}%")
                )
            ) \
            .limit(50) \
            .all()
       
        return pessoas
    
    def count(self):
        count = db.session.query(F.count(Pessoas.id)).scalar()
        return count