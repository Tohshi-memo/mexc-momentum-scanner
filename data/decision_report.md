# Decision Report

- generated_at: 2026-08-27T20:56:22.943951+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12837**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.17% / filled 20/20。**
- 全期間 MARKET基準: n=12837, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.17% | **+3.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.17% | **+3.17%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.35% | **+1.64%** |
| LIMIT_1PCT | 15/20 | 75.0% | +2.05% | **+1.54%** |
| LIMIT_BB3S | 6/17 | 35.3% | +1.45% | **+0.51%** |
| LIMIT_5PCT | 2/20 | 10.0% | +1.08% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.40% | **+0.77%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.02% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.03** / 初期 $100.00 (+616.03%)
- 確定: 4669件 (Win 1414 / Loss 1532 / Flat 1723) / skip 4729件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $716.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4245件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.79** / 初期 $100.00 (+14.79%)
- 確定: 1988件 (Win 580 / Loss 762 / Flat 646) / pending 0件 / skip 2323件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: WIF/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.79

## 6. Latest Market Context

- 更新: 2026-08-27T20:56:13.564220+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=79957.3
- Funnel: target 1019 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +14.58% | $1,936,953.12 |
| HEMI/USDT:USDT | +13.55% | $2,371,078.47 |
| UAI/USDT:USDT | +4.98% | $1,845,431.25 |
| BLESS/USDT:USDT | +4.55% | $5,716,429.48 |
| LIT/USDT:USDT | +3.77% | $4,888,977.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +4.97% | +4.86% |
| PROM/USDT:USDT | below_1h_threshold | +4.95% | +4.84% |
| MUU/USDT:USDT | below_1h_threshold | +4.44% | +4.33% |
| SOXL/USDT:USDT | below_1h_threshold | +2.61% | +2.51% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.28% | +2.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
