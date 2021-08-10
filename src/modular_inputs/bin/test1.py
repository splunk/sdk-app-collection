import sys

scheme = """
<scheme>
    <title>Test "Input" - 1</title>
    <description>A description of test input 1 with special characters: //;!*%</description>
    <use_external_validation>false</use_external_validation>
    <streaming_mode>xml</streaming_mode>

    <endpoint>
        <args>
            <arg name="resname">
                <title>Resource name</title>
                <description>Name of resource</description>
                <required_on_create>false</required_on_create>
            </arg>
            <arg name="key_id">
                <title>Key ID</title>
                <description>The key of the system</description>
                <required_on_create>false</required_on_create>
            </arg>
            <arg name="no_description">
                <title>Field sans description</title>
                <required_on_create>false</required_on_create>
            </arg>
            <arg name="empty_description">
                <title>Field with empty description</title>
                <description></description>
                <required_on_create>false</required_on_create>
            </arg>
            <arg name="arg_required_on_edit">
                <title>Field with required_on_edit</title>
                <required_on_edit>true</required_on_edit>
                <required_on_create>false</required_on_create>
            </arg>
            <arg name="not_required_on_edit">
                <title>Field not required on edit</title>
                <required_on_edit>false</required_on_edit>
                <required_on_create>false</required_on_create>
            </arg>
            <arg name="required_on_create">
                <title>Field required on create</title>
                <required_on_create>true</required_on_create>
            </arg>
            <arg name="not_required_on_create">
                <title>Field not required on create</title>
                <required_on_create>false</required_on_create>
            </arg>
            <arg name="number_field">
                <title>An number</title>
                <data_type>number</data_type>
                <required_on_create>false</required_on_create>
            </arg>
            <arg name="string_field">
                <title>A string field</title>
                <data_type>string</data_type>
                <required_on_create>false</required_on_create>
            </arg>
            <arg name="boolean_field">
                <title>A boolean field</title> 
                <data_type>boolean</data_type>
                <required_on_create>false</required_on_create>
            </arg>
        </args>
    </endpoint>
</scheme>
"""

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "--scheme":
        print (scheme)
        exit(0)


            
