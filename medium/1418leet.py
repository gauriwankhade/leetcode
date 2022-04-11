class Solution(object):
    def displayTable(self, orders):
        final_dict = {}
        headers = []
        results = []

        #unique food items
        headers = sorted(list(set([item[2] for item in orders])))


        #pre-processing of order items to calculate frequency of food items
        for order in orders:
            order[1] = int(order[1])

            if not final_dict.get(order[1]) :
                final_dict[order[1]] = ['0'] * len(headers)
            
            temp = final_dict[order[1]][headers.index(order[2])]
            final_dict[order[1]][headers.index(order[2])] = str(int(temp) + 1)

        tableSorted = sorted(final_dict)
        results = [["Table"] + headers]
       
        #output format
        for item in tableSorted:
            subList = [str(item)] + final_dict[item]
            results.append(subList)
        
        return results




s = Solution()
s.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],
                ["David","3","Fried Chicken"],["Carla","5","Water"],
                ["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
                )





