
def calculate_distances_chunk(points_chunk, polygons_gdf,polygons_sindex, return_attribute=None,):

    results_list = []
    for point in points_chunk:
        result = polygons_sindex.nearest(point, return_distance=True, return_all=False)
        nearest_idx = result[0][1][0]
        distance = result[1][0] * 111  # Convert to kilometers
        if return_attribute:
            attribute_value = polygons_gdf.iloc[nearest_idx][return_attribute]
            results_list.append((distance, attribute_value))
        else:
            results_list.append(distance)
    return results_list