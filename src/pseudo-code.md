
**Project Input:**

- lyric file path
- tone number (optionally as a list?)
- (optional) tone style (obikhod or kievan)
- (optional) output file path
- (optional) emphasis and recit markers
- (optional) syllable separator

**Project Output:**

- Write lyric map file (with lyrics and notes)
- Write master lilypond file with main template plus:
    * import lyric mapping file
    * title/subtitle
    * info (tone and style)
    * verse framework

**Pseudo-code**

```
Read in lyric file
Update main file template with title, call to outfile, etc
Split lyrics into verses
for each verse:
  Read in tone file (for each verse, as needed)
  split lyrics into lines
  for each line:
    split lyrics into syllables
    get correct line from tone ("notes")
    check if number of emph matches in lyrics and noes
    determine if recit is labeled in lyrics
    get recit position idx in tone line
    get list of lyric idx where markers occur
    get list of note idx markers
    start lyr idx = start note idx = 0
    recit phrase = False
    
    # Iterate over phrases
    # Note that phrases end prior to next marker
    while list of lyric idx occurs (looking for EOL):
      end lyr idx = first value in lyric idx markers
      end note idx = idx of next marker of any type
    
      if recit phrase is True:
        combine the appropriate number of lyr syllables using \left{}
        
      else:
    
        if recit is labeled:
          id lyr marker type
          id note marker type
          check marker types match
          remove
          if marker type is recit:
            recit phrase = True
    
        else:
          end note idx = idx of next emph marker
          check if recit happens between start and end note idx
          if so:
            count notes from start to recit (in notes)
            set end lyr idx so numer of syllables match num of notes above
            recit phrase = True
         
        if more lyr syllables than notes:
          add notes (repeat first note of phrase)
        elif more notes than lyr syllables:
          combine notes using tie/slur (from first note of phrase)
        else:
          collapse lists (lyr and notes) into strings (sep with " ")    


      start note idx = end note idx
      start lyr idx = end lyr idx

    collapse phrase (lyr and notes) lists into strings (sep with " ")
    append " \ibar" to end of line
    append strings to relevant list (part/lyric)
    
  for each part & lyric list:
    write prep line to outfile (e.g. sopA = \relative c' {
    write each line to outfile
    write " \endbar }"
    write empty newline
  
  Add new choir staff to main file template

```







