import json

import yaml
from pydantic import BaseModel
from pymonad.either import Right, Left, Either


class SPGData:
    """Constants and expectations for the SPG model"""
    THEME_CAPTION = "Thème"
    TITLE_CAPTION = "Titre"
    PRESENTATION_CAPTION = "Présentation et description"
    MINDMAP_CAPTION = "Carte thématique"
    PUBLIC_PROSPECT_CAPTION = "Public"
    PRE_REQUIS_CAPTION = "Pré-requis et conditions d'accès à la formation (Qualiopi)"
    OBJECTIVES_CAPTION = "Objectifs pédagogiques (Qualiopi)"
    SKILLS_CAPTION = "Compétences visées (Qualiopi)"
    TIMING_CAPTION = "Durée (Temporisation) (Qualiopi)"
    MEANS_CAPTION = "Moyen d'accompagnement et Suivi pédagogique (Qualiopi)"
    PROGRAM_CAPTION = "Programme pédagogique (Modalités pédagogiques) (Qualiopi) : du contenu et du séquencement"
    EVALUATIONS_CAPTION = "Modalités d'évaluations (Qualiopi)"
    CERTIFICATION_CAPTION = "Modalités de certification et Certification visé (Qualiopi)"
    PLACE_CAPTION = "Lieux (Qualiopi)"
    PRICE_CAPTION = "Tarifs"
    INFRASTRUCTURE_CAPTION = "Moyens logistiques et matériels (Qualiopi)"
    PURSUIT_CAPTION = "Poursuite en formation (Qualiopi)"
    ACCESS_TIME_CAPTION = "Délais d'accès (Réglementaire)"
    MOBILITY_CAPTION = "Accessibilité et Handicap (Qualiopi)"
    TESTIMONY_CAPTION = "Témoignage Evaluation de la formation (Qualiopi)"
    TESTIMONY_CUSTOMER_CAPTION = "Témoignage apprenant/commanditaire"

    # All the expectations texts are kept as class attributes
    # For brevity, I've included just a few examples - you would include all of them
    THEME_EXPECTATIONS = """Thème : on dissocie le thème qui est au global dans laquelle s'insère la formation,
    le thème n'est pas la formation mais le sujet général dans lequel il s'insère."""


class SPD(BaseModel):
    """Scénario Pédagogique Détaillé"""
    titre: str = ""
    objectif: str = ""

    def to_yaml(self) -> Either[Exception, str]:
        try:
            return Right(yaml.dump(self.model_dump()))
        except Exception as e:
            return Left(e)

    def to_json(self) -> Either[Exception, str]:
        try:
            return Right(json.dumps(self.model_dump()))
        except Exception as e:
            return Left(e)

    @classmethod
    def from_yaml(cls, yaml_str: str) -> Either[Exception, 'SPD']:
        try:
            data = yaml.safe_load(yaml_str)
            return Right(cls(**data))
        except Exception as e:
            return Left(e)

    @classmethod
    def from_json(cls, json_str: str) -> Either[Exception, 'SPD']:
        try:
            data = json.loads(json_str)
            return Right(cls(**data))
        except Exception as e:
            return Left(e)

class SPG(BaseModel):
    """Scénario Pédagogique Global"""
    # theme: Dict[str, str] = Field(default_factory=lambda: {SPGData.THEME_CAPTION: ""})
    # theme: Dict[str, str] = Field(default_factory=lambda: {SPGData.THEME_CAPTION: ""})
    # title: Dict[str, str] = Field(default_factory=lambda: {SPGData.TITLE_CAPTION: ""})
    # presentation: Dict[str, str] = Field(default_factory=lambda: {SPGData.PRESENTATION_CAPTION: ""})
    # mindmap: Dict[str, str] = Field(default_factory=lambda: {SPGData.MINDMAP_CAPTION: ""})
    # public_prospect: Dict[str, str] = Field(default_factory=lambda: {SPGData.PUBLIC_PROSPECT_CAPTION: ""})
    # pre_requis: Dict[str, str] = Field(default_factory=lambda: {SPGData.PRE_REQUIS_CAPTION: ""})
    # objectives: Dict[str, str] = Field(default_factory=lambda: {SPGData.OBJECTIVES_CAPTION: ""})
    # skills: Dict[str, str] = Field(default_factory=lambda: {SPGData.SKILLS_CAPTION: ""})
    # timing: Dict[str, str] = Field(default_factory=lambda: {SPGData.TIMING_CAPTION: ""})
    # means: Dict[str, str] = Field(default_factory=lambda: {SPGData.MEANS_CAPTION: ""})
    # program: Dict[str, str] = Field(default_factory=lambda: {SPGData.PROGRAM_CAPTION: ""})
    # evaluations: Dict[str, str] = Field(default_factory=lambda: {SPGData.EVALUATIONS_CAPTION: ""})
    # certification: Dict[str, str] = Field(default_factory=lambda: {SPGData.CERTIFICATION_CAPTION: ""})
    # place: Dict[str, str] = Field(default_factory=lambda: {SPGData.PLACE_CAPTION: ""})
    # price: Dict[str, str] = Field(default_factory=lambda: {SPGData.PRICE_CAPTION: ""})
    # infrastructure: Dict[str, str] = Field(default_factory=lambda: {SPGData.INFRASTRUCTURE_CAPTION: ""})
    # pursuit: Dict[str, str] = Field(default_factory=lambda: {SPGData.PURSUIT_CAPTION: ""})
    # access_time: Dict[str, str] = Field(default_factory=lambda: {SPGData.ACCESS_TIME_CAPTION: ""})
    # mobility: Dict[str, str] = Field(default_factory=lambda: {SPGData.MOBILITY_CAPTION: ""})
    # testimony: Dict[str, str] = Field(default_factory=lambda: {SPGData.TESTIMONY_CAPTION: ""})
    # testimony_customer: Dict[str, str] = Field(default_factory=lambda: {SPGData.TESTIMONY_CUSTOMER_CAPTION: ""})

    def to_yaml(self) -> Either[Exception, str]:
        try:
            return Right(yaml.dump(self.model_dump()))
        except Exception as e:
            return Left(e)

    def to_json(self) -> Either[Exception, str]:
        try:
            return Right(json.dumps(self.model_dump()))
        except Exception as e:
            return Left(e)

    @classmethod
    def from_yaml(cls, yaml_str: str) -> Either[Exception, 'SPG']:
        try:
            data = yaml.safe_load(yaml_str)
            return Right(cls(**data))
        except Exception as e:
            return Left(e)

    @classmethod
    def from_json(cls, json_str: str) -> Either[Exception, 'SPG']:
        try:
            data = json.loads(json_str)
            return Right(cls(**data))
        except Exception as e:
            return Left(e)


class Training(BaseModel):
    """Training model containing SPG and optional SPDs"""
    spg: SPG

    # spds: Set[SPD] = Field(default_factory=set)

    def to_yaml(self) -> Either[Exception, str]:
        try:
            return Right(yaml.dump(self.model_dump()))
        except Exception as e:
            return Left(e)

    def to_json(self) -> Either[Exception, str]:
        try:
            return Right(json.dumps(self.model_dump()))
        except Exception as e:
            return Left(e)

    @classmethod
    def from_yaml(cls, yaml_str: str) -> Either[Exception, 'Training']:
        try:
            data = yaml.safe_load(yaml_str)
            return Right(cls(**data))
        except Exception as e:
            return Left(e)

    @classmethod
    def from_json(cls, json_str: str) -> Either[Exception, 'Training']:
        try:
            data = json.loads(json_str)
            return Right(cls(**data))
        except Exception as e:
            return Left(e)
