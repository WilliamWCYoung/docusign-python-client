# Change Log
All notable changes to this project will be documented in this file.

See [DocuSign Support Center](https://support.docusign.com/en/releasenotes/) for Product Release Notes.

## [3.0.0] - eSignature API v2.1-19.2.02 - 2019-10-10
### Changed
* Updated the way the models and classes are initialized. Now using constructor parameters to initialize the classes. Updates to unit tests. (DCM-1788)
### Fixed
* A bug in model mapping where instead of mapping to custom DocuSign `Date` class, was mapping to python `date` class. Causing the functions such as `envelope_api.list_tabs()` to raise exception. (DCM-3102)
### BREAKING
* The SDK now supports API v2.1-19.2.02 of the DocuSign eSignature API.
* SDK Release Version updated.

## [3.0.0rc1] - eSignature API v2.1-19.2.02 - 2019-08-28
### Changed
* Updated the way the models and classes are initialized. Now using constructor parameters to initialize the classes. Updates to unit tests. (DCM-1788)
### Fixed
* A bug in model mapping where instead of mapping to custom DocuSign `Date` class, was mapping to python `date` class. Causing the functions such as `envelope_api.list_tabs()` to raise exception. (DCM-3102)
### BREAKING
* The SDK now supports API v2.1-19.2.02 of the DocuSign eSignature API.
* SDK Release Version updated.

## [2.0.1] - 2019-06-24
### Removed
* Removed harcoded test config values from the test cases. Now getting test config values from the environment variables.
### Changed
* Made dependencies versions broader (using '>=' to specify minimum supported versions).

## [2.0.0] - eSignature API v19.1.02 - 2019-05-24
### Removed
* configure_jwt_authorization_flow has been removed. Update to use either request_jwt_user_token or request_jwt_application_token
* empty test placeholder files
### Changed
* The SDK now supports version 19.1.02 of the DocuSign eSignature API.
* SDK Release Version updated.
* ApiException, ApiClient and Configuration classes have moved under client folder. New import statement was simplified. Example: from docusign_esign import ApiException
* Using PyJWT and cryptography libraries for OAuth, instead of jwcrypto and py-oauth2
### Added
* Added a new *tabGroupLabels* field to all Tabs models
* Added a new *Witnesses* field to all Recipients models
* Implemented models for Smart Sections feature
* Implemented initial support of HMAC for DocuSign Connect
### Fixed
* A bug with that could cause the *moveEnvelopes* method call to return a response without a *Content-Type* header. (DCM-2871)

## [2.0.0rc1] - eSignature API v19.1.02 - 2019-05-13
### Removed
* configure_jwt_authorization_flow has been removed. Update to use either request_jwt_user_token or request_jwt_application_token
* empty test placeholder files
### Changed
* The SDK now supports version 19.1.02 of the DocuSign eSignature API.
* SDK Release Version updated.
* ApiException, ApiClient and Configuration classes have moved under client folder. New import statement was simplified. Example: from docusign_esign import ApiException
* Using PyJWT and cryptography libraries for OAuth, instead of jwcrypto and py-oauth2
### Added
* Added a new *tabGroupLabels* field to all Tabs models
* Added a new *Witnesses* field to all Recipients models
* Implemented models for Smart Sections feature
* Implemented initial support of HMAC for DocuSign Connect
### Fixed
* A bug with that could cause the *moveEnvelopes* method call to return a response without a *Content-Type* header. (DCM-2871)

## [1.0.3] - 2018-03-22
### Fixed
- Issue [`#7`](https://github.com/docusign/docusign-python-client/issues/7): TypeError: the JSON object must be str, not 'bytes'.
- PR [`#8`](https://github.com/docusign/docusign-python-client/pull/8): Ensure closure of private key file to prevent open handles. Allow key bytes to be supplied to JWT configure method.
- PR [`#9`](https://github.com/docusign/docusign-python-client/pull/9): Support for cross-version json parsing of response.

## [1.0.2] - 2017-12-05
### Fixed
- PR [`#6`](https://github.com/docusign/docusign-python-client/pull/6): Invalid Grant URI at get_jwt_uri().

## [1.0.1] - 2017-09-05
### Added
- Added OAuth support.

## [1.0.0] - 2017-08-08
### Added
- Initial commit of the new Python SDK for DocuSign API, automatically generated from OpenAPI specification.