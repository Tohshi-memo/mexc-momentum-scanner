# Decision Report

- generated_at: 2026-08-26T12:11:27.141363+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12704**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=12704, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/18 | 50.0% | +2.42% | **+1.21%** |
| LIMIT_ATR | 17/20 | 85.0% | +1.06% | **+0.90%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.59% | **+0.47%** |
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.51% | **+1.06%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.09% | **+0.71%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.28% | **+0.58%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.47% | **+0.21%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.53% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$700.48** / 初期 $100.00 (+600.48%)
- 確定: 4603件 (Win 1400 / Loss 1513 / Flat 1690) / skip 4662件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $700.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.61** / 初期 $100.00 (+57.61%)
- 確定: 1999件 (Win 544 / Loss 481 / Flat 974) / skip 4116件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0974 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $157.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.61** / 初期 $100.00 (+16.61%)
- 確定: 1976件 (Win 580 / Loss 753 / Flat 643) / pending 4件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000354 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.61

## 6. Latest Market Context

- 更新: 2026-08-26T12:11:16.370526+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=78408.6
- Funnel: target 1023 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +248.97% | $17,534,292.55 |
| BMT/USDT:USDT | +50.21% | $15,722,613.69 |
| TAC/USDT:USDT | +43.69% | $7,302,233.60 |
| LONGXIA/USDT:USDT | +30.88% | $1,988,600.06 |
| PORTAL/USDT:USDT | +16.93% | $4,099,598.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +3.84% | +3.89% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.68% | +1.72% |
| HEI/USDT:USDT | below_1h_threshold | +1.04% | +1.09% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.03% | +1.08% |
| SOXS/USDT:USDT | below_1h_threshold | +0.85% | +0.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
