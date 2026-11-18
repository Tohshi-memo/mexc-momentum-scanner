# Decision Report

- generated_at: 2026-11-18T01:31:22.922636+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19104**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19104, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.09% | **-1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/19 | 26.3% | +0.57% | **+0.15%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.09% | **+0.05%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.31% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.55% | **+1.02%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.98% | **+0.69%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.68% | **+0.59%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.58% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$120.76** / 初期 $100.00 (+20.76%)
- 確定トレード: 280件 (TP 100 / SL 172 / EXP 8)
- 最新: MVLL/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,677.36** / 初期 $100.00 (+1577.36%)
- 確定: 7352件 (Win 2109 / Loss 2358 / Flat 2885) / skip 8313件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGU/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,677.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$431.95** / 初期 $100.00 (+331.95%)
- 確定: 4997件 (Win 1333 / Loss 1084 / Flat 2580) / skip 7518件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BREV/USDT:USDT `LIMIT_FIB1272` TP_HIT account +0.69% 残高後 $431.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-18T01:31:09.523325+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=64530.5
- Funnel: target 1073 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BREV/USDT:USDT | +31.67% | $9,631,884.61 |
| ICNT/USDT:USDT | +17.93% | $1,179,612.81 |
| MUU/USDT:USDT | +14.76% | $36,338,123.76 |
| SNXX/USDT:USDT | +14.27% | $47,425,281.23 |
| MMT/USDT:USDT | +13.72% | $2,073,872.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CSOPSKHYNIX2L/USDT:USDT | below_1h_threshold | +2.61% | +2.98% |
| MURATASTOCK/USDT:USDT | below_1h_threshold | +2.12% | +2.48% |
| ARIA/USDT:USDT | below_1h_threshold | +1.84% | +2.21% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.80% | +2.16% |
| NVDL/USDT:USDT | below_1h_threshold | +1.66% | +2.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
