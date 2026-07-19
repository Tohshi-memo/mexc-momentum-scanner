# Decision Report

- generated_at: 2026-07-19T09:41:00.793074+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9018**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9018, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.96% | **-2.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 4/18 | 22.2% | +1.54% | **+0.34%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.98% | **+0.25%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.28% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.75% | **+4.75%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +4.15% | **+3.11%** |
| MARKET_LONG | 20/20 | 100.0% | +2.93% | **+2.93%** |
| LIMIT_3PCT_LONG | 6/20 | 30.0% | +4.31% | **+1.29%** |
| LIMIT_2PCT_LONG | 6/20 | 30.0% | +3.47% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$401.81** / 初期 $100.00 (+301.81%)
- 確定: 3080件 (Win 965 / Loss 978 / Flat 1137) / skip 2499件
- 成長率目線: 平均log +0.000452 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $401.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.64** / 初期 $100.00 (+27.64%)
- 確定: 979件 (Win 251 / Loss 198 / Flat 530) / skip 1450件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2200 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: B/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $127.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.50** / 初期 $100.00 (+0.50%)
- 確定: 220件 (Win 70 / Loss 110 / Flat 40) / pending 5件 / skip 265件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000529 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $100.50

## 6. Latest Market Context

- 更新: 2026-07-19T09:40:56.492231+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=64487.8
- Funnel: target 885 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +103.11% | $46,128,430.25 |
| BANK/USDT:USDT | +71.56% | $20,988,711.33 |
| TLM/USDT:USDT | +47.73% | $5,882,097.67 |
| B/USDT:USDT | +41.90% | $41,703,253.08 |
| BULLA/USDT:USDT | +29.55% | $1,371,441.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +4.74% | +5.03% |
| BANK/USDT:USDT | below_1h_threshold | +4.67% | +4.97% |
| B/USDT:USDT | below_1h_threshold | +3.99% | +4.28% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.63% | +1.92% |
| BILL/USDT:USDT | below_1h_threshold | +1.21% | +1.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
