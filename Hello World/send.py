# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:11:03 2020

@author: TechieMak
"""
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key = 'hello',
                      body='Sent From Producer...')

print("[x] Sent From 'Producer...'")

connection.close()
