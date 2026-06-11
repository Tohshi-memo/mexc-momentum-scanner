# Decision Report

- generated_at: 2026-06-11T16:34:32.783353+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6377**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6377, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.29% | **+0.10%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.01% | **+0.00%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.75% | **+1.14%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.35% | **+0.94%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.17% | **+0.88%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.55% | **+0.64%** |
| MARKET_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.89** / 初期 $100.00 (+51.89%)
- 確定: 1294件 (Win 332 / Loss 410 / Flat 552) / skip 1644件
- 成長率目線: 平均log +0.000323 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $151.89

## 4. Latest Market Context

- 更新: 2026-06-11T16:34:29.584092+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=62681.5
- Funnel: target 782 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZBT/USDT:USDT | +4.58% | $1,142,040.68 |
| ESPORTS/USDT:USDT | +3.94% | $8,512,682.54 |
| VELVET/USDT:USDT | +3.81% | $93,129,600.03 |
| SIREN/USDT:USDT | +3.43% | $5,768,005.06 |
| HMSTR/USDT:USDT | +3.17% | $4,893,664.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZBT/USDT:USDT | below_1h_threshold | +4.59% | +4.65% |
| VELVET/USDT:USDT | below_1h_threshold | +3.87% | +3.94% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.65% | +3.72% |
| SIREN/USDT:USDT | below_1h_threshold | +3.44% | +3.51% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.31% | +3.38% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
