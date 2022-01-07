from roleEnums import Role
from typeEnums import Type

# Data taken from https://www.comp.nus.edu.sg/about/depts/cs/faculty/

'''
pokedex = {
    chatId : {
        profs
    }
}
'''

pokedex = {}

'''
Database storing all the profs
'''


profs = {
	'Lee Wee Sun' : {
         	'ID' : 1,
		'Subtitle' : Role.head,
		'Description' : 'He has been an area chair for machine learning and AI conferences.',
		'Type' : [Type.ai],
		'Location' : 'COM1-03-10',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/leews.jpg',
        'isFound' : False
	},
 	'Anthony Tung' : {
         	'ID' : 2,
		'Subtitle' : Role.dpHead1,
		'Description' : 'He received both his B.Sc.(2nd Class Honour) and M.Sc. in computer sciences from NUS and Ph.D. in computer sciences from Simon Fraser University.',
		'Type' : [Type.database],
		'Location' : 'COM1-03-21 ',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/atung.jpg',
        'isFound' : False
	},
  	'Chan Mun Choon' : {
         	'ID' : 3,
		'Subtitle' : Role.dpHead2,
		'Description' : 'He has graduated 16 PhD students, served as the Associate Editor of IEEE Transaction on Mobile Computing, published more than 100 conference/journal papers and has been awarded 7 US patents.',
		'Type' : [Type.systemsAndNetworking],
		'Location' : 'COM2-04-17',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/chanmc.jpg',
        'isFound' : False
	},
   	'Damith Chatura Rajapakse' : {
         	'ID' : 4,
		'Subtitle' : Role.dpHead3,
		'Description' : 'He has authored or co-authored several books and is the founder of a number of education related software projects benefitting thousands of students and instructors around the world.',
		'Type' : [Type.programmingLanguagesAndSWE],
		'Location' : 'COM2-02-57',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/damithch.jpg',
        'isFound' : False
	},
       	'Boyd Anderson' : {
         	'ID' : 5,
		'Subtitle' : Role.lecturer,
		'Description' : 'His doctorate research focused on human gait measurement and analysis using Ultra Wideband sensor systems.',
		'Type' : [],
		'Location' : 'COM2-03-26',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/boyd.jpg',
        'isFound' : False
	},       	
        'Hugh Anderson' : {
         	'ID' : 6,
		'Subtitle' : Role.assocProf,
		'Description' : 'These days he spends a lot of time developing embedded systems software for wearable sensors.',
		'Type' : [Type.programmingLanguagesAndSWE, Type.security, Type.systemsAndNetworking],
		'Location' : 'COM2-03-24',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/hugh.jpg',
        'isFound' : False
	},
        'Arnab Bhattacharya' : {
         	'ID' : 7,
		'Subtitle' : Role.assisProf,
		'Description' : "He is Associate Editor of Computers and Electrical Engineering Journal, Elsevier and Vice President of International Researchers club, Singapore.",
		'Type' : [Type.systemsAndNetworking, Type.media],
		'Location' : 'COM2-04-26',
		'Image' :'https://www.comp.nus.edu.sg/stfphotos/arnab.jpg',
        'isFound' : False
	},
        'Anand Bhojan' : {
         	'ID' : 8,
		'Subtitle' : Role.seniorLect,
		'Description' : "His work has been presented at several premier international conferences and journals. He is the recipient of an NRF Fellowship for AI and an Amazon Research Award.",
		'Type' : [Type.algoAndTheory, Type.ai],
		'Location' : 'COM2-03-44',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/bhojan.jpg',
        'isFound' : False
	},
        'Stephane Bressan' : {
         	'ID' : 9,
		'Subtitle' : Role.assocProf,
		'Description' : "He is Affiliate Professor at NUS Business Analytics Centre and Faculty Affiliate at NUS Institute of Data Science",
		'Type' : [Type.database],
		'Location' : 'COM1-03-20',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/steph.jpg',
        'isFound' : False
	},
        'Cristina CARBUNARU' : {
         	'ID' : 10,
		'Subtitle' : Role.seniorLect,
		'Description' : "Her research interests include analytic modeling and performance analysis for distributed systems.",
		'Type' : [],
		'Location' : 'COM2-02-07',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/ccris.jpg',
        'isFound' : False
	},
        'Trevor Erik Carlson' : {
         	'ID' : 11,
		'Subtitle' : Role.assisProf,
		'Description' : "Through the use of fast bottleneck analysis and simulation, his goal is to improve both performance and efficiency of next-generation processors. ",
		'Type' : [Type.systemsAndNetworking],
		'Location' : 'COM2-03-43',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/tcarlson.jpg',
        'isFound' : False
	},
        'Chan Chee Yong' : {
         	'ID' : 12,
		'Subtitle' : Role.assocProf,
		'Description' : "His research has been published in ACM SIGMOD, VLDB, and IEEE ICDE Conferences. He is currently an Associate Editor of ACM SIGMOD Record and VLDB Journal.",
		'Type' : [Type.database],
		'Location' : 'COM1-03-24',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/chancy.jpg',
        'isFound' : False
	},
        'CHANG Ee Chien' : {
         	'ID' : 13,
		'Subtitle' : Role.assocProf,
		'Description' : "More recently, he has been investigating issues in data privacy and cloud security. He is a lead-PI of the recently established National Cybersecurity R&D Laboratory in Singapore.",
		'Type' : [Type.systemsAndNetworking, Type.media, Type.security],
		'Location' : 'COM2-04-30',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/changec.jpg',
        'isFound' : False
	},
        'Alan Cheng' : {
         	'ID' : 14,
		'Subtitle' : Role.seniorLect,
		'Description' : "His interests include computational geometry, parametric surfaces, computer graphics, visualization.",
		'Type' : [Type.media],
		'Location' : 'AS6-05-03',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/hcheng.jpg',
        'isFound' : False
	},
        'Henry Chia' : {
         	'ID' : 15,
		'Subtitle' : Role.seniorLect,
		'Description' : "Henry believes that every student must be delicately primed as the beneficiary; they must sense that a teacher teaches, not because he can, but because he cares.",
		'Type' : [],
		'Location' : 'COM2-03-10',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/hchia.jpg',
        'isFound' : False
	},
        'Chua Tat Seng' : {
         	'ID' : 16,
		'Subtitle' : Role.chairProf,
		'Description' : "He has organized and served as program committee member of numerous international conferences in the areas of computer graphics, multimedia and text processing",
		'Type' : [Type.media],
		'Location' : 'AS6-05-08',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/chuats.jpg',
        'isFound' : False
	},
        'Seth Lewis Gilbert' : {
         	'ID' : 17,
		'Subtitle' : Role.deanChairAssocProf,
		'Description' : "My research focuses on algorithms for large-scale distributed systems, with a particular interest in issues of scalability and fault-tolerance.",
		'Type' : [Type.systemsAndNetworking, Type.algoAndTheory],
		'Location' : 'COM2-03-23',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/gilbert.jpg',
        'isFound' : False
	},
        'Steven Halim' : {
         	'ID' : 18,
		'Subtitle' : Role.seniorLect,
		'Description' : "Apparently his students like to be tortured with heavy and tedious modules of his. He is currently placed on the ATEA Honour Roll (in 2020), i.e., 'banned from competing within University' until AY2025/26. ",
		'Type' : [Type.algoAndTheory],
		'Location' : 'COM2-03-37',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/stevenha.jpg',
        'isFound' : False
	},
	'He Bingsheng' : {
         	'ID' : 19,
		'Subtitle' : Role.assocProf,
		'Description' : "Bingsheng has served as a PC member for international conferences in databases, cloud computing and parallel and distributed systems.",
		'Type' : [Type.systemsAndNetworking, Type.database],
		'Location' : 'COM2-03-21',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/hebs.jpg',
        'isFound' : False
	},
        'Martin Henz' : {
         	'ID' : 20,
		'Subtitle' : Role.assocProf,
		'Description' : "With his NUS colleagues, he has scaled the experiential course CS1101S (computer science introduction) from 48 students in 2012 to 670 students in 2021.",
		'Type' : [Type.ai, Type.programmingLanguagesAndSWE],
		'Location' : 'COM2-03-51',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/henz.jpg',
        'isFound' : False
	},
        'Bryan Hooi' : {
         	'ID' : 21,
		'Subtitle' : Role.assisProf,
		'Description' : "His research interests include machine learning, graph mining, anomaly detection, spatiotemporal data, and biomedical applications of AI.",
		'Type' : [Type.ai, Type.database],
		'Location' : 'COM2-03-15',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/bhooi.jpg',
        'isFound' : False
	},
        'David Hsu' : {
         	'ID' : 22,
		'Subtitle' : Role.proChairProf,
		'Description' : "In recent years, he has been working on robot planning and learning under uncertainty and human-robot collaboration.",
		'Type' : [Type.ai],
		'Location' : 'COM2-03-52',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/dyhsu.jpg',
        'isFound' : False
	},
        'Wynne Hsu' : {
         	'ID' : 23,
		'Subtitle' : Role.proChairProf,
		'Description' : "Her research interests include: data analytics in the context of social networks, machine learning, as well as retina image analysis.",
		'Type' : [Type.ai, Type.database, Type.compBio],
		'Location' : 'COM2-03-05',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/whsu.jpg',
        'isFound' : False
	},
        'Huang Zhiyong' : {
         	'ID' : 24,
		'Subtitle' : Role.assocProf,
		'Description' : "He is a Senior Member of ACM and IEEE, and a Pioneer Member of ACM SIGGRAPH and Chair of Singapore ACM SIGGRAPH Chapter.",
		'Type' : [Type.media],
		'Location' : 'AS6-05-11',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/huangzy.jpg',
        'isFound' : False
	},
        'Joxan Jaffar' : {
         	'ID' : 25,
		'Subtitle' : Role.prof,
		'Description' : "His current research tool Tracer-X performs dynamic symbolic execution with interpolation, which supports his analysis algorithms for quantitative analysis, memory usage, and string constraint reasoning.",
		'Type' : [Type.programmingLanguagesAndSWE, Type.algoAndTheory],
		'Location' : 'COM1-03-11',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/joxan.jpg',
        'isFound' : False
	},
        'Sanjay Jain' : {
         	'ID' : 26,
		'Subtitle' : Role.proChairProf,
		'Description' : "His research work has been published in various journals such as Journal of Computer and System Sciences, Information and Computation, Theoretical Computer Science, Siam Journal of Computation, and Annals of Pure and Applied Logic, etc",
		'Type' : [Type.algoAndTheory],
		'Location' : 'COM2-03-59',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/sanjay.jpg',
        'isFound' : False
	},
        'Djordje Jevdjic' : {
         	'ID' : 27,
		'Subtitle' : Role.assisProf,
		'Description' : "During his stay at Microsoft, Djordje created the first fully automated pipeline for encoding and decoding data to and from DNA, and created an efficient and distributed error analysis pipeline running on Microsoft Azure, all of which are extensively used in production at Microsoft.",
		'Type' : [Type.systemsAndNetworking, Type.compBio, Type.database],
		'Location' : 'COM2-03-34',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/jevdjic.jpg',
        'isFound' : False
	},
        'Kan Min Yen' : {
         	'ID' : 28,
		'Subtitle' : Role.assocProf,
		'Description' : "Some of his specific projects include work in the areas of scientific discourse analysis, full-text literature mining, machine translation and applied text summarization.",
		'Type' : [Type.ai, Type.media],
		'Location' : 'AS6-05-12',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/kanmy.jpg',
        'isFound' : False
	},
        'Mohan Kankanhalli' : {
         	'ID' : 29,
		'Subtitle' : Role.proChairProf,
		'Description' : "He directs the SeSaMe (Sensor-enhanced Social Media) Centre which does fundamental exploration of social cyber-physical systems which has applications in social sensing, sensor analytics and smart systems.",
		'Type' : [Type.media, Type.security],
		'Location' : 'AS6-05-06/COM1-03-33',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/mohan.jpg',
        'isFound' : False
	},
        'Khoo Siau Cheng' : {
         	'ID' : 30,
		'Subtitle' : Role.assocProf,
		'Description' : "He has abundant knowledge in inferring of semantic attributes for code and in applying sound and optimized code search techniques. He has also applied advanced programming language theories to the design and implementation of a domain-specific language that helps investors analyze financial data",
		'Type' : [Type.programmingLanguagesAndSWE],
		'Location' : 'COM2-04-11',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/khoosc.jpg',
        'isFound' : False
	},
        'Lee Gim Hee' : {
         	'ID' : 31,
		'Subtitle' : Role.assisProf,
		'Description' : "He heads the Computer Vision and Robotic Perception (CVRP) Laboratory.",
		'Type' : [Type.ai, Type.media],
		'Location' : 'COM2-03-54',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/leegh.jpg',
        'isFound' : False
	},
        'Lee Mong Li' : {
         	'ID' : 32,
		'Subtitle' : Role.prof,
		'Description' : "She is a co-inventor of an AI system that uses deep learning to screen for major eye conditions (diabetic retinopathy, glaucoma suspect and age-related macular degeneration) from retinal images.",
		'Type' : [Type.compBio, Type.database],
		'Location' : 'COM2-03-06',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/leeml.jpg',
        'isFound' : False
	},
        'Ben Leong' : {
         	'ID' : 33,
		'Subtitle' : Role.assocProf,
		'Description' : "He currently leads a team of 20 full stack software engineers in the development of modern software systems for MOE using modern technologies like Ruby on Rails, Golang, React, Docker and Kubernetes.",
		'Type' : [Type.systemsAndNetworking],
		'Location' : 'COM2-03-20',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/bleong.jpg',
        'isFound' : False
	},
        'Leong Hon Wai' : {
         	'ID' : 34,
		'Subtitle' : Role.assocProf,
		'Description' : "He pioneered many things in NUS (and received many arrows on his back) -- first to give an 'Open Book' exam, first to give a 'Take-Home' exam, establishing the 'practical examinations' for introductory programming courses.",
		'Type' : [Type.algoAndTheory, Type.compBio],
		'Location' : 'COM1-03-17',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/leonghw.jpg',
        'isFound' : False
	},
        'Leong Tze Yun' : {
         	'ID' : 35,
		'Subtitle' : Role.prof,
		'Description' : "With both academic background and business experience, she has contributed to panels and committees that advice on R&D directions and education in Computer Science, Artificial Intelligence and Health Informatics in Singapore and abroad. ",
		'Type' : [Type.ai],
		'Location' : 'COM2-03-53',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/leongty.jpg',
        'isFound' : False
	},
        'Leong Wai Kay' : {
         	'ID' : 36,
		'Subtitle' : Role.lecturer,
		'Description' : "He is currently teaching undergraduate courses in programming methodology, and software engineering on iOS platform.",
		'Type' : [],
		'Location' : 'COM2-02-11',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/leongwai.jpg',
        'isFound' : False
	},
        'Leow Wee Kheng' : {
         	'ID' : 37,
		'Subtitle' : Role.assocProf,
		'Description' : "He heads the Computer Vision and Robotic Perception (CVRP) Laboratory.",
		'Type' : [Type.algoAndTheory, Type.media],
		'Location' : 'AS6-05-07',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/leegh.jpg',
        'isFound' : False
	},
        'Liang Zhenkai' : {
         	'ID' : 38,
		'Subtitle' : Role.assocProf,
		'Description' : " He has been publishing high-impact papers in top security and software engineering conferences, and has won several best paper awards.",
		'Type' : [Type.security, Type.systemsAndNetworking],
		'Location' : 'COM1-03-16',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/liangzk.jpg',
        'isFound' : False
	},
        'Brian Lim' : {
         	'ID' : 39,
		'Subtitle' : Role.assisProf,
		'Description' : "He leads the NUS Ubicomp Lab focusing on research on ubiquitous computing, human-computer interaction, machine learning and explainable artificial intelligence for user-centric and trustworthy systems",
		'Type' : [Type.media],
		'Location' : 'COM2-03-49',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/brianlim.jpg',
        'isFound' : False
	},
        'Ling Tok Wang' : {
         	'ID' : 40,
		'Subtitle' : Role.prof,
		'Description' : "He serves/served on the steering committees of 5 international conferences, namely ER, DASFAA, DOOD, HSI, and BigComp.",
		'Type' : [Type.database],
		'Location' : 'COM2-03-01',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/lingtw.jpg',
        'isFound' : False
	},
        'Low Kian Hsiang' : {
         	'ID' : 41,
		'Subtitle' : Role.assocProf,
		'Description' : "He has also served as associate editors, area chairs and program committee members, and reviewers for premier AI (specifically, multiagent systems, AI planning, robotics, machine learning) conferences and journals.",
		'Type' : [Type.ai],
		'Location' : 'COM2-02-58',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/lowkh.jpg',
        'isFound' : False
	},
        'Low Kok Lim' : {
         	'ID' : 42,
		'Subtitle' : Role.seniorLect,
		'Description' : "His research in this has produced interesting methods to automate the design of various types of artistic papercraft.",
		'Type' : [Type.media],
		'Location' : 'AS6-04-09',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/lowkl.jpg',
        'isFound' : False
	},
        'Richard MA' : {
         	'ID' : 43,
		'Subtitle' : Role.assocProf,
		'Description' : "He leads the Systems, Analytics, Networks, Economics (SANE) group, which develops cloud-based data systems and performance models/analyses of network systems.",
		'Type' : [Type.systemsAndNetworking],
		'Location' : 'COM2-04-27',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/tbma.jpg',
    'isFound' : False
	},
        'Kuldeep S. Meel' : {
         	'ID' : 44,
		'Subtitle' : Role.presidentialYoungProf,
		'Description' : "The broader goal of his research is to advance artificial intelligence techniques, which utilize ubiquity of data and formal methods, to enable computing to deal with increasingly uncertain real-world environments.",
		'Type' : [Type.ai, Type.algoAndTheory, Type.programmingLanguagesAndSWE],
		'Location' : 'COM2-03-41',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/meel_2.jpg',
    'isFound' : False
	},
        'Tulika Mitra' : {
         	'ID' : 45,
		'Subtitle' : Role.proChairProf,
		'Description' : "She has served in the organizing and program committees of almost all major conferences in the embedded systems, real-time systems, and design automation domain.",
		'Type' : [Type.systemsAndNetworking],
		'Location' : 'COM2-03-08',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/tulika.jpg',
    'isFound' : False
	},
        'Akshay Narayan' : {
         	'ID' : 46,
		'Subtitle' : Role.lecturer,
		'Description' : " His current research is on transfer learning in reinforcement learning.",
		'Type' : [Type.ai],
		'Location' : 'COM2-02-03',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/anarayan.jpg',
    'isFound' : False
	},
        'NG Hwee Tou' : {
         	'ID' : 47,
		'Subtitle' : Role.proChairProf,
		'Description' : "He is a Fellow of the Association for Computational Linguistics (ACL).",
		'Type' : [Type.ai, Type.media],
		'Location' : 'AS6-05-16',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/nght.jpg',
    'isFound' : False
	},
        'Ng Teck Khim' : {
         	'ID' : 48,
		'Subtitle' : Role.assocProf,
		'Description' : "He was the Head of Signal Processing Lab, DSO National Laboratories Singapore. His lab was doing image processing, computer vision and audio processing research for military applications.",
		'Type' : [Type.media],
		'Location' : 'COM2-03-28',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/ngtk.jpg',
    'isFound' : False
	},
        'Ooi Wei Tsang' : {
         	'ID' : 49,
		'Subtitle' : Role.assocProf,
		'Description' : "He is keen in building multimedia systems that contributes towards better wellness and healthcare for all.",
		'Type' : [Type.media],
		'Location' : 'AS6-05-14',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/ooiwt.jpg',
    'isFound' : False
	},
        'PEH Li Shiuan' : {
         	'ID' : 50,
		'Subtitle' : Role.proChairProf,
		'Description' : " She received the IEEE Fellow in 2017, NRF Returning Singaporean Scientist Award in 2016, ACM Distinguished Scientist Award in 2011, MICRO Hall of Fame in 2011, CRA Anita Borg Early Career Award in 2007, Sloan Research Fellowship in 2006, and the NSF CAREER award in 2003.",
		'Type' : [Type.systemsAndNetworking],
		'Location' : 'AS6-04-05',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/peh.jpg',
    'isFound' : False
	}, 
	'Abhik Roychoudhury' : {
         	'ID' : 51,
		'Subtitle' : Role.proChairProf,
		'Description' : "His present research projects are on machine learning security, decentralized systems, privacy and harware architectures for security.",
		'Type' : [Type.programmingLanguagesAndSWE, Type.security],
		'Location' : 'COM2-03-07',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/abhik.jpg',
    'isFound' : False
	}, 
        'Prateek Saxena' : {
         	'ID' : 52,
		'Subtitle' : Role.deanChairAssocProf,
		'Description' : "He is keen in building multimedia systems that contributes towards better wellness and healthcare for all.",
		'Type' : [Type.systemsAndNetworking, Type.security, Type.algoAndTheory],
		'Location' : 'COM2-03-40',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/prateeks.jpg',
    'isFound' : False
	}, 
        'Reza SHOKRI' : {
         	'ID' : 53,
		'Subtitle' : Role.presidentialYoungProf,
		'Description' : " He is a recipient of the IEEE Security and Privacy (S&P) Test-of-Time Award 2021, for his paper on quantifying location privacy.",
		'Type' : [Type.security, Type.ai, Type.algoAndTheory],
		'Location' : 'COM2-03-60',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/reza.jpg',
    'isFound' : False
	}, 
        'Terence Sim' : {
         	'ID' : 54,
		'Subtitle' : Role.assocProf,
		'Description' : "Explain. Demonstrate. Experiment. Inspire.",
		'Type' : [Type.media, Type.security],
		'Location' : 'AS6-05-13',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/tsim.jpg',
    'isFound' : False
	}, 
        'Harold SOH' : {
         	'ID' : 55,
		'Subtitle' : Role.assisProf,
		'Description' : "His work spans cognitive modeling (specifically human trust) to physical systems (perception with novel e-skins) and has been recognized with best paper award nominations at RSS, HRI, and IROS.",
		'Type' : [Type.ai],
		'Location' : 'COM2-03-03',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/hsoh.jpg',
    'isFound' : False
	}, 
        'Soo Yuen Jien' : {
         	'ID' : 56,
		'Subtitle' : Role.assocProf,
		'Description' : "Uncle Soo.",
		'Type' : [Type.systemsAndNetworking],
		'Location' : 'COM2-02-61',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/sooyj.jpg',
    'isFound' : False
	}, 
        'Sufatrio' : {
         	'ID' : 57,
		'Subtitle' : Role.lecturer,
		'Description' : "He is interested in many areas of computer security, and have published numerous papers on systems, network and mobile security.",
		'Type' : [],
		'Location' : 'COM2-03-42',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/sufatrio.jpg',
    'isFound' : False
	}, 
        'Ken Sung' : {
         	'ID' : 58,
		'Subtitle' : Role.prof,
		'Description' : "He is a senior group leader in Genome Institute of Singapore. He has over 20 years experience in Algorithm and Bioinformatics research. ",
		'Type' : [Type.algoAndTheory, Type.compBio],
		'Location' : 'COM2-02-06',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/ksung.jpg',
    'isFound' : False
	}, 
        'Ravi Suppiah' : {
         	'ID' : 59,
		'Subtitle' : Role.lecturer,
		'Description' : "His focus is on using BCI for Biometric Identification. This is a relatively unexplored area and holds a lot of potential for secure authentication and verification.",
		'Type' : [],
		'Location' : 'COM2-03-36',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/suppiah_2.jpg',
    'isFound' : False
	}, 
        'Aaron Tan' : {
         	'ID' : 60,
		'Subtitle' : Role.assocProf,
		'Description' : "Aaron has won several teaching awards both at the school level as well as university level in the period from 1999 through 2010, and has been placed on the honour roll since 2010.",
		'Type' : [],
		'Location' : 'COM1-03-12',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/tantc.jpg',
    'isFound' : False
	}, 
        'Colin Tan' : {
         	'ID' : 61,
		'Subtitle' : Role.seniorLect,
		'Description' : "Colin has written a lightweight operating system for the Arduino called ArdOS that fits into less than a kilobyte of memory, available at https://bitbucket.org/ctank/ardos-ide/wiki/Home.",
		'Type' : [Type.systemsAndNetworking, Type.ai],
		'Location' : 'COM2-02-08',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/ctank.jpg',
    'isFound' : False
	}, 
        'Gary Tan' : {
         	'ID' : 62,
		'Subtitle' : Role.assocProf,
		'Description' : "He serves on the program committee of Distributed Simulation and Real-time Systems Symposium, and is on the Editorial Board of the International Journal of Modelling, Simulation, and Scientific Computing (World Scientific).",
		'Type' : [Type.systemsAndNetworking],
		'Location' : 'COM2-03-50',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/gtan.jpg',
    'isFound' : False
	}, 
        'Tan Kian Lee' : {
         	'ID' : 63,
		'Subtitle' : Role.shawSeniorProf,
		'Description' : " Kian-Lee has published over 300 research articles in international journals and conference proceedings, and co-authored several books/monographs.",
		'Type' : [Type.media, Type.compBio, Type.database],
		'Location' : 'COM1-03-23',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/tankl.jpg',
    'isFound' : False
	}, 
	'Tan Tiow Seng' : {
         	'ID' : 64,
		'Subtitle' : Role.assocProf,
		'Description' : " His team has released a number of GPU software on geometric computation for free download to the community. These are the only ones available that are robust, accurate and efficient till date. ",
		'Type' : [Type.media],
		'Location' : 'AS6-04-10',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/tants.jpg',
    'isFound' : False
	}, 
        'Teo Yong Meng' : {
         	'ID' : 65,
		'Subtitle' : Role.assocProf,
		'Description' : "Professor Teo’s research focuses on performance modeling of modern processor systems (clusters, cloud and edge) and modeling and formalization of emergence in complex systems.",
		'Type' : [Type.systemsAndNetworking],
		'Location' : 'COM2-04-39',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/teoym.jpg',
    'isFound' : False
	}, 
        'Bimlesh Wadhwa' : {
         	'ID' : 66,
		'Subtitle' : Role.assocProf,
		'Description' : "Dr Wadhwa is the initiator and leader of the Code for Community programme, an initiative by NUS School of Computing to bring computing education to underserved communities. ",
		'Type' : [Type.programmingLanguagesAndSWE, Type.media],
		'Location' : 'COM2-02-62',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/bimlesh.jpg',
    'isFound' : False
	}, 
        'Wang Ye' : {
         	'ID' : 67,
		'Subtitle' : Role.assocProf,
		'Description' : "He has developed and has taught the first and only course on “Sound and Music Computing” in Singapore.",
		'Type' : [Type.media],
		'Location' : 'AS6-04-08',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/wangye.jpg',
    'isFound' : False
	}, 
        'Wong Lim Soon' : {
         	'ID' : 68,
		'Subtitle' : Role.chairProf,
		'Description' : "He co-founded Molecular Connections in India, and has served as its chairman for over a decade, seeing the company growing progressively to some 2,000 information curators, software engineers, research scientists.",
		'Type' : [Type.compBio, Type.algoAndTheory, Type.database],
		'Location' : 'COM2-03-57',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/wongls.jpg',
    'isFound' : False
	}, 
        'Wong Weng Fai' : {
         	'ID' : 69,
		'Subtitle' : Role.assocProf,
		'Description' : "hese days, his focus is on approximate computing, including precision analysis, variable precision arithmetic, and approximation of deep learning networks using approximate hardware accelerators.",
		'Type' : [Type.systemsAndNetworking],
		'Location' : 'COM2-03-56',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/wongwf.jpg',
    'isFound' : False
	}, 
        'Xiao Xiaokui' : {
         	'ID' : 70,
		'Subtitle' : Role.assocProf,
		'Description' : "Xiaokui’s research focuses on data management and analytics, especially on algorithms for large data, data privacy, and data mining.",
		'Type' : [Type.database, Type.algoAndTheory],
		'Location' : 'COM1-03-25',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/xiaoxk.jpg',
    'isFound' : False
	}, 
        'Angela Yao' : {
         	'ID' : 71,
		'Subtitle' : Role.assisProf,
		'Description' : "My students and I develop algorithms for automated interpretation of images and video. We work on topics ranging from segmentation, pose estimation, to video understanding.",
		'Type' : [Type.ai, Type.media],
		'Location' : 'COM1-03-06',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/ayao.jpg',
    'isFound' : False
	}, 
        'Roland Yap' : {
         	'ID' : 72,
		'Subtitle' : Role.assocProf,
		'Description' : "He is well known for pioneering research in CLP(R) and the CLP(R) system which has been influential in the development of the field of Constraint Programming (CP).",
		'Type' : [Type.ai, Type.security, Type.programmingLanguagesAndSWE, Type.algoAndTheory],
		'Location' : 'COM2-03-09',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/ryap.jpg',
    'isFound' : False
	}, 
        'Yu Haifeng' : {
         	'ID' : 73,
		'Subtitle' : Role.deanChairAssocProf,
		'Description' : "He has won several best paper awards, including the best paper award in SIGCOMM 2010. He has also served on the PC of many premier international conferences such as PODC, DISC, SIGCOMM, CCS, and Oakland.",
		'Type' : [Type.systemsAndNetworking, Type.algoAndTheory, Type.security],
		'Location' : 'COM2-04-25',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/yuhf.jpg',
    'isFound' : False
	}, 
        'Zhao Jin' : {
         	'ID' : 74,
		'Subtitle' : Role.seniorLect,
		'Description' : "He is the coordinator of NUS Orbital, which is an independent software development project course that attracts more than 400 students every year.",
		'Type' : [],
		'Location' : 'COM2-02-10',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/zhaojin.jpg',
    'isFound' : False
	}, 
        'Zhao Shengdong' : {
         	'ID' : 75,
		'Subtitle' : Role.assocProf,
		'Description' : " ACM Interaction Magazine mentioned him as one of the most prolific authors in Asia for the ACM SIGCHI conference. ",
		'Type' : [Type.media],
		'Location' : 'COM2-03-25',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/yuhf.jpg',
    'isFound' : False
	}, 
        'Zhou Lifeng' : {
         	'ID' : 76,
		'Subtitle' : Role.seniorLect,
		'Description' : "In order to provide a good student learning experience, he uses a variety of questioning techniques to engage students in drawing connections between conceptual and procedural knowledge.",
		'Type' : [],
		'Location' : 'COM2-02-56',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/zhoulife.jpg',
    'isFound' : False
	}, 
        'Roger Zimmermann' : {
         	'ID' : 77,
		'Subtitle' : Role.prof,
		'Description' : "He has co-authored a book, seven patents and more than three hundred conference publications, journal articles and book chapters in the areas of multimedia, GIS and information management. ",
		'Type' : [Type.media],
		'Location' : 'AS6-05-05',
		'Image' : 'https://www.comp.nus.edu.sg/stfphotos/rogerz.jpg',
    'isFound' : False
	},                                                                                                                                                                                                                         
}

profs_name_list = list(sorted(list(profs.keys())))

for i in range(len(profs_name_list)):
  profs[profs_name_list[i]]["ID"] = i + 1