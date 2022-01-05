# Generated by Django 2.2.24 on 2022-01-05 16:25

from django.db import migrations

from project.modelcomponents.access import AccessPolicy


def migrate_forward(apps, schema_editor):
    ActiveProject = apps.get_model('project', 'ActiveProject')
    ArchivedProject = apps.get_model('project', 'ArchivedProject')
    PublishedProject = apps.get_model('project', 'PublishedProject')
    License = apps.get_model('project', 'License')

    contributor_review_license_data = {
        "name": "PhysioNet Contributor Review Health Data License 1.5.0",
        "slug": "physionet-contributor-review-health-data-license-150",
        "text_content": "The PhysioNet Contributor Review Health Data License\r\nVersion 1.5.0\r\n\r\nCopyright (c) <YEAR> MIT Laboratory for Computational Physiology\r\n\r\nThe MIT Laboratory for Computational Physiology (MIT-LCP) wishes \r\nto make data available for research and educational purposes to \r\nqualified requestors, but only if the data are used and protected \r\nin accordance with the terms and conditions stated in this License.\r\n\r\nIt is hereby agreed between the data requestor, hereinafter referred to\r\nas the \"LICENSEE\", and MIT-LCP, that:\r\n\r\n1. The LICENSEE will not attempt to identify any individual or\r\n   institution referenced in PhysioNet restricted data.  \r\n2. The LICENSEE will exercise all reasonable and prudent care to avoid\r\n   disclosure of the identity of any individual or institution\r\n   referenced in PhysioNet restricted data in any publication or other\r\n   communication.  \r\n3. The LICENSEE will not share access to PhysioNet restricted data\r\n   with anyone else. \r\n4. The LICENSEE will exercise all reasonable and prudent care to\r\n   maintain the physical and electronic security of PhysioNet restricted\r\n   data.  \r\n5. If the LICENSEE finds information within PhysioNet restricted data\r\n   that he or she believes might permit identification of any individual\r\n   or institution, the LICENSEE will report the location of this\r\n   information promptly by email to PHI-report@physionet.org, citing the\r\n   location of the specific information in question.  \r\n6. The LICENSEE will use the data for the sole purpose of lawful use in\r\n   scientific research and no other.  \r\n7. The LICENSEE will be responsible for ensuring that he or she\r\n   maintains up to date certification in human research subject\r\n   protection and HIPAA regulations.\r\n8. The LICENSEE agrees to contribute code associated with publications\r\n   arising from this data to a repository that is open to the research community.\r\n9. This agreement may be terminated by either party at any time, but the\r\n   LICENSEE's obligations with respect to PhysioNet data shall continue\r\n   after termination.  \r\n\r\nTHE DATA ARE PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\r\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\r\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL\r\nTHE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR\r\nOTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\r\nARISING FROM, OUT OF OR IN CONNECTION WITH THE DATA OR THE USE OR OTHER\r\nDEALINGS IN THE DATA.",
        "html_content": "<p><br>\n<strong>The PhysioNet Contributor Review Health Data License</strong><br>\nVersion 1.5.0</p>\n\n<p>Copyright (c) &lt;YEAR&gt; MIT Laboratory for Computational Physiology</p>\n\n<p>The MIT Laboratory for Computational Physiology (MIT-LCP) wishes to make data available for research and educational purposes to qualified requestors, but only if the data are used and protected in accordance with the terms and conditions stated in this License.</p>\n\n<p>It is hereby agreed between the data requestor, hereinafter referred to as the &quot;LICENSEE&quot;, and MIT-LCP, that:</p>\n\n<ol>\n\t<li>The LICENSEE will not attempt to identify any individual or institution referenced in PhysioNet restricted data.</li>\n\t<li>The LICENSEE will exercise all reasonable and prudent care to avoid disclosure of the identity of any individual or institution referenced in PhysioNet restricted data in any publication or other communication.</li>\n\t<li>The LICENSEE will not share access to PhysioNet restricted data with anyone else.</li>\n\t<li>The LICENSEE will exercise all reasonable and prudent care to maintain the physical and electronic security of PhysioNet restricted data.</li>\n\t<li>If the LICENSEE finds information within PhysioNet restricted data that he or she believes might permit identification of any individual or institution, the LICENSEE will report the location of this information promptly by email to PHI-report@physionet.org, citing the location of the specific information in question.</li>\n\t<li>The LICENSEE will use the data for the sole purpose of lawful use in scientific research and no other.</li>\n\t<li>The LICENSEE will be responsible for ensuring that he or she maintains up to date certification in human research subject protection and HIPAA regulations.</li>\n\t<li>The LICENSEE agrees to contribute&nbsp;code associated with publications arising from this data to a repository that is open to the research community.</li>\n\t<li>This agreement may be terminated by either party at any time, but the LICENSEE&#39;s obligations with respect to PhysioNet data shall continue after termination. &nbsp;</li>\n</ol>\n\n<p>THE DATA ARE PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE DATA OR THE USE OR OTHER DEALINGS IN THE DATA.</p>",
        "home_page": "https://github.com/MIT-LCP/license-and-dua/tree/master/drafts",
        "access_policy": 3,
        "resource_types": "0,2,3",
        "dua_name": "PhysioNet Contributor Review Health Data Use Agreement 1.5.0",
        "dua_html_content": "<p>The Department for Intensive Care Medicine of the University Hospital of Bern, Bern, Switzerland (ICU) and the Department of Computer Science, ETH Zurich, Zurich, Switzerland (ETHZ) grant access to the HiRID patient database to make data available for research purposes, but only if the data are used and protected in accordance with the terms and conditions stated in this License. It is hereby agreed between the data requestor, hereinafter referred to as the &quot;LICENSEE&quot;, and ICU / ETHZ, that:</p>\n\n<ol>\n\t<li>The LICENSEE will not share access to HiRID data with anyone else.</li>\n\t<li>The LICENSEE will exercise all reasonable and prudent care to maintain the physical and electronic security of HiRID data.</li>\n\t<li>The LICENSEE will use the data for the sole purpose of lawful use in scientific research.</li>\n\t<li>The LICENSEE will not attempt to identify any individual referenced in the HiRID data.</li>\n\t<li>The LICENSEE will exercise all reasonable and prudent care to avoid disclosure of the identity of any individual referenced in HiRID data in any publication or other communication.</li>\n\t<li>If the LICENSEE finds information within HiRID data that he or she believes might permit the identification of any individual or institution, the LICENSEE will report the location of this information promptly by email to&nbsp;<a href=\"mailto:hirid@intensivecare.ai\">hirid@intensivecare.ai</a>&nbsp;citing the location of the specific information in question.</li>\n\t<li>The LICENSEE agrees to share any code associated with publications arising from this data on a defined HiRID repository (<a href=\"https://github.com/HIRID/HiRID_v1\">https://github.com/HIRID/HiRID_v1</a>).</li>\n\t<li>The LICENSEE will be responsible for ensuring that he or she maintains up to date certification of training in Good Clinical Practice (GCP) according to ICH-GCP international guidelines. Training in GCP may be achieved through a class or course, academic training program, or certification from a recognized clinical research professional organization.</li>\n\t<li>This agreement may be terminated by either party at any time, but the LICENSEE&#39;s obligations with respect to HRID data shall continue after termination.</li>\n</ol>\n\n<p>The data are provided without any warranty of any kind, expressed or implied. In no event shall the ICU or ETHZ be liable for any claim, damages or other liability arising from, out of or in connection with HiRID or the use or other dealing with HiRID.</p>",
        "access_request_template": ""
    }
    license = License.objects.create(**contributor_review_license_data)

    ActiveProject.objects.filter(is_self_managed_access=True).update(access_policy=AccessPolicy.CONTRIBUTOR_REVIEW, license=license)
    ArchivedProject.objects.filter(is_self_managed_access=True).update(access_policy=AccessPolicy.CONTRIBUTOR_REVIEW, license=license)
    PublishedProject.objects.filter(is_self_managed_access=True).update(access_policy=AccessPolicy.CONTRIBUTOR_REVIEW, license=license)


def migrate_backward(apps, schema_edtior):
    ActiveProject = apps.get_model('project', 'ActiveProject')
    ArchivedProject = apps.get_model('project', 'ArchivedProject')
    PublishedProject = apps.get_model('project', 'PublishedProject')
    License = apps.get_model('project', 'License')

    license = License.objects.get(slug='physionet-contributor-review-health-data-license-150')

    ActiveProject.objects.filter(access_policy=AccessPolicy.CONTRIBUTOR_REVIEW).update(is_self_managed_access=True, self_managed_dua=license.dua_html_content, self_managed_request_template=license.access_request_template)
    ArchivedProject.objects.filter(access_policy=AccessPolicy.CONTRIBUTOR_REVIEW).update(is_self_managed_access=True, self_managed_dua=license.dua_html_content, self_managed_request_template=license.access_request_template)
    PublishedProject.objects.filter(access_policy=AccessPolicy.CONTRIBUTOR_REVIEW).update(is_self_managed_access=True, self_managed_dua=license.dua_html_content, self_managed_request_template=license.access_request_template)

    license.delete()


class Migration(migrations.Migration):
    MIGRATE_AFTER_INSTALL = True

    dependencies = [
        ('project', '0047_auto_20211129_0427'),
    ]

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]
