import os
import csv
from collections import Counter
from itertools import islice
from typing import List

from config import settings


class StatisticsService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StatisticsService, cls).__new__(cls)
        return cls._instance

    def get_statistics(self) -> dict[str, dict[str, List[any]]]:
        interfaces_per_year = self.csv_to_dict_of_lists("processed_data/interfaces_per_year.tsv", ["Year", "Count", "Cumulative"], "\t")
        pdbs_per_year = self.csv_to_dict_of_lists("processed_data/pdbs_per_year.tsv", ["Year", "Count", "Cumulative"], "\t")
        organism_analysis = self.csv_to_dict_of_lists("processed_data/interface_organisms_analysis.tsv", ["SPECIES", "HS_OTHER"], "\t")
        organism_analysis = [
            self.get_count_for_pie_chart(organism_analysis["SPECIES"]),
            self.get_count_for_pie_chart(organism_analysis["HS_OTHER"])
        ]
        frequent_organisms = self.csv_to_dict_of_lists("processed_data/most_frequent_12_organisms.tsv", ["ORGANISM_NAME", "COUNTS"], "\t")
        dm_frequency = self.csv_to_dict_of_lists("processed_data/dm_frequency.tsv", ["dm_desc", "frequency"], "\t", 12)
        sf_frequency = self.csv_to_dict_of_lists("processed_data/sf_frequency.tsv", ["sf_desc", "frequency"], "\t", 12)
        cf_frequency = self.csv_to_dict_of_lists("processed_data/cf_frequency.tsv", ["cf_desc", "frequency"], "\t", 12)

        return {
            "interfaces_per_year": interfaces_per_year,
            "pdbs_per_year": pdbs_per_year,
            "organism_analysis": organism_analysis,
            "frequent_organisms": frequent_organisms,
            "dm_frequency": dm_frequency,
            "sf_frequency": sf_frequency,
            "cf_frequency": cf_frequency,
        }
        
    def csv_to_dict_of_lists(self, file_path: str, columns_to_read: List[str], separater: str=',', limit: int = None) -> dict[str, List[any]]:
        dict_of_lists = {}

        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=separater)
            
            for key in columns_to_read:
                dict_of_lists[key] = []

            if limit is not None:
                reader = islice(reader, limit)
            
            for row in reader:
                for key in columns_to_read:
                    dict_of_lists[key].append(row[key])
        
        return dict_of_lists
    
    def get_count_for_pie_chart(self, data: List[any]):
        counts = Counter(data)
        return {
            "labels": list(counts.keys()),
            "values": list(counts.values())
            }
