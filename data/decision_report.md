# Decision Report

- generated_at: 2026-06-15T13:36:15.056335+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6784**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=6784, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.95% | **+0.86%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.95% | **+0.71%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.87% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.06% | **+0.02%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.02%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.22% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.61** / 初期 $100.00 (+73.61%)
- 確定: 1657件 (Win 431 / Loss 515 / Flat 711) / skip 1688件
- 成長率目線: 平均log +0.000333 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $173.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.27** / 初期 $100.00 (-1.73%)
- 確定: 145件 (Win 28 / Loss 27 / Flat 90) / skip 50件
- 成長率目線: 平均log -0.000120 / 幾何平均 -0.012% per trade / maxDD +2.37%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0126 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $98.27

## 5. Latest Market Context

- 更新: 2026-06-15T13:36:07.758033+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=66777.2
- Funnel: target 771 → liquid 150 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.2 >= 65=1, 4h RSI 68.5 >= 65=1, 4h RSI 69.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +82.34% | $5,324,295.09 |
| EVAA/USDT:USDT | +63.75% | $35,537,907.22 |
| CLO/USDT:USDT | +38.75% | $2,335,354.31 |
| UAI/USDT:USDT | +31.36% | $3,722,186.04 |
| ZRO/USDT:USDT | +29.26% | $2,543,216.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_relative_strength | +5.22% | +4.85% |
| 1000BONK/USDT:USDT | below_1h_threshold | +4.00% | +3.62% |
| ZRO/USDT:USDT | below_1h_threshold | +3.10% | +2.73% |
| JTO/USDT:USDT | below_1h_threshold | +3.04% | +2.67% |
| BSB/USDT:USDT | below_1h_threshold | +2.57% | +2.19% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
