# Decision Report

- generated_at: 2026-06-15T19:35:22.282112+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6806**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.51% / filled 20/20。**
- 全期間 MARKET基準: n=6806, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.51% | **+0.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.40% | **+0.98%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.30% | **+0.69%** |
| MARKET | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.39% | **+0.31%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.47% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.39% | **+1.11%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.42% | **+0.99%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.56% | **+0.34%** |
| ASK_LONG | 20/20 | 100.0% | +0.02% | **+0.02%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.38% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$104.05** / 初期 $100.00 (+4.05%)
- 確定トレード: 7件 (TP 5 / SL 2 / EXP 0)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$177.44** / 初期 $100.00 (+77.44%)
- 確定: 1679件 (Win 438 / Loss 524 / Flat 717) / skip 1688件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FOLKS/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.19% 残高後 $177.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 62件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0146 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-15T19:35:18.833554+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=66647.1
- Funnel: target 772 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +25.57% | $1,648,464.90 |
| EVAA/USDT:USDT | +21.98% | $43,955,188.63 |
| FOLKS/USDT:USDT | +9.40% | $1,927,529.03 |
| MRVLSTOCK/USDT:USDT | +4.96% | $14,670,669.57 |
| SPCXSTOCK/USDT:USDT | +4.88% | $190,255,401.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +3.57% | +3.69% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.78% | +2.90% |
| XLM/USDT:USDT | below_1h_threshold | +1.91% | +2.03% |
| BSB/USDT:USDT | below_1h_threshold | +1.58% | +1.70% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.00% | +1.12% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
