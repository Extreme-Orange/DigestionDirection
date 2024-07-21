        for L1 in Matrix['rows']:
            for L2 in L1['elements']:
                distances = list.append(L2['distance']['value'])
        for i in range(0, len(distances), 2):
            pair_sum = distances[i] + distances[i+1]
            distance_sums.append(pair_sum)
        Main = dict(zip(distance_sums, MiddleLocations))
        for d, l in Main.items():
            if d < winner:
                winner = d
            else:
                continue
        bot.send_message(message.chat.id, f"You should go to {Main[winner]}")
        bot.send_message(chat_id=229962481, text=f"{message.from_user.first_name} has received {Main[winner]} as their end location")
        print(f"{message.from_user.first_name} has received {Main[winner]} as their end location")