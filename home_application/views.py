# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context
from django.http import HttpResponse
from blueking.component.shortcuts import get_client_by_request
import json

def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def helloworld(request):
    return render_mako_context(request, '/home_application/helloworld.html')

def esb(request):
    client=get_client_by_request(request)
    #data = client.cc.search_business()
    
    #data = client.bk_login.get_all_users()
    #data = client.cc.search_host()
    kwargs = {"bk_host_id":1}
    data = client.cc.get_host_base_info(kwargs)
    result = json.dumps(data,ensure_ascii=False)
    return HttpResponse(result)

def sendmail(request):
    client=get_client_by_request(request)
    kwargs = {
        "bk_app_code":"cyctest1",
        "bk_app_secret":"934c2047-9414-4ce0-924e-8f62e69d8944",
        "receiver": "13302803028@189.cn",
        "sender": "836963281@qq.com",
        "title": "This is a Test",
        "content": "<html>Welcome to Blueking</html>",
    }
    data=client.cmsi.send_mail(kwargs)
    result = json.dumps(data,ensure_ascii=False)
    return HttpResponse(result)