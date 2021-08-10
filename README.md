# Splunk SDK App Collection for SDK testing

The Splunk SDK App Collection contains several small Splunk applications that are purely used for testing Splunk's Software Development Kits (SDKs).

This repository is **ONLY** useful if you are testing one of Splunk's SDKs. **DO NOT INSTALL** unless you are planning to test a Splunk SDK against Splunk.

This SDK App Collection is used to test the following SDKs:

* [splunk-sdk-python](https://github.com/splunk/splunk-sdk-python)
* [splunk-sdk-javascript](https://github.com/splunk/splunk-sdk-javascript)
* [splunk-sdk-java](https://github.com/splunk/splunk-sdk-java)
* [splunk-sdk-ruby](https://github.com/splunk/splunk-sdk-ruby)
* [splunk-sdk-csharp](https://github.com/splunk/splunk-sdk-charp)
* [splunk-sdk-csharp-pcl](https://github.com/splunk/splunk-sdk-charp-pcl)
* [splunk-sdk-php](https://github.com/splunk/splunk-sdk-php)

Without the Splunk SDK App Collection Installed, many tests in the previously mentioned SDKs will fail.

## Installation:
1. Clone the sdk-app-collection repo
2. Move it to ```$SPLUNK_HOME/etc/apps/``` (where $SPLUNK_HOME is the path to your splunk directory)
3. Restart splunk

### How to contribute

If you would like to contribute to the SDK, go here for more information:

* [Splunk and open source][contributions]

* [Individual contributions][indivcontrib]

* [Company contributions][companycontrib]

## Documentation and resources

If you need to know more:

* For all things developer with Splunk, your main resource is the
  [Splunk Developer Portal][devportal].

* For more about the Splunk REST API, see the
  [REST API Reference][restapiref].

* For more about about Splunk in general, see [Splunk>Docs][splunkdocs].

### Contact us

You can reach the Developer Platform team at _devinfo@splunk.com_.

## License

The Splunk JavaScript Software Development Kit is licensed under the Apache
License 2.0. Details can be found in the LICENSE file.


[devportal]:                http://dev.splunk.com
[restapiref]:               http://docs.splunk.com/Documentation/Splunk/latest/RESTAPI
[splunkdocs]:               http://docs.splunk.com/Documentation/Splunk
[contributions]:            http://dev.splunk.com/view/opensource/SP-CAAAEDM
[indivcontrib]:             http://dev.splunk.com/goto/individualcontributions
[companycontrib]:           http://dev.splunk.com/view/companycontributions/SP-CAAAEDR
