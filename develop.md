# jagger

### Mindstorm

- to jagger:
	+ Read file
	+ check for section: `<STARTTOKEN> <ENDTOKEN>`
	+ check for tags: `<TAGS>`
	+ create blog entry with template
- it should have an easy init process to know where to put the files. Maybe a config yaml that can be written with interactive `jagger init` or `jagger target <folderPath>`
- it should just take a .md-file and jagger it (e.g. `jagger <file>`)
- it should take a whole folder and use all .md-files within a folder and jagger them `jagger <folder>`
- it should be able to push to the repository to update the site (e.g. `jagger push` or a flag `-p`)
- it should be able to configure files or folders that it automatically checks for updates (e.g.`jagger add <file/folder>` and `jagger all`)

#### Problems/Questions

- what happens if section is changed later?
- how to check if file is changed.
- does it need to hold a state (e.g. last time of `jagger all`)
- how should the start and stop token look like
- how should the tags look like


#### Layout

```
Usage:
  jagger fly <path> [-p] [-f]
  jagger target <directory>
  jagger add <path>
  jagger all [-p]
  jagger push
  jagger status
  jagger -h | --help
  jagger -v | --version
```

#### User Stories


