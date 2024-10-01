// shapes.cpp
#include <iostream>
using namespace std;

class Shape {
public:
    virtual void area() = 0; // Pure virtual function
};

class Rectangle : public Shape {
private:
    int width, height;
public:
    Rectangle(int w, int h) : width(w), height(h) {}
    void area() override {
        cout << "Rectangle area: " << width * height << endl;
    }
};

class Circle : public Shape {
private:
    int radius;
public:
    Circle(int r) : radius(r) {}
    void area() override {
        cout << "Circle area: " << 3.14 * radius * radius << endl;
    }
};

// Usage
int main() {
    Shape* shapes[2];
    shapes[0] = new Rectangle(5, 6);
    shapes[1] = new Circle(3);

    for (int i = 0; i < 2; ++i) {
        shapes[i]->area();
    }

    // Clean up
    delete shapes[0];
    delete shapes[1];
    
    return 0;
}
