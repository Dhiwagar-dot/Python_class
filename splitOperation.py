inputdata = """Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto Europa Titan Ganymede Callisto Io Triton Sun Sirius Betelgeuse Rigel Vega Polaris Aldebaran Antares Proxima Centauri Alpha Centauri Barnard's Star Arcturus Deneb Altair Spica Milky Way Andromeda Whirlpool Galaxy Sombrero Galaxy Triangulum Galaxy Large Magellanic Cloud Small Magellanic Cloud Orion Nebula Crab Nebula Eagle Nebula Helix Nebula Ring Nebula Lagoon Nebula Carina Nebula Tarantula Nebula Apollo Voyager Hubble Sputnik Chandrayaan Mangalyaan Artemis Cassini Galileo Kepler Juno New Horizons Curiosity Perseverance Insight Orion Ursa Major Ursa Minor Cassiopeia Leo Taurus Gemini Scorpio Sagittarius Aquarius Pisces Capricorn Aries Libra Virgo Black Hole Supernova Quasar Pulsar Asteroid Comet Meteor Meteorite Nebula Galaxy Orbit Gravity Light Year Cosmic Ray Event Horizon Space-Time Dark Matter Dark Energy Big Bang Solar Wind Exoplanet Red Giant White Dwarf Neutron Star Accretion Disk""" 
code = inputdata.split()
tepmlate = {
    "id":"1",
    "enrolled": "yes",
    "isActive": True
}

result = []
for code in code:
    value = {"name": code.strip()}  # Create a dictionary with the name key and the stripped code as its value
    tepmlate.update(value)  # Update the template with the new name value
    result.append(tepmlate.copy())  # Append a copy of the updated template to the result list
print(result)
inputdata = """Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto Europa Titan Ganymede Callisto Io Triton Sun Sirius Betelgeuse Rigel Vega Polaris Aldebaran Antares Proxima Centauri Alpha Centauri Barnard's Star Arcturus Deneb Altair Spica Milky Way Andromeda Whirlpool Galaxy Sombrero Galaxy Triangulum Galaxy Large Magellanic Cloud Small Magellanic Cloud Orion Nebula Crab Nebula Eagle Nebula Helix Nebula Ring Nebula Lagoon Nebula Carina Nebula Tarantula Nebula Apollo Voyager Hubble Sputnik Chandrayaan Mangalyaan Artemis Cassini Galileo Kepler Juno New Horizons Curiosity Perseverance Insight Orion Ursa Major Ursa Minor Cassiopeia Leo Taurus Gemini Scorpio Sagittarius Aquarius Pisces Capricorn Aries Libra Virgo Black Hole Supernova Quasar Pulsar Asteroid Comet Meteor Meteorite Nebula Galaxy Orbit Gravity Light Year Cosmic Ray Event Horizon Space-Time Dark Matter Dark Energy Big Bang Solar Wind Exoplanet Red Giant White Dwarf Neutron Star Accretion Disk"""

inputdata1 = """Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Europa, Titan, Ganymede, Callisto, Io, Triton, Sun, Sirius, Betelgeuse, Rigel, Vega, Polaris, Aldebaran, Antares, Proxima Centauri, Alpha Centauri, Barnard's Star, Arcturus, Deneb, Altair, Spica, Milky Way, Andromeda, Whirlpool Galaxy, Sombrero Galaxy, Triangulum Galaxy, Large Magellanic Cloud, Small Magellanic Cloud, Orion Nebula, Crab Nebula, Eagle Nebula, Helix Nebula, Ring Nebula, Lagoon Nebula, Carina Nebula, Tarantula Nebula, Apollo, Voyager, Hubble, Sputnik, Chandrayaan, Mangalyaan, Artemis, Cassini, Galileo, Kepler, Juno, New Horizons, Curiosity, Perseverance, Insight, Orion, Ursa Major, Ursa Minor, Cassiopeia, Leo, Taurus, Gemini, Scorpio, Sagittarius, Aquarius, Pisces, Capricorn, Aries, Libra, Virgo, Black Hole, Supernova, Quasar, Pulsar, Asteroid, Comet, Meteor, Meteorite, Nebula, Galaxy, Orbit, Gravity, Light Year, Cosmic Ray, Event Horizon, Space-Time, Dark Matter, Dark Energy, Big Bang, Solar Wind, Exoplanet, Red Giant, White Dwarf, Neutron Star, Accretion Disk"""

# Use comma-based split so multi-word names stay together.
names = [item.strip() for item in inputdata1.split(",") if item.strip()]

template = {
    "id": "1",
    "enrolled": "yes",
    "isActive": True,
}

result = []
for name in names:
    item = template.copy()
    item["name"] = name
    result.append(item)

# print(result)

words =["dhiwagar", "python", "programming", "language", "split", "operation"]
joined_string = " ".join(words)
print(joined_string)

content= " java is a high-level, interpreted programming language known for its readability and versatility. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python's extensive standard library and large ecosystem of third-party packages make it a popular choice for web development, data analysis, artificial intelligence, scientific computing, and more. With its simple syntax and powerful features, Python continues to be a favorite among developers worldwide."
sentences = content.replace("java", "Python")
print(sentences)

name= "dhiwagar"
name= name.upper()
print(name)
