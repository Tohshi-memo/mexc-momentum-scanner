# Decision Report

- generated_at: 2026-07-11T16:56:16.550772+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8542**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.83% / filled 20/20。**
- 全期間 MARKET基準: n=8542, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 9/9 | 100.0% | +1.56% | **+1.56%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.84% | **+1.47%** |
| LIMIT_ATR | 9/20 | 45.0% | +2.44% | **+1.10%** |
| LIMIT_BB3S | 2/18 | 11.1% | +8.00% | **+0.89%** |
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| MARKET_LONG | 20/20 | 100.0% | +0.19% | **+0.19%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.06% | **-0.02%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | -0.19% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$103.57** / 初期 $100.00 (+3.57%)
- 確定トレード: 84件 (TP 30 / SL 53 / EXP 1)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.57
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$317.92** / 初期 $100.00 (+217.92%)
- 確定: 2730件 (Win 862 / Loss 916 / Flat 952) / skip 2373件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $317.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1311件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0342 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.95** / 初期 $100.00 (-1.05%)
- 確定: 9件 (Win 1 / Loss 8 / Flat 0) / pending 5件 / skip 1件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000170 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.95

## 6. Latest Market Context

- 更新: 2026-07-11T16:56:05.546430+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64096.2
- Funnel: target 863 → liquid 140 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +19.52% | $46,007,523.76 |
| CASHCAT/USDT:USDT | +5.30% | $1,503,800.19 |
| BSB/USDT:USDT | +5.19% | $1,896,135.27 |
| EVAA/USDT:USDT | +4.60% | $28,257,807.64 |
| EDGE/USDT:USDT | +3.25% | $2,412,509.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.55% | +4.61% |
| EDGE/USDT:USDT | below_1h_threshold | +3.44% | +3.51% |
| XPIN/USDT:USDT | below_1h_threshold | +2.39% | +2.46% |
| CLO/USDT:USDT | below_1h_threshold | +1.92% | +1.98% |
| THETA/USDT:USDT | below_1h_threshold | +1.89% | +1.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
