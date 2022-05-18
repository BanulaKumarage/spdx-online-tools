# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2017 Rohit Lodha
# Copyright (c) 2017 Rohit Lodha
# SPDX-License-Identifier: Apache-2.0
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.urls import path

from api import views

urlpatterns = [
    path('validate/', views.validate, name='validate-api'),
    path('convert/', views.convert, name='convert-api'),
    path('compare/', views.compare, name='compare-api'),
    path('check_license/', views.check_license, name='check_license-api'),
    path('submit_license/', views.submit_license, name='submit_license-api'),
]
