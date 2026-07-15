# Decision Report

- generated_at: 2026-07-15T18:31:20.319104+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8758**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.80% / filled 20/20。**
- 全期間 MARKET基準: n=8758, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.80% | **+1.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.02% | **+1.51%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.60% | **+1.36%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.29% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.45% | **+0.20%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.24% | **+0.12%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.07% | **+0.04%** |
| MARKET_LONG | 20/20 | 100.0% | -0.05% | **-0.05%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 98件 (TP 34 / SL 62 / EXP 2)
- 最新: MAGMA/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$341.20** / 初期 $100.00 (+241.20%)
- 確定: 2882件 (Win 902 / Loss 937 / Flat 1043) / skip 2437件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAC/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $341.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.77** / 初期 $100.00 (+5.77%)
- 確定: 722件 (Win 167 / Loss 167 / Flat 388) / skip 1447件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1104 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DODO/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $105.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 165件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000277 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-15T18:31:13.604795+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=65068.0
- Funnel: target 871 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CAP/USDT:USDT | +7.67% | $1,185,597.42 |
| SNDKSTOCK/USDT:USDT | +6.65% | $107,813,619.32 |
| LDO/USDT:USDT | +5.59% | $3,528,794.08 |
| ORDI/USDT:USDT | +5.12% | $3,493,282.45 |
| SKHYSTOCK/USDT:USDT | +4.98% | $20,992,289.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +4.83% | +4.76% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.78% | +4.71% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.85% | +2.78% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.80% | +2.73% |
| DRAM/USDT:USDT | below_1h_threshold | +2.54% | +2.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
