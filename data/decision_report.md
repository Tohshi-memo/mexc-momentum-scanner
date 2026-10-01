# Decision Report

- generated_at: 2026-10-01T13:06:31.826286+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15903**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15903, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.03% | **-2.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_BB3S | 5/12 | 41.7% | +0.42% | **+0.17%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +0.85% | **+0.09%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.06% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +2.64% | **+2.31%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.17% | **+2.06%** |
| MARKET_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.75% | **+1.05%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,290.46** / 初期 $100.00 (+1190.46%)
- 確定: 6018件 (Win 1782 / Loss 1936 / Flat 2300) / skip 6446件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,290.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$272.08** / 初期 $100.00 (+172.08%)
- 確定: 3556件 (Win 986 / Loss 818 / Flat 1752) / skip 5758件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1160 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $272.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4064件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000287 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T13:06:20.410826+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=83526.8
- Funnel: target 1097 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +67.27% | $19,163,409.08 |
| LONGXIA/USDT:USDT | +67.26% | $5,234,583.12 |
| NOM/USDT:USDT | +25.54% | $2,786,277.00 |
| CT/USDT:USDT | +24.00% | $6,713,548.82 |
| ACNSTOCK/USDT:USDT | +18.19% | $2,195,128.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +1.12% | +1.33% |
| BTW/USDT:USDT | below_1h_threshold | +0.71% | +0.93% |
| SYN/USDT:USDT | below_1h_threshold | +0.39% | +0.61% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.13% | +0.35% |
| MOVR/USDT:USDT | below_1h_threshold | +0.09% | +0.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
