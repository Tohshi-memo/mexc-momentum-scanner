# Decision Report

- generated_at: 2026-05-28T15:00:10.848388+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4969**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=4969, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.36% | **+0.82%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.76% | **+0.69%** |
| ASK | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +1.49% | **+1.28%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.66% | **+0.43%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.88% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.06** / 初期 $100.00 (+28.06%)
- 確定: 704件 (Win 173 / Loss 220 / Flat 311) / skip 826件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.06

## 4. Latest Market Context

- 更新: 2026-05-28T14:59:59.754008+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=73003.4
- Funnel: target 776 → liquid 159 → pre 50 → checked 50 → surge 4 → strict 4
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +38.38% | $4,485,963.10 |
| SNOWSTOCK/USDT:USDT | +33.29% | $11,532,667.64 |
| ONDSSTOCK/USDT:USDT | +22.69% | $1,187,364.95 |
| XLM/USDT:USDT | +20.92% | $239,805,473.01 |
| PRL/USDT:USDT | +13.33% | $2,541,281.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +4.48% | +4.46% |
| DRAM/USDT:USDT | below_1h_threshold | +3.02% | +3.00% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +3.00% | +2.98% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.69% | +2.67% |
| MYX/USDT:USDT | below_1h_threshold | +2.38% | +2.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
