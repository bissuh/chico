import {AbsoluteFill, useCurrentFrame, Img, staticFile} from 'remotion';
import {loadFont as loadInter} from '@remotion/google-fonts/Inter';
import {loadFont as loadJetBrains} from '@remotion/google-fonts/JetBrainsMono';

const {fontFamily: INTER} = loadInter();
const {fontFamily: MONO} = loadJetBrains();

type Item = {label: string; note?: string};

export type CleanSlideProps = {
  theme?: 'green' | 'dark' | 'light';
  layout?: 'cover' | 'statement' | 'list' | 'prompt' | 'detail';
  kicker?: string;
  title?: string;
  subtitle?: string;
  body?: string;
  items?: Item[];
  prompt?: string;
  promptLabel?: string;
  tip?: string;
  tipLabel?: string;
  footnote?: string;
  slideNo?: number;
  slideTotal?: number;
  handle?: string;
};

const palette = (theme: CleanSlideProps['theme']) => {
  if (theme === 'light')
    return {bg: '#F3EEE3', ink: '#15211E', sub: 'rgba(21,33,30,0.62)', accent: '#1F6E5F', line: 'rgba(21,33,30,0.16)', card: '#FBF8F1'};
  if (theme === 'dark')
    return {bg: '#0E1513', ink: '#FFFFFF', sub: 'rgba(255,255,255,0.66)', accent: '#46AE9A', line: 'rgba(255,255,255,0.14)', card: '#13201D'};
  // green (default, brand)
  return {bg: '#2A7A6D', ink: '#FFFFFF', sub: 'rgba(255,255,255,0.85)', accent: '#CFEFE7', line: 'rgba(255,255,255,0.28)', card: 'rgba(255,255,255,0.12)'};
};

const Texture: React.FC<{light: boolean}> = ({light}) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill
      style={{
        opacity: light ? 0.35 : 0.05,
        mixBlendMode: light ? 'multiply' : 'soft-light',
        backgroundImage: `radial-gradient(circle at ${15 + (frame % 20)}% ${25 + (frame % 18)}%, ${light ? '#000' : '#fff'} 0.5px, transparent 1.5px)`,
        backgroundSize: '6px 6px',
        pointerEvents: 'none',
      }}
    />
  );
};

const Tag: React.FC<{handle: string; c: ReturnType<typeof palette>; slideNo?: number; slideTotal?: number; footnote?: string}> = ({
  handle,
  c,
  slideNo,
  slideTotal,
  footnote,
}) => (
  <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', opacity: 0.9}}>
    <div style={{display: 'flex', alignItems: 'center', gap: 14}}>
      <Img src={staticFile('logo-b.png')} style={{height: 40, width: 'auto'}} />
      <div style={{fontFamily: INTER, fontWeight: 600, fontSize: 22, color: c.sub}}>{handle}</div>
    </div>
    <div style={{fontFamily: INTER, fontWeight: 600, fontSize: 22, color: c.sub, letterSpacing: '0.06em'}}>
      {footnote ? footnote : slideNo ? `${slideNo} / ${slideTotal ?? 7}` : ''}
    </div>
  </div>
);

export const CleanSlide: React.FC<CleanSlideProps> = ({
  theme = 'green',
  layout = 'statement',
  kicker,
  title,
  subtitle,
  items = [],
  prompt,
  promptLabel = 'Prompt',
  tip,
  tipLabel = 'Tip',
  body,
  footnote,
  slideNo,
  slideTotal,
  handle = '@thebillionperson',
}) => {
  const c = palette(theme);
  const h1 = {fontFamily: INTER, fontWeight: 800 as const, color: c.ink, lineHeight: 1.05, letterSpacing: '-0.02em'};

  return (
    <AbsoluteFill style={{backgroundColor: c.bg, fontFamily: INTER}}>
      <Texture light={theme === 'light'} />
      <AbsoluteFill style={{padding: 100, display: 'flex', flexDirection: 'column'}}>
        {kicker ? (
          <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 26, letterSpacing: '0.16em', textTransform: 'uppercase', color: c.accent}}>
            {kicker}
          </div>
        ) : <div />}

        <div style={{flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center', paddingTop: 32, paddingBottom: 32}}>
          {layout === 'cover' && (
            <div>
              {title ? <div style={{...h1, fontSize: 108}}>{title}</div> : null}
              {subtitle ? <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 42, color: c.sub, marginTop: 26, maxWidth: 820}}>{subtitle}</div> : null}
            </div>
          )}

          {layout === 'statement' && (
            <div>
              {title ? <div style={{...h1, fontSize: 92}}>{title}</div> : null}
              {subtitle ? <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 40, lineHeight: 1.35, color: c.sub, marginTop: 28, maxWidth: 820}}>{subtitle}</div> : null}
            </div>
          )}

          {layout === 'list' && (
            <div>
              {title ? <div style={{...h1, fontSize: 64, marginBottom: 36}}>{title}</div> : null}
              <div style={{display: 'flex', flexDirection: 'column'}}>
                {items.map((it, i) => (
                  <div
                    key={i}
                    style={{
                      display: 'flex',
                      gap: 26,
                      alignItems: 'baseline',
                      padding: '24px 0',
                      borderTop: i === 0 ? `2px solid ${c.line}` : 'none',
                      borderBottom: `2px solid ${c.line}`,
                    }}
                  >
                    <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 40, color: c.accent, minWidth: 54}}>{String(i + 1).padStart(2, '0')}</div>
                    <div>
                      <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 42, color: c.ink, lineHeight: 1.1}}>{it.label}</div>
                      {it.note ? <div style={{fontFamily: INTER, fontWeight: 400, fontSize: 30, color: c.sub, marginTop: 6}}>{it.note}</div> : null}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {layout === 'prompt' && (
            <div>
              {title ? <div style={{...h1, fontSize: 60, marginBottom: 28}}>{title}</div> : null}
              <div style={{background: c.card, border: `2px solid ${c.line}`, borderRadius: 22, padding: 44}}>
                <div style={{fontFamily: MONO, fontWeight: 700, fontSize: 23, letterSpacing: '0.08em', textTransform: 'uppercase', color: c.accent, marginBottom: 22}}>{promptLabel}</div>
                <div style={{fontFamily: MONO, fontWeight: 400, fontSize: 33, lineHeight: 1.5, color: c.ink}}>{prompt}</div>
              </div>
              {subtitle ? <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 32, color: c.sub, marginTop: 26}}>{subtitle}</div> : null}
            </div>
          )}

          {layout === 'detail' && (
            <div>
              {title ? <div style={{...h1, fontSize: 56, marginBottom: 26}}>{title}</div> : null}
              {body ? <div style={{fontFamily: INTER, fontWeight: 400, fontSize: 37, lineHeight: 1.46, color: c.ink, maxWidth: 880}}>{body}</div> : null}
              {tip ? (
                <div style={{marginTop: 32, padding: '22px 28px', background: c.card, border: `2px solid ${c.line}`, borderRadius: 16, maxWidth: 820}}>
                  <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 22, letterSpacing: '0.08em', textTransform: 'uppercase', color: c.accent, marginBottom: 8}}>{tipLabel}</div>
                  <div style={{fontFamily: INTER, fontWeight: 400, fontSize: 28, lineHeight: 1.36, color: c.ink}}>{tip}</div>
                </div>
              ) : null}
              {subtitle ? <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 32, color: c.sub, marginTop: 24, maxWidth: 880}}>{subtitle}</div> : null}
            </div>
          )}
        </div>

        <Tag handle={handle} c={c} slideNo={slideNo} slideTotal={slideTotal} footnote={footnote} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
