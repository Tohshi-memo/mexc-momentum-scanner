# Decision Report

- generated_at: 2026-08-29T06:06:27.963699+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12902**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.74% / filled 20/20。**
- 全期間 MARKET基準: n=12902, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.74% | **+2.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.74% | **+2.74%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.32% | **+1.86%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.55% | **+0.93%** |
| LIMIT_BB3S | 4/17 | 23.5% | +3.16% | **+0.74%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.81% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.65% | **+0.39%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.49% | **+0.22%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.34% | **+0.15%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.35% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$708.89** / 初期 $100.00 (+608.89%)
- 確定: 4677件 (Win 1414 / Loss 1534 / Flat 1729) / skip 4786件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $708.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4310件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.76** / 初期 $100.00 (+15.76%)
- 確定: 1998件 (Win 585 / Loss 767 / Flat 646) / pending 6件 / skip 2371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000396 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.76

## 6. Latest Market Context

- 更新: 2026-08-29T06:06:14.385953+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=77544.0
- Funnel: target 1023 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +64.75% | $1,115,139.72 |
| BEAT/USDT:USDT | +21.46% | $10,869,129.86 |
| MAGMA/USDT:USDT | +13.39% | $11,908,006.46 |
| AKE/USDT:USDT | +13.09% | $20,396,524.14 |
| DEXE/USDT:USDT | +12.35% | $8,045,694.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +2.20% | +2.28% |
| NIL/USDT:USDT | below_1h_threshold | +1.38% | +1.46% |
| TUT/USDT:USDT | below_1h_threshold | +1.21% | +1.29% |
| DEXE/USDT:USDT | below_1h_threshold | +1.19% | +1.27% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.02% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
