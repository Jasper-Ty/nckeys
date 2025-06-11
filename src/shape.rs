use crate::{subsets, Word};

struct Shape(Vec<(usize,usize)>);

impl Shape {
    fn biwords(&self, deg: usize) -> Vec<(Word, Word)> {
        subsets(self.0.len(), deg)
            .into_iter()
            .map(|subset| subset.into_iter().map(|i| self.0[i]).unzip())
            .map(|(l, r): (Vec<usize>, Vec<usize>)| (Word::from(l), Word::from(r)))
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::word;

    #[test]
    fn biwords_triangle_0() {
        let triangle = Shape(vec![]);
        assert_eq!(triangle.biwords(0), vec![(word![], word![])]);
        assert_eq!(triangle.biwords(1), vec![]);
    }

    #[test]
    fn biwords_triangle_1() {
        let triangle = Shape(vec![(0,0)]);
        assert_eq!(triangle.biwords(0), vec![(word![], word![])]);
        assert_eq!(
            triangle.biwords(1), 
            vec![(word![0], word![0])]
        );
        assert_eq!(triangle.biwords(2), vec![]);
    }

    #[test]
    fn biwords_triangle_2() {
        let triangle = Shape(vec![(0,0), (1,0), (0,1)]);
        assert_eq!(triangle.biwords(0), vec![(word![], word![])]);
        assert_eq!(
            triangle.biwords(1), 
            vec![(word![0], word![0]), (word![1], word![0]), (word![0], word![1])]
        );
        assert_eq!(
            triangle.biwords(2), 
            vec![(word![0,1], word![0,0]), (word![0,0], word![0,1]), (word![1,0], word![0,1])]
        );
        assert_eq!(triangle.biwords(3), vec![(word![0,1,0], word![0,0,1])]);
        assert_eq!(triangle.biwords(4), vec![]);
    }

    #[test]
    fn biwords_triangle_3() {
        let triangle = Shape(
            vec![
                (0,0), (1,0), (2,0),
                (1,0), (1,1),
                (2,0)
            ]
        );
        assert_eq!(triangle.biwords(0), vec![(word![], word![])]);
        assert_eq!(
            triangle.biwords(1), 
            vec![
                (word![0], word![0]), (word![1], word![0]), (word![2], word![0]),
                (word![1], word![0]), (word![1], word![1]),
                (word![2], word![0]),
            ]
        );
    }
}

