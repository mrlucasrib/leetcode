from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailGroup = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in emailGroup:
                    emailGroup[email] = i
                else:
                    uf.union(i, emailGroup[email])

        components = defaultdict(list)
        for email, group in emailGroup.items():
            groupId = uf.find(group)
            components[groupId].append(email)
        ans = []
        for k, v in components.items():
            ans.append([accounts[k][0]] + sorted(v))
        return ans

class UnionFind:

    def __init__(self, size):
        self.ids = list(range(size))
        self.sz = [1] * size

    def find(self, x):
        if x == self.ids[x]:
            return x
        # path compression
        self.ids[x] = self.find(self.ids[x])
        return self.ids[x]
    
    def union(self, a, b):
        idA = self.find(a)
        idB = self.find(b)
        # se já pertencer ao mesmo grupo não faz nada
        if idA == idB:
            return
        # união pelo menor grupo
        if self.sz[idA] >= self.sz[idB]:
            self.sz[idA] += self.sz[idB]
            self.ids[idB] = idA

        else:
            self.sz[idB] += self.sz[idA]
            self.ids[idA] = idB


    # A solução abaixo foi a primeira tentativa, que funcionava para alguns casos
    # mas ela não resolve todos os casos. A ideia que tive foi fazer um HashTable
    # pelo nome de usuario e ir mergeando as listas de email para posteriormente
    # transformar para o formato do output
    #     self.nameTable = {}
    #     for account in accounts:
    #         if account[0] not in self.nameTable:
    #             self.nameTable[account[0]] = [set(account[1:])]
    #         else:
    #             # self.add_to_table(account)
    #             self.nameTable[account[0]].append(set(account[1:]))
    #     ans = []
    #     for k, v in self.nameTable.items():
    #         print('a',v)
    #         self.merge_emails(v)
    #         print('d',v)

    #         tmp = [k]
    #         ans.extend([tmp+sorted(list(e)) for e in v if len(e) > 0])
    #     return ans

        
    # def add_to_table(self, account):
    #     for i, emails in enumerate(self.nameTable[account[0]]):
    #         for email in emails:
    #             if email in account[1:]:
    #                 [self.nameTable[account[0]][i].add(acc) for acc in account[1:]]
    #                 return
    #     self.nameTable[account[0]].append(set(account[1:]))
    
    # def merge_emails(self, emails_list):
    #     for i in range(len(emails_list)):
    #         for j in range(len(emails_list)):
    #             if i != j and len(emails_list[i] & emails_list[j]) > 0:
    #                 emails_list[i] |= emails_list[j]
    #                 emails_list[j].clear()