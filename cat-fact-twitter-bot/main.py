
import base64
import hashlib
import os
import re
import json
import requests
import redis
from requests.auth import AuthBase, HTTPBasicAuth
from requests_oauthlib import OAuth2Session, TokenUpdated
from flask import Flask, request, redirect, session, url_for, render_template