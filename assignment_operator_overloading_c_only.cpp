// 此题仅针对C++有效

class Solution {
public:
    char *m_pData;
    Solution() {
        this->m_pData = NULL;
    }
    Solution(char *pData) {
        this->m_pData = pData;
    }

    // Implement an assignment operator
    Solution operator=(const Solution &object) {
        // write your code here
        if (this != &object) {
            delete[] m_pData;
            if (object.m_pData != NULL) {
                int len = strlen(object.m_pData);
                m_pData = new char[len + 1];
                strcpy(m_pData, object.m_pData);
            }
            else {
                m_pData = NULL;
            }
        }
        return *this;
    }
};

// medium: http://lintcode.com/zh-cn/problem/assignment-operator-overloading-c-only/
