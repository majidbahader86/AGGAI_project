
from typing import List, Dict, Any, Union

class DiseaseReport:
    def __init__(self, disease_id: str, plant_type: str, symptoms: str, diagnosis: str, treatment: str, date_of_incident: str, latitude: float, longitude: float, submitted_by: str, notes: str = "", severity: str = "", environmental_conditions: Dict[str, Any] = None) -> None:
        self.disease_id = disease_id
        self.plant_type = plant_type
        self.symptoms = symptoms
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.date_of_incident = date_of_incident
        self.latitude = latitude
        self.longitude = longitude
        self.submitted_by = submitted_by
        self.notes = notes
        self.severity = severity
        self.environmental_conditions = environmental_conditions if environmental_conditions else {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "disease_id": self.disease_id,
            "plant_type": self.plant_type,
            "symptoms": self.symptoms,
            "diagnosis": self.diagnosis,
            "treatment": self.treatment,
            "date_of_incident": self.date_of_incident,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "submitted_by": self.submitted_by,
            "notes": self.notes,
            "severity": self.severity,
            "environmental_conditions": self.environmental_conditions
        }

class SciencePaper:
    def __init__(self, paper_id: str, title: str, authors: List[str], abstract: str, publication_date: str, journal: str, url: str, 
                 keywords: List[str] = None, citation_count: int = 0, related_topics: List[str] = None,
                 doi: str = "", research_field: str = "", methodology: str = "", **kwargs: Any) -> None:
        self.paper_id = paper_id
        self.title = title
        self.authors = authors
        self.abstract = abstract
        self.publication_date = publication_date
        self.journal = journal
        self.url = url
        self.keywords = keywords if keywords else []
        self.citation_count = citation_count
        self.related_topics = related_topics if related_topics else []
        self.doi = doi
        self.research_field = research_field
        self.methodology = methodology
        self.additional_attributes = kwargs

    def to_dict(self) -> Dict[str, Any]:
        paper_dict = {
            "paper_id": self.paper_id,
            "title": self.title,
            "authors": self.authors,
            "abstract": self.abstract,
            "publication_date": self.publication_date,
            "journal": self.journal,
            "url": self.url,
            "keywords": self.keywords,
            "citation_count": self.citation_count,
            "related_topics": self.related_topics,
            "doi": self.doi,
            "research_field": self.research_field,
            "methodology": self.methodology
        }
        paper_dict.update(self.additional_attributes)
        return paper_dict


class Dataset:
    def __init__(self, dataset_id: str, name: str, description: str, creation_date: str, url: str, creator: str,
                 data_format: str = "", size_bytes: int = 0, license: str = "", tags: list = None,
                 version: str = "", data_sources: list = None, data_quality_metrics: Dict[str, Any] = None,
                 hash_value: str = "") -> None:
        self.dataset_id = dataset_id
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.url = url
        self.creator = creator
        self.data_format = data_format
        self.size_bytes = size_bytes
        self.license = license
        self.tags = tags if tags else []
        self.version = version
        self.data_sources = data_sources if data_sources else []
        self.data_quality_metrics = data_quality_metrics if data_quality_metrics else {}
        self.hash_value = hash_value

    def to_dict(self) -> Dict[str, Any]:
        return {
            "dataset_id": self.dataset_id,
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date,
            "url": self.url,
            "creator": self.creator,
            "data_format": self.data_format,
            "size_bytes": self.size_bytes,
            "license": self.license,
            "tags": self.tags,
            "version": self.version,
            "data_sources": self.data_sources,
            "data_quality_metrics": self.data_quality_metrics,
            "hash_value": self.hash_value
        }

DataEntry = Union[DiseaseReport, SciencePaper, Dataset]

