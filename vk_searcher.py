#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import vk
from re import search
from pyshorteners import Shortener
from common import uformat
from config import *


class VkMusicSearcher:
    def __init__(self, vk_api_token, google_api_token):
        __session = vk.Session(access_token=vk_api_token)
        __google_api_token = google_api_token
        self.vk_api = vk.API(__session)
        self.shortener = Shortener('Google', api_key=__google_api_token)
        # result_count <= 9
        self.result_count = 9

    def print_menu(self, local_count):
        print "\nMenu:"
        print "-> Next page - [n]"
        print "-> Get info about audio - [1-{0}]".format(local_count - 1)
        print "-> Exit menu - [q]"

    def search_music(self, query):
        offset = 0

        for counter in range(10):
            query_result = self.vk_api.audio.search(q=query, count=self.result_count, offset=offset)
            local_count = len(query_result)
            query_result.pop(0)
            music_counter = 1
            for q in query_result:
                print "{0}) {1}\t: {2}".format(music_counter, uformat(q["artist"]), uformat(q["title"]))
                music_counter += 1

            self.print_menu(local_count)
            option = raw_input("\nInput option: ").lower()
            if option == "n":
                offset += local_count
                continue
            elif option == "q":
                break
            elif search(r"^[1-{0}]$".format(local_count - 1), option):
                music_number = int(option)
                music_info = query_result[music_number - 1]
                print "----> {0} : {1} | {2}\n".format(uformat(music_info["artist"]), uformat(music_info["title"]),
                                                       self.shortener.short(music_info["url"]))
            else:
                continue

if __name__ == "__main__":
    v = VkMusicSearcher(VK_TOKEN, GOOGLE_TOKEN)
    while True:
        try:
            query = raw_input("\nInput audio name: ")
        except KeyboardInterrupt as e:
            print ""
            exit(0)
        if query == "q":
            break
        v.search_music(query)
