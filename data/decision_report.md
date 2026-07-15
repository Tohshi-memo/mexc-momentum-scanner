# Decision Report

- generated_at: 2026-07-15T20:11:09.211413+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8761**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.38% / filled 20/20。**
- 全期間 MARKET基準: n=8761, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.38% | **+2.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.38% | **+2.38%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.29% | **+1.94%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.42% | **+1.70%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.74% | **+0.96%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.17% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.02% | **+0.01%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.03% | **-0.02%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -2.23% | **-0.45%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 98件 (TP 34 / SL 62 / EXP 2)
- 最新: MAGMA/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$341.20** / 初期 $100.00 (+241.20%)
- 確定: 2882件 (Win 902 / Loss 937 / Flat 1043) / skip 2440件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAC/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $341.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.40** / 初期 $100.00 (+5.40%)
- 確定: 725件 (Win 167 / Loss 168 / Flat 390) / skip 1447件
- 成長率目線: 平均log +0.000073 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0942 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.35% 残高後 $105.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 169件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000265 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-15T20:11:03.651246+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64931.1
- Funnel: target 871 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.9 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +75.02% | $2,278,796.44 |
| SKL/USDT:USDT | +14.81% | $1,494,620.86 |
| CAP/USDT:USDT | +11.04% | $1,229,100.38 |
| SNXX/USDT:USDT | +9.03% | $1,301,229.41 |
| LDO/USDT:USDT | +5.47% | $4,829,035.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDO/USDT:USDT | below_1h_threshold | +4.05% | +4.04% |
| SOXL/USDT:USDT | below_1h_threshold | +2.86% | +2.86% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +2.30% | +2.29% |
| ALABSTOCK/USDT:USDT | below_1h_threshold | +1.66% | +1.66% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
