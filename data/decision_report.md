# Decision Report

- generated_at: 2026-09-23T04:26:25.155362+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15388**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.99% / filled 20/20。**
- 全期間 MARKET基準: n=15388, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.99% | **+0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.71% | **+0.64%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.38% | **+0.21%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.34% | **+1.12%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.47% | **+0.33%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.27% | **+0.22%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,161.51** / 初期 $100.00 (+1061.51%)
- 確定: 5864件 (Win 1731 / Loss 1882 / Flat 2251) / skip 6085件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,161.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5446件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.35** / 初期 $100.00 (+22.35%)
- 確定: 3124件 (Win 919 / Loss 1226 / Flat 979) / pending 5件 / skip 3737件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $122.35

## 6. Latest Market Context

- 更新: 2026-09-23T04:26:15.964988+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.52% price=87116.5
- Funnel: target 1058 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +62.92% | $1,172,830.56 |
| ALLO/USDT:USDT | +17.80% | $2,620,391.48 |
| NIL/USDT:USDT | +16.04% | $6,406,591.49 |
| MUBARAK/USDT:USDT | +15.93% | $18,694,336.98 |
| USELESS/USDT:USDT | +15.65% | $10,752,003.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_relative_strength | +5.27% | +4.75% |
| NIL/USDT:USDT | below_1h_threshold | +3.59% | +3.06% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.28% | +1.76% |
| BTW/USDT:USDT | below_1h_threshold | +1.84% | +1.32% |
| ALLO/USDT:USDT | below_1h_threshold | +1.42% | +0.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
