# Decision Report

- generated_at: 2026-06-18T08:03:23.275056+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7023**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=7023, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.30% | **+0.78%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.33% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | -0.12% | **-0.07%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$217.20** / 初期 $100.00 (+117.20%)
- 確定: 1869件 (Win 524 / Loss 594 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $217.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.77** / 初期 $100.00 (+5.77%)
- 確定: 296件 (Win 83 / Loss 80 / Flat 133) / skip 138件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0644 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GUA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $105.77

## 5. Latest Market Context

- 更新: 2026-06-18T08:03:17.987760+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=64407.2
- Funnel: target 793 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +107.99% | $40,618,703.65 |
| O/USDT:USDT | +69.50% | $3,747,562.62 |
| SYN/USDT:USDT | +64.37% | $5,545,672.59 |
| HOME/USDT:USDT | +35.39% | $2,168,912.24 |
| H/USDT:USDT | +25.45% | $31,650,607.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +0.94% | +1.04% |
| SYN/USDT:USDT | below_1h_threshold | +0.84% | +0.94% |
| SOXL/USDT:USDT | below_1h_threshold | +0.73% | +0.83% |
| HOME/USDT:USDT | below_1h_threshold | +0.64% | +0.74% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +0.63% | +0.72% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
