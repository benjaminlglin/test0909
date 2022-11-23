// @flow strict
import React from 'react';
import moment from 'moment';
import { Link } from 'gatsby';
import type { Edges } from '../../types';
import styles from './Feed.module.scss';

type Props = {
  edges: Edges
};

const Feed = ({ edges }: Props) => (
  <div className={styles['feed']}>
    {edges.map((edge) => (
      <div className={styles['feed__item']} key={edge.node.fields.slug}>
        <div className={styles['feed__item-meta']}>
          <time className={styles['feed__item-meta-time']} dateTime={moment(edge.node.frontmatter.date).format('MMMM D, YYYY')}>
            {moment(edge.node.frontmatter.date).format('YYYY/MM/DD')}
          </time>
          <span className={styles['feed__item-meta-divider']} />
          <span className={styles['feed__item-meta-category']}>
            <Link to={edge.node.fields.categorySlug} className={styles['feed__item-meta-category-link']}>{edge.node.frontmatter.category}</Link>
          </span>
        </div>
        <div className={styles['feed__item-content']}>          
          <Link to={edge.node.fields.slug}>
            <h2 className={styles['feed__item-content-title']}> 
              {edge.node.frontmatter.title}
            </h2>
            <p className={styles['feed__item-content-description']} to={edge.node.fields.slug}>{edge.node.frontmatter.description}</p>
          </Link>
        </div>
      </div>
    ))}
  </div>
);

export default Feed;
