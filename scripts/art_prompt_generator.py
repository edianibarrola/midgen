import random

# Define the information about paintings

paintings = [
	{
  	"artist": "Leonardo da Vinci",
  	"title": "Mona Lisa",
  	"year": "1503-1506",
  	"style": "High Renaissance",
  	"color_scheme": "Subdued earth tones with warm colors",
  	"feel": "Enigmatic and serene",
  	"setting": "A woman against a distant landscape with a river and bridge",
  	"theme": "Human identity and emotion",
  	"technical_style": "Leonardo's use of sfumato, blending and softening outlines, creates a lifelike and mysterious atmosphere."
	},
	{
  	"artist": "Vincent van Gogh",
  	"title": "The Starry Night",
  	"year": "1889",
  	"style": "Post-Impressionism",
  	"color_scheme": "Dark blues and yellows dominating the night sky",
  	"feel": "Expressive and dreamlike",
  	"setting": "A village with swirling stars and cypress trees",
  	"theme": "Nature and the universe",
  	"technical_style": "Van Gogh's bold impasto technique and swirling brushstrokes give the painting a vibrant and textured surface."
	},
	{
  	"artist": "Michelangelo",
  	"title": "The Creation of Adam",
  	"year": "1512",
  	"style": "High Renaissance",
  	"color_scheme": "Warm tones, reds and pinks in particular",
  	"feel": "Powerful and divine",
  	"setting": "Sistine Chapel ceiling, God reaching out to Adam",
  	"theme": "Divine creation and human connection",
  	"technical_style": "Michelangelo's mastery of anatomical accuracy and sculptural form is evident in the detailed muscular structure of the figures."
	},
	{
  	"artist": "Pablo Picasso",
  	"title": "Guernica",
  	"year": "1937",
  	"style": "Cubism",
  	"color_scheme": "Black, white, and grayscale tones",
  	"feel": "Chaotic and anguished",
  	"setting": "Depicts the aftermath of the bombing of Guernica",
  	"theme": "Anti-war and suffering",
  	"technical_style": "Picasso's deconstruction of form and use of fractured geometric shapes characterize his Cubist approach to representing complex subjects."
	},
	{
  	"artist": "Edvard Munch",
  	"title": "The Scream",
  	"year": "1893",
  	"style": "Symbolism and Expressionism",
  	"color_scheme": "Vivid colors, swirling oranges and yellows",
  	"feel": "Anxiety-ridden and haunting",
  	"setting": "A bridge with a turbulent sky and fjord",
  	"theme": "Existential despair",
  	"technical_style": "Munch's bold and exaggerated brushwork and intense color choices amplify the emotional intensity of the scene."
	},
	{
  	"artist": "Johannes Vermeer",
  	"title": "Girl with a Pearl Earring",
  	"year": "1665",
  	"style": "Dutch Golden Age",
  	"color_scheme": "Warm tones and soft shadows",
  	"feel": "Mysterious and intimate",
  	"setting": "A young woman against a dark background",
  	"theme": "Beauty and innocence",
  	"technical_style": "Vermeer's meticulous attention to light and shadow, known as 'chiaroscuro,' creates a sense of depth and luminosity in his paintings."
	},
	{
  	"artist": "Grant Wood",
  	"title": "American Gothic",
  	"year": "1930",
  	"style": "Regionalism",
  	"color_scheme": "Earthy and muted tones",
  	"feel": "Serious and stoic",
  	"setting": "A farmhouse with a farmer and his daughter",
  	"theme": "Rural American resilience",
  	"technical_style": "Wood's precise and detailed style captures the realism of rural life, while the stiff poses of the subjects reflect the style of Northern Renaissance portraiture."
	},
	{
  	"artist": "Frida Kahlo",
  	"title": "The Two Fridas",
  	"year": "1939",
  	"style": "Surrealism",
  	"color_scheme": "Vivid and contrasting colors",
  	"feel": "Introspective and emotional",
  	"setting": "An abstract and symbolic setting",
  	"theme": "Identity and emotional turmoil",
  	"technical_style": "Kahlo's incorporation of surreal and symbolic elements, combined with her meticulous rendering of detail, exemplifies her unique approach to Surrealism."
	},
	{
  	"artist": "Leonardo da Vinci",
  	"title": "The Last Supper",
  	"year": "1495-1498",
  	"style": "High Renaissance",
  	"color_scheme": "Subdued earth tones with warm highlights",
  	"feel": "Spiritual and momentous",
  	"setting": "A dining hall with Jesus and disciples",
  	"theme": "Final meal before crucifixion",
  	"technical_style": "Leonardo's use of one-point perspective and mastery of foreshortening contributes to the harmonious composition and spatial depth of the scene."
	},
	{
  	"artist": "Salvador Dalí",
  	"title": "The Persistence of Memory",
  	"year": "1931",
  	"style": "Surrealism",
  	"color_scheme": "Muted and dreamlike tones",
  	"feel": "Surreal and mysterious",
  	"setting": "A barren landscape with melting clocks",
  	"theme": "Time, reality, and the subconscious",
  	"technical_style": "Dalí's meticulous rendering of dreamlike and distorted forms, combined with his precise application of paint, creates a sense of uncanny reality in his surrealist works."
	},
	{
  	"artist": "Sandro Botticelli",
  	"title": "The Birth of Venus",
  	"year": "c. 1484-1486",
  	"style": "Early Renaissance",
  	"color_scheme": "Soft and ethereal pastel colors",
  	"feel": "Graceful and mythological",
  	"setting": "Venus rising from the sea on a shell, surrounded by mythological figures",
  	"theme": "Symbolizes the rebirth of classical beauty and the divine feminine",
  	"technical_style": "Botticelli's use of delicate lines and flowing forms, combined with his attention to graceful proportions, captures the idealized beauty of the Renaissance."
	},
	{
  	"artist": "Claude Monet",
  	"title": "Impression, Sunrise",
  	"year": "1872",
  	"style": "Impressionism",
  	"color_scheme": "Cool blues and hazy oranges",
  	"feel": "Luminous and atmospheric",
  	"setting": "A misty harbor with boats and a rising sun",
  	"theme": "Captures the fleeting effects of light and color in a moment",
  	"technical_style": "Monet's loose brushwork and emphasis on capturing light and atmosphere define the Impressionist movement, giving the painting its ethereal quality."
	},
	{
  	"artist": "Rembrandt van Rijn",
  	"title": "The Night Watch",
  	"year": "1642",
  	"style": "Dutch Golden Age",
  	"color_scheme": "Rich earth tones and dramatic contrasts of light and shadow",
  	"feel": "Dynamically posed and dramatic",
  	"setting": "A group portrait of militia guards in a darkened city square",
  	"theme": "Celebrates civic duty and unity in the face of danger",
  	"technical_style": "Rembrandt's mastery of chiaroscuro and his ability to convey emotional depth through light and shadow make this painting a prime example of his style."
	},
	{
  	"artist": "Gustav Klimt",
  	"title": "The Kiss",
  	"year": "1907-1908",
  	"style": "Symbolism and Art Nouveau",
  	"color_scheme": "Rich golds and intricate patterns",
  	"feel": "Elegant and sensuous",
  	"setting": "A couple locked in an embrace against a golden, geometric background",
  	"theme": "Love and the merging of human and divine",
  	"technical_style": "Klimt's use of gold leaf and elaborate patterns, combined with his focus on intricate details, characterizes his distinctive Art Nouveau style."
	},
	{
  	"artist": "Diego Velázquez",
  	"title": "Las Meninas",
  	"year": "1656",
  	"style": "Baroque",
  	"color_scheme": "Rich colors and dramatic light contrasts",
  	"feel": "Complex and immersive",
  	"setting": "A royal family surrounded by attendants and a mirror reflecting the viewer's perspective",
  	"theme": "Explores the role of the artist, reality, and illusion",
  	"technical_style": "Velázquez's masterful manipulation of light and shadow, combined with his attention to individual characterizations, showcases his Baroque approach to realism."
	},
	{
  	"artist": "Edgar Degas",
  	"title": "The Dance Class",
  	"year": "1873-1876",
  	"style": "Impressionism and Realism",
  	"color_scheme": "Soft pastels and subtle shades",
  	"feel": "Graceful and observational",
  	"setting": "Ballerinas practicing in a dance studio",
  	"theme": "Captures the everyday lives of dancers and their dedication",
  	"technical_style": "Degas's fascination with movement and his use of pastels and loose brushwork create a sense of immediacy and capture the fleeting moments of the scene."
	},
	{
  	"artist": "Hieronymus Bosch",
  	"title": "The Garden of Earthly Delights",
  	"year": "1490-1510",
  	"style": "Northern Renaissance and Early Netherlandish",
  	"color_scheme": "Vivid and fantastical colors",
  	"feel": "Surreal and mysterious",
  	"setting": "Triptych depicting earthly pleasures, sin, and divine punishment",
  	"theme": "Symbolizes the human experience, morality, and salvation",
  	"technical_style": "Bosch's intricate and imaginative detailing, combined with his exploration of fantastical and grotesque imagery, characterizes his unique Northern Renaissance style."
	},
	{
  	"artist": "Georgia O'Keeffe",
  	"title": "Jimson Weed/White Flower No. 1",
  	"year": "1932",
  	"style": "American Modernism",
  	"color_scheme": "Subdued whites and greens",
  	"feel": "Bold and organic",
  	"setting": "Close-up of a large white flower against a simple background",
  	"theme": "Celebrates the beauty and abstraction of nature",
  	"technical_style": "O'Keeffe's attention to magnified detail and her use of simplified forms make her work an important contribution to American Modernist art."
	},
	{
  	"artist": "Wassily Kandinsky",
  	"title": "Composition VII",
  	"year": "1913",
  	"style": "Abstract Expressionism",
  	"color_scheme": "Vibrant and contrasting colors",
  	"feel": "Energetic and nonrepresentational",
  	"setting": "A complex arrangement of geometric and organic shapes",
  	"theme": "Explores the relationship between color, form, and emotion",
  	"technical_style": "Kandinsky's pioneering work in abstract art is characterized by his bold use of color and form to convey the spiritual and emotional aspects of his subjects."
	},



	{
  	"artist": "Jackson Pollock",
  	"title": "Number 1A, 1948",
  	"year": "1948",
  	"style": "Abstract Expressionism",
  	"color_scheme": "Dripping and splattered colors",
  	"feel": "Dynamic and spontaneous",
  	"setting": "An expansive canvas covered in intricate drips and splatters",
  	"theme": "Explores the physicality of paint and gesture",
  	"technical_style": "Pollock's innovative 'drip painting' technique involves the rhythmic and spontaneous application of paint, creating a sense of movement and energy."
	},
	{
  	"artist": "Paul Cézanne",
  	"title": "Mont Sainte-Victoire",
  	"year": "1902-1906",
  	"style": "Post-Impressionism",
  	"color_scheme": "Muted and harmonious colors",
  	"feel": "Serene and contemplative",
  	"setting": "A view of Mont Sainte-Victoire in the French countryside",
  	"theme": "Explores the relationship between nature and artistic representation",
  	"technical_style": "Cézanne's unique approach to color and form, characterized by his use of geometric shapes and planes, lays the foundation for later modernist movements."
	},
	{
  	"artist": "Diego Rivera",
  	"title": "Man at the Crossroads",
  	"year": "1934",
  	"style": "Mexican Muralism",
  	"color_scheme": "Vibrant and bold colors",
  	"feel": "Political and monumental",
  	"setting": "A mural depicting a worker holding a hammer and sickle at a crossroads",
  	"theme": "Addresses the social and political struggles of the working class",
  	"technical_style": "Rivera's mastery of large-scale murals and his use of vivid colors to convey socio-political messages make this work a prime example of Mexican Muralism."
	},
	{
  	"artist": "Katsushika Hokusai",
  	"title": "The Great Wave off Kanagawa",
  	"year": "c. 1830-1833",
  	"style": "Ukiyo-e",
  	"color_scheme": "Contrasting blues and whites",
  	"feel": "Dramatic and iconic",
  	"setting": "A towering wave threatens boats near Mount Fuji",
  	"theme": "Captures the power of nature and its relationship with humans",
  	"technical_style": "Hokusai's woodblock print technique and use of perspective create a striking visual impact, contributing to the enduring popularity of this image."
	},
	{
  	"artist": "Mark Rothko",
  	"title": "No. 61 (Rust and Blue)",
  	"year": "1953",
  	"style": "Color Field Painting",
  	"color_scheme": "Rich and contemplative colors",
  	"feel": "Meditative and immersive",
  	"setting": "A large canvas dominated by rectangles of rust and blue",
  	"theme": "Focuses on the emotional and spiritual impact of color",
  	"technical_style": "Rothko's signature color field technique involves the use of large, flat color areas to evoke emotional and psychological responses from viewers."
	},
	{
  	"artist": "Frida Kahlo",
  	"title": "Self-Portrait with Thorn Necklace and Hummingbird",
  	"year": "1940",
  	"style": "Surrealism and Mexican Folk Art",
  	"color_scheme": "Vivid and contrasting colors",
  	"feel": "Introspective and symbolic",
  	"setting": "A self-portrait with thorns around her neck and a hummingbird",
  	"theme": "Explores pain, identity, and personal mythology",
  	"technical_style": "Kahlo's incorporation of surreal and symbolic elements, combined with her intense self-exploration, is a hallmark of her artistic style."
	},

	{
  	"artist": "Andy Warhol",
  	"title": "Campbell's Soup Cans",
  	"year": "1961-1962",
  	"style": "Pop Art",
  	"color_scheme": "Vibrant and commercial colors",
  	"feel": "Bold and iconic",
  	"setting": "A series of 32 paintings depicting different varieties of Campbell's Soup",
  	"theme": "Celebrates consumer culture and mass production",
  	"technical_style": "Warhol's use of repetition and commercial imagery, combined with his flattened and graphic approach, defines the Pop Art movement."
	},
	{
  	"artist": "Gustave Courbet",
  	"title": "The Origin of the World",
  	"year": "1866",
  	"style": "Realism",
  	"color_scheme": "Natural flesh tones",
  	"feel": "Provocative and intimate",
  	"setting": "A close-up view of a woman's genitals",
  	"theme": "Explores themes of sexuality and intimacy",
  	"technical_style": "Courbet's precise and unapologetic realism challenges societal norms and conventions, making this painting a provocative statement."
	},
	{
  	"artist": "Banksy",
  	"title": "Girl with a Balloon",
  	"year": "2002",
  	"style": "Street Art",
  	"color_scheme": "Monochromatic with a pop of red",
  	"feel": "Playful and subversive",
  	"setting": "A girl reaching out to a heart-shaped balloon",
  	"theme": "Blends political commentary with artistic expression",
  	"technical_style": "Banksy's stenciled technique and use of unexpected context create thought-provoking statements within the urban environment."
	},
	{
  	"artist": "Yayoi Kusama",
  	"title": "Infinity Mirror Room - Phalli's Field",
  	"year": "1965",
  	"style": "Contemporary Art",
  	"color_scheme": "Dazzling and multicolored",
  	"feel": "Mesmerizing and immersive",
  	"setting": "An installation with mirrored walls and countless red polka-dotted phallic forms",
  	"theme": "Explores the artist's fascination with repetition and infinity",
  	"technical_style": "Kusama's use of mirrored surfaces and repetitive elements invites viewers to experience an illusion of infinite space and forms."
	},
	{
  	"artist": "Tamara de Lempicka",
  	"title": "Autoportrait (Tamara in a Green Bugatti)",
  	"year": "1929",
  	"style": "Art Deco",
  	"color_scheme": "Vibrant and luxurious colors",
  	"feel": "Elegant and glamorous",
  	"setting": "A self-portrait of the artist in a green Bugatti car",
  	"theme": "Reflects the spirit of the Jazz Age and female empowerment",
  	"technical_style": "De Lempicka's sharp angles, bold lines, and geometric forms characterize the Art Deco style of the era, capturing the elegance and dynamism of the period."
	},
	{
  	"artist": "J.M.W. Turner",
  	"title": "The Fighting Temeraire",
  	"year": "1839",
  	"style": "Romanticism",
  	"color_scheme": "Dramatic and fiery colors",
  	"feel": "Epic and nostalgic",
  	"setting": "An old warship being towed by a steam-powered tugboat at sunset",
  	"theme": "Symbolizes the passing of an era and the impact of technology",
  	"technical_style": "Turner's mastery of light and atmospheric effects, combined with his ability to convey emotion and narrative through nature, exemplifies the Romantic style."
	},




	{
  	"artist": "Marc Chagall",
  	"title": "I and the Village",
  	"year": "1911",
  	"style": "Modernism and Surrealism",
  	"color_scheme": "Vibrant and dreamlike colors",
  	"feel": "Whimsical and symbolic",
  	"setting": "A fantastical scene featuring a village and various symbolic elements",
  	"theme": "Blends personal memories, folklore, and dreamscapes",
  	"technical_style": "Chagall's use of bold colors and imaginative compositions, often defying conventional perspective, contributes to his unique and dreamlike visual language."
	},
	{
  	"artist": "Amedeo Modigliani",
  	"title": "Reclining Nude",
  	"year": "1917",
  	"style": "Modernism",
  	"color_scheme": "Simplified and harmonious colors",
  	"feel": "Elegant and sensual",
  	"setting": "A reclining nude woman against a simple background",
  	"theme": "Captures the beauty and sensuality of the female form",
  	"technical_style": "Modigliani's elongated and stylized figures, characterized by almond-shaped eyes and graceful curves, convey a sense of elegance and modernist simplicity."
	},
	{
  	"artist": "Roy Lichtenstein",
  	"title": "Whaam!",
  	"year": "1963",
  	"style": "Pop Art",
  	"color_scheme": "Bold and primary colors with Ben-Day dots",
  	"feel": "Graphic and comic-inspired",
  	"setting": "An explosive depiction of a fighter jet firing rockets",
  	"theme": "Transforms popular culture and comics into high art",
  	"technical_style": "Lichtenstein's use of bold outlines, flat colors, and Ben-Day dots imitates the printing techniques of comics, emphasizing the iconic and mass-produced nature of the subject."
	},
	{
  	"artist": "Caravaggio",
  	"title": "Judith Beheading Holofernes",
  	"year": "c. 1599-1602",
  	"style": "Baroque",
  	"color_scheme": "Rich and dramatic chiaroscuro",
  	"feel": "Intense and dramatic",
  	"setting": "The biblical scene of Judith beheading the Assyrian general Holofernes",
  	"theme": "Symbolizes courage, triumph, and the power of women",
  	"technical_style": "Caravaggio's mastery of chiaroscuro, the strong contrast between light and dark, creates a sense of drama and three-dimensionality in his works."
	},
	{
  	"artist": "Camille Pissarro",
  	"title": "Boulevard Montmartre at Night",
  	"year": "1897",
  	"style": "Impressionism",
  	"color_scheme": "Nocturnal blues and warm streetlights",
  	"feel": "Atmospheric and urban",
  	"setting": "A view of a bustling Parisian street at night",
  	"theme": "Captures the urban energy and the effects of artificial light",
  	"technical_style": "Pissarro's ability to convey the transient effects of light and atmosphere, even at night, contributes to his role as an Impressionist pioneer."
	},
	{
  	"artist": "Hokusai",
  	"title": "Thirty-Six Views of Mount Fuji: The Great Wave off Kanagawa",
  	"year": "c. 1830-1833",
  	"style": "Ukiyo-e",
  	"color_scheme": "Contrasting blues and whites",
  	"feel": "Dramatic and iconic",
  	"setting": "A towering wave threatens boats near Mount Fuji",
  	"theme": "Captures the power of nature and its relationship with humans",
  	"technical_style": "Hokusai's woodblock print technique and use of perspective create a striking visual impact, contributing to the enduring popularity of this image."
	},

	{
  	"artist": "Jean-Michel Basquiat",
  	"title": "Untitled",
  	"year": "1982",
  	"style": "Neo-Expressionism",
  	"color_scheme": "Bold and contrasting colors",
  	"feel": "Raw and energetic",
  	"setting": "A composition of layered texts, symbols, and imagery",
  	"theme": "Reflects street art, social commentary, and personal experiences",
  	"technical_style": "Basquiat's raw and instinctive approach, characterized by frenetic brushwork and the fusion of text and image, exemplifies the intensity of Neo-Expressionism."
	},
	{
  	"artist": "Edouard Manet",
  	"title": "Olympia",
  	"year": "1863",
  	"style": "Realism",
  	"color_scheme": "Subdued and earthy tones",
  	"feel": "Provocative and confrontational",
  	"setting": "A reclining nude woman with a confrontational gaze",
  	"theme": "Challenges conventions of the female nude in art",
  	"technical_style": "Manet's departure from idealized depictions and his direct portrayal of his subject create a sense of realism and social critique in this iconic painting."
	},
	{
  	"artist": "Kara Walker",
  	"title": "Gone: An Historical Romance of a Civil War as It Occurred Between the Dusky Thighs of One Young Negress and Her Heart",
  	"year": "1994",
  	"style": "Contemporary Art and Silhouette Art",
  	"color_scheme": "Black and white contrasts",
  	"feel": "Provocative and unsettling",
  	"setting": "A large-scale silhouette narrative depicting a racially charged scene",
  	"theme": "Addresses the complexities of race, history, and power",
  	"technical_style": "Walker's use of traditional silhouette techniques and her subversion of historical imagery create a powerful commentary on race and gender in contemporary society."
	},
	{
  	"artist": "Egon Schiele",
  	"title": "The Self-Seers (Death and Man)",
  	"year": "1911",
  	"style": "Expressionism",
  	"color_scheme": "Saturated and emotive colors",
  	"feel": "Intense and introspective",
  	"setting": "A twisted and anguished depiction of two intertwined figures",
  	"theme": "Explores existential and psychological states",
  	"technical_style": "Schiele's distortion of form, use of bold line work, and emotive color palette contribute to the emotional intensity and psychological depth of his work."
	},
	{
  	"artist": "Diego Rivera",
  	"title": "Detroit Industry Murals",
  	"year": "1932-1933",
  	"style": "Mexican Muralism",
  	"color_scheme": "Vibrant and industrial colors",
  	"feel": "Epic and socio-political",
  	"setting": "A series of murals depicting industrial scenes and workers",
  	"theme": "Celebrates labor, industry, and technological progress",
  	"technical_style": "Rivera's use of monumental scale and intricate detailing, combined with his commitment to portraying social themes, reflects the essence of Mexican Muralism."
	},
	{
  	"artist": "Yves Klein",
  	"title": "Blue Monochrome",
  	"year": "1957",
  	"style": "Nouveau Réalisme and Monochromatic Art",
  	"color_scheme": "Vibrant and deep blue",
  	"feel": "Serene and immersive",
  	"setting": "A canvas painted entirely in a rich blue hue",
  	"theme": "Focuses on color as the primary artistic element",
  	"technical_style": "Klein's exploration of monochromatic color and his invention of 'International Klein Blue' showcases his dedication to elevating color to a central role in his art."
	},

	{
  	"artist": "Norman Rockwell",
  	"title": "Freedom of Speech",
  	"year": "1943",
  	"style": "Illustration",
  	"color_scheme": "Warm and realistic colors",
  	"feel": "Nostalgic and patriotic",
  	"setting": "A scene of a man speaking at a town meeting",
  	"theme": "Captures American ideals and democratic participation",
  	"technical_style": "Rockwell's meticulous attention to detail, emotive expressions, and narrative storytelling abilities are hallmarks of his illustrative approach."
	},
	{
  	"artist": "René Magritte",
  	"title": "The Son of Man",
  	"year": "1964",
  	"style": "Surrealism",
  	"color_scheme": "Muted colors with a pop of red",
  	"feel": "Puzzling and enigmatic",
  	"setting": "A suited man with his face obscured by a hovering green apple",
  	"theme": "Examines the nature of identity and reality",
  	"technical_style": "Magritte's precise rendering and juxtaposition of ordinary elements in unexpected contexts contribute to the dreamlike quality of his surrealist works."
	},
	{
  	"artist": "Akira Kurosawa",
  	"title": "Seven Samurai",
  	"year": "1954",
  	"style": "Cinematic",
  	"color_scheme": "Dynamic and cinematic color palette",
  	"feel": "Epic and intense",
  	"setting": "A story of seven ronin defending a village from bandits",
  	"theme": "Explores honor, sacrifice, and the complexities of human relationships",
  	"technical_style": "Kurosawa's masterful use of composition, pacing, and camera movement creates a cinematic experience that influences filmmaking to this day."
	},
	{
  	"artist": "Edward Hopper",
  	"title": "Nighthawks",
  	"year": "1942",
  	"style": "Realism",
  	"color_scheme": "Cool and atmospheric colors",
  	"feel": "Lonely and introspective",
  	"setting": "A late-night diner scene with isolated figures",
  	"theme": "Evokes urban isolation and a sense of quiet contemplation",
  	"technical_style": "Hopper's meticulous attention to light and shadow, combined with his ability to convey a sense of solitude, defines his realist approach to capturing modern life."
	},
	{
  	"artist": "Hayao Miyazaki",
  	"title": "Spirited Away",
  	"year": "2001",
  	"style": "Animation and Fantasy",
  	"color_scheme": "Vivid and fantastical colors",
  	"feel": "Magical and adventurous",
  	"setting": "A young girl navigating a mysterious and magical world",
  	"theme": "Celebrates imagination, nature, and personal growth",
  	"technical_style": "Miyazaki's imaginative storytelling and attention to intricate details, combined with his hand-drawn animation, create a sense of wonder in his films."
	},
	{
  	"artist": "Edgar Wright",
  	"title": "Baby Driver",
  	"year": "2017",
  	"style": "Cinematic",
  	"color_scheme": "Dynamic and visually striking colors",
  	"feel": "Energetic and rhythmic",
  	"setting": "A young getaway driver's life intertwines with crime and music",
  	"theme": "Uses music and visuals to create a unique cinematic experience",
  	"technical_style": "Wright's mastery of visual storytelling, use of music synchronization, and creative editing contribute to the distinct style of his films."
	},

	{
  	"artist": "J.R.R. Tolkien (Illustrator)",
  	"title": "The Hobbit",
  	"year": "1937",
  	"style": "Illustration",
  	"color_scheme": "Earthy and whimsical colors",
  	"feel": "Adventurous and fantastical",
  	"setting": "Illustrations from the beloved fantasy novel",
  	"theme": "Embodies the world of Middle-earth and its magical creatures",
  	"technical_style": "Tolkien's intricate illustrations capture the spirit of his own created mythology and add depth to his literary works."
	},
	{
  	"artist": "Federico Fellini",
  	"title": "8½",
  	"year": "1963",
  	"style": "Cinematic",
  	"color_scheme": "Dreamlike and surreal colors",
  	"feel": "Meta and introspective",
  	"setting": "A film director navigates his own creative crisis",
  	"theme": "Blurs the line between reality and fantasy in a filmmaker's mind",
  	"technical_style": "Fellini's use of dream sequences, extravagant costumes, and his exploration of the artist's inner world make his films stand out as works of art."
	},
	{
  	"artist": "Ralph McQuarrie",
  	"title": "Star Wars Concept Art",
  	"year": "Late 1970s",
  	"style": "Illustration and Science Fiction",
  	"color_scheme": "Space-inspired and futuristic colors",
  	"feel": "Epic and otherworldly",
  	"setting": "Concept art for the Star Wars universe",
  	"theme": "Shaped the visual identity of the Star Wars galaxy",
  	"technical_style": "McQuarrie's visionary concept art helped establish the iconic look of the Star Wars universe, blending realism and imagination."
	},
	{
  	"artist": "Frida Kahlo",
  	"title": "The Two Fridas",
  	"year": "1939",
  	"style": "Surrealism and Self-Portraiture",
  	"color_scheme": "Contrasting and emotional colors",
  	"feel": "Personal and introspective",
  	"setting": "Two self-portraits of Frida Kahlo, connected by a vein",
  	"theme": "Explores duality, identity, and emotional struggles",
  	"technical_style": "Kahlo's self-exploration through vivid symbolism, combined with her fusion of personal experiences and surrealism, is a hallmark of her art."
	},
	{
  	"artist": "Jean-Pierre Jeunet",
  	"title": "Amélie",
  	"year": "2001",
  	"style": "Cinematic",
  	"color_scheme": "Whimsical and warm colors",
  	"feel": "Quirky and heartwarming",
  	"setting": "A young woman spreads joy and magic in Montmartre, Paris",
  	"theme": "Infuses everyday life with wonder and whimsy",
  	"technical_style": "Jeunet's visual storytelling, use of vibrant colors, and inventive camera techniques contribute to the enchanting atmosphere of his films."
	},
	{
  	"artist": "Tove Jansson",
  	"title": "Moomin Series",
  	"year": "Mid-20th century",
  	"style": "Illustration and Children's Literature",
  	"color_scheme": "Playful and inviting colors",
  	"feel": "Lighthearted and imaginative",
  	"setting": "Illustrations from the Moomin book series",
  	"theme": "Invites readers into a whimsical world of friendly creatures and adventures",
  	"technical_style": "Jansson's charming illustrations bring to life the Moomin world, evoking a sense of warmth, friendship, and creativity."
	},

	{
  	"artist": "Chris Foss",
  	"title": "Spaceship Illustrations",
  	"year": "Various",
  	"style": "Sci-Fi Illustration",
  	"color_scheme": "Futuristic and cosmic colors",
  	"feel": "Epic and futuristic",
  	"setting": "Illustrations of spaceships and futuristic landscapes",
  	"theme": "Defines the visual identity of sci-fi book covers and concept art",
  	"technical_style": "Foss's attention to intricate spaceship designs and imaginative landscapes has left an indelible mark on the aesthetics of sci-fi artwork."
	},
	{
  	"artist": "Syd Mead",
  	"title": "Blade Runner Concept Art",
  	"year": "1982",
  	"style": "Concept Art and Futurism",
  	"color_scheme": "Neon and cyberpunk colors",
  	"feel": "Dystopian and atmospheric",
  	"setting": "Concept art for the film Blade Runner",
  	"theme": "Visualized a futuristic, gritty, and cyberpunk world",
  	"technical_style": "Mead's iconic concept art played a pivotal role in shaping the futuristic cityscape of Blade Runner, blending realism and speculative fiction."
	},
	{
  	"artist": "H.R. Giger",
  	"title": "Necronom IV",
  	"year": "1976",
  	"style": "Surreal Sci-Fi",
  	"color_scheme": "Dark and biomechanical colors",
  	"feel": "Alien and unsettling",
  	"setting": "A biomechanical creature in a surreal landscape",
  	"theme": "Explores the fusion of organic and mechanical forms",
  	"technical_style": "Giger's biomechanical and otherworldly aesthetic, characterized by intricate detailing, has left an enduring impact on sci-fi and horror visuals."
	},
	{
  	"artist": "Ridley Scott",
  	"title": "Alien",
  	"year": "1979",
  	"style": "Cinematic and Sci-Fi Horror",
  	"color_scheme": "Eerie and atmospheric colors",
  	"feel": "Tense and suspenseful",
  	"setting": "A commercial spaceship encounters a deadly extraterrestrial",
  	"theme": "Marries sci-fi and horror, exploring the unknown and survival",
  	"technical_style": "Scott's masterful use of lighting, tension-building, and claustrophobic cinematography contributes to the iconic sci-fi horror atmosphere of Alien."
	},
	{
  	"artist": "Moebius",
  	"title": "The Long Tomorrow",
  	"year": "1975",
  	"style": "Sci-Fi Comic Art",
  	"color_scheme": "Vibrant and retro-futuristic colors",
  	"feel": "Pioneering and imaginative",
  	"setting": "Illustrations for the comic series The Long Tomorrow",
  	"theme": "Defines the aesthetics of cyberpunk and retro-futurism",
  	"technical_style": "Moebius's innovative comic art, characterized by intricate details and imaginative world-building, has influenced generations of sci-fi artists."
	},
	{
  	"artist": "Isaac Asimov (Writer)",
  	"title": "Foundation Series",
  	"year": "1951 onwards",
  	"style": "Sci-Fi Literature",
  	"color_scheme": "Varies based on book covers",
  	"feel": "Intellectual and speculative",
  	"setting": "Illustrations from the science fiction book series Foundation",
  	"theme": "Explores the future of human civilization, mathematics, and history",
  	"technical_style": "Asimov's imaginative storytelling and intricate exploration of scientific concepts make his Foundation series a cornerstone of sci-fi literature."
	},

	{
  	"artist": "Moebius",
  	"title": "The Incal",
  	"year": "1980-1988",
  	"style": "Sci-Fi Comic Art",
  	"color_scheme": "Vibrant and cosmic colors",
  	"feel": "Epic and metaphysical",
  	"setting": "Illustrations for the graphic novel series The Incal",
  	"theme": "Blends science fiction, fantasy, and philosophy",
  	"technical_style": "Moebius's richly detailed artwork and surreal settings contribute to the expansive and mind-bending narrative of The Incal."
	},
	{
  	"artist": "Philip K. Dick (Writer)",
  	"title": "Do Androids Dream of Electric Sheep?",
  	"year": "1968",
  	"style": "Sci-Fi Literature",
  	"color_scheme": "Varies based on book covers",
  	"feel": "Thought-provoking and speculative",
  	"setting": "Illustrations from the science fiction novel",
  	"theme": "Explores artificial intelligence, empathy, and human identity",
  	"technical_style": "Dick's exploration of psychological and philosophical themes through science fiction makes his work a cornerstone of the genre."
	},
	{
  	"artist": "Mass Effect Game Series (BioWare)",
  	"title": "Mass Effect 2",
  	"year": "2010",
  	"style": "Video Game Art and Sci-Fi",
  	"color_scheme": "Futuristic and interstellar colors",
  	"feel": "Epic and immersive",
  	"setting": "Concept art from the Mass Effect video game series",
  	"theme": "Blends space exploration, alien races, and moral dilemmas",
  	"technical_style": "The game's concept art, characterized by its attention to alien design, futuristic technology, and vibrant worlds, contributes to the series' immersive universe."
	},
	{
  	"artist": "William Gibson (Writer)",
  	"title": "Neuromancer",
  	"year": "1984",
  	"style": "Sci-Fi Literature",
  	"color_scheme": "Cyberpunk and neon colors",
  	"feel": "Gritty and futuristic",
  	"setting": "Illustrations from the cyberpunk novel Neuromancer",
  	"theme": "Explores cyberspace, hacking, and the intersection of technology and humanity",
  	"technical_style": "Gibson's pioneering work in cyberpunk literature and his vivid description of a digital future continue to influence sci-fi and cyber culture."
	},
	{
  	"artist": "Simon Stålenhag",
  	"title": "The Electric State",
  	"year": "2017",
  	"style": "Illustration and Sci-Fi",
  	"color_scheme": "Muted and retro-futuristic colors",
  	"feel": "Eerie and nostalgic",
  	"setting": "Illustrations from the art book The Electric State",
  	"theme": "Blends sci-fi, technology, and a sense of wonder with a touch of unease",
  	"technical_style": "Stålenhag's unique blend of realistic settings, nostalgic elements, and futuristic concepts creates a haunting and thought-provoking atmosphere."
	},
	{
  	"artist": "William Cameron Menzies (Production Designer)",
  	"title": "Things to Come",
  	"year": "1936",
  	"style": "Cinematic and Futurism",
  	"color_scheme": "Monochromatic and futuristic hues",
  	"feel": "Visionary and utopian",
  	"setting": "Concept art and designs from the film Things to Come",
  	"theme": "Envisions a future world and the evolution of society",
  	"technical_style": "Menzies's futuristic set designs and visualizations of advanced technology contributed to the film's utopian and futuristic aesthetic."
	},



	{
  	"artist": "Katsushika Hokusai",
  	"title": "The Great Wave off Kanagawa",
  	"year": "c. 1830-1833",
  	"style": "Ukiyo-e",
  	"color_scheme": "Contrasting blues and whites",
  	"feel": "Dramatic and iconic",
  	"setting": "A towering wave threatens boats near Mount Fuji",
  	"theme": "Captures the power of nature and its relationship with humans",
  	"technical_style": "Hokusai's woodblock print technique and use of perspective create a striking visual impact, contributing to the enduring popularity of this image."
	},
	{
  	"artist": "Qi Baishi",
  	"title": "Two Chickens",
  	"year": "1929",
  	"style": "Chinese Brush Painting",
  	"color_scheme": "Subtle ink washes with pops of color",
  	"feel": "Delicate and harmonious",
  	"setting": "A depiction of two chickens in a natural setting",
  	"theme": "Celebrates the beauty of nature and everyday life",
  	"technical_style": "Qi Baishi's mastery of traditional Chinese brushwork and ink wash techniques brings a sense of life and movement to his paintings."
	},
	{
  	"artist": "Utagawa Hiroshige",
  	"title": "Sudden Shower over Shin-Ōhashi Bridge and Atake",
  	"year": "1857",
  	"style": "Ukiyo-e",
  	"color_scheme": "Elegant and muted tones",
  	"feel": "Tranquil and atmospheric",
  	"setting": "A scene of travelers caught in a rain shower on a bridge",
  	"theme": "Depicts everyday life and the ephemeral beauty of nature",
  	"technical_style": "Hiroshige's use of color, perspective, and his skill in conveying mood through weather effects characterize his ukiyo-e landscapes."
	},
	{
  	"artist": "Akira Yamaguchi",
  	"title": "Kinkaku-ji (Golden Pavilion)",
  	"year": "Contemporary",
  	"style": "Contemporary Realism",
  	"color_scheme": "Golden hues against a serene background",
  	"feel": "Serene and reverent",
  	"setting": "A realistic depiction of the Kinkaku-ji temple in Kyoto",
  	"theme": "Captures the tranquility and elegance of Japanese architecture",
  	"technical_style": "Yamaguchi's meticulous attention to detail and realistic rendering capture the beauty and cultural significance of historical Japanese landmarks."
	},
	{
  	"artist": "Zhang Daqian",
  	"title": "Lotus",
  	"year": "1940",
  	"style": "Chinese Splash Ink Painting",
  	"color_scheme": "Monochromatic with ink splatters",
  	"feel": "Dynamic and harmonious",
  	"setting": "A portrayal of lotus flowers in ink and splashed color",
  	"theme": "Embraces spontaneity and the fluidity of ink",
  	"technical_style": "Zhang Daqian's combination of traditional Chinese ink painting techniques with a modern, dynamic approach creates a sense of movement and life in his works."
	},
	{
  	"artist": "Hayao Miyazaki",
  	"title": "Spirited Away",
  	"year": "2001",
  	"style": "Animation and Fantasy",
  	"color_scheme": "Vivid and fantastical colors",
  	"feel": "Magical and adventurous",
  	"setting": "A young girl navigating a mysterious and magical world",
  	"theme": "Celebrates imagination, nature, and personal growth",
  	"technical_style": "Miyazaki's imaginative storytelling and attention to intricate details, combined with his hand-drawn animation, create a sense of wonder in his films."
	},

	{
  	"artist": "Guan Daosheng",
  	"title": "Bamboo and Rocks",
  	"year": "13th century",
  	"style": "Chinese Literati Painting",
  	"color_scheme": "Ink washes and subtle earth tones",
  	"feel": "Elegant and contemplative",
  	"setting": "A delicate depiction of bamboo and rocks in ink",
  	"theme": "Reflects the spirit of scholarly pursuits and nature appreciation",
  	"technical_style": "Guan Daosheng's expressive brushwork and emphasis on individuality over realism characterize the literati approach to painting."
	},
	{
  	"artist": "Hokusai",
  	"title": "Thirty-Six Views of Mount Fuji: Red Fuji",
  	"year": "c. 1830-1833",
  	"style": "Ukiyo-e",
  	"color_scheme": "Vibrant reds against a serene background",
  	"feel": "Stunning and majestic",
  	"setting": "Mount Fuji with a red tint, seen from a distance",
  	"theme": "Presents the iconic Mount Fuji in various moods and seasons",
  	"technical_style": "Hokusai's meticulous details and use of color in his ukiyo-e prints add depth and visual impact to his landscapes."
	},
	{
  	"artist": "Raja Ravi Varma",
  	"title": "Sita in Exile",
  	"year": "c. 1896",
  	"style": "Indian Academic Realism",
  	"color_scheme": "Rich and vibrant colors",
  	"feel": "Emotional and narrative",
  	"setting": "A portrayal of Sita in the forest during her exile",
  	"theme": "Captures mythological and historical themes with a realistic approach",
  	"technical_style": "Ravi Varma's blending of European academic realism with Indian themes and aesthetics defines the style of Indian academic art."
	},
	{
  	"artist": "Akira Kurosawa",
  	"title": "Ran",
  	"year": "1985",
  	"style": "Cinematic",
  	"color_scheme": "Bold and visually striking colors",
  	"feel": "Epic and tragic",
  	"setting": "An adaptation of Shakespeare's King Lear set in feudal Japan",
  	"theme": "Translates Western literature into a Japanese historical context",
  	"technical_style": "Kurosawa's masterful use of composition, color, and grand cinematography contributes to the epic and emotional impact of his films."
	},
	{
  	"artist": "Liu Bolin",
  	"title": "Hiding in the City",
  	"year": "2005 onwards",
  	"style": "Contemporary Art and Performance",
  	"color_scheme": "Camouflage against urban backdrops",
  	"feel": "Conceptual and thought-provoking",
  	"setting": "Photographs of the artist blending into various cityscapes",
  	"theme": "Addresses urbanization, identity, and visibility",
  	"technical_style": "Liu Bolin's innovative performance art and photography create a visual commentary on the complexities of urban life and individuality."
	},
	{
  	"artist": "Kim Jung Gi",
  	"title": "Urban Sketches",
  	"year": "Contemporary",
  	"style": "Illustration and Urban Sketching",
  	"color_scheme": "Realistic and vivid colors",
  	"feel": "Dynamic and immersive",
  	"setting": "Detailed illustrations of urban scenes and characters",
  	"theme": "Showcases the artist's astonishing drawing skills and imaginative scenes",
  	"technical_style": "Kim Jung Gi's incredible ability to create intricate scenes from memory, emphasizing perspective and intricate details, defines his unique illustrative approach."
	},

	{
  	"artist": "El Anatsui",
  	"title": "Dzesi II",
  	"year": "1990",
  	"style": "Contemporary African Art",
  	"color_scheme": "Metallic and earthy tones",
  	"feel": "Intricate and reflective",
  	"setting": "A large-scale sculpture made from discarded materials",
  	"theme": "Repurposes discarded materials to create artworks that reflect African traditions and colonial history",
  	"technical_style": "Anatsui's unique technique of transforming discarded materials like bottle caps into monumental installations explores themes of history, culture, and sustainability."
	},
	{
  	"artist": "Romuald Hazoumè",
  	"title": "La Bouche du Roi (The Mouth of the King)",
  	"year": "1997",
  	"style": "Contemporary African Art",
  	"color_scheme": "Earth tones with pops of vibrant colors",
  	"feel": "Powerful and evocative",
  	"setting": "A mask-like assemblage made from found objects",
  	"theme": "Addresses the historical and cultural impact of the transatlantic slave trade",
  	"technical_style": "Hazoumè's assemblage technique, using found objects and traditional African art forms, creates thought-provoking artworks that engage with history and identity."
	},
	{
  	"artist": "Malick Sidibé",
  	"title": "Nuit de Noël (Happy Club)",
  	"year": "1963",
  	"style": "Photography",
  	"color_scheme": "Black and white with striking contrasts",
  	"feel": "Lively and nostalgic",
  	"setting": "A candid photograph capturing a lively dance party",
  	"theme": "Documents the exuberant youth culture of Mali in the 1960s",
  	"technical_style": "Sidibé's candid and empathetic photography captures the spirit of post-colonial Mali and its vibrant youth culture."
	},
	{
  	"artist": "Ablade Glover",
  	"title": "Market Women",
  	"year": "1983",
  	"style": "Contemporary African Art",
  	"color_scheme": "Vivid and dynamic colors",
  	"feel": "Energetic and bustling",
  	"setting": "A bustling market scene with colorful stalls and women",
  	"theme": "Celebrates the vibrant culture and commerce of Ghana",
  	"technical_style": "Glover's energetic brushwork and use of vibrant colors create a lively atmosphere that captures the essence of bustling market scenes."
	},
	{
  	"artist": "Yinka Shonibare",
  	"title": "The Swing (After Fragonard)",
  	"year": "2001",
  	"style": "Contemporary African Art",
  	"color_scheme": "Bold and contrasting colors",
  	"feel": "Whimsical and subversive",
  	"setting": "A reimagined version of Fragonard's Rococo painting 'The Swing'",
  	"theme": "Explores post-colonial identity and cultural appropriation",
  	"technical_style": "Shonibare's fusion of historical Western art with African influences challenges conventional narratives and addresses complex issues of identity and colonialism."
	},
	{
  	"artist": "William Kentridge",
  	"title": "The Soho Eckstein Series",
  	"year": "1989-2003",
  	"style": "Contemporary African Art and Animation",
  	"color_scheme": "Monochromatic and sepia tones",
  	"feel": "Cerebral and introspective",
  	"setting": "A series of drawings, prints, and animations depicting a fictional businessman's life",
  	"theme": "Critiques apartheid, capitalism, and the human condition",
  	"technical_style": "Kentridge's use of drawing, animation, and allegory creates visually and conceptually layered artworks that engage with South Africa's complex history."
	},




	{
  	"artist": "Chéri Samba",
  	"title": "J'aime la couleur (I Like the Color)",
  	"year": "1982",
  	"style": "Contemporary African Art",
  	"color_scheme": "Vibrant and bold colors",
  	"feel": "Lively and playful",
  	"setting": "A self-portrait of the artist surrounded by colorful patterns",
  	"theme": "Celebrates African culture, identity, and the power of art",
  	"technical_style": "Samba's colorful and narrative style, often combined with text, reflects his interest in storytelling and the role of art in society."
	},
	{
  	"artist": "Wangechi Mutu",
  	"title": "You Love Me, You Love Me Not",
  	"year": "2003",
  	"style": "Contemporary African Art and Collage",
  	"color_scheme": "Rich and layered colors",
  	"feel": "Provocative and surreal",
  	"setting": "A mixed-media collage featuring a hybrid female figure",
  	"theme": "Addresses issues of gender, race, and identity through fantastical imagery",
  	"technical_style": "Mutu's collage technique, combining various materials and textures, creates complex and thought-provoking artworks that challenge societal norms."
	},
	{
  	"artist": "Kudzanai Chiurai",
  	"title": "Genesis",
  	"year": "2011",
  	"style": "Contemporary African Art and Photography",
  	"color_scheme": "Bold and striking colors",
  	"feel": "Bold and confrontational",
  	"setting": "A photographic series that reimagines biblical stories in a contemporary African context",
  	"theme": "Engages with colonialism, power, and identity",
  	"technical_style": "Chiurai's use of photography and digital manipulation creates visually arresting compositions that challenge established narratives and provoke critical thought."
	},
	{
  	"artist": "Omar Victor Diop",
  	"title": "The Studio of Vanities",
  	"year": "2014",
  	"style": "Contemporary African Art and Photography",
  	"color_scheme": "Vibrant and theatrical colors",
  	"feel": "Theatrical and symbolic",
  	"setting": "A photographic series that reimagines historical European portraits with an African twist",
  	"theme": "Subverts Eurocentric narratives and empowers African representation",
  	"technical_style": "Diop's meticulous attention to detail and historical accuracy, combined with imaginative recontextualization, create powerful and subversive reinterpretations."
	},
	{
  	"artist": "Roméo Mivekannin",
  	"title": "Métissage (Mixing)",
  	"year": "1999",
  	"style": "Contemporary African Art and Sculpture",
  	"color_scheme": "Earth tones with contrasting elements",
  	"feel": "Thought-provoking and expressive",
  	"setting": "A mixed-media sculpture of a hybrid figure",
  	"theme": "Explores themes of cultural identity and hybridity",
  	"technical_style": "Mivekannin's use of diverse materials and forms reflects the complexity and fluidity of cultural identities in a globalized world."
	},
	{
  	"artist": "Malangatana Ngwenya",
  	"title": "The Struggle",
  	"year": "1973",
  	"style": "Contemporary African Art",
  	"color_scheme": "Energetic and symbolic colors",
  	"feel": "Powerful and emotive",
  	"setting": "A vivid painting depicting scenes of struggle and resistance",
  	"theme": "Addresses political and social issues, reflecting the Mozambican struggle for independence",
  	"technical_style": "Ngwenya's use of vibrant colors and symbolic imagery communicates powerful narratives of resistance and resilience."
	},

	{
  	"artist": "William Kentridge",
  	"title": "Ubu Tells the Truth",
  	"year": "1997",
  	"style": "Contemporary African Art and Animation",
  	"color_scheme": "Monochromatic with splashes of color",
  	"feel": "Satirical and thought-provoking",
  	"setting": "A series of animated films featuring the character Ubu Roi",
  	"theme": "Addresses political satire and absurdity in South African society",
  	"technical_style": "Kentridge's signature animation style, blending drawing, collage, and allegory, creates impactful narratives that confront societal issues."
	}
	,


	{
  	"artist": "Omar Victor Diop",
  	"title": "Diaspora",
  	"year": "2016",
  	"style": "Contemporary African Art and Photography",
  	"color_scheme": "Rich and contrasting colors",
  	"feel": "Empowering and narrative",
  	"setting": "A photographic series reimagining historical portraits with contemporary African figures",
  	"theme": "Explores themes of identity, representation, and historical legacy",
  	"technical_style": "Diop's use of historical and cultural references combined with contemporary aesthetics creates powerful visual narratives."
	},
	{
  	"artist": "Sokari Douglas Camp",
  	"title": "Battle Bus",
  	"year": "2003",
  	"style": "Contemporary African Art and Sculpture",
  	"color_scheme": "Bold and metallic colors",
  	"feel": "Energetic and defiant",
  	"setting": "A dynamic sculpture of a bus adorned with figures and symbols",
  	"theme": "Reflects the resilience and struggles of the Niger Delta people",
  	"technical_style": "Camp's sculptural technique, characterized by intricate metalwork and storytelling, conveys a sense of movement and cultural narrative."
	},
	{
  	"artist": "Aïda Muluneh",
  	"title": "The World is 9",
  	"year": "2016",
  	"style": "Contemporary African Art and Photography",
  	"color_scheme": "Vibrant and symbolic colors",
  	"feel": "Dreamlike and introspective",
  	"setting": "A series of photographs exploring identity and Ethiopian culture",
  	"theme": "Examines themes of memory, belonging, and cultural heritage",
  	"technical_style": "Muluneh's use of color, symbolism, and visual metaphor creates evocative and enigmatic photographic narratives."
	},
	{
  	"artist": "Kwame Akoto-Bamfo",
  	"title": "Nkyinkyim Installation",
  	"year": "2019",
  	"style": "Contemporary African Art and Installation",
  	"color_scheme": "Earthy and somber colors",
  	"feel": "Emotive and commemorative",
  	"setting": "A series of sculptures commemorating the lives lost during the transatlantic slave trade",
  	"theme": "Honors the memory of enslaved Africans and their resilience",
  	"technical_style": "Akoto-Bamfo's use of sculptural forms and poignant details creates a powerful and emotionally charged installation."
	}
	,

	{
  	"artist": "Claude Monet",
  	"title": "Impression, Sunrise",
  	"year": "1872",
  	"style": "Impressionism",
  	"color_scheme": "Subtle and naturalistic colors",
  	"feel": "Atmospheric and evocative",
  	"setting": "A harbor scene with boats and a rising sun",
  	"theme": "Captures the play of light, color, and atmosphere",
  	"technical_style": "Monet's loose brushwork and emphasis on capturing transient light effects are central to the Impressionist movement."
	},
	{
  	"artist": "Pierre-Auguste Renoir",
  	"title": "Luncheon of the Boating Party",
  	"year": "1881",
  	"style": "Impressionism",
  	"color_scheme": "Warm and vibrant colors",
  	"feel": "Convivial and lively",
  	"setting": "A scene of friends enjoying a leisurely meal by the Seine",
  	"theme": "Depicts leisure, social interaction, and a snapshot of Parisian life",
  	"technical_style": "Renoir's focus on capturing the effects of light on skin, fabrics, and water contributes to the charm and vibrancy of his paintings."
	},
	{
  	"artist": "Berthe Morisot",
  	"title": "The Cradle",
  	"year": "1872",
  	"style": "Impressionism",
  	"color_scheme": "Soft and delicate colors",
  	"feel": "Intimate and tender",
  	"setting": "A mother and child by a cradle",
  	"theme": "Explores domestic scenes and the bond between mother and child",
  	"technical_style": "Morisot's delicate brushwork and attention to domestic subjects challenge traditional gender roles in art."
	},
	{
  	"artist": "Edgar Degas",
  	"title": "The Dance Class",
  	"year": "1873-1876",
  	"style": "Impressionism",
  	"color_scheme": "Muted colors with pops of warm hues",
  	"feel": "Elegant and dynamic",
  	"setting": "A ballet class in progress",
  	"theme": "Captures the grace and movement of dancers",
  	"technical_style": "Degas's interest in depicting movement and his skillful rendering of human figures contribute to the sense of elegance and motion in his works."
	}
	,


	{
  	"artist": "Camille Pissarro",
  	"title": "Boulevard Montmartre at Night",
  	"year": "1897",
  	"style": "Impressionism",
  	"color_scheme": "Rich and contrasting colors",
  	"feel": "Urban and atmospheric",
  	"setting": "A bustling Parisian street scene at night",
  	"theme": "Explores city life, artificial lighting, and the play of colors",
  	"technical_style": "Pissarro's unique approach to Impressionism captures the interplay of artificial light, wet pavements, and urban energy."
	},
	{
  	"artist": "Mary Cassatt",
  	"title": "The Child's Bath",
  	"year": "1893",
  	"style": "Impressionism",
  	"color_scheme": "Soft pastels and tender hues",
  	"feel": "Intimate and nurturing",
  	"setting": "A mother bathing her child",
  	"theme": "Focuses on maternal love and the bond between mother and child",
  	"technical_style": "Cassatt's combination of Impressionist techniques with themes of domesticity and female experiences distinguishes her art."
	},
	{
  	"artist": "Alfred Sisley",
  	"title": "Snow at Louveciennes",
  	"year": "1878",
  	"style": "Impressionism",
  	"color_scheme": "Cool and serene tones",
  	"feel": "Tranquil and serene",
  	"setting": "A snowy landscape near the town of Louveciennes",
  	"theme": "Captures the effects of light and atmosphere on winter scenes",
  	"technical_style": "Sisley's dedication to depicting landscapes and his focus on capturing the subtleties of light and atmosphere define his Impressionist style."
	},
	{
  	"artist": "Gustave Caillebotte",
  	"title": "Paris Street; Rainy Day",
  	"year": "1877",
  	"style": "Impressionism",
  	"color_scheme": "Muted tones with pops of color",
  	"feel": "Urban and contemplative",
  	"setting": "A rainy Parisian street with umbrellas and pedestrians",
  	"theme": "Reflects the modernity and solitude of urban life",
  	"technical_style": "Caillebotte's use of perspective, geometry, and meticulous attention to architectural detail contribute to the precision of his Impressionist works."
	}
	,

	{
  	"artist": "Edouard Manet",
  	"title": "A Bar at the Folies-Bergère",
  	"year": "1882",
  	"style": "Impressionism",
  	"color_scheme": "Rich and atmospheric colors",
  	"feel": "Complex and enigmatic",
  	"setting": "A barmaid at the Folies-Bergère nightclub",
  	"theme": "Addresses modernity, consumerism, and human connection",
  	"technical_style": "Manet's innovative composition and exploration of reflections and spatial depth contribute to the psychological complexity of his painting."
	},
	{
  	"artist": "Armand Guillaumin",
  	"title": "Sunset at Ivry",
  	"year": "1873",
  	"style": "Impressionism",
  	"color_scheme": "Warm and vibrant colors",
  	"feel": "Vivid and atmospheric",
  	"setting": "A sunset over the rooftops of Ivry-sur-Seine",
  	"theme": "Explores the effects of light and color in natural landscapes",
  	"technical_style": "Guillaumin's use of bold colors and impasto technique creates an intense and luminous portrayal of light and atmosphere."
	},
	{
  	"artist": "Frédéric Bazille",
  	"title": "The Artist's Studio - Rue de la Condamine",
  	"year": "1870",
  	"style": "Impressionism",
  	"color_scheme": "Harmonious and subdued tones",
  	"feel": "Introspective and artistic",
  	"setting": "A depiction of the artist's studio and friends",
  	"theme": "Examines the artistic process and camaraderie among artists",
  	"technical_style": "Bazille's attention to detail and his inclusion of friends and fellow artists capture the spirit of creative collaboration."
	},
	{
  	"artist": "Eva Gonzalès",
  	"title": "A Loge at the Théâtre des Italiens",
  	"year": "1874",
  	"style": "Impressionism",
  	"color_scheme": "Elegant and refined colors",
  	"feel": "Stylish and contemplative",
  	"setting": "A woman in a theater box observing the performance",
  	"theme": "Examines the act of observation and the role of women in society",
  	"technical_style": "Gonzalès's focus on modern subjects and her skillful depiction of interiors reflect her role as a pioneering female Impressionist."
	}
	,

	{
  	"artist": "Salvador Dalí",
  	"title": "The Persistence of Memory",
  	"year": "1931",
  	"style": "Surrealism",
  	"color_scheme": "Dreamlike and muted colors",
  	"feel": "Dreamy and unsettling",
  	"setting": "A surreal landscape with melting watches",
  	"theme": "Explores the fluidity of time and the subconscious mind",
  	"technical_style": "Dalí's precise technique and juxtaposition of dreamlike elements create a sense of disorientation and intrigue."
	},
	{
  	"artist": "René Magritte",
  	"title": "The Son of Man",
  	"year": "1964",
  	"style": "Surrealism",
  	"color_scheme": "Subdued tones with pops of color",
  	"feel": "Mysterious and thought-provoking",
  	"setting": "A self-portrait with a hovering green apple obscuring the face",
  	"theme": "Plays with notions of identity, concealment, and perception",
  	"technical_style": "Magritte's meticulous rendering and use of visual paradoxes challenge the viewer's perception and engage with philosophical concepts."
	},
	{
  	"artist": "Max Ernst",
  	"title": "The Horde",
  	"year": "1927",
  	"style": "Surrealism",
  	"color_scheme": "Eerie and earthy colors",
  	"feel": "Surreal and unsettling",
  	"setting": "A fantastical landscape with strange creatures",
  	"theme": "Creates an unsettling and dreamlike atmosphere",
  	"technical_style": "Ernst's use of frottage (rubbing) and decalcomania (pressing) techniques adds texture and spontaneity to his surreal compositions."
	},
	{
  	"artist": "Joan Miró",
  	"title": "The Tilled Field",
  	"year": "1923-1924",
  	"style": "Surrealism",
  	"color_scheme": "Vivid and primary colors",
  	"feel": "Playful and whimsical",
  	"setting": "An abstract landscape with biomorphic shapes",
  	"theme": "Expresses a playful and imaginative view of the world",
  	"technical_style": "Miró's use of biomorphic forms, bold colors, and spontaneous brushwork reflects his childlike wonder and exploration of the subconscious."
	}
	,

	{
  	"artist": "Yves Tanguy",
  	"title": "Indefinite Divisibility",
  	"year": "1942",
  	"style": "Surrealism",
  	"color_scheme": "Eerie and atmospheric colors",
  	"feel": "Otherworldly and mysterious",
  	"setting": "A surreal landscape with organic forms and strange structures",
  	"theme": "Invites viewers into a fantastical and enigmatic realm",
  	"technical_style": "Tanguy's precise rendering of surreal landscapes and his exploration of strange forms contribute to the surreal atmosphere of his paintings."
	},
	{
  	"artist": "Rene Magritte",
  	"title": "The Treachery of Images",
  	"year": "1928-1929",
  	"style": "Surrealism",
  	"color_scheme": "Subdued tones with stark contrasts",
  	"feel": "Intellectual and playful",
  	"setting": "A painting of a pipe with the text 'Ceci n'est pas une pipe' (This is not a pipe)",
  	"theme": "Questions the relationship between images and reality",
  	"technical_style": "Magritte's exploration of semiotics and image-text relationships challenges conventional modes of representation."
	},
	{
  	"artist": "Leonora Carrington",
  	"title": "The Pomps of the Subsoil",
  	"year": "1947",
  	"style": "Surrealism",
  	"color_scheme": "Muted and earthy colors",
  	"feel": "Mystical and symbolic",
  	"setting": "A dreamlike scene with mythical creatures",
  	"theme": "Expresses a personal mythology and inner world",
  	"technical_style": "Carrington's detailed rendering of fantastical creatures and her exploration of psychological and mythological themes define her surrealist style."
	},
	{
  	"artist": "Salvador Dalí",
  	"title": "The Elephants",
  	"year": "1948",
  	"style": "Surrealism",
  	"color_scheme": "Dreamlike and muted colors",
  	"feel": "Ethereal and imaginative",
  	"setting": "A desert landscape with elongated, spindly-legged elephants",
  	"theme": "Invokes a dreamlike and surreal atmosphere",
  	"technical_style": "Dalí's precise rendering and the dreamlike quality of his imagery transport viewers to a realm of fantastical possibilities."
	},

	{
  	"artist": "Jackson Pollock",
  	"title": "Number 1A, 1948",
  	"year": "1948",
  	"style": "Abstract Expressionism",
  	"color_scheme": "Dynamic and contrasting colors",
  	"feel": "Energetic and spontaneous",
  	"setting": "An expansive canvas covered in drips, splatters, and lines",
  	"theme": "Explores the act of painting as a physical and emotional expression",
  	"technical_style": "Pollock's 'drip painting' technique, characterized by controlled chaos and gestural movements, captures the energy and emotions of the artist's process."
	},
	{
  	"artist": "Willem de Kooning",
  	"title": "Woman I",
  	"year": "1950-1952",
  	"style": "Abstract Expressionism",
  	"color_scheme": "Bold and vibrant colors",
  	"feel": "Intense and gestural",
  	"setting": "A monumental painting of a female figure",
  	"theme": "Examines the complexity and emotional depth of human form and identity",
  	"technical_style": "De Kooning's dynamic brushwork and exploration of figurative abstraction create a powerful and emotive representation of the human figure."
	},
	{
  	"artist": "Mark Rothko",
  	"title": "No. 61 (Rust and Blue)",
  	"year": "1953",
  	"style": "Abstract Expressionism",
  	"color_scheme": "Subdued and contemplative colors",
  	"feel": "Transcendent and meditative",
  	"setting": "A large canvas with stacked rectangles of color",
  	"theme": "Invites viewers to engage with color, form, and emotion on a spiritual level",
  	"technical_style": "Rothko's signature 'color field' technique and exploration of emotional states through color create a transcendent and contemplative experience."
	},
	{
  	"artist": "Franz Kline",
  	"title": "Chief",
  	"year": "1950",
  	"style": "Abstract Expressionism",
  	"color_scheme": "Bold black and white contrasts",
  	"feel": "Bold and assertive",
  	"setting": "An energetic composition of bold black brushstrokes",
  	"theme": "Emphasizes the power of gesture and form",
  	"technical_style": "Kline's large and dynamic brushwork creates a sense of urgency and raw expression, defining his approach to Abstract Expressionism."
	},

	{
  	"artist": "Lee Krasner",
  	"title": "The Eye is the First Circle",
  	"year": "1960",
  	"style": "Abstract Expressionism",
  	"color_scheme": "Vibrant and dynamic colors",
  	"feel": "Energetic and rhythmic",
  	"setting": "An abstract composition with bold brushwork and organic shapes",
  	"theme": "Showcases the artist's bold approach to color and form",
  	"technical_style": "Krasner's combination of gestural brushwork, dynamic compositions, and exploration of color create a sense of movement and emotional intensity."
	},
	{
  	"artist": "Helen Frankenthaler",
  	"title": "Mountains and Sea",
  	"year": "1952",
  	"style": "Abstract Expressionism",
  	"color_scheme": "Soft and atmospheric colors",
  	"feel": "Lyrical and harmonious",
  	"setting": "An abstract composition with poured and stained pigments",
  	"theme": "Explores the interplay between color, gesture, and the canvas",
  	"technical_style": "Frankenthaler's innovative 'soak-stain' technique and her focus on color as a carrier of emotional meaning define her abstract style."
	},
	{
  	"artist": "Joan Mitchell",
  	"title": "Ladybug",
  	"year": "1957",
  	"style": "Abstract Expressionism",
  	"color_scheme": "Bold and vibrant colors",
  	"feel": "Energetic and emotional",
  	"setting": "An exuberant composition with sweeping brushstrokes",
  	"theme": "Expresses emotional intensity and artistic energy",
  	"technical_style": "Mitchell's dynamic and expressive brushwork, combined with her use of color and composition, captures the emotional depth of her artistic process."
	},
	{
  	"artist": "Sam Francis",
  	"title": "Big Red",
  	"year": "1953",
  	"style": "Abstract Expressionism",
  	"color_scheme": "Bold reds and contrasting hues",
  	"feel": "Vibrant and expansive",
  	"setting": "A composition of bold red brushstrokes and vibrant color fields",
  	"theme": "Celebrates the expressive potential of color and form",
  	"technical_style": "Francis's use of color as a central expressive element and his emphasis on abstraction define his contribution to Abstract Expressionism."
	},

	{
  	"artist": "Andy Warhol",
  	"title": "Campbell's Soup Cans",
  	"year": "1962",
  	"style": "Pop Art",
  	"color_scheme": "Bold and vibrant colors",
  	"feel": "Iconic and commercial",
  	"setting": "A series of paintings depicting Campbell's soup cans",
  	"theme": "Critiques consumer culture and mass production",
  	"technical_style": "Warhol's use of repetition and commercial imagery challenges traditional notions of art and blurs the line between high and low culture."},
    

    {
        "artist": "Leonardo da Vinci",
        "title": "Mona Lisa",
        "year": "1503-1506",
        "style": "High Renaissance",
        "color_scheme": "Subdued earth tones with warm colors",
        "feel": "Enigmatic and serene",
        "setting": "A woman against a distant landscape with a river and bridge",
        "theme": "Human identity and emotion",
        "technical_style": "Leonardo's use of sfumato, blending and softening outlines, creates a lifelike and mysterious atmosphere."
    },
    # Add more paintings here...
]

# Function to generate random prompts
def generate_random_prompt(paintings):
    random_prompt = []
    
    # Randomly select aspects from different paintings
    for aspect in paintings[0]:
        random_painting = random.choice(paintings)
        random_prompt.append(random_painting[aspect])
    
    prompt_text = ". ".join(random_prompt)  # Join with commas
    prompt_text += " --ar 16:9 --chaos 100"  # Add the specified parameters
    return prompt_text

# Generate the markdown prompt
def generate_markdown_prompt(prompt_text):
    markdown_prompt = f"/imagine prompt:{prompt_text}\n"
    return markdown_prompt

# Generate and print a random markdown prompt
random_prompt_text = generate_random_prompt(paintings)
markdown_prompt = generate_markdown_prompt(random_prompt_text)
print(markdown_prompt)
