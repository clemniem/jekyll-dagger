## Dagger

### Mindstorm

- to dagger:
	+ Read file
	+ check for section: `<STARTTOKEN> <ENDTOKEN>`
	+ check for tags: `<TAGS>`
	+ create blog entry with template
- it should have an easy init process to know where to put the files. Maybe a config yaml that can be written with interactive `dagger init` or `dagger target <folderPath>`
- it should just take a .md-file and dagger it (e.g. `dagger <file>`)
- it should take a whole folder and use all .md-files within a folder and dagger them `dagger <folder>`
- it should be able to push to the repository to update the site (e.g. `dagger push` or a flag `-p`)
- it should be able to configure files or folders that it automatically checks for updates (e.g.`dagger add <file/folder>` and `dagger all`)

### Problems/Questions

- what happens if section is changed later?
- how to check if file is changed.
- does it need to hold a state (e.g. last time of `dagger all`)
- how should the start and stop token look like
- how should the tags look like


### Layout

```
Usage:
  dagger fly <path> [-p] [-f]
  dagger target <directory>
  dagger add <path>
  dagger all [-p]
  dagger push
  dagger status
  dagger -h | --help
  dagger -v | --version
```

### User Stories


