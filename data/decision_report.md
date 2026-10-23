# Decision Report

- generated_at: 2026-10-23T02:31:27.235572+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17181**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.07% / filled 20/20。**
- 全期間 MARKET基準: n=17181, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.76% | **+1.58%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.48% | **+1.18%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.91% | **+0.55%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.88% | **+0.94%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,329.32** / 初期 $100.00 (+1229.32%)
- 確定: 6538件 (Win 1898 / Loss 2085 / Flat 2555) / skip 7204件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,329.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.89** / 初期 $100.00 (+176.89%)
- 確定: 3858件 (Win 1056 / Loss 900 / Flat 1902) / skip 6734件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0344 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.35% 残高後 $276.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5343件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000287 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T02:31:14.327898+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.45% price=81677.6
- Funnel: target 1096 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +43.62% | $11,596,602.67 |
| IRYS/USDT:USDT | +26.76% | $4,063,524.83 |
| AGT/USDT:USDT | +15.96% | $5,086,282.83 |
| DNA/USDT:USDT | +10.50% | $4,188,263.94 |
| DASH/USDT:USDT | +10.00% | $18,289,869.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +4.20% | +3.75% |
| BTW/USDT:USDT | below_1h_threshold | +3.38% | +2.93% |
| BULLA/USDT:USDT | below_1h_threshold | +2.87% | +2.42% |
| INJ/USDT:USDT | below_1h_threshold | +2.40% | +1.95% |
| AKE/USDT:USDT | below_1h_threshold | +2.31% | +1.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
