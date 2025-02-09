# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DisplayAppliancePdf(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, attachment_info=None, doc_name=None, document_id=None, latest_pdf=None, latest_pdf_id=None, original_pdf=None, original_pdf_id=None, page_count=None, pdf_type=None):
        """
        DisplayAppliancePdf - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attachment_info': 'DisplayApplianceSignerAttachment',
            'doc_name': 'str',
            'document_id': 'str',
            'latest_pdf': 'str',
            'latest_pdf_id': 'str',
            'original_pdf': 'str',
            'original_pdf_id': 'str',
            'page_count': 'int',
            'pdf_type': 'str'
        }

        self.attribute_map = {
            'attachment_info': 'attachmentInfo',
            'doc_name': 'docName',
            'document_id': 'documentId',
            'latest_pdf': 'latestPdf',
            'latest_pdf_id': 'latestPDFId',
            'original_pdf': 'originalPdf',
            'original_pdf_id': 'originalPDFId',
            'page_count': 'pageCount',
            'pdf_type': 'pdfType'
        }

        self._attachment_info = attachment_info
        self._doc_name = doc_name
        self._document_id = document_id
        self._latest_pdf = latest_pdf
        self._latest_pdf_id = latest_pdf_id
        self._original_pdf = original_pdf
        self._original_pdf_id = original_pdf_id
        self._page_count = page_count
        self._pdf_type = pdf_type

    @property
    def attachment_info(self):
        """
        Gets the attachment_info of this DisplayAppliancePdf.

        :return: The attachment_info of this DisplayAppliancePdf.
        :rtype: DisplayApplianceSignerAttachment
        """
        return self._attachment_info

    @attachment_info.setter
    def attachment_info(self, attachment_info):
        """
        Sets the attachment_info of this DisplayAppliancePdf.

        :param attachment_info: The attachment_info of this DisplayAppliancePdf.
        :type: DisplayApplianceSignerAttachment
        """

        self._attachment_info = attachment_info

    @property
    def doc_name(self):
        """
        Gets the doc_name of this DisplayAppliancePdf.
        

        :return: The doc_name of this DisplayAppliancePdf.
        :rtype: str
        """
        return self._doc_name

    @doc_name.setter
    def doc_name(self, doc_name):
        """
        Sets the doc_name of this DisplayAppliancePdf.
        

        :param doc_name: The doc_name of this DisplayAppliancePdf.
        :type: str
        """

        self._doc_name = doc_name

    @property
    def document_id(self):
        """
        Gets the document_id of this DisplayAppliancePdf.
        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.

        :return: The document_id of this DisplayAppliancePdf.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """
        Sets the document_id of this DisplayAppliancePdf.
        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.

        :param document_id: The document_id of this DisplayAppliancePdf.
        :type: str
        """

        self._document_id = document_id

    @property
    def latest_pdf(self):
        """
        Gets the latest_pdf of this DisplayAppliancePdf.
        

        :return: The latest_pdf of this DisplayAppliancePdf.
        :rtype: str
        """
        return self._latest_pdf

    @latest_pdf.setter
    def latest_pdf(self, latest_pdf):
        """
        Sets the latest_pdf of this DisplayAppliancePdf.
        

        :param latest_pdf: The latest_pdf of this DisplayAppliancePdf.
        :type: str
        """

        self._latest_pdf = latest_pdf

    @property
    def latest_pdf_id(self):
        """
        Gets the latest_pdf_id of this DisplayAppliancePdf.
        

        :return: The latest_pdf_id of this DisplayAppliancePdf.
        :rtype: str
        """
        return self._latest_pdf_id

    @latest_pdf_id.setter
    def latest_pdf_id(self, latest_pdf_id):
        """
        Sets the latest_pdf_id of this DisplayAppliancePdf.
        

        :param latest_pdf_id: The latest_pdf_id of this DisplayAppliancePdf.
        :type: str
        """

        self._latest_pdf_id = latest_pdf_id

    @property
    def original_pdf(self):
        """
        Gets the original_pdf of this DisplayAppliancePdf.
        

        :return: The original_pdf of this DisplayAppliancePdf.
        :rtype: str
        """
        return self._original_pdf

    @original_pdf.setter
    def original_pdf(self, original_pdf):
        """
        Sets the original_pdf of this DisplayAppliancePdf.
        

        :param original_pdf: The original_pdf of this DisplayAppliancePdf.
        :type: str
        """

        self._original_pdf = original_pdf

    @property
    def original_pdf_id(self):
        """
        Gets the original_pdf_id of this DisplayAppliancePdf.
        

        :return: The original_pdf_id of this DisplayAppliancePdf.
        :rtype: str
        """
        return self._original_pdf_id

    @original_pdf_id.setter
    def original_pdf_id(self, original_pdf_id):
        """
        Sets the original_pdf_id of this DisplayAppliancePdf.
        

        :param original_pdf_id: The original_pdf_id of this DisplayAppliancePdf.
        :type: str
        """

        self._original_pdf_id = original_pdf_id

    @property
    def page_count(self):
        """
        Gets the page_count of this DisplayAppliancePdf.
        

        :return: The page_count of this DisplayAppliancePdf.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count of this DisplayAppliancePdf.
        

        :param page_count: The page_count of this DisplayAppliancePdf.
        :type: int
        """

        self._page_count = page_count

    @property
    def pdf_type(self):
        """
        Gets the pdf_type of this DisplayAppliancePdf.
        

        :return: The pdf_type of this DisplayAppliancePdf.
        :rtype: str
        """
        return self._pdf_type

    @pdf_type.setter
    def pdf_type(self, pdf_type):
        """
        Sets the pdf_type of this DisplayAppliancePdf.
        

        :param pdf_type: The pdf_type of this DisplayAppliancePdf.
        :type: str
        """

        self._pdf_type = pdf_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
