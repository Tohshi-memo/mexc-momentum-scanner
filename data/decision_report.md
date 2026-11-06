# Decision Report

- generated_at: 2026-11-06T03:16:25.617132+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18227**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18227, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.65% | **-0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.63% | **+0.57%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.37% | **+0.26%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.33% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.64% | **+0.79%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.90% | **+0.32%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.26% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 263件 (TP 96 / SL 159 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,492.09** / 初期 $100.00 (+1392.09%)
- 確定: 7030件 (Win 2022 / Loss 2245 / Flat 2763) / skip 7758件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,492.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$375.26** / 初期 $100.00 (+275.26%)
- 確定: 4611件 (Win 1235 / Loss 1030 / Flat 2346) / skip 7027件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLANKER/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $375.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6389件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000103 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T03:16:11.137546+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=76088.0
- Funnel: target 1084 → liquid 186 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +67.85% | $7,671,837.36 |
| CYBER/USDT:USDT | +41.52% | $2,069,390.82 |
| IRENSTOCK/USDT:USDT | +17.45% | $3,121,845.42 |
| BLESS/USDT:USDT | +14.10% | $5,400,721.63 |
| ETHFI/USDT:USDT | +9.90% | $5,762,620.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +4.40% | +4.50% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +3.12% | +3.22% |
| SOXL/USDT:USDT | below_1h_threshold | +2.75% | +2.85% |
| MUU/USDT:USDT | below_1h_threshold | +2.48% | +2.57% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.05% | +2.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
