#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import vk
from os import path, makedirs
from urllib import urlopen
from urllib2 import HTTPError
from common import uformat
from config import *
from multithreading import printf, Threadpool
from argparse import ArgumentParser


class VkMusicDownloader:
    def __init__(self, vk_api_token, user_id, out_folder, thread_count=10):
        __session = vk.Session(access_token=vk_api_token)
        self.vk_api = vk.API(__session)
        self.user_id = user_id
        self.out_folder = out_folder
        self.thread_count = thread_count

    def get_dict_audio(self):
        audio_info = self.vk_api.audio.get(owner_id=self.user_id)
        audio_info.pop(0)
        dict_audio = {}
        for audio in audio_info:
            audio_name = "{0} - {1}".format(uformat(audio["artist"]), uformat(audio["title"]))
            audio_url = audio['url']
            if audio_name not in dict_audio:
                dict_audio[audio_name] = audio_url
        return dict_audio

    @staticmethod
    def download_file(out_folder, file_name=None, url=None):
        resource = urlopen(url)
        full_path = path.join(out_folder, "{0}.mp3".format(file_name))
        with open(full_path, "wb") as output:
            output.write(resource.read())

    def make_out_folder(self):
        if not path.exists(self.out_folder):
            makedirs(self.out_folder)

    def worker(self, name, url):
        try:
            self.download_file(self.out_folder, name, url)
        except HTTPError as e:
            printf("[-] : {0} - Download failed : {1}".format(name, e))
        else:
            printf("[+] : {0} - Download successful".format(name))

    def download_music(self):
        self.make_out_folder()
        try:
            user_audio = self.get_dict_audio()
        except Exception as e:
            printf("Probably audio is hidden: {0}".format(e))
            exit(1)

        printf("Count audio : {0}".format(len(user_audio)))
        printf("Please, wait...\n")

        pool = Threadpool(self.thread_count)
        for name, url in user_audio.items():
            pool.add_task(self.worker, name, url)
        pool.wait_completion()


def get_args():
    parser = ArgumentParser(description="Script for download audio from vk.com")
    parser.add_argument("-i", "--id", help='User id', type=str, required=True)
    parser.add_argument("-o", "--out", help="Output folder with audio files", type=str, required=True)
    parser.add_argument("-j", "--job", help="Setting maximum of threads", type=int, required=False, default=10)
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    d = VkMusicDownloader(VK_TOKEN, args.id, args.out, args.job)
    d.download_music()
