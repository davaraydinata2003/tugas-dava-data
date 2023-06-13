#!/usr/bin/env python
# coding: utf-8

# In[1]:


{
 "cells": [
  {
   celltype: code,
   "execution_count": 1,
   "id": "a4d965d0",
   "metadata": {},
   outputs: [],
   source: [
    "class Node:\n",
    "    def __init__(self, value=None):\n",
    "        self.value = value\n",
    "        self.next = None\n",
    "        self.prev = None"
   ]
  
   "cell_type": "code",
   "execution_count": 2,
   "id": "e139faef",
   "metadata": {},
   "outputs": [],
   "source": [
    "class CircularDoublyLinkedList:\n",
    "    def __init__(self):\n",
    "        self.head = None\n",
    "        self.tail = None\n",
    "\n",
    "    \n",
    "    def __iter__(self):\n",
    "        node = self.head\n",
    "        while node:\n",
    "            yield node\n",
    "            node = node.next\n",
    "            if node == self.tail.next:\n",
    "                break\n",
    "    \n",
    "    #  Creation of Circular Doubly Linked List\n",
    "    def createCDLL(self, nodeValue):\n",
    "        newNode = Node(nodeValue)\n",
    "        self.head = newNode\n",
    "        self.tail = newNode\n",
    "        newNode.prev = newNode\n",
    "        newNode.next = newNode\n",
    "        return \"The CDLL is created successfully\"\n",
    "\n",
    "\n",
    "    # Insertion Method in Circular Doubly Linked List\n",
    "    def insertCDLL(self, value, location):\n",
    "        if self.head is None:\n",
    "            return \"The CDLL does not exist\"\n",
    "        else:\n",
    "            newNode = Node(value)\n",
    "            if location == 0:\n",
    "                newNode.next = self.head\n",
    "                newNode.prev = self.tail\n",
    "                self.head.prev = newNode\n",
    "                self.head = newNode\n",
    "                self.tail.next = newNode\n",
    "            elif location == 1:\n",
    "                newNode.next = self.head\n",
    "                newNode.prev = self.tail\n",
    "                self.head.prev = newNode\n",
    "                self.tail.next = newNode\n",
    "                self.tail = newNode\n",
    "            else:\n",
    "                tempNode = self.head\n",
    "                index = 0\n",
    "                while index < location - 1:\n",
    "                    tempNode = tempNode.next\n",
    "                    index += 1\n",
    "                newNode.next = tempNode.next\n",
    "                newNode.prev = tempNode\n",
    "                newNode.next.prev = newNode\n",
    "                tempNode.next = newNode\n",
    "            return \"The node has been successfully inserted\"\n",
    "\n",
    "    # Traversal of Circular Doubly Linked List\n",
    "    def traversalCDLL(self):\n",
    "        if self.head is None:\n",
    "            print(\"There is not any node for traversal\")\n",
    "        else:\n",
    "            tempNode = self.head\n",
    "            while tempNode:\n",
    "                print(tempNode.value)\n",
    "                if tempNode == self.tail:\n",
    "                    break\n",
    "                tempNode = tempNode.next\n",
    "\n",
    "    # Reverse traversal of Circular Doubly Linked List\n",
    "    def reverseTraversalCDLL(self):\n",
    "        if self.head is None:\n",
    "            print(\"There is not any node for reverse traversal\")\n",
    "        else:\n",
    "            tempNode = self.tail\n",
    "            while tempNode:\n",
    "                print(tempNode.value)\n",
    "                if tempNode == self.head:\n",
    "                    break\n",
    "                tempNode = tempNode.prev\n",
    "    \n",
    "    # Search Circular Doubly Linked List\n",
    "    def searchCDLL(self, nodeValue):\n",
    "        if self.head is None:\n",
    "            return \"There is not any node in CDLL\"\n",
    "        else:\n",
    "            tempNode = self.head\n",
    "            while tempNode:\n",
    "                if tempNode.value == nodeValue:\n",
    "                    return tempNode.value\n",
    "                if tempNode == self.tail:\n",
    "                    return \"The value does not exist in CDLL\"\n",
    "                tempNode = tempNode.next\n",
    "    \n",
    "    # Delete a node from Circular Doubly Linked List\n",
    "    def deleteNode(self, location):\n",
    "        if self.head is None:\n",
    "            print(\"There is not any node to delete\")\n",
    "        else:\n",
    "            if location == 0:\n",
    "                if self.head == self.tail:\n",
    "                    self.head.prev = None\n",
    "                    self.head.next = None\n",
    "                    self.head = None\n",
    "                    self.tail = None\n",
    "                else:\n",
    "                    self.head = self.head.next\n",
    "                    self.head.prev = self.tail\n",
    "                    self.tail.next = self.head\n",
    "            elif location == 1:\n",
    "                if self.head == self.tail:\n",
    "                    self.head.prev = None\n",
    "                    self.head.next = None\n",
    "                    self.head = None\n",
    "                    self.tail = None\n",
    "                else:\n",
    "                    self.tail = self.tail.prev\n",
    "                    self.tail.next = self.head\n",
    "                    self.head.prev = self.tail\n",
    "            else:\n",
    "                curNode = self.head\n",
    "                index = 0\n",
    "                while index < location - 1:\n",
    "                    curNode = curNode.next\n",
    "                    index += 1\n",
    "                curNode.next = curNode.next.next\n",
    "                curNode.next.prev = curNode\n",
    "            print(\"The node has been successfully deleted\")\n",
    "    \n",
    "    # Delete entire Circular Doubly Linked List\n",
    "    def deleteCDLL(self):\n",
    "        if self.head is None:\n",
    "            print(\"There is not any element to delete\")\n",
    "        else:\n",
    "            self.tail.next = None\n",
    "            tempNode = self.head\n",
    "            while tempNode:\n",
    "                tempNode.prev = None\n",
    "                tempNode = tempNode.next\n",
    "            self.head = None\n",
    "            self.tail = None\n",
    "            print(\"The CDLL has been successfully deleted\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9c7c10a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 5, 2, 1]\n"
     ]
    }
   ],
   "source": [
    "circularDLL = CircularDoublyLinkedList()\n",
    "circularDLL.createCDLL(5)\n",
    "circularDLL.insertCDLL(0,0)\n",
    "circularDLL.insertCDLL(1,1)\n",
    "circularDLL.insertCDLL(2,2)\n",
    "print([node.value for node in circularDLL])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1577e732",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The CDLL has been successfully deleted\n",
      "[]\n"
     ]
    }
   ],
   "source": [
    "circularDLL.deleteCDLL()\n",
    "print([node.value for node in circularDLL])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
 "nbformat": 4,
 "nbformat_minor": 5
}


# In[ ]:



