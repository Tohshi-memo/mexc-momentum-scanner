# Decision Report

- generated_at: 2026-08-20T15:06:24.758325+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12054**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12054, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.63% | **-1.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -1.14% | **-0.40%** |
| LIMIT_3PCT | 14/20 | 70.0% | -1.09% | **-0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.41% | **+2.05%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.41% | **+1.56%** |
| MARKET_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.79% | **+0.98%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.47% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$610.07** / 初期 $100.00 (+510.07%)
- 確定: 4267件 (Win 1307 / Loss 1394 / Flat 1566) / skip 4348件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.20%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $610.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3644件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0032 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.69** / 初期 $100.00 (+16.69%)
- 確定: 1757件 (Win 521 / Loss 672 / Flat 564) / pending 0件 / skip 1770件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PUMPFUN/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $116.69

## 6. Latest Market Context

- 更新: 2026-08-20T15:06:14.592435+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.57% price=72200.8
- Funnel: target 1011 → liquid 201 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +61.13% | $5,512,614.84 |
| BOME/USDT:USDT | +38.51% | $16,820,356.64 |
| ACE/USDT:USDT | +36.59% | $20,288,330.71 |
| ONG/USDT:USDT | +32.99% | $3,641,976.21 |
| MAGMA/USDT:USDT | +32.57% | $10,806,985.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUMPFUN/USDT:USDT | below_relative_strength | +5.11% | +4.54% |
| ACE/USDT:USDT | below_1h_threshold | +4.95% | +4.38% |
| XPL/USDT:USDT | below_1h_threshold | +2.34% | +1.78% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.33% | +1.76% |
| GALA/USDT:USDT | below_1h_threshold | +1.88% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
