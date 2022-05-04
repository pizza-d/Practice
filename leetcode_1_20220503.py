### Median of Two Sorted Arrays

### solution 1
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
  total = sorted(nums1 + nums2)
  l = len(total)
  if l % 2 == 0:
    i = int(l / 2)
    result = (total[i-1]+total[i]) / 2
  else:
    i = math.floor(l / 2)
    result = total[i]
  return result

### solution 2
import math
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
  total_len = len(nums1) + len(nums2)
  if total_len % 2 == 0:
    median = int(total_len / 2) + 1
    is_odd = 'false'
  else:
    median = math.ceil((total_len) / 2)
    is_odd = 'true'
    
  result = []
  n1_i = 0
  n2_i = 0
  while len(result) < median:
    if n1_i == len(nums1):
      result.append(nums2[n2_i])
      n2_i += 1
    elif n2_i == len(nums2):
      result.append(nums1[n1_i])
      n1_i += 1
    elif nums1[n1_i] < nums2[n2_i]:
      result.append(nums1[n1_i])
      n1_i += 1
    elif nums1[n1_i] > nums2[n2_i]:
      result.append(nums2[n2_i])
      n2_i += 1
    elif nums1[n1_i] == nums2[n2_i]:
      result.append(nums1[n1_i])
      result.append(nums2[n2_i])
      n1_i += 1
      n2_i += 1
  if is_odd == 'true':
      return result[median-1]
  else:
      return (result[median-2] + result[median-1]) / 2
