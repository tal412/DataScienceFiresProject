import numpy as np


def calculate_distances_chunk(points_chunk, polygons_gdf, polygons_sindex, return_attribute=None, ):
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


def find_nearest_area_codes(row, tree, gdf_points, k=10):
    point = row.geometry
    distance, indices = tree.query(np.array([[point.x, point.y]]), k=k)
    nearest_area_codes = gdf_points.iloc[indices[0]]['area_code'].values
    return nearest_area_codes
