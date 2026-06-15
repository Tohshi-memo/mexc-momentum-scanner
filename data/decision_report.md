# Decision Report

- generated_at: 2026-06-15T13:22:53.116925+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6783**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6783, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.69% | **+0.66%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.56% | **+0.36%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.52% | **+0.34%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.73% | **+0.22%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$174.48** / 初期 $100.00 (+74.48%)
- 確定: 1656件 (Win 431 / Loss 514 / Flat 711) / skip 1688件
- 成長率目線: 平均log +0.000336 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $174.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.27** / 初期 $100.00 (-1.73%)
- 確定: 145件 (Win 28 / Loss 27 / Flat 90) / skip 49件
- 成長率目線: 平均log -0.000120 / 幾何平均 -0.012% per trade / maxDD +2.37%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $98.27

## 5. Latest Market Context

- 更新: 2026-06-15T13:22:46.558065+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.41% price=66798.1
- Funnel: target 771 → liquid 149 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +101.27% | $33,795,747.94 |
| ASTEROID/USDT:USDT | +82.86% | $5,275,811.10 |
| CLO/USDT:USDT | +44.48% | $2,289,851.31 |
| UAI/USDT:USDT | +31.36% | $3,647,107.80 |
| ZRO/USDT:USDT | +29.40% | $2,407,209.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_relative_strength | +5.03% | +4.62% |
| 1000BONK/USDT:USDT | below_1h_threshold | +4.65% | +4.24% |
| ZRO/USDT:USDT | below_1h_threshold | +3.04% | +2.63% |
| FLOKI/USDT:USDT | below_1h_threshold | +2.92% | +2.51% |
| JUP/USDT:USDT | below_1h_threshold | +2.47% | +2.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
