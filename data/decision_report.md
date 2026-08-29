# Decision Report

- generated_at: 2026-08-29T05:06:23.428936+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12899**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=12899, expectancy=+0.01%
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
| LIMIT_1PCT | 17/20 | 85.0% | +1.37% | **+1.16%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_BB3S | 5/16 | 31.2% | +2.54% | **+0.79%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.17% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.02% | **+3.02%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.39% | **+0.69%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.20% | **+0.42%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.16% | **+0.41%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.62% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 193件 (TP 73 / SL 115 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$708.89** / 初期 $100.00 (+608.89%)
- 確定: 4677件 (Win 1414 / Loss 1534 / Flat 1729) / skip 4783件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $708.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4307件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.17** / 初期 $100.00 (+15.17%)
- 確定: 1995件 (Win 583 / Loss 766 / Flat 646) / pending 6件 / skip 2371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000445 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $115.17

## 6. Latest Market Context

- 更新: 2026-08-29T05:06:14.123307+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77647.0
- Funnel: target 1023 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +53.67% | $1,070,884.40 |
| AKE/USDT:USDT | +18.32% | $19,689,032.54 |
| MAGMA/USDT:USDT | +16.89% | $11,669,056.64 |
| DOS/USDT:USDT | +12.69% | $1,514,618.15 |
| BEAT/USDT:USDT | +11.41% | $8,264,987.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +1.48% | +1.44% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.14% | +1.10% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.77% | +0.73% |
| SKR/USDT:USDT | below_1h_threshold | +0.70% | +0.67% |
| BEAT/USDT:USDT | below_1h_threshold | +0.65% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
