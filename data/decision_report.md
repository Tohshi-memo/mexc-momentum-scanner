# Decision Report

- generated_at: 2026-08-11T04:01:25.604196+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11219**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.37% / filled 20/20。**
- 全期間 MARKET基準: n=11219, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.37% | **+0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| MARKET | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.03% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.92% | **+0.46%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.69% | **+0.38%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.84% | **+0.21%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.31% | **+0.16%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.10% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3936件 (Win 1230 / Loss 1285 / Flat 1421) / skip 3844件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1514件 (Win 424 / Loss 361 / Flat 729) / skip 3116件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.46** / 初期 $100.00 (+16.46%)
- 確定: 1317件 (Win 407 / Loss 516 / Flat 394) / pending 6件 / skip 1373件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000154 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $116.46

## 6. Latest Market Context

- 更新: 2026-08-11T04:01:17.592487+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64110.7
- Funnel: target 962 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +99.29% | $16,581,274.47 |
| TOAD/USDT:USDT | +53.87% | $1,233,967.93 |
| BICO/USDT:USDT | +16.91% | $9,944,291.30 |
| CYS/USDT:USDT | +12.50% | $23,936,733.06 |
| COOKIE/USDT:USDT | +11.55% | $1,460,380.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TOAD/USDT:USDT | below_1h_threshold | +1.72% | +1.72% |
| BTW/USDT:USDT | below_1h_threshold | +1.32% | +1.32% |
| BICO/USDT:USDT | below_1h_threshold | +1.21% | +1.21% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.17% | +1.17% |
| KORU/USDT:USDT | below_1h_threshold | +0.99% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
