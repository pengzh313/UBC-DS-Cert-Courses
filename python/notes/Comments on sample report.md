The below was Peng'comments regarding the course provided sample report. The comments had been shared with the course instructor.

After submitting my final project yesterday, Aug 30th, I would like to share some of my thoughts on the Python course-provided sample report (Lego datasets) pertaining to our final assignment. Please note that these are just my personal opinions for your future considerations.

1. The major concern is regarding the exploratory question and the logical way to justify the question & answer. The report mentioned, “I am interested in finding out which theme has the most sets associated with it. This is interesting because, as you may know, the lego sets are based on various themes. It would be interesting to see if the themes with the most sets would match the popular culture.” The key confusion here is how should we define the “theme” in this case.

It is interpreted that there are at least two levels of the themes according to the table, themes.csv: the parent theme and themes that are part of the parent theme. Based on this assumption, I would argue with the analysis approach that the author only counted the parent themes and concluded that “Gear is the theme with the most sets”. As per the table, sets.csv, it is clear that all themes, no matter which are parent themes or non-parent themes, have their sets being listed. By removing all the non-parent themes, this report has excluded a large number of sets that are relevant to non-parent themes. Therefore, it becomes a questionable conclusion.

Here, I will not redo the analysis but would show an example to justify my argument as below:

The author did expect the Star Wars theme to have the most sets. However, as sorted from the table, themes.csv, it shows there are actually 27 Star Wars related themes including one parent theme (theme id 158) and 26 non-parent themes. Based on the last dataframe and bar plot generated in this report, it only counted the number of sets (105) from the parent theme (theme id 158) and disregarded all other Star Wars related themes. The report just created confusion for readers that the author intended to discover the popularity of Star Wars Lego sets but excluded so much available data.

If the exploratory question is clearly defined as “which theme without parent id has the most sets associated with it”, the existing methods and results in the report might be accurate but from the readers’ perspective, it would not be a meaningful question, in my opinion.

Theme id

name

parent_id

18

Star Wars

1

158

Star Wars

160

Star Wars Clone Wars

159

161

Star Wars Episode 2

159

162

Star Wars Episode 3

159

163

Star Wars Episode 4/5/6

159

164

Star Wars Episode 1

159

165

Star Wars Clone Wars

158

166

Star Wars Episode 1

158

167

Star Wars Episode 2

158

168

Star Wars Episode 3

158

169

Star Wars Episode 4/5/6

158

170

Star Wars Other

158

172

Star Wars Episode 1

171

173

Star Wars Episode 3

171

174

Star Wars Episode 4/5/6

171

175

Star Wars Episode 2

171

181

Star Wars Episode 4/5/6

180

182

Star Wars Rebels

158

183

Star Wars Expanded Universe

158

184

Star Wars Episode 7

158

185

Star Wars Rogue One

158

209

Star Wars

207

225

Star Wars

217

261

Star Wars

258

431

Star Wars

425

612

Star Wars Episode 8

158

 

It is understandable the primary object for a sample report in a Computer Programming course is to demonstrate the technical methods and coding process. But telling a story from the provided data is also considered a critical skill for data analysis practitioners. Without defining quality questions and logical organization in writing, it is hard to say turning data into insights.

2. The second concern is about the reporting style of the sample report. My background is in engineering and business administration. Objective writing rather than subject writing is one of the principles when we create technical reports or business reports. It may be a standard or common style in this type of data analysis reports to narrate the whole process and use lots of “I”. But it might be a better approach to use more impartial language in a professional manner because in most cases the audiences of reports are clients or the public.

In addition, it could be a controversial argument that I would share my understanding in regard to the following:

At the end of the References section of the report, it states that “Lets give to Ceasar what belongs to Ceasar.”

I was not born in the English language culture. By googling the above statement, it makes sense what the author would like to tell us. However, my question is whether or not this is a popular phrase in North America? If so, it may be reasonable to include it in a report but again this is a typical subject writing style. If not, it will confuse readers, especially for people whose first language is not English. Any written document is to transform information so why do we have to create extra barriers? The easiest way is to delete it.

Another point is that I am not quite sure this phrase could be considered religion-related or not. It is out of my knowledge.
