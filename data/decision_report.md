# Decision Report

- generated_at: 2026-08-16T12:21:37.223411+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11736**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11736, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.09% | **-0.07%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.26% | **-0.19%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.26% | **-0.21%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.69% | **-0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.86% | **+1.77%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.06% | **+1.55%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.19% | **+1.32%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.43% | **+1.22%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.24% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4114件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.89** / 初期 $100.00 (+54.89%)
- 確定: 1783件 (Win 495 / Loss 417 / Flat 871) / skip 3364件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $154.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.38** / 初期 $100.00 (+19.38%)
- 確定: 1636件 (Win 496 / Loss 619 / Flat 521) / pending 6件 / skip 1571件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000192 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.38

## 6. Latest Market Context

- 更新: 2026-08-16T12:21:27.624443+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=62990.5
- Funnel: target 986 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +18.64% | $1,407,920.77 |
| SPORTFUN/USDT:USDT | +17.61% | $4,803,428.31 |
| VELVET/USDT:USDT | +15.86% | $30,144,939.09 |
| BTW/USDT:USDT | +14.54% | $12,594,960.28 |
| CHIP/USDT:USDT | +13.55% | $5,362,954.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYRUP/USDT:USDT | below_1h_threshold | +2.69% | +2.67% |
| BTW/USDT:USDT | below_1h_threshold | +2.52% | +2.50% |
| PRL/USDT:USDT | below_1h_threshold | +2.37% | +2.35% |
| VELVET/USDT:USDT | below_1h_threshold | +1.68% | +1.67% |
| XAI/USDT:USDT | below_1h_threshold | +1.18% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
