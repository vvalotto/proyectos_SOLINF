"""
Definición del modelo de datos y declaración de las tablas del modelo
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

Base = declarative_base()


class ProyectoDTO(Base):
    """
    Tabla Proyecto
    """
    __tablename__ = "td_proyecto"

    id = Column(String(36), primary_key=True)
    nombre_proyecto = Column(String(100), nullable=False)
    tipo_proyecto = Column(String(50), nullable=False)
    descripcion = Column(String(200), nullable=False)
    fecha_fin = Column(String(10), nullable=False)


class ComponenteDTO(Base):
    """
    Tabla Componente
    """
    __tablename__ = "td_componente"

    id = Column(String(36), primary_key=True)
    nombre_componente = Column(String(200), nullable=False)
    tipo_componente = Column(String(50), nullable=False)
    id_proyecto = Column(String(36), ForeignKey(ProyectoDTO.id))


class ElementoDTO(Base):

    __tablename__ = "td_elemento"

    id = Column(String(36), primary_key=True)
    tipo_elemento = Column(String(20), nullable=False)
    nombre_elemento = Column(String(100), nullable=False)
    descripcion = Column(String(200), nullable=False)
    id_componente = Column(String(36), ForeignKey(ComponenteDTO.id))