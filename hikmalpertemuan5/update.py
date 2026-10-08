hobbits = {'frodo', 'sam', 'merry', 'pippin'}

dunedain = {'aragorn'}
elf = {'legolas'}
dwarf = {'gimli'}
human = {'boromir'}
maiar = {'gandalf'}

hobbits.update(dunedain, elf, dwarf, human, maiar)

print("hobbits:", hobbits)