# Decision Report

- generated_at: 2026-08-27T23:51:11.771257+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12846**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=12846, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.59% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| MARKET_LONG | 20/20 | 100.0% | -0.17% | **-0.17%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -1.08% | **-0.43%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -1.02% | **-0.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.03** / 初期 $100.00 (+616.03%)
- 確定: 4669件 (Win 1414 / Loss 1532 / Flat 1723) / skip 4738件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $716.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4254件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.79** / 初期 $100.00 (+14.79%)
- 確定: 1988件 (Win 580 / Loss 762 / Flat 646) / pending 0件 / skip 2328件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000170 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: WIF/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.79

## 6. Latest Market Context

- 更新: 2026-08-27T23:51:02.614704+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80229.9
- Funnel: target 1019 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +25.26% | $3,785,337.71 |
| HEMI/USDT:USDT | +19.16% | $2,840,013.04 |
| BLESS/USDT:USDT | +10.35% | $7,005,051.96 |
| BTR/USDT:USDT | +9.71% | $19,019,745.59 |
| MERL/USDT:USDT | +7.50% | $1,566,683.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +3.46% | +3.50% |
| BMT/USDT:USDT | below_1h_threshold | +2.93% | +2.98% |
| BLESS/USDT:USDT | below_1h_threshold | +1.97% | +2.01% |
| BICO/USDT:USDT | below_1h_threshold | +1.88% | +1.93% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.22% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
