# Decision Report

- generated_at: 2026-07-11T15:56:09.509698+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8537**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.03% / filled 20/20。**
- 全期間 MARKET基準: n=8537, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.03% | **+2.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.03% | **+2.03%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.10% | **+1.57%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.19% | **+1.32%** |
| ASK | 14/14 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.50% | **+1.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.38% | **+0.84%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |
| MARKET_LONG | 20/20 | 100.0% | -0.61% | **-0.61%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -1.68% | **-0.67%** |

## 2. $100 Live Portfolio

- 残高: **$104.09** / 初期 $100.00 (+4.09%)
- 確定トレード: 83件 (TP 30 / SL 52 / EXP 1)
- 最新: NES/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$316.35** / 初期 $100.00 (+216.35%)
- 確定: 2725件 (Win 861 / Loss 915 / Flat 949) / skip 2373件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $316.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1306件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定: 4件 (Win 1 / Loss 3 / Flat 0) / pending 3件 / skip 0件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000319 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.82

## 6. Latest Market Context

- 更新: 2026-07-11T15:56:03.506771+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=64138.6
- Funnel: target 863 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +38.09% | $7,089,703.59 |
| CLO/USDT:USDT | +20.63% | $1,267,097.09 |
| ANSEM/USDT:USDT | +20.32% | $6,979,026.88 |
| VIRTUAL/USDT:USDT | +12.84% | $38,923,478.93 |
| B3/USDT:USDT | +12.65% | $1,301,489.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +4.93% | +5.22% |
| T/USDT:USDT | below_1h_threshold | +4.04% | +4.32% |
| XPIN/USDT:USDT | below_1h_threshold | +3.19% | +3.47% |
| B3/USDT:USDT | below_1h_threshold | +2.94% | +3.22% |
| AAVE/USDT:USDT | below_1h_threshold | +2.16% | +2.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
