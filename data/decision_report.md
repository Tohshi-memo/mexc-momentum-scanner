# Decision Report

- generated_at: 2026-06-18T07:48:42.151308+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7020**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.39% / filled 20/20。**
- 全期間 MARKET基準: n=7020, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.26% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| ASK | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.15% | **+0.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.25% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$213.99** / 初期 $100.00 (+113.99%)
- 確定: 1866件 (Win 522 / Loss 593 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $213.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.42** / 初期 $100.00 (+5.42%)
- 確定: 293件 (Win 82 / Loss 79 / Flat 132) / skip 138件
- 成長率目線: 平均log +0.000180 / 幾何平均 +0.018% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0429 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $105.42

## 5. Latest Market Context

- 更新: 2026-06-18T07:48:29.802942+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.63% price=64452.1
- Funnel: target 793 → liquid 175 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +117.10% | $40,456,932.86 |
| O/USDT:USDT | +67.07% | $3,648,417.82 |
| SYN/USDT:USDT | +63.34% | $5,420,180.41 |
| HOME/USDT:USDT | +34.33% | $2,158,287.70 |
| H/USDT:USDT | +26.03% | $32,486,255.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_relative_strength | +5.53% | +4.90% |
| RUNE/USDT:USDT | below_1h_threshold | +2.83% | +2.21% |
| RIF/USDT:USDT | below_1h_threshold | +2.60% | +1.98% |
| LAB/USDT:USDT | below_1h_threshold | +2.15% | +1.53% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.89% | +1.26% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
