The below was from Peng's notes regarding URL for data.world_110m

The key here is the URL for data.world_110m.

Firstly, we can read the online article via https://github.com/vega/vega-datasets

Based on the article, the Vega and Vega-Lite datasets are located via GitHub or jsDelivr (a fast CDN).

In this question, we can get the data.world_110m via two URLs:

GitHub: https://vega.github.io/vega-datasets/data/world-110m.json

or jsDelivr (a fast CDN): https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/world-110m.json

There are two ways to indicate the URL in the code:

Option 1: Directly add the URL link into the code. For example: 

world_map = alt.topo_feature("https://vega.github.io/vega-datasets/data/world-110m.json", 'countries'), Or

world_map = alt.topo_feature("https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/world-110m.json", 'countries')

Note that the test_4_1 only recognizes the github URL.

Option 2: Access the URLs of any Vega and Vega-Lite dataset with data[NAME].url ( .url is particularly defined to automatically load the URLs for distinct Vega and Vega-Lite dataset). In this case:

world_map = alt.topo_feature(world_data.url, 'countries')    (Note: we have already read data.world_110m into world_data variable)

As users, we do not need to know the specific url for data.world_110m. "world_data.url" automatically does this for us.

Till now, we can confirm the code "world_map = alt.topo_feature(world_data.url, 'countries')" is correct to extract the GeoJSON features from the world_data data for the countries object. The reason test_4_1 shows an error is the test has preloaded the answer with github URL; however, "world_data.url" automatically generates url with jsDelivr URL.

I am not sure technical details here. Based on my research so far, the ASSUMPTION is jsDelivr repositories are preferred or recommended by Vega and Vega-Lite datasets. That is why "world_data.url" had been updated to automatically generate url with jsDelivr URL not github URL. Our course materials have not been updated to keep consistent. In Module 6, the world_110m data source is also from github URL.
