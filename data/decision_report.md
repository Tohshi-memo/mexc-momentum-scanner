# Decision Report

- generated_at: 2026-10-21T01:01:28.422449+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17084**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.46% / filled 20/20。**
- 全期間 MARKET基準: n=17084, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.46% | **+1.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.03% | **+1.93%** |
| MARKET | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.94% | **+1.36%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.09% | **+1.25%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.13% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.80% | **+0.12%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.15% | **+0.08%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.04% | **+0.03%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | -0.67% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 248件 (TP 92 / SL 149 / EXP 7)
- 最新: USELESS/USDT:USDT TP_HIT PnL +7.06% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,344.00** / 初期 $100.00 (+1244.00%)
- 確定: 6488件 (Win 1889 / Loss 2071 / Flat 2528) / skip 7157件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AERO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.84% 残高後 $1,344.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$280.10** / 初期 $100.00 (+180.10%)
- 確定: 3818件 (Win 1050 / Loss 892 / Flat 1876) / skip 6677件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0084 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $280.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5246件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000161 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-21T01:01:16.546011+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=82945.0
- Funnel: target 1084 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOOD/USDT:USDT | +22.54% | $1,807,574.40 |
| ICNT/USDT:USDT | +20.94% | $3,727,521.17 |
| SMCISTOCK/USDT:USDT | +16.60% | $1,279,677.68 |
| BTW/USDT:USDT | +12.07% | $26,726,884.15 |
| SPCXSTOCK/USDT:USDT | +8.78% | $87,212,414.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.38% | +2.43% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.63% | +1.68% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +1.24% | +1.30% |
| SNXX/USDT:USDT | below_1h_threshold | +1.14% | +1.19% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +0.98% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
