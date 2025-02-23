# Define a list of notes
notes = [:c4, :e4, :g4, :c5]

# Loop through each note and play it
notes.each do |note|
  play note
  sleep 0.5 # Wait for half a second before playing the next note
end

# Play a drum beat in the background
live_loop :drums do
  sample :bd_haus, rate: 1
  sleep 1
end