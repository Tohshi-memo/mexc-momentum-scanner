# Decision Report

- generated_at: 2026-05-28T14:55:05.933789+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4968**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=4968, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 13/20 | 65.0% | +1.51% | **+0.98%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.03% | **+0.92%** |
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.88% | **+0.31%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.28% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.06** / 初期 $100.00 (+28.06%)
- 確定: 703件 (Win 173 / Loss 220 / Flat 310) / skip 826件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.06

## 4. Latest Market Context

- 更新: 2026-05-28T14:54:59.174325+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=72929.8
- Funnel: target 776 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +40.75% | $4,241,604.79 |
| SNOWSTOCK/USDT:USDT | +33.33% | $11,515,271.37 |
| ONDSSTOCK/USDT:USDT | +22.50% | $1,186,723.28 |
| XLM/USDT:USDT | +22.31% | $237,929,496.11 |
| PRL/USDT:USDT | +14.58% | $2,527,236.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.95% | +4.03% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +3.87% | +3.95% |
| DRAM/USDT:USDT | below_1h_threshold | +2.88% | +2.96% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.63% | +2.71% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.56% | +2.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
