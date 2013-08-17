# Inspired by wapex3.py in http://products.wolframalpha.com/docs/Python_Binding_1_1.zip written by derik66@gmail.com
# New feature : Introduced allowed types to distinguish between pod types (for diffrent applications e.g geomatry, trigonomatry, etc.

import wap
from array import array

class InfoProvider:
	
	def searchWolfram(self, q, t):
	
		server = 'http://api.wolframalpha.com/v2/query'
		appid = 'WJ7EUR-77XE8GLY3V'
		
		#allowedTypes = ['', 'Math', 'Percent' ,'FamousMathProblems' ,'theorem', 'Formula', 'MathWorld', 'NamedConstant', 'Character', 'MathWorldClass', 'MathematicalFunctionIdentity']
		allowedTypes = { 'test' : ['','Math'],
						'math':['','Math','Percent'], 
						'numbers':['','Math','NumberTypeQ','ConvertBase'] ,
						'base':['','Math','ConvertBase'], 
						'historic':['','Math','BaseForm'],
						'plot':['','Math','Plot'],
						'algebra':['','Math','Solve', 'Factor', 'Simplify', 'Vectors','QuaternionTimes','FiniteGroup','FiniteGroups','FunctionDomainAndRange',''],
						'calculus':['','Math','D','IntegerSequence','Sum','Product','MathematicalFunctionIdentity','Series','InflectionPoints','AreaBetweenCurves','Residue','Grad','Curl','Discontinuities','Geometry','Cusp','Asymptotes','SaddlePoints','StationaryPoints'],
						'seq':['','Math','IntegerSequence'],
						'geometry':['','Math',"MathematicalFunctionIdentity", "Formula", "People", "Formula", "Geometry", "Graph", "Surface", "Math", "PlaneCurve", "FiniteGroup", "Knot", "Transform", "Polyhedron"],
						'coordinategeometry':['','Math','AreaBetweenCurves','InflectionPoints','Geometry','Cusp','Asymptotes','SaddlePoints','StationaryPoints'],
						'planegeometry':['','Math',"Formula", "Lamina", "PlaneCurve", "People", "Geometry", "Graph"],
						'trigonometry':['','Math',"Factor", "Expand", "Math", "Plot", "MathematicalFunctionIdentity", "FunctionProperties"],
						'geometrictransformations':['','Math','Transform'],
						'numbertheory':['','Math',"NumberTypeQ", "MathematicalFunctionIdentity", "Factor", "Solve"],
						'discretemathematics': ['','Math',"Combinatorics", "MathematicalFunctionIdentity", "CrystallographicSpaceGroup", "CrystalFamily", "Graph", "Lattice", "LatticeSystem", "Ellipsis", "CrystalSystem", "FiniteGroup"],
						'optimization' :['', 'Math',"StationaryPoints", "Maximize", "Minimize", "Extrema"],
						'graphtheory' :['', 'Math', "Graph"],
						'appliedmathematics' :['', 'Math',"Maximize", "Formula", "ControlSystem", "FamousMathGames"],
						'booleanalgebra' :['', 'Math'],
						'settheory' : ['','Math',"SetSymmetricDifference", "Intersection"],
						'probability' : ['', 'Math',"Probability", "Formula"],
						'regressionanalysis' : ['','Math',"DataFit"],
						'statistics': ['','Math',"Probability", "Formula", "DataFit"],
						'aeronautics' : ['','Math',"Formula"],
						'fluidmechanics': ['','Math',"Wood", "Chemical", "Formula"],
						'quantumphysics' :['','Math',"AtomicSpectrum", "Formula", "Element", "LightColor", "FamousPhysicsProblems", "Particle", "People", "Quantity", "PhysicalSystems"],
						'mechanics':['','Math',"Formula", "People", "PhysicalSystems"],
						'thermodynamics' : ['','Math',"ThermodynamicDataRP", "People", "Formula", "PhysicalSystems", "Chemical"],
						'photography' : ['','Math',"DisplayFormat", "Formula"],
						'optics' : ['','Math',"Material", "Formula", "Laser", "Chemical"],
						'nuclearphysics' :['','Math',"Formula", "Chemical", "Element", "Math", "Isotope", "Financial", "Particle", "NuclearReactor", "USCounty", "Mineral", "ParticleStoppingMaterial"],
						'particlephysics' :['','Math',"Country", "Math", "ParticleInteraction", "Particle", "Isotope", "Formula", "ParticleAccelerator"],
						'astrophysics' :['','Math',"Astronomical", "Formula"],
						'electricitymagnetism':['','Math',"Particle", "USEnergyResource", "Country", "Element", "Quantity", "PhysicalSystems", "Formula", "EnergyResource", "USState", "Laser", "LightColor", "People"],
						'physics':['','Math',"Quantity", "People", "Element", "LightColor", "AtomicSpectrum", "ParticleStoppingMaterial", "Formula", "FamousPhysicsProblems", "Particle", "Math", "Isotope", "ParticleInteraction", "Chemical", "PhysicalSystems", "Astronomical"],
						'imageprocessing':['','Math',"Dinosaur", "People", "TelevisionProgram", "City", "Astronomical", "Species", "MusicalInstrument", "Mineral"],
						'computationalsciences'	:['','Math',"Mineral", "MusicalInstrument", "Formula", "TuringMachine", "CellularAutomaton", "ComputationalComplexity", "AlgebraicCode", "Mathematica", "Species"],
						'earthsciences':['','Math',"Earthquake", "Formula", "Mineral", "Formula", "Geogravity", "Geochronology", "EarthImpact", "Tide", "Geodesy", "GeologicalComponentLayer", "City", "Dinosaur", "AtmosphericLayers", "Geomagnetism"],
						'astronomy':['','Math',"Character", "People", "AstronomicalObservatory", "PlanetaryAstronomy", "Constellation", "Country", "Quantity", "Astronomical", "ApolloMission", "MeteorShower", "WikipediaStats", "Formula", "DeepSpaceProbe", "Math", "Chemical", "Satellite"],
						'engineering':['','Math',"Bridge", "Mine", "Alloy", "Chemical", "Formula", "ControlSystem", "ThermodynamicDataRP", "Math", "Country", "WikipediaStats", "Building", "Castle"],
						'materials':['','Math',"Material", "Mineral", "Math", "Stockpile"],
						'webcomputersystems':['','Math',"StringFunction", "Internet", "Characters", "FileFormat", "StringEncoding", "DataTransferDevice", "City", "DisplayFormat", "SingleCharacter", "NotableComputer", "Country", "Formula", "ConvertBase", "USState"],
						'transportation':['','Math',"GasPrice", "Tide", "InternationalTransportation", "DeepSpaceProbe", "Aircraft", "Satellite", "Country", "City", "USState", "Formula", "Astronomical", "Airline", "Math", "WorldDevelopment", "Flight", "Airport", "WikipediaStats"],
						'foodnutrition' :['','Math',"Relocation", "Country", "ExpandedFood", "DietaryReference", "Formula", "City", "Math", "Agriculture", "USCounty"],
						'healthmedicine':['','Math',"Death", "USState", "Chemical", "Mortality", "HealthCare", "Disease", "MedicalTest", "MatterPhase", "Hospital", "HealthIndicator", "Country", "City", "Formula", "Isotope", "Tooth"],
						'datestimes':['','Math',"CalendarEvent", "WeddingAnniversary", "RecurringEvent", "BirthMonth", "EarthImpact", "City", "HistoricalEvent", "Holiday", "TimeZone", "DateDifference", "DateObject", "Quantity", "Plant", "Geochronology", "USState", "Mineral", "DatePlus", "Dinosaur"],
						'unitsmeasures':['','Math',"Element", "KnittingNeedleSize", "ThreadedFasteners", "Math", "Quantity", "DrillBit", "RingSize", "SteelGauge", "WireGauge", "DisplayFormat"],
						'chemistry':['','Math',"Isotope", "Chemical", "ChemicalIntermediate", "Math", "Element", "ChemicalSolutions", "ChemicalProtectingGroups", "MatterPhase", "ChemicalReaction", "ThermodynamicDataRP"],
						'minerals':['','Math',"Country", "FamousGem", "CrystalSystem", "CrystallographicSpaceGroup", "Mineral", "FiniteGroup", "Lattice", "LatticeSystem", "CrystalFamily"],
						'geography':['','Math',"Language", "USState", "River", "NuclearReactor", "River", "Island", "Ocean", "Mountain", "Species", "UnderseaFeature", "Airport", "Internet", "Waterfall", "ZIPCode", "AdministrativeDivision", "Religion", "University", "CongressionalDistrict", "Flight", "USCounty", "USSchoolDistrict", "WikipediaStats", "Country", "MetropolitanArea", "City", "Crime", "MilitaryBase", "Country", "Bridge", "USFairMarketRent", "Airport", "WorldDevelopment", "Hospital", "ACS"],
						'colors':['','Math',"Quantity", "ColorSet", "Color", "Laser", "LightColor", "Species"],
						'music':['','Math',"People", "MusicalInstrument", "Quantity", "Country", "MusicAct", "City", "MusicalKey", "MusicAlbumRelease", "WikipediaStats", "MusicArtistCredit", "MusicWork", "MusicAlbum"],
						'musictheory':['','Math',"Quantity", "MusicalKey", "MusicalInstrument", "WikipediaStats", "People",  "Country", "MusicAct", "City", "MusicAlbumRelease",  "MusicArtistCredit", "MusicWork", "MusicAlbum"],
						'movies':['','Math',"USState", "Country", "AcademyAward", "City", "Movie", "People","Quantity", "MusicalKey", "MusicalInstrument", "WikipediaStats", "People",  "Country", "MusicAct", "City", "MusicAlbumRelease",  "MusicArtistCredit", "MusicWork", "MusicAlbum"],
						'aphorisms':['','Math',],
						'televisionprograms':['','Math',"Holiday", "City", "TelevisionProgram", "TelevisionNetwork"],
						'mythology':['','Math',"AdministrativeDivision", "Country", "City", "Book", "Mythology"],
						'fictionalcharacters':['','Math',"USState", "City", "FictionalCharacter", "WikipediaStats"],
						'education':['','Math',"WikipediaStats", "USState", "Country", "USPrivateSchool", "USPublicSchool", "WorldDevelopment", "USSchoolDistrict", "Library", "University", "Internet", "Probability", "ACS", "City"],
						'orgsearch':['','Math',"City", "WikipediaStats", "USState", "Country", "Internet", "University", "Library","Foundation","WorldDevelopment"],
						'videogames':['','Math',"VideoGameRelease", "VideoGame"],
						'wordpuzzles':['','Math',"Country", "Acronym", "Word"],
						'sports':['','Math',"Lamina", "SportObject", "City", "AdministrativeDivision", "TennisTournament", "NBAPlayer", "Country", "NFLPlayer", "GolfTournament", "WikipediaStats", "USState", "TennisPlayer", "People", "Acronym", "Stadium", "Olympic"],
						'gamesofchance':['','Math',"Probability"],
						}
		waeo = wap.WolframAlphaEngine(appid, server)

		waeq = wap.WolframAlphaQuery(q, appid)
		waeq.ToURL()
		waeq.AddPodScanner('Mathematics')
		query = waeq.Query

		print 'Server=' + server + ' :: ', query

		result = waeo.PerformQuery(query)

		waeqr = wap.WolframAlphaQueryResult(result)
		datatypes = waeqr.DataTypes()[0].split(',')
		#print '\n', type(datatypes), 'datatypes=', datatypes
		rs = list(set(datatypes) & set(allowedTypes[t]))
		if(len(rs) == 0):
			return {'status':'fail', 'newDt' : datatypes}


		pods = waeqr.Pods()
		if len(pods) == 0:
			didyoumeans = waeqr.DidYouMeans()
			#print 'DidYouMean=', didyoumeans
			if(len(didyoumeans[0]) == 1): 
				return {'status' :'fail'}
		  
			didYouMeanArray = []
			for didyoumean in didyoumeans[0][1:]:
				didYouMeanArray.append(didyoumean[1])
			return {'status':'dum','didyoumeans':didYouMeanArray}
		

		result = {'status' : 'success', 'dt':datatypes}
		data = {}

		for pod in pods:
		  waep = wap.Pod(pod)
		  iserror = waep.IsError()
		  numsubpods = waep.NumSubpods()
		  title = waep.Title()
		  #print '\n' , title[0]
		  subpods = waep.Subpods()
		  for subpod in subpods:
			waesp = wap.Subpod(subpod)
			plaintext = waesp.Plaintext()
			if plaintext[0] == '(requires interactivity)':
				continue
			img = waesp.Img()
			imgData = dict((x, y) for x, y in img[0])
			#print '\n', img[0][0][1]
			data[title[0]] = imgData['src']

		result['data'] = data
		return result
