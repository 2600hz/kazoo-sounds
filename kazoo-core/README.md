# Kazoo Core Media

## Importing prompts for a language

This will import all prompts for a given language.  Depending on the version or install source your path to the media files may differ.

```
sup whistle_media_maintenance import_prompts /opt/kazoo/media/prompts/en/us/ en-us
sup whistle_media_maintenance import_prompts /opt/kazoo/media/prompts/fr/ca/ fr-ca
```

## Importing individual prompts

Create the media files one by one in BigCouch like so..

```
sup whistle_media_maintenance import_prompt /opt/kazoo/system_media/dir-enter_person_lastname.wav en-us
```

## Notes

* Kazoo does not read the files from disk, you must import a new prompt before it becomes available (and flush the appropriate caches).
* This is documented here for convenience, but more information is available in the docs.
* If you run the script over and over it will overwrite the meta records and media already in bigcouch.
* You must(should) install English "en-us" *plus* other languages if you want to avoid troubles and save debugging time.  Kazoo will eventually always fallback to English if everythign else fails.
* Please note the media_import tool is depreciated and specifically is not multi language aware.  Use it at your own risk in 3.18 and beyond.
* If anyone needs help with making new simplistic "language packs" you can contact wlloyd@stormqloud.ca or the usual sources!

