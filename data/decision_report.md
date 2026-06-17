# Decision Report

- generated_at: 2026-06-17T22:00:41.143580+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6970**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6970, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.84% | **+0.84%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.34% | **+0.25%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.79% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.81% | **+2.89%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.90% | **+0.63%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.70% | **+0.56%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.69% | **+0.55%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.71** / 初期 $100.00 (+98.71%)
- 確定: 1818件 (Win 496 / Loss 573 / Flat 749) / skip 1713件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $198.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.90** / 初期 $100.00 (+2.90%)
- 確定: 243件 (Win 64 / Loss 61 / Flat 118) / skip 138件
- 成長率目線: 平均log +0.000118 / 幾何平均 +0.012% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0690 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $102.90

## 5. Latest Market Context

- 更新: 2026-06-17T22:00:36.093645+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64191.1
- Funnel: target 790 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +97.43% | $1,287,002.69 |
| SYN/USDT:USDT | +56.54% | $3,375,938.17 |
| RE/USDT:USDT | +18.46% | $1,787,350.37 |
| MITO/USDT:USDT | +11.23% | $1,561,729.05 |
| UP/USDT:USDT | +9.56% | $2,698,272.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_1h_threshold | +0.51% | +0.57% |
| ALLO/USDT:USDT | below_1h_threshold | +0.30% | +0.36% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.29% | +0.35% |
| SPX500/USDT:USDT | below_1h_threshold | +0.08% | +0.14% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.08% | +0.14% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
