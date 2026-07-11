# Decision Report

- generated_at: 2026-07-11T11:46:03.829166+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8533**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.99% / filled 20/20。**
- 全期間 MARKET基準: n=8533, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.99% | **+0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 18/18 | 100.0% | +1.00% | **+1.00%** |
| MARKET | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.64% | **+0.98%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.26% | **+0.82%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.84% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| MARKET_LONG | 20/20 | 100.0% | -0.01% | **-0.01%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | -0.87% | **-0.39%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | -1.60% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.09** / 初期 $100.00 (+4.09%)
- 確定トレード: 83件 (TP 30 / SL 52 / EXP 1)
- 最新: NES/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$319.54** / 初期 $100.00 (+219.54%)
- 確定: 2721件 (Win 861 / Loss 913 / Flat 947) / skip 2373件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAG/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $319.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1302件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.83** / 初期 $100.00 (-0.17%)
- 確定: 1件 (Win 0 / Loss 1 / Flat 0) / pending 1件 / skip 0件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAG/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $99.83

## 6. Latest Market Context

- 更新: 2026-07-11T11:45:57.893483+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=64162.3
- Funnel: target 862 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XPIN/USDT:USDT | +20.33% | $2,178,632.80 |
| BEAT/USDT:USDT | +19.28% | $31,825,682.50 |
| CASHCAT/USDT:USDT | +16.07% | $1,497,435.76 |
| HMSTR/USDT:USDT | +15.43% | $1,468,002.41 |
| VIRTUAL/USDT:USDT | +15.19% | $35,553,454.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DEXE/USDT:USDT | below_1h_threshold | +3.53% | +3.54% |
| B3/USDT:USDT | below_1h_threshold | +1.77% | +1.77% |
| TIA/USDT:USDT | below_1h_threshold | +1.74% | +1.74% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +1.43% | +1.44% |
| WLD/USDT:USDT | below_1h_threshold | +1.26% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
