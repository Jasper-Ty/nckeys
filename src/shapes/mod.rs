use crate::shape::Shape;

pub fn triangle(n: usize) -> Shape {
    let mut v = vec![];

    for i in 0..n {
        for j in 0..n-i {
            v.push((i,j));
        }
    }

    Shape::from(v)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn triangle_0() {
        let left = triangle(0);
        let right = Shape::from(vec![]);

        assert_eq!(left, right)
    }

    #[test]
    fn triangle_1() {
        let left = triangle(1);
        let right = Shape::from(vec![
            (0,0)
        ]);

        assert_eq!(left, right)
    }

    #[test]
    fn triangle_2() {
        let left = triangle(2);
        let right = Shape::from(vec![
            (0,0), (0,1),
            (1,0),
        ]);

        assert_eq!(left, right)
    }

    #[test]
    fn triangle_3() {
        let left = triangle(3);
        let right = Shape::from(vec![
            (0,0), (0,1), (0,2),
            (1,0), (1,1),
            (2,0)
        ]);

        assert_eq!(left, right)
    }
}