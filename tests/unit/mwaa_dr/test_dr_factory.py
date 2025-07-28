# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from unittest.mock import patch
from sure import expect
from mwaa_dr import dr_factory
import importlib


class TestDRFactory:
    def test_factory_on_airflow_v_2_9_2(self):
        with patch("airflow.version.version", "2.9.2"):
            importlib.reload(dr_factory)
            from mwaa_dr.v_2_9.dr_factory import DRFactory_2_9

            expect(dr_factory.DRFactory).to.equal(DRFactory_2_9)

    def test_factory_on_airflow_v_2_10_3(self):
        with patch("airflow.version.version", "2.10.3"):
            importlib.reload(dr_factory)
            from mwaa_dr.v_2_10.dr_factory import DRFactory_2_10

            expect(dr_factory.DRFactory).to.equal(DRFactory_2_10)

    def test_factory_on_airflow_invalid_version(self):
        with patch("airflow.version.version", "-1"):
            importlib.reload(dr_factory)
            from mwaa_dr.framework.factory.default_dag_factory import DefaultDagFactory

            expect(dr_factory.DRFactory).to.equal(DefaultDagFactory)
