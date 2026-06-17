# Decision Report

- generated_at: 2026-06-17T22:42:25.017346+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6971**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6971, expectancy=-0.05%
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
| LIMIT_2PCT | 16/20 | 80.0% | +0.82% | **+0.65%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.61% | **+0.43%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.29% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.81% | **+2.89%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.90% | **+0.63%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.70% | **+0.56%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.69% | **+0.55%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.71** / 初期 $100.00 (+98.71%)
- 確定: 1818件 (Win 496 / Loss 573 / Flat 749) / skip 1714件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $198.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.54** / 初期 $100.00 (+2.54%)
- 確定: 244件 (Win 64 / Loss 62 / Flat 118) / skip 138件
- 成長率目線: 平均log +0.000103 / 幾何平均 +0.010% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0690 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HIGH/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $102.54

## 5. Latest Market Context

- 更新: 2026-06-17T22:42:15.777548+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.20% price=64360.1
- Funnel: target 790 → liquid 173 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +95.20% | $1,377,385.59 |
| SYN/USDT:USDT | +41.34% | $3,941,925.44 |
| ESPORTS/USDT:USDT | +27.29% | $16,424,064.35 |
| RE/USDT:USDT | +16.79% | $1,810,619.01 |
| MITO/USDT:USDT | +13.62% | $1,624,373.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +2.75% | +2.54% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.72% | +2.52% |
| XLM/USDT:USDT | below_1h_threshold | +2.17% | +1.97% |
| HBAR/USDT:USDT | below_1h_threshold | +1.86% | +1.65% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.58% | +1.38% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
