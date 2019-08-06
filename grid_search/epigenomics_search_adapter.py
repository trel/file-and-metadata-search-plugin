from swagger_server.models import Indexes, IndexSearchAttributes, SearchAttributes


class EpigenomicsSearchAdapter:
    """Supports Epigenomics core Elastic search functions provided to the standard API"""

    def __init__(self):
        """
        Parameters

        """

        pass

    def describe_index(self):
        """
        Describe the capabilities of this particular index server
        :return: index
        """

        index_search = Indexes()
        index_search.id ="niehs-epigenomics"
        index_search.name = "Epigenomics ElasticSearch Indexes"
        index_search.info ="NIEHS Data Commons search for Epigenomics data via project and sample information"
        indexes = []
        index_entry = Indexes();
        index_entry.id = "EpigenomicsProjects"
        index_entry.name = "Epigenomics Projects"
        index_entry.maintainer = "ODS"
        index_entry.contact_email = "mike.conway@nih.gov"
        index_entry.info = "Search of project request information, hypothesis, purpose, etc. " \
                           "as entered during the project approval phase"
        indexes.append(index_entry)
        index_entry = Indexes();
        index_entry.id = "EpigenomicsSamplesandRuns"
        index_entry.name = "Epigenomics Samples and Runs"
        index_entry.info = "Search of sequencing runs and samples"
        index_entry.maintainer = "ODS"
        index_entry.contact_email = "mike.conway@nih.gov"
        indexes.append(index_entry)

        index_search.attributes = indexes

        return index_search

    def search_attributes(self, index_name):
        """
        Parse index attribute and an particular index
        :return: searchAttributes
        """
        result = SearchAttributes()
        result.id = 'epi_projects'
        result.info = 'Projects indexed from Epigenomics core'
        result.name = index_name
        result.attributes = []

        attribute_entry = IndexSearchAttributes(
            attrib_name='Hypothesis',
            attrib_type='String',
            info='Descriptive hypothesis of the porject submitted by researcher',
            shortcut_text='hyp'
        )
        result.attributes.append(attribute_entry)

        attribute_entry = IndexSearchAttributes(
            attrib_name='Title',
            attrib_type='String',
            info='Descriptive title of the project submitted by researcher',
            shortcut_text='hyp'
        )
        result.attributes.append(attribute_entry)

        return result
