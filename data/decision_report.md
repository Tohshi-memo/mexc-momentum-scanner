# Decision Report

- generated_at: 2026-10-16T15:46:30.393020+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16812**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.86% / filled 20/20。**
- 全期間 MARKET基準: n=16812, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.86% | **+1.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.86% | **+1.86%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.75% | **+1.66%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.08% | **+0.87%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.34% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.98% | **+0.54%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.70% | **+0.39%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定トレード: 241件 (TP 89 / SL 145 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,254.65** / 初期 $100.00 (+1154.65%)
- 確定: 6316件 (Win 1849 / Loss 2027 / Flat 2440) / skip 7057件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,254.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3688件 (Win 1027 / Loss 878 / Flat 1783) / skip 6535件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0617 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4972件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000209 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-16T15:46:13.477915+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=81643.5
- Funnel: target 1084 → liquid 178 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DNA/USDT:USDT | +88.64% | $4,026,819.02 |
| AGT/USDT:USDT | +88.36% | $11,978,452.38 |
| ICNT/USDT:USDT | +35.40% | $2,070,370.96 |
| SI/USDT:USDT | +31.20% | $2,522,497.54 |
| BR/USDT:USDT | +20.04% | $6,602,720.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICNT/USDT:USDT | below_1h_threshold | +4.72% | +5.09% |
| STBL/USDT:USDT | below_1h_threshold | +1.22% | +1.59% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.20% | +1.57% |
| BAT/USDT:USDT | below_1h_threshold | +1.10% | +1.46% |
| ZINC/USDT:USDT | below_1h_threshold | +0.50% | +0.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
